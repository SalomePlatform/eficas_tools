# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
"""
   Ce module contient le plugin generateur de fichier au format 
   CARMEL3D pour EFICAS.

"""
import traceback
import types,string,re,os

from generator_python import PythonGenerator

# dictionnaire contenant la liste des materiaux :
#     cle = nom du materiau 
#     valeur = nature du materiau ; correspond a un sous bloc du bloc MATERIALS du fichier de parametres Carmel3D
#
# les materiaux sont : 
#  - des materiaux de reference connus fournis par THEMIS,
#  - ou des materiaux generiques theoriques 
#
#
dictNatureMaterRef={"ACIER_CIMBLOT":"CONDUCTOR", 
                    "ACIER_Noir":"CONDUCTOR", 
                    "ACIER_PE":"CONDUCTOR", 
                    "ALU":"CONDUCTOR", 
                    "BRONZE":"CONDUCTOR", 
                    "CUIVRE":"CONDUCTOR", 
                    "FERRITE_Mn_Zn":"CONDUCTOR", 
                    "FERRITE_Ni_Zn":"CONDUCTOR", 
                    "INCONEL600":"CONDUCTOR", 
                    "POTASSE":"CONDUCTOR",
                    "COND_LINEAR":"CONDUCTOR",
                    "M6X2ISO1":"CONDUCTOR", 
                    "AIR":"NOCOND", 
                    "FERRITEB30":"NOCOND", 
                    "E24":"NOCOND",
                    "FEV470":"NOCOND",
                    "FEV600":"NOCOND",
                    "FEV800":"NOCOND",
                    "FEV1000":"NOCOND",
                    "HA600":"NOCOND",
                    "M600_65":"NOCOND",
                    "NOCOND_LINEAR":"NOCOND",
                    "NOCOND_NL_MAR":"NOCOND",
                    "NOCOND_NL_MARSAT":"NOCOND",
                    "M6X":"EMANISO",
                    "M6X_lineaire":"EMANISO",
                    "M6X_homog":"EMANISO",
                    "EM_ISOTROPIC":"EMISO",
                    "EM_ANISOTROPIC":"EMANISO",
                    "ZSURFACIC":"ZSURFACIC",
                    "ZINSULATOR":"ZINSULATOR",
                    "NILMAT":"NILMAT"
                    }

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
      un texte au format attendu par le code Carmel3D (fichier '.PHYS') 

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

#----------------------------------------------------------------------------------------
   def gener(self,obj,format='brut',config=None):
       
      self.initDico()
      
      # Cette instruction genere le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)

      # Cette instruction genere le contenu du fichier de parametres pour le code Carmel3D
      # si le jdc est valide (sinon cela n a pas de sens)
      if obj.isvalid() : 
           # constitution du bloc VERSION du fichier PHYS
           self.generBLOC_VERSION(obj)

           # constitution du bloc MATERIALS du fichier PHYS
           self.generBLOC_MATERIALS()

           # constitution du bloc SOURCES du fichier PHYS
           self.generBLOC_SOURCES()

#      print "texte carmel3d :\n",self.texteCarmel3D
#      print "dictName : ",self.dictName
#      print "dictMaterConductor : ",self.dictMaterConductor
#      print "dictMaterNocond : ",self.dictMaterNocond
      
      return self.text


#----------------------------------------------------------------------------------------
# initialisations
#----------------------------------------------------------------------------------------
   
   def initDico(self) :
 
      self.texteCarmel3D=""
      self.dicoEtapeCourant=None
      self.dicoMCFACTCourant=None
      self.dicoCourant=None
      self.dictName={"grm_def":"        NAME      gr_maille_a_saisir\n"}
      self.dictMaterConductor={}
      self.dictMaterNocond={}
      self.dictMaterZsurfacic={}
      self.dictMaterEmIso={}
      self.dictMaterEmAnIso={}
      self.dictMaterNilmat={}
      self.dictMaterZinsulator={}
      self.dictSourceStInd={}
      self.dictSourceEport={}
      self.dictSourceHport={}


