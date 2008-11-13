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

# Modules Eficas
import prefs

from qt import *

from desPlusieursBase import DPlusBase
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiquePlusieurs

# Import des panels

class MonPlusieursBasePanel(DPlusBase,QTPanel,SaisieValeur):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        QTPanel.__init__(self,node,parent)
        DPlusBase.__init__(self,parent,name,fl)
        self.politique=PolitiquePlusieurs(node,parent)
        self.BuildLBValeurs()
        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        self.InitCommentaire()
        self.detruitBouton()

  def detruitBouton(self):
        mc = self.node.item.get_definition()
        type = mc.type[0]
        print self.editor.salome
        if not(('grma' in repr(type)) or ('grno' in repr(type))) or not(self.editor.salome) :
           self.BSalome.close()
           self.BView2D.close()

  def ViewDoc(self):
        QTPanel.ViewDoc(self)

  def BuildLBValeurs(self):
       # redefinit en raison de l heritage par monFonctionPanel
        SaisieValeur.BuildLBValeurs(self)

  def BOkPourListePressed(self):
        if self.listeValeursCourantes == [] :
           self.editor.affiche_infos("Pas de validation d un groupe vide")
           return
        self.node.item.set_valeur(self.listeValeursCourantes)
	self.editor.affiche_infos("Valeur Acceptée")

  def BSupPressed(self):
        QTPanel.BSupPressed(self)

  def BParametresPressed(self):
        QTPanel.BParametresPressed(self)

  def LEValeurPressed(self):
        self.Ajout1Valeur()

  def Sup1Valeur(self):
        index=self.LBValeurs.currentItem()
        self.LEValeur.setText(self.LBValeurs.currentText())
        self.LBValeurs.removeItem(self.LBValeurs.currentItem())
        listeVal=[]
        i=0
        for valeur in self.listeValeursCourantes :
                if i != index : listeVal.append(valeur)
                i = i+1
        self.listeValeursCourantes=listeVal
          

  def Ajout1Valeur(self,valeur=None):
        liste,validite=SaisieValeur.TraiteLEValeur(self,valeur)
        if validite == 0 : return
        if liste ==[]    : return

        index=self.LBValeurs.currentItem() + 1
        listeVal=[]
        for valeur in self.listeValeursCourantes :
                listeVal.append(valeur)
        validite,comm,comm2,listeRetour=self.politique.AjoutValeurs(liste,index,listeVal) 
	self.Commentaire.setText(comm2)
        if not validite :
		self.editor.affiche_infos(comm)
        else:
           self.LEValeur.setText(QString(""))
           l1=self.listeValeursCourantes[:index]
           l3=self.listeValeursCourantes[index:]
           for valeur in listeRetour:
               self.LBValeurs.insertItem(QString(str(valeur)),index)
               index=index+1
           self.listeValeursCourantes=l1+listeRetour+l3

  def BImportPressed(self):
        init=QString( self.editor.CONFIGURATION.rep_user)
        fn = QFileDialog.getOpenFileName(init, self.trUtf8('All Files (*)',))
        if fn == None : return
        if fn == "" : return
        from monSelectVal import MonSelectVal
        MonSelectVal(file=fn,parent=self).show()

  def InitCommentaire(self):
        commentaire=""
        mc = self.node.item.get_definition()
        d_aides = { 'TXM' : 'chaînes de caractères',
                  'R'   : 'réels',
                  'I'   : 'entiers',
                  'C'   : 'complexes'}
        type = mc.type[0]
        if not d_aides.has_key(type) :
           if mc.min == mc.max:
               commentaire="Entrez "+str(mc.min)+" valeurs "
           else :
               commentaire="Entrez entre "+str(mc.min)+" et "+str(mc.max)+" valeurs "
        else :
           if mc.min == mc.max:
               commentaire="Entrez "+str(mc.min)+" "+d_aides[type]
           else :
               commentaire="Entrez entre "+str(mc.min)+" et  "+str(mc.max) +" " + d_aides[type]
        aideval=self.node.item.aide()
        commentaire=commentaire + "\n" + aideval
        self.Commentaire.setText(QString(commentaire))

  def BSalomePressed(self):

        genea=self.node.item.get_genealogie()
        kwType = None
        for e in genea:
            if "GROUP_NO" in e: kwType = "GROUP_NO"
            if "GROUP_MA" in e: kwType = "GROUP_MA"

        #print "BkwType",kwType
        #print "editor", self.editor
        selection, commentaire = self.editor.parent.appliEficas.selectGroupFromSalome(kwType,editor=self.editor)
        if commentaire !="" :
            self.Commentaire.setText(QString(commentaire))
        monTexte=""
        if selection == [] : return
        for geomElt in selection: 
            monTexte=geomElt+","
        monTexte= monTexte[0:-1]
        self.LEValeur.setText(QString(monTexte))

  def BView2DPressed(self):
        valeur=self.LEValeur.text()
        if valeur == QString("") :
           valeur=self.LBValeurs.currentText()
        if valeur == QString("") : return
        valeur = str(valeur)
        if valeur :
           ok, msgError = self.editor.parent.appliEficas.displayShape(valeur)
           if not ok:
              self.editor.parent.appli.affiche_infos(msgError)

