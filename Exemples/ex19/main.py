# -*- coding: utf-8 -*-
"""
   Exemple d'utilisation d'un générateur au format asterv5

   Dans un premier temps on importe un catalogue
   de définition contenu dans un module et on le valide ::

      import cata
      from cata import JdC
      cr=JdC.report()
      if cr.estvide(): ...

   Dans un deuxième temps, on construit un jeu de commandes
   a partir d'une chaine de caractères et on vérifie sa
   conformité.
"""

import sys
sys.path[:0]=['../..','../../Aster/Cata','../../Aster']

from cataSTA6 import cata

cr=cata.JdC.report()
print cr

f=open('ahlv100a.comm','r')
text=f.read()
f.close()

j=cata.JdC(procedure=text,cata=cata,nom="ahlv100a")

j.compile()
if not j.cr.estvide():
   print j.cr
   sys.exit()

j.exec_compile()
if not j.cr.estvide():
   print j.cr
   sys.exit()

cr=j.report()
if not cr.estvide():
   print cr
   sys.exit()

# On récupère les plugins de la famille generator
import generator

g=generator.plugins['asterv5']()
print g.gener(j,format='beautifie')
g.writefile('titi.comm')

