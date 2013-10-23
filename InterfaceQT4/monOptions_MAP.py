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

import os, re, sys

from PyQt4.QtGui  import *
from PyQt4.QtCore import *

from OptionsMAP import Ui_desOptionsMap


class desOptions(Ui_desOptionsMap,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.setupUi(self)
       self.setModal(modal)

class Options(desOptions):
   def __init__(self,parent = None,modal = 0,configuration=None):
       desOptions.__init__(self,parent,modal)
       self.configuration=configuration
       self.viewMan=parent
       self.connecterSignaux()
       self.code='MAP'
       self.initAll()

   def connecterSignaux(self) :
       self.connect(self.LESaveDir,SIGNAL("returnPressed()"),self.ChangeSaveDir)
       self.connect(self.BOk,SIGNAL("clicked()"),self.BOkClicked)
       self.connect(self.BOk2,SIGNAL("clicked()"),self.BOkClicked2)
       self.connect(self.BCancel,SIGNAL("clicked()"),self.close)
       self.connect(self.BDir,SIGNAL("clicked()"),self.BDirClicked)


   def initAll(self):

       if hasattr(self.configuration,"savedir"):
          self.LESaveDir.setText(self.configuration.savedir)


   def BOkClicked(self):
       self.configuration.save_params()

   def BOkClicked2(self):
       self.configuration.save_params()
       self.close()

   def ChangeSaveDir(self):
       if not os.path.isdir(self.LESaveDir.text()) :
          res = QMessageBox.warning( None,
                 "Dossier de sauvegarde par defaut",
                 "Le dossier n'existe pas.",
                 "&Ok",
                 "&Abandonner")
          if res == 1 :
             if hasattr(self.configuration,"savedir"):
                self.LESaveDir.setText(self.configuration.savedir)
       self.configuration.savedir=str(self.LESaveDir.text())
       self.configuration.save_params()

   def BDirClicked(self):
       directory = QFileDialog.getExistingDirectory(self,
               directory = self.configuration.savedir,
               options = QFileDialog.ShowDirsOnly)
       if directory:
          self.LESaveDir.setText(directory)
          self.ChangeSaveDir()
