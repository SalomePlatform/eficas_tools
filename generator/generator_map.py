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
   CARMEL3D pour EFICAS.

"""
import traceback
import types,string,re,os
import Accas

from generator_python import PythonGenerator

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

   def gener(self,obj,format='brut',config=None):
      self.initDico()
      self.text=PythonGenerator.gener(self,obj,format)
      if obj.isvalid() :self.genereExeMap()
      return self.text


   def genereExeMap(self) :
      '''
      Prepare le contenu du fichier de parametres python
      peut ensuite etre obtenu au moyen de la fonction getTubePy().
      '''
      nomSpec="spec_"+self.schema
      self.texteEXE="from map.spec import %s;\n"%nomSpec
      self.texteEXE+="node=%s.new();\n"%nomSpec
      self.texteEXE+="node.getInputData();\n"
      self.texteEXE+="node.setInputData(%s);\n"%self.dictValeur
      self.texteEXE+="node.execute();\n"
      self.texteEXE+="res=node.getOutputData();\n"
      

   def initDico(self) :
      if not hasattr(self,'schema') : self.schema=""
      self.dictParam={}
      self.dictValeur={}
  
   def writeDefault(self, fn):
      fileEXE = fn[:fn.rfind(".")] + '.py'
      f = open( str(fileEXE), 'wb')
      f.write( self.texteEXE )
      f.close()

   def generMCSIMP(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      Remplit le dictionnaire des MCSIMP 
      """
      
      if obj.get_genealogie()[0][-6:-1]=="_PARA":
         self.dictParam[obj.nom]=obj.valeur
      else :
         self.dictValeur[obj.nom]=obj.valeur
      s=PythonGenerator.generMCSIMP(self,obj)
      return s
  
  
   def generRUN(self,obj,schema):
       if not(obj.isvalid()) :
          print "TODO TODO TODO"
       self.texteEXE=""
       self.schema=schema
       textComm=self.gener(obj)
       return self.texteEXE
