"""
    $Id: __init__.py,v 1.3 2003/02/06 15:11:22 eficas Exp $

    Le package UTILITES contient les fonctions permettant
    d'instrumenter un script :
    - MESSAGE (module message)
    - SCRUTE (module scrute)
    - PAUSE (module pause)
"""


##__all__ = [ "ici" , "message" , "scrute" , "pause" , "appels" ]

try :
	from developpeur import *
except :
	pass
from ici import *
from execute import *
from pause import *
from scrute import *
from message import *
from appels import *
from modification import *



if __name__ == "__main__" :
    MODIFICATION( "toto" )
    developpeur.write( dir()+'\n' )
    developpeur.write( "import du package effectu� !" +'\n' )
