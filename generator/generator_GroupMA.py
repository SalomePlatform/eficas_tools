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
    Ce module contient le plugin generateur d une liste des GroupNo et GroupMA
"""
import traceback
import types,string,re

from generator_python import PythonGenerator
def entryPoint():
   """
       Retourne les informations nécessaires pour le chargeur de plugins

       Ces informations sont retournées dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'GroupMA',
        # La factory pour créer une instance du plugin
          'factory' : GroupMAGenerator,
          }


class GroupMAGenerator(PythonGenerator):
   """
       Ce generateur parcourt un objet de type JDC et produit
       un texte au format eficas et 
       un texte au format homard 

   """
   # Les extensions de fichier préconisées
   extensions=('.comm',)

   def __init__(self):
      PythonGenerator.__init__(self)
      self.listeMA=[]
      self.listeNO=[]

   def gener(self,obj,format='brut',configuration=None):
      self.liste=[]
      self.text=PythonGenerator.gener(self,obj,'brut',config=None)
      return self.listeMA,self.listeNO

   def generMCSIMP(self,obj) :
       if 'grma' in repr(obj.definition.type) :
          if not type(obj.valeur) in (list, tuple):
             aTraiter=(obj.valeur,)
          else :
	     aTraiter=obj.valeur
          for group in aTraiter :
             if group not in self.listeMA :
                self.listeMA.append(group)
       if 'grno' in repr(obj.definition.type) :
          if not type(obj.valeur) in (list, tuple):
             aTraiter=(obj.valeur,)
          else :
	     aTraiter=obj.valeur
          for group in aTraiter :
             if group not in self.listeNO :
                self.listeNO.append(group)
       s=PythonGenerator.generMCSIMP(self,obj)
       return s
