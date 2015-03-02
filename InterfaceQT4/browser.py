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

import string,re
import types,sys,os
import traceback
import typeNode
from PyQt4 import *
from PyQt4.QtGui  import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
from monChoixCommande import MonChoixCommande

class JDCTree( QTreeWidget ):
    def __init__( self, jdc_item, QWParent):        
        #if hasattr(QWParent,'widgetTree') : 
        if QWParent.widgetTree !=None  :
           QTreeWidget.__init__(self, QWParent.widgetTree ) 
           QWParent.verticalLayout_2.addWidget(self)
           self.headerItem().setText(0,  "Commande   ")
           self.headerItem().setText(1, "Concept/Valeur")
           self.setColumnWidth(0,200)
           self.setExpandsOnDoubleClick(False)
           self.setSelectionMode(3)
        else :
           QTreeWidget.__init__(self, None ) 
        self.item          = jdc_item
        self.tree          = self        
        self.editor	   = QWParent
        self.appliEficas   = self.editor.appliEficas
        self.childrenComplete=[]
        self.childrenIssusDesBlocs=[]
        self.racine=self.item.itemNode(self,self.item)
 
        self.itemCourrant=None

        self.connect(self, SIGNAL("itemClicked ( QTreeWidgetItem * ,int) "), self.handleOnItem)
        #self.connect(self, SIGNAL("itemDoubleClicked ( QTreeWidgetItem * ,int) "), self.handleDoubleClickedOnItem)

        #PNPNPN verifier dans quel cas on se trouve : affiche l arbre ou la commande
        self.node_selected=self.racine
        self.expandItem(self.racine)
        if self.racine.children !=[] :  self.racine.children[0].affichePanneau()
        else : self.racine.affichePanneau()


    def contextMenuEvent(self,event) :
        print "contextMenuEvent"
        coord=event.globalPos()
        item= self.currentItem()
        self.handleContextMenu(item,coord)

    def handleContextMenu(self,item,coord):
        """
        Private slot to show the context menu of the listview.
        
        @param itm the selected listview item (QListWidgetItem)
        @param coord the position of the mouse pointer (QPoint)
        Attention : existeMenu permet de savoir si un menu est associe a cet item
        """
        print "handleContextMenu"
        if item == None : return
        if item.existeMenu == 0 : return
        if item.menu == None:
           item.createPopUpMenu()
        if item.menu != None:
           if item.item.get_nom() == "DISTRIBUTION" and item.item.isvalid() :
              item.Graphe.setEnabled(1)
           item.menu.exec_(coord)            
            

    def handleOnItem(self,item,int):
        if (len(self.selectedIndexes())!=2): return
        self.itemCourrant=item
        self.handleDoubleClickedOnItem(item,int)
        #try :
        if 1:
           fr = item.item.get_fr()
           if self.editor: self.editor.labelCommentaire.setText(unicode(fr))
        #except:
        else :
            pass

    def handleDoubleClickedOnItem(self,item,int):
        print "je passe dans handleDoubleClickedOnItem"
        #if item.fenetre == None :
        #   while not (hasattr (item,'getPanel2')) : item=item.treeParent 
        #   item.affichePanneau()
        #   self.expandItem(item)
        #else:
        #   item.fenetre.rendVisible()
        itemParent=item
        while not (hasattr (itemParent,'getPanel2')) : itemParent=item.treeParent 
        itemParent.affichePanneau()
        if itemParent!=item:
           item.fenetre.rendVisible()

    def choisitPremier(self,name):
        self.editor.layoutJDCCHOIX.removeWidget(self.racine.fenetre)
        self.racine.fenetre.close()
        new_node=self.racine.append_brother(name,'after')
 
# type de noeud
COMMENT     = "COMMENTAIRE"
PARAMETERS  = "PARAMETRE"
 
