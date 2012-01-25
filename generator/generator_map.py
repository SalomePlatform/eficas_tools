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
import time
from datetime import date

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

   def writeDefault(self, fn):
      print "data saved in file ", fn

   def initialise(self,config):
      self.config=config
#      self.nom_racine=self.config.PATH_STUDY+"/"+self.config.NAME_SCHEME+"/"
#      print "*"*50+"\n"+self.nom_racine
      self.nom_racine = "/tmp"
      if not( os.path.exists(self.nom_racine)):
         os.makedirs(self.nom_racine)
      self.listeCODE=[]
      self.text=""

      self.ssCode=self.config.appli.ssCode
      self.INSTALLDIR=self.config.appli.INSTALLDIR
      self.ssCodeDir=os.path.join(self.INSTALLDIR,'MAP/Templates',self.ssCode)
      self.fichierYacs=self.ssCode+"_YACS_nodes"
#      self.texteExecution="import os,sys\n"
#      self.texteExecution+="sys.path.append('"+self.ssCodeDir+"')\n"
#      self.texteExecution+="from " + self.fichierYacs +" import *\n"

   def gener(self,obj,format='brut',config=None):
      self.initialise(config)
      text=PythonGenerator.gener(self,obj,format)
      return text

   def generRUN(self,obj,format='brut',config=None,):
      self.initialise(config)
      text=PythonGenerator.gener(self,obj,format)
      string = ""
      for elt in self.listeCODE:
          code=elt.keys()[0]
          string = "[" + code + "]\n"
          self.dico=elt[code]
          for key in self.dico.keys():
             string += key + "=" + str(self.dico[key]) + "\n"
          if code in self.__class__.__dict__.keys():
             texteCode=apply(self.__class__.__dict__[code],(self,))
             self.texteExecution += texteCode
      self.temp_parameter_file = os.tempnam(None, "map_" + code + "_")
      self.texteExecution = os.path.join(os.getenv("MAP_DIRECTORY"), "runMAP")
      self.texteExecution += " " + self.temp_parameter_file + " -v"
      f_id = open(self.temp_parameter_file, "w")
      f_id.write(string)
      f_id.close()
      print "parameter file name :", self.temp_parameter_file
      print string
      print "command :", self.texteExecution
      return self.texteExecution


   def generRUNYACS(self,obj,format='brut',config=None,nomFichier=None):
      self.initialise(config)
      text=PythonGenerator.gener(self,obj,format)
      #self.generePythonMap("non")

      import sys
      sys.path.append(os.path.join(os.getenv("YACS_ROOT_DIR"),"lib/python2.4/site-packages/salome/"))
      import monCreateYacs
      self.monSchema=monCreateYacs.getSchema(config)
      self.proc=self.monSchema.createProc(self)
      for elt in self.listeCODE:
          code=elt.keys()[0]
          dico=elt[code]
          if code in self.__class__.__dict__.keys():
             codeYACS=str(code)+"YACS"
             if hasattr(self.monSchema, codeYACS): 
                fct=getattr(self.monSchema, codeYACS)
                fct(self.proc,dico)
                
      print str(nomFichier)
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
      #clef=""
      #for i in obj.get_genealogie() :
      #     clef=clef+"_"+i
      self.DictTemp[obj.nom]=obj.valeur
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

