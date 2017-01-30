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

import os,sys,re
from desChoixLangue import Ui_ChoixLangue
from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets import QDialog, QRadioButton, QGroupBox, QButtonGroup
    from PyQt5.QtGui import QPalette
    from PyQt5.QtCore import QProcess, QFileInfo, Qt, QSize
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *

    
# Import des panels

class MonChoixLangue(Ui_ChoixLangue,QDialog):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,  parentAppli=None):
      QDialog.__init__(self,parentAppli)
      self.setModal(True)
      self.setupUi(self)
      self.parentAppli=parentAppli
      self.installLangue()
      self.code=None
      if monEnvQT5: self.pB_OK.clicked.connect(self.choisitLangue)
      else : self.connect(self.pB_OK,SIGNAL("clicked()"),self.choisitLangue)


  def installLangue(self):
      if self.parentAppli.langue == 'fr' : self.rbFrancais.setChecked(True)
      else : self.rbEnglish.setChecked(True)

  def choisitLangue(self):
      if self.rbFrancais.isChecked() : self.parentAppli.langue='fr'
      else                           : self.parentAppli.langue ='ang'
      self.close()

