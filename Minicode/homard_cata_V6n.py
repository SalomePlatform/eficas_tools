
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
#class entier  (ASSD):pass
#class reel    (ASSD):pass
#class complexe(ASSD):pass
#class liste   (ASSD):pass
#class chaine  (ASSD):pass

# Types geometriques
#class no  (GEOM):pass
#class grno(GEOM):pass
#class ma  (GEOM):pass
#class grma(GEOM):pass

# --------------------------------------------------
# fin entete
# --------------------------------------------------

def bloc_maj_champ():
    return BLOC(condition = "( RAFFINEMENT != None ) or ( DERAFFINEMENT != None ) ",
                fr="Nom MED du maillage en sortie, numero d'iteration et mise à jour de champs",
                ang="MED name of the out-mesh, iteration rank and field updating",
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

def critere_de_deraffinement():
   return BLOC(condition = "( DERAFFINEMENT == 'LIBRE' ) ",
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

TEST=PROC(nom="TEST",op= 189, docu="U7.04.01-b",
          fr="Imprime le fichier de configuration de HOMARD.",
       TRAITEMENT      =FACT(statut='o',
          regles=( UN_PARMI('TYPE_RAFFINEMENT_LIBRE','TYPE_RAFFINEMENT_UNIFORME'),),
          TYPE_RAFFINEMENT_LIBRE = FACT(statut='f',
                                   RAFFINEMENT   = SIMP(statut='o',typ='TXM',
                                                    fr="Choix du mode de raffinement.",
                                                    ang="Choice of refinement mode.",
                                                    into=("LIBRE","UNIFORME",),
                                                   ),
                                   DERAFFINEMENT = SIMP(statut='o',typ='TXM',
                                                    fr="Choix du mode de deraffinement.",
                                                    ang="Choice of unrefinement mode.",
                                                    into=("LIBRE",), 
                                                   ),
                                   b_iteration_maj_champ =bloc_maj_champ(),
                                   b_critere_de_deraffinement =critere_de_deraffinement(),
                                   ),

           TYPE_RAFFINEMENT_UNIFORME = FACT(statut='f',
                                       RAFFINEMENT   = SIMP(statut='o',typ='TXM',
                                                       fr="Choix du mode de raffinement.",
                                                       ang="Choice of refinement mode.",
                                                       into=("NON","NON-CONFORME","NON-CONFORME-INDICATEUR"),
                                                       ),
                                       DERAFFINEMENT = SIMP(statut='o',typ='TXM',
                                                       fr="Choix du mode de deraffinement.",
                                                       ang="Choice of unrefinement mode.",
                                                       into=("UNIFORME","NON",),
                                                       ),
                                       b_iteration_maj_champ =bloc_maj_champ(),
                                       b_critere_de_deraffinement =critere_de_deraffinement(),
                                       ),
       ),
);

DONNEES_HOMARD=PROC(nom="DONNEES_HOMARD",op= 189, docu="U7.04.01-b",
            UIinfo={"groupes":("Fonction",)},
                    fr="Imprime le fichier de configuration de HOMARD.",
                    ang="Writes the configuration file for HOMARD.",
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
#
         regles=( AU_MOINS_UN('TYPE_RAFFINEMENT_LIBRE','TYPE_RAFFINEMENT_UNIFORME'),
                  EXCLUS('TYPE_RAFFINEMENT_LIBRE','TYPE_RAFFINEMENT_UNIFORME'),),
	   TYPE_RAFFINEMENT_LIBRE = FACT(statut='f',
           	RAFFINEMENT      = SIMP(statut='o',typ='TXM',     
                                 position='global',
                                 fr="Choix du mode de raffinement.",
                                 ang="Choice of refinement mode.",
                                 into=("LIBRE","UNIFORME",) ),
	        DERAFFINEMENT = SIMP(statut='o',typ='TXM',     
                                 position='global',
                                 fr="Choix du mode de deraffinement.",
                                 ang="Choice of unrefinement mode.",
                                 into=("LIBRE",), ),),
	   TYPE_RAFFINEMENT_UNIFORME = FACT(statut='f',
           	RAFFINEMENT      = SIMP(statut='o',typ='TXM',     
                                 fr="Choix du mode de raffinement.",
                                 ang="Choice of refinement mode.",
                                 into=("NON","NON-CONFORME","NON-CONFORME-INDICATEUR") ),
	        DERAFFINEMENT = SIMP(statut='o',typ='TXM',     
                                 fr="Choix du mode de deraffinement.",
                                 ang="Choice of unrefinement mode.",
                                 into=("UNIFORME","NON",), ),),
#
           b_iteration_maj_champ =BLOC(condition = "( RAFFINEMENT != None ) or ( DERAFFINEMENT != None ) ",
           #b_iteration_maj_champ =BLOC(condition = "(TYPE_RAFFINEMENT_UNIFORME != None) or (TYPE_RAFFINEMENT_LIBRE != None)",
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
     ),
);
