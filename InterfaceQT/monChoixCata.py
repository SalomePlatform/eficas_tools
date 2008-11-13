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

from desChoixCata import DChoixCata
from qt import *


# Import des panels

class MonChoixCata(DChoixCata):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,listeCata,readercata, parent = None,name = None,fl = 0):
      DChoixCata.__init__(self,parent,name,fl)
      self.listeCata=listeCata
      self.readercata=readercata
      for cata in self.listeCata :
		self.CBChoixCata.insertItem(cata,0)
      lab  = QString(repr(len(listeCata)))
      lab += QString(" versions du catalogue sont disponibles")
      self.TLNb.setText(lab)
      self.readercata.version_cata=self.CBChoixCata.currentText()

  def BSupPressed(self):
      QTPanel.BSupPressed(self)

  def CataChoisi(self):
      self.readercata.version_cata=self.CBChoixCata.currentText()

  def BOkPressed(self):
      QDialog.accept(self)

  def BCancelPressed(self):
      QDialog.reject(self)
