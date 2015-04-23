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
import pdb
from PyQt4 import *
from PyQt4.QtGui  import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
from monChoixCommande import MonChoixCommande

class JDCTree( QTreeWidget ):
    def __init__( self, jdc_item, QWParent):        
        #if hasattr(QWParent,'widgetTree') : 
        self.editor	   = QWParent
        self.plie=False
        if self.editor.widgetTree !=None  :
           QTreeWidget.__init__(self, self.editor.widgetTree ) 
           self.editor.verticalLayout_2.addWidget(self)
           if self.editor.enteteQTree=='complet':
                 self.headerItem().setText(0,  "Commande   ")
                 self.headerItem().setText(1, "Concept/Valeur")
           else :
                 self.headerItem().setText(0,  "Commande   ")
           self.setColumnWidth(0,200)
           self.setExpandsOnDoubleClick(False)
           self.setSelectionMode(3)
        else :
           QTreeWidget.__init__(self, None ) 
        self.item          = jdc_item
        self.tree          = self        
        self.appliEficas   = self.editor.appliEficas
        self.childrenComplete=[]
        self.childrenIssusDesBlocs=[]
        self.racine=self.item.itemNode(self,self.item)
 
        self.itemCourrant=None

        self.connect(self, SIGNAL("itemClicked ( QTreeWidgetItem * ,int) "), self.handleOnItem)
        self.connect(self, SIGNAL("itemCollapsed ( QTreeWidgetItem *) "), self.handleCollapsedItem)
        self.connect(self, SIGNAL("itemExpanded ( QTreeWidgetItem *) "), self.handleExpandedItem)

        #PNPNPN verifier dans quel cas on se trouve : affiche l arbre ou la commande
        self.node_selected=self.racine
        self.inhibeExpand=True
        self.expandItem(self.racine)
        self.inhibeExpand=False
        #print "self.editor.afficheCommandesPliees", self.editor.afficheCommandesPliees
        if self.racine.children !=[] :  
           if self.editor.afficheCommandesPliees : self.racine.children[0].plieToutEtReaffiche()
           else : self.racine.children[0].deplieToutEtReaffiche()
           self.racine.children[0].fenetre.donnePremier()
        else : self.racine.affichePanneau()
        #PNPNPN
        #pdb.set_trace()

    def contextMenuEvent(self,event) :
        #print "contextMenuEvent"
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
        #print "handleContextMenu"
        if item == None : return
        if item.existeMenu == 0 : return
        if item.menu == None:
           item.createPopUpMenu()
        if item.menu != None:
           if item.item.get_nom() == "DISTRIBUTION" and item.item.isvalid() :
              item.Graphe.setEnabled(1)
           item.menu.exec_(coord)            
            

    def handleCollapsedItem(self,item):
        #print "dans CollapsedItem", self.inhibeExpand  
        if self.inhibeExpand == True : return
        # On traite le cas de l item non selectionne
        itemParent=item
        while not (hasattr (itemParent,'getPanel2')) : 
           itemParent=itemParent.treeParent 
        if self.tree.node_selected != itemParent : 
             item.setExpanded(False)
             return

        itemParent=item
        item.setPlie()
        item.plieToutEtReaffiche()

    def handleExpandedItem(self,item):
        #print "dans ExpandItem", self.inhibeExpand  
        if self.inhibeExpand == True : return
        #print "apres if"
        itemParent=item
        while not (hasattr (itemParent,'getPanel2')) : 
           if itemParent.plie==True : itemParent.setDeplie()
           itemParent=itemParent.treeParent 
        #print "apres if"
        if self.tree.node_selected != itemParent : 
             item.setExpanded(True)
             #print "je suis la"
             return
        item.deplieToutEtReaffiche()

    def handleOnItem(self,item,int):
        #if (len(self.selectedIndexes())!=2): return
        #print "je passe dans handleOnItem"
        self.inhibeExpand == True 
        self.itemCourrant=item
        itemParent=item
        #print self.itemCourrant
        while not (hasattr (itemParent,'getPanel2')) : 
           if itemParent.plie==True : itemParent.setDeplie()
           itemParent=itemParent.treeParent 
        #print itemParent
        #print itemParent.fenetre
        #print self.editor.afficheCommandesPliees
        if itemParent.fenetre != self.editor.fenetreCentraleAffichee : 
            #print self.editor.afficheCommandesPliees
            if self.editor.afficheCommandesPliees : itemParent.plieToutEtReaffiche()
            else :                                  itemParent.affichePanneau()
        if itemParent!=item and item.fenetre != None: item.fenetre.rendVisible()
        #try :
        if 1:
           fr = item.item.get_fr()
           if self.editor: self.editor.labelCommentaire.setText(unicode(fr))
        #except:
        else :
            pass
        self.inhibeExpand == False 
        #print "je mets inhibeExpand a false handleOnItem"


    def choisitPremier(self,name):
        self.editor.layoutJDCCHOIX.removeWidget(self.racine.fenetre)
        self.racine.fenetre.close()
        new_node=self.racine.append_brother(name,'after')
 
