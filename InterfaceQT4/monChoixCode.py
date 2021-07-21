# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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
try :
   from builtins import str
except : pass

import os,sys,re
from desChoixCode import Ui_ChoixCode
from PyQt5.QtWidgets import QDialog, QRadioButton, QGroupBox, QButtonGroup
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import QProcess, QFileInfo, Qt, QSize

    
# Import des panels

class MonChoixCode(Ui_ChoixCode,QDialog):
  """
  Classe definissant le panel associe aux mots-cles qui demandent
  a l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discretes
  """
  def __init__(self,  appliEficas=None):
      QDialog.__init__(self,parent=appliEficas,flags=Qt.Window)
      self.setModal(True)
      self.setupUi(self)
      self.appliEficas=appliEficas
      self.verifieInstall()
      self.code=None
      self.buttonBox.accepted.disconnect(self.accept)
      self.buttonBox.accepted.connect(self.choisitCode)
     # self.pB_OK.clicked.connect(self.choisitCode)
      #self.pB_cancel.clicked.connect(self.sortie)

  def sortie(self):
      QDialog.reject(self)

  def verifieInstall(self):
      self.groupCodes=QButtonGroup(self.groupBox)
      vars=list(os.environ.items())
      listeCode=('Adao','Carmel3D','CarmelCND','CF','MAP','MT','PSEN','PSEN_N1','Telemac','ZCracks',)
      for code in listeCode:
          dirCode=os.path.abspath(os.path.join(os.path.abspath(__file__),'../..',code))
          try :
             l=os.listdir(dirCode)
             bouton=QRadioButton(self.groupBox)
             bouton.setText(code)
             self.groupCodes.addButton(bouton)
             self.vlBouton.addWidget(bouton)
          except :
             clef="PREFS_CATA_"+code
             try :
                repIntegrateur=os.path.abspath(os.environ[clef])
                l=os.listdir(repIntegrateur)
                bouton=QRadioButton(self.groupBox)
                bouton.setText(code)
                bouton.show()
                self.groupCodes.addButton(bouton)
             except :
                pass
      listeCodesIntegrateur=[]
      for k,v in vars:
          if re.search('^PREFS_CATA_',k) != None and k[11:] not in listeCode:
             listeCodesIntegrateur.append(k[11:])
      for code in listeCodesIntegrateur:
          try :
              clef="PREFS_CATA_"+code
              repIntegrateur=os.path.abspath(os.environ[clef])
              l=os.listdir(repIntegrateur)
              bouton=QRadioButton(self)
              bouton.setText(code)
              bouton.show()
              self.groupCodes.addButton(bouton)
          except :
              pass
      self.appliEficas.listeCode=self.appliEficas.listeCode+listeCodesIntegrateur

  def choisitCode(self):
      bouton=self.groupCodes.checkedButton()
      if bouton==None : return
      code=str(bouton.text())
      codeUpper=code.upper()
      self.appliEficas.code=codeUpper
      try :
          dirCode=os.path.abspath(os.path.join(os.path.abspath(__file__),'../..',code))
          l=os.listdir(dirCode)
          sys.path.insert(0,dirCode)
      except :
          clef="PREFS_CATA_"+code
          repIntegrateur=os.path.abspath(os.environ[clef])
          l=os.listdir(repIntegrateur)
          sys.path.insert(0,repIntegrateur)
      self.close()