#----------------------------------------------------------------------------------------
# ecriture
#----------------------------------------------------------------------------------------

   def writeDefault(self,fn) :
      '''
      Ecrit le fichier de parametres (PHYS) pour le code Carmel3D
      '''
      #print "ecriture fic phys"
      filePHYS = fn[:fn.rfind(".")] + '.phys'
      f = open( str(filePHYS), 'wb')
      f.write( self.texteCarmel3D)
      f.close()

#----------------------------------------------------------------------------------------
#  analyse de chaque noeud de l'arbre 
#----------------------------------------------------------------------------------------

   def generMCSIMP(self,obj) :
      """
      recuperation de l objet MCSIMP
      """
      
   #   print "MCSIMP", obj.nom, "  ", obj.valeur
      
      s=PythonGenerator.generMCSIMP(self,obj)
      self.dicoCourant[obj.nom]=obj.valeurFormatee
      return s

  
#----------------------------------------------------------------------------------------
   def generMCFACT(self,obj) :
      """
      recuperation de l objet MCFACT
      """
      dico={}
      self.dicoMCFACTCourant=dico
      self.dicoCourant=self.dicoMCFACTCourant
      s=PythonGenerator.generMCFACT(self,obj)
      self.dicoEtapeCourant[obj.nom]=self.dicoMCFACTCourant
      self.dicoMCFACTCourant=None
      self.dicoCourant=self.dicoEtapeCourant
      return s

  
#----------------------------------------------------------------------------------------
   def generPROC_ETAPE(self,obj):
      # analyse des PROC du catalogue  ( VERSION )   
         
      dico={}
      self.dicoEtapeCourant=dico
      self.dicoCourant=self.dicoEtapeCourant
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      obj.valeur=self.dicoEtapeCourant
      
 #     print "PROC_ETAPE", obj.nom, "  ", obj.valeur
     
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      return s

  
#----------------------------------------------------------------------------------------
   def generETAPE(self,obj):
      # analyse des OPER du catalogue
      dico={}
      self.dicoEtapeCourant=dico
      self.dicoCourant=self.dicoEtapeCourant
      s=PythonGenerator.generETAPE(self,obj)
      obj.valeur=self.dicoEtapeCourant

  #    print "ETAPE", obj.nom, "  ", obj.valeur

      if obj.nom=="MESH_GROUPE" : self.generMESHGROUPE(obj)
      if obj.nom=="MATERIALS" : self.generMATERIALS(obj)
      if obj.nom=="SOURCES" : self.generSOURCES(obj)

      s=PythonGenerator.generETAPE(self,obj)
      return s

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
   def generMESHGROUPE(self,obj):
      # preparation de la ligne NAME referencant le groupe de mailles 
      # associe le groupe de mailles au materiau ou a la source utilisateur
       try :
           texteName="        NAME     "+obj.get_sdname()+"\n"
           for cle in obj.valeur :
   #            print "cle : ", cle
               self.dictName[obj.valeur[cle].nom]=texteName
    #           print "dans gener_mesh dictName : ",self.dictName
       except:
           pass


   def generMATERIALS(self,obj):
      # preparation du bloc MATERIALS du fichier PHYS 
          texte=""
         # print "gener materials obj valeur = ", obj.valeur
	  try :
              nature=dictNatureMaterRef[obj.valeur['MAT_REF']]
              if nature=="CONDUCTOR" : self.generMATERIALSCONDUCTOR(obj)
	      if nature=="NOCOND" : self.generMATERIALSNOCOND(obj)
	      if nature=="ZSURFACIC" : self.generMATERIALSZSURFACIC(obj)
	      if nature=="EMISO" : self.generMATERIALSEMISO(obj)
	      if nature=="EMANISO" : self.generMATERIALSEMANISO(obj)
	      if nature=="NILMAT" : self.generMATERIALSNILMAT(obj)
	      if nature=="ZINSULATOR" : self.generMATERIALSZINSULATOR(obj)
	  except:
	      pass

   def generMATERIALSCONDUCTOR(self,obj):
      # preparation du sous bloc CONDUCTOR
       texte=""
      # print "__________cond_________________"
      # parcours des proprietes du sous bloc CONDUCTOR
       for keyN1 in obj.valeur :
	   if keyN1=='MAT_REF': continue
      #     print "keyN1=", keyN1
