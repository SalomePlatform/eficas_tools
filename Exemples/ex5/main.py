import sys
sys.path[:0]=['../..','../../..']

from Accas import SIMP,FACT

cata= FACT(sect1=FACT(a=SIMP(typ='I'),b=SIMP(typ='I')),
           sect2=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
          )

cr=cata.report()
if cr.estvide():
   print "Verification sans erreur"
else:
   print cr

# On récupère les plugins de la famille convert
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

o=cata(p.convert('dict'),'mcf2',None)
print o
print o.report()

# On récupère les plugins de la famille generator
import generator

g=generator.plugins['ini']()
g.gener(o)
g.writefile('titi.ini')

g=generator.plugins['pyth']()
g.gener(o)
g.writefile('titi.pyth')

p=convert.plugins['pyth']()
p.readfile('toto.pyth')
d=p.convert('dict')
if not p.cr.estvide():
   print p.cr
   sys.exit(0)

o=cata(d,'mcf3',None)
print o
print o.report()
