"""
   Exemple d'utilisation d'un JDC sur le cas test eficas
   de la base de test d'ASTER
   Ce test va jusqu'à la phase de construction des macros
   en utilisant le module codex qui emule une partie du fonctionnement 
   du code ASTER réel 

"""

import sys
sys.path[:0]=['../..']

import cata
from cata import JdC

cr=JdC.report()
print cr

f=open('cas.py','r')
text=f.read()
f.close()
j=JdC(procedure=text,cata=cata,nom="eficas")

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

j.Build()
