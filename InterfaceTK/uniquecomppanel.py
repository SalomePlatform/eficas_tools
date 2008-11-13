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
from uniquepanel import UNIQUE_Panel

      
class UNIQUE_COMP_Panel(UNIQUE_Panel):
  """
  Classe servant à définir le panneau associé aux mots-clés simples
  qui attendent une valeur de type complexe
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie de la valeur du mot-clé simple courant qui doit être de type
      de base cad entier, réel, string ou complexe
      """
      # Récupération de l'aide associée au panneau et de l'aide destinée à l'utilisateur
      bulle_aide=self.get_bulle_aide()
      aide=self.get_aide()
      aide= justify_text(texte=aide)
      # Remplissage du panneau
      self.frame_valeur = Frame(page)
      self.frame_valeur.pack(fill='both',expand=1)
      self.frame_valeur.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      self.frame_valeur.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      self.label  = Label(self.frame_valeur,text='Complexe de la forme : a+bj')
      self.label1 = Label(self.frame_valeur,text='Imaginaire')
      self.label2 = Label(self.frame_valeur,text='Phase')
      self.label3 = Label(self.frame_valeur,text='OU')
      self.label.place (relx=0.15,rely=0.1)
      self.label1.place(relx=0.6,rely=0.50)
      self.label2.place(relx=0.6,rely=0.57)
      self.label3.place(relx=0.15,rely=0.4)
      self.typ_cplx=StringVar()
      self.typ_cplx.set('RI')
      rb1 = Radiobutton(self.frame_valeur, text='RI  : Réel',variable=self.typ_cplx,value='RI')
      rb2 = Radiobutton(self.frame_valeur, text='MP  : Module',variable=self.typ_cplx,value='MP')
      rb1.place(relx=0.15,rely = 0.50)
      rb2.place(relx=0.15,rely = 0.57)
      self.entry1 = Pmw.EntryField(self.frame_valeur,validate='real')
      self.entry2 = Pmw.EntryField(self.frame_valeur,validate='real')
      self.entry3 = Pmw.EntryField(self.frame_valeur)
      self.entry1.component('entry').bind("<Return>",lambda e,s=self:s.entry2.component('entry').focus())
      self.entry1.component('entry').bind("<KP_Enter>",lambda e,s=self:s.entry2.component('entry').focus())
      self.entry2.component('entry').bind("<Return>",lambda e,c=self.valid_valeur:c())
      self.entry2.component('entry').bind("<KP_Enter>",lambda e,c=self.valid_valeur:c())
      self.entry3.component('entry').bind("<Return>",lambda e,c=self.valid_complexe:c())
      self.entry3.component('entry').bind("<KP_Enter>",lambda e,c=self.valid_complexe:c())
      self.entry1.place(relx=0.15,rely = 0.65,relwidth=0.35)
      self.entry2.place(relx=0.60,rely = 0.65,relwidth=0.35)
      self.entry3.place(relx=0.15,rely = 0.20,relwidth=0.60)
      self.entry1.focus()
      self.bouton_val=Button(self.frame_valeur,text="Valider",command=self.valider,width=14)
      self.bouton_val.place(relx=0.4,rely=0.8)
      self.frame_valeur.update()
      self.aide = Label(self.frame_valeur,
                        text = aide,
                        wraplength=int(self.frame_valeur.winfo_width()*0.8),
                        justify='center')
      self.aide.place(relx=0.5,rely=0.9,anchor='n')
      # affichage de la valeur du MCS
      self.display_valeur()

  def valider(self):
      if ((self.entry3.get() != None) and (self.entry3.get() != "" )):
         self.erase_valeur()
         self.valid_complexe()
      else :
         self.valid_valeur()
         

  def display_valeur(self):
      """
      Affiche la valeur de l'objet pointé par self
      """
      valeur = self.node.item.get_valeur()
      if valeur == None or valeur == '' : return # pas de valeur à afficher ...
      self.entry1.delete(0,END)
      self.entry2.delete(0,END)
      self.entry3.delete(0,END)
      if type(valeur) not in (types.ListType,types.TupleType) :
         self.display_complexe()
      else:
         typ_cplx,x1,x2=valeur
         self.typ_cplx.set(typ_cplx)
         self.entry1.setentry(x1)
         self.entry2.setentry(x2)

  def display_complexe(self):
      valeur = self.node.item.get_valeur()
      self.entry3.setentry(valeur)

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide du panneau
      """
      return """-Choisissez votre format de saisie du complexe :
      \t 'RI' = parties réelle et imaginaire
      \t 'MP' = module/phase (en degrés)
      - Saisissez ensuite dans les deux zones de saisie les deux nombres attendus"""

  def get_aide(self):
      """
      Retourne la phrase d'aide décrivant le type de la valeur que peut prendre
      le mot-clé simple courant
      """
      commentaire='Un complexe est attendu'
      aideval=self.node.item.aide()
      commentaire=commentaire +"\n"+ aideval
      return commentaire

  def get_valeur(self):
      """
      Retourne le complexe saisi par l'utilisateur
      """
      l=[]
      l.append(self.typ_cplx.get())
      try :
         l.append(string.atof(self.entry1.get()))
         l.append(string.atof(self.entry2.get()))
      except :
         return None
      return `tuple(l)`

  def erase_valeur(self):
      """
      Efface les entries de saisie
      """
      self.typ_cplx.set('RI')
      self.entry1.delete(0,END)
      self.entry2.delete(0,END)
      
  def valid_complexe(self):
      valeurentree=self.entry3.get()
      self.valid_valeur(valeurentree=valeurentree)
