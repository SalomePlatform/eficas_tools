# -*- coding: utf-8 -*-

# --------------------------------------------------
# debut entete
# --------------------------------------------------

import Accas
from Accas import *

class loi ( ASSD ) : pass
class variable ( ASSD ) : pass


#CONTEXT.debug = 1
JdC = JDC_CATA ( code = 'PERFECT',
                 execmodul = None,
                 regles = ( AU_MOINS_UN ( 'RPV' , 'INTERNALS'), ),
                 ) # Fin JDC_CATA

# --------------------------------------------------
# fin entete
# --------------------------------------------------


#================================
# 1. Definition des LOIS
#================================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)
RPV = PROC(nom = "RPV",
           op = 68,
           fr = "end-products RPV-2 and ToughnessModule", 
           regles = ( AU_MOINS_UN ( 'RPV2' , 'ToughnessModule'), ),
           RPV2 = FACT(statut='f',
                   regles = ( AU_MOINS_UN ( 'IRRAD' , 'CONVOLVE', 'LONG_TERM','HARD'), ),
                        IRRAD = FACT( statut='f',
                            neutron_spectrum = SIMP(statut='f',typ='R', max='**'),
                            fcc_crystal = FACT(statut='o',
                                 nu       = SIMP(statut='o',typ='R',defaut=0.3),
                                 mu       = SIMP(statut='o',typ='R',defaut=70),),
                            operating_conditions = FACT(statut = 'o',
                              relative_time_increments = SIMP(statut='o',typ='R', max='**'),
			      time_irrad = SIMP(statut='o',typ='R',defaut=1e+07,),
                              temp_irrad = SIMP(statut='o',typ='R',defaut=573,),
                              flux_cut_off_energy = SIMP (statut='o',typ='R',defaut=1),)
                        ),
                        CONVOLVE = FACT(statut='f',
                        UNITE_RESU  = SIMP(statut='f',typ='I',defaut=32),
                        UNITE_RESU2  = SIMP(statut='f',typ='I',defaut=32),
                             ))
);
                      
INTERNALS = PROC ( nom = "INTERNALS",
            op = 68,
            fr = "end-products INTERN-1",
           # regles = ( AU_MOINS_UN ( 'RPV2' , 'ToughnessModule'), ),
             INTERN1 = FACT(statut='f',
                          UNITE_RESU_FORC = SIMP(statut='f',typ='I',defaut=33),
                          UNITE_RESU_IMPE  = SIMP(statut='f',typ='I',defaut=32),)
);

