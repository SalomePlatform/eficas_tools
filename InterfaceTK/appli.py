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
"""
    Ce module contient la classe APPLI qui est la classe mère de
    l'application EFICAS. Elle prend en charge l'organisation générale
    des composants graphiques et l'initialisation Tk
    L'aspect applicatif doit etre pris en charge par la classe dérivée
"""
# Modules Python
import os
import string
import sys
import types
import Pmw
import Tkinter
from widgets import showerror

# Modules Eficas
import splash
import prefs
import styles
from styles import style
import fontes
import tooltip
import properties
import convert,generator
from Editeur import comploader
from Editeur.utils import extension_fichier,stripPath

from widgets import Fenetre
from Misc import MakeNomComplet
from Editeur import session

import listeFichiers
import listePatronsTK

REPTK=os.path.dirname(os.path.abspath(__file__))
sys.path[:0]=[REPTK]

VERSION="EFICAS v1.15"

class APPLI: 
  def __init__ (self,master,code=prefs.code,fichier=None,test=0,ihm="TK",salome=0) :
      self.ihm=ihm
      self.code=code
      self.salome=salome
      self.top=master
      self.top.protocol("WM_DELETE_WINDOW",self.exitEFICAS)

      #dimensionnement de la fenetre principale
      #aspect ratio de l'ecran
      aspect=float(self.top.winfo_screenwidth())/float(self.top.winfo_screenheight())
      #resolution (pixels par point). On utilise le fait qu'on a "normalement" 72 points par inch
      resolution= self.top.winfo_screenwidth()/(self.top.winfo_screenmmwidth()/25.4*72)
      DDY=max(20,resolution*(fontes.standard[1]+4)) #largeur d'un caractere fonte standard en pixel
      x=int(45*DDY) #largeur d'ouverture de 45 caracteres de fonte standard 
      y=int(25*DDY) #hauteur d'ouverture de 25 caracteres de fonte standard
      minx=x*8/10 #largeur min (80 pour cent de largeur)
      miny=y*8/10 #hauteur min (80 pour cent de hauteur)
      self.top.minsize(minx,miny)
      self.top.geometry('%dx%d' % (x,y))

      self.top.title(VERSION + ' pour '+self.code)
      self.titre=VERSION + ' pour '+self.code
      self.top.withdraw()
      self.initializeTk(master)
      Pmw.initialise(master)

      self.dict_reels={}
      self.liste_simp_reel=[]
      # L'attribut test permet d'activer les panneaux de splash et d'erreur (test=0)
      # Si test est different de 0, les panneaux ne sont pas activés
      self.test=test

      # Lecture des parametres de configuration (fichier global editeur.ini 
      # et utilisateur eficas.ini)
      self.lecture_parametres()

      self.format_fichier = Tkinter.StringVar()
      self.message=''
      # Avant la creation du bureau qui lit le catalogue
      self.version_code=session.d_env.cata

      # Creation de la menubar, toolbar, messagebar
      self.cree_composants_graphiques()
      # Creation des autres composants graphiques dont le bureau (parametrable par prefs.py)
      self.load_appli_composants()                
      self.listeFichiers=listeFichiers.listeFichiers(self)
      self.listePatrons=listePatronsTK.listePatronsTK(self)
      self.dir=None

      # Fermer le splash et deiconifier la fenetre principale si on n'est pas en test
      if (self.test == 0):
           splash.fini_splash()
           #self.affiche_FAQ()

      # Ouverture des fichiers de commandes donnes sur la ligne de commande
      cwd=os.getcwd()
      self.dir=cwd
      for study in session.d_env.studies:
          os.chdir(cwd)
          d=session.get_unit(study,self)
          self.bureau.openJDC(file=study["comm"],units=d)


  def send_message(self,message):
      self.message=message

  def exitEFICAS(self):
      self.quit()

  def quit(self):
      if self.top:
        self.top.quit()

  def lecture_parametres(self):
      """
          Active la lecture des paramètres standards et utilisateur
      """
      if (self.test == 0):
         splash._splash.configure(text = "Chargement des paramètres utilisateur")
      import configuration
      self.CONFIGURATION = configuration.make_config(self,prefs.REPINI)
      self.CONFIGStyle = configuration.make_config_style(self,prefs.REPINI)

  def cree_composants_graphiques(self):
      """
          Cree les constituants graphiques fixes de l'application :
           - menubar
           - toolbar
           - statusbar
      """
      if (self.test == 0):
         splash._splash.configure(text = "Chargement de l'IHM")
         splash._splash.configure(text = "Chargement de la menubar")
      import menubar
      self.menubar=menubar.MENUBAR(self,self.top)
      if (self.test == 0):
         splash._splash.configure(text = "Chargement de la toolbar")
      import toolbar
      self.toolbar=toolbar.TOOLBAR(self,self.top)
      if (self.test == 0):
         splash._splash.configure(text = "Chargement de la statusbar")
      import statusbar
      self.statusbar=statusbar.STATUSBAR(self.top,styles.style.statusfont)

  def load_appli_composants(self):
      """
          Cree les autres constituants graphiques de l'application :
           - bureau 
           - readercata
           - ...
          Cette creation est parametrable par fichier prefs.py
      """
      if (self.test == 0):
         splash._splash.configure(text = "Chargement des appli_composants")
      for mname in self.appli_composants:
         self.load_appli_composant(mname)

  def load_appli_composant(self,mname):
      module=__import__(mname,globals(),locals())
      factory=getattr(module,mname.upper())
      appli_composant=factory(self,self.top)
      setattr(self,mname,appli_composant)
      self.fill_menus(appli_composant,appli_composant.menu_defs)
      self.toolbar.creer_boutons_appli_composant(appli_composant.button_defs,appli_composant)

  def affiche_FAQ(self):
      import faq
      faq.affiche(self.top)

  def affiche_infos(self,message):
      self.statusbar.affiche_infos(message)
      return

  def  initializeTk(self, root):
        """
        Initialize platform specific options
        """
        if sys.platform == 'mac':
            self.initializeTk_mac(root)
        elif sys.platform == 'win32':
            self.initializeTk_win32(root)
        else:
            self.initializeTk_unix(root)

  def initializeTk_win32(self, root):
        root.option_add('*Font', fontes.standard)
        root.option_add('*EntryField.Entry.Font', fontes.standard)
        root.option_add('*Listbox*Font',fontes.standard)

  def initializeTk_colors_common(self, root):
        root.option_add('*background', style.background)
        root.option_add('*foreground', style.foreground)
        root.option_add('*EntryField.Entry.background', style.entry_background)
        root.option_add('*Entry*background', style.entry_background)
        root.option_add('*Listbox*background', style.list_background)
        root.option_add('*Listbox*selectBackground', style.list_select_background)
        root.option_add('*Listbox*selectForeground', style.list_select_foreground)

  def initializeTk_mac(self, root):
        self.initializeTk_colors_common(root)

  def initializeTk_unix(self, root):
      root.option_add('*Font', fontes.standard)
      root.option_add('*EntryField.Entry.Font',fontes.standard )
      root.option_add('*Listbox*Font', fontes.standard)
      self.initializeTk_colors_common(root)

  def get_texte_infos(self):
      """
          Retourne un texte d'informations sur la session courante d'EFICAS
      """
      texte = VERSION + '\n\n'
      texte = texte + 'EFICAS est un produit développé par \nEDF-R&D\n'
      texte = texte + 'Equipe : SINETICS\n\n'
      texte = texte + 'Code utilisé : %s version %s\n' % (self.code,properties.version)
      return texte

  def efface_aide(self,event):
      """
          Efface la bulle d'aide d'un panneau
      """
      try:
          self.aide.destroy()
      except:
          pass
      return

  def affiche_aide(self,event,aide):
      """
          Affiche l'aide concernant un panneau
      """
      x=event.x
      y=event.y
      widget=event.widget
      self.aide=tooltip.TOOLTIP(widget)
      self.aide.xoffset = 10
      self.aide.yoffset = - widget.winfo_height()/2
      self.aide.setText(aide)
      self.aide._showTip()
      return 

  def cree_menu(self,menu,itemlist,appli_composant):
      """
          Ajoute les items du tuple itemlist
          dans le menu menu
      """
      number_item=0
      radio=None
      for item in itemlist:
         number_item=number_item + 1
         raccourci_label=""
         if not item :
            #menu.add_separator()
            pass
         else:
            if len(item)==3:
               raccourci=item[2]
               raccourci_label="   "+raccourci
               newitem=(item[0],item[1])
            else :
               if len(item)==4:
                  raccourci=item[2]
                  raccourci_label="   "+item[3]
                  newitem=(item[0],item[1])
               else :
                  raccourci=""
                  newitem=item
            item=newitem
            label,method=item
            if type(method) == types.TupleType:
               # On a un tuple => on cree une cascade
               menu_cascade=Tkinter.Menu(menu)
               menu.add_cascade(label=label,menu=menu_cascade)
               self.cree_menu(menu_cascade,method,appli_composant)
            elif method[0] == '&':
               # On a une chaine avec & en tete => on cree un radiobouton
               command=getattr(appli_composant,method[1:])
               menu.add_radiobutton(label=label,command=command)
               if radio == None:radio=number_item
            else:
               command=getattr(appli_composant,method)
               menu.add_command(label=label,accelerator=raccourci_label,command=command)
               if raccourci != "" :
                  self.top.bind(raccourci,command)
      # Si au moins un radiobouton existe on invoke le premier
      if radio:menu.invoke(radio)

  def fill_menus(self,appli_composant,defs):
      menudict=self.menubar.menudict
      for mname,itemlist in defs:
          if mname in menudict.keys() : 
             menu=menudict[mname]
          else :
             continue
          self.cree_menu(menu,itemlist,appli_composant)

  def update_jdc_courant(self):
      self.bureau.update_jdc_courant()

  def affiche_alerte(self,titre,message):
      f=Fenetre(self, titre="Compte-rendu d'erreur", texte = titre + "\n\n" + message)
      f.wait()


