from Noyau import N_MCSIMP
from Validation import V_MCSIMP
from Ihm import I_MCSIMP

class MCSIMP(I_MCSIMP.MCSIMP,N_MCSIMP.MCSIMP,V_MCSIMP.MCSIMP):
   def __init__(self,val,definition,nom,parent):
      N_MCSIMP.MCSIMP.__init__(self,val,definition,nom,parent)
      V_MCSIMP.MCSIMP.__init__(self)
