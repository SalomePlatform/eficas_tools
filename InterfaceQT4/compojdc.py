# -*- coding: utf-8 -*-
# Copyright (C) 2007-2017   EDF R&D
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
from Editeur import Objecttreeitem
from . import browser
from . import typeNode
from Extensions.i18n import tr


class Node(browser.JDCNode,typeNode.PopUpMenuRacine):

    def getPanel(self):
        from .monChoixCommande import MonChoixCommande
        return MonChoixCommande(self,self.item, self.editor)
        

    def createPopUpMenu(self):
        typeNode.PopUpMenuRacine.createPopUpMenu(self)

    def addParameters(self,apres):
        param=self.appendChild("PARAMETRE",pos=0)
        return param
       


class JDCTreeItem(Objecttreeitem.ObjectTreeItem):
  itemNode=Node
  
  def isExpandable(self):
    return 1

  def getText(self):
      return  "    "

  def getLabelText(self):
      # None --> fonte et couleur par defaut
      return tr(self.object.nom),None,None

  def getJdc(self):
    """
    Retourne l'objet pointe par self
    """
    return self.object
  
  def getIconName(self):
    if self.object.isValid():
      return "ast-green-square"
    else:
      return "ast-red-square"

  #def keys(self):
  #    if self.object.etapes_niveaux != []:
  #        return range(len(self.object.etapes_niveaux))
  #    else:
  #        return range(len(self.object.etapes))

  def addItem(self,name,pos):
      cmd = self._object.addEntite(name,pos)
      return cmd

  def suppItem(self,item) :
    # item             = item de l'ETAPE a supprimer du JDC
    # item.getObject() = ETAPE ou COMMENTAIRE
    # self.object      = JDC

    itemobject=item.getObject()
    if self.object.suppEntite(itemobject):
       if itemobject.nature == "COMMENTAIRE" :
          message = tr("Commentaire supprime")
       else :
          message = tr("Commande %s supprimee",itemobject.nom)
       return 1,message
    else:
       message=tr("Pb interne : impossible de supprimer cet objet")
       return 0,message

  def getSubList(self):
    """
       Retourne la liste des items fils de l'item jdc.
       Cette liste est conservee et mise a jour a chaque appel
    """
    if self.object.etapes_niveaux != []:
        liste = self.object.etapes_niveaux
    else:
        liste = self.object.etapes
    sublist=[None]*len(liste)
    # suppression des items lies aux objets disparus
    for item in self.sublist:
       old_obj=item.getObject()
       if old_obj in liste:
          pos=liste.index(old_obj)
          sublist[pos]=item
       else:
          pass # objets supprimes ignores
    # ajout des items lies aux nouveaux objets
    pos=0
    for obj in liste:
       if sublist[pos] is None:
          # nouvel objet : on cree un nouvel item
          item = self.makeObjecttreeitem(self.appliEficas, obj.nom + " : ", obj)
          sublist[pos]=item
       pos=pos+1

    self.sublist=sublist
    return self.sublist

  def getLNomsEtapes(self):
      """ Retourne la liste des noms des etapes de self.object"""
      return self.object.getLNomsEtapes()

  def getListeCmd(self):
      listeCmd = self.object.niveau.definition.getListeCmd()
      return listeCmd

import Accas
treeitem =JDCTreeItem
objet = Accas.JDC    
