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

# Modules Eficas
from monPlusieursIntoPanel import MonPlusieursIntoPanel
from monPlusieursIntoPanel import DPlusInto
from qtCommun              import QTPanel
from politiquesValidation  import PolitiquePlusieurs

class MonPlusieursASSDPanel(MonPlusieursIntoPanel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonPlusieursASSDPanel"
        QTPanel.__init__(self,node,parent)
        DPlusInto.__init__(self,parent,fl)

        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        self.InitValeursCourantes()
        self.DisplayListBoxCourantes()
        self.DisplayListBoxPossibles()

        self.politique=PolitiquePlusieurs(node,parent)
        self.connecterSignaux()

  def DisplayListBoxPossibles(self):
        listeNomsSD = self.node.item.get_sd_avant_du_bon_type()
        self.listBoxVal.clear()
        for aSD in listeNomsSD:
            self.listBoxVal.addItem( aSD)
        if len(listeNomsSD) == 1 :
            self.listBoxVal.setCurrentRow(1)

  def DisplayListBoxCourantes(self):
        self.LBValeurs.clear()
        for aSD in self.listNomsValeurs :
            self.LBValeurs.addItem( aSD)

  def InitValeursCourantes(self):
        self.listNomsValeurs=[]
        for i in self.listeValeursCourantes :
              self.listNomsValeurs.append(i.get_name())

  def BOkPourListePressed(self):
        if self.listeValeursCourantes == [] :
	   self.editor.affiche_infos("Pas de Validation d un groupe vide")
           return
        self.node.item.set_valeur(self.listeValeursCourantes)
	self.editor.affiche_infos("Valeur Acceptée")
	pass

  def BSupPressed(self):
        QTPanel.BSupPressed(self)

  def Sup1Valeur(self):
        indexCourant=self.LBValeurs.currentRow()
        if indexCourant < 0 : return
        if self.LBValeurs.isItemSelected(self.LBValeurs.item(indexCourant))== 0 : return
        if self.LBValeurs.item(indexCourant).text()==QString("") : return
        self.LBValeurs.takeItem(indexCourant)
     
        listeVal=[]
        i=0
        for valeur in self.listeValeursCourantes :
                if i != indexCourant : listeVal.append(valeur)
                i = i+1
        self.listeValeursCourantes=listeVal
        self.InitValeursCourantes()
        self.DisplayListBoxCourantes()
        self.DisplayListBoxPossibles()
          
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
            valeurSD,validite=self.node.item.eval_valeur(valeur)
            if validite : listeVal.append(valeur)
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
           self.InitValeursCourantes()
           self.DisplayListBoxCourantes()
           self.DisplayListBoxPossibles()


