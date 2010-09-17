# -*- coding: utf-8 -*-
import types
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


# --------------------------------------------------
# debut entete
# --------------------------------------------------

import Accas
from Accas import *


#CONTEXT.debug = 1
JdC = JDC_CATA ( code = 'CUVE1D-DEFAILLGLOB',
                 execmodul = None,
                 regles = ( AU_MOINS_UN ('OPTIONS','DEFAUT', 'CUVE', 'MODELES', 'INITIALISATION', 'REVETEMENT', 'METAL_BASE', 'TRANSITOIRE'), 
                            A_CLASSER ( ('OPTIONS',), ('DEFAUT', 'CUVE', 'MODELES', 'INITIALISATION', 'REVETEMENT', 'METAL_BASE', 'TRANSITOIRE'))
                          )
                 ) # Fin JDC_CATA

# --------------------------------------------------
# fin entete
# --------------------------------------------------






#================================
# 1. Definition des OPTIONS
#================================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)

OPTIONS = PROC ( nom = "OPTIONS",
                 op = 68,
                 fr = "Definitions des options", 

#===
# Liste des paramètres
#===

# INCRTPS
  IncrementTemporel = SIMP ( statut = "o",
                             typ = "I",
                             defaut = "1",
          	             max = 1,
                             #val_max = 100,
                             fr = "Increment temporel (=1 pour calcul deterministe)",
                             ),

# DTPREC
  IncrementMaxTemperature = SIMP ( statut = "o", 
                                   typ = "R", 
				   defaut = "0.1", 
				   max = 1, 
				   val_max = 1., 
				   fr = "Increment maximum d'evolution de la temperature par noeud et par instant (°C)",
				   ),

# DTARCH
  IncrementMaxTempsAffichage = SIMP ( statut = "o", 
                                      typ = "R", 
				      defaut = "1000.", 
				      max = 1, 
				      val_max = 1000., 
				      fr = "Increment maximum de temps pour l'affichage (s)",
				      ),

# NBO
# Question : NBO depend-il de TYPGEOM ??
  NombreNoeudsMaillage = SIMP ( statut = "o", 
                                typ = "R", 
				max=1, 
				val_max = 1000., 
				fr = "Nombre de noeuds a considerer dans le maillage interne",
				),

# 
  ListeInstants = SIMP ( statut = "o",
                         typ = Tuple(2),
                         max = "**",
                         fr = "Liste des instants ",
                         validators=VerifTypeTuple(('R','R')),
                         ),

  ListeInstants2 = SIMP ( statut = "o",
                         typ = Tuple(2),
                         max = "**",
                         fr = "Liste des instants ",
                         ),

) # Fin OPER OPTIONS
