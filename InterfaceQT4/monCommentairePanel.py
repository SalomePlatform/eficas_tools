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

from PyQt4 import *
from PyQt4.QtGui  import *
from PyQt4.QtCore import *

from desCommentaire import Ui_DComment
from qtCommun      import QTPanel
from qtCommun      import QTPanelTBW2

class DComment(Ui_DComment,QDialog):
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

class MonCommentairePanel(DComment,QTPanelTBW2,QTPanel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonCommentairePanel"
        DComment.__init__(self,parent,fl)
        QTPanel.__init__(self,node,parent)
        QTPanelTBW2.__init__(self,node,parent)
        self.RemplitPanel()
        self.connecterSignaux()
        self.textCommentaire.setFocus()

  def connecterSignaux(self) :
        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListWidgetItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.BNext,SIGNAL("pressed()"),self.BNextPressed)
        self.connect(self.textCommentaire,SIGNAL("textChanged()"),self.TexteCommentaireEntre)

  def RemplitPanel(self):
        texte=self.node.item.get_valeur()
        self.textCommentaire.setText(texte)

  def TexteCommentaireEntre(self):
        texte=str(self.textCommentaire.toPlainText())
        self.editor.init_modif()
        self.node.item.set_valeur(texte)
        self.node.onValid()

  def LEFiltreTextChanged(self):
      QTPanelTBW2.LEFiltreTextChanged(self)

  def LEfiltreReturnPressed(self):
      QTPanelTBW2.LEfiltreReturnPressed(self)

  def LBNouvCommandeClicked(self):
      QTPanelTBW2.LBNouvCommandeClicked(self)

  def BNextPressed(self) :
      QTPanelTBW2.BNextPressed(self)

  def BOkPressed(self):
      QTPanel.BOkPressed(self)

  def BuildTabCommandChanged(self):
      QTPanelTBW2.BuildLBNouvCommandChanged(self)

