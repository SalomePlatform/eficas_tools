# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
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

from feuille               import Feuille
from desWidgetRadioButton  import Ui_WidgetRadioButton 
from politiquesValidation  import PolitiqueUnique
from qtSaisie              import SaisieValeur


class MonWidgetRadioButtonCommun (Feuille):
  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        self.setMaxI()
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.politique=PolitiqueUnique(self.node,self.editor)
        self.dict_bouton={}
        self.determineChoix()
        self.setValeursApresBouton()
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.maCommande.listeAffichageWidget.append(self.radioButton_1)


  def setValeursApresBouton(self):
      if self.objSimp.get_valeur()==None : return
      valeur=self.objSimp.get_valeur()
      if not(type(valeur) in types.StringTypes) : valeur=str(valeur)
      try :
        self.dict_bouton[valeur].setChecked(True)
      except :
        pass

  def determineChoix(self):
      self.horizontalLayout.setAlignment(Qt.AlignLeft)
      i=1
      j=len(self.monSimpDef.into)
      if j > self.maxI : 
         print "poumbadaboum"
         return
      while i < j+1 :
         nomBouton="radioButton_"+str(i)
         bouton=getattr(self,nomBouton)
         valeur=self.monSimpDef.into[i-1]
         if not(type(valeur) in types.StringTypes) : valeur=str(valeur)
         bouton.setText(valeur)
         self.dict_bouton[valeur]=bouton
         self.connect(bouton,SIGNAL("clicked()"),self.boutonclic)
         bouton.keyPressEvent=self.keyPressEvent
         setattr(self,nomBouton,bouton)
         i=i+1
      while i < self.maxI +1 :
         nomBouton="radioButton_"+str(i)
         bouton=getattr(self,nomBouton)
         bouton.close()
         i=i+1

  def boutonclic(self):
      for valeur in self.dict_bouton.keys():
          if self.dict_bouton[valeur].isChecked():
             print "dans boutonclic is checked", valeur, type(valeur)
             SaisieValeur.LEValeurPressed(self,valeur)
      self.parentQt.reaffiche()


  def keyPressEvent(self, event):
    if event.key() == Qt.Key_Right : self.selectSuivant(); return
    if event.key() == Qt.Key_Left  : self.selectPrecedent(); return
    QWidget.keyPressEvent(self,event)

  def selectSuivant(self):
      aLeFocus=self.focusWidget()
      nom=aLeFocus.objectName()[12:]
      i=nom.toInt()[0]+1
      if i ==  len(self.monSimpDef.into) +1 : i=1
      nomBouton="radioButton_"+str(i)
      courant=getattr(self,nomBouton)
      courant.setFocus(True)

  def selectPrecedent(self):
      aLeFocus=self.focusWidget()
      nom=aLeFocus.objectName()[12:]
      i=nom.toInt()[0]-1
      print i
      if i == 0 : i= len(self.monSimpDef.into)  
      print i
      print "_______"
      nomBouton="radioButton_"+str(i)
      courant=getattr(self,nomBouton)
      courant.setFocus(True)


class MonWidgetRadioButton (Ui_WidgetRadioButton,MonWidgetRadioButtonCommun):
  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        MonWidgetRadioButtonCommun.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        
  def setMaxI(self):
        self.maxI=3
