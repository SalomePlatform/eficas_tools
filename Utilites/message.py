"""
Module message
--------------
    le module message propose la fonction MESSAGE pour afficher
    sur la stderr, le texte passé en argument.
"""

import sys
sortie=sys.stderr
sortie.write( "import de "+__name__+" : $Id$" )
sortie.write( "\n" )

def MESSAGE( text , offset=1 ) :

    """
    Fonction MESSAGE
    ----------------
    La fonction MESSAGE affiche sur la stderr, le texte passé en argument.
    Elle précise également le nom du fichier et le numéro de la ligne où
    elle a été appelée.

    Usage :
        from message import MESSAGE

        MESSAGE("debut du traitement")
        MESSAGE( "Exception interceptée "+str(e) )
    """

    sortie=sys.stderr

    import ici
    ici.ICI( offset )
    sortie.write( str(text)+'\n' )
    sortie.flush()
    return



def DEBUT() :

    """
    Fonction DEBUT
    --------------
    La fonction DEBUT affiche sur la stderr, le texte signalant le début
    d'un traitement

    Usage :
        from message import *
        DEBUT()
    """

    MESSAGE("DEBUT du traitement",offset=2)
    return



def FIN() :

    """
    Fonction FIN
    ------------
    La fonction FIN affiche sur la stderr, le texte signalant la fin
    d'un traitement

    Usage :
        from message import *
        FIN()
    """

    print
    MESSAGE("FIN du traitement",offset=2)
    return
