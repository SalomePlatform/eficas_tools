"""
Module appels
-------------
    le module appels ...
"""

import sys
sortie=sys.stderr
sortie.write( "import de "+__name__+" : $Id$" )
sortie.write( "\n" )


def APPELS() :

    """
    Fonction APPELS
    ---------------
    La fonction APPELS ...
    ..


    Usage :
        from appels import APPELS
        APPELS()
    """

    print  "Passage dans APPELS"
### try :
###     1/0
### except :
###     import traceback
###     trace=traceback.extract_stack()
###     print trace

    import traceback
    trace=traceback.extract_stack()

    trace.reverse()

    decalage=""
    if len(trace)>2 :
        for e in trace[2:-1] :
            fic,numero,fonc,inst = e
            print decalage+fic+":"+str(numero)+": "+fonc,inst
            decalage += "\t"

    fic,numero,fonc,inst = trace[-1]
    print decalage+fic+":"+str(numero)+": "+"__main__",inst


    return


if __name__ == "__main__" :
	APPELS()
