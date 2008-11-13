# -*- coding: utf-8 -*-
from qt import *

#---------------------------#
class PopUpMenuNodePartiel :
#---------------------------#
    def createPopUpMenu(self):
        #menu
        self.menu = QPopupMenu(self.tree)

        #ss-menu Comment:
        self.commentMenu = QPopupMenu( self.menu )
        self.menu.insertItem( qApp.translate('Browser','Commentaire'), self.commentMenu ) 
        self.commentMenu.insertItem( 'après', self.addCommentAfter )
        self.commentMenu.insertItem( 'avant', self.addCommentBefore )

        #ss-menu Parameters:
        self.parametersMenu = QPopupMenu( self.menu )
        self.parametersMenu.insertItem( 'après', self.addParametersAfter )
        self.parametersMenu.insertItem( 'avant', self.addParametersBefore )

        #items du menu
        self.menu.insertItem( qApp.translate('Browser','Supprimer'), self.delete )
        self.menu.insertItem( qApp.translate('Browser','Parametres'), self.parametersMenu )

    
    def addCommentAfter(self):
        """
        """
        self.addComment()

    def addCommentBefore(self):
        """
        """
        self.addComment(False)

    def addParametersAfter(self):
        """
        """
        self.addParameters()

    def addParametersBefore(self):
        """
        """
        self.addParameters(False)


#-----------------------------------------#
class PopUpMenuNode(PopUpMenuNodePartiel) :
#-----------------------------------------#
    def createPopUpMenu(self):
        PopUpMenuNodePartiel.createPopUpMenu(self)
        self.commentMenu.insertItem( 'ce noeud', self.commentIt )
