"""
"""

import sys
sys.path[:0]=['../..']

from Accas import SIMP,FACT,OPER,PROC,JDC_CATA

# Construction objet de définition

class concept:
   def __init__(self,etape):
      self.etape=etape
   def is_object(valeur):
      """
          Indique si valeur est d'un type conforme à la classe (1) ou non conforme (0)
      """
      return 0

JdC=JDC_CATA(code="ASTER")
OP1 = OPER(nom='OP1',op=1,sd_prod=concept,reentrant='f',
           a=SIMP(typ='I'),
           b=SIMP(typ=concept),
          )
DEBUT=PROC(nom='DEBUT',op=0,INFO=SIMP(typ='I'),)

