#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#


import sys,os
import types
import Accas
import imp
from copy import deepcopy, copy
import traceback

# CONTEXT est accessible (__init__.py de Noyau)

#import raw.efficas as efficas
sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))

# ds l init du SIMP il manque siValide et fenetreIhm

from .mapDesTypes import dictSIMPEficasXML, dictSIMPXMLEficas
from .mapDesTypes import dictFACTEficasXML, dictFACTXMLEficas
from .mapDesTypes import dictPROCEficasXML, dictPROCXMLEficas
from .mapDesTypes import dictOPEREficasXML, dictOPERXMLEficas
from .mapDesTypes import dictBLOCEficasXML, dictBLOCXMLEficas
from .mapDesTypes import dictPourCast, dictNomsDesTypes
from .mapDesTypes import listeParamDeTypeTypeAttendu, listeParamDeTypeStr, dictPourCast
from .mapDesTypes import listeParamTjsSequence, listeParamSelonType
from .mapDesTypes import Tuple

PourTraduction = False

from .balisesXSD import *

# -----------------
class X_definition:
# -----------------
    def adjoint(self, liste1, liste2):
        #print ('adjoint', liste1, liste2)
        l=[]
        for elt1 in liste1:
            for elt2 in liste2:
                newListe=deepcopy(elt1)
                if  elt2 != []: newListe.append(elt2)
                l.append(newListe)
        return l

    def adjointUnMot(self, liste1, mot):
        l=[]
        for elt1 in liste1:
            newListe=deepcopy(elt1)
            newListe.append(mot)
            l.append(newListe)
        return l

    def remplaceListeParContenuEtVide(self, liste1, liste2):
        listeFinale=[]
        for elt1 in liste1 :
            for eltListe in liste2:
                newListe=deepcopy(elt1)
                if eltListe!=[] :newListe+=eltListe
                if newListe not in listeFinale : listeFinale.append(newListe)
        return listeFinale


    def fusionne2Listes(self, liste1, liste2):
        #print ('fusionne2Liste', liste1, liste2)
        listeFinale=[]
        for elt1 in liste1 :
            for eltListe in liste2:
                newListe=deepcopy(elt1)
                if eltListe!=[] :newListe.append(eltListe)
                listeFinale.append(newListe)
        #print (listeFinale)
        return listeFinale

    def getNomDuCodeDumpe(self):
        if hasattr(self,'nomDuCodeDumpe') : return
        obj=self
        while ( not hasattr(obj,'nomDuCodeDumpe') ): obj=obj.pere
        self.nomDuCodeDumpe = obj.nomDuCodeDumpe
        self.code=obj.code

    def getXPathComplet(self):
        obj=self
        textePath='/'+self.code+":"+self.nom
        while ( hasattr(obj,'pere') ):
            obj=obj.pere
            if isinstance(obj, X_BLOC) : continue
            textePath= '/'+ self.code + ":" + obj.nom + textePath
        textePath='.' + textePath
        return textePath

    def getXPathSansSelf(self):
        obj=self
        textePath=''
        while ( hasattr(obj,'pere') ):
            obj=obj.pere
            if isinstance(obj, X_BLOC) : continue
            textePath=  self.code + ":" + obj.nom + '/' + textePath
        textePath='./'+ self.code + ":" + textePath
        return textePath

    def getNomCompletAvecBloc(self):
        obj=self
        texteNom=self.nom
        while ( hasattr(obj,'pere') ):
            texteNom=obj.pere.nom+'_'+texteNom
            obj=obj.pere
        return texteNom

    def metAJourPyxb(self,nomDuTypePyxb) :
        self.aCreer=False
        self.nomDuTypePyxb=nomDuTypePyxb
        cata = CONTEXT.getCurrentCata()
        nom='T_'+self.nom
        if (hasattr (self, 'nomXML')) and self.nomXML != None : nom='T_'+self.nomXML
        if not (nom in cata.dictTypesXSD.keys()) :
            cata.dictTypesXSD[nom] = [self,]
        else :
            cata.dictTypesXSD[nom].append(self)

    def definitNomDuTypePyxb(self,forceACreer=False,debug=False):
        #if self.nom == 'SubgridScaleModel' : debug=True
        #print ('definitNomDuTypePyxb', self, self.nom,self.nomComplet(),forceACreer)
        #PNPN
        if hasattr(self,'nomDuTypePyxb') : self.aCreer = False; return self.nomDuTypePyxb
        #debug=False
        if debug : print ('definitNomDuTypePyxb traitement pour ',  self.nom)
        self.aCreer = True
        cata = CONTEXT.getCurrentCata()
        nom='T_'+self.nom
        if (hasattr (self, 'nomXML')) and self.nomXML != None : nom='T_'+self.nomXML
        if not (nom in cata.dictTypesXSD.keys()) :
            if debug : print ('definitNomDuTypePyxb encore jamais traite ',  self.nom , ' a pour type' , nom)
            cata.dictTypesXSD[nom] = [self,]
            self.nomDuTypePyxb=nom
            return nom

        if nom == 'T_Consigne' : return nom

        if not forceACreer :
            self.aCreer = False
            listePossible=cata.dictTypesXSD[nom]
            indice=0
            while (indice < len(listePossible)) :
                objAComparer=listePossible[indice]
                if debug : print (self.compare)
                if self.compare(objAComparer) :
                    self.nomDuTypePyxb=objAComparer.nomDuTypePyxb
                    if debug : print (self, objAComparer)
                    if debug : print (type(self), type(objAComparer))
                    if debug : print ('definitNomDuTypePyxb',  self.nom , 'type identique', objAComparer.nomDuTypePyxb )
                # c est nul pour la comparaison mais cela permet d etre ok dans le dictionnaire passe a Accas
                    cata.dictTypesXSD[nom].append(self)
                    if self.label != 'SIMP' :
                        if objAComparer not in list(cata.dictTypesXSDJumeaux.keys()) : cata.dictTypesXSDJumeaux[objAComparer]=[self,]
                        else : cata.dictTypesXSDJumeaux[objAComparer].append(self)
                    return objAComparer.nomDuTypePyxb
                indice += 1
        self.aCreer = True
        cata.dictTypesXSD[nom].append(self)
        nomAlter='T_'+self.nom+'_'+str(indice)
        if (hasattr (self, 'nomXML')) and self.nomXML != None :
            nomAlter='T_'+self.nomXML+'_'+str(indice)
        self.nomDuTypePyxb=nomAlter
        return nomAlter


