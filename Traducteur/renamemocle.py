# -*- coding: utf-8 -*-
import logging
from parseur import FactNode
debug=1

#on n'a qu'un mocle par commande. 
#en fin de traitement, on remet à jour l'arbre syntaxique (lineno,colno,etc.)

def renamemocle(jdc,command,mocle,new_name):
    for c in jdc.root.childNodes:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != mocle:continue
            if debug:print "Renommage de:",c.name,mc.name,mc.lineno,mc.colno
            logging.info("Renommage de: %s, %s, %s, %s en %s",c.name,mc.name,mc.lineno,mc.colno,new_name)
            s=jdc.getLines()[mc.lineno-1]
            jdc.getLines()[mc.lineno-1]=s[:mc.colno]+new_name+s[mc.colno+len(mocle):]

    jdc.reset(jdc.getSource())
                
def renamemocleinfact(jdc,command,fact,mocle,new_name):
    for c in jdc.root.childNodes:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != fact:continue
            l=mc.childNodes[:]
            #on itere a l'envers
            l.reverse()
            for ll in l:
                for n in ll.childNodes:
                    if n.name != mocle:continue
                    s=jdc.getLines()[n.lineno-1]
                    jdc.getLines()[n.lineno-1]=s[:n.colno]+new_name+s[n.colno+len(mocle):]

    jdc.reset(jdc.getSource())

def renamecommande(jdc,command,new_name):
# nom de la commande "ancien format" , nom de la commande " nouveau format "
    for c in jdc.root.childNodes:
        if c.name != command:continue
        if debug:print "Renommage de:",c.name,new_name ,c.lineno,c.colno
        logging.info("Renommage de: %s, %s, %s, %s en %s",c.name,"",c.lineno,c.colno,new_name)
        s=jdc.getLines()[c.lineno-1]
        jdc.getLines()[c.lineno-1]=s[:c.colno]+new_name+s[c.colno+len(command):]

    jdc.reset(jdc.getSource())


