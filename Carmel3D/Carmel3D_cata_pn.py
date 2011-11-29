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
#                           AU_MOINS_UN ('MATERIALS'),
#                           AU_MOINS_UN ('SOURCES'),
#			    A_CLASSER ('MATERIALS','SOURCES'),
                           ),
                 ) # Fin JDC_CATA
##=========================================================
## definition des parametres d une law 
##
## Constitution de sous bloc NONLINEAR
## produit un objet "bloc NONLINEAR" de type (classe) lawNL 
##------------------------------------------------

L_LAW = OPER (nom = "L_LAW",
                    op = None,
	            repetable = 'n',
		    ang= "", 
		    fr= "", 
                    sd_prod= law,
                    UIinfo= {"groupes":("CACHE",)},
)
LAW = OPER (nom = "LAW",
                    op = None,
	            repetable = 'n',
		    ang= "", 
		    fr= "", 
                    sd_prod= law,

	                       NATURE       =  SIMP (statut="o",
		                                     typ="TXM",
			                             defaut="SPLINE",
						     into=("SPLINE","MARROCCO","MARROCCO+SATURATION"),
						     ang="nature of the law",
						     fr ="nature de la law",
                                                     ), 

                                   SplineParam  =  BLOC (condition="NATURE=='SPLINE'",

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
				                        ), # fin BLOC SplineParam

                                   MarroccoParam= BLOC (condition="NATURE=='MARROCCO'",

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
				                        ), # fin BLOC MarroccoParam
                                   
				   MarroSatuParam= BLOC (condition="NATURE=='MARROCCO+SATURATION'",

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
				                        ), # fin BLOC MarroSatuParam
 ) # fin OPER LAW
LINEAR=L_LAW(),

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

              Material    =  SIMP (statut="f",
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
#definition des 3 types de matériaux isotropiques et homogenes 
#------------------------------------
# sous bloc niveau 1 : CONDUCTOR
#------------------------------------
#
MATERIAU = OPER (nom = "MATERIAU",
                    op = None,
	            repetable = 'n',
		    ang= "CONDUCTOR block definition", 
		    fr= "definition d un materiau", 
                    sd_prod= materiau,
  TYPE = SIMP(statut='o',typ='TXM',into=("CONDUCTOR","DIELECTRIC","ZSURFACIC","NILMAT","EM_ISOTROPIC_FILES","EM_ANISOTROPIC_FILES") ),

#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
  b_conductor=BLOC(condition="TYPE=='CONDUCTOR'",
  
     CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",
                        regles = ( UN_PARMI ('VALUE_REAL','VALUE_COMPLEX'),
                                 ),

 	         LAW             = SIMP (statut="o",
 		                         typ=law,
                                         defaut=LINEAR,
                                         ang = "type of law",
                                         fr = "type de law",
 				        ),
		 
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
	 
	         VALUE_REAL     = SIMP (statut="f",
		                        typ="R", 
                                        ang = "enter a real value",
                                        fr  = "entrer un reel",
				       ),
	         VALUE_COMPLEX  = SIMP (statut="f",
		                        typ="C", 
                                        ang = "enter a complex value",
                                        fr  = "entrer un complexe",
		                       ),

	         ), # fin FACT CONDUCTIVITY

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                        regles = ( UN_PARMI ('VALUE_REAL','VALUE_COMPLEX'),
                                 ),
                
	         LAW             = SIMP (statut="o",
		                         typ=law,
				         defaut="LINEAR",
                                         ang = "type of law",
				        ),
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
	         VALUE_REAL     = SIMP (statut="f",
		                        typ="R", 
                                        ang = "enter a real value",
                                        fr  = "entrer un reel",
				       ),
	         VALUE_COMPLEX  = SIMP (statut="o",
		                        typ="C", 
                                        ang = "enter a complex value",
                                        fr  = "entrer un complexe",
				       ),

	         ), # fin FACT PERMEABILITY


             ) # fin BLOC conductor
    ) # fin OPER Materiau
