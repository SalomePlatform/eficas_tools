"""
"""

import sys
sys.path[:0]=['../..','../../Minicode']

import cata_saturne

import convert
c=convert.plugins['python']()
c.readfile('kk.py')
text=c.convert('exec')
print text

j=cata_saturne.JdC(procedure=text,cata=cata_saturne,nom="essai_saturne")

j.analyse()
if not j.cr.estvide():
   print j.cr
   sys.exit()

cr=j.report()
if not cr.estvide():
   print cr
   sys.exit()

# On récupère les plugins de la famille generator
import generator

g=generator.plugins['python']()
print g.gener(j,format='beautifie')
g.writefile('titi.comm')

