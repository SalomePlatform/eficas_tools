# -*- coding: utf-8 -*-
# --------------------------------------------------
# Copyright (C) 2007-2013   EDF R&D
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
VERSION_CATA = "code_Carmel 1.13.0 for time-dependant problems"
# --------------------------------------------------
# definition d une classe pour les materiaux
# definition d une classe pour les sources
# definition d une classe pour les groupes de mailles
# --------------------------------------------------
class material ( ASSD ) : pass
class source   ( ASSD ) : pass
class grmaille ( ASSD ) : pass
class stranded_inductor_geometry ( ASSD ) : pass
class macro_groupe ( ASSD ) : pass 
class mouvement ( ASSD ) : pass


#CONTEXT.debug = 1
# --------------------------------------------------
# déclaration du jeu de commandes : 1ere instruction du catalogue obligatoire 
#---------------------------------------------------

##=========================================================
JdC = JDC_CATA ( code = 'CARMEL3D',
                execmodul = None,
                 regles =(
                           AU_MOINS_UN ('MATERIAL','INCLUDE'),
                           AU_MOINS_UN ('SOURCE','INCLUDE'),
                           AU_MOINS_UN ('MESHGROUP'),
                           AU_MOINS_UN ('POST_TRAITEMENT'),
                           #ENSEMBLE ('POST_COMMANDS','POSTPROCESS_DATA'),
                           AU_MOINS_UN ('PARAMETERS'),
                           AU_MOINS_UN ('SOLVEUR'),
                           ),
                 ) # Fin JDC_CATA
##=========================================================
# création d'une macro pour traiter les INCLUDE
#
#----------------------------------------------------------

import opsCarmel
INCLUDE = MACRO ( nom = "INCLUDE",
                 op = None,
                 UIinfo = { "groupes" : ( "3) Bibliotheque", ) },
                 sd_prod = opsCarmel.INCLUDE,
                 op_init = opsCarmel.INCLUDE_context,
                 fichier_ini = 1,
 
   FileName = SIMP ( statut = "o",
                    typ = ('Fichier', 'comm Files (*.comm);;All Files (*)',),
                     fr = u"Emplacement du fichier (chemin absolu ou relatif) contenant la bibliothèque des matériaux, etc.",
                    ang = "material library file (full or relative path)",
                     ),
  
 ) # Fin MACRO 
# --------------------------------------------------
# definition de groupe de mailles
# il est associe a un  materiau ou a une source
#---------------------------------------------------

MACRO_GROUPE = OPER (nom="MACRO_GROUPE", 
                    op=None, 
                    repetable='n', 
                    sd_prod=macro_groupe, 
                    UIinfo = { "groupes" : ( "Definition", ) },  
                    fr=u"Macro-groupe = liste de groupes de maillage, e.g., inducteur bobiné en morceaux.", 
                    ang=u"Macro-groupe = liste of mesh groups, e.g., stranded inductor defined as several parts.", 
                    regles =(
                             AU_MOINS_UN ('LISTE_MESHGROUP'),
                             AU_MOINS_UN ('MATERIAL',  'SOURCE',  'STRANDED_INDUCTOR_GEOMETRY',  'CONDITION_LIMITE'),
                           ),

                MATERIAL =  SIMP (statut="f",
                                            typ=(material,),
                                            ang="name of the linked real or imaginary material",
                                            fr =u"nom du matériau réel ou imaginaire associé",
                                    ), 
                SOURCE =  SIMP (statut="f",
                                        typ=(source,),
                                        ang="name of the linked source",
                                        fr =u"nom de la source associée",
                                    ), 
                STRANDED_INDUCTOR_GEOMETRY =  SIMP (statut="f",
                                        typ=(stranded_inductor_geometry,),
                                        ang="name of the linked stranded inductor geometry",
                                        fr =u"nom de la géométrie d'inducteur bobiné associée",
                                    ), 
                CONDITION_LIMITE = SIMP (statut="f", 
                                         typ="TXM", 
                                         into=("B.n=0", "H.t=0", "E.t=0", "Jind.n=0","K.t=0"),
                                         ), 
                LISTE_MESHGROUP=SIMP(statut='f' # facultatif pour l'acquisition automatique des groupes du maillage 
                                            ,typ=(grmaille,),
                                            min=1,max=100, 
                                            fr=u"Liste des groupes de maillage associés"),
                                            
) # Fin OPER MACRO GROUPE


