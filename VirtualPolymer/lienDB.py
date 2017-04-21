# coding: utf-8
import types
import sys,os

import listesDB


maClasseDelistesDB = listesDB.classeListesDB()
monModele=listesDB.sModele().monModele


# --------------------------------------
# Fonctions appellees depuis le catalogue
# --------------------------------------
 
# --------------------------------------
# Dans Equation
# --------------------------------------

def recupereDicoEquation(monMC):
    # Equation_reaction (ds 2 blocs)
    #  ou dans Equation b_type_show b_reaction_type
    #  ou dans Equation b_type_show b_aging_type

    if hasattr(monMC,'dsMaFunct') and monMC.dsMaFunct== True : return
    editor=monMC.jdc.editor

    valeurDB=editor.getValeur('Equation','Equation_DB',())
    maClasseDelistesDB.metAJour(valeurDB)
    listEquation=maClasseDelistesDB.getListEquation()

    valeurEquationListe=editor.getValeur('Equation','Equation_Liste',('b_type_show',))
    valeurAgingType=editor.getValeur('Equation','Equation_reaction',('b_type_show','b_reaction_type',))
    if valeurAgingType == None :
       valeurAgingType=editor.getValeur('Equation','Equation_reaction',('b_type_show','b_aging_type',))
    if valeurAgingType == None : monMC.dsMaFunct = False; return

    listeEquationPourIhm = []
    listeReprEquationPourIhm = []
    dicoListAffiche = {}
   
    for equation in listEquation :
        if valeurEquationListe == 'aging_type' :
           if equation.type_vieil == valeurAgingType : 
              listeEquationPourIhm.append(equation)
              listeReprEquationPourIhm.append(equation.representation)
              dicoListAffiche[equation.representation]=equation
        else:
           if equation.type_react == valeurAgingType : 
              listeEquationPourIhm.append(equation)
              listeReprEquationPourIhm.append(equation.representation)
              dicoListAffiche[equation.representation]=equation
    maClasseDelistesDB.dicoListAffiche = dicoListAffiche

    change=editor.changeIntoDefMC('Equation', ('b_type_show','ListeEquation'), listeReprEquationPourIhm )
    if change :
       editor.reCalculeValiditeMCApresChgtInto('Equation', 'listeEquation', ('b_type_show',)) 
       if editor.fenetreCentraleAffichee : editor.fenetreCentraleAffichee.node.affichePanneau()
    monMC.dsMaFunct = False

def afficheValeurEquation(monMC):
    # Equation b_modification modification
    if hasattr(monMC,'dsMaFunct') and monMC.dsMaFunct== True : return
    valeur=monMC.valeur
    if valeur == None : return
    maClasseDelistesDB.valeurEquationChoisie=str(valeur)
    monEquation=maClasseDelistesDB.dicoListAffiche[str(valeur)]

    aAfficher='jkljkljk \n je ne sais plus \njfkqsljqfkl\nkfsjqklfjkl\n'
    editor=monMC.jdc.editor
    editor._viewText(aAfficher, "Rapport",largeur=30,hauteur=150)
    
    monMC.dsMaFunct = False
              

def instancieChemicalFormulation(monMC):
    if hasattr(monMC,'dsMaFunct') and monMC.dsMaFunct== True : return
    if monMC.valeur == False : return

    editor=monMC.jdc.editor
    if hasattr(editor,'dsMaFunct') and editor.dsMaFunct== True : return
    editor.dsMaFunct = True

    print ('ds instancie')
    v=maClasseDelistesDB.valeurEquationChoisie
    monEquation=maClasseDelistesDB.dicoListAffiche[v]
    type_react=monEquation.type_react
    type_vieil=monEquation.type_vieil

    editor.changeIntoMCandSet('Equation', ('b_type_show','b_modification','b_modif','ChemicalFormulation'),( v,),v )
    return
    #change=editor.changeDefautDefMC('Equation', ('b_type_show','b_modification','b_modif','Reaction_Type'),type_react )
    change=editor.changeDefautDefMC('Equation', ('b_type_show','b_modification','b_modif','Aging_Type'), type_vieil )

    for index,valeurConstituant in enumerate(monEquation.constituants):
        valeurEquation=monEquation.equation[index] 
        editor.ajoutMC(monMC.etape,'OptionnelConstituant',None,('b_type_show','b_modification','b_modif',))
        print (index,valeurConstituant,valeurEquation)

            #OptionnelConstituant =  FACT ( statut = 'f',max = '**',
            #    Constituant = SIMP (statut = 'o', typ = 'TXM'),
            #    Differential_Equation =  SIMP(statut= 'o',typ= 'TXM'),

    for index,valeurConstituant in enumerate(monEquation.const_cine_nom):
         valeurArrhe=monEquation.arrhenius[index] 
         if valeurArrhe : valeurConstanteType='Arrhenius type'
         else           : valeurConstanteType='non Arrhenius type'
         print (index,valeurConstituant,valeurConstanteType)
            #OptionnelleConstante  = FACT (statut = 'f', max = '**',
            #     ConstanteName= SIMP (statut = 'o', typ = 'TXM',),
            #    ConstanteType =  SIMP(statut= 'o',typ= 'TXM', min=1,into=('Arrhenius type','non Arrhenius type'),defaut='Arrhenius type'),

    change=editor.changeDefautDefMC('Equation', ('b_type_show','b_modification','b_modif','Commentaire'),monEquation.comment )
    print (monEquation.comment )
    if editor.fenetreCentraleAffichee : editor.fenetreCentraleAffichee.node.affichePanneau()

    monMC.dsMaFunct = False
    editor.dsMaFunct = False
 
