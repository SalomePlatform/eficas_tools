"""
   Cet exemple montre :
    - la création d'une définition de mot-clé simple
    - sa vérification (report)
    - la création d'un mot-clé simple valide 
    - sa vérification (isvalid)
    - la création d'une autre définition de mot-clé simple
    - sa vérification (report)
    - la création d'un mot-clé simple invalide 
    - sa vérification (report)

"""
import sys
sys.path[:0]=['../..']

import Accas
from Accas import SIMP

a=SIMP(typ='I')
print a.report()
o=a(1,'mcs1')
print o
print o.isvalid()

a=SIMP(typ='I',statut='o')
cr=a.report()
if cr.estvide():
   print "Verification sans erreur"
else:
   print cr
o=a(None,'mcs1')
print o.report()
