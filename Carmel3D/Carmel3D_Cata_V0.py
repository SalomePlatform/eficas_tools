# -*- coding: utf-8 -*-

# --------------------------------------------------
# --------------------------------------------------

import os
import sys
from Accas import *
import types
# repertoire ou sont stockés le catalogue carmel3d 
# et les fichiers de donnees des materiaux de reference
from prefs_CARMEL3D import repIni

#print "catalogue carmel"
#print "repIni = ", repIni

# --------------------------------------------------
# definition d une classe pour les materiaux
# definition d une classe pour les groupes de mailles
# --------------------------------------------------
class materiau ( ASSD ) : pass
class grmaille ( ASSD ) : pass

# definition d une classe de Tuple : ne sert pas actuellement
class Tuple :

   def __init__(self,ntuple):
     self.ntuple=ntuple
 
   def __convert__(self,valeur):
     if type(valeur) == types.StringType:
       return None
     if len(valeur) != self.ntuple:
       return None
     return valeur
 
   def info(self):
     return "Tuple de %s elements" % self.ntuple

   __repr__=info
   __str__=info


#CONTEXT.debug = 1
# --------------------------------------------------
# déclaration du jeu de commandes : 1ere instruction du catalogue obligatoire 
#---------------------------------------------------

JdC = JDC_CATA ( code = 'CARMEL3D',
#                execmodul = None,
                  regles =(
                           AU_MOINS_UN ('MATERIALS'),
                           ),
                 ) # Fin JDC_CATA
##=========================================================

# --------------------------------------------------
# definition de groupe de mailles
# et association du nom du materiau au groupe de mailles
#---------------------------------------------------

MESH_GROUPE     = OPER (nom = "MESH_GROUPE",
                    op = None,
	            repetable = 'n',
                    UIinfo= {"groupes":("Definition",)},
		    fr= "definition du groupe de mailles", 
		    ang = " mesh group definition", 
                    sd_prod= grmaille,

# ----------------------------------------------------------
# le mot cle SIMP doit etre facultatif sinon la recuperation 
# des groupes de mailles sous SALOME ne fonctionne pas car 
# le concept ne peut pas etre nomme car non valide
#-----------------------------------------------------------
              MON_MATER =  SIMP (statut="f",
 		                 typ=(materiau,),
                                 ang="name of the linked material",
 		                 fr ="nom du materiau associe",
                                ), 
                      )


#======================================================================
# le fichier .PHYS contient 3 blocs et jusqu'a 3 niveaux de sous-blocs
# 
#======================================================================
# 1er bloc : bloc VERSION
# ce bloc est volontairement cache dans l IHM 
#===================================================

VERSION = PROC ( nom = "VERSION",
                        op = None,
		        repetable = 'n',
                        UIinfo= {"groupes":("CACHE",)},
                        ang= "version block definition", 

#----------------------
# Liste des parametres
#----------------------
		
   NUM      = SIMP (statut="o",
                    typ="I",
		    defaut=1, 
                    ang="version number of the physical model", 
                    into=( 1,),
                   ),
   FILETYPE = SIMP (statut="o",
                    typ="TXM",
		    defaut="PHYS", 
                    ang="file type",
                    into=( "PHYS",),
                   ),

) # Fin PROC VERSION

