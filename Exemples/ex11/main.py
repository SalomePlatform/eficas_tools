"""
   Exemple d'utilisation avec un op�rateur
   Cet exemple construit un objet de d�finition (OP1) de type OPER
   qui est compos� d'un objet SIMP

   Dans un premier temps on v�rifie la conformite de l'objet 
   de d�finition ::

      cr=OP1.report()
      if cr.estvide(): ...

   Dans un deuxi�me temps, on construit plusieurs objets de type 
   ETAPE dont la d�finition est OP1 et on v�rifie la conformit�
   de ces objets.
"""

import sys
sys.path[:0]=['../..']

from Accas import SIMP,FACT,OPER

# Construction objet de d�finition

class concept:
   def __init__(self,etape):
      self.etape=etape
   def is_object(sd):
      """ Retourne 1 si sd est du bon type par rapport � la classe """
      return 0

class cata:
   def __init__(self):
      CONTEXT.unset_current_cata()
      CONTEXT.set_current_cata(self)

   def enregistre(self,commande):
      return

c=cata()

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
cr= co1.etape.report()
if cr.estvide():
   print "L'objet ETAPE  est valide " 
else:
   print "L'objet ETAPE  n'est pas valide " 
   print cr

# Test avec reutilisation de concept
co=OP1(reuse=co1,a=1,b=sd)
e=cont.etapes[1]
cr= e.report()
if cr.estvide():
   print "L'objet ETAPE  est valide "
else:
   print "L'objet ETAPE  n'est pas valide "
   print cr

