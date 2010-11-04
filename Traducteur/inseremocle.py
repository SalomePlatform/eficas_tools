# -*- coding: utf-8 -*-
import logging
from parseur import FactNode
from dictErreurs import jdcSet
from dictErreurs import EcritErreur
import string
import regles
debug=0


#-----------------------------------
def insereMotCle(jdc,recepteur,texte):
#-----------------------------------
# appelle la methode selon la classe 
# du recepteur

    if recepteur.name  not in jdcSet : return
    if recepteur.__class__.__name__ == "Command" :
       if debug : print " Ajout de ", texte, "dans la commande : " ,recepteur.name 
       insereMotCleDansCommande(jdc,recepteur,texte)
       return


#--------------------------------------------
def insereMotCleDansCommande(jdc,command,texte):
#---------------------------------------------
# insere le texte comme 1er mot cle
# de la commande
    if command.name  not in jdcSet : return
    if debug : print "insereMotCle ", texte , " dans ", command.name
    numcol=chercheDebut1Mot(jdc,command)
    if numcol > 0 :
       jdc.splitLine(command.lineno,numcol)
    indice = -1
    while texte[indice] == " " : 
       indice = indice -1
    if texte[indice] != "," : texte=texte+","
    texteinfo=texte
    texte=texte+'\n'
    jdc.addLine(texte,command.lineno) 
    logging.info("Insertion de : %s ligne %d", texteinfo,command.lineno)
    if numcol > 0 : 		# Les mots clefs etaient sur la m�me ligne
        jdc.joinLineandNext(command.lineno)

#---------------------------------------------
def insereMotCleDansFacteur(jdc,facteur,texte):
#-------------------------------------------------
    if debug : print "insereMotCle ", texte , " dans ", facteur.name

    if texte[-1] == "\n" : texte=texte[0:-1] 
    ancien=jdc.getLine(facteur.lineno)

    # On va chercher la derniere ) pour ajouter avant
    # on va verifier s il il y a un , avant
    # si le texte ne finit pas par une ","
    # on en met une

    indice = -1
    while texte[indice] == " " : 
       indice = indice -1
    if texte[indice] != "," : 
       texte=texte+","
    if (texte.find("#") > -1) and (texte.find("#") < texte.find(",")) :
          texte=texte+"\n,"
          
    texteinfo=texte
    texte=texte+"\n"
  
    ligneaCouper=facteur.lineno
    trouve=0
    trouveF=0
    trouveP=0
    while ligneaCouper < facteur.endline + 1 :
       indiceDeCoupe=0
       while  ancien.find("_F") > 0 :
          longueur=len(ancien)
          indice=ancien.find("_F")
          indiceParcours=0
          # pour ne pas tenir compte des autres noms 
          # Attention si 2 MCF sur la meme ligne (la 1ere)
          if trouveF == 0 :
            if ((ligneaCouper!=facteur.lineno) or ((ancien.find(facteur.name) < indice ) or (ancien.find(facteur.name) < 0))) :
               trouveF=1
               indiceParcours=indice + 2
          # attention pour regler DEFI_FONCTION .. 
            else :
               indiceDeCoupe=indiceDeCoupe+indice+2
               ancien=ancien[indice +2:]
               continue

          if trouveF == 1 :
             indiceDeCoupe=indiceDeCoupe+indice
    #         print "indice de Parcours" ,indiceParcours
    #         print ancien[indiceParcours] 
    #         print ancien[indiceParcours+1] 
    #         print ancien[indiceParcours+2] 
             while  indiceParcours < longueur :
               if ancien[indiceParcours] == "(" :
                trouveP=1
    #            print "trouve"
                break
               if ancien[indiceParcours] != " " :
                trouveP=0
    #            print "mouv"
                break
               indiceParcours = indiceParcours+1
          trouve = trouveP * trouveF
          if trouve : break
          ancien=ancien[indice+1:]
          
       trouve = trouveP * trouveF
       if trouve : break
       ligneaCouper=ligneaCouper+1
       ancien=jdc.getLine(ligneaCouper)
         
    if trouve :
       debut=indiceDeCoupe + 3
       jdc.splitLine(ligneaCouper,debut)
    else :
       print "Le traducteur ne sait pas faire"
       assert 0

    # enleve les blancs en debut de texte
    i = 0
    while i < len(texte) :
      if texte[i] != " " : break
      i = i +1

    jdc.addLine(texte,ligneaCouper)
    jdc.joinLineandNext(ligneaCouper)
    logging.info("Insertion de %s ligne %d", texteinfo,ligneaCouper)
    # Gestion du cas particulier du mot clef facteur vide
    if facteur.childNodes == []:
       jdc.joinLineandNext(facteur.lineno)


