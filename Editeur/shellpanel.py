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
#import prefs
#import panels
#import images
#from widgets import ListeChoix
#from widgets import FenetreDeSelection

from Noyau.N_CR import justify_text
from utils import substract_list
from newsimppanel import newSIMPPanel


class SHELLPanel(newSIMPPanel):
  """
  Classe Panel utilisé pour les mots-clés simples qui attendent un shell pour valeur
  """

  def makeValeurPage(self,page):
      """ 
      Affiche la page concernant l'objet pointé par self qui attend un shell
      """
      objet_mc = self.node.item.get_definition()
      aide = self.gen_aide()
      aide = justify_text(texte=aide)
      self.frame = Frame(page)
      self.frame.place(relx=0,rely=0,relwidth=1,relheight=1)
      label_aide = Label(self.frame,text = aide)
      label_aide.place(relx=0.5,rely=0.1,anchor='center')
      self.text = Text(self.frame,bg='gray95')
      self.text.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.6)
      but_val = Button(self.frame,text='Valider',command = self.valide_shell)
      but_ann = Button(self.frame,text='Annuler',command = self.annule_shell)
      but_val.place(relx=0.35,rely=0.9,anchor='center')
      but_ann.place(relx=0.65,rely=0.9,anchor='center')
      self.display_valeur()

  def gen_aide(self):
      """
      Retourne une chaîne de caractères d'aide sur la valeur qu'attend l'objet
      pointé par self
      """
      return "Un shell est attendu"
    
  def valide_shell(self,event=None):
      """
      Récupère la valeur saisie par l'utilisateur dans self.text
      et la stocke dans l'objet MCSIMP courant
      """
      texte = self.text.get(1.0,END)
      self.record_valeur(texte)

  def annule_shell(self,event=None):
      """
      Annule toute saisie dans self.text
      """
      self.text.delete(0,END)

  def display_valeur(self,val=None):
      """
      Affiche la valeur de l'objet pointé par self
      """
      if val != None :
          valeur = val
      else:
          valeur = self.node.item.get_valeur()
      if valeur == None  or valeur == '': return
      self.text.insert(END,valeur)

