# -*- coding: utf-8 -*-

"""
   Vérification des cycles de références d'objets sur un exemple
   d'utilisation d'un JDC

"""

import sys
sys.path[:0]=['../..','../../..']

import cata
from cata import JdC

cr=JdC.report()
print cr

text="""
DEBUT()
a=OP1(a=1)
b=OP1(a=1,b=a)
c=OP1(a=1)
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

JdC.supprime()
j.supprime()

def testcycle():
   """
       Cette fonction permet de détecter les cycles de références entre objets
       à l'aide du module Cyclops
   """
   from Misc import Cyclops
   global j
   z=Cyclops.CycleFinder()
   z.register(j)
   del j
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

