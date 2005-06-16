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
import string
import os
from Tkinter import *
import Pmw
import time
import traceback

import widgets
from widgets import ListeChoix
from widgets import ListeChoixParGroupes
import prefs
import options

SEPARATEUR = '-'*30


class Panel(Frame) :
  """
  Classe servant de classe mère à toutes celles représentant les
  panneaux à afficher en fonction de la nature de l'objet en cours
  Elle est toujours dérivée.
  """
  def __init__(self,parent,panneau,node) :
      # Le parent d'un panel est un objet de la classe JDCDISPLAY ou derivee
      # ou un objet qui a les attributs : appli (de classe APPLI ou derivee),
      # modified et la methode init_modif
      self.parent=parent
      self.panneau = panneau
      self.node=node
      Frame.__init__(self,self.panneau)
      self.place(x=0,y=0,relheight=1,relwidth=1)
      self.creer_boutons()
      self.init()

  def __del__(self):
      """ appele a la destruction du panel """
      #print "PANEL DETRUIT"

  def update_panel(self):
      """Methode appele pour demander une mise a jour du panneau"""

  def destroy(self):
      Frame.destroy(self)
      self.panneau=None
      self.parent=None
      # Because on herite de Frame
      self.master=None
      # On supprime explicitement les references aux objets Tk
      self.nb=None
      self.fr_but=None
      self.bouton_cata=None
      self.bouton_doc=None
      self.bouton_com=None
      self.bouton_sup=None
      #self.frame_eval=None
      self.label=None
      self.frame_boutons=None
      self.frame_comment=None
      self.frame_param=None
      # On termine la suppression de facon brutale (objets Tk et non Tk)
      for k in self.__dict__.keys():
         # il est plus prudent de ne pas détruire le lien sur le Node
	 # si on voulait mettre l'attribut node à None, il faudrait
	 # que tous les appels à node.parent.select() apparaissent après
	 # toutes les autres actions liées au panel (node.item.isglobal(), ...)
         if k != 'node' : setattr(self,k,None)

  def creer_boutons(self):
      """
      Méthode créant les boutons se trouvant dans la partie contextuelle d'EFICAS
      (à droite sous les onglets )
      """
      self.fr_but = Frame(self,height=30)
      self.fr_but.pack(side='bottom',fill='x')
      self.bouton_com = Button(self.fr_but,
                               text = 'Commentariser',
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
          self.bouton_sup.place(relx=0.25,rely = 0.5,relheight = 0.8,anchor='center')
          self.bouton_cata.place(relx=0.5,rely = 0.5,relheight = 0.8,anchor='center')
          self.bouton_doc.place(relx=0.75,rely = 0.5,relheight = 0.8,anchor='center')
      else:
          self.bouton_sup.place(relx=0.3,rely = 0.5,relheight = 0.8,anchor='center')
          self.bouton_doc.place(relx=0.7,rely = 0.5,relheight = 0.8,anchor='center')

  def show_catalogue(self):
      try:
          genea = self.node.item.get_genealogie()
          self.parent.appli.browser_catalogue_objet(genea)
      except Exception,e:
          traceback.print_exc()
      
  def efface(self):
      self.node.efface()

# ------------------------------------------------------------------------
#     Méthodes permettant d'ajouter des commentaires, des paramètres
#                     et des objets EVAL.
#       Ces méthodes sont utilisées par les panneaux des JDC,ETAPE,
#                 COMMENTAIRE et PARAMETRE
# ------------------------------------------------------------------------

  def ajout_commentaire(self,ind='after'):
      """
      Ajoute un commentaire à l'intérieur du JDC :
      - si ind='after'  : l'ajoute après l'objet courant
      - si ind='before' : l'ajoute avant.
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      return self.node.append_brother("COMMENTAIRE",ind)
    
  def ajout_commentaire_first(self):
      """
      Ajoute un commentaire en début de JDC
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      return self.node.append_child("COMMENTAIRE",'first')

  def ajout_parametre(self,ind='after'):
      """
      Ajoute un parametre à l'intérieur du JDC :
      - si ind='after'  : l'ajoute après l'objet courant
      - si ind='before' : l'ajoute avant.
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      return self.node.append_brother("PARAMETRE",ind)
    
  def ajout_parametre_first(self):
      """
      Ajoute un parametre en début de JDC
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      return self.node.append_child("PARAMETRE",'first')

#  def ajout_parametre_eval(self,ind='after'):
#      """
#      Ajoute un paramètre EVAL à l'intérieur du JDC :
#      - si ind='after'  : l'ajoute après l'objet courant
#      - si ind='before' : l'ajoute avant.
#      """
#      if self.parent.modified == 'n' : self.parent.init_modif()
#      return self.node.append_brother("PARAMETRE_EVAL",ind)
    
#  def ajout_parametre_eval_first(self):
#      """
#      Ajoute un paramètre EVAL en début de JDC
#      """
#      if self.parent.modified == 'n' : self.parent.init_modif()
#      return self.node.append_child("PARAMETRE_EVAL",'first')
    
# ------------------------------------------------------------------------
   
  def visu_doc(self):
      """ Permet d'ouvrir le fichier doc U de la commande au format pdf avec Acrobat Reader
        - Ne fonctionne pas sous UNIX (chemin d'accès Acrobat Reader)
        - indication du chemin d'accès aux fichiers pdf à revoir : trop statique"""
      cle_doc = self.node.item.get_docu()
      if cle_doc == None : return
      cle_doc = string.replace(cle_doc,'.','')
      cle_doc = string.replace(cle_doc,'-','')
      commande = self.parent.appli.CONFIGURATION.exec_acrobat
      nom_fichier = cle_doc+".pdf"
      fichier = os.path.abspath(os.path.join(self.parent.appli.CONFIGURATION.path_doc,
                                       nom_fichier))
      if os.name == 'nt':
          os.spawnv(os.P_NOWAIT,commande,(commande,fichier,))
      elif os.name == 'posix':
          script ="#!/usr/bin/sh \n%s %s&" %(commande,fichier)
          pid = os.system(script)
      
  def supprimer(self):
      """
      Suppression du noeud courant
      """
      # On signale au parent du panel (le JDCDisplay) une modification 
      self.parent.init_modif()
      self.node.delete()
      
  def affiche(self):
      """ Force l'affichage des fenêtres en cours """
      self.tkraise()

  def selectMC(self,name):
      """ On retrouve le mot-clé sous le curseur pour affichage du fr """
      cmd=self.node.item.get_definition()
      texte_infos = ''
      for e in cmd.entites.keys() :
          if e == name :
              texte_infos=getattr(cmd.entites[e],prefs.lang)
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

  def selectCmd(self,name):
      """ On retrouve la commande sous le curseur pour affichage du fr """
      if name != 'COMMENTAIRE' and name != SEPARATEUR:
          texte_infos=getattr(self.parent.jdc.get_cmd(name),prefs.lang)
          self.parent.appli.affiche_infos(texte_infos)
          
  def defCmd(self,name):
      """
      On ajoute une commande après la commande selectionnée : after
      ou bien on ajoute un commentaire
      """
      if name == SEPARATEUR:return
      if self.parent.modified == 'n' : self.parent.init_modif()
      if name != "COMMENTAIRE":
          #parent=self.node.parent
          #new_obj = parent.item.append_child(name,self.node.item.getObject())
          #parent.children[parent.children.index(self.node)+1].select()
          new_node = self.node.append_brother(name,'after')
      else :
          new_node = self.ajout_commentaire()

  def defCmdFirst(self,name):
      """ On ajoute une commande ou un commentaire au début du fichier de commandes """
      if name == SEPARATEUR:return
      if self.parent.modified == 'n' : self.parent.init_modif()
      if name != "COMMENTAIRE":
          #new_obj = self.node.item.append_child(name,'first')
          #self.node.children[0].select()
          new_node = self.node.append_child(name,'first')
      else :
          new_node = self.ajout_commentaire_first()
        
class OngletPanel(Panel) :
  """ Cette classe est virtuelle et doit être dérivée
      Elle contient les principales méthodes d'affichage des différents onglets"""

  def raisecmd(self,page):
      self.nb.page(page).focus_set()
      if page == 'Concept':
          try:
              self._any.focus()
          except:
              pass
      elif page == 'Commande':
          try:
              self.command_entry.component('entry').focus()
          except:
              pass


  def affiche(self):
      page=self.nb.getcurselection()
      self.nb.page(page).focus_set()
      if page == 'Concept':
          try:
#	      _any est un pointeur sur entry
#	      component est une methode de pmw 
#	      a priori, jamais ok
              self._any.component('entry').focus_set()
          except:
              pass
      self.tkraise()

# ------------------------------------------------------------------------
#     Méthodes permettant d'afficher des pages partagées par différents
#           types d'objets (règles,mots-clés,concept,...)
# ------------------------------------------------------------------------

  def makeConceptPage(self,page):
      """
      Crée la page de saisie du nom du concept
      """
      self.label = Label(page,text='Nom du concept :')
      self.label.place(relx=0.1,rely=0.4)
      self._any = Entry(page,relief='sunken')
      self._any.place(relx=0.35,rely=0.4,relwidth=0.5)
      self._any.bind("<Return>",lambda e,s=self:s.execConcept())
      self._any.insert(0,self.node.item.GetText())
      type_sd = self.node.item.get_type_sd_prod()
      if type_sd :
          txt = "L'opérateur courant retourne un objet de type %s" %type_sd
          self.label = Label(page, text = txt)
          self.label.place(relx=0.5,rely=0.55,anchor='n')
      self._any.focus()
      # aide associée au panneau
      bulle_aide="""Tapez dans la zone de saisie le nom que vous voulez donner
      au concept retounré par l'opérateur courant et pressez <Return> pour valider"""
      page.bind("<Button-3>", lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      page.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
        
  def makeMoclesPage(self,page):
      """
      Crée la page qui affiche la liste des mots-clés que l'on peut
      encore ajouter
      """
      genea =self.node.item.get_genealogie()
      jdc = self.node.item.get_jdc()
      liste_mc=self.node.item.get_liste_mc_ordonnee(genea,jdc.cata_ordonne_dico)
      liste_commandes = (("<Enter>",self.selectMC),
                         ("<Leave>",self.deselectMC),
                         ("<Double-Button-1>",self.defMC))
      Liste = ListeChoix(self,page,liste_mc,liste_commandes = liste_commandes,titre = "Mots-clés permis")
      Liste.affiche_liste()
      # aide associée au panneau
      bulle_aide="""Double-cliquez sur le mot-clé que vous voulez ajouter à
      la commande en cours d'édition"""
      Liste.MCbox.bind("<Button-3>", lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      Liste.MCbox.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

  def makeCommentairePage(self,page):
      label = Label(page,text = "Insérer un commentaire :")
      label.grid(column = 0, row = 2)
      but_avant = Button(page,text = "AVANT",command = lambda s=self :s.ajout_commentaire(ind = 'before'))
      but_apres = Button(page,text = "APRES",command = self.ajout_commentaire)
      but_avant.grid(column = 1,row =2)
      but_apres.grid(column = 1,row =3)
      
  def makeCommandePage(self,page):
      """
         Cree l'onglet
      """
      frame1 = Frame(page,height = 20)
      frame1.pack(side='top',fill='x')
      label = Label(frame1,text ="La commande choisie sera ajoutée\n APRES la commande courante")
      label.pack(side='top')
      frame2 = Frame(page)
      frame2.pack(side='top',fill='both',expand=1)
      liste_commandes = (("<Enter>",self.selectCmd),
                         ("<Leave>",self.deselectCmd),
                         ("<Double-Button-1>",self.defCmd))
      if options.affichage_commandes == "alphabetic":
         liste_cmd = self.get_liste_cmd()
         Liste = ListeChoix(self,frame2,liste_cmd,liste_commandes = liste_commandes,
                                   filtre='oui',titre = "Commandes",optionReturn="oui")
      else:
         liste_commandes=liste_commandes+(("<Return>",self.defCmd),)
         liste_groupes,dict_groupes=self.get_groups()
         Liste = ListeChoixParGroupes(self,frame2,liste_groupes,dict_groupes,
                                      liste_commandes = liste_commandes,
                                      filtre='oui',titre = "Commandes",optionReturn="oui")
      Liste.affiche_liste()
      self.command_entry=Liste.entry
      # aide associée au panneau
      bulle_aide="""Double-cliquez sur la commande que vous voulez ajouter au jeu de commandes"""
      Liste.MCbox.bind("<Button-3>", lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      Liste.MCbox.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      global panneauCommande
      panneauCommande=self

  def makeJDCPage(self,page):
      """
      Crée la page correspondant à un objet de type JDC
      """
      liste_commandes = (("<Enter>",self.selectCmd),
                         ("<Leave>",self.deselectCmd),
                         ("<Double-Button-1>",self.defCmdFirst))
      if options.affichage_commandes == "alphabetic":
         liste_cmd = self.get_liste_cmd()
         Liste = ListeChoix(self,page,liste_cmd,liste_commandes = liste_commandes,
                            filtre='oui',titre = "Commandes",optionReturn="oui")
      else:
         liste_commandes=liste_commandes+(("<Return>",self.defCmd),)
         liste_groupes,dict_groupes=self.get_groups()
         Liste = ListeChoixParGroupes(self,page,liste_groupes,dict_groupes,
                                      liste_commandes = liste_commandes,
                                      filtre='oui',titre = "Commandes",optionReturn="oui")
      Liste.affiche_liste()
       # aide associée au panneau
      bulle_aide="""Double-cliquez sur la commande que vous voulez ajouter au jeu de commandes"""
      Liste.MCbox.bind("<Button-3>", lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      Liste.MCbox.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

  def makeReglesPage(self,page) :
      """
      Crée la page qui affiche la liste des règles avec celle qui ne sont
      pas respectées en rouge
      """
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
      # aide associée au panneau
      bulle_aide="""Ce panneau contient la liste des règles qui s'appliquent à l'objet
      en cours d'édition.
      - en noir : règles valides
      - en rouge : règles violées"""
      Liste.MCbox.bind("<Button-3>", lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      Liste.MCbox.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

  def makeParamCommentPage_for_etape(self,page):
      """
      Crée la page qui offre le choix à l'utilisateur d'ajouter un commentaire
      ou un paramètre, avant ou après le noeud courant dans l'arbre.
      Cette page est destinée aux objets de niveau ETAPE cad à toutes les CMD,
      les commentaires inter commandes et les paramètres
      """
      # les frame ...
      self.frame_comment = Frame(page,bd=1,relief='raised')
      self.frame_param   = Frame(page,bd=1,relief='raised')
      #self.frame_eval    = Frame(page,bd=1,relief='raised')
      self.frame_boutons = Frame(page,bd=1,relief='raised')
      self.frame_comment.place(relx=0,rely=0,relwidth=1,relheight=0.40)
      self.frame_param.place(relx=0,rely=0.40,relwidth=1,relheight=0.40)
      #self.frame_eval.place(relx=0,rely=0.56,relwidth=1,relheight=0.28)
      self.frame_boutons.place(relx=0,rely=0.84,relwidth=1,relheight=0.16)
      # remplissage de la frame commentaire
      Label(self.frame_comment,text = "Insérer un commentaire :").place(relx=0.1,rely=0.5,anchor='w')
      but_comment_avant = Button(self.frame_comment,
                                 text = "AVANT "+self.node.item.get_nom(),
                                 command = lambda s=self :s.ajout_commentaire(ind = 'before'))
      but_comment_apres = Button(self.frame_comment,
                                 text = "APRES "+self.node.item.get_nom(),
                                 command = self.ajout_commentaire)
      but_comment_avant.place(relx=0.6,rely=0.3,anchor='w',relwidth=0.3)
      but_comment_apres.place(relx=0.6,rely=0.7,anchor='w',relwidth=0.3)
      # remplissage de la frame paramètre
      Label(self.frame_param,text = "Insérer un paramètre :").place(relx=0.1,rely=0.5,anchor='w')
      but_param_avant = Button(self.frame_param,
                                 text = "AVANT "+self.node.item.get_nom(),
                                 command = lambda s=self :s.ajout_parametre(ind = 'before'))
      but_param_apres = Button(self.frame_param,
                                 text = "APRES "+self.node.item.get_nom(),
                                 command = self.ajout_parametre)
      but_param_avant.place(relx=0.6,rely=0.3,anchor='w',relwidth=0.3)
      but_param_apres.place(relx=0.6,rely=0.7,anchor='w',relwidth=0.3)
      # remplissage de la frame eval
      #Label(self.frame_eval,text="Insérer un paramètre EVAL :").place(relx=0.1,rely=0.5,anchor='w')
          #Label(self.frame_eval,text='Non encore disponible').place(relx=0.6,rely=0.5,anchor='w')
      #but_eval_avant = Button(self.frame_eval,
      #                        text = "AVANT "+self.node.item.get_nom(),
      #                        command = lambda s=self :s.ajout_parametre_eval(ind = 'before'))
      #but_eval_apres = Button(self.frame_eval,
      #                        text = "APRES "+self.node.item.get_nom(),
      #                        command = self.ajout_parametre_eval)
      #but_eval_avant.place(relx=0.6,rely=0.3,anchor='w',relwidth=0.3)
      #but_eval_apres.place(relx=0.6,rely=0.7,anchor='w',relwidth=0.3)      
      # remplissage de la frame boutons
      Button(self.frame_boutons,
             text="Commentariser toute la commande",
             command = self.comment_commande).place(relx=0.5,rely=0.5,anchor='center')
    
  def deselectMC(self,name):
      self.parent.appli.affiche_infos('')
    
  def get_liste_cmd_BAK(self):
      raise "OBSOLETE"
      listeCmd = self.cata.listCmd()
      return listeCmd

  def get_groups(self):
      jdc=self.node.item.object.get_jdc_root()
      return jdc.get_groups()

  def get_liste_cmd(self):
      #print "get_liste_cmd",self.node.item.object
      jdc=self.node.item.object.get_jdc_root()
      listeCmd = jdc.get_liste_cmd()
      return listeCmd

  def deselectCmd(self,name):
      self.parent.appli.affiche_infos('')
    
  def execConcept(self):
      """
      Nomme le concept SD retourné par l'étape
      """
      if not hasattr(self,'valeur_choisie'):
          nom = self._any.get()
      else:
          nom = self.valeur_choisie.get()
      nom = string.strip(nom)
      if nom == '' : return # si pas de nom, on ressort sans rien faire ...
      if self.parent.modified == 'n' : self.parent.init_modif()
      test,mess = self.node.item.nomme_sd(nom)
      #self.node.verif()
      #self.node.racine.update()
      self.parent.appli.affiche_infos(mess)
  
  def changed(self):
      pass

  def comment_commande(self):
    """
    Cette méthode a pour but de commentariser la commande pointée par self.node
    """
    # On traite par une exception le cas où l'utilisateur final cherche à désactiver
    # (commentariser) un commentaire.
    try :
        pos=self.node.parent.children.index(self.node)
        commande_comment = self.node.item.get_objet_commentarise()
        # On signale au parent du panel (le JDCDisplay) une modification
        self.parent.init_modif()
        self.node.parent.children[pos].select()
    except Exception,e:
        traceback.print_exc()
        widgets.showerror("TOO BAD",str(e))
    return

      
class Panel_Inactif(Panel):
  """
     Cette classe sert à définir un panneau dans lequel on dit que le noeud 
     sélectionné n'est pas actif
  """
  def __init__(self,parent,panneau,node) :
      self.parent=parent
      self.panneau = panneau
      self.node=node
      Frame.__init__(self,self.panneau)
      self.place(x=0,y=0,relheight=1,relwidth=1)
      self.creer_texte()

  def creer_texte(self):
      texte = "Le noeud sélectionné ne correspond pas à un objet actif\n"
      texte = texte + "Seules les commandes placées entre \nDEBUT/POURSUITE et FIN sont actives"
      longueur = int(self.panneau.winfo_width()*0.8)
      self.label = Label(self,text=texte,wraplength=longueur,justify='center')
      self.label.place(relx=0.5,rely=0.4,relwidth=0.8,anchor='center')
      self.bouton_sup = Button(self,
                               text = "Supprimer",
                               command=self.supprimer,
                               width=14)
      self.bouton_sup.place(relx=0.5,rely=0.8,anchor='center')


if __name__ == "__main__" : pass
