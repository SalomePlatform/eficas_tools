# -*- coding: utf-8 -*-
"""
   Cet exemple construit un objet de d�finition (cata) de type FACT
   qui est compos� de 3 objets de d�finition de type FACT et
   d'une r�gle AU_MOINS_UN.

   Dans un premier temps on v�rifie la conformite de l'objet 
   de d�finition ::

      cr=cata.report()
      if cr.estvide(): ...

   Dans un deuxi�me temps, on construit deux objets de type 
   MCFACT dont la d�finition est cata et on v�rifie la conformit�
   de ces objets.
"""

import sys
sys.path[:0]=['../..','../../Aster']

from Accas import SIMP,FACT
from Accas import AU_MOINS_UN

# Construction objet de d�finition

cata= FACT(sect1=FACT(a=SIMP(typ='I'),b=SIMP(typ='I')),
           sect2=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
           sect3=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
           regles=AU_MOINS_UN('sect3')
          )

# V�rification objet de d�finition

cr=cata.report()
if cr.estvide():
   print "L'objet de d�finition est valide "
else:
   print cr

# Cr�ation de l'objet MCFACT de nom mcf1

d={'sect1':{'a':1},'sect2':{'c':3}}
o=cata(d,'mcf1',None)

# V�rification objet MCFACT

cr= o.report()
if cr.estvide():
   print "L'objet MCFACT bas� sur le dictionnaire %s est valide " % d
else:
   print "L'objet MCFACT bas� sur le dictionnaire %s n'est pas valide " % d
   print cr
assert o.isvalid() == 0

d={'sect1':{'a':1},'sect3':{'c':3}}
o=cata(d,'mcf1',None)
cr= o.report()
if cr.estvide():
   print "L'objet MCFACT bas� sur le dictionnaire %s est valide " % d
else:
   print "L'objet MCFACT bas� sur le dictionnaire %s n'est pas valide " % d
   print cr
assert o.isvalid() == 1
