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
import os
import sys
import types
import string
import Pmw
from widgets import showinfo
from Tkinter import *

# Modules Eficas
import fontes
from widgets import *
from treewidget import Tree
from Objecttreeitem import TreeItem
from Accas import AsException
from Noyau.N_CR import justify_text

from Accas import ASSD,GEOM
import definition_cata

#
__version__="$Name:  $"
__Id__="$Id: cataediteur.py,v 1.7 2005/08/09 09:54:02 eficas Exp $"
#

Fonte_Niveau = fontes.canvas_gras_italique

class Panel(Frame) :
  """ Classe servant de classe mère à toutes celles représentant les
      panneaux à afficher en fonction de la nature de l'objet en cours
      Elle est toujours dérivée."""
  def __init__(self,parent,panneau,node) :
      self.parent=parent
      self.panneau = panneau
      self.node=node
      Frame.__init__(self,self.panneau)
      self.place(x=0,y=0,relheight=1,relwidth=1)
      #self.creer_boutons()
      self.init()

  def creer_boutons(self):
      """ Méthode créant les boutons se trouvant dans la partie contextuelle d'EFICAS
      (à droite sous les onglets ) """
      self.fr_but = Frame(self,height=30)
      self.fr_but.pack(side='bottom',fill='x')
      self.bouton_com = Button(self.fr_but,
                               text = 'Commentaire',
                               command = self.ajout_commentaire,
                               width=14)
      self.bouton_sup = Button(self.fr_but,
                               text = "Supprimer",
                               command=self.supprimer,
                               width=14)
      self.bouton_doc = Button(self.fr_but,
                               text="Documentation",
                               command=self.visu_doc,
                               width=14)
      self.bouton_cata = Button(self.fr_but,
                                text = "Catalogue",
                                command = self.show_catalogue,
                                width=14)
      if self.parent.appli.CONFIGURATION.isdeveloppeur == 'OUI':
          self.bouton_sup.place(relx=0.25,rely = 0.5,relheight = 0.8,anchor='w')
          self.bouton_cata.place(relx=0.5,rely = 0.5,relheight = 0.8,anchor='w')
          self.bouton_doc.place(relx=0.75,rely = 0.5,relheight = 0.8,anchor='w')
      else:
          self.bouton_sup.place(relx=0.3,rely = 0.5,relheight = 0.8,anchor='w')
          self.bouton_doc.place(relx=0.7,rely = 0.5,relheight = 0.8,anchor='w')

  def show_catalogue(self):
      try:
          genea = self.node.item.get_genealogie()
          self.parent.appli.browser_catalogue_objet(genea)
      except Exception,e:
          traceback.print_exc()
      
  def efface(self):
      self.node.efface()
      
  def ajout_commentaire(self,ind='after'):
      """ Ajoute un commentaire à l'intérieur du JDC, par défaut après le noeud en cours"""
      if self.parent.modified == 'n' : self.parent.init_modif()
      return self.node.append_brother("COMMENTAIRE",ind)
    
  def ajout_commentaire_first(self):
      """ Ajoute un commentaire en début de JDC"""
      if self.parent.modified == 'n' : self.parent.init_modif()
      return self.node.append_child("COMMENTAIRE",'first')
        
  def visu_doc(self):
      """ Permet d'ouvrir le fichier doc U de la commande au format pdf avec Acrobat Reader
        - Ne fonctionne pas sous UNIX (chemin d'accès Acrobat Reader)
        - indication du chemin d'accès aux fichiers pdf à revoir : trop statique"""
      #cle_doc = self.node.item.get_docu()
      cle_doc = self.parent.appli.get_docu(self.node)
      if cle_doc == None : return
      cle_doc = string.replace(cle_doc,'.','')
      #cle_doc = string.upper(cle_doc)
      commande = self.parent.appli.CONFIGURATION.exec_acrobat
      #nom_fichier = cle_doc+".pdf"
      nom_fichier = cle_doc+".doc"
      rep_fichier = cle_doc[0:2]
      fichier = os.path.abspath(os.path.join(self.parent.appli.CONFIGURATION.path_doc,rep_fichier,nom_fichier))
      print 'commande =',commande
      print 'fichier =',fichier
      print 'existe =',os.path.isfile(fichier)
      if os.name == 'nt':
          os.spawnv(os.P_NOWAIT,commande,(commande,fichier))
      elif os.name == 'posix':
          script ="#!/usr/bin/sh \n%s %s" %(commande,nom_fichier)
          pid = os.system(script)
      
  def supprimer(self):
      """ Suppression du noeud courant """
      if self.parent.modified == 'n' : self.parent.init_modif()
      pere = self.node.parent
      self.node.delete()
      pere.select()
      
  def affiche(self):
      """ Force l'affichage des fenêtres en cours """
      self.tkraise()

  def selectMC(self,name):
      """ On retrouve le mot-clé sous le curseur pour affichage du fr """
      cmd=self.node.item.get_definition()
      texte_infos = ''
      for e in cmd.entites.keys() :
          if e == name :
              texte_infos=getattr(cmd.entites[e],'fr')
              break
      if texte_infos == '' : texte_infos="Pas d'infos disponibles"
      self.parent.appli.affiche_infos(texte_infos)

  def defMC(self,name):
      """ On ajoute un mot-clé à la commande : subnode """
      if name == SEPARATEUR:return
      if self.parent.modified == 'n' : self.parent.init_modif()
      if name != "COMMENTAIRE":
          self.node.append_child(name)
      else :
          self.ajout_commentaire()    

  def selectFilsCmd(self,name):
      pass
          
  def defFilsCmd(self,name):
      pass
    
  def defCmdFirst(self,name):
      """ On ajoute une commande ou un commentaire au début du fichier de commandes """
      if name == SEPARATEUR:return
      if self.parent.modified == 'n' : self.parent.init_modif()
      if name != "COMMENTAIRE":
          new_node = self.node.append_child(name,'first')
      else :
          new_node = self.ajout_commentaire_first()

  def add_commande_avant(self,event=None):
    pass

  def add_commande_apres(self,event=None):
    pass          
        
