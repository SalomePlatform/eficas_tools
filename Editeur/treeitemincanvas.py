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
      self.canvas=Pmw.ScrolledCanvas(self.parent,borderframe=1)
      self.canvas.pack(padx=10,pady=10,fill = 'both', expand = 1)
      if not sel:
         def sel(event=None):
            return
      self.tree=treewidget.Tree(self.appli,self.item,self.canvas,command=sel)
      self.tree.draw()

   def mainloop(self):
      self.parent.mainloop()