# type de noeud
COMMENT     = "COMMENTAIRE"
PARAMETERS  = "PARAMETRE"
 
class JDCNode(QTreeWidgetItem):
    def __init__( self, treeParent, item):
        #print "creation d'un noeud : ", item, " ",item.nom,"", treeParent, self
        self.a=0
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
        if self.editor.enteteQTree=='complet': mesColonnes <<  name << value
        else : mesColonnes <<  name

        if self.treeParent.plie==True :
            self.plie        = True
            self.appartientAUnNoeudPlie=True
        else :
            self.plie        = False
            self.appartientAUnNoeudPlie = False
        #print "self.plie", self.plie
        #print "self.appartientAUnNoeudPlie", self.appartientAUnNoeudPlie
        #print self.treeParent

        ajoutAuParentduNoeud=0
        from InterfaceQT4 import compobloc
        from InterfaceQT4 import compomclist
        while (isinstance(self.treeParent,compobloc.Node) or ( isinstance(self.treeParent,compomclist.Node) and self.treeParent.item.isMCList())) : 
        #while (isinstance(self.treeParent,compobloc.Node)) :
              self.treeParent=self.treeParent.treeParent
              ajoutAuParentduNoeud=1
        if ajoutAuParentduNoeud :
           treeParent.childrenComplete.append(self)
           self.treeParent.childrenIssusDesBlocs.append(self)
        while (isinstance(self.treeParent,compobloc.Node)) : self.treeParent=self.treeParent.treeParent

        #if isinstance(self,compobloc.Node) : 
        if (isinstance(self,compobloc.Node) or ( isinstance(self,compomclist.Node) and self.item.isMCList())) : 
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
          if self.item.getObject().isBLOC() : 
                self.setExpanded(True) 
                self.plie=False
        except :
          pass


    def build_children(self,posInsertion=10000):
        """ Construit la liste des enfants de self """
        """ Se charge de remettre les noeuds Expanded dans le meme etat """
        #print "*********** build_children ",self.item, self.item.GetLabelText()
        
        listeExpanded=[]
        for item in self.childrenComplete :
            #print dir(item)
            #if item.isExpanded():
            #   if self.childrenComplete.index(item) < posInsertion :
            #      listeExpanded.append(self.childrenComplete.index(item))
            #      print dir(item.item )
            #   else :
            #      listeExpanded.append( self.childrenComplete.index(item) +1)
            self.detruit_les_noeuds_issus_de_blocs(item)
            parent=item.treeParent
            parent.removeChild(item)

        #print listeExpanded
        self.children = []
        self.childrenComplete = []
        sublist = self.item._GetSubList()
        ind=0
        for item in sublist :
            nouvelItem=item.itemNode(self,item)
            self.children.append(nouvelItem)
            #print "         J ajoute ", nouvelItem ,nouvelItem.item.GetLabelText(),"dans" ,self.item.GetLabelText()
            #print item
            #if ind in listeExpanded : nouvelItem.setExpanded(1)
 
            #if ind in listeExpanded : print "plie=0"
            #else 		    : print "plie=1"
            #if ind in listeExpanded : nouvelItem.plie=0
            #else 		    : nouvelItem.plie=1
            #ind=ind+1

        #print "*********** fin build_children ",self.item, self.item.GetLabelText()
        
    def chercheNoeudCorrespondant(self,objSimp):
        sublist = self.item._GetSubList()
        for node in self.childrenComplete:
            if node.item.object==objSimp : return node
        return None

    def affichePanneau(self) :
        #print "dans affichePanneau appel getPanel2", self.item.GetLabelText()
        if self.item.isactif(): 
           itemParent=self
           while not (hasattr (itemParent,'getPanel2')) : 
                itemParent=itemParent.treeParent 
           if itemParent!=self : 
              itemParent.affichePanneau()
              return
           self.fenetre=self.getPanel2()
        else:
            from monInactifPanel import PanelInactif
            self.fenetre = PanelInactif(self,self.editor)
         
        self.editor.widgetCentraleLayout.addWidget(self.fenetre)
        #print "widgetCentraleLayout = ", self.editor.widgetCentraleLayout
        #print "nouvelle fenetre ", self.fenetre, " associee a ", self

        self.editor.anciennefenetre=self.editor.fenetreCentraleAffichee
        #print "ancienne fenetre ", self.editor.anciennefenetre
        self.editor.fenetreCentraleAffichee=self.fenetre
        self.tree.node_selected= self

        if self.editor.anciennefenetre != None : 
           a=self.editor.anciennefenetre.close()
           #print "je ferme ", self.editor.anciennefenetre

        if self.editor.widgetTree !=None  : index=1
        else : index=0

        if self.editor.first :
           self.editor.splitter.setSizes((400,1400,400))
           if not(isinstance(self.fenetre,MonChoixCommande)): self.editor.first=False
        self.tree.inhibeExpand=True
        self.tree.expandItem(self)
        self.select()
        self.tree.inhibeExpand=False
        #print "fin de affichePanneau"
        #print "______________________________"
          

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
        #print "je suis sur select"
        for item in self.tree.selectedItems() :
            item.setSelected(0)
        self.setSelected( True )    
        #self.setExpanded( True )    
        self.tree.setCurrentItem( self )    
        self.tree.node_selected= self
                               
    #------------------------------------------------------------------
    # Methodes de creation et destruction de noeuds
    # Certaines de ces methodes peuvent etre appelees depuis l'externe
    #------------------------------------------------------------------
    def append_brother(self,name,pos='after',plier=False):
        """
        Permet d'ajouter un objet frere a l'objet associe au noeud self
        par defaut on l'ajoute immediatement apres 
        Methode externe
        """
        self.editor.init_modif()
        index = self.treeParent.children.index(self)
        if   pos == 'before': index = index
        elif pos == 'after': index = index +1
        else:
            print unicode(pos), tr("  n'est pas un index valide pour append_brother")
            return 0
        return self.treeParent.append_child(name,pos=index,plier=plier)

    def append_child(self,name,pos=None,plier=False):
        """
           Methode pour ajouter un objet fils a l'objet associe au noeud self.
           On peut l'ajouter en debut de liste (pos='first'), en fin (pos='last')
           ou en position intermediaire.
           Si pos vaut None, on le place a la position du catalogue.
        """
        #print "************** append_child ",self.item.GetLabelText(), plier
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
        self.tree.inhibeExpand=True
        obj=self.item.additem(name,index) #CS_pbruno emet le signal 'add'
        if obj is None:obj=0
        if obj == 0:return 0
        #try :
        #  old_obj = self.item.object.get_child(name.nom,restreint = 'oui')
        #  child=old_obj[-1]
        #  if plier : child.plieToutEtReaffiche()
        #  else     : child.affichePanneau() 
        #  print "dans le 1er Try"
        #else :
        #except:
          # Souci pour gerer les copies des AFFE d'une commande à l autre
        #  try :
        #     child=self.children[index]
        #     if plier == True : child.setPlie()
        #     else             : child.setDeplie() 
        #     print "dans le 2nd Try"
        #  except :
        #     child=self.children[index]
        #     print "dans le except"
        try :
        #if 1:
           child=self.children[index]
           if plier == True : child.setPlie()
           else             : child.setDeplie() 
        except :
           child=self.children[index]
           #print "dans le except"
        self.tree.inhibeExpand=False
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
           #print "J appelle reaffiche de browser apres delete"
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
        #print "dans onAdd" ,self.item 
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


    def plieToutEtReaffiche(self):
        #print "je suis dans plieToutEtReaffiche", self.item.get_nom()
        self.editor.deplier = False
        for item in self.children :
            item.setPlie()
        self.affichePanneau()

    def deplieToutEtReaffiche(self):
        self.editor.deplier = True
        for item in self.children :
            item.setDeplie()
        self.affichePanneau()

    def setPlie(self):
        #print "je mets inhibeExpand a true dans setPlie"
        #print "je suis dans plieTout", self.item.get_nom()
        import compojdc
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
        self.plie=True
        for c in self.children :
            c.setPlieChildren()
            #print "dans setPlieChildren appartientAUnNoeudPlie=True ", c, c.item.GetLabelText()[0]
            c.appartientAUnNoeudPlie=True
            c.plie=True
            c.setExpanded(False)

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
                c.setExpanded(False)

        # on affiche un niveau de plus
        #if isinstance(self,compomclist.Node)  : 
        #if isinstance(self,compobloc.Node)  : 
        #    niveauPere=self.treeParent
        #    while (isinstance(niveauPere,compobloc.Node)):
        #       niveauPere=niveauPere.treeParent
        #    for c in self.children :
        #        c.appartientAUnNoeudPlie=niveauPere.appartientAUnNoeudPlie

    def setDeplie(self):
        #print "je mets inhibeExpand a true dans setDeplie"
        self.tree.inhibeExpand=True
        self.plie=False
        self.tree.expandItem(self)
        self.setDeplieChildren()
        self.tree.inhibeExpand=False
        #print "je mets inhibeExpand a false dans setDePlie"

    def setDeplieChildren(self):
        #print "dans setDeplieChildren appartientAUnNoeudPlie=False ", self.item.GetLabelText()
        for c in self.children :
            c.setDeplieChildren()
            #print "dans setDeplieChildren appartientAUnNoeudPlie=False ", c.item.GetLabelText()
            c.appartientAUnNoeudPlie=False
            c.setExpanded(True)
            c.plie=False
       
    def selectAvant(self):
        i=self.item.jdc.etapes.index(self.item.object)
        try :
           cherche=self.item.jdc.etapes[i-1]
        except :
           cherche=self.item.jdc.etapes[-1]
        node=None
        for i in self.tree.racine.children :
            if i.item.object== cherche  : 
               node=i
               break
        if node : node.affichePanneau()

    def selectApres(self):
        i=self.item.jdc.etapes.index(self.item.object)
        try :
           cherche=self.item.jdc.etapes[i+1]
        except :
           cherche=self.item.jdc.etapes[0]
        node=None
        for i in self.tree.racine.children :
            if i.item.object== cherche  : 
               node=i
               break
        if node : node.affichePanneau()
