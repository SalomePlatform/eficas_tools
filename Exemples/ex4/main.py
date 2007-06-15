# -*- coding: utf-8 -*-
import sys
sys.path[:0]=['../..','../../Aster']

from Accas import SIMP,FACT

cata= FACT(sect1=FACT(a=SIMP(typ='I'),b=SIMP(typ='I')),
           sect2=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
          )

cr=cata.report()
if cr.estvide():
   print "Verification sans erreur"
else:
   print cr

# On r�cup�re les plugins de la famille convert
import convert

p=convert.plugins['ini']()
p.readfile('toto.ini')
s=p.convert('eval')
if not p.cr.estvide():
   print p.cr
   sys.exit(0)

o=cata(eval(s),'mcf1',None)
print o
print o.report()
assert o.isvalid() == 1

o=cata(p.convert('dict'),'mcf2',None)
print o
print o.report()
assert o.isvalid() == 1

p=convert.plugins['pyth']()
p.readfile('toto.pyth')
d=p.convert('dict')
if not p.cr.estvide():
   print p.cr
   sys.exit(0)

o=cata(d,'mcf3',None)
print o
print o.report()
assert o.isvalid() == 0
