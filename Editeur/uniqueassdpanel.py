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


class UNIQUE_ASSD_Panel(UNIQUE_Panel):
  """
  Classe servant à définir le panneau associé aux objets qui attendent une valeur unique
  d'un type dérivé d'ASSD
  """
  def valid_valeur_automatique(self):
      """
         Réalise la validation d'un concept sans remonter dans le
         node parent dans le cas ou il n'y a qu'un concept possible (liste de longueur 1)
         Identique à valid_valeur moins appel de self.node.parent.select()
         On pourrait supposer que le seul concept présent est valide et donc ne pas
         réaliser tous les tests de vérification.
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      valeur = self.get_valeur()
      self.erase_valeur()
      anc_val = self.node.item.get_valeur()
      valeur,validite=self.node.item.eval_valeur_item(valeur)
      test = self.node.item.set_valeur(valeur)
      if not test :
          mess = "impossible d'évaluer : %s " %`valeur`
          self.parent.appli.affiche_infos("Valeur du mot-clé non autorisée :"+mess)
      elif self.node.item.isvalid() :
          self.parent.appli.affiche_infos('Valeur du mot-clé enregistrée')
          if self.node.item.get_position()=='global':
              self.node.etape.verif_all()
          elif self.node.item.get_position()=='global_jdc':
              self.node.racine.verif_all()
          else :
              self.node.parent.verif()
          self.node.update()
      else :
          cr = self.node.item.get_cr()
          mess = "Valeur du mot-clé non autorisée :"+cr.get_mess_fatal()
          self.reset_old_valeur(anc_val,mess=mess)

  def makeValeurPage(self,page):
      """
          Génère la page de saisie de la valeur du mot-clé simple courant qui doit être une 
          SD de type dérivé d'ASSD
      """
      # Récupération de l'aide associée au panneau, de l'aide destinée à l'utilisateur,
      # et de la liste des SD du bon type (constituant la liste des choix)
      bulle_aide=self.get_bulle_aide()
      aide=self.get_aide()
      aide= justify_text(texte=aide)
      liste_noms_sd = self.node.item.get_sd_avant_du_bon_type()
      # Remplissage du panneau
      self.valeur_choisie = StringVar()
      self.valeur_choisie.set('')
      min,max =  self.node.item.GetMinMax()
      if (min == 1 and min == max and len(liste_noms_sd)==1):
          if self.valeur_choisie.get() != liste_noms_sd[0]:
	     self.valeur_choisie.set(liste_noms_sd[0])
             self.valid_valeur_automatique()
	 
      self.frame_valeur = Frame(page)
      self.frame_valeur.pack(fill='both',expand=1)
      self.frame_valeur.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      self.frame_valeur.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      self.listbox = Pmw.ScrolledListBox(self.frame_valeur,
                                         items=liste_noms_sd,
                                         labelpos='n',
                                         label_text="Structures de données du type\n requis par l'objet courant :",
                                         listbox_height = 6,
                                         selectioncommand=self.select_valeur_from_list,
                                         dblclickcommand=lambda s=self,c=self.valid_valeur : s.choose_valeur_from_list(c))
      self.listbox.place(relx=0.5,rely=0.3,relheight=0.4,anchor='center')
      Label(self.frame_valeur,text='Structure de donnée choisie :').place(relx=0.05,rely=0.6)
      #self.label_valeur = Label(self.frame_valeur,textvariable=self.valeur_choisie)
      Label(self.frame_valeur,textvariable=self.valeur_choisie).place(relx=0.5,rely=0.6)
      # affichage de la valeur courante
      self.display_valeur()

  def get_bulle_aide(self):
      """
      Retourne l'aide associée au panneau
      """
      return "Double-cliquez sur la structure de donnée désirée pour valoriser le mot-clé simple courant"

  def get_aide(self):
      """
      Retourne la phrase d'aide indiquant de quel type doit être la valeur à donner par l'utilisateur
      """
      mc = self.node.item.get_definition()
      type = mc.type[0].__name__  
      if len(mc.type)>1 :
          for typ in mc.type[1:] :
              type = type + ' ou '+typ.__name__
      commentaire="Un objet de type "+type+" est attendu"
      aideval=self.node.item.aide()
      commentaire=commentaire +"\n"+ aideval
      return commentaire

    
  def select_valeur_from_list(self):
      """
      Affecte à valeur choisie la sélection courante dans la liste des choix proposée
      """
      if len(self.listbox.get()) == 0 : return
      choix = self.listbox.getcurselection()[0]
      self.valeur_choisie.set(choix)

  def choose_valeur_from_list(self,command):
      """
      Affecte à valeur choisie la sélection courante dans la liste des choix proposée
      Exécute command
      """
      if len(self.listbox.get()) == 0 : return
      choix = self.listbox.getcurselection()[0]
      self.valeur_choisie.set(choix)
      apply(command,(),{})

  def get_valeur(self):
      """
      Retourne la valeur donnée par l'utilisateur au MCS
      """
      return self.valeur_choisie.get()
    
  def display_valeur(self):
      """
      Affiche la valeur de l'objet pointé par self
      """
      valeur = self.node.item.get_valeur()
      if valeur == None or valeur == '' : return # pas de valeur à afficher ...
      self.valeur_choisie.set(valeur.nom)

  def erase_valeur(self):
      pass

