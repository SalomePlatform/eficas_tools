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
from Ihm.I_LASSD import LASSD
from Extensions.parametre import PARAMETRE

from utils import substract_list
from plusieurspanel import PLUSIEURS_Panel
from uniqueassdpanel import UNIQUE_ASSD_Panel

import fontes
import math

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
      #print "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
      #print "                                                  "
      #print "A priori on ne doit plus passer dans cette methode "
      #print "                                                  "
      #print "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
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
      #self.frame_boutons.place(relx=0.35,rely=0.,relwidth=0.3,relheight=1.)
      self.frame_boutons.place(relx=0.2,rely=0.,relwidth=1,relheight=1.)
      for fram in (self.frame1,self.frame2,self.frame_right,self.frame_valeurs,
                 self.frame_boutons_fleches,self.frame_choix,self.frame_aide,self.frame_boutons):
          fram.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
          fram.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

      # création des objets dans les frames
      liste_commandes_valeurs = (("<Button-1>",self.selectValeur),
                                 ("<Button-3>",self.deselectValeur),
                                 ("<Double-Button-1>",self.sup_valeur_sans_into))
      self.Liste_valeurs=ListeChoix(self,self.frame_valeurs,l_valeurs,liste_commandes = liste_commandes_valeurs,
                                      titre="Valeur(s) actuelle(s)")

      # Création de l'entry ou de la liste des SD
      # PN : pour ajouter les validators
      self.label = Label(self.frame_choix,text="Valeur :")
      self.make_entry(frame = self.frame_choix,command = self.add_valeur_plusieurs_base)
      self.label.place(relx=0.05,rely=0.2)

      # Création d'un bouton "Importer ..." et d'un bouton "Paramatres" sur le panel.
      bouton_valeurs_fichier = Button(self.frame_choix,
                                      text="Importer",
                                      command=self.select_in_file)
      bouton_valeurs_fichier.place(relx=0.28,rely=0.4,relwidth=0.6)
      bouton_parametres = Button(self.frame_choix, text="Parametres", command=self.affiche_parametre)
      bouton_parametres.place(relx=0.28,rely=0.6,relwidth=0.6)
      self.ajout_valeurs = None

      # boutons Ajouter et Supprimer
      self.bouton_add = Button(self.frame_boutons_fleches,
                          image = images.get_image('arrow_left'),
                          command = self.add_valeur_plusieurs_base)
      self.bouton_sup = Button(self.frame_boutons_fleches,
                          image = images.get_image('arrow_right'),
                          command = self.sup_valeur_sans_into)
      self.bouton_add.place(relx=0.3,rely=0.35)
      self.bouton_sup.place(relx=0.3,rely=0.65)
      # affichage de l'aide
      self.frame_aide.update()
      self.aide = Label(self.frame_aide,
                        text = aide,
                        justify='center',
                        anchor='center',
                              wraplength=int(self.frame_aide.winfo_width()*0.8))
      self.aide.place(relx=0.5,rely=0.5,anchor='center',relwidth=1)
      self.Liste_valeurs.affiche_liste()
      if len(l_valeurs) > 0 :
          liste_marque=l_valeurs[-1]
          self.Liste_valeurs.surligne(liste_marque)
          self.selectValeur(liste_marque)
      # boutons Accepter et Annuler
      self.bouton_accepter = Button(self.frame_boutons,
                               text='Valider',
                               command = lambda s=self,m=min,M=max : s.accepte_modifs_valeur(m,M))
      self.bouton_annuler = Button(self.frame_boutons,
                              text = 'Annuler',
                              command = self.annule_modifs_valeur)
      self.bouton_accepter.place(relx=0.2, rely=0.2,relwidth=0.25)
      self.bouton_annuler.place(relx=0.5, rely=0.2,relwidth=0.25)

  def affiche_parametre(self) :
      if self.node.item.get_liste_param_possible() != [ ]:
         txtparam=""
         for param in self.node.item.get_liste_param_possible():
            txtparam=txtparam+repr(param)+"\n"
         if txtparam=="":
            showerror("Aucun parametre ","Pas de parametre de ce type")
         else :
            try :
                    self.self.fenetreparam.destroy()
            except:
                pass
            self.fenetreparam=FenetreDeParametre( self, self.node.item, self.parent.appli, txtparam)

  def valid_valeur(self):
      self.add_valeur_plusieurs_base()

  def add_valeur_plusieurs_base(self,name=None):
      if name != None :
         valeur = name
      else:
         valeur,validite,commentaire=self.get_valeur()
         if not validite :
            self.parent.appli.affiche_infos(commentaire)
            return

      atraiter=[]
      if type(valeur)  in (types.ListType,types.TupleType) :
         indice = 0
         while (indice < len(valeur)):
            v=valeur[indice]
            if self.node.item.wait_complex :
               if (v== 'RI' or v == 'MP'):
                  try :
                     t=tuple([v,valeur[indice+1],valeur[indice+2]])
                     atraiter.append(t)
                     indice=indice+3
                  except :
                     validite=0
                     commentaire = "Veuillez entrer le complexe sous forme aster ou sous forme python"
                     self.parent.appli.affiche_infos(commentaire)
                     return
               else :     # ce n'est pas un tuple à la mode aster
                  atraiter.append(v)
                  indice = indice + 1
            else:  # on n'attend pas un complexe
              atraiter.append(v)
              indice=indice+1
      else:
         atraiter.append(valeur)
         
      for valeur in atraiter :
         encorevalide=self.node.item.valide_item(valeur)
         # qdsjfkllllllllllllllllll
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

  def make_entry(self,frame,command,x=0.28,y=0.2):
      self.entry = Entry(frame,relief='sunken')
      self.entry.place(relx=0.28,rely=y,relwidth=0.6)
      self.entry.bind("<Return>",lambda e,c=command:c())
      self.entry.bind("<KP_Enter>",lambda e,c=command:c())
      self.entry.focus()

  def get_valeur(self):
      """
      Retourne la valeur saisie par l'utilisateur dans self.entry
      """
      commentaire = ""
      if hasattr(self,'entry'):
         # Traitement d'une entree unique
         valeurentree = self.entry.get()
         if (valeurentree == None or valeurentree ==""):
            return None,0,""

         #On tente une evaluation globale
         valeur,validite=self.node.item.eval_valeur(valeurentree)
         if valeur == valeurentree:
             #L'evaluation n'a rien donné : on a toujours la string
             #on découpe la string sur le séparateur , si c'est possible
             if valeurentree.find(',') != -1:
                 valeur=[]
                 for v in valeurentree.split(','):
                     vsimple,validite=self.node.item.eval_valeur(v)
                     valeur.append(vsimple)

         return valeur,validite,commentaire


        # if (valeurentree[0] != "(") and (valeurentree.find(',') < len(valeurentree)):
        #    valeurs=[]
        #    for v in valeurentree.split(','):
        #      vsimple,validite=self.node.item.eval_valeur(v)
              # Pn If ajoute  pour le panneau "double"
              #if isinstance(vsimple,LASSD) : 
              #         commentaire = "impossible de mélanger reels et liste prédéfinie"
              #  validite = 0
              #         break 
        #      if validite :
        #         valeurs.append(vsimple)
        #      else:
        #         commentaire = "impossible d'évaluer : %s " %`valeurentree`
        #         break
        #    valeur=valeurs
        # else: 
        #    valeur,validite=self.node.item.eval_valeur(valeurentree)
        # if not validite and commentaire == "":
        #    commentaire = "impossible d'évaluer : %s " %`valeurentree`
        # return valeur,validite,commentaire
      #else:
      #   # Traitement d'une entree de type complexe
      #   try:
      #      valeur= (self.typ_cplx.get(),
      #               string.atof(self.entry1.get()),
      #               string.atof(self.entry2.get()))
      #      return valeur,1,""
      #   except:
      #      #traceback.print_exc()
      #      return None,0,"impossible d'évaluer la valeur d'entree"

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

