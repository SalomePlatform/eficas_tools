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
import os,sys,string,re,types,traceback
from Tkinter import *


import fontes
import images
from Ihm import CONNECTOR

#
__version__="$Name:  $"
__Id__="$Id: treewidget.py,v 1.22 2005/06/01 15:18:16 eficas Exp $"
#

Fonte_Standard = fontes.standard

class Tree :
    def __init__(self,appli,jdc_item,scrolledcanvas,command = None,rmenu=None):
        self.item = jdc_item
        self.scrolledcanvas = scrolledcanvas
        self.canvas = self.scrolledcanvas.component('canvas')
        self.canvas.bind("<Key-Prior>", self.page_up)
        self.canvas.bind("<Key-Next>", self.page_down)
        self.canvas.bind("<Key-Up>", self.unit_up)
        self.canvas.bind("<Key-Down>", self.unit_down)             
        self.canvas.bind("<Key-Left>", self.mot_up)
        self.canvas.bind("<Key-Right>", self.mot_down)
        self.canvas.bind("<1>", self.canvas_select)             
        self.tree = self
        self.command = command
        self.rmenu=rmenu
        self.appli = appli
        self.parent = None
        self.racine = self
        self.node_selected = None
        self.build_children()

    def canvas_select(self,event):
        self.canvas.focus_set()

    def page_up(self,event):
        event.widget.yview_scroll(-1, "page")
    def page_down(self,event):
        event.widget.yview_scroll(1, "page")
    def unit_up(self,event):
        event.widget.yview_scroll(-1, "unit")
    def unit_down(self,event):
        event.widget.yview_scroll(1, "unit")              

    def mot_down(self,event):
        self.select_next(None)
        self.canvas.focus_set()

    def mot_up(self,event):
        self.node_selected.select_mot_previous()
        self.canvas.focus_set()

    def build_children(self):
        """ Construit la liste des enfants de self """
        self.children = []
        child = self.item.itemNode(self,self.item,self.command,self.rmenu)
        self.children.append(child)
        child.state='expanded'

    def draw(self):
        """ Dessine l'arbre """
        lasty = 8
        x = 5
        for child in self.children:
            child.draw(x,lasty)
            lasty = child.lasty + 15
        self.children[0].select()
        self.resizescrollregion()

    def deselectall(self):
        """ déselectionne tous les éléments de l'arbre """
        if self.node_selected :
            self.node_selected.deselect()
            
    def update(self):
        """ Update tous les éléments de l'arbre """
        for child in self.children:
            child.update()

    def update_valid(self) :
        """Cette methode a pour but de mettre a jour la validite du noeud
           et de propager la demande de mise à jour à son parent
        """
        pass

    def resizescrollregion(self):
        x0,y0,x1,y1=self.canvas.bbox(ALL)
        # On ajoute une marge approximativement de la moitié du canvas
        y1=y1+self.canvas.winfo_height()/2
        self.canvas.configure(scrollregion = (x0,y0,x1,y1))

    def select_next(self,event):
        self.node_selected.select_next()
        self.canvas.focus_set()

    def select_previous(self,event):
        self.node_selected.select_previous()

    def full_creation(self,name,index):
        raise "OBSOLETE"
        # A changer lorsqu'il y aura plusieurs jdc ouverts en même temps
        self.children[0].full_creation(name,index)

    def verif_all(self):
        raise "OBSOLETE"
        traceback.print_stack()
        for child in self.children :
            self.verif_all_children()

    def see(self,items):
        x1, y1, x2, y2=apply(self.canvas.bbox, items)
        while x2 > self.canvas.canvasx(0)+self.canvas.winfo_width():
            old=self.canvas.canvasx(0)
            self.canvas.xview_scroll( 1, 'units')
            # avoid endless loop if we can't scroll
            if old == self.canvas.canvasx(0):
                break
        while y2 > self.canvas.canvasy(0)+self.canvas.winfo_height():
            old=self.canvas.canvasy(0)
            self.canvas.yview_scroll( 1, 'units')
            if old == self.canvas.canvasy(0):
                break
        # done in this order to ensure upper-left of object is visible
        while x1 < self.canvas.canvasx(0):
            old=self.canvas.canvasx(0)
            self.canvas.xview_scroll( -1, 'units')
            if old == self.canvas.canvasx(0):
                break
        while y1 < self.canvas.canvasy(0):
            old=self.canvas.canvasy(0)
            self.canvas.yview_scroll( -1, 'units')
            if old == self.canvas.canvasy(0):
                break
            
