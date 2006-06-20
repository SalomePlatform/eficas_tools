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
from  newsimppanel import newSIMPPanel


class PLUSIEURS_Panel(newSIMPPanel):
  """
  Classe virtuelle servant de classe mère à toutes celles définissant
  un panneau pour un mot-clé simple qui attend une liste de valeurs
  """
  def accepte_modifs_valeur(self,min,max,liste=None):
      """
      Méthode qui récupère la liste des valeurs donnée par l'utilisateur
      et l'affecte au mot-clé courant.
      le parametre None n'est pas rempli sauf par l appel a partir de fonctionpanel
      """
      if liste==None:
         l1_valeurs = self.Liste_valeurs.get_liste()
      else:
         l1_valeurs = liste

      #nettoyage de la liste
      l_valeurs=[]
      for  val in l1_valeurs :
        if val != '' and val != None :
           l_valeurs.append(val)
    
      longueur = len(l_valeurs)
      if longueur < min or longueur > max :
          self.parent.appli.affiche_infos("Valeur refusée : nombre d'éléments incorrect dans la liste")
          return
      if longueur > 1:
         valeur = tuple(l_valeurs)
      elif longueur == 1:
         valeur = l_valeurs[0]
      else:
         valeur = None

      self.parent.appli.affiche_infos("Valeur acceptée")
      self.record_valeur(valeur)
      # fermeture de la fenêtre de sélection
      if self.ajout_valeurs:
          self.ajout_valeurs.quit()
          
  def annule_modifs_valeur(self):
      """
      RAZ de la liste des valeurs (annule toutes les valeurs saisies par l'utilisateur)
      """
      self.node.select()
      # fermeture de la fenêtre de sélection
      if self.ajout_valeurs:
          self.ajout_valeurs.quit()
          
  def add_valeur_sans_into(self,name=None,encorevalide=1):
      """
      Tente d'ajouter la valeur fournie (name) à la liste courante :
        - si la valeur est acceptable, elle est ajoutée dans la liste des valeurs
        - sinon elle est refusée

      encorevalide vaut 1 si le validateur trouve l item et la liste correctes
                        0 si le validateur trouve la valeur de l item incorrecte
                       -1 si le validateur trouve la liste incorrecte
      """
      valeur = name
      commentaire="Valeur incorrecte : ajout à la liste refusé"
      testvalide=1

      # Pas de traitement des valeurs nulles ( a priori clic involontaire
      if (valeur == None or valeur =="") :
          commentaire = "Pas de saisie des valeurs nulles"
          encorevalide = -2 
          testtype=0
      else :
          testtype = self.node.item.object.verif_type(valeur)
          if not testtype :
               commentaire ="Type de la valeur incorrecte"
               encorevalide=-2
                
      if (encorevalide ==0) :
         commentaire=self.node.item.info_erreur_item()
      if (encorevalide == -1) :
         commentaire=self.node.item.info_erreur_liste()
         # On traite le cas ou la liste n est pas valide pour un pb de cardinalite
         min,max = self.node.item.GetMinMax()
         if len(self.Liste_valeurs.get_liste()) >= max : 
            commentaire="La liste a déjà atteint le nombre maximum d'éléments,ajout refusé"

      if testvalide and (encorevalide == 1):
         min,max = self.node.item.GetMinMax()

         if testtype :
            liste_valeurs = self.Liste_valeurs.get_liste()
            if len(liste_valeurs) >= max :
                commentaire="La liste a déjà atteint le nombre maximum d'éléments,ajout refusé"
            else :
               if (self.Liste_valeurs.selection != None):
                   ligne=self.Liste_valeurs.cherche_selected_item()
                   liste_valeurs.insert(ligne,valeur)
               else :
                   liste_valeurs.append(valeur)
               try :
                  self.set_valeur_texte(str(self.entry.get()))
               except :
                  pass
               self.Liste_valeurs.put_liste(liste_valeurs)
               self.erase_valeur()
               commentaire="Nouvelle valeur acceptée"
         else :
            commentaire ="Type de la valeur incorrecte"

      self.parent.appli.affiche_infos(commentaire)

  def sup_valeur_sans_into(self,name=None):
      """
      Méthode qui sert à retirer de la liste des valeurs la valeur sélectionnée
      """
      try:
          self.Liste_valeurs.remove_selected_item()
          self.display_valeur(self.selected_valeur)
          self.selected_valeur = None      
      except:
          # la valeur sélectionnée n'est pas dans la liste
          return

  def display_valeur(self,val=None):
      """
      Affiche la valeur passée en argument dans l'entry de saisie.
      Par défaut affiche la valeur du mot-clé simple
      """
      if not val :
          #valeur = self.node.item.getval()
          valeur = self.node.item.object.getval()
      else:
          valeur = val
      self.entry.delete(0,END)
      if not valeur : return
      self.entry.insert(0,str(valeur))
      
