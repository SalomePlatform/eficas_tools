# -*- coding: utf-8 -*-
"""
   Cet exemple construit un objet regle (cata) 
   de type AU_MOINS_UN

   Ensuite on vérifie le fonctionnement de la règle sur un dictionnaire non conforme
   à la règle et un dictionnaire conforme à la règle.
"""

import sys
sys.path[:0]=['../..','../../Aster']

from Accas import AU_MOINS_UN

# Construction objet de définition

cata=           AU_MOINS_UN('sect3')


# Vérification dictionnaire d

d={'sect1':{'a':1},'sect2':{'c':3}}

text,valid= cata.verif(d)

if valid:
   print "Le dictionnaire %s est conforme à la règle" % d
else:
   print "Le dictionnaire %s n'est pas conforme à la règle" % d
assert valid==0

d={'sect3':{'a':1},'sect2':{'c':3}}
text,valid= cata.verif(d)
if valid:
   print "Le dictionnaire %s est conforme à la règle" % d
else:
   print "Le dictionnaire %s n'est pas conforme à la règle" % d
assert valid==1
