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
# Modules Python
import os
import sys
import types
import string
import Pmw
from Tkinter import *

# Modules Eficas
import fontes
from treewidget import Tree
from Objecttreeitem import TreeItem
from Accas import AsException
from Noyau.N_CR import justify_text
from Accas import OPER,PROC,MACRO,FORM
from Accas import FACT,BLOC,SIMP

#
__version__="$Name:  $"
__Id__="$Id: catabrowser.py,v 1.3 2002/09/10 15:59:37 eficas Exp $"
#
class Tableau:
  incr = 10
  def __init__(self,parent,colonnes):
    self.parent = parent
    self.colonnes = colonnes
    self.init()

  def init(self):
    # recherche du nombre maxi de lignes et de colonnes....
    for col in self.colonnes :
      nb_l = 0
      if len(col) > nb_l : nb_l = len(col)
    self.nb_lignes = nb_l
    self.nb_colonnes = len(self.colonnes)
    # initialisation des coordonnées dans le canvas
    self.x0 = self.incr
    self.y0 = self.incr
    self.x = self.x0 + self.incr
    self.y = self.y0 + self.incr

  def affiche(self):    
    self.scrolledcanvas=Pmw.ScrolledCanvas(self.parent,
                                           hull_width=1.,
                                           hull_height=1.,
                                           borderframe=1)
    Pmw.Color.changecolor(self.scrolledcanvas.component('canvas'),background='gray95')
    self.scrolledcanvas.pack(padx=10,pady=10,expand=1, fill="both")
    self.canvas = self.scrolledcanvas.component('canvas')
    self.affiche_colonnes()

  def affiche_colonnes(self):
    for i in range(self.nb_lignes):
      self.affiche_ligne(i)
    self.aligne_colonnes()
    self.trace_traits()
    self.scrolledcanvas.resizescrollregion()

  def get_xy_max(self):
    try:
      x0,y0,xmax,ymax = self.canvas.bbox(ALL)
      return xmax,ymax
    except:
      return None,None
    
  def trace_traits(self):
    xmax,ymax = self.get_xy_max()
    if not xmax : return
    xmax = xmax+self.incr
    ymax = ymax+self.incr
    # trace les traits horizontaux
    for i in range(self.nb_lignes):
      tag_lig = 'ligne_'+`i`
      l_id = self.canvas.find_withtag(tag_lig)
      x0,y0,x1,y1 = self.bbox(l_id)
      self.canvas.create_line(x0-self.incr,y0-self.incr,xmax,y0-self.incr)
    self.canvas.create_line(self.x0,ymax,xmax,ymax)  
    # trace les traits verticaux
    for j in range(self.nb_colonnes):
      tag_col = 'colonne_'+`j`
      l_id = self.canvas.find_withtag(tag_col)
      x0,y0,x1,y1 = self.bbox(l_id)
      self.canvas.create_line(x0-self.incr,y0-self.incr,x0-self.incr,ymax)
    self.canvas.create_line(xmax,self.y0,xmax,ymax)
    
  def bbox(self,l_id):
    x0,y0,x1,y1 = self.canvas.bbox(l_id[0])
    for id in l_id[1:]:
      x2,y2,x3,y3 = self.canvas.bbox(id)
      x0 = min(x2,x0)
      y0 = min(y2,y0)
      x1 = max(x3,x1)
      y1 = max(y3,y1)
    return x0,y0,x1,y1
  
  def affiche_ligne(self,num_lig):
    tag_lig = 'ligne_'+`num_lig`
    num_col = 0
    for col in self.colonnes:
      tag_col = 'colonne_'+`num_col`
      x = 100*num_col+self.x
      id = self.canvas.create_text(x,self.y,
                                   text = justify_text(col[num_lig],cesure=60),
                                   tag=(tag_lig,tag_col),
                                   anchor='nw',
                                   font = fontes.canvas)
      x0,y0,x1,y1 = self.canvas.bbox(id)
      num_col = num_col+1
    l_id = self.canvas.find_withtag(tag_lig)
    x0,y0,x1,y1 = self.bbox(l_id)
    self.y = y1 + 2*self.incr

  def aligne_colonnes(self):
    num_col = 0
    for col in self.colonnes:
      tag_col = 'colonne_'+`num_col`
      l_id = self.canvas.find_withtag(tag_col)
      if not l_id : continue
      x0,y0,x1,y1 = self.bbox(l_id)
      self.move(x1+self.incr,self.colonnes[num_col+1:],num_col+1)
      num_col = num_col+1

  def move(self,x,colonnes,num):
    num_col = num
    for col in colonnes:
      tag_col = 'colonne_'+`num_col`
      l_id = self.canvas.find_withtag(tag_col)
      if not l_id : continue
      x0,y0,x1,y1 = self.canvas.bbox(l_id[0])
      self.canvas.move(tag_col,x+self.incr-x0,0)
      num_col = num_col+1
    
