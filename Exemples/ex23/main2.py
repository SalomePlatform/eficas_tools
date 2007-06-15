# -*- coding: utf-8 -*-
"""
"""

import sys
sys.path[:0]=['../..','../../Aster/Cata','../../Aster']

from cataSTA6 import cata

f=open('titi.comm','r')
text=f.read()
f.close()

j=cata.JdC(procedure=text,cata=cata,nom="ahlv100a")
j.analyse()
if not j.cr.estvide():
   print j.cr
   sys.exit()

# On récupère les plugins de la famille generator
import generator

g=generator.plugins['python']()
print g.gener(j,format='beautifie')
g.writefile('toto.comm')

