from Noyau import N_FORM_ETAPE
from Validation import V_MACRO_ETAPE
from Ihm import I_FORM_ETAPE

class FORM_ETAPE(I_FORM_ETAPE.FORM_ETAPE,V_MACRO_ETAPE.MACRO_ETAPE,N_FORM_ETAPE.FORM_ETAPE):
   def __init__(self,oper=None,reuse=None,args={}):
      N_FORM_ETAPE.FORM_ETAPE.__init__(self,oper,reuse,args)
      V_MACRO_ETAPE.MACRO_ETAPE.__init__(self)
      I_FORM_ETAPE.FORM_ETAPE.__init__(self)

