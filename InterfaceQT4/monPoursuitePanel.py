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

import os,traceback,sys
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from monMacroPanel import MonMacroPanel


# Import des panels
# La page est ajoutee a partir du python genere par designer

class MonPoursuitePanel(MonMacroPanel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        MonMacroPanel.__init__(self,node,parent,name,fl)
        self.node=node
        self.ajoutPageOk()

  def ajoutPageOk(self) :
        self.TabPage = QtGui.QWidget()
        self.TabPage.setGeometry(QtCore.QRect(0,0,499,433))
        self.TabPage.setObjectName("TabPage")
        self.gridLayout_2 = QtGui.QGridLayout(self.TabPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textLabel1_3 = QtGui.QLabel(self.TabPage)
        self.textLabel1_3.setWordWrap(False)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.gridLayout_2.addWidget(self.textLabel1_3,0,0,1,1)
        self.LENomFichier = QtGui.QLineEdit(self.TabPage)
        self.LENomFichier.setMinimumSize(QtCore.QSize(470,40))
        self.LENomFichier.setObjectName("LENomFichier")
        self.gridLayout_2.addWidget(self.LENomFichier,1,0,1,1)
        spacerItem = QtGui.QSpacerItem(21,190,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem,2,0,1,1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem1 = QtGui.QSpacerItem(331,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.BBrowse = QtGui.QPushButton(self.TabPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BBrowse.sizePolicy().hasHeightForWidth())
        self.BBrowse.setSizePolicy(sizePolicy)
        self.BBrowse.setMinimumSize(QtCore.QSize(140,50))
        self.BBrowse.setObjectName("BBrowse")
        self.hboxlayout.addWidget(self.BBrowse)
        self.gridLayout_2.addLayout(self.hboxlayout,3,0,1,1)
        spacerItem2 = QtGui.QSpacerItem(21,87,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2,4,0,1,1)
        self.TWChoix.addTab(self.TabPage,"")
        self.textLabel1_3.setText(QtGui.QApplication.translate("DPour", "<font size=\"+1\">La commande POURSUITE requiert un nom de Fichier :</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.BBrowse.setText(QtGui.QApplication.translate("DPour", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.TabPage), QtGui.QApplication.translate("DPour", "Fichier Poursuite", None, QtGui.QApplication.UnicodeUTF8))

        self.LENomFichier.setText(self.node.item.object.jdc_aux.nom)
        self.connect(self.BBrowse,SIGNAL("clicked()"),self.BBrowsePressed)


  def BBrowsePressed(self):
      self.node.makeEdit()


