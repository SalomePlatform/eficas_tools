# -*- coding: utf-8 -*-

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

import string,re
import types,sys,os
import traceback
import typeNode
from PyQt4 import *
from PyQt4.QtGui  import *
from PyQt4.QtCore import *

class JDCTree( QTreeWidget ):
    def __init__( self, jdc_item, QWParent):        
        QListView.__init__( self, QWParent )
        
        self.item          = jdc_item
        self.tree          = self        
        self.editor	   = QWParent
        self.appliEficas   = self.editor.appliEficas
        
        self.setColumnCount(2)
        mesLabels=QStringList()
        mesLabels << self.trUtf8('Commande                   ') << self.trUtf8('Concept/Valeur           ')
        self.setHeaderLabels(mesLabels)
                
        self.setMinimumSize(QSize(600,505))
        self.setColumnWidth(0,300)
        self.itemCourrant=None

        self.connect(self, SIGNAL("itemClicked ( QTreeWidgetItem * ,int) "), self.handleOnItem)
        self.racine=self.item.itemNode(self,self.item)
        self.expandItem(self.racine)
        self.node_selected=self.racine
        self.racine.affichePanneau()


    def contextMenuEvent(self,event) :
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
        if item == None : return
        if item.existeMenu == 0 : return
        if item.menu == None:
           item.createPopUpMenu()
        if item.menu != None:
           if item.item.get_nom() == "DISTRIBUTION" and item.item.isvalid() :
              item.Graphe.setEnabled(1)
           item.menu.exec_(coord)            
            
    def handleOnItem(self,item,int):
        item.affichePanneau()
        self.itemCourrant=item
        try :
           fr = item.item.get_fr()
           if self.editor:
              self.editor.affiche_infos(fr)
        except:
            pass


# type de noeud
COMMENT     = "COMMENTAIRE"
PARAMETERS  = "PARAMETRE"
 
class JDCNode(QTreeWidgetItem):
    def __init__( self, treeParent, item):
        self.item        = item
        self.treeParent  = treeParent
        self.tree        = self.treeParent.tree
        self.editor	 = self.treeParent.editor
        self.appliEficas = treeParent.appliEficas
                        
        name  = self.appliEficas.trUtf8(  str( item.GetLabelText()[0] ) )
        value = self.appliEficas.trUtf8(  str( item.GetText() ) )
        mesColonnes=QStringList()
        mesColonnes <<  name << value
        QTreeWidgetItem.__init__(self,treeParent,mesColonnes)

        RepIcon=QString(self.appliEficas.RepIcon)
        monIcone = QIcon(RepIcon+"/" +self.item.GetIconName() + ".png")
        self.setIcon(0,monIcone)
        self.children = []
        self.build_children()
        self.menu=None
        self.existeMenu=1

        self.item.connect("valid",self.onValid,())
        self.item.connect("supp" ,self.onSupp,())
        self.item.connect("add"  ,self.onAdd,())


    def build_children(self,posInsertion=10000):
        """ Construit la liste des enfants de self """
        """ Se charge de remettre les noeuds Expanded dans le meme etat """
        #print "*********** build_children ", self.item.GetLabelText()
        listeExpanded=[]
        for item in self.children :
            if item.isExpanded():
               if self.children.index(item) < posInsertion :
                  listeExpanded.append(self.children.index(item))
               else :
                  listeExpanded.append( self.children.index(item) +1)
            self.removeChild(item)
        self.children = []
        sublist = self.item._GetSubList()
        ind=0
        for item in sublist :
            nouvelItem=item.itemNode(self,item)
            self.children.append(nouvelItem)
            if ind in listeExpanded : nouvelItem.setExpanded(1)
            ind=ind+1

    def affichePanneau(self) :
        if self.item.isactif():
	    panel=self.getPanel()
        else:
            from monInactifPanel import PanelInactif
            panel = PanelInactif(self,self.editor)
        panel.show()
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
        #print "select -----------> " , self.item.GetLabelText()
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
            print str(pos)," n'est pas un index valide pour append_brother"
            return 0
        return self.treeParent.append_child(name,pos=index)

    def append_child(self,name,pos=None,verif='oui'):
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
        child=self.children[index]
        child.affichePanneau() 
        return child

    def delete(self):
        """ 
            Methode externe pour la destruction de l'objet associe au noeud
        """
        self.editor.init_modif()
        index = self.treeParent.children.index(self) - 1 
        if index < 0 : index =0
        if self.item.nom == "VARIABLE" :
            self.item.jdc.set_Copules_recalcule_etat()

        ret=self.treeParent.item.suppitem(self.item)
        if ret == 0:return

        self.treeParent.build_children()
        brothers=self.treeParent.children
        if brothers:
           toselect=brothers[index]
        else:
           toselect=self.treeParent
        toselect.select()
        toselect.affichePanneau()

