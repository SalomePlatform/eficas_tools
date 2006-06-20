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
    Ce module permet de lancer l'application EFICAS en affichant
    un ecran Splash pour faire patentier l'utilisateur
"""
# Modules Python
import sys
import os

# Modules Eficas
import import_code
import session
import prefs
import convert
import generator
import string
from utils import extension_fichier,stripPath, save_in_file

class DUP :

   def __init__(self,code):
       """
       """
       self.format_fichier="python"
       self.version_code=None
       self.code=code

       self.top=None
       self.test=2
       import configuration
       self.CONFIGURATION=configuration.make_config(self,prefs.REPINI)

       self.load_readercata()
       self.cata=self.readercata.cata

       self.JDC=None
       self.JDCName=""
       self.J2=None

   def load_readercata(self):
       mname='readercata'
       module=__import__(mname,globals(),locals())
       factory=getattr(module,mname.upper())
       appli_composant=factory(self,self.top)
       setattr(self,mname,appli_composant)


   def openJDC(self,fichier):
      if fichier :
          self.fichier = fichier
          e=extension_fichier(fichier)
          self.JDCName=stripPath(fichier)
          self.initialdir = os.path.dirname(os.path.abspath(fichier))
      else :
          return

      format=self.format_fichier
      # Il faut convertir le contenu du fichier en fonction du format
      if convert.plugins.has_key(format):
         # Le convertisseur existe on l'utilise
         p=convert.plugins[format]()
         p.readfile(fichier)
         text=p.convert('exec',self)
         if not p.cr.estvide(): 
            print ("Erreur à la conversion")
            print str(p.cr)
            return

      # On se met dans le repertoire ou se trouve le fichier de commandes
      # pour trouver les eventuels fichiers include ou autres
      # localises a cote du fichier de commandes
      os.chdir(self.initialdir)
      CONTEXT.unset_current_step()
      J=self.cata[0].JdC(procedure=text,appli=self,
                         cata=self.cata,cata_ord_dico=self.readercata.cata_ordonne_dico,
                         nom = self.JDCName,
                         rep_mat=self.CONFIGURATION.rep_mat,
                         )

      J.analyse()

      txt_exception = J.cr.get_mess_exception()
      if txt_exception :
          # des exceptions ont été levées à la création du JDC 
          # --> on affiche les erreurs mais pas le JDC
          self.JDC=J
          print("Erreur fatale au chargement de %s" %file)
      else :
          self.JDC=J

   def modifieJDC(self,texte):
         if texte == None or texte == "" : return
         format="python"
         lignes=string.split(texte,";")
         textedecoup=""
         for l in lignes :
            textedecoup=textedecoup+l+'\n'
         if convert.plugins.has_key(format):
            p=convert.plugins[format]()
            p.settext(textedecoup)
            text=p.convert('exec',self)
            print text
         if not p.cr.estvide(): 
            print ("Erreur à la conversion")
            print str(p.cr)
            return
         self.J2=self.cata[0].JdC(procedure=text,appli=self,
                         cata=self.cata,
                         cata_ord_dico=self.readercata.cata_ordonne_dico,
                         nom = self.JDCName+"2",
                         rep_mat=self.CONFIGURATION.rep_mat,
                         )
         self.J2.definition.code = "MODIF"
         self.J2.analyse()
     

   def saveJDC(self,fichierSortie):
      """ 
          Sauvegarde le JDC courant.
          Retourne 1 si la sauvegarde s'est bien faite, 0 sinon.
      """
      if not hasattr(self,'JDC') : return 0

      format="Modif"

      if generator.plugins.has_key(format):
         g=generator.plugins[format]()
         jdc_formate=g.genermodifparam(self.JDC,self.J2)
         if not g.cr.estvide():
            self.affiche_infos("Erreur à la generation")
            return 0
      else:
         self.affiche_infos("Format %s non reconnu" % format)
         return 0

      self.jdc_fini = string.replace(jdc_formate,'\r\n','\n')

      if not save_in_file(fichierSortie,self.jdc_fini) :
         self.affiche_infos("Problème à la sauvegarde du fichier")
         return 0
      else :
         self.affiche_infos("sauvegarde effectuée")
         return 1


   def affiche_infos(self,mess):
       print mess
          
