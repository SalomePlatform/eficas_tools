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

from desChoixCata import Ui_DChoixCata
from PyQt4  import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *


# Import des panels

class MonChoixCata(Ui_DChoixCata,QtGui.QDialog):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,listeCata,readercata, QWparent , name = None,fl = 0):
      #print "MonChoixCata"
      QtGui.QDialog.__init__(self)
      self.setModal(True)
      self.setupUi(self)
      self.listeCata=listeCata
      self.readercata=readercata
      for cata in self.listeCata :
		self.CBChoixCata.insertItem(0,cata)
      lab  = QString(repr(len(listeCata)))
      lab += QString(" versions du catalogue sont disponibles")
      self.TLNb.setText(lab)
      self.CBChoixCata.setCurrentIndex(0)
      self.readercata.version_cata=self.CBChoixCata.currentText()

  def on_buttonCancel_clicked(self):
      QDialog.reject(self)

  def on_CBChoixCata_activated(self):
      self.readercata.version_cata=self.CBChoixCata.currentText()

  def on_buttonOk_clicked(self):
      QDialog.accept(self)

