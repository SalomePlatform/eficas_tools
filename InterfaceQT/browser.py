# -*- coding: utf-8 -*-
import os,sys,string,re,types,traceback

from qt import *
import utilIcons


class JDCTree( QListView ):
    def __init__( self, jdc_item, parent = None ):        
        QListView.__init__( self, parent )
        
        self.item     = jdc_item
        self.tree     = self        
        self.editor   = parent
        self.racine   = self
        self.node_selected = None
        self.children      = self.build_children()        
        
        self.setCaption(self.trUtf8('Browser'))
        self.setRootIsDecorated(1)
        self.setSorting(-1)
        self.addColumn(self.trUtf8('Commande'))
        self.addColumn(self.trUtf8('Concept/Valeur'))
                
        self.resize(QSize(400,500))
        self.connect(self,SIGNAL('contextMenuRequested(QListViewItem *, const QPoint &, int)'),
                     self.handleContextMenu)

        #self.connect(self, SIGNAL("onItem ( QListViewItem * ) "), self.handleOnItem)
        self.connect(self, SIGNAL("clicked ( QListViewItem * ) "), self.handleOnItem)
        self.connect(self, SIGNAL('mouseButtonPressed(int, QListViewItem*, const QPoint&, int)'),
                     self.handleNommeItem)
        
        
    def handleContextMenu(self,itm,coord,col):
        """
        Private slot to show the context menu of the listview.
        
        @param itm the selected listview item (QListViewItem)
        @param coord the position of the mouse pointer (QPoint)
        @param col the column of the mouse pointer (int)
        """
        try:
            if itm.menu:
                itm.menu.popup(coord)            
        except:
            pass
            
    def handleNommeItem(self,bouton,itm,coord,col):
        """
        PN --> a finir eventuellement pour nommer
        le concept dans l arbre
        """
        try :
            if itm :
               panel=itm.getPanel()
               if panel.node.item.object.get_type_produit() != None :
                  pass
        except:
            pass

    def handleOnItem(self,  item ):
        try :
           fr = item.item.get_fr()
           if self.editor:
              self.editor.affiche_infos(fr)
        except:
            pass
        
    def build_children(self):
        """ Construit la liste des enfants de self """
        children = []
        child = self.item.itemNode(self,self.item)
        children.append(child)
        child.state='expanded'
        return children
        
    def supprime(self):
        """ supprime tous les elements de l'arbre """
        raise RuntimeError, 'Not implemented'
        self.tree = None
        self.racine = None
        self.node_selected = None
        self.item = None
        self.scrolledcanvas = None
        for child in self.children:
            child.supprime()
        self.children=[]
                
    def showEvent(self, event):
        """ QT : pour afficher le 1er niveau d'arborescence de l''arbre"""        
        self.children[0].select()
        
    def update(self):
        """ Update tous les elements de l'arbre """
        for child in self.children:
            child.update()
            
