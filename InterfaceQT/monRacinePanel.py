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

from desRacine import DRac
from qtCommun  import QTPanel
from qtCommun  import QTPanelTBW2
from qtCommun  import itemColore
from qt import *


# Import des panels

class MonRacinePanel(DRac,QTPanelTBW2):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        DRac.__init__(self,parent,name,fl)
        QTPanel.__init__(self,node,parent)
        QTPanelTBW2.__init__(self,node,parent,racine=1)
        self.setMinimumSize(0,0)
        self.LEFiltre.setFocus()

  def BSupPressed(self):
      QTPanel.BSupPressed(self)

  def BOkPressed(self):
      self.DefCmd()

  def ViewDoc(self):
      QTPanel.ViewDoc(self)

  def BNextPressed(self):
      QTPanelTBW2.BNextPressed(self)

  def BuildTabCommand(self):
      QTPanelTBW2.BuildLBNouvCommande(self)

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
      if self.LBNouvCommande.selectedItem()== None : return
      name=str(self.LBNouvCommande.selectedItem().text())
      if name==QString(" "): return
      if name.find("GROUPE :")==0 : return
      self.editor.init_modif()
      new_node = self.node.append_child(name,'first')
