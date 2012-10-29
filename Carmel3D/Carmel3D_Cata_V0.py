# -*- coding: utf-8 -*-
# --------------------------------------------------
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
# --------------------------------------------------

import os
import sys
from Accas import *
import types
from decimal import Decimal
# repertoire ou sont stockés le catalogue carmel3d 
# et les fichiers de donnees des materiaux de reference
from prefs_CARMEL3D import repIni


#print "catalogue carmel"
#print "repIni = ", repIni

# Version du catalogue
VERSION_CATA = "2.3.1 for harmonic problems"
# --------------------------------------------------
# definition d une classe pour les materiaux
# definition d une classe pour les sources
# definition d une classe pour les groupes de mailles
# --------------------------------------------------
class material ( ASSD ) : pass
class source   ( ASSD ) : pass
class grmaille ( ASSD ) : pass

#CONTEXT.debug = 1
# --------------------------------------------------
# déclaration du jeu de commandes : 1ere instruction du catalogue obligatoire 
#---------------------------------------------------

JdC = JDC_CATA ( code = 'CARMEL3D',
#                execmodul = None,
                  regles =(
                           AU_MOINS_UN ('MATERIAL'),
                           AU_MOINS_UN ('SOURCE'),
                           AU_MOINS_UN ('MESHGROUP'),
                           ),
                 ) # Fin JDC_CATA
##=========================================================
import opsCarmel
INCLUDE = MACRO ( nom = "INCLUDE",
                 op = None,
                 UIinfo = { "groupes" : ( "Gestion du travail", ) },
                 sd_prod = opsCarmel.INCLUDE,
                 op_init = opsCarmel.INCLUDE_context,
                 fichier_ini = 1,
 
   FileName = SIMP ( statut = "o",
                    typ = ('Fichier', 'comm Files (*.comm);;All Files (*)',),
                     fr = u"bibliothèque des matériaux",
                    ang = "material library file",
                     ),
  
 ) # Fin PROC MODEL

# --------------------------------------------------
# definition de groupe de mailles
# il est associe a un  materiau ou a une source
#---------------------------------------------------