# ----------------------------------------
class X_compoFactoriseAmbigu(X_definition):
# ----------------------------------------

    def __init__(self,nom,listeDeCreation,pere, debug=True):

        if debug :
            for i in listeDeCreation : print (i.nom)
        self.label='BlocAmbigu'
        self.nom=nom
        self.pere=pere
        self.statut='f'
        self.entites={}
        self.mcXSD=[]
        self.typesXSDDejaDumpes=[]
        self.ordre_mc=[]
        self.lesConditions = 'Possible Conditions : '
        for mc in listeDeCreation :
            if hasattr(mc, 'condition'):self.lesConditions += '\n\t\t\t\t\t\t' + mc.condition
            self.mcXSD.append(mc)
            self.ordre_mc.append(mc.nom)

        if debug : print (self.mcXSD)
        if debug : print (self.ordre_mc)
        self.construitEntites(self.mcXSD)
        self.constructionArbrePossibles()
        lesPossibles=deepcopy(self.arbrePossibles)
        if debug : print ('lesPossibles ', lesPossibles)

        self.getNomDuCodeDumpe()
        self.nomDuTypePyxb = self.definitNomDuTypePyxb()
        if debug : print (self.nomDuTypePyxb)
        self.texteSimple = ''
        self.texteComplexeVenantDesFils = ''
        self.texteComplexe = debutTypeSubstDsBlocFactorise.format(self.nomDuTypePyxb)
        # on enleve [] des possibles puisque l elt sera optionnel
        lesPossibles.remove([])
        if debug : print ('________________ init de compoAmbigu',self.nom, lesPossibles)
        if debug : print ('self.entites', self.entites)
        self.mcXSD=self.factoriseEtCreeDump(lesPossibles,nomAppel='Root')
        if debug : print ('self.mcXSD',self.mcXSD)
        self.texteComplexe += finTypeSubstDsBlocFactorise
        self.texteComplexe +=self.texteComplexeVenantDesFils
        #print ('fin pour prepareDumpXSD pour', self.nom)

    def compare(self,autreMC):
        if self.label != autreMC.label : return False
        #PN : le bug est la
        # arbre des possibles identiques mais les types different
        # comment faire ?
        #print (self.arbrePossibles)
        #print (autreMC.arbrePossibles)
        #if self.arbrePossibles== autreMC.arbrePossibles : return True
        return False

    def construitEntites(self, laListe):
        for mc in laListe :
            if mc.nom in self.entites.keys() : self.entites[mc.nom].append(mc)
            else : self.entites[mc.nom] = [mc,]
            if mc.label == 'BLOC' or  mc.label == 'BlocAmbigu':
                self.ajouteLesMCFilsAEntite(mc)


    def ajouteLesMCFilsAEntite(self,blocMc):
        for mcFilsNom in blocMc.entites.keys():
            if mcFilsNom == 'Consigne' or mcFilsNom == 'blocConsigne' : continue
            if mcFilsNom not in self.entites.keys(): self.entites[mcFilsNom]=[]
            if blocMc.label == 'BlocAmbigu' :
                for mc in blocMc.entites[mcFilsNom] :
                    self.entites[mcFilsNom].append(mc)
                    if mc.label == 'BLOC' or  mc.label == 'BlocAmbigu':
                        self.ajouteLesMCFilsAEntite(mc)
            else :
                self.entites[mcFilsNom].append(blocMc.entites[mcFilsNom])
                if blocMc.entites[mcFilsNom].label == 'BLOC' or  blocMc.entites[mcFilsNom].label == 'BlocAmbigu':
                    self.ajouteLesMCFilsAEntite(blocMc.entites[mcFilsNom])




    def constructionArbrePossibles(self, debug = False):
        if debug : print ('construction pour FACT ambigu _______________', self.nom)
        toutesLesLignes=[[]]
        for child in self.mcXSD :
            if not hasattr(child, 'arbrePossibles') : child.construitArbrePossibles()
            if child.label != 'BLOC' :
                toutesLesLignes = deepcopy(self.fusionne2Listes(toutesLesLignes, child.arbrePossibles))
            else :
                toutesLesLignes = deepcopy(self.fusionne2Listes(toutesLesLignes, [child.nom, []]))

        lignesAGarder=[]
        for ligne in toutesLesLignes:
            blocContenus=[]
            aAjouter=True
            for mc in ligne :
                objMC=self.entites[mc][0]
                if objMC.label == 'BLOC' :
                    blocContenus.append(objMC)
            for b in blocContenus :
                for frere in blocContenus[blocContenus.index(b)+1:]:
                    if b.isDisjoint(frere) : continue
                    aAjouter=False
                    break
                if not aAjouter : break
            if  aAjouter and ligne not in lignesAGarder :
                lignesAGarder.append(ligne)

        #print ("______________________________________")
        #for l in lignesAGarder : print (l)
        #print (len(lignesAGarder))
        #print ("______________________________________")
        self.arbrePossibles=[]
        for ligne in lignesAGarder :
            #print ('lignesAGarder', ligne)
            for newLigne in self.deploye(ligne):
                #print (newLigne)
                if newLigne not in self.arbrePossibles : self.arbrePossibles.append(newLigne)
        #for l in self.arbrePossibles : print (l)
        #print ("______________________________________")


    def deploye (self, ligne):
        toutesLesLignes=[[]]
        for mc in ligne :
            #print ( 'mc in deploye', mc)
            objMC=self.entites[mc][0]
            #print ( 'nom', objMC.nom, objMC.label)
            if objMC.label == 'BLOC' or objMC.label == 'BlocAmbigu':
                toutesLesLignes = deepcopy(self.remplaceListeParContenuEtVide(toutesLesLignes, objMC.arbrePossibles))
            else :
                toutesLesLignes = deepcopy(self.adjointUnMot(toutesLesLignes,mc ))
        return toutesLesLignes

    def construitArbrePossibles(self):
    # inutile car on a deja l arbre mais appele parfois
        #print ('dans X_factCompoAmbigu ne fait rien', self.nom, self.arbrePossibles)
        pass

    def dumpXsd(self, dansFactorisation=False, multiple = False, first=False):
        # on ne fait rien, tout a ete fait dans le init
        self.texteElt=substDsSequence.format(self.code,self.nomDuTypePyxb,0,1, self.lesConditions)

    def nomComplet(self) :
        print ('dans nomComplet pourquoi ?',self, self.nom)


    def factoriseEtCreeDump(self, laListe, indent=2 ,nomAppel=None, debug=False):
        if debug : print ('_______________________________ factoriseEtCreeDump')
        if debug : print(self.nom, laListe, indent, nomAppel)
        maListeRetour=[]
        aReduire={}

        if [] in laListe :
            declencheChoiceAvecSeqVid=True
            while [] in laListe : laListe.remove([])
            #min=0
        else :
            declencheChoiceAvecSeqVid=False
            #min=1
        


        for ligne in laListe :
            if ligne[0] in aReduire.keys():
                if len(ligne) == 1 :aReduire[ligne[0]].append([])
                else : aReduire[ligne[0]].append(ligne[1:])
            else :
                if len(ligne) == 1 : aReduire[ligne[0]]=[[]]
                else : aReduire[ligne[0]]=[ligne[1:],]


        if debug : print ('la Liste', laListe, declencheChoiceAvecSeqVid)
        if debug : print (aReduire)
        if len(aReduire.keys()) == 1 :
            if declencheChoiceAvecSeqVid == False :
                creeChoice=False
                creeSequence=True
                self.texteComplexe += '\t'*(indent) +  debSequenceDsBloc; indent=indent+1
            else :
                creeChoice=True
                creeSequence=False
                # pour regler le souci du 1er Niveau
                self.texteComplexe += '\t'*indent + debutChoiceDsBloc; indent=indent+1
                #if min == 1 : self.texteComplexe += '\t'*indent + debutChoiceDsBloc; indent=indent+1
                #else        : self.texteComplexe += '\t'*indent + debutChoiceDsBlocAvecMin.format(min); indent=indent+1
        else :
            #self.texteComplexe += '\t'*indent + debutChoiceDsBlocAvecMin.format(min); indent=indent+1
            self.texteComplexe += '\t'*indent + debutChoiceDsBloc; indent=indent+1
            creeChoice=True
            creeSequence=False

        if debug : print ('creeSequence', creeSequence, aReduire)
        for nomMC in aReduire.keys():
            if debug : print (nomMC)
            listeSuivante=aReduire[nomMC]
            if creeChoice and  listeSuivante != [[]] :
                self.texteComplexe += '\t'*(indent) +  debSequenceDsBloc; indent=indent+1
            self.ajouteAuxTextes(nomMC,indent)
            if listeSuivante == [[]] : continue # Est-ce toujours vrai ?
            if len(listeSuivante) == 1 : self.ajouteAuxTextes(listeSuivante[0],indent)
            else : self.factoriseEtCreeDump(listeSuivante, indent+int(creeSequence),nomMC)
            if creeChoice   : indent=indent -1 ; self.texteComplexe += '\t'*(indent) + finSequenceDsBloc

        if declencheChoiceAvecSeqVid :
            self.texteComplexe +=  '\t'*indent +  debSequenceDsBloc
            self.texteComplexe +=  '\t'*indent + finSequenceDsBloc
        if creeChoice   : indent=indent -1 ; self.texteComplexe += '\t'*indent + finChoiceDsBloc
        if creeSequence : indent=indent -1 ; self.texteComplexe += '\t'*(indent) + finSequenceDsBloc

        #if doitFermerSequence : indent=indent-1;self.texteComplexe += '\t'*(indent) + finSequenceDsBloc
        #print (self.texteSimple)
        #print ('______',' self.texteComplexe')
        #print (self.texteComplexe)
        #print ('_____', 'self.texteComplexeVenantDesFils')
        #print (self.texteComplexeVenantDesFils)
        #print ('fin pour _______________________________', self.nom)
        return (maListeRetour)


    def ajouteAuxTextes(self,nomMC,indent,debug=False) :
        if debug : 
           print ('______________________________________________________')
           print ('ajouteAuxTextes', nomMC, self.nom)
        #  for i in self.entites.keys() : print (self.entites[i][0].nom)
        if (indent  > 3) : indent = indent - 3

        # PN change le 17 fevrier . Est-ce normal  d arriver la ?
        # if faut traiter les Blocs exclusifs qui donnent des choices de sequences
        # mais celles-ci risquent d etre ambigues
        while (isinstance(nomMC,list)) :
            nomMC=nomMC[0]

        if nomMC == 'Consigne' or nomMC == 'blocConsigne' : return
        if debug : print (nomMC, 'dans ajoute vraiment aux textes', self.entites )
        if len(self.entites[nomMC]) == 1:
            mc=self.entites[nomMC][0]
            mc.dumpXsd(dansFactorisation=True)
            self.texteComplexe += '\t'*(indent) + mc.texteElt
            if mc.aCreer : self.texteComplexeVenantDesFils += mc.texteComplexe
            if mc.aCreer : self.texteSimple   += mc.texteSimple
            if mc.aCreer : mc.aCreer=False
            return

        leType=type(self.entites[nomMC][0])
        for e in (self.entites[nomMC][1:]) :
            if type(e) != leType:
                print ('Projection XSD impossible, changez un des ', nomMC)
                exit()

        # cette boucle ne fonctionne que pour des SIMP
        resteATraiter=copy(self.entites[nomMC])
        #print ('________resteATraiter', resteATraiter)
        listePourUnion=[]
        first=1
        while resteATraiter != [] :
            nvlListeATraiter=[]
            mc=resteATraiter[0]
            listePourUnion.append(mc)
            for autre in resteATraiter[1:]:
                if not (mc.compare(autre)) :  nvlListeATraiter.append(autre)
            resteATraiter=copy(nvlListeATraiter)

        if len(listePourUnion) == 1:
            mc=listePourUnion[0]
            mc.dumpXsd(dansFactorisation=True,multiple=False,first=first)
            self.texteComplexe += '\t'*(indent) + mc.texteElt
            if mc.aCreer : self.texteComplexeVenantDesFils += mc.texteComplexe
            if mc.aCreer : self.texteSimple   += mc.texteSimple
            for mcIdent in self.entites[nomMC][1:]: mcIdent.metAJourPyxb(mc.nomDuTypePyxb)
            if mc.aCreer : mc.aCreer=False
            return

        # on ajoute le nom de l element
        if not (isinstance(self.entites[nomMC][0], Accas.SIMP)) :
            sontTousDisjoint=True
            index=1
            if debug : print ('on cherche si ils sont disjoints : ',self.entites[nomMC])
            for mc in self.entites[nomMC] :
                if debug : print ('compare mc' , mc, ' avec :')
                for mcFrere in self.entites[nomMC][index:]:
                    ok = mc.isDisjoint(mcFrere) 
                    if not ok : 
                       sontTousDisjoint=False
                       break
                if not(sontTousDisjoint) : break 
                index+=1
            if not sontTousDisjoint: 
               print ('2 blocs freres ont le meme nom et ne sont pas disjoints : pas encore traite')
               print ('Projection XSD impossible, changez un des ', nomMC)
               exit()
            self.fusionneDsUnChoix(nomMC,indent)
            if debug : print ('self.nom', self.nom)
            if debug : print ('self.texteComplexe' , self.texteComplexe)
            if debug : print ('self.texteSimple' , self.texteSimple)
            if debug : print ('self.texteElt' , self.texteElt)
            if debug : print ('________________________')
            return
        
       
        if hasattr(self.entites[nomMC][0], 'dejaDumpe') : # on a deja cree le type
            if debug : print (self.entites[nomMC][0].nomDuTypePyxb, ' deja dumpe')
        else :
            if debug : print ('appel de dumpXsd')
            self.entites[nomMC][0].dejaDumpe=True
            self.entites[nomMC][0].dumpXsd(dansFactorisation=True,multiple=True,first=first)
            if debug : print (self.entites[nomMC][0].nomDuTypePyxb)

        texteDocUnion='\n'
        i=1
        for mc in self.entites[nomMC]:
            if mc.ang != ''   : texteDocUnion += str(i) + '- ' + mc.ang + ' or \n'; i=i+1
            elif mc .fr != '' : texteDocUnion += str(i) + '- ' + mc.fr  + ' ou \n'; i=i+1
        if texteDocUnion == '\n' :
            self.texteComplexe += '\t'*(indent) + self.entites[nomMC][0].texteElt
        else :
            texteDocUnion = texteDocUnion[0:-4]
            debutTexteEltUnion = self.entites[nomMC][0].texteElt.split('maxOccurs=')[0]
            self.texteComplexe += '\t'*(indent)+ reconstitueUnion.format(debutTexteEltUnion,texteDocUnion)
        if self.entites[nomMC][0].nomDuTypePyxb in self.typesXSDDejaDumpes : return
        self.typesXSDDejaDumpes.append(self.entites[nomMC][0].nomDuTypePyxb)
        if debug : print ('et la j ajoute les definitions de type', self.entites[nomMC][0].nomDuTypePyxb)

        nomTypePyxbUnion=self.entites[nomMC][0].nomDuTypePyxb
        texteSimpleUnion = debutSimpleType.format(nomTypePyxbUnion)
        texteSimpleUnion += debutUnion
        texteSimpleUnion += '\t'*(indent)+self.entites[nomMC][0].texteSimplePart2
        texteSimplePart1  = self.entites[nomMC][0].texteSimplePart1
        for e in listePourUnion[1:] :
            e.dumpXsd(dansFactorisation=True,multiple=True,first=False)
            # si on ext un mc simple la ligne suivante est inutile
            # en revanche on ajoute le texte a tous les coups
            #self.texteComplexeVenantDesFils += e.texteComplexe
            e.metAJourPyxb(nomTypePyxbUnion)
            texteSimpleUnion += '\t'*(indent) + e.texteSimplePart2
            texteSimplePart1 += e.texteSimplePart1
        texteSimpleUnion += finUnion
        texteSimpleUnion +=fermeSimpleType
        self.texteSimple += texteSimplePart1 + texteSimpleUnion
        if debug : 
           print ('______________')
           print (self.texteSimple)
           print ('______________')
        #print ('self.texteSimple', self.texteSimple)

    def fusionneDsUnChoix(self, nomMC,indent, debug=False):
        if debug : print ('_________________________________', self.nom, self, nomMC,indent)
        if debug : print (self.texteComplexe)
        texteDocUnion='\n'
        texteComplexe=''
        texteComplexeVenantDesFils=''
        texteSimple=''
        mcRef= self.entites[nomMC][0]
        # max = 1 : a priori les choix sont exclusifs
        if (hasattr (mcRef, 'aDejaEteDumpe')) : 
          if debug : print ("je passe la NORMALEMENT car j ai deja ete dumpe")
          return
        leNomDuTypePyxb  = mcRef.definitNomDuTypePyxb(forceACreer=True)
        if debug : print ('nomMC', nomMC)
        for mc in self.entites[nomMC]:
            if debug : print ('------------', mc)
            # on laisse dansFactorisation a False car ce n est pas comme une fusion de bloc 
            mc.texteComplexe = ''
            mc.texteSimple = ''
            mc.texteElt = ''
            mc.dumpXsd(dansFactorisationDeFusion=True)
            if debug : print ('texteSimple\n', mc.texteSimple, '\n fin\n')
            if debug : print ('texteComplexeVenantDesFils\n',mc.texteComplexeVenantDesFils, '\n fin\n')
            if debug : print ('texteComplexe\n', mc.texteComplexe, '\n fin\n')
            if mc.ang != ''   : texteDocUnion += str(i) + '- ' + mc.ang + ' or \n'; i=i+1
            elif mc .fr != '' : texteDocUnion += str(i) + '- ' + mc.fr  + ' ou \n'; i=i+1
            texteComplexe += mc.texteComplexe
            texteComplexeVenantDesFils += mc.texteComplexeVenantDesFils 
            texteSimple += mc.texteSimple

        if debug : print ('______________________________')
        if debug : print ('textecomplexeVenantDesFils : \n' ,texteComplexeVenantDesFils )
        if debug : print ('______________________________')
        if debug : print ('______________________________')
        if debug : print ('textecomplexe : \n' ,texteComplexe )
        if debug : print ('______________________________')
        self.entites[nomMC][0].aDejaEteDumpe=True 

        self.texteElt = eltCompoDsSequence.format(nomMC, self.nomDuCodeDumpe,mcRef.nomDuTypePyxb,1,1)
        self.texteDuFact = debutTypeCompo.format(self.entites[nomMC][0].nomDuTypePyxb)
        self.texteDuFact += debutChoiceDsBloc
        self.texteDuFact += texteComplexe 
        self.texteDuFact += finChoiceDsBloc
        self.texteDuFact += finTypeCompo
        self.texteSimple += texteSimple
        self.texteComplexeVenantDesFils   += texteComplexeVenantDesFils
        self.texteComplexeVenantDesFils   += self.texteDuFact 
        self.texteComplexe += self.texteElt 
        if debug : print ('______________________________')
        if debug : print ('texteSimple : \n' ,self.texteSimple )
        if debug : print ('______________________________')
        self.entites[nomMC][0].aDejaEteDumpe=True 



