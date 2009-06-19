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

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'SEP',
        # La factory pour creer une instance du plugin
          'factory' : SEPGenerator,
          }


class SEPGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 
      un texte au format py 

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

   def gener(self,obj,format='brut'):
      self.initDico()
      self.text=PythonGenerator.gener(self,obj,format)
      self.genereSEP()
      return self.text

   def getTubePy(self) :
      return self.texteTubePy

   def genereSEP(self) :
      self.texteTubePy="# Parametres generes par Eficas \n"
      for MC in self.dictMCVal.keys():
	 ligne = MC +"="+ repr(self.dictMCVal[MC])+'\n'
         self.texteTubePy=self.texteTubePy+ligne
      print self.texteTubePy

      fichier=os.path.join(os.path.dirname(__file__),"tube.py")
      f=open(fichier,'r')
      for ligne in f.readlines():
         self.texteTubePy=self.texteTubePy+ligne
      f.close

   def initDico(self) :
      self.tube=0
      self.coude=0
      self.dictMCVal={}
      self.texteTubePy=""

   def generMCSIMP(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      Remplit le dictionnaire des MCSIMP si nous ne sommes ni dans une loi, ni dans une variable
      """
      s=PythonGenerator.generMCSIMP(self,obj)
      self.dictMCVal[obj.nom]=obj.valeur
      return s
  
   def generMACRO_ETAPE(self,obj):
      print obj.nom
      if obj.nom == "M_TUBE" :
	 self.tube=1
      if obj.nom == "M_COUDE" :
	 self.coude=1
      s=PythonGenerator.generMACRO_ETAPE(self,obj)
      return s