class OngletPanel(Panel) :
  """ Cette classe est virtuelle et doit être dérivée
      Elle contient les principales méthodes d'affichage des différents onglets"""

  def raisecmd(self,page):
      self.nb.page(page).focus_set()
      if page == 'Concept': self._any.focus()

  def affiche(self):
      page=self.nb.getcurselection()
      self.nb.page(page).focus_set()
      if page == 'Concept':self._any.component('entry').focus_set()
      self.tkraise()

  def makeConceptPage(self,page):
      """ Crée la page de saisie du nom du concept """
      self.label = Label(page,text='Nom du concept :')
      self.label.place(relx=0.1,rely=0.4)
      self._any = Entry(page,relief='sunken')
      self._any.place(relx=0.35,rely=0.4,relwidth=0.5)
      self._any.bind("<Return>",lambda e,s=self:s.execConcept())
      self._any.bind("<KP_Enter>",lambda e,s=self:s.execConcept())
      self._any.insert(0,self.node.item.GetText())
      type_sd = self.node.item.object.get_type_sd_prod()
      if type_sd :
          txt = "L'opérateur courant retourne un objet de type %s" %type_sd
          self.label = Label(page, text = txt)
          self.label.place(relx=0.5,rely=0.55,anchor='n')
      self._any.focus()
          
  def makeCommandePage(self,page):
      """ Affiche la page d'ajout d'une commande relativement à l'objet commande sélectionné """
      titre = "Où voulez-vous insérer une commande par rapport à %s" %self.node.item.object.nom
      Label(page,text=titre).place(relx=0.5,rely=0.2,anchor='w')
      b_avant = Button(page,text='AVANT',
                       command = self.node.item.add_commande_avant)
      b_apres = Button(page,text='APRES',
                       command = self.node.item.add_commande_apres)
      b_avant.place(relx=0.35,rely=0.5,anchor='w')
      b_apres.place(relx=0.65,rely=0.5,anchor='w')

  def deselectMC(self,name):
      self.parent.appli.affiche_infos('')
    
  def get_liste_cmd(self):
      listeCmd = self.node.item.object.niveau.definition.get_liste_cmd()
      return listeCmd

  def get_liste_fils_cmd(self):
      return ['Mot-clé simple','Mot-clé facteur','Bloc']

  def makeMoclesPage(self,page):
      frame1 = Frame(page,height = 20)
      frame1.pack(side='top',fill='x')
      label = Label(frame1,text ="Le mot-clé choisi sera ajouté à la fin du catalogue")
      label.pack(side='top')
      frame2 = Frame(page)
      frame2.pack(side='top',fill='both',expand=1)
      liste_cmd = self.get_liste_fils_cmd()
      liste_commandes = (("<Enter>",self.selectFilsCmd),
                         ("<Leave>",self.deselectFilsCmd),
                         ("<Double-Button-1>",self.defFilsCmd))
      Liste = ListeChoix(self,frame2,liste_cmd,liste_commandes = liste_commandes,titre = "Mots-clés")
      Liste.affiche_liste()

  def deselectFilsCmd(self,name):
      pass
    
  def makeJDCPage(self,page):
      liste_cmd = self.get_liste_cmd()
      liste_commandes = (("<Enter>",self.selectCmd),
                         ("<Leave>",self.deselectCmd),
                         ("<Double-Button-1>",self.defCmdFirst))
      Liste = ListeChoix(self,page,liste_cmd,liste_commandes = liste_commandes,filtre='oui',titre = "Commandes")
      Liste.affiche_liste()

  def makeReglesPage(self,page) :
    regles = []
    regles = self.node.item.get_regles()
    dictionnaire = self.node.item.get_mc_presents()
    texte_regles = []
    l_regles_en_defaut=[]
    if len(regles) > 0:
      i = 0
      for regle in regles :
        texte_regles.append(regle.gettext())
        texte,test = regle.verif(dictionnaire)
        if test == 0 : l_regles_en_defaut.append(i)
        i = i+1
    Liste = ListeChoix(self,page,texte_regles,liste_marques=l_regles_en_defaut,active='non',titre="Règles")
    Liste.affiche_liste()
    #self.afficheListe(page,texte_regles,self.selectRegle,self.execRegle)

  def execConcept(self):
      """ Nomme le concept SD retourné par l'étape """
      if self.parent.modified == 'n' : self.parent.init_modif()
      nom = self._any.get()
      # Pourquoi node.etape ???
      #test,mess = self.node.etape.item.nomme_sd(nom)
      test,mess = self.node.item.nomme_sd(nom)
      self.parent.appli.affiche_infos(mess)
      self.node.racine.update()
  
  def changed(self):
      pass

  def makeAttributsPage(self,page):
    l_attributs=self.node.item.object.attributs
    d_defauts = self.node.item.object.attributs_defauts
    for attribut in l_attributs :
      attr = self.node.item.object.entites_attributs.get(attribut,None)
      if attr.valeur is d_defauts[attribut] :
        texte = attribut+' = '+repr(attr.valeur)+' (defaut)'
      else:
        texte = attribut+' = '+repr(attr.valeur)
      Label(page,text=texte).pack(side='top')

  def makeSimpPage(self,page):
    texte = "Où voulez-vous ajouter un mot-clé simple ?"
    Label(page,text=texte).place(relx=0.5,rely=0.3,anchor='center')
    b1 = Button(page,text='AVANT '+self.node.item.object.nom,command=self.add_simp_avant)
    b2 = Button(page,text='APRES '+self.node.item.object.nom,command=self.add_simp_apres)
    b1.place(relx=0.5,rely=0.5,anchor='center')
    b2.place(relx=0.5,rely=0.6,anchor='center')

  def add_simp_avant(self,event=None):
    """
    Ajoute un mot-clé simple avant celui courant
    """
    self.node.append_brother('new_simp','before')
    self.node.update()

  def add_simp_apres(self,event=None):
    """
    Ajoute un mot-clé simple après celui courant
    """
    self.node.append_brother('new_simp','after')
    self.node.update()    
    
