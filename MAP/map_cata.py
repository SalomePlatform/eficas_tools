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
from prefs_MAP import PATH_MAP


class Tuple:
  def __init__(self,ntuple):
    self.ntuple=ntuple

  def __convert__(self,valeur):
    if type(valeur) == types.StringType:
      return None
    if len(valeur) != self.ntuple:
      return None
    return valeur

  def info(self):
    return "Tuple de %s elements" % self.ntuple

  __repr__=info
  __str__=info

#
#CONTEXT.debug = 1
JdC = JDC_CATA ( code = 'MAP',
                execmodul = None,
                #regles=(AU_MOINS_UN('DISPL',),A_CLASSER('RBM','DISPL'))
                       )# Fin JDC_CATA
s_test01_PARAM=PROC(nom='s_test01_PARAM',op=None,
v=SIMP(typ='TXM',fr='',ang='',statut='o',docu='',into=['1', '2'],min=1,max=1,val_min='**',val_max='**',defaut=None),
)
s_test01_DATA=PROC(nom='s_test01_DATA',op=None,
y=SIMP(typ='R',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
x=SIMP(typ='R',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
z=SIMP(typ='I',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)

