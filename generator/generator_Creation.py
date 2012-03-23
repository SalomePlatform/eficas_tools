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

from generator_python import PythonGenerator
debut="""
lqdkqmldk
"""


def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'Creation',
        # La factory pour creer une instance du plugin
          'factory' : CreationGenerator,
          }


class CreationGenerator(PythonGenerator):
   """

   """
   # Les extensions de fichier permis?

   def gener(self,obj,format='brut',config=None):
       
      self.initDico(obj)
      # Cette instruction génère le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)
      if obj.isvalid() : self.genereDescription()
      return self.text


   def genereParam(self):
      listeParam=[]
      for monParam in self.dictParam.keys():
          if self.dico.has_key(monParam) : continue
          listeParam.append(self.dictParam[monParam])

      if len(listeParam)== 0 : return
      try:
         jdcDict=self.jdc.jdcDict
      except:
         raise valueError, "toutes les donnees ne sont pas connues"
      for param in listeParam:
          obj=None
          for etape in self.jdc.jdcDict.etapes:
              if str(etape.sdnom) != str(param) : 
                  continue
              obj=etape
              break
              
      if obj==None:
         raise valueError, "toutes les donnees ne sont pas connues"
         return

      texteEtape=self.generETAPE(obj)

   def genereDescription(self) :
      '''
      '''
      self.texte=debut 
      self.genereParam()

   def initDico(self,obj) :
      self.dicoCourant={}
      self.dico={}
      self.dictParam={}
      self.listeParam=[]
      self.jdc=obj.get_jdc_root()
      try :
        self.texte_jdc_aux=self.jdc.recorded_units[999]
      except :
        self.texte_jdc_aux=""


   def generMCSIMP(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      Remplit le dictionnaire des MCSIMP si nous ne sommes ni dans une loi, ni dans une variable
      """
      
      #print "MCSIMP", obj.nom, "  ", obj.valeur
      from cree_map_cata import param_map
      if isinstance(obj.valeur,param_map):
        self.dicoCourant[obj.nom]=obj.valeur.nom
        self.dictParam[obj.valeur.nom]=obj.valeur
      else :
        self.dicoCourant[obj.nom]=obj.valeur
      s=PythonGenerator.generMCSIMP(self,obj)
      return s
  
   def generPROC_ETAPE(self,obj):
      self.dicoCourant={}
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      self.dico[obj.nom]=self.dicoCourant
      return s
  
   def generETAPE(self,obj):
      #print "ETAPE", obj.nom, " ",obj.sdnom
      self.dicoCourant={}
      s=PythonGenerator.generETAPE(self,obj)
      self.dico[obj.sdnom]=self.dicoCourant
      return s

