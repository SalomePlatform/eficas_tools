#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cette version ne fonctionne pas bien


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

   #def remplaceNomListeParContenu(self, liste1, liste2):
       #print ('remplaceNomListeParContenu', liste1, liste2)
   #    listeFinale=[]
   #    for elt1 in liste1 :
   #      for eltListe in liste2:
   #           if eltListe == [] : continue
   #           newListe=deepcopy(elt1)
   #           if eltListe!=[] :newListe+=eltListe
   #           listeFinale.append(newListe)
       #print ('listeFinale', listeFinale)
   #    return listeFinale

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
       

   def definitNomDuTypePyxb(self,forceACreer=False):
       if hasattr(self,'nomDuTypePyxb') : 
          self.aCreer = False
          return self.nomDuTypePyxb
       self.aCreer = True
       cata = CONTEXT.getCurrentCata() 
       nom='T_'+self.nom
       if (hasattr (self, 'nomXML')) and self.nomXML != None : nom='T_'+self.nomXML
       if not (nom in cata.dictTypesXSD.keys()) :
          cata.dictTypesXSD[nom] = [self,]
          self.nomDuTypePyxb=nom
          return nom
       self.aCreer = False
       if nom == 'T_Consigne' : return nom
       
       listePossible=cata.dictTypesXSD[nom]
       indice=0
       while (indice < len(listePossible)) :
          objAComparer=listePossible[indice]
          if self.compare(objAComparer) : 
             self.nomDuTypePyxb=objAComparer.nomDuTypePyxb
             return objAComparer.nomDuTypePyxb
          indice += 1
       self.aCreer = True
       cata.dictTypesXSD[nom].append(self)
       nomAlter='T_'+self.nom+'_'+str(indice)
       if (hasattr (self, 'nomXML')) and self.nomXML != None : 
           nomAlter='T_'+self.nomXML+'_'+str(indice)
       self.nomDuTypePyxb=nomAlter
       #traceback.print_stack()
       return nomAlter


