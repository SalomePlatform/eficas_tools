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

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import string

from Editeur     import Objecttreeitem
import browser
import typeNode


class Node(browser.JDCNode,typeNode.PopUpMenuNodePartiel):
    def getPanel( self ):
        """
        """
        from monCommentairePanel import MonCommentairePanel
        return MonCommentairePanel(self,parent=self.editor)

    def createPopUpMenu(self):
        typeNode.PopUpMenuNodePartiel.createPopUpMenu(self)
        self.Decommente = QAction('Decommenter',self.tree)
        self.tree.connect(self.Decommente,SIGNAL("activated()"),self.Decommenter)
        self.Decommente.setStatusTip("Decommente la commande ")

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
      Retourne le nom de l'icône associée au noeud qui porte self,
      dépendant de la validité de l'objet
      NB : un commentaire est toujours valide ...
      """
      return "ast-white-percent"

    def GetLabelText(self):
        """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return 'c',None,None

    def get_valeur(self):
      """
      Retourne la valeur de l'objet Commentaire cad son texte
      """
      return self.object.get_valeur() or ''
    
    def GetText(self):
        texte = self.object.valeur
        texte = string.split(texte,'\n')[0]
        if len(texte) < 25 :
            return texte
        else :
            return texte[0:24]

    def set_valeur(self,valeur):
      """
      Afecte valeur à l'objet COMMENTAIRE
      """
      self.object.set_valeur(valeur)
      
    def GetSubList(self):
      """
      Retourne la liste des fils de self
      """
      return []


    def get_objet_commentarise(self):
       """
           La méthode get_objet_commentarise() de la classe compocomm.COMMTreeItem
           surcharge la méthode get_objet_commentarise de la classe Objecttreeitem.ObjectTreeItem
           elle a pour but d'empecher l'utilisateur final de commentariser un commentaire.
       """
       raise Exception( 'Impossible de commentariser un commentaire' )
  
import Extensions
treeitem =COMMTreeItem
objet = Extensions.commentaire.COMMENTAIRE    