STRANDED_INDUCTOR_GEOMETRY=OPER(nom="STRANDED_INDUCTOR_GEOMETRY",
            op=None,
            repetable = 'n',
            sd_prod=stranded_inductor_geometry,
            UIinfo = { "groupes" : ( "Definition", ) },
            
            Direction=SIMP(statut='o',typ='R',min=3,max=3),
            Section=SIMP(statut='o', typ='R',),
            Forme=SIMP(statut='o', typ="TXM", into=("Droit", "Circulaire"), ), 
            Propriete= BLOC (condition="Forme=='Circulaire'",
            Centre=SIMP(statut='o',typ='R',min=3,max=3),
                    ),  
                    
)#Fin OPER STRANDED INDUCTOR GEOMETRY

SYMETRIE = PROC (nom="SYMETRIE",
                  op = None, 
                  repetable = 'n',
                  UIinfo= {"groupes":("Definition",)},                 
                 Type= SIMP (statut="o", 
                             typ="TXM", 
                             into=("aucune", "periodicite", "periodicite+Ksymetrique","antiperiodicite", "libre"), 
                             ), 
                 
                 Face1 = SIMP (statut="o", 
                                        fr="groupe de noeuds attendu" , 
                                        typ=(grmaille, ), 
                                        ), 
                 Face2 = SIMP (statut="o", 
                                        fr="groupe de noeuds attendu" , 
                                        typ=(grmaille, ), 
                                        ), 
                Mouvement_associe = SIMP (statut="f",
                                          typ=(mouvement, ), 
                                          ),     
                Groupe_Points = SIMP (statut="o", 
                                          typ=(grmaille, ), 
                                          ), 
                                                
)#Fin PROC SYMETRIE

MOUVEMENT = OPER (nom="MOUVEMENT", 
                  op = None, 
                  sd_prod=mouvement, 
                  repetable = 'n',
                  UIinfo= {"groupes":("Definition",)},
                    Milieu_glissement= SIMP (statut='o', 
                                             typ=(grmaille, ), 
                                             ), 
                     Surface_glissement = SIMP (statut='o', 
                                             typ=(grmaille, ), 
                                             ), 
                     Delta_maillage = SIMP (statut='o', 
                                            typ='R', 
                                            defaut=1), 
                     Nombre_pas_permutation = SIMP ( statut="o", 
                                                   typ="I"), 
                     Axe_rotation = SIMP ( statut="o", typ="TXM", into=('Ox', 'Oy', 'Oz'),  defaut='Oz'), 
                            )

              
SOLVEUR = PROC ( nom ="SOLVEUR",
          op=None,
          repetable = 'n',
          UIinfo= {"groupes":("1) Parametres",)},
          ang= "Solver parameters for this study", 
          fr= u"Paramètres liés au solveur de l'étude", 
          
          Type= SIMP (statut="o",
                              typ="TXM",
                              into=("Solveur_lineaire","Solveur_non_lineaire" ),  
                            ), 
                            
                Solveur_lineaire=BLOC(condition="Type in('Solveur_lineaire','Solveur_non_lineaire')", 
                            Methode_lineaire=SIMP(statut='o', typ='TXM', into=("Methode iterative BICGCR", "Methode directe MUMPS"), ), 
                            
                    Parametres_methode_iterative_BICGCR = BLOC (condition="Methode_lineaire=='Methode iterative BICGCR'", 
#                              Nom=SIMP(statut='o', typ='TXM', into=("BICGCR"), defaut="BICGCR"), 
                              Precision=SIMP(statut='o', typ='R', defaut=1e-9),
                              Nombre_iterations_max=SIMP(statut='o', typ='I',defaut=10000 ),  
                              Preconditionneur=SIMP(statut='o', typ='TXM',  into=("Crout", "Jacobi", "MUMPS"),defaut="Crout"), 
                              ), 

                    Parametres_methode_direct_MUMPS=BLOC(condition="Methode_lineaire=='Methode directe MUMPS'",
#                              Name=SIMP(statut='o', typ='TXM', into=("MUMPS"),  defaut="MUMPS"),
                              MUMPS_renumeroteur=SIMP(statut='o', typ='TXM', into=("METIS", "AUTO"), defaut="METIS"),
                              MUMPS_memoire=SIMP(statut='o', typ='TXM', into=("AUTO","IC"), defaut="AUTO"),
                              MUMPS_pivot=SIMP(statut='o', typ='R', defaut=20.0),
                              MUMPS_pretraitement=SIMP(statut='o', typ='TXM', into=("AUTO", "OFF"), defaut="AUTO"),
                              MUMPS_post_traitement=SIMP(statut='o', typ='TXM', into=("AUTO", "OFF"), defaut="AUTO"), 
                              MUMPS_valeur_max_de_la_borne_erreur=SIMP(statut='o', typ='R', defaut=-1.0e-3),
                              MUMPS_autocorrection=SIMP(statut='o', typ='TXM', into=(".true.", ".false."), defaut=".true."),
                              MUMPS_coefficient_relaxation=SIMP(statut='o', typ='R',  defaut=1e-6),   
                              ), 
                        ), 
                              
          Solveur_non_lineaire = BLOC (condition="Type=='Solveur_non_lineaire'", 
                      Methode_non_lineaire=SIMP(statut='o', typ="TXM", into=("Methode de Newton","Methode de substitution"), ),           
                      PrecisionNonLineaire = SIMP(statut='o', typ='R', defaut=1e-9),
                      Coefficient_de_Relaxation=SIMP(statut='o', typ="R", defaut=1.0),
                        ), 
               
)#Fin PROC SOLVEUR

