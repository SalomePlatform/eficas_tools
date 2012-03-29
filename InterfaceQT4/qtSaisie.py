# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
# Modules Python
import string,types,os
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# Import des panels

class SaisieValeur:
  """
  Classe contenant les méthodes communes aux  panels
  permettant de choisir des valeurs 
  """
  def __init__(self):
       pass

  def InitListBoxASSD(self):
       listeNomsSD = self.node.item.get_sd_avant_du_bon_type()
       for aSD in listeNomsSD:
            self.listBoxASSD.addItem( aSD)
            QObject.connect(self.listBoxASSD, SIGNAL("doubleClicked(QListWidgetItem*)" ), self.ClicASSD )
       min,max =  self.node.item.GetMinMax()
       l= self.node.item.GetListeValeurs()
       
       if (min == 1 and min == max and len(listeNomsSD)==1 and (l==[] or l==None)):
            if ('R' not in self.node.item.get_type()) :
               self.listBoxASSD.setCurrentRow(0)


  def BuildLBValeurs(self):
        self.LBValeurs.clear()
        listeValeurs=self.node.item.GetListeValeurs()
        #print self.node.item.definition.validators
        for valeur in listeValeurs:
            try :
               val=self.politique.GetValeurTexte(valeur)
            except :
               val=valeur
            self.LBValeurs.addItem(str(val))
        if listeValeurs != None and listeValeurs != [] :
            self.LBValeurs.setCurrentRow(len(listeValeurs) - 1)
       

  def RemplitPanel(self,listeDejaLa=[],alpha=0):
        self.listBoxVal.clear()
        # Traitement particulier pour le validator VerifExistence
        # dont les valeurs possibles peuvent changer : into variable
        if hasattr(self.node.item.definition.validators,'set_MCSimp'):
            obj=self.node.item.getObject()
            self.node.item.definition.validators.set_MCSimp(obj)
            if self.node.item.isvalid() == 0 : 
               liste=[]
               for item in listeDejaLa:
                   if self.node.item.definition.validators.verif_item(item)==1:
                      liste.append(item)
                   self.node.item.set_valeur(liste)
                   self.BuildLBValeurs()
                   self.listeValeursCourantes=liste
                   self.editor.affiche_infos("Attention, valeurs modifiees", Qt.red)
               listeDejaLa=liste
        lChoix=self.node.item.get_liste_possible(listeDejaLa)
        if ((len(lChoix) < 10 ) and (hasattr (self,'BAlpha'))) : self.BAlpha.close()
        if alpha==1 : lChoix.sort()
        for valeur in lChoix :
            self.listBoxVal.addItem( str(valeur) ) 
        if len(lChoix) == 1 :
            self.listBoxVal.setCurrentRow(0)
            self.listBoxVal.item(0).setSelected(1)
            self.bOk.setFocus()
            

  def ClicASSD(self):
         if self.listBoxASSD.currentItem()== None : return
         valeurQstring=self.listBoxASSD.currentItem().text()
         commentaire = QString("Valeur selectionnée : ") 
         commentaire.append(valeurQstring)
         self.Commentaire.setText(commentaire)
         valeur=str(valeurQstring)
         validite,commentaire=self.politique.RecordValeur(valeur)
         self.Commentaire.setText(QString(commentaire))
         self.editor.affiche_infos(commentaire)

  def ClicValeur(self):
         if self.listBoxVal.currentItem()== None : return
         valeurQstring=self.listBoxVal.currentItem().text()
         valeur=str(valeurQstring)
         validite,commentaire=self.politique.RecordValeur(valeur)
         #self.Commentaire.setText(QString(commentaire))
         self.editor.affiche_infos(commentaire)

  def BOkPressed(self):
         if self.listBoxVal.currentItem()==None :
            commentaire = "Pas de valeur selectionnée" 
            self.Commentaire.setText(QString(commentaire))
         else :
            self.ClicValeur()       

  def BOk2Pressed(self):
         if str(self.lineEditVal.text())== "" :
            commentaire = "Pas de valeur entrée " 
            self.Commentaire.setText(QString(commentaire))
         else :
            self.LEValeurPressed()       

  def LEValeurPressed(self,valeur=None):
         if valeur == None :
            nouvelleValeur=str(self.lineEditVal.text())
         else :
            self.lineEditVal.setText(QString(valeur.nom))
            nouvelleValeur=valeur
         validite,commentaire=self.politique.RecordValeur(nouvelleValeur)
         if commentaire != "" :
            #self.Commentaire.setText(QString(commentaire))
            self.editor.affiche_infos(commentaire)


  def TraiteLEValeurTuple(self) :
        listeValeurs=[]
        valeurBrute=str(self.LEValeur.text())
        listeValeursSplit=valeurBrute.split(',')
        for val in listeValeursSplit :
            try :
               valeur=eval(val,{})        
            except :
               valeur=val
            listeValeurs.append(valeur)
        return listeValeurs

  def TraiteLEValeur(self,valeurTraitee=None) :
        # lit la chaine entree dans le line edit
        # et la tranforme en chaine de valeurs
        # a traiter. renvoie eventuellement des complexes
        listeValeurs=[]
        if valeurTraitee == None :
           valeurBrute=str(self.LEValeur.text())
        else :
           valeurBrute=valeurTraitee
        if valeurBrute == str("") : return listeValeurs,1

        try :
            valeur=eval(valeurBrute,{})        
        except :
            valeur=valeurBrute

        if type(valeur)  in (types.ListType,types.TupleType) :
           if self.node.item.wait_complex() :
              indice = 0
              while (indice < len(valeur)):
                 v=valeur[indice]

                 if (v== 'RI' or v == 'MP'):
                    try :
                       t=tuple([v,valeur[indice+1],valeur[indice+2]])
                       listeValeurs.append(t)
                       indice=indice+3
                    except :
                       commentaire = "Veuillez entrer le complexe sous forme aster ou sous forme python"
                       self.editor.affiche_infos(commentaire)
                       return listeValeurs,0
                       

                 else :     # ce n'est pas un tuple à la mode aster
                    listeValeurs.append(v)
                    indice = indice + 1

           else:  # on n'attend pas un complexe
             listeValeurs=valeurBrute.split(',')

        elif type(valeur) == types.StringType:
             listeValeurs=valeur.split(',')
        else:
          listeValeurs.append(valeurBrute)

        return listeValeurs,1


class SaisieSDCO :
  def __init__(self):
        pass

  def LESDCOReturnPressed(self):
        """
           Lit le nom donné par l'utilisateur au concept de type CO qui doit être
           la valeur du MCS courant et stocke cette valeur
        """
        self.editor.init_modif()
        anc_val = self.node.item.get_valeur()
        if anc_val != None:
          # il faut egalement propager la destruction de l'ancien concept
          self.node.item.delete_valeur_co(valeur=anc_val)
          # et on force le recalcul des concepts de sortie de l'etape
          self.node.item.object.etape.get_type_produit(force=1)
          # et le recalcul du contexte
          self.node.item.object.etape.parent.reset_context()
        nomConcept = str(self.LESDCO.text())
        if nomConcept == "" : return

        test,commentaire=self.node.item.set_valeur_co(nomConcept)
        if test:
           commentaire="Valeur du mot-clé enregistree"
           self.node.update_node_valid()
        else :
           cr = self.node.item.get_cr()
           commentaire = "Valeur du mot-clé non autorisée :"+cr.get_mess_fatal()
           self.node.item.set_valeur_co(anc_val)
        self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))