#        
#    #------------------------------------------------------------------
    def onValid(self):        
        if self.item.nom == "VARIABLE" and self.item.isvalid():
           self.item.jdc.recalcule_etat_correlation()
        self.editor.init_modif()
        self.update_node_valid()
        self.update_node_label()
        self.update_node_texte()

    def onAdd(self,object):
        #import traceback
        #print traceback.print_stack()
        self.editor.init_modif()
        self.update_nodes()
 
    def onSupp(self,object):
        self.editor.init_modif()
        self.update_nodes()
 

    def update_node_valid(self):
        """Cette methode remet a jour la validite du noeud (icone)
           Elle appelle isvalid
        """
        #print 'NODE update_node_valid', self.item.GetLabelText()
        RepIcon=QString(self.appliEficas.RepIcon)
        monIcone = QIcon(RepIcon+"/" +self.item.GetIconName() + ".png")
        self.setIcon(0,monIcone)

    def update_node_label(self):
        """ Met a jour le label du noeud """
        #print "NODE update_node_label", self.item.GetLabelText()
        labeltext,fonte,couleur = self.item.GetLabelText()
        self.setText(0, labeltext)        
    
    def update_node_texte(self):
        """ Met a jour les noms des SD et valeurs des mots-cles """
        #print "NODE update_node_texte", self.item.GetLabelText()
        value = self.item.GetText()
        self.setText(1, value)

    def update_nodes(self):
        print 'NODE update_nodes', self.item.GetLabelText()
        self.build_children()

    def update_valid(self) :
        """Cette methode a pour but de mettre a jour la validite du noeud
           et de propager la demande de mise a jour a son parent
        """
        print "NODE update_valid", self.item.GetLabelText()
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
        

    def doPaste(self,node_selected):
        """
            Déclenche la copie de l'objet item avec pour cible
            l'objet passé en argument : node_selected
        """
        #print 'je passe dans doPaste'
        objet_a_copier = self.item.get_copie_objet()
        child=node_selected.doPasteCommande(objet_a_copier)
        return child

    def doPasteCommande(self,objet_a_copier):
        """
          Réalise la copie de l'objet passé en argument qui est nécessairement
          une commande
        """
        #print 'je passe dans doPasteCommande'
        try :
          child = self.append_brother(objet_a_copier)
        except :
           pass
        return child

    def doPasteMCF(self,objet_a_copier):
        """
           Réalise la copie de l'objet passé en argument (objet_a_copier)
           Il s'agit forcément d'un mot clé facteur
        """
        #print 'je passe dans doPasteMCF'
        child = self.append_child(objet_a_copier,pos='first',retour='oui')
        return child


if __name__=='__main__':
    from PyQt4 import *
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *
    

#    sys.path[:0]=['..','../Aster','../Aster/Cata' ]

#    app = QApplication(sys.argv)
        
#    fn      = 'azAster.comm'
#    jdcName =  os.path.basename(fn)
#    f=open(fn,'r')
#    text=f.read()
#    f.close()
#    print 'text',text
    print "afaire"
    
#
#    from autre_analyse_cata import analyse_catalogue
#    from Cata import cataSTA8
#    cata=cataSTA8
#    fic_cata="../../Aster/Cata/cataSTA8/cata.py"
#    cata_ordonne ,list_simp_reel = analyse_catalogue(cata)
#    
#    
#    
#    j=cata.JdC( procedure=text, cata=cata, nom=jdcName,
#                            cata_ord_dico=cata_ordonne )
#                            
#    j.compile()
#    if not j.cr.estvide():
#        print j.cr
#        sys.exit()
#    
#    j.exec_compile()
#    if not j.cr.estvide():
#        print j.cr
#        sys.exit()
#                            
#    from Editeur import comploader
#    comploader.charger_composants(QT)    
#    from Editeur import Objecttreeitem
#    jdc_item=Objecttreeitem.make_objecttreeitem( app, "nom", j)
#                
#    if jdc_item:                        
#        tree = JDCTree( jdc_item, None )                
#    
#    app.setMainWidget(tree)    
#    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
#    tree.show()
#            
#    res = app.exec_loop()
#    sys.exit(res)
#    
#    
