"""
Module ici
----------
    le module ici propose la fonction ICI pour afficher
    le fichier courant et le numéro de la ligne courante.
"""

import sys
sortie=sys.stderr
sortie.write( "import de "+__name__+" : $Id$" )
sortie.write( "\n" )

def ICI(offset=1) :

    """
    Fonction ICI
    ------------
    La fonction ICI affiche sur la stderr, le nom du fichier qui l'appelle,
    le numéro de la ligne ou elle est appelée et retourne ces deux informations.

    Usage :
        from ici import ICI
        ICI()
        filename,lineno=ICI()
    """

    sortie=sys.stderr

    sys.stdout.flush()
    sys.stderr.flush()
    try :
        1/0
    except :

        ###f=sys.exc_info()[2].tb_frame.f_back
        ###lineno=f.f_lineno
        ###code=f.f_code
        ###filename=code.co_filename

        import traceback
        trace=traceback.extract_stack()

        indice = len(trace)-(2+offset)
        if indice<0 : indice=0


        assert( indice<len(trace) ),"valeur de offset INVALIDE : "+str(offset)+" taille de la table "+len(trace)
        file, lineno, funcname, dummytxt = trace[ indice ]

        assert( (indice>0) or (funcname=="?") )
        if funcname=="?" : funcname = "main"

        sortie.write( file+':'+str(lineno)+': ('+funcname+') : ' )
        sortie.flush()

    return file,lineno
