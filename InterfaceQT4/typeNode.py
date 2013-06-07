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
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
import types



#---------------------------#
class PopUpMenuRacine :
#---------------------------#


    def createPopUpMenu(self):
        self.ParamApres = QAction(tr('Parametre'),self.tree)
        self.tree.connect(self.ParamApres,SIGNAL("activated()"),self.addParametersApres)
        self.ParamApres.setStatusTip(tr("Insere un parametre"))
        self.menu = QMenu(self.tree)
        self.menu.addAction(self.ParamApres)


    def addParametersApres(self):
        item= self.tree.currentItem()
        item.addParameters(True)

#---------------------------#
class PopUpMenuNodeMinimal :
#---------------------------#

    def createPopUpMenu(self):
        #self.appliEficas.salome=True
        self.createActions()
        self.menu = QMenu(self.tree)
        #items du menu
        self.menu.addAction(self.Supprime)
        if hasattr(self.appliEficas, 'mesScripts'):
            if self.tree.currentItem().item.get_nom() in self.appliEficas.mesScripts.dict_commandes.keys() : 
               self.ajoutScript()
    
    def ajoutScript(self):
    # cochon mais je n arrive pas a faire mieux avec le mecanisme de plugin
        listeCommandes=self.appliEficas.mesScripts.dict_commandes[self.tree.currentItem().item.get_nom()]
        if type(listeCommandes) != types.TupleType: listeCommandes=(listeCommandes,)
        if len(listeCommandes) > 5 : print "pas possible appeler la maintenance" 
        numero=0
        for commande in listeCommandes :
           conditionSalome=commande[3]
           if (self.appliEficas.salome == 0 and conditionSalome == True): return
           label=commande[1]
           tip=commande[5]
           self.action=QAction(label,self.tree)
           self.action.setStatusTip(tip)
           if numero==4: 
              self.tree.connect(self.action,SIGNAL("activated()"),self.AppelleFonction4)
           if numero==3: 
              self.tree.connect(self.action,SIGNAL("activated()"),self.AppelleFonction3)
              numero=4
           if numero==2: 
              self.tree.connect(self.action,SIGNAL("activated()"),self.AppelleFonction2)
              numero=3
           if numero==1: 
              self.tree.connect(self.action,SIGNAL("activated()"),self.AppelleFonction1)
              numero=2
           if numero==0: 
              self.tree.connect(self.action,SIGNAL("activated()"),self.AppelleFonction0)
              numero=1
           self.menu.addAction(self.action)


    def AppelleFonction0(self):
        self.AppelleFonction(0)

    def AppelleFonction1(self):
        self.AppelleFonction(1)

    def AppelleFonction2(self):
        self.AppelleFonction(2)

    def AppelleFonction3(self):
        self.AppelleFonction(3)

    def AppelleFonction4(self):
        self.AppelleFonction(4)


    def AppelleFonction(self,numero):
        listeCommandes=self.appliEficas.mesScripts.dict_commandes[self.tree.currentItem().item.get_nom()]
        commande=listeCommandes[numero]
        conditionValid=commande[4]
        if (self.tree.currentItem().item.isvalid() == 0 and conditionValid == True):
                 QMessageBox.warning( None, 
                             tr("item invalide"),
                             tr("l item doit etre valide"),
                             tr("&Ok"))
		 return
        fonction=commande[0]
        listenomparam=commande[2]
        listeparam=[]
        for p in listenomparam:
            if hasattr(self.tree.currentItem(),p):
               listeparam.append(getattr(self.tree.currentItem(),p))
            if p=="self" : listeparam.append(self)
        try :
           fonction(listeparam,self.appliEficas)
        except :
           fonction(listeparam)


    def createActions(self):
        self.CommApres = QAction(tr('apres'),self.tree)
        self.tree.connect(self.CommApres,SIGNAL("activated()"),self.addCommApres)
        self.CommApres.setStatusTip(tr("Insere un commentaire apres la commande "))
        self.CommAvant = QAction(tr('avant'),self.tree)
        self.tree.connect(self.CommAvant,SIGNAL("activated()"),self.addCommAvant)
        self.CommAvant.setStatusTip(tr("Insere un commentaire avant la commande "))

        self.ParamApres = QAction(tr('apres'),self.tree)
        self.tree.connect(self.ParamApres,SIGNAL("activated()"),self.addParametersApres)
        self.ParamApres.setStatusTip(tr("Insere un parametre apres la commande "))
        self.ParamAvant = QAction(tr('avant'),self.tree)
        self.tree.connect(self.ParamAvant,SIGNAL("activated()"),self.addParametersAvant)
        self.ParamAvant.setStatusTip(tr("Insere un parametre avant la commande "))

        self.Supprime = QAction(tr('Supprimer'),self.tree)
        self.tree.connect(self.Supprime,SIGNAL("activated()"),self.supprimeNoeud)
        self.Supprime.setStatusTip(tr("supprime le mot clef "))
        self.Documentation = QAction(tr('Documentation'),self.tree)
        self.tree.connect(self.Documentation,SIGNAL("activated()"),self.viewDoc)
        self.Documentation.setStatusTip(tr("documentation sur la commande "))

    def supprimeNoeud(self):
        item= self.tree.currentItem()
        item.delete()

    def viewDoc(self):
        self.node=self.tree.currentItem()
        cle_doc = self.node.item.get_docu()
        if cle_doc == None :
            QMessageBox.information( self.editor,tr( "Documentation Vide"), \
                                    tr("Aucune documentation n'est associee a ce noeud"))
            return
        commande = self.editor.appliEficas.CONFIGURATION.exec_acrobat
        try :
            f=open(commande,"rb")
        except :
             texte=tr("impossible de trouver la commande  ") + commande
             QMessageBox.information( self.editor, tr("Lecteur PDF"), texte)
             return
        import os
        if cle_doc.startswith('http:'):
           fichier = cle_doc
        else :
            fichier = os.path.abspath(os.path.join(self.editor.CONFIGURATION.path_doc,
                                       cle_doc))
            try :
               f=open(fichier,"rb")
            except :
               texte=tr("impossible d'ouvrir ") + fichier
               QMessageBox.information( self.editor, tr("Documentation Vide"), texte)
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
        self.commentMenu=self.menu.addMenu(tr('Commentaire'))
        self.commentMenu.addAction(self.CommApres)
        self.commentMenu.addAction(self.CommAvant)
        #ss-menu Parameters:
        self.paramMenu =self.menu.addMenu(tr('Parametre')) 
        self.paramMenu.addAction(self.ParamApres)
        self.paramMenu.addAction(self.ParamAvant)
        self.menu.addAction(self.Documentation)
        self.menu.removeAction(self.Supprime)
        self.menu.addAction(self.Supprime)


#-----------------------------------------#
class PopUpMenuNode(PopUpMenuNodePartiel) :
#-----------------------------------------#
    def createPopUpMenu(self):
        PopUpMenuNodePartiel.createPopUpMenu(self)
        self.Commente = QAction(tr('ce noeud'),self.tree)
        self.tree.connect(self.Commente,SIGNAL("activated()"),self.Commenter)
        self.Commente.setStatusTip(tr("commente le noeud "))
        self.commentMenu.addAction(self.Commente)
        self.menu.removeAction(self.Supprime)
        self.menu.addAction(self.Supprime)

    def Commenter(self):
        item= self.tree.currentItem()
        item.commentIt()
