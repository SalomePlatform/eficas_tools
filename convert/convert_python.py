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
    au format python pour EFICAS.

    Un plugin convertisseur doit fournir deux attributs de classe :
    extensions et formats et deux m�thodes : readfile,convert.

    L'attribut de classe extensions est une liste d'extensions
    de fichiers pr�conis�es pour ce type de format. Cette information
    est seulement indicative.

    L'attribut de classe formats est une liste de formats de sortie
    support�s par le convertisseur. Les formats possibles sont :
    eval, dict ou exec.
    Le format eval est un texte source Python qui peut etre evalu�. Le
    r�sultat de l'�valuation est un objet Python quelconque.
    Le format dict est un dictionnaire Python.
    Le format exec est un texte source Python qui peut etre execut�. 

    La m�thode readfile a pour fonction de lire un fichier dont le
    nom est pass� en argument de la fonction.
       - convertisseur.readfile(nom_fichier)

    La m�thode convert a pour fonction de convertir le fichier
    pr�alablement lu dans un objet du format pass� en argument.
       - objet=convertisseur.convert(outformat)

    Ce convertisseur supporte le format de sortie exec

"""
import sys,string,traceback

import parseur_python
from Noyau import N_CR

def entryPoint():
   """
       Retourne les informations n�cessaires pour le chargeur de plugins
       Ces informations sont retourn�es dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'python',
        # La factory pour cr�er une instance du plugin
          'factory' : PythonParser,
          }


class PythonParser:
   """
       Ce convertisseur lit un fichier au format python avec la 
       methode readfile : convertisseur.readfile(nom_fichier)
       et retourne le texte au format outformat avec la 
       methode convertisseur.convert(outformat)

       Ses caract�ristiques principales sont expos�es dans 2 attributs 
       de classe :
          - extensions : qui donne une liste d'extensions de fichier pr�conis�es
          - formats : qui donne une liste de formats de sortie support�s
   """
   # Les extensions de fichier pr�conis�es
   extensions=('.py',)
   # Les formats de sortie support�s (eval dict ou exec)
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
         self.cr.fatal("Impossible ouvrir fichier %s" % filename)
         return

   def convert(self,outformat):
      if outformat == 'exec':
         try:
            return parseur_python.PARSEUR_PYTHON(self.text).get_texte()
         except:
            # Erreur lors de la conversion
            l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],
                                         sys.exc_info()[2])
            self.cr.exception("Impossible de convertir le fichier python \
                               qui doit contenir des erreurs.\n \
                               On retourne le fichier non converti \n \
                               Pr�venir la maintenance. \n" + string.join(l))
            # On retourne n�anmoins le source initial non converti (au cas o�)
            return self.text
      elif outformat == 'execnoparseur':
         return self.text
      else:
         raise "Format de sortie : %s, non support�"
         return None

