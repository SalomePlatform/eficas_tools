# -*- coding: utf-8 -*-

# --------------------------------------------------
# --------------------------------------------------

import os
import sys
from Accas import *
import types

# --------------------------------------------------
# definition d une classe pour les materiaux
# definition d une classe pour les groupes de mailles
# definition d une classe pour les laws non lineaires
# --------------------------------------------------
class materiau ( ASSD ) : pass
class grmaille ( ASSD ) : pass
class law    ( ASSD ) : pass


#CONTEXT.debug = 1
# --------------------------------------------------
# déclaration du jeu de commandes : 1ere instruction du catalogue obligatoire 
#---------------------------------------------------

JdC = JDC_CATA ( code = 'CARMEL3D',
#                execmodul = None,
                  regles =(
                           AU_MOINS_UN ('MATERIALS'),
#                           AU_MOINS_UN ('SOURCES'),
#			    A_CLASSER ('MATERIALS','SOURCES'),
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

              MON_MATER =  SIMP (statut="f",
 		                 typ=(materiau,),
                                 ang="name of the linked material",
 		                 fr ="nom du materiau associe",
                                ), 
                      )


#=========================================================
# le fichier .PHYS contient 3 blocs et jusqu'a 3 niveaux de sous-blocs
# 
#================================
# 1er bloc : bloc VERSION
# ce bloc est volontairement cache dans l IHM 
#================================

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

#================================
# 2eme bloc : bloc MATERIALS
#================================
#definition des matériax utilisateurs 
# a partir des materiaux de reference
#------------------------------------
#
MATERIALS = OPER (nom = "MATERIALS",
                    op = None,
	            repetable = 'n',
		    ang= "material block definition", 
		    fr= "definition d un materiau", 
                    sd_prod= materiau,

            MAT_REF = SIMP(statut='o',
                           typ='TXM',
	                   into=("MAT_REF_COND1","MAT_REF_DIEL1",
		                 "MAT_REF_ZSURF1","MAT_REF_NILMAT","MAT_REF_EM_ISOTROPIC1","MAT_REF_EM_ANISOTROPIC1")
		          ),

#------------------------------------
# sous bloc niveau 1 : CONDUCTOR
#------------------------------------
#  1er materiau Conductor de reference 
#------------------------------------
  mat_ref_c1_properties = BLOC(condition="MAT_REF=='MAT_REF_COND1'",
  
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
 	         LAW             = SIMP (statut="o",
 		                         typ="TXM",
                                         defaut="SIGMA1",
		                         into = ("SIGMA1","SIGMA2"),
                                         ang = "conductivity law",
                                         fr = "loi de conductivite",
 				        ),
		 
                param_sigma1 = BLOC(condition="LAW=='SIGMA1'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_COMPLEX",
		                         into = ("LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		               ), # fin bloc sigma1

                param_sigma2 = BLOC(condition="LAW=='SIGMA2'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc sigma2
	 

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
	         LAW             = SIMP (statut="o",
 		                         typ="TXM",
                                         defaut="MU2",
		                         into = ("MU1","MU2"),
                                         ang = "permeability law",
                                         fr = "loi de permeabilite",
				        ),


                param_mu1 = BLOC(condition="LAW=='MU1'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc mu1

                param_mu2 = BLOC(condition="LAW=='MU2'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_COMPLEX",
		                         into = ("LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc mu2
	         ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor1
# 
##------------------------------------
## sous bloc niveau 1 : DIELECTRIC
##------------------------------------
# 1er materiau Dielectric de reference 
#------------------------------------
  mat_ref_d1_properties = BLOC(condition="MAT_REF=='MAT_REF_DIEL1'",

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
 	         LAW             = SIMP (statut="o",
 		                         typ="TXM",
                                         defaut="EPSILON1",
		                         into = ("EPSILON1","EPSILON2"),
                                         ang = "permittivity law",
                                         fr = "loi de permittivite",
 				        ),

                 param_epsilon1 = BLOC(condition="LAW=='EPSILON1'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc epsilon1

                param_epsilon2 = BLOC(condition="LAW=='EPSILON2'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_COMPLEX",
		                         into = ("LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc epsilon2
		 
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
	         LAW             = SIMP (statut="o",
 		                         typ="TXM",
                                         defaut="MU4",
		                         into = ("MU4","MU5","MU6","MU7","MU8"),
                                         ang = "permeability law",
                                         fr = "loi de permeabilite",
				        ),

                param_mu4 = BLOC(condition="LAW=='MU4'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc mu4

                param_mu5 = BLOC(condition="LAW=='MU5'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_COMPLEX",
		                         into = ("LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc mu5

                param_mu6 = BLOC(condition="LAW=='MU6'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="SPLINE",
		                         into = ("SPLINE"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
				        ),

                      FILENAME = SIMP (statut="o", 
	                               typ=("Fichier",'All Files (*)',),
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
			     ), # fin BLOC mu6

                param_mu7 = BLOC(condition="LAW=='MU7'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="MARROCCO",
		                         into = ("MARROCCO"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
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
			), # fin BLOC mu7
                                   
                param_mu8 = BLOC(condition="LAW=='MU8'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="MARROCCO+SATURATION",
		                         into = ("MARROCCO+SATURATION"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
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
			), # fin BLOC mu8

	         ), # fin FACT PERMEABILITY

 ), # fin BLOC dielectric1

# ------------------------------------
# sous bloc niveau 1 : ZSURFACIC
#------------------------------------
# 1er materiau Zsurfasic de reference 
#------------------------------------
  mat_ref_z1_properties = BLOC(condition="MAT_REF=='MAT_REF_ZSURF1'",

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
 	         LAW             = SIMP (statut="o",
 		                         typ="TXM",
                                         defaut="SIGMA3",
		                         into = ("SIGMA3","SIGMA4"),
                                         ang = "conductivity law",
                                         fr = "loi de conductivite",
 				        ),

                 param_sigma3 = BLOC(condition="LAW=='SIGMA3'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc sigma3

                param_sigma4 = BLOC(condition="LAW=='SIGMA4'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_COMPLEX",
		                         into = ("LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc sigma4
		 

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
	         LAW             = SIMP (statut="o",
 		                         typ="TXM",
                                         defaut="MU1",
		                         into = ("MU1","MU2"),
                                         ang = "permeability law",
                                         fr = "loi de permeabilite",
				        ),

                param_mu1 = BLOC(condition="LAW=='MU1'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_REAL",
		                         into = ("LINEAR_REAL"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_REAL = SIMP (statut="o",
		                         typ="R", 
		                         defaut=1,
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
		                        ),
		            ), # fin bloc mu1

                param_mu2 = BLOC(condition="LAW=='MU2'",
                      TYPE_LAW   = SIMP (statut="o",
		                         typ="TXM",
				         defaut="LINEAR_COMPLEX",
		                         into = ("LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
				        ),
	              VALUE_COMPLEX = SIMP (statut="o",
		                         typ="C", 
		                         defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
		                        ),
		            ), # fin bloc mu2
	         ), # fin FACT PERMEABILITY

	     ), # fin bloc ZSURFACIC1


#===================================
# 1 type de matériau fictif 
#---------------------------------------
# sous bloc niveau 1 : materiau NILMAT   
#---------------------------------------
#  1er materiau Nilmat de reference 
#------------------------------------
  
# aucun parametre a saisir pour ce materiau


#============================================
# 1 type de matériau isotropique non homogene
#----------------------------------------
# sous bloc niveau 1 : EM_ISOTROPIC_FILES   
#----------------------------------------
#  1er materiau EM_isotropic de reference 
#----------------------------------------
   mat_ref_i1_properties=BLOC(condition="MAT_REF=='MAT_REF_EM_ISOTROPIC1'", 
               
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

#============================================
# 1 type de matériau  non isotropique 
#----------------------------------------
# sous bloc niveau 1 : EM_ANISOTROPIC_FILES   
#----------------------------------------
#  1er materiau EM_anisotropic de reference 
#----------------------------------------
   mat_ref_a1_properties=BLOC(condition="MAT_REF=='MAT_REF_EM_ANISOTROPIC1'",
                 
	       CONDUCTIVITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
	                                 ang="CONDUCTIVITY .mater data file name",
	                                 fr ="nom du fichier .mater CONDUCTIVITY",
	                                ),
	       PERMEABILITY_File = SIMP (statut="o", 
	                                 typ=("Fichier",'.mater Files (*.mater)',),
	                                 ang="PERMEABILITY .mater data file name",
	                                 fr ="nom du fichier .mater PERMEABILITY",
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

