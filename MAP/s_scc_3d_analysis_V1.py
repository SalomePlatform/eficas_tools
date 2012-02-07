## -*- coding: utf-8 -*-
#
## --------------------------------------------------
## debut entete
## --------------------------------------------------
#
from Accas import *
from prefs_MAP import PATH_MODULE

#
#CONTEXT.debug = 1
JdC = JDC_CATA ( code = 'MAP',
                execmodul = None,
                #regles=(AU_MOINS_UN('TABLEAU',),AU_MOINS_UN('BENHUR',), AVANT ('PYGMEE' , 'BENHUR'),),
                regles=(AU_MOINS_UN('TABLEAU',),AU_MOINS_UN('TRAITEMENT',),A_CLASSER('TABLEAU','TRAITEMENT',)),
                       )# Fin JDC_CATA
#

TABLEAU= PROC(nom="TABLEAU",op=None,
              fr='lecture des proprietes a traiter ',
              FICHIER=SIMP(statut = "o", typ='Fichier',),
)

TRAITEMENT= PROC(nom="TRAITEMENT",op=None,
              fr='analyse statistique classique d une des variables du  tableau ',
              TYPE        =SIMP(statut='o',typ='TXM',defaut="analyse statistique classique",
                                 into=( "analyse statistique classique", "analyse statistique de la qualite","analyse de la dispersion suivant la distance au joint", "analyse de la dispersion suivant la distance a la pointe de fissure","visualisation dans le triangle standard"),),
              VARIABLE    =SIMP(statut='o',typ='TXM',defaut="stress_eq",
                                 into=( "stress_eq", "strain_eq","strain_xx","strain_yy","strain_zz"),)
)

