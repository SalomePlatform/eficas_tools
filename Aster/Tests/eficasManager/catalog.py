# -*- coding: iso-8859-1 -*-
from Accas import *

JdC = JDC_CATA (code = 'DEMO_AUS20120329',
                execmodul = None,
                regles=(UN_PARMI('EPREUVE_ENCEINTE'),)
                )

EPREUVE_ENCEINTE=MACRO(
    nom = 'EPREUVE_ENCEINTE',op=None, fr="Mise en épreuve d'enceinte",
    z_inf_corbeau         = SIMP(typ='R',fr='Altitude inférieure du corbeau',statut='o',defaut=41.2),
    z_mi_corbeau          = SIMP(typ='R',fr='Altitude médiane du corbeau',statut='o',defaut=42.80),
    z_top_corbeau         = SIMP(typ='R',fr='Altitude supérieure du corbeau',statut='o',defaut=43.65),
    rayon_interne_corbeau = SIMP(typ='R',fr='Rayon interne du corbeau',statut='o',defaut=20.2,val_min=17.0,val_max=21.9)
    )

#EPREUVE_ENCEINTE=MACRO(
#    nom = 'EPREUVE_ENCEINTE',op=None, fr="Mise en Ã©preuve d'enceinte",
#    MAILLAGE = FACT(
    
