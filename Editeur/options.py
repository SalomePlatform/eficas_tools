"""
"""
# Modules Python
import os,string
from tkFileDialog import *

# Modules Eficas


class OPTIONS:

   menu_defs=[
              ('Options',[
                           ("Catalogue développeur",'choix_cata_developpeur'),
                         ]
              )
             ]

   button_defs=[]

   def __init__(self,appli,parent):
      self.appli=appli
      self.parent=parent

   def choix_cata_developpeur(self):
      """ 
          Cette méthode demande à l'utilisateur-développeur d'indiquer quel catalogue
          il veut utiliser en remplacement du catalogue standard du code
          NB : il faut que le développeur ait les droits d'écriture dans le répertoire où
          se trouve le catalogue 
      """
      file = askopenfilename(title="Choix d'un catalogue personnel",
                             defaultextension=".py",
                             filetypes = ( ("Catalogue", "cata*.py"),))
      if file != '':
          self.parent.update_idletasks()
          self.appli.reset_affichage_infos()
          rep_fic = os.path.dirname(file)
          nom_fic = string.split(os.path.basename(file),'.')[0]
          rep_courant = os.getcwd()
          os.chdir(rep_fic)
          self.cata = __import__(nom_fic)
          self.code = self.cata.CODE
          os.chdir(rep_courant)
          self.fic_cata = file
          fic_cata_p = nom_fic+'_pickled.py'
          self.fic_cata_p = os.path.join(rep_fic,fic_cata_p)
          pile_erreurs = self.cata.erreurs_cata
          if pile_erreurs.existe_message() :
              messages = pile_erreurs.retourne_messages()
              print messages
          else :
              # XXX ne doit pas fonctionner
              self.catalo = catabrowser.CataItem(cata=self.cata)
              self.Retrouve_Ordre_Cata('personnel')
          pile_erreurs.efface()

