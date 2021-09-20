# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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
from __future__ import print_function
try :
    from builtins import str
    from builtins import range
except : pass

import re
import types,sys,os
import traceback
from . import typeNode


from PyQt5.QtWidgets import QTreeWidget , QTreeWidgetItem, QApplication, QMessageBox
from PyQt5.QtGui     import QIcon
from PyQt5.QtCore    import Qt

from  Extensions.i18n  import tr
from .gereRegles       import GereRegles
from .monChoixCommande import MonChoixCommande

#------------------------------------------
class JDCTree( QTreeWidget,GereRegles ):
#------------------------------------------

    def __init__( self, jdc_item, QWParent):
    #----------------------------------------
        self.editor      = QWParent
        self.plie=False
        if self.editor.widgetTree !=None  :
            QTreeWidget.__init__(self, self.editor.widgetTree )
            self.editor.verticalLayout_2.addWidget(self)
            if self.editor.enteteQTree=='complet':
                self.headerItem().setText(0, "Commande   ")
                self.headerItem().setText(1, "Concept/Valeur")
            else :
                self.headerItem().setText(0, "Commande   ")
            self.setColumnWidth(0,200)
            self.setExpandsOnDoubleClick(False)
            self.setSelectionMode(3)
        else :
            QTreeWidget.__init__(self, None )
        self.item          = jdc_item
        self.tree          = self
        self.appliEficas   = self.editor.appliEficas
        self.childrenComplete=[]
        self.racine=self.item.itemNode(self,self.item)

        self.itemCourant=None

        self.itemClicked.connect(self.handleOnItem)
        self.itemCollapsed.connect(self.handleCollapsedItem)
        self.itemExpanded.connect(self.handleExpandedItem)

        self.node_selected = self.racine
        self.inhibeExpand  =  True
        self.expandItem(self.racine)
        self.inhibeExpand = False
        if self.racine.children !=[] :
            if self.editor.maConfiguration.afficheCommandesPliees : self.racine.children[0].plieToutEtReaffiche()
            else                                                  : self.racine.children[0].deplieToutEtReaffiche()
            self.racine.children[0].fenetre.donnePremier()
        else :
            self.racine.affichePanneau()

    def contextMenuEvent(self,event) :
    #---------------------------------
        coord = event.globalPos()
        item  = self.currentItem()
        self.handleContextMenu(item,coord)

    def handleContextMenu(self,item,coord):
    #-------------------------------------
        """
        Private slot to show the context menu of the listview.

        @param itm the selected listview item (QListWidgetItem)
        @param coord the position of the mouse pointer (QPoint)
        Attention : existeMenu permet de savoir si un menu est associe a cet item
        """
        print ("handleContextMenu")
        if item == None : return
        self.itemCourant = item
        if item.existeMenu == 0 : return

        if item.menu == None:
            item.createPopUpMenu()
        if item.menu != None:
        # PNPN reflechir a qqchose de generique pour remplacer cette fonctionnalite
        #   if item.item.getNom() == "DISTRIBUTION" and item.item.isValid() :
        #      item.Graphe.setEnabled(1)
           item.menu.exec_(coord)


    def handleCollapsedItem(self,item):
    #----------------------------------
        #print ("dans CollapsedItem", self.inhibeExpand  )
        if self.inhibeExpand == True : return

        # On traite le cas de l item non selectionne
        self.itemCourant = item
        itemParent = item
        while not (hasattr (itemParent,'getPanel')) : itemParent=itemParent.treeParent
        if self.tree.node_selected != itemParent :
            item.setExpanded(False)
            return

        item.setPlie()
        item.plieToutEtReaffiche()
        item.select()

    def handleExpandedItem(self,item):
    #----------------------------------
        #print ("handleExpandedItem pour ", item.item.nom, self.inhibeExpand)
        #import traceback
        #traceback.print_stack()
        if self.inhibeExpand == True : return

        self.itemCourant  = item
        self.inhibeExpand = True
        itemParent = item
        while not (hasattr (itemParent,'getPanel')) :
            if itemParent.plie==True : itemParent.setDeplie()
            itemParent=itemParent.treeParent
        if self.tree.node_selected != itemParent :
            item.setExpanded(True)
            self.inhibeExpand = False
            return
        item.deplieToutEtReaffiche()
        self.inhibeExpand = False


    def handleOnItem(self,item,int):
    #----------------------------------
        #print ("je passe dans handleOnItem pour ",self, item.item.nom, item, item.item, item.item.getLabelText())

        from InterfaceQT4 import composimp
        self.inhibeExpand = True
        self.itemCourant  = item
        itemParent        = item
        itemAvant         = item

        # PN : 22 juil 2021 --> bizarre ce itemAvant Verifier le while
        while not (hasattr (itemParent,'getPanel')) :
            if itemParent.plie==True : itemParent.setDeplie()
            itemAvant=itemParent
            itemParent=itemParent.treeParent

        if itemParent.fenetre != self.editor.fenetreCentraleAffichee :
            estUneFeuille=(isinstance(item,composimp.Node))
            # il faut afficher le parent
            # Attention - Specification particuliere pour MT qui permet de nn afficher qu 1 niveau
            # le catalogue contient cette indication dans fenetreIhm
            if estUneFeuille and itemParent.fenetreIhm=='deplie1Niveau' :
                if item == itemParent : itemParent.affichePanneau()
                else                  : itemAvant.afficheCeNiveau()
            elif estUneFeuille        : itemParent.affichePanneau()
            elif self.editor.maConfiguration.afficheCommandesPliees : itemParent.plieToutEtReafficheSaufItem(item)
            else                      : itemParent.affichePanneau()


        elif (isinstance(item,composimp.Node)) and item.fenetre : item.fenetre.rendVisible()
        elif itemParent!=item: self.tree.handleExpandedItem(item)

        # aide
        try :
            fr = item.item.getFr()
            chaineDecoupee= fr.split('\n')
            if len(chaineDecoupee) > 3 :
                txt='\n'.join(chaineDecoupee[0:2])+'...\nfull help : double clicked on validity chip of '+ str(item.item.nom)+ ' in central widget'
            else : txt=fr
            if self.editor: self.editor.afficheCommentaire(str(txt))
        except:
            pass

        item.select()
        self.inhibeExpand = False


    def choisitPremier(self,name):
    #----------------------------
        self.editor.layoutJDCCHOIX.removeWidget(self.racine.fenetre)
        self.racine.fenetre.close()
        new_node=self.racine.appendBrother(name,'after')

