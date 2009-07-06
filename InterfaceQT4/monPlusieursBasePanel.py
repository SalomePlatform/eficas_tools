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
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from desPlusieursBase import Ui_DPlusBase
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiquePlusieurs

class DPlusBase (Ui_DPlusBase,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       if hasattr(parent,"leLayout"):
          parent.leLayout.removeWidget(parent.leLayout.widgetActive)
          parent.leLayout.widgetActive.close()
          parent.leLayout.addWidget(self)
          parent.leLayout.widgetActive=self
       else:
          parent.partieDroite=QWidget()
          parent.leLayout=QGridLayout(parent.partieDroite)
          parent.leLayout.addWidget(self)
          parent.addWidget(parent.partieDroite)
          parent.leLayout.widgetActive=self
       self.setupUi(self)
       icon = QIcon(self.RepIcon+"arrow_left.png")
       self.BAjout1Val.setIcon(icon)
       icon2 = QIcon(self.RepIcon+"arrow_right.png")
       self.BSup1Val.setIcon(icon2)
       icon3 = QIcon(self.RepIcon+"image240.png")
       self.BSalome.setIcon(icon3)

# Import des panels

class MonPlusieursBasePanel(DPlusBase,QTPanel,SaisieValeur):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonPlusieursBasePanel"
        QTPanel.__init__(self,node,parent)
        DPlusBase.__init__(self,parent,fl)
        self.politique=PolitiquePlusieurs(node,parent)
        self.BuildLBValeurs()
        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        self.InitCommentaire()
        self.detruitBouton()
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPourListePressed)
        self.connect(self.bParam,SIGNAL("clicked()"),self.BParametresPressed)
        self.connect(self.bImport,SIGNAL("clicked()"),self.BImportPressed)
        self.connect(self.BAjout1Val,SIGNAL("clicked()"),self.Ajout1Valeur)
        self.connect(self.BSup1Val,SIGNAL("clicked()"),self.Sup1Valeur)
        self.connect(self.LEValeur,SIGNAL("returnPressed()"),self.LEValeurPressed)
        self.connect(self.BSalome,SIGNAL("clicked()"),self.BSalomePressed)

  def detruitBouton(self):
        mc = self.node.item.get_definition()
        type = mc.type[0]
        if not(('grma' in repr(type)) or ('grno' in repr(type))) or not(self.editor.salome) :
           self.BSalome.close()
           self.BView2D.close()


  def BuildLBValeurs(self):
       # redefinit en raison de l heritage par monFonctionPanel
        SaisieValeur.BuildLBValeurs(self)

  def BOkPourListePressed(self):
        self.editor.init_modif()
        if self.listeValeursCourantes == [] :
           self.editor.affiche_infos("Aucune Valeur")
           return
        self.node.item.set_valeur(self.listeValeursCourantes)
	self.editor.affiche_infos("Valeur Acceptée")


  def BParametresPressed(self):
        QTPanel.BParametresPressed(self)

  def LEValeurPressed(self):
        self.Ajout1Valeur()

  def Sup1Valeur(self):
        index=self.LBValeurs.currentRow()
        if index < 0 : return
        if self.LBValeurs.isItemSelected(self.LBValeurs.item(index)) == 0 : return
        self.LEValeur.setText(self.LBValeurs.item(index).text())
        self.LBValeurs.takeItem(index)
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

        indexCourant=self.LBValeurs.currentRow()
        if ( (self.LBValeurs.isItemSelected(self.LBValeurs.item(indexCourant )) == 0) 
           and (indexCourant > 0 )):
           index=0
        else :
           index=self.LBValeurs.currentRow() + 1

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
               self.LBValeurs.insertItem(index,QString(str(valeur)))
               item=self.LBValeurs.item(index)
               item.setSelected(1)
               self.LBValeurs.setCurrentItem(item)
               index=index+1
           self.listeValeursCourantes=l1+listeRetour+l3
	   self.editor.affiche_infos("Valeurs Ajoutées")

  def AjoutNValeur(self,liste) :
      for val in liste :
        print val
	self.Ajout1Valeur(val)

  def BImportPressed(self):
        init=QString( self.editor.CONFIGURATION.savedir)
        fn = QFileDialog.getOpenFileName(self.node.appliEficas, 
                                         self.node.appliEficas.trUtf8('Fichier de données'), 
                                         init,
                                         self.trUtf8('All Files (*)',))
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
        print "editor", self.editor
        print "appliEficas", self.editor.appliEficas
        selection, commentaire = self.editor.appliEficas.selectGroupFromSalome(kwType,editor=self.editor)
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

