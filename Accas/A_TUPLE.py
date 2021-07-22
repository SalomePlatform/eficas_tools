#
from __future__ import absolute_import
from Noyau import N_TUPLE
from Ihm  import I_TUPLE

class Tuple (N_TUPLE.N_Tuple): pass
class Matrice (I_TUPLE.I_Matrice,N_TUPLE.N_Matrice):pass
#      def __init__(self,*tup,**args):
#          I_TUPLE.I_Matrice.__init__(self)
#          N_TUPLE.N_Matrice(self,*tup,**args)
#          print (tup)
#          print (args)
