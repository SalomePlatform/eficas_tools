##################
# -*- coding: utf-8 -*-
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
                #regles=(AU_MOINS_UN('DISPL',),A_CLASSER('RBM','DISPL'))
                       )# Fin JDC_CATA
S_TEST01_PARAM=PROC(nom='S_TEST01_PARAM',op=None,
v=SIMP(typ='TXM',fr='',ang='',statut='o',docu='',into=['a', 'b'],min=1,max=1,defaut=None),
                    )

S_TEST01_DATA=PROC(nom='S_TEST01_DATA',op=None,
a_string=SIMP(typ='TXM',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
an_integer=SIMP(typ='I',fr='',ang='',statut='o',docu='',into=None,min=1,max=1000,val_min='**',val_max='**',defaut=None),
a_float=SIMP(typ='R',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
file_output=SIMP(typ='TXM',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)

