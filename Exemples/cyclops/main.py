# -*- coding: utf-8 -*-
"""
   Vérification des cycles de références d'objets dans Accas

   Cet exemple met en oeuvre plusieurs éléments de définition et
   après l'opération de vérification du dictionnaire d
   et l'appel à la méthode supprime de l'objet o 
   exécute l'utilitaire Cyclops pour vérifier qu'il ne reste plus
   de cycles de références.
"""

import sys
sys.path[:0]=['../..','../../..']

from Accas import SIMP,FACT,BLOC
from Accas import AU_MOINS_UN

# Construction objet de définition

cata= FACT(mcf1=FACT(a=SIMP(typ='I'),b=SIMP(typ='I')),
           mcf2=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
           a    =SIMP(typ='I'),
           bloc1=BLOC(condition="a==1",
                       c=SIMP(typ='I'),
                       d=SIMP(typ='I')
                     ),
           sect3=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
           regles=AU_MOINS_UN('sect3'),
          )

# Vérification objet de définition
cr=cata.report()
if cr.estvide():
   print "L'objet de définition est valide "
else:
   print cr


d= {'mcf1':{'a':1,'b':2},
    'mcf2':({'c':3},{'c':5}),
    'sect3':{'c':3,'d':5},
    'a':1,
    'c':2,
   }

# Création de l'objet MCFACT de nom mcf1
o=cata(d,'mcf1',None)
# Vérification objet MCFACT
cr= o.report()
if cr.estvide():
   print "L'objet MCFACT basé sur le dictionnaire %s est valide " % d
else:
   print "L'objet MCFACT basé sur le dictionnaire %s n'est pas valide " % d
   print cr

o.supprime()

def testcycle():
   """
       Cette fonction permet de détecter les cycles de références entre objets
       à l'aide du module Cyclops
   """
   from Misc import Cyclops
   global o,cr,cata
   z=Cyclops.CycleFinder()
   z.register(o)
   z.register(cata)
   del o,cr,cata
   z.find_cycles()
   z.show_stats()
   z.show_cycles()
   z.show_cycleobjs()
   z.show_sccs()
   z.show_arcs()
   print "dead root set objects:"
   for rc, cyclic, x in z.get_rootset():
      if rc == 0:
         z.show_obj(x)
   z.find_cycles(1)
   z.show_stats()

testcycle()

