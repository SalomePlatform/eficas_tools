from Noyau import N_PROC_ETAPE
from Validation import V_PROC_ETAPE
from Ihm import I_PROC_ETAPE

class PROC_ETAPE(I_PROC_ETAPE.PROC_ETAPE,
                 V_PROC_ETAPE.PROC_ETAPE,
                 N_PROC_ETAPE.PROC_ETAPE):
   def __init__(self,oper=None,args={}):
      N_PROC_ETAPE.PROC_ETAPE.__init__(self,oper=oper,args=args)
      V_PROC_ETAPE.PROC_ETAPE.__init__(self)
      I_PROC_ETAPE.PROC_ETAPE.__init__(self)
