from Noyau import N_MCFACT
from Validation import V_MCFACT
from Ihm import I_MCFACT

class MCFACT(I_MCFACT.MCFACT,N_MCFACT.MCFACT,V_MCFACT.MCFACT):
   def __init__(self,val,definition,nom,parent):
      N_MCFACT.MCFACT.__init__(self,val,definition,nom,parent)
      V_MCFACT.MCFACT.__init__(self)
