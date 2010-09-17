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

from desListeParam import Ui_DLisParam
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# Import des panels
class DLisParam(Ui_DLisParam,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.setupUi(self)

class MonListeParamPanel(DLisParam):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,liste,parent,name = None,fl = 0):
        #print "MonListeParamPanel"
        self.panel=parent
        DLisParam.__init__(self,parent,fl)
        self.liste=liste
        self.dictListe={}
        self.initVal()
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.LBParam,SIGNAL("itemPressed(QListWidgetItem*)"),self.LBParamItemPressed)

  def initVal(self):
        self.LBParam.clear()
        for param in self.liste :
            self.LBParam.addItem(QString(repr(param)))
            self.dictListe[QString(repr(param))] = param

  def LBParamItemPressed(self):
        #print self.LBParam.selectedItems()
        if self.LBParam.selectedItems()== None : return
        i=self.LBParam.selectedItems()[0].text()
        self.panel.Ajout1Valeur(self.dictListe[i])

  def on_BOk_clicked(self):
        self.LBParamItemPressed()
        self.close()
