# -*- coding: utf-8 -*-
"""
   Cet exemple montre :
   - la cr�ation d'une d�finition de mot-cl� facteur comportant un mot-cl� simple
   - sa v�rification (report)
   - la cr�ation d'un mot-cl� facteur valide
   - sa v�rification (report)
"""
import sys
sys.path[:0]=['../..']

import Accas
from Accas import SIMP,FACT

a=FACT(b=SIMP(typ='I'))

cr=a.report()
if cr.estvide():
   print "Verification sans erreur"
else:
   print cr

o=a({'b':1},'mcf1',None)
print o
print o.report()
