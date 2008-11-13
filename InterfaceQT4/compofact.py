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

from PyQt4 import *
from PyQt4.QtGui  import *
from PyQt4.QtCore import *
import browser

from Editeur import Objecttreeitem


class Node(browser.JDCNode):
    def getPanel(self):
        """
        """
        from monMCFactPanel import MonMCFactPanel
        return MonMCFactPanel(self,parent=self.editor)
        
    def doPaste(self,node_selected):
        objetACopier = self.item.get_copie_objet()
        child=node_selected.doPasteMCF(objetACopier)
        return child

    def doPasteMCF(self,objetACopier):
        child = self.parent.append_child(objetACopier,
                                              pos=self.item,
                                              retour='oui')
        return child


class FACTTreeItem(Objecttreeitem.ObjectTreeItem):
  itemNode=Node
  
  def IsExpandable(self):
    return 1

  def GetText(self):
      return  ''

  def GetLabelText(self):
      """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
      """
      # None --> fonte et couleur par défaut
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
         self.appli.affiche_infos('Impossible de supprimer un mot-clé obligatoire ')
         return 0

      if self.object.suppentite(itemobject):
         message = "Mot-clé " + itemobject.nom + " supprimé"
         self.appli.affiche_infos(message)
         return 1
      else:
         self.appli.affiche_infos('Pb interne : impossible de supprimer ce mot-clé')
         return 0

import Accas
objet = Accas.MCFACT
treeitem = FACTTreeItem
