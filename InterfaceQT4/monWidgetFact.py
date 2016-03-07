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
from determine import monEnvQT5
if monEnvQT5:
   from PyQt5.QtCore import Qt
   from PyQt5.QtWidgets import QWidget
else :
   from PyQt4.QtCore import *
   from PyQt4.QtGui import *


# Modules Eficas

from groupe import Groupe
from desWidgetFact import Ui_WidgetFact
from Extensions.i18n import tr
# Import des panels

class MonWidgetFact(Ui_WidgetFact,Groupe):
  """
  """
  def __init__(self,node,editor,parentQt,definition, obj, niveau,commande):
      #print "init de Fact"
      Groupe.__init__(self,node,editor,parentQt, definition,obj,niveau,commande)
      labeltext,fonte,couleur = self.node.item.GetLabelText()
      self.GroupBox.setText(tr(labeltext))
      self.GroupBox.setTextInteractionFlags(Qt.TextSelectableByMouse)
      self.parentQt.commandesLayout.insertWidget(-1,self)

  def focusInEvent(self,event):
     # print "je passe dans focusInEvent"
      if self.editor.code != "CARMELCND" :self.afficheOptionnel()
      QWidget.focusInEvent(self,event)