class TYPEPanel(Frame):
  def __init__(self,parent,panneau,node) :
      self.parent=parent
      self.panneau = panneau
      self.node=node
      Frame.__init__(self,self.panneau)
      self.place(x=0,y=0,relheight=1,relwidth=1)
      self.creer_texte()

  def creer_texte(self):
      texte = "Le noeud sélectionné correspond à un type\n"
      self.label = Label(self,text=texte)
      self.label.place(relx=0.5,rely=0.4,relwidth=0.8,anchor='center')

class OPERPanel(OngletPanel):
  def init(self):
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    
    nb.pack(fill = 'both', expand = 1)
    self.nb=nb
    nb.add('Mocles', tab_text='Ajouter mots-clés')
    nb.add('Commandes',tab_text='Ajouter une commande')
    self.makeMoclesPage(nb.page("Mocles"))
    self.makeCommandePage(nb.page("Commandes"))
    nb.tab('Mocles').focus_set()
    nb.setnaturalsize()
    self.affiche()
   
class SIMPPanel(OngletPanel):
  def init(self):
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    nb.pack(fill = 'both', expand = 1)
    self.nb=nb
    nb.add('generaux', tab_text='Données générales')
    nb.add('ihm',tab_text='Données IHM')
    nb.add('mocle',tab_text='Ajouter un mot-cle simple')
    self.makeAttributsGenerauxPage(nb.page("generaux"))
    self.makeAttributsIHMPage(nb.page("ihm"))
    self.makeSimpPage(nb.page('mocle'))
    nb.tab('generaux').focus_set()
    nb.setnaturalsize()
    self.affiche()

  def makeAttributsGenerauxPage(self,page):
    fr1 = Frame(page,bd=1,relief='raised')
    fr2 = Frame(page,bd=1,relief='raised')
    fr3 = Frame(page,bd=1,relief='raised')
    fr4 = Frame(page,bd=1,relief='raised')
    fr5 = Frame(page,bd=1,relief='raised')
    fr1.place(relheight=0.14,relwidth=1,rely=0)
    fr2.place(relheight=0.14,relwidth=1,rely=0.14)
    fr3.place(relheight=0.29,relwidth=1,rely=0.28)
    fr4.place(relheight=0.14,relwidth=1,rely=0.57)
    fr5.place(relheight=0.28,relwidth=1,rely=0.71)
    # nom du mot-clé
    Label(fr1,text = 'Nom :').place(relx=0.05,rely=0.3,anchor='w')
    self.e_nom = Entry(fr1)
    self.e_nom.place(relx=0.35,rely=0.3,relwidth=0.3,anchor='w')
    self.e_nom.bind("<Return>",lambda e,s=self : s.set_valeur_attribut('nom',None))
    self.e_nom.bind("<KP_Enter>",lambda e,s=self : s.set_valeur_attribut('nom',None))
    self.e_nom.insert(0,self.get_valeur_attribut('nom'))
    # Statut
    Label(fr1,text='Statut : ').place(relx=0.05,rely=0.7,anchor='w')
    self.statut=StringVar()
    valeurs_statut=[('obligatoire','o'),
                    ('facultatif','f'),
                    ('caché','c')
                    ]
    self.statut.set(self.node.item.object.get_valeur_attribut('statut'))
    i=0
    for text,mode in valeurs_statut:
      b=Radiobutton(fr1,text=text,variable=self.statut,value=mode,
                    command = lambda s=self,m=mode : s.set_valeur_attribut('statut',m))
      b.place(relx=0.25+i*0.25,rely=0.7,anchor='w')
      i=i+1
    # Type ...
    Label(fr2,text='Type de la valeur : ').place(relx=0.05,rely=0.5,anchor='w')
    self.e_type = Entry(fr2)
    self.e_type.place(relx=0.35,rely=0.5,relwidth=0.5,anchor='w')
    self.e_type.insert(0,self.node.item.object.get_valeur_attribut('type'))
    # Domaine de validité
    Label(fr3,text='Domaine de validité : ').place(relx=0.05,rely=0.2,anchor='w')
    self.domaine = StringVar()
    self.domaine.set(self.node.item.object.get_valeur_attribut('domaine_validité'))
    b1=Radiobutton(fr3,text='continu',variable=self.domaine,value='continu',
                   command=lambda s=self,f=fr3 :s.change_domaine(f))
    b2=Radiobutton(fr3,text='discret',variable=self.domaine,value='discret',
                   command=lambda s=self,f=fr3 :s.change_domaine(f))
    b1.place(relx=0.35,rely=0.2,anchor='w')
    b2.place(relx=0.65,rely=0.2,anchor='w')
    self.change_domaine(fr3)
    # Défaut ...
    if self.domaine.get() == 'continu':
      # le développeur peut donner la valeur qu'il souhaite, moyennant la vérification de type...
      Label(fr4,text='Valeur par défaut : ').place(relx=0.05,rely=0.5,anchor='w')
      self.e_defaut = Entry(fr4)
      self.e_defaut.place(relx=0.35,rely=0.5,relwidth=0.5,anchor='w')
      if self.node.item.object.get_valeur_attribut('defaut') :
        self.e_defaut.insert(0,self.node.item.object.get_valeur_attribut('defaut'))
      self.e_defaut.bind("<Return>",lambda e,s=self : s.set_valeur_attribut('defaut',None))
      self.e_defaut.bind("<KP_Enter>",lambda e,s=self : s.set_valeur_attribut('defaut',None))
    else :
      # dans le cas discret, la valeur par défaut doit être dans l'ensemble des valeurs possibles (into)
      liste = self.node.item.object.get_valeur_attribut('into')
      if self.node.item.object.get_valeur_attribut('defaut') :
        self.set_valeur_attribut('defaut',self.node.item.object.get_valeur_attribut('defaut'))
      if liste == None : liste = []
      self.e_defaut = Pmw.OptionMenu(fr4,labelpos='w',label_text = "Valeur par défaut : ",
                                     items = self.node.item.object.get_valeur_attribut('into'),
                                     menubutton_width=30)
      self.e_defaut.configure(command = lambda e,s=self : s.set_valeur_attribut('defaut',None))
      self.e_defaut.place(relx=0.05,rely=0.5,anchor='w')
    # Liste de valeurs ?
    Label(fr5,text='Liste de valeurs : ').place(relx=0.05,rely=0.2,anchor='w')
    self.liste_valeurs = BooleanVar()
    liste_valeurs = [('OUI',1),('NON',0)]
    self.liste_valeurs.set(0)
    i=0
    for text,mode in liste_valeurs:
      b=Radiobutton(fr5,text=text,variable=self.liste_valeurs,value=mode,
                    command=lambda s=self,f=fr5 :s.change_liste_valeurs(f))
      b.place(relx=0.35+i*0.2,rely=0.2,anchor='w')
      i=i+1
    self.change_liste_valeurs(fr5)

  def makeAttributsIHMPage(self,page):
    fr1 = Frame(page,height=100,bd=1,relief='raised')
    fr2 = Frame(page,height=50,bd=1,relief='raised')
    fr1.pack(side='top',fill='x')
    fr2.pack(side='top',fill='x')
    # Champ fr ...
    Label(fr1,text='Champ fr : ').place(relx=0.05,rely=0.35,anchor='w')
    self.e_fr = Entry(fr1)
    self.e_fr.place(relx=0.35,rely=0.35,relwidth=0.6,anchor='w')
    self.e_fr.insert(0,self.node.item.object.get_valeur_attribut('fr'))
    # Champ ang ...
    Label(fr1,text='Champ ang : ').place(relx=0.05,rely=0.70,anchor='w')
    self.e_ang = Entry(fr1)
    self.e_ang.place(relx=0.35,rely=0.70,relwidth=0.6,anchor='w')
    self.e_ang.insert(0,self.node.item.object.get_valeur_attribut('ang'))
    # Clé documentaire ...
    Label(fr2,text='Clé documentaire : ').place(relx=0.05,rely=0.50,anchor='w')
    self.e_docu = Entry(fr2)
    self.e_docu.place(relx=0.35,rely=0.50,relwidth=0.6,anchor='w')
    self.e_docu.insert(0,self.node.item.object.get_valeur_attribut('docu'))
    
  def detruit_widgets(self,l_widgets):
    for nom_widg in l_widgets :
      try:
        widg = getattr(self,nom_widg)
        widg.place_forget()
        delattr(self,nom_widg)
      except:
        pass

  def change_liste_valeurs(self,fr5):
    valeur = self.liste_valeurs.get()
    if valeur == 0 :
      # pas de liste de valeurs
      l_widgets=['l_homo','b1_homo','b2_homo','l_min','e_min','l_max','e_max']
      self.detruit_widgets(l_widgets)
    elif valeur == 1:
      # pas de widgets à détruire ...
      if hasattr(self,'l_homo') :
        # on est déjà en mode 'liste' --> rien à faire
        return 
      # homo
      self.l_homo = Label(fr5,text='Liste homogène : ')
      self.l_homo.place(relx=0.05,rely=0.4,anchor='w')
      self.homo = BooleanVar()
      self.homo.set(self.node.item.object.get_valeur_attribut('homo'))
      self.b1_homo=Radiobutton(fr5,text='OUI',variable=self.homo,value=1)
      self.b2_homo=Radiobutton(fr5,text='NON',variable=self.homo,value=0)
      self.b1_homo.place(relx=0.35,rely=0.4,anchor='w')
      self.b2_homo.place(relx=0.65,rely=0.4,anchor='w')
      # min ...
      self.l_min = Label(fr5,text='Longueur minimale : ')
      self.l_min.place(relx=0.05,rely=0.6,anchor='w')
      self.e_min = Entry(fr5)
      self.e_min.place(relx=0.4,rely=0.6,relwidth=0.3,anchor='w')
      self.e_min.insert(0,self.node.item.object.get_valeur_attribut('min'))
      # max ...
      self.l_max = Label(fr5,text='Longueur maximale : ')
      self.l_max.place(relx=0.05,rely=0.8,anchor='w')
      self.e_max = Entry(fr5)
      self.e_max.place(relx=0.4,rely=0.8,relwidth=0.3,anchor='w')
      self.e_max.insert(0,self.node.item.object.get_valeur_attribut('max'))
      
  def change_domaine(self,fr3):
    valeur = self.domaine.get()
    if valeur == 'discret' :
      l_widgets = ['l_val_min','l_val_max','e_val_min','e_val_max']
      self.detruit_widgets(l_widgets)
      # into
      #self.l_into = Label(fr3,text='Ensemble de valeurs : ')
      #self.l_into.place(relx=0.2,rely=0.5,anchor='w')
      self.e_into = Pmw.ScrolledListBox(fr3,
                                        items=self.node.item.object.get_valeur_attribut('into'),
                                        labelpos='w',
                                        label_text= 'Ensemble de valeurs : ',
                                        listbox_height = 3,
                                        dblclickcommand = self.change_into)
      self.e_into.place(relx=0.05,rely=0.6,relwidth=0.9,anchor='w')
      #self.e_into.insert(0,self.node.item.object.get_valeur_attribut('into'))
    elif valeur == 'continu':
      l_widgets = ['l_into','e_into']
      self.detruit_widgets(l_widgets)
      if hasattr(self,'l_val_min'):
        # on est déjà en mode 'continu' --> rien à faire
        return
      # val_min
      self.l_val_min = Label(fr3,text='Valeur minimale : ')
      self.l_val_min.place(relx=0.05,rely=0.5,anchor='w')
      self.e_val_min = Entry(fr3)
      self.e_val_min.place(relx=0.35,rely=0.5,relwidth=0.5,anchor='w')
      self.e_val_min.bind("<Return>",lambda e,s=self : s.set_valeur_attribut('val_min',None))
      self.e_val_min.bind("<KP_Enter>",lambda e,s=self : s.set_valeur_attribut('val_min',None))
      self.set_valeur_attribut('val_min',self.get_valeur_attribut('val_min'))
      # val_max
      self.l_val_max = Label(fr3,text='Valeur maximale : ')
      self.l_val_max.place(relx=0.05,rely=0.8,anchor='w')
      self.e_val_max = Entry(fr3)
      self.e_val_max.place(relx=0.35,rely=0.8,relwidth=0.5,anchor='w')
      self.e_val_max.bind("<Return>",lambda e,s=self : s.set_valeur_attribut('val_max',None))
      self.e_val_max.bind("<KP_Enter>",lambda e,s=self : s.set_valeur_attribut('val_max',None))
      self.set_valeur_attribut('val_max',self.get_valeur_attribut('val_max'))

