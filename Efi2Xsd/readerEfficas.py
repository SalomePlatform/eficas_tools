#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import raw.efficas as efficas
import types

sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))


from Accas import *

# traiter le cas des tuples

# ds l init du SIMP il manque siValide et fenetreIhm

from mapDesTypes import dictSIMPEficasXML, dictSIMPXMLEficas
from mapDesTypes import dictFACTEficasXML, dictFACTXMLEficas
from mapDesTypes import dictPROCEficasXML, dictPROCXMLEficas
from mapDesTypes import listeParamDeTypeTypeAttendu, listeParamDeTypeStr, dicoPourCast
from mapDesTypes import listeParamEnListeSiMax,  listeParamTjsEnListe

# ------------------------------
class objetDefinitionAccas:
# ------------------------------

   def argumentXMLToEficas(self):
   # ---------------------------
      # Attention, pas de validation pour l instant
      # il faut verifier la coherence entre les types contenus dans defaut, sug ... et le typeAttendu
      # tout cela dans une fonction verifie pas faite -)

      # Recuperation parametres
      self.dictArgsEficas={}
      for nomXMLArg in dir(self) :
          if nomXMLArg in self.dictATraiter :
              nomEficasArg=self.dictATraiter[nomXMLArg]
              argu=getattr(self,nomXMLArg)
              if argu==None : continue

              if type(nomEficasArg) == types.DictionaryType:
                 for nomXML in list(nomEficasArg.keys()):
                      arguDecoupe=getattr(argu,nomXML)
                      nomEficasDecoupe=nomEficasArg[nomXML]
                      if arguDecoupe == None : continue
                      self.dictArgsEficas[nomEficasDecoupe]=arguDecoupe
              else :
                self.dictArgsEficas[nomEficasArg] = argu
                    
      # Cast dans le bon type des parametres si necessaire
      if 'min' in list(self.dictArgsEficas.keys()): 
            self.dictArgsEficas['min']=int(self.dictArgsEficas['min'])

      if 'max' in list(self.dictArgsEficas.keys()): 
            if self.dictArgsEficas['max']== -1   :  self.dictArgsEficas['max']="**"
            else                                 :  self.dictArgsEficas['max']=int(self.dictArgsEficas['max'])

      #for param in list(self.dictArgsEficas.keys()):
      #    if param in listeParamDeTypeStr :
      #       self.dictArgsEficas[param]=unicode(self.dictArgsEficas[param])
      
      # Pour commodite ? pas sur que cela soit necessaire
      #self.strNomObj=str(self.nom)
          
         
   def getAccasEquivalent(self):
   # ---------------------------
       return self.nom, self.objAccas
#

# ---------------------------------------------------------
class objetComposeDefinitionAccas (objetDefinitionAccas):
# ---------------------------------------------------------
    def exploreArbre(self):
    # --------------------------
      liste=[]
      for obj in self.content(): liste.append(obj)
      liste.reverse()
      # PNPNPN essayer de comprendre reverse ou non

      for obj in liste: 
          if  hasattr(obj,'explore') : obj.explore ()
          if  hasattr(obj,'getAccasEquivalent') : 
              nom,objetAccas=obj.getAccasEquivalent()
              self.dictArgsEficas[nom]=objetAccas
     
# ----------------------------------------------------
class monSIMP (efficas.T_SIMP,  objetDefinitionAccas):
# ----------------------------------------------------

   def explore(self):
   # --------------------
   # 2 arguments pour ne pas avoir a differencier les appels explore
      self.dictATraiter= dictSIMPXMLEficas
      self.argumentXMLToEficas()

      self.objAccas=A_SIMP.SIMP(**self.dictArgsEficas)
      self.objAccas.nom=self.nom
      #self.strNomObj=str(self.nom)

   def argumentXMLToEficas(self):
   # ----------------------------
      objetDefinitionAccas.argumentXMLToEficas(self)
      self.convertitEnListes()
      self.convertitLesTypes()

   def estListe(self):
   # ---------------
       if hasattr(self,'max') and self.max > 1 : return True
       else : return False

   def attendTuple(self):
   # -------------------
       return False

   def convertitEnListes(self):
   # ------------------------
   # Cas des Tuples non traites
       for param in listeParamTjsEnListe :
          if  param in self.dictArgsEficas :
              if not self.attendTuple() :
                 self.dictArgsEficas[param]=[self.dictArgsEficas[param],]

       if self.estListe() :
         for param in listeParamEnListeSiMax:
             if param in self.dictArgsEficas :
                if not self.attendTuple() :
                   self.dictArgsEficas[param]=[self.dictArgsEficas[param],]

   def convertitLesTypes(self):
   # ------------------------
   # Cas des Tuples non traites

       typeAttendu = self.dictArgsEficas['typ']
       if typeAttendu in list(dicoPourCast.keys()):
          for param in listeParamDeTypeTypeAttendu :
             if param in list(self.dictArgsEficas.keys()):
                castDsLeTypeAttendu=dicoPourCast[typeAttendu]
                valeurACaster=self.dictArgsEficas[param].typesimple
                if not isinstance(valeurACaster, (list, tuple)) :
                   val=castDsLeTypeAttendu(valeurACaster)
                   self.dictArgsEficas[param]=val
                else :
                   print (dir(self.dictArgsEficas[param]))
       print ('==========',  self.dictArgsEficas)


# -------------------------------------------------------
class monFACT(efficas.T_FACT, objetComposeDefinitionAccas):
# -------------------------------------------------------
   def explore(self):
   # --------------------
      #print "je passe dans  explore pour FACT ", self.nom

      self.dictATraiter= dictFACTXMLEficas
      self.argumentXMLToEficas()
      self.exploreArbre()
      self.objAccas=A_FACT.FACT(**self.dictArgsEficas)


# ---------------------------------------------------------
class monPROC(efficas.T_PROC, objetComposeDefinitionAccas):
# ---------------------------------------------------------
   def explore(self,cata):
   # --------------------
      #print "je passe dans  explore pour PROC ", self.nom
      self.dictATraiter= dictPROCXMLEficas
      self.argumentXMLToEficas()
      self.exploreArbre()
      self.dictArgsEficas['op']=None

      self.objAccas=A_PROC.PROC(**self.dictArgsEficas)
      setattr(cata, self.nom,self.objAccas)


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


   xml = open('cata_test1.xml').read()
   #xml = open('Cata_MED_FAM.xml').read()
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
