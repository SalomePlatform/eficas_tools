# -*- coding: utf-8 -*-
"""
   Cet exemple construit un objet de définition (cata) de type FACT
   qui est composé d'un objet SIMP et d'un bloc conditionnel
   contenant deux objets SIMP

   Dans un premier temps on vérifie la conformite de l'objet 
   de définition ::

      cr=cata.report()
      if cr.estvide(): ...

   Dans un deuxième temps, on construit plusieurs objets de type 
   MCFACT dont la définition est cata et on vérifie la conformité
   de ces objets.
"""

import sys
sys.path[:0]=['../..']

from Accas import SIMP,FACT,BLOC

# Construction objet de définition

cata= FACT(a    =SIMP(typ='I'),
           bloc1=BLOC(condition="a==1",
                       c=SIMP(typ='I'),
                       d=SIMP(typ='I')
                     ),
          )

# Vérification objet de définition
cr=cata.report()
if cr.estvide():
   print "L'objet de définition est valide "
else:
   print cr


for d in ({'a':1},
          {'a':1,'c':3},
          {'a':2,'c':3},
         ):
   # Création de l'objet MCFACT de nom mcf1
   o=cata(d,'mcf1',None)
   # Vérification objet MCFACT
   cr= o.report()
   if cr.estvide():
      print "L'objet MCFACT basé sur le dictionnaire %s est valide " % d
   else:
      print "L'objet MCFACT basé sur le dictionnaire %s n'est pas valide " % d
      print cr

