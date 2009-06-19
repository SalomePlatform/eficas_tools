# -*- coding: utf-8 -*-
import logging
import sys
from parseur import FactNode
from dictErreurs import jdcSet
import regles
from dictErreurs import EcritErreur
#debug=1
debug=0

#on n'a qu'un mocle par commande. 
#en fin de traitement, on remet à jour l'arbre syntaxique (lineno,colno,etc.)

#--------------------------------------------------------------------------------
def renameMotCle(jdc,command,mocle,new_name, erreur=0,ensemble=regles.SansRegle):
#--------------------------------------------------------------------------------
    if command not in jdcSet : return
    boolChange=0
    for c in jdc.root.childNodes:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != mocle:continue
            if ensemble.verif(c) == 0 : continue
            boolChange=1
            if debug:print "Renommage de:",c.name,mc.name,mc.lineno,mc.colno
            if erreur :
               EcritErreur((command,mocle),c.lineno)
            else :
               logging.info("Renommage de: %s  %s ligne %d en %s",c.name,mc.name,mc.lineno,new_name)
            s=jdc.getLines()[mc.lineno-1]
            jdc.getLines()[mc.lineno-1]=s[:mc.colno]+new_name+s[mc.colno+len(mocle):]
            diff=len(new_name) - len(mocle)
            decaleLignesdeNBlancs(jdc,mc.lineno,mc.endline-1,diff)

    if boolChange : jdc.reset(jdc.getSource())
                
#------------------------------------------------------
def renameMotCleAvecErreur(jdc,command,mocle,new_name):
#------------------------------------------------------
    if command not in jdcSet : return
    renameMotCle(jdc,command,mocle,new_name,1,regles.SansRegle)

#--------------------------------------------------------------------------
def renameMotCleSiRegle(jdc,command,mocle,new_name,liste_regles, erreur=0):
#--------------------------------------------------------------------------
    if command not in jdcSet : return
    mesRegles=regles.ensembleRegles(liste_regles)
    renameMotCle(jdc,command,mocle,new_name, erreur,mesRegles)

#-------------------------------------------
def renameOper(jdc,command,new_name):
#-------------------------------------------
    if command not in jdcSet : return
    jdcSet.add(new_name)
    boolChange=0
    for c in jdc.root.childNodes:
        if c.name != command:continue
        if debug:print "Renommage de:",c.name,c.lineno,c.colno
        logging.info("Renommage de: %s ligne %d en %s",c.name,c.lineno,new_name)
        boolChange=1
        s=jdc.getLines()[c.lineno-1]
        jdc.getLines()[c.lineno-1]=s[:c.colno]+new_name+s[c.colno+len(command):]
        diff=len(new_name) - len(command)
        decaleLignesdeNBlancs(jdc,c.lineno,c.endline,diff)
    if boolChange : jdc.reset(jdc.getSource())

#----------------------------------------------------------
def decaleLignesdeNBlancs(jdc,premiere,derniere,nbBlanc):
#----------------------------------------------------------
    ligne = premiere + 1
    while ligne < derniere :
       s=jdc.getLines()[ligne]
       if nbBlanc > 0 :
         jdc.getLines()[ligne] = nbBlanc*" " + s
       else :
         toutblancs=-1*nbBlanc*" "
         if jdc.getLines()[ligne][0:-1*nbBlanc] == toutblancs: 
            jdc.getLines()[ligne] = s[-1*nbBlanc:]
       ligne=ligne+1

#---------------------------------------------------------------------------------------------
def renameMotCleInFact(jdc,command,fact,mocle,new_name, ensemble=regles.SansRegle, erreur=0):
#---------------------------------------------------------------------------------------------
    if command not in jdcSet : return
    boolChange=0
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
                    if ensemble.verif(c) == 0 : continue
                    s=jdc.getLines()[n.lineno-1]
                    jdc.getLines()[n.lineno-1]=s[:n.colno]+new_name+s[n.colno+len(mocle):]
                    boolChange=1
                    if erreur :
                       EcritErreur((command,fact,mocle),c.lineno)
                    else :
                       logging.info("Renommage de: %s, ligne %s, en %s",n.name,n.lineno,new_name)

    if boolChange : jdc.reset(jdc.getSource())

#--------------------------------------------------------------------------
def renameMotCleInFactSiRegle(jdc,command,fact,mocle,new_name,liste_regles):
#--------------------------------------------------------------------------
    if command not in jdcSet : return
    mesRegles=regles.ensembleRegles(liste_regles)
    renameMotCleInFact(jdc,command,fact,mocle,new_name,mesRegles)

#-----------------------------------------------------------------
def renameCommande(jdc,command,new_name,ensemble=regles.SansRegle):
#-----------------------------------------------------------------
# nom de la commande "ancien format" , nom de la commande " nouveau format "
    if command not in jdcSet : return
    jdcSet.add(new_name)
    boolChange=0
    if debug :
        if ensemble != regles.SansRegle :
          logging.info("Traitement de %s renomme en %s sous conditions", command, new_name)
        else  :
          logging.info("Traitement de %s renomme en %s ", command, new_name)
    for c in jdc.root.childNodes:
        if c.name != command:continue
        if ensemble.verif(c) == 0 : continue
        boolChange=1
        if debug:print "Renommage de:",c.name,new_name ,c.lineno,c.colno
        logging.info("Renommage de: %s ligne %d en %s",c.name,c.lineno,new_name)
        s=jdc.getLines()[c.lineno-1]
        jdc.getLines()[c.lineno-1]=s[:c.colno]+new_name+s[c.colno+len(command):]

    if boolChange : jdc.reset(jdc.getSource())

#-----------------------------------------------------------
def renameCommandeSiRegle(jdc,command,new_name,liste_regles):
#-----------------------------------------------------------
    
    if command not in jdcSet : return
    mesRegles=regles.ensembleRegles(liste_regles)
    renameCommande(jdc,command,new_name,mesRegles)

