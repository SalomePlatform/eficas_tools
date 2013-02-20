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

from desChoixCata import Ui_DChoixCata
from PyQt4  import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Extensions.i18n import tr
# Import des panels

class MonChoixCata(Ui_DChoixCata,QtGui.QDialog):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self, QWparent, listeCata, title = None):
      QtGui.QDialog.__init__(self, QWparent)
      self.setModal(True)
      self.setupUi(self)
      self.CBChoixCata.addItems(listeCata)
      self.TLNb.setText(tr("%d versions du catalogue sont disponibles", len(listeCata)))
      if title is not None:
          self.setWindowTitle(tr(title))

  def on_buttonCancel_clicked(self):
      QDialog.reject(self)

  def on_buttonOk_clicked(self):
      QDialog.accept(self)

