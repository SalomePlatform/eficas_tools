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
import string,types,os

# Modules Eficas
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from desUniqueInto        import Ui_DUnIn
from qtCommun             import QTPanel
from qtSaisie             import SaisieValeur
from politiquesValidation import PolitiqueUnique

class DUnIn(Ui_DUnIn,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       if hasattr(parent,"leLayout"):
          parent.leLayout.removeWidget(parent.leLayout.widgetActive)
          parent.leLayout.widgetActive.close()
          parent.leLayout.addWidget(self)
          parent.leLayout.widgetActive=self
       else:
          parent.partieDroite=QWidget()
          parent.leLayout=QGridLayout(parent.partieDroite)
          parent.leLayout.addWidget(self)
          parent.addWidget(parent.partieDroite)
          parent.leLayout.widgetActive=self
       self.setupUi(self)


class MonUniqueIntoPanel(DUnIn,QTPanel,SaisieValeur):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonUniqueIntoPanel"
        self.alpha=0
        QTPanel.__init__(self,node,parent)
        DUnIn.__init__(self,parent,fl)
        SaisieValeur.RemplitPanel(self)
        self.politique=PolitiqueUnique(node,parent)
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.listBoxVal, SIGNAL("itemDoubleClicked(QListWidgetItem*)" ), self.ClicValeur )
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.BAlpha,SIGNAL("clicked()"),self.BAlphaPressed)

  def ClicValeur(self):
        SaisieValeur.ClicValeur(self)
        self.editor.init_modif()

  def BOkPressed(self):
        SaisieValeur.BOkPressed(self)

  def BAlphaPressed(self):
       if self.alpha==1 :
         self.alpha=0
         self.BAlpha.setText(QApplication.translate("DPlusInto", "Tri Alpha",None,QApplication.UnicodeUTF8))
       else :
         self.alpha=1
         self.BAlpha.setText(QApplication.translate("DPlusInto", "Tri Cata",None,QApplication.UnicodeUTF8))
       SaisieValeur.RemplitPanel(self,alpha=self.alpha)