MESHGROUP  = OPER (nom = "MESHGROUP",
                op = None,
                repetable = 'n',
                UIinfo= {"groupes":("Definition",)},
                fr= u"attribution d'un matériau ou d'une source à un groupe du maillage", 
                ang = "mesh group association to material or source", 
                sd_prod= grmaille,
                regles =(
                         #EXCLUS ('MATERIAL','SOURCE'),
                           ),

# ----------------------------------------------------------
# le mot cle SIMP doit etre facultatif sinon la recuperation 
# des groupes de mailles sous SALOME ne fonctionne pas car 
# le concept ne peut pas etre nomme car non valide
#-----------------------------------------------------------
              MATERIAL =  SIMP (statut="f",
                        typ=(material),
                        ang="name of the linked real or imaginary material",
                        fr =u"nom du matériau réel ou imaginaire associé",
                                ), 
              SOURCE =  SIMP (statut="f",
                        typ=(source,),
                        ang="name of the linked source",
                        fr =u"nom de la source associée",
                                ), 
                CONDITION_LIMITE = SIMP (statut="f", 
                                         typ="TXM", 
                                         into=("B.n=0", "H.t=0", "E.t=0", "Jind.n=0","K.t=0"),
                                         fr=u"Association d'une condition aux limites à ce groupe de noeuds", 
                                         ang="Setting a boundary condition to this nodal meshgroup", 
                                         ), 
               STRANDED_INDUCTOR_GEOMETRY = SIMP ( statut="f", 
                       typ=(stranded_inductor_geometry), 
                                         fr=u"Association d'une géométrie d'inducteur bobiné, déjà définie, à ce groupe de volumes", 
                                         ang=u"Setting an already defined stranded inductor geometry to this 3D element meshgroup", 
                                                   ), 
                Potentiel_Flottant = SIMP (statut="f", 
                                         typ="TXM", 
                                         defaut='oui', 
                                         into=("oui"),
                                         fr=u"Définition d'un potentiel flottant sur ce groupe de noeuds", 
                                         ), 
                Spire_Exploratrice = SIMP (statut="f", 
                                         typ="TXM", 
                                         defaut='oui', 
                                         into=("oui"),
                                         fr=u"Définition d'une spire exploratrice associée à ce groupe de noeuds", 
                                         ), 
)#Fin OPER MESHGROUP

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