class JDCNode(QTreeWidgetItem):
    def __init__( self, treeParent, item):
        #print "creation d'un noeud : ", item, " ",item.nom,"", treeParent
        self.item        = item
        self.vraiParent  = treeParent
        self.treeParent  = treeParent
        self.tree        = self.treeParent.tree
        self.editor	 = self.treeParent.editor
        self.appliEficas = treeParent.appliEficas
        self.treeParent.childrenIssusDesBlocs=[]
        self.childrenComplete=[]
                        
        from InterfaceQT4 import compocomm
        from InterfaceQT4 import compoparam
        if   (isinstance(self.item,compocomm.COMMTreeItem)) : name=tr("Commentaire")
        elif (isinstance(self.item,compoparam.PARAMTreeItem)) : name=self.appliEficas.trUtf8(str(item.GetLabelText()[0]))
        else:   name  = self.appliEficas.trUtf8(str(tr( item.nom))+" :")
        value = self.appliEficas.trUtf8(str( item.GetText() ) )

        mesColonnes=QStringList()
        mesColonnes <<  name << value

        ajoutAuParentduNoeud=0
        from InterfaceQT4 import compobloc
        while (isinstance(self.treeParent,compobloc.Node)) :
              self.treeParent=self.treeParent.treeParent
              ajoutAuParentduNoeud=1
        if ajoutAuParentduNoeud :
           treeParent.childrenComplete.append(self)
           self.treeParent.childrenIssusDesBlocs.append(self)
        while (isinstance(self.treeParent,compobloc.Node)) : self.treeParent=self.treeParent.treeParent

        if isinstance(self,compobloc.Node) : 
           QTreeWidgetItem.__init__(self,None,mesColonnes)
        else :
           QTreeWidgetItem.__init__(self,self.treeParent,mesColonnes)
           self.treeParent.childrenComplete.append(self)

        self.setToolTip(0,QString(self.item.get_fr()))
        self.setToolTip(1,QString(self.item.get_fr()))

        repIcon=QString(self.appliEficas.repIcon)
        monIcone = QIcon(repIcon+"/" +self.item.GetIconName() + ".png")
        self.setIcon(0,monIcone)

        self.children = []
        self.build_children()
        self.menu=None
        self.existeMenu=1

        self.item.connect("valid",self.onValid,())
        self.item.connect("supp" ,self.onSupp,())
        self.item.connect("add"  ,self.onAdd,())
        self.state=""
        self.fenetre=None
        try :
          if self.item.getObject().isBLOC() : self.setExpanded(True) 
        except :
          pass


    def build_children(self,posInsertion=10000):
        """ Construit la liste des enfants de self """
        """ Se charge de remettre les noeuds Expanded dans le meme etat """
        #print "*********** build_children ",self.item, self.item.GetLabelText()
        
        listeExpanded=[]
        for item in self.childrenComplete :
            #try :
            #  print "              je detruis ",  item.item.GetLabelText() ," parent : ", item.treeParent.item.GetLabelText()
            #except :
            #  print "mot clef fact"
            if item.isExpanded():
               if self.childrenComplete.index(item) < posInsertion :
                  listeExpanded.append(self.childrenComplete.index(item))
               else :
                  listeExpanded.append( self.childrenComplete.index(item) +1)
            self.detruit_les_noeuds_issus_de_blocs(item)
            parent=item.treeParent
            parent.removeChild(item)

        self.children = []
        self.childrenComplete = []
        sublist = self.item._GetSubList()
        ind=0
        for item in sublist :
            nouvelItem=item.itemNode(self,item)
            self.children.append(nouvelItem)
            #print "         J ajoute ", nouvelItem ,nouvelItem.item.GetLabelText(),"dans" ,self.item.GetLabelText()
            if ind in listeExpanded : nouvelItem.setExpanded(1)
            ind=ind+1
        #print "*********** fin build_children ",self.item, self.item.GetLabelText()
        
    def chercheNoeudCorrespondant(self,objSimp):
        sublist = self.item._GetSubList()
        for node in self.childrenComplete:
            if node.item.object==objSimp : return node
        return None

    def affichePanneau(self) :
        if self.item.isactif():
	    panel=self.getPanel2()
        else:
            from monInactifPanel import PanelInactif
            panel = PanelInactif(self,self.editor)
        if hasattr(self,'fenetre') and self.fenetre: 
           self.fenetre.close()
        self.fenetre=panel
        if self.editor.fenetreCentraleAffichee != None : 
           self.editor.fenetreCentraleAffichee.close()
        self.editor.fenetreCentraleAffichee=panel
        if self.editor.widgetTree !=None  : index=1
        else : index=0
        self.editor.widgetCentraleLayout.addWidget(self.fenetre)

        if self.editor.first :
           self.editor.splitter.setSizes((400,1400,400))
           if not(isinstance(self.fenetre,MonChoixCommande)): self.editor.first=False
        self.tree.expandItem(self)
        self.select()
          

    def createPopUpMenu(self):
        #implemente dans les noeuds derives si necessaire
        self.existeMenu = 0

    def commentIt(self):
        """
        Cette methode a pour but de commentariser la commande pointee par self
        """
        # On traite par une exception le cas ou l'utilisateur final cherche a désactiver
        # (commentariser) un commentaire.
        try :
            pos=self.treeParent.children.index(self)
            commande_comment = self.item.get_objet_commentarise()
            # On signale a l editeur du panel (le JDCDisplay) une modification
            self.editor.init_modif()
            self.treeParent.build_children()
            self.treeParent.children[pos].select()
            self.treeParent.children[pos].affichePanneau()
        except Exception,e:
            traceback.print_exc()
            QMessageBox.critical( self.editor, "TOO BAD",str(e))
        
    def unCommentIt(self):
        """
        Realise la decommentarisation de self
        """
        try :
            pos=self.treeParent.children.index(self)
            commande,nom = self.item.uncomment()
            self.editor.init_modif()
            self.treeParent.build_children()
            self.treeParent.children[pos].select()
            self.treeParent.children[pos].affichePanneau()
        except Exception,e:
            QMessageBox.critical( self.editor, "Erreur !",str(e))
        
    def addComment( self, after=True ):
        """
        Ajoute un commentaire a l'interieur du JDC :
        """
        self.editor.init_modif()
        if after:
            pos = 'after'
        else:
            pos = 'before'
        return self.append_brother( COMMENT, pos )
                
    def addParameters( self, after=True ):
        """
        Ajoute un parametre a l'interieur du JDC :
        """
        self.editor.init_modif()
        if after:
            pos = 'after'
        else:
            pos = 'before'
        return self.append_brother( PARAMETERS, pos )
    
    
    def select( self ):
        """
        Rend le noeud courant (self) selectionne et deselectionne
        tous les autres
        """        
        for item in self.tree.selectedItems() :
            item.setSelected(0)
        self.setSelected( True )    
        self.setExpanded( True )    
        self.tree.setCurrentItem( self )    
        self.tree.node_selected= self
                               
    #------------------------------------------------------------------
    # Methodes de creation et destruction de noeuds
    # Certaines de ces methodes peuvent etre appelees depuis l'externe
    #------------------------------------------------------------------
    def append_brother(self,name,pos='after'):
        """
        Permet d'ajouter un objet frere a l'objet associe au noeud self
        par defaut on l'ajoute immediatement apres 
        Methode externe
        """
        #print "*********** append_brother ", self.item.GetLabelText()
        self.editor.init_modif()
        index = self.treeParent.children.index(self)
        if pos == 'before':
            index = index
        elif pos == 'after':
            index = index +1
        else:
            print unicode(pos), tr("  n'est pas un index valide pour append_brother")
            return 0
        return self.treeParent.append_child(name,pos=index)

    def append_child(self,name,pos=None):
        """
           Methode pour ajouter un objet fils a l'objet associe au noeud self.
           On peut l'ajouter en debut de liste (pos='first'), en fin (pos='last')
           ou en position intermediaire.
           Si pos vaut None, on le place a la position du catalogue.
        """
        #print "************** append_child ",self.item.GetLabelText()
        self.editor.init_modif()
        if pos == 'first':
            index = 0
        elif pos == 'last':
            index = len(self.children)
        elif type(pos) == types.IntType :
            # position fixee
            index = pos
        elif type(pos) == types.InstanceType:
            # pos est un item. Il faut inserer name apres pos
            index = self.item.get_index(pos) +1
        elif type(name) == types.InstanceType:
            index = self.item.get_index_child(name.nom)
        else:
            index = self.item.get_index_child(name)
        obj=self.item.additem(name,index) #CS_pbruno emet le signal 'add'
        if obj is None:obj=0
        if obj == 0:return 0
        ## PNPNPN : cas de Map nouvelle version 
        #if 1 :
        try :
          #print "1er Try"
          old_obj = self.item.object.get_child(name.nom,restreint = 'oui')
          child=old_obj[-1]
          child.affichePanneau() 
        #else :
        except:
          # Souci pour gerer les copies des AFFE d'une commande à l autre
          try :
             child=self.children[index]
             child.affichePanneau() 
          except :
             child=self.children[index]
             pass
        return child

    def deplace(self):
        self.editor.init_modif()
        index = self.treeParent.children.index(self) - 1 
        if index < 0 : index =0
        ret=self.treeParent.item.deplaceEntite(self.item.getObject())

    def delete(self):
        """ 
            Methode externe pour la destruction de l'objet associe au noeud
        """
        self.editor.init_modif()
        index = self.vraiParent.children.index(self) - 1 
        if index < 0 : index =0
        recalcule=0
        if self.item.nom == "VARIABLE" :
           recalcule=1
           jdc=self.item.jdc
        ret=self.vraiParent.item.suppitem(self.item)
        self.treeParent.build_children()
        if self.treeParent.childrenComplete : toselect=self.treeParent.childrenComplete[index]
        else: toselect=self.treeParent
        if recalcule : jdc.recalcule_etat_correlation()
        from InterfaceQT4 import compojdc
        # cas ou on detruit dans l arbre sans affichage
        if isinstance(self.treeParent,compojdc.Node) : 
           toselect.affichePanneau()
        else :
           if self.treeParent.fenetre== None : return
           print "J appelle reaffiche de browser apres delete"
           self.treeParent.fenetre.reaffiche(toselect)

    def deleteMultiple(self,liste=()):
        """ 
            Methode externe pour la destruction d une liste de noeud
        """
        from InterfaceQT4 import compojdc 
        self.editor.init_modif()
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

        # Cas ou on détruit dans une ETape
        if index == 9999 : 
              parentPosition=self.treeParent
              while not(isinstance(parentPosition, compojdc.Node)):
                 index=parentPosition.treeParent.children.index(parentPosition)
                 parentPosition=parentPosition.treeParent

        for noeud in liste:
            noeud.treeParent.item.suppitem(noeud.item)

        jdc.build_children()
        if recalcule : jdc.recalcule_etat_correlation()
        try    : toselect=parentPosition.children[index]
        except : toselect=jdc
        toselect.select()
        toselect.affichePanneau()
