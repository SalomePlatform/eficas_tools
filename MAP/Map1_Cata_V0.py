## -*- coding: utf-8 -*-
#
## --------------------------------------------------
## debut entete
## --------------------------------------------------
#
from Accas import *
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
                regles=(AU_MOINS_UN('VER_MOX',),),
                       )# Fin JDC_CATA
#


VER_MOX= PROC(nom="VER_MOX",op=None,
              fr='mise en donnee de la generation du VER MOX',

              NBPHASES=SIMP(statut='o',typ='I',defaut=1,into=(1,2)),
              FUSEAU1=FACT(fr="entree de lecfus", statut='o',
                  FORME=SIMP(statut = "o", typ='TXM', defaut="fichier", into=("manuel","fichier")),

                  b_forme=BLOC( condition = "FORME == 'fichier'",
                     FORMAT  = SIMP(statut = "o", typ='TXM', defaut="croissant", into=("croissant","decroissant")),
                     FICHIER = SIMP ( statut = "o", typ = "Fichier", ),
                              ),

                  b_manuel=BLOC( condition = "FORME == 'manuel'",
                     LFUSEAU = SIMP ( statut = "o", typ=Tuple(2),validators=VerifTypeTuple(('R','R')), max="**",) ,),),


              TAILLE=SIMP(statut = "o",fr="taille du VER en microns", typ='I'),
              DISTANCE=SIMP(statut = "o",fr="distance de replusions", typ='R'),
)