#===================================================================
# 2eme bloc : bloc MATERIALS
#===================================================================
# definition des matériaux utilisateurs 
# a partir des materiaux de reference ou de materiaux generiques
#-------------------------------------------------------------------
#
MATERIALS = OPER (nom = "MATERIALS",
                    op = None,
	            repetable = 'n',
		    ang= "material block definition", 
		    fr= "definition d un materiau", 
                    sd_prod= materiau,

#---------------------------------------------------------------------
# liste des matériaux de reference fournis par THEMIS et  des
# materiaux generiques (les materiaux generiques peuvent etre utilises 
# si aucun materiau de reference  ne convient) 
#---------------------------------------------------------------------
            MAT_REF = SIMP(statut='o',
                           typ='TXM',
	                   into=(
#  type CONDUCTOR lineaire 
                                 "ACIER_Noir","ACIER_PE","ACIER_CIMBLOT",
		                 "ALU","BRONZE","CUIVRE",
		                 "FERRITE_Mn_Zn","FERRITE_Ni_Zn",
                                 "INCONEL600",
                                 "POTASSE",
#  type NOCOND 
                                 "AIR","FERRITEB30",
                                 "FEV470","FEV600","FEV800","FEV1000",
                                 "E24","HA600",
                                 "M600_65",
#  type EM_ANISO 
                                 "M6X","M6X_lineaire","M6X_homog", 
#  type EM_ISO 
                                 "M6X2ISO1", 
#  materiaux generiques 
                                 "COND_LINEAR",
                                 "NOCOND_LINEAR",
                                 "NOCOND_NL_MAR",
                                 "NOCOND_NL_MARSAT",
                                 "ZINSULATOR","ZSURFACIC",
                                 "NILMAT","EM_ISOTROPIC","EM_ANISOTROPIC"
                                ),
                           ang = "reference  materials list",
                           fr  = "liste des materiaux de reference",
		          ),

##############################################################################
#------------------------------------------------------
# sous bloc niveau 1 : CONDUCTOR
#------------------------------------------------------
#  materiau de reference type CONDUCTOR lineaire : ALU 
#------------------------------------------------------
   ALU_properties = BLOC(condition="MAT_REF=='ALU'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",

                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=3.448E7,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor1
 
#--------------------------------------------------------
# materiau de reference type CONDUCTOR  lineaire : BRONZE
#--------------------------------------------------------
   BRONZE_properties = BLOC(condition="MAT_REF=='BRONZE'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",

                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000E6,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=3.000000,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor2

#---------------------------------------------------
# materiau de reference type CONDUCTOR  lineaire : INCONEL600
#----------------------------------------------------
  INCONEL600_properties = BLOC(condition="MAT_REF=='INCONEL600'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",

                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=9.700000E5,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.010000,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor3

#---------------------------------------------------------------------
# materiau de reference de type CONDUCTOR  lineaire : FERRITE Mn Zn
#---------------------------------------------------------------------
  FERRITE_Mn_Zn_properties = BLOC(condition="MAT_REF=='FERRITE_Mn_Zn'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
  CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000E0,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc

	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.250000E3,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor4

#------------------------------------------------------------------
# materiau de reference de type CONDUCTOR lineaire : FERRITE Ni Zn
#------------------------------------------------------------------
  FERRITE_Ni_Zn_properties = BLOC(condition="MAT_REF=='FERRITE_Ni_Zn'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
  CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000E-6,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc

	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.500000E1,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor5

#-------------------------------------------------------------
# materiau de reference type CONDUCTOR lineaire : ACIER Noir
#-------------------------------------------------------------
   ACIER_Noir_properties = BLOC(condition="MAT_REF=='ACIER_Noir'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",

                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=6.000000E6,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 

	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000E2,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor6


#------------------------------------------------------------
# materiau de reference type CONDUCTOR lineaire : ACIER PE
#------------------------------------------------------------
   ACIER_PE_properties = BLOC(condition="MAT_REF=='ACIER_PE'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",

                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.750000E6,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=7.000000E1,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor7

#---------------------------------------------------------------
# materiau de reference type CONDUCTOR lineaire : ACIER CIMBLOT
#---------------------------------------------------------------
   ACIER_CIMBLOT_properties = BLOC(condition="MAT_REF=='ACIER_CIMBLOT'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",

                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=3.000000E6,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=5.000000E1,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor8

#----------------------------------------------------------------
# materiau de reference type CONDUCTOR lineaire : CUIVRE
#----------------------------------------------------------------
   CUIVRE_properties = BLOC(condition="MAT_REF=='CUIVRE'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",

                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=5.85000000E07,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc

	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor9

#---------------------------------------------------------
# materiau de reference type CONDUCTOR lineaire : POTASSE
#---------------------------------------------------------
   POTASSE_properties = BLOC(condition="MAT_REF=='POTASSE'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",

                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=7.143E1,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000E0,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor10

#-------------------------------------------------
#  materiau generique de type CONDUCTOR  lineaire 
#-------------------------------------------------
   COND_L_properties = BLOC(condition="MAT_REF=='COND_LINEAR'",
  
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",

                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.0,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc

	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.0,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor
 
###################################################################################################
##--------------------------------------------
## sous bloc niveau 1 : NOCOND
##----------------------------------------------------------
# materiau generique de type NOCOND lineaire  
#-----------------------------------------------------------
  NOCOND_L_properties = BLOC(condition="MAT_REF=='NOCOND_LINEAR'",
#
#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
         			         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.0,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMITTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------

     PERMEABILITY = FACT ( statut="o", 
                           ang ="Permeability properties",
                           fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
         			         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.0,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT 
 
             ), # fin BLOC

##-----------------------------------------------------
# materiau de reference de type NOCOND lineaire : AIR  
#------------------------------------------------------
  AIR_properties = BLOC(condition="MAT_REF=='AIR'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------

     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	         ), # fin FACT PERMEABILITY

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMITTIVITY

            ), # fin BLOC NOCOND
#
##-------------------------------------------------------------
# materiau de reference de type NOCOND lineaire : FERRITE B30  
#--------------------------------------------------------------
  FERRITEB30_properties = BLOC(condition="MAT_REF=='FERRITEB30'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------

     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.100000E3,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	         ), # fin FACT PERMEABILITY

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.000000,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	 
	         ), # fin FACT PERMITTIVITY

            ), # fin BLOC NOCOND
#--------------------------------------------------------
# materiau de reference de type NOCOND non lineaire : E24  
#--------------------------------------------------------
  E24_properties = BLOC(condition="MAT_REF=='E24'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="SPLINE",
		                         into = ("SPLINE"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),
	              VALUE      = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),

                      FILENAME = SIMP (statut="o", 
	                               typ=("Fichier",'All Files (*)',),
		                       defaut=str(repIni)+"/E24",
	                               ang="data file name",
			               fr ="nom du fichier",
			              ),
		      APPLIEDTO = SIMP (statut="o",	
		                        typ="TXM",   
		                        into=("B(H)&H(B)","B(H)","H(B)"),
				        defaut="B(H)&H(B)",
				        ang="spline applied to",
				        fr ="spline appliquee a ",
				       ),

	         ), # fin FACT PERMEABILITY

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc complex
		 
	         ), # fin FACT PERMITTIVITY
 ), # fin BLOC E24

##------------------------------------------------------------
# materiau de reference de type NOCOND  non lineaire : FEV470 
#-------------------------------------------------------------
  FEV470_properties = BLOC(condition="MAT_REF=='FEV470'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="SPLINE",
		                         into = ("SPLINE"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),
	              VALUE      = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),

                      FILENAME = SIMP (statut="o", 
	                               typ=("Fichier",'All Files (*)',),
		                       defaut=str(repIni)+"/FEV470",
	                               ang="data file name",
			               fr ="nom du fichier",
			              ),
		      APPLIEDTO = SIMP (statut="o",	
		                        typ="TXM",   
		                        into=("B(H)&H(B)","B(H)","H(B)"),
				        defaut="B(H)&H(B)",
				        ang="spline applied to",
				        fr ="spline appliquee a ",
				       ),

	         ), # fin FACT PERMEABILITY

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc complex
		 
	         ), # fin FACT PERMITTIVITY

 ), # fin BLOC FEV470

##---------------------------------------------------------
# materiau de reference de type NOCOND : FEV600 
#----------------------------------------------------------
  FEV600_properties = BLOC(condition="MAT_REF=='FEV600'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="SPLINE",
		                         into = ("SPLINE"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),
	              VALUE      = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),

                      FILENAME = SIMP (statut="o", 
	                               typ=("Fichier",'All Files (*)',),
		                       defaut=str(repIni)+"/FEV600",
	                               ang="data file name",
			               fr ="nom du fichier",
			              ),
		      APPLIEDTO = SIMP (statut="o",	
		                        typ="TXM",   
		                        into=("B(H)&H(B)","B(H)","H(B)"),
				        defaut="B(H)&H(B)",
				        ang="spline applied to",
				        fr ="spline appliquee a ",
				       ),

	         ), # fin FACT PERMEABILITY

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc complex
		 
	         ), # fin FACT PERMITTIVITY

 ), # fin BLOC FEV600

##---------------------------------------------------------
# materiau de reference de type NOCOND : FEV800 
#----------------------------------------------------------
  FEV800_properties = BLOC(condition="MAT_REF=='FEV800'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="SPLINE",
		                         into = ("SPLINE"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),
	              VALUE      = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),

                      FILENAME = SIMP (statut="o", 
	                               typ=("Fichier",'All Files (*)',),
		                       defaut=str(repIni)+"/FEV800",
	                               ang="data file name",
			               fr ="nom du fichier",
			              ),
		      APPLIEDTO = SIMP (statut="o",	
		                        typ="TXM",   
		                        into=("B(H)&H(B)","B(H)","H(B)"),
				        defaut="B(H)&H(B)",
				        ang="spline applied to",
				        fr ="spline appliquee a ",
				       ),

	         ), # fin FACT PERMEABILITY

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc complex
		 
	         ), # fin FACT PERMITTIVITY

 ), # fin BLOC FEV800