# TEMPORAIRE 
# TODO TODO TODO
# PNPNPNPNPN



def recupereDicoModele(monMC):
    if monMC.valeur == None: return
    if hasattr(monMC,'dsMaFunct') and monMC.dsMaFunct== True : return
    print ('je passe dans recupereDicoModele')
    listEquation, listModele,listPostTraitement=recupereDicoGenerique(monMC)
    editor=monMC.jdc.editor
    editor.maClasseVisuEquation = classeVisuEquation({},listEquation, listModele,listPostTraitement)
    monMC.dsMaFunct = False


def creeListeEquation(monMC):
    if monMC.valeur == None: return
    if hasattr(monMC,'dsMaFunct') and monMC.dsMaFunct== True : return

    editor=monMC.jdc.editor
# TEMPORAIRE 
# TODO TODO TODO
    listeEquationsAAfficher=[]
    listeConstantesAAfficher=[]
    for index,equation in enumerate( editor.maClasseVisuEquation.listEquation):
        if index in monModele.equa:
            listeEquationsAAfficher.append(equation.representation)
            listeConstantesAAfficher.append(equation.const_cine_nom)

    monMC.dsMaFunct = False

  #        listeEquation_stabilization=SIMP(statut='o', homo='SansOrdreNiDoublon', max='**', min=0 ),

def recupereModeleEquation(monMC):
    if hasattr(monMC,'dsMaFunct') and monMC.dsMaFunct== True : return
    if monMC.valeur==False : return
    editor=monMC.jdc.editor
    if hasattr(editor,'dsMaFunct') and editor.dsMaFunct== True : return

    editor.dsMaFunct = True
    dicoListeEquationAAfficher={}

    for valeurReactionType in monDico['Equation_Liste']:
      dicoListeEquationAAfficher[valeurReactionType] = [] 
      for index,equation in enumerate( editor.maClasseVisuEquation.listEquation):
        if equation.type_react==valeurReactionType : 
           dicoListeEquationAAfficher[valeurReactionType].append(equation.representation)
    print (dicoListeEquationAAfficher)
       
    change=editor.changeIntoDefMC('Modele', ('b_type_creation','b_ajout_equation','listeEquation_initiation'),dicoListeEquationAAfficher['initiation'] )
    change=editor.changeIntoDefMC('Modele', ('b_type_creation','b_ajout_equation','listeEquation_propagation'),dicoListeEquationAAfficher['propagation'] )
    change=editor.changeIntoDefMC('Modele', ('b_type_creation','b_ajout_equation','listeEquation_termination'),dicoListeEquationAAfficher['termination'] )
    change=editor.changeIntoDefMC('Modele', ('b_type_creation','b_ajout_equation','listeEquation_stabilization'),dicoListeEquationAAfficher['stabilization'] )
    if editor.fenetreCentraleAffichee : editor.fenetreCentraleAffichee.node.affichePanneau()
    editor.dsMaFunct = False

def prepareDiffusion(monMC):
    print ('je suis dans prepareDiffusion')
    if monMC.valeur==False : return
    if hasattr(monMC,'dsMaFunct') and monMC.dsMaFunct== True : return
    monMC.dsMaFunct=True
    editor=monMC.jdc.editor
    if hasattr(editor,'dsMaFunct') and editor.dsMaFunct== True : return
    editor.dsMaFunct = True
    editor.dicoCoefS={}
    editor.dicoCoefD={}
    for c in monModele.coef[0].keys() :
        if c[0]=='S':
           clef=c[1:]
           valeur= monModele.coef[0][c]
           editor.dicoCoefS[clef]=valeur
        if c[0]=='D':
           clef=c[1:]
           valeur= monModele.coef[0][c]
           editor.dicoCoefD[clef]=valeur
    print (editor.dicoCoefS,editor.dicoCoefD)
    monMC.dsMaFunct=False
    editor.dsMaFunct = False


def ajouteDiffusion(monMC):
    print ('je suis dans ajouteDiffusion')
    if monMC.valeur == None : return
    print (monMC.valeur)
    if hasattr(monMC,'dsMaFunct') and monMC.dsMaFunct== True : return
    monMC.dsMaFunct=True
    editor=monMC.jdc.editor
    if hasattr(editor,'dsMaFunct') and editor.dsMaFunct== True : return
    editor.dsMaFunct = True


    for v in monMC.valeur :
        print (v)
        mesValeurs=editor.dicoCoefS[v]
        print (editor.dicoCoefS)
        print (mesValeurs) 
        MCFils='S'+v
        for e in monMC.jdc.etapes:
            if e.nom == Modele :break

        print (e)
        editor.ajoutDefinitionMC(e,('b_type_creation','b_diffusion'),MCFils,typ='TXM',statut='o' )
        print ('ggggg')
        editor.ajoutMC(e,MCFils,mesValeurs,('b_type_creation','b_diffusion',))
        print ('______')
    if editor.fenetreCentraleAffichee : editor.fenetreCentraleAffichee.node.affichePanneau()
    monMC.dsMaFunct=False
    editor.dsMaFunct = False

