"""
    $Id$

    Le package UTILITES contient les fonctions permettant
    d'instrumenter un script :
    - MESSAGE (module message)
    - SCRUTE (module scrute)
    - PAUSE (module pause)
"""


__all__ = [ "ici" , "message" , "scrute" , "pause" ]
from pause import *
from ici import *
from scrute import *
from message import *



if __name__ == "__main__" :
    print dir()
    print "import du package effectué !"
