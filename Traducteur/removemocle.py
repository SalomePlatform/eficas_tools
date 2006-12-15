# -*- coding: utf-8 -*-
import logging
import regles
from parseur import FactNode
from dictErreurs import EcritErreur
from dictErreurs import jdcSet

#debug=1
debug=0
#on n'a qu'un mocle par commande. On peut donc supprimer le mocle sans trop de pr�cautions (a part iterer a l'envers sur les commandes)
#avant de supprimer un autre mocle, on remet � jour l'arbre syntaxique (lineno,colno,etc.)


#-----------------------------------------------------------------------
def removeMotCle(jdc,command,mocle,ensemble=regles.SansRegle,erreur = 0):
#-----------------------------------------------------------------------
    #on itere sur les commandes a l'envers pour ne pas polluer les numeros de ligne avec les modifications
    if command not in jdcSet : return
    boolChange=0
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != mocle:continue
            if ensemble.verif(c) == 0 : continue
            if erreur : EcritErreur((command,mocle),c.lineno)
            boolChange=1
            removeMC(jdc,c,mc)

    if boolChange : jdc.reset(jdc.getSource())

#-------------------------------------------------------
def removeMotCleSiRegle(jdc,command,mocle,liste_regles) :
#-------------------------------------------------------
    if command not in jdcSet : return
    mesRegles=regles.ensembleRegles(liste_regles)
    removeMotCle(jdc,command,mocle,mesRegles,erreur=0)

#----------------------------------------------------------------
def removeMotCleSiRegleAvecErreur(jdc,command,mocle,liste_regles) :
#--------------------------------------------------------------
    if command not in jdcSet : return
    mesRegles=regles.ensembleRegles(liste_regles)
    removeMotCle(jdc,command,mocle,mesRegles,erreur=1)

#----------------------------------------------------------------
def removeMotCleAvecErreur(jdc,command,mocle) :
#--------------------------------------------------------------
    if command not in jdcSet : return
    removeMotCle(jdc,command,mocle,erreur=1)
      

#--------------------------------------------------------------------
def removeCommande(jdc,command,ensemble=regles.SansRegle,erreur=0):
#--------------------------------------------------------------------
    if command not in jdcSet : return
    boolChange=0
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        if c.name != command:continue
        if ensemble.verif(c) == 0 : continue
        boolChange=1
        if erreur : EcritErreur((command,),c.lineno)
        jdc.supLignes(c.lineno,c.endline)
        logging.warning("Suppression de: %s ligne %s",c.name,c.lineno)
    if boolChange : jdc.reset(jdc.getSource())

#-------------------------------------------------------------
def removeCommandeSiRegleAvecErreur(jdc,command,liste_regles):
#-------------------------------------------------------------
    if command not in jdcSet : return
    mesRegles=regles.ensembleRegles(liste_regles)
    removeCommande(jdc,command,mesRegles,1)
                
#---------------------------------
def removeMC(jdc,c,mc):
#---------------------------------
    if debug : print "Suppression de:",c.name,mc.name,mc.lineno,mc.colno,mc.endline,mc.endcol
    logging.info("Suppression de: %s, %s, ligne %d",c.name,mc.name,mc.lineno)

    if mc.endline > mc.lineno:
        if debug:print "mocle sur plusieurs lignes--%s--" % jdc.getLines()[mc.lineno-1][mc.colno:]
        jdc.getLines()[mc.lineno-1]=jdc.getLines()[mc.lineno-1][:mc.colno]
        jdc.getLines()[mc.endline-1]=jdc.getLines()[mc.endline-1][mc.endcol:]

        #attention : supprimer les lignes � la fin
        jdc.getLines()[mc.lineno:mc.endline-1]=[]
    else:
        if debug:print "mocle sur une ligne--%s--" % jdc.getLines()[mc.lineno-1][mc.colno:mc.endcol]
        s=jdc.getLines()[mc.lineno-1]
        jdc.getLines()[mc.lineno-1]=s[:mc.colno]+s[mc.endcol:]
        fusionne(jdc,mc.lineno-1)

#---------------------------------------------------------------------------------
def removeMotCleInFact(jdc,command,fact,mocle,ensemble=regles.SansRegle,erreur=0):
#----------------------------------------------------------------------------------
    # on itere sur les commandes a l'envers pour ne pas polluer 
    # les numeros de ligne avec les modifications
    if command not in jdcSet : return
    commands= jdc.root.childNodes[:]
    commands.reverse()
    boolChange=0
    for c in commands:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != fact:continue
            l=mc.childNodes[:]
            l.reverse()
            for ll in l:
                for n in ll.childNodes:
                    if n.name != mocle:continue
                    if ensemble.verif(c) == 0 : continue
                    if erreur : EcritErreur((command,fact,mocle),c.lineno)
                    boolChange=1
                    removeMC(jdc,c,n)

    if boolChange : jdc.reset(jdc.getSource())

#------------------------------------------------------------------
def removeMotCleInFactSiRegle(jdc,command,fact,mocle,liste_regles):
#------------------------------------------------------------------
    if command not in jdcSet : return
    erreur=0
    mesRegles=regles.ensembleRegles(liste_regles)
    removeMotCleInFact(jdc,command,fact,mocle,mesRegles,erreur)

#----------------------------------------------------------------------
def removeMotCleInFactSiRegleAvecErreur(jdc,command,fact,mocle,liste_regles):
#----------------------------------------------------------------------
    if command not in jdcSet : return
    erreur=1
    mesRegles=regles.ensembleRegles(liste_regles)
    removeMotCleInFact(jdc,command,fact,mocle,mesRegles,erreur)


#------------------------------------------
def fusionne(jdc,numLigne):
#------------------------------------------
#   fusionne la ligne numLigne et numLigne+1
#   si la ligne numLigne+1 ne contient que des parentheses
#   fermantes
#   et si la ligne  numLigne ne contient pas par un "#"
#   Attention a la difference de numerotation
#        jdc.getLines()[numLigne] donne la ligne numLigne + 1
#        alors que joinLineandNext(numLigne) travaille sur le tableau
    index=0
    texte=jdc.getLines()[numLigne]
    fusion=1
    while (index < len(texte)) :
      if texte[index] not in (" ",",",")",";","\n") :
         fusion=0
         break
      index=index+1
       
    if fusion == 0 : return;

    texte=jdc.getLines()[numLigne -1]
    if texte.find("#") < 0 :
       fusion=1
    else :
       fusion=0
 
    if fusion : 
       import load 
       jdc.joinLineandNext(numLigne)
