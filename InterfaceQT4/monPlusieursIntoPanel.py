# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
# Modules Python
import string,types,os

# Modules Eficas
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Extensions.i18n import tr
from desPlusieursInto import Ui_DPlusInto
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiquePlusieurs

class DPlusInto(Ui_DPlusInto,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.RepIcon=parent.appliEficas.RepIcon
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
       icon = QIcon(self.RepIcon+"/arrow_left.png")
       self.BAjout1Val.setIcon(icon)
       icon2 = QIcon(self.RepIcon+"/arrow_right.png")
       self.BSup1Val.setIcon(icon2)


class MonPlusieursIntoPanel(DPlusInto,QTPanel,SaisieValeur):
  """
  Classe definissant le panel associe aux mots-cles qui demandent
  a l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrÃ¨tes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonPlusieursIntoPanel"
        self.alpha=0
        QTPanel.__init__(self,node,parent)
        DPlusInto.__init__(self,parent,fl)
        self.politique=PolitiquePlusieurs(node,parent)
        self.InitCommentaire()
        SaisieValeur.BuildLBValeurs(self)
        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        SaisieValeur.RemplitPanel(self,self.listeValeursCourantes,self.alpha)
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.listBoxVal, SIGNAL("itemDoubleClicked(QListWidgetItem*)" ), self.Ajout1Valeur )
        self.connect(self.LBValeurs,SIGNAL("itemDoubleClicked(QListWidgetItem*)"),self.Sup1Valeur)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPourListePressed)
        self.connect(self.BAjout1Val,SIGNAL("clicked()"),self.Ajout1Valeur)
        self.connect(self.BSup1Val,SIGNAL("clicked()"),self.Sup1Valeur)
        self.connect(self.BAlpha,SIGNAL("clicked()"),self.BAlphaPressed)

  def BAlphaPressed(self):
      if self.alpha==1 :
         self.alpha=0
         self.BAlpha.setText(tr("Tri Alpha"))
      else :
         self.alpha=1
         self.BAlpha.setText(tr("Tri Cata"))
      SaisieValeur.RemplitPanel(self,self.listeValeursCourantes, self.alpha)

  def BOkPourListePressed(self):
        if self.listeValeursCourantes == [] and self.node.item.GetMinMax()[0] !=0 :
           self.editor.affiche_infos("Pas de validation d un groupe vide",Qt.red)
           return
        if hasattr(self.node.item.definition.validators,'verifie_liste'):
            if self.node.item.definition.validators.verifie_liste(self.listeValeursCourantes) == 0 :
               self.editor.affiche_infos("les valeurs ne sont pas correctes",Qt.red)
               return
        self.node.item.set_valeur(self.listeValeursCourantes)
	self.editor.affiche_infos("Valeur Acceptee")


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
        self.LBValeurs.setCurrentItem(self.LBValeurs.item(indexCourant -1))
        self.listeValeursCourantes=listeVal
        SaisieValeur.RemplitPanel(self,self.listeValeursCourantes,self.alpha)
          
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
		self.editor.affiche_infos(comm,Qt.red)
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
        SaisieValeur.RemplitPanel(self,self.listeValeursCourantes,self.alpha)

  def InitCommentaire(self):
        commentaire=""
        mc = self.node.item.get_definition()
        d_aides = { 'TXM' : 'chaînes de caractéres',
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
        commentaire=commentaire + "   " + QString.toUtf8(QString(aideval))
        self.Commentaire.setText(tr(commentaire))

