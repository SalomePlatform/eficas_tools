"""
   Cet exemple construit un objet de définition (cata) de type BLOC
   contenant deux objets SIMP

   Dans un premier temps on vérifie la conformite de l'objet 
   de définition ::

      cr=cata.report()
      if cr.estvide(): ...

   Dans un deuxième temps, on construit des objets de type 
   MCBLOC dont la définition est cata et on vérifie la conformité
   de ces objets.
"""

import sys
sys.path[:0]=['../..']

from Accas import SIMP,FACT,BLOC

# Construction objet de définition

cata= BLOC(condition="a==1",
           c=SIMP(typ='I'),
           d=SIMP(typ='I'),
          )

# Vérification objet de définition
cr=cata.report()
if cr.estvide():
   print "L'objet de définition est valide "
else:
   print cr


for d in ({'a':1},
          {'a':1,'c':3},
          {'a':2,'c':3},
         ):
   # Création de l'objet MCBLOC de nom mcf1
   o=cata(d,'mcf1',None)
   print "Mots-clés restants : ",o.reste_val
   # Vérification objet MCBLOC
   cr= o.report()
   if cr.estvide():
      print "L'objet MCBLOC basé sur le dictionnaire %s est valide " % d
   else:
      print "L'objet MCBLOC basé sur le dictionnaire %s n'est pas valide " % d
      print cr