# ------------------------------------------------------------------
# Méthodes de validation des entrées faites par l'utilisateur
# ------------------------------------------------------------------

  def get_valeur_attribut(self,nom_attr):
    """
    Demande à l'item de retourner la valeur de l'attribut nom_attr
    """
    return self.node.item.get_valeur_attribut(nom_attr)
  
  def set_valeur_attribut(self,nom_attr,new_valeur):
    """
    Affecte la valeur new_valeur à l'attribut nom_attr
    Vérifie si celle-ci est valide, sinon restaure l'ancienne
    """
    if new_valeur is None :
      widget = getattr(self,'e_'+nom_attr)
      if hasattr(widget,'getcurselection'):
        new_valeur = widget.getcurselection()
      else:
        new_valeur = widget.get()
    print "on affecte %s a %s" %(str(new_valeur),nom_attr)
    self.node.item.set_valeur_attribut(nom_attr,new_valeur)
    self.node.update()

  def change_into(self):
    """
    Méthode activée par double clic sur la ListBox d'affichage des valeurs discrètes possibles :
    permet de changer la liste de ces valeurs
    """
    showinfo("Fonction non encore disponible",
             "Vous ne pouvez pas encore modifier la liste into par cette IHM")
    
class OBJECTItem(TreeItem):
  def __init__(self,appli,labeltext,object,setfunction=None,objet_cata_ordonne = None):
    self.appli = appli
    self.labeltext = labeltext
    self.object=object
    self.setfunction = setfunction
    self.objet_cata_ordonne = objet_cata_ordonne
    
  def GetLabelText(self):
    return self.labeltext,None,None

  def get_fr(self):
    return ''
  
  def isMCList(self):
    return 0

  def isactif(self):
    return 1

  def add_commande_avant(self):
    pass

  def add_commande_apres(self):
    pass

  def set_valeur_attribut(self,nom_attr,new_valeur):
    """
    Affecte la valeur new_valeur à l'attribut nom_attr
    Vérifie si celle-ci est valide, sinon restaure l'ancienne
    """
    old_valeur = self.object.get_valeur_attribut(nom_attr)
    self.object.set_valeur_attribut(nom_attr,new_valeur)
    verificateur = 'verif_'+nom_attr
    if hasattr(self.object,verificateur):
      if not getattr(self.object,verificateur)():
        # la nouvelle valeur de nom_attr n'est pas valide : on restaure l'ancienne (sans vérification)
        self.object.set_valeur_attribut(nom_attr,old_valeur)
        print 'changement de valeur refuse'
        return
    print 'changement de valeur accepte'
    self.object.init_modif()

  def get_valeur_attribut(self,nom_attr):
    """
    Retourne la valeur de l'attribut nom_attr
    """
    return self.object.get_valeur_attribut(nom_attr)
        
