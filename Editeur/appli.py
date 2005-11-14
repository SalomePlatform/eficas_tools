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
from widgets import Fenetre
from Misc import MakeNomComplet
import session
import listeFichiers
import listePatrons

VERSION="EFICAS v1.9"

class APPLI: 
  def __init__ (self,master,code=prefs.code,fichier=None,test=0) :
      self.code=code
      self.top=master
      self.top.protocol("WM_DELETE_WINDOW",self.exitEFICAS)
      self.top.minsize(900,500)
      self.top.geometry("900x500")
      self.top.title(VERSION + ' pour '+self.code)
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
      self.listePatrons=listePatrons.listePatrons(self)

      # PN : ajout d un attribut pour indiquer si 
      # l appli a ete lance depuis Salome
      self.salome=0
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
      self.top.quit()

  def lecture_parametres(self):
      """
          Active la lecture des paramètres standards et utilisateur
      """
      if (self.test == 0):
         splash._splash.configure(text = "Chargement des paramètres utilisateur")
      import configuration
      self.CONFIGURATION = configuration.make_config(self,prefs.REPINI)

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
      self.statusbar=statusbar.STATUSBAR(self.top)

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
          menu=menudict.get(mname)
          if not menu:continue
          self.cree_menu(menu,itemlist,appli_composant)

  def update_jdc_courant(self):
      self.bureau.update_jdc_courant()

  def affiche_alerte(self,titre,message):
      f=Fenetre(self, titre="Compte-rendu d'erreur", texte = titre + "\n\n" + message)
      f.wait()


