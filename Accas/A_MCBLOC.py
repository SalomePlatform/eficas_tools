from Noyau import N_MCBLOC
from Validation import V_MCBLOC
from Ihm import I_MCBLOC

class MCBLOC(I_MCBLOC.MCBLOC,N_MCBLOC.MCBLOC,V_MCBLOC.MCBLOC):
   def __init__(self,val,definition,nom,parent):
      N_MCBLOC.MCBLOC.__init__(self,val,definition,nom,parent)
      V_MCBLOC.MCBLOC.__init__(self)
