"""
   Exemple d'utilisation d'un JDC

   Dans un premier temps on importe un catalogue
   de d�finition contenu dans un module et on le valide ::

      import cata
      from cata import JdC
      cr=JdC.report()
      if cr.estvide(): ...

   Dans un deuxi�me temps, on construit un jeu de commandes
   a partir d'une chaine de caract�res et on v�rifie sa
   conformit�.
"""

import sys
sys.path[:0]=['../..']

import cata
from cata import JdC

cr=JdC.report()
print cr

text="""
DEBUT()
a=OP1(a=1)
b=OP2(a=1,
           b=a)
c=OP1(a=1,
         b=10)
d=MA_MACRO(A=1)
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
if not j.cr.estvide():
   print j.cr
   sys.exit()

