# -*- coding: utf-8 -*-
"""
   Cet exemple montre :
   - la création d'une définition de mot-clé facteur comportant un mot-clé simple
   - sa vérification (report)
   - la création d'un mot-clé facteur valide
   - sa vérification (report)
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