# type de noeud
COMMENT     = "COMMENTAIRE"
PARAMETERS  = "PARAMETRE"

#------------------------------------------
class JDCNode(QTreeWidgetItem,GereRegles):
#------------------------------------------
    def __init__( self, treeParent, item, itemExpand=False, ancien=False ):
    #----------------------------------------------------------------------
        #print ("creation d'un noeud : ", item, " ",item.nom,"", treeParent, self)
        #self.a=0


        self.item        = item
        self.vraiParent  = treeParent
        self.treeParent  = treeParent
        self.tree        = self.treeParent.tree
        self.editor      = self.treeParent.editor
        self.appliEficas = treeParent.appliEficas
        self.JESUISOFF   = 0
        self.firstAffiche = True
        self.childrenComplete=[]


        from InterfaceQT4 import compocomm
        from InterfaceQT4 import compoparam
        from InterfaceQT4 import composimp
        if   (isinstance(self.item,compocomm.COMMTreeItem))   : name = tr("Commentaire")
        elif (isinstance(self.item,compoparam.PARAMTreeItem)) : name = tr(str(item.getLabelText()[0]))
        else                                                  : name = tr(item.getLabelText()[0])
        if item.nom != tr(item.nom)                           : name = str(tr(item.nom)+" :")
        value = tr(str(item.getText() ) )

        # si specialisation de la fenetre
        if self.item.object.definition == None : self.fenetreIhm = None
            # Cas des listes de mots_clefs
        else : self.fenetreIhm = self.item.object.definition.fenetreIhm

        if self.editor.enteteQTree=='complet':mesColonnes=(name,value)
        else : mesColonnes=(name,)

        if self.treeParent.plie==True :
            self.plie                   = True
            self.appartientAUnNoeudPlie = True
            if self.treeParent.item.isMCList() : self.appartientAUnNoeudPlie =  self.treeParent.appartientAUnNoeudPlie
        else :
            self.plie                   = False
            self.appartientAUnNoeudPlie = False

        #if item.nom == "POUTRE" :print "creation d'un noeud : ", item, " ",item.nom,"", self.treeParent, self.appartientAUnNoeudPlie , self.plie

        if ancien and itemExpand     : self.plie = False
        if ancien and not itemExpand : self.plie = True
        if (isinstance(self.item,composimp.SIMPTreeItem)) : self.plie=False

        from InterfaceQT4 import compobloc
        from InterfaceQT4 import compomclist

        ajoutAuParentduNoeud=0
        self.treeParent=treeParent
        while (isinstance(self.treeParent,compobloc.Node) or ( isinstance(self.treeParent,compomclist.Node) and self.treeParent.item.isMCList())) :
            self.treeParent.childrenComplete.append(self)
            self.treeParent=self.treeParent.vraiParent
        self.treeParent.childrenComplete.append(self)


        if (isinstance(self,compobloc.Node) or (isinstance(self,compomclist.Node) and self.item.isMCList()) or ( hasattr(self.item.parent,'inhibeValidator') and isinstance(self,compomclist.Node) and self.item.parent.inhibeValidator)) :
        # Le dernier or ne sert que lorsqu'on est en train de creer une liste par les validator
            QTreeWidgetItem.__init__(self,None,mesColonnes)
        else :
            QTreeWidgetItem.__init__(self,self.treeParent,mesColonnes)

        self.setToolTip(0,self.item.getFr())
        self.setToolTip(1,self.item.getFr())
        repIcon=self.appliEficas.repIcon

        couleur=self.item.getIconName()
        monIcone = QIcon(repIcon+"/" + couleur + ".png")

        self.setIcon(0,monIcone)

        self.children = []
        self.buildChildren()
        self.menu=None
        self.existeMenu=1

        self.item.connect("valid",self.onValid,())
        self.item.connect("supp" ,self.onSupp,())
        self.item.connect("add"  ,self.onAdd,())
        self.item.connect("redessine"  ,self.onRedessine,())

        self.state=""
        self.fenetre=None
        try :
            if self.item.getObject().isBLOC() :
                self.setExpanded(True)
                self.plie=False
        except :
            pass


    def buildChildren(self,posInsertion=10000):
    #------------------------------------------
        """ Construit la liste des enfants de self """
        """ Se charge de remettre les noeuds Expanded dans le meme etat """
        #print ("*********** buildChildren ",self,self.item, self.item.nom)
        #print (poum)

        self.listeItemExpanded=[]
        self.listeItemPlie=[]

        for enfant in self.childrenComplete :
            if enfant.plie : self.listeItemPlie.append(enfant.item)
            else : self.listeItemExpanded.append(enfant.item)

        for enfant in self.childrenComplete :
            parent = enfant.treeParent
            parent.removeChild(enfant)
            enfant.JESUISOFF=1


        self.children = []
        self.childrenComplete = []
        sublist = self.item._getSubList()
        ind=0

        for item in sublist :
            itemExpand=False
            ancien=False
            if item in self.listeItemExpanded : itemExpand=True;  ancien=True
            if item in self.listeItemPlie     : itemExpand=False; ancien=True
            nouvelItem=item.itemNode(self,item,itemExpand,ancien)
            self.children.append(nouvelItem)

        #print ("fin *********** buildChildren ",self,self.item, self.item.nom, self.children)


    def chercheNoeudCorrespondant(self,objSimp):
    #-------------------------------------------
        sublist = self.item._getSubList()
        for node in self.childrenComplete:
            if node.item.object==objSimp : return node
        return None


    def afficheCeNiveau(self):
    #-------------------------
        #print ('afficheCeNiveau pour ', self.item.nom, self.item.getLabelText())
        for indiceWidget in range(self.editor.widgetCentraleLayout.count()):
            widget=self.editor.widgetCentraleLayout.itemAt(indiceWidget)
            self.editor.widgetCentraleLayout.removeItem(widget)
        if self.editor.fenetreCentraleAffichee != None :
            self.editor.widgetCentraleLayout.removeWidget(self.editor.fenetreCentraleAffichee)
            self.editor.fenetreCentraleAffichee.setParent(None)
            self.editor.fenetreCentraleAffichee.close()
            self.editor.fenetreCentraleAffichee.deleteLater()

        from monWidgetNiveauFact import MonWidgetNiveauFact, MonWidgetNiveauFactTableau
        maDefinition = self.item.get_definition()
        monObjet     = self.item.object
        if maDefinition.fenetreIhm=='Tableau' : self.maFenetreCadre=MonWidgetNiveauFactTableau(self,self.editor,maDefinition,monObjet)
        else : self.maFenetreCadre=MonWidgetNiveauFact(self,self.editor,maDefinition,monObjet)

        self.fenetre = self.maFenetreCadre
        self.editor.widgetCentraleLayout.addWidget(self.maFenetreCadre)
        self.editor.fenetreCentraleAffichee=self.maFenetreCadre
        self.select()
        #print ('fin afficheCeNiveau pour ', self.item.nom)


    def getPanelModifie(self):
    #-------------------------

        if self.fenetreIhm == None : return None
        if self.fenetreIhm =='deplie1Niveau':
            from InterfaceQT4.monWidgetCommandeDeplie1Niveau import MonWidgetCommandeDeplie1Niveau
            return MonWidgetCommandeDeplie1Niveau (self,self.editor ,self.item.object)
        return None


    def affichePanneau(self) :
    #-------------------------
        #print ('_________________ds affichePanneau pour', self.item.nom)
        # pour l instant pas d inactif
        if  not(self.item.isActif()) :
            from .monWidgetInactif import MonWidgetInactif
            self.fenetre = MonWidgetInactif(self,self.editor)
        else:
            itemParent=self
            while not (hasattr (itemParent,'getPanel')) : itemParent=itemParent.treeParent
            if itemParent != self :
            #print ('j appelle affichePanneau pour ', itemParent.item.nom , 'par', self.item.nom)
                itemParent.affichePanneau()
                #print ('fin _________________ds affichePanneau pour', self.item.nom)
                return

            self.fenetre = self.getPanelModifie()
            if self.fenetre == None : self.fenetre=self.getPanel()
            self.editor.restoreSplitterSizes()

        for indiceWidget in range(self.editor.widgetCentraleLayout.count()):
            widget = self.editor.widgetCentraleLayout.itemAt(indiceWidget)
            self.editor.widgetCentraleLayout.removeItem(widget)

        # ceinture et bretelle
        #print 'old fenetre = ',self.editor.fenetreCentraleAffichee
        if self.editor.fenetreCentraleAffichee != None :
            try :
                self.editor.widgetCentraleLayout.removeWidget(self.editor.fenetreCentraleAffichee)
                self.editor.fenetreCentraleAffichee.setParent(None)
                self.editor.fenetreCentraleAffichee.close()
                self.editor.fenetreCentraleAffichee.deleteLater()
            except :
                pass

        self.editor.widgetCentraleLayout.addWidget(self.fenetre)
        #print ("j ajoute ", self.fenetre, self.fenetre.node.item.nom)
        self.editor.fenetreCentraleAffichee=self.fenetre
        self.tree.node_selected= self

        if self.editor.first :
            if not(isinstance(self.fenetre,MonChoixCommande)): self.editor.first=False
        self.tree.inhibeExpand=True
        self.tree.expandItem(self)
        self.tree.inhibeExpand=False
        #print( '_________________fin affichePanneau pour', self.item.nom)


    def createPopUpMenu(self):
    #-------------------------
        #implemente dans les noeuds derives si necessaire
        self.existeMenu = 0

    def commentIt(self):
    #-------------------------
        """
        Cette methode a pour but de commentariser la commande pointee par self
        """
        # On traite par une exception le cas ou l'utilisateur final cherche a desactiver
        # (commentariser) un commentaire.
        try :
            pos=self.treeParent.children.index(self)
            commande_comment = self.item.getObjetCommentarise()
            # On signale a l editeur du panel (le JDCDisplay) une modification
            self.editor.initModif()
            self.treeParent.buildChildren()
            self.treeParent.children[pos].select()
            self.treeParent.children[pos].affichePanneau()
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical( self.editor, "TOO BAD",str(e))

    def unCommentIt(self):
    #-------------------------
        """
        Realise la decommentarisation de self
        """
        try :
            pos=self.treeParent.children.index(self)
            commande,nom = self.item.unComment()
            self.editor.initModif()
            self.treeParent.buildChildren()
            self.treeParent.children[pos].select()
            self.treeParent.children[pos].affichePanneau()
        except Exception as e:
            QMessageBox.critical( self.editor, "Erreur !",str(e))

    def addComment( self, after=True ):
    #-----------------------------------
        """
        Ajoute un commentaire a l'interieur du JDC :
        """
        self.editor.initModif()
        if after:
            pos = 'after'
        else:
            pos = 'before'
        return self.appendBrother( COMMENT, pos )

    def addParameters( self, after=True ):
    #-------------------------------------
        """
        Ajoute un parametre a l'interieur du JDC :
        """
        self.editor.initModif()
        if after: pos = 'after'
        else: pos = 'before'
        child=self.appendBrother( PARAMETERS, pos )
        return  child


    def select( self ):
    #------------------
        """
        Rend le noeud courant (self) selectionne et deselectionne
        tous les autres
        """
        #print "select pour", self.item.nom
        for item in self.tree.selectedItems() :
            item.setSelected(0)
        self.tree.setCurrentItem( self )

    #------------------------------------------------------------------
    # Methodes de creation et destruction de noeuds
    #------------------------------------------------------------------

    def appendBrother(self,name,pos='after',plier=False):
    #----------------------------------------------------
        """
        Permet d'ajouter un objet frere a l'objet associe au noeud self
        par defaut on l'ajoute immediatement apres
        Methode externe
        """
        self.editor.initModif()

        from InterfaceQT4 import compojdc
        if (isinstance(self.treeParent, compojdc.Node)) and not self.verifiePosition(name,pos)  : return 0

        if self.treeParent != self.vraiParent :
            index = self.vraiParent.children.index(self)
            if   pos == 'before' : index = index
            elif pos == 'after'  : index = index +1
            return self.vraiParent.appendChild(name,pos=index,plier=plier)
        else :
            index = self.treeParent.children.index(self)
            if   pos == 'before': index = index
            elif pos == 'after' : index = index +1
            else:
                print(pos, tr("  n'est pas un index valide pour appendBrother"))
                return 0
            return self.treeParent.appendChild(name,pos=index,plier=plier)

    def verifiePosition(self,name,pos,aLaRacine=False):
    #----------------------------------------------------
        if name not in self.editor.readercata.Classement_Commandes_Ds_Arbre : return True
        indexName=self.editor.readercata.Classement_Commandes_Ds_Arbre.index(name)

        etapes=self.item.getJdc().etapes
        if etapes == [] : return True

        if aLaRacine == False :indexOu=etapes.index(self.item.object)
        else : indexOu=0

        if pos=="after" : indexOu = indexOu+1
        for e in etapes[:indexOu] :
            nom=e.nom
            if nom not in self.editor.readercata.Classement_Commandes_Ds_Arbre : continue
            indexEtape=self.editor.readercata.Classement_Commandes_Ds_Arbre.index(nom)
            if indexEtape > indexName :
                comment=tr('le mot clef ')+name+tr(' doit etre insere avant ')+nom
                QMessageBox.information( None,tr('insertion impossible'),comment, )
                return False
        for e in etapes[indexOu:] :
            nom=e.nom
            if nom not in self.editor.readercata.Classement_Commandes_Ds_Arbre : continue
            indexEtape=self.editor.readercata.Classement_Commandes_Ds_Arbre.index(nom)
            if indexEtape < indexName :
                comment=tr('le mot clef ')+name+tr(' doit etre insere apres ')+nom
                QMessageBox.information( None,tr('insertion impossible'),comment, )
                return False
        return True

    def appendChild(self,name,pos=None,plier=False):
    #------------------------------------------------
        """
           Methode pour ajouter un objet fils a l'objet associe au noeud self.
           On peut l'ajouter en debut de liste (pos='first'), en fin (pos='last')
           ou en position intermediaire.
           Si pos vaut None, on le place a la position du catalogue.
        """
        #print ("************** appendChild ",self.item.getLabelText(), pos, plier)
        #import traceback
        #traceback.print_stack()


        self.editor.initModif()
        if   pos == 'first'       : index = 0
        elif pos == 'last'        : index = len(self.children)
        elif type(pos)   == int   : index = pos  # position fixee
        elif type(pos)  == object : index = self.item.getIndex(pos) +1 # pos est un item. Il faut inserer name apres pos
        elif type(name) == object : index = self.item.getIndexChild(name.nom)
        else                      : index = self.item.getIndexChild(name)

        # si on essaye d inserer a la racine
        if (isinstance(self.treeParent,JDCTree) and index==0) :
            verifiePosition=self.verifiePosition(name,'first',aLaRacine=True)
            if not verifiePosition : return 0

        self.tree.inhibeExpand = True
        obj = self.item.addItem(name,index) # emet le signal 'add'
        if obj is None : obj=0
        if obj == 0    :return 0

        try :
        #if 1 :
            child = self.children[index]
            if plier == True : child.setPlie()
            else             : child.setDeplie()
        except :
            child=self.children[index]

        try :
            if len(obj) > 1 : self.buildChildren()
        except : pass

        self.tree.inhibeExpand=False
        #print (" fin append child")
        return child

    def deplace(self):
    #-----------------
        self.editor.initModif()
        index = self.treeParent.children.index(self) - 1
        if index < 0 : index =0
        ret=self.treeParent.item.deplaceEntite(self.item.getObject())

    def delete(self):
    #----------------
        """
            Methode externe pour la destruction de l'objet associe au noeud
        """
        self.editor.initModif()
        index = self.vraiParent.children.index(self) - 1
        if index < 0 : index =0

        recalcule=0
        if self.item.nom == "VARIABLE" :
            recalcule=1
            jdc=self.item.jdc

        ret,commentaire=self.vraiParent.item.suppItem(self.item)
        if ret==0 : self.editor.afficheInfos(commentaire,Qt.red)
        else      : self.editor.afficheInfos(commentaire)
        self.treeParent.buildChildren()
        if self.treeParent.childrenComplete : toselect=self.treeParent.childrenComplete[index]
        else                                : toselect=self.treeParent

        if recalcule : jdc.recalculeEtatCorrelation()
        if ret==0 :
            if self.treeParent.childrenComplete :
                notdeleted=self.treeParent.childrenComplete[index+1]
                notdeleted.select()
        else :
            toselect.select()

        from InterfaceQT4 import compojdc
        # cas ou on detruit dans l arbre sans affichage
        if isinstance(self.treeParent,compojdc.Node) :
            toselect.affichePanneau()
        else :
            if self.treeParent.fenetre== None : return
            #print "J appelle reaffiche de browser apres delete"
            self.treeParent.fenetre.reaffiche(toselect)

    def deleteMultiple(self,liste=()):
    #--------------------------------
        """
            Methode externe pour la destruction d une liste de noeud
        """
        from InterfaceQT4 import compojdc
        self.editor.initModif()
        index=9999
        recalcule=0
        jdc=self.treeParent
        parentPosition=jdc
        while not(isinstance(jdc,compojdc.Node)):
            jdc=jdc.treeParent
        for noeud in liste :
            if not( isinstance(noeud.treeParent, compojdc.Node)): continue
            if noeud.item.nom == "VARIABLE" : recalcule=1
            if noeud.treeParent.children.index(noeud) < index : index=noeud.treeParent.children.index(noeud)
        if index < 0 : index =0

        # Cas ou on detruit dans une ETape
        if index == 9999 :
            parentPosition=self.treeParent
            while not(isinstance(parentPosition, compojdc.Node)):
                index=parentPosition.treeParent.children.index(parentPosition)
                parentPosition=parentPosition.treeParent

        for noeud in liste:
            noeud.treeParent.item.suppItem(noeud.item)

        jdc.buildChildren()
        if recalcule : jdc.recalculeEtatCorrelation()
        try    : toselect=parentPosition.children[index]
        except : toselect=jdc
        toselect.select()
        toselect.affichePanneau()
