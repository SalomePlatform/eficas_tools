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

import browser
import typeNode
from Extensions.i18n import tr


from Editeur import Objecttreeitem


class Node(browser.JDCNode,typeNode.PopUpMenuNodePartiel):

    def getPanelGroupe(self,parentQt,commande):
        maDefinition=self.item.get_definition()
        monObjet=self.item.object
        monNom=self.item.nom
        maCommande=commande
        if hasattr(parentQt,'niveau'): self.niveau=parentQt.niveau+1
        else : self.niveau=1
        if  hasattr(self,'plie') :print self.item.nom, self.plie
        if  hasattr(self,'plie') and self.plie==True : 
           from monWidgetFactPlie import MonWidgetFactPlie
           widget=MonWidgetFactPlie(self,self.editor,parentQt,maDefinition,monObjet,self.niveau,maCommande)
        else:
           from monWidgetFact import MonWidgetFact
           widget=MonWidgetFact(self,self.editor,parentQt,maDefinition,monObjet,self.niveau,maCommande)
        return widget


    def createPopUpMenu(self):
        typeNode.PopUpMenuNodeMinimal.createPopUpMenu(self)


class FACTTreeItem(Objecttreeitem.ObjectTreeItem):
  itemNode=Node
  
  def IsExpandable(self):
    return 1

  def GetText(self):
      return  ''

  def GetLabelText(self):
      """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud representant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
      """
      # None --> fonte et couleur par defaut
      return self.object.getlabeltext(),None,None

  def isvalid(self):
    return self.object.isvalid()

  def iscopiable(self):
    return 1

  def GetIconName(self):
    if self.object.isvalid():
      return "ast-green-los"
    elif self.object.isoblig():
      return "ast-red-los"
    else:
      return "ast-yel-los"

  def keys(self):
    keys=self.object.mc_dict.keys()
    return keys

  def GetSubList(self):
      """
         Reactualise la liste des items fils stockes dans self.sublist
      """
      liste=self.object.mc_liste
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
            def setfunction(value, object=obj):
                object.setval(value)
            item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj, setfunction)
            sublist[pos]=item
         pos=pos+1

      self.sublist=sublist
      return self.sublist

  def additem(self,name,pos):
    objet = self.object.addentite(name,pos)
    return objet

  def suppitem(self,item) :
      """ 
         Cette methode a pour fonction de supprimer l'item passee en argument
         des fils de l'item FACT qui est son pere
           - item = item du MOCLE a supprimer du MOCLE pere
           - item.getObject() = MCSIMP ou MCBLOC 
      """
      itemobject=item.getObject()
      if itemobject.isoblig() :
         #self.editor.affiche_infos(tr('Impossible de supprimer un mot-cle obligatoire '),Qt.red)
         return (0, tr('Impossible de supprimer un mot-cle obligatoire '))

      if self.object.suppentite(itemobject):
         message = tr("Mot-cle %s supprime")+ unicode(itemobject.nom)
         #self.editor.affiche_commentaire(message)
         return (1, message)
      else:
         #self.editor.affiche_infos(tr('Pb interne : impossible de supprimer ce mot-cle'),Qt.red)
         return (0,tr('Pb interne : impossible de supprimer ce mot-cle'))

import Accas
objet = Accas.MCFACT
treeitem = FACTTreeItem
