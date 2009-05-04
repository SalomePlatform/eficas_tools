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
          'name' : 'openturns_wrapper',
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
       self.dictVariables={}
       self.listeFichiers=[]
       self.dictTempo={}
       self.traiteMCSIMP=1
       self.numOrdre=0
       self.texteSTD="""#!/usr/bin/env python
       import sys
       print "Invalid file. Check build process."
       sys.exit(1)
       """
       self.wrapperXML=None

   def gener(self,obj,format='brut'):
       #print "IDM: gener dans generator_openturns_wrapper.py"
       self.initDico()
       self.text=PythonGenerator.gener(self,obj,format)
       self.genereXML()
       #self.genereSTD()
       return self.text

   def generMCSIMP(self,obj) :
       """
       Convertit un objet MCSIMP en texte python
       Remplit le dictionnaire des MCSIMP si nous ne sommes ni dans une loi, ni dans une variable
       """
       s=PythonGenerator.generMCSIMP(self,obj)
       if self.traiteMCSIMP == 1 : 
          self.dictMCVal[obj.nom]=obj.val
       else :
          self.dictTempo[obj.nom]=obj.valeur
       return s

   def generETAPE(self,obj):
       #print "generETAPE" , obj.nom
       if obj.nom == "VARIABLE" :
          self.traiteMCSIMP=0
          self.dictTempo={}
       s=PythonGenerator.generETAPE(self,obj)
       if obj.nom == "VARIABLE" :
          self.dictTempo["numOrdre"]=self.numOrdre
          self.numOrdre = self.numOrdre +1
          if obj.sd == None :
             self.dictVariables["SansNom"]=self.dictTempo
          else :
             self.dictVariables[obj.sd.nom]=self.dictTempo
          self.dictTempo={}
       self.traiteMCSIMP=1
       return s

   def generMCFACT(self,obj):
       # Il n est pas possible d utiliser obj.valeur qui n est pas 
       # a jour pour les nouvelles variables ou les modifications 
       #print "generMCFACT" , obj.nom
       if obj.nom in ( "Files", ) :
          self.traiteMCSIMP=0
	  self.dictTempo={}
       s=PythonGenerator.generMCFACT(self,obj)
       self.listeFichiers.append(self.dictTempo)
       self.traiteMCSIMP=1
       return s

   def genereXML(self):
       #print "IDM: genereXML dans generator_openturns_wrapper.py"
       #print "appli.CONFIGURATION=",self.appli.CONFIGURATION.__dict__
       if self.listeFichiers != [] :
          self.dictMCVal["Files"]=self.listeFichiers
       print "dictMCVal", self.dictMCVal, "dictVariables", self.dictVariables
       MonBaseGenerateur=Generateur(self.appli,self.dictMCVal, [], {} ,self.dictVariables)
       MonGenerateur=MonBaseGenerateur.getXMLGenerateur()
       #try :
       if 1== 1 :
          self.wrapperXML=MonGenerateur.CreeXML()
       #except :
       else :
	  self.wrapperXML=None

   def writeOpenturnsXML(self, filename):
      self.wrapperXML.writeFile( str(filename) )