# ----------------------------------------
class X_definitionComposee (X_definition):
# ------------------------------------------

    def creeTexteComplexeVenantDesFils(self,dansFactorisation=False,debug=False):
        texteComplexeVenantDesFils=""
        blocsDejaDumpes=set()
        #for nom in self.ordre_mc:
        #  mcFils = self.entites[nom]
        if debug : print ('creeTexteComplexeVenantDesFils', self.nom)
        if self.nom == 'LeProc' : debug = True
        for mcFils in self.mcXSD :
            #print (mcFils,mcFils.nom)
            if mcFils.nom == 'B1_B2' :debug=True 
            else : debug=False
            if not (isinstance(mcFils, Accas.BLOC)) :
                mcFils.dumpXsd(dansFactorisation)
                self.texteComplexe += mcFils.texteElt
                if mcFils.aCreer : self.texteSimple   += mcFils.texteSimple
                if mcFils.aCreer : texteComplexeVenantDesFils += mcFils.texteComplexe
            else   :
                if hasattr(mcFils,'nomXML')  and mcFils.nomXML in blocsDejaDumpes and mcFils.nomXML != None : continue
                if hasattr(mcFils,'nomXML')  and mcFils.nomXML != None: blocsDejaDumpes.add(mcFils.nomXML)
                mcFils.dumpXsd(dansFactorisation)
                self.texteComplexe += mcFils.texteElt
                if mcFils.aCreer : self.texteSimple   += mcFils.texteSimple
                if mcFils.aCreer : texteComplexeVenantDesFils += mcFils.texteComplexe
        return texteComplexeVenantDesFils

    def dumpXsd(self, dansFactorisation=False, dansFactorisationDeFusion = False, multiple = False, first=True, debug=False):
        if PourTraduction  : print (self.nom)
        # le prepareDump est appele sur les fils
        if not (self.dejaPrepareDump) : self.prepareDumpXSD()

        self.getNomDuCodeDumpe()
        if first :
            if multiple : self.nomDuTypePyxb  = self.definitNomDuTypePyxb(forceACreer=True)
            else        : self.nomDuTypePyxb  = self.definitNomDuTypePyxb()
        self.texteSimple    = "" # on n ajoute pas de type simple

        self.traduitMinMax()
        # pour accepter les PROC et ...
        #
        if debug : print ('dumpXsd', self.nom, self.aCreer)
        if self.aCreer or dansFactorisationDeFusion:
            if not dansFactorisationDeFusion : self.texteComplexe = debutTypeCompo.format(self.nomDuTypePyxb)
            if isinstance(self,X_OPER) or isinstance(self,X_PROC) :
                self.texteComplexe += debutTypeCompoEtape.format(self.code)
            self.texteComplexe += debutTypeCompoSeq
            texteComplexeVenantDesFils= self.creeTexteComplexeVenantDesFils(dansFactorisation)
            if not dansFactorisationDeFusion : 
               self.texteComplexe  = texteComplexeVenantDesFils + self.texteComplexe
               self.texteComplexeVenantDesFils  = ''
            else : 
               self.texteComplexeVenantDesFils  = texteComplexeVenantDesFils 
            # la fin de l oper est traitee dans le dumpXSD de X_OPER
            if not isinstance(self,X_OPER ) : self.texteComplexe += finTypeCompoSeq
            if isinstance(self,X_PROC)      : self.texteComplexe += finTypeCompoEtape
            if not isinstance(self,X_OPER ) and not dansFactorisationDeFusion: self.texteComplexe += finTypeCompo
        else :
            self.texteComplexe = ""

        if self.ang != "" : self.texteElt=eltCompoDsSequenceWithHelp.format(self.nom,self.nomDuCodeDumpe,self.nomDuTypePyxb,self.minOccurs,self.maxOccurs, self.ang)
        elif self.fr != ""  : self.texteElt=eltCompoDsSequenceWithHelp.format(self.nom,self.nomDuCodeDumpe,self.nomDuTypePyxb,self.minOccurs,self.maxOccurs, self.fr)
        else : self.texteElt=eltCompoDsSequence.format(self.nom,self.nomDuCodeDumpe,self.nomDuTypePyxb,self.minOccurs,self.maxOccurs)
        #print ('------------------------------------------------',self.nom)
        #print (self.texteComplexe)

    def traduitMinMax(self):
    # ______________________
    # valable pour PROC et OPER
        self.minOccurs = 0
        self.maxOccurs = 1

    def compare(self,autreMC):
        if self.label != autreMC.label : return False
        if hasattr(self,'nomXML') and hasattr(autreMC,'nomXML') and self.nomXML==autreMC.nomXML and self.nomXML != None : return True
        for attr in (  'regles', 'fr',  'defaut', 'min' ,'max', 'position' , 'docu' ) :
            val1=getattr(self,attr)
            val2=getattr(autreMC,attr)
            if val1 != val2 : return False
        if len(self.entites) != len(autreMC.entites) : return False
        for defFille in self.entites.keys():
            if defFille not in autreMC.entites.keys() : return False
            if not self.entites[defFille].compare(autreMC.entites[defFille]) : return False
        return True

    def prepareDumpXSD(self):
        self.dejaPrepareDump=True
        self.inUnion=False
        self.tousLesFils=[]
        self.mcXSD=[]
        for nomMC in self.ordre_mc:
            mc=self.entites[nomMC]
            self.mcXSD.append(mc)
            mc.prepareDumpXSD()
        self.chercheListesDeBlocsNonDisjoints()
        for l in list(self.listeDesBlocsNonDisjoints) :
            if not(self.besoinDeFactoriserTrivial(l)) : self.listeDesBlocsNonDisjoints.remove(l)
            else : self.factorise(l)

    def chercheListesDeBlocsNonDisjoints(self):
        self.listeDesBlocsNonDisjoints=[]
        for nomChild in self.ordre_mc :
            child=self.entites[nomChild]
            if child.label != 'BLOC' : continue
            if self.listeDesBlocsNonDisjoints == [] :
                self.listeDesBlocsNonDisjoints.append([child])
                continue
            vraimentIndependant=True
            for liste in list(self.listeDesBlocsNonDisjoints):
                independant=True
                for bloc in liste :
                    if bloc.isDisjoint(child)   : continue
                    if bloc.estLeMemeQue(child) : continue
                    independant=False
                    vraimentIndependant=False
                if not (independant) :
                    liste.append(child)
            if vraimentIndependant:
                self.listeDesBlocsNonDisjoints.append([child])
        # on nettoye la liste des blocs tous seuls
        for l in list(self.listeDesBlocsNonDisjoints) :
            if len(l) ==1 : self.listeDesBlocsNonDisjoints.remove(l)

    def estLeMemeQue(self,autreMC):
        if hasattr(self,'nomXML') and hasattr(autreMC,'nomXML') and self.nomXML==autreMC.nomXML and self.nomXML != None: return True
        return False

    def aUnPremierCommunDansLesPossibles(self, laListe) :
     # fonctionne avec liste de mc ou une liste(mc,index)
        import types
        mesPremiers=set()
        for elt,index in laListe :
            if not type(e) == types.ListType :
                if elt.nom in mesPremiers : return True
                mesPremiers.add(elt.nom)
            else :
                if elt[0].nom in mesPremiers : return True
                mesPremiers.add(elt[0].nom)
        return False

    def besoinDeFactoriserTrivial(self,laListe):
        # tout faux
        # a revoir
        return True
        besoin=False
        lesPremiers=set()
        for mcBloc in laListe  :
            mc=mcBloc.mcXSD[0]
            if mc.label == 'BLOC'    : return True
            if not(mc.statut=='o')   : return True
            if mc.nom in lesPremiers : return True
            lesPremiers.add(mc.nom)
        return False

    def factorise(self,liste,debug=False):
        self.listeConstruction=liste
        nomDebut=liste[0].nom
        indexDebut=self.mcXSD.index(liste[0])
        nomFin=liste[-1].nom
        indexFin=self.mcXSD.index(liste[-1]) + 1
        nom=nomDebut+'_'+nomFin
        if debug : print ('___________ dans factorise', nom)
        listeAFactoriser=[]
        for  i in range(indexDebut, indexFin) :
            listeAFactoriser.append(self.mcXSD[i])

        newListe=self.mcXSD[0:indexDebut]

        monEltFacteur=X_compoFactoriseAmbigu(nom,listeAFactoriser,self)
        newListe.append(monEltFacteur)
        newListe=newListe+self.mcXSD[indexFin:]
        self.mcXSD=newListe
        if debug :print ('___________ fin fin factorise', nom)

    def construitTousLesFils(self):
        for nomChild in self.ordre_mc :
            if nomChild == 'Consigne' or nomChild == 'blocConsigne' : continue
            child=self.entites[nomChild]
            if child.label != 'BLOC' :
                self.tousLesFils.append(child.nom)
            else:
                if child.tousLesFils == [] : child.construitTousLesFils()
                for nomPetitFils in child.tousLesFils : self.tousLesFils.append(nomPetitFils)
        #print ('construitArbreEntier pour ', self.nom, self.tousLesFils)


    def isDisjoint(self, mc1) :
        if self.tousLesFils == [] : self.construitTousLesFils()
        if not (hasattr(mc1, 'tousLesFils')) : mc1.tousLesFils  = []
        if mc1.tousLesFils  == []  : mc1.construitTousLesFils()
        for fils in mc1.tousLesFils :
            if fils in  self.tousLesFils : return False
        return True




