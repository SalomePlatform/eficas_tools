"""
Module scrute
-------------
    le module scrute propose la fonction SCRUTE qui affiche sur
    la stderr, la valeur de l'objet (pass� en argument)
    pr�c�d�e le nom de l'objet.
"""

import sys
sortie=sys.stderr
sortie.write( "import de "+__name__+" : $Id$" )
sortie.write( "\n" )


def SCRUTE( valeur ) :

    """
    Fonction SCRUTE
    ---------------
    La fonction SCRUTE affiche sur la stderr, la valeur (pass�e en argument)
    d'une variable pr�c�d�e de son nom.
    L'affichage pr�cise �galement le nom du fichier et le num�ro
    de la ligne o� la fonction SCRUTE a �t� appel�e.

    N.B. : le type de la variable doit poss�der de pr�f�rence une m�thode __str__

    Usage :
        from scrute import SCRUTE
        r=1.0
        SCRUTE(r)
        SCRUTE(r+1)
        SCRUTE(f(r))
    Erreur :
        SCRUTE(r) ; SCRUTE(f(r)) # ==> ERREUR
    """

    import re
    import linecache
    import ici

    filename,lineno=ici.ICI()

    line = linecache.getline( filename, lineno )

    ll=re.sub( "\s*#.*$" , '' ,line)
    l_occurrences=[]
    l_occurrences=re.findall( "SCRUTE" , ll )
    assert(len(l_occurrences)>0),__name__+" : pas de SCRUTE trouv� !"
    assert(len(l_occurrences)<=1),\
        __name__+" : "+str(len(l_occurrences))+" SCRUTE sur la m�me ligne ; c'est LIMITE � 1 !"

    ll=re.sub( "\s*;.*$" , '' ,line)
    regex='^.*SCRUTE[^(]*\('
    l=re.sub( regex , '' ,ll)
    regex='\)[^)]*$'
    nom_objet=re.sub( regex , '' ,l)

    try :
        sortie.write( nom_objet+'=' )
        sortie.write( str(valeur) )
        sortie.write( " ("+str(type(valeur))+")" )
    except : pass
    sortie.write( '\n' )
    sortie.flush()

    return
