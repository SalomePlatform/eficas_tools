#@ MODIF composimp Editeur  DATE 05/09/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# Modules Python
import string,types,os
from Tkinter import *
import Pmw
from tkFileDialog import *
from tkMessageBox import showinfo
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
      #nb.add('Commentaire',tab_text='Insérer commentaire')
      self.makeValeurPage(nb.page('Valeur'))
      #self.makeCommentairePage(nb.page("Commentaire"))
      nb.setnaturalsize()
      
# ----------------------------------------------------------------------------------------
#   Méthodes utlisées pour l'affectation de la valeur donnée par l'utilisateur
#    au mot-clé courant
# ----------------------------------------------------------------------------------------

  def record_valeur(self,name=None,mess='Valeur du mot-clé enregistrée'):
      """
          Enregistre  val comme valeur de self.node.item.object SANS 
          faire de test de validité
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      if name != None:
          valeur =name
      else :
          valeur= self.entry.get()
          self.entry.delete(0,END)
      self.node.item.set_valeur(valeur,evaluation='non')
      self.parent.appli.affiche_infos(mess)
      if self.node.item.get_position()=='global':
          self.node.etape.verif_all()
      elif self.node.item.get_position()=='global_jdc':
          self.node.racine.verif_all()
      else :
          self.node.parent.verif()
      if self.node.item.isvalid():
          self.node.parent.select()
      self.node.update()
# ----------------------------------------------------------------------------------------
#   Méthodes utlisées pour la manipulation des items dans les listes de choix
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
      liste_valeurs = self.Liste_valeurs.get_liste()
      liste_valeurs.remove(self.selected_valeur)
      liste_choix = self.node.item.get_definition().into
      liste_choix = substract_list(liste_choix,liste_valeurs)
      self.Liste_valeurs.put_liste(liste_valeurs)
      self.Liste_choix.put_liste(liste_choix)
      self.selected_valeur = None

  def add_choix(self,name=None):
      """
      Ajoute le choix selectionné à la liste des valeurs et le retire
      de la liste des choix possibles
      """
      min,max = self.node.item.GetMinMax()
      liste_valeurs = self.Liste_valeurs.get_liste()
      if len(liste_valeurs) >= max :
          self.parent.appli.affiche_infos("La liste ne peut pas avoir plus de %d éléments" %max)
          return
      liste_valeurs.append(self.selected_choix)
      liste_choix = self.Liste_choix.get_liste()
      liste_choix.remove(self.selected_choix)
      self.Liste_valeurs.put_liste(liste_valeurs)
      self.Liste_choix.put_liste(liste_choix)
      self.selected_choix = None

  def selectChoix(self,name):
      self.selected_choix = name

  def deselectChoix(self,name):
      self.selectChoix = None
      
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
      if valeur == None : return
      self.text.insert(END,valeur)

class PLUSIEURS_Panel(newSIMPPanel):
  """
  Classe virtuelle servant de classe mère à toutes celles définissant
  un panneau pour un mot-clé simple qui attend une liste de valeurs
  """
  def accepte_modifs_valeur(self,min,max):
      """
      Méthode qui récupère la liste des valeurs donnée par l'utilisateur
      et l'affecte au mot-clé courant.
      """
      l_valeurs = self.Liste_valeurs.get_liste()
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
      if self.node.item.isvalid():
          self.node.parent.select()
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
          
  def traite_reel(self,valeur):
      """
      Cette fonction a pour but de rajouter le '.' en fin de chaîne pour un réel
      ou de détecter si on fait référence à un concept produit par DEFI_VALEUR
      ou un EVAL ...
      """
      valeur = string.strip(valeur)
      liste_reels = self.node.item.get_sd_avant_du_bon_type()
      if valeur in liste_reels:
          return valeur
      if len(valeur) >= 3 :
          if valeur[0:4] == 'EVAL' :
              # on a trouvé un EVAL --> on retourne directement la valeur
              return valeur
      if string.find(valeur,'.') == -1 :
          # aucun '.' n'a été trouvé dans valeur --> on en rajoute un à la fin
          return valeur+'.'
      else:
          return valeur
        
  def add_valeur_sans_into(self,name=None):
      """
      Lit ce que l'utilisateur a saisi dans self.entry et cherche à
      l'évaluer :
      - si la valeur est acceptable, elle est ajoutée dans la liste des valeurs
      - sinon elle est refusée
      """
      min,max = self.node.item.GetMinMax()
      if name != None :
          valeur = name
      else:
          valeur = self.get_valeur()
      if self.node.item.wait_reel():
          valeur = self.traite_reel(valeur)
      if self.node.item.wait_geom():
          val,test1 = valeur,1
      else:
          val,test1 = self.node.item.object.eval_valeur(valeur)
      if test1 :
          test2 = self.node.item.object.verif_type(val)
          if test2 :
              liste_valeurs = self.Liste_valeurs.get_liste()
              if len(liste_valeurs) >= max :
                  self.parent.appli.affiche_infos("La liste a déjà atteint le nombre maximum d'éléments, ajout refusé")
                  self.erase_valeur()
                  return
              liste_valeurs.append(val)
              self.Liste_valeurs.put_liste(liste_valeurs)
              self.erase_valeur()
              self.parent.appli.affiche_infos("Nouvelle valeur acceptée")
          else:
              self.parent.appli.affiche_infos("Valeur incorrecte : ajout à la liste refusé")
      else:
          print "impossible d'évaluer %s" %val
          self.parent.appli.affiche_infos("Valeur incorrecte : ajout à la liste refusé")
      #if self.node.item.isvalid():
      #    self.node.parent.select()

  def sup_valeur_sans_into(self,name=None):
      """
      Méthode qui sert à retirer de la liste des valeurs la valeur sélectionnée
      """
      liste_valeurs = self.Liste_valeurs.get_liste()
      try:
          liste_valeurs.remove(self.selected_valeur)
      except:
          # la valeur sélectionnée n'est pas dans la liste
          return
      self.Liste_valeurs.put_liste(liste_valeurs)
      #self.display_valeur('')
      self.display_valeur(self.selected_valeur)
      self.selected_valeur = None      

  def display_valeur(self,val=None):
      """
      Affiche la valeur passée en argument dans l'entry de saisie.
      Par défaut affiche la valeur du mot-clé simple
      """
      if not val :
          valeur = self.node.item.getval()
      else:
          valeur = val
      self.entry.delete(0,END)
      if not valeur : return
      self.entry.insert(0,str(valeur))
      
            
class PLUSIEURS_INTO_Panel(PLUSIEURS_Panel):
  """
  Classe servant à définir le panneau permettant d'afficher et de saisir une
  liste de valeurs à choisir parmi une liste discrètes de valeurs possibles
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie de plusieurs valeurs parmi un ensemble discret
      de possibles
      """
      self.ajout_valeurs = None
      # On récupère la bulle d'aide du panneau, l'objet, min et max (cardinalité de la liste),
      # la liste des choix et la liste des valeurs
      bulle_aide=self.get_bulle_aide()
      objet_mc = self.node.item.get_definition()
      min,max = self.node.item.GetMinMax()
      l_choix=list(objet_mc.into)
      l_choix.sort()
      l_valeurs = self.node.item.GetListeValeurs()
      # remplissage du panneau
      self.frame_valeurs = Frame(page)
      self.frame_valeurs.place(relx=0.05,rely=0.05,relwidth=0.35,relheight=0.7)
      self.frame_boutons_fleches = Frame(page)
      self.frame_boutons_fleches.place(relx=0.4,rely=0.,relwidth=0.2,relheight=0.7)
      self.frame_choix = Frame(page)
      self.frame_choix.place(relx=0.6,rely=0.05,relwidth=0.35,relheight=0.7)
      self.frame_boutons = Frame(page)
      self.frame_boutons.place(relx=0.35,rely=0.87,relwidth=0.3,relheight=0.1)
      liste_commandes_valeurs = (("<Button-1>",self.selectValeur),
                                 ("<Button-3>",self.deselectValeur),
                                 ("<Double-Button-1>",self.sup_valeur))
      liste_commandes_choix = (("<Button-1>",self.selectChoix),
                               ("<Button-3>",self.deselectChoix),
                               ("<Double-Button-1>",self.add_choix))
      self.Liste_valeurs = ListeChoix(self,self.frame_valeurs,l_valeurs,liste_commandes = liste_commandes_valeurs,
                                      titre="Valeur(s) actuelle(s)")
      self.Liste_choix = ListeChoix(self,self.frame_choix,l_choix,liste_commandes = liste_commandes_choix,
                                    titre= "Valeurs possibles")
      bouton_add = Button(self.frame_boutons_fleches,
                          #text="<--",
                          image = images.get_image('arrow_left'),
                          command = self.add_choix)
      bouton_sup = Button(self.frame_boutons_fleches,
                          #text="-->",
                          image = images.get_image('arrow_right'),
                          command = self.sup_valeur)
      bouton_accepter = Button(self.frame_boutons,
                               text='Valider',
                               command = lambda s=self,m=min,M=max : s.accepte_modifs_valeur(m,M))
      bouton_annuler = Button(self.frame_boutons,
                              text = 'Annuler',
                              command = self.annule_modifs_valeur)
      bouton_add.place(relx=0.3,rely=0.35)
      bouton_sup.place(relx=0.3,rely=0.65)
      for but in (bouton_accepter,bouton_annuler):
          but.pack(side='left',padx=5)
      self.Liste_valeurs.affiche_liste()
      self.Liste_choix.affiche_liste()
      for fram in (self.frame_valeurs,self.frame_boutons_fleches,self.frame_choix,self.frame_boutons):
          fram.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
          fram.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide du panneau (affichée par clic droit)
      """
      return """Un clic sur une valeur des deux listes la sélectionne.
      - Un clic sur la flèche gauche stocke la valeur possible sélectionnée
      dans la liste des valeurs que vous voulez affecter au mot-clé simple
      - Un clic sur la flèche droite déstocke la valeur du mot-clé simple
      sélectionnée (elle apparaît alors à nouveau comme choix possible
      dans la liste des choix à droite)
      - Cliquez sur 'Valider' pour affecter la liste des valeurs sélectionnées
      au mot-clé simple courant
      - Cliquez sur 'Annuler' pour restaurer la valeur du mot-clé simple
      avant toute modification depuis le dernier 'Valider'"""

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
      self.frame_choix.place(relx=0.2,rely=0.2,relwidth=0.7,relheight=0.5)
      self.frame_aide = Frame(self.frame_right)
      self.frame_aide.place(relx=0.1,rely=0.7,relwidth=0.8,relheight=0.3)
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
      self.label = Label(self.frame_choix,text="Valeur :")
      self.make_entry(frame = self.frame_choix,command = self.add_valeur_sans_into)
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
                          command = self.add_valeur_sans_into)
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

  def select_in_file(self):
      """ Permet d'ouvrir un fichier choisi par l'utilisateur. """
      nom_fichier = askopenfilename(title="Choix fichier :")
      if nom_fichier == "":
          return
      try:
          f = open(nom_fichier, "rb")
          selection_texte = f.read()
          f.close()
          self.ajout_valeurs = FenetreDeSelection(self, self.node.item,
                                         titre="Sélection de valeurs",
                                         texte=selection_texte)
      except:
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
      mc = self.node.item.get_definition()
      d_aides = { 'TXM' : 'chaînes de caractères',
                  'R'   : 'réels',
                  'I'   : 'entiers',
                  'C'   : 'complexes'}
      type = mc.type[0]
      if not d_aides.has_key(type) : return 'Type de base inconnu'
      if mc.min == mc.max:
          return "Une liste de "+d_aides[type]+" chaînes de caractères est attendue"
      else :
          return "Une liste de "+d_aides[type]+" est attendue (min="+`mc.min`+",max="+`mc.max`+')'

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
          self.entry.place(relx=0.28,rely=0.5,relwidth=0.6)
          self.entry.bind("<Return>",lambda e,c=command:c())
          self.entry.focus()

  def get_valeur(self):
      """
      Retourne la valeur saisie par l'utilisateur dans self.entry
      """
      return self.entry.get()

  def erase_valeur(self):
      """
      Efface la valeur donnée par l'utilisateur dans l'entry
      """
      self.entry.delete(0,END)
        
