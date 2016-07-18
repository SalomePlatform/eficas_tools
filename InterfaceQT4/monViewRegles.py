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
import traceback

from Extensions.i18n import tr
from determine import monEnvQT5
if monEnvQT5:
   from PyQt5.QtCore import Qt
   from PyQt5.QtWidgets import QDialog, QListWidgetItem
else :
   from PyQt4.QtGui import *
   from PyQt4.QtCore import *
from desViewRegles import Ui_viewRegles

# ------------------------------------ #
class ViewRegles(Ui_viewRegles,QDialog):
# ------------------------------------ #
    """
    Classe permettant la visualisation de texte
    """
    def __init__(self,parent,liste,entete=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.setModal(False)
        if monEnvQT5 : self.bclose.clicked.connect(self.close)
        else         : self.connect( self.bclose,SIGNAL("clicked()"), self, SLOT("close()") )

        if entete != None : self.setWindowTitle (entete)
        for ligne in liste :
          texte=ligne[0]
          couleur=ligne[1]
          if couleur==Qt.black :
             self.LBRegles.addItem(texte)
          else :
             monItem=QListWidgetItem(texte)
             monItem.setForeground(Qt.red)
             self.LBRegles.addItem(monItem)


        
