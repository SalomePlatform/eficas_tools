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
from widgets import showinfo
from widgets import askopenfilename
from widgets import ListeChoix
from widgets import FenetreDeSelection
from widgets import FenetreDeParametre

from Noyau.N_CR import justify_text
from utils import substract_list
from plusieurspanel import PLUSIEURS_Panel



class PLUSIEURS_BASE_Panel(PLUSIEURS_Panel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de donner une liste de valeurs qui ne sont pas
  à choisir dans une liste discrètes et qui sont de type de base :
  entier, réel, string,...
  """
  def makeValeurPage(self,page):
      """
      Crée la page de saisie d'une liste de valeurs à priori quelconques,
      cad qui ne sont  pas à choisir dans une liste prédéfinie
      """
      # On récupère la bulle d'aide du panneau, l'objet, l'aide,min et max (cardinalité de la liste),
      # et la liste des valeurs déjà affectées à l'objet courant
      bulle_aide=self.get_bulle_aide()
      objet_mc = self.node.item.get_definition()
      aide = self.get_aide()
      aide = justify_text(texte=aide)
      min,max = self.node.item.GetMinMax()
      l_valeurs = self.node.item.GetListeValeurs()

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
      self.frame_choix.place(relx=0.2,rely=0.2,relwidth=0.7,relheight=0.8)
      self.frame_aide = Frame(self.frame_right)
      self.frame_aide.place(relx=0.1,rely=0.8,relwidth=0.8,relheight=0.2)
      self.frame_boutons = Frame(self.frame2)
      self.frame_boutons.place(relx=0.35,rely=0.,relwidth=0.3,relheight=1.)
      for fram in (self.frame1,self.frame2,self.frame_right,self.frame_valeurs,
                 self.frame_boutons_fleches,self.frame_choix,self.frame_aide,self.frame_boutons):
          fram.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
          fram.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

      # création des objets dans les frames
      liste_commandes_valeurs = (("<Button-1>",self.selectValeur),
                                 ("<Button-3>",self.deselectValeur),
                                 ("<Double-Button-1>",self.sup_valeur_sans_into))
      self.Liste_valeurs = ListeChoix(self,self.frame_valeurs,l_valeurs,liste_commandes = liste_commandes_valeurs,
                                      titre="Valeur(s) actuelle(s)")

      # Création de l'entry ou de la liste des SD
      # PN : pour ajouter les validators
      self.label = Label(self.frame_choix,text="Valeur :")
      self.make_entry(frame = self.frame_choix,command = self.add_valeur_plusieurs_base)
      self.label.place(relx=0.05,rely=0.3)

      # Création d'un bouton "Importer ..." et d'un bouton "Paramatres" sur le panel.
      bouton_valeurs_fichier = Button(self.frame_choix,
                                      text="Importer",
                                      command=self.select_in_file)
      bouton_valeurs_fichier.place(relx=0.28,rely=0.4,relwidth=0.6)
      bouton_parametres = Button(self.frame_choix, text="Parametres", command=self.affiche_parametre)
      bouton_parametres.place(relx=0.28,rely=0.6,relwidth=0.6)
      self.ajout_valeurs = None

      # boutons Ajouter et Supprimer
      bouton_add = Button(self.frame_boutons_fleches,
                          image = images.get_image('arrow_left'),
                          command = self.add_valeur_plusieurs_base)
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
                               command = lambda s=self,m=min,M=max : s.accepte_modifs_valeur(m,M))
      bouton_annuler = Button(self.frame_boutons,
                              text = 'Annuler',
                              command = self.annule_modifs_valeur)
      for but in (bouton_accepter,bouton_annuler):
          but.pack(side='left',padx=5)

  def affiche_parametre(self) :
      if self.node.item.get_liste_param_possible() != [ ]:
         txtparam=""
	 for param in self.node.item.get_liste_param_possible():
	    txtparam=txtparam+repr(param)+"\n"
	 if txtparam=="":
	    showerror("Aucun parametre ","Pas de parametre de ce type")
	 else :
	    self.fenetreparam=FenetreDeParametre( self, self.node.item, self.parent.appli, txtparam)


  def add_valeur_plusieurs_base(self,name=None):
      if name != None :
         valeur = name
      else:
         valeur,validite,commentaire=self.get_valeur()
         if not validite :
            self.parent.appli.affiche_infos(commentaire)
            return

      encorevalide=self.node.item.valide_item(valeur)
      if encorevalide :
         listecourante=self.Liste_valeurs.get_liste()
         encorevalide=self.node.item.valide_liste_partielle(valeur,listecourante)
         if not encorevalide : encorevalide = -1
      self.add_valeur_sans_into(valeur,encorevalide)
    
  def select_in_file(self):
      """ Permet d'ouvrir un fichier choisi par l'utilisateur. """
      nom_fichier = askopenfilename(title="Choix fichier :")

      if not nom_fichier:
          return

      try:
          f = open(nom_fichier, "rb")
          selection_texte = f.read()
          f.close()
          self.ajout_valeurs = FenetreDeSelection(self, 
	                                          self.node.item,
						  self.parent.appli,
                                        	  titre="Sélection de valeurs",
                                        	  texte=selection_texte)
      except:
          traceback.print_exc()
          showinfo("Erreur de fichier","impossible d'ouvir le fichier "+nom_fichier)
          
  def get_bulle_aide(self):
      """
      Retourne l'aide associée au panneau courant
      """
      return """Taper dans la boîte de saisie de droite la valeur que
      vous voulez affecter au mot-clé simple.
      - Cliquez sur la flèche gauche ou pressez <Return> pour la faire glisser
      dans la liste des valeurs que vous voulez affecter au mot-clé simple
      - Un clic sur une valeur de la liste la sélectionne
      - Un clic sur la flèche droite ou un double-clic retire la valeur
      sélectionnée de la liste
      - Cliquez sur 'Valider' pour que la nouvelle valeur désirée soit affectée
      au mot-clé simple
      - Cliquez sur 'Annuler' pour annuler toutes les modifications faites
      depuis le dernier clic sur 'Valider'"""

  def get_aide(self):
      """
      Retourne la phrase d'aide indiquant de quel type de base doivent être les valeurs
      que saisit l'utilisateur
      """
      commentaire=""
      mc = self.node.item.get_definition()
      d_aides = { 'TXM' : 'chaînes de caractères',
                  'R'   : 'réels',
                  'I'   : 'entiers',
                  'C'   : 'complexes'}
      type = mc.type[0]
      if not d_aides.has_key(type) : return 'Type de base inconnu'
      if mc.min == mc.max:
          commentaire="Une liste de "+d_aides[type]+" de longueur " + `mc.min`  + " est attendue"
      else :
          commentaire="Une liste de "+d_aides[type]+" est attendue (min="+`mc.min`+",max="+`mc.max`+')'

      aideval=self.node.item.aide()
      commentaire=commentaire +"\n"+aideval
      return commentaire

  def make_entry(self,frame,command):
      """
      Crée l'entry de saisie de la valeur souhaitée : distingue le
      cas d'un complexe attendu, d'une autre valeur quelconque
      """
      if self.node.item.wait_complex():
          self.typ_cplx=StringVar()
          self.typ_cplx.set('RI')
          rb1 = Radiobutton(frame, text='RI',variable=self.typ_cplx,value='RI')
          rb2 = Radiobutton(frame, text='MP',variable=self.typ_cplx,value='MP')
          self.entry1 = Pmw.EntryField(frame,validate='real')
          self.entry2 = Pmw.EntryField(frame,validate='real')
          rb1.place(relx=0.05,rely = 0.4)
          rb2.place(relx=0.05,rely = 0.6)
          self.entry1.component('entry').bind("<Return>",lambda e,s=self:s.entry2.component('entry').focus)
          self.entry2.component('entry').bind("<Return>",lambda e,c=command:c())
          self.entry1.place(relx=0.27,rely = 0.5,relwidth=0.35)
          self.entry2.place(relx=0.65,rely = 0.5,relwidth=0.35)
          self.entry1.focus()
      else:
          self.entry = Entry(frame,relief='sunken')
          self.entry.place(relx=0.28,rely=0.2,relwidth=0.6)
          self.entry.bind("<Return>",lambda e,c=command:c())
          self.entry.focus()

  def get_valeur(self):
      """
      Retourne la valeur saisie par l'utilisateur dans self.entry
      """
      if hasattr(self,'entry'):
         # Traitement d'une entree unique
         valeurentree = self.entry.get()
         valeur,validite=self.node.item.eval_valeur(valeurentree)
         if not validite :
            commentaire = "impossible d'évaluer : %s " %`valeurentree`
         else:
            commentaire = ""
         return valeur,validite,commentaire
      else:
         # Traitement d'une entree de type complexe
         try:
            valeur= (self.typ_cplx.get(),
                     string.atof(self.entry1.get()),
                     string.atof(self.entry2.get()))
            return valeur,1,""
         except:
            #traceback.print_exc()
            return None,0,"impossible d'évaluer la valeur d'entree"

  def erase_valeur(self):
      """
      Efface la valeur donnée par l'utilisateur dans l'entry
      """
      if hasattr(self,'entry'):
         self.entry.delete(0,END)
      else:
         self.typ_cplx.set('RI')
         self.entry1.delete(0,END)
         self.entry2.delete(0,END)

        
  def display_valeur(self,val=None):
      """
      Affiche la valeur passée en argument dans l'entry de saisie.
      Par défaut affiche la valeur du mot-clé simple
      """
      if not val :
          valeur = self.node.item.object.getval()
      else:
          valeur = val
      if not valeur : return

      if hasattr(self,'entry'):
         # Traitement d'une entree unique
         self.entry.delete(0,END)
         self.entry.insert(0,str(valeur))
      else:
         # Traitement d'une entree de type complexe
         typ_cplx,x1,x2=valeur
         self.entry1.delete(0,END)
         self.entry2.delete(0,END)
         self.typ_cplx.set(typ_cplx)
         self.entry1.setentry(x1)
         self.entry2.setentry(x2)


