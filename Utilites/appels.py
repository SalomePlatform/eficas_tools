# -*- coding: utf-8 -*-
"""
Module appels
-------------
    le module appels ...
"""

try :
        from developpeur import DEVELOPPEUR
except :
        DEVELOPPEUR=None

def NULL( *l_args, **d_args  ) : pass

if DEVELOPPEUR :

    import developpeur
    developpeur.sortie.write( "import de "+__name__+" : $Id: appels.py,v 1.3.8.1 2006/03/10 15:09:53 eficas Exp $" )
    developpeur.sortie.write( "\n" )

    import sys
    import re
    import ici
    import funcname
    
    
    def Alonge( chaine , longueur ) :
        return chaine+' ' # provisoirement on ne complete pas la chaine
        k=len(chaine)
        while( k<longueur ) :
            chaine = chaine + ' '
            k+=1
        return chaine
    
    def APPELS( dec="" ) :
    
        """
        Fonction APPELS
        ---------------
        La fonction APPELS ...
        ..
    
    
        Usage :
            from appels import APPELS
            APPELS()
        """
    
    ### try :
    ###     1/0
    ### except :
    ###     import traceback
    ###     trace=traceback.extract_stack()
    ###     print trace
    
        nombre_de_blancs=None
    
        import traceback
        trace=traceback.extract_stack()
    
        trace.reverse()
    
        decalage=dec
        sys.stderr.flush()
        sys.stdout.flush()
    
        developpeur.sortie.write( 3*'\n' )
        developpeur.sortie.write( decalage )
        developpeur.sortie.write( "LISTE des appels" )
        developpeur.sortie.write( '\n' )
        developpeur.sortie.flush()
        if len(trace)>2 :
            decalage += '\t'
    
            # Recherche du plus long nom de fichier pour la mise en forme
            lmax=0
            for e in trace[2:-1] :
                fic,numero,fonc,inst = e
                position=fic+":"+str(numero)+":"
                if len(position)>lmax : lmax=len(position)
            lmax += 1 # Pour eloigner les informations du nom du fichier
    
            for e in trace[1:-1] :
                fic,numero,fonc,inst = e
                position = chaine=fic+":"+str(numero)+":"
                position = Alonge( chaine=position , longueur=lmax )
                developpeur.sortie.write( decalage+position)
                developpeur.sortie.flush()
                fname=funcname.FUNCNAME(fic,numero)
                developpeur.sortie.write( str(fname) )
                developpeur.sortie.write( ' : ' )
                developpeur.sortie.write( inst )
                developpeur.sortie.write( '\n' )
                developpeur.sortie.flush()
                decalage += ""
    
        fic,numero,fonc,inst = trace[-1]
        position = chaine=fic+":"+str(numero)+":"
        position = Alonge( chaine=position , longueur=lmax )
        developpeur.sortie.write( decalage+position)
        developpeur.sortie.flush()
        fname="__main__"
        developpeur.sortie.write( str(fname) )
        developpeur.sortie.write( ' : ' )
        developpeur.sortie.write( inst )
        developpeur.sortie.write( 3*'\n' )
        developpeur.sortie.flush()
    
    
        return

else :
        APPELS = NULL



if __name__ == "__main__" :
    TOTO=NULL
    TOTO(  dec="" )
