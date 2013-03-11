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

from desPixmap import Ui_LabelPixmap
from PyQt4  import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr


# Import des panels

class MonLabelPixmap(Ui_LabelPixmap,QtGui.QDialog):
  """
  classe servant a afficher le PDF d une loi pour Openturns
  """
  def __init__(self, QWparent , fichier, name):
      QtGui.QDialog.__init__(self,QWparent)
      self.fichier = fichier
      self.setModal(False)
      self.setupUi(self)
      self.setWindowTitle(tr("PDF de la loi : ") + name)
      self.labelPix.setPixmap(QPixmap(fichier));
      

  def on_buttonCancel_clicked(self):
      QDialog.reject(self)

  def closeEvent(self,event):
    import os
    os.system("rm -f %s" % self.fichier)
