#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
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

