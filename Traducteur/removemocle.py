# -*- coding: utf-8 -*-
import logging
from parseur import FactNode

#debug=1
debug=0
#on n'a qu'un mocle par commande. On peut donc supprimer le mocle sans trop de précautions (a part iterer a l'envers sur les commandes)
#avant de supprimer un autre mocle, on remet à jour l'arbre syntaxique (lineno,colno,etc.)
def removemocle(jdc,command,mocle):
    #on itere sur les commandes a l'envers pour ne pas polluer les numeros de ligne avec les modifications
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != mocle:continue
            removemc(jdc,c,mc)

    jdc.reset(jdc.getSource())
                
def removemc(jdc,c,mc):
    if debug:print "Suppression de:",c.name,mc.name,mc.lineno,mc.colno,mc.endline,mc.endcol
    logging.info("Suppression de: %s, %s, %s, %s, %d, %d",c.name,mc.name,mc.lineno,mc.colno,mc.endline,mc.endcol)
    if mc.endline > mc.lineno:
        if debug:print "mocle sur plusieurs lignes--%s--" % jdc.getLines()[mc.lineno-1][mc.colno:]
        jdc.getLines()[mc.lineno-1]=jdc.getLines()[mc.lineno-1][:mc.colno]
        jdc.getLines()[mc.endline-1]=jdc.getLines()[mc.endline-1][mc.endcol:]
        #attention : supprimer les lignes à la fin
        jdc.getLines()[mc.lineno:mc.endline-1]=[]
    else:
        if debug:print "mocle sur une ligne--%s--" % jdc.getLines()[mc.lineno-1][mc.colno:mc.endcol]
        s=jdc.getLines()[mc.lineno-1]
        jdc.getLines()[mc.lineno-1]=s[:mc.colno]+s[mc.endcol:]
    fusionne(jdc,mc.lineno-1)
    jdc.reset(jdc.getSource())

def removemocleinfact(jdc,command,fact,mocle):
    #on itere sur les commandes a l'envers pour ne pas polluer les numeros de ligne avec les modifications
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != fact:continue
            l=mc.childNodes[:]
            l.reverse()
            for ll in l:
                for n in ll.childNodes:
                    if n.name != mocle:continue
                    removemc(jdc,c,n)

    jdc.reset(jdc.getSource())

def fusionne(jdc,numLigne):
    index=0
    texte=jdc.getLines()[numLigne]
    fusion=1
    while (index < len(texte)) :
      if texte[index] not in (" ",",",")",";","\n") :
         fusion=0
         break
      index=index+1
    if fusion : 
       import load 
       jdc.joinLineandNext(numLigne)