##-----------------------------------------------
# materiau de reference de type NOCOND : FEV1000 
#------------------------------------------------
  FEV1000_properties = BLOC(condition="MAT_REF=='FEV1000'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="SPLINE",
		                         into = ("SPLINE"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),
	              VALUE      = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),

                      FILENAME = SIMP (statut="o", 
	                               typ=("Fichier",'All Files (*)',),
		                       defaut=str(repIni)+"/FEV1000",
	                               ang="data file name",
			               fr ="nom du fichier",
			              ),
		      APPLIEDTO = SIMP (statut="o",	
		                        typ="TXM",   
		                        into=("B(H)&H(B)","B(H)","H(B)"),
				        defaut="B(H)&H(B)",
				        ang="spline applied to",
				        fr ="spline appliquee a ",
				       ),

	         ), # fin FACT PERMEABILITY

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc complex
		 
	         ), # fin FACT PERMITTIVITY

 ), # fin BLOC FEV1000

##----------------------------------------------------------
# materiau de reference de type NOCOND : HA600 
#-----------------------------------------------------------
  HA600_properties = BLOC(condition="MAT_REF=='HA600'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="SPLINE",
		                         into = ("SPLINE"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),
	              VALUE      = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),

                      FILENAME = SIMP (statut="o", 
	                               typ=("Fichier",'All Files (*)',),
		                       defaut=str(repIni)+"/HA600",
	                               ang="data file name",
			               fr ="nom du fichier",
			              ),
		      APPLIEDTO = SIMP (statut="o",	
		                        typ="TXM",   
		                        into=("B(H)&H(B)","B(H)","H(B)"),
				        defaut="B(H)&H(B)",
				        ang="spline applied to",
				        fr ="spline appliquee a ",
				       ),

	         ), # fin FACT PERMEABILITY

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc complex
		 
	         ), # fin FACT PERMITTIVITY

 ), # fin BLOC HA600 

