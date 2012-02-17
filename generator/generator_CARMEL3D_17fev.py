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

# dictionnaire contenant :
#           cle = nom du materiau de reference
#           valeur = nature du materiau de reference ; correspond a l entete du sous bloc dans le bloc MATERIALS du fichier de parametres Carmel3D
#
dictNatureMaterRef={"MAT_REF_COND1":"CONDUCTOR", 
                    "MAT_REF_DIEL1":"DIELECTRIC"}
print "generateur carmel "
print "generateur carmel "

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
      un texte au format attendu par le code Carmel3D 

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

   def gener(self,obj,format='brut',config=None):
       
      self.initDico()
      
      # Cette instruction génère le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)

      # Cette instruction génère le contenu du fichier de pametres pour le code Carmel3D
      self.genereCARMEL3D()
      
      print "texte carmel3d :\n",self.texteCarmel3D
      print "dictName : ",self.dictName
      print "dictMaterConductor : ",self.dictMaterConductor
      print "text = ", self.text
      
      return self.text


   def genereCARMEL3D(self) :
      '''
      Prépare le contenu du fichier de parmetres pour le code Carmel3D
      '''
      print "cle dico materconductor : " , self.dictMaterConductor.keys()
    
      self.texteCarmel3D+="[MATERIALS\n"
      self.texteCarmel3D+="     [CONDUCTOR\n"
    
      for cle in self.dictMaterConductor.keys():
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour materiau : ",cle
              print "fichier phys incomplet "
          else : 
              for chaine in self.dictMaterConductor[cle] :
                   self.texteCarmel3D+=str(self.dictName[cle])
                   self.texteCarmel3D+=chaine
     
     
      self.texteCarmel3D+="     ]\n"
      self.texteCarmel3D+="]\n"


   def initDico(self) :
      self.texteCarmel3D=""
      self.dictName={}
      self.dictMaterConductor={}

  
   def generPROC_ETAPE(self,obj):
      # analyse des PROC du catalogue
      # ( SOURCES et VERSION )   
      #   
      print "PROC_ETAPE", obj.nom, "  ", obj.valeur
      if obj.nom=="SOURCES" : self.generSOURCES(obj)
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      return s
  
   def generETAPE(self,obj):
      # analyse des OPER du catalogue

      print "ETAPE", obj.nom, "  ", obj.valeur
  #   print "DIR = ", dir(obj)

      if obj.nom=="MESH_GROUPE" : self.generMESHGROUPE(obj)
      if obj.nom=="MATERIALS" : self.generMATERIALS(obj)

      s=PythonGenerator.generETAPE(self,obj)
      return s

   def generSOURCES(self,obj):
      # preparation du bloc SOURCES 

      self.texteCarmel3D+="["+obj.nom+"\n"
      for keyN1 in obj.valeur :
          self.texteCarmel3D+="   ["+keyN1+"\n"
	  for keyN2 in obj.valeur[keyN1]:
	      self.texteCarmel3D+="      "+keyN2+" "+str(obj.valeur[keyN1][keyN2])+"\n"
	  self.texteCarmel3D+="   ]"+"\n"
      self.texteCarmel3D+="]"+"\n"

   def generMESHGROUPE(self,obj):
      # preparation de la ligne NAME referencant le groupe de mailles 
      # associe le groupe de mailles au materiau utilisateur
       texteName="       NAME     "+obj.get_sdname()+"\n"
       self.dictName[obj.valeur['MON_MATER'].nom]=texteName

   def generMATERIALS(self,obj):
      # preparation du bloc MATERIALS 
          texte=""
          print "gener materials obj valeur = ", obj.valeur
	  try :
              nature=dictNatureMaterRef[obj.valeur['MAT_REF']]
	      if nature=="CONDUCTOR" : self.generMATERIALSCONDUCTOR(obj)
#	      if nature=="DIELECTRIC" : self.generMATERIALSDIELECTRIC(obj)
	  except:
	      pass


   def generMATERIALSCONDUCTOR(self,obj):
      # preparation du sous bloc CONDUCTOR
       texte=""
       print "___________________________"
       for keyN1 in obj.valeur :
	   if keyN1=='MAT_REF': continue
           print "keyN1=", keyN1
	   print obj.valeur[keyN1]['TYPE_LAW']
	   texte+="         ["+keyN1+"\n"
	   if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_REAL' :
	      texte+="            LAW LINEAR\n"
	      texte+="            HOMOGENOUS TRUE\n"
	      texte+="            ISOTROPIC TRUE\n"
	      texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_REAL"])+" 0\n"
	   if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_COMPLEX' :
	         texte+="            LAW LINEAR\n"
	         texte+="            HOMOGENOUS TRUE\n"
	         texte+="            ISOTROPIC TRUE\n"
	         texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_COMPLEX"][1])+" "+str(obj.valeur[keyN1]["VALUE_COMPLEX"][2])+"\n"
	          
	   texte+="         ]"+"\n"

       print "obj get sdname= ", obj.get_sdname()
       if obj.get_sdname() in self.dictMaterConductor.keys() :
         self.dictMaterConductor[obj.get_sdname()].append(texte) 
       else :
         self.dictMaterConductor[obj.get_sdname()]=[texte,]
       print texte
   

