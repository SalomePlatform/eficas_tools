"""
Module pause
------------
    le module pause propose la fonction PAUSE pour effectuer
    une attente.
"""

import sys
sortie=sys.stderr
sortie.write( "import de "+__name__+" : $Id$" )
sortie.write( "\n" )

def PAUSE( secondes ) :

    """

    Fonction PAUSE
    ----------------
    La fonction PAUSE permet d'interrompre le traitement pendant un délai
    passé en argument. La localisation de l'appel est tracée sur la stderr

    Usage :
        from pause import PAUSE

        PAUSE(secondes=5)
    """

    if secondes > 0 :
        sortie.write( "\n\n\n" )
        import ici
        ici.ICI()
            
        sortie.write( "pause de "+str(secondes)+" secondes" )
        sortie.write( "\n\n\n" )
        sortie.flush()

        import time
        time.sleep( secondes )

    sortie.flush()

    return


if __name__ == "__main__" :
    print
    print "PAUSE(secondes=-1)"
    PAUSE(secondes=-1)
    print "PAUSE(secondes=0)"
    PAUSE(secondes=0)
    print "PAUSE(secondes=2)"
    PAUSE(secondes=2)