##-----------------------------------------------
# materiau de reference de type NOCOND : M600_65 
#------------------------------------------------
  M600_65_properties = BLOC(condition="MAT_REF=='M600_65'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="SPLINE",
		                         into = ("SPLINE"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),
	              VALUE      = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),

                      FILENAME = SIMP (statut="o", 
	                               typ=("Fichier",'All Files (*)',),
		                       defaut=str(repIni)+"/M600_65",
	                               ang="data file name",
			               fr ="nom du fichier",
			              ),
		      APPLIEDTO = SIMP (statut="o",	
		                        typ="TXM",   
		                        into=("B(H)&H(B)","B(H)","H(B)"),
				        defaut="B(H)&H(B)",
				        ang="spline applied to",
				        fr ="spline appliquee a ",
				       ),

	         ), # fin FACT PERMEABILITY

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc complex
		 
	         ), # fin FACT PERMITTIVITY

 ), # fin BLOC M600_65


##------------------------------------------------------------------
# materiau generique de type NOCOND  non lineaire MARROCCO  
#-------------------------------------------------------------------
  NOCOND_NLM_properties = BLOC(condition="MAT_REF=='NOCOND_NL_MAR'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
#
#
  PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="MARROCCO",
		                         into = ("MARROCCO"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),
	              VALUE      = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
			   ALPHA    = SIMP (statut="o", 
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="alpha parameter",
					    fr ="parametre alpha" ,
					   ),
			   TAU      = SIMP (statut="o",	
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="tau parameter",
					    fr ="parametre tau" ,
					    ),
			   C        = SIMP (statut="o",	
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="c parameter",
					    fr ="parametre c" ,
					    ),
			   EPSILON  = SIMP (statut="o",	
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="epsilon parameter",
					    fr ="parametre epsilon" ,
					    ),
                                  
              ), # fin FACT
 
