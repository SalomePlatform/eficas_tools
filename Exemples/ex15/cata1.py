"""
"""

from Accas import SIMP,FACT,OPER,PROC,JDC_CATA,MACRO,ASSD

# Construction objet de d�finition

class concept(ASSD):pass

JdC=JDC_CATA(code="ASTER")

OP1 = OPER(nom='OP1',op=1,sd_prod=concept,reentrant='f',
           a=SIMP(typ='I'),
           b=SIMP(typ=concept),
          )
DEBUT=PROC(nom='DEBUT',op=0,INFO=SIMP(typ='I'),)
MA_MACRO=MACRO(nom="MA_MACRO",op=-1,sd_prod=concept,
                        A=SIMP(typ='I'))

