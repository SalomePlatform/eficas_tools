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

    Ce convertisseur supporte le format de sortie exec

"""
import sys,string,traceback

import parseur_python
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
          'name' : 'homard',
        # La factory pour créer une instance du plugin
          'factory' : PythonParser,
          }


class PythonParser:
   """
       Ce convertisseur lit un fichier au format python avec la 
       methode readfile : convertisseur.readfile(nom_fichier)
       et retourne le texte au format outformat avec la 
       methode convertisseur.convert(outformat)

       Ses caractéristiques principales sont exposées dans 2 attributs 
       de classe :
          - extensions : qui donne une liste d'extensions de fichier préconisées
          - formats : qui donne une liste de formats de sortie supportés
   """
   # Les extensions de fichier préconisées
   extensions=('.py',)
   # Les formats de sortie supportés (eval dict ou exec)
   # Le format exec est du python executable (commande exec) converti avec PARSEUR_PYTHON
   # Le format execnoparseur est du python executable (commande exec) non converti
   formats=('exec','execnoparseur')

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le 
      # compte-rendu standard
      self.text=''
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR convertisseur format python',
                         fin='fin CR format python')

   def readfile(self,filename):
      self.filename=filename
      try:
         self.text=open(filename).read()
      except:
         self.cr.fatal(tr("Impossible d'ouvrir le fichier %s", filename))
         return

   def convert(self,outformat,appli=None):
      if outformat == 'exec':
         try:
            return parseur_python.PARSEUR_PYTHON(self.text).get_texte()
         except:
            # Erreur lors de la conversion
            l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],
                                         sys.exc_info()[2])
            self.cr.exception(tr("Impossible de convertir le fichier Python \
                                        qui doit contenir des erreurs.\n \
                                        On retourne le fichier non converti \n \
                                        Prévenir la maintenance. \n %s", string.join(l)))
            # On retourne néanmoins le source initial non converti (au cas où)
            return self.text
      elif outformat == 'execnoparseur':
         return self.text
      else:
         raise EficasException(tr("Format de sortie : %s, non supporté", unicode(outformat)))
         return None
