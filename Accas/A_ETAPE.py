from Noyau import N_ETAPE
from Validation import V_ETAPE
from Ihm import I_ETAPE

class ETAPE(I_ETAPE.ETAPE,V_ETAPE.ETAPE,
            N_ETAPE.ETAPE):
   def __init__(self,oper=None,reuse=None,args={}):
      # Pas de constructeur pour B_ETAPE.ETAPE
      N_ETAPE.ETAPE.__init__(self,oper,reuse,args)
      V_ETAPE.ETAPE.__init__(self)
      I_ETAPE.ETAPE.__init__(self)
