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
from desChoixCode import Ui_ChoixCode
f monEnvQT5:
    from PyQt5.QtWidgets import QDialog, QRadioButton
    from PyQt5.QtGui import QPalette
    from PyQt5.QtCore import QProcess, QFileInfo, Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *

    
# Import des panels

class MonChoixCode(Ui_ChoixCode,QDialog):
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
      self.verifieInstall()
      self.code=None
      if monEnvQT5:
         self.pB_OK.clicked.connect(self.choisitCode)
         self.pB_cancel.clicked.connect(self.sortie)
      else :
         self.connect(self.pB_OK,SIGNAL("clicked()"),self.choisitCode)
         self.connect(self.pB_cancel,SIGNAL("clicked()"),self.sortie)

  def sortie(self):
      QDialog.reject(self)

  def verifieInstall(self):
      self.groupCodes=QButtonGroup(self.groupBox)
      vars=os.environ.items()
      listeCode=('Aster','Adao','Carmel3D','CarmelCND','CF','MAP','MT','PSEN','Telemac','ZCracks',)
      i=1
      for code in listeCode:
          nom='rB_'+code
          dirCode=os.path.abspath(os.path.join(os.path.abspath(__file__),'../..',code))
          try :
             l=os.listdir(dirCode)
             bouton=QRadioButton(self)
             bouton.setMinimumSize(QSize(0, 30))
             bouton.setText(code)
             bouton.setGeometry(QRect(10,20+30*i, 300, 30))
             bouton.show()
             self.groupCodes.addButton(bouton)
             i=i+1
          except :
             clef="PREFS_CATA_"+code
             try :
                repIntegrateur=os.path.abspath(os.environ[clef])
                l=os.listdir(repIntegrateur)
                bouton=QRadioButton(self)
                bouton.setGeometry(QRect(10,20+30*i, 300, 30))
                bouton.setMinimumSize(QSize(0, 30))
                bouton.setText(code)
                bouton.show()
                i=i+1
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
              bouton.setGeometry(QRect(10,20+30*i, 300, 30))
              i=i+1
              bouton.setMinimumSize(QSize(0, 30))
              bouton.setText(code)
              bouton.show()
              self.groupCodes.addButton(bouton)
          except :
              pass
      self.parentAppli.ListeCode=self.parentAppli.ListeCode+listeCodesIntegrateur

  def choisitCode(self):
      bouton=self.groupCodes.checkedButton()
      code=str(bouton.text())
      codeUpper=code.upper()
      self.parentAppli.code=codeUpper
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
