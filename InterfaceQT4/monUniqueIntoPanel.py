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


from desUniqueInto        import Ui_DUnIn
from qtCommun             import QTPanel
from qtSaisie             import SaisieValeur
from politiquesValidation import PolitiqueUnique

class DUnIn(Ui_DUnIn,QDialog):
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


class MonUniqueIntoPanel(DUnIn,QTPanel,SaisieValeur):
  """
  Classe definissant le panel associe aux mots-cles qui demandent
  a l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discretes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonUniqueIntoPanel"
        self.alpha=0
        QTPanel.__init__(self,node,parent)
        DUnIn.__init__(self,parent,fl)
        SaisieValeur.RemplitPanel(self,alpha=self.alpha)
        self.surligneValeur()
        self.politique=PolitiqueUnique(node,parent)
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.listBoxVal, SIGNAL("itemDoubleClicked(QListWidgetItem*)" ), self.ClicValeur )
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.BAlpha,SIGNAL("clicked()"),self.BAlphaPressed)

  def ClicValeur(self):
        SaisieValeur.ClicValeur(self)
        self.editor.init_modif()

  def BOkPressed(self):
        SaisieValeur.BOkPressed(self)

  def BAlphaPressed(self):
       if self.alpha==1 :
         self.alpha=0
         self.BAlpha.setText(tr("Tri Alpha"))
       else :
         self.alpha=1
         self.BAlpha.setText(tr("Tri Cata"))
       SaisieValeur.RemplitPanel(self,alpha=self.alpha)

  def surligneValeur(self):
      l=self.node.item.get_val()
      if l== None : return
      for i in self.listBoxVal.findItems(str(l),Qt.MatchExactly):
          i.setSelected(True)