#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc complex
		 
	         ), # fin FACT PERMITTIVITY
   ), # fin BLOC

##--------------------------------------------------------------------
# materiau generique de type NOCOND  non lineaire MARROCCO+SATURATION  
#---------------------------------------------------------------------
  NOCOND_NLMS_properties = BLOC(condition="MAT_REF=='NOCOND_NL_MARSAT'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
#
#
  PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="MARROCCO+SATURATION",
		                         into = ("MARROCCO+SATURATION"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),
	              VALUE      = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
			   ALPHA    = SIMP (statut="o", 
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="alpha parameter",
					    fr ="parametre alpha" ,
					   ),
			   TAU      = SIMP (statut="o",	
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="tau parameter",
					    fr ="parametre tau" ,
					    ),
			   C        = SIMP (statut="o",	
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="c parameter",
					    fr ="parametre c" ,
					    ),
			   EPSILON  = SIMP (statut="o",	
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="epsilon parameter",
					    fr ="parametre epsilon" ,
					    ),
			   BMAX     = SIMP (statut="o",	
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="intersection B",
					    fr ="intersection B" ,
					    ),
			   HSAT     = SIMP (statut="o",	
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="H value",
					    fr ="valeur H" ,
					    ),
			   BSAT     = SIMP (statut="o",	
					    typ="R",
					    defaut=0,
					    val_min=0,
					    ang="B value",
					    fr ="valeur B" ,
					    ),
			   JOIN     = SIMP (statut="o",	
					    typ="TXM",
					    defaut="SPLINE",
					    into= ("SPLINE","PARABOLIC","LINEAR"),
					    ang="type of join between laws",
					    fr ="type de jointure entre les 2 law" ,
					    ),
			   APPLIEDTO = SIMP (statut="o",	
					     typ="TXM",   
					     into=("B(H)&H(B)","B(H)","H(B)"),
					     defaut="B(H)&H(B)",
					     ang="join applied to",
					     fr ="jointure appliquee a ",
					    ),

	         ), # fin FACT PERMEABILITY
#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),

                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1.000000E0,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc complex
		 
	         ), # fin FACT PERMITTIVITY

   ), # fin BLOC


###################################################################################################
# ----------------------------------------
# sous bloc niveau 1 : ZSURFACIC
#i----------------------------------------
# materiau generique de type ZSURFASIC 
#-----------------------------------------
  zsurfacic_properties = BLOC(condition="MAT_REF=='ZSURFACIC'",

#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
  CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.0,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
		 
	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
				        ),
	         ISOTROPIC       = SIMP (statut="f",
		                         typ="TXM",
				         defaut="TRUE",
		                         into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
				        ),
                  TYPE_LAW       = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_COMPLEX","LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
		 
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX'",
	                     VALUE_COMPLEX = SIMP (statut="o",
		                                   typ="C", 
		                                   defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = "saisir une valeur complexe relative",
		                                  ),
		                         ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL'",
	                     VALUE_REAL    = SIMP (statut="o",
		                                   typ="R", 
		                                   defaut=1.0,
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
		                                   ),
		                         ), # fin bloc
	         ), # fin FACT PERMEABILITY

	     ), # fin bloc ZSURFACIC