PARAMETERS= PROC ( nom = "PARAMETERS",
    op = None,
    repetable = 'n',
    UIinfo = { "groupes" : ( "1) Parametres", ) },
    ang= "General parameters for this study", 
    fr= u"Paramètres généraux de l'étude", 
#----------------------
# Liste des parametres
#----------------------                
    Identification_du_Modele = SIMP (statut="o", typ='TXM',  defaut='Simulation code_Carmel', # phrase d'identification du modèle
                                             ang="Model identity title.",
                                             fr =u"Phrase permettant d'identifier le modèle traité.",
                                           ),

    RepCarmel=SIMP(typ='Repertoire', statut='o', 
                                ang= "code_Carmel's carmel executable directory",
                                fr= u"Répertoire contenant le programme carmel de code_Carmel",
                                ), 
    Fichier_maillage = SIMP (statut="o", typ=("FichierNoAbs",'All Files (*)',), # l'existence du fichier n'est pas vérifiée
                                             ang="Mesh file path (relative, aka file name, or absolute path).",
                                             fr =u"Emplacement du fichier contenant le maillage (relatif, i.e., nom du fichier, ou absolu, i.e., chemin complet).",
                                           ),
    
    Echelle_du_maillage = SIMP (statut='o',  typ="TXM",  defaut= "Millimetre",  into = ("Metre", "Millimetre"), 
                                                 ang="Mesh geometry units.",
                                                 fr =u"Unités géométriques du maillage.",
                                                ), 

    Formulation=SIMP(statut='o',
                        typ='TXM',
                        into=("(T-)Omega seulement","A(-Phi) seulement", "(T-)Omega puis A(-Phi)", "A(-Phi) puis (T-)Omega")),
                                
    Jauge = SIMP (statut='o', typ="TXM",defaut="non", into = ("oui","non"), ), 
    kEpsilonDistance=SIMP(statut='o', typ='R', defaut=5e-4), 
    kdistanceRef=SIMP(statut='o', typ='R', defaut=5e-1), 
    Nb_pas_de_temps=SIMP(statut='o', typ='I', defaut=1), 
    Pas_de_temps=SIMP(statut='o', typ='R', defaut=1),  
    Resoudre_probleme = SIMP (statut='o',  typ="TXM", defaut="oui", into=("oui", "non"), ), 
    Realiser_post_traitement_aposteriori = SIMP (statut='o',  typ="TXM", defaut="oui", into=("oui", "non"), ),

) # Fin PROC PARAMETERS

POST_TRAITEMENT = PROC (nom = "POST_TRAITEMENT", 
                        op = None, 
                        repetable = 'n', 
                                                UIinfo = { "groupes" : ( "1) Parametres", ) },
                                                ang= "post-processing choices", 
                                                fr= u"choix possibles concernant le post-traitement", 
                        
    Cartes_des_champs = SIMP (statut='o', 
                              typ='R', min=1, max=10, 
                              fr=u"Liste des indices des pas de temps pour la sauvegarde des cartes champs", 
                              ), 
    Cartes_des_courants_induits = SIMP (statut='o', 
                              typ='R', min=1, max=10, 
                              fr=u"Liste des indices des pas de temps pour la sauvegarde des cartes courants induits", 
                              ), 
    Cartes_des_forces = SIMP (statut='o', 
                              typ='R', min=1, max=10, 
                              fr=u"Liste des indices des pas de temps pour la sauvegarde des cartes forces", 
                              ), 
    Pertes_Joules = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création du fichier de sortie des pertes par courant induit", 
                              ), 
    Flux_par_inducteur = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sorties des flux par inducteur", 
                              ), 
    Courants_par_inducteur = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sortie des courants par inducteur", 
                              ),                               
    Tensions_par_inducteur = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sortie des tensions par inducteur", 
                              ), 
    Energie = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création du fichier de sortie de l'énergie", 
                              ),   
    Forces_et_couple = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création du fichier de sortie des forces et du couple", 
                              ), 
    Flux_par_spire = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sortie des flux par spire", 
                              ),   
    Flux_par_groupe = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sortie des flux par groupe", 
                              ),   
    Tensions_electriques = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sortie des tensions électriques", 
                              ),   
    DDP_magnetiques = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sortie des DDP magnétique", 
                              ),   
    Flux_magnetiques = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sortie des flux magnétiques", 
                              ),   
    Flux_J_induit = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sortie des flux de J induit", 
                              ),   
    Potentiel_Flottant = SIMP (statut="o",typ='TXM',into=("oui", "non"), defaut="non", 
                              fr=u"Création des fichiers de sortie des potentiels flottants", 
                              ),   
)#Fin PROC POST TRAITEMENT
                              
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
                 UIinfo = { "groupes" : ( "2) Proprietes", ) },
                 ang= "real material block definition", 
                 fr= u"définition d'un matériau réel", 
                 sd_prod= material,