#	   print obj.valeur[keyN1]['TYPE_LAW']
	   texte+="         ["+keyN1+"\n"
      # loi lineaire reelle
	   if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_REAL' :
	      texte+="            LAW LINEAR\n"
	      texte+="            HOMOGENOUS TRUE\n"
	      texte+="            ISOTROPIC TRUE\n"
	      texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_REAL"])+" 0\n"
      # loi lineaire complexe
	   if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_COMPLEX' :
#	         print "si avec linear complex"
                 texte+="            LAW LINEAR\n"
	         texte+="            HOMOGENOUS TRUE\n"
	         texte+="            ISOTROPIC TRUE\n"
	         texte+="            VALUE "
  #               print "nbre a formater : ",obj.valeur[keyN1]["VALUE_COMPLEX"]
                 chC= self.formateCOMPLEX(obj.valeur[keyN1]["VALUE_COMPLEX"])
	         texte+= chC+"\n"
      # loi non lineaire de nature spline, Marrocco ou Marrocco et Saturation
      #  seuls les reels sont pris en compte
	   if obj.valeur[keyN1]['TYPE_LAW']=='NONLINEAR' :
	              texte+="            LAW NONLINEAR\n"
		      texte+="            HOMOGENOUS TRUE\n"
		      texte+="            ISOTROPIC TRUE\n"
	              texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE"])+" 0\n"
		      texte+="            [NONLINEAR \n"
		      texte+="                ISOTROPY TRUE\n"
		      texte+="                NATURE "+str(obj.valeur[keyN1]['NATURE'])+"\n"
		      for keyN2 in obj.valeur[keyN1] :
		          if keyN2 != 'TYPE_LAW' and keyN2 != 'VALUE' and keyN2 != 'NATURE' :
		               texte+="                "+keyN2+" "+str(obj.valeur[keyN1][keyN2])+"\n"
	              texte+="            ]"+"\n"

	   texte+="         ]"+"\n"

       self.dictMaterConductor[obj.get_sdname()]=[texte,]
#       print texte
   

   def generMATERIALSNOCOND(self,obj):
      # preparation du sous bloc NOCOND
       texte=""
      # print "______________nocond_____________"
      # parcours des proprietes du sous bloc NOCOND
       for keyN1 in obj.valeur :
	   if keyN1=='MAT_REF': continue
          # print "type loi = ", obj.valeur[keyN1]['TYPE_LAW']
      # debut du sous bloc de propriete du NOCOND
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
	         texte+="            VALUE "
                 chC= self.formateCOMPLEX(obj.valeur[keyN1]["VALUE_COMPLEX"])
	         texte+= chC+"\n"
	          
      # loi non lineaire de nature spline, Marrocco ou Marrocco et Saturation
      #  seuls les reels sont pris en compte
	   if obj.valeur[keyN1]['TYPE_LAW']=='NONLINEAR' :
	              texte+="            LAW NONLINEAR\n"
		      texte+="            HOMOGENOUS TRUE\n"
		      texte+="            ISOTROPIC TRUE\n"
	              texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE"])+" 0\n"
		      texte+="            [NONLINEAR \n"
		      texte+="                ISOTROPY TRUE\n"
		      texte+="                NATURE "+str(obj.valeur[keyN1]['NATURE'])+"\n"
		      for keyN2 in obj.valeur[keyN1] :
		          if keyN2 != 'TYPE_LAW' and keyN2 != 'VALUE' and keyN2 != 'NATURE' :
		               texte+="                "+keyN2+" "+str(obj.valeur[keyN1][keyN2])+"\n"
	              texte+="            ]"+"\n"

      # fin du sous bloc de propriete
	   texte+="         ]"+"\n"
       #print "texte = ", texte    
       self.dictMaterNocond[obj.get_sdname()]=[texte,]
 
   def generMATERIALSZSURFACIC(self,obj):
      # preparation du sous bloc ZSURFACIC
       texte=""
       #print "______________zsurf_____________"
       for keyN1 in obj.valeur :
	   if keyN1=='MAT_REF': continue
  #         print "keyN1=", keyN1