MESHGROUP     = OPER (nom = "MESHGROUP",
                    op = None,
                repetable = 'n',
                    UIinfo= {"groupes":("Definition",)},
            fr= u"attribution d'un matériau ou d'une source à un groupe du maillage", 
            ang = "mesh group association to material or source", 
                    sd_prod= grmaille,
                    regles =(
                             EXCLUS ('MATERIAL','SOURCE'),
                           ),

# ----------------------------------------------------------
# le mot cle SIMP doit etre facultatif sinon la recuperation 
# des groupes de mailles sous SALOME ne fonctionne pas car 
# le concept ne peut pas etre nomme car non valide
#-----------------------------------------------------------
              MATERIAL =  SIMP (statut="f",
                         typ=(material,),
                                 ang="name of the linked material",
                         fr =u"nom du matériau associé",
                                ), 
              SOURCE =  SIMP (statut="f",
                         typ=(source,),
                                 ang="name of the linked source",
                         fr =u"nom de la source associée",
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
MATERIAL = OPER (nom = "MATERIAL",
                    op = None,
                repetable = 'n',
            ang= "material block definition", 
            fr= u"définition d'un matériau", 
                    sd_prod= material,

#---------------------------------------------------------------------
# liste des matériaux de reference fournis par THEMIS et  des
# materiaux generiques (les materiaux generiques peuvent etre utilises 
# si aucun materiau de reference  ne convient) 
#---------------------------------------------------------------------
            MAT_REF = SIMP(statut='o',
                           typ='TXM',
                       into=(
#  matériaux génériques 
                                 "DIELECTRIC",
                                 "CONDUCTOR",
                                 "ZINSULATOR","ZSURFACIC",
                                 "NILMAT","EM_ISOTROPIC","EM_ANISOTROPIC",
#  type CONDUCTOR lineaire 
                                 "ACIER_Noir","ACIER_PE","ACIER_CIMBLOT",
                         "ALU","BRONZE","CUIVRE",
                         "FERRITE_Mn_Zn","FERRITE_Ni_Zn",
                                 "INCONEL600",
                                 "POTASSE",
#  type CONDUCTOR non lineaire 
                                 "M6X2ISO1", 
#  type DIELECTRIC 
                                 "AIR","FERRITEB30",
                                 "FEV470","FEV600","FEV800","FEV1000",
                                 "E24","HA600",
                                 "M600_65",
#  type EM_ANISO 
                                 "M6X","M6X_lineaire","M6X_homog", 
                                ),
                           ang = "reference  materials list",
                           fr  = u"liste des matériaux de référence",
                  ),

##############################################################################
# Remarque generale a tous les materiaux : 
# pour conserver l'affichage scientifique le nombre derriere l'exposant doit
# etre strictement superieur au nombre de decimales 
#

##--------------------------------------------------------------------
# materiau generique diélectrique (préfixe NOCOND dans le maillage)
#---------------------------------------------------------------------
  DIELECTRIC_properties = BLOC(condition="MAT_REF=='DIELECTRIC'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
#
#
  PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  =u"propriétés du bloc PERMEABILITY",
                
                     HOMOGENEOUS = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous or not",
                                         fr  = u"le matériau est homogène ou non",
                        ),
                 ISOTROPIC   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic or not",
                                         fr  = u"le matériau est isotrope ou non",
                        ),
                  TYPE_LAW       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="LINEAR_COMPLEX",
                                 into = ("LINEAR_COMPLEX","LINEAR_REAL","NONLINEAR"),
                                         ang = "harmonic or time-domain linear or nonlinear law only for homogeneous and isotropic materials",
                                         fr  = u"loi linéaire (fréquentielle ou temporelle) ou non (homogène et isotrope seulement)",
                        ),
         
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                         VALUE_COMPLEX = SIMP (statut="o",
                                           typ="C", 
                                           defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = u"saisir une valeur complexe relative",
                                          ),
                                 ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                         VALUE_REAL    = SIMP (statut="o",
                                           typ="R", 
                                           defaut=1.0,
                                                   ang = "enter a real relative value",
                                                   fr = u"saisir une valeur réelle relative",
                                           ),
                                 ), # fin bloc
                   NONLINEAR_ISOTROPIC_LAW_PROPERTIES = BLOC (condition="TYPE_LAW=='NONLINEAR' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
                                         ang = "Relative linear permeability value, also used at first nonlinear iteration",
                                         fr = u"Valeur de la perméabilité relative à l'air utilisée pour une loi linéaire ou pour la première itération non-linéaire",
                                ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="MARROCCO",
                                 into = ("SPLINE","MARROCCO","MARROCCO+SATURATION"),
                                         ang = "nature law",
                                         fr  = u"nature de la loi",
                        ),
                      SPLINE_LAW_PROPERTIES = BLOC (condition="NATURE=='SPLINE'",
                FILENAME = SIMP (statut="o", 
                         typ=("Fichier",'All Files (*)',),
                         ang="data file name",
                         fr =u"nom du fichier contenant les mesures expérimentales B(H)",
                         ),
                      ), # Fin BLOC SPLINE_PROPERTIES
                      MARROCCO_LAW_PROPERTIES = BLOC (condition="NATURE in ('MARROCCO','MARROCCO+SATURATION')",
               ALPHA    = SIMP (statut="o", 
                        typ="R",
                        defaut=0,
                        val_min=0,
                        ang="alpha parameter",
                        fr =u"paramètre alpha de la loi de Marrocco" ,
                       ),
               TAU      = SIMP (statut="o", 
                        typ="R",
                        defaut=0,
                        val_min=0,
                        ang="tau parameter",
                        fr =u"paramètre tau de la loi de Marrocco" ,
                        ),
               C        = SIMP (statut="o", 
                        typ="R",
                        defaut=0,
                        val_min=0,
                        ang="c parameter",
                        fr =u"paramètre c de la loi de Marrocco" ,
                        ),
               EPSILON  = SIMP (statut="o", 
                        typ="R",
                        defaut=0,
                        val_min=0,
                        ang="epsilon parameter",
                        fr =u"paramètre epsilon de la loi de Marrocco" ,
                        ),
                      ), # Fin BLOC MARROCCO_LAW_PROPERTIES
                      SATURATION_LAW_PROPERTIES = BLOC (condition="NATURE=='MARROCCO+SATURATION'",
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
                        fr =u"type de raccord entre la loi choisie et la loi de saturation" ,
                        ),
                      ), # Fin BLOC SATURATION_LAW_PROPERTIES
               APPLIEDTO = SIMP (statut="o",    
                         typ="TXM",   
                         into=("B(H)&H(B)","B(H)","H(B)"),
                         defaut="B(H)&H(B)",
                         ang="join applied to",
                         fr =u"Le raccord tel que défini est appliqué à la courbe B(H) seulement, à la courbe H(B) seulement ou aux deux courbes à la fois. Dans les deux premiers cas, le raccord de la courbe H(B) est inversé numériquement à partir du raccord défini pour la courbe B(H), et vice-versa.",
                        ),

                      ), # Fin BLOC NONLINEAR_LAW_PROPERTIES
             ), # fin FACT PERMEABILITY
