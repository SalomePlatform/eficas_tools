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
   Ce module sert a retrouver l'ordre des mots cles d'un catalogue de
   commandes
"""
if __name__ == "__main__" :
   import sys
   sys.path[:0]=[".."]
   sys.path[:0]=["../Aster"]
   sys.path[:0]=["../Saturne"]

from Accas import NUPL

def traite_entiteNUPL(entite):
   """
       Fonction speciale pour les nuplets (classe NUPL)
       Cette fonction ajoute a l'objet entite un attribut de nom ordre_mc
       qui est une liste vide.
   """
   entite.ordre_mc=[]

def traite_entite(entite):
   """
       Cette fonction ajoute a l'objet entite un attribut de nom ordre_mc
       qui est une liste contenant le nom des sous entites dans l'ordre 
       de leur apparition dans le catalogue.
       L'ordre d'apparition dans le catalogue est donné par l'attribut _no
       de l'entite
       La fonction active le meme type de traitement pour les sous entites
       de entite
   """
   l=[]
   for k,v in entite.entites.items():
      if isinstance(v,NUPL):
         traite_entiteNUPL(v)
      else:
         traite_entite(v)
      l.append((v._no,k))
   l.sort()
   entite.ordre_mc=[ item for index, item in l ]

def analyse_niveau(cata_ordonne_dico,niveau):
   """
       Analyse un niveau dans un catalogue de commandes
   """
   if niveau.l_niveaux == ():
       # Il n'y a pas de sous niveaux
       for oper in niveau.entites:
           traite_entite(oper)
           cata_ordonne_dico[oper.nom]=oper
   else:
       for niv in niveau.l_niveaux:
           analyse_niveau(cata_ordonne_dico,niv)
  
def analyse_catalogue(cata):
   """
      Cette fonction analyse le catalogue cata pour construire avec l'aide
      de traite_entite la structure de données ordre_mc qui donne l'ordre
      d'apparition des mots clés dans le catalogue
      Elle retourne un dictionnaire qui contient toutes les commandes
      du catalogue indexées par leur nom
   """
   cata_ordonne_dico={}
   if cata.JdC.l_niveaux == ():
       # Il n'y a pas de niveaux
       for oper in cata.JdC.commandes:
           traite_entite(oper)
           cata_ordonne_dico[oper.nom]=oper
   else:
       for niv in cata.JdC.l_niveaux:
           analyse_niveau(cata_ordonne_dico,niv)
   return cata_ordonne_dico


if __name__ == "__main__" :
   from Cata import cata_STA6
   dico=analyse_catalogue(cata_STA6)
   #import cata_saturne
   #dico=analyse_catalogue(cata_saturne)

   def print_entite(entite,dec='  '):
       print dec,entite.nom,entite.__class__.__name__
       for mocle in entite.ordre_mc:
          print_entite(entite.entites[mocle],dec=dec+'  ')

   for k,v in dico.items():
      print_entite(v,dec='')

   print dico.keys()
