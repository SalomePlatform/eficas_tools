#)# -*- coding: utf-8 -*-
#
## --------------------------------------------------
## debut entete
## --------------------------------------------------
#
from Accas import *
import os
import sys

from prefs_MAP import PATH_STUDY

try :
   fichUtilisateur=os.path.join(os.environ['HOME'],'.Eficas_MAP/prefs_MAP.py')
   f=open(fichUtilisateur)
   txt=f.read()
   f.close()
   exec txt in locals()
except :
   pass


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
                regles=(AU_MOINS_UN('DISPL',),A_CLASSER('RBM','DISPL'))
                       )# Fin JDC_CATA
#
LIST_IMAGES=PROC(nom="LIST_IMAGES",op=None,
                FILE =SIMP(statut='r',typ='Fichier',fr='toto'),)
# Ordre Catalogue LIST_IMAGES

RBM= PROC(nom="RBM",op=None,
              CS=SIMP(statut = "o",fr="", typ='I',defaut="40"),
              CSJ=SIMP(statut = "f",fr="", typ='I',defaut="40"),
              GS=SIMP(statut = "o",fr="", typ='I',defaut="40"),
              GSJ=SIMP(statut = "f",fr="", typ='I',defaut="40"),
              VMAX=SIMP(statut = "o",fr="", typ='I',defaut="10"),
              VMAXJ=SIMP(statut = "f",fr="", typ='I',defaut="10"),
)
# Ordre Catalogue RBM

DISPL= PROC(nom="DISPL",op=None,
              CS=SIMP(statut = "o",fr="", typ='I',defaut="20"),
              CSJ=SIMP(statut = "f",fr="", typ='I',defaut="20"),
              GS=SIMP(statut = "o",fr="", typ='I',defaut="20"),
              GSJ=SIMP(statut = "f",fr="", typ='I',defaut="20"),
              VMAX=SIMP(statut = "o",fr="", typ='I',defaut="5"),
              VMAXJ=SIMP(statut = "f",fr="", typ='I',defaut="5"),
              )
# Ordre Catalogue DISPL

ETUDE= PROC(nom="ETUDE",op=None,
              fr="determination du nom et du repertoire de l'etude)",
              study_name=SIMP(statut = "o",fr="", typ='TXM',defaut="s_DIC"),
              study_path=SIMP(statut = "o",fr="", typ='TXM',defaut=PATH_STUDY),
              )
# Ordre Catalogue ETUDE