class CATAItem(OBJECTItem):
  def GetSubList(self):
    sublist=[]
    for fils in self.object.entites_fils:
      item = make_objecttreeitem(self.appli,fils.objet.label + " : ",fils,objet_cata_ordonne=self.objet_cata_ordonne)
      sublist.append(item)
    return sublist
  
  def GetIconName(self):
    if self.object.isvalid():
      return 'ast-green-square'
    else:
      return 'ast-red-square'

  def GetText(self):
    return "Catalogue %s" %self.appli.code

  def add_commande_avant(self):
    pass

  def add_commande_apres(self):
    pass

     
def transforme_liste_dico(liste):
  d={}
  for item in liste :
    d[item.nom]=item
  return d
      
class OPERItem(OBJECTItem):
  panel = OPERPanel
  def GetSubList(self):
    sublist=[]
    # on classe les fils dans l'ordre du catalogue ...
    l_cles_fils = self.get_liste_mc_ordonnee()
    # on crée les items fils ...
    dico_fils = transforme_liste_dico(self.object.entites_fils)
    for k in l_cles_fils :
      typ = TYPE_COMPLET(dico_fils[k])
      if type(self.objet_cata_ordonne) == types.InstanceType :
        objet_cata = self.objet_cata_ordonne.entites[k]
      else :
        objet_cata = self.objet_cata_ordonne.get(k,None)
      item = make_objecttreeitem(self.appli,typ + " : ",dico_fils[k],objet_cata_ordonne = objet_cata)
      sublist.append(item)
    return sublist

  def GetText(self):
    #return self.object.nom
    return self.object.get_valeur_attribut('nom')

  def get_liste_mc_ordonnee(self):
    return self.objet_cata_ordonne.ordre_mc

  def GetIconName(self):
    if self.object.isvalid():
      return 'ast-green-square'
    else:
      return 'ast-red-square'

  def additem(self,name,pos):
      if isinstance(name,TreeItem) :
          cmd=self.object.addentite(name.getObject(),pos)
      else :
          cmd = self.object.addentite(name,pos)
      typ = TYPE_COMPLET(cmd)
      item = make_objecttreeitem(self.appli,typ + " : ", cmd)
      return item

  def get_attribut(self,nom):
    if nom == 'nature': return 'OPERATEUR'

  def get_liste_mc_presents(self):
    return []

  def verif_condition_regles(self,liste):
    return []
  
