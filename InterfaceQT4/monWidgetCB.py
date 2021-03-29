# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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
from __future__ import absolute_import
try :
   from builtins import str
except : pass

import types,os

# Modules Eficas
from Extensions.i18n import tr

from InterfaceQT4.feuille               import Feuille
from desWidgetCB                        import Ui_WidgetCB 
from InterfaceQT4.politiquesValidation  import PolitiqueUnique
from InterfaceQT4.qtSaisie              import SaisieValeur

from PyQt5.QtWidgets import QComboBox, QCompleter
from PyQt5.QtCore import Qt


class MonWidgetCBCommun (Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.politique=PolitiqueUnique(self.node,self.editor)
        self.determineChoix()
        self.setValeursApresBouton()
        self.CBChoix.currentIndexChanged.connect(self.choixSaisi)
        #self.CBChoix.lineEdit().setText(tr("Select"))
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.maCommande.listeAffichageWidget.append(self.CBChoix)
        self.AAfficher=self.CBChoix


  def setValeursApresBouton(self):
      if self.objSimp.getValeur()==None : 
         self.CBChoix.setCurrentIndex(-1)
         #self.CBChoix.lineEdit().setStyleSheet(("QLineEdit {" " background:yellow;\n" "font: italic ;\n" " }\n" " "))
         self.CBChoix.lineEdit().setText(tr("Select"))
         return
      valeur=self.objSimp.getValeur()
      if not(type(valeur) == str) : valeur=str(valeur)
      self.CBChoix.setCurrentIndex(self.CBChoix.findText(valeur))
      
  def determineChoix(self):
      listeChoix=[]
      if self.maListeDeValeur == None : self.maListeDeValeur=[]
      for choix in self.maListeDeValeur:
          if not(type(choix) == str) : choix=str(choix)
          listeChoix.append(choix)
          self.CBChoix.addItem(choix)
      self.CBChoix.setEditable(True)
      monCompleteur=QCompleter(listeChoix,self) 
      monCompleteur.setCompletionMode(QCompleter.PopupCompletion) 
      self.CBChoix.setCompleter(monCompleteur)

  def choixSaisi(self):
      self.CBChoix.lineEdit().setStyleSheet(("\n"
"QLineEdit {\n"
"     font : italic ;\n"
"     background: rgb(235,235,235);\n"
" }"))
      valeur=str(self.CBChoix.currentText())
      SaisieValeur.LEvaleurPressed(self,valeur)
      self.reaffiche()

class MonWidgetCB (Ui_WidgetCB, MonWidgetCBCommun):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
      self.maListeDeValeur=monSimpDef.into
      MonWidgetCBCommun. __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)

class MonWidgetCBSD (Ui_WidgetCB,MonWidgetCBCommun):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
      self.maListeDeValeur=node.item.getSdAvantDuBonType()
      MonWidgetCBCommun.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
