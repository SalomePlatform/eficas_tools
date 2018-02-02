#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import raw.efficas as efficas
import types

sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))


from Accas import *


# Attention pas d heritage possible (cf doc pyxbe)
# bizarre le comportement de max est different entre les facts et les simps ?

dictSIMPEficasXML= { 'typ'    : 'typeAttendu', 'statut'     : 'statut', 
                     'min_occurs': 'min'        , 'max_occurs' : 'max', 
                     'homo'      : 'homo'       , 'position'   : 'portee', 
                     'validators': 'validators' , 'sug'        : 'valeur_sugg',
                     'defaut'    : 'valeurDef'  , 'into'       : ('plageValeur','into'), 
                     'val_min'   : ('plageValeur','borne_inf') , 'val_max'    : ('plageValeur','borne_sup'),
                     'ang'       : ('doc','ang')               , 'fr'         : ('doc','fr',)   ,
                     'docu'      : ('doc','docu'),}
 
dictSIMPXMLEficas = {'doc' : {'fr' : 'fr' , 'ang' : 'ang' , 'docu' : 'docu' },
		     'plageValeur' : {'borne_sup' : 'val_max' , 'into' : 'into' , 'borne_inf' : 'val_min' ,},
		     'statut' : 'statut' , 'validators' : 'validators' , 'homo' : 'homo' ,
		     'valeurDef' : 'defaut' ,  'min_occurs' : 'min' ,
		     'valeur_sugg' : 'sug' , 'portee' : 'position' , 'max_occurs' : 'max' , }

dictFACTXMLEficas = {'doc' : {'fr' : 'fr' , 'ang' : 'ang' , 'docu' : 'docu' },
		     'statut' : 'statut' , 'validators' : 'validators' ,
		     'min_occurs' : 'min' , 'max_occurs' : 'max' , }

# ------------------------------
class monSIMP (efficas.T_SIMP):
# ------------------------------

   def explore(self,cata):
      #print "je passe dans  explore pour SIMP ", self.nom
      self.dictArgsEficas={}
      self.dictArgsEficas['typ']=self.typeAttendu
      for nomXMLArg in dir(self) :
          if nomXMLArg in dictSIMPXMLEficas.keys() :
              nomEficasArg=dictSIMPXMLEficas[nomXMLArg]
              argu=getattr(self,nomXMLArg)
              if argu==None : continue
              if nomEficasArg == 'defaut' : print (argu); 
              if nomEficasArg == 'defaut' : print (dir(argu)); 
              if nomEficasArg == 'defaut' : print (argu.value)
              #if nomEficasArg == 'defaut' : print (efficas.T_I(argu))
              if nomEficasArg == 'defaut' : print (argu.content())
              if type(nomEficasArg) == types.DictionaryType:
                 for nomXML in nomEficasArg.keys():
                      arguDecoupe=getattr(argu,nomXML)
                      nomEficasDecoupe=nomEficasArg[nomXML]
                      self.dictArgsEficas[nomEficasDecoupe]=arguDecoupe
              else :
                 self.dictArgsEficas[nomEficasArg] = argu
                    
      if 'min' in self.dictArgsEficas.keys(): self.dictArgsEficas['min']=int(self.dictArgsEficas['min'])
      if 'max' in self.dictArgsEficas.keys(): 
            if self.dictArgsEficas['max']== -1   :  self.dictArgsEficas['max']="**"
            else                                 :  self.dictArgsEficas['max']=int(self.dictArgsEficas['max'])
      self.objAccas=A_SIMP.SIMP(**self.dictArgsEficas)
      self.objAccas.nom=self.nom
      self.strNomObj=str(self.nom)
     
   def getAccasEquivalent(self):
       return self.strNomObj, self.objAccas