#---------------------------------------------------------------------
# liste des matériaux de reference fournis par THEMIS et  des
# materiaux generiques (les materiaux generiques peuvent etre utilises 
# si aucun materiau de reference  ne convient) 
#---------------------------------------------------------------------
                 TYPE = SIMP(statut='o',
                             typ='TXM',
                             into=(
#  matériaux génériques 
                                 "DIELECTRIC",
                                 "CONDUCTOR",
                                  "ZINSULATOR","ZSURFACIC",
                                 "NILMAT","EM_ISOTROPIC","EM_ANISOTROPIC",
                             ),
                             ang = "generic materials list",
                             fr  = u"liste des matériaux génériques",
                            ),

##############################################################################
# Remarque generale a tous les materiaux : 
# pour conserver l'affichage scientifique le nombre derriere l'exposant doit
# etre strictement superieur au nombre de decimales 
#

##----------------------------------------------------------------------------------------------
# Données de perméabilité, utilisée pour les diélectriques, conducteurs et impédances de surface
#-----------------------------------------------------------------------------------------------

#------------------------------------------------
# sous bloc niveau 2 : PERMEABILITY
#------------------------------------------------
#
 PERMEABILITY_properties = BLOC (condition="TYPE=='DIELECTRIC' or TYPE=='CONDUCTOR'", 
  PERMEABILITY = FACT ( statut="o", 
                        ang ="Permeability properties",
                        fr  =u"propriétés de perméabilité du matériau",
                        HOMOGENEOUS = SIMP (statut="o",
                                            typ="TXM",
                                            defaut="TRUE",
                                            into = ("TRUE","FALSE"),
                                            ang = "the material is homogeneous or not",
                                            fr  = u"le matériau est homogène ou non",
                                           ),
                        ISOTROPIC = SIMP (statut="o",
                                          typ="TXM",
                                          defaut="TRUE",
                                          into = ("TRUE","FALSE"),
                                          ang = "the material is isotropic or not",
                                          fr  = u"le matériau est isotrope ou non",
                                         ),
                   HOMOGENEOUS_ISOTROPIC_PROPERTIES = BLOC (condition="HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                        LAW = SIMP (statut="o",
                                    typ="TXM",
                                    defaut="LINEAR",
                                    into = ("LINEAR","NONLINEAR"),
                                    ang = "harmonic or time-domain linear or nonlinear law only for homogeneous and isotropic materials",
                                    fr  = u"loi linéaire (fréquentielle ou temporelle) ou non (homogène et isotrope seulement)",
                                   ), 
                        VALUE = SIMP (statut="o",
                                      typ="C", 
                                      defaut=1,
                                      ang = "Relative linear permeability value, also used at first nonlinear iteration",
                                      fr = u"Valeur de la perméabilité relative à l'air utilisée pour une loi linéaire ou pour la première itération non-linéaire",
                                     ),

                    NONLINEAR_LAW_PROPERTIES = BLOC (condition="LAW=='NONLINEAR'",
                        NATURE = SIMP (statut="o",
                                       typ="TXM",
                                       defaut="MARROCCO",
                                       into = ("SPLINE","MARROCCO","MARROCCO+SATURATION"),
                                       ang = "nature law",
                                       fr  = u"nature de la loi",
                                      ),
                     SPLINE_LAW_PROPERTIES = BLOC (condition="NATURE=='SPLINE'",
                        FILENAME = SIMP (statut="o", 
                                         typ=("FichierNoAbs",'All Files (*)',), # l'existence du fichier n'est pas vérifiée
                                         ang="data file name",
                                         fr =u"nom du fichier contenant les mesures expérimentales B(H)",
                                        ),
                     ), # Fin BLOC SPLINE_PROPERTIES
                     MARROCCO_LAW_PROPERTIES = BLOC (condition="NATURE in ('MARROCCO','MARROCCO+SATURATION')",
                        ALPHA = SIMP (statut="o", 
                                      typ="R",
                                      defaut=0,
                                      val_min=0,
                                      ang="alpha parameter",
                                      fr =u"paramètre alpha de la loi de Marrocco" ,
                                     ),
                        TAU = SIMP (statut="o", 
                                    typ="R",
                                    defaut=0,
                                    val_min=0,
                                    ang="tau parameter",
                                    fr =u"paramètre tau de la loi de Marrocco" ,
                                   ),
                        C = SIMP (statut="o", 
                                  typ="R",
                                  defaut=0,
                                  val_min=0,
                                  ang="c parameter",
                                  fr =u"paramètre c de la loi de Marrocco" ,
                                 ),
                        EPSILON = SIMP (statut="o", 
                                        typ="R",
                                        defaut=0,
                                        val_min=0,
                                        ang="epsilon parameter",
                                        fr =u"paramètre epsilon de la loi de Marrocco" ,
                                       ),
                     ), # Fin BLOC MARROCCO_LAW_PROPERTIES
                     SATURATION_LAW_PROPERTIES = BLOC (condition="NATURE=='MARROCCO+SATURATION'",
                        BMAX = SIMP (statut="o", 
                                     typ="R",
                                     defaut=0,
                                     val_min=0,
                                     ang="intersection B",
                                     fr = u"valeur de B marquant la fin de la loi de Marrocco et le début du raccord à la loi de saturation",
                                    ),
                        HSAT = SIMP (statut="o", 
                                     typ="R",
                                     defaut=0,
                                     val_min=0,
                                     ang="H value",
                                     fr = u"valeur de H définissant la loi de saturation",
                                    ),
                        BSAT = SIMP (statut="o", 
                                     typ="R",
                                     defaut=0,
                                     val_min=0,
                                     ang="B value",
                                     fr = u"valeur de B définissant la loi de saturation",
                                    ),
                        JOIN = SIMP (statut="o", 
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
                   ), # Fin BLOC HOMOGENEOUS_ISOTROPIC_PROPERTIES
             ), 
    ),# fin FACT PERMEABILITY


###----------------------------------------------------------------------------------------------
# Données de conductivité, utilisée pour les conducteurs et impédances de surface
# sous bloc niveau 2 : CONDUCTIVITY
#------------------------------------------------
  
 CONDUCTIVITY_properties= BLOC (condition="TYPE=='CONDUCTOR'", 
  CONDUCTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  = u"propriétés de permittivité du matériau",
                        HOMOGENEOUS = SIMP (statut="o",
                                            typ="TXM",
                                            defaut="TRUE",
                                            into = ("TRUE","FALSE"),
                                            ang = "the material is homogeneous or not",
                                            fr  = u"le matériau est homogène ou non",
                                           ),
                        ISOTROPIC = SIMP (statut="o",
                                          typ="TXM",
                                          defaut="TRUE",
                                          into = ("TRUE","FALSE"),
                                          ang = "the material is isotropic or not",
                                          fr  = u"le matériau est isotrope ou non",
                                         ),
                       HOMOGENEOUS_ISOTROPIC_PROPERTIES = BLOC (condition="HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                        LAW = SIMP (statut="o",
                                    typ="TXM",
                                    defaut="LINEAR",
                                    into = ("LINEAR",),
                                    ang = "linear law",
                                    fr  = u"loi linéaire",
                                   ),
                        VALUE = SIMP (statut="o",
                                      typ="C", 
                                      defaut=1, 
                                      ang = "enter a complex relative value",
                                      fr = u"saisir une valeur complexe relative",
                                     ),
                       ), # Fin BLOC HOMOGENEOUS_ISOTROPIC_PROPERTIES
                      ), 

             ), 

            
        # fin FACT CONDUCTIVITY

   

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
    EM_ISOTROPIC_properties=BLOC(condition="TYPE=='EM_ISOTROPIC'", 
               
                 regles =(
                           AU_MOINS_UN ('CONDUCTIVITY_File','PERMEABILITY_File'),
                           ),
           CONDUCTIVITY_File = SIMP (statut="f", 
                                     typ=("FichierNoAbs",'MED Files (*.med)',),
                                     ang="CONDUCTIVITY MED data file name",
                                     fr = u"nom du fichier MED CONDUCTIVITY",
                                    ),
           PERMEABILITY_File = SIMP (statut="f", 
                                     typ=("FichierNoAbs",'MED Files (*.med)',),
                                     ang="PERMEABILITY MED data file name",
                                     fr = u"nom du fichier MED PERMEABILITY",
                                    ),
   ), # fin bloc EM_ISOTROPIC_properties

    