#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous or not",
                                         fr  = u"le matériau est homogène ou non",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic or not",
                                         fr  = u"le matériau est isotrope ou non",
                        ),

                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="LINEAR_COMPLEX",
                                 into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
                        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                  VALUE_REAL = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
                                ),
                    ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                  VALUE_COMPLEX = SIMP (statut="o",
                                 typ="C", 
                                 defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
                                ),
                    ), # fin bloc complex
         
             ), # fin FACT PERMITTIVITY

   ), # fin BLOC DIELECTRIC


##--------------------------------------------------------------------
# materiau generique conducteur (type COND dans le maillage)
#---------------------------------------------------------------------
  CONDUCTOR_properties = BLOC(condition="MAT_REF=='CONDUCTOR'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
#
#
  PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  =u"propriétés du bloc PERMEABILITY",
                
                     HOMOGENEOUS = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous or not",
                                         fr  = u"le matériau est homogène ou non",
                        ),
                 ISOTROPIC   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic or not",
                                         fr  = u"le matériau est isotrope ou non",
                        ),
                  TYPE_LAW       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="LINEAR_COMPLEX",
                                 into = ("LINEAR_COMPLEX","LINEAR_REAL","NONLINEAR"),
                                         ang = "harmonic or time-domain linear or nonlinear law only for homogeneous and isotropic materials",
                                         fr  = u"loi linéaire (fréquentielle ou temporelle) ou non (homogène et isotrope seulement)",
                        ),
         
                  val_complex    = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                         VALUE_COMPLEX = SIMP (statut="o",
                                           typ="C", 
                                           defaut=('RI',1,0),
                                                   ang = "enter a complex relative value",
                                                   fr = u"saisir une valeur complexe relative",
                                          ),
                                 ), # fin bloc 

                  val_real       = BLOC(condition="TYPE_LAW=='LINEAR_REAL' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                         VALUE_REAL    = SIMP (statut="o",
                                           typ="R", 
                                           defaut=1.0,
                                                   ang = "enter a real relative value",
                                                   fr = u"saisir une valeur réelle relative",
                                           ),
                                 ), # fin bloc
                   NONLINEAR_ISOTROPIC_LAW_PROPERTIES = BLOC (condition="TYPE_LAW=='NONLINEAR' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
                                         ang = "Relative linear permeability value, also used at first nonlinear iteration",
                                         fr = u"Valeur de la perméabilité relative à l'air utilisée pour une loi linéaire ou pour la première itération non-linéaire",
                                ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="MARROCCO",
                                 into = ("SPLINE","MARROCCO","MARROCCO+SATURATION"),
                                         ang = "nature law",
                                         fr  = u"nature de la loi",
                        ),
                      SPLINE_LAW_PROPERTIES = BLOC (condition="NATURE=='SPLINE'",
                FILENAME = SIMP (statut="o", 
                         typ=("Fichier",'All Files (*)',),
                         ang="data file name",
                         fr =u"nom du fichier contenant les mesures expérimentales B(H)",
                         ),
                      ), # Fin BLOC SPLINE_PROPERTIES
                      MARROCCO_LAW_PROPERTIES = BLOC (condition="NATURE in ('MARROCCO','MARROCCO+SATURATION')",
               ALPHA    = SIMP (statut="o", 
                        typ="R",
                        defaut=0,
                        val_min=0,
                        ang="alpha parameter",
                        fr =u"paramètre alpha de la loi de Marrocco" ,
                       ),
               TAU      = SIMP (statut="o", 
                        typ="R",
                        defaut=0,
                        val_min=0,
                        ang="tau parameter",
                        fr =u"paramètre tau de la loi de Marrocco" ,
                        ),
               C        = SIMP (statut="o", 
                        typ="R",
                        defaut=0,
                        val_min=0,
                        ang="c parameter",
                        fr =u"paramètre c de la loi de Marrocco" ,
                        ),
               EPSILON  = SIMP (statut="o", 
                        typ="R",
                        defaut=0,
                        val_min=0,
                        ang="epsilon parameter",
                        fr =u"paramètre epsilon de la loi de Marrocco" ,
                        ),
                      ), # Fin BLOC MARROCCO_LAW_PROPERTIES
                      SATURATION_LAW_PROPERTIES = BLOC (condition="NATURE=='MARROCCO+SATURATION'",
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
                        fr =u"type de raccord entre la loi choisie et la loi de saturation" ,
                        ),
                      ), # Fin BLOC SATURATION_LAW_PROPERTIES
               APPLIEDTO = SIMP (statut="o",    
                         typ="TXM",   
                         into=("B(H)&H(B)","B(H)","H(B)"),
                         defaut="B(H)&H(B)",
                         ang="join applied to",
                         fr =u"Le raccord tel que défini est appliqué à la courbe B(H) seulement, à la courbe H(B) seulement ou aux deux courbes à la fois. Dans les deux premiers cas, le raccord de la courbe H(B) est inversé numériquement à partir du raccord défini pour la courbe B(H), et vice-versa.",
                        ),

                      ), # Fin BLOC NONLINEAR_LAW_PROPERTIES
             ), # fin FACT PERMEABILITY
