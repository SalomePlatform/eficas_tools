# -*- coding: utf-8 -*-
"""
   Cet exemple met en oeuvre le profiling de Python sur un cas
   avec plusieurs éléments de définition,
   une opération de vérification du dictionnaire d
   et l'appel à la méthode supprime de l'objet o 
"""

import sys
sys.path[:0]=['../..']

def main():
   from Accas import SIMP,FACT,BLOC
   from Accas import AU_MOINS_UN

   # Construction objet de définition

   cata= FACT(mcf1=FACT(a=SIMP(typ='I'),b=SIMP(typ='I')),
              mcf2=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
              a    =SIMP(typ='I'),
              bloc1=BLOC(condition="a==1",
                          c=SIMP(typ='I'),
                          d=SIMP(typ='I')
                        ),
              sect3=FACT(c=SIMP(typ='I'),d=SIMP(typ='I')),
              regles=AU_MOINS_UN('sect3'),
             )

   # Vérification objet de définition
   cr=cata.report()
   if cr.estvide():
      print "L'objet de définition est valide "
   else:
      print cr


   d= {'mcf1':{'a':1,'b':2},
       'mcf2':({'c':3},{'c':5}),
       'sect3':{'c':3,'d':5},
       'a':1,
       'c':2,
      }

   # Création de l'objet MCFACT de nom mcf1
   o=cata(d,'mcf1',None)
   # Vérification objet MCFACT
   cr= o.report()
   if cr.estvide():
      print "L'objet MCFACT basé sur le dictionnaire %s est valide " % d
   else:
      print "L'objet MCFACT basé sur le dictionnaire %s n'est pas valide " % d
      print cr

   o.supprime()

import profile
#profile.run("main()")
prof=profile.Profile()
try:
   prof.run("main()")
except SystemExit:
   pass

import pstats
# Impression de différentes statistiques
p=pstats.Stats(prof)

print "*********************************************"
print "*  Trié par temps interne (20 plus grands)  *"
print "*********************************************"
p.sort_stats('time').print_stats(20)

print "***********************************************"
print "*  Liste des appellés triée par temps interne *"
print "***********************************************"
p.print_callees()

print "************************************************************"
print "*  Liste des appellants de is_reel triée par temps interne *"
print "************************************************************"
p.print_callers('is_reel')

print "*********************************************"
print "*  Trié par temps cumulé (20 plus grands)   *"
print "*********************************************"
p.sort_stats('cumulative').print_stats(20)

print "*********************************************"
print "*  Trié par noms de fonction                *"
print "*********************************************"
p.sort_stats('name').print_stats()

print "*********************************************"
print "*  Statistique standard                     *"
print "*********************************************"
prof.print_stats()

print "*************************************************"
print "*  Trié par fichier seulement methodes __init__ *"
print "*************************************************"
p.sort_stats('file').print_stats('__init__')





