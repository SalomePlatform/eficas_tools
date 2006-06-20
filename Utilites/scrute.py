# -*- coding: utf-8 -*-
"""
Module scrute
-------------
    Le module scrute propose la fonction SCRUTE qui affiche sur
    la stderr, la valeur de l'objet (pass� en argument)
    pr�c�d�e le nom de l'objet.
    Il propose �galement la fonction EXAMINE qui d�taille sur
    la stderr le contenu d'un objet
    
    N.B. : les fonctions SCRUTE e EXAMINE ne sont op�rantes que pour les d�veloppeurs
           (la variable DEVELOPPEUR doit �tre d�finie)
"""

try :
        from developpeur import DEVELOPPEUR
except :
        DEVELOPPEUR=None

def NULL( *l_args, **d_args  ) : pass

if DEVELOPPEUR :

    import developpeur
    developpeur.sortie.write( "import de "+__name__+" : $Id: scrute.py,v 1.3.8.1 2006/03/10 15:09:56 eficas Exp $" )
    developpeur.sortie.write( "\n" )
    import re
    import linecache
    import ici
    import sys

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
            developpeur.sortie.write( nom_objet+'=' )
            s=str(valeur)
            developpeur.sortie.write( s )
            developpeur.sortie.write( " ("+str(type(valeur))+")" )
        except : pass
        developpeur.sortie.write( '\n' )
        developpeur.sortie.flush()

        return

    def makeClassName( ob ) :
        import types
        if type(ob) == types.InstanceType :
            return str(ob.__class__)
        else :
            return str(type(ob))
        

    def EXAMINE( ob ) :
        """
        Affiche sur la developpeur.sortie le contenu d'un objet

        Usage :
            class KLASS : pass
            import Utilites
            object=KLASS()
            Utilites.EXAMINE(object)
        """

        appel_EXAMINE=1
        f = sys._getframe( appel_EXAMINE )
        context=f.f_locals

        filename,lineno=ici.ICI()
        line = linecache.getline( filename, lineno )
        nom=re.sub( "^.*EXAMINE *\(", "" , line )
        nom=re.sub( " *[,\)].*$", "" , nom )
        nom=re.sub( "\n", "" , nom )
        developpeur.sortie.write( "Examen de "+nom+" de type "+makeClassName(ob)+"\n" )

        for att in dir(ob) :
            st=nom+'.'+att
            developpeur.sortie.write( '\t'+st+' = ' )
            developpeur.sortie.flush()
            commande="import developpeur;developpeur.sortie.write( str("+st+")+'\\n' )"
            try :
                exec commande in context
            except :
                commande="import sys; sys.stderr.write( str("+st+")+'\\n' )"
                exec commande in context
            
        return


else :

    SCRUTE = NULL
    EXAMINE = NULL
