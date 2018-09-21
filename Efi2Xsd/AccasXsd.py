#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import types

# CONTEXT est accessible (__init__.py de Noyau)

#import raw.efficas as efficas
sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))

# ds l init du SIMP il manque siValide et fenetreIhm

from mapDesTypes import dictSIMPEficasXML, dictSIMPXMLEficas
from mapDesTypes import dictFACTEficasXML, dictFACTXMLEficas
from mapDesTypes import dictPROCEficasXML, dictPROCXMLEficas
from mapDesTypes import dictOPEREficasXML, dictOPERXMLEficas
from mapDesTypes import dictBLOCEficasXML, dictBLOCXMLEficas
from mapDesTypes import dictPourCast, dictNomsDesTypes
from mapDesTypes import listeParamDeTypeTypeAttendu, listeParamDeTypeStr, dictPourCast
from mapDesTypes import listeParamTjsSequence, listeParamSelonType
from mapDesTypes import Tuple


from balises import *

# -----------------
class X_definition:
# -----------------

   def getCode(self):
       if hasattr(self,'code') : return
       obj=self
       while ( not hasattr(obj,'code') ): obj=obj.pere
       self.code = obj.code

   #def genealogie(self,n):
   #    texte=self.nom
   #    obj=self
   #    j=1
   #    while ( hasattr(obj,'pere') ):
   #        texte=obj.pere.nom+'_'+texte
   #        obj=obj.pere
   #        j=j+1
   #        if j > n : return (True, 'T_'+texte)
   #    return (False, 'T_'+texte)

   def definitNomDuTypePyxb(self):
       self.aCreer = True
       cata = CONTEXT.getCurrentCata() 
       nom='T_'+self.nom
       if not (nom in cata.dictTypesXSD.keys()) :
          cata.dictTypesXSD[nom] = [self,]
          return nom
       self.aCreer = False
       if nom == 'T_Consigne' : return nom
       listePossible=cata.dictTypesXSD[nom]
       indice=0
       while (indice < len(listePossible)) :
          objAComparer=listePossible[indice]
          if self.compare(objAComparer) : return objAComparer.nomDuTypePyxb
          indice += 1
       self.aCreer = True
       cata.dictTypesXSD[nom].append(self)
       nomAlter='T_'+self.nom+'_'+str(indice)
       return nomAlter

  # def existeDeja(self,nom):
  #     if nom in cata.dictTypesXSD.keys() :
  #         self.aCreer = False
  #         return cata.dictTypesXSD[nom]
  #     else :
  #         cata.dictTypesXSD[nom] = self
  #         return None

# ----------------------------------------
class X_definitionComposee (X_definition):
# ----------------------------------------
   
   def CreeTexteComplexeVenantDesFils(self):
       texteComplexeVenantDesFils=""
       for nom in self.ordre_mc:
          mcFils = self.entites[nom]
          mcFils.dumpXsd()
          self.texteComplexe += mcFils.texteElt
          self.texteSimple   += mcFils.texteSimple 
          texteComplexeVenantDesFils += mcFils.texteComplexe
       return texteComplexeVenantDesFils

   def dumpXsd(self):
       #print ('------------------------------------------------')
       #print ('dumpXsd de ' , self.nom)
 
       self.getCode()
       self.nomDuTypePyxb  = self.definitNomDuTypePyxb()
       self.texteSimple    = "" # on n ajoute pas de type simple

       self.traduitMinMax()
       # pour accepter les PROC et ...
       # 
       if self.aCreer :
          self.texteComplexe = debutTypeCompo.format(self.nomDuTypePyxb,self.minOccurs,self.maxOccurs)
          texteComplexeVenantDesFils=self.CreeTexteComplexeVenantDesFils()
          self.texteComplexe  = texteComplexeVenantDesFils + self.texteComplexe
          self.texteComplexe += finTypeCompo
       else :
          self.texteComplexe = ""

       minDsSequence=0
       if hasattr(self, 'statut') and self.statut=='f'  : minDsSequence=0
       maxDsSequence=1
       if self.label in ('BLOC', 'FACT'):
          self.texteElt=eltCompoDsSequence.format(self.nom,self.code,self.nomDuTypePyxb,minDsSequence,maxDsSequence)
       else :
          self.texteElt=eltCompoDsSequenceSiProc.format(self.nom,self.code,self.nomDuTypePyxb)
       #print (self.texteComplexe)
       #print ('------------------------------------------------')

   def traduitMinMax(self):
   # ____________________
   # valable pour bloc, proc et oper
      self.minOccurs = 0
      self.maxOccurs = 1

   def compare(self,autreMC):
       if self.label != autreMC.label : return False
       for attr in (  'regles', 'fr',  'defaut', 'min' ,'max', 'position' , 'docu' ) :
           val1=getattr(self,attr)
           val2=getattr(autreMC,attr)
           if val1 != val2 : return False
       for defFille in self.entites.keys():
           if defFille not in autreMC.entites.keys() : return False
           if not self.entites[defFille].compare(autreMC.entites[defFille]) : return False
       return True

# ---------------------------------
class X_FACT (X_definitionComposee):
#--------- ------------------------
   def traduitMinMax(self):
       if self.max     == '**' or self.max  == float('inf') : self.maxOccurs="unbounded"
       else :                                                 self.maxOccurs = self.max
       self.minOccurs = self.min
       if self.statut =='f' : self.minOccurs=0

