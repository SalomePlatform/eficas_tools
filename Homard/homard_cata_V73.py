# -*- coding: utf-8 -*-
# --------------------------------------------------
# debut entete
# --------------------------------------------------

import Accas
from Accas import *

#CONTEXT.debug=1

JdC = JDC_CATA(code='HOMARD',
               execmodul=None,
               regles = (AU_MOINS_UN('DONNEES_HOMARD'),),
			)

# Type le plus general
class entier  (ASSD):pass
class reel    (ASSD):pass
class complexe(ASSD):pass
class liste   (ASSD):pass
class chaine  (ASSD):pass

# Types geometriques
class no  (GEOM):pass
class grno(GEOM):pass
class ma  (GEOM):pass
class grma(GEOM):pass

# --------------------------------------------------
# fin entete
# --------------------------------------------------

def bloc_adaptation():
    return BLOC(condition = "( RAFFINEMENT != None ) or ( DERAFFINEMENT != None ) ",
                fr="Nom MED du maillage en sortie, numero d'iteration",
                ang="MED name of the out-mesh, iteration rank",
                NITER =SIMP(statut='o',typ='I',
                           fr="Numéro d'itération avant l'adaptation.",
                           ang="Iteration number before adaptation." ),
                NOM_MED_MAILLAGE_NP1 =SIMP(statut='o',typ='TXM',
                           fr="Nom MED du maillage en sortie",
                           ang="MED name of the out-mesh" ),
                FICHIER_MED_MAILLAGE_NP1 =SIMP(statut='o',typ='TXM',
                           fr="Nom du fichier MED du maillage en sortie",
                           ang="MED file name of the out-mesh" ),
           )

#
def critere_de_raffinement() :
  return BLOC(condition = "( RAFFINEMENT != 'NON' ) ",
               fr="Critère de raffinement.",
               ang="Refinement threshold.",
               regles=(UN_PARMI ( 'CRIT_RAFF_ABS', 'CRIT_RAFF_REL', 'CRIT_RAFF_PE' ),),
               CRIT_RAFF_ABS   =SIMP (statut='f',typ='R',
                                      fr="Critère absolu",
                                      ang="Absolute threshold"  ),
               CRIT_RAFF_REL   =SIMP (statut='f',typ='R',
                                      fr="Critère relatif",
                                      ang="Relative threshold" ),
               CRIT_RAFF_PE    =SIMP (statut='f',typ='R',
                                      fr="Pourcentage d'éléments",
                                      ang="Percentage of elements" ),
               )
#
def critere_de_deraffinement():
   return BLOC(condition = "( DERAFFINEMENT != 'NON' ) ",
               fr="Critère de déraffinement.",
               ang="Unrefinement threshold.",
               regles=(UN_PARMI ( 'CRIT_DERA_ABS', 'CRIT_DERA_REL', 'CRIT_DERA_PE' ),),
               CRIT_DERA_ABS =SIMP(statut='f',typ='R' ,
                                   fr="Critère absolu",
                                   ang="Absolute threshold" ),
               CRIT_DERA_REL   =SIMP(statut='f',typ='R',
                                     fr="Critère relatif",
                                     ang="Relative threshold" ),
               CRIT_DERA_PE    =SIMP(statut='f',typ='R',
                                     fr="Pourcentage d'éléments",
                                     ang="Percentage of elements" ),
          )

def indicateur_d_erreur():
   return  BLOC(condition = "( RAFFINEMENT == 'LIBRE' ) or ( RAFFINEMENT == 'NON-CONFORME' ) or \
                          ( RAFFINEMENT == 'NON-CONFORME-INDICATEUR') or (DERAFFINEMENT == 'LIBRE')",
             fr="Indicateur d'erreur",
             ang="Error indicator",
             NOM_MED  =    SIMP (statut='o',typ='TXM',
                             fr="Nom MED de l'indicateur d'erreur.",
                             ang="MED name of error indicator.",),
             COMPOSANTE  = SIMP(statut='o',typ='TXM',
                             fr="Nom de la composante de l'indicateur d'erreur retenue.",
                             ang="Name of the selected component of the error indicator.",),
             NUME_ORDRE  = SIMP(statut='o',typ='I',
                             fr="Numero d'ordre de l'indicateur.",
                             ang="Rank number of the error indicator.",),
             NUME_PAS_TEMPS  = SIMP(statut='f',typ='I',
                             fr="Numero de pas de temps de l'indicateur.",
                             ang="Time step number of the error indicator.",),
                           ) 

def niveau_maximum():
   return BLOC ( condition = " ( RAFFINEMENT == 'LIBRE' ) or ( RAFFINEMENT == 'NON-CONFORME' ) or \
                                ( RAFFINEMENT == 'NON-CONFORME-INDICATEUR' ) or \
                                ( RAFFINEMENT == 'UNIFORME' ) ",
                 NIVE_MAX      = SIMP(statut='f',typ='I',
                                 fr="Niveau maximum de profondeur de raffinement",
                                 ang="Maximum level for refinement"),
                           )
