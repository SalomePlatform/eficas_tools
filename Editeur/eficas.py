"""
    Ce module contient la classe EFICAS qui est l'application
    proprement dite. Elle est d�riv�e de la classe APPLI
"""
# Modules Python
import string
from Tkinter import Label
import Pmw
from tkCommonDialog import Dialog
from tkFileDialog import *
from tkMessageBox import askyesno,showerror
import traceback

# Modules Eficas
import appli
from widgets import Fenetre

class EFICAS(appli.APPLI):

  extensions=['readercata','bureau','browser','options']

  def get_texte_infos(self):
     texte=appli.APPLI.get_texte_infos(self)
     texte = texte + 'Catalogue utilis� : %s\n' %  self.bureau.fic_cata
     return texte

  def exitEFICAS(self):
     self.bureau.exitEFICAS()

  def browse(self,result):
      if result == 'Browse':
        self.ulfile = askopenfilename(title="Choix fichier :")
        self._ulfile.setentry(self.ulfile)
      elif result == 'OK':
        self.ulfile = self._ulfile.get()
        # On utilise le convertisseur d�fini par format_fichier
        source=self.get_source(self.ulfile)
        if source:
           # On a r�ussi � convertir le fichier self.ulfile
           self.dialog.deactivate(result)
           self.text=source
        else:
           # Une erreur a �t� rencontr�e
           self.text=''
      elif result == 'Cancel':
        self._ulfile.setentry('')
        self.dialog.deactivate(result)
        self.ulfile = None
        self.text=''

  def get_file(self,unite=None,fic_origine = ''):
      """ 
          Retourne le nom du fichier correspondant a l unite logique unite (entier)
      """
      if unite :
          titre = "Choix unite %d " %unite
      else:
          titre = "Choix d'un fichier de poursuite"
      self.dialog=Pmw.Dialog(self.top,
                             title = titre,
                             buttons = ('OK', 'Browse','Cancel'),
                             defaultbutton='OK',
                             command=self.browse,
                             )
      self.dialog.withdraw()
      if unite :
          texte = "Le fichier %s contient une commande INCLUDE \n" % fic_origine
          texte = texte+'Donnez le nom du fichier correspondant\n � l unit� logique %d' % unite
      else:
          texte="Le fichier %s contient une commande %s\n" %(fic_origine,'POURSUITE')
          texte = texte+'Donnez le nom du fichier dont vous \n voulez faire une poursuite'
      w = Label(self.dialog.interior(),
                text = texte)
      w.pack(padx = 10, pady = 10)
      if unite != None :
          labeltexte = 'Fichier pour unite %d :' % unite
      else:
          labeltexte = 'Fichier � poursuivre :'
      self._ulfile=Pmw.EntryField(self.dialog.interior(),
                                  labelpos = 'w',
                                  label_text = labeltexte,
                                  )
      self._ulfile.pack(fill='x', expand=1, padx=10, pady=5)
      self._ulfile.component('entry').focus_set()
      self.dialog.activate(geometry='centerscreenalways')
      return self.ulfile,self.text

  def get_source(self,file):
      import convert
      format=self.format_fichier.get()
      # Il faut convertir le contenu du fichier en fonction du format
      if convert.plugins.has_key(format):
         # Le convertisseur existe on l'utilise
         p=convert.plugins[format]()
         p.readfile(file)
         text=p.convert('execnoparseur')
         if not p.cr.estvide():
            self.affiche_infos("Erreur � la conversion")
            Fenetre(self,
                    titre="compte-rendu d'erreurs, EFICAS ne sait pas convertir ce fichier",
                    texte = str(p.cr)).wait()
            return text
         return text
      else:
         # Il n'existe pas c'est une erreur
         self.affiche_infos("Type de fichier non reconnu")
         showerror("Type de fichier non reconnu","EFICAS ne sait pas ouvrir ce type de fichier")
         return None

