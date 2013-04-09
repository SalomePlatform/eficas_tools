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
import types
from repr import Repr
from copy import copy,deepcopy

# Modules Eficas
from Editeur import Objecttreeitem
from Extensions.eficas_exception import EficasException

myrepr = Repr()
myrepr.maxstring = 100
myrepr.maxother = 100

# Si Expandable vaut 1 les éléments du nuplet apparaissent dans l'arbre
# Si Expandable vaut 0 les éléments n'apparaissent pas
Expandable=1


import browser

class Node(browser.JDCNode): pass
    

class NUPLETTreeItem(Objecttreeitem.ObjectTreeItem):
  itemNode=Node

  def IsExpandable(self):
    return Expandable

  def GetText(self):
      return  ''

  def isvalid(self):
    return self.object.isvalid()

  def GetIconName(self):
    if self.object.isvalid():
      return "ast-green-los"
    elif self.object.isoblig():
      return "ast-red-los"
    else:
      return "ast-yel-los"

  def GetSubList(self):
    if not Expandable:return []
    sublist=[]
    for obj in self.object.mc_liste:
      item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj, None)    
      sublist.append(item)
    return sublist

  def additem(self,name,pos):
    raise EficasException("NUPLET")

  def suppitem(self,item) :
    raise EficasException("NUPLET")

import Accas
treeitem=NUPLETTreeItem
objet=Accas.MCNUPLET
