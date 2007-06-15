# -*- coding: utf-8 -*-
"""
   Exemple d'utilisation d'un JDC

   Dans un premier temps on importe un catalogue
   de définition contenu dans un module et on le valide ::

      import cata
      from cata import JdC
      cr=JdC.report()
      if cr.estvide(): ...

   Dans un deuxième temps, on construit un jeu de commandes
   a partir d'une chaine de caractères et on vérifie sa
   conformité.
"""

import sys
sys.path[:0]=['../..','../../Aster']

import cata
from cata import JdC

cr=JdC.report()
print cr

text="""
DEBUT()
a=OP1(a=1)
b=OP1(a=1,b=a)
c=OP1(a=1,b=10)
"""

j=JdC(procedure=text,cata=cata,nom="bidon")

j.compile()
if not j.cr.estvide():
   print j.cr
   sys.exit()

j.exec_compile()
if not j.cr.estvide():
   print j.cr
   sys.exit()

cr=j.report()
assert j.isvalid() == 0
if not j.cr.estvide():
   print j.cr
   sys.exit()