class PROCItem(OPERItem):
  panel = OPERPanel
  
class MACROItem(OPERItem):
  panel = OPERPanel
    
class SIMPItem(OPERItem):
  panel = SIMPPanel
  
  def GetIconName(self):
    if self.object.isvalid():
      return 'ast-green-ball'
    else:
      return 'ast-red-ball'

  def IsExpandable(self):
    return 0

  def GetSubList(self):
    return []
  
class FACTItem(OPERItem):
  def GetIconName(self):
    if self.object.isvalid():
      return 'ast-green-los'
    else:
      return 'ast-red-los'

class BLOCItem(FACTItem): pass

class TYPEItem(SIMPItem):
  panel = TYPEPanel
  def get_dico_attributs(self):
    self.d_attributs = {}

  def GetSubList(self):
    return []

  def IsExpandable(self):
    return 0

  def GetText(self):
    return self.object.nom

class NIVEAUItem(OPERItem):
  def IsExpandable(self):
      return 1

  def get_liste_mc_ordonnee(self):
    l=[]
    for fils in self.object.entites_fils:
      l.append(fils.nom)
    return l
  
  def GetSubList(self):
    sublist=[]
    # on classe les fils dans l'ordre du catalogue ...
    l_cles_fils = self.get_liste_mc_ordonnee()
    # on crê¥ les items fils ...
    dico_fils = transforme_liste_dico(self.object.entites_fils)
    for k in l_cles_fils :
      typ = TYPE_COMPLET(dico_fils[k])
      if type(self.objet_cata_ordonne) == types.InstanceType :
        objet_cata = self.objet_cata_ordonne.entites[k]
      else :
        objet_cata = self.objet_cata_ordonne.get(k,None)
      item = make_objecttreeitem(self.appli,typ + " : ",dico_fils[k],objet_cata_ordonne = objet_cata)
      sublist.append(item)
    return sublist
  
  def GetLabelText(self):
      """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
      """
      return self.labeltext,Fonte_Niveau,'#00008b'
    
  def GetIconName(self):
    if self.object.isvalid():
      return "ast-green-text"
    else:
      return 'ast-red-text'

  def additem(self,name,pos):
      if isinstance(name,TreeItem) :
          cmd=self.object.addentite(name.getObject(),pos)
      else :
          cmd = self.object.addentite(name,pos)
      typ = TYPE_COMPLET(obj)
      item = make_objecttreeitem(self.appli,typ+ " : ", cmd)
      return item

  def suppitem(self,item) :
    # item = item de l'ETAPE à supprimer du JDC
    # item.getObject() = ETAPE ou _C
    # self.object = JDC
    itemobject=item.getObject()
    if self.object.suppentite(itemobject):
       if isinstance(itemobject,_C):
          message = "Commentaire supprimé"
       else :
          message = "Commande " + itemobject.nom + " supprimée"
       self.appli.affiche_infos(message)
       return 1
    else:
       self.appli.affiche_infos("Pb interne : impossible de supprimer cet objet")
       return 0

  def GetText(self):
      return ''
    
