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


from desUniqueBool import Ui_DBool
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiqueUnique
listeSuffixe= ('bmp','png','jpg' )



class DUnBool(Ui_DBool,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.appliEficas=parent.appliEficas
       self.RepIcon=parent.appliEficas.RepIcon
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

class MonUniqueBoolPanel(DUnBool,QTPanel,SaisieValeur):
  """
  Classe definissant le panel associe aux mots-cles qui demandent
  a l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discretes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonUniqueBoolPanel"
        self.editor=parent
        QTPanel.__init__(self,node,parent)
        DUnBool.__init__(self,parent,fl)
        self.InitrButton()
        self.connecterSignaux()
        self.Commentaire.setText(tr("un booleen est attendu"))

  def connecterSignaux(self) :
       self.connect(self.rbVrai,SIGNAL("clicked()"),self.vraiPressed)
       self.connect(self.rbFaux,SIGNAL("clicked()"),self.fauxPressed)

  def InitrButton(self):
        valeur=self.node.item.get_valeur()
        if valeur : self.rbVrai.setChecked(True)
        else 	  : self.rbFaux.setChecked(True)

  def vraiPressed(self):
        self.node.item.set_valeur(True)

  def fauxPressed(self):
        self.node.item.set_valeur(False)

