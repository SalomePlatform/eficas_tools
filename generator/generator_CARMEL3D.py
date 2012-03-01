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
#           valeur = nature du materiau de reference ; correspond a un sous bloc du bloc MATERIALS du fichier de parametres Carmel3D
#
dictNatureMaterRef={"MAT_REF_COND1":"CONDUCTOR", 
                    "MAT_REF_DIEL1":"DIELECTRIC",
                    "MAT_REF_ZSURF1":"ZSURFACIC",
                    "MAT_REF_EM_ISOTROPIC1":"EMISO",
                    "MAT_REF_EM_ANISOTROPIC1":"EMANISO",
                    "MAT_REF_NILMAT":"NILMAT"
                    }
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
      
      # Cette instruction genere le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)

      # Cette instruction genere le contenu du fichier de parametres pour le code Carmel3D
      # si le jdc est valide (sinon cela n a pas de sens)
      if obj.isvalid() : 
           self.genereCARMEL3D()
           self.writePHYS()

      print "texte carmel3d :\n",self.texteCarmel3D
      print "dictName : ",self.dictName
      print "dictMaterConductor : ",self.dictMaterConductor
      print "dictMaterDielectric : ",self.dictMaterDielectric
      #print "text = ", self.text
      
      return self.text


   def initDico(self) :
   # initialisations
  
      self.texteCarmel3D=""
      self.dicoEtapeCourant=None
      self.dicoMCFACTCourant=None
      self.dicoCourant=None
      self.dictName={"grm_def":"        NAME      gr_maille_a_saisir\n"}
      self.dictMaterConductor={}
      self.dictMaterDielectric={}
      self.dictMaterZsurfacic={}
      self.dictMaterEmIso={}
      self.dictMaterEmAnIso={}
      self.dictMaterNilmat={}


   def genereCARMEL3D(self) :
      '''
      Prepare une partie du contenu du fichier de parametres (PHYS) pour le code Carmel3D
      (bloc MATERIALS)
      ce bloc existe toujours ! 
      '''
      #print "cle dico materconductor : " , self.dictMaterConductor.keys()
      #print "cle dico materdielectric : " , self.dictMaterDielectric.keys()
    
      # constitution du bloc MATERIALS du fichier PHYS
      self.texteCarmel3D+="[MATERIALS\n"

      # constitution du bloc CONDUCTOR du fichier PHYS si existe
      if self.dictMaterConductor != {} : self.creaBLOC_CONDUCTOR()
     
      # constitution du bloc DIELECTRIC du fichier PHYS si exixte
      if self.dictMaterDielectric != {} : self.creaBLOC_DIELECTRIC()
     
      # constitution du bloc ZSURFACIC du fichier PHYS si exixte
      if self.dictMaterZsurfacic != {} : self.creaBLOC_ZSURFACIC()
     
      # constitution du bloc EM_ISOTROPIC_FILES du fichier PHYS si exixte
      if self.dictMaterEmIso != {} : self.creaBLOC_EMISO()
     
      # constitution du bloc EM_ANISOTROPIC_FILES du fichier PHYS si exixte
      if self.dictMaterEmAnIso != {} : self.creaBLOC_EMANISO()
     
      # constitution du bloc NILMAT du fichier PHYS si exixte
      if self.dictMaterNilmat != {} : self.creaBLOC_NILMAT()
     
      # fin du bloc MATERIALS du fichier PHYS
      self.texteCarmel3D+="]\n"


   def writePHYS(self) :
      '''
      Ecrit le fichier de parametres (PHYS) pour le code Carmel3D
      '''
      print "ecriture fichier "
      f=open('monficPHYS','w')
      f.write(self.texteCarmel3D)
      f.close()

    
   def creaBLOC_CONDUCTOR(self) :
      # constitution du bloc CONDUCTOR du fichier PHYS
      self.texteCarmel3D+="     [CONDUCTOR\n"
    
      for cle in self.dictMaterConductor.keys():
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour materiau : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          for chaine in self.dictMaterConductor[cle] :
              self.texteCarmel3D+=chaine
     
      self.texteCarmel3D+="     ]\n"


   def creaBLOC_DIELECTRIC(self) :
      # constitution du bloc DIELECTRIC du fichier PHYS
      self.texteCarmel3D+="     [DIELECTRIC\n"
    
      for cle in self.dictMaterDielectric.keys():
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour materiau : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          for chaine in self.dictMaterDielectric[cle] :
              self.texteCarmel3D+=chaine
      self.texteCarmel3D+="     ]\n"


   def creaBLOC_ZSURFACIC(self) :
      # constitution du bloc ZSURFACIC du fichier PHYS
      self.texteCarmel3D+="     [ZSURFACIC\n"
    
      for cle in self.dictMaterZsurfacic.keys():
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour materiau : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          for chaine in self.dictMaterZsurfacic[cle] :
              self.texteCarmel3D+=chaine
      self.texteCarmel3D+="     ]\n"

   def creaBLOC_EMISO(self) :
      # constitution du bloc EMISO du fichier PHYS
      self.texteCarmel3D+="     [EM_ISOTROPIC_FILES\n"
    
      for cle in self.dictMaterEmIso.keys():
          for chaine in self.dictMaterEmIso[cle] :
              self.texteCarmel3D+=chaine
      self.texteCarmel3D+="     ]\n"

   def creaBLOC_EMANISO(self) :
      # constitution du bloc EMANISO du fichier PHYS
      self.texteCarmel3D+="     [EM_ANISOTROPIC_FILES\n"
    
      for cle in self.dictMaterEmAnIso.keys():
          for chaine in self.dictMaterEmAnIso[cle] :
              self.texteCarmel3D+=chaine
      self.texteCarmel3D+="     ]\n"

   def creaBLOC_NILMAT(self) :
      # constitution du bloc NILMAT du fichier PHYS
      self.texteCarmel3D+="     [NILMAT\n"
    
      for cle in self.dictMaterNilmat.keys():
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour materiau : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
      self.texteCarmel3D+="     ]\n"

   def generMCSIMP(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      """
      
   #   print "MCSIMP", obj.nom, "  ", obj.valeur
      self.dicoCourant[obj.nom]=obj.valeur
      s=PythonGenerator.generMCSIMP(self,obj)
      return s

  
   def generMCFACT(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      """
      dico={}
      self.dicoMCFACTCourant=dico
      self.dicoCourant=self.dicoMCFACTCourant
      s=PythonGenerator.generMCFACT(self,obj)
      self.dicoEtapeCourant[obj.nom]=self.dicoMCFACTCourant
   #   print "MCFACT", obj.nom, "  ", obj.valeur
      self.dicoMCFACTCourant=None
      self.dicoCourant=self.dicoEtapeCourant
      return s

  
   def generPROC_ETAPE(self,obj):
      # analyse des PROC du catalogue  ( SOURCES et VERSION )   
         
      dico={}
      self.dicoEtapeCourant=dico
      self.dicoCourant=self.dicoEtapeCourant
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      obj.valeur=self.dicoEtapeCourant
      
      print "PROC_ETAPE", obj.nom, "  ", obj.valeur
      
      if obj.nom=="SOURCES" : self.generSOURCES(obj)
     
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      return s

  
   def generETAPE(self,obj):
      # analyse des OPER du catalogue
      dico={}
      self.dicoEtapeCourant=dico
      self.dicoCourant=self.dicoEtapeCourant
      s=PythonGenerator.generETAPE(self,obj)
      obj.valeur=self.dicoEtapeCourant

      print "ETAPE", obj.nom, "  ", obj.valeur

      if obj.nom=="MESH_GROUPE" : self.generMESHGROUPE(obj)
      if obj.nom=="MATERIALS" : self.generMATERIALS(obj)

      s=PythonGenerator.generETAPE(self,obj)
      return s

   def generSOURCES(self,obj):
      # preparation du bloc SOURCES du fichier PHYS

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
      # preparation du bloc MATERIALS du fichier PHYS 
          texte=""
    #      print "gener materials obj valeur = ", obj.valeur
	  try :
              nature=dictNatureMaterRef[obj.valeur['MAT_REF']]
	      if nature=="CONDUCTOR" : self.generMATERIALSCONDUCTOR(obj)
	      if nature=="DIELECTRIC" : self.generMATERIALSDIELECTRIC(obj)
	      if nature=="ZSURFACIC" : self.generMATERIALSZSURFACIC(obj)
	      if nature=="EMISO" : self.generMATERIALSEMISO(obj)
	      if nature=="EMANISO" : self.generMATERIALSEMANISO(obj)
	      if nature=="NILMAT" : self.generMATERIALSNILMAT(obj)
	  except:
	      pass


   def generMATERIALSCONDUCTOR(self,obj):
      # preparation du sous bloc CONDUCTOR
       texte=""
       print "__________cond_________________"
      # parcours des proprietes du sous bloc CONDUCTOR
       for keyN1 in obj.valeur :
	   if keyN1=='MAT_REF': continue
      #     print "keyN1=", keyN1
#	   print obj.valeur[keyN1]['TYPE_LAW']
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
    #   if obj.get_sdname() in self.dictMaterConductor.keys() :
     #    self.dictMaterConductor[obj.get_sdname()].append(texte) 
      # else :
       self.dictMaterConductor[obj.get_sdname()]=[texte,]
 #      print texte
   

   def generMATERIALSDIELECTRIC(self,obj):
      # preparation du sous bloc DIELECTRIC
       texte=""
       print "______________diel_____________"
      # parcours des proprietes du sous bloc DIELECTRIC
       for keyN1 in obj.valeur :
	   if keyN1=='MAT_REF': continue
  #         print "keyN1=", keyN1
#	   print obj.valeur[keyN1]['TYPE_LAW']
      # debut du sous bloc de propriete du DIELECTRIC
	   texte+="         ["+keyN1+"\n"
      # loi lineaire reelle
	   if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_REAL' :
	      texte+="            LAW LINEAR\n"
	      texte+="            HOMOGENOUS TRUE\n"
	      texte+="            ISOTROPIC TRUE\n"
	      texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_REAL"])+" 0\n"
      # loi lineaire complexe
	   if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_COMPLEX' :
	         texte+="            LAW LINEAR\n"
	         texte+="            HOMOGENOUS TRUE\n"
	         texte+="            ISOTROPIC TRUE\n"
	         texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_COMPLEX"][1])+" "+str(obj.valeur[keyN1]["VALUE_COMPLEX"][2])+"\n"
	          
      # loi non lineaire de type spline, Marrocco ou Marrocco et Saturation
           for loiNL in [ 'SPLINE', 'MARROCCO', 'MARROCCO+SATURATION'] :
	        if loiNL == obj.valeur[keyN1]['TYPE_LAW']:
			 texte+="            LAW NONLINEAR\n"
			 texte+="            HOMOGENOUS TRUE\n"
			 texte+="            ISOTROPIC TRUE\n"
		         texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_COMPLEX"][1])+" "+str(obj.valeur[keyN1]["VALUE_COMPLEX"][2])+"\n"
			 texte+="            [NONLINEAR \n"
			 texte+="                ISOTROPY TRUE\n"
			 texte+="                NATURE "+str(obj.valeur[keyN1]['TYPE_LAW'])+"\n"
			 for keyN2 in obj.valeur[keyN1] :
			     if keyN2 != 'LAW' and keyN2 != 'TYPE_LAW' and keyN2 != 'VALUE_COMPLEX' :
				  texte+="                "+keyN2+" "+str(obj.valeur[keyN1][keyN2])+"\n"
			 texte+="            ]"+"\n"

      # fin du sous bloc de propriete
	   texte+="         ]"+"\n"

       print "obj get sdname= ", obj.get_sdname()
       #if obj.get_sdname() in self.dictMaterDielectric.keys() :
       #  self.dictMaterDielectric[obj.get_sdname()].append(texte) 
       #else :
       self.dictMaterDielectric[obj.get_sdname()]=[texte,]
 #      print texte
  
 
   def generMATERIALSZSURFACIC(self,obj):
      # preparation du sous bloc ZSURFACIC
       texte=""
       print "______________zsurf_____________"
       for keyN1 in obj.valeur :
	   if keyN1=='MAT_REF': continue
  #         print "keyN1=", keyN1
#	   print obj.valeur[keyN1]['TYPE_LAW']
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
      # if obj.get_sdname() in self.dictMaterZsurfacic.keys() :
       #  self.dictMaterZsurfacic[obj.get_sdname()].append(texte) 
       #else :
       self.dictMaterZsurfacic[obj.get_sdname()]=[texte,]
 #      print texte
   
 
   def generMATERIALSEMISO(self,obj):
      # preparation du sous bloc EMISO
       texte=""
       print "______________emiso________"
       texte+="        CONDUCTIVITY MED "+str(obj.valeur["CONDUCTIVITY_File"])+"\n"
       texte+="        PERMEABILITY MED "+str(obj.valeur["PERMEABILITY_File"])+"\n"

       print "obj get sdname= ", obj.get_sdname()
    #   if obj.get_sdname() in self.dictMaterEmIso.keys() :
     #    self.dictMaterEmIso[obj.get_sdname()].append(texte) 
      # else :
       self.dictMaterEmIso[obj.get_sdname()]=[texte,]
  #     print texte
  
 
   def generMATERIALSEMANISO(self,obj):
      # preparation du sous bloc EMANISO
       texte=""
       print "______________emaniso________"
       texte+="        CONDUCTIVITY  "+str(obj.valeur["CONDUCTIVITY_File"])+"\n"
       texte+="        PERMEABILITY  "+str(obj.valeur["PERMEABILITY_File"])+"\n"

       print "obj get sdname= ", obj.get_sdname()
     #  if obj.get_sdname() in self.dictMaterEmAnIso.keys() :
     #    self.dictMaterEmAnIso[obj.get_sdname()].append(texte) 
     #  else :
       self.dictMaterEmAnIso[obj.get_sdname()]=[texte,]
   #    print texte
   
   def generMATERIALSNILMAT(self,obj):
      # preparation du sous bloc NILMAT
       texte=""
       print "____________nil_____________"

       print "obj get sdname= ", obj.get_sdname()
       self.dictMaterNilmat[obj.get_sdname()]=[texte,]
   