# type de noeud
COMMENT     = "COMMENTAIRE"
PARAMETERS  = "PARAMETRE"

        
class JDCNode(QListViewItem):
    def __init__( self, parent, item, after=None, bold=0):
        """
        Constructor
        
        @param parent parent Browser or BrowserNode
        @param text text to be displayed by this node (string or QString)
        @param after sibling this node is positioned after
        @param bold flag indicating a highlighted font
        """        
        self.item   = item
        self.parent = parent
        self.tree   = self.parent.tree
        self.editor = self.parent.tree.editor
        self.bold   = bold
                        
        name  = self.tree.trUtf8(  str( item.GetLabelText()[0] ) )
        value = self.tree.trUtf8(  str( item.GetText() ) )
        
        if after is None:        
            QListViewItem.__init__(self,parent)            
            self.setText(0, name )
            self.setText(1, value )            
        else:
            QListViewItem.__init__(self,parent, after)
            self.setText(0, name )
            self.setText(1, value)
            
        p = utilIcons.getPixmap(item.GetIconName() + ".gif")
        self.setPixmap(0,p)
        self.setExpandable(item.IsExpandable())
                
        self.connect()    
        self.init()        
        self.createPopUpMenu()
        
        
    def paintCell(self, p, cg, column, width, alignment):
        """
        Overwritten class to set a different text color, if bold is true.
        
        @param p the painter (QPainter)
        @param cg the color group (QColorGroup)
        @param column the column (int)
        @param width width of the cell (int)
        @param alignment alignment of the cell (int)
        """
        _cg = QColorGroup(cg)
        c = _cg.text()
        
        if self.bold and column == 0:
            _cg.setColor(QColorGroup.Text, Qt.red)
            
        QListViewItem.paintCell(self, p, _cg, column, width, alignment)
        
        _cg.setColor(QColorGroup.Text, c)
        
        
    def setOpen(self, o):
        """
        Public slot to set/reset the open state.
        
        @param o flag indicating the open state
        """        
        if o:        
            if not self.children :                
                self.build_children()
            self.selected = 1
            self.tree.node_selected = self            
        else:
            
            for child in self.children:
                self.takeItem(child)
                del child
            self.children = []
        QListViewItem.setOpen(self,o)
	self.tree.setSelected(self,o)
    
     
    #----------------------------------------------------------
    #   interface a implementer par les noeuds derives (debut)
    #----------------------------------------------------------
    def getPanel(self):
        print self.__class__
        return None
        
    def createPopUpMenu(self):
        pass 
        
    #----------------------------------------------------
    #   interface a implementer par les noeuds derives (fin)
    #----------------------------------------------------
    
    def init(self): #CS_pbruno toclean
        self.state='collapsed'
        self.displayed = 0
        self.selected = 0
        self.x = self.y  =None
        self.lasty = 0
        self.children = []
        self.id = []
        if self.parent is self.tree:
           self.racine=self
        else:
           self.racine = self.parent.racine
                      
    def connect(self):
        self.item.connect("add",self.onAdd,())
        self.item.connect("supp",self.onSupp,())
        self.item.connect("valid",self.onValid,())

           
    def commentIt(self):
        """
        Cette methode a pour but de commentariser la commande pointee par self
        """
        # On traite par une exception le cas ou l'utilisateur final cherche a désactiver
        # (commentariser) un commentaire.
        try :
            pos=self.parent.children.index(self)
            commande_comment = self.item.get_objet_commentarise()
            # On signale au parent du panel (le JDCDisplay) une modification
            self.editor.init_modif()
            self.parent.children[pos].select()
        except Exception,e:
            traceback.print_exc()
            QMessageBox.critical( self.parent, "TOO BAD",str(e))
        return
        
    def unCommentIt(self):
        """
        Realise la decommentarisation de self
        """
        try :
            pos=self.parent.children.index(self)
            commande,nom = self.item.uncomment()
            self.editor.init_modif()
            self.parent.children[pos].select()
        except Exception,e:
            QMessageBox.critical( self.editor, "Erreur !",str(e))
            return        
        
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
        self.setOpen( True )    
                               
    #------------------------------------------------------------------
    # Methodes de creation et destruction de noeuds
    # Certaines de ces methodes peuvent etre appelees depuis l'externe
    #------------------------------------------------------------------
    def append_brother(self,name,pos='after',retour='non'):
        """
        Permet d'ajouter un objet frere a l'objet associe au noeud self
        par defaut on l'ajoute immediatement apres 
        Methode externe
        """
        # on veut ajouter le frere de nom name directement avant ou apres self
##       print "*********** append_brother ", self.item.GetLabelText()
        index = self.parent.children.index(self)
        if pos == 'before':
            index = index
        elif pos == 'after':
            index = index +1
        else:
            print str(pos)," n'est pas un index valide pour append_brother"
            return 0
        return self.parent.append_child(name,pos=index)

    def append_child(self,name,pos=None,verif='oui',retour='non'):
        """
           Methode pour ajouter un objet fils a l'objet associe au noeud self.
           On peut l'ajouter en debut de liste (pos='first'), en fin (pos='last')
           ou en position intermediaire.
           Si pos vaut None, on le place a la position du catalogue.
        """
