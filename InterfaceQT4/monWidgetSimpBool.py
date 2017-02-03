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
from determine import monEnvQT5
if monEnvQT5 :
   from PyQt5.QtWidgets import QRadioButton
else :
   from PyQt4.QtGui import *
   from PyQt4.QtCore import *
from Extensions.i18n import tr

from feuille               import Feuille
from desWidgetSimpBool     import Ui_WidgetSimpBool 
from politiquesValidation  import PolitiqueUnique
from qtSaisie              import SaisieValeur


class MonWidgetSimpBool (Ui_WidgetSimpBool,Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.politique=PolitiqueUnique(self.node,self.editor)
        if monEnvQT5 :
           self.RBTrue.clicked.connect(self.boutonTrueClic)
           self.RBFalse.clicked.connect(self.boutonFalseClic)
        else :
           self.connect(self.RBTrue,SIGNAL("clicked()"),self.boutonTrueClic)
           self.connect(self.RBFalse,SIGNAL("clicked()"),self.boutonFalseClic)
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.maCommande.listeAffichageWidget.append(self.RBTrue)

  def setValeurs(self):
       valeur=self.node.item.get_valeur()
       if valeur == None  : return
       if valeur == True  : self.RBTrue.setChecked(True)
       if valeur == False : self.RBFalse.setChecked(True)


  def boutonTrueClic(self):
      SaisieValeur.LEValeurPressed(self,True)
      self.reaffiche()

  def boutonFalseClic(self):
      SaisieValeur.LEValeurPressed(self,False)
      self.reaffiche()