###################################################################################################
#---------------------------------------------
# sous bloc niveau 1  
#---------------------------------------
# matériau generique de type ZINSULATOR 
#---------------------------------------
  
# aucun parametre a saisir pour ce materiau


###################################################################################################
#---------------------------------------------
# sous bloc niveau 1     
#---------------------------------------------
# matériau generique de type NILMAT (fictif)  
#---------------------------------------------
  
# aucun parametre a saisir pour ce materiau


###################################################################################################
#----------------------------------------------------------
# sous bloc niveau 1 : EM_ISOTROPIC_FILES   
#----------------------------------------------------------
# matériau de reference isotropique non homogene : M6X2ISO1
#-----------------------------------------------------------
   M6X2ISO1_properties=BLOC(condition="MAT_REF=='M6X2ISO1'", 
               
	       CONDUCTIVITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'MED Files (*.med)',),
		                         defaut=str(repIni)+"/M6X2ISO1_sigma.med",
	                                 ang="CONDUCTIVITY MED data file name",
	                                 fr ="nom du fichier MED CONDUCTIVITY",
	                                ),
	       PERMEABILITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'MED Files (*.med)',),
		                         defaut=str(repIni)+"/M6X2ISO1_mu.med",
	                                 ang="PERMEABILITY MED data file name",
	                                 fr ="nom du fichier MED PERMEABILITY",
	                                ),
	      ), # fin bloc EM_ISOTROPIC

#-------------------------------------------------
# matériau isotropique non homogene generique
#-------------------------------------------------
   em_iso_properties=BLOC(condition="MAT_REF=='EM_ISOTROPIC'", 
               
	       CONDUCTIVITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'MED Files (*.med)',),
	                                 ang="CONDUCTIVITY MED data file name",
	                                 fr ="nom du fichier MED CONDUCTIVITY",
	                                ),
	       PERMEABILITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'MED Files (*.med)',),
	                                 ang="PERMEABILITY MED data file name",
	                                 fr ="nom du fichier MED PERMEABILITY",
	                                ),
	      ), # fin bloc EM_ISOTROPIC

###################################################################################################
#----------------------------------------------------------
# sous bloc niveau 1 : EM_ANISOTROPIC_FILES   
##---------------------------------------------------------
# materiau de reference anisotrope non homogene : M6X 
#----------------------------------------------------------
   M6X_properties=BLOC(condition="MAT_REF=='M6X'",
                 
	       PERMEABILITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
		                         defaut=str(repIni)+"/M6X_mu.mater",
	                                 ang="PERMEABILITY .mater data file name",
	                                 fr ="nom du fichier .mater PERMEABILITY",
	                                ),
	       PERMITTIVITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
		                         defaut=str(repIni)+"/M6X_epsilon.mater",
	                                 ang="PERMITTIVITY .mater data file name",
	                                 fr ="nom du fichier .mater PERMITTIVITY",
	                                ),
	      ), # fin bloc EM_ANISOTROPIC

##--------------------------------------------------------------
# materiau de reference anisotrope non homogene : M6X_lineaire 
#---------------------------------------------------------------
   M6X_lineaire_properties=BLOC(condition="MAT_REF=='M6X_lineaire'",
                 
	       PERMEABILITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
		                         defaut=str(repIni)+"/M6X_lineaire_mu.mater",
	                                 ang="PERMEABILITY .mater data file name",
	                                 fr ="nom du fichier .mater PERMEABILITY",
	                                ),
	       CONDUCTIVITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
		                         defaut=str(repIni)+"/M6X_lineaire_sigma.mater",
	                                 ang="CONDUCTIVITY .mater data file name",
	                                 fr ="nom du fichier .mater CONDUCTIVITY",
	                                ),
	      ), # fin bloc EM_ANISOTROPIC
    
