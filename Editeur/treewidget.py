#@ MODIF treewidget Editeur  DATE 02/07/2001   AUTEUR D6BHHJP J.P.LEFEBVRE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
import os,sys,string,re,types
from Tkinter import *


import fontes
import images

#
__version__="$Name: V1_1p1 $"
__Id__="$Id: treewidget.py,v 1.1.1.1 2001/12/04 15:38:23 eficas Exp $"
#

Fonte_Standard = fontes.standard

class Tree :
    def __init__(self,appli,jdc_item,scrolledcanvas,command = None):
        self.item = jdc_item
        self.scrolledcanvas = scrolledcanvas
        self.canvas = self.scrolledcanvas.component('canvas')
        self.canvas.bind("<Key-Prior>", self.page_up)
        self.canvas.bind("<Key-Next>", self.page_down)
        self.canvas.bind("<Key-Up>", self.unit_up)
        self.canvas.bind("<Key-Down>", self.unit_down)             
        self.tree = self
        self.command = command
        self.appli = appli
        self.parent = None
        self.racine = self
        self.node_selected = None
        self.build_children()

    def page_up(self,event):
        event.widget.yview_scroll(-1, "page")
    def page_down(self,event):
        event.widget.yview_scroll(1, "page")
    def unit_up(self,event):
        event.widget.yview_scroll(-1, "unit")
    def unit_down(self,event):
        event.widget.yview_scroll(1, "unit")              

    def build_children(self):
        """ Construit la liste des enfants de self """
        self.children = []
        child = Node(self,self.item,self.command)
        self.children.append(child)
        child.state='expanded'

    def draw(self):
        """ Dessine l'arbre """
        lasty = 8
        x = 5
        for child in self.children:
            child.draw(x,lasty)
            lasty = child.lasty + 15
            child.trace_ligne()
        #self.update()
        self.children[0].select()
        self.resizescrollregion()

    def deselectall_old(self):
        """ d�selectionne tous les �l�ments de l'arbre """
        for child in self.children:
            child.deselect()

    def deselectall(self):
        """ d�selectionne tous les �l�ments de l'arbre """
        if self.node_selected :
            self.node_selected.deselect()
            
    def update(self):
        """ Update tous les �l�ments de l'arbre """
        for child in self.children:
            child.update()

    def resizescrollregion(self):
        self.scrolledcanvas.resizescrollregion()

    def select_next(self,event):
        self.node_selected.select_next()

    def select_previous(self,event):
        self.node_selected.select_previous()

    def full_creation(self,name,index):
        # A changer lorsqu'il y aura plusieurs jdc ouverts en m�me temps
        self.children[0].full_creation(name,index)

    def verif_all(self):
        for child in self.children :
            self.verif_all_children()
            