#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
  CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  ="proprietes du bloc PERMITTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE","FALSE"),
                                         ang = "the material is homogeneous or not",
                                         fr  = u"le matériau est homogène ou non",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE","FALSE"),
                                         ang = "the material is isotropic or not",
                                         fr  = u"le matériau est isotrope ou non",
                        ),

                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="LINEAR_REAL",
                                 into = ("LINEAR_REAL","LINEAR_COMPLEX"),
                                         ang = "linear law",
                                         fr  = "loi lineaire",
                        ),
                 val_real = BLOC(condition="TYPE_LAW=='LINEAR_REAL' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                  VALUE_REAL = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
                                ),
                    ), # fin bloc real

                val_complex = BLOC(condition="TYPE_LAW=='LINEAR_COMPLEX' and HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                  VALUE_COMPLEX = SIMP (statut="o",
                                 typ="C", 
                                 defaut=('RI',1,0),
                                         ang = "enter a complex relative value",
                                         fr = "saisir une valeur complexe relative",
                                ),
                    ), # fin bloc complex
         
             ), # fin FACT CONDUCTIVITY

   ), # fin BLOC CONDUCTOR


###################################################################################################
# ----------------------------------------
# sous bloc niveau 1 : ZSURFACIC
#i----------------------------------------
# materiau generique de type ZSURFASIC 
#-----------------------------------------
  ZSURFACIC_properties = BLOC(condition="MAT_REF=='ZSURFACIC'",

#------------------------------------------------
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
  CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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

   ), # fin bloc ZSURFACIC_properties

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
#-------------------------------------------------
# matériau isotropique non homogene generique
#-------------------------------------------------
   EM_ISOTROPIC_properties=BLOC(condition="MAT_REF=='EM_ISOTROPIC'", 
               
           CONDUCTIVITY_File = SIMP (statut="o", 
                                     typ=("Fichier",'MED Files (*.med)',),
                                     ang="CONDUCTIVITY MED data file name",
                                     fr = u"nom du fichier MED CONDUCTIVITY",
                                    ),
           PERMEABILITY_File = SIMP (statut="o", 
                                     typ=("Fichier",'MED Files (*.med)',),
                                     ang="PERMEABILITY MED data file name",
                                     fr = u"nom du fichier MED PERMEABILITY",
                                    ),
   ), # fin bloc EM_ISOTROPIC_properties

    
