from N_ASSD import ASSD

class CO(ASSD):
  def __init__(self,nom):
    ASSD.__init__(self,etape=None,sd=None,reg='oui')
    #
    #  On demande le nommage du concept
    #
    if self.parent : 
       self.parent.NommerSdprod(self,nom)
    else:
       self.nom=nom

