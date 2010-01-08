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

from desChoixMap import Ui_DChoixMap
from PyQt4  import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *


# Import des panels

class MonChoixMap(Ui_DChoixMap,QtGui.QDialog):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self, QWparent , name = None,fl = 0):
      QtGui.QDialog.__init__(self)
      self.setMinimumSize(50, 50);
      self.setModal(True)
      self.setupUi(self)
      self.appliEficas=QWparent
      
      self.RepIcon=self.appliEficas.RepIcon
      icon = QIcon(self.RepIcon+"/oslo.png")
      self.Pb1.setIcon(icon)
      icon1 = QIcon(self.RepIcon+"/munich.png")
      self.Pb2.setIcon(icon1)
      icon2 = QIcon(self.RepIcon+"/beijing.png")
      self.Pb3.setIcon(icon2)

  def closeEvent(self,event):
      self.appliEficas.sous_code=0
      
  def on_PB1_clicked(self):
      self.appliEficas.sous_code=1
      print "hhhhh"
      self.close()

  def on_Pb2_clicked(self):
      self.appliEficas.sous_code=2
      self.close()

  def on_Pb3(self):
      self.appliEficas.sous_code=3
      self.close()