#---------------------------------------------------
# matériau  anisotropique non homogene generique 
#---------------------------------------------------
   EM_ANISOTROPIC_properties=BLOC(condition="TYPE=='EM_ANISOTROPIC'",
                 
                 regles =(
                           AU_MOINS_UN ('CONDUCTIVITY_File','PERMEABILITY_File'),
                           ),                 
           PERMEABILITY_File = SIMP (statut="f", 
                                     #typ=("Fichier",'.mater Files (*.mater)'), # le fichier doit exister dans le répertoire d'où on lancer Eficas si le fichier est défini par un nom relatif, ce qui est trop contraignant
                                     #typ=("Fichier",'.mater Files (*.mater)','Sauvegarde'), # Le fichier peut ne pas exister, mais on propose de le sauvegarder et d'écraser un fichier existant : pas approprié
                                     typ=("FichierNoAbs",'.mater Files (*.mater)'), # l'existence du fichier n'est pas vérifiée, mais on peut le sélectionner quand même via la navigateur. C'est suffisant et permet une bibliothèque de matériaux.
                                     ang="PERMEABILITY .mater data file name",
                                     fr ="nom du fichier .mater PERMEABILITY",
                                    ),
           CONDUCTIVITY_File = SIMP (statut="f", 
                                     typ=("FichierNoAbs",'.mater Files (*.mater)'),
                                     ang="CONDUCTIVITY .mater data file name",
                                     fr ="nom du fichier .mater CONDUCTIVITY",
                                    ),
   ), # fin bloc EM_ANISOTROPIC_properties


