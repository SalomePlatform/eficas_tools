"""
Module scrute
-------------
    le module scrute propose la fonction SCRUTE qui affiche sur
    la stderr, la valeur de l'objet (passé en argument)
    précédée le nom de l'objet.
"""

import sys
sortie=sys.stderr
sortie.write( "import de "+__name__+" : $Id$" )
sortie.write( "\n" )


def SCRUTE( valeur ) :

    """
    Fonction SCRUTE
    ---------------
    La fonction SCRUTE affiche sur la stderr, la valeur (passée en argument)
    d'une variable précédée de son nom.
    L'affichage précise également le nom du fichier et le numéro
    de la ligne où la fonction SCRUTE a été appelée.

    N.B. : le type de la variable doit posséder de préférence une méthode __str__

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
    assert(len(l_occurrences)>0),__name__+" : pas de SCRUTE trouvé !"
    assert(len(l_occurrences)<=1),\
        __name__+" : "+str(len(l_occurrences))+" SCRUTE sur la même ligne ; c'est LIMITE à 1 !"

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