#        
#    #------------------------------------------------------------------
    def onValid(self):        

        #print "onValid pour ", self.item.nom
        if hasattr(self,'fenetre') and self.fenetre: 
           self.fenetre.setValide()
        if self.item.nom == "VARIABLE" and self.item.isvalid():
           self.item.jdc.recalcule_etat_correlation()
        if hasattr(self.item,'forceRecalcul'):
           self.forceRecalculChildren(self.item.forceRecalcul)
        self.editor.init_modif()
        
        self.update_node_valid()
        self.update_node_label()
        self.update_node_texte()

    def onAdd(self,object):
        #print "onAdd pour ", self.item.nom
        self.editor.init_modif()
        self.update_nodes()
        print "dans onAdd" ,self.item 
        # PN -- non necessaire si item=jdc
        if hasattr(self.item,'jdc'): self.item.jdc.aReafficher=True
 
    def onSupp(self,object):
        #print "onSupp pour ", self.item.nom
        self.editor.init_modif()
        self.update_nodes()
        # PN -- non necessaire si item=jdc
        if hasattr(self.item,'jdc'): self.item.jdc.aReafficher=True
         
    def detruit_les_noeuds_issus_de_blocs(self,bloc):
        from InterfaceQT4 import compobloc
        if (isinstance(bloc,compobloc.Node)) :
           for node in bloc.childrenComplete :
               self.detruit_les_noeuds_issus_de_blocs(node)
               parent=node.treeParent
               #print "je detruit " , node.item.GetLabelText()
               parent.removeChild(node)

    def update_node_valid(self):
        """Cette methode remet a jour la validite du noeud (icone)
           Elle appelle isvalid
        """
        repIcon=QString(self.appliEficas.repIcon)
        monIcone = QIcon(repIcon+"/" +self.item.GetIconName() + ".png")
        self.setIcon(0,monIcone)


    def update_node_label(self):
        """ Met a jour le label du noeud """
        #print "NODE update_node_label", self.item.GetLabelText()
        labeltext,fonte,couleur = self.item.GetLabelText()
        # PNPN a reflechir
        #self.setText(0, labeltext)        
    
    
    def update_node_label_in_blue(self):
        if hasattr(self.appliEficas,'noeudColore'):
           self.appliEficas.noeudColore.setTextColor( 0,Qt.black)
           self.appliEficas.noeudColore.update_node_label()
        self.setTextColor( 0,Qt.blue )
        labeltext,fonte,couleur = self.item.GetLabelText()
        self.setText(0, labeltext)        
        self.appliEficas.noeudColore=self

    def update_plusieurs_node_label_in_blue(self,liste):
        if hasattr(self.appliEficas,'listeNoeudsColores'):
           for noeud in self.appliEficas.listeNoeudsColores:
               noeud.setTextColor( 0,Qt.black)
               noeud.update_node_label()
        self.appliEficas.listeNoeudsColores=[]
        for noeud in liste :
            noeud.setTextColor( 0,Qt.blue )
            labeltext,fonte,couleur = noeud.item.GetLabelText()
            noeud.setText(0, labeltext)        
            self.appliEficas.listeNoeudsColores.append(noeud)

    def update_node_texte_in_black(self):
        """ Met a jour les noms des SD et valeurs des mots-cles """
        self.setTextColor( 1,Qt.black )
        value = self.item.GetText()
        self.setText(1, value)

    def update_node_texte(self):
        """ Met a jour les noms des SD et valeurs des mots-cles """
        value = self.item.GetText()
        self.setText(1, value)

    def update_node_texte_in_blue(self):
        self.setTextColor( 1,Qt.blue )
        value = self.item.GetText()
        self.setText(1, value)

    def update_nodes(self):
        #print 'NODE update_nodes', self.item.GetLabelText()
        self.build_children()

    def update_valid(self) :
        """Cette methode a pour but de mettre a jour la validite du noeud
           et de propager la demande de mise a jour a son parent
        """
        #print "NODE update_valid", self.item.GetLabelText()
        self.update_node_valid()
        try :
          self.treeParent.update_valid()
        except:
          pass
            
    def update_texte(self):
        """ Met a jour les noms des SD et valeurs des mots-cles """
        #print "NODE update_texte", self.item.GetLabelText()
        self.update_node_texte()
        if self.isExpanded() :
            for child in self.children:
                if child.isHidden() == false : child.update_texte()


    def forceRecalculChildren(self,niveau):
        if self.state=='recalcule' : 
           self.state=""
           return
        self.state='recalcule'
        if hasattr(self.item,'object'):
           self.item.object.state="modified"
        for child in self.children:
           if niveau > 0 : child.forceRecalculChildren(niveau - 1)
              
        

    def doPaste(self,node_selected,pos='after'):
        """
            Déclenche la copie de l'objet item avec pour cible
            l'objet passé en argument : node_selected
        """
        #print 'je passe dans doPaste'
        objet_a_copier = self.item.get_copie_objet()
        child=node_selected.doPasteCommande(objet_a_copier,pos)
        return child

    def doPasteCommande(self,objet_a_copier,pos='after'):
        """
          Réalise la copie de l'objet passé en argument qui est nécessairement
          une commande
        """
        child=None
        try :
          child = self.append_brother(objet_a_copier,pos)
        except :
           pass
        return child

    def doPastePremier(self,objet_a_copier):
        """
           Réalise la copie de l'objet passé en argument (objet_a_copier)
        """
        objet = objet_a_copier.item.get_copie_objet()
        child = self.append_child(objet,pos='first')
        return child

    def setPlie(self):
        self.plie=True
        self.setPlieChildren()

    def setPlieChildren(self):
        self.appartientAUnNoeudPlie=True
        for item in self.children :
            item.setPlieChildren()
            

    def setDeplie(self):
        self.plie=False
        self.setDeplieChildren()

    def setDeplieChildren(self):
        self.appartientAUnNoeudPlie=False
        for item in self.children :
            item.setDeplieChildren()
            

       
