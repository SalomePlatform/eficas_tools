"""
"""

from Accas import SIMP,FACT,OPER,PROC,JDC_CATA,MACRO,ASSD

# Construction objet de définition

class concept(ASSD):pass

JdC=JDC_CATA(code="ASTER")

def op2_sdprod(a,**args):
   return concept

OP2 = OPER(nom='OP2',op=2,sd_prod=op2_sdprod,reentrant='f',
           a=SIMP(typ='I'),
           b=SIMP(typ=concept),
          )
OP1 = OPER(nom='OP1',op=1,sd_prod=concept,reentrant='f',
           a=SIMP(typ='I'),
           b=SIMP(typ=concept),
          )
DEBUT=PROC(nom='DEBUT',op=0,INFO=SIMP(typ='I'),)
MA_MACRO=MACRO(nom="MA_MACRO",op=-1,sd_prod=concept,
                        A=SIMP(typ='I'))


