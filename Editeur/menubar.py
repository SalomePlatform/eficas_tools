"""
"""
from Tkinter import Menu

class MENUBAR:
   def __init__(self,appli,parent):
      # L'attribut appli pointe vers l'objet application qui détient la menubar et les autres composants
      self.appli=appli
      # L'attribut parent pointe vers l'objet graphique parent de la menubar
      self.parent=parent
      self.menubar=Menu(self.parent)
      self.parent.configure(menu=self.menubar)
      self.init()

   try:
      from prefs import labels
   except:
      labels= ('Fichier','Edition','Jeu de commandes','Catalogue','Browsers','Options')

   def init(self):
      self.menudict={}
      for label in self.labels:
         menu=Menu(self.menubar,tearoff=0)
         self.menudict[label]=menu
         self.menubar.add_cascade(label=label,menu=menu)