class PLUSIEURS_BASE_OR_UNELISTE_Panel(PLUSIEURS_BASE_Panel,UNIQUE_ASSD_Panel):

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
      aide2 = self.get_aide2()
      aide2 = justify_text(texte=aide2)
      min,max = self.node.item.GetMinMax()
      l_valeurs = self.node.item.GetListeValeurs()
      for i in l_valeurs:
         if isinstance(i,LASSD) :
            affiche_entry=l_valeurs
            l_valeurs=()

      # Il faut traiter ici pour avoir le choix entre une liste
      # deja constituee (listr8aster) ou manuelle

      # création des frames globales
      self.frame1 = Frame(page,relief='groove',bd=2)
      self.frame2 = Frame(page)
      self.frame1.place(relx=0.,rely=0.,relwidth=1.,relheight=0.9)
      self.frame2.place(relx=0.,rely=0.9,relwidth=1,relheight=0.1)

      # création des frames internes dans frame1
      self.frame_valeurs = Frame(self.frame1)
      self.frame_valeurs.place(relx=0.02,rely=0.55,relwidth=0.35,relheight=0.45)
      self.frame_haut = Frame(self.frame1)
      self.frame_haut.place(relx=0.02,rely=0.02,relwidth=0.98,relheight=0.45)
      self.frame_bas = Frame(self.frame1)
      self.frame_bas.place(relx=0.37,rely=0.55,relwidth=0.63,relheight=0.45)

      # création des frames internes dans frame_right
      self.frame_fleches = Frame(self.frame_bas)
      self.frame_fleches.place(relx=0.,rely=0.4,relwidth=0.2,relheight=0.5)
      self.frame_choix = Frame(self.frame_bas)
      self.frame_choix.place(relx=0.2,rely=0.1,relwidth=0.75,relheight=1)

      # affichage de l'aide
      self.aide = Label(self.frame_haut, text = aide, justify='center', anchor='center',)
      self.aide.place(relx=0.72,rely=0.25,anchor='center',relwidth=1)
      self.aide2 = Label(self.frame2, text = aide2,)
      self.aide2.place(relx=0.4,rely=0.01,relwidth=0.6)

      # Création d'un bouton "Importer ..." et d'un bouton "Parametres" sur le panel.
      bouton_valeurs_fichier = Button(self.frame_choix,
                                      text="Importer",
                                      command=self.select_in_file)
      bouton_valeurs_fichier.place(relx=0.28,rely=0.0,relwidth=0.6)
      bouton_parametres = Button(self.frame_choix, text="Parametres", command=self.affiche_parametre)
      bouton_parametres.place(relx=0.28,rely=0.25,relwidth=0.6)
      self.ajout_valeurs = None


      # Création de la liste des SD
      liste_noms_sd = self.node.item.get_sd_avant_du_bon_type_pour_type_de_base()
      liste_noms_sd = self.tri(liste_noms_sd)
      self.listbox = Pmw.ScrolledListBox(self.frame_haut,
                        items=liste_noms_sd,
                labelpos='n',
                #label_text="Structures de données du type\n requis parl'objet courant :",
                label_text="Listes du type\n requis parl'objet courant :",
                listbox_height = 6,
                dblclickcommand=lambda s=self,c=UNIQUE_ASSD_Panel.valid_valeur : s.choose_valeur_from_list(c))
      self.listbox.place(relx=0.00,rely=0.00,relwidth=0.4)

      # On eneleve le label pour gagner de la place 
      #self.label = Label(self.frame_choix,text="Valeur :")
      #self.label.place(relx=0.05,rely=0.85)
      self.make_entry(frame = self.frame_choix,command = self.add_valeur_plusieurs_base,x=0.28,y=0.55)
      
      # boutons Ajouter et Supprimer
      bouton_add = Button(self.frame_fleches, image = images.get_image('arrow_left'),
                          command = self.add_valeur_plusieurs_base)
      bouton_sup = Button(self.frame_fleches, image = images.get_image('arrow_right'),
                          command = self.sup_valeur_sans_into)
      bouton_add.place(relx=0.2,rely=0.25)
      bouton_sup.place(relx=0.2,rely=0.70)


      # boutons Accepter et Annuler dans frame2
      bouton_accepter = Button(self.frame2, text='Valider',
                               command = lambda s=self,m=min,M=max : s.accepte_modifs_valeur(m,M))
      bouton_annuler = Button(self.frame2, text = 'Annuler',
                              command = self.annule_modifs_valeur)
      for but in (bouton_accepter,bouton_annuler):
          but.pack(side='left',padx=5)

      # création des objets dans les frames
      liste_commandes_valeurs = (("<Button-1>",self.selectValeur),
                                 ("<Button-3>",self.deselectValeur),
                                 ("<Double-Button-1>",self.sup_valeur_sans_into))
      self.Liste_valeurs = ListeChoix(self,self.frame_valeurs,l_valeurs,
                                      liste_commandes = liste_commandes_valeurs,
                                      titre="Valeur(s) non-prédéfinies(s)",
                                      fonte_titre=None
                                      )

      for fram in (self.frame1,self.frame2,self.frame_bas,self.frame_haut,self.frame_valeurs,
                 self.frame_fleches,self.frame_choix):
          fram.bind("<Button-3>",lambda e,s=self,a=bulle_aide: s.parent.appli.affiche_aide(e,a))
          fram.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

      self.Liste_valeurs.affiche_liste()
      if len(l_valeurs) > 0 :
          liste_marque=l_valeurs[-1]
          self.Liste_valeurs.surligne(liste_marque)
      
  def get_aide(self):
      """
      Retourne la phrase d'aide indiquant de quel type de base doivent être les valeurs
      saisies par l'utilisateur
      """
      commentaire="Ce motclef accepte soit un nom de liste déja définie soit une liste manuelle de valeurs"
      return commentaire

  def get_aide2(self):
      min,max = self.node.item.GetMinMax()
      aideval=self.node.item.aide()
      commentaire="min : " + str(min) + ", max : " + str(max)
      aideval=commentaire + aideval
      return aideval

  def choose_valeur_from_list(self,command):
      """
      Affecte à valeur choisie la sélection courante dans la liste des choix proposés
      Exécute command
      """
      self.Liste_valeurs.liste=[]
      self.Liste_valeurs.affiche_liste()
      if len(self.listbox.get()) == 0 : return
      choix = self.listbox.getcurselection()[0]
      d={}
      d["valeurentree"]=choix
      apply(command,(self,),d)
     


  def tri(self,liste_noms_sd):
      a=(3+8j)
      d_types = { 'TXM' : type('A'),
                  'R'   : type(3.),
                  'I'   : type(0),
                  'C'   : type(a)}

      # On enleve seulement ceux qu'on peut
      # Sur certaines listes, il est possible qu'on ne 
      # sache pas déterminer le type
      listefinale=[]
      typespossibles=self.node.item.object.definition.type
      typecherche = None
      for t in typespossibles:
          if t in d_types.keys() :
             typecherche = d_types[t]
             break
      for liste in liste_noms_sd:
          valeur,validite=self.node.item.eval_valeur(liste)
          for mc in valeur.etape.mc_liste :
              try :
                 if type(mc.valeur)  in (types.ListType,types.TupleType) :
                    typeliste=type(mc.valeur[0])
                 else :
                    typeliste=type(mc.valeur)
                 if type(mc.valeur[0]) == typecherche:
                    listefinale.append(liste)
              except:
                 listefinale.append(liste)
      return listefinale