class ATTRIBUTItem(SIMPItem):
  def get_dico_attributs(self):
    self.d_attributs = {}

  def GetSubList(self):
    return []

  def IsExpandable(self):
    return 0

  def GetText(self):
    return self.object

  def GetIconName(self):
    return 'aucune' 

class CataEditeur:
  def __init__(self,parent,appli,cata):
    self.parent = parent
    self.cata = definition_cata.CATALOGUE(cata)
    self.appli = appli
    self.top = Toplevel()
    self.top.geometry("800x500")
    self.top.title("Edition d'un catalogue")
    self.init()

  def close(self):
    self.top.destroy()

  def init(self):
    self.nodes={}
    self.creerbarremenus()
    self.pane = Pmw.PanedWidget(self.top,
                                hull_width = 800,
                                hull_height = 500,
                                orient = 'horizontal')
    self.pane.add('canvas',min = 0.4, max = 0.6, size = 0.45)
    self.pane.add('panel',min = 0.4, max = 0.6, size = 0.55)
    self.pane.pack(expand =1, fill = 'both')
    self.scrolledcanvas = Pmw.ScrolledCanvas(self.pane.pane('canvas'),
                                             hull_width=1.,
                                             hull_height=1.,
                                             borderframe=1)
    Pmw.Color.changecolor(self.scrolledcanvas.component('canvas'),background='gray95')
    self.scrolledcanvas.pack(padx=10,pady=10,expand=1, fill="both")
    self.item = CATAItem(self.appli,"Catalogue",
                           self.cata,
                          objet_cata_ordonne = self.appli.readercata.cata_ordonne_dico)

    self.tree = Tree(self.appli,self.item,self.scrolledcanvas,command = self.select_node)
    self.tree.draw()
    self.node = self.tree.node_selected

  def creerbarremenus(self) :
      self.menubar=Menu(self.top)
      self.filemenu=Menu(self.menubar,tearoff=0)
      self.filemenu.add_command(label='Quitter',command=self.quit)

      self.editmenu=Menu(self.menubar,tearoff=0)
      #self.editmenu.add_command(label='Copier',command=self.copy)
      #self.editmenu.add_command(label='Couper',command=self.cut)
      #self.editmenu.add_command(label='Coller',command=self.paste)

      self.affichagemenu=Menu(self.menubar,tearoff=0)
      self.affichagemenu.add_command(label='Rapport de validation',
                                     command = self.visuCR)
      self.affichagemenu.add_command(label='shell',command = self.shell)
      #self.affichagemenu.add_command(label='Fichier à¡°lat',command=self.visu_a_plat)
      #self.affichagemenu.add_command(label='Fichier .py',command =self.visuJDC_py)
      #self.affichagemenu.add_command(label='Fichier source',command = self.visu_txt_brut_JDC)
      #self.affichagemenu.add_command(label='Paraméµ²es Eficas',command=self.affichage_fichier_ini)
      
      #self.optionmenu=Menu(self.menubar,tearoff=0)
      #self.optionmenu.add_command(label='Catalogue dê·¥loppeur',command=self.choix_cata_developpeur)

      self.menubar.add_cascade(label='Fichier',menu=self.filemenu)
      self.menubar.add_cascade(label='Edition',menu=self.editmenu)
      self.menubar.add_cascade(label='Jeu de commandes',menu=self.affichagemenu)
      #self.menubar.add_cascade(label='Browsers',menu=self.browsermenu)
      #self.menubar.add_cascade(label='Catalogue',menu=self.cataloguemenu)
      #self.menubar.add_cascade(label='Options',menu=self.optionmenu)
      self.top.configure(menu=self.menubar)
      self.top.protocol("WM_DELETE_WINDOW",self.quit)
      self.top.minsize(900,500)
      self.top.geometry("900x500")

  def shell(self,event=None):
      import Interp
      d={'j':self.tree.item.getObject()}
      Interp.InterpWindow(d,parent=self.parent)
      
  def visuCR(self,mode='Cata'):
    txt = str(self.cata.report())
    titre="Rapport de validation du catalogue"
    Fenetre(self.appli,titre=titre,texte=txt)
  
  def select_node(self,node):
    self.nodes[node]=self.create_panel(node)

  def create_panel(self,node):
    if hasattr(node.item,"panel"):
      return getattr(node.item,"panel")(self,self.pane.pane('panel'),node)
      
  def quit(self) :
    self.top.destroy()
    
  def settitle(self):
    self.top.wm_title("Browser de catalogue " )
    self.top.wm_iconname("CataBrowser")

 
