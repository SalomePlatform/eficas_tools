from I_ASSD import ASSD

class FONCTION(ASSD):
  def __init__(self,etape=None,sd=None,reg='oui'):
    #ASSD.__init__(self,etape=etape,sd=sd,reg=reg)
    if reg=='oui':
      self.jdc.register_fonction(self)

  def get_formule(self):
    """
    Retourne une formule décrivant self sous la forme d'un tuple :
    (nom,type_retourne,arguments,corps)
    """
    if hasattr(self.etape,'get_formule'):
      # on est dans le cas d'une formule Aster
      return self.etape.get_formule()
    else:
      # on est dans le cas d'une fonction
      return (self.nom,'REEL','(REEL:x)','''bidon''')

class fonction(FONCTION) : pass