#
def niveau_minimum():
   return BLOC ( condition = " ( DERAFFINEMENT == 'LIBRE' ) or ( DERAFFINEMENT == 'UNIFORME' ) ",
                 NIVE_MIN  = SIMP(statut='f',typ='I',
                             fr="Niveau minimum de déraffinement",
                             ang="Minimum level for unrefinement" ),
                           ) 


DONNEES_HOMARD=PROC(nom="DONNEES_HOMARD",op= 189, docu="U7.04.01-b",
            UIinfo={"groupes":("Fonction",)},
                    fr="Imprime le fichier de configuration de HOMARD.",
                    ang="Writes the configuration file for HOMARD.",
#
# 1. Langue des messages issus de HOMARD
#
         LANGUE = SIMP(statut='f',typ='TXM',defaut="FRANCAIS",    
                               into=("FRANCAIS","FRENCH","ANGLAIS","ENGLISH",),
                           fr="Langue des messages issus de HOMARD.",
                           ang="Language for HOMARD messages." ),
#
# 2. Les fichiers en entree/sortie
#
         MESSAGES =  SIMP(statut='o' ,typ='TXM',
                         fr="Nom du fichier contenant les messages de sortie",
                         ang="Log File"),
#
# 3. Le type de traitement :
#
          TRAITEMENT      =FACT(statut='o',
           regles=( UN_PARMI('TYPE_RAFFINEMENT_LIBRE','TYPE_DERAFFINEMENT_UNIFORME','TYPE_RAFFINEMENT_UNIFORME','INFORMATION'),
###                    EXCLUS('TYPE_RAFFINEMENT_LIBRE','INFORMATION'),
###                    EXCLUS('TYPE_RAFFINEMENT_UNIFORME','INFORMATION'),
		    ),
#
          TYPE_RAFFINEMENT_LIBRE = FACT(statut='f',
                           RAFFINEMENT   = SIMP (statut='o',typ='TXM',
                                           fr="Choix du mode de raffinement.",
                                           ang="Choice of refinement mode.",
                                           into=("NON","LIBRE","NON-CONFORME","NON-CONFORME-INDICATEUR"),),

                           DERAFFINEMENT = SIMP(statut='o',typ='TXM',
                                           fr="Choix du mode de deraffinement.",
                                           ang="Choice of unrefinement mode.",
                                           into=("NON","LIBRE",),),

                           b_adaptation 	      = bloc_adaptation(),
           		   b_indicateur_d_erreur      = indicateur_d_erreur(),
           		   b_critere_de_raffinement   = critere_de_raffinement(),
           		   b_critere_de_deraffinement = critere_de_deraffinement(),
                           b_niveau_minimum 	      = niveau_minimum(),
                           b_niveau_maximum 	      = niveau_maximum(),

                                   ),

#
           TYPE_RAFFINEMENT_UNIFORME = FACT( statut='f',
                           RAFFINEMENT   = SIMP (statut='o',typ='TXM',
                                           fr="Choix du mode de raffinement.",
                                           ang="Choice of refinement mode.",
					   defaut="UNIFORME",
                                           into=("UNIFORME",),),

                           DERAFFINEMENT = SIMP(statut='o',typ='TXM',
                                           fr="Choix du mode de deraffinement.",
                                           ang="Choice of unrefinement mode.",
					   defaut="NON",
                                           into=("NON",),),

                           b_adaptation 	      = bloc_adaptation(),
                           b_niveau_minimum 	      = niveau_minimum(),
                           b_niveau_maximum 	      = niveau_maximum(),

                                       ),

#
           TYPE_DERAFFINEMENT_UNIFORME = FACT( statut='f',
                           RAFFINEMENT   = SIMP (statut='o',typ='TXM',
                                           fr="Choix du mode de raffinement.",
                                           ang="Choice of refinement mode.",
					   defaut="NON",
                                           into=("NON",),),

                           DERAFFINEMENT = SIMP(statut='o',typ='TXM',
                                           fr="Choix du mode de deraffinement.",
                                           ang="Choice of unrefinement mode.",
					   defaut="UNIFORME",
                                           into=("UNIFORME",),),

                           b_adaptation 	      = bloc_adaptation(),
                           b_niveau_minimum 	      = niveau_minimum(),
                           b_niveau_maximum 	      = niveau_maximum(),
                                       ),
#
           INFORMATION     =SIMP(statut='f',typ='TXM',
                                 fr="Information sur un maillage",
                                 ang="Information on a mesh",
                                 into=("OUI",) ),
       ),
#
# 3.2. LES CONTRAINTES :
#
# 3.2.1. POUR DE L'ADAPTATION LIBRE, IL FAUT :
#      A. LE NUMERO D'ITERATION DU MAILLAGE DE DEPART
#      B. LE NOM MED DU MAILLAGE D'ENTREE
#      C. LE NOM MED DE L'INDICATEUR D'ERREUR
#      D. LE NUMERO D'ITERATION DU MAILLAGE DE DEPART
#      E. LA MISE A JOUR DE SOLUTION
#      F. LE NOM MED DU MAILLAGE DE SORTIE
#      REMARQUE : IL FAUT DES CRITERES, MAIS ON NE SAIT PAS LESQUELS
#
# 3.2.2. POUR DE L'ADAPTATION UNIFORME
#          IL FAUT :
#      A. LE NUMERO D'ITERATION DU MAILLAGE DE DEPART
#      B. LE NOM MED DU MAILLAGE DE SORTIE
#          IL NE FAUT PAS :
#      A. LE NOM MED DE L'INDICATEUR D'ERREUR
#      B. LE NOM DE LA COMPOSANTE DE L'INDICATEUR D'ERREUR
#      C. LES CRITERES
#      REMARQUE : A L'ITERATION 0, OU AUX ITERATIONS SUIVANTES SI MAJ DE SOLUTION,
#                 IL FAUT LE NOM MED DU MAILLAGE D'ENTREE
#
# 3.2.3. POUR DE L'INFORMATION :
#          IL FAUT :
#      A. LE NOM MED DU MAILLAGE D'ENTREE
#          IL NE FAUT PAS :
#      A. LE NOM MED DE L'INDICATEUR D'ERREUR
#      B. LE NOM DE LA COMPOSANTE DE L'INDICATEUR D'ERREUR
#      C. LES CRITERES
#      D. LE NUMERO D'ITERATION DU MAILLAGE DE DEPART
#      E. LA MISE A JOUR DE SOLUTION
#
           NOM_MED_MAILLAGE_N    = SIMP(statut='o',typ='TXM',     
                                 fr="Nom MED du maillage en entrée",
                                 ang="MED name of the in-mesh",),
           FICHIER_MED_MAILLAGE_N  = SIMP(statut='o',typ='TXM',     
                                 fr="Nom du fichier MED du maillage en entrée",
                                 ang="MED file name of the in-mesh",),
#
#
#
#
# 3.3. Le suivi de frontiere eventuel :
#
         NOM_MED_MAILLAGE_FRONTIERE =SIMP(statut='f',typ='TXM',
                           fr="Nom MED du maillage de la frontiere à suivre",
                           ang="MED name of the boundary mesh" ),
#
         b_frontiere_1 =BLOC ( condition = "NOM_MED_MAILLAGE_FRONTIERE != None" ,
                           GROUP_MA        =SIMP(statut='f',typ=grma,validators=NoRepeat(),max='**',
                                                 fr="Groupes définissant la frontière",
                                                 ang="Groups which define the boundary" ),
                               ) ,
         fichier_frontiere=BLOC ( condition = "NOM_MED_MAILLAGE_FRONTIERE != None" ,
			  FIC_FRON = SIMP(statut='f',typ='TXM',
			                 fr="Nom du fichier MED contenant le maillage frontiere",
			                 ang="MED File including the boundary mesh" ),
                               ), 
#
#
# 4. L'ANALYSE DU MAILLAGE
#
         ANALYSE         =FACT(statut='f',
                               fr="Analyse du maillage.",
                               ang="Mesh analysis.",
#
#    5 CHOIX NON EXCLUSIFS, AVEC DEUX VARIANTES (OUI/NON) :
#    A. NOMBRE DES ELEMENTS
#    B. QUALITE DES ELEMENTS
#    C. INTERPENETRATION DES ELEMENTS
#    D. CONNEXITE DU MAILLAGE
#    E. TAILLE DES DIFFERENTS SOUS-DOMAINES
#
           regles=(AU_MOINS_UN('NOMBRE','QUALITE','INTERPENETRATION','CONNEXITE','TAILLE'),),
#
         NOMBRE          =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON"),
                          fr="Nombre de noeuds et éléments du maillage",
                          ang="Number of nodes and elements in the mesh" ),
#
         QUALITE         =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Qualité du maillage",
                          ang="Mesh quality" ),
#
         INTERPENETRATION=SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Controle de la non interpénétration des éléments.",
                          ang="Overlapping checking." ),
#
         CONNEXITE       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Connexité du maillage.",
                          ang="Mesh connexity." ),
#
         TAILLE          =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Tailles des sous-domaines du maillage.",
                          ang="Sizes of mesh sub-domains." ),
#
         ),
#
#
# 5. Les fichiers en entree/sortie
#
#
)  ;