# ------------------------------
class monPROC(efficas.T_PROC):
# ------------------------------
   def explore(self,cata):
      #print "je passe dans  explore pour PROC ", self.nom
      self.dictConstruction={}
      self.dictConstruction['nom']=self.nom
      liste=[]
      for obj in self.content(): liste.append(obj)
      liste.reverse()
      for obj in liste: 
          if  hasattr(obj,'explore') : obj.explore (cata)
          if  hasattr(obj,'getAccasEquivalent') : 
              nom,objetAccas=obj.getAccasEquivalent()
              self.dictConstruction[nom]=objetAccas
      self.dictConstruction['op']=None
      self.objAccas=A_PROC.PROC(**self.dictConstruction)
      self.strNomObj=str(self.nom)
      setattr(cata, self.strNomObj,self.objAccas)


# ------------------------------
class monFACT(efficas.T_FACT):
# ------------------------------
   def explore(self,cata):
      #print "je passe dans  explore pour FACT ", self.nom
      self.dictConstruction={}

      for nomXMLArg in dir(self) :
          if nomXMLArg in dictFACTXMLEficas.keys() :
              nomEficasArg=dictFACTXMLEficas[nomXMLArg]
              argu=getattr(self,nomXMLArg)
              if argu==None : continue
              argu=str(argu)
              if type(nomEficasArg) == types.DictionaryType:
                 for nomXML in nomEficasArg.keys():
                      arguDecoupe=getattr(argu,nomXML)
                      nomEficasDecoupe=nomEficasArg[nomXML]
                      self.dictConstruction[nomEficasDecoupe]=arguDecoupe
              else :
                 self.dictConstruction[nomEficasArg] = argu
      if 'min' in self.dictConstruction.keys(): self.dictConstruction['min']=int(self.dictConstruction['min'])
      if 'max' in self.dictConstruction.keys(): 
            if self.dictConstruction['max']== '-1' :  self.dictConstruction['max']="**"
            else                                 :  self.dictConstruction['max']=int(self.dictConstruction['max'])
      liste=[]
      for obj in self.content(): liste.append(obj)
      liste.reverse()
      for obj in liste: 
          if  hasattr(obj,'explore') : obj.explore(cata)
          if  hasattr(obj,'getAccasEquivalent') : 
              nom,objetAccas=obj.getAccasEquivalent()
              self.dictConstruction[nom]=objetAccas
      
      self.objAccas=A_FACT.FACT(**self.dictConstruction)
      self.strNomObj=str(self.nom)

   def getAccasEquivalent(self):
       return self.strNomObj, self.objAccas


# ------------------------------
class monCata(efficas.T_cata):
# ------------------------------
   def exploreCata(self):
   # On positionne le contexte ACCAS
      self.VERSION_CATALOGUE='V1'
      self.JdC = JDC_CATA (code = 'MED', execmodul = None,)
      self.fromXML=1
      objAExplorer=self.commandes[0]
      for obj in objAExplorer.content(): 
         if  hasattr(obj,'explore') : obj.explore(self)
      #print dir(self.JdC)
      
     

efficas.T_SIMP._SetSupersedingClass(monSIMP)
efficas.T_FACT._SetSupersedingClass(monFACT)
efficas.T_PROC._SetSupersedingClass(monPROC)
efficas.T_cata._SetSupersedingClass(monCata)

if __name__ == "__main__":
#   print dir(efficas)
#   print dir(efficas.T_SIMP)


   xml = open('Cata_MED_FAM.xml').read()
   SchemaMed = efficas.CreateFromDocument(xml)
   SchemaMed.exploreCata()
   #print dir(SchemaMed)
   #print dir(SchemaMed.FAS)
   #print SchemaMed.FAS

   #print dir(efficas.T_SIMP)
   #print dir(efficas.T_SIMP)

   #for maCommande in monCata.commandes :
   #    for monProc in maCommande.PROC:
   #        for monFact in monProc.FACT:
   #            for simp in monFact.SIMP:
   #                simp.creeAccasEquivalent()