class valeur:
   def __init__(self,v=None):
      self.v=v
   def set(self,v):
      self.v=v
   def get(self):
      return self.v

class STANDALONE(APPLI):
   def __init__ (self,code=prefs.code,fichier=None,version='v8.2',ihm="TK") :
      self.ihm=ihm
      self.salome=0
      self.code=code
      self.top=None
      self.format_fichier=valeur()

      self.dict_reels={}
      self.liste_simp_reel=[]
      # L'attribut test doit valoir 1 si on ne veut pas creer les fenetres
      self.test=1
      self.titre="STANDALONE POUR TEST"

      # Lecture des parametres de configuration (fichier global editeur.ini
      # et utilisateur eficas.ini)
      self.lecture_parametres()

      self.message=''
      # Avant la creation du bureau qui lit le catalogue
      self.version_code=version
      import readercata
      self.readercata=readercata.READERCATA(self,None)

      self.dir=None

   def affiche_infos(self,message):
      return

   def get_text_JDC(self,JDC,format):
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         g=generator.plugins[format]()
         jdc_formate=g.gener(JDC,format='beautifie')
         return jdc_formate
      else:
         # Il n'existe pas c'est une erreur
         return

   def newJDC(self):
      CONTEXT.unset_current_step()
      J=self.readercata.cata[0].JdC(procedure="",
                                    appli=self,
                                    cata=self.readercata.cata,
                                    cata_ord_dico=self.readercata.cata_ordonne_dico,
                                    rep_mat=self.CONFIGURATION.rep_mat,
                                   )
      J.analyse()
      return J

   def openJDC(self,file):
      self.fileName = file
      e=extension_fichier(file)
      self.JDCName=stripPath(file)
      self.initialdir = os.path.dirname(os.path.abspath(file))
      format=self.format_fichier.get()
      # Il faut convertir le contenu du fichier en fonction du format
      if convert.plugins.has_key(format):
         # Le convertisseur existe on l'utilise
         p=convert.plugins[format]()
         p.readfile(file)
         text=p.convert('exec',self)
         if not p.cr.estvide():
             raise ValueError(str(p.cr))

      # On se met dans le repertoire ou se trouve le fichier de commandes
      # pour trouver les eventuels fichiers include ou autres
      # localises a cote du fichier de commandes
      os.chdir(self.initialdir)
      CONTEXT.unset_current_step()
      J=self.readercata.cata[0].JdC(procedure=text,
                                    appli=self,
                                    cata=self.readercata.cata,
                                    cata_ord_dico=self.readercata.cata_ordonne_dico,
                                    nom=self.JDCName,
                                    rep_mat=self.CONFIGURATION.rep_mat,
                                   )
      J.analyse()
      txt= J.cr.get_mess_exception()
      if txt:raise ValueError(txt)
      return J

   def openTXT(self,text):
      self.JDCName="TEXT"
      CONTEXT.unset_current_step()
      J=self.readercata.cata[0].JdC(procedure=text,
                                    appli=self,
                                    cata=self.readercata.cata,
                                    cata_ord_dico=self.readercata.cata_ordonne_dico,
                                    nom=self.JDCName,
                                    rep_mat=self.CONFIGURATION.rep_mat,
                                   )
      J.analyse()
      txt= J.cr.get_mess_exception()
      if txt:raise ValueError(txt)
      return J

   def create_item(self,obj):
      return comploader.make_objecttreeitem(self,getattr(obj,"nom","item"),obj)

   def get_file(self,unite=None,fic_origine = ''):
      """
          Retourne le nom du fichier correspondant a l unite logique unite (entier)
          ou d'un fichier poursuite
      """
      f,ext=os.path.splitext(fic_origine)
      if unite :
          #include
          finclude=f+".%d" % unite
      else:
          #poursuite
          n=ext[-1]
          if n == '0':
             ext=".comm"
          else: 
             ext=".com%d" % (string.atoi(n)-1)
             if ext == '.com0' and not os.path.isfile(f+".com0"):
                ext=".comm"
          finclude=f+ext
      ff=open(finclude)
      text=ff.read()
      ff.close()
      return finclude,text

   def affiche_alerte(self,titre,message):
      print titre+ "\n\n" + message
