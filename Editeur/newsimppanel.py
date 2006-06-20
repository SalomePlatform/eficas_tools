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
import composimp
from widgets import ListeChoix
from widgets import FenetreDeSelection

from Noyau.N_CR import justify_text
from utils import substract_list


class newSIMPPanel(panels.OngletPanel):
  """
  Classe virtuelle servant de classe mère à toutes les classes Panel
  servant à afficher et récupérer la valeur d'un mot-clé simple.
  Le panel est différent suivant le type de la valeur attendu
  """
  def init(self):
      """
      Méthode appelée par le constructeur de OngletPanel :
      construit le notebook à 2 onglets utilisé par tous les panels de
      tous les mots-clés simples
      """
      nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
      nb.pack(fill = 'both', expand = 1)
      self.nb=nb
      nb.add('Valeur', tab_text='Saisir valeur')
      self.makeValeurPage(nb.page('Valeur'))
      self.enlevebind()
      self.creebind()
      nb.setnaturalsize()
      
# ----------------------------------------------------------------------------------------
#   Méthodes utilisées pour l'affectation de la valeur donnée par l'utilisateur
#    au mot-clé courant
# ----------------------------------------------------------------------------------------

  def reset_old_valeur(self,name=None,mess='Valeur du mot-clé enregistrée'):
      """
          Enregistre  val comme valeur de self.node.item.object SANS 
          faire de test de validité ni ré-évaluer l'ancienne valeur
          permet de rester avec des valeurs non entrees et de ne pas 
          ré-évaluer des entiers par exemple
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      self.node.item.set_valeur(name)
      self.parent.appli.affiche_infos(mess)

  def record_valeur(self,name=None,mess='Valeur du mot-clé enregistrée'):
      """
          Enregistre  val comme valeur de self.node.item.object  
          en evaluant l item et en le validant 
          Si name n'est pas renseigné, la valeur 
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      if name != None:
          valeur = name
          validite = 1
      else :
          valeurentree= self.entry.get()
          self.entry.delete(0,END)
          if valeurentree == '': valeurentree=None
          valeur,validite=self.node.item.eval_valeur(valeurentree)
          if not validite :
                  valeur= self.entry.get()
                  commentaire = "impossible d'évaluer : %s " %`valeurentree`
                  self.parent.appli.affiche_infos(commentaire)
                
      if validite : 
          validite,commentaire=self.node.item.valide_val(valeur)
 
      if validite :
          self.node.item.set_valeur(valeur)
          self.parent.appli.affiche_infos(mess)
      else :
          self.parent.appli.affiche_infos(commentaire)

# ----------------------------------------------------------------------------------------
#   Méthodes utilisées pour la manipulation des items dans les listes de choix
# ----------------------------------------------------------------------------------------
  def selectValeur(self,name):
      self.selected_valeur = name

  def deselectValeur(self,name):
      self.selectValeur = None

  def sup_valeur(self,name=None):
      """
      Supprime la valeur selectionnée de la liste des valeurs et la rajoute
      à la liste des choix possibles
      """
      if hasattr(self,'selected_valeur') :
         if ( self.selected_valeur != None and self.selected_valeur != ''):
            liste_valeurs = self.Liste_valeurs.get_liste()
            liste_valeurs.remove(self.selected_valeur)
            self.Liste_valeurs.put_liste(liste_valeurs)
            listeActuelle=self.Liste_valeurs.get_liste()
            liste_choix=self.node.item.get_liste_possible(listeActuelle)
            self.Liste_choix.put_liste(liste_choix)
            self.selected_valeur = None

  def add_choix(self,name=None):
      """
      Ajoute le choix selectionné à la liste des valeurs et le retire
      de la liste des choix possibles
      """
      
      if hasattr(self,'selected_choix') :
         if (self.selected_choix != None and self.selected_choix != ''):
            min,max = self.node.item.GetMinMax()
            liste_valeurs = self.Liste_valeurs.get_liste()
            if len(liste_valeurs) >= max :
                self.parent.appli.affiche_infos("La liste ne peut pas avoir plus de %d éléments" %max)
                return
            if (self.Liste_valeurs.selection != None):
                ligne=self.Liste_valeurs.cherche_selected_item()
                liste_valeurs.insert(ligne,self.selected_choix)
            else :
                liste_valeurs.append(self.selected_choix)
            self.Liste_valeurs.put_liste(liste_valeurs)
            listeActuelle=self.Liste_valeurs.get_liste()
            liste_choix=self.node.item.get_liste_possible(listeActuelle)
            self.Liste_choix.put_liste(liste_choix)
            self.selected_choix = None

  def selectChoix(self,name):
      self.selected_choix = name

  def deselectChoix(self,name):
      self.selectChoix = None
      
  def raisecmd(self,page):
      try:
         self.entry.focus()
      except:
         pass

# ----------------------------------------------------------------------------------------
#   Méthodes utilisées pour la manipulation des items en notation scientifique
# ----------------------------------------------------------------------------------------
  def set_valeur_texte(self,texte_valeur) :
      """ Sert à mettre à jour la notation scientifique"""
      try :
        if "R" in self.node.item.object.definition.type:
            if texte_valeur[0] != "'":
               clef=eval(texte_valeur)
               if str(clef) != str(texte_valeur) :
                  self.node.item.object.init_modif()
                  clefobj=self.node.item.object.GetNomConcept()
                  if not self.parent.appli.dict_reels.has_key(clefobj):
                     self.parent.appli.dict_reels[clefobj] = {}
                  self.parent.appli.dict_reels[clefobj][clef]=texte_valeur
                  self.parent.appli.dict_reels[clefobj]
                  self.node.item.object.fin_modif()
      except:
        pass


  def get_valeur_texte(self,valeur) :
     valeur_texte=""
     if "R" in self.node.item.object.definition.type:
        clefobj=self.node.item.object.GetNomConcept()
        if self.parent.appli.dict_reels.has_key(clefobj):
           if self.parent.appli.dict_reels[clefobj].has_key(valeur):
              valeur_texte=self.parent.appli.dict_reels[clefobj][valeur]
     return valeur_texte
 
