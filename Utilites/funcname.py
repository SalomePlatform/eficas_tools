import re,types
import sys

sortie=sys.stderr
sortie.write( "import de "+__name__+" : $Id$" )
sortie.write( "\n" )

def get_nombre_de_blancs( str ) :
    nombre_de_blancs=0
    if str :
        nombre_de_blancs=len(re.sub( "[^ ].*$" , "" , str ))
    return nombre_de_blancs



def get_classname( filename, lineno ) :
    """
        Cette méthode sert à trouver dans quelle classe (le cas échéant)
        se trouve l'instruction numéro lineno dans le fichier filename.
    """
    classname = ""
    current_func = ""
    assert(type(filename)==types.StringType)
    ####print "RECHERCHE de la classe de "+filename+" ligne : ",lineno
    if lineno>0 :
        try :
        	f=open( filename , 'r' )
	except Exception,e :
        	print ">>>>",str(e)
		sys.stdout.flush()
		sys.exit(17)

        s = f.read()
        f.close()
        l_lines = s.split( '\n' )
        k=1
        inst = l_lines[lineno]
        nb_blancs= get_nombre_de_blancs( inst )

        for line in l_lines :
            if k == lineno :
                break
            elif re.search( "^ *def ", line ) != None :
                if get_nombre_de_blancs( line ) < nb_blancs :
                    current_func=re.sub( "^ *def  *" , "" , line )
                    current_func=re.sub( " *\(.*$" , "" , current_func )
            elif re.search( "^class ", line ) != None :
                classname = re.sub( "^class  *" , "" , line )
                classname = re.sub( " *[(:].*$" , "" , classname )
	        current_func = ""
            elif current_func != "" and re.search( "^[^ \t]", line ) != None :
	        current_func = ""
	        classname = ""
            k = k+1
    if current_func == "" : current_func="__main__"
    return classname ,current_func




class FUNCNAME :

    """
        Conversion des 3 informations nom de méthode, nom de fichier
        numéro de ligne en un nom complet de méthode
    """

    def __init__ ( self , *args ) :

	# le premier argument est optionnel (c'est un nom de fonction 
        # qu'on peut reconstituer avec le nom du fichier et le numéro de ligne.
        k=0
        self.name = None
        if len(args)>2 :
            if args[k] != "" : self.name = args[k]
            k = k+1

        assert(args[k]!=None)
        assert(args[k]!="")
        self.filename = args[k]	# recuperation du nom du fichier source

        k = k+1
        assert(args[k]>0)
        self.lineno = args[k]	# recupération du numero de ligne

        self.classname,funcname = get_classname( self.filename, self.lineno )
        if self.name == None : self.name = funcname
        ###assert(funcname==self.name or self.name=="main" or self.name=="<lambda>" ), "attendue '"+self.name+"' - trouvee '"+funcname+"'"

    def __str__ ( self ) :
        if self.classname != "" :
            name=self.classname+"."+self.name
        else :
            name=self.name
        return name


if __name__ == "__main__" :
	print  'FUNCNAME("","funcname.py", 68)='+str(FUNCNAME("","funcname.py", 63) )
	print  'FUNCNAME("funcname.py", 68)='+str(FUNCNAME("funcname.py", 63) )