# ---------------------------------
class X_FACT (X_definitionComposee):
#--------- ------------------------
#Un FACT avec max=** doit se projeter en XSD sous forme d'une sequence a cardinalite 1 et
# l'element qui porte la repetition du FACT
    def traduitMinMax(self):
        if self.max     == '**' or self.max  == float('inf') : self.maxOccurs="unbounded"
        else :                                                 self.maxOccurs = self.max
        self.minOccurs = self.min
        if self.statut =='f' : self.minOccurs=0
        if self.statut =='o'  and self.min < 2: self.minOccurs=1

    def construitArbrePossibles(self):
        if self.statut   ==  'f' :
            self.arbrePossibles = (self.nom,[])
            self.arbreMCPossibles = (self,None)
        else :
            self.arbrePossibles = (self.nom,)
            self.arbreMCPossibles = (self,)
        #print ('XFACT arbre des possibles de ' ,self.nom, self.arbrePossibles)



# ---------------------------------
class X_OPER (X_definitionComposee):
# ---------------------------------
    def dumpXsd(self, dansFactorisation=False, multiple = False, first=False):
        X_definitionComposee.dumpXsd(self,dansFactorisation)
        self.texteComplexe += finTypeCompoSeq
        self.texteComplexe += attributeNameName
        self.texteComplexe += attributeTypeForASSD
        self.texteComplexe += attributeTypeUtilisateurName.format(self.sd_prod.__name__)
        self.texteComplexe += finTypeCompoEtape
        self.texteComplexe += finTypeCompo


        cata = CONTEXT.getCurrentCata()
        if self.sd_prod.__name__ not in list(cata.dictTypesASSDorUserASSDCrees) :
            cata.dictTypesASSDorUserASSDCrees[self.sd_prod.__name__]=[self,]
        else :
            cata.dictTypesASSDorUserASSDCrees[self.sd_prod.__name__].append(self)


