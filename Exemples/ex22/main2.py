# -*- coding: utf-8 -*-
"""
"""

import sys
sys.path[:0]=['../..']

from Cata import cata_STA5
cata=cata_STA5

import convert
c=convert.plugins['asterv5']()
c.readfile('titi.comm')
text=c.convert('exec')

j=cata.JdC(procedure=text,cata=cata,nom="totalmod")
j.analyse()
if not j.cr.estvide():
   print j.cr
   sys.exit()

# On r�cup�re les plugins de la famille generator
import generator

g=generator.plugins['asterv5']()
textout= g.gener(j,format='beautifie')
g.writefile('tutu.comm')

