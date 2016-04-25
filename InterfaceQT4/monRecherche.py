# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
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
from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets import QDialog
    from PyQt5.QtCore import Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *


# Import des panels

class DRecherche(Ui_desRecherche ,QDialog):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,parent = None , name = None,fl = 0):
      QDialog.__init__(self,parent)
      self.parentQT=parent
      self.tree=self.parentQT.tree
      self.setModal(True)
      self.setupUi(self)
      self.PBSuivant.setDefault(True)
      self.PBSuivant.setAutoDefault(False)
      if monEnvQT5 :
         self.PBSuivant.clicked.connect( self.suivantClicked)
         self.LERecherche.returnPressed.connect(self.recherche)
      else :
         self.connect(self.PBSuivant,SIGNAL("clicked()"), self.suivantClicked)
         self.connect(self.LERecherche,SIGNAL("returnPressed()"),self.recherche)
      self.surLigne=0
      self.listeTrouvee=()
      self.nodeSurligne=None

  def suivantClicked(self):
      #if self.motAChercher!=self.LERecherche.text(): self.recherche()
      if self.listeTrouvee=={} : return
      if self.surLigne > len(self.listeTrouvee) -1 : return
      if self.nodeSurligne!=None : self.nodeSurligne.update_node_texte_in_black()
      #self.listeTrouvee[self.surLigne].update_node_texte_in_blue()
      #self.nodeSurligne=self.listeTrouvee[self.surLigne]
      self.listeTrouvee[self.surLigne].select()
      self.listeTrouvee[self.surLigne].affichePanneau()
      self.surLigne=self.surLigne+1
      self.PBSuivant.setFocus()
      if self.surLigne == len(self.listeTrouvee): self.surLigne=0

  def recherche(self):
      self.motAChercher=self.LERecherche.text()
      self.listeTrouvee=self.tree.findItems(self.motAChercher,Qt.MatchContains|Qt.MatchRecursive,1)
      self.surLigne=0

