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

from desVisu import Ui_DVisu
from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets import QDialog
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *


# Import des panels

class DVisu(Ui_DVisu ,QtGui.QDialog):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,parent = None , name = None,fl = 0):
      QtGui.QDialog.__init__(self,parent)
      self.setModal(True)
      self.setupUi(self)

  def on_buttonCancel_clicked(self):
      QDialog.reject(self)

  def on_buttonOk_clicked(self):
      QDialog.accept(self)

