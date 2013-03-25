# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
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
    au format python pour EFICAS.

    Un plugin convertisseur doit fournir deux attributs de classe :
    extensions et formats et deux méthodes : readfile,convert.

    L'attribut de classe extensions est une liste d'extensions
    de fichiers préconisées pour ce type de format. Cette information
    est seulement indicative.

    L'attribut de classe formats est une liste de formats de sortie
    supportés par le convertisseur. Les formats possibles sont :
    eval, dict ou exec.
    Le format eval est un texte source Python qui peut etre evalué. Le
    résultat de l'évaluation est un objet Python quelconque.
    Le format dict est un dictionnaire Python.
    Le format exec est un texte source Python qui peut etre executé. 

    La méthode readfile a pour fonction de lire un fichier dont le
    nom est passé en argument de la fonction.
       - convertisseur.readfile(nom_fichier)

    La méthode convert a pour fonction de convertir le fichier
    préalablement lu dans un objet du format passé en argument.
       - objet=convertisseur.convert(outformat)

    Ce convertisseur supporte le format de sortie dict

"""
import sys,string,traceback

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
          'name' : 'pyth',
        # La factory pour créer une instance du plugin
          'factory' : PythParser,
          }


class PythParser:
   """
       Ce convertisseur lit un fichier au format pyth avec la 
       methode readfile : convertisseur.readfile(nom_fichier)
       et retourne le texte au format outformat avec la 
       methode convertisseur.convert(outformat)

       Ses caractéristiques principales sont exposées dans 2 attributs 
       de classe :
         - extensions : qui donne une liste d'extensions de fichier préconisées
         - formats : qui donne une liste de formats de sortie supportés
   """
   # Les extensions de fichier préconisées
   extensions=('.pyth',)
   # Les formats de sortie supportés (eval dict ou exec)
   formats=('dict',)

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR convertisseur format pyth',
                         fin='fin CR format pyth')
      self.g={}

   def readfile(self,filename):
      self.filename=filename
      try:
         self.text=open(filename).read()
      except:
         self.cr.fatal(tr("Impossible d'ouvrir le fichier : %s",str( filename)))
         return
      self.g={}
      try:
         exec self.text in self.g
      except EficasException as e:
         l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
         s= string.join(l[2:])
         s= string.replace(s,'"<string>"','"<%s>"'%self.filename)
         self.cr.fatal(tr("Erreur a l'evaluation :\n %s", s))

   def convert(self,outformat,appli=None):
      if outformat == 'dict':
         return self.getdict()
      else:
         raise EficasException(tr("Format de sortie : %s, non supporte", outformat))

   def getdict(self):
      d={}
      for k,v in self.g.items():
         if k[0] != '_':d[k]=v
      return d
