# -*- coding: utf-8 -*-
"""
Module pause
------------
    le module pause propose la fonction PAUSE pour effectuer
    une attente.
"""
try :
        from developpeur import DEVELOPPEUR
except :
        DEVELOPPEUR=None

def NULL( *l_args, **d_args  ) : pass

if DEVELOPPEUR :

    import developpeur
    developpeur.sortie.write( "import de "+__name__+" : $Id: pause.py,v 1.3.8.1 2006/03/10 15:09:56 eficas Exp $" )
    developpeur.sortie.write( "\n" )

    import sys
    import ici
    
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
            developpeur.sortie.write( "\n\n\n" )
            ici.ICI()
                
            developpeur.sortie.write( "pause de "+str(secondes)+" secondes" )
            developpeur.sortie.write( "\n\n\n" )
            developpeur.sortie.flush()
    
            import time
            time.sleep( secondes )
    
        developpeur.sortie.flush()
    
        return

else :
    PAUSE = NULL


if __name__ == "__main__" :
    print
    print "PAUSE(secondes=-1)"
    PAUSE(secondes=-1)
    print "PAUSE(secondes=0)"
    PAUSE(secondes=0)
    print "PAUSE(secondes=2)"
    PAUSE(secondes=2)
