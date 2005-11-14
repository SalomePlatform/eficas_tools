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
from widgets import askopenfilename
from widgets import showinfo

from Noyau.N_CR import justify_text
from utils import substract_list
from plusieursbasepanel import PLUSIEURS_BASE_Panel


class FONCTION_Panel(PLUSIEURS_BASE_Panel):
  def makeValeurPage(self,page):
      """
      Crée la page de saisie d'une liste de valeurs à priori quelconques,
      cad qui ne sont  pas à choisir dans une liste prédéfinie
      """
      genea=self.node.item.get_genealogie()
      if "VALE" in genea:
	self.nb_valeurs=2
      if "VALE_C" in genea:
	self.nb_valeurs=3
      # On récupère la bulle d'aide du panneau, l'objet, l'aide,min et max (cardinalité de la liste),
      # et la liste des valeurs déjà affectées à l'objet courant
      bulle_aide=self.get_bulle_aide()
      objet_mc = self.node.item.get_definition()
      aide = self.get_aide()
      aide = justify_text(texte=aide)
      min,max = self.node.item.GetMinMax()
      l_valeurs = self.node.item.GetListeValeurs()
      l2_valeurs=self.decoupeListeValeurs(l_valeurs)

      # création des frames globales
      self.frame1 = Frame(page,relief='groove',bd=2)
      self.frame2 = Frame(page)
      self.frame1.place(relx=0.,rely=0.,relwidth=1.,relheight=0.85)
      self.frame2.place(relx=0.,rely=0.85,relwidth=1,relheight=0.15)
      self.frame_right = Frame(self.frame1)
      self.frame_right.place(relx=0.35,rely=0.,relwidth=0.65,relheight=1.)

      # création des frames internes
      self.frame_valeurs = Frame(self.frame1)
      self.frame_valeurs.place(relx=0.02,rely=0.05,relwidth=0.35,relheight=0.95)
      self.frame_boutons_fleches = Frame(self.frame_right)
      self.frame_boutons_fleches.place(relx=0.,rely=0.2,relwidth=0.2,relheight=0.5)
      self.frame_choix = Frame(self.frame_right)
      self.frame_choix.place(relx=0.2,rely=0.2,relwidth=0.7,relheight=0.5)
      self.frame_aide = Frame(self.frame_right)
      self.frame_aide.place(relx=0.1,rely=0.7,relwidth=0.8,relheight=0.3)
      self.frame_boutons = Frame(self.frame2)
      self.frame_boutons.place(relx=0.35,rely=0.,relwidth=0.5,relheight=1.)
      for fram in (self.frame1,self.frame2,self.frame_right,self.frame_valeurs,
                 self.frame_boutons_fleches,self.frame_choix,self.frame_aide,self.frame_boutons):
          fram.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
          fram.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

      # création des objets dans les frames
      liste_commandes_valeurs = (("<Button-1>",self.selectValeur),
                                 ("<Button-3>",self.deselectValeur),
                                 ("<Double-Button-1>",self.afficheValeurListe))
      self.Liste_valeurs = ListeChoix(self,self.frame_valeurs,l2_valeurs,liste_commandes = liste_commandes_valeurs,
                                      titre="Valeur(s) actuelle(s)")

      # Création de l'entry ou de la liste des SD
      self.label = Label(self.frame_choix,text="Valeur :")
      self.make_entry(frame = self.frame_choix,command = self.add_double_valeur_plusieurs_base)
      self.label.place(relx=0.05,rely=0.5)

      # Création d'un bouton "Importer ..." sur le panel.
      bouton_valeurs_fichier = Button(self.frame_choix,
                                      text="Importer ...",
                                      command=self.select_in_file)
      bouton_valeurs_fichier.place(relx=0.28,rely=0.7,relwidth=0.6)
      self.ajout_valeurs = None

      # boutons Ajouter et Supprimer
      bouton_add = Button(self.frame_boutons_fleches,
                          image = images.get_image('arrow_left'),
                          command = self.add_double_valeur_plusieurs_base)
      bouton_sup = Button(self.frame_boutons_fleches,
                          image = images.get_image('arrow_right'),
                          command = self.sup_valeur_sans_into)
      bouton_add.place(relx=0.3,rely=0.35)
      bouton_sup.place(relx=0.3,rely=0.65)
      # affichage de l'aide
      self.frame_aide.update()
      self.aide = Label(self.frame_aide,
                        text = aide,
                        justify='center',
                        anchor='center',
			wraplength=int(self.frame_aide.winfo_width()*0.8))
      self.aide.place(relx=0.5,rely=0.5,anchor='center',relwidth=1)
      self.Liste_valeurs.affiche_liste()
      # boutons Accepter et Annuler
      bouton_accepter = Button(self.frame_boutons,
                               text='Valider',
                               command = lambda s=self,m=min,M=max : s.accepte_modifs_valeur_recolle(m,M))
      bouton_annuler = Button(self.frame_boutons,
                              text = 'Annuler',
                              command = self.annule_modifs_valeur)
      for but in (bouton_accepter,bouton_annuler):
          but.pack(side='left',padx=4)


  def afficheValeurListe(self,name):
      self.display_valeur(name)

  def decoupeListeValeurs(self,liste):
      #decoupe la liste des valeurs en n ( les x puis les y)
      nb=self.nb_valeurs
      l_valeurs=[]
      if (len(liste)%nb != 0):
          message="La cardinalité n'est pas correcte, la dernière valeur est ignorée"
          showinfo("Problème",message)
      for i in range(len(liste)/nb) :
          if (nb==2):
              t=(liste[i*nb], liste[i*nb+1])
          else:
              t=(liste[i*nb], liste[i*nb+1], liste[i*nb+2])
          l_valeurs.append(t)
      return l_valeurs


  def accepte_modifs_valeur_recolle(self,min,max):
      l_valeurs=[]
      l1_valeurs = self.Liste_valeurs.get_liste()
      for val in l1_valeurs :
	  for item in val :
	     l_valeurs.append(item) 
      self.accepte_modifs_valeur(min,max,l_valeurs)


  def add_double_valeur_plusieurs_base(self):
      # on verifie qu'il s agit bien d un tuple
      # on enleve les parentheses eventuelles
      #doublevaleur_entree,validite,commentaire=self.get_valeur_double()
      doublevaleur_entree= self.entry.get()
      try:
        if doublevaleur_entree[0]=='(' :
           doublevaleur_entree=doublevaleur_entree[1:-1]
        if doublevaleur_entree[-1]==')' :
           doublevaleur_entree=doublevaleur_entree[0:-2]
	val1=doublevaleur_entree.split(',')[0] 
	val2=doublevaleur_entree.split(',')[1] 
        saisie=(val1,val2)
        if (self.nb_valeurs==3):
	    val3=doublevaleur_entree.split(',')[2] 
            saisie=(val1,val2,val3)
      except :
        commentaire = "%s n est pas un tuple de la forme (x,y)" %`doublevaleur_entree`
        if (self.nb_valeurs==3):
	    commentaire = "%s n est pas un tuple de la forme (x,y,z)" %`doublevaleur_entree`
        self.parent.appli.affiche_infos(commentaire)
        return

      # et seulement d un tuple
      try:
	val=doublevaleur_entree.split(',')[self.nb_valeurs]
        commentaire = "%s n est pas un tuple de la forme (x,y)" %`doublevaleur_entree`
        if (self.nb_valeurs==3):
	    commentaire = "%s n est pas un tuple de la forme (x,y,z)" %`doublevaleur_entree`
        self.parent.appli.affiche_infos(commentaire)
        self.parent.appli.affiche_infos(commentaire)
        return
      except :
        # c est la le cas normal
	pass

      # on verifie la validite des valeurs sont correctes
      valeur,validite=self.node.item.eval_valeur(saisie)
      if not validite :
        commentaire = "impossible d'évaluer : %s " %`doublevaleur_entree`
        self.parent.appli.affiche_infos(commentaire)
	return

      # on verifie la validite de la liste
      liste=[]
      l1_valeurs = self.Liste_valeurs.get_liste()
      for val in l1_valeurs :
	  for item in val :
	     liste.append(item) 
      validite_liste=self.node.item.valide_liste_partielle(valeur[0],liste)
      if not validite_liste:
        commentaire = "impossible d'ajouter %s a la liste " %`doublevaleur_entree`
        self.parent.appli.affiche_infos(commentaire)
	return
      # liste a deja ete modifiee par l appel precedent a valide_liste_partielle 
      # et contient deja valeur[0]
      validite_liste=self.node.item.valide_liste_partielle(valeur[1],liste)
      if not validite_liste:
        commentaire = "impossible d'ajouter %s a la liste " %`doublevaleur_entree`
        self.parent.appli.affiche_infos(commentaire)
	return
     
      # si une valeur est selectionnee on insere apres 
      # sinon on ajoute la valeur à la fin
      if (self.Liste_valeurs.selection != None):
         ligne=self.Liste_valeurs.cherche_selected_item()
         if self.nb_valeurs==2:
            l1_valeurs.insert(ligne,(valeur[0],valeur[1]))
         else :
            l1_valeurs.insert(ligne,(valeur[0],valeur[1],valeur[2]))
      else :
         if self.nb_valeurs==2:
            l1_valeurs.append((valeur[0],valeur[1]))
         else :
            l1_valeurs.append((valeur[0],valeur[1],valeur[2]))
      i = 0
      while i < self.nb_valeurs : 
         self.set_valeur_texte(saisie[i])
         i=i+1
      self.Liste_valeurs.put_liste(l1_valeurs)
      self.Liste_valeurs.affiche_liste()


  def display_valeur(self,val=None):
      """
      Affiche la valeur passée en argument dans l'entry de saisie.
      Par défaut affiche la valeur du mot-clé simple
      Doit être redéfinie pour un pb avec les parametres dans un tuple
      """
      if not val :
          valeur = self.node.item.object.getval()
      else:
          valeur = val
      if not valeur : return

      try:
        affiche="("
        separe=""
	for val in valeur:
	    affiche=affiche+separe+str(val)
	    separe=","
        affiche=affiche+")"
        self.entry.delete(0,END)
	self.entry.insert(0,affiche)
      except :
	self.entry.delete(0,END)

# Surcharge de select in file pour prendre en compte la saisie de tuple
  def select_in_file(self):
      """ Permet d'ouvrir un fichier choisi par l'utilisateur. """
      nom_fichier = askopenfilename(title="Choix fichier :")

      if not nom_fichier:
          return

      try:
          f = open(nom_fichier, "rb")
          selection_texte = f.read()
          f.close()
          self.add_double_valeur_plusieurs_base = FenetreDeSelection(self,
                                                  self.node.item,
                                                  self.parent.appli,
                                                  titre="Sélection de valeurs",
                                                  texte=selection_texte,
                                                  cardinal = self.nb_valeurs)
      except:
          traceback.print_exc()
          showinfo("Erreur de fichier","impossible d'ouvir le fichier "+nom_fichier)