##--------------------------------------------------------------
# materiau de reference anisotrope non homogene : M6X_homog 
#---------------------------------------------------------------
   M6X_homog_properties=BLOC(condition="MAT_REF=='M6X_homog'",
                 
	       PERMEABILITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
		                         defaut=str(repIni)+"/M6X_homog_mu.mater",
	                                 ang="PERMEABILITY .mater data file name",
	                                 fr ="nom du fichier .mater PERMEABILITY",
	                                ),
	       CONDUCTIVITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
		                         defaut=str(repIni)+"/M6X_homog_sigma.mater",
	                                 ang="CONDUCTIVITY .mater data file name",
	                                 fr ="nom du fichier .mater CONDUCTIVITY",
	                                ),
	      ), # fin bloc EM_ANISOTROPIC
    
#---------------------------------------------------
# matériau  anisotropique non homogene generique 
#---------------------------------------------------
   em_aniso_properties=BLOC(condition="MAT_REF=='EM_ANISOTROPIC'",
                 
	       PERMEABILITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
	                                 ang="PERMEABILITY .mater data file name",
	                                 fr ="nom du fichier .mater PERMEABILITY",
	                                ),
	       CONDUCTIVITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
	                                 ang="CONDUCTIVITY .mater data file name",
	                                 fr ="nom du fichier .mater CONDUCTIVITY",
	                                ),
	      ), # fin bloc EM_ANISOTROPIC
    

    ) # fin OPER Materials
    
#================================
# 3eme bloc : bloc SOURCES
#================================

SOURCES = PROC ( nom = "SOURCES",
                 op = None,
		 repetable = 'n',
                 ang = "sources block definition", 
                 fr = "definition du bloc sources", 

 STRANDED_INDUCTOR  = FACT (statut="f",
                            fr="stranded inductor source",
                            ang="stranded inductor source",
		
                      NAME     = SIMP (statut="o",
		                       typ="TXM",
                                       ang="name of the source",
                                       fr="nom de la source",
				       ),
                      NTURNS   = SIMP (statut="o",
		                       typ="I",
				       defaut=1,
                                       ang="number of turns in the inductor",
                                       fr="nombre de tours dans l inducteur",
				       ),
                      CURJ     = SIMP (statut="o",
		                       typ="R",
				       defaut=0,
                                       ang="intensity",
                                       fr="intensite",
				       ),
		      POLAR    = SIMP (statut="o",
		                       typ="R",
				       defaut=0,
                                       fr="polarisation",
                                       ang="polarization",
				       ),

                      ), # fin FACT inductor
			    
 EPORT = FACT (statut="f",
               fr="eport source",
               ang="eport source",
		
         NAME     = SIMP (statut="o",
	                  typ="TXM",
                          ang="name of the source",
                          fr="nom de la source",
			  ),
         TYPE     = SIMP (statut="o",
	                  typ="TXM",
			  into=("VOLTAGE","CURRENT"),
                          fr="type de eport source",
                          ang="type of eport source",
			  ),
         AMP      = SIMP (statut="o",
	                  typ="R",
			  defaut=0,
                          fr="amplitude",
                          ang="amplitude",
			  ),
         POLAR    = SIMP (statut="o",
	                  typ="R",
			  defaut=0,
                          fr="polarisation",
                          ang="polarization",
			  ),

               ), # fin FACT eport

 HPORT = FACT (statut="f",
               fr="hport source",
               ang="hport source",
         
	 NAME     = SIMP (statut="o",
	                  typ="TXM",
                          ang="name of the source",
                          fr="nom de la source",
			  ),
         TYPE     = SIMP (statut="o",
	                  typ="TXM",
			  into=("VOLTAGE","CURRENT"),
                          fr="type de hport source",
                          ang="type of hport source",
			  ),
         AMP      = SIMP (statut="o",
	                  typ="R",
			  defaut=0,
                          ang="amplitude",
                          fr="amplitude",
			  ),
         POLAR    = SIMP (statut="o",
	                  typ="R",
			  defaut=0,
                          fr="polarisation",
                          ang="polarization",
			  ),

               ), # fin FACT hport
) # Fin PROC sources

