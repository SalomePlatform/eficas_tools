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
    au format asterv5 pour EFICAS.

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

    Ce convertisseur supporte uniquement le format de sortie exec

"""
import sys,string,traceback

from Noyau import N_CR

def entryPoint():
   """
       Retourne les informations nécessaires pour le chargeur de plugins
       Ces informations sont retournées dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'asterv5',
        # La factory pour créer une instance du plugin
          'factory' : AsterParser,
          }

import Parserv5.conv
import parseur_python

class AsterParser:
   """
   """
   # Les extensions de fichier préconisées
   extensions=('.comm',)
   # Les formats de sortie supportés (eval dict ou exec)
   formats=('exec','execnoparseur')

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR convertisseur format asterv5',
                         fin='fin CR format asterv5')
      self.oldtext=''
      self.out=self.err=self.warn=''

   def readfile(self,filename):
      self.filename=filename
      try:
         self.text=open(filename).read()
      except:
         self.cr.fatal("Impossible ouvrir fichier %s" % filename)
         return

   def convert(self,outformat,appli=None):
      if outformat == 'exec':
         return self.getexec()
      elif outformat == 'execnoparseur':
         return self.getexecnoparseur()
      else:
         raise "Format de sortie : %s, non supporté"

   def getexec(self):
      if self.text != self.oldtext:
         self.out, self.err, self.warn= Parserv5.conv.conver(self.text)
         if self.err:
            self.cr.fatal("Erreur a l'interpretation de %s" % self.filename)
            self.cr.fatal(str(self.err))
            return self.out
         # On transforme les commentaires et les parametres en objets Python
         # avec un deuxième parseur
         try:
            self.out = parseur_python.PARSEUR_PYTHON(self.out).get_texte()
         except:
            self.cr.fatal("Erreur dans la deuxième phase d interpretation de %s" % self.filename)
            tracebak.print_exc()
            return ""
         self.oldtext=self.text
      return self.out

   def getexecnoparseur(self):
      if self.text != self.oldtext:
         self.out, self.err, self.warn= Parserv5.conv.conver(self.text)
         if self.err:
            self.cr.fatal("Erreur a l'interpretation de %s" % self.filename)
            self.cr.fatal(str(self.err))
            return self.out
         self.oldtext=self.text
      return self.out

