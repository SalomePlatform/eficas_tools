"""
    $Id: __init__.py,v 1.2 2003/02/04 10:40:57 eficas Exp $

    Le package UTILITES contient les fonctions permettant
    d'instrumenter un script :
    - MESSAGE (module message)
    - SCRUTE (module scrute)
    - PAUSE (module pause)
"""


##__all__ = [ "ici" , "message" , "scrute" , "pause" , "appels" ]
from pause import *
from ici import *
from scrute import *
from message import *
from appels import *



if __name__ == "__main__" :
    print dir()
    print "import du package effectué !"
