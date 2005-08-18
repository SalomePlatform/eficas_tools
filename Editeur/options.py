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
# Modules Python
import os,string

# Modules Eficas
from widgets import askopenfilename
import panels

# l'option affichage_commandes peut prendre les valeurs "groupes" ou "alphabetic"
affichage_commandes="alphabetic"

class OPTIONS:

   menu_defs=[
        ('Options',[
                   ("Affichage commandes",(("alphabétique",'&affichage_alpha'),("groupes",'&affichage_grp'))),
                   #("Couleur",(("fond",'change_fond'),("barre",'change_barre'))),
                   # ("Catalogue développeur",'choix_cata_developpeur'),
                   ]
        )
             ]

   button_defs=[]

   def __init__(self,appli,parent):
      self.appli=appli
      self.parent=parent

   def affichage_grp(self):
      global affichage_commandes
      affichage_commandes="groupes"
      if hasattr(panels,'panneauCommande'):
         panel=panels.panneauCommande
	 parent=panel.parent
	 if parent != None :
	    parent.create_panel(parent.node_selected)
	    # si on a un panel avec plusieurs onglets
	    # on affiche Commande
	    try :
	      parent.panel_courant.nb.selectpage("Commande")
	    except :
	      pass

   def affichage_alpha(self):

      global affichage_commandes
      affichage_commandes="alphabetic"
      if hasattr(panels,'panneauCommande'):
         panel=panels.panneauCommande
	 parent=panel.parent
	 if parent != None :
	    parent.create_panel(parent.node_selected)
	    # si on a un panel avec plusieurs onglets
	    # on affiche Commande
	    try :
	      parent.panel_courant.nb.selectpage("Commande")
	    except :
	      pass

   def change_fond(self):
      from tkColorChooser import askcolor
      #nouvelle=askcolor(self.appli.background)
      nouvelle=askcolor('grey')

   def change_barre(self):
       pass

   def choix_cata_developpeur(self):
      """ 
          Cette méthode demande à l'utilisateur-développeur d'indiquer quel catalogue
          il veut utiliser en remplacement du catalogue standard du code
          NB : il faut que le développeur ait les droits d'écriture dans le répertoire où
          se trouve le catalogue 
      """
      file = askopenfilename(title="Choix d'un catalogue personnel",
                             defaultextension=".py",
                             filetypes = ( ("Catalogue", "cata*.py"),))
      if file :
          self.parent.update_idletasks()
          self.appli.reset_affichage_infos()
          rep_fic = os.path.dirname(file)
          nom_fic = string.split(os.path.basename(file),'.')[0]
          rep_courant = os.getcwd()
          os.chdir(rep_fic)
          self.cata = __import__(nom_fic)
          self.code = self.cata.CODE
          os.chdir(rep_courant)
          self.fic_cata = file
          fic_cata_p = nom_fic+'_pickled.py'
          self.fic_cata_p = os.path.join(rep_fic,fic_cata_p)
          pile_erreurs = self.cata.erreurs_cata
          if pile_erreurs.existe_message() :
              messages = pile_erreurs.retourne_messages()
              print messages
          else :
              # XXX ne doit pas fonctionner
              self.catalo = catabrowser.CataItem(cata=self.cata)
              self.Retrouve_Ordre_Cata('personnel')
          pile_erreurs.efface()

