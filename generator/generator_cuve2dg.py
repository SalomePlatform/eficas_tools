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
    homard pour EFICAS.

"""
import traceback
import types,string,re

from Noyau import N_CR
from Noyau.N_utils import repr_float
from Accas import ETAPE,PROC_ETAPE,MACRO_ETAPE,ETAPE_NIVEAU,JDC,FORM_ETAPE
from Accas import MCSIMP,MCFACT,MCBLOC,MCList,EVAL
from Accas import GEOM,ASSD,MCNUPLET
from Accas import COMMENTAIRE,PARAMETRE, PARAMETRE_EVAL,COMMANDE_COMM
from Formatage import Formatage
from generator_python import PythonGenerator

def entryPoint():
   """
       Retourne les informations nécessaires pour le chargeur de plugins

       Ces informations sont retournées dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'cuve2dg',
        # La factory pour créer une instance du plugin
          'factory' : Cuve2dgGenerator,
          }


class Cuve2dgGenerator(PythonGenerator):
   """
       Ce generateur parcourt un objet de type JDC et produit
       un texte au format eficas et 
       un texte au format homard 

   """
   # Les extensions de fichier préconisées
   extensions=('.comm',)

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR generateur format homard pour homard',
                         fin='fin CR format homard pour homard')
      # Le texte au format homard est stocké dans l'attribut text
      self.text=''
      self.textCuve=''

   def gener(self,obj,format='brut'):
      self.text=''
      self.textCuve=''
      self.dico_mot={}
      self.dico_genea={}
      self.text=PythonGenerator.gener(self,obj,format)
      return self.text

   def generMCSIMP(self,obj) :
       self.dico_mot[obj.nom]=obj.valeur
       clef=""
       for i in obj.get_genealogie() :
           clef=clef+"_"+i
       self.dico_genea[clef]=obj.valeur
       s=PythonGenerator.generMCSIMP(self,obj)
       return s

   def writeCuve2DG(self):
      print "je passe dans writeCuve2DG"
      self.genereTexteCuve()
      f = open( "/tmp/data_template", 'wb')
      print self.texteCuve
      f.write( self.texteCuve )
      f.close()

   def genereTexteCuve(self):
      self.texteCuve=""
      self.texteCuve+="############################################################################################"+"\n"
      self.texteCuve+="# OPTIONS : Fichier Option.don"+"\n"
      self.texteCuve+="############################################################################################"+"\n"
      if self.dico_mot.has_key('IncrementTemporel'):
         self.texteCuve+="INCRTPS = "+ str(self.dico_mot["IncrementTemporel"])+"\n"
      if self.dico_mot.has_key('ProfilTemporel_Pression'):
         self.imprime(2,(self.dico_mot["ProfilTemporel_Pression"]))
      

   def imprime(self,nbdeColonnes,valeur):
      self.liste=[]
      self.transforme(valeur)
      i=0
      while i < len(self.liste):
          for k in range(nbdeColonnes) :
              self.texteCuve+=str(self.liste[i+k]) +"  "
          self.texteCuve+="\n"
          i=i+k+1
               

   def transforme(self,valeur):
      for i in valeur :
          if type(i) == tuple :
             self.transforme(i)
          else :
             self.liste.append(i)
          