# 
##------------------------------------
## sous bloc niveau 1 : DIELECTRIC
##------------------------------------
#DIELECTRIC = OPER (nom = "DIELECTRIC",
#                    op = None,
#	            repetable = 'n',
#                    UIinfo= {"groupes":("Isotropic Homogeneous Materials",)},
#		    ang= "DIELECTRIC block definition", 
#		    fr= "definition du bloc DIELECTRIC", 
#                    sd_prod= materiau,
#
#
##------------------------------------------------
## sous bloc niveau 2 : PERMITTTIVITY
##------------------------------------------------
#  PERMITTIVITY = FACT ( statut="o", 
#                        ang ="Permittivity properties",
#                        fr  ="proprietes du bloc PERMITTIVITY",
#                        regles = ( UN_PARMI ('VALUE_REAL','VALUE_COMPLEX'),
#                                 ),
#                
#	         LAW             = SIMP (statut="o",
#		                         typ="TXM",
#				         defaut="LINEAR",
#		                         into = ("LINEAR","NONLINEAR"),
#                                         ang = "type of law",
#				        ),
#                 HOMOGENEOUS     = SIMP (statut="f",
#		                         typ="TXM",
#				         defaut="TRUE",
#		                         into = ("TRUE","FALSE"),
#                                         ang = "the material is homogeneous",
#                                         fr  = "le materiau est homogene",
#				        ),
#	         ISOTROPIC       = SIMP (statut="f",
#		                         typ="TXM",
#				         defaut="TRUE",
#		                         into = ("TRUE","FALSE"),
#                                         ang = "the material is isotropic",
#                                         fr  = "le materiau est isotrope",
#				        ),
#	         VALUE_REAL     = SIMP (statut="f",
#		                        typ="R", 
#                                        ang = "enter a real value",
#                                        fr  = "entrer un reel",
#				       ),
#	         VALUE_COMPLEX  = SIMP (statut="o",
#		                        typ="C", 
#                                        ang = "enter a complex value",
#                                        fr  = "entrer un complexe",
#				       ),
#
#	         ), # fin FACT PERMITTIVITY
#
##------------------------------------------------
## sous bloc niveau 2 : PERMEABILITY
##------------------------------------------------
#  PERMEABILITY = FACT ( statut="o", 
#                        ang ="Permeability properties",
#                        fr  ="proprietes du bloc PERMEABILITY",
#                        regles = ( UN_PARMI ('VALUE_REAL','VALUE_COMPLEX'),
#                                 ),
#                
#	         LAW             = SIMP (statut="o",
#		                         typ="TXM",
#				         defaut="LINEAR",
#		                         into = ("LINEAR","NONLINEAR"),
#                                         ang = "type of law",
#				        ),
#                 HOMOGENEOUS     = SIMP (statut="f",
#		                         typ="TXM",
#				         defaut="TRUE",
#		                         into = ("TRUE","FALSE"),
#                                         ang = "the material is homogeneous",
#                                         fr  = "le materiau est homogene",
#				        ),
#	         ISOTROPIC       = SIMP (statut="f",
#		                         typ="TXM",
#				         defaut="TRUE",
#		                         into = ("TRUE","FALSE"),
#                                         ang = "the material is isotropic",
#                                         fr  = "le materiau est isotrope",
#				        ),
#	         VALUE_REAL     = SIMP (statut="f",
#		                        typ="R", 
#                                        ang = "enter a real value",
#                                        fr  = "entrer un reel",
#				       ),
#	         VALUE_COMPLEX  = SIMP (statut="o",
#		                        typ="C", 
#                                        ang = "enter a complex value",
#                                        fr  = "entrer un complexe",
#				       ),
#
#                 NonLinearCond  = BLOC (condition="LAW=='NONLINEAR'",
#                                  NONLINEAR   = SIMP (statut="o",
#		                                      typ= (law,),
#                                                      ang = "enter a complex value",
#                                                      fr  = "parametres de la law non lineaire",
#      				                     ),
#                                       ), 
#
#	         ), # fin FACT PERMEABILITY
#
#
#	     ) # fin OPER DIELECTRIC
#
#
##------------------------------------
## sous bloc niveau 1 : ZSURFACIC
##------------------------------------
#ZSURFACIC  = OPER (nom = "ZSURFACIC",
#                    op = None,
#	            repetable = 'n',
#                    UIinfo= {"groupes":("Isotropic Homogeneous Materials",)},
#		    ang= "ZSURFACIC block definition", 
#		    fr= "definition du bloc ZSURFACIC", 
#                    sd_prod= materiau,
#		    
##------------------------------------------------
## sous bloc niveau 2 : CONDUCTIVITY
##------------------------------------------------
#  CONDUCTIVITY = FACT ( statut="o", 
#                        ang ="Conductivity properties",
#                        fr  ="proprietes du bloc CONDUCTIVITY",
#                        regles = ( UN_PARMI ('VALUE_REAL','VALUE_COMPLEX'),
#                                 ),
#                
#	         LAW             = SIMP (statut="o",
#		                         typ="TXM",
#				         defaut="LINEAR",
#		                         into = ("LINEAR","NONLINEAR"),
#                                         ang = "type of law",
#                                         fr = "type de law",
#				        ),
#                 HOMOGENEOUS     = SIMP (statut="f",
#		                         typ="TXM",
#				         defaut="TRUE",
#		                         into = ("TRUE","FALSE"),
#                                         ang = "the material is homogeneous",
#                                         fr  = "le materiau est homogene",
#				        ),
#	         ISOTROPIC       = SIMP (statut="f",
#		                         typ="TXM",
#				         defaut="TRUE",
#		                         into = ("TRUE","FALSE"),
#                                         ang = "the material is isotropic",
#                                         fr  = "le materiau est isotrope",
#				        ),
#	         VALUE_REAL     = SIMP (statut="f",
#		                        typ="R", 
#                                        ang = "enter a real value",
#                                        fr  = "entrer un reel",
#				       ),
#	         VALUE_COMPLEX  = SIMP (statut="o",
#		                        typ="C", 
#                                        ang = "enter a complex value",
#                                        fr  = "entrer un complexe",
#				       ),
#		 
#
#	         ), # fin FACT CONDUCTIVITY
#
##------------------------------------------------
## sous bloc niveau 2 : PERMEABILITY
##------------------------------------------------
#  PERMEABILITY = FACT ( statut="o", 
#                        ang ="Permeability properties",
#                        fr  ="proprietes du bloc PERMEABILITY",
#                        regles = ( UN_PARMI ('VALUE_REAL','VALUE_COMPLEX'),
#                                 ),
#                
#	         LAW             = SIMP (statut="o",
#		                         typ="TXM",
#				         defaut="LINEAR",
#		                         into = ("LINEAR","NONLINEAR"),
#                                         ang = "type of law",
#                                         fr = "type de law",
#				        ),
#                 HOMOGENEOUS     = SIMP (statut="f",
#		                         typ="TXM",
#				         defaut="TRUE",
#		                         into = ("TRUE","FALSE"),
#                                         ang = "the material is homogeneous",
#                                         fr  = "le materiau est homogene",
#				        ),
#	         ISOTROPIC       = SIMP (statut="f",
#		                         typ="TXM",
#				         defaut="TRUE",
#		                         into = ("TRUE","FALSE"),
#                                         ang = "the material is isotropic",
#                                         fr  = "le materiau est isotrope",
#				        ),
#	         VALUE_REAL     = SIMP (statut="f",
#		                        typ="R", 
#                                        ang = "enter a real value",
#                                        fr  = "entrer un reel",
#				       ),
#	         VALUE_COMPLEX  = SIMP (statut="o",
#		                        typ="C", 
#                                        ang = "enter a complex value",
#                                        fr  = "entrer un complexe",
#				       ),
#
#	         ), # fin FACT PERMEABILITY
#             
#	     ) # fin OPER ZSURFACIC
#
#
##===================================
## definition d un type de matériau fictif 
##------------------------------------
## sous bloc niveau 1 : NILMAT   
##------------------------------------
#NILMAT     = OPER (nom = "NILMAT",
#                    op = None,
#	            repetable = 'n',
#                    UIinfo= {"groupes":("Fictitious Materials",)},
#		    ang= "NILMAT block definition", 
#		    fr= "definition du bloc NILMAT", 
#                    sd_prod= materiau,
#             
#	     ) # fin OPER NILMAT
#
#
##============================================
## 1 type de matériau isotropique non homogene 
##----------------------------------------
## sous bloc niveau 1 : EM_ISOTROPIC_FILES   
##----------------------------------------
#EM_ISOTROPIC = PROC (nom = "EM_ISOTROPIC",
#                    op = None,
#	            repetable = 'n',
#                    UIinfo= {"groupes":("Isotropic Inhomogeneous Materials",)},
#		    ang= "EM_ISOTROPIC block definition", 
#		    fr= "definition du bloc EM_ISOTROPIC", 
#             
#	       CONDUCTIVITY_File = SIMP (statut="o", 
#	                                 typ=("Fichier",'MED Files (*.med)',),
#	                                 ang="CONDUCTIVITY MED data file name",
#	                                 fr ="nom du fichier MED CONDUCTIVITY",
#	                                ),
#	       PERMEABILITY_File = SIMP (statut="o", 
#	                                 typ=("Fichier",'MED Files (*.med)',),
#	                                 ang="PERMEABILITY MED data file name",
#	                                 fr ="nom du fichier MED PERMEABILITY",
#	                                ),
#					
#	     ) # fin PROC EM_ISOTROPIC
#	     
##============================================
## 1 type de matériau  non isotropique 
##----------------------------------------
## sous bloc niveau 1 : EM_ANISOTROPIC_FILES   
##----------------------------------------
#EM_ANISOTROPIC = PROC (nom = "EM_ANISOTROPIC",
#                    op = None,
#	            repetable = 'n',
#                    UIinfo= {"groupes":("Anisotropic Materials",)},
#		    ang= "EM_ANISOTROPIC block definition", 
#		    fr= "definition du bloc EM_ANISOTROPIC", 
#             
#	       CONDUCTIVITY_File = SIMP (statut="o", 
#	                                 typ=("Fichier",'.mater Files (*.mater)',),
#	                                 ang="CONDUCTIVITY .mater data file name",
#	                                 fr ="nom du fichier .mater CONDUCTIVITY",
#	                                ),
#	       PERMEABILITY_File = SIMP (statut="o", 
#	                                 typ=("Fichier",'.mater Files (*.mater)',),
#	                                 ang="PERMEABILITY .mater data file name",
#	                                 fr ="nom du fichier .mater PERMEABILITY",
#	                                ),
#	      ) # fin PROC EM_ANISOTROPIC
#
#================================
# 3eme bloc : bloc SOURCES
#================================

