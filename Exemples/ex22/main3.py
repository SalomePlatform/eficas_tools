# -*- coding: utf-8 -*-
"""
"""

import sys
sys.path[:0]=['../..','../../Aster/Cata','../../Aster']

from cataSTA5 import cata

import convert
c=convert.plugins['python']()
c.readfile('toto.comm')
text=c.convert('exec')

j=cata.JdC(procedure=text,cata=cata,nom="totalmod")
j.analyse()
if not j.cr.estvide():
   print j.cr
   sys.exit()

# On récupère les plugins de la famille generator
import generator

g=generator.plugins['python']()
textout= g.gener(j,format='beautifie')
g.writefile('tyty.comm')

