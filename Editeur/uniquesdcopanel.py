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
from uniqueassdpanel import UNIQUE_ASSD_Panel


class UNIQUE_SDCO_Panel(UNIQUE_ASSD_Panel):
  """
  Classe servant à définir le panneau correspondant à un mot-clé simple
  qui attend une valeur unique de type dérivé d'ASSD ou non encore
  existante (type CO(...) utilisé dans les macros uniquement)
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie de la valeur du mot-clé simple courant qui doit être une SD de type dérivé
      d'ASSD
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
      # affichage de la liste des SD existantes et du bon type
      self.listbox = Pmw.ScrolledListBox(self.frame_valeur,
                                         items=liste_noms_sd,
                                         labelpos='n',
                                         label_text="Structures de données du type\n requis par l'objet courant :",
                                         listbox_height = 6,
                                         selectioncommand=self.select_valeur_from_list,
                                         dblclickcommand=lambda s=self,c=self.valid_valeur : s.choose_valeur_from_list(c))
      self.listbox.component("listbox").bind("<Return>",lambda e,s=self,c=self.valid_valeur : s.choose_valeur_from_list(c))
      if liste_noms_sd != [] :
         self.listbox.place(relx=0.5,rely=0.3,relheight=0.4,anchor='center')
         self.b_co = Pmw.OptionMenu(self.frame_valeur,labelpos='w',label_text = "Nouveau concept : ", items = ('NON','OUI'),
                                         menubutton_width=10)
      else :
         self.b_co = Pmw.OptionMenu(self.frame_valeur,labelpos='w',label_text = "Nouveau concept : ", items = ('OUI',),
                                         menubutton_width=10)
      # affichage du bouton 'Nouveau concept'
      self.b_co.configure(command = self.ask_new_concept)
      if liste_noms_sd != [] :
         self.b_co.place(relx=0.05,rely=0.6,anchor='w')
      else :
         self.b_co.place(relx=0.05,rely=0.3,anchor='w')
      self.label_co = Label(self.frame_valeur,text='Nom du nouveau concept :')
      self.entry_co = Entry(self.frame_valeur)
      self.entry_co.bind('<Return>',self.valid_nom_concept_co)
      self.entry_co.bind('<KP_Enter>',self.valid_nom_concept_co)
      # affichage du label de la structure de donnée choisie
      self.l_resu = Label(self.frame_valeur,text='Structure de donnée choisie :')
      self.valeur_choisie = StringVar()
      self.label_valeur = Label(self.frame_valeur,textvariable=self.valeur_choisie)
      self.frame_valeur.update()
      self.aide = Label(self.frame_valeur,
                        text = aide,
                        wraplength=int(self.frame_valeur.winfo_width()*0.8),
                        justify='center')
      self.aide.place(relx=0.5,rely=0.85,anchor='n')
      # affichage de la valeur courante
      self.display_valeur()
      if liste_noms_sd == [] :
          self.b_co.invoke('OUI')
      
  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide du panneau
      """
      return """Double-cliquez sur la structure de donnée désirée
      pour valoriser le mot-clé simple courant ou cliquez sur NOUVEAU CONCEPT pour
      entrer le nom d'un concept non encore existant"""

  def valid_valeur(self):
      """
      Teste si la valeur fournie par l'utilisateur est une valeur permise :
      - si oui, l'enregistre
      - si non, restaure l'ancienne valeur
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      valeur = self.get_valeur()
      #print "valid_valeur",valeur

      self.erase_valeur()
      anc_val = self.node.item.get_valeur()
      test_CO=self.node.item.is_CO(anc_val)
      #PN essai pour bug dans MACRO_PROJ_BASE 
      valeur,validite=self.node.item.eval_valeur(valeur)
      test = self.node.item.set_valeur(valeur)
      if not test :
          mess = "impossible d'évaluer : %s " %`valeur`
          self.parent.appli.affiche_infos("Valeur du mot-clé non autorisée :"+mess)
          return
      #PN essai pour bug dans MACRO_PROJ_BASE 
      #elif self.node.item.isvalid() :
      elif validite: 
          self.parent.appli.affiche_infos('Valeur du mot-clé enregistrée')
          if test_CO:
             # il faut egalement propager la destruction de l'ancien concept
             self.node.item.delete_valeur_co(valeur=anc_val)
             # et on force le recalcul des concepts de sortie de l'etape
             self.node.item.object.etape.get_type_produit(force=1)
             # et le recalcul du contexte
             self.node.item.object.etape.parent.reset_context()
          self.node.parent.select()
      else :
          cr = self.node.item.get_cr()
          mess = "Valeur du mot-clé non autorisée :"+cr.get_mess_fatal()
          self.reset_old_valeur(anc_val,mess=mess)
          return

  def valid_nom_concept_co(self,event=None):
      """
      Lit le nom donné par l'utilisateur au concept de type CO qui doit être
      la valeur du MCS courant et stocke cette valeur
      """
      #print "valid_nom_concept_co"
      if self.parent.modified == 'n' : self.parent.init_modif()
      anc_val = self.node.item.get_valeur()
      if anc_val != None:
          # il faut egalement propager la destruction de l'ancien concept
          self.node.item.delete_valeur_co(valeur=anc_val)
          # et on force le recalcul des concepts de sortie de l'etape
          self.node.item.object.etape.get_type_produit(force=1)
          # et le recalcul du contexte
          self.node.item.object.etape.parent.reset_context()
      nom_concept = self.entry_co.get()
      #print "valid_nom_concept_co",nom_concept
      test,mess=self.node.item.set_valeur_co(nom_concept)
      if not test:
          # On n'a pas pu créer le concept
          self.parent.appli.affiche_infos(mess)
          return
      elif self.node.item.isvalid() :
          self.parent.appli.affiche_infos('Valeur du mot-clé enregistrée')
          self.node.parent.select()
      else :
          cr = self.node.item.get_cr()
          mess = "Valeur du mot-clé non autorisée :"+cr.get_mess_fatal()
          self.reset_old_valeur(anc_val,mess=mess)
          return

  def ask_new_concept(self,tag):
      """
      Crée une entry dans le panneau d'un MCS qui attend un concept OU un CO() afin de
      permettre à l'utilisateur de donner le nom du nouveau concept
      """
      new_concept = self.b_co.getcurselection()
      if new_concept == 'OUI':
          self.label_co.place(relx=0.05,rely=0.7)
          self.entry_co.place(relx=0.45,rely=0.7,relwidth=0.25)
          self.l_resu.place_forget()
          self.label_valeur.place_forget()
          self.entry_co.focus()
      elif new_concept == 'NON':
          # On est passe de OUI à NON, on supprime la valeur
# PN correction de bug (on passe de non a non et cela supprime la valeur)
# ajout du if de le ligne suivane
          if self.node.item.is_CO():
                self.node.item.delete_valeur_co()
                self.record_valeur(name=None,mess="Suppression CO enregistrée")
                self.label_co.place_forget()
                self.entry_co.place_forget()
                self.l_resu.place(relx=0.05,rely=0.7)
                self.label_valeur.place(relx=0.45,rely=0.7)
          
  def display_valeur(self):
      """
      Affiche la valeur de l'objet pointé par self
      """
      valeur = self.node.item.get_valeur()
      #print "display_valeur",valeur
      if valeur == None or valeur == '': 
         self.valeur_choisie.set('')
         return # pas de valeur à afficher ...
      # il faut configurer le bouton si la valeur est un objet CO
      # sinon afficher le nom du concept dans self.valeur_choisie
      if self.node.item.is_CO():
          #print "display_valeur.is_CO"
          self.b_co.invoke('OUI')
          self.entry_co.insert(0,valeur.nom)
      else:
          self.valeur_choisie.set(valeur.nom)

  def record_valeur(self,name=None,mess='Valeur du mot-clé enregistrée'):
      """
      Enregistre  val comme valeur de self.node.item.object SANS faire de test de validité
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      if name != None:
          valeur =name
      else :
          self.entry_co.delete(0,END)
          valeur= self.entry_co.get()
      self.node.item.set_valeur_co(valeur)
      self.parent.appli.affiche_infos(mess)
      # On met a jour le display dans le panneau
      self.display_valeur()
      if self.node.item.isvalid():
          self.node.parent.select()