class Node :
    def __init__(self,parent,item,command=None,rmenu=None):
        self.parent = parent
        self.item = item
        self.connections=[]
        self.connect()

        self.command = command
        self.rmenu=rmenu
        self.tree = self.parent.tree
        self.appli = self.parent.appli
        self.canvas = self.parent.canvas
        self.init()

    def init(self):
        self.state='collapsed'
        self.displayed = 0
        self.selected = 0
        self.x = self.y  =None
        self.lasty = 0
        self.children = None
        self.id = []
        if self.parent is self.tree:
           self.racine=self
        else:
           self.racine = self.parent.racine
           
        # etape = noeud d'étape auquel appartient self
        # = self si c'est lui-même
        #if isinstance(self.parent,Tree) :
            # on est  sur un noeud de JDC
            #self.etape=None
        #elif isinstance(self.parent.parent,Tree) :
            # on est sur un noeud d'étape
            #self.etape=self
        #else :
            # on est sur un noeud de mot-clé
            #self.etape=self.parent.etape

    def reconnect(self):
        self.disconnect()
        self.connect()

    def connect(self):
        self.connections.append(self.item._object)
        CONNECTOR.Connect(self.item._object,"add",self.onAdd,())
        CONNECTOR.Connect(self.item._object,"supp",self.onSupp,())
        CONNECTOR.Connect(self.item._object,"valid",self.onValid,())
        if self.item.object is not self.item._object:
           CONNECTOR.Connect(self.item.object,"add",self.onAdd,())
           CONNECTOR.Connect(self.item.object,"supp",self.onSupp,())
           CONNECTOR.Connect(self.item.object,"valid",self.onValid,())
           self.connections.append(self.item.object)

    def disconnect(self):
        for c in self.connections:
           CONNECTOR.Disconnect(c,"add",self.onAdd,())
           CONNECTOR.Disconnect(c,"supp",self.onSupp,())
           CONNECTOR.Disconnect(c,"valid",self.onValid,())
        self.connections=[]

    def __del__(self):
        """ appele a la destruction du noeud """
        #print "NOEUD DETRUIT",self,self.item.GetLabelText()[0]

    def force_select(self):
        if self.selected:
           # le noeud est selectionné. On force la reconstruction du panel associé
           if self.command:apply(self.command,(None,))
           self.select()

    def onValid(self):
        #print "onValid : l'item a changé de validité ",self.item,self.item.object,self.item.object.isvalid()
        self.update_node_valid()
        self.update_node_label()
        self.update_node_texte()

    def onAdd(self,objet):
        #print "onAdd : un objet a été ajouté aux fils de l'item ",self.item.object,objet
        self.expand_node()
        old_nodes=self.children
        self.update_nodes()
        self.redraw_children(old_nodes)
        self.force_select()

    def onSupp(self,objet):
        #print "onSupp : un objet a été supprimé des fils de l'item ",self.item.object,objet
        self.expand_node()
        old_nodes=self.children
        self.update_nodes()
        self.redraw_children(old_nodes)
        self.force_select()

    def update_nodes(self):
        #print "update_nodes",self
        newnodes=[]
        inodes=iter(self.children)
        sublist=self.item._GetSubList()
        iliste=iter(sublist)

        while(1):
           old_item=item=None
           for node in inodes:
              old_item=node.item
              if old_item in sublist:break
              #print "item supprime",old_item
           for item in iliste:
              if item is old_item:break
              #print "item ajoute",item
              child = item.itemNode(self,item,self.command,self.rmenu)
              newnodes.append(child)

           if old_item is None and item is None:break
           if old_item is item:
              #print "item conserve",item
              newnodes.append(node)

        self.children=newnodes
        self.reconnect()

    def supprime(self):
        self.disconnect()
        self.efface_node()

        #self.label_id=None
        #self.text_id=None
        #self.label=None
        #self.text=None
        #self.image_id=None
        #self.icone_id=None
        #self.etape=None
        ####self.parent=None
        #self.command = None
        #self.rmenu=None
        #self.tree = None
        #self.appli=None
        #self.canvas = None

        if not self.children : return
        for child in self.children:
            child.supprime()
        self.children=None

    def redraw_children(self,old_nodes):
        #print "redraw_children",old_nodes
        #print self.children
        y = self.y + 20
        x = self.x + 15
        supp_nodes=[]

        inodes=iter(old_nodes)
        iliste=iter(self.children)
        # on parcourt la liste des anciens noeuds (node)
        # et la liste des nouveaux noeuds (new_node) en parallele (iterateurs)

        while(1):
           new_node=node=None
           for node in inodes:
              #print "ancien noeud",node
              if node in self.children:break # ancien noeud toujours present
              #print "noeud supprime",node,node.item.GetLabelText()[0]
              dy=node.y-node.lasty -20
              #print "deplacer noeuds",y,dy
              node.move_nodes(y,dy)
              node.supprime()
              #supp_nodes.append(node)

           for new_node in iliste:
              #print "nouveau noeud",new_node
              if new_node in old_nodes: break # nouveau noeud deja present
              #print "noeud ajoute",new_node,new_node.item.GetLabelText()[0]
              y=self.draw_node(new_node,x,y)

           if node is None and new_node is None : break

           if node is new_node: # ancien noeud
              #print "noeud conserve",node
              node.update_label_texte()
              y=y+node.lasty-node.y +20

        self.racine.update_coords()
        self.canvas.delete('line')
        self.racine.trace_ligne()
        self.tree.resizescrollregion()
        # Mettre à 1 pour verifier les cycles entre objets node
        #withCyclops=0
        #if withCyclops:
           #from Misc import Cyclops
           #z = Cyclops.CycleFinder()
           #print supp_nodes
           #for o in supp_nodes:
             #z.register(o)
           #del supp_nodes
           #del o
           #z.find_cycles()
           #z.show_stats()
           #z.show_cycles()

    def tag_move_nodes(self,y):
        """ Marque pour deplacement tous les noeuds au dela de l'ordonnée y """
        self.canvas.dtag(ALL,'move')
        # on marque tous les ids au dela de y
        x0, y0, x1, y1 = self.canvas.bbox(ALL)
        self.canvas.addtag_overlapping('move',x0,y,x1,y1)

    def move_nodes(self,y,dy):
        """ Déplace de l'incrément dy les noeuds au dela de l'ordonnée y """
	self.tag_move_nodes(y)
        # on déplace tous les items de dy
        self.canvas.move('move',0,dy)

    def draw_node(self,new_node,x,y):
        """ Dessine le noeud new_node en x,y en deplacant les noeuds existants
            en y et au dela
            Retourne la position du premier des noeuds deplaces
        """
        self.tag_move_nodes(y)
        #if new_node.item.isactif():
           #new_node.state = 'expanded'
        new_node.state = 'expanded'
        new_node.draw(x,y)
        dy=(new_node.get_nb_children()+1)*20
        #print "deplacer noeuds",y,dy
        self.canvas.move('move',0,dy)
        return new_node.lasty+20

    def build_children(self):
        """ Construit la liste des enfants de self """
        self.children = []
        sublist = self.item._GetSubList()
        if not sublist : return
        for item in sublist :
            child = item.itemNode(self,item,self.command,self.rmenu)
            self.children.append(child)
            
    #-----------------------------------------------
    # Méthodes de sélection/déselection d'un noeud
    #-----------------------------------------------
    
    def select(self, event=None):
        """
        Rend le noeud courant (self) sélectionné et déselectionne
        tous les autres
        """
        #print "SELECT",self
        if not self.children : self.build_children()
        self.tree.deselectall()
        self.selected = 1
        self.tree.node_selected = self
        if self.command:apply(self.command,(self,))
        self.highlight()
        self.make_visible()

    def deselect(self, event=None):
        """ Déselectionne self """
        self.selected = 0
        if self.displayed == 1 : self.dehighlight()
            
    def make_visible(self):
        """ Rend l'objet self visible cad déplace le scroll pour que self soit dans
            la fenêtre de visu
        """
        lchild=self.last_child()
        self.tree.see((self.image_id,lchild.image_id))
        
    def select_next(self,ind=0):
        """ on doit chercher à sélectionner dans l'ordre:
                - son premier fils s'il est affiché
                - son frère cadet s'il existe
                - son oncle (benjamin de son père)
                - ... appel récursif ...
        """
        if self.state=='expanded' and len(self.children) > ind:
            self.children[ind].select()
        else :
            index = self.parent.children.index(self) + 1
            try :
              if isinstance(self.parent,TREE) :
                try:
                    self.children[ind].select()
                except:
                    self.children[0].select()
              else :                
                self.parent.select_next(index)
            except :
                self.parent.select_next(index)

    def select_mot_previous(self):
        index = self.parent.children.index(self) - 1
        try :
            if index > 0  :
               self.parent.children[index].select()
            else :
               self.parent.select()
        except:
            self.parent.select()

    def select_previous(self):
        """ on doit d'abord sélectionner(dans l'ordre) :
             - son frère aîné
             - son père
        """
        index = self.parent.children.index(self) + 1
        try :
            self.parent.children[index].select()
        except:
            self.parent.select()

    def popup(self,event=None):
        """
            Declenche le traitement associé au clic droit de la souris
            sur l'icone du Node
        """
        if not self.rmenu:return
        apply(self.rmenu,(self,event))

    #-----------------------------------------------
    # Méthodes de recherche d'informations
    #-----------------------------------------------
    def geticonimage(self,name=None):
        """
        Retourne l'image qui doit être associée à self
        """
        if not name :
            name = self.item.GetIconName()
        if not name or name == 'aucune' :
            return None
        return images.get_image(name)

    def get_nb_children(self):
        """ Retourne le nombre d'enfants affichés de self """
        nb = 0
        if self.state =='collapsed' :  return nb
        for child in self.children :
            nb = nb + 1 + child.get_nb_children()
        return nb

    def get_liste_id(self):
        """ Retourne la liste de tous les id (filiation comprise) de self """
        liste = self.id
        for child in self.children:
            liste.extend(child.get_liste_id())
        return liste

    def get_node_fils(self,name) :
        """ Retourne le fils de self de nom name s'il existe"""
        for child in self.children:
            if child.item.get_nom() == name: return child
        return None

    #-----------------------------------------------
    # Méthodes d'affichage d'un noeud
    #-----------------------------------------------
    def draw(self,x,y):
        """ Permet de tracer le noeud self """
        # le début du noeud est en x,y
        self.x = x
        self.y = y
        self.lasty = y
        self.displayed = 1
        self.id=[]
        # choix de l'icone à afficher : + ou -
        if self.item.IsExpandable():
            if self.state == 'expanded':
                iconname = "minusnode"
                callback = self.collapse
            else:
                iconname = "plusnode"
                callback = self.expand
            image = self.geticonimage(name=iconname)
            self.icone_id = self.canvas.create_image(self.x, self.y, image=image)
            self.callback_id=self.canvas.tag_bind(self.icone_id, "<1>", callback)
            self.id.append(self.icone_id)
        # création de la ligne horizontale
        self.ligne_id = self.canvas.create_line(self.x,self.y,self.x+10,self.y)
        self.id.append(self.ligne_id)
        self.canvas.tag_lower(self.ligne_id)
        # affichage de l'icone (carre ,rond, ovale ...) de couleur
        image = self.geticonimage()
        if image != None :
            self.image_id = self.canvas.create_image(self.x+15,self.y,image = image)
            self.select_id2=self.canvas.tag_bind(self.image_id,"<1>",self.select)
            self.popup_id2=self.canvas.tag_bind(self.image_id,"<3>",self.popup)
            self.id.append(self.image_id)
        else:
            self.image_id = None
        # affichage du texte : nom de l'objet (ETAPE ou MOT-CLE) et sa valeur
        self.drawtext()
        if self.state == 'expanded' :
            if not self.children : self.build_children()
            if len(self.children) > 0:
                self.drawchildren()
                self.lasty = self.children[-1].lasty
   
    def drawchildren(self):
        """ Dessine les enfants de self """
        y = self.y + 20
        x = self.x + 15
        for child in self.children:
            child.draw(x,y)
            nb = child.get_nb_children()
            y = y + 20*(nb+1)
        self.trace_ligne()

    def drawtext(self):
        """ Affiche les deux zones de texte après l'icône de couleur de l'objet """
        if self.image_id != None :
            textx = self.x + 30
        else:
            textx = self.x + 15
        texty = self.y
        # nom,fonte et couleur de l'objet du noeud à afficher
        labeltext,fonte,couleur = self.item.GetLabelText()
        if labeltext    == ''   : labeltext = '   '
        if fonte        == None : fonte = Fonte_Standard
        if couleur      == None : couleur = 'black'
        # création du widget label
        self.label = Label(self.canvas,
                           text = labeltext,
                           fg = couleur,
                           bg = 'gray95',
                           font=fonte)
        self.label_id = self.canvas.create_window(textx,texty,window=self.label,anchor='w')
        self.id.append(self.label_id)
        # bindings sur le widget label
        self.select_id=self.label.bind("<1>", self.select)
        self.popup_id=self.label.bind("<3>", self.popup)
        self.enter_id=self.label.bind("<Enter>",self.enter)
        self.leave_id=self.label.bind("<Leave>",self.leave)
        # valeur de cet objet à afficher
        x0, y0, x1, y1 = self.canvas.bbox(self.label_id)
        textx = max(x1, 200) + 10
        text = self.item.GetText() or " "
        self.text = Label(self.canvas, text=text,
                            bd=0, padx=2, pady=2,background='gray95',
                            font=fonte)
        if self.selected:
            self.highlight()
        else:
            self.dehighlight()
        self.text_id = self.canvas.create_window(textx, texty,anchor="w", window=self.text)
        self.id.append(self.text_id)
        
    def highlight(self,event=None):
        """ Met en surbrillance self"""
        if hasattr(self,'label'):
            self.label.configure(fg='white',bg='#00008b')
            
    def dehighlight(self,event=None):
        """ Rétablit l'affichage normal de self"""
        if hasattr(self,'label'):
            self.label.configure(fg='black',bg='gray95')

    def enter(self,event=None):
        """ Met en surbrillance self et affiche le fr de l'objet """
        self.highlight()
        fr = self.item.get_fr()
        self.appli.affiche_infos(fr)
        
    def leave(self,event=None):
        """ Rétablit l'affichage normal de self et efface le fr de l'objet """
        if not self.selected :
            self.dehighlight()
        self.appli.affiche_infos('')

    def collapse_children(self):
        """ Collapse récursivement tous les descendants de self """
        if not self.children : return
        for child in self.children:
            child.state='collapsed'
            child.collapse_children()
            
    def collapse(self,event = None):
        """ Collapse self et descendants et retrace self """
        nb = self.get_nb_children()
        self.state = 'collapsed'
        self.collapse_children()
        self.redraw(-nb)
        self.select()
   
    def expand_node(self,event = None):
        """ Expanse self et le retrace """
        if self.state == 'expanded':return
        #if not self.item.isactif() : return
        if not self.children : self.build_children()
        self.state = 'expanded'
        nb = self.get_nb_children()
        self.redraw(nb)

    def expand(self,event = None):
        """ Expanse self et le retrace """
        self.expand_node()
        self.select()

    def redraw(self,nb):
        """ Redessine self :  nb est le décalage à introduire
            en dessous de self pour le redessiner """
        # nb = nombre d'items de décalage
        self.move(20*nb)
        # on efface self et on le redessine
        self.efface()
        self.draw(self.x,self.y)
        # Il n'est pas nécessaire d'appeler update
        # il suffit d'updater les coordonnees et de retracer les lignes
        self.racine.update_coords()
        self.racine.trace_ligne()
        self.update_valid()
        self.tree.resizescrollregion()
        
    def update_coords(self):
        """ Permet d'updater les coordonnes de self et de tous ses enfants"""
        if self.displayed == 0 : return
        if self.image_id != None :
            coords = self.canvas.coords(self.image_id)
            self.x = coords[0]-15
        else:
            coords = self.canvas.coords(self.label_id)
            self.x = coords[0]-15
        self.y = coords[1]
        self.lasty = self.y
        if self.state == 'expanded' :
            for child in self.children:
                if child.displayed != 0:
                    child.update_coords()
                    self.lasty = child.lasty

    def update_icone(self):
        """ Met à jour les icônes de tous les noeuds : teste la validité de l'objet
        Cette méthode est très lente, trop !!"""
        if self.image_id != None :
            image = self.geticonimage()
            self.canvas.itemconfig(self.image_id,image=image)
        if self.state == 'expanded':
            for child in self.children:
                if child.displayed != 0:
                    child.update_icone()

    def update_label_texte(self):
        """ Met a jour le label du noeud et celui de tous ses fils ouverts """
        self.update_node_label()
        if self.state == 'expanded' :
            for child in self.children:
                if child.displayed != 0 : child.update_label_texte()

    def update_texte(self):
        """ Met à jour les noms des SD et valeurs des mots-clés """
        self.update_node_texte()
        if self.state == 'expanded' :
            for child in self.children:
                if child.displayed != 0 : child.update_texte()
        
    def update_node_label(self):
        """ Met a jour le label du noeud """
        # nom,fonte et couleur de l'objet du noeud à afficher
        labeltext,fonte,couleur = self.item.GetLabelText()
        if labeltext    == ''   : labeltext = '   '
        if fonte        == None : fonte = Fonte_Standard
        if couleur      == None : couleur = 'black'
        self.label.configure(text=labeltext,font=fonte)

    def update_node_texte(self):
        """ Met à jour les noms des SD et valeurs des mots-clés """
        text = self.item.GetText()
        if text == None : text = ''
        self.text.configure(text=text)

    def update_node_valid(self) :
        """Cette methode remet a jour la validite du noeud (icone)
           Elle appelle isvalid
        """
        if self.image_id != None :
            image = self.geticonimage()
            self.canvas.itemconfig(self.image_id,image=image)

    def update_valid(self) :
        """Cette methode a pour but de mettre a jour la validite du noeud
           et de propager la demande de mise à jour à son parent
        """
        self.update_node_valid()
        self.parent.update_valid()

    def update(self,event=None) :
        """ Classe Node :
            Cette méthode est appelée pour demander l update d un noeud 
            d'un jeu de commandes
            Cette demande est transmise au noeud racine (le JDC) qui update
            tout l arbre représentant le jeu de commandes
            Pendant cette mise à jour, on appelle la méthode isvalid qui
            fera l update de tous les objets déclarés modifiés lors des
            actions précédentes
            La métode isvalid est en général appelée par l intermédiaire de
            update_icone -> geticonimage -> GetIconName
        """
        #print "update",self
        #traceback.print_stack()
        self.racine.update_coords()
        self.racine.trace_ligne()
        self.racine.update_icone()
        self.racine.update_texte()
        self.tree.resizescrollregion()

    def efface_node(self):
        if self.displayed != 0:
           self.label.unbind("<1>", self.select_id)
           self.label.unbind("<3>", self.popup_id)
           self.label.unbind("<Enter>",self.enter_id)
           self.label.unbind("<Leave>",self.leave_id)
           self.canvas.tag_unbind(self.image_id,"<1>",self.select_id2)
           self.canvas.tag_unbind(self.image_id,"<3>",self.popup_id2)
           if self.item.IsExpandable():
              self.canvas.tag_unbind(self.icone_id, "<1>", self.callback_id)
           self.label.destroy()
           self.text.destroy()

        for id in self.id :
            self.canvas.delete(id)
        self.id=[]
        self.label_id=None
        self.text_id=None
        self.image_id=None
        self.icone_id=None
        self.label=None
        self.text=None
	self.displayed=0

    def efface(self):
        """ Efface du canvas les id associés à self : cad les siens et ceux
            de ses enfants """
        self.efface_node()
        if not self.children : return
        for child in self.children:
            child.efface()

    def move(self,dy):
        """ Déplace de l'incrément dy tous les id en dessous de self """
        # il faut marquer tous les suivants de self
        bbox1 = self.canvas.bbox(ALL)
        self.canvas.dtag(ALL,'move')
        self.canvas.delete('line')
        try:
            self.canvas.addtag_overlapping('move',bbox1[0],self.y +10,bbox1[2],bbox1[3])
        except:
	    print "Erreur dans move :"
            print self
            print self.item
            print self.item.getObject()
            print self.item.getObject().definition.label
            print 'y=',self.y
            print 'dy=',dy
        # on déplace tous les items de dy
        self.canvas.move('move',0,dy)

    def trace_ligne(self):
        """ Dessine les lignes verticales entre frères et entre père et premier fils"""
        if self.state=='collapsed' : return
        if len(self.children)==0 : return
        # on est bien dans le cas d'un noeud expansé avec enfants ...
        # il faut rechercher l'ordonnée du dernier fils de self
        y_end = self.children[-1].y
        ligne = self.canvas.create_line(self.x+15,self.y,self.x+15,y_end,tags='line')
        self.canvas.tag_lower(ligne)
        for child in self.children :
            try:
                child.trace_ligne()
            except:
	        print "Erreur dans trace_ligne :"
                print child
                print child.item.getObject()

    def last_child(self):
        lchild=self
        if self.state == 'expanded' and self.children:
           lchild= self.children[-1].last_child()
        return lchild

    #------------------------------------------------------------------
    # Méthodes de création et destruction de noeuds
    # Certaines de ces méthodes peuvent être appelées depuis l'externe
    #------------------------------------------------------------------
    def replace_node(self,node1,node2):
        """ Remplace le noeud 1 par le noeud 2 dans la liste des enfants de self"""
        raise "OBSOLETE"
        index= self.children.index(node1)
        self.delete_node_child(node1)
        self.children.insert(index,node2)
        
    def replace_enfant(self,item):
        """ Retourne le noeud fils à éventuellement remplacer """
        raise "OBSOLETE"
        return self.get_node_fils(item.get_nom())

    def full_creation(self,name,pos=None):
        """
            Interface avec ACCAS : création de l'objet de nom name et
            du noeud associé. Retourne le noeud fils ainsi créé
        """
        raise "OBSOLETE"
        #print "full_creation",name,pos,self.item
        item = self.item.additem(name,pos)
        if item == None or item == 0:
            # impossible d'ajouter le noeud de nom : name
            return 0

        enfant = self.replace_enfant(item)
        if enfant :
            # un fils de même nom existe déjà : on le remplace
            child = item.itemNode(self,item,self.command,self.rmenu)
            self.replace_node(enfant,child)
        else :            
            child = item.itemNode(self, item,self.command,self.rmenu)
            if pos is None:
                self.children.append(child)
            else :
                self.children.insert(pos,child)
        return child

    def append_brother_BAK(self,name,pos='after',retour='non'):
        """
        Permet d'ajouter un frère à self
        par défaut on l'ajoute après self
        Méthode externe
        """
        raise "OBSOLETE"
        # on veut ajouter le frère de nom name directement avant ou après self
        index = self.parent.children.index(self)
        if pos == 'before':
            index = index
        elif pos == 'after':
            index = index +1
        else:
            print str(pos)," n'est pas un index valide pour append_brother"
            return
        return self.parent.append_child(name,pos=index,retour=retour)
    
    def append_node_child(self,fils,pos=None,verif='oui'):
        """
        Fait appel à la création complète de fils et à la vérification
        des conditions en fonction du contexte
        Attention : fils peut être un nom ou déjà un object (cas d'une copie)
        """
        raise "OBSOLETE"
        if not self.children : self.build_children()
        if pos == None :
            if type(fils) == types.InstanceType:
                pos = self.item.get_index_child(fils.nom)
            else:
                pos = self.item.get_index_child(fils)
        child = self.full_creation(fils,pos)
        if child == 0 :
            # on n'a pas pu créer le noeud fils
            return 0
        self.state = 'expanded'
        child.displayed = 1
        if child.item.isactif():
           child.state = 'expanded'
        if not child.children : child.build_children()
        if verif == 'oui':
           child.verif_condition()
           self.verif_condition()
        return child
            
    def append_brother(self,name,pos='after',retour='non'):
        """
        Permet d'ajouter un objet frère à l'objet associé au noeud self
        par défaut on l'ajoute immédiatement après 
        Méthode externe
        """
        # on veut ajouter le frère de nom name directement avant ou après self
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
           Methode pour ajouter un objet fils à l'objet associé au noeud self.
           On peut l'ajouter en début de liste (pos='first'), en fin (pos='last')
           ou en position intermédiaire.
           Si pos vaut None, on le place à la position du catalogue.
        """
        #print "append_child",self,self.children
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
        obj=self.item.additem(name,index)
        #print obj
        if obj is None:obj=0
        if obj == 0:return 0
        #print "append_child",index,self.children
        child=self.children[index]
        child.select()
        return child

    def append_child_BAK(self,name,pos=None,verif='oui',retour='non'):
        """
        Permet d'ajouter un fils à self
        on peut l'ajouter en fin de liste (défaut) ou en début
        Méthode externe
        """
        raise "OBSOLETE"
        if pos == 'first':
            index = 0
        elif pos == 'last':
            index = len(self.children)
        elif pos != None and type(pos) == types.IntType :
            # on donne la position depuis l'extérieur
            # (appel de append_child par append_brother par exemple)
            index = pos
        elif type(pos) == types.InstanceType:
            # pos est un item. Il faut inserer name apres pos
            index = self.item.get_index(pos) +1
        else :
            if type(name) == types.InstanceType:
                index = self.item.get_index_child(name.nom)
            else:
                index = self.item.get_index_child(name)
        nbold = self.get_nb_children()
        self.state='expanded'
        child = self.append_node_child(name,pos=index)
        if child == 0 :
            # on n'a pas pu créer le fils
            return 0
        nbnew = self.get_nb_children()
        self.redraw(nbnew-nbold)
        child.select()
        if retour == 'oui': return child

    def delete_node_child_BAK(self,child):
        """ Supprime child des enfants de self et les id associés """
        raise "OBSOLETE"
        child.efface()
        self.children.remove(child)
        self.canvas.update()
        
    def delete_child_BAK(self,child):
        """ 
            Supprime child des enfants de self, tous les id associés
            ET l'objet associé 
        """
        raise "OBSOLETE"
        if self.item.suppitem(child.item):
            self.delete_node_child(child)
            return 1
        else :
            return 0
                    
    def delete(self):
        """ 
            Méthode externe pour la destruction de l'objet associé au noeud
            La mise à jour des noeuds est faite par onSupp sur notification
        """
        index = self.parent.children.index(self) - 1 
        if index < 0 : index =0

        ret=self.parent.item.suppitem(self.item)
        if ret == 0:return

        brothers=self.parent.children
        if brothers:
           toselect=brothers[index]
        else:
           toselect=self.parent
        toselect.select()

    def delete_BAK(self):
        """ Méthode externe pour la destruction du noeud ET de l'objet
            Gère l'update du canvas"""
        raise "OBSOLETE"
        pere = self.parent
        nbold = pere.get_nb_children()

	if self.parent.children.index(self) > 0 :
            index = self.parent.children.index(self) - 1 
	else:
	    index=0
        if self.parent.delete_child(self):
            if self.item.get_position() == 'global':
                self.etape.verif_all()
            elif self.item.get_position() == 'global_jdc':
                self.racine.verif_all()
            else:
                self.parent.verif_condition()
        else:
            print 'Erreur dans la destruction de ',self.item.get_nom(),' dans delete'

        nbnew = pere.get_nb_children()
        pere.redraw(nbnew-nbold)

        # Le noeud n'est pas au 1er niveau
        if  pere.parent.parent != None:
            pere.select()
        else:
            enfants = self.parent.children
            try:
              enfants[index].select()
            except :
	      try :
	        enfants[index+1].select()
	      except :
	        # on est avant debut
	        pass

    def doPaste(self,node_selected):
        self.appli.message="Vous ne pouvez copier que des commandes ou des mots-clés facteurs !"
        return 0

    def doPaste_Commande(self,objet_a_copier):
        """
	Réalise la copie de l'objet passé en argument qui est nécessairement
	une commande
	"""
	child = self.append_brother(objet_a_copier,retour='oui')
	return child

    #--------------------------------------------------------------
    # Méthodes de vérification du contexte et de validité du noeud
    #--------------------------------------------------------------
    def verif_all(self):
        raise "OBSOLETE"
        traceback.print_stack()
        self.verif_all_children()
            
    def verif_all_children(self):
        raise "OBSOLETE"
        traceback.print_stack()
        if not self.children : self.build_children()
        self.verif()
        for child in self.children :
            child.verif_all_children()

    def verif(self) :
        """ 
            Lance la vérification des conditions des blocs de self et le cas
            échéant redessine self 
        """
        raise "OBSOLETE"
        traceback.print_stack()
        nbold = self.get_nb_children()
        test = self.verif_condition()
        nbnew = self.get_nb_children()
        if test != 0 :
            self.redraw(nbnew-nbold)

    def verif_condition(self):
        """
        on lance la vérification des conditions de chaque bloc de self
        on crée ou supprime les noeuds concernés
        (self est d'un niveau inférieur ou égal à l'ETAPE)
        """
        raise "OBSOLETE"
        traceback.print_stack()
        test = 0
        l_bloc_arajouter,l_bloc_aenlever = self.verif_condition_bloc()
        if len(l_bloc_arajouter) > 0:
            test = 1
            for mc in l_bloc_arajouter:
                self.append_node_child(mc,verif='non')
        if len(l_bloc_aenlever) > 0:
            test = 1
            for mc in l_bloc_aenlever:
                mocle = self.get_node_fils(mc)
                self.delete_child(mocle)
        l_mc_presents = self.item.get_liste_mc_presents()
        l_mc_arajouter= self.verif_condition_regles(l_mc_presents)
        if len(l_mc_arajouter) > 0:
            test = 1
            for mc in l_mc_arajouter:
                self.append_node_child(mc,verif='non')
        if len(l_mc_arajouter)+len(l_bloc_arajouter)+len(l_bloc_aenlever) != 0 :
            self.verif_condition()
        return test
        
    def verif_condition_bloc(self):
        raise "OBSOLETE"
        traceback.print_stack()
        return self.item.verif_condition_bloc()

    def verif_condition_regles(self,l_mc_presents):
        raise "OBSOLETE"
        traceback.print_stack()
        return self.item.verif_condition_regles(l_mc_presents)
    

