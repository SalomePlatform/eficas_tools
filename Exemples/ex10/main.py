"""
   Exemple d'utilisation avec des mots-cl�s facteurs multiples.
   Cet exemple construit un objet de d�finition (cata) de type FACT
   qui est compos� de deux objets FACT

   Dans un premier temps on v�rifie la conformite de l'objet 
   de d�finition ::

      cr=cata.report()
      if cr.estvide(): ...

   Dans un deuxi�me temps, on construit plusieurs objets de type 
   MCFACT dont la d�finition est cata et on v�rifie la conformit�
   de ces objets.
"""

import sys
sys.path[:0]=['../..']

from Accas import SIMP,FACT

# Construction objet de d�finition

cata= FACT(mcf1=FACT(a=SIMP(typ='I'),b=SIMP(typ='I')),
           mcf2=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
          )

# V�rification objet de d�finition
cr=cata.report()
if cr.estvide():
   print "L'objet de d�finition est valide "
else:
   print cr


for d in ({'mcf1':{'a':1}},
          {'mcf1':{'a':1,'b':2}},
          {'mcf1':{'a':1,'b':2},'mcf2':{'c':3}},
          {'mcf1':{'a':1,'b':2},'mcf2':({'c':3},{'c':5})},
         ):
   # Cr�ation de l'objet MCFACT de nom mcf1
   o=cata(d,'mcf1',None)
   # V�rification objet MCFACT
   cr= o.report()
   if cr.estvide():
      print "L'objet MCFACT bas� sur le dictionnaire %s est valide " % d
   else:
      print "L'objet MCFACT bas� sur le dictionnaire %s n'est pas valide " % d
      print cr

