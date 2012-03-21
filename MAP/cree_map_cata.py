##################
# -*- coding: utf-8 -*-
#
## --------------------------------------------------
## debut entete
## --------------------------------------------------
#
from Accas import *
class param_map	(ASSD) : pass


#
#CONTEXT.debug = 1
JdC = JDC_CATA ( code = 'MAP',
                execmodul = None,
                )# Fin JDC_CATA

import opsMAP
DICTDATA= MACRO ( nom = "DICTDATA",
                op = None,
                UIinfo = { "groupes" : ( "Gestion du travail", ) },
                fr = "Chargement du dictionnaire des donnees possibles",
                ang = "load data dictionnary",
                sd_prod = opsMAP.INCLUDE,
                op_init = opsMAP.INCLUDE_context,
                fichier_ini = 1,
                FileName = SIMP ( statut = "o",
                    typ = ('Fichier', 'comm Files (*.comm);;All Files (*)',),
                    defaut="DictDonnees.py",
                    ang = "Physical identifier",
                ),

) # Fin PROC MODEL


CODE=PROC(nom="CODE", op=None,
          fr="Description du code",
          NAME    = SIMP(statut='o',typ='TXM',max=1),
          COMMENT = SIMP(statut='f',typ='TXM',max=1),
          FUNCT   = FACT(statut= 'o',max=1,
                  functionName = SIMP(statut= 'o',typ= 'TXM' ,max=1,defaut="myexecute"),
                  moduleName   = SIMP(statut= 'f',typ= 'TXM' ,max=1),
                  packageName  = SIMP(statut= 'f',typ= 'TXM' ,max=1,defaut="map.schemas")
          )
)
DONNEE=OPER(nom="DONNEE",op=  None,sd_prod=param_map,
   DATA_TYP = SIMP(statut='o',typ='TXM', 
              into=("MAP_INT","MAP_STRING","MAP_BOOL","MAP_FILE","MAP_FILENAME","MAP_FOLDER","MAP_DOUBLE","MAP_COMPLEX","MAP_TUPLE")),
              b_tuple       = BLOC(condition = "DATA_TYP == 'MAP_TUPLE'",
                  LONGUEUR  = SIMP(statut='o',typ='I',defaut= 2),),
   DATA_ANG=SIMP(statut='o',typ='TXM'),
   DATA_STATUT=SIMP(statut='f',typ='TXM',into=['f','o'],),

   b_defaut_int  = BLOC(condition = "DATA_TYP == 'MAP_INT'",
      DATA_DEF  = SIMP(statut='f',typ='I',fr='valeur par defaut'),
      DATA_INTO = SIMP(statut='f',typ='I',fr="liste des valeurs discretes", min=1, max="**")
                      ),
   b_defaut_real = BLOC(condition = "DATA_TYP == 'MAP_DOUBLE'",
      DATA_DEF  = SIMP(statut='f',typ='R',fr='valeur par defaut'),),
   b_defaut_txm  = BLOC(condition = "DATA_TYP == 'MAP_STRING'",
      DATA_DEF  = SIMP(statut='f',typ='TXM',fr='valeur par defaut'),),
  
)


INPUTINTERFACE=PROC(nom="INPUTINTERFACE",op=None,
          fr="Description de interface en entree",
          DATA=SIMP(statut='o',typ=param_map,min=1,max="**")
)

OUTPUTINTERFACE=PROC(nom="OUTPUTINTERFACE",op=None,
          fr="Description de interface en entree",
          DATA=SIMP(statut='o',typ=param_map,min=1,max="**")
)