#	   print obj.valeur[keyN1]['TYPE_LAW']
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
	         texte+="            VALUE "
                 chC= self.formateCOMPLEX(obj.valeur[keyN1]["VALUE_COMPLEX"])
	         texte+= chC+"\n"
	          
	   texte+="         ]"+"\n"

       self.dictMaterZsurfacic[obj.get_sdname()]=[texte,]

   def generMATERIALSEMISO(self,obj):
      # preparation du sous bloc EMISO
       texte=""
       texte+="        CONDUCTIVITY MED "+str(obj.valeur["CONDUCTIVITY_File"])+"\n"
       texte+="        PERMEABILITY MED "+str(obj.valeur["PERMEABILITY_File"])+"\n"

 #      print "obj get sdname= ", obj.get_sdname()
    #   if obj.get_sdname() in self.dictMaterEmIso.keys() :
     #    self.dictMaterEmIso[obj.get_sdname()].append(texte) 
      # else :
       self.dictMaterEmIso[obj.get_sdname()]=[texte,]
  
   def generMATERIALSEMANISO(self,obj):
      # preparation du sous bloc EMANISO
       texte=""
       texte+="        CONDUCTIVITY  "+str(obj.valeur["CONDUCTIVITY_File"])+"\n"
       texte+="        PERMEABILITY  "+str(obj.valeur["PERMEABILITY_File"])+"\n"

     #  print "obj get sdname= ", obj.get_sdname()
     #  if obj.get_sdname() in self.dictMaterEmAnIso.keys() :
     #    self.dictMaterEmAnIso[obj.get_sdname()].append(texte) 
     #  else :
       self.dictMaterEmAnIso[obj.get_sdname()]=[texte,]
   
   def generMATERIALSNILMAT(self,obj):
      # preparation du sous bloc NILMAT
       texte=""
       self.dictMaterNilmat[obj.get_sdname()]=[texte,]
   
   def generMATERIALSZINSULATOR(self,obj):
      # preparation du sous bloc ZINSULATOR
       texte=""
       self.dictMaterZinsulator[obj.get_sdname()]=[texte,]

#-------------------------------------------------------------------

   def generSOURCES(self,obj):
      # preparation du bloc SOURCES du fichier PHYS 
     #     print "gener sources obj valeur = ", obj.valeur
          texte=""
	  try :
              source=obj.valeur['TYPE_SOURCE']
              if source=="STRANDED_INDUCTOR" : self.generSOURCES_ST_IND(obj)
              if source=="HPORT" : self.generSOURCES_H_PORT(obj)
              if source=="EPORT" : self.generSOURCES_E_PORT(obj)
	  except:
	      pass

   def generSOURCES_ST_IND(self,obj):
      # preparation du sous bloc STRANDED INDUCTOR 
          texte=""
	  try :
	      texte+="        NTURNS "+ str(obj.valeur['NTURNS']) + "\n"
	      texte+="        CURJ POLAR " + str(obj.valeur['CURJ']) +" " +str(obj.valeur['POLAR'])+"\n" 
              self.dictSourceStInd[obj.get_sdname()]=[texte,]
  #            print texte
	  except:
	      pass

   def generSOURCES_H_PORT(self,obj):
      # preparation du sous bloc HPORT  
          texte=""
	  try :
	      texte+="        TYPE "+ str(obj.valeur['TYPE']) + "\n"
	      texte+="        AMP POLAR " + str(obj.valeur['AMP']) +" " +str(obj.valeur['POLAR'])+"\n" 
              self.dictSourceHport[obj.get_sdname()]=[texte,]
  #            print texte
	  except:
	      pass

   def generSOURCES_E_PORT(self,obj):
      # preparation du sous bloc EPORT  
          texte=""
	  try :
	      texte+="        TYPE "+ str(obj.valeur['TYPE']) + "\n"
	      texte+="        AMP POLAR " + str(obj.valeur['AMP']) +" " +str(obj.valeur['POLAR'])+"\n" 
              self.dictSourceEport[obj.get_sdname()]=[texte,]
  #            print texte
	  except:
	      pass

