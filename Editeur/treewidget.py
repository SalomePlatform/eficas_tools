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
__Id__="$Id: treewidget.py,v 1.29 2005/11/29 17:39:50 eficas Exp $"
#

Fonte_Standard = fontes.standard

class Tree :
    def __init__(self,appli,jdc_item,scrolledcanvas,command = None,rmenu=None):
        self.item = jdc_item
        self.scrolledcanvas = scrolledcanvas
        self.canvas = self.scrolledcanvas.component('canvas')
        self.id_up=self.canvas.bind("<F11>", self.page_up)
        self.id_down=self.canvas.bind("<F12>", self.page_down)
        self.id_um=self.canvas.bind("<Key-Left>", self.mot_up)
        self.id_dm=self.canvas.bind("<Key-Right>", self.mot_down)
        self.id_s=self.canvas.bind("<1>", self.canvas_select)             
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

    def mot_down_force(self):
        self.select_next(None)
        self.canvas.focus_set()

    def mot_up(self,event):
        self.node_selected.select_mot_previous()
        self.canvas.focus_set()

    def mot_up_force(self):
        self.node_selected.select_mot_prev()
        self.canvas.focus_set()

    def deplieReplieNode(self):
        self.node_selected.deplieReplieNode()

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

    def supprime(self):
        """ supprime tous les éléments de l'arbre """
        #print "supprime",self
        self.canvas.unbind("<Key-Prior>",self.id_up)
        self.canvas.unbind("<Key-Next>",self.id_down)
        self.canvas.unbind("<Key-Left>",self.id_um)
        self.canvas.unbind("<Key-Right>",self.id_dm)
        self.canvas.unbind("<1>",self.id_s)             
        self.tree = None
        self.racine = None
        self.node_selected = None
        self.item = None
        self.scrolledcanvas = None
        self.canvas = None
        self.command = None
        self.rmenu=None
        for child in self.children:
            child.supprime()
        self.children=[]

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

    #def __del__(self):
    #   print "__del__",self

            
class Node :
    def __init__(self,parent,item,command=None,rmenu=None):
        self.parent = parent
        self.item = item
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
           
    def connect(self):
        self.item.connect("add",self.onAdd,())
        self.item.connect("supp",self.onSupp,())
        self.item.connect("valid",self.onValid,())

    #def __del__(self):
    #    print "__del__",self

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
        if self.selected and self.command:
           self.command(self)

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
        self.connect()

    def supprime(self):
        #print "supprime",self
        self.efface_node()
        self.racine = None
        self.command = None
        self.rmenu=None
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
              node.update_node_label()
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
	#print "tag_move_nodes",y
        self.canvas.dtag(ALL,'move')
        # on marque tous les ids au dela de y
        x0, y0, x1, y1 = self.canvas.bbox(ALL)
	if y > y1: # pas d'objet a deplacer
	   return
        self.canvas.addtag_overlapping('move',x0,y,x1,y1)

    def move_nodes(self,y,dy):
        """ Déplace de l'incrément dy les noeuds au dela de l'ordonnée y """
	#print "move_nodes",y,dy
	self.tag_move_nodes(y)
        # on déplace tous les items de dy
        self.canvas.move('move',0,dy)

    def draw_node(self,new_node,x,y):
        """ Dessine le noeud new_node en x,y en deplacant les noeuds existants
            en y et au dela
            Retourne la position du premier des noeuds deplaces
        """
	#print "draw_node",new_node,x,y
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
            except :
		if self.parent is self.tree:
		   pass
		else :
                   self.parent.select_next(index)

    def select_mot_prev(self):
        index = self.parent.children.index(self) - 1
	try :
	   if index > -1  :
	      self.parent.children[index].select()
	      if self.parent.children[index].state=="expanded":
		 print len(self.parent.children[index].children)
		 if len(self.parent.children[index].children)!=0 :
		    max=len(self.parent.children[index].children) - 1
	            self.parent.children[index].children[max].select()
		 else :
	            self.parent.children[index].select()
	      else :
	         self.parent.children[index].select()
	   elif self.parent is self.tree:
	      pass
	   else :
              self.parent.select()
        except:
	    if self.parent is self.tree:
		   pass
	    else :
               self.parent.select_previous()

        
    def select_mot_previous(self):
        index = self.parent.children.index(self) - 1
        try :
            if index > -1  :
               self.parent.children[index].select()
	    elif self.parent is self.tree:
	       pass
	    else :
               self.parent.select()
        except:
	    if self.parent is self.tree:
		   pass
	    else :
               self.parent.select_previous()

    def select_previous(self):
        """ on doit d'abord sélectionner(dans l'ordre) :
             - son frère aîné
             - son père
        """
        index = self.parent.children.index(self) - 1
        try :
            self.parent.children[index].select()
        except:
            #self.parent.select()
	    if self.parent is self.tree:
		   pass
	    else :
               self.parent.select_previous()

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

    def deplieReplieNode(self):           
        if self.state == 'expanded':
	   self.collapse()
	else :
	   self.expand_node()

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
        if self.displayed == 0 : return
        # nom,fonte et couleur de l'objet du noeud à afficher
        labeltext,fonte,couleur = self.item.GetLabelText()
        if labeltext    == ''   : labeltext = '   '
        if fonte        == None : fonte = Fonte_Standard
        if couleur      == None : couleur = 'black'
        self.label.configure(text=labeltext,font=fonte)

    def update_node_texte(self):
        """ Met à jour les noms des SD et valeurs des mots-clés """
        if self.displayed == 0 : return
        text = self.item.GetText()
        if text == None : text = ''
        self.text.configure(text=text)

    def update_node_valid(self) :
        """Cette methode remet a jour la validite du noeud (icone)
           Elle appelle isvalid
        """
        if self.displayed == 0 : return
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
        self.racine.update_label_texte()
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

    def delete(self):
        """ 
            Méthode externe pour la destruction de l'objet associé au noeud
            La mise à jour des noeuds est faite par onSupp sur notification
        """
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

