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
      labels= ('Fichier','Edition','Jeu de commandes','Catalogue','Browsers','Options','Aide')

   def init(self):
      self.menudict={}
      for label in self.labels:
         menu=Menu(self.menubar,tearoff=0)
         self.menudict[label]=menu
         self.menubar.add_cascade(label=label,menu=menu)

