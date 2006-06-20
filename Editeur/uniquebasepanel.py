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
from Tkinter import Widget
import Pmw
from copy import copy,deepcopy
import traceback

# Modules Eficas
import Objecttreeitem
import prefs
import panels
import images
from widgets import FenetreDeParametre
from widgets import showerror

from Noyau.N_CR import justify_text
from utils import substract_list

# Import des panels
from uniquepanel import UNIQUE_Panel


class UNIQUE_BASE_Panel(UNIQUE_Panel):
  """
  Classe servant à définir le panneau associé aux mots-clés simples qui attendent
  une valeur d'un type de base (entier, réel ou string).
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie de la valeur du mot-clé simple courant qui doit être de type
      de base cad entier, réel, string ou complexe
      """
      # Récupération de l'aide associée au panneau, de l'aide destinée à l'utilisateur,
      # et de la liste des SD du bon type (constituant la liste des choix)
      bulle_aide=self.get_bulle_aide()
      aide=self.get_aide()
      aide= justify_text(texte=aide)
      liste_noms_sd = self.node.item.get_sd_avant_du_bon_type()
      # Remplissage du panneau
      self.frame_valeur = Frame(page)
      self.frame_valeur.pack(fill='both',expand=1)
      self.frame_valeur.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      self.frame_valeur.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      self.label = Label(self.frame_valeur,text='Valeur :')
      self.label.place(relx=0.1,rely=0.2)
      self.entry = Entry(self.frame_valeur,relief='sunken')
      self.entry.place(relx=0.28,rely=0.2,relwidth=0.6)
      self.entry.bind("<Return>",lambda e,c=self.valid_valeur:c())
      self.entry.bind("<KP_Enter>",lambda e,c=self.valid_valeur:c())
      # aide associée au panneau
      self.frame_valeur.update()
      self.aide = Label(self.frame_valeur, 
                        text = aide,
                        wraplength=int(self.frame_valeur.winfo_width()*0.8),
                        justify='center')
      self.aide.place(relx=0.5,rely=0.7,anchor='n')
      # bouton parametre
      bouton_parametres = Button(self.frame_valeur, text="Parametres", command=self.affiche_parametre)
      bouton_parametres.place(relx=0.28,rely=0.5,relwidth=0.4)
      # affichage de la valeur du MCS
      self.display_valeur()

  def affiche_parametre(self) :
     if self.node.item.get_liste_param_possible() != [ ]:
        txtparam=""
        for param in self.node.item.get_liste_param_possible():
           txtparam=txtparam+repr(param)+"\n"
        if txtparam=="":
           showerror("Aucun parametre ","Pas de parametre de ce type")
        else :
           try :
                   self.fenetreparam.destroy()
           except :
                pass
           self.fenetreparam=FenetreDeParametre( self, self.node.item, self.parent.appli, txtparam)

  def destroy(self):
      try :
              self.fenetreparam.destroy()
      except :
        pass
      Widget.destroy(self)

  def get_aide(self):
      """
      Retourne la phrase d'aide indiquant de quel type doit être la valeur
      du mot-clé simple fournie par l'utilisateur
      """
      mc = self.node.item.get_definition()
      d_aides = { 'TXM' : "Une chaîne de caractères est attendue",
                  'R'   : "Un réel est attendu",
                  'I'   : "Un entier est attendu"}
      type = mc.type[0]
      commentaire=d_aides.get(type,"Type de base inconnu")
      aideval=self.node.item.aide()
      commentaire=commentaire +"\n"+ aideval
      return commentaire

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide associée au panneau et affichée par clic droit
      """
      return """Saisissez la valeur que vous voulez affecter au mot-clé simple
      dans la zone de saisie et pressez <Return>"""
      
  def display_valeur(self):
      """
      Affiche la valeur de l'objet pointé par self
      """
      valeur = self.node.item.get_valeur()
      if valeur == None or valeur == '' : # pas de valeur à afficher ...
         self.entry.delete(0,END)
         self.entry.focus()
         return

      valeur_texte=self.get_valeur_texte(valeur)
      if valeur_texte != "":
         valeur=valeur_texte
      self.entry.delete(0,END)
      self.entry.insert(0,valeur)
      self.entry.focus()
      
