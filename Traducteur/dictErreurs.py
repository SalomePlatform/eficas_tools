# -*- coding: utf-8 -*-

import logging
import sets

jdcSet=sets.Set()


def EcritErreur(listeGena,ligne=None) :
    from sys import dict_erreurs
    maCle=""
    for Mot in listeGena :
        maCle=maCle+"_"+Mot
    #try :
    if ( 1 == 1) :
	maClef=maCle[1:]
        if maClef in dict_erreurs.keys() :
           if ligne != None :
	      logging.warning("ligne %d : %s ",ligne,dict_erreurs[maClef])
           else :
	      logging.warning("%s",dict_erreurs[maClef])
        else :
           maCle=""
           for Mot in listeGena[:-1] :
              maCle=maCle+"_"+Mot
	   maClef=maCle[1:]
	   maClef=maCle+"_"+"VALEUR"
           if maClef in dict_erreurs.keys() :
              if ligne != None :
	          logging.warning("ligne %d : %s ",ligne,dict_erreurs[maClef])
              else :
	          logging.warning("%s",dict_erreurs[maClef])
    #except :
    #    pass

def GenereErreurPourCommande(jdc,listeCommande) :
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        jdcSet.add(c.name) 
        for Mot in listeCommande :
           if c.name != Mot :continue
           EcritErreur((Mot,),c.lineno)

def GenereErreurMotCleInFact(jdc,command,fact,mocle):
    for c in jdc.root.childNodes:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != fact:continue
            l=mc.childNodes[:]
            for ll in l:
                for n in ll.childNodes:
                    if n.name != mocle:
                       continue
 		    else :
                       EcritErreur((command,fact,mocle,),c.lineno)

def GenereErreurMCF(jdc,command,fact):
    for c in jdc.root.childNodes:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != fact:
                continue
            else : 
                EcritErreur((command,fact,),c.lineno)

def GenereErreurValeur(jdc,command,fact,list_valeur):
    for c in jdc.root.childNodes:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != fact:continue
            texte=mc.getText(jdc)
            for valeur in list_valeur:
               trouve=texte.find(valeur)
               if trouve > -1 :  
                  logging.warning("%s doit etre supprimee ou modifiee dans %s : ligne %d",valeur,c.name,mc.lineno)

def GenereErreurValeurDsMCF(jdc,command,fact,mocle,list_valeur):
    for c in jdc.root.childNodes:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != fact:continue
            l=mc.childNodes[:]
            for ll in l:
                for n in ll.childNodes:
                    if n.name != mocle:continue
                    texte=n.getText(jdc)
                    for valeur in list_valeur:
                        trouve=texte.find(valeur)
                        if trouve > -1 :  
                           logging.warning("%s doit etre supprimee ou modifiee dans %s : ligne %d",valeur,c.name,n.lineno)