#---------------------------------------------------
# matériau  anisotropique non homogene generique 
#---------------------------------------------------
   EM_ANISOTROPIC_properties=BLOC(condition="MAT_REF=='EM_ANISOTROPIC'",
                 
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
   ), # fin bloc EM_ANISOTROPIC_properties


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

                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('3.448E7'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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

                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('1.00000E6'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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

                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('9.7000E5'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('1.0E1'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('1.25E3'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('1.0000E-6'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('1.50000E1'),
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

                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('6.00000E6'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('1.0E2'),
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

                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('1.75000E6'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('7.0E1'),
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

                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('3.00000E6'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('5.00000E1'),
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

                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('5.85E7'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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

                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('7.143E1'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('1.0E0'),
                                                   ang = "enter a real relative value",
                                                   fr = "saisir une valeur reelle relative",
                                           ),
                                 ), # fin bloc
     
             ), # fin FACT PERMEABILITY

             ), # fin BLOC conductor10

#----------------------------------------------------------------
# materiau de reference de type CONDUCTOR non lineaire : M6X2ISO1
#----------------------------------------------------------------
  M6X2ISO1_properties = BLOC(condition="MAT_REF=='M6X2ISO1'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
                        ),
                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="NONLINEAR",
                                 into = ("NONLINEAR"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
                        ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="SPLINE",
                                 into = ("SPLINE"),
                                         ang = "nature law",
                                         fr  = "nature de la loi",
                        ),
                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
                                         ang = "enter a real relative value",
                                         fr = "saisir une valeur reelle relative",
                                ),

                      FILENAME = SIMP (statut="o", 
                                   typ=("Fichier",'All Files (*)',),
                               defaut=str(repIni)+"/M6X2ISO1",
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
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
  CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Conductivity properties",
                        fr  ="proprietes du bloc CONDUCTIVITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                 defaut=Decimal('1.724E6'),
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
         
             ), # fin FACT CONDUCTIVITY
 ), # fin BLOC 


##-----------------------------------------------------
# materiau de reference de type DIELECTRIC lineaire : AIR  
#------------------------------------------------------
  AIR_properties = BLOC(condition="MAT_REF=='AIR'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------

     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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

            ), # fin BLOC DIELECTRIC
#
##-------------------------------------------------------------
# materiau de reference de type DIELECTRIC lineaire : FERRITE B30  
#--------------------------------------------------------------
  FERRITEB30_properties = BLOC(condition="MAT_REF=='FERRITEB30'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------

     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                           defaut=Decimal('1.10E3'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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

            ), # fin BLOC DIELECTRIC
#--------------------------------------------------------
# materiau de reference de type DIELECTRIC non lineaire : E24  
#--------------------------------------------------------
  E24_properties = BLOC(condition="MAT_REF=='E24'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
                        ),
                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="NONLINEAR",
                                 into = ("NONLINEAR"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
                        ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="SPLINE",
                                 into = ("SPLINE"),
                                         ang = "nature law",
                                         fr  = "nature de la loi",
                        ),
                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                 defaut=Decimal('1.0E0'),
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
# materiau de reference de type DIELECTRIC  non lineaire : FEV470 
#-------------------------------------------------------------
  FEV470_properties = BLOC(condition="MAT_REF=='FEV470'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
                        ),
                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="NONLINEAR",
                                 into = ("NONLINEAR"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
                        ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="SPLINE",
                                 into = ("SPLINE"),
                                         ang = "nature law",
                                         fr  = "nature de la loi",
                        ),

                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                 defaut=Decimal('1.0E0'),
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
# materiau de reference de type DIELECTRIC : FEV600 
#----------------------------------------------------------
  FEV600_properties = BLOC(condition="MAT_REF=='FEV600'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
                        ),

                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="NONLINEAR",
                                 into = ("NONLINEAR"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
                        ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="SPLINE",
                                 into = ("SPLINE"),
                                         ang = "nature law",
                                         fr  = "nature de la loi",
                        ),
                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                 defaut=Decimal('1.0E0'),
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
# materiau de reference de type DIELECTRIC : FEV800 
#----------------------------------------------------------
  FEV800_properties = BLOC(condition="MAT_REF=='FEV800'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
                        ),
                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="NONLINEAR",
                                 into = ("NONLINEAR"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
                        ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="SPLINE",
                                 into = ("SPLINE"),
                                         ang = "nature law",
                                         fr  = "nature de la loi",
                        ),

                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                 defaut=Decimal('1.0E0'),
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
# materiau de reference de type DIELECTRIC : FEV1000 
#------------------------------------------------
  FEV1000_properties = BLOC(condition="MAT_REF=='FEV1000'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
                        ),
                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="NONLINEAR",
                                 into = ("NONLINEAR"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
                        ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="SPLINE",
                                 into = ("SPLINE"),
                                         ang = "nature law",
                                         fr  = "nature de la loi",
                        ),

                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                 defaut=Decimal('1.0E0'),
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
# materiau de reference de type DIELECTRIC : HA600 
#-----------------------------------------------------------
  HA600_properties = BLOC(condition="MAT_REF=='HA600'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
                        ),
                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="NONLINEAR",
                                 into = ("NONLINEAR"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
                        ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="SPLINE",
                                 into = ("SPLINE"),
                                         ang = "nature law",
                                         fr  = "nature de la loi",
                        ),

                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                 defaut=Decimal('1.0E0'),
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
# materiau de reference de type DIELECTRIC : M600_65 
#------------------------------------------------
  M600_65_properties = BLOC(condition="MAT_REF=='M600_65'",

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
     PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  ="proprietes du bloc PERMEABILITY",
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is isotropic",
                                         fr  = "le materiau est isotrope",
                        ),
                      TYPE_LAW   = SIMP (statut="o",
                                 typ="TXM",
                         defaut="NONLINEAR",
                                 into = ("NONLINEAR"),
                                         ang = "non linear law",
                                         fr  = "loi non lineaire",
                        ),
                      NATURE     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="SPLINE",
                                 into = ("SPLINE"),
                                         ang = "nature law",
                                         fr  = "nature de la loi",
                        ),

                  VALUE      = SIMP (statut="o",
                                 typ="R", 
                                 defaut=Decimal('1.0E0'),
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
                
                 HOMOGENEOUS     = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
                                         ang = "the material is homogeneous",
                                         fr  = "le materiau est homogene",
                        ),
             ISOTROPIC       = SIMP (statut="o",
                                 typ="TXM",
                         defaut="TRUE",
                                 into = ("TRUE"),
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
                                 defaut=Decimal('1.0E0'),
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
          ), # fin bloc M6X_homog_properties

    ) # fin OPER Materials
    
#===================================================================
# 3eme bloc : bloc SOURCES
#====================================================================
# definition des differentes sources qui seront dans le bloc SOURCES
#-------------------------------------------------------------------
#

SOURCE = OPER ( nom = "SOURCE",
                 op = None,
         repetable = 'n',
                 ang = "source definition", 
                 fr = u"définition d'une source", 
                 sd_prod= source,

         TYPE_SOURCE = SIMP (statut="o",
                         typ="TXM",
                 into=("STRANDED_INDUCTOR","HPORT","EPORT"),
                             fr=u"type de source",
                             ang="type of source",
              ),


#----------------------------------------------------------
# sous bloc niveau 1 : stranded inductor source 
##---------------------------------------------------------
  st_ind_properties = BLOC(condition="TYPE_SOURCE=='STRANDED_INDUCTOR'",
        
         NTURNS   = SIMP (statut="o",
                      typ="I",
               defaut=1,
                          ang="number of turns in the inductor",
                          fr="nombre de tours dans l inducteur",
               ),
     CURJ     = SIMP (statut="o",
                      typ="C", 
                      defaut=('MP',1,0),
                          ang = "enter the current value (magnitude and polarization in degrees) as a complex number",
                          fr = u"saisir la valeur du courant (amplitude et phase en degrés) sous la forme d'un nombre complexe",
                      ),
  ), # fin bloc stranded inductor
                
#----------------------------------------------------------
# sous bloc niveau 1 : eport source 
#----------------------------------------------------------
  eport_properties = BLOC(condition="TYPE_SOURCE=='EPORT'",
        
         TYPE     = SIMP (statut="o",
                      typ="TXM",
              into=("VOLTAGE","CURRENT"),
                          fr="type de eport source",
                          ang="type of eport source",
              ),
     AMP      = SIMP (statut="o",
                      typ="C", 
                      defaut=('MP',1,0),
                          ang = "enter the amplitude value (magnitude and polarization in degrees) as a complex number",
                          fr = u"saisir la valeur de l'amplitude (amplitude et phase en degrés) sous la forme d'un nombre complexe",
                      ),

  ), # fin bloc eport

#----------------------------------------------------------
# sous bloc niveau 1 : hport source 
#----------------------------------------------------------
  hport_properties = BLOC(condition="TYPE_SOURCE=='HPORT'",
         TYPE     = SIMP (statut="o",
                      typ="TXM",
              into=("VOLTAGE","CURRENT"),
                          fr="type de hport source",
                          ang="type of hport source",
              ),
     AMP      = SIMP (statut="o",
                      typ="C", 
                      defaut=('MP',1,0),
                          ang = "enter the amplitude value (magnitude and polarization in degrees) as a complex number",
                          fr = u"saisir la valeur de l'amplitude (amplitude et phase en degrés) sous la forme d'un nombre complexe",
                      ),
  ), # fin bloc hport
) # Fin OPER SOURCE