dispatch = {
    'OPER'   : OPERItem,
    'PROC'   : PROCItem,
    'MACRO'  : MACROItem,
    'SIMP'   : SIMPItem,
    'FACT'   : FACTItem,
    'BLOC'   : BLOCItem,
    'TYPE'   : TYPEItem,
    'NIVEAU' : NIVEAUItem
}

def TYPE(o):
  if isinstance(o,definition_cata.OPER_CATA):return 'OPER'
  elif isinstance(o,definition_cata.PROC_CATA):return 'PROC'
  elif isinstance(o,definition_cata.MACRO_CATA):return 'MACRO'
  elif isinstance(o,definition_cata.SIMP_CATA):return 'SIMP'
  elif isinstance(o,definition_cata.FACT_CATA):return 'FACT'
  elif isinstance(o,definition_cata.BLOC_CATA):return 'BLOC'
  elif isinstance(o,definition_cata.TYPE_CATA):return 'TYPE'
  elif isinstance(o,definition_cata.NIVEAU_CATA) : return 'NIVEAU'
  else:return type(o)

def TYPE_COMPLET(o):
  if isinstance(o,definition_cata.OPER_CATA):return "OPERATEUR"
  elif isinstance(o,definition_cata.PROC_CATA):return "PROCEDURE"
  elif isinstance(o,definition_cata.MACRO_CATA):return "MACRO"
  elif isinstance(o,definition_cata.SIMP_CATA):return "Mot-clé SIMPLE"
  elif isinstance(o,definition_cata.FACT_CATA):return "Mot-clé FACTEUR"
  elif isinstance(o,definition_cata.BLOC_CATA):return "BLOC"
  elif isinstance(o,definition_cata.TYPE_CATA):return "Type"
  elif isinstance(o,definition_cata.NIVEAU_CATA):return "Niveau"
  else: return "Inconnu ("+`type(o)`+")"
  
def make_objecttreeitem(appli,labeltext, object, setfunction=None,objet_cata_ordonne=None):
    t = TYPE(object)
    if dispatch.has_key(t):
      c = dispatch[t]
    else:
      print 'on a un objet de type :',type(object),'  ',object
      c = ATTRIBUTItem
    return c(appli,labeltext, object, setfunction = setfunction,objet_cata_ordonne=objet_cata_ordonne)



