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
#
# 3.1. DEUX CHOIX EXCLUSIFS :
#
#      A. ADAPTATION AVEC DES VARIANTES SUR LE MODE DE RAFFINEMENT/DERAFFINEMENT
#         . RAFFINEMENT ET DERAFFINEMENT
#         . RAFFINEMENT SEUL
#         . DERAFFINEMENT SEUL
#      B. INFORMATION SUR UN MAILLAGE
#
           regles=( AU_MOINS_UN('RAFFINEMENT','DERAFFINEMENT','INFORMATION'),
                    EXCLUS('RAFFINEMENT','INFORMATION'),
                    EXCLUS('DERAFFINEMENT','INFORMATION'),),
                    #PRESENT_PRESENT('RAFFINEMENT','DERAFFINEMENT'),
                    #PRESENT_PRESENT('DERAFFINEMENT','RAFFINEMENT'),),
           RAFFINEMENT      =SIMP(statut='f',typ='TXM',     
                                 fr="Choix du mode de raffinement.",
                                 ang="Choice of refinement mode.",
                                 into=("LIBRE","UNIFORME","NON","NON-CONFORME","NON-CONFORME-INDICATEUR") ),
           DERAFFINEMENT   =SIMP(statut='f',typ='TXM',     
                                 fr="Choix du mode de deraffinement.",
                                 ang="Choice of unrefinement mode.",
                                 into=("LIBRE","UNIFORME","NON") ),
           INFORMATION     =SIMP(statut='f',typ='TXM',
                                 fr="Information sur un maillage",
                                 ang="Information on a mesh",
                                 into=("OUI",) ),
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
           NOM_MED_MAILLAGE_N    =SIMP(statut='o',typ='TXM',     
                                 fr="Nom MED du maillage en entrée",
                                 ang="MED name of the in-mesh",),
           FICHIER_MED_MAILLAGE_N    =SIMP(statut='o',typ='TXM',     
                                 fr="Nom du fichier MED du maillage en entrée",
                                 ang="MED file name of the in-mesh",),
#
           b_iteration_maj_champ =BLOC(condition = "( RAFFINEMENT != None ) or ( DERAFFINEMENT != None ) ",
                           fr="Nom MED du maillage en sortie, numero d'iteration et mise à jour de champs",
                           ang="MED name of the out-mesh, iteration rank and field updating",
                           NITER                =SIMP(statut='o',typ='I',
                           fr="Numéro d'itération avant l'adaptation.",
                           ang="Iteration number before adaptation." ),
                           NOM_MED_MAILLAGE_NP1 =SIMP(statut='o',typ='TXM',
                           fr="Nom MED du maillage en sortie",
                           ang="MED name of the out-mesh" ),
                           FICHIER_MED_MAILLAGE_NP1 =SIMP(statut='o',typ='TXM',
                           fr="Nom du fichier MED du maillage en sortie",
                           ang="MED file name of the out-mesh" ),
                           ) ,
#
           b_indicateur_d_erreur  =BLOC(condition = "( RAFFINEMENT == 'LIBRE' ) or ( RAFFINEMENT == 'NON-CONFORME' ) or \
                                                     ( RAFFINEMENT == 'NON-CONFORME-INDICATEUR' ) or ( DERAFFINEMENT == 'LIBRE' ) ",
                           fr="Indicateur d'erreur",
                           ang="Error indicator",
                           NOM_MED  =SIMP(statut='o',typ='TXM',
                           fr="Nom MED de l'indicateur d'erreur.",
                           ang="MED name of error indicator.",),
                           COMPOSANTE  =SIMP(statut='o',typ='TXM',
                           fr="Nom de la composante de l'indicateur d'erreur retenue.",
                           ang="Name of the selected component of the error indicator.",),
                           NUME_ORDRE  =SIMP(statut='f',typ='I',
                           fr="Numero d'ordre de l'indicateur.",
                           ang="Rank number of the error indicator.",),
                           ) ,
#
           b_critere_de_raffinement =BLOC( condition = "( RAFFINEMENT == 'LIBRE' ) or ( RAFFINEMENT == 'NON-CONFORME' ) or \
                                                        ( RAFFINEMENT == 'NON-CONFORME-INDICATEUR' ) ",
                           fr="Critère de raffinement.",
                           ang="Refinement threshold.",
                           regles=(UN_PARMI ( 'CRIT_RAFF_ABS', 'CRIT_RAFF_REL', 'CRIT_RAFF_PE' ),),
                           CRIT_RAFF_ABS   =SIMP(statut='f',typ='R',
                                                 fr="Critère absolu",
                                                 ang="Absolute threshold"  ),
                           CRIT_RAFF_REL   =SIMP(statut='f',typ='R',
                                                 fr="Critère relatif",
                                                 ang="Relative threshold" ),
                           CRIT_RAFF_PE    =SIMP(statut='f',typ='R',
                                                 fr="Pourcentage d'éléments",
                                                 ang="Percentage of elements" ),
                           ) ,
#
           b_critere_de_deraffinement =BLOC ( condition = "( DERAFFINEMENT == 'LIBRE' ) ",
                           fr="Critère de déraffinement.",
                           ang="Unrefinement threshold.",
                           regles=(UN_PARMI ( 'CRIT_DERA_ABS', 'CRIT_DERA_REL', 'CRIT_DERA_PE' ),),
                           CRIT_DERA_ABS   =SIMP(statut='f',typ='R' ,
                                                 fr="Critère absolu",
                                                 ang="Absolute threshold" ),
                           CRIT_DERA_REL   =SIMP(statut='f',typ='R',
                                                 fr="Critère relatif",
                                                 ang="Relative threshold" ),
                           CRIT_DERA_PE    =SIMP(statut='f',typ='R',
                                                 fr="Pourcentage d'éléments",
                                                 ang="Percentage of elements" ),
                           ) ,
#
           b_niveau_maximum =BLOC ( condition = " ( RAFFINEMENT == 'LIBRE' ) or ( RAFFINEMENT == 'NON-CONFORME' ) or \
                                                  ( RAFFINEMENT == 'NON-CONFORME-INDICATEUR' ) or ( RAFFINEMENT == 'UNIFORME' ) ",
                           NIVE_MAX        =SIMP(statut='f',typ='I',
                                                 fr="Niveau maximum de profondeur de raffinement",
                                                 ang="Maximum level for refinement"),
                           ) ,
#
           b_niveau_minimum =BLOC ( condition = " ( DERAFFINEMENT == 'LIBRE' ) or ( DERAFFINEMENT == 'UNIFORME' ) ",
                           NIVE_MIN        =SIMP(statut='f',typ='I',
                                                 fr="Niveau minimum de déraffinement",
                                                 ang="Minimum level for unrefinement" ),
                           ) ,
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
         ),
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
)  ;
