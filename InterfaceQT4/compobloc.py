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


from __future__ import absolute_import
from Editeur     import Objecttreeitem

from . import compofact
from . import browser
from . import typeNode


class Node(browser.JDCNode,typeNode.PopUpMenuNodeMinimal):
        

    def createPopUpMenu(self):
        typeNode.PopUpMenuNodeMinimal.createPopUpMenu(self)


    def getPanelGroupe(self,parentQt,commande):
        maDefinition=self.item.get_definition()
        monObjet=self.item.object
        monNom=self.item.nom
        maCommande=commande
        if hasattr(parentQt,'niveau'): self.niveau=parentQt.niveau+1
        else : self.niveau=1
        from .monWidgetBloc import MonWidgetBloc
        widget=MonWidgetBloc(self,self.editor,parentQt,maDefinition,monObjet,self.niveau,maCommande)


class BLOCTreeItem(compofact.FACTTreeItem):
  itemNode=Node

  def get_objet(self,name) :
      for v in self.object.mc_liste:
          if v.nom == name : return v
      return None
    
  def iscopiable(self):
    return 0


import Accas
treeitem = BLOCTreeItem
objet = Accas.MCBLOC   
