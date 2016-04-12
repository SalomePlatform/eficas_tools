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
from Extensions.i18n import tr

from feuille               import Feuille
from desWidgetCB           import Ui_WidgetCB 
from politiquesValidation  import PolitiqueUnique
from qtSaisie              import SaisieValeur

from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets import QComboBox, QCompleter
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *


class MonWidgetCBCommun (Ui_WidgetCB,Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.politique=PolitiqueUnique(self.node,self.editor)
        self.determineChoix()
        self.setValeursApresBouton()
        if monEnvQT5:
           self.CBChoix.currentIndexChanged.connect(self.ChoixSaisi)
        else :
           self.connect(self.CBChoix,SIGNAL("currentIndexChanged(int)"),self.ChoixSaisi)
        #self.CBChoix.lineEdit().setText(tr("Select"))
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.maCommande.listeAffichageWidget.append(self.CBChoix)


  def setValeursApresBouton(self):
      if self.objSimp.get_valeur()==None : 
         self.CBChoix.setCurrentIndex(-1)
         #self.CBChoix.lineEdit().setStyleSheet(("QLineEdit {" " background:yellow;\n" "font: italic ;\n" " }\n" " "))
         self.CBChoix.lineEdit().setText(tr("Select"))
         return
      valeur=self.objSimp.get_valeur()
      if not(type(valeur) in types.StringTypes) : valeur=str(valeur)
      self.CBChoix.setCurrentIndex(self.CBChoix.findText(valeur))
      
  def determineChoix(self):
      if monEnvQT5: listeChoix=[]
      else : listeChoix=QStringList()
      for choix in self.maListeDeValeur:
          if not(type(choix) in types.StringTypes) : choix=str(choix)
          if monEnvQT5: listeChoix.append(choix)
          else : listeChoix<<choix
          self.CBChoix.addItem(choix)
      self.CBChoix.setEditable(True)
      monCompleteur=QCompleter(listeChoix,self) 
      monCompleteur.setCompletionMode(QCompleter.PopupCompletion) 
      self.CBChoix.setCompleter(monCompleteur)

  def ChoixSaisi(self):
      self.CBChoix.lineEdit().setStyleSheet(("\n"
"QLineEdit {\n"
"     font : italic ;\n"
"     background: rgb(235,235,235);\n"
" }"))
      valeur=str(self.CBChoix.currentText())
      SaisieValeur.LEValeurPressed(self,valeur)
      self.reaffiche()

class MonWidgetCB (MonWidgetCBCommun):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
      self.maListeDeValeur=monSimpDef.into
      MonWidgetCBCommun. __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)

class MonWidgetCBSD (MonWidgetCBCommun):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
      self.maListeDeValeur=node.item.get_sd_avant_du_bon_type()
      MonWidgetCBCommun.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
