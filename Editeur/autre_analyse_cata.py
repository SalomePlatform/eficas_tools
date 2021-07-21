# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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
   Ce module sert a retrouver l'ordre des mots cles d'un catalogue de
   commandes
"""
from __future__ import absolute_import
from __future__ import print_function
if __name__ == "__main__" :
   import sys
   sys.path[:0]=[".."]
   sys.path[:0]=["../Aster"]
   sys.path[:0]=["../Saturne"]

from Accas import NUPL

def traiteEntiteNUPL(entite):
   """
       Fonction speciale pour les nuplets (classe NUPL)
       Cette fonction ajoute a l'objet entite un attribut de nom ordre_mc
       qui est une liste vide.
   """
   entite.ordre_mc=[]

def traiteEntite(entite,liste_simp_reel):
   """
       Cette fonction ajoute a l'objet entite un attribut de nom ordre_mc
       qui est une liste contenant le nom des sous entites dans l'ordre 
       de leur apparition dans le catalogue.
       L'ordre d'apparition dans le catalogue est donne par l'attribut _no
       de l'entite
       La fonction active le meme type de traitement pour les sous entites
       de entite
   """
   l=[]
   for k,v in list(entite.entites.items()):
      if isinstance(v,NUPL):
         traiteEntiteNUPL(v)
      else:
         traiteReel(v,liste_simp_reel)
         traiteEntite(v,liste_simp_reel)
         traiteCache(v)
      l.append((v._no,k))
   l.sort()
   entite.ordre_mc=[ item for index, item in l ]

def traiteCache(objet):
    if not hasattr(objet, "cache"): return
    if objet.cache == 0 :return
    clef=objet.nom
    if objet.equiv != None : clef=objet.equiv
    if hasattr(objet.pere,"mcOblig"):
      objet.pere.mcOblig[clef]=objet.defaut
    else :
      objet.pere.mcOblig={}
      objet.pere.mcOblig[clef]=objet.defaut

def traiteReel(objet,liste_simp_reel):
    if objet.__class__.__name__ == "SIMP":
       if ( 'R' in objet.type):
          if objet.nom not in liste_simp_reel :
             liste_simp_reel.append(objet.nom)

def analyseNiveau(cata_ordonne_dico,niveau,liste_simp_reel):
   """
       Analyse un niveau dans un catalogue de commandes
   """
   if niveau.l_niveaux == ():
       # Il n'y a pas de sous niveaux
       for oper in niveau.entites:
           traiteEntite(oper,liste_simp_reel)
           cata_ordonne_dico[oper.nom]=oper
   else:
       for niv in niveau.l_niveaux:
           analyseNiveau(cata_ordonne_dico,niv)
  
def analyseCatalogue(cata):
   """
      Cette fonction analyse le catalogue cata pour construire avec l'aide
      de traiteEntite la structure de donnees ordre_mc qui donne l'ordre
      d'apparition des mots cles dans le catalogue
      Elle retourne un dictionnaire qui contient toutes les commandes
      du catalogue indexees par leur nom
   """
   cata_ordonne_dico={}
   liste_simp_reel=[]
   if cata.JdC.l_niveaux == ():
       # Il n'y a pas de niveaux
       for oper in cata.JdC.commandes:
           traiteEntite(oper,liste_simp_reel)
           cata_ordonne_dico[oper.nom]=oper
   else:
       for niv in cata.JdC.l_niveaux:
           analyseNiveau(cata_ordonne_dico,niv,liste_simp_reel)
   return cata_ordonne_dico,liste_simp_reel


if __name__ == "__main__" :
   from Cata import cata_STA6
   dico=analyseCatalogue(cata_STA6)
   #import cata_saturne
   #dico=analyseCatalogue(cata_saturne)

   def print_entite(entite,dec='  '):
       print (dec,entite.nom,entite.__class__.__name__)
       for mocle in entite.ordre_mc:
          print_entite(entite.entites[mocle],dec=dec+'  ')

   for k,v in list(dico.items()):
      print_entite(v,dec='')

   print (dico)