class CATAPanel(Frame) :
  """ Classe servant à créer le panneau représentant l'objet sélectionné dans l'arbre"""
  def __init__(self,parent,panneau,node) :
    self.parent=parent
    self.panneau = panneau
    self.node=node
    Frame.__init__(self,self.panneau)
    self.place(x=0,y=0,relheight=1,relwidth=1)
    self.init()

  def init(self):
    # création du label initial
    label = Label(self,
                  text = 'Attributs de '+self.node.item.labeltext,
                  font = fontes.standard_gras_souligne)
    label.pack(side='top',pady=10)
    # création des listes correspondant aux colonnes du tableau à afficher
    colonne1,colonne2 = self.get_listes()
    # affichage du tableau
    self.tableau = Tableau(self,(colonne1,colonne2))
    self.tableau.affiche()

  def get_listes(self):    
    self.node.item.get_dico_attributs()
    l_cles_attributs = self.node.item.d_attributs.keys()
    l_cles_attributs.sort()
    ind=0
    liste1 = []
    liste2=[]
    for nom_attr in l_cles_attributs :
      valeur = self.node.item.d_attributs[nom_attr]
      if type(valeur) == types.TupleType:
        texte =''
        for elem in valeur:
          if type(elem) == types.ClassType:
            texte = texte + elem.__name__
          else:
            texte = texte + str(elem)
      elif type(valeur) == types.ClassType :
        texte = valeur.__name__
      else:
        texte = str(valeur)
      liste1.append(nom_attr)
      liste2.append(texte)
    return liste1,liste2

class CATAItem(TreeItem):
  panel = CATAPanel
  def __init__(self,appli,labeltext,object,setfunction=None,objet_cata_ordonne = None):
    self.appli = appli
    self.labeltext = labeltext
    self.object=object
    self.setfunction = setfunction
    self.objet_cata_ordonne = objet_cata_ordonne

  def get_dico_fils(self):
    d_fils = {}
    if type(self.object) != types.TupleType:
      for e in dir(self.object):
        cmd = getattr(self.object,e)
        if isCMD(cmd) :
          d_fils[string.strip(cmd.nom)] = cmd
    else:
      for obj in self.object :
        for e in dir(obj):
          cmd = getattr(obj,e)
          if isCMD(cmd) :
            d_fils[string.strip(cmd.nom)] = cmd
    self.d_fils = d_fils

  def get_dico_attributs(self):
    d_attributs ={}
    if type(self.object) == types.TupleType :
      self.d_attributs = d_attributs
      return
    l_noms_attributs = ['nom','op','sd_prod','reentrant','repetable','fr','docu','into','valide_vide','actif',
                        'regles','op_init','niveau','definition','code','niveaux','statut',
                        'defaut','min','max','homo','position','val_min','val_max','condition']
    for nom_attribut in l_noms_attributs :
      if hasattr(self.object,nom_attribut):
        attr = getattr(self.object,nom_attribut)
        d_attributs[nom_attribut] = attr
    self.d_attributs = d_attributs

  def get_liste_mc_ordonnee(self):
    """ Retourne la liste ordonnée (suivant le catalogue) brute des fils
    de l'entite courante """
    if hasattr(self.objet_cata_ordonne,'ordre_mc'):
      return self.objet_cata_ordonne.ordre_mc
    else :
      l=self.objet_cata_ordonne.keys()
      l.sort()
      return l
      
  def GetLabelText(self):
    return self.labeltext,None,None

  def get_fr(self):
    return ''
  
  def isMCList(self):
    return 0
  
  def GetSubList(self):
    sublist=[]
    if not hasattr(self,'d_fils'):
      self.get_dico_fils()
    # on classe les fils dans l'odre du catalogue ...
    l_cles_fils = self.get_liste_mc_ordonnee()
    for k in l_cles_fils :
      if type(self.objet_cata_ordonne) == types.InstanceType :
        objet_cata = self.objet_cata_ordonne.entites[k]
      else :
        objet_cata = self.objet_cata_ordonne.get(k,None)
      item = make_objecttreeitem(self.appli,k + " : ",self.d_fils[k],
                                 objet_cata_ordonne = objet_cata)
      sublist.append(item)
    return sublist

  def GetIconName(self):
    return 'ast-green-square'

  def isactif(self):
    return 1
  
