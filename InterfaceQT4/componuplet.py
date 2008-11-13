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
import types
from repr import Repr
from copy import copy,deepcopy

# Modules Eficas
from Editeur import Objecttreeitem

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
    raise "NUPLET"

  def suppitem(self,item) :
    raise "NUPLET"

import Accas
treeitem=NUPLETTreeItem
objet=Accas.MCNUPLET
