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
import types
import Tkinter,Pmw

# Modules EFICAS
import images
import tooltip
import Objecttreeitem
from widgets import Fenetre

class MACRO2TreeItem(Objecttreeitem.ObjectTreeItem):
  def IsExpandable(self):
    return 1

  def GetText(self):
      return  "    "

  def GetIconName(self):
    if self.object.isvalid():
      return "ast-green-square"
    else:
      return "ast-red-square"

  def keys(self):
    return range(len(self.object.etapes))

  def GetSubList(self):
    sublist=[]
    for key in self.keys():
      liste = self.object.etapes
      try:
        value = liste[key]
      except KeyError:
        continue
      def setfunction(value, key=key, object=liste):
        object[key] = value
      item = self.make_objecttreeitem(self.appli,value.ident() + " : ", value, setfunction)
      sublist.append(item)
    return sublist

  def verif_condition_bloc(self):
      # retourne la liste des sous-items dont la condition est valide
      # sans objet pour le JDC
      return [],[]

  def get_l_noms_etapes(self):
      """ Retourne la liste des noms des étapes de self.object"""
      return self.object.get_l_noms_etapes()

class MacroDisplay:
  def __init__(self,appli,jdc,nom_jdc):
    self.fenetre = Tkinter.Toplevel()
    self.fenetre.configure(width = 800,height=500)
    self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
    self.fenetre.title("Visualisation Macro_Etape")
    self.jdc=jdc
    self.nom_jdc=nom_jdc
    self.appli=appli
    self.barre=Tkinter.Frame(self.fenetre,relief="ridge",bd=2)
    self.barre.pack(expand=1,fill=Tkinter.X)
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
    self.item=MACRO2TreeItem(self.appli,nom_jdc,jdc)
    import treewidget
    self.tree = treewidget.Tree(self.appli,self.item,self.mainPart,command=None,rmenu=self.make_rmenu)
    self.tree.draw()

  def visufile(self):
    Fenetre(self.appli,titre="Source du fichier inclus",texte=self.jdc.fichier_text)

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
                    menu.add_radiobutton(label=label,command=lambda a=self.appli,c=command:c(a))
                    if radio == None:radio=number_item
                 except:pass
            else:
                 try:
                    command=getattr(node.item,method)
                    menu.add_command(label=label,command=lambda a=self.appli,c=command:c(a))
                 except:pass
      # Si au moins un radiobouton existe on invoke le premier
      if radio:menu.invoke(radio)

  def quit(self):
    self.fenetre.destroy()

def makeMacroDisplay(appli,jdc,nom_jdc):
  return MacroDisplay(appli,jdc,nom_jdc)

