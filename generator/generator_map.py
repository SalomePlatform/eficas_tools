# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
   Ce module contient le plugin generateur de fichier au format
   SEP pour EFICAS.

"""
import traceback
import types,string,re,os

from generator_python import PythonGenerator
try :
   sys.path.append(os.path.join(os.getenv('MAP_DIRECTORY'),'classes/python/'))
   from class_MAP_parameters import *
except :
   pass



def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins
      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'MAP',
        # La factory pour creer une instance du plugin
          'factory' : MapGenerator,
          }


class MapGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et
      un texte au format py

   """
   # Les extensions de fichier permis?
   extensions=('.map',)


   def initialise(self,config):
      self.config=config
      self.nom_racine=self.config.PATH_STUDY+"/"+self.config.NAME_SCHEME+"/"
      if not( os.path.exists(self.nom_racine)):
         os.makedirs(self.nom_racine)
      self.listeCODE=[]
      self.text=""
      self.textCode=""
      self.texteExecution=""
      self.ssCode=self.config.appli.ssCode

   def verifie(self):
      print 'verification generique'

   def gener(self,obj,format='brut',config=None):
      print 'generation dans generator_map'
      self.initialise(config)
      text=PythonGenerator.gener(self,obj,format)
      self.verifie()
      self.generePythonMap("non")
      return text

   def generRUN(self,obj,format='brut',config=None,):
      print 'generRUN dans generator_map'
      self.initialise(config)
      text=PythonGenerator.gener(self,obj,format)
      self.verifie()
      self.generePythonMap("oui") 
      return self.texteExecution


   def generRUNYACS(self,obj,format='brut',config=None,nomFichier=None):
      self.initialise(config)
      text=PythonGenerator.gener(self,obj,format)
      import sys
      sys.path.append('/local/noyret/Salome_5.1.3/Install/YACS/lib/python2.5/site-packages/salome/')
      self.verifie()
      import monCreateYacs
      self.monSchema=monCreateYacs.getSchema(config)
      self.proc=self.monSchema.createProc()
      for elt in self.listeCODE:
          code=elt.keys()[0]
          dico=elt[code]
          if code in self.__class__.__dict__.keys():
             codeYACS=str(code)+"YACS"
             if hasattr(self.monSchema, codeYACS): 
                fct=getattr(self.monSchema, codeYACS)
                fct(self.proc,dico)
      self.monSchema.write_yacs_proc(self.proc,str(nomFichier))

   def generePythonMap(self,execution) :
      '''
         self.dictMCVal est un dictionnaire qui est indexe par le nom du code (exple PYGMEE)
         la valeur associee a la clef est egalement un dictionnaire 
         ce dictionnaire a pour clef la genealogie du MCSimp suivi de sa valeur

      '''
      for elt in self.listeCODE:
          code=elt.keys()[0]
          dico=elt[code]
          self.dictMCVal={}
          self.dictMCVal[code]=dico
          if code in self.__class__.__dict__.keys():
             texteCode=apply(self.__class__.__dict__[code],(self,execution))
             self.texteExecution=self.texteExecution+texteCode

   def generPROC_ETAPE(self,obj):
      self.DictTemp={}
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      dico={}
      dico[obj.nom]=self.DictTemp
      self.listeCODE.append(dico)
      if hasattr(obj.definition,"mcOblig") :
         for clef in obj.definition.mcOblig.keys():
             setattr(self,clef,obj.definition.mcOblig[clef])
      return s


   def generMCSIMP(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      """
      s=PythonGenerator.generMCSIMP(self,obj)
      clef=""
      for i in obj.get_genealogie() :
           clef=clef+"_"+i
      self.DictTemp[clef]=obj.valeur
      if hasattr(obj.definition,'equiv') and obj.definition.equiv!= None:
         setattr(self,obj.definition.equiv,obj.valeur)
      else :
         setattr(self,obj.nom,obj.valeur)
      return s


   def  remplaceCONFIG(self,chaine,liste) :
       for mot in liste :
           rplact="%_"+mot+"%"
           result=chaine.replace(rplact,self.config.__dict__[mot])
           chaine=result
       return chaine


   def  remplaceDICO(self,chaine,dico) :
       for mot in dico.keys() :
           rplact="%"+mot+"%"
           result=chaine.replace(rplact,str(dico[mot]))
           chaine=result
       return chaine

