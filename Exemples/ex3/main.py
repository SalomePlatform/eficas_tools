# -*- coding: utf-8 -*-
"""
    Cet exemple montre :
     - la cr�ation d'une d�finition de mot-cl� facteur
     - sa v�rification (report)
     - la cr�ation d'un mot-cl� facteur � partir d'un fichier .ini
     - sa v�rification (report)

"""
import sys
sys.path[:0]=['../..','../../Aster']

from Accas import SIMP,FACT
from parse import MyConfParser

p=MyConfParser()
p.read('toto.ini')


cata= FACT(sect1=FACT(a=SIMP(typ='I'),b=SIMP(typ='I')),
           sect2=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
          )

cr=cata.report()
if cr.estvide():
   print "Verification sans erreur"
else:
   print cr

o=cata(p.getdict(),'mcf1',None)
print o
print o.report()
assert o.isvalid() == 0
