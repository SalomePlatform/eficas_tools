"""
   Cet exemple construit un objet de d�finition (cata) de type BLOC
   contenant deux objets SIMP

   Dans un premier temps on v�rifie la conformite de l'objet 
   de d�finition ::

      cr=cata.report()
      if cr.estvide(): ...

   Dans un deuxi�me temps, on construit des objets de type 
   MCBLOC dont la d�finition est cata et on v�rifie la conformit�
   de ces objets.
"""

import sys
sys.path[:0]=['../..']

from Accas import SIMP,FACT,BLOC

# Construction objet de d�finition

cata= BLOC(condition="a==1",
           c=SIMP(typ='I'),
           d=SIMP(typ='I'),
          )

# V�rification objet de d�finition
cr=cata.report()
if cr.estvide():
   print "L'objet de d�finition est valide "
else:
   print cr


for d in ({'a':1},
          {'a':1,'c':3},
          {'a':2,'c':3},
         ):
   # Cr�ation de l'objet MCBLOC de nom mcf1
   o=cata(d,'mcf1',None)
   print "Mots-cl�s restants : ",o.reste_val
   # V�rification objet MCBLOC
   cr= o.report()
   if cr.estvide():
      print "L'objet MCBLOC bas� sur le dictionnaire %s est valide " % d
   else:
      print "L'objet MCBLOC bas� sur le dictionnaire %s n'est pas valide " % d
      print cr

