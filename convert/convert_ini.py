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
    Ce module contient le plugin convertisseur de fichier
    au format ini pour EFICAS.
    Le convertisseur supporte le format de sortie eval

    Le format eval est un texte Python qui peut etre 
    evalué avec la commande eval de Python. Il doit donc 
    etre une expression Python dont l'évaluation permet d'obtenir un objet

"""
import traceback

from ConfigParser import ConfigParser
from Noyau import N_CR

def entryPoint():
   """
       Retourne les informations nécessaires pour le chargeur de plugins
       Ces informations sont retournées dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'ini',
        # La factory pour créer une instance du plugin
          'factory' : IniParser,
          }


class IniParser(ConfigParser):
   """
       Ce convertisseur lit un fichier au format ini avec la 
       methode readfile : convertisseur.readfile(nom_fichier)
       et retourne le texte au format outformat avec la 
       methode convertisseur.convert(outformat)

       Ses caractéristiques principales sont exposées dans 2 attributs 
       de classe :
         - extensions : qui donne une liste d'extensions de fichier préconisées
         - formats : qui donne une liste de formats de sortie supportés
   """
   # Les extensions de fichier préconisées
   extensions=('.ini','.conf')
   # Les formats de sortie supportés (eval ou exec)
   formats=('eval','dict')

   def __init__(self,cr=None):
      ConfigParser.__init__(self)
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR convertisseur format ini',
                         fin='fin CR format ini')

   def readfile(self,filename):
      try:
         self.read(filename)
      except Exception,e:
         self.cr.fatal(str(e))

   def convert(self,outformat,appli=None):
      if outformat == 'eval':
         return self.getdicttext()
      elif outformat == 'dict':
         return self.getdict()
      else:
         raise "Format de sortie : %s, non supporté"

   def getdicttext(self):
      s='{'
      for section in self.sections():
         s=s+ "'" + section + "' : {"
         options=self.options(section)
         for option in options:
            value=self.get(section,option)
            if value == '':value="None"
            s=s+"'%s' : %s," % (option, value)
         s=s+"}, "
      s=s+"}"
      return s

   def getdict(self):
      s={}
      for section in self.sections():
         s[section]=d={}
         options=self.options(section)
         for option in options:
            value=self.get(section,option)
            if value == '':
               d[option]=None
            else:
               d[option]=eval(value)
      return s

