#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import types

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


from balises import *

# -----------------
class X_definition:
# -----------------

   def getCode(self):
       if hasattr(self,'code') : return
       obj=self
       while ( not hasattr(obj,'code') ): obj=obj.pere
       self.code = obj.code

   def genealogie(self):
       texte=self.nom
       obj=self
       while ( hasattr(obj,'pere') ):
           texte=obj.pere.nom+'_'+texte
           obj=obj.pere
       return 'T_'+texte

   def nomSimple(self):
       return 'T_'+self.nom
       #return self.genealogie()



# ----------------------------------------
class X_definitionComposee (X_definition):
# ----------------------------------------
   

   def dumpXsd(self):
       #print ('------------------------------------------------')
       #print ('dumpXsd de ' , self.nom)
 
       self.getCode()
       self.nomDuTypeCree  = self.nomSimple()
       self.texteSimple    = "" # on n ajoute pas de type simple

       self.texteComplexe = debutTypeComplexe.format(self.nomDuTypeCree)
       texteComplexeVenantDesFils=""
       for nom in self.ordre_mc:
          mcFils = self.entites[nom]
          mcFils.dumpXsd()
          self.texteComplexe += mcFils.texteElt
          self.texteSimple   += mcFils.texteSimple 
          texteComplexeVenantDesFils += mcFils.texteComplexe
       self.texteComplexe += finTypeComplexe
       self.texteComplexe  = texteComplexeVenantDesFils + self.texteComplexe

       self.traduitMinMax()
       self.texteElt=eltDsSequence.format(self.nom,self.code,self.nomDuTypeCree,self.minOccurs,self.maxOccurs)

   def traduitMinMax(self):
   # ____________________
   # valable pour bloc, proc et oper
      self.minOccurs = 0
      self.maxOccurs = 1

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
      X_definitionComposee.dumpXsd(self)

#--------------------------------
class X_SIMP (X_definition):
#--------------------------------
   def dumpXsd(self):
       #print ('exploreObjet SIMP')
       self.getCode()

       #  --> homonymie on peut utiliser genealogie
       #self.traduitMinMax()
       #self.traduitValMinValMax()
       self.nomDuTypeDeBase = self.traduitType()
       self.nomDuTypeCree   = self.nomSimple()
       self.texteSimple     = typeSimple.format(self.nomDuTypeCree, self.nomDuTypeDeBase)
       self.texteComplexe   = ""

       # on se sert des listes si maxOccurs est > 0
       if self.statut =='f' : minOccurs = 0
       else : 	              minOccurs = 1
       self.texteElt = eltDsSequence.format(self.nom,self.code,self.nomDuTypeCree,minOccurs,1)
 

   def traduitType(self):
       # il faut traduire le min et le max
       # il faut ajouter les regles
       # il faut gerer les types tuple et fichier
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


#-----------------
class X_JDC_CATA :
#-----------------

    def dumpXsd(self):
        self.texteSimple   = ""
        self.texteComplexe = ""
        self.nomDuTypeCree='T_'+self.code
        self.texteCata = debutTypeCata.format(self.nomDuTypeCree)
        for commande in  self.commandes :
            commande.code=self.code
            commande.dumpXsd()
            self.texteSimple += commande.texteSimple
            self.texteSimple += commande.texteComplexe
            self.texteCata   += commande.texteElt
        self.texteCata += finTypeCata
        self.texteElt=eltCata.format(self.code, self.nomDuTypeCree)
        print (self.texteSimple)
        print (self.texteComplexe)
        print (self.texteCata)
        print (self.texteElt)
   
