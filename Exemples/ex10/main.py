"""
   Exemple d'utilisation avec des mots-clés facteurs multiples.
   Cet exemple construit un objet de définition (cata) de type FACT
   qui est composé de deux objets FACT

   Dans un premier temps on vérifie la conformite de l'objet 
   de définition ::

      cr=cata.report()
      if cr.estvide(): ...

   Dans un deuxième temps, on construit plusieurs objets de type 
   MCFACT dont la définition est cata et on vérifie la conformité
   de ces objets.
"""

import sys
sys.path[:0]=['../..']

from Accas import SIMP,FACT

# Construction objet de définition

cata= FACT(mcf1=FACT(a=SIMP(typ='I'),b=SIMP(typ='I')),
           mcf2=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
          )

# Vérification objet de définition
cr=cata.report()
if cr.estvide():
   print "L'objet de définition est valide "
else:
   print cr


for d in ({'mcf1':{'a':1}},
          {'mcf1':{'a':1,'b':2}},
          {'mcf1':{'a':1,'b':2},'mcf2':{'c':3}},
          {'mcf1':{'a':1,'b':2},'mcf2':({'c':3},{'c':5})},
         ):
   # Création de l'objet MCFACT de nom mcf1
   o=cata(d,'mcf1',None)
   # Vérification objet MCFACT
   cr= o.report()
   if cr.estvide():
      print "L'objet MCFACT basé sur le dictionnaire %s est valide " % d
   else:
      print "L'objet MCFACT basé sur le dictionnaire %s n'est pas valide " % d
      print cr