##        print "************** append_child ",self.item.GetLabelText()
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
        #print obj
        if obj is None:obj=0
        if obj == 0:return 0
        #print "append_child",index,self.children
        child=self.children[index]
        child.select()
        return child

    def delete(self):
        """ 
            Methode externe pour la destruction de l'objet associe au noeud
            La mise a jour des noeuds est faite par onSupp sur notification
        """
        self.editor.init_modif()
        index = self.parent.children.index(self) - 1 
        if index < 0 : index =0

        parent=self.parent
        ret=parent.item.suppitem(self.item)
        if ret == 0:return

        brothers=parent.children
        if brothers:
           toselect=brothers[index]
        else:
           toselect=parent
        toselect.select()
        
    #------------------------------------------------------------------
    def onValid(self):        
        self.update_node_valid()
        self.update_node_label()
        self.update_node_texte()
        

    def onAdd(self,objet):        
        #print "NODE onAdd : un objet a ete ajoute aux fils de l'item ",self.item.GetLabelText()
        old_nodes=self.children
        self.update_nodes()
        #self.select()

    def onSupp(self,objet):
        #print "NODE onSupp : un objet a ete supprime des fils de l'item ",self.item.object,objet
        old_nodes=self.children
        self.update_nodes()
        #self.select()
        
    def update_node_valid(self):
        """Cette methode remet a jour la validite du noeud (icone)
           Elle appelle isvalid
        """
        #print 'NODE update_node_valid', self.item.GetLabelText()
        p = utilIcons.getPixmap(self.item.GetIconName() + ".gif")
        self.setPixmap(0,p)

    def update_node_label(self): #CS_pbruno todo
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
        #print "NODE update_nodes ", self.item.GetLabelText()
        self.setOpen( False )
        self.setOpen( True )
        #self.select()
            
    def update_texte(self):
        """ Met a jour les noms des SD et valeurs des mots-cles """
        #print "NODE update_texte", self.item.GetLabelText()
        self.update_node_texte()
        if self.state == 'expanded' :
            for child in self.children:
                if child.displayed != 0 : child.update_texte()
        
    def update_valid(self) :
        """Cette methode a pour but de mettre a jour la validite du noeud
           et de propager la demande de mise a jour a son parent
        """
        #print "NODE update_valid", self.item.GetLabelText()
        #PN a reverifier SVP parent
        self.update_node_valid()
        try :
          self.parent.update_valid()            
        except:
          pass

    def supprime(self):
        #print "NODE supprime",self.item.GetLabelText()
        self.efface_node()
        self.racine = None        
        if not self.children : return
        for child in self.children:
            child.supprime()
        self.children=None    

    def build_children(self):
        """ Construit la liste des enfants de self """        
        #print "NODE : Construit la liste des enfants de", self.item.GetLabelText()
        self.children = []
        sublist = self.item._GetSubList()
        if sublist :            
            last = None
            for item in sublist :                
                child = item.itemNode(self, item, last)
                last = child
                self.children.append(child)
            
            
    def doPasteCommande(self,objet_a_copier):
        """
          Réalise la copie de l'objet passé en argument qui est nécessairement
          une commande
        """
        parent=self.parent
        #child = parent.item.append_child(objet_a_copier,self.item.getObject())
        child = self.append_brother(objet_a_copier,retour='oui')
        #if child is None:return 0
        return child

    def doPasteMCF(self,objet_a_copier):
        """
           Réalise la copie de l'objet passé en argument (objet_a_copier)
           Il s'agit forcément d'un mot clé facteur
        """
        child = self.append_child(objet_a_copier,pos='first',retour='oui')
        return child


        
    
if __name__=='__main__':
    from qt import *
    

    sys.path[:0]=['..','../Aster','../Aster/Cata' ]

    app = QApplication(sys.argv)
        
    fn      = 'azAster.comm'
    jdcName =  os.path.basename(fn)
    f=open(fn,'r')
    text=f.read()
    f.close()
    print 'text',text

    from autre_analyse_cata import analyse_catalogue
    from Cata import cataSTA8
    cata=cataSTA8
    fic_cata="../../Aster/Cata/cataSTA8/cata.py"
    cata_ordonne ,list_simp_reel = analyse_catalogue(cata)
    
    
    
    j=cata.JdC( procedure=text, cata=cata, nom=jdcName,
                            cata_ord_dico=cata_ordonne )
                            
    j.compile()
    if not j.cr.estvide():
        print j.cr
        sys.exit()
    
    j.exec_compile()
    if not j.cr.estvide():
        print j.cr
        sys.exit()
                            
    from Editeur import comploader
    comploader.charger_composants(QT)    
    from Editeur import Objecttreeitem
    jdc_item=Objecttreeitem.make_objecttreeitem( app, "nom", j)
                
    if jdc_item:                        
        tree = JDCTree( jdc_item, None )                
    
    app.setMainWidget(tree)    
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    tree.show()
            
    res = app.exec_loop()
    sys.exit(res)
    
    
