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

from desPlusieursInto import Ui_DPlusInto
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiquePlusieurs

class DPlusInto(Ui_DPlusInto,QDialog):
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

class MonPlusieursIntoPanel(DPlusInto,QTPanel,SaisieValeur):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonPlusieursIntoPanel"
        QTPanel.__init__(self,node,parent)
        DPlusInto.__init__(self,parent,fl)
        self.politique=PolitiquePlusieurs(node,parent)
        SaisieValeur.BuildLBValeurs(self)
        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        SaisieValeur.RemplitPanel(self,self.listeValeursCourantes)
        self.InitCommentaire()
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.listBoxVal, SIGNAL("itemDoubleClicked(QListWidgetItem*)" ), self.Ajout1Valeur )
        self.connect(self.LBValeurs,SIGNAL("itemDoubleClicked(QListWidgetItem*)"),self.Sup1Valeur)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPourListePressed)
        self.connect(self.BAjout1Val,SIGNAL("clicked()"),self.Ajout1Valeur)
        self.connect(self.BSup1Val,SIGNAL("clicked()"),self.Sup1Valeur)


  def BOkPourListePressed(self):
        if self.listeValeursCourantes == [] :
           self.editor.affiche_infos("Pas de validation d un groupe vide")
           return
        self.node.item.set_valeur(self.listeValeursCourantes)
	self.editor.affiche_infos("Valeur Acceptée")


  def Sup1Valeur(self):
        indexCourant=self.LBValeurs.currentRow()
        if indexCourant == None : return
        if self.LBValeurs.isItemSelected(self.LBValeurs.item(indexCourant))== 0 : return
        if self.LBValeurs.item(indexCourant).text()==QString("") : return 
        self.LBValeurs.takeItem(indexCourant)
        listeVal=[]
        i=0
        for valeur in self.listeValeursCourantes :
                if i != indexCourant : listeVal.append(valeur)
                i = i+1
        self.listeValeursCourantes=listeVal
        SaisieValeur.RemplitPanel(self,self.listeValeursCourantes)
          
  def Ajout1Valeur(self):
        liste=[]

        indexCourant=self.listBoxVal.currentRow()
        if indexCourant == None : return
        if self.listBoxVal.isItemSelected(self.listBoxVal.item(indexCourant))== 0 : return
        if self.listBoxVal.item(indexCourant).text()==QString("") : return 
        liste.append(str(self.listBoxVal.item(indexCourant).text()))
        if self.LBValeurs.currentItem() != None :
           index= self.LBValeurs.currentRow()+ 1
        else :
           index = 0
        listeVal=[]
        for valeur in self.listeValeursCourantes :
                listeVal.append(valeur)
        validite,comm,comm2,listeRetour=self.politique.AjoutValeurs(liste,index,listeVal) 
	self.Commentaire.setText(comm2)
        if not validite :
		self.editor.affiche_infos(comm)
        else:
           l1=self.listeValeursCourantes[:index]
           l3=self.listeValeursCourantes[index:]
           for valeur in listeRetour:
               self.LBValeurs.insertItem(index,QString(str(valeur)))
               item=self.LBValeurs.item(index)
               item.setSelected(1)
	       self.LBValeurs.setCurrentItem(item)
               index=index+1
           self.listeValeursCourantes=l1+listeRetour+l3
        SaisieValeur.RemplitPanel(self,self.listeValeursCourantes)

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
               commentaire="Entrez entre "+str(mc.min)+" et "+str(mc.max)+" "+d_aides[type]
        aideval=self.node.item.aide()
        commentaire=commentaire + "\n" + aideval
        self.Commentaire.setText(QString(commentaire))