# ----------------------------------
class X_PROC (X_definitionComposee):
#-----------------------------------
    pass

#-----------------------------------
class X_BLOC (X_definitionComposee):
#-----------------------------------
    def dumpXsd(self, dansFactorisation=False, multiple = False, first=False, debug = False):
        if debug : print ('X_BLOC dumpXsd', self.nom)
        self.tousLesFils=[]
        if self.nom == 'blocConsigne' :
            self.texteComplexe = ""
            self.texteSimple   = ""
            self.nomDuTypePyxb = "NonTraiteConsigne"
            self.texteSimpleVenantDesFils = ""
            self.aCreer = False
            self.texteElt = ""

            return
        self.getNomDuCodeDumpe()
        # dans ce cas les blocs successifs sont identiques et on ne dumpe que le 1er

        self.nomDuTypePyxb  = self.definitNomDuTypePyxb()
        self.texteSimple    = "" # on n ajoute pas de type simple

        # Pour les blocs le minOccurs vaut 0 et le max 1
        if self.aCreer :
            self.texteComplexe = debutTypeSubst.format(self.nomDuTypePyxb)
            texteComplexeVenantDesFils=self.creeTexteComplexeVenantDesFils(dansFactorisation)
            self.texteComplexe  = texteComplexeVenantDesFils + self.texteComplexe
            self.texteComplexe += finTypeSubst

        else :
            self.texteComplexe = ""

        self.texteElt=substDsSequence.format(self.code,self.nomDuTypePyxb,0,1,'condition : ' +self.condition)

        #print ('------------------------------------------------')

    def compare(self,autreMC):
        if self.label != autreMC.label : return False
        if self.inUnion == True or autreMC.inUnion == True : return False
        if hasattr(self,'nomXML') and hasattr(autreMC,'nomXML') and self.nomXML==autreMC.nomXML and self.nomXML != None : return True
        for attr in ( 'condition', 'regles', ):
            val1=getattr(self,attr)
            val2=getattr(autreMC,attr)
            if val1 != val2 : return False
        if len(self.entites) != len(autreMC.entites) : return False
        for defFille in self.entites.keys():
            if defFille not in autreMC.entites.keys() : return False
            if not self.entites[defFille].compare(autreMC.entites[defFille]) : return False
        return True

    def construitArbrePossibles(self):
        self.arbrePossibles=[[],]
        #print ('X_BLOC je construis l arbre des possibles pour ', self.nom)
        for child in self.mcXSD :
            if not hasattr(child, 'arbrePossibles') : child.construitArbrePossibles()
            #print (child.nom, child.label, child.arbrePossibles)
            if child.label == 'BLOC' :
                self.arbrePossibles = deepcopy(self.remplaceListeParContenuEtVide(self.arbrePossibles, child.arbrePossibles))
            elif child.label == 'BlocAmbigu':
                #print ("je passe par la pour", self.nom, child.nom, self.arbrePossibles, child.arbrePossibles)
                self.arbrePossibles = deepcopy(self.remplaceListeParContenuEtVide(self.arbrePossibles, child.arbrePossibles))
                #print ('resultat', self.arbrePossibles)
            else :
                self.arbrePossibles = deepcopy(self.adjoint(self.arbrePossibles, child.arbrePossibles))
        self.arbrePossibles.append([]) # un bloc n est pas obligatoire
        #print ('arbre des possibles de ' ,self.nom, self.arbrePossibles)


