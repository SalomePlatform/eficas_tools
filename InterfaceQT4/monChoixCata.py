# -*- coding: utf-8 -*-
# Copyright (C) 2007-2017   EDF R&D
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

from __future__ import absolute_import
from desChoixCata import Ui_DChoixCata
from PyQt5.QtWidgets import QDialog

from Extensions.i18n import tr
# Import des panels

class MonChoixCata(Ui_DChoixCata,QDialog):
  """
  """
  def __init__(self, QWparent, listeCata, title = None):
      QDialog.__init__(self, QWparent)
      self.setModal(True)
      self.setupUi(self)
      self.CBChoixCata.addItems(listeCata)
      self.TLNb.setText(tr("%d versions du catalogue sont disponibles", len(listeCata)))
      if title is not None:
          self.setWindowTitle(tr(title))
      self.buttonOk.clicked.connect(self.cataChoisi)
      self.buttonCancel.clicked.connect(self.sortSansChoix)


  def sortSansChoix(self):
      QDialog.reject(self)

  def cataChoisi(self):
      QDialog.accept(self)