#---------------------------------------------------------------------------------------
# traitement fichier PHYS
#---------------------------------------------------------------------------------------

   def generBLOC_VERSION(self,obj) :
      # constitution du bloc VERSION du fichier PHYS
      # creation d une entite  VERSION ; elle sera du type PROC car decrit ainsi
      # dans le du catalogue
      version=obj.addentite('VERSION',pos=None)
      self.generPROC_ETAPE(obj.etapes[0])
      self.texteCarmel3D+="["+obj.etapes[0].nom+"\n"
      for cle in obj.etapes[0].valeur :
          self.texteCarmel3D+="   "+cle+" "+str(obj.etapes[0].valeur[cle])+"\n"
      self.texteCarmel3D+="]\n"
      # destruction de l entite creee 
      obj.suppentite(version)

#----------------------------------------------------------------------------------------
   def generBLOC_MATERIALS(self) :
      '''
      Prepare une partie du contenu du fichier de parametres (PHYS) pour le code Carmel3D
      (bloc MATERIALS) 
      le bloc MATERIALS existe toujours ! 
      '''
      #print "cle dico materconductor : " , self.dictMaterConductor.keys()
      #print "cle dico materdielectric : " , self.dictMaterNocond.keys()
    
      # constitution du bloc MATERIALS du fichier PHYS
      self.texteCarmel3D+="[MATERIALS\n"

      # constitution du bloc CONDUCTOR du fichier PHYS si existe
      if self.dictMaterConductor != {} : self.creaBLOC_CONDUCTOR()
     
      # constitution du bloc NOCOND du fichier PHYS si exixte
      if self.dictMaterNocond != {} : self.creaBLOC_NOCOND()
     
      # constitution du bloc ZSURFACIC du fichier PHYS si exixte
      if self.dictMaterZsurfacic != {} : self.creaBLOC_ZSURFACIC()
     
      # constitution du bloc EM_ISOTROPIC_FILES du fichier PHYS si exixte
      if self.dictMaterEmIso != {} : self.creaBLOC_EMISO()
     
      # constitution du bloc EM_ANISOTROPIC_FILES du fichier PHYS si exixte
      if self.dictMaterEmAnIso != {} : self.creaBLOC_EMANISO()
     
      # constitution du bloc NILMAT du fichier PHYS si exixte
      if self.dictMaterNilmat != {} : self.creaBLOC_NILMAT()
     
      # constitution du bloc ZINSULATOR du fichier PHYS si exixte
      if self.dictMaterZinsulator != {} : self.creaBLOC_ZINSULATOR()
     
      # fin du bloc MATERIALS du fichier PHYS
      self.texteCarmel3D+="]\n"
  
    
   def creaBLOC_CONDUCTOR(self) :
      # constitution du bloc CONDUCTOR du fichier PHYS
    
      for cle in self.dictMaterConductor.keys():
          self.texteCarmel3D+="     [CONDUCTOR\n"
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour materiau : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          for chaine in self.dictMaterConductor[cle] :
              self.texteCarmel3D+=chaine
     
          self.texteCarmel3D+="     ]\n"


   def creaBLOC_NOCOND(self) :
      # constitution du bloc NOCOND du fichier PHYS
    
      for cle in self.dictMaterNocond.keys():
          self.texteCarmel3D+="     [NOCOND\n"
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour materiau : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          for chaine in self.dictMaterNocond[cle] :
              self.texteCarmel3D+=chaine
          self.texteCarmel3D+="     ]\n"


   def creaBLOC_ZSURFACIC(self) :
      # constitution du bloc ZSURFACIC du fichier PHYS
    
      for cle in self.dictMaterZsurfacic.keys():
          self.texteCarmel3D+="     [ZSURFACIC\n"
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
    
      for cle in self.dictMaterEmIso.keys():
          self.texteCarmel3D+="     [EM_ISOTROPIC_FILES\n"
          for chaine in self.dictMaterEmIso[cle] :
              self.texteCarmel3D+=chaine
          self.texteCarmel3D+="     ]\n"

   def creaBLOC_EMANISO(self) :
      # constitution du bloc EMANISO du fichier PHYS
    
      for cle in self.dictMaterEmAnIso.keys():
          self.texteCarmel3D+="     [EM_ANISOTROPIC_FILES\n"
          for chaine in self.dictMaterEmAnIso[cle] :
              self.texteCarmel3D+=chaine
          self.texteCarmel3D+="     ]\n"

   def creaBLOC_ZINSULATOR(self) :
      # constitution du bloc ZINSULATOR du fichier PHYS
    
      for cle in self.dictMaterZinsulator.keys():
          self.texteCarmel3D+="     [ZINSULATOR\n"
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour materiau : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          self.texteCarmel3D+="     ]\n"

   def creaBLOC_NILMAT(self) :
      # constitution du bloc NILMAT du fichier PHYS
    
      for cle in self.dictMaterNilmat.keys():
          self.texteCarmel3D+="     [NILMAT\n"
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour materiau : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          self.texteCarmel3D+="     ]\n"