#--------------------------------
class X_SIMP (X_definition):
#--------------------------------
    def dumpXsd(self, dansFactorisation=False, multiple=False, first=False, debug=False):
        #debug = True
        #if PourTraduction  : print (self.nom)
        if debug : print ('X_SIMP dumpXsd pour', self.nom, '___________________________')
        self.prepareDumpXSD()
        # si inUnion la comparaison est fausse : on cree le nomDuType
        if multiple : self.inUnion=True
        #print ('exploreObjet SIMP')
        self.getNomDuCodeDumpe()
        self.aCreer = True
        self.texteComplexe = ""
        self.texteSimple   = ""
        self.texteElt      = ""
        if self.nom =='Consigne' : return

        #  --> homonymie on peut utiliser genealogie ?
        self.nomDuTypeDeBase = self.traduitType()
        if debug : print ('nomDuTypeDeBase', self.nomDuTypeDeBase)
        if debug : print ('multiple', multiple, 'first', first)
        if not multiple :
            self.nomDuTypePyxb   = self.definitNomDuTypePyxb()
        else :
            if first :
                # on force la creation
                self.nomDuTypePyxb   = self.definitNomDuTypePyxb()
                self.aCreer = True
            else :
                self.nomDuTypePyxb='NonDetermine'

        if debug : print ('nomDuTypePyxb', self.nomDuTypePyxb)
        if debug : print ('aCreer', self.aCreer)


        # on se sert des listes ou non pour  la gestion des minOccurs /maxOccurs est > 0
        if self.statut =='f' : minOccurs = 0
        else                 : minOccurs = 1
        if dansFactorisation : minOccurs = 1

        if self.suisUneMatrice :
           self.dumpSpecifiqueMatrice(minOccurs)
           return

        if self.suisUnTuple :
           self.dumpSpecifiqueTuple(minOccurs)
           return

        if self.avecBlancs and self.max > 1 :
           #print ('je suis avec blanc pour ', self.nom)
           self.dumpSpecifiqueTexteAvecBlancs(minOccurs,multiple)
           return

        #print ('minOccurs',minOccurs)
        # le defaut est dans l elt Name -> tester la coherence d existence avec Accas
        # regles Accas

        # pas d elt si on est dans multiple
        # sauf si on est le '1er'  dans un element ambigu
        if not multiple :
            #print ('je passe la pas multiple')
            texteAide = ""
            if self.ang != '' : texteAide = self.ang
            else : texteAide = self.fr
            if self.intoXML and self.into :
               if self.intoXML != self.into :
                  #print ('je passe la pour ', self.nom)
                  texteAide :texteAide =  texteAide+'\nPossible choices for '+ self.nom + 'at this place : \n'+str(self.into)+'\n'

            if self.defaut :
               if self.max > 1 or self.max == '**' or self.max ==  float('inf') : 
                    txtDefaut=""
                    for val in self.defaut : txtDefaut+=str(val) + " " 
                    # cela ne fonctionne pas tres bien. a revoir
                    txtDefaut+=txtDefaut[0:-1]
                    if not('TXM' in (self.type)) : 
                        # a revoir pour les tuples avec defaut
                        if texteAide != ''  : self.texteElt = eltDsSequenceWithDefautAndHelp.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1,txtDefaut,texteAide)
                        else : self.texteElt = eltDsSequenceWithDefaut.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1,txtDefaut)
                    else :
                        texteAide +=  texteAide+'\ndefault Value in MDM : \n'+txtDefaut
                        self.texteElt = eltDsSequenceWithHelp.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1,texteAide)
               else :
                    if str(self.defaut)   == 'True'  : txtDefaut = 'true'
                    elif str(self.defaut) == 'False' : txtDefaut = 'false'
                    else : txtDefaut = str(self.defaut)
                    if texteAide != ''  : self.texteElt = eltDsSequenceWithDefautAndHelp.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1,txtDefaut,texteAide)
                    else : self.texteElt = eltDsSequenceWithDefaut.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1,txtDefaut)
            else :
               if texteAide  != '' : self.texteElt = eltDsSequenceWithHelp.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1,texteAide)
               else : self.texteElt = eltDsSequence.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1)
        elif first:
            # l'aide est geree a la fusion 
            self.texteElt = eltDsSequence.format(self.nom,self.code,self.nomDuTypePyxb,1,1)

        # self.aCreer est mis a jour ds definitNomDuTypePyxb
        # ou si elt est le 1er d une liste identique
        if debug : print ('je suis aCreer', self.aCreer)
        if not self.aCreer : return

        typeATraduire=self.type[0]

        self.texteSimplePart1=""
        if not(isinstance(typeATraduire,str)) and not(isinstance(typeATraduire,Accas.Tuple)) and issubclass(typeATraduire, Accas.UserASSD) :
            cata = CONTEXT.getCurrentCata()
            if len(self.type) == 2 and self.type[1]=='createObject' : suffixe = 'C'
            else : suffixe = 'U' 
            #print (cata.listeUserASSDDumpes)
            #print (typeATraduire.__name__)
            #print (typeATraduire.__name__ in cata.listeUserASSDDumpes)
            if typeATraduire.__name__  not in cata.listeUserASSDDumpes :
                cata.listeUserASSDDumpes.add(typeATraduire.__name__)
                if issubclass(typeATraduire, Accas.UserASSDMultiple) : 
                   self.texteSimplePart1 = defUserASSDMultiple.format(typeATraduire.__name__)
                   if cata.definitUserASSDMultiple == False  :
                      cata.definitUserASSDMultiple = True
                      cata.texteSimple = cata.texteSimple + defBaseXSDUserASSDMultiple
                else :
                   self.texteSimplePart1 = defUserASSD.format(typeATraduire.__name__)
                   if cata.definitUserASSD == False  :
                      cata.definitUserASSD = True
                      cata.texteSimple = cata.texteSimple + defBaseXSDUserASSD
            if typeATraduire.__name__+'_'+suffixe not in cata.listeUserASSDDumpes :
                cata.texteSimple = cata.texteSimple + defUserASSDOrUserASSDMultiple.format(typeATraduire.__name__, suffixe,typeATraduire.__name__)
                cata.listeUserASSDDumpes.add(typeATraduire.__name__+'_'+suffixe)


        if not multiple : self.texteSimple  += debutSimpleType.format(self.nomDuTypePyxb)
        else : self.texteSimple  += debutSimpleTypeSsNom
        # On est dans une liste
        if self.max > 1 or self.max == '**' or self.max ==  float('inf') or  hasattr(self.type[0], 'ntuple') :
            self.texteSimple  += debutTypeSimpleListe
            self.texteSimple  += "\t\t\t\t"+debutRestrictionBase.format(self.nomDuTypeDeBase)
            if self.val_min != float('-inf')  : self.texteSimple += "\t\t\t\t"+minInclusiveBorne.format(self.val_min)
            if self.val_max != float('inf') and self.val_max != '**' : self.texteSimple +="\t\t\t\t"+ maxInclusiveBorne.format(self.val_max)
            if self.into != None:
                # PN --> traduction des into
                into=self.into
                if self.intoXML != None : into = self.intoXML
                for val in into : self.texteSimple += "\t\t\t\t"+enumeration.format(val)
                if PourTraduction  :
                    for val in into : print (str(val))
            self.texteSimple  += fermeBalisesMileu
            if  self.max !=1 and self.max != '**' and self.max !=  float('inf') : self.texteSimple  += maxLengthTypeSimple.format(self.max)
            if  self.min !=1 and self.min !=  float('-inf') : self.texteSimple  += minLengthTypeSimple.format(self.min)
            self.texteSimple  += fermeRestrictionBase
        else :
        # ou pas
            self.texteSimple  += debutRestrictionBase.format(self.nomDuTypeDeBase)
            if self.val_min != float('-inf')  : self.texteSimple += minInclusiveBorne.format(self.val_min)
            if self.val_max != float('inf') and self.val_max != '**' : self.texteSimple += maxInclusiveBorne.format(self.val_max)
            if self.into != None:
                into=self.into
                if self.intoXML != None : into = self.intoXML
                for val in into : self.texteSimple += enumeration.format(val)
                if PourTraduction  :
                    for val in into : print (str(val))
            self.texteSimple  += fermeRestrictionBase
        self.texteSimple  += fermeSimpleType
        self.texteSimplePart2 = self.texteSimple
        self.texteSimple = self.texteSimplePart1 + self.texteSimplePart2


    def dumpSpecifiqueTexteAvecBlancs(self,minOccurs,multiple):
        # attention multiple non traite
        # pour l instant on n a pas max =1 et on ne traite pas les into

        texteAide = ""
        if  self.ang != '' : texteAide = self.ang
        elif self.fr != '' : texteAide = self.fr

        self.texteElt = eltDsSequenceWithHelp.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1,texteAide)
        txtDefaut=""
        # Pas de Defaut pour les string en XSD
        # max sert pour la taille de la liste
        if self.defaut : texteAide += ' Valeur par defaut dans le comm : '+str(self.defaut)
        if texteAide != ''  : self.texteElt = eltDsSequenceWithHelp.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1,texteAide)
        else : self.texteElt = eltDsSequence.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1)
         
        
        if self.max == '**' or self.max ==  float('inf') : max='unbounded'
        else  : max = self.max
  
        if self.max > 1 : # juste au cas ou on traite 1 pareil
            self.texteSimple = ''
            cata = CONTEXT.getCurrentCata()
            if self.nomDuTypePyxb in cata.listeTypeTXMAvecBlancs: return
            cata.listeTypeTXMAvecBlancs.add(self.nomDuTypePyxb)
            self.texteSimple = complexChaineAvecBlancs.format(self.nomDuTypePyxb,max,self.nomDuTypePyxb)
            if self.intoXML != None : into = self.intoXML
            else : into = self.into
            if into  == None :
               self.texteSimple += typeEltChaineAvecBlancSansInto.format(self.nomDuTypePyxb)
            else : 
               self.texteSimple += debutChaineAvecBlancsInto.format(self.nomDuTypePyxb)
               for val in into : self.texteSimple += milieuChaineAvecBlancsInto.format(val)
               self.texteSimple += finChaineAvecBlancsInto
           
        
    def dumpSpecifiqueTuple(self,minOccurs):
        self.nomDuTypeDeBase = self.traduitType()
        tousPareil=True
        # il faut gerer l aide et les defaut
        if self.defaut : print ('il faut tester le defaut')
        if self.max == '**' or self.max ==  float('inf') : max='unbounded'
        else  : max = self.max
        self.texteElt = tupleNonHomogeneElt.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,max)
        leType=self.nomDuTypeDeBase[0]
        for leTypeComp in self.nomDuTypeDeBase[1:] :
            if leTypeComp != leType : 
                tousPareil = False
                break;
        #if tousPareil :
        #PN PN a statuer
        #    self.texteSimple  += debutSimpleType.format(self.nomDuTypePyxb)
        #    self.texteSimple  += debutTypeSimpleListe
        #    self.texteSimple  += "\t\t\t\t"+debutRestrictionBase.format(leType)
        #    if self.val_min != float('-inf')  : self.texteSimple += "\t\t\t\t"+minInclusiveBorne.format(self.val_min)
        #    if self.val_max != float('inf') and self.val_max != '**' : self.texteSimple +="\t\t\t\t"+ maxInclusiveBorne.format(self.val_max)
        #    if self.into != None:
        #        into=self.into
        #        if self.intoXML != None : into = self.intoXML
        #        for val in into : self.texteSimple += "\t\t\t\t"+enumeration.format(val)
        #        if PourTraduction  : 
        #            for val in into : print (str(val))
        #    self.texteSimple  += fermeBalisesMileu
        #    if self.max !=1 and self.max != '**' and self.max !=  float('inf') : self.texteSimple  += maxLengthTypeSimple.format(self.max)
        #    if self.min !=1 and self.min !=  float('-inf') : self.texteSimple  += minLengthTypeSimple.format(self.min)
        #    self.texteSimple  += fermeSimpleType
        #    return

        self.texteSimple = ''
        complexeTypeTuple = tupleDebutComplexeType.format(self.nomDuTypePyxb)
        num = 1
        for leType in self.nomDuTypeDeBase :
            self.texteSimple  += tupleNonHomogeneSimpleType.format(self.nomDuTypePyxb,str(num),leType)
            complexeTypeTuple += tupleMilieuComplexeType.format(str(num),self.nomDuTypePyxb,str(num))
            num = num + 1
        complexeTypeTuple += tupleFinComplexeType
        self.texteSimple  += complexeTypeTuple
              

    def dumpSpecifiqueMatrice(self,minOccurs):
    # if faut traiter le defaut
        typeDeMatrice =self.type[0]

        self.texteSimple  += debutSimpleType.format(self.nomDuTypePyxb+'_element')
        self.texteSimple  += debutRestrictionBase.format(self.nomDuTypeDeBase)
        if typeDeMatrice.typEltInto != None:
            for val in typeDeMatrice.typEltInto : self.texteSimple += enumeration.format(val)
        self.texteSimple  += fermeRestrictionBase
        self.texteSimple += fermeSimpleType
        nom=self.nomDuTypePyxb
        nbCols=typeDeMatrice.nbCols
        nbLigs=typeDeMatrice.nbCols
        self.texteSimple += matriceSimpleType.format(nom,nom,nbCols,nom,self.code,nom,nbLigs,nbLigs,nom,self.code,nom,self.min,self.max)
        self.texteElt = eltMatrice.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1)

        
    def prepareDumpXSD(self):
        self.inUnion=False
        if self.statut   ==  'f' : self.arbrePossibles = (self.nom,[])
        else                     : self.arbrePossibles = (self.nom,)
        self.mcXSD=[]



    def traduitType(self,debug=False):
        # il faut traduire le min et le max
        # il faut ajouter les regles
        # il faut gerer les types tuple et fichier
        # on ne paut pas tester le type qui depend du cataloge
        if hasattr(self.type[0], 'typElt') : 
            #print ('je suis une Matrice de ' ,dictNomsDesTypes[self.type[0].typElt]) 
            self.suisUneMatrice = True
            # on presume que le type de l elt est un ASSD
            if self.type[0].typElt not in dictNomsDesTypes.keys(): return 'xs:string'
            return dictNomsDesTypes[self.type[0].typElt] 
        else :
            self.suisUneMatrice = False
        if hasattr(self.type[0], 'ntuple') :
            self.suisUnTuple = True
            # Pour l instant pas de into dans les tuples non homogenes et pas de reference
            # sinon, il faudra faire un for sur la suite avec les createObjet
            leType=self.validators.typeDesTuples[0]
            enRetour=[]
            for i in range(self.type[0].ntuple):
                enRetour.append(dictNomsDesTypes[self.validators.typeDesTuples[i]])
            return enRetour
            #typeATraduire=leType
        else :
            self.suisUnTuple = False
            typeATraduire=self.type[0]
        if not (typeATraduire in list(dictNomsDesTypes.keys())) :
            #if (isinstance(typeATraduire, Accas.ASSD) or issubclass(typeATraduire, Accas.ASSD)) :
            if (not(isinstance(typeATraduire,str)) and issubclass(typeATraduire, Accas.ASSD)) :
            # cas d une creation
                cata = CONTEXT.getCurrentCata()
                # PNPNPN a Revoir pour la creation des keyrefs
                if len(self.type) == 2 and self.type[1]=='createObject' :
                    if typeATraduire.__name__ not in list(cata.dictTypesASSDorUserASSDCrees) :
                        cata.dictTypesASSDorUserASSDCrees[typeATraduire.__name__]=[self,]
                    else :
                        cata.dictTypesASSDorUserASSDCrees[typeATraduire.__name__].append(self)
                    if issubclass(typeATraduire, Accas.UserASSD) : return typeATraduire.__name__+'_C'
                    else : return  'xs:string'

                # cas d une consommation
                if typeATraduire not in list(cata.dictTypesASSDorUserASSDUtilises) :
                    cata.dictTypesASSDorUserASSDUtilises[typeATraduire]=[self,]
                else :
                    cata.dictTypesASSDorUserASSDUtilises[typeATraduire].append(self,)
                if issubclass(typeATraduire, Accas.UserASSD) : return typeATraduire.__name__+'_U'
                else : return  'xs:string'
            else : return ('YYYYY')
        return dictNomsDesTypes[typeATraduire]

    def traduitValMinValMax(self):
        self.maxInclusive=self.val_max
        self.minInclusive=self.val_min
        if self.val_min == float('-inf') and val_max== float('inf') : return
        #print ('il faut affiner le type du SIMP ', self.nom)
        if self.val_max == '**' or self.val_max == float('inf') : self.maxInclusive=None
        else : self.maxInclusive = self.val_max
        if self.val_min == '**' or self.val_max == float('-inf') : self.maxInclusive=None
        else : self.minInclusive = self.val_min

    def traduitMinMax(self):
        if self.min == 1 and self.max == 1 :  return
        #print ('il faut creer une liste ' , self.nom)

    def compare(self,autreMC):
        if self.label != autreMC.label : return False
        if self.inUnion == True or autreMC.inUnion == True : return False
        if hasattr(self,'nomXML') and hasattr(autreMC,'nomXML') and self.nomXML==autreMC.nomXML and self.nomXML != None : return True
        listeAComparer = [ 'type', 'defaut', 'min' ,'max' ,'val_min' , 'val_max' ]
        if self.intoXML != None : listeAComparer.append('intoXML')
        else : listeAComparer.append('into')
        if (hasattr (self, 'nomXML')) and self.nomXML != None : nomUtil=self.nomXML
        for attr in listeAComparer :
            val1=getattr(self,attr)
            val2=getattr(autreMC,attr)
            if val1 != val2 : return False
        return True

    def construitArbrePossibles(self):
        if self.statut   ==  'f' :
            self.arbrePossibles = (self.nom,[])
        else :
            self.arbrePossibles = (self.nom,)
        #print ('SIMP arbre des possibles de ' ,self.nom, self.arbrePossibles)