#-----------------------------------
def chercheDebut1Mot(jdc,command):
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
       debut=chercheDebutFacteur(jdc,command) 
    if debut == -1 and debug : print "attention!!! pb pour trouver le debut dans ", command
    return debut

#-----------------------------------
def chercheDebutFacteur(jdc,facteur):
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

#---------------------------------------------------------------------------------------------------------
def chercheOperInsereFacteur(jdc,nomcommande,nouveau,ensemble=regles.SansRegle, estunFacteur=1, erreur=0):
#--------------------------------------------------------------------------------------------------------
# Cherche l oper
# cree le texte
# appelle insereMotCle pour ajouter le texte
#
    boolChange=0
    if estunFacteur : 
      texte=nouveau+"=_F(),"
    else :
      texte=nouveau
    if nomcommande  not in jdcSet : return
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        if c.name != nomcommande:continue
        if ensemble.verif(c) == 0 : continue
        if erreur : EcritErreur((nomcommande,nouveau),c.lineno)
        boolChange=1
        insereMotCle(jdc,c,texte)
    if boolChange : jdc.reset(jdc.getSource())

#----------------------------------------------------------------------------------------
def chercheOperInsereFacteurSiRegle(jdc,nomcommande,nouveau,liste_regles, estunFacteur=1):
#----------------------------------------------------------------------------------------
# Cherche l oper
# cree le texte
# appelle insereMotCle pour ajouter le texte
#
    if nomcommande  not in jdcSet : return
    mesRegles=regles.ensembleRegles(liste_regles)
    chercheOperInsereFacteur(jdc,nomcommande,nouveau,mesRegles,estunFacteur)
    
#---------------------------------------------------------------------------------------------------------
def chercheOperInsereFacteurSiRegleAvecAvertissement(jdc,nomcommande,nouveau,liste_regles, estunFacteur=1):
#---------------------------------------------------------------------------------------------------------
    if nomcommande  not in jdcSet : return
    mesRegles=regles.ensembleRegles(liste_regles)
    chercheOperInsereFacteur(jdc,nomcommande,nouveau,mesRegles,estunFacteur,erreur=1)

#-------------------------------------------------------------------------------------------------
def AjouteMotClefDansFacteur(jdc,commande,fact,nouveau,ensemble=regles.SansRegle, estunFacteur=0):
#-------------------------------------------------------------------------------------------------
# Cherche la commande
# Cherche le MCF
# cree le texte
# appelle insereMotCle pour ajouter le texte
#
    if commande  not in jdcSet : return
    if estunFacteur : 
      texte=nouveau+"=_F(),"
    else :
      texte=nouveau
    commands= jdc.root.childNodes[:]
    commands.reverse()
    boolChange=0
    for c in commands:
        if c.name != commande : continue
        for mcF in c.childNodes:
          if mcF.name != fact : continue
          if ensemble.verif(c) == 0 : continue
          l=mcF.childNodes[:]
          l.reverse()
          boolChange=1
          insereMotCleDansFacteur(jdc,mcF,texte)
    if boolChange : jdc.reset(jdc.getSource())

#-------------------------------------------------------------------------------------------
def AjouteMotClefDansFacteurSiRegle(jdc,commande,fact,nouveau,liste_regles,estunFacteur=0):
#-------------------------------------------------------------------------------------------
#
    if commande  not in jdcSet : return
    mesRegles=regles.ensembleRegles(liste_regles)
    AjouteMotClefDansFacteur(jdc,commande,fact,nouveau,mesRegles,estunFacteur)
