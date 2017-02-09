# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
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
from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException


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
      except Exception as e:
         self.cr.fatal(tr("lecture du fichier impossible :")+str(e))

   def convert(self,outformat,appli=None):
      if outformat == 'eval':
         return self.getdicttext()
      elif outformat == 'dict':
         return self.getdict()
      else:
        raise Exception("Format de sortie : %s, non supporte", outformat)


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

