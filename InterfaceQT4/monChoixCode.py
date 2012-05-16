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

import os,sys
from desChoixCode import Ui_ChoixCode
from PyQt4.QtGui import * 
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
      self.connect(self.pB_OK,SIGNAL("clicked()"),self.choisitCode)
      self.connect(self.pB_cancel,SIGNAL("clicked()"),self.sortie)

  def sortie(self):
      QDialog.reject(self)

  def verifieInstall(self):
      self.groupCodes=QButtonGroup(self)
      for code in ('Aster','Cuve2dg','Openturns_Study','Openturns_Wrapper','Carmel3D','MAP'):
          nom='rB_'+code
          bouton=getattr(self,nom)
          dirCode=os.path.abspath(os.path.join(os.path.abspath(__file__),'../..',code))
          try :
             l=os.listdir(dirCode)
             self.groupCodes.addButton(bouton)
          except :
             bouton.close()

  def choisitCode(self):
      bouton=self.groupCodes.checkedButton()
      code=str(bouton.text())
      codeUpper=code.upper()
      self.parentAppli.code=codeUpper
      sys.path.insert(0,os.path.abspath(os.path.join(os.path.abspath(__file__),'../..',code)))
      self.close()
