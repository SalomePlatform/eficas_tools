# -*- coding: utf-8 -*-

import compiler
import types
from parseur  import Keyword, FactNode, lastparen, lastparen2,maskStringsAndComments
from visiteur import KeywordFinder, visitor
from utils    import indexToCoordinates
import traceback

debug=0

#------------------------
def parseFact(match,c,kw):
#------------------------
    submatch=match[2]
    lastpar=match[0]+lastparen(c.src[match[0]:])
    if type(submatch[0][0]) ==types.IntType:
        #mot cle facteur isol�
        no=FactNode()
        kw.addChild(no)
        for ii in range(len(submatch)-1):
            e=submatch[ii]
            x,y=indexToCoordinates(c.src,e[0])
            lineno=y+c.lineno
            colno=x
            x,y=indexToCoordinates(c.src,submatch[ii+1][0])
            endline=y+c.lineno
            endcol=x
            no.addChild(Keyword(e[1],lineno,colno,endline,endcol))
        #last one
        e=submatch[-1]
        x,y=indexToCoordinates(c.src,e[0])
        lineno=y+c.lineno
        colno=x
        x,y=indexToCoordinates(c.src,lastpar-1)
        endline=y+c.lineno
        endcol=x
        no.addChild(Keyword(e[1],lineno,colno,endline,endcol))
    else:
        #mot cle facteur multiple
        ii=0
        for l in submatch:
            lastpar=l[0][0]+lastparen2(c.src[l[0][0]:])
            ii=ii+1
            no=FactNode()
            kw.addChild(no)
            for j in range(len(l)-1):
                e=l[j]
                x,y=indexToCoordinates(c.src,e[0])
                lineno=y+c.lineno
                colno=x
                x,y=indexToCoordinates(c.src,l[j+1][0])
                endline=y+c.lineno
                endcol=x
                no.addChild(Keyword(e[1],lineno,colno,endline,endcol))
            #last one
            e=l[-1]
            x,y=indexToCoordinates(c.src,e[0])
            lineno=y+c.lineno
            colno=x
            x,y=indexToCoordinates(c.src,lastpar-1)
            endline=y+c.lineno
            endcol=x
            no.addChild(Keyword(e[1],lineno,colno,endline,endcol))


#-----------------------
def parseKeywords(root):
#-----------------------
    """A partir d'un arbre contenant des commandes, ajoute les noeuds 
       fils correspondant aux mocles de la commande
    """
    #print "parseKeywords"
    #traceback.print_stack(limit=5)

    matchFinder=KeywordFinder()

    for c in root.childNodes:
        maskedsrc=maskStringsAndComments(c.src)
        #on supprime seulement les blancs du debut pour pouvoir compiler
        #meme si la commande est sur plusieurs lignes seul le debut compte
        ast=compiler.parse(c.src.lstrip())
        #print ast
        #Ne pas supprimer les blancs du debut pour avoir les bons numeros de colonne
        matchFinder.reset(maskedsrc)
        visitor.walk(ast, matchFinder)
        #print matchFinder.matches
        if len(matchFinder.matches) > 1:
            # plusieurs mocles trouv�s : 
            # un mocle commence au d�but du keyword (matchFinder.matches[i][0])
            # et finit juste avant le keyword suivant 
            # (matchFinder.matches[i+1][0]])
            for i in range(len(matchFinder.matches)-1):
                if debug:print "texte:",c.src[matchFinder.matches[i][0]:matchFinder.matches[i+1][0]]
                x,y=indexToCoordinates(c.src,matchFinder.matches[i][0])
                lineno=y+c.lineno
                colno=x
                x,y=indexToCoordinates(c.src,matchFinder.matches[i+1][0])
                endline=y+c.lineno
                endcol=x
                if debug:print matchFinder.matches[i][0],matchFinder.matches[i][1],lineno,colno,endline,endcol
                kw=Keyword(matchFinder.matches[i][1],lineno,colno,endline,endcol)
                c.addChild(kw)
                submatch= matchFinder.matches[i][2]
                if submatch:
                    parseFact(matchFinder.matches[i],c,kw)

            # dernier mocle : 
            #   il commence au debut du dernier keyword 
            #   (matchFinder.matches[i+1][0]) et
            #   finit avant la parenthese fermante de la commande (c.lastparen)

            if debug:print "texte:",c.src[matchFinder.matches[i+1][0]:c.lastparen]
            x,y=indexToCoordinates(c.src,matchFinder.matches[i+1][0])
            lineno=y+c.lineno
            colno=x
            x,y=indexToCoordinates(c.src,c.lastparen)
            endline=y+c.lineno
            endcol=x
            if debug:print matchFinder.matches[i+1][0],matchFinder.matches[i+1][1],lineno,colno,endline,endcol
            kw=Keyword(matchFinder.matches[i+1][1],lineno,colno,endline,endcol)
            c.addChild(kw)
            submatch= matchFinder.matches[i+1][2]
            if submatch:
                parseFact(matchFinder.matches[i+1],c,kw)

        elif len(matchFinder.matches) == 1:
            #un seul mocle trouve : 
            # il commence au d�but du keyword (matchFinder.matches[0][0]) et 
            # finit juste avant la parenthese fermante de la 
            # commande (c.lastparen)
            if debug:print "texte:",c.src[matchFinder.matches[0][0]:c.lastparen]
            x,y=indexToCoordinates(c.src,matchFinder.matches[0][0])
            lineno=y+c.lineno
            colno=x
            x,y=indexToCoordinates(c.src,c.lastparen)
            endline=y+c.lineno
            endcol=x
            if debug:print matchFinder.matches[0][0],matchFinder.matches[0][1],lineno,colno,endline,endcol
            kw=Keyword(matchFinder.matches[0][1],lineno,colno,endline,endcol)
            c.addChild(kw)
            submatch= matchFinder.matches[0][2]
            if submatch:
                parseFact(matchFinder.matches[0],c,kw)
        else:
            pass
