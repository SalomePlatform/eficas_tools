from Noyau import N_MACRO_ETAPE
from Validation import V_MACRO_ETAPE
from Ihm import I_MACRO_ETAPE

class MACRO_ETAPE(I_MACRO_ETAPE.MACRO_ETAPE,
                  V_MACRO_ETAPE.MACRO_ETAPE,
                  N_MACRO_ETAPE.MACRO_ETAPE):
   def __init__(self,oper=None,reuse=None,args={}):
      N_MACRO_ETAPE.MACRO_ETAPE.__init__(self,oper,reuse,args)
      V_MACRO_ETAPE.MACRO_ETAPE.__init__(self)
      I_MACRO_ETAPE.MACRO_ETAPE.__init__(self)
