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

from desRecherche import Ui_desRecherche
from PyQt4  import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Import des panels

class DRecherche(Ui_desRecherche ,QtGui.QDialog):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,parent = None , name = None,fl = 0):
      QtGui.QDialog.__init__(self,parent)
      self.parentQT=parent
      self.tree=self.parentQT.tree
      self.setModal(True)
      self.setupUi(self)
      self.PBSuivant.setDefault(False)
      self.PBSuivant.setAutoDefault(False)
      self.connect(self.PBSuivant,SIGNAL("clicked()"), self.suivantClicked)
      self.connect(self.LERecherche,SIGNAL("returnPressed()"),self.recherche)
      self.surLigne=0
      self.listeTrouvee=()
      self.nodeSurligne=None

  def suivantClicked(self):
      if self.listeTrouvee=={} : return
      if self.surLigne > len(self.listeTrouvee) -1 : return
      if self.nodeSurligne!=None : self.nodeSurligne.update_node_texte_in_black()
      self.listeTrouvee[self.surLigne].update_node_texte_in_blue()
      self.nodeSurligne=self.listeTrouvee[self.surLigne]
      self.surLigne=self.surLigne+1
      if self.surLigne == len(self.listeTrouvee): self.surLigne=0

  def recherche(self):
      motAChercher=self.LERecherche.text()
      self.listeTrouvee=self.tree.findItems(motAChercher,Qt.MatchContains|Qt.MatchRecursive,1)
      self.surLigne=0
      self.suivantClicked()

      #self.tree.collapseAll()
      
     

