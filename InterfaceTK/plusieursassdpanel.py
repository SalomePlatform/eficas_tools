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
from Editeur import Objecttreeitem
import prefs
import panels
import images
from widgets import ListeChoix
from widgets import FenetreDeSelection

from Noyau.N_CR import justify_text
from Editeur.utils import substract_list

# Import des panels
from plusieurspanel import PLUSIEURS_Panel 

class PLUSIEURS_ASSD_Panel(PLUSIEURS_Panel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de donner une liste de valeurs qui ne sont pas
  à choisir dans une liste discrètes et qui sont de type dérivé d'ASSD
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie de plusieurs noms de SD parmi un ensemble discret
      de SD possibles, cad d'un type cohérent avec les types attendus par le mot-clé simple
      """
      # On récupère la bulle d'aide du panneau, l'objet, l'aide, min et max (cardinalité de la liste),
      # la liste des valeurs déjà affectées à l'objet courant et la liste des SD du bon type
      bulle_aide=self.get_bulle_aide()
      self.ajout_valeurs=None
      objet_mc = self.node.item.get_definition()
      aide = self.get_aide()
      aide = justify_text(texte=aide)
      min,max = self.node.item.GetMinMax()
      l_valeurs = self.node.item.GetListeValeurs()
      l_choix=self.node.item.get_sd_avant_du_bon_type()
      l_choix.sort()
      # remplissage du panneau
      self.frame_valeurs = Frame(page)
      self.frame_valeurs.place(relx=0.05,rely=0.05,relwidth=0.35,relheight=0.7)
      self.frame_boutons_fleches = Frame(page)
      self.frame_boutons_fleches.place(relx=0.4,rely=0.,relwidth=0.2,relheight=0.7)
      self.frame_choix = Frame(page)
      self.frame_choix.place(relx=0.6,rely=0.05,relwidth=0.35,relheight=0.7)
      self.frame_boutons = Frame(page)
      self.frame_boutons.place(relx=0.35,rely=0.87,relwidth=0.5,relheight=0.1)
      liste_commandes_valeurs = (("<Button-1>",self.selectValeur),
                                 ("<Button-3>",self.deselectValeur),
                                 ("<Double-Button-1>",self.sup_valeur_sans_into))
      liste_commandes_choix = (("<Button-1>",self.selectChoix),
                               ("<Button-3>",self.deselectChoix),
                               ("<Double-Button-1>",self.add_eval_valeur_sans_into))
      self.Liste_valeurs = ListeChoix(self,self.frame_valeurs,l_valeurs,liste_commandes = liste_commandes_valeurs,
                                      titre="Valeur(s) actuelle(s)")
      self.Liste_choix = ListeChoix(self,self.frame_choix,l_choix,liste_commandes = liste_commandes_choix,
                                    titre= "Valeurs possibles")
      self.bouton_add = Button(self.frame_boutons_fleches,
                          image = images.get_image('arrow_left'),
                          command = self.add_eval_valeur_sans_into)
      self.bouton_sup = Button(self.frame_boutons_fleches,
                          image = images.get_image('arrow_right'),
                          command = self.sup_valeur_sans_into)
      self.bouton_accepter = Button(self.frame_boutons,
                               text='Valider',
                               command = lambda s=self,m=min,M=max : s.accepte_modifs_valeur(m,M))
      self.bouton_annuler = Button(self.frame_boutons,
                              text = 'Annuler',
                              command = self.annule_modifs_valeur)
      self.bouton_add.place(relx=0.3,rely=0.35)
      self.bouton_sup.place(relx=0.3,rely=0.65)
      for but in (self.bouton_accepter,self.bouton_annuler):
          but.pack(side='left',padx=4)
      self.Liste_valeurs.affiche_liste()
      if len(l_valeurs) > 0 :
          liste_marque=l_valeurs[-1]
          self.Liste_valeurs.surligne(liste_marque)
      self.Liste_choix.affiche_liste()
      for fram in (self.frame_valeurs,self.frame_boutons_fleches,self.frame_choix,self.frame_boutons):
          fram.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
          fram.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
  
  def add_eval_valeur_sans_into(self,valeurentree=None):
      if valeurentree == None:
         valeurentree = self.get_valeur()
      valeur,validite=self.node.item.eval_valeur(valeurentree)
      if not validite :
         commentaire = "impossible d'évaluer : %s " %`valeurentree`
         self.parent.appli.affiche_infos(commentaire)
         return
      self.add_valeur_sans_into(valeur)

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide associée au panneau
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

  def get_aide(self):
      """
      Retourne la phrase d'aide indiquant de quel type doivent être les
      valeurs que doit entrer l'utilisateur
      """
      commentaire=""
      mc = self.node.item.get_definition()
      type = mc.type[0].__name__  
      if len(mc.type)>1 :
          for typ in mc.type[1:] :
              type = type + ' ou '+typ.__name__
      if mc.min == mc.max:
        commentaire="Une liste de "+`mc.min`+" objets de type "+type+" est attendue"
      else :
        commentaire="Une liste d'objets de type "+type+" est attendue (min="+`mc.min`+",max="+`mc.max`+')'
      aideval=self.node.item.aide()
      commentaire=commentaire +"\n"+ aideval
      return commentaire

    
  def sup_valeur(self,name=None):
      """
      Supprime la valeur selectionnée de la liste des valeurs et la rajoute
      à la liste des choix possibles
      """
      liste_valeurs = self.Liste_valeurs.get_liste()
      liste_valeurs.remove(self.selected_valeur)
      liste_choix = self.node.item.get_definition().into
      liste_choix = substract_list(liste_choix,liste_valeurs)
      self.Liste_valeurs.put_liste(liste_valeurs)
      self.Liste_choix.put_liste(liste_choix)
      self.selected_valeur = None      
    
  def erase_valeur(self):
      pass

  def get_valeur(self):
      """
      Retourne la valeur sélectionnée dans la liste des choix
      """
      return self.selected_choix

  def display_valeur(self,val=None):
      """
         Affiche la valeur passée en argument dans l'entry de saisie.
         Par défaut affiche la valeur du mot-clé simple
      """
      # Il n'y a pas d'entry pour ce type de panneau
      return

    