#------------------------------------------------------------------
# Données de permittivité, utilisée pour les diélectriques seulement
#-------------------------------------------------------------------
  #HAS_PERMITTIVITY = BLOC(condition="TYPE == 'DIELECTRIC'",

#------------------------------------------------
# sous bloc niveau 2 : PERMITTIVITY
#------------------------------------------------

 Utiliser_la_permittivite = SIMP (statut='o', 
                                 typ='TXM',
                                 into = ("OUI","NON"),
                                 defaut="NON", 
                                ang ="Optionnaly use permittivity or not (default)",
                                fr  = u"Utilisation optionnelle de la permittivité du matériau. Pas d'utilisation par défaut.",
                                ), 
 PERMITTIVITY_properties = BLOC (condition="Utiliser_la_permittivite=='OUI'", 
  PERMITTIVITY = FACT ( statut="o", 
                        ang ="Permittivity properties",
                        fr  = u"propriétés de permittivité du matériau",
                        HOMOGENEOUS = SIMP (statut="o",
                                            typ="TXM",
                                            defaut="TRUE",
                                            into = ("TRUE","FALSE"),
                                            ang = "the material is homogeneous or not",
                                            fr  = u"le matériau est homogène ou non",
                                           ),
                        ISOTROPIC = SIMP (statut="o",
                                          typ="TXM",
                                          defaut="TRUE",
                                          into = ("TRUE","FALSE"),
                                          ang = "the material is isotropic or not",
                                          fr  = u"le matériau est isotrope ou non",
                                         ),
                       HOMOGENEOUS_ISOTROPIC_PROPERTIES = BLOC (condition="HOMOGENEOUS=='TRUE' and ISOTROPIC=='TRUE'",
                        LAW = SIMP (statut="o",
                                    typ="TXM",
                                    defaut="LINEAR",
                                    into = ("LINEAR",),
                                    ang = "linear law",
                                    fr  = u"loi linéaire",
                                   ),
                        VALUE = SIMP (statut="o",
                                      typ="C", 
                                      defaut=1,
                                      ang = "enter a complex relative value",
                                      fr = u"saisir une valeur complexe relative",
                                     ),
                       ), # Fin BLOC HOMOGENEOUS_ISOTROPIC_PROPERTIES
                    ), 
                ),# fin FACT PERMITTIVITY

) # fin OPER MATERIAL

##############################################################################
# Remarque generale a tous les materiaux : 
# pour conserver l'affichage scientifique le nombre derriere l'exposant doit
# etre strictement superieur au nombre de decimales 
#


#===================================================================
# 3eme bloc : bloc SOURCES
#====================================================================
# definition des differentes sources qui seront dans le bloc SOURCES
#-------------------------------------------------------------------
#