class CMDItem(CATAItem):

  def get_dico_fils(self):
    self.d_fils = self.object.entites

class SIMPItem(CATAItem):
  d_fils={}
  d_attributs={}

  def GetIconName(self):
    return 'ast-green-ball'

  def IsExpandable(self):
    return 0
  
class FACTItem(CMDItem):
  def GetIconName(self):
    return 'ast-green-los'

class BLOCItem(FACTItem): pass

class ATTRIBUTItem(SIMPItem):
  def get_dico_attributs(self):
    self.d_attributs = {}

  def GetSubList(self):
    return []

  def IsExpandable(self):
    return 0

  def GetText(self):
    return self.object

  def GetIconName(self):
    return 'aucune'  

class CataBrowser:
  def __init__(self,parent,appli,cata,item = None):
    self.parent = parent
    self.cata = cata
    self.appli = appli
    self.item = item
    self.init()

  def close(self):
    self.top.destroy()

  def init(self):
    self.nodes={}
    self.top = Pmw.Dialog(self.parent,
                          title = "Visualisation d'un catalogue",
                          buttons=('OK',),
                          command = self.quit)
    self.pane = Pmw.PanedWidget(self.top.component('dialogchildsite'),
                                hull_width = 800,
                                hull_height = 500,
                                orient = 'horizontal')
    self.pane.add('canvas',min = 0.4, max = 0.6, size = 0.5)
    self.pane.add('panel',min = 0.4, max = 0.6, size = 0.5)
    self.pane.pack(expand =1, fill = 'both')
    self.scrolledcanvas = Pmw.ScrolledCanvas(self.pane.pane('canvas'),
                                             hull_width=1.,
                                             hull_height=1.,
                                             borderframe=1)
    Pmw.Color.changecolor(self.scrolledcanvas.component('canvas'),background='gray95')
    self.scrolledcanvas.pack(padx=10,pady=10,expand=1, fill="both")
    if self.item == None :
      self.item = CATAItem(self.appli,"Catalogue",self.cata)
    self.tree = Tree(self.appli,self.item,self.scrolledcanvas,command = self.select_node)
    self.tree.draw()
    self.node = self.tree.node_selected

  def select_node(self,node):
    self.nodes[node]=self.create_panel(node)

  def create_panel(self,node):
    if hasattr(node.item,"panel"):
      return getattr(node.item,"panel")(self,self.pane.pane('panel'),node)
      
  def quit(self,nom_bouton) :
    self.top.destroy()
    
  def settitle(self):
    self.top.wm_title("Browser de catalogue " )
    self.top.wm_iconname("CataBrowser")

 
dispatch = {
    OPER  : CMDItem,
    PROC  : CMDItem,
    MACRO  : CMDItem,
    SIMP : SIMPItem,
    FACT : FACTItem,
    BLOC : BLOCItem,
}

def TYPE(o):
  if isinstance(o,OPER):return OPER
  elif isinstance(o,PROC):return PROC
  elif isinstance(o,MACRO):return MACRO
  elif isinstance(o,FORM):return MACRO
  elif isinstance(o,SIMP):return SIMP
  elif isinstance(o,FACT):return FACT
  elif isinstance(o,BLOC):return BLOC
  else:return type(o)

def make_objecttreeitem(appli,labeltext, object, setfunction=None,objet_cata_ordonne=None):
    t = TYPE(object)
    if dispatch.has_key(t):
      c = dispatch[t]
    else:
      #print 'on a un objet de type :',t,'  ',object
      c = ATTRIBUTItem
    return c(appli,labeltext, object, setfunction = setfunction,objet_cata_ordonne=objet_cata_ordonne)

def isCMD(cmd):
   return isinstance(cmd,OPER) or isinstance(cmd,PROC) or isinstance(cmd,MACRO) or isinstance(cmd,FORM)