#----------------------------------------------------------------------------------------
   def generBLOC_SOURCES(self):
      
      # constitution du bloc SOURCES du fichier PHYS
      self.texteCarmel3D+="[SOURCES\n"

      if self.dictSourceStInd != {} : self.creaBLOC_ST_IND()

      if self.dictSourceEport != {} : self.creaBLOC_EPORT()

      if self.dictSourceHport != {} : self.creaBLOC_HPORT()

      # fin du bloc SOURCES du fichier PHYS
      self.texteCarmel3D+="]\n"


   def creaBLOC_ST_IND(self) :
      # constitution du bloc STRANDED INDUCTOR du fichier PHYS
    
      for cle in self.dictSourceStInd.keys():
          self.texteCarmel3D+="     [STRANDED INDUCTOR\n"
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour source : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          for chaine in self.dictSourceStInd[cle] :
              self.texteCarmel3D+=chaine
          self.texteCarmel3D+="     ]\n"

   def creaBLOC_EPORT(self) :
      # constitution du bloc EPORT du fichier PHYS
    
      for cle in self.dictSourceEport.keys():
          self.texteCarmel3D+="     [EPORT\n"
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour source : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          for chaine in self.dictSourceEport[cle] :
              self.texteCarmel3D+=chaine
          self.texteCarmel3D+="     ]\n"

   def creaBLOC_HPORT(self) :
      # constitution du bloc HPORT du fichier PHYS
    
      for cle in self.dictSourceHport.keys():
          self.texteCarmel3D+="     [HPORT\n"
          if cle not in self.dictName.keys():
              print "Attention : groupe de maille non defini pour source : ",cle
              print "fichier phys incomplet "
              self.texteCarmel3D+=str(self.dictName["grm_def"])
          else : 
              self.texteCarmel3D+=str(self.dictName[cle])
          for chaine in self.dictSourceHport[cle] :
              self.texteCarmel3D+=chaine
          self.texteCarmel3D+="     ]\n"

#----------------------------------------------------------------------------

   def formateCOMPLEX(self,nbC):
 # prise en compte des differentes formes de description d un nombre complexe
 # 3 formats possibles : 2 listes (anciennement tuples?)  et 1 nombre complexe
 #      print "formatage "
 #      print "type : ", type(nbC), "pour ", nbC
       nbformate =""
       if isinstance(nbC,(tuple,list)) :
          if nbC[0] == "'RI'" :
                nbformate = "COMPLEX " + str(nbC[1])+" "+str(nbC[2])            
      
          if nbC[0] == "'MP'" :
                nbformate = "POLAR " + str(nbC[1])+" "+str(nbC[2])            

       else :
          nbformate = "COMPLEX " + str(nbC.real)+" "+str(nbC.imag)

  #     print "nbformate : ", nbformate
       return nbformate