SOURCE = OPER ( nom = "SOURCE",
                op = None,
                repetable = 'n',
                UIinfo = { "groupes" : ( "2) Proprietes", ) },
                ang = "source definition", 
                fr = u"définition d'une source", 
                sd_prod = source,
                        
        Type=SIMP(statut='o', 
                                typ='TXM', 
                                into=("STRANDED_INDUCTOR", "HPORT", "EPORT"), 
                                ang = "Source type", 
                                fr = u"Type de source", 
                                ), 

            STRANDED_INDUCTOR_properties = BLOC (condition="Type=='STRANDED_INDUCTOR'", 
                STRANDED_INDUCTOR = FACT(statut='o',
                                         ang="Stranded inductor source",
                                         fr=u"source de type inducteur bobiné",
                                         NTURNS = SIMP (statut="o",
                                                        typ="I",
                                                        defaut=1,
                                                        ang="number of turns in the inductor",
                                                        fr= u"nombre de tours dans l'inducteur bobiné",
                                                       ),
                                         TYPE = SIMP (statut="o",
                                                      typ="TXM",
                                                      defaut="CURRENT",
                                                      into=("CURRENT","VOLTAGE"),
                                                      fr= u"source de type courant",
                                                      ang="current source type",
                                                     ),
                                         Resistance = SIMP (statut="f", 
                                                      typ="R", 
                                                      ), 
                                ), 
            ),# FIN de FACT STRANDED_INDUCTOR
         HPORT_properties = BLOC (condition="Type=='HPORT'",
                HPORT = FACT(statut='o',
                             ang="Magnetic port source",
                             fr=u"source de type port magnétique",
                             TYPE = SIMP (statut="o",
                                          typ="TXM",
                                          into=("VOLTAGE","CURRENT"),
                                          fr= u"source de type tension ou courant",
                                          ang="voltage or current source type",
                                         ),
                             Surface_Entree = SIMP (statut="o", 
                                                    typ=(grmaille, ), 
                                                    ), 
                             Surface_Sortie = SIMP (statut="o", 
                                                    typ=(grmaille, ), 
                                                    ), 
                ), 
            ),# FIN de FACT HPORT
         EPORT_properties = BLOC (condition="Type=='EPORT'",
                EPORT = FACT(statut='o',
                             ang="Electric port source",
                             fr=u"source de type port électrique",
                             TYPE = SIMP (statut="o",
                                          typ="TXM",
                                          into=("VOLTAGE","CURRENT"),
                                          fr= u"source de type tension ou courant",
                                          ang="voltage or current source type",
                                         ),
                             Surface_Entree = SIMP (statut="o", 
                                                    typ=(grmaille, ), 
                                                    ), 
                             Surface_Sortie = SIMP (statut="o", 
                                                    typ=(grmaille, ), 
                                                    ), 
                ), 
            ),# FIN de FACT EPORT
            
            Signal=SIMP(statut='o', 
                                typ='TXM', 
                                into=("WAVEFORM_CONSTANT", "WAVEFORM_SINUS"), 
                                ang = "Signal type, i.e., source evolution shape", 
                                fr = u"Type de signal, i.e., forme de la source", 
                                ), 
           WAVEFORM_CONSTANT_properties = BLOC (condition="Signal=='WAVEFORM_CONSTANT'", 
                WAVEFORM_CONSTANT = FACT(statut='o',
                                         ang="constant source",
                                         fr=u"source constante",
                                         AMPLITUDE = SIMP (statut="o",
                                                           typ="R", 
                                                           defaut=1,
                                                           ang = "enter the source magnitude value, in A or V units",
                                                           fr = u"saisir la valeur de l'amplitude de la source, en unités A ou V",
                                                          ),
                ),
            ),# FIN de FACT WAVEFORM_CONSTANT
            
            WAVEFORM_SINUS_properties = BLOC (condition="Signal=='WAVEFORM_SINUS'", 
                WAVEFORM_SINUS = FACT(statut='o',
                                      ang="sinus variation source",
                                      fr=u"source variant avec une forme sinusoïdale, définie par son amplitude, sa fréquence et sa phase",
                                      AMPLITUDE = SIMP (statut="o",
                                                        typ="R", 
                                                        defaut=1,
                                                        ang = "enter the source magnitude value, in A or V units",
                                                        fr = u"saisir la valeur de l'amplitude de la source, en unités A ou V",
                                                       ),
                                      FREQUENCY = SIMP (statut="o",
                                                        typ="R", 
                                                        defaut=0.0,
                                                        ang = "enter the source frequency value, in Hz units",
                                                        fr = u"saisir la valeur de la fréquence de la source, en Hz",
                                                       ),
                                      PHASE = SIMP (statut="o",
                                                    typ="R", 
                                                    defaut=0.0,
                                                    ang = "enter the source phase value, in degrees units",
                                                    fr = u"saisir la valeur de la phase de la source, en degrés",
                                                   ),
                ), 
            ),# FIN de FACT WAVEFORM_SINUS

       
)# Fin OPER SOURCE
