# -*- coding: utf-8 -*-
# Auteur : A. Yessayan
# Date : jeudi 06/03/2003 a 14:36:00

"""

Module MakeNomComplet
---------------------
    Construction du nom complet d'un fichier dans un répertoire existant.
    Le fichier n'existe pas forcément mais le répertoire doit OBLIGATOIREMENT
    exister.
    
    Usage :
           import MakeNomComplet

           txt="main.py"
           txt="./main.py"
           txt="/tmp/main.py"
           try :
                nom_complet=str(MakeNomComplet.FILNAME( txt ))
                dir_name = MakeNomComplet.dirname(txt)
                fic_name = MakeNomComplet.basename(txt)
           except Exception,e:
                print txt,' est un nom INVALIDE'
                print str(e) 

"""

try :
	from developpeur import DEVELOPPEUR
except :
	DEVELOPPEUR=None

if DEVELOPPEUR :
    import developpeur
    developpeur.sortie.write( "import de "+__name__+" : $Id: MakeNomComplet.py,v 1.2 2003/03/07 14:30:48 eficas Exp $" )
    developpeur.sortie.write( "\n" )


import string
import os
import os.path
import types
import re

class FILENAME :
    def __init__( self , s ) :
        assert(type(s)==types.StringType)
        assert(len(s)>0)
        self.text = s
        self.rep=None
        self.file=None
        liste=string.split( self.text , '/' )
        l=len(liste)
        assert(l>=1)
        if l == 1 :
            rep="."
        else :
            # evaluation des eventuels paramètres shell : DEBUT
            l_evalue=[]
            for d in liste :
                if len(d) and d[0]=='$' :
                     d=re.sub( "[\${}]" , "" , d )
                     d=os.getenv(d)
                l_evalue.append(d)
            # evaluation des eventuels paramètres shell : FIN

            rep=string.join( l_evalue[0:l-1] , '/' )
        try :
            self.rep = self.getcwd_( rep )
            self.file = liste[-1]
        except Exception,e :
            raise Exception( "nom de repertoire INVALIDE : "+rep )

    def getcwd_ ( self , rep ) :
        prev = os.getcwd()
        os.chdir( rep )
        wd = os.getcwd()
        os.chdir( prev )
        return wd

    def dirname( self ) :
        return self.rep

    def basename( self ) :
        return self.file

    def __str__ ( self ) :
        return self.rep+'/'+self.file
        
        


def dirname( s ) :
    """
    retourne dans une string, le nom complet du répertoire
    du fichier dont le nom est passe dans s.
    S'il n' y a pas de chemin dans s, c'ets le nom complet
    du répertoire courant qui est retourné.
    N.B. : ce repertoire doit exister
    """
    f=FILENAME(s)
    return f.dirname()


def basename( s ) :
    """
    retourne dans une string, le nom simple du fichier dont le nom
    est passe dans s.
    N.B. : le repertoire (s'il ya un chemin dans s) doit exister
    """
    f=FILENAME(s)
    return f.basename()


if __name__ == "__main__" :

    import sys

    import MakeNomComplet

    s="${PWD}/MakeNomComplet.py"
    print dirname( s )
    print basename( s )
    print str(MakeNomComplet.FILENAME(s))

    print dirname( "MakeNomComplet.py" )
    print basename( "MakeNomComplet.py" )

    print dirname( "./MakeNomComplet.py" )
    print basename( "./MakeNomComplet.py" )


    try :
    	print basename( "/toto/main.py" )
    	print "ERREUR"
        sys.exit(5)
    except Exception,e :
        print str(e)
    	print "OKAY"
        pass
    print "FIN NORMALE DE "+__name__
    sys.exit(0)