SOURCES = PROC ( nom = "SOURCES",
                 op = None,
		 repetable = 'n',
                 ang = "sources block definition", 

 STRANDED_INDUCTOR  = FACT (statut="f",
                            fr="stranded inductor source",
		
                      NAME     = SIMP (statut="o",
		                       typ="TXM",
                                       fr="name of the source",
				       ),
                      NTURNS   = SIMP (statut="o",
		                       typ="I",
				       defaut=1,
                                       fr="number of tuns in the inductor",
				       ),
                      CURJ     = SIMP (statut="o",
		                       typ="R",
				       defaut=0,
                                       fr="intensity",
				       ),
		      POLAR    = SIMP (statut="o",
		                       typ="R",
				       defaut=0,
                                       fr="polarization",
				       ),

                      ), # fin FACT 
			    
 EPORT = FACT (statut="f",
               fr="eport source",
		
         NAME     = SIMP (statut="o",
	                  typ="TXM",
                          fr="name of the source",
			  ),
         TYPE     = SIMP (statut="o",
	                  typ="TXM",
			  into=("VOLTAGE","CURRENT"),
                          fr="type of eport source",
			  ),
         AMP      = SIMP (statut="o",
	                  typ="R",
			  defaut=0,
                          fr="amplitude",
			  ),
         POLAR    = SIMP (statut="o",
	                  typ="R",
			  defaut=0,
                          fr="polarization",
			  ),

               ), # fin FACT eport

 HPORT = FACT (statut="f",
               fr="hport source",
         
	 NAME     = SIMP (statut="o",
	                  typ="TXM",
                          fr="name of the source",
			  ),
         TYPE     = SIMP (statut="o",
	                  typ="TXM",
			  into=("VOLTAGE","CURRENT"),
                          fr="type of hport source",
			  ),
         AMP      = SIMP (statut="o",
	                  typ="R",
			  defaut=0,
                          fr="amplitude",
			  ),
         POLAR    = SIMP (statut="o",
	                  typ="R",
			  defaut=0,
                          fr="polarization",
			  ),

               ), # fin FACT hport
		

) # Fin PROC sources