class PLUSIEURS_ASSD_Panel(PLUSIEURS_Panel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de donner une liste de valeurs qui ne sont pas
  à choisir dans une liste discrètes et qui sont de type dérivé d'ASSD
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie de plusieurs noms de SD parmi un ensemble discret
      de SD possibles, cad d'un type cohérent avec les types attendus par le mot-clé simple
      """
      # On récupère la bulle d'aide du panneau, l'objet, l'aide, min et max (cardinalité de la liste),
      # la liste des valeurs déjà affectées à l'objet courant et la liste des SD du bon type
      bulle_aide=self.get_bulle_aide()
      self.ajout_valeurs=None
      objet_mc = self.node.item.get_definition()
      aide = self.get_aide()
      aide = justify_text(texte=aide)
      min,max = self.node.item.GetMinMax()
      l_valeurs = self.node.item.GetListeValeurs()
      l_choix=self.node.item.get_sd_avant_du_bon_type()
      l_choix.sort()
      # remplissage du panneau
      self.frame_valeurs = Frame(page)
      self.frame_valeurs.place(relx=0.05,rely=0.05,relwidth=0.35,relheight=0.7)
      self.frame_boutons_fleches = Frame(page)
      self.frame_boutons_fleches.place(relx=0.4,rely=0.,relwidth=0.2,relheight=0.7)
      self.frame_choix = Frame(page)
      self.frame_choix.place(relx=0.6,rely=0.05,relwidth=0.35,relheight=0.7)
      self.frame_boutons = Frame(page)
      self.frame_boutons.place(relx=0.35,rely=0.87,relwidth=0.3,relheight=0.1)
      liste_commandes_valeurs = (("<Button-1>",self.selectValeur),
                                 ("<Button-3>",self.deselectValeur),
                                 ("<Double-Button-1>",self.sup_valeur_sans_into))
      liste_commandes_choix = (("<Button-1>",self.selectChoix),
                               ("<Button-3>",self.deselectChoix),
                               ("<Double-Button-1>",self.add_valeur_sans_into))
      self.Liste_valeurs = ListeChoix(self,self.frame_valeurs,l_valeurs,liste_commandes = liste_commandes_valeurs,
                                      titre="Valeur(s) actuelle(s)")
      self.Liste_choix = ListeChoix(self,self.frame_choix,l_choix,liste_commandes = liste_commandes_choix,
                                    titre= "Valeurs possibles")
      bouton_add = Button(self.frame_boutons_fleches,
                          #text="<--",
                          image = images.get_image('arrow_left'),
                          command = self.add_valeur_sans_into)
      bouton_sup = Button(self.frame_boutons_fleches,
                          #text="-->",
                          image = images.get_image('arrow_right'),
                          command = self.sup_valeur_sans_into)
      bouton_accepter = Button(self.frame_boutons,
                               text='Valider',
                               command = lambda s=self,m=min,M=max : s.accepte_modifs_valeur(m,M))
      bouton_annuler = Button(self.frame_boutons,
                              text = 'Annuler',
                              command = self.annule_modifs_valeur)
      bouton_add.place(relx=0.3,rely=0.35)
      bouton_sup.place(relx=0.3,rely=0.65)
      for but in (bouton_accepter,bouton_annuler):
          but.pack(side='left',padx=5)
      self.Liste_valeurs.affiche_liste()
      self.Liste_choix.affiche_liste()
      for fram in (self.frame_valeurs,self.frame_boutons_fleches,self.frame_choix,self.frame_boutons):
          fram.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
          fram.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide associée au panneau
      """
      return """Un clic sur une valeur des deux listes la sélectionne.
      - Un clic sur la flèche gauche stocke la valeur possible sélectionnée
      dans la liste des valeurs que vous voulez affecter au mot-clé simple
      - Un clic sur la flèche droite déstocke la valeur du mot-clé simple
      sélectionnée (elle apparaît alors à nouveau comme choix possible
      dans la liste des choix à droite)
      - Cliquez sur 'Valider' pour affecter la liste des valeurs sélectionnées
      au mot-clé simple courant
      - Cliquez sur 'Annuler' pour restaurer la valeur du mot-clé simple
      avant toute modification depuis le dernier 'Valider'"""

  def get_aide(self):
      """
      Retourne la phrase d'aide indiquant de quel type doivent être les
      valeurs que doit entrer l'utilisateur
      """
      mc = self.node.item.get_definition()
      type = mc.type[0].__name__  
      if len(mc.type)>1 :
          for typ in mc.type[1:] :
              type = type + ' ou '+typ.__name__
      if mc.min == mc.max:
        return "Une liste de "+`mc.min`+" objets de type "+type+" est attendue"
      else :
        return "Une liste d'objets de type "+type+" est attendue (min="+`mc.min`+",max="+`mc.max`+')'
    
  def sup_valeur(self,name=None):
      """
      Supprime la valeur selectionnée de la liste des valeurs et la rajoute
      à la liste des choix possibles
      """
      liste_valeurs = self.Liste_valeurs.get_liste()
      liste_valeurs.remove(self.selected_valeur)
      liste_choix = self.node.item.get_definition().into
      liste_choix = substract_list(liste_choix,liste_valeurs)
      self.Liste_valeurs.put_liste(liste_valeurs)
      self.Liste_choix.put_liste(liste_choix)
      self.selected_valeur = None      
    
  def erase_valeur(self):
      pass

  def get_valeur(self):
      """
      Retourne la valeur sélectionnée dans la liste des choix
      """
      return self.selected_choix

  def display_valeur(self,val=None):
      """
         Affiche la valeur passée en argument dans l'entry de saisie.
         Par défaut affiche la valeur du mot-clé simple
      """
      # Il n'y a pas d'entry pour ce type de panneau
      return

    
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
    
  def valid_valeur(self):
      """
      Teste si la valeur fournie par l'utilisateur est une valeur permise :
      - si oui, l'enregistre
      - si non, restaure l'ancienne valeur
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      valeur = self.get_valeur()
      self.erase_valeur()
      anc_val = self.node.item.get_valeur()
      test = self.node.item.set_valeur(valeur)
      if not test :
          mess = "impossible d'évaluer : %s " %`valeur`
          self.parent.appli.affiche_infos("Valeur du mot-clé non autorisée :"+mess)
          return
      elif self.node.item.isvalid() :
          self.parent.appli.affiche_infos('Valeur du mot-clé enregistrée')
          self.node.parent.select()
      else :
          cr = self.node.item.get_cr()
          mess = "Valeur du mot-clé non autorisée :"+cr.get_mess_fatal()
          self.record_valeur(anc_val,mess=mess)
          return
      if self.node.item.get_position()=='global':
          self.node.etape.verif_all()
      elif self.node.item.get_position()=='global_jdc':
          self.node.racine.verif_all()
      else :
          self.node.parent.verif()
      self.node.update()

class UNIQUE_INTO_Panel(UNIQUE_Panel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie d'une seule valeur parmi un ensemble
      discret de possibles
      """
      # récupération de la bulle d'aide et de l'objet mc
      bulle_aide=self.get_bulle_aide()
      objet_mc = self.node.item.get_definition()
      # remplissage du panel
      self.frame_valeur = Frame(page)
      self.frame_valeur.pack(fill='both',expand=1)
      self.frame_valeur.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      self.frame_valeur.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      l_choix=list(objet_mc.into)
      l_choix.sort()
      self.label = Label(self.frame_valeur,text='Choisir une valeur :')
      self.label.pack(side='top')
      self.frame = Frame(page)
      self.frame.place(relx=0.33,rely=0.2,relwidth=0.33,relheight=0.6)
      liste_commandes = (("<Button-1>",self.selectChoix),
                         ("<Button-3>",self.deselectChoix),
                         ("<Double-Button-1>",self.record_valeur))
      self.Liste_choix = ListeChoix(self,self.frame,l_choix,liste_commandes = liste_commandes,
                                    titre="Valeurs possibles")
      self.Liste_choix.affiche_liste()

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide affectée au panneau courant (affichée par clic droit)
      """
      return """Double-cliquez sur la valeur désirée
      pour valoriser le mot-clé simple courant"""

class UNIQUE_ASSD_Panel(UNIQUE_Panel):
  """
  Classe servant à définir le panneau associé aux objets qui attendent une valeur unique
  d'un type dérivé d'ASSD
  """
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
      return  "Un objet de type "+type+" est attendu"
    
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
      if valeur == None : return # pas de valeur à afficher ...
      self.valeur_choisie.set(valeur.nom)

  def erase_valeur(self):
      pass

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
      self.listbox.place(relx=0.5,rely=0.3,relheight=0.4,anchor='center')
      # affichage du bouton 'Nouveau concept'
      self.b_co = Pmw.OptionMenu(self.frame_valeur,labelpos='w',label_text = "Nouveau concept : ",
                                 items = ('NON','OUI'),menubutton_width=10)
      self.b_co.configure(command = lambda e,s=self : s.ask_new_concept())
      self.b_co.place(relx=0.05,rely=0.6,anchor='w')
      self.label_co = Label(self.frame_valeur,text='Nom du nouveau concept :')
      self.entry_co = Entry(self.frame_valeur)
      self.entry_co.bind('<Return>',self.valid_nom_concept_co)
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
      self.erase_valeur()
      anc_val = self.node.item.get_valeur()
      test_CO=self.node.item.is_CO(anc_val)
      test = self.node.item.set_valeur(valeur)
      if not test :
          mess = "impossible d'évaluer : %s " %`valeur`
          self.parent.appli.affiche_infos("Valeur du mot-clé non autorisée :"+mess)
          return
      elif self.node.item.isvalid() :
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
          self.record_valeur(anc_val,mess=mess)
          return
      if self.node.item.get_position()=='global':
          self.node.etape.verif_all()
      elif self.node.item.get_position()=='global_jdc':
          self.node.racine.verif_all()
      else :
          self.node.parent.verif()
      self.node.update()

  def valid_nom_concept_co(self,event=None):
      """
      Lit le nom donné par l'utilisateur au concept de type CO qui doit être
      la valeur du MCS courant et stocke cette valeur
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      anc_val = self.node.item.get_valeur()
      nom_concept = self.entry_co.get()
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
          self.record_valeur(anc_val,mess=mess)
          return
      if self.node.item.get_position()=='global':
          self.node.etape.verif_all()
      elif self.node.item.get_position()=='global_jdc':
          self.node.racine.verif_all()
      else :
          self.node.parent.verif()
      if self.node.item.isvalid():
          self.node.parent.select()
      self.node.update()

  def ask_new_concept(self):
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
      if valeur == None or valeur == '': 
         self.valeur_choisie.set('')
         return # pas de valeur à afficher ...
      # il faut configurer le bouton si la valeur est un objet CO
      # sinon afficher le nom du concept dans self.valeur_choisie
      if self.node.item.is_CO():
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
      if self.node.item.get_position()=='global':
          self.node.etape.verif_all()
      elif self.node.item.get_position()=='global_jdc':
          self.node.racine.verif_all()
      else :
          self.node.parent.verif()
      if self.node.item.isvalid():
          self.node.parent.select()
      self.node.update()


class UNIQUE_BASE_Panel(UNIQUE_Panel):
  """
  Classe servant à définir le panneau associé aux mots-clés simples qui attendent
  une valeur d'un type de base (entier, réel ou string).
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie de la valeur du mot-clé simple courant qui doit être de type
      de base cad entier, réel, string ou complexe
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
      self.label = Label(self.frame_valeur,text='Valeur :')
      self.label.place(relx=0.1,rely=0.5)
      self.entry = Entry(self.frame_valeur,relief='sunken')
      self.entry.place(relx=0.28,rely=0.5,relwidth=0.6)
      self.entry.bind("<Return>",lambda e,c=self.valid_valeur:c())
      self.entry.focus()
      # aide associée au panneau
      self.frame_valeur.update()
      self.aide = Label(self.frame_valeur, 
                        text = aide,
			wraplength=int(self.frame_valeur.winfo_width()*0.8),
			justify='center')
      self.aide.place(relx=0.5,rely=0.7,anchor='n')
      # affichage de la valeur du MCS
      self.display_valeur()

  def get_aide(self):
      """
      Retourne la phrase d'aide indiquant de quel type doit être la valeur
      du mot-clé simple fournie par l'utilisateur
      """
      mc = self.node.item.get_definition()
      d_aides = { 'TXM' : "Une chaîne de caractères est attendue",
                  'R'   : "Un réel est attendu",
                  'I'   : "Un entier est attendu"}
      type = mc.type[0]
      return d_aides.get(type,"Type de base inconnu")

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide associée au panneau et affichée par clic droit
      """
      return """Saisissez la valeur que vous voulez affecter au mot-clé simple
      dans la zone de saisie et pressez <Return>"""
      
  def display_valeur(self):
      """
      Affiche la valeur de l'objet pointé par self
      """
      valeur = self.node.item.get_valeur()
      if valeur == None : return # pas de valeur à afficher ...
      self.entry.delete(0,END)
      self.entry.insert(0,valeur)
      
class UNIQUE_COMP_Panel(UNIQUE_Panel):
  """
  Classe servant à définir le panneau associé aux mots-clés simples
  qui attendent une valeur de type complexe
  """
  def makeValeurPage(self,page):
      """
      Génère la page de saisie de la valeur du mot-clé simple courant qui doit être de type
      de base cad entier, réel, string ou complexe
      """
      # Récupération de l'aide associée au panneau et de l'aide destinée à l'utilisateur
      bulle_aide=self.get_bulle_aide()
      aide=self.get_aide()
      aide= justify_text(texte=aide)
      # Remplissage du panneau
      self.frame_valeur = Frame(page)
      self.frame_valeur.pack(fill='both',expand=1)
      self.frame_valeur.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      self.frame_valeur.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      self.label = Label(self.frame_valeur,text='Valeur :')
      self.label.place(relx=0.1,rely=0.5)
      self.typ_cplx=StringVar()
      self.typ_cplx.set('RI')
      rb1 = Radiobutton(self.frame_valeur, text='RI',variable=self.typ_cplx,value='RI')
      rb2 = Radiobutton(self.frame_valeur, text='MP',variable=self.typ_cplx,value='MP')
      self.entry1 = Pmw.EntryField(self.frame_valeur,validate='real')
      self.entry2 = Pmw.EntryField(self.frame_valeur,validate='real')
      rb1.place(relx=0.05,rely = 0.4)
      rb2.place(relx=0.05,rely = 0.6)
      self.entry1.component('entry').bind("<Return>",lambda e,s=self:s.entry2.component('entry').focus())
      self.entry2.component('entry').bind("<Return>",lambda e,c=self.valid_valeur:c())
      self.entry1.place(relx=0.27,rely = 0.5,relwidth=0.35)
      self.entry2.place(relx=0.65,rely = 0.5,relwidth=0.35)
      self.entry1.focus()
      self.frame_valeur.update()
      self.aide = Label(self.frame_valeur,
                        text = aide,
                        wraplength=int(self.frame_valeur.winfo_width()*0.8),
			justify='center')
      self.aide.place(relx=0.5,rely=0.7,anchor='n')

  def get_bulle_aide(self):
      """
      Retourne la bulle d'aide du panneau
      """
      return """-Choisissez votre format de saisie du complexe :
      \t 'RI' = parties réelle et imaginaire
      \t 'MP' = module/phase (en degrés)
      - Saisissez ensuite dans les deux zones de saisie les deux nombres attendus"""

  def get_aide(self):
      """
      Retourne la phrase d'aide décrivant le type de la valeur que peut prendre
      le mot-clé simple courant
      """
      return 'Un complexe est attendu'

  def get_valeur(self):
      """
      Retourne le complexe saisi par l'utilisateur
      """
      l=[]
      l.append(self.typ_cplx.get())
      l.append(string.atof(self.entry1.get()))
      l.append(string.atof(self.entry2.get()))
      return `tuple(l)`

  def erase_valeur(self):
      """
      Efface les entries de saisie
      """
      self.typ_cplx = 'RI'
      self.entry1.delete(0,END)
      self.entry2.delete(0,END)
      
class SIMPTreeItem(Objecttreeitem.AtomicObjectTreeItem):
  panel = newSIMPPanel

  def init(self) :
      self.expandable = 0
      self.affect_panel()

  def affect_panel(self):
      """
      Cette méthode attribue le panel à l'objet pointé par self en fonction de la
      nature de la valeur demandée pour cet objet
      """
      if self.wait_shell():
          # l'objet attend un shell
          self.panel = SHELLPanel
      elif self.wait_into():
          # l'objet prend sa (ses) valeur(s) dans un ensemble discret de valeurs
          min,max = self.GetMinMax()
          if max != 1 and ((min != 0 and min != max) or (min == 0)):
             # l'objet attend une liste de valeurs
             self.panel = PLUSIEURS_INTO_Panel
          else:
             # l'objet n'attend qu'une seule valeur
             self.panel = UNIQUE_INTO_Panel
      else:
          # l'objet prend une ou des valeurs à priori quelconques
          min,max = self.GetMinMax()
          if max != 1 :
              # on attend une liste de valeurs mais de quel type ?
              if self.wait_assd():
                  # on attend une liste de SD
                  self.panel = PLUSIEURS_ASSD_Panel
              else:
                  # on attend une liste de valeurs de types debase (entiers, réels,...)
                  self.panel = PLUSIEURS_BASE_Panel
          else:
              # on n'attend qu'une seule valeur mais de quel type ?
              if self.wait_co():
                  # on attend une SD ou un objet de la classe CO (qui n'existe pas encore)
                  self.panel = UNIQUE_SDCO_Panel
              elif self.wait_assd():
                  # on attend une SD
                  self.panel = UNIQUE_ASSD_Panel
              else:
                  # on attend une valeur d'un type de base (entier,réel,...)
                  if self.wait_complex():
                      # on attend un complexe
                      self.panel = UNIQUE_COMP_Panel
                  else:
                      # on attend un entier, un réel ou une string
                      self.panel = UNIQUE_BASE_Panel
      
  def SetText(self, text):
    try:
      value = eval(text)
      self.object.setval(value)
    except:
      pass

  def GetIconName(self):
    if self.isvalid():
      return "ast-green-ball"
    elif self.object.isoblig():
      return "ast-red-ball"
    else:
      return "ast-yel-ball"

  def GetText(self):
    """
    Classe SIMPTreeItem
    Retourne le texte à afficher dans l'arbre représentant la valeur de l'objet
    pointé par self 
    """
    return self.object.GetText()

  def wait_co(self):
      """
      Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un objet de type ASSD qui n'existe pas encore (type CO()),
      0 sinon
      """
      return self.object.wait_co()

  def wait_geom(self):
      """
      Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un objet GEOM, 0 sinon
      """
      return self.object.wait_geom()
    
  def wait_complex(self):
      """ Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un complexe, 0 sinon """
      if 'C' in self.object.definition.type:
          return 1
      else:
          return 0

  def wait_reel(self):
      """ Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un réel, 0 sinon """
      if 'R' in self.object.definition.type:
          return 1
      else:
          return 0
        
  def wait_shell(self):
      """ Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un shell, 0 sinon """
      if 'shell' in self.object.definition.type:
          return 1
      else:
          return 0

  def wait_into(self):
      """ Méthode booléenne qui retourne 1 si l'objet pointé par self
      prend ses valeurs dans un ensemble discret (into), 0 sinon """
      if self.object.definition.into != None :
          return 1
      else:
          return 0

  def wait_assd(self):
      """Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un objet de type ASSD ou dérivé, 0 sinon """
      return self.object.wait_assd()
    
  def getval(self):
      return self.object.getval()
    
  def GetMinMax(self):
      """ Retourne les valeurs min et max de la définition de object """
      return self.object.get_min_max()

  def GetMultiplicite(self):
      """ A préciser.
          Retourne la multiplicité des valeurs affectées à l'objet
          représenté par l'item. Pour le moment retourne invariablement 1.
      """
      return 1

  def GetType(self):
      """ 
          Retourne le type de valeur attendu par l'objet représenté par l'item.
      """
      return self.object.get_type()

  def GetIntervalle(self):
      """ 
           Retourne le domaine de valeur attendu par l'objet représenté 
           par l'item.
      """
      return self.object.getintervalle()

  def IsInIntervalle(self,valeur):
      """ 
          Retourne 1 si la valeur est dans l'intervalle permis par
          l'objet représenté par l'item.
      """
      return self.object.isinintervalle(valeur)

  def set_valeur_co(self,nom_co):
      """
      Affecte au MCS pointé par self l'objet de type CO et de nom nom_co
      """
      return self.object.set_valeur_co(nom_co)
      
  def get_sd_avant_du_bon_type(self):
      """
      Retourne la liste des noms des SD présentes avant l'étape qui contient
      le MCS pointé par self et du type requis par ce MCS
      """
      return self.object.etape.parent.get_sd_avant_du_bon_type(self.object.etape,
                                                               self.object.definition.type)
    
  def GetListeValeurs(self) :
      """ Retourne la liste des valeurs de object """
      return self.object.get_liste_valeurs()
    
  def verif(self):
      pass

  def isvalid(self):
    return self.object.isvalid()

  def eval_valeur(self,valeur):
      """ Lance l'interprétation de 'valeur' (chaîne de caractères) comme valeur
      de l'objet pointé par self :
        - retourne l'objet associé si on a pu interpréter (entier, réel, ASSD,...)
        - retourne 'valeur' (chaîne de caractères) sinon """
      return self.object.eval_valeur(valeur)

  def is_CO(self,valeur=None):
      """
         Indique si valeur est un concept produit de la macro
         Cette méthode n'a de sens que pour un MCSIMP d'une MACRO
         Si valeur vaut None on teste la valeur du mot cle
      """
      # Pour savoir si un concept est un nouveau concept de macro
      # on regarde s'il est présent dans l'attribut sdprods de l'étape
      # ou si son nom de classe est CO.
      # Il faut faire les 2 tests car une macro non valide peut etre
      # dans un etat pas tres catholique avec des CO pas encore types
      # et donc pas dans sdprods (resultat d'une exception dans type_sdprod)
      if not valeur:valeur=self.object.valeur
      if valeur in self.object.etape.sdprods:return 1
      if type(valeur) is not types.ClassType:return 0
      if valeur.__class__.__name__ == 'CO':return 1
      return 0

  def delete_valeur_co(self,valeur=None):
      """
           Supprime la valeur du mot cle (de type CO)
           il faut propager la destruction aux autres etapes
      """
      if not valeur : valeur=self.object.valeur
      # XXX faut il vraiment appeler del_sdprod ???
      #self.object.etape.parent.del_sdprod(valeur)
      self.object.etape.parent.delete_concept(valeur)

import Accas
treeitem = SIMPTreeItem
objet = Accas.MCSIMP

