# -*- coding: utf-8 -*-

import logging
import removemocle
import inseremocle
from parseur import FactNode
from dictErreurs import jdcSet
debug=0

#-----------------------------------------------------
def moveMotCleFromFactToFather(jdc,command,fact,mocle):
#-----------------------------------------------------
# exemple type : IMPR_GENE

    if command not in jdcSet : return
    boolChange=0
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != fact:continue
            l=mc.childNodes[:]
            for ll in l:
                for n in ll.childNodes:
                    if n.name != mocle:continue
                    if debug : print "Changement de place :", n.name, n.lineno, n.colno
                    MonTexte=n.getText(jdc);
                    boolChange=1
                    inseremocle.insereMotCle(jdc,c,MonTexte)
                    logging.info("Changement de place  %s ligne %s ",n.name, n.lineno)
            
    if boolChange : jdc.reset(jdc.getSource())
    removemocle.removeMotCleInFact(jdc,command,fact,mocle)


#----------------------------------------------------------------------------
def moveMotCleFromFactToFactMulti(jdc,oper,factsource,mocle,liste_factcible):
#----------------------------------------------------------------------------
# exemple type STAT_NON_LINE et RESI_INTER_RELA
    for factcible in liste_factcible :
       moveMotCleFromFactToFact(jdc,oper,factsource,mocle,factcible)
    removemocle.removeMotCleInFact(jdc,oper,factsource,mocle)


#----------------------------------------------------------------------------
def moveMotCleFromFactToFact(jdc,oper,factsource,mocle,factcible):
#----------------------------------------------------------------------------
    if oper not in jdcSet : return
    if debug : print "moveMotCleFromFactToFact pour " ,oper,factsource,mocle,factcible
    boolChange=0
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        if c.name != oper : continue
        cible=None
        for mc in c.childNodes:
           if mc.name != factcible : 
              continue
           else :
              cible=mc
              break
        if cible==None :
           if debug : print "Pas de changement pour ", oper, " ", factsource, " ",mocle, "cible non trouvée"
           continue

        for mc in c.childNodes:
           source=None
           if mc.name != factsource:
              continue
           else :
              source=mc
              break
        if source==None :
           if debug : print "Pas de changement pour ", oper, " ", factsource, " ",mocle, "source non trouvée"
           continue

        if debug : print "Changement pour ", oper, " ", factsource, " ",mocle, "cible et source trouvées"
        l=source.childNodes[:]
        for ll in l:
           for n in ll.childNodes:
              if n.name != mocle:continue
              MonTexte=n.getText(jdc);
              inseremocle.insereMotCleDansFacteur(jdc,cible,MonTexte)
              boolChange=1
              logging.info("Changement de place   %s ligne %s vers %s",n.name, n.lineno, cible.name)
    if boolChange : jdc.reset(jdc.getSource())




#------------------------------------------------------
def moveMotClefInOperToFact(jdc,oper,mocle,factcible):
#------------------------------------------------------
# Attention le cas type est THETA_OLD dans calc_G

    if oper not in jdcSet : return
    if debug : print "movemocleinoper pour " ,oper,mocle,factcible
    boolChange=9
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        if c.name != oper : continue
        cible=None
        for mc in c.childNodes:
           if mc.name != factcible : 
              continue
           else :
              cible=mc
              break
        if cible==None :
           if debug : print "Pas de changement pour ", oper, " ", factcible, " ", "cible non trouvée"
           continue

        source=None
        for mc in c.childNodes:
           if mc.name != mocle:
              continue
           else :
              source=mc
              break
        if source==None :
           if debug : print "Pas de changement pour ", oper, " ", mocle, " source non trouvée"
           continue
        MonTexte=source.getText(jdc);
        boolChange=1
        inseremocle.insereMotCleDansFacteur(jdc,cible,MonTexte)
    if boolChange : jdc.reset(jdc.getSource())
    removemocle.removeMotCle(jdc,oper,mocle)
