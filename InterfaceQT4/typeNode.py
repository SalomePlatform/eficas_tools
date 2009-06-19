# -*- coding: utf-8 -*-
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#---------------------------#
class PopUpMenuNodeMinimal :
#---------------------------#
    def createPopUpMenu(self):
        self.createActions()
        self.menu = QMenu(self.tree)
        #items du menu
        self.menu.addAction(self.Supprime)
    
    def createActions(self):
        self.CommApres = QAction('après',self.tree)
        self.tree.connect(self.CommApres,SIGNAL("activated()"),self.addCommApres)
        self.CommApres.setStatusTip("Insere un commentaire apres la commande ")
        self.CommAvant = QAction('avant',self.tree)
        self.tree.connect(self.CommAvant,SIGNAL("activated()"),self.addCommAvant)
        self.CommAvant.setStatusTip("Insere un commentaire avant la commande ")

        self.ParamApres = QAction('après',self.tree)
        self.tree.connect(self.ParamApres,SIGNAL("activated()"),self.addParametersApres)
        self.ParamApres.setStatusTip("Insere un parametre apres la commande ")
        self.ParamAvant = QAction('avant',self.tree)
        self.tree.connect(self.ParamAvant,SIGNAL("activated()"),self.addParametersAvant)
        self.ParamAvant.setStatusTip("Insere un parametre avant la commande ")

        self.Supprime = QAction('Supprimer',self.tree)
        self.tree.connect(self.Supprime,SIGNAL("activated()"),self.supprimeNoeud)
        self.Supprime.setStatusTip("supprime le mot clef ")
        self.Documentation = QAction('Documentation',self.tree)
        self.tree.connect(self.Documentation,SIGNAL("activated()"),self.viewDoc)
        self.Documentation.setStatusTip("documentation sur la commande ")

    def supprimeNoeud(self):
        item= self.tree.currentItem()
        item.delete()

    def viewDoc(self):
        self.node=self.tree.currentItem()
        cle_doc = self.node.item.get_docu()
        if cle_doc == None :
            QMessageBox.information( self.editor, "Documentation Vide", \
                                    "Aucune documentation Aster n'est associée à ce noeud")
        return
        #cle_doc = string.replace(cle_doc,'.','')
        #cle_doc = string.replace(cle_doc,'-','')
        #print dir(self)
        commande = self.editor.appliEficas.CONFIGURATION.exec_acrobat
        try :
            f=open(commande,"rb")
        except :
             texte="impossible de trouver la commande  " + commande
             QMessageBox.information( self.editor, "Lecteur PDF", texte)
             return
        nom_fichier = cle_doc+".pdf"
        fichier = os.path.abspath(os.path.join(self.editor.CONFIGURATION.path_doc,
                                       nom_fichier))
        try :
           f=open(fichier,"rb")
        except :
           texte="impossible d'ouvrir " + fichier
           QMessageBox.information( self.editor, "Documentation Vide", texte)
           return
        if os.name == 'nt':
           os.spawnv(os.P_NOWAIT,commande,(commande,fichier,))
        elif os.name == 'posix':
            script ="#!/usr/bin/sh \n%s %s&" %(commande,fichier)
            pid = os.system(script)

    def addParametersApres(self):
        item= self.tree.currentItem()
        item.addParameters(True)

    def addParametersAvant(self):
        item= self.tree.currentItem()
        item.addParameters(False)

    def addCommApres(self):
        item= self.tree.currentItem()
        item.addComment(True)

    def addCommAvant(self):
        item= self.tree.currentItem()
        item.addComment(False)

#--------------------------------------------#
class PopUpMenuNodePartiel (PopUpMenuNodeMinimal):
#---------------------------------------------#
    def createPopUpMenu(self):
        PopUpMenuNodeMinimal.createPopUpMenu(self)
        #ss-menu Comment:
        self.commentMenu=self.menu.addMenu('Commentaire')
        self.commentMenu.addAction(self.CommApres)
        self.commentMenu.addAction(self.CommAvant)
        #ss-menu Parameters:
        self.paramMenu =self.menu.addMenu('Parametre') 
        self.paramMenu.addAction(self.ParamApres)
        self.paramMenu.addAction(self.ParamAvant)
        self.menu.addAction(self.Documentation)


#-----------------------------------------#
class PopUpMenuNode(PopUpMenuNodePartiel) :
#-----------------------------------------#
    def createPopUpMenu(self):
        PopUpMenuNodePartiel.createPopUpMenu(self)
        self.Commente = QAction('ce noeud',self.tree)
        self.tree.connect(self.Commente,SIGNAL("activated()"),self.Commenter)
        self.Commente.setStatusTip("commente le noeud ")
        self.commentMenu.addAction(self.Commente)

    def Commenter(self):
        item= self.tree.currentItem()
        item.commentIt()