#-----------------
class X_JDC_CATA :
#-----------------

    def dumpXsd(self, avecEltAbstrait,  debug = True):
        cata = CONTEXT.getCurrentCata()
        if debug : print ('avecEltAbstrait   -------------------', avecEltAbstrait)

        if debug : print ('self.importedBy -------------------', self.importedBy)
        if debug : print ('self.code       -------------------', self.code)

        self.texteSimple   = ""
        self.texteComplexe = ""
        self.texteCata     = ""
        self.texteDeclaration  = ""
        self.texteInclusion    = ""
        self.texteElt          = ""
        self.texteTypeAbstrait = ""

        if self.implement == "" :
            self.nomDuCodeDumpe = self.code
            self.implement      = self.code
            self.nomDuXsdPere   = self.code
        else :
            self.implement,self.nomDuXsdPere=self.implement.split(':')
            self.nomDuCodeDumpe = self.implement

        if debug : print ('self.implement       -------------------', self.implement)
        if debug : print ('self.nomDuCodeDumpe   -------------------', self.nomDuCodeDumpe)
        if debug : print ('self.nomDuXsdPere  -------------------', self.nomDuXsdPere)

        self.nomDuTypePyxb    = 'T_'+self.nomDuCodeDumpe
        self.dumpLesCommandes()

        if self.implement == self.code :
            self.texteCata += eltAbstraitCataPPal.format(self.code)
            if 0 : pass
            else  : self.texteCata += eltCataPPal.format(self.code,self.code,self.code)
        else :
            self.texteCata += eltAbstraitCataFils.format(self.implement,self.nomDuXsdPere,self.nomDuXsdPere)
            if 0 : pass
            else : self.texteCata += eltCataFils.format(self.implement,self.nomDuXsdPere,self.nomDuXsdPere,self.nomDuXsdPere)
            self.texteInclusion += includeCata.format(self.nomDuXsdPere)

    
        self.texteCata += eltCata.format(self.implement,self.implement,self.implement,self.implement,self.nomDuXsdPere)
        #if self.implement == self.code :
        #   self.texteCata      += debutTypeCata.format(self.nomDuCodeDumpe)
        #else :
        #   self.texteCata      += debutTypeCataExtension.format(self.nomDuCodeDumpe)
        #   self.texteCata      += debutExtension.format(self.code,self.nomDuCodeDumpe)
        #   self.texteInclusion += includeCata.format(self.nomDuXsdPere)



        #for codeHeritant in self.importedBy:
        #    self.texteCata += eltCodeSpecDsCata.format(codeHeritant)
        #    self.texteTypeAbstrait += eltAbstrait.format(codeHeritant,codeHeritant,self.code,codeHeritant)

        #if self.implement != "" : self.texteCata = self.texteCata + finExtension + finTypeCompo
        #else : self.texteCata  += finTypeCata

        #if self.implement != "" :
        #   self.texteElt=implementeAbstrait.format(self.nomDuCodeDumpe,self.code,self.nomDuTypePyxb,self.code,self.nomDuCodeDumpe)
        #else :
        #   self.texteElt  = eltCata.format(self.nomDuCodeDumpe,self.code, self.nomDuTypePyxb)

        if self.implement == self.code :
            self.texteXSD  = texteDebut.format(self.code,self.code,self.code,self.code,self.code,self.code)
        elif self.nomDuXsdPere ==  self.code :
            self.texteXSD  = texteDebutNiveau2.format(self.code,self.implement,self.code,self.code,self.code, self.code,self.code,self.code,self.code,self.code)
        else :
            self.texteXSD  = texteDebutNiveau3.format(self.code,self.implement,self.code,self.nomDuXsdPere,self.code,self.code,self.code, self.code,self.code,self.code,self.code,self.code)

        if self.texteInclusion != ""   : self.texteXSD += self.texteInclusion
        self.texteXSD += self.texteSimple
        self.texteXSD += self.texteComplexe

        #if self.texteTypeAbstrait != "" : self.texteXSD += self.texteTypeAbstrait
        self.texteXSD += self.texteCata
        #self.texteXSD += self.texteElt

        toutesLesKeys=set()
        texteKeyRef = ""
        # Pour le nom des key_ref en creation : le type ( une seule key-ref par type. facile a retrouver)
        for clef in self.dictTypesASSDorUserASSDCrees:
            existeASSD=0
            texteDesFields=""
            for unOper in self.dictTypesASSDorUserASSDCrees[clef]:
                if  not(isinstance(unOper, Accas.OPER)) : continue
                existeASSD=1
                texteDesFields+=texteFieldUnitaire.format(self.code, unOper.nom)
            if existeASSD : texteDesFields=texteDesFields[0:-2]
            texteDesUserASSD=''
            existeunUserASSD=0
            for unSimp in self.dictTypesASSDorUserASSDCrees[clef]:
                if not (isinstance(unSimp, Accas.SIMP)) : continue
                texteDesUserASSD += unSimp.getXPathSansSelf() + " | "
                #print (unSimp.getXPathSansSelf())
                #texteFieldUnitaire='/'+self.code+":"+unSimp.nom
                existeunUserASSD=1
            if existeunUserASSD:
                if existeASSD : texteDesFields = texteDesFields + texteDesUserASSD[0:-2] +"/>\n\t\t"
                else: texteDesFields = texteDesUserASSD[0:-2]
            #print (texteDesUserASSD)
            #print (texteDesFields)
            if texteDesFields != "" :
                texteKeyRef  += producingASSDkeyRefDeclaration.format( clef ,texteDesFields)


        # Pour le nom des key-ref en utilisation : la genealogie complete  ( une  key-ref par utilisation et on retrouve facilement la )
        for clef in self.dictTypesASSDorUserASSDUtilises:
            for unSimp in self.dictTypesASSDorUserASSDUtilises[clef]:
                # il faut la genealogie
                texteKeyRef  += UsingASSDkeyRefDeclaration.format(unSimp.getNomCompletAvecBloc(), unSimp.type[0].__name__,self.code, unSimp.type[0].__name__,unSimp.getXPathComplet() )

        #PNPN on debranche les keyref le temps de bien reflechir a leur forme
        #if texteKeyRef != '' :
        #   self.texteXSD = self.texteXSD[0:-3]+'>\n'
        #   self.texteXSD += texteKeyRef
        #   self.texteXSD += fermeEltCata



        #if not PourTraduction : print (self.texteXSD)

        import pprint
        #pprint.pprint (cata.dictTypesXSDJumeaux)
        #for k in cata.dictTypesXSDJumeaux:
        #    print (k.nom, k.nomComplet())
        #    print (cata.dictTypesXSDJumeaux[k][0].nom, cata.dictTypesXSDJumeaux[k][0].nomComplet())

        #pprint.pprint (cata.dictTypesXSD)
        #for k in cata.dictTypesXSD:
        #    print (k)
        #    print (cata.dictTypesXSD)

        dico = {}
        for  k in list(cata.dictTypesXSD.keys()):
            dico[k]={}
            different=False
            for definition in cata.dictTypesXSD[k] :
                if definition.label  == 'BLOC' or  definition.label == 'BlocAmbigu':continue
                if definition.nomDuTypePyxb != 'T_'+definition.nom : different=True
                listeATraiter=[definition.geneaCompleteSousFormeDeListe(),]
                while listeATraiter != [] :
                    listeGenea=listeATraiter[0]
                    listeATraiter=listeATraiter[1:]
                    txtNomComplet=''
                    indexMC=0
                    for MC in listeGenea:
                        txtNomComplet=txtNomComplet+'_'+MC.nom
                        if MC in list(cata.dictTypesXSDJumeaux.keys()) :
                            for MCJumeau in cata.dictTypesXSDJumeaux[MC]:
                                # attention nvlleGenalogie n a pas de sens en Accas
                                nvlleGenalogie=listeGenea[:indexMC]+MCJumeau.geneaCompleteSousFormeDeListe()
                                listeATraiter.append(nvlleGenalogie)
                        indexMC=indexMC+1
                    dico[k][txtNomComplet]=definition.nomDuTypePyxb
            if dico[k]== {} or (not different) : del dico[k]
        import pprint
        #pprint.pprint(dico)
        # PN reflechir a ce *** de nom
        #if dico != {} : self.texteXSD += texteAnnotation.format(self.nomDuCodeDumpe,str(dico))
        if dico != {} : self.texteXSD += texteAnnotation.format(str(dico))

        #import pprint
        #if (not PourTraduction) and  (dico != {}) : pprint.pprint(dico)
        print ('__________________________ decommenter pour le texteXSD________________________')
        #print (dico)
        #print (self.texteXSD)
        self.texteXSD += texteFin
        return self.texteXSD


    def dumpLesCommandes(self):
        cata = CONTEXT.getCurrentCata()
        fichierCataSourceExt=os.path.basename(cata.cata.__file__)
        fichierCataSource, extension=os.path.splitext(fichierCataSourceExt)
        importCataSource=__import__(fichierCataSource,{},{})

        texte=""
        for m in sys.modules:
            monModule=sys.modules[m]
            try :
                if m in ('os', 'sys', 'inspect', 'six', 'pickle', 'codecs')      : continue
                if m in ('cPickle', 'pprint', 'dis', '_sre', 'encodings.aliases'): continue
                if m in ('numbers', 'optparse', 'binascii', 'posixpath')         : continue
                if m in ('_locale', '_sysconfigdata_nd', 'gc', 'functools')      : continue
                if m in ('posixpath', 'types', 'posix', 'prefs')                 : continue
                if m in ('warnings', 'types', 'posix', 'prefs')                  : continue
                if monModule.__name__[0:15] == '_sysconfigdata_' : continue
                if monModule.__name__ == '__future__' :  continue
                if monModule.__name__[0:3] == 'Ihm'   :  continue
                if monModule.__name__[0:5] == 'numpy' :  continue
                if monModule.__name__[0:5] == 'Noyau' :  continue
                if monModule.__name__[0:5] == 'Accas' :  continue
                if monModule.__name__[0:7] == 'convert'       :  continue
                if monModule.__name__[0:7] == 'Efi2Xsd'       :  continue
                if monModule.__name__[0:7] == 'Editeur'       :  continue
                if monModule.__name__[0:9] == 'generator'     :  continue
                if monModule.__name__[0:10] == 'Validation'   :  continue
                if monModule.__name__[0:10] == 'Extensions'   :  continue
                if monModule.__name__[0:12] == 'InterfaceQT4' :  continue
                if monModule.__name__ == fichierCataSource    :  continue
                texte= texte + "try : import "+ monModule.__name__ + " \n"
                texte= texte + "except : pass \n"
                texte= texte + "try : from  "+ monModule.__name__ + ' import * \n'
                texte= texte + "except : pass \n"
            except :
                pass

        newModule=imp.new_module('__main__')
        exec (texte, newModule.__dict__)
        allClassToDump=[]
        for i in dir(importCataSource):
            if i not in dir(newModule):
                allClassToDump.append(importCataSource.__dict__[i])


        self.texteSimple = ''
        self.texteComplexe = ''
        for c in allClassToDump :
            if not(isinstance(c, Accas.OPER)) and not(isinstance(c, Accas.PROC))  : continue
            c.nomDuCodeDumpe=self.nomDuCodeDumpe
            c.code=self.implement
            c.dumpXsd()

            self.texteSimple   += c.texteSimple
            self.texteComplexe += c.texteComplexe
            if  c.ang != '' : c.texteElt = eltEtapeWithHelp.format(c.nom,self.implement,c.nomDuTypePyxb,self.implement,c.ang)
            elif c.fr != '' : c.texteElt = eltEtapeWithHelp.format(c.nom,self.implement,c.nomDuTypePyxb,self.implement,c.fr)
            else : c.texteElt = eltEtape.format(c.nom,self.implement,c.nomDuTypePyxb,self.implement)
            self.texteCata   += c.texteElt
