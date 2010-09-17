## -*- coding: utf-8 -*-
#
## --------------------------------------------------
## debut entete
## --------------------------------------------------
#
from Accas import *
#
#CONTEXT.debug = 1
JdC = JDC_CATA ( code = 'SEP',
                 execmodul = None,
                # regles = ( AU_MOINS_UN ( 'M_TUBE','MAILLAGE_COUDE','CHARGE_LIMITE ), ),
                 regles = ( AU_MOINS_UN ( 'S_EP_INTERNE',), ),
                 ) # Fin JDC_CATA
#

S_EP_INTERNE= MACRO (nom       = 'S_EP_INTERNE',
              op        = None,
              sd_prod   = None,
              reentrant = 'n',
              UIinfo    = {"groupes":("Outils métier",)},
              fr        = "Sous epaisseur  ",
              dir_name  = SIMP(statut='o', typ='TXM',),
              methode   = SIMP(statut='o', typ='TXM',into=('generatrices','tortue',),),
              PARA_GEOM = FACT( statut='o',
				max=1,
				r_ext=SIMP(statut='o', typ='R', defaut=228.6,val_min=100,val_max=300),
 				unite=SIMP(statut='o', typ='TXM', defaut='mm',into=('mm',),),
			        ep_nominale=SIMP(statut='o', typ='R', defaut=22.000),	
                               ),
)


