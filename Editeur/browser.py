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
import os,string

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



