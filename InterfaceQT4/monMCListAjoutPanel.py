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
# Modules Eficas

from desMCListAjout import Ui_DMCListAjout
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qtCommun import QTPanel



class DMCListAjout(Ui_DMCListAjout,QDialog):
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

# Import des panels

class MonMCListAjoutPanel(DMCListAjout,QTPanel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node,parent = None,name = None,fl = 0):
        #print "MonMCListAjoutPanel"
        DMCListAjout.__init__(self,parent,fl)
        QTPanel.__init__(self,node,parent)
        monMCFact=self.node.item.get_nom()
        self.MCFacteur.setText(QString(monMCFact))
        self.MCFacteur.setAlignment(Qt.AlignHCenter)
        self.connecterSignaux()

  def connecterSignaux(self):
        self.connect(self.bAjout,SIGNAL("clicked()"),self.BAjoutClicked)

  def BAjoutClicked(self):
        self.node.treeParent.append_child(self.node.item.get_nom())


