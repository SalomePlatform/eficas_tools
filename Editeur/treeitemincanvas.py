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
"""
# Modules Python
import Tkinter,Pmw

# Modules Eficas
import Objecttreeitem
import treewidget

class TREEITEMINCANVAS:
   def __init__(self,object,nom="",parent=None,appli=None,sel=None):
      self.object=object
      self.nom=nom

      if not appli:
         class Appli:
            def affiche_infos(self,message):
               pass
         appli=Appli()
      self.appli=appli

      if not parent:
         parent=Tkinter.Tk()
         Pmw.initialise(parent)
      self.parent=parent

      self.item=Objecttreeitem.make_objecttreeitem(self.appli,self.nom,self.object)
      self.canvas=Pmw.ScrolledCanvas(self.parent,borderframe=1,canvas_background='gray95')
      self.canvas.pack(padx=10,pady=10,fill = 'both', expand = 1)
      if not sel:
         def sel(event=None):
            return
      self.tree=treewidget.Tree(self.appli,self.item,self.canvas,command=sel)
      self.tree.draw()

   def mainloop(self):
      self.parent.mainloop()

   def update(self):
      """Cette methode est utilisee pour signaler une mise a jour des objets associes"""
      self.tree.update()