# ---------------------------------
class X_OPER (X_definitionComposee):
# ---------------------------------
    pass

# ----------------------------------
class X_PROC (X_definitionComposee):
#-----------------------------------
    pass

#-----------------------------------
class X_BLOC (X_definitionComposee):
#-----------------------------------
   def dumpXsd(self):
       #print ('------------------------------------------------')
       #print ('dumpXsd de ' , self.nom)
 
       self.getCode()
       self.nomDuTypePyxb  = self.definitNomDuTypePyxb()
       self.texteSimple    = "" # on n ajoute pas de type simple

       # Pour les blocs le minOccurs vaut 0 et le max 1
       if self.aCreer :
          self.texteComplexe = debutTypeSubst.format(self.nomDuTypePyxb)
          texteComplexeVenantDesFils=self.CreeTexteComplexeVenantDesFils()
          self.texteComplexe  = texteComplexeVenantDesFils + self.texteComplexe
          self.texteComplexe += finTypeSubst
       else :
          self.texteComplexe = ""

       self.texteElt=substDsSequence.format(self.code,self.nomDuTypePyxb,0,1)

       #print ('------------------------------------------------')

   def compare(self,autreMC):
       if self.label != autreMC.label : return False
       for attr in ( 'condition', 'regles', ):
           val1=getattr(self,attr)
           val2=getattr(autreMC,attr)
           if val1 != val2 : return False
       for defFille in self.entites.keys():
           if defFille not in autreMC.entites.keys() : return False
           if not self.entites[defFille].compare(autreMC.entites[defFille]) : return False
       return True


#--------------------------------
class X_SIMP (X_definition):
#--------------------------------
   def dumpXsd(self):
       #print ('exploreObjet SIMP')
       self.getCode()
       self.aCreer = True

       #  --> homonymie on peut utiliser genealogie
       #self.traduitMinMax()
       #self.traduitValMinValMax()
       self.nomDuTypeDeBase = self.traduitType()
       self.nomDuTypePyxb   = self.definitNomDuTypePyxb()
       if self.aCreer == True :
         if self.into != None:
           self.texteSimple   =  debutTypeSimpleWithInto.format (self.nomDuTypePyxb, self.nomDuTypeDeBase)
           for val in self.into :
               self.texteSimple += typeSimpleWithInto.format(val)
           self.texteSimple  += finTypeSimpleWithInto
         else :
           self.texteSimple     = typeSimple.format(self.nomDuTypePyxb, self.nomDuTypeDeBase)
       else :
         # le type existe deja
         self.texteSimple=""
       self.texteComplexe   = ""

       # on se sert des listes si maxOccurs est > 0
       # a gerer dans le dump
       if self.statut =='f' : minOccurs = 0
       else : 	              minOccurs = 1
       self.texteElt = eltDsSequence.format(self.nom,self.code,self.nomDuTypePyxb,minOccurs,1)
 

   def traduitType(self):
       # il faut traduire le min et le max
       # il faut ajouter les regles
       # il faut gerer les types tuple et fichier

       if hasattr(self.type[0], 'label') and self.type[0].label == "Tuple"  : return ('XXXXXXXX')
       return dictNomsDesTypes[self.type[0]]
  
   def traduitValMinValMax(self):
       self.maxInclusive=self.val_max
       self.minInclusive=self.val_min
       if self.val_min == float('-inf') and val_max== float('inf') : return
       print ('il faut affiner le type du SIMP ', self.nom)
       if self.val_max == '**' or self.val_max == float('inf') : self.maxInclusive=None
       else : self.maxInclusive = self.val_max
       if self.val_min == '**' or self.val_max == float('-inf') : self.maxInclusive=None
       else : self.minInclusive = self.val_min
       
   def traduitMinMax(self):
       if self.min == 1 and self.max == 1 :  return
       print ('il faut creer une liste ' , self.nom)
 
   def compare(self,autreMC):
       if self.label != autreMC.label : return False
       for attr in ( 'type', 'ang', 'fr', 'into', 'intoSug' , 'siValide', 'defaut', 'min' ,'max' ,'homo' ,'position' ,'val_min' , 'val_max' , 'docu' , 'validators' , 'sug' ) :
           val1=getattr(self,attr)
           val2=getattr(autreMC,attr)
           if val1 != val2 : return False
       return True

#-----------------
class X_JDC_CATA :
#-----------------

    def dumpXsd(self):
       
        self.texteSimple   = ""
        self.texteComplexe = ""
        self.nomDuTypePyxb='T_'+self.code
        self.texteCata = debutTypeCata.format(self.nomDuTypePyxb)
        for commande in  self.commandes :
            commande.code=self.code
            commande.dumpXsd()
            self.texteSimple += commande.texteSimple
            self.texteSimple += commande.texteComplexe
            self.texteCata   += commande.texteElt
        self.texteCata += finTypeCata
        self.texteElt=eltCata.format(self.code,self.code, self.nomDuTypePyxb)

        self.texteXSD  = texteDebut.format(self.code,self.code,self.code)
        self.texteXSD += self.texteSimple
        self.texteXSD += self.texteCata
        self.texteXSD += self.texteElt
        self.texteXSD += texteFin
        #print (self.texteSimple)
        #print (self.texteCata)
        #print (self.texteElt)
        print (self.texteXSD)
   
