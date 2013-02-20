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

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr


# Modules Eficas
from monPlusieursIntoPanel import MonPlusieursIntoPanel
from monPlusieursIntoPanel import DPlusInto
from qtCommun              import QTPanel
from politiquesValidation  import PolitiquePlusieurs

class MonPlusieursASSDPanel(MonPlusieursIntoPanel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  a l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonPlusieursASSDPanel"
        self.alpha=0
        QTPanel.__init__(self,node,parent)
        DPlusInto.__init__(self,parent,fl)

        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        self.InitValeursCourantes()
        self.DisplayListBoxCourantes()
        self.DisplayListBoxPossibles()

        self.politique=PolitiquePlusieurs(node,parent)
        self.connecterSignaux()
        self.BAlpha.close()

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
           #pour resoudre le typ= not_checked
           try :
              self.listNomsValeurs.append(i.get_name())
           except :
              self.listNomsValeurs.append(i)

  def BOkPourListePressed(self):
        if self.listeValeursCourantes == [] :
	   self.editor.affiche_infos("Pas de Validation d un groupe vide",Qt.red)
           return
        try :
          if  len(self.listeValeursCourantes) == 1 : self.listeValeursCourantes=self.listeValeursCourantes[0]
        except :
          pass
        self.node.item.set_valeur(self.listeValeursCourantes)
	self.editor.affiche_infos("Valeur Acceptée")
	pass


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
           self.InitValeursCourantes()
           self.DisplayListBoxCourantes()
           self.DisplayListBoxPossibles()


  def BAlphaPressed(self):
      if self.alpha==1 :
         self.alpha=0
         self.BAlpha.setText(tr( "Tri Alpha"))
      else :
         self.alpha=1
         self.BAlpha.setText(tr( "Tri Cata"))
      self.DisplayListBoxPossibles()

