from Noyau import N_JDC_CATA
import A_JDC
from Ihm import I_JDC_CATA

class JDC_CATA(I_JDC_CATA.JDC_CATA,N_JDC_CATA.JDC_CATA):
   class_instance=A_JDC.JDC
   def __init__(self,*pos,**kw):
      N_JDC_CATA.JDC_CATA.__init__(self,*pos,**kw)
      I_JDC_CATA.JDC_CATA.__init__(self)