#
#    ------------------------------------------------------------------

    def onValid(self):
    #-----------------
        #print ("onValid pour ", self.item.nom)
        if self.JESUISOFF==1 : return

        if hasattr(self,'fenetre') and self.fenetre:
            try : self.fenetre.setValide()
            except : pass

        # PNPN  lignes suivantes a repenser
        if (self.item.nom == "VARIABLE" or self.item.nom == "DISTRIBUTION") and self.item.isValid():
            self.item.jdc.recalculeEtatCorrelation()
        if hasattr(self.item,'forceRecalcul') : self.forceRecalculChildren(self.item.forceRecalcul)
        self.editor.initModif()

        self.updateNodeValid()
        self.updateNodeLabel()
        self.updateNodeTexte()


    def onAdd(self,object):
    #----------------------
        #print ("onAdd pour ", self.item.nom, object)
        if self.JESUISOFF == 1 : return
        self.editor.initModif()
        self.updateNodes()
        if hasattr(self.item,'jdc'): self.item.jdc.aReafficher=True

    def onSupp(self,object):
    #-----------------------
        #print ("onSup pour ", self.item.nom, object)
        #import traceback
        #traceback.print_stack()
        if self.JESUISOFF==1 : return
        self.editor.initModif()
        self.updateNodes()
        if hasattr(self.item,'jdc'): self.item.jdc.aReafficher=True

    def onRedessine(self):
    #---------------------
        #print ('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!je passe dans onRedessine pour', self.item.nom)
        self.affichePanneau()

    def updateNodeValid(self):
    #-----------------------
        """Cette methode remet a jour la validite du noeud (icone)
           Elle appelle isValid
        """
        repIcon  = self.appliEficas.repIcon
        couleur  = self.item.getIconName()
        monIcone = QIcon(repIcon+"/" + couleur + ".png")
        self.setIcon(0,monIcone)



    def updateNodeLabel(self):
    #-------------------------
        """ Met a jour le label du noeud """
        #print ("NODE updateNodeLabel", self.item.getLabelText())
        labeltext,fonte,couleur = self.item.getLabelText()
        # PNPN a reflechir
        if self.item.nom != tr(self.item.nom) : labeltext = str(tr(self.item.nom)+" :")
        self.setText(0, tr(labeltext))

    def updateNodeLabelInBlack(self):
    #-------------------------------
        if hasattr(self.appliEficas,'noeudColore'):
            self.appliEficas.noeudColore.setForeground(0,Qt.black)
            self.appliEficas.noeudColore.updateNodeLabel

    def updateNodeLabelInBlue(self):
    #-------------------------------
        if hasattr(self.appliEficas,'noeudColore'): self.appliEficas.noeudColore.setForeground(0,Qt.black)
        self.setForeground(0,Qt.blue)
        labeltext,fonte,couleur = self.item.getLabelText()
        if self.item.nom != tr(self.item.nom) : labeltext = str(tr(self.item.nom)+" :")
        self.setText(0, labeltext)
        self.appliEficas.noeudColore=self

    def updatePlusieursNodeLabelInBlue(self,liste):
    #----------------------------------------------
        if hasattr(self.appliEficas,'listeNoeudsColores'):
            for noeud in self.appliEficas.listeNoeudsColores:
                noeud.setTextColor( 0,Qt.black)
                noeud.updateNodeLabel()
        self.appliEficas.listeNoeudsColores=[]
        for noeud in liste :
            noeud.setTextColor( 0,Qt.blue )
            labeltext,fonte,couleur = noeud.item.getLabelText()
            if item.nom != tr(item.nom) : labeltext = str(tr(item.nom)+" :")
            noeud.setText(0, labeltext)
            self.appliEficas.listeNoeudsColores.append(noeud)

    def updateNodeTexteInBlack(self):
    #--------------------------------
        """ Met a jour les noms des SD et valeurs des mots-cles """
        self.setTextColor( 1,Qt.black )
        value = self.item.getText()
        self.setText(1, value)

    def updateNodeTexte(self):
    #----------------------------
        """ Met a jour les noms des SD et valeurs des mots-cles """
        value = self.item.getText()
        self.setText(1, value)


    def updateNodeTexteInBlue(self):
    #--------------------------------
        self.setTextColor( 1,Qt.blue )
        value = self.item.getText()
        self.setText(1, value)

    def updateNodes(self):
    #--------------------------------
        #print 'NODE updateNodes', self.item.getLabelText()
        self.buildChildren()

    def updateValid(self) :
    #----------------------
        """Cette methode a pour but de mettre a jour la validite du noeud
           et de propager la demande de mise a jour a son parent
        """
        #print "NODE updateValid", self.item.getLabelText()
        self.updateNodeValid()
        try   : self.treeParent.updateValid()
        except: pass

    def updateTexte(self):
    #----------------------
        """ Met a jour les noms des SD et valeurs des mots-cles """
        #print "NODE updateTexte", self.item.getLabelText()
        self.updateNodeTexte()
        if self.isExpanded() :
            for child in self.children:
                if child.isHidden() == false : child.updateTexte()


    def forceRecalculChildren(self,niveau):
    #--------------------------------------
        if self.state == 'recalcule' :
            self.state = ""
            return
        self.state='recalcule'
        if hasattr(self.item,'object'):
            self.item.object.state="modified"
        for child in self.children:
            if niveau > 0 : child.forceRecalculChildren(niveau - 1)



    def doPaste(self,node_selected,pos='after'):
    #--------------------------------------------
        """
            Declenche la copie de l'objet item avec pour cible
            l'objet passe en argument : node_selected
        """
        objet_a_copier = self.item.getCopieObjet()
        child=node_selected.doPasteCommande(objet_a_copier,pos)
        if self.editor.fenetreCentraleAffichee : self.editor.fenetreCentraleAffichee.node.affichePanneau()
        self.updateNodeLabelInBlack()
        return child

    def doPasteCommande(self,objet_a_copier,pos='after'):
    #-----------------------------------------------------
        """
          Realise la copie de l'objet passe en argument qui est necessairement
          un onjet
        """
        child=None
        try :
        #if 1 :
            child = self.appendBrother(objet_a_copier,pos)
        except :
            pass
        return child

    def doPastePremier(self,objet_a_copier):
    #---------------------------------------
        """
           Realise la copie de l'objet passe en argument (objet_a_copier)
        """
        objet = objet_a_copier.item.getCopieObjet()
        child = self.appendChild(objet,pos='first')
        return child

    def plieToutEtReafficheSaufItem(self, itemADeplier):
    #---------------------------------------------------
        self.inhibeExpand=True
        from InterfaceQT4 import compojdc
        if (isinstance(self, compojdc.Node)) :
            self.affichePanneau()
            self.inhibeExpand=False
            return
        self.editor.deplier = False
        for item in self.children :
            # il ne faut pas plier les blocs
            from InterfaceQT4 import compobloc
            if (isinstance(item,compobloc.Node)) : continue
            item.setPlie()
            if item==itemADeplier :
                itemADeplier.setDeplie()
        self.affichePanneau()
        self.inhibeExpand=False

    def plieToutEtReaffiche(self):
    #-----------------------------
        #print ('plieToutEtReaffiche', self.item.getNom())
        from InterfaceQT4 import compojdc
        if (isinstance(self, compojdc.Node)) : self.affichePanneau(); return
        self.inhibeExpand=True
        self.editor.deplier = False
        for item in self.children :
            # il ne faut pas plier les blocs
            from InterfaceQT4 import compobloc
            if (isinstance(item,compobloc.Node)) : continue
            item.setPlie()
        self.affichePanneau()
        #print ("fin plieToutEtReaffiche", self.item.getNom())

    def deplieToutEtReaffiche(self):
    #-----------------------------
        self.editor.deplier = True
        for item in self.children :
            item.setDeplie()
        self.affichePanneau()

    def setPlie(self):
    #-----------------
        #print "je mets inhibeExpand a true dans setPlie"
        #print ("je suis dans plieTout", self.item.getNom())
        from . import compojdc
        if self.fenetre == self.editor.fenetreCentraleAffichee  and isinstance(self.treeParent,compojdc.Node):
            return
        self.tree.inhibeExpand=True
        self.tree.collapseItem(self)
        self.setPlieChildren()
        self.tree.inhibeExpand=False
        #print "je mets inhibeExpand a false dans setPlie"


        # on ne plie pas au niveau 1
        #   self.plie=False
        #   for item in self.children :
        #       item.appartientAUnNoeudPlie=False

    def setPlieChildren(self):
    #-----------------------------
        self.plie=True
        from InterfaceQT4 import composimp
        if isinstance(self,composimp.Node) : return
        for c in self.children :
            c.setPlieChildren()
            #print "dans setPlieChildren appartientAUnNoeudPlie=True ", c, c.item.getLabelText()[0]
            c.appartientAUnNoeudPlie=True
            c.plie=True
            #print "dans setPlieChildren plie", c.item.nom
            #  01/2018 PNPN : boucle sur MT __ La ligne suivante ne me semble pas necessaire
            #if not (isinstance(c,composimp.Node)) :c.setExpanded(False)

        # Pour les blocs et les motcles list
        # on affiche un niveau de plus
        from InterfaceQT4 import compobloc
        from InterfaceQT4 import compomclist
        if (isinstance(self,compobloc.Node) or ( isinstance(self,compomclist.Node) and self.item.isMCList())) :
            niveauPere=self.treeParent
            while (isinstance(niveauPere,compobloc.Node) or (isinstance(niveauPere,compomclist.Node) and niveauPere.item.isMCList())) :
                niveauPere=niveauPere.treeParent
            for c in self.children :
                c.appartientAUnNoeudPlie=niveauPere.appartientAUnNoeudPlie
                #print ("dans setPlieChildren appartientAUnNoeudPlie=True ", c, c.item.getLabelText()[0], "mis a la valeur ", niveauPere.appartientAUnNoeudPlie)
                c.setExpanded(False)


    def setDeplie(self):
    #-----------------------------
        #print "dans setPlieChildren pour", self.item.nom
        #print "je mets inhibeExpand a true dans setDeplie"
        self.tree.inhibeExpand=True
        self.plie=False
        self.tree.expandItem(self)
        self.setDeplieChildren()
        self.tree.inhibeExpand=False
        #print "je mets inhibeExpand a false dans setDePlie"

    def setDeplieChildren(self):
    #-----------------------------
        #print "dans setDeplieChildren appartientAUnNoeudPlie=False ", self.item.getLabelText()
        for c in self.children :
            c.setDeplieChildren()
            #print "dans setDeplieChildren ", c.item.nom
            c.appartientAUnNoeudPlie=False
            c.setExpanded(True)
            c.plie=False

    def selectAvant(self):
    #-----------------------------
        i=self.item.jdc.etapes.index(self.item.object)
        try    : cherche=self.item.jdc.etapes[i-1]
        except : cherche=self.item.jdc.etapes[-1]
        node=None
        for i in self.tree.racine.children :
            if i.item.object== cherche  :
                node=i
                break
        if node :
            node.affichePanneau()
            node.select()

    def selectApres(self):
    #---------------------
        i=self.item.jdc.etapes.index(self.item.object)
        try    : cherche=self.item.jdc.etapes[i+1]
        except : cherche=self.item.jdc.etapes[0]
        node=None
        for i in self.tree.racine.children :
            if i.item.object== cherche  :
                node=i
                break
        if node :
            node.affichePanneau()
            node.select()
