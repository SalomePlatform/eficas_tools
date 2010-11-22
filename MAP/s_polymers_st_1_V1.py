## -*- coding: utf-8 -*-
#
## --------------------------------------------------
## debut entete
## --------------------------------------------------
#
from Accas import *
from prefs_MAP import PATH_MODULE
from prefs_MAP import PATH_STUDY
from prefs_MAP import PATH_PYGMEE

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
                regles=(AU_MOINS_UN('METHODE',),AU_MOINS_UN('MATERIAUX',),AU_MOINS_UN('DISCRETISATION',),),
                       )# Fin JDC_CATA
#

ETUDE= PROC(nom="ETUDE",op=None,
              fr="determination du nom et du repertoire de l'etude)",
              study_name=SIMP(statut = "f",fr="", typ='TXM',defaut="s_polymers_st_1_for_YACS"),
              study_path=SIMP(statut = "f",fr="", typ='TXM',defaut=PATH_STUDY),
              )

METHODE= PROC(nom="METHODE",op=None,
              fr='choix de la methode de calcul (maillage ou grille cartesienne)',
              CHOIX=SIMP(statut = "o",fr="elements finis sur maillage ou differences finies sur grilles", 
                         typ='TXM', defaut="FD+grid", into=("FEM+mesh","FD+grid")),
              LANCEMENT=SIMP(statut = "o",fr="lancement de Code_Aster ou de fdvgrid selon le choix", 
                         typ='TXM', defaut="oui", into=("oui","non")),
              )

MATERIAUX= PROC(nom="MATERIAUX",op=None,
              fr='definition des proprietes du materiau : fuseau, taille du VER, proprietes des phases',
              rve_size=SIMP(statut = "o",fr="taille du VER", typ='R', defaut=50.),
              sieve_curve_in = SIMP ( statut = "o", fr="Fichier représentant le fuseau granulaire",typ = "Fichier", defaut=PATH_STUDY+"/inclusion_size_distribution.txt"),
              repulsion_distance=SIMP(statut = "o",fr="distance de replusions", typ='R', defaut=0.1),
              lambda_M=SIMP(statut = "o",fr="conductivite de la matrice", typ='R', defaut=1.0 , val_min =0.),
              lambda_I=SIMP(statut = "o",fr="conductivite des inclusions", typ='R', defaut=10.0, val_min =0.),
              inclusion_name=SIMP(statut = "f",fr="", typ='TXM',defaut=PATH_STUDY+"/pygmee_v2_test_1.inclusions",cache=1),
              rve_name=SIMP(statut = "f",fr="", typ='TXM',defaut=PATH_STUDY+"/pygmee_v2_test_1.rve",cache=1),
              sieve_curve_out=SIMP(statut = "f",fr="", typ='TXM',defaut=PATH_STUDY+"/pygmee_v2.sieve_out",cache=1),
)

DISCRETISATION= PROC(nom="DISCRETISATION",op=None,
              fr='definition du nombre d''elements sur le cote du VER',
              finesse=SIMP(statut = "o",fr="nombre d'elements sur le cote", typ='I', defaut=10 , into=(10,12,20,32,64,128),),
)
