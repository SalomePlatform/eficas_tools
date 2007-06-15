# -*- coding: utf-8 -*-
"""
   Cet exemple construit un objet de définition (cata) de type FACT
   qui est composé de 3 objets de définition de type FACT et
   d'une règle AU_MOINS_UN.

   Dans un premier temps on vérifie la conformite de l'objet 
   de définition ::

      cr=cata.report()
      if cr.estvide(): ...

   Dans un deuxième temps, on construit deux objets de type 
   MCFACT dont la définition est cata et on vérifie la conformité
   de ces objets.
"""

import sys
sys.path[:0]=['../..','../../Aster']

from Accas import SIMP,FACT
from Accas import AU_MOINS_UN

# Construction objet de définition

cata= FACT(sect1=FACT(a=SIMP(typ='I'),b=SIMP(typ='I')),
           sect2=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
           sect3=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
           regles=AU_MOINS_UN('sect3')
          )

# Vérification objet de définition

cr=cata.report()
if cr.estvide():
   print "L'objet de définition est valide "
else:
   print cr

# Création de l'objet MCFACT de nom mcf1

d={'sect1':{'a':1},'sect2':{'c':3}}
o=cata(d,'mcf1',None)

# Vérification objet MCFACT

cr= o.report()
if cr.estvide():
   print "L'objet MCFACT basé sur le dictionnaire %s est valide " % d
else:
   print "L'objet MCFACT basé sur le dictionnaire %s n'est pas valide " % d
   print cr
assert o.isvalid() == 0

d={'sect1':{'a':1},'sect3':{'c':3}}
o=cata(d,'mcf1',None)
cr= o.report()
if cr.estvide():
   print "L'objet MCFACT basé sur le dictionnaire %s est valide " % d
else:
   print "L'objet MCFACT basé sur le dictionnaire %s n'est pas valide " % d
   print cr
assert o.isvalid() == 1
