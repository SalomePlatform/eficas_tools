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

from PyQt5.QtWidgets import QAction

from Editeur     import Objecttreeitem
from . import browser
from . import typeNode
from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException


class Node(browser.JDCNode,typeNode.PopUpMenuNodePartiel):
    def getPanel( self ):
        """
        """
        from .monWidgetCommentaire import MonWidgetCommentaire
        return MonWidgetCommentaire(self,self.editor,self.item.object)

    def createPopUpMenu(self):
        typeNode.PopUpMenuNodePartiel.createPopUpMenu(self)
        self.Decommente = QAction(tr("Decommenter"),self.tree)
        self.Decommente.triggered.connect(self.Decommenter)
        self.Decommente.setStatusTip(tr("Decommente la commande "))

        if hasattr(self.item,'uncomment'):
           self.menu.addAction(self.Decommente)

    def Decommenter(self) :
        item= self.tree.currentItem()
        item.unCommentIt()

    def update_node_label(self) :
        """
        """
        debComm=self.item.GetText()
        self.setText(1,debComm)


    
class COMMTreeItem(Objecttreeitem.ObjectTreeItem):
    itemNode=Node    

    def init(self):
      self.setfunction = self.set_valeur

    def GetIconName(self):
      """
      Retourne le nom de l'icone associee au noeud qui porte self,
      dependant de la validite de l'objet
      NB : un commentaire est toujours valide ...
      """
      return "ast-white-percent"

    def GetLabelText(self):
        """ Retourne 3 valeurs :
        - le texte a afficher dans le noeud representant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return tr('Commentaire'),None,None

    def get_valeur(self):
      """
      Retourne la valeur de l'objet Commentaire cad son texte
      """
      return self.object.get_valeur() or ''
    
    def GetText(self):
        texte = self.object.valeur
        texte = texte.split('\n')[0]
        if len(texte) < 25 :
            return texte
        else :
            return texte[0:24]

    def set_valeur(self,valeur):
      """
      Affecte valeur a l'objet COMMENTAIRE
      """
      self.object.set_valeur(valeur)
      
    def GetSubList(self):
      """
      Retourne la liste des fils de self
      """
      return []


    def get_objet_commentarise(self):
       """
           La methode get_objet_commentarise() de la classe compocomm.COMMTreeItem
           surcharge la methode get_objet_commentarise de la classe Objecttreeitem.ObjectTreeItem
           elle a pour but d'empecher l'utilisateur final de commentariser un commentaire.
       """
       raise EficasException( 'Impossible de commentariser un commentaire' )
  
import Extensions
treeitem =COMMTreeItem
objet = Extensions.commentaire.COMMENTAIRE    
