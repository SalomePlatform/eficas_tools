# -*- coding: utf-8 -*-
"""
   Cet exemple montre :
    - la cr�ation d'une d�finition de mot-cl� simple
    - sa v�rification (report)
    - la cr�ation d'un mot-cl� simple valide 
    - sa v�rification (isvalid)
    - la cr�ation d'une autre d�finition de mot-cl� simple
    - sa v�rification (report)
    - la cr�ation d'un mot-cl� simple invalide 
    - sa v�rification (report)

"""
import sys
sys.path[:0]=['../..','../../Aster']

import Accas
from Accas import SIMP

a=SIMP(typ='I')
print a.report()
o=a(1,'mcs1')
assert o.isvalid() == 1

a=SIMP(typ='I',statut='o')
cr=a.report()
if cr.estvide():
   print "Verification sans erreur"
else:
   print cr
o=a(None,'mcs1')
print o.report()
assert o.isvalid() == 0
