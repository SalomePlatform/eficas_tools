# -*- coding: utf-8 -*-

import logging
import removemocle
import inseremocle
from parseur import FactNode
debug=1

def movemoclefromfacttofather(jdc,command,fact,mocle):
# exemple type : IMPR_GENE
    for c in jdc.root.childNodes:
        if c.name != command:continue
        for mc in c.childNodes:
            if mc.name != fact:continue
            l=mc.childNodes[:]
            for ll in l:
                for n in ll.childNodes:
                    if n.name != mocle:continue
                    if debug : print "Changement de place :", n.name, n.lineno, n.colno
                    MonTexte=n.getText(jdc);
                    inseremocle.inseremotcle(jdc,c,MonTexte)
                    logging.info("Changement de place :  %s,%s, %s ",n.name, n.lineno, n.colno)
            
    removemocle.removemocleinfact(jdc,command,fact,mocle)

def movemoclefromfacttofactmulti(jdc,oper,factsource,mocle,liste_factcible):
# exemple type STAT_NON_LINE et RESI_INTER_RELA
    for factcible in liste_factcible :
       movemoclefromfacttofact(jdc,oper,factsource,mocle,factcible)
    removemocle.removemocleinfact(jdc,oper,factsource,mocle)


def movemoclefromfacttofact(jdc,oper,factsource,mocle,factcible):
    if debug : print "movemoclefromfacttofact pour " ,oper,factsource,mocle,factcible
    for c in jdc.root.childNodes:
        if c.name != oper : continue
        cible=None
        for mc in c.childNodes:
           if mc.name != factcible : 
              continue
           else :
              cible=mc
              break
        if cible==None :
           logging.info("Pas de changement pour %s,%s,%s", oper, factsource,mocle)
           logging.info("Le mot clef cible  %s n est pas présent", factcible)
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
           logging.info("Pas de changement pour %s,%s,%s", oper, factsource,mocle)
           logging.info("Le mot clef source  %s n est pas présent", factsource)
           if debug : print "Pas de changement pour ", oper, " ", factsource, " ",mocle, "source non trouvée"
           continue

        if debug : print "Changement pour ", oper, " ", factsource, " ",mocle, "cible et source trouvées"
        l=source.childNodes[:]
        for ll in l:
           for n in ll.childNodes:
              if n.name != mocle:continue
              MonTexte=n.getText(jdc);
              inseremocle.inseremotcleinfacteur(jdc,cible,MonTexte)
              logging.info("Changement de place :  %s,%s, %s ",n.name, n.lineno, n.colno)
              logging.info("vers :  %s", cible.name)