# ----------------------------------------
class X_compoFactoriseAmbigu(X_definition):
# ----------------------------------------

   def __init__(self,nom,listeDeCreation,pere):
       #print ('__ X_compoFactoriseAmbigu', listeDeCreation)
       #for (i,index) in listeDeCreation : print i.nom
       self.label = 'compoAmbigu'
       self.nom=nom
       self.pere=pere
       self.statut='f'
       self.entites={}
       self.mcXSD=[]
       self.ordre_mc=[]
       self.mcDejaDumpe=set()
       #print (listeDeCreation)
       for (mc, index) in listeDeCreation : 
           self.mcXSD.append(mc)
           self.ordre_mc.append(mc.nom)
       #self.mcXSD=list(deepcopy(self.ordre_mc))
       #for i in self.entites : print (i,self.entites[i])
       #print ('creation de X_compoFactoriseAmbigu', self.nom, self.mcXSD)
       self.construitEntites(self.mcXSD)
       self.constructionArbrePossibles()
       lesPossibles=deepcopy(self.arbrePossibles)
      
       self.getNomDuCodeDumpe()
       self.nomDuTypePyxb = self.definitNomDuTypePyxb()
       self.texteSimple = ''
       self.texteComplexeVenantDesFils = ''
       self.texteComplexe = debutTypeSubstDsBlocFactorise.format(self.nomDuTypePyxb)
       # on enleve [] des possibles puisque l elt sera optionnel
       lesPossibles.remove([])
       #print ('________________ init de compoAmbigu',self.nom, lesPossibles)
       #print ('self.entites', self.entites)
       self.mcXSD=self.factoriseEtCreeDump(lesPossibles,nomAppel='Root')
       #print ('self.mcXSD',self.mcXSD)
       self.texteComplexe += finTypeSubstDsBlocFactorise
       self.texteComplexe +=self.texteComplexeVenantDesFils
       # PN ?? 12 mai self.texteComplexe=self.texteComplexe+self.texteComplexeVenantDesFils
       self.label='BlocAmbigu'
       #print ('fin pour prepareDumpXSD pour', self.nom)

   def compare(self,autreMC):
       if self.label != autreMC.label : return False
       if self.arbrePossibles== autreMC.arbrePossible : return True
       return False

   def construitEntites(self, laListe):
       for mc in laListe :
           if mc.nom in self.entites.keys() : self.entites[mc.nom].append(mc)
           else : self.entites[mc.nom] = [mc,]
           if mc.label == 'BLOC' or  mc.label == 'BlocAmbigu':
              self.ajouteLesMCFilsAEntite(mc)
           

   def ajouteLesMCFilsAEntite(self,blocMc):
       for mcFilsNom in blocMc.entites.keys():
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
           

           

   def constructionArbrePossibles(self):
       #print ('construction pour FACT ambigu _______________', self.nom)
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
       #print ('dans X_factCompoAmbigue ne fait rien', self.nom, self.arbrePossibles)
       pass

   def dumpXsd(self, dansFactorisation=False, multiple = False, first=False):
       # on ne fait rien, tout a ete fait dans le init
       self.texteElt=substDsSequence.format(self.code,self.nomDuTypePyxb,0,1)

   def nomComplet(self) :
       print ('dans nomComplet pourquoi ?',self, self.nom)

       
   def factoriseEtCreeDump(self, laListe, indent=2 ,nomAppel=None):
       #print ('_______________________________ factoriseEtCreeDump')
       #print(self.nom, laListe, indent, nomAppel)
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

       for nomMC in aReduire.keys():
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
       print ('fin pour _______________________________', self.nom)
       return (maListeRetour)
       
       
   def ajouteAuxTextes(self,nomMC,indent) :
       #print ('ajouteAuxTextes', nomMC, self.nom, self.entites)
       #print ('ajouteAuxTextes', nomMC)
       #for i in self.entites.keys() : print (self.entites[i][0].nom)
       if (indent  > 3) : indent = indent - 3
       else : indent = 0
       if len(self.entites[nomMC]) == 1:
           mc=self.entites[nomMC][0]
           mc.dumpXsd(dansFactorisation=True)
           self.texteComplexe += '\t'*(indent) + mc.texteElt
           if mc.nomDuTypePyxb not in self.mcDejaDumpe :
              self.texteComplexeVenantDesFils += mc.texteComplexe
              self.texteSimple   += mc.texteSimple
              self.mcDejaDumpe.add(mc.nomDuTypePyxb)
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
           if mc.nomDuTypePyxb not in self.mcDejaDumpe :
              self.texteComplexeVenantDesFils += mc.texteComplexe
              self.texteSimple   += mc.texteSimple
              self.mcDejaDumpe.add(mc.nomDuTypePyxb)
           return
             
       # on ajoute le nom de l element
       self.entites[nomMC][0].dumpXsd(dansFactorisation=True,multiple=True,first=first)
       self.texteComplexe += '\t'*(indent) + self.entites[nomMC][0].texteElt
       texteSimpleUnion=debutSimpleType.format(self.entites[nomMC][0].nomDuTypePyxb)
       texteSimpleUnion+=debutUnion
       if len(listePourUnion) == 1 :
           mc=self.entites[nomMC][0]
           mc.dumpXsd(dansFactorisation=True,multiple=True,first=first)
           if mc.nomDuTypePyxb not in self.mcDejaDumpe :
              self.texteComplexeVenantDesFils += mc.texteComplexe
              self.texteSimple   += mc.texteSimple
              self.mcDejaDumpe.add(mc.nomDuTypePyxb)
       else :
           for e in listePourUnion :
               e.dumpXsd(dansFactorisation=True,multiple=True,first=first)
               if first and (e.nomDuTypePyxb not in self.mcDejaDumpe) :
                  self.texteComplexeVenantDesFils += e.texteComplexe
                  self.mcDejaDumpe.add(e.nomDuTypePyxb)
                  texteSimpleUnion += '\t'*(indent)+e.texteSimple
                  first=first * 0
           texteSimpleUnion += finUnion
       texteSimpleUnion+=fermeSimpleType
       self.texteSimple   += texteSimpleUnion
   


