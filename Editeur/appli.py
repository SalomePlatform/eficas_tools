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
import sys
import Pmw
import Tkinter

# Modules Eficas
import splash
import prefs
import fontes

class APPLI: 
  def __init__ (self,master,code='ASTER',fichier=None) :
      self.top=master
      self.code=code
      self.top.protocol("WM_DELETE_WINDOW",self.exitEFICAS)
      self.top.minsize(900,500)
      self.top.geometry("900x500")
      self.top.title('EFICAS v1.1 pour '+self.code)
      self.top.withdraw()
      self.initializeTk(master)
      Pmw.initialise(master)
      self.lecture_parametres()
      self.format_fichier = Tkinter.StringVar()
      self.message=''
      self.cree_composants_graphiques()
      self.load_extensions()
      self.affiche_FAQ()
      splash.fini_splash()

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
      splash._splash.configure(text = "Chargement des paramètres utilisateur")
      import configuration
      self.CONFIGURATION = configuration.make_config(self,prefs.REPINI)

  def cree_composants_graphiques(self):
      """
          Cree les constituants de l'application :
           - menubar
           - tollbar
           - bureau
           - statusbar
      """
      splash._splash.configure(text = "Chargement de l'IHM")
      splash._splash.configure(text = "Chargement de la menubar")
      import menubar
      self.menubar=menubar.MENUBAR(self,self.top)
      splash._splash.configure(text = "Chargement de la toolbar")
      import toolbar
      self.toolbar=toolbar.TOOLBAR(self,self.top)
      splash._splash.configure(text = "Chargement de la statusbar")
      import statusbar
      self.statusbar=statusbar.STATUSBAR(self.top)

  def load_extensions(self):
      splash._splash.configure(text = "Chargement des extensions")
      for mname in self.extensions:
         self.load_extension(mname)

  def load_extension(self,mname):
      module=__import__(mname,globals(),locals())
      factory=getattr(module,mname.upper())
      extension=factory(self,self.top)
      setattr(self,mname,extension)
      self.fill_menus(extension,extension.menu_defs)
      self.toolbar.creer_boutons_extension(extension.button_defs,extension)

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
        root.option_add('*background', 'grey')
        root.option_add('*foreground', 'black')
        root.option_add('*EntryField.Entry.background', 'white')
	root.option_add('*Entry*background', 'white')
        root.option_add('*Listbox*background', 'white')
        root.option_add('*Listbox*selectBackground', '#00008b')
        root.option_add('*Listbox*selectForeground', 'white')

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
      texte = 'EFICAS v1.1\n\n'
      texte = texte + 'EFICAS est un produit développé par \nEDF-Division Stratégie et Développement\n'
      texte = texte + 'Equipe : MTI/MMN\n\n'
      texte = texte + 'Code utilisé : %s\n' %self.code
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
      self.aide = Tkinter.Label(widget ,text = aide,
                        bg="yellow",relief="ridge",anchor='w')
      self.aide.place(in_=widget,
                      relx=0.5,rely=0.5,anchor='center')
      print aide
      return

  def fill_menus(self,extension,defs):
      menudict=self.menubar.menudict
      for mname,itemlist in defs:
          menu=menudict.get(mname)
          if not menu:continue
          for item in itemlist:
             if not item :
                menu.add_separator()
             else:
                label,method=item
                command=getattr(extension,method)
                menu.add_command(label=label,command=command)
                
      
