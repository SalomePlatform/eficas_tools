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
   openturns pour EFICAS.

"""
import traceback
import types,string,re

from generator_python import PythonGenerator
from OpenturnsBase import Generateur 
#from OpenturnsXML import XMLGenerateur 
#from OpenturnsSTD import STDGenerateur 

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'openturns_study',
        # La factory pour creer une instance du plugin
          'factory' : OpenturnsGenerator,
          }


class OpenturnsGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 
      un texte au format xml 

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

   def initDico(self):
      self.dictMCVal={}
      self.listeVariables=[]
      self.listeFichiers=[]
      self.dictMCLois={}
      self.dictTempo={}
      self.TraiteMCSIMP=1
      self.texteSTD="""#!/usr/bin/env python
      import sys
      print "Invalid file. Check build process."
      sys.exit(1)
      """

   def gener(self,obj,format='brut',config=None):
      print "IDM: gener dans generator_openturns_study.py"
      self.initDico()
      self.text=PythonGenerator.gener(self,obj,format)
      self.genereSTD()
      return self.text

   def generMCSIMP(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      Remplit le dictionnaire des MCSIMP si nous ne sommes ni dans une loi, ni dans une variable
      """
      s=PythonGenerator.generMCSIMP(self,obj)
      if self.TraiteMCSIMP == 1 : 
         self.dictMCVal[obj.nom]=obj.valeur
      else :
         self.dictTempo[obj.nom]=obj.valeur
      return s


   def generETAPE(self,obj):
      print "IDM: generETAPE dans generator_openturns_study.py"
      print "IDM: obj.nom=", obj.nom
      if obj.nom in ( "DISTRIBUTION", ) :
         self.TraiteMCSIMP=0
         self.dictTempo={}
      s=PythonGenerator.generETAPE(self,obj)
      if obj.nom in ( "DISTRIBUTION", ) :
         self.dictMCLois[obj.sd]=self.dictTempo
         self.dictTempo={}
      self.TraiteMCSIMP=1
      return s

   def generPROC_ETAPE(self,obj):
      print "IDM: generPROC_ETAPE dans generator_openturns_study.py"
      print "IDM: obj.nom=", obj.nom
      if obj.nom in ( "VARIABLE",  ) :
         self.TraiteMCSIMP=0
         self.dictTempo={}
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      if obj.nom in ( "VARIABLE", ) :
         self.listeVariables.append(self.dictTempo)
         self.dictTempo={}
      self.TraiteMCSIMP=1
      return s

   def genereSTD(self):
      print "IDM: genereSTD dans generator_openturns_study.py"
      print "IDM: self.listeVariables=", self.listeVariables
      MonGenerateur=self.getGenerateur()
      #try :
      if 1== 1 :
         self.texteSTD=MonGenerateur.CreeSTD()
      #except :
      else :
         self.texteSTD="Il y a un pb a la Creation du STD"

   def writeDefault(self, fn):
      fileSTD = fn[:fn.rfind(".")] + '.py'
      f = open( str(fileSTD), 'wb')
      f.write( self.texteSTD )
      f.close()

   def getGenerateur (self):
      print "IDM: getGenerateur dans generator_openturns_study.py"
      print "IDM: self.dictMCVal=", self.dictMCVal
      print "IDM: self.listeVariables=", self.listeVariables
      print "IDM: self.dictMCLois=", self.dictMCLois
      MonBaseGenerateur=Generateur(self.appli,self.dictMCVal, self.listeVariables, self.dictMCLois)
      MonGenerateur=MonBaseGenerateur.getSTDGenerateur()
      return MonGenerateur
