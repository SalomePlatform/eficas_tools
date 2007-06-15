# -*- coding: utf-8 -*-
"""
   Cet exemple construit un objet regle (cata) 
   de type AU_MOINS_UN

   Ensuite on v�rifie le fonctionnement de la r�gle sur un dictionnaire non conforme
   � la r�gle et un dictionnaire conforme � la r�gle.
"""

import sys
sys.path[:0]=['../..','../../Aster']

from Accas import AU_MOINS_UN

# Construction objet de d�finition

cata=           AU_MOINS_UN('sect3')


# V�rification dictionnaire d

d={'sect1':{'a':1},'sect2':{'c':3}}

text,valid= cata.verif(d)

if valid:
   print "Le dictionnaire %s est conforme � la r�gle" % d
else:
   print "Le dictionnaire %s n'est pas conforme � la r�gle" % d
assert valid==0

d={'sect3':{'a':1},'sect2':{'c':3}}
text,valid= cata.verif(d)
if valid:
   print "Le dictionnaire %s est conforme � la r�gle" % d
else:
   print "Le dictionnaire %s n'est pas conforme � la r�gle" % d
assert valid==1
