# -*- coding: utf-8 -*-
"""
Module ici
----------
    le module ici propose la fonction ICI pour afficher
    le fichier courant et le numéro de la ligne courante.
"""

try :
	from developpeur import DEVELOPPEUR
except :
	DEVELOPPEUR=None

def NULL( *l_args, **d_args  ) : pass

if DEVELOPPEUR :

    import developpeur
    developpeur.sortie.write( "import de "+__name__+" : $Id: ici.py,v 1.2 2003/03/06 14:36:11 eficas Exp $" )
    developpeur.sortie.write( "\n" )

    import sys

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

        N.B. : la fonction ICI n'est opérante que pour les développeurs
        """
    
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
            file_name, lineno, func_name, dummytxt = trace[ indice ]
    
            assert( (indice>0) or (func_name=="?") )
            if func_name=="?" : func_name = "main"
    
        if offset >= 0 :
                import funcname
                developpeur.sortie.write( file_name+':'+str(lineno)+': ('+str(funcname.FUNCNAME(func_name,file_name,lineno))+') : ' )
                developpeur.sortie.flush()
    
        return file_name,lineno


else :
	ICI = NULL
