#)# -*- coding: utf-8 -*-
#
## --------------------------------------------------
## debut entete
## --------------------------------------------------
#
from Accas import *
import os
import sys
import types

#
#CONTEXT.debug = 1
JdC = JDC_CATA ( code = 'MAP',
                execmodul = None,
               )# Fin JDC_CATA
#


AFAIRE=PROC(nom='AFAIRE',op=None,
      MCSIMP=SIMP(typ='TXM',defaut='afaire', statut='o', fr = '', ang = 'A class for the definition of a file', max=1,),
)

