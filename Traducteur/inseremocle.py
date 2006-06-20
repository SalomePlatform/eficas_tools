# -*- coding: utf-8 -*-
import logging
from parseur import FactNode
import string
debug=1


#-----------------------------------
def inseremotcle(jdc,recepteur,texte):
#-----------------------------------
# appelle la methode selon la classe 
# du recepteur

    if recepteur.__class__.__name__ == "Command" :
       if debug : print " Ajout de ", texte, "dans la commande : " ,recepteur.name 
       inseremotcleincommand(jdc,recepteur,texte)
       return


#--------------------------------------------
def inseremotcleincommand(jdc,command,texte):
#---------------------------------------------
# insere le texte comme 1er mot cle
# de la commande
    if debug : print "inseremotcle ", texte , " dans ", command.name
    numcol=chercheDebut1mot(jdc,command)
    if numcol > 0 :
       jdc.splitLine(command.lineno,numcol)
    debut=chercheAlignement(jdc,command)
    texte=debut+texte+"\n"
    jdc.addLine(texte,command.lineno) 
    if numcol > 0 : 		# Les mots clefs etaient sur la même ligne
        jdc.joinLineandNext(command.lineno)

#---------------------------------------------
def inseremotcleinfacteur(jdc,facteur,texte):
#-------------------------------------------------
    if debug : print "inseremotcle ", texte , " dans ", facteur.name
    ancien=jdc.getLine(facteur.lineno )
    # On va chercher la dernier ) pour ajouter avant
    # on va verifier s il il y a un , avant
    ligne,col,boolvirgule=chercheDerniereParenthese(jdc,facteur)
    if col > 0 :
       jdc.splitLine(ligne,col)
    if boolvirgule == 0 :
       jdc.addLine(",\n",ligne)
       jdc.joinLineandNext(ligne)
    debut=ancien.find("_F") + 3
    aligne=debut*" "
    # enleve les blancs en debut de texte
    i = 0
    while i < len(texte) :
      if texte[i] != " " : break
      i = i +1
    texte=aligne+texte+"\n"
    jdc.addLine(texte,ligne)
    jdc.joinLineandNext(ligne+1)

#---------------------------------------
def chercheDerniereParenthese(jdc,facteur):
#---------------------------------------
    ligne=facteur.endline-1
    col=-1
    boolvirgule=0
    trouveParent=0
    while ( trouveParent == 0) :
       texte=jdc.getLine(ligne)
       col=texte.rfind(")")
       if col < 0 :
          ligne=ligne-1
       else :
          trouveParent=1
    indice=col -1
    while ( indice > -1 and texte[indice] == " " ):
          indice = indice -1
    if texte[indice]=="," :
       boolvirgule = 1
    return (ligne,col,boolvirgule)

#-----------------------------------
def chercheDebut1mot(jdc,command):
#-----------------------------------
# Retourne le numero de colonne si le 1er mot clef est 
# sur la meme ligne que le mot clef facteur
# -1 sinon
    assert (command.childNodes != [])
    debut=-1
    node1=command.childNodes[0]
    if hasattr(node1,"lineno"):
       if node1.lineno == command.lineno :
          debut=node1.colno
    else:
       debut=chercheDebutfacteur(jdc,command) 
    if debut == -1 and debug : print "attention!!! pb pour trouver le debut dans ", command
    return debut

#-----------------------------------
def chercheDebutfacteur(jdc,facteur):
#-----------------------------------
    debut=-1
    ligne=jdc.getLines()[facteur.lineno]
    debut=ligne.find("_F")
    if debut >  -1 : debut=debut + 3
    return debut
    


#-----------------------------------
def chercheAlignement(jdc,command):
#-----------------------------------
# Retourne le nb de blanc
# pour aligner sur le 1er mot clef fils
    assert (command.childNodes != []) 
    node1=command.childNodes[0]
    nbBlanc=node1.colno
    return " "*nbBlanc


