from Noyau import N_JDC
from Validation import V_JDC
from Extensions import jdc
from Ihm import I_JDC

class JDC(jdc.JDC,I_JDC.JDC,V_JDC.JDC,N_JDC.JDC):
   from A_ASSD import CO,assd

   def __init__(self,*pos,**args):
      N_JDC.JDC.__init__(self,*pos,**args)
      V_JDC.JDC.__init__(self)
      I_JDC.JDC.__init__(self)
      jdc.JDC.__init__(self)
