"""
"""
# Modules Python
import os,string
from tkFileDialog import *

# Modules Eficas
import Interp
import catabrowser
import cataediteur

class BROWSER:

   menu_defs=[
              ('Browsers',[
                           ('Browser catalogue','browser_catalogue'),
                           ('Editeur catalogue','edite_catalogue'),
                           ('Shell','shell'),
                         ]
              )
             ]

   button_defs=[]

   def __init__(self,appli,parent):
      self.appli=appli
      self.parent=parent
      self.cataitem = catabrowser.CATAItem(self,"Catalogue "+self.appli.readercata.code,
                                           self.appli.readercata.cata,
                                           objet_cata_ordonne = self.appli.readercata.cata_ordonne_dico)

   def shell(self,event=None):
      if not hasattr(self.appli.bureau.JDCDisplay_courant,'jdc'):return
      d={'j':self.appli.bureau.JDCDisplay_courant.jdc}
      Interp.InterpWindow(d,parent=self.parent)

   def browser_catalogue(self,event=None):
      catabrowser.CataBrowser(parent=self.parent,appli=self.appli,
                                cata = self.appli.readercata.cata,
                                item = self.cataitem)

   def edite_catalogue(self,event=None):
      cataediteur.CataEditeur(parent=self.parent,appli=self.appli,cata=self.appli.readercata.cata)



