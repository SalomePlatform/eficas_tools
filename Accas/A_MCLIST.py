from Noyau import N_MCLIST
from Validation import V_MCLIST
from Ihm import I_MCLIST

class MCList(I_MCLIST.MCList,N_MCLIST.MCList,V_MCLIST.MCList):
   def __init__(self):
      N_MCLIST.MCList.__init__(self)
