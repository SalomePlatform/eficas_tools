# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
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
