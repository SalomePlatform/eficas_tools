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
    Ce module contient le plugin generateur de fichier au format pyth pour EFICAS.


"""
import traceback
import types,string

from Noyau import N_CR
from Accas import MCSIMP,MCFACT,MCList
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
          'factory' : PythGenerator,
          }


class PythGenerator:
   """
       Ce generateur parcourt un objet de type MCFACT et produit
       un fichier au format pyth

       L'acquisition et le parcours sont réalisés par la méthode
       generator.gener(objet_mcfact)

       L'écriture du fichier au format ini par appel de la méthode
       generator.writefile(nom_fichier)

       Ses caractéristiques principales sont exposées dans des attributs 
       de classe :
          - extensions : qui donne une liste d'extensions de fichier préconisées

   """
   # Les extensions de fichier préconisées
   extensions=('.py','.comm')

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR generateur format ini',
                         fin='fin CR format ini')
      # Le texte au format pyth est stocké dans l'attribut text
      self.text=''

   def writefile(self,filename):
      fp=open(filename,'w')
      fp.write(self.text)
      fp.close()

   def gener(self,obj,format='standard',config=None):
      """
         Tous les mots-clés simples du niveau haut sont transformés en variables 

         Tous les mots-clés facteurs sont convertis en dictionnaires

         Les mots-clés multiples ne sont pas traités
      """
      s=''
      if isinstance(obj,MCList):
        if len(obj.data) > 1:
          raise EficasException(tr("Pas supporte"))
        else:
          obj=obj.data[0]

      for mocle in obj.mc_liste:
        if isinstance(mocle,MCList):
          if len(mocle.data) > 1:
            raise EficasException(tr("Pas supporte"))
          else:
            valeur=self.generMCFACT(mocle.data[0])
            s=s+"%s = %s\n" % (mocle.nom,valeur)
        elif isinstance(mocle,MCFACT):
          valeur=self.generMCFACT(mocle)
          s=s+"%s = %s\n" % (mocle.nom,valeur)
        elif isinstance(v,MCSIMP):
          valeur = self.generMCSIMP(mocle)
          s=s+"%s = %s\n" % (mocle.nom,valeur)
        else:
          self.cr.fatal("Entite inconnue ou interdite : "+`mocle`)

      self.text=s
      return self.text

   def generMCFACT(self,obj):
      """
         Cette méthode convertit un mot-clé facteur 
         en une chaine de caractères représentative d'un dictionnaire
      """
      s = '{'
      for mocle in obj.mc_liste:
         if isinstance(mocle,MCSIMP):
            valeur = self.generMCSIMP(mocle)
            s=s+"'%s' : %s,\n" % (mocle.nom,valeur)
         elif isinstance(mocle,MCFACT):
            valeur=self.generMCFACT(mocle)
            s=s+"'%s' : %s,\n" % (mocle.nom,valeur)
         else:
            self.cr.fatal(tr("Entite inconnue ou interdite : %s. Elle est ignoree", `mocle`))

      s=s+'}'
      return s

   def generMCSIMP(self,obj):
      """
         Cette méthode convertit un mot-clé simple en une chaine de caractères
         au format pyth
      """
      try:
         s="%s" % obj.valeur
      except Exception as e :
         self.cr.fatal(tr("Type de valeur non supporté par le format pyth : n %(exception)s", \
                           {'nom': obj.nom, 'exception': unicode(e)}))


         s="ERREUR"
      return s

