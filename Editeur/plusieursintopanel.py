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
from plusieurspanel import PLUSIEURS_Panel

class PLUSIEURS_INTO_Panel(PLUSIEURS_Panel):
  """
  Classe servant à définir le panneau permettant d'afficher et de saisir une
  liste de valeurs à choisir parmi une liste discrètes de valeurs possibles
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie de plusieurs valeurs parmi un ensemble discret
      de possibles
      """
      self.ajout_valeurs = None
      # On récupère la bulle d'aide du panneau, l'objet, min et max (cardinalité de la liste),
      # la liste des choix et la liste des valeurs
      aide = self.get_aide()
      aide = justify_text(texte=aide)
      bulle_aide=self.get_bulle_aide()
      objet_mc = self.node.item.get_definition()
      min,max = self.node.item.GetMinMax()
      #l_choix=list(objet_mc.into)
      l_valeurs = self.node.item.GetListeValeurs()
      l_choix= self.node.item.get_liste_possible(l_valeurs)
      # reinitialisation de l_valeurs
      l_valeurs = self.node.item.GetListeValeurs()

      # remplissage du panneau
      self.frame_valeurs = Frame(page)
      self.frame_valeurs.place(relx=0.05,rely=0.05,relwidth=0.35,relheight=0.7)
      self.frame_boutons_fleches = Frame(page)
      self.frame_boutons_fleches.place(relx=0.4,rely=0.,relwidth=0.2,relheight=0.7)
      self.frame_choix = Frame(page)
      self.frame_choix.place(relx=0.6,rely=0.05,relwidth=0.35,relheight=0.7)
      self.frame_boutons = Frame(page)
      self.frame_boutons.place(relx=0.35,rely=0.87,relwidth=0.3,relheight=0.1)
      self.frame_aide = Frame(page)
      self.frame_aide.place(relx=0.1,rely=0.75,relwidth=0.9,relheight=0.1)
      liste_commandes_valeurs = (("<Button-1>",self.selectValeur),
                                 ("<Button-3>",self.deselectValeur),
                                 ("<Double-Button-1>",self.sup_valeur))
      liste_commandes_choix = (("<Button-1>",self.selectChoix),
                               ("<Button-3>",self.deselectChoix),
                               ("<Double-Button-1>",self.add_choix))
      self.Liste_valeurs = ListeChoix(self,self.frame_valeurs,
                                      l_valeurs,liste_commandes = liste_commandes_valeurs,
                                      titre="Valeur(s) actuelle(s)")
      self.Liste_choix = ListeChoix(self,self.frame_choix,l_choix,
                                    liste_commandes = liste_commandes_choix,
                                    titre= "Valeurs possibles")
      bouton_add = Button(self.frame_boutons_fleches,
                          #text="<--",
                          image = images.get_image('arrow_left'),
                          command = self.add_choix)
      bouton_sup = Button(self.frame_boutons_fleches,
                          #text="-->",
                          image = images.get_image('arrow_right'),
                          command = self.sup_valeur)
      bouton_accepter = Button(self.frame_boutons,
                               text='Valider',
                               command = lambda s=self,m=min,M=max : s.accepte_modifs_valeur(m,M))
      bouton_annuler = Button(self.frame_boutons,
                              text = 'Annuler',
                              command = self.annule_modifs_valeur)
      bouton_add.place(relx=0.3,rely=0.35)
      bouton_sup.place(relx=0.3,rely=0.65)
      for but in (bouton_accepter,bouton_annuler):
          but.pack(side='left',padx=5)
      self.Liste_valeurs.affiche_liste()
      if len(l_valeurs) > 0 :
          liste_marque=l_valeurs[-1]
          self.Liste_valeurs.surligne(liste_marque)
      self.Liste_choix.affiche_liste()
      for fram in (self.frame_valeurs,self.frame_boutons_fleches,self.frame_choix,self.frame_boutons):
          fram.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
          fram.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      self.frame_aide.update()
      self.aide = Label(self.frame_aide,
                        text = aide,
                        justify='center',
                        anchor='center',
			wraplength=int(self.frame_aide.winfo_width()*0.8))
      self.aide.place(relx=0.5,rely=0.5,anchor='center',relwidth=1)

  def get_aide(self):
      """
      Retourne la phrase d'aide indiquant de quel type de base doivent être les valeurs
      que saisit l'utilisateur
      """
      commentaire=""
      mc = self.node.item.get_definition()
      d_aides = { 'TXM' : 'chaînes de caractères',
                  'R'   : 'réels',
                  'I'   : 'entiers',
                  'C'   : 'complexes'}
      type = mc.type[0]
      if not d_aides.has_key(type) : 
	 if mc.min == mc.max:
	    return str(mc.min)+" valeur(s) est(sont) attendue(s)"
         else :
	    return "entrez entre "+str(mc.min)+" et "+str(mc.max)+" valeurs"
      if mc.min == mc.max:
	    commentaire="Une liste de "+str(mc.min)+" "+d_aides[type]+" est attendue"
      else :
	    commentaire="Entre "+str(mc.min)+" et "+str(mc.max)+" valeurs de type  "+d_aides[type]+" sont attendues"
      aideval=self.node.item.aide()
      commentaire=commentaire + "\n" + aideval
      return commentaire

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide du panneau (affichée par clic droit)
      """
      return """Un clic sur une valeur des deux listes la sélectionne.
      - Un clic sur la flèche gauche stocke la valeur possible sélectionnée
      dans la liste des valeurs que vous voulez affecter au mot-clé simple
      - Un clic sur la flèche droite déstocke la valeur du mot-clé simple
      sélectionnée (elle apparaît alors à nouveau comme choix possible
      dans la liste des choix à droite)
      - Cliquez sur 'Valider' pour affecter la liste des valeurs sélectionnées
      au mot-clé simple courant
      - Cliquez sur 'Annuler' pour restaurer la valeur du mot-clé simple
      avant toute modification depuis le dernier 'Valider'"""

