"""
Module message
--------------
    le module message propose la fonction MESSAGE pour afficher
    sur la stderr, le texte passé en argument.
    N.B. : la fonction MESSAGE n'est opérante que pour les développeurs
           (la variable DEVELOPPEUR doit être définie)
"""

try :
	from developpeur import DEVELOPPEUR
except :
	DEVELOPPEUR=None

def NULL( *l_args, **d_args  ) : pass

if DEVELOPPEUR :

    import developpeur
    developpeur.sortie.write( "import de "+__name__+" : $Id$" )
    developpeur.sortie.write( "\n" )

    import sys
    import ici

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

        ici.ICI( offset )
        developpeur.sortie.write( str(text)+'\n' )
        developpeur.sortie.flush()
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
            N.B. : la fonction DEBUT n'est opérante que pour les développeurs
        """

        developpeur.sortie.write( '\n\n' )
        MESSAGE("DEBUT du traitement [",offset=2)
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

            N.B. : la fonction FIN n'est opérante que pour les développeurs
        """

        MESSAGE("] FIN du traitement",offset=2)
        return

else :
    MESSAGE= NULL
    DEBUT = NULL
    FIN = NULL
