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
dictNatureMateriau={"MAT_REF_COND1":"CONDUCTOR"}

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'CARMEL3D',
        # La factory pour creer une instance du plugin
          'factory' : CARMEL3DGenerator,
          }


class CARMEL3DGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 
      un texte au format py 

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

   def gener(self,obj,format='brut',config=None):
      self.initDico()
      # Cette instruction génère le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)
      # Cette instruction génère le contenu du fichier de paramètres python
      self.genereCARMEL3D()
      print self.texteCarmel3D
      print self.dictName
      print self.dictMaterConductor
      
      return self.text


   def genereCARMEL3D(self) :
      '''
      Prépare le contenu du fichier de paramètres python. Le contenu
      peut ensuite être obtenu au moyen de la fonction getTubePy().
      '''
      self.texteCarmel3D+="[MATERIALS\n"
      self.texteCarmel3D+="     [CONDUCTOR\n"
      for key in self.dictMaterConductor:
          for ligne in self.dictName[key] :
              self.texteCarmel3D+=self.dictName[key]
              self.texteCarmel3D+=self.dictMaterConductor[key]
      self.texteCarmel3D+="     ]\n"
      self.texteCarmel3D+="]\n"


   def initDico(self) :
      self.texteCarmel3D=""
      self.dictName={}
      self.dictMaterConductor={}

  
   #def generMCSIMP(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      Remplit le dictionnaire des MCSIMP si nous ne sommes ni dans une loi, ni dans une variable
      """
      #clef=""
      #for i in obj.get_genealogie() :
      #   clef=clef+"__"+i
      #self.dictMCVal[obj.nom]=obj.valeur
      #self.dictMCVal[clef]=obj.valeur
      
      #print "MCSIMP", obj.nom, "  ", obj.valeur
      #s=PythonGenerator.generMCSIMP(self,obj)
      #return s
  
   #def generMCFACT(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      Remplit le dictionnaire des MCSIMP si nous ne sommes ni dans une loi, ni dans une variable
      """
      #print "MCFACT", obj.nom, "  ", obj.valeur
      #clef=""
      #for i in obj.get_genealogie() :
      #   clef=clef+"__"+i
      #self.dictMCVal[obj.nom]=obj.valeur
      #self.dictMCVal[clef]=obj.valeur
      #s=PythonGenerator.generMCFACT(self,obj)
      #return s
  
   def generPROC_ETAPE(self,obj):
      print "PROC_ETAPE", obj.nom, "  ", obj.valeur
      if obj.nom=="SOURCES" : self.generSOURCES(obj)
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      return s
  
   def generETAPE(self,obj):
      print "ETAPE", obj.nom, "  ", obj.valeur
      if obj.nom=="MESH_GROUPE" : self.generGROUPE(obj)
      if obj.nom=="MATERIALS" : self.generMATERIALS(obj)
      s=PythonGenerator.generETAPE(self,obj)
      return s

   def generSOURCES(self,obj):
      self.texteCarmel3D+="["+obj.nom+"\n"
      for keyN1 in obj.valeur :
          self.texteCarmel3D+="   ["+keyN1+"\n"
	  for keyN2 in obj.valeur[keyN1]:
	      self.texteCarmel3D+="      "+keyN2+" "+str(obj.valeur[keyN1][keyN2])+"\n"
	  self.texteCarmel3D+="   ]"+"\n"
      self.texteCarmel3D+="]"+"\n"

   def generGROUPE(self,obj):
       texteName="       NAME     "+obj.get_sdname()+"\n"
       self.dictName[obj.valeur['Material'].nom]=texteName

   def generMATERIALS(self,obj):
          texte=""
	  try :
              nature=dictNatureMateriau[obj.valeur['NATURE']]
	      if nature=="CONDUCTOR" : self.generMATERIALSCONDUCTOR(obj)
	  except:
	      pass


   def generMATERIALSCONDUCTOR(self,obj):
       texte=""
       print "___________________________"
       for keyN1 in obj.valeur :
	   if keyN1=='NATURE': continue
           print "keyN1=", keyN1
	   print obj.valeur[keyN1]['TYPE_LAW']
	   texte+="      ["+keyN1+"\n"
	   if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_REAL' or obj.valeur[keyN1]['TYPE_LAW']=='LINEAR' :
	      texte+="         LAW LINEAR\n"
	      texte+="         HOMOGENOUS TRUE\n"
	      texte+="         ISOTROPIC TRUE\n"
	      texte+="         VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_REAL"])+" 0\n"
	   if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_COMPLEX' :
	         texte+="         LAW LINEAR\n"
	         texte+="         HOMOGENOUS TRUE\n"
	         texte+="         ISOTROPIC TRUE\n"
	         texte+="         VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_COMPLEX"][1])+" "+str(obj.valeur[keyN1]["VALUE_COMPLEX"][2])+"\n"
	          
	   texte+="   ]"+"\n"
       if obj.get_sdname() in self.ditMaterConductor.keys() :
         self.dictMaterConductor[obj.get_sdname()].append(texte) 
       else :
         self.dictMaterConductor[obj.get_sdname()]=(texte,)
       print texte
