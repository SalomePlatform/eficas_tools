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

from desRacine import Ui_DRac
from qtCommun  import QTPanel
from qtCommun  import QTPanelTBW2

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DRac(Ui_DRac,QWidget):
   def __init__(self,parent ,modal = 0 ) :
       QWidget.__init__(self,parent)
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



# Import des panels

class MonRacinePanel(DRac,QTPanelTBW2):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonRacinePanel"
        DRac.__init__(self,parent,0)
        self.connecterSignaux()
        QTPanel.__init__(self,node,parent)
        QTPanelTBW2.__init__(self,node,parent,racine=1)
        self.LEFiltre.setFocus()


  def connecterSignaux(self):
        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListBoxItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.BNext,SIGNAL("clicked()"),self.BNextPressed)

  def BOkPressed(self):
      self.DefCmd()

  def BNextPressed(self):
      QTPanelTBW2.BNextPressed(self)

  def BuildTabCommandChanged(self):
      QTPanelTBW2.BuildLBNouvCommandChanged(self)

  def LEFiltreTextChanged(self):
      QTPanelTBW2.LEFiltreTextChanged(self)

  def LEfiltreReturnPressed(self):
      QTPanelTBW2.LEfiltreReturnPressed(self)

  def LBNouvCommandeClicked(self):
      QTPanelTBW2.LBNouvCommandeClicked(self)

  def AppelleBuildLBRegles(self):
      listeRegles=self.node.item.get_regles()
      listeNomsEtapes = self.node.item.get_l_noms_etapes()
      self.BuildLBRegles(listeRegles,listeNomsEtapes)

  def DefCmd(self):
      if self.LBNouvCommande.currentItem()== None : return
      name=str(self.LBNouvCommande.currentItem().text())
      if name==QString(" "): return
      if name.find("GROUPE :")==0 : return
      self.editor.init_modif()
      print self.node.__class__
      new_node = self.node.append_child(name,'first')
