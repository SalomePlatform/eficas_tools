"""
Module exec
-----------
    le module exec ...
"""

try :
	from developpeur import DEVELOPPEUR
except :
	DEVELOPPEUR=None

if DEVELOPPEUR :

    import message
    import scrute
    import types
    import developpeur
    developpeur.sortie.write( "import de "+__name__+" : $Id$" )
    developpeur.sortie.write( "\n" )
    developpeur.sortie.flush()


    class EXEC :

        def __init__ ( self, texte, contexte=None, verbeux=1 ) :

            assert( type(texte) == types.StringType )
            if contexte == None :
                contexte = globals()

            if verbeux :
                message.MESSAGE( "execution de "+texte )
            try :
                exec texte in contexte
            except Exception,e :
                if verbeux :
                    import traceback
                    traceback.print_exc()
                    developpeur.sortie.write( "\n\n\n" )
                    message.MESSAGE( "Exception interceptee" )
                    scrute.SCRUTE( texte )
                    scrute.SCRUTE( contexte )
                    scrute.SCRUTE( e.__class__.__name__ )
                    scrute.SCRUTE( str(e) )
                    developpeur.sortie.write( "\n\n\n" )
                    developpeur.sortie.flush()
                raise 


else :
    class EXEC : pass




if __name__ == "__main__" :
    class Ex(Exception) : pass
    def toto() :
        print "toto"
        raise Ex( "y a bel et bien un erreur" )

    def tutu() :
        s = "toto()"
        EXEC( s , verbeux=1)

    try :
        tutu()
    except Exception,ee :
        scrute.SCRUTE(str(ee))
        scrute.SCRUTE(ee.__class__)
        pass
