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
                regles=(AU_MOINS_UN('PYGMEE',),AU_MOINS_UN('BENHUR',), AVANT ('PYGMEE' , 'BENHUR'),),
                       )# Fin JDC_CATA
#

PYGMEE= PROC(nom="PYGMEE",op=None,
              fr='definition de la morphologie',

#              NBPHASES=SIMP(statut='o',typ='I',defaut=1,into=(1,2)),
              FUSEAU1=FACT(fr="entree de lecfus", statut='o',
                  FORME=SIMP(statut = "o", typ='TXM', defaut="fichier", into=("manuel","fichier")),

                  b_forme=BLOC( condition = "FORME == 'fichier'",
                     FORMAT  = SIMP(statut = "o", typ='TXM', defaut="croissant", into=("croissant","decroissant")),
                     FICHIER = SIMP ( statut = "o", typ = "Fichier", defaut="/local/noyret/MAP/modules/polymers/s_poly_st_1/inclusion_size_distribution.txt"),
                              ),

                  b_manuel=BLOC( condition = "FORME == 'manuel'",
                     LFUSEAU = SIMP ( statut = "o", typ=Tuple(2),validators=VerifTypeTuple(('R','R')), max="**",) ,),),
#                     LFUSEAU = SIMP ( statut = "o", typ=Tuple(2), max="**",) ,),),


              TAILLE=SIMP(statut = "o",fr="taille du VER", typ='R', defaut=50.),
              DISTANCE=SIMP(statut = "o",fr="distance de replusions", typ='R', defaut=0.1),
              LANCEMENT=SIMP(statut = "o",fr="lancement de PYGMEE", typ='TXM', defaut="oui", into=("oui","non")),
)

BENHUR= PROC(nom="BENHUR",op=None,
              fr='definition du maillage',

              FINESSE=SIMP(statut = "o",fr="nombre d\'elements par cote", typ='I', into=(10,12), defaut=10),
              LANCEMENT=SIMP(statut = "o",fr="lancement de BENHUR", typ='TXM', defaut="oui", into=("oui","non")),
)

ASTER= PROC(nom="ASTER",op=None,
              fr='definition du calcul',

              CONDUCTIVITE_M=SIMP(statut = "o",fr="conductivite de la matrice", typ='R', defaut=1.0 , val_min =0.),
              CONDUCTIVITE_I=SIMP(statut = "o",fr="conductivite des inclusions", typ='R', defaut=1.0, val_min =0.),
              LANCEMENT=SIMP(statut = "o",fr="lancement de Code_Aster", typ='TXM', defaut="oui", into=("oui","non")),
)

GMSH= PROC(nom="GMSH",op=None,
              fr='post-traitement',

              LANCEMENT=SIMP(statut = "o",fr="lancement de GMSH", typ='TXM', defaut="oui", into=("oui","non")),
)
