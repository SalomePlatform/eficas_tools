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
    Ce module contient la classe EFICAS qui est l'application
    proprement dite. Elle est dérivée de la classe APPLI
"""
# Modules Python
import string
from Tkinter import Label
import Pmw
import traceback

# Modules Eficas
from widgets import showerror
from widgets import askopenfilename
import patches
import appli
from widgets import Fenetre

class EFICAS(appli.APPLI):

  try:
     from prefs import appli_composants
  except:
     appli_composants=['readercata','bureau','browser','options']

  def get_texte_infos(self):
     texte=appli.APPLI.get_texte_infos(self)
     texte = texte + 'Catalogue utilisé : %s\n' %  self.bureau.fic_cata
     return texte

  def exitEFICAS(self):
     self.bureau.exitEFICAS()

  def getBureau(self):
      return self.bureau
      
  def browse(self,result):
      if result == 'Browse':
        self.ulfile = askopenfilename(title="Choix fichier :")
        self._ulfile.setentry(self.ulfile)
      elif result == 'OK':
        self.ulfile = self._ulfile.get()
        # On utilise le convertisseur défini par format_fichier
        source=self.get_source(self.ulfile)
        if source:
           # On a réussi à convertir le fichier self.ulfile
           self.dialog.deactivate(result)
           self.text=source
        else:
           # Une erreur a été rencontrée
           self.text=''
      elif result == 'Cancel':
        self._ulfile.setentry('')
        self.dialog.deactivate(result)
        self.ulfile = None
        self.text=None

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
          texte = texte+'Donnez le nom du fichier correspondant\n à l unité logique %d' % unite
      else:
          texte="Le fichier %s contient une commande %s\n" %(fic_origine,'POURSUITE')
          texte = texte+'Donnez le nom du fichier dont vous \n voulez faire une poursuite'
      w = Label(self.dialog.interior(),
                text = texte)
      w.pack(padx = 10, pady = 10)
      if unite != None :
          labeltexte = 'Fichier pour unite %d :' % unite
      else:
          labeltexte = 'Fichier à poursuivre :'
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
            self.affiche_infos("Erreur à la conversion")
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

  def affiche_texte(self,entete,texte):
      """Cette methode ouvre une fenetre modale dans laquelle on affiche un texte
      """
      self.affiche_infos(entete)
      f=Fenetre(self, titre=entete, texte = texte)
      f.wait()