class Node :
    def __init__(self,parent,item,command=None):
        self.parent = parent
        self.item = item
        self.command = command
        self.tree = self.parent.tree
        self.appli = self.parent.appli
        self.canvas = self.parent.canvas
        self.init()
        #self.build_children()

    def init(self):
        self.state='collapsed'
        self.displayed = 0
        self.selected = 0
        self.x = self.y  =None
        self.lasty = 0
        self.children = None
        self.id = []
        # etape = noeud d'�tape auquel appartient self
        # = self si c'est lui-m�me
        if isinstance(self.parent,Tree) :
            # on est  sur un noeud de JDC
            self.racine=self
            self.etape=None
            self.nature='JDC'
        elif isinstance(self.parent.parent,Tree) :
            # on est sur un noeud d'�tape
            self.racine = self.parent
            self.etape=self
            self.nature = 'ETAPE'
        else :
            # on est sur un noeud de mot-cl�
            self.racine = self.parent.racine
            self.etape=self.parent.etape
            self.nature = 'MOTCLE'

    def build_children(self):
        """ Construit la liste des enfants de self """
        self.children = []
        sublist = self.item._GetSubList()
        if not sublist : return
        for item in sublist :
            child = Node(self,item,self.command)
            self.children.append(child)
            
    #-----------------------------------------------
    # M�thodes de s�lection/d�selection d'un noeud
    #-----------------------------------------------
    
    def select(self, event=None):
        """
        Rend le noeud courant (self) s�lectionn� et d�selectionne
        tous les autres
        """
        if not self.children : self.build_children()
        self.tree.deselectall()
        self.selected = 1
        self.tree.node_selected = self
        if self.command:apply(self.command,(self,))
        self.highlight()
        self.canvas.focus_force()
        #self.make_visible()

    def deselect_old(self, event=None):
        """ D�selectionne self """
        self.selected = 0
        if self.displayed == 1:
            self.dehighlight()
        for child in self.children:
            child.deselect()

    def deselect(self, event=None):
        """ D�selectionne self """
        self.selected = 0
        if self.displayed == 1 : self.dehighlight()
            
    def make_visible(self):
        """ Rend l'objet self visible cad d�place le scroll pour que self soit dans
        la fen�tre de visu"""
        x0,y0,x1,y1 = self.canvas.bbox(ALL)
        self.canvas.yview("moveto",self.y/y1)
        
    def select_next(self,ind=0):
        """ on doit chercher � s�lectionner dans l'ordre:
                - son premier fils s'il est affich�
                - son fr�re cadet s'il existe
                - son oncle (benjamin de son p�re)
                - ... appel r�cursif ...
        """
        if self.state=='expanded' and len(self.children) > ind:
            self.children[ind].select()
        else :
            index = self.parent.children.index(self) + 1
            if isinstance(self.parent,TREE) :
                try:
                    self.children[ind].select()
                except:
                    self.children[0].select()
            else :                
                self.parent.select_next(index)

    def select_previous(self):
        """ on doit d'abord s�lectionner(dans l'ordre) :
             - son fr�re a�n�
             - son p�re
        """
        index = self.parent.children.index(self) + 1
        try :
            self.parent.children[index].select()
        except:
            self.parent.select()
    #-----------------------------------------------
    # M�thodes de recherche d'informations
    #-----------------------------------------------
    def geticonimage(self,name=None):
        """
        Retourne l'image qui doit �tre associ�e � self
        """
        if not name :
            name = self.item.GetIconName()
        if not name or name == 'aucune' :
            return None
        return images.get_image(name)

    def get_nb_children(self):
        """ Retourne le nombre d'enfants affich�s de self """
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
    # M�thodes d'affichage d'un noeud
    #-----------------------------------------------
    def draw(self,x,y):
        """ Permet de tracer le noeud self """
        # le d�but du noeud est en x,y
        self.x = x
        self.y = y
        self.lasty = y
        self.displayed = 1
        self.id=[]
        # choix de l'icone � afficher : + ou -
        if self.item.IsExpandable():
            if self.state == 'expanded':
                iconname = "minusnode"
                callback = self.collapse
            else:
                iconname = "plusnode"
                callback = self.expand
            image = self.geticonimage(name=iconname)
            self.icone_id = self.canvas.create_image(self.x, self.y, image=image)
            self.canvas.tag_bind(self.icone_id, "<1>", callback)
            self.id.append(self.icone_id)
        # cr�ation de la ligne horizontale
        self.ligne_id = self.canvas.create_line(self.x,self.y,self.x+10,self.y)
        self.id.append(self.ligne_id)
        self.canvas.tag_lower(self.ligne_id)
        # affichage de l'icone (carre ,rond, ovale ...) de couleur
        image = self.geticonimage()
        if image != None :
            self.image_id = self.canvas.create_image(self.x+15,self.y,image = image)
            self.canvas.tag_bind(self.image_id,"<1>",self.select)
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

    def drawtext(self):
        """ Affiche les deux zones de texte apr�s l'ic�ne de couleur de l'objet """
        if self.image_id != None :
            textx = self.x + 30
        else:
            textx = self.x + 15
        texty = self.y
        # nom,fonte et couleur de l'objet du noeud � afficher
        labeltext,fonte,couleur = self.item.GetLabelText()
        if labeltext    == ''   : labeltext = '   '
        if fonte        == None : fonte = Fonte_Standard
        if couleur      == None : couleur = 'black'
        # cr�ation du widget label
        self.label = Label(self.canvas,
                           text = labeltext,
                           fg = couleur,
                           bg = 'gray95',
                           font=fonte)
        self.label_id = self.canvas.create_window(textx,texty,window=self.label,anchor='w')
        self.id.append(self.label_id)
        # bindings sur le widget label
        self.label.bind("<1>", self.select)
        self.label.bind("<Enter>",self.enter)
        self.label.bind("<Leave>",self.leave)
        # valeur de cet objet � afficher
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
        """ R�tablit l'affichage normal de self"""
        if hasattr(self,'label'):
            self.label.configure(fg='black',bg='gray95')

    def enter(self,event=None):
        """ Met en surbrillance self et affiche le fr de l'objet """
        self.highlight()
        fr = self.item.get_fr()
        self.appli.affiche_infos(fr)
        
    def leave(self,event=None):
        """ R�tablit l'affichage normal de self et efface le fr de l'objet """
        if not self.selected :
            self.dehighlight()
        self.appli.affiche_infos('')

    def collapse_children(self):
        """ Collapse r�cursivement tous les descendants de self """
        if not self.children : return
        for child in self.children:
            child.state='collapsed'
            child.displayed = 0
            child.collapse_children()
            
    def collapse(self,event = None):
        """ Collapse self et descendants et retrace self """
        nb = self.get_nb_children()
        self.state = 'collapsed'
        self.collapse_children()
        self.efface()
        try:
            self.move(-20*nb)
        except:
            pass
        self.draw(self.x,self.y)
        self.select()
        self.update()

    def expand(self,event = None):
        """ Expanse self et le retrace """
        if not self.item.isactif() : return
        if not self.children : self.build_children()
        self.state = 'expanded'
        nb = self.get_nb_children()
        self.move(20*nb)
        self.efface()
        self.draw(self.x,self.y)
        self.select()
        self.update()

    def redraw(self,nb):
        """ Redessine self :  nb est le d�calage � introduire
            en dessous de self pour le redessiner """
        # nb = nombre d'items de d�calage
        self.move(20*nb)
        # on efface self et on le redessine
        self.efface()
        self.draw(self.x,self.y)
        self.update()
        
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
        if self.state == 'expanded' :
            for child in self.children:
                if child.displayed != 0:
                    child.update_coords()

    def update_icone(self):
        """ Met � jour les ic�nes de tous les noeuds : teste la validit� de l'objet
        Cette m�thode est tr�s lente, trop !!"""
        if self.image_id != None :
            image = self.geticonimage()
            self.canvas.itemconfig(self.image_id,image=image)
        if self.state == 'expanded':
            for child in self.children:
                if child.displayed != 0:
                    child.update_icone()

    def update_texte(self):
        """ Met � jour les noms des SD et valeurs des mots-cl�s """
        text = self.item.GetText()
        if text == None : text = ''
        self.text.configure(text=text)
        if self.state == 'expanded' :
            for child in self.children:
                if child.displayed != 0 : child.update_texte()
        
    def update(self,event=None) :
        """ Classe Node :
            Cette m�thode est appel�e pour demander l update d un noeud 
             d'un jeu de commandes
             Cette demande est transmise au noeud racine (le JDC) qui update
             tout l arbre repr�sentant le jeu de commandes
             Pendant cette mise � jour, on appelle la m�thode isvalid qui
             fera l update de tous les objets d�clar�s modifi�s lors des
             actions pr�c�dentes
             La m�tode isvalid est en g�n�ral appel�e par l interm�diaire de
             update_icone -> geticonimage -> GetIconName
        """
        self.racine.update_coords()
        self.racine.trace_ligne()
        self.racine.update_icone()
        self.racine.update_texte()
        self.tree.resizescrollregion()

    def efface(self):
        """ Efface du canvas les id associ�s � self : cad les siens et ceux
            de ses enfants """
        for id in self.id :
            self.canvas.delete(id)
        if not self.children : return
        for child in self.children:
            child.efface()

    def move(self,dy):
        """ D�place de l'incr�ment dy tous les id en dessous de self """
        # il faut marquer tous les suivants de self
        bbox1 = self.canvas.bbox(ALL)
        self.canvas.dtag(ALL,'move')
        self.canvas.delete('line')
        try:
            self.canvas.addtag_overlapping('move',bbox1[0],self.y +10,bbox1[2],bbox1[3])
        except:
            print self
            print self.item
            print self.item.object
            print self.item.object.definition.label
            print 'y=',self.y
            print 'dy=',dy
        # on d�place tous les items de dy
        self.canvas.move('move',0,dy)
        # il faut r�actualiser la zone de scroll
        self.tree.resizescrollregion()

    def trace_ligne(self):
        """ Dessine les lignes verticales entre fr�res et entre p�re et premier fils"""
        if self.state=='collapsed' : return
        #if self.displayed == 0 : return
        if len(self.children)==0 : return
        # on est bien dans le cas d'un noeud expans� avec enfants ...
        # il faut rechercher l'ordonn�e du dernier fils de self
        y_end = self.children[-1].y
        ligne = self.canvas.create_line(self.x+15,self.y,self.x+15,y_end,tags='line')
        self.canvas.tag_lower(ligne)
        for child in self.children :
            try:
                child.trace_ligne()
            except:
                print child
                print child.item.object

    def make_visible_OBSOLETE(self,nb):
        """ Cette m�thode a pour but de rendre le noeud self (avec tous ses descendants
        affich�s) visible dans le canvas """
        x = self.canvas.canvasx(self.canvas.cget('width'))
        y = self.canvas.canvasy(self.canvas.cget('height'))
        #print 'x,y =',x,y
        x0,y0,x1,y1 = self.canvas.bbox(ALL)
        #print 'x0,y1=',x0,y1
        y_deb = self.y
        nb = self.get_nb_children()
        y_fin = y_deb + 20*nb
        #print 'y_deb,y_fin=',y_deb,y_fin
        
    #------------------------------------------------------------------
    # M�thodes de cr�ation et destruction de noeuds
    # Certaines de ces m�thodes peuvent �tre appel�es depuis l'externe
    #------------------------------------------------------------------
    def replace_node(self,node1,node2):
        """ Remplace le noeud 1 par le noeud 2 dans la liste des enfants de self"""
        index= self.children.index(node1)
        self.delete_node_child(node1)
        self.children.insert(index,node2)
        
    def full_creation(self,name,pos=None):
        """
        Interface avec ACCAS : cr�ation de l'objet de nom name et
        du noeud associ�. Retourne le noeud fils ainsi cr��
        """
        item = self.item.additem(name,pos)
        if item == None or item == 0:
            # impossible d'ajouter le noeud de nom : name
            return 0
        nature = item.get_nature()
        #if nature =="COMMANDE" or nature == "OPERATEUR" or nature == "PROCEDURE":
        if nature in ("COMMANDE","OPERATEUR","PROCEDURE","COMMENTAIRE",
                      "PARAMETRE","COMMANDE_COMMENTARISEE","PARAMETRE_EVAL"):
            # on veut ajouter une commande ou un commentaire ou un param�tre
            # il ne faut pas rechercher un m�me objet d�j� existant
            # � modifier : il faut tester l'attribut 'repetable' 
            enfant = None
        else :
            enfant = self.get_node_fils(item.get_nom())
        if enfant :
            # un fils de m�me nom existe d�j� : on remplace
            # un MCFACT (ou une MCList) par une (autre) MCList
            child = Node(self,item,self.command)
            self.replace_node(enfant,child)
        else :            
            child = Node(self, item,self.command)
            if pos is None:
                self.children.append(child)
            else :
                self.children.insert(pos,child)
        return child

    def append_brother(self,name,pos='after',retour='non'):
        """
        Permet d'ajouter un fr�re � self
        par d�faut on l'ajoute apr�s self
        M�thode externe
        """
        # on veut ajouter le fr�re de nom name directement avant ou apr�s self
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
        Fait appel � la cr�ation compl�te de fils et � la v�rification
        des conditions en fonction du contexte
        Attention : fils peut �tre un nom ou d�j� un object (cas d'une copie)
        """
        if not self.children : self.build_children()
        if pos == None :
            #pos = len(self.children)
            if type(fils) == types.InstanceType:
                pos = self.item.get_index_child(fils.nom)
            else:
                pos = self.item.get_index_child(fils)
        child = self.full_creation(fils,pos)
        if child == 0 :
            # on n'a pas pu cr�er le noeud fils
            return 0
        child.displayed = 1
        self.state = 'expanded'
        if verif == 'oui':
            if not child.children : child.build_children()
            test = child.item.isMCList()
            if test :
                child.children[-1].verif_condition()
            else :
                child.verif_condition()
            self.verif_condition()
        return child
            
    def append_child(self,name,pos=None,verif='oui',retour='non'):
        """
        Permet d'ajouter un fils � self
        on peut l'ajouter en fin de liste (d�faut) ou en d�but
        M�thode externe
        """
        if pos == 'first':
            index = 0
        elif pos == 'last':
            index = len(self.children)
        elif pos != None and type(pos) == types.IntType :
            # on donne la position depuis l'ext�rieur
            # (appel de append_child par append_brother par exemple)
            index = pos
        else :
            if type(name) == types.InstanceType:
                index = self.item.get_index_child(name.nom)
            else:
                index = self.item.get_index_child(name)
        nbold = self.get_nb_children()
        self.state='expanded'
        child = self.append_node_child(name,pos=index)
        if child == 0 :
            # on n'a pas pu cr�er le fils
            return 0
        nbnew = self.get_nb_children()
        self.redraw(nbnew-nbold)
        child.select()
        child.expand()
        #child.make_visible()
        if retour == 'oui': return child

    def delete_node_child(self,child):
        """ Supprime child des enfants de self et les id associ�s """
        child.efface()
        child.displayed = 0
        self.children.remove(child)
        self.canvas.update()
        
    def delete_child(self,child):
        """ 
            Supprime child des enfants de self, tous les id associ�s
            ET l'objet associ� 
        """
        if self.item.suppitem(child.item):
            self.delete_node_child(child)
            return 1
        else :
            return 0
                    
    def delete(self):
        """ M�thode externe pour la destruction du noeud ET de l'objet
            G�re l'update du canvas"""
        if self.parent.item.isMCList():
            pere = self.parent.parent
            nbold = pere.get_nb_children()
            if self.parent.delete_child(self):
                self.parent.traite_mclist()
            if self.item.get_position() == 'global':
                self.etape.verif_all()
            elif self.item.get_position() == 'global_jdc':
                self.racine.verif_all()
            else:
                self.parent.verif_condition()
            nbnew = pere.get_nb_children()
        else:
            pere = self.parent
            nbold = pere.get_nb_children()
            if self.parent.delete_child(self):
                if self.item.get_position() == 'global':
                    self.etape.verif_all()
                elif self.item.get_position() == 'global_jdc':
                    self.racine.verif_all()
                else:
                    self.parent.verif_condition()
            else :
                print 'Erreur dans la destruction de ',self.item.get_nom(),' dans delete'
            nbnew = pere.get_nb_children()
        pere.redraw(nbnew-nbold)

    def copynode(self,node,pos) :
        """ node est le noeud � copier � la position pos de self ( = parent de node) """
        objet_copie = node.item.get_copie_objet()
        child = self.full_creation(node.item,pos)
        child.displayed = node.displayed
        #child.image_id = node.image_id
        #child.label_id = node.label_id
        if child.item.get_nature() == "MCList":
            child.item.object[-1].mc_liste = objet_copie.mc_liste
        else :
            try :
                child.item.object.mc_liste = objet_copie.mc_liste
            except:
                pass
    #--------------------------------------------------------------
    # M�thodes de v�rification du contexte et de validit� du noeud
    #--------------------------------------------------------------
    def traite_mclist(self):
        """ Dans le cas d'une MCList il faut v�rifier qu'elle n'est pas vide
            ou r�duite � un seul �l�ment suite � une destruction
        """
        # self repr�sente une MCList
        if len(self.item) == 0 :
            # la liste est vide : il faut la supprimer
            self.delete()
        elif len(self.item) == 1:
            # il ne reste plus qu'un �l�ment dans la liste
            # il faut supprimer la liste et cr�er directement l'objet
            index = self.parent.children.index(self)
            noeud = self.children[0]
            if self.parent.delete_child(self):
                self.parent.append_node_child(noeud.item,pos=index,verif='non')
            #if self.parent.delete_child(self):
            #    self.parent.copynode(self.children[0],index)
            #else :
            #    print 'erreur dans la destruction de :',self.item.get_nom(),' dans traite_mclist'
        else :
            return

    def verif_all(self):
        self.verif_all_children()
            
    def verif_all_children(self):
        if not self.children : self.build_children()
        if self.nature != 'JDC' :
            self.verif()
        for child in self.children :
            child.verif_all_children()

    def verif(self) :
        """ 
            Lance la v�rification des conditions des blocs de self et le cas
            �ch�ant redessine self 
        """
        nbold = self.get_nb_children()
        test = self.verif_condition()
        nbnew = self.get_nb_children()
        if test != 0 :
            self.redraw(nbnew-nbold)

    def verif_condition(self):
        """
        on lance la v�rification des conditions de chaque bloc de self
        on cr�e ou supprime les noeuds concern�s
        (self est d'un niveau inf�rieur ou �gal � l'ETAPE)
        """
        if self.item.object.__class__.__name__ == 'ETAPE_NIVEAU': return 0
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
        return self.item.verif_condition_bloc()

    def verif_condition_regles(self,l_mc_presents):
        return self.item.verif_condition_regles(l_mc_presents)
    

