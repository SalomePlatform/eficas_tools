"""
   V�rification des cycles de r�f�rence d'objets sur 
   un exemple avec des op�rateurs
"""

import sys
sys.path[:0]=['../..','../../..']

from Accas import SIMP,FACT,OPER

# Construction objet de d�finition

class concept:
   def __init__(self,etape):
      self.etape=etape
   def is_object(sd):
      """ Retourne 1 si sd est du bon type par rapport � la classe """
      return 0
   def supprime(self):
      self.etape=None

OP1 = OPER(nom='OP1',op=1,sd_prod=concept,reentrant='f',
           a=SIMP(typ='I'),
           c=SIMP(typ='I',position='global'),
           b=SIMP(typ=concept),
          )

# V�rification objet de d�finition
cr=OP1.report()
if cr.estvide():
   print "L'objet de d�finition est valide "
else:
   print cr

class context:
   def __init__(self):
      self.etapes=[]
      self.mc_globaux={}
      self.cata_ordonne_dico=None
      self.par_lot="OUI"

   def register(self,etape):
      self.etapes.append(etape)
      return self.etapes.index(etape)
   def get_jdc_root(self):
      return self
   def create_sdprod(self,etape,nomsd):
      sd= etape.get_sd_prod()
      if sd != None and etape.reuse == None:
         # ATTENTION : On ne nomme la SD que dans le cas de non reutilisation d un concept
         sd.nom=nomsd
      return sd


cont=context()
CONTEXT.set_current_step(cont)

sd=concept(None)
# Cr�ation de l'objet ETAPE
co1=OP1(a=1,b=sd)

# V�rification objet ETAPE
e1=cont.etapes[0]
cr= e1.report()
if cr.estvide():
   print "L'objet ETAPE  est valide " 
else:
   print "L'objet ETAPE  n'est pas valide " 
   print cr

# Test avec reutilisation de concept
co=OP1(reuse=co1,a=1,b=sd)
e2=cont.etapes[1]
cr= e2.report()
if cr.estvide():
   print "L'objet ETAPE  est valide "
else:
   print "L'objet ETAPE  n'est pas valide "
   print cr

e1.supprime()
e2.supprime()

def testcycle():
   """
       Cette fonction permet de d�tecter les cycles de r�f�rences entre objets
       � l'aide du module Cyclops
   """
   from Misc import Cyclops
   global e1,e2
   z=Cyclops.CycleFinder()
   z.register(e1)
   z.register(e2)
   del e1,e2
   z.find_cycles()
   z.show_stats()
   z.show_cycles()
   z.show_cycleobjs()
   z.show_sccs()
   z.show_arcs()
   print "dead root set objects:"
   for rc, cyclic, x in z.get_rootset():
      if rc == 0:
         z.show_obj(x)
   z.find_cycles(1)
   z.show_stats()

testcycle()

