# -*- coding: utf-8 -*-
"""
Module intervention
-------------------
    Permet aux développeurs de signer leur intervention à
    destination des autres développeurs.
"""

try :
	from developpeur import DEVELOPPEUR
except :
	DEVELOPPEUR=None

def NULL( *l_args, **d_args  ) : pass


if DEVELOPPEUR :

    import developpeur
    developpeur.sortie.write( "import de "+__name__+" : $Id: modification.py,v 1.1 2003/03/06 14:36:11 eficas Exp $" )
    developpeur.sortie.write( "\n" )
    import ici

    def MODIFICATION( text , offset=1 ) :
    
        """
        Fonction MODIFICATION
        ---------------------
    
        Usage :
            from utilites import MODIFICATION
    
            utilites.MODIFICATION("auteur,date et intention")
        """
    
        ici.ICI( offset )
        developpeur.sortie.write( "MODIFICATION "+str(text)+'\n' )
        developpeur.sortie.flush()
        return


else :
    MODIFICATION = NULL
        

if __name__ == "__main__" :
    MODIFICATION( "baratin inutile" )
