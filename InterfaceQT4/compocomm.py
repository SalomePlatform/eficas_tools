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
        self.Decommente = QAction(tr("decommenter"),self.tree)
        self.Decommente.triggered.connect(self.decommenter)
        self.Decommente.setStatusTip(tr("Decommente la commande "))

        if hasattr(self.item,'unComment'):
           self.menu.addAction(self.Decommente)

    def decommenter(self) :
        item= self.tree.currentItem()
        item.unCommentIt()

    def updateNodeLabel(self) :
        """
        """
        debComm=self.item.getText()
        self.setText(1,debComm)


    
class COMMTreeItem(Objecttreeitem.ObjectTreeItem):
    itemNode=Node    

    def init(self):
      self.setFunction = self.setValeur

    def getIconName(self):
      """
      Retourne le nom de l'icone associee au noeud qui porte self,
      dependant de la validite de l'objet
      NB : un commentaire est toujours valide ...
      """
      return "ast-white-percent"

    def getLabelText(self):
        """ Retourne 3 valeurs :
        - le texte a afficher dans le noeud representant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return tr('Commentaire'),None,None

    def getValeur(self):
      """
      Retourne la valeur de l'objet Commentaire cad son texte
      """
      return self.object.getValeur() or ''
    
    def getText(self):
        texte = self.object.valeur
        texte = texte.split('\n')[0]
        if len(texte) < 25 :
            return texte
        else :
            return texte[0:24]

    def setValeur(self,valeur):
      """
      Affecte valeur a l'objet COMMENTAIRE
      """
      self.object.setValeur(valeur)
      
    def getSubList(self):
      """
      Retourne la liste des fils de self
      """
      return []


    def getObjetCommentarise(self):
       """
           La methode getObjetCommentarise() de la classe compocomm.COMMTreeItem
           surcharge la methode getObjetCommentarise de la classe Objecttreeitem.ObjectTreeItem
           elle a pour but d'empecher l'utilisateur final de commentariser un commentaire.
       """
       raise EficasException( 'Impossible de commentariser un commentaire' )
  
import Extensions
treeitem =COMMTreeItem
objet = Extensions.commentaire.COMMENTAIRE    
