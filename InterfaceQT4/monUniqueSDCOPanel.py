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
from PyQt4.QtCore import *
from PyQt4.QtGui  import *

from Extensions.i18n import tr
from desUniqueSDCO        import Ui_DUnSDCO
from qtCommun             import QTPanel
from qtSaisie             import SaisieSDCO

class DUnSDCO(Ui_DUnSDCO,QDialog):
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

class MonUniqueSDCOPanel(DUnSDCO,QTPanel,SaisieSDCO):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonUniquesSDCOPanel"
        QTPanel.__init__(self,node,parent)
        DUnSDCO.__init__(self,parent,fl)
        valeur = self.node.item.get_valeur()
        if valeur  != "" and valeur != None :
           self.LESDCO.setText(valeur.nom)
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.LESDCO,SIGNAL("returnPressed()"),self.LESDCOReturnPressed)


  def BOkPressed(self):
        SaisieSDCO.LESDCOReturnPressed(self)


  def BOuiPressed(self):
        self.Commentaire.setText(tr("Aucun Objet de ce type n'est defini"))
        self.rbOui.setChecked(1)

  def LESDCOReturnPressed(self):
        """
           Lit le nom donné par l'utilisateur au concept de type CO qui doit être
           la valeur du MCS courant et stocke cette valeur
        """
        SaisieSDCO.LESDCOReturnPressed(self)


