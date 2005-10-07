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
from newsimppanel import newSIMPPanel

    
class UNIQUE_Panel(newSIMPPanel):
  """
  Classe virtuelle servant de classe mère à toutes celles définissant un panneau
  permettant l'affichage et la saisie d'une valeur unique pour le mot-clé simple
  """

  def erase_valeur(self):
      """
      Efface l'entry de saisie
      """
      self.entry.delete(0,END)

  def get_valeur(self):
      """
      Retourne la valeur donnée par l'utilisateur
      """
      return self.entry.get()
    
  
  def valid_valeur(self,valeurentree=None):
      """
      Teste si la valeur fournie par l'utilisateur est une valeur permise :
      - si oui, l'enregistre
      - si non, restaure l'ancienne valeur
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      anc_val = self.node.item.get_valeur()
      if valeurentree== None :
         valeurentree = self.get_valeur()
      valeur,validite=self.node.item.eval_valeur(valeurentree)
      if not validite :
             commentaire = "impossible d'évaluer : %s " %`valeurentree`
             self.display_valeur()
             self.parent.appli.affiche_infos(commentaire)
             return
   
      test = self.node.item.set_valeur(valeur)
      if test :
          self.set_valeur_texte(str(valeurentree))
       
      if not test :
          mess = "impossible d'évaluer : %s " %`valeur`
          self.parent.appli.affiche_infos("Valeur du mot-clé non autorisée : "+mess)
      elif self.node.item.isvalid() :
          self.parent.appli.affiche_infos('Valeur du mot-clé enregistrée')
      else :
          cr = self.node.item.get_cr()
          mess = "Valeur du mot-clé non autorisée :"+cr.get_mess_fatal()
          self.reset_old_valeur(anc_val,mess=mess)

      self.display_valeur()