# ----------------------------------------
class X_definitionComposee (X_definition):
# ------------------------------------------
   
   def CreeTexteComplexeVenantDesFils(self,dansFactorisation=False):
       texteComplexeVenantDesFils=""
       blocsDejaDumpes=set()
       #for nom in self.ordre_mc:
       #  mcFils = self.entites[nom]
       #print (self.nom)
       for mcFils in self.mcXSD :
          if not (isinstance(mcFils, Accas.BLOC)) :
             mcFils.dumpXsd(dansFactorisation)
             self.texteComplexe += mcFils.texteElt
             self.texteSimple   += mcFils.texteSimple 
             texteComplexeVenantDesFils += mcFils.texteComplexe
             continue
          else   :
             #print (mcFils.nom)
             if hasattr(mcFils,'nomXML')  and mcFils.nomXML in blocsDejaDumpes and mcFils.nomXML != None : continue 
             if hasattr(mcFils,'nomXML')  and mcFils.nomXML != None: blocsDejaDumpes.add(mcFils.nomXML)
             mcFils.dumpXsd(dansFactorisation)
             self.texteComplexe += mcFils.texteElt
             self.texteSimple   += mcFils.texteSimple 
             texteComplexeVenantDesFils += mcFils.texteComplexe
       return texteComplexeVenantDesFils

   def dumpXsd(self, dansFactorisation=False, multiple = False, first=False):
       #print ('_________ dumpXsd___________', self.nom)
       if PourTraduction  : print (self.nom)
       self.prepareDumpXSD()
 
       self.getNomDuCodeDumpe()
       self.nomDuTypePyxb  = self.definitNomDuTypePyxb()
       self.texteSimple    = "" # on n ajoute pas de type simple

       self.traduitMinMax()
       # pour accepter les PROC et ...
       # 
       if self.aCreer :
          self.texteComplexe = debutTypeCompo.format(self.nomDuTypePyxb)
          if isinstance(self,X_OPER) or isinstance(self,X_PROC) : 
            self.texteComplexe += debutTypeCompoEtape.format(self.code)
          self.texteComplexe += debutTypeCompoSeq
          texteComplexeVenantDesFils=self.CreeTexteComplexeVenantDesFils(dansFactorisation)
          self.texteComplexe  = texteComplexeVenantDesFils + self.texteComplexe
          # la fin de l oper est traitee dans le dumpXSD de X_OPER
          if not isinstance(self,X_OPER ) : self.texteComplexe += finTypeCompoSeq
          if isinstance(self,X_PROC)      : self.texteComplexe += finTypeCompoEtape
          if not isinstance(self,X_OPER ) : self.texteComplexe += finTypeCompo
       else :
          self.texteComplexe = ""

       self.texteElt=eltCompoDsSequence.format(self.nom,self.nomDuCodeDumpe,self.nomDuTypePyxb,self.minOccurs,self.maxOccurs)
       #print (self.texteComplexe)
       #print ('------------------------------------------------',self.nom)

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
       for defFille in self.entites.keys():
           if defFille not in autreMC.entites.keys() : return False
           if not self.entites[defFille].compare(autreMC.entites[defFille]) : return False
       return True

   def prepareDumpXSD(self):
       #print (' ************************ prepareDumpXSD pour', self.nom)
       self.inUnion=False
       self.tousLesFils=[]
       self.mcXSD=[]
       for nomMC in self.ordre_mc:
           mc=self.entites[nomMC]
           self.mcXSD.append(mc)
           mc.prepareDumpXSD()
       self.chercheListesDeBlocsNonDisjointsAvecIndex()
       for l in list(self.listeDesBlocsNonDisjointsAvecIndex) :
           #print ('je traite ', l, self.besoinDeFactoriserTrivial(l))
           if not(self.besoinDeFactoriserTrivial(l)) : self.listeDesBlocsNonDisjointsAvecIndex.remove(l)
           else : self.factorise(l)
              #print (self.aUnPremierCommunDansLesPossibles(l))
           #if self.aUnPremierCommunDansLesPossibles(l) :
           #     print ('aUnCommunDansLesPossibles --> Factorisation')
           #else : self.listeDesBlocsNonDisjointsAvecIndex.remove(l)
           # trouver un cas test

   def chercheListesDeBlocsNonDisjointsAvecIndex(self):
       self.listeDesBlocsNonDisjointsAvecIndex=[]
       index=-1
       for nomChild in self.ordre_mc :
         child=self.entites[nomChild]
         index=index+1
         if child.label != 'BLOC' : continue
         if self.listeDesBlocsNonDisjointsAvecIndex == [] :
             self.listeDesBlocsNonDisjointsAvecIndex.append([(child,index),])
             continue
         vraimentIndependant=True
         for liste in list(self.listeDesBlocsNonDisjointsAvecIndex):
             independant=True
             for (bloc,indInListe) in liste :
                 if bloc.isDisjoint(child) : continue
                 if bloc.estLeMemeQue(child) : continue
                 independant=False
                 vraimentIndependant=False
             if not (independant) :
                 liste.append((child, index))
         if vraimentIndependant:
             self.listeDesBlocsNonDisjointsAvecIndex.append([(child,index),])
       # on nettoye la liste des blocs tous seuls
       for l in list(self.listeDesBlocsNonDisjointsAvecIndex) :
           if len(l) ==1 : self.listeDesBlocsNonDisjointsAvecIndex.remove(l)

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
       besoin=False
       lesPremiers=set()
       for mcBloc,indice in laListe  :
          mc=mcBloc.mcXSD[0]
          if mc.label == 'BLOC': return True
          if not(mc.statut=='o') : return True
          if mc.nom in lesPremiers  : return True
          lesPremiers.add(mc.nom)
       return False

   def factorise(self,liste):
       self.listeConstruction=liste
       indexDebut=liste[0][1]
       nomDebut=liste[0][0].nom
       indexFin=liste[-1][1]+1
       nomFin=liste[-1][0].nom
       nom=nomDebut+'_'+nomFin
       listeAFactoriser=[]
       for  i in range(indexDebut, indexFin) :
          listeAFactoriser.append((self.mcXSD[i],i))

       newListe=self.mcXSD[0:indexDebut]
       #print (newListe, newListe.__class__)
       #print ('je factorise dans -->', self.nom)
       monEltFacteur=X_compoFactoriseAmbigu(nom,listeAFactoriser,self)
       newListe.append(monEltFacteur)
       newListe=newListe+self.mcXSD[indexFin:]
       self.mcXSD=newListe
       #print (self.mcXSD)
       #for i in self.mcXSD : print (i.nom)

   def construitTousLesFils(self):
       for nomChild in self.ordre_mc :
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
       self.texteComplexe += operAttributeName
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
   def dumpXsd(self, dansFactorisation=False, multiple = False, first=False):
       self.tousLesFils=[]
       
       self.getNomDuCodeDumpe()
       # dans ce cas les blocs successifs sont identiques et on ne dumpe que le 1er 

       self.nomDuTypePyxb  = self.definitNomDuTypePyxb()
       self.texteSimple    = "" # on n ajoute pas de type simple

       # Pour les blocs le minOccurs vaut 0 et le max 1
       #print ('dumpXsd Bloc', self.nom, self.aCreer)
       if self.aCreer :
          self.texteComplexe = debutTypeSubst.format(self.nomDuTypePyxb)
          texteComplexeVenantDesFils=self.CreeTexteComplexeVenantDesFils(dansFactorisation)
          self.texteComplexe  = texteComplexeVenantDesFils + self.texteComplexe
          self.texteComplexe += finTypeSubst
       else :
          self.texteComplexe = ""

       self.texteElt=substDsSequence.format(self.code,self.nomDuTypePyxb,0,1)

       #print ('------------------------------------------------')

   def compare(self,autreMC):
       if self.label != autreMC.label : return False
       if self.inUnion == True or autreMC.inUnion == True : return False
       if hasattr(self,'nomXML') and hasattr(autreMC,'nomXML') and self.nomXML==autreMC.nomXML and self.nomXML != None : return True
       for attr in ( 'condition', 'regles', ):
           val1=getattr(self,attr)
           val2=getattr(autreMC,attr)
           if val1 != val2 : return False
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
   def dumpXsd(self, dansFactorisation=False, multiple = False, first=False):
       #print ('_______________' , '*******************', 'je passe la dans dumpXsd SIMP', self.nom, multiple, first)
       if PourTraduction  : print (self.nom)
       self.prepareDumpXSD()
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
       if not multiple : 
          self.nomDuTypePyxb   = self.definitNomDuTypePyxb()
          if first : self.aCreer = True
       elif first :
          self.nomDuTypePyxb   = self.definitNomDuTypePyxb(forceACreer=1)
          self.aCreer = True
       #else : print ('multiple and not first', self.aCreer)

    
       
       # on se sert des listes ou non pour  la gestion des minOccurs /maxOccurs est > 0
       if self.statut =='f' : minOccurs = 0
       else                 : minOccurs = 1
       if dansFactorisation : minOccurs = 1

       #print ('minOccurs',minOccurs)
       # le defaut est dans l elt Name -> tester la coherence d existence avec Accas
       # regles Accas
       if (hasattr (self, 'nomXML')) and self.nomXML != None : nomUtil=self.nomXML
       else : nomUtil = self.nom

       # pas d elt si on est dans multiple
       # sauf si on est le '1er'  dans un element ambigu 
       if not multiple : 
          #print ('je passe la pas multiple')
          if self.defaut : 
             if self.max > 1 or self.max == '**' or self.max ==  float('inf') : 
                # a revoir pour les tuples avec defaut
                txtDefaut=""
                for val in self.defaut : txtDefaut+=str(val) +" "
                self.texteElt = eltWithDefautDsSequence.format(nomUtil,self.code,self.nomDuTypePyxb,minOccurs,1,txtDefaut)
             else :
                if str(self.defaut) == 'True' : txtDefaut = 'true'
                else : txtDefaut = str(self.defaut)
                self.texteElt = eltWithDefautDsSequence.format(nomUtil,self.code,self.nomDuTypePyxb,minOccurs,1,txtDefaut)
          else : self.texteElt = eltDsSequence.format(nomUtil,self.code,self.nomDuTypePyxb,minOccurs,1)
       elif first: 
          self.texteElt = eltDsSequence.format(nomUtil,self.code,self.nomDuTypePyxb,1,1)
    
       # self.aCreer est mis a jour ds definitNomDuTypePyxb
       # ou si elt est le 1er d une liste identique
       if not self.aCreer : return
 
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


   def prepareDumpXSD(self):
       self.inUnion=False
       if self.statut   ==  'f' :
          self.arbrePossibles = (self.nom,[])
       else :
          self.arbrePossibles = (self.nom,)
       self.mcXSD=[]



   def traduitType(self):
       # il faut traduire le min et le max
       # il faut ajouter les regles
       # il faut gerer les types tuple et fichier
       if hasattr(self.type[0], 'ntuple') : 
          try :
             leType=self.validators.typeDesTuples[0]
             for i in range(self.type[0].ntuple):
                 if self.validators.typeDesTuples[i] != leType : return ('XXXXXXXX')
             typeATraduire=leType
          except : 
             return ('XXXXXXXX')
       else : 
             typeATraduire=self.type[0]
       if not (typeATraduire in list(dictNomsDesTypes.keys())) :
          if (isinstance(typeATraduire, Accas.ASSD) or issubclass(typeATraduire, Accas.ASSD)) : 
             # cas d une creation
             cata = CONTEXT.getCurrentCata() 
             if len(self.type) == 2 and self.type[1]=='createObject' : 
                if typeATraduire.__name__ not in list(cata.dictTypesASSDorUserASSDCrees) :
                    cata.dictTypesASSDorUserASSDCrees[typeATraduire.__name__]=[self,]
                else :
                    cata.dictTypesASSDorUserASSDCrees[typeATraduire.__name__].append(self)
                return 'xs:string'

             # cas d une consommation
             if typeATraduire not in list(cata.dictTypesASSDorUserASSDUtilises) :
                cata.dictTypesASSDorUserASSDUtilises[typeATraduire]=[self,]
             else :
                cata.dictTypesASSDorUserASSDUtilises[typeATraduire].append(self,)
             return 'xs:string'
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
           self.texteCata += eltCataPPal.format(self.code,self.code,self.code)
        else :
           self.texteCata += eltAbstraitCataFils.format(self.implement,self.nomDuXsdPere,self.nomDuXsdPere)
           self.texteCata += eltCataFils.format(self.implement,self.nomDuXsdPere,self.nomDuXsdPere,self.nomDuXsdPere)
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
            print (texteDesUserASSD)
            print (texteDesFields)
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

        self.texteXSD += texteFin



        #if not PourTraduction : print (self.texteXSD)
        dico = {}
        for  k in list(cata.dictTypesXSD.keys()):
             if len(cata.dictTypesXSD[k]) > 1:
                index=0
                dico[k]={}
                for definition in cata.dictTypesXSD[k] : 
                    nom=definition.nomComplet()
                    if index == 0 : dico[k][nom]=k+str(index)
                    else :          dico[k][nom]=k+str(index)
                    index=index+1
  
        #import pprint
        #if (not PourTraduction) and  (dico != {}) : pprint.pprint(dico)
        print ('__________________________ decommenter pour le texteXSD________________________')
        print (self.texteXSD)
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
            #c.texteElt=eltCompoDsSequenceInExtension.format(c.nom,self.code,c.nomDuTypePyxb)
            c.texteElt=eltEtape.format(c.nom,self.implement,c.nomDuTypePyxb,self.implement)
            self.texteCata   += c.texteElt
