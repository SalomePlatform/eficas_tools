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
from qt import *

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
            self.listBoxASSD.insertItem( aSD)
            QObject.connect(self.listBoxASSD, SIGNAL("doubleClicked(QListBoxItem*)" ), self.ClicASSD )
       min,max =  self.node.item.GetMinMax()
       l= self.node.item.GetListeValeurs()
       
       if (min == 1 and min == max and len(listeNomsSD)==1 and (l==[] or l==None)):
            if ('R' not in self.node.item.get_type()) :
               self.listBoxASSD.setCurrentItem(0)


  def BuildLBValeurs(self,politique=None):
        self.LBValeurs.clear()
        listeValeurs=self.node.item.GetListeValeurs()
        for valeur in listeValeurs:
            if politique :
              self.LBValeurs.insertItem(str(self.politique.GetValeurTexte(valeur)))
            else :
              self.LBValeurs.insertItem(str(valeur))
        if listeValeurs != None and listeValeurs != [] :
            self.LBValeurs.setCurrentItem(len(listeValeurs) - 1)
       

  def RemplitPanel(self,listeDejaLa=[]):
        self.listBoxVal.clear()
        lChoix=self.node.item.get_liste_possible(listeDejaLa)
        for valeur in lChoix :
            self.listBoxVal.insertItem( str(valeur) ) 
        if len(lChoix) == 1 :
            self.listBoxVal.setSelected(0,1)

  def ClicASSD(self):
         if self.listBoxASSD.selectedItem()== None : return
         valeurQstring=self.listBoxASSD.selectedItem().text()
         commentaire = QString("Valeur selectionnée : ") 
         commentaire.append(valeurQstring)
         self.Commentaire.setText(commentaire)
         valeur=valeurQstring.latin1()
         validite,commentaire=self.politique.RecordValeur(valeur)
         self.Commentaire.setText(QString(commentaire))
         self.editor.affiche_infos(commentaire)

  def ClicValeur(self):
         if self.listBoxVal.selectedItem()== None : return
         valeurQstring=self.listBoxVal.selectedItem().text()
         valeur=valeurQstring.latin1()
         validite,commentaire=self.politique.RecordValeur(valeur)
         #self.Commentaire.setText(QString(commentaire))
         self.editor.affiche_infos(commentaire)

  def BOkPressed(self):
         if self.listBoxVal.selectedItem()==None :
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


  def TraiteLEValeur(self,valeurTraitee=None) :
        # lit la chaine entree dans le line edit
        # et la tranforme en chaine de valeurs
        # a traiter. renvoie eventuellement des complexes
        listeValeurs=[]
        if valeurTraitee == None :
           valeurBrute=str(self.LEValeur.text())
        else :
           valeurBrute=valeurTraitee
        if valeurBrute == str("") : return  listeValeurs,1,valeurBrute
        try :
           valeur=eval(valeurBrute,{})        
        except :
           valeur=valeurBrute
        if type(valeur)  in (types.ListType,types.TupleType) :
           indice = 0
           while (indice < len(valeur)):
              v=valeur[indice]
              if self.node.item.wait_complex() :
                 if (v== 'RI' or v == 'MP'):
                    try :
                       t=tuple([v,valeur[indice+1],valeur[indice+2]])
                       listeValeurs.append(t)
                       indice=indice+3
                    except :
                       commentaire = "Veuillez entrer le complexe sous forme aster ou sous forme python"
                       self.editor.affiche_infos(commentaire)
                       return listeValeurs,0,valeurBrute
                       

                 else :     # ce n'est pas un tuple à la mode aster
                    
                    listeValeurs.append(v)
                    indice = indice + 1

              else:  # on n'attend pas un complexe
                 listeValeurs.append(v)
                 indice=indice+1
        elif type(valeur) == types.StringType:
             listeValeurs=valeur.split(',')
        else:
          listeValeurs.append(valeur)

        return listeValeurs,1,valeurBrute


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
        self.Commentaire.setText(QString(commentaire))
