"""
Module message
--------------
    le module message propose la fonction MESSAGE pour afficher
    sur la stderr, le texte pass� en argument.
    N.B. : la fonction MESSAGE n'est op�rante que pour les d�veloppeurs
           (la variable DEVELOPPEUR doit �tre d�finie)
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
        La fonction MESSAGE affiche sur la stderr, le texte pass� en argument.
        Elle pr�cise �galement le nom du fichier et le num�ro de la ligne o�
        elle a �t� appel�e.

        Usage :
        from message import MESSAGE

        MESSAGE("debut du traitement")
        MESSAGE( "Exception intercept�e "+str(e) )
        """

        ici.ICI( offset )
        developpeur.sortie.write( str(text)+'\n' )
        developpeur.sortie.flush()
        return



    def DEBUT() :

        """
        Fonction DEBUT
        --------------
        La fonction DEBUT affiche sur la stderr, le texte signalant le d�but
        d'un traitement

        Usage :
            from message import *
            DEBUT()
            N.B. : la fonction DEBUT n'est op�rante que pour les d�veloppeurs
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

            N.B. : la fonction FIN n'est op�rante que pour les d�veloppeurs
        """

        MESSAGE("] FIN du traitement",offset=2)
        return

else :
    MESSAGE= NULL
    DEBUT = NULL
    FIN = NULL
