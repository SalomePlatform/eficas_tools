"""
   Exemple d'utilisation d'un JDC

   Dans un premier temps on v�rifie la conformite de l'objet 
   de d�finition ::

      cr=OP1.report()
      if cr.estvide(): ...

   Dans un deuxi�me temps, on construit plusieurs objets de type 
   ETAPE dont la d�finition est OP1 et on v�rifie la conformit�
   de ces objets.
"""

import sys
sys.path[:0]=['../..']

import cata
from cata import JdC

cr=JdC.report()
print cr

text="""

a=OP1(a=1)
b=OP1(a=1,b=a)
c=OP1(a=1,b=10)
"""

j=JdC(procedure=text,cata=cata,nom="bidon")

j.compile()
print j.cr

j.exec_compile()
print j.cr

cr=j.report()
print cr
