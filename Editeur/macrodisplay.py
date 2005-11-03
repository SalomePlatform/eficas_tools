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
"""
   Ce module contient la classe MacroDisplay qui realise l'affichage 
   des sous commandes d'une macro sous forme d'arbre
"""
# Modules Python
import types,sys
import Tkinter,Pmw

# Modules EFICAS
import images
import tooltip
import Objecttreeitem
import compojdc
import treewidget
from widgets import Fenetre
from Ihm import CONNECTOR

class MACRO2TreeItem(compojdc.JDCTreeItem):
      pass

class MacroDisplay:
  def __init__(self,appli,macroitem,nom_jdc):
    self.fenetre = Tkinter.Toplevel()
    self.fenetre.configure(width = 800,height=500)
    self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
    self.fenetre.title("Visualisation Macro_Etape")
    self.macroitem=macroitem
    self.jdc=macroitem.object.jdc_aux
    self.nom_jdc=nom_jdc
    self.appli=appli
    self.barre=Tkinter.Frame(self.fenetre,relief="ridge",bd=2)
    self.barre.pack(expand=1,fill=Tkinter.X)
    if self.macroitem.object.fichier_text is not None:
      b=Tkinter.Button(self.barre,image=images.get_image("Zoom24"),command=self.visufile)
      b.pack(side='left')
      tp=tooltip.TOOLTIP(b,"View file")
    self.mainPart=Pmw.ScrolledCanvas(self.fenetre,
                                     hull_width=600,
                                     hull_height=500,
                                     borderframe=1)
    self.canvas=self.mainPart.component('canvas')
    Pmw.Color.changecolor(self.canvas,background='gray95')
    self.mainPart.pack(padx=10,pady=10,fill = 'both', expand = 1)
    self.item=MACRO2TreeItem(self.appli,nom_jdc,self.jdc)
    self.tree = treewidget.Tree(self.appli,self.item,self.mainPart,command=None,rmenu=self.make_rmenu)
    self.tree.draw()
    CONNECTOR.Connect(self.jdc,"close",self.onCloseView,())

  def onCloseView(self):
    self.quit()

  def visufile(self):
    Fenetre(self.appli,titre="Source du fichier inclus",texte=self.macroitem.object.fichier_text)

  def make_rmenu(self,node,event):
      if hasattr(node.item,'rmenu_specs'):
         rmenu = Tkinter.Menu(self.canvas, tearoff=0)
         self.cree_menu(rmenu,node.item.rmenu_specs,node)
         rmenu.tk_popup(event.x_root,event.y_root)

  def cree_menu(self,menu,itemlist,node):
      """
            Ajoute les items du tuple itemlist
            dans le menu menu
      """
      number_item=0
      radio=None
      for item in itemlist:
         number_item=number_item + 1
         if not item :
            menu.add_separator()
         else:
            label,method=item
            if type(method) == types.TupleType:
                 # On a un tuple => on cree une cascade
                 menu_cascade=Tkinter.Menu(menu)
                 menu.add_cascade(label=label,menu=menu_cascade)
                 self.cree_menu(menu_cascade,method,node)
            elif method[0] == '&':
                 # On a une chaine avec & en tete => on cree un radiobouton
                 try:
                    command=getattr(node.item,method[1:])
                    menu.add_radiobutton(label=label,command=lambda a=self.appli,c=command,n=node:c(a,n))
                    if radio == None:radio=number_item
                 except:pass
            else:
                 try:
                    command=getattr(node.item,method)
                    menu.add_command(label=label,command=lambda a=self.appli,c=command,n=node:c(a,n))
                 except:pass
      # Si au moins un radiobouton existe on invoke le premier
      if radio:menu.invoke(radio)

  def quit(self):
    #print "quit",self
    self.tree.supprime()
    self.tree=None
    self.fenetre.destroy()

  #def __del__(self):
  #  print "__del__",self

def makeMacroDisplay(appli,macroitem,nom_item):
  return MacroDisplay(appli,macroitem,nom_item)

import treeitemincanvas

class TREEITEMINCANVAS(treeitemincanvas.TREEITEMINCANVAS):
   def __init__(self,object,nom="",parent=None,appli=None,sel=None,rmenu=None):
      #print "TREEITEMINCANVAS",object
      self.object=object
      self.nom=nom
      self.appli=appli
      self.parent=parent

      self.item=MACRO2TreeItem(self.appli,self.nom,self.object)
      self.canvas=Pmw.ScrolledCanvas(self.parent,borderframe=1,canvas_background='gray95')
      self.canvas.pack(padx=10,pady=10,fill = 'both', expand = 1)
      if not sel:
         def sel(event=None):
            return
      self.tree=treewidget.Tree(self.appli,self.item,self.canvas,command=sel,rmenu=rmenu)
      self.tree.draw()

import jdcdisplay

class MACRODISPLAY(jdcdisplay.JDCDISPLAY):
   def __init__(self,jdc,nom_jdc,appli=None,parent=None):
      #print "MACRODISPLAY",jdc
      self.jdc=jdc
      self.nom_jdc=nom_jdc
      self.fichier=None
      self.panel_courant=None
      self.appli=appli
      self.parent=parent
      self.node_selected = None
      self.modified='n'

      self.pane=Pmw.PanedWidget(self.parent,orient='horizontal')
      self.pane.add('treebrowser',min=0.4,size=0.5)
      self.pane.add('selected',min=0.4)
      self.pane.pack(expand=1,fill='both')
      self.tree=TREEITEMINCANVAS(jdc,nom_jdc,self.pane.pane('treebrowser'),
                 self.appli,self.select_node,self.make_rmenu)

