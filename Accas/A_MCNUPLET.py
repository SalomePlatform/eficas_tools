from Extensions import mcnuplet
from Ihm import I_MCCOMPO

class MCNUPLET(mcnuplet.MCNUPLET,I_MCCOMPO.MCCOMPO):
   def __init__(self,*pos,**args):
      mcnuplet.MCNUPLET.__init__(self,*pos,**args)
