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
import string,types,os
from Tkinter import *
import Pmw
from copy import copy,deepcopy
import traceback

# Modules Eficas
import Objecttreeitem
import prefs
import panels
import images
from widgets import ListeChoix
from widgets import FenetreDeSelection

from Noyau.N_CR import justify_text
from utils import substract_list

# Import des panels
from uniquepanel import UNIQUE_Panel

class UNIQUE_INTO_Panel(UNIQUE_Panel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie d'une seule valeur parmi un ensemble
      discret de possibles
      """
      # récupération de la bulle d'aide et de l'objet mc
      bulle_aide=self.get_bulle_aide()
      objet_mc = self.node.item.get_definition()
      # remplissage du panel
      self.frame_valeur = Frame(page)
      self.frame_valeur.pack(fill='both',expand=1)
      self.frame_valeur.bind("<Button-3>",lambda e,s=self,a=bulle_aide : 
                              s.parent.appli.affiche_aide(e,a))
      self.frame_valeur.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      #l_choix=list(objet_mc.into)
      #l_choix.sort()
      l_choix=self.node.item.get_liste_possible([])
      self.label = Label(self.frame_valeur,text='Choisir une valeur :')
      self.label.pack(side='top')
      self.frame = Frame(page)
      self.frame.place(relx=0.33,rely=0.2,relwidth=0.33,relheight=0.6)
      liste_commandes = (("<Button-1>",self.selectChoix),
                         ("<Button-3>",self.deselectChoix),
                         ("<Double-Button-1>",self.record_valeur))
      self.Liste_choix = ListeChoix(self,self.frame,l_choix,
                                    liste_commandes = liste_commandes,
                                    titre="Valeurs possibles")
      self.Liste_choix.affiche_liste()

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide affectée au panneau courant (affichée par clic droit)
      """
      return """Double-cliquez sur la valeur désirée
      pour valoriser le mot-clé simple courant"""

