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
# Modules Eficas

from desRacine import Ui_DRac
from qtCommun  import QTPanel
from qtCommun  import QTPanelTBW2

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DRac(Ui_DRac,QWidget):
   def __init__(self,parent ,modal = 0 ) :
       QWidget.__init__(self,parent)
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

class MonRacinePanel(DRac,QTPanelTBW2):
  """
  Classe definissant le panel associe aux mots-clefs qui demandent
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonRacinePanel"
        DRac.__init__(self,parent,0)
        self.connecterSignaux()
        QTPanel.__init__(self,node,parent)
        QTPanelTBW2.__init__(self,node,parent,racine=1)
        self.LEFiltre.setFocus()


  def connecterSignaux(self):
        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListWidgetItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.BNext,SIGNAL("clicked()"),self.BNextPressed)

  def BOkPressed(self):
      self.DefCmd()

  def BNextPressed(self):
      QTPanelTBW2.BNextPressed(self)

  def BuildTabCommandChanged(self):
      QTPanelTBW2.BuildLBNouvCommandChanged(self)

  def LEFiltreTextChanged(self):
      QTPanelTBW2.LEFiltreTextChanged(self)

  def LEfiltreReturnPressed(self):
      QTPanelTBW2.LEfiltreReturnPressed(self)

  def LBNouvCommandeClicked(self):
      QTPanelTBW2.LBNouvCommandeClicked(self)

  def AppelleBuildLBRegles(self):
      listeRegles=self.node.item.get_regles()
      listeNomsEtapes = self.node.item.get_l_noms_etapes()
      self.BuildLBRegles(listeRegles,listeNomsEtapes)

  def DefCmd(self):
      if self.LBNouvCommande.currentItem()== None : return
      name=str(self.LBNouvCommande.currentItem().text())
      if name==QString(" "): return
      if name.find("GROUPE :")==0 : return
      self.editor.init_modif()
      new_node = self.node.append_child(name,'first')
