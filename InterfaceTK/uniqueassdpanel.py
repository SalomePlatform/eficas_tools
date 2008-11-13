# -*- coding: utf-8 -*-
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


class UNIQUE_ASSD_Panel(UNIQUE_Panel):
  """
  Classe servant � d�finir le panneau associ� aux objets qui attendent une valeur unique
  d'un type d�riv� d'ASSD
  """
  def valid_valeur_automatique(self):
      """
         R�alise la validation d'un concept sans remonter dans le
         node parent dans le cas ou il n'y a qu'un concept possible (liste de longueur 1)
         Identique � valid_valeur moins appel de self.node.parent.select()
         On pourrait supposer que le seul concept pr�sent est valide et donc ne pas
         r�aliser tous les tests de v�rification.
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      valeur = self.get_valeur()
      self.erase_valeur()
      anc_val = self.node.item.get_valeur()
      valeur,validite=self.node.item.eval_valeur_item(valeur)
      test = self.node.item.set_valeur(valeur)
      if not test :
          mess = "impossible d'�valuer : %s " %`valeur`
          self.parent.appli.affiche_infos("Valeur du mot-cl� non autoris�e :"+mess)
      elif self.node.item.isvalid() :
          self.parent.appli.affiche_infos('Valeur du mot-cl� enregistr�e')
          #if self.node.item.get_position()=='global':
              #self.node.etape.verif_all()
          #elif self.node.item.get_position()=='global_jdc':
              #self.node.racine.verif_all()
          #else :
              #self.node.parent.verif()
          #self.node.update()
      else :
          cr = self.node.item.get_cr()
          mess = "Valeur du mot-cl� non autoris�e :"+cr.get_mess_fatal()
          self.reset_old_valeur(anc_val,mess=mess)

  def makeValeurPage(self,page,reel="non"):
      """
          G�n�re la page de saisie de la valeur du mot-cl� simple courant qui doit �tre une 
          SD de type d�riv� d'ASSD
      """
      # R�cup�ration de l'aide associ�e au panneau, de l'aide destin�e � l'utilisateur,
      # et de la liste des SD du bon type (constituant la liste des choix)
      bulle_aide=self.get_bulle_aide()
      aide=self.get_aide()
      aide= justify_text(texte=aide)
      liste_noms_sd = self.node.item.get_sd_avant_du_bon_type()

      # Remplissage du panneau
      self.valeur_choisie = StringVar()
      self.valeur_choisie.set('')
      min,max =  self.node.item.GetMinMax()
      if (min == 1 and min == max and len(liste_noms_sd)==1 ):
          if self.valeur_choisie.get() != liste_noms_sd[0]:
            if ('R' not in self.node.item.get_type()) :
                self.valeur_choisie.set(liste_noms_sd[0])
                self.valid_valeur_automatique()
         
      self.frame_valeur = Frame(page)
      self.frame_valeur.pack(fill='both',expand=1)
      self.frame_valeur.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      self.frame_valeur.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      self.listbox = Pmw.ScrolledListBox(self.frame_valeur,
                                         items=liste_noms_sd,
                                         labelpos='n',
                                         label_text="Structures de donn�es du type\n requis par l'objet courant :",
                                         listbox_height = 6,
                                         selectioncommand=self.select_valeur_from_list,
                                         dblclickcommand=lambda s=self,c=self.valid_valeur : s.choose_valeur_from_list(c))
      self.listbox.place(relx=0.5,rely=0.3,relheight=0.4,anchor='center')
      Label(self.frame_valeur,text='Structure de donn�e choisie :').place(relx=0.05,rely=0.6)
      Label(self.frame_valeur,textvariable=self.valeur_choisie).place(relx=0.5,rely=0.6)
      self.but_val = Button(self.frame_valeur,text = "Valider",command= self.Choisir)
      self.but_val.place(relx=0.3,rely=0.8,relwidth=0.35)

      # affichage de la valeur courante
      self.display_valeur()
      if self.__class__.__name__ == 'UNIQUE_ASSD_Panel_Reel' :
        Label(self.frame_valeur,text='Valeur R�elle').place(relx=0.1,rely=0.9)
        self.entry = Entry(self.frame_valeur,relief='sunken')
        self.entry.place(relx=0.28,rely=0.9,relwidth=0.6)
        self.entry.bind("<Return>",lambda e,c=self.valid_valeur_reel:c())
        self.entry.bind("<KP_Enter>",lambda e,c=self.valid_valeur_reel:c())



  def get_bulle_aide(self):
      """
      Retourne l'aide associ�e au panneau
      """
      return "Double-cliquez sur la structure de donn�e d�sir�e pour valoriser le mot-cl� simple courant"

  def get_aide(self):
      """
      Retourne la phrase d'aide indiquant de quel type doit �tre la valeur � donner par l'utilisateur
      """
      mc = self.node.item.get_definition()
      try :
              type = mc.type[0].__name__  
      except :
        type = str(mc.type[0])
      if len(mc.type)>1 :
          for typ in mc.type[1:] :
              try :
                l=typ.__name__
              except:
                l=str(typ)
              type = type + ' ou '+l
      commentaire="Un objet de type "+type+" est attendu"
      aideval=self.node.item.aide()
      commentaire=commentaire +"\n"+ aideval
      return commentaire

    
  def select_valeur_from_list(self):
      """
      Affecte � valeur choisie la s�lection courante dans la liste des choix propos�e
      """
      if len(self.listbox.get()) == 0 : return
      if len(self.listbox.getcurselection()) == 0 : return
      choix = self.listbox.getcurselection()[0]
      self.valeur_choisie.set(choix)
      self.listbox.component("listbox").focus_set()

  def choose_valeur_from_list(self,command):
      """
      Affecte � valeur choisie la s�lection courante dans la liste des choix propos�e
      Ex�cute command
      """
      if len(self.listbox.get()) == 0 : return
      if len(self.listbox.getcurselection()) == 0 : return
      choix = self.listbox.getcurselection()[0]
      self.valeur_choisie.set(choix)
      apply(command,(),{})

  def Choisir(self) :
      #Appeler par le bouton Valider
      self.choose_valeur_from_list(self.valid_valeur)
      
  def get_valeur(self):
      """
      Retourne la valeur donn�e par l'utilisateur au MCS
      """
      return self.valeur_choisie.get()
    
  def display_valeur(self):
      """
      Affiche la valeur de l'objet point� par self
      """
      valeur = self.node.item.get_valeur()
      if valeur == None or valeur == '' : return # pas de valeur � afficher ...
      self.valeur_choisie.set(getattr(valeur,"nom","unknown"))

  def erase_valeur(self):
      pass

  def appel_make(self,page):
      self.makeValeurPage(page,reel="oui")
      
class UNIQUE_ASSD_Panel_Reel(UNIQUE_ASSD_Panel):
 
  def valid_valeur_reel(self):
      if self.parent.modified == 'n' : self.parent.init_modif()
      anc_val = self.node.item.get_valeur()
      valeurentree = self.entry.get()
      self.valeur_choisie.set(valeurentree)
      self.valid_valeur()

  def display_valeur(self):
      valeur = self.node.item.get_valeur()
      if valeur == None or valeur == '' : return # pas de valeur � afficher ...
      if type(valeur) == types.FloatType :
         self.valeur_choisie.set(valeur)
      else :
         self.valeur_choisie.set(valeur.nom)

       

