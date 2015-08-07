# -*- coding: iso-8859-1 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

# --------------------------------------------------
# debut entete
# --------------------------------------------------

#from Accas import ASSD, JDC_CATA, AU_MOINS_UN, PROC, SIMP, FACT, OPER, MACRO, BLOC, A_VALIDATOR
from Accas import *
import opsPSEN

class loi      ( ASSD ) : pass
class variable ( ASSD ) : pass
class sd_charge     ( ASSD ) : pass
class sd_generateur ( ASSD ) : pass
class sd_ligne     ( ASSD ) : pass
class sd_transfo ( ASSD ) : pass
#class sd_busbar ( sd_generateur,sd_charge ) : pass

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

class Matrice:
  def __init__(self,nbLigs=None,nbCols=None,methodeCalculTaille=None,formatSortie="ligne",valSup=None,valMin=None,structure=None):
      self.nbLigs=nbLigs
      self.nbCols=nbCols
      self.methodeCalculTaille=methodeCalculTaille
      self.formatSortie=formatSortie
      self.valSup=valSup
      self.valMin=valMin
      self.structure=structure

  def __convert__(self,valeur):
    # Attention ne verifie pas grand chose
    if type(valeur) != types.ListType :
      return None
    return valeur

  def info(self):
      return "Matrice %s x %s" % (self.nbLigs, self.nbCols)

      __repr__=info
      __str__=info


#CONTEXT.debug = 1
JdC = JDC_CATA ( code = 'PSEN',
                 execmodul = None,
                 regles = ( AU_MOINS_UN ( 'PARAMETRES_PSSE' ),
                            AU_MOINS_UN ( 'DIRECTORY' ),
                            AU_MOINS_UN ( 'DISTRIBUTION' ),
                            AU_MOINS_UN ( 'SIMULATION' ),
                            AU_PLUS_UN ( 'PARAMETRES_PSSE' ),
                            AU_PLUS_UN ( 'DIRECTORY' ),
                            AU_PLUS_UN ( 'SIMULATION' ),
                            AU_PLUS_UN ( 'CORRELATION' ),
                            ),
                 ) # Fin JDC_CATA


# --------------------------------------------------
# fin entete
# --------------------------------------------------

MONGENER =  OPER ( nom = "MONGENER",
            sd_prod = sd_generateur,
            UIinfo = {"groupes": ("CACHE")},
            op = None,
            fr = "Generateur",
            ang = "Generator",

  ID = SIMP ( statut = 'o', typ = "TXM", fr = "num bus", ang = "num bus",),
)
MACHARGE =  OPER ( nom = "MACHARGE",
            sd_prod = sd_charge,
            UIinfo = {"groupes": ("CACHE")},
            op = None,
            fr = "Charge",
            ang = "Load",

  ID = SIMP ( statut = 'o', typ = "TXM", fr = "nom charge", ang = "load name",),
)
MALIGNE =  OPER ( nom = "MALIGNE",
            sd_prod = sd_ligne,
            UIinfo = {"groupes": ("CACHE")},
            op = None,
            fr = "Ligne",
            ang = "Line",

  ID = SIMP ( statut = 'o', typ = "TXM", fr = "nom ligne", ang = "line name",),
)
MONTRANSFO =  OPER ( nom = "MONTRANSFO",
            sd_prod = sd_transfo,
            UIinfo = {"groupes": ("CACHE")},
            op = None,
            fr = "Transformateur",
            ang = "Transformer",

  ID = SIMP ( statut = 'o', typ = "TXM", fr = "nom transformateur", ang = "transformer name",),
)



PARAMETRES_PSSE = PROC ( nom = "PARAMETRES_PSSE",
             op=None,
             docu = "",
  COUT_COMBUSTIBLE = SIMP ( statut = "o",
                     typ=bool,
                     defaut=True,
                     ),
  COUT_DELESTAGE = SIMP ( statut = "o",
                     typ=bool,
                     defaut=False,
                     ),
  COUT_MVAR = SIMP ( statut = "o",
                     typ=bool,
                     defaut=False,
                    ),
  IMAP = SIMP ( statut = "o",
                     typ='TXM',
                     into=['RateA','RateB','RateC'],
                     defaut=False,
                    ),
  LOCK_TAPS = SIMP ( statut = "o",
                     typ=bool,
                     defaut=True,
                     ),
  P_MIN= SIMP ( statut = "o",
                     typ=bool,
                     defaut=True,
                     ),
)

SIMULATION = PROC ( nom = "SIMULATION",
             op = None,
             docu = "",
  regles             =(EXCLUS('NUMBER_PACKAGE','CONVERGENCE'),),
               
  SIZE_PACKAGE = SIMP ( statut = "o",
                 typ = "I",
                 val_min=10,
                 defaut=100,
                 ),
  NUMBER_PACKAGE = SIMP ( statut = "f",
                 typ = "I",
                 val_min=1,
                 ),
  CONVERGENCE = SIMP ( statut = "f",
                 typ="I",
                 into=[1],
                ),

##  STUDY = SIMP ( statut = "o",
##                 typ = "TXM",
##                 into = ( 'N-1', 'Load', 'Wind-1', 'Wind-2', 'PV' ),
##                 max=5,
##                 fr = "Affichage du niveau de wrapper de la bibliotheque Open TURNS",
##                 ang = "Open TURNS library debug level print",
##                 ), 
) 



#================================
# Importation des fichiers csv N-1
#================================

N_1_LINES = PROC( nom="N_1_LINES",
                     op = None,
                     docu = "",
                     fr = "N-1 lignes",
                     ang = "N-1 lines",

  FileName = SIMP ( statut = "o",
                    typ = ('Fichier', 'Wrapper Files (*.csv);;All Files (*)',),
                    fr = "chemin du fichier csv des probabilites des defauts lignes",
                    ang = "csv file path with probabilities of line outages",
                    ),
              )

N_1_TRANSFORMERS = PROC( nom="N_1_TRANSFORMERS",
                     op = None,
                     docu = "",
                     fr = "N-1 transformateurs",
                     ang = "N-1 transformers",

  FileName = SIMP ( statut = "o",
                    typ = ('Fichier', 'Wrapper Files (*.csv);;All Files (*)',),
                    fr = "chemin du fichier csv des probabilites des defauts transformateur",
                    ang = "csv file path with probabilities of transformer outages",
                    ),
              )
N_1_GENERATORS = PROC( nom="N_1_GENERATORS",
                     op = None,
                     docu = "",
                     fr = "N-1 generateurs",
                     ang = "N-1 generators",

  FileName = SIMP ( statut = "o",
                    typ = ('Fichier', 'Wrapper Files (*.csv);;All Files (*)',),
                    fr = "chemin du fichier csv des probabilites des defauts generateurs",
                    ang = "csv file path with probabilities of generator outages",
                    ),
              )
N_1_LOADS = PROC( nom="N_1_LOADS",
                     op = None,
                     docu = "",
                     fr = "N-1 charges",
                     ang = "N-1 loads",

  FileName = SIMP ( statut = "o",
                    typ = ('Fichier', 'Wrapper Files (*.csv);;All Files (*)',),
                    fr = "chemin du fichier csv des probabilites des defauts charges",
                    ang = "csv file path with probabilities of load outages",
                    ),
              )

#================================
LINE_LIST = PROC (nom='LINE_LIST',
                op = None,
                docu = "",
                fr = "PN",
                ang = "PN",

                       Values = SIMP ( statut = 'o',
                                       typ = Tuple(2),
                                       max = '**', 
                                       fr = "Liste de couples : largeur de classe, hauteur de classe",
                                       ang = "Class bandwidth, class height couple list",
                                       validators=VerifTypeTuple((sd_ligne,'R')),
                                       ),
)
#================================
# Definition des LOIS
#================================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)
DISTRIBUTION = OPER ( nom = "DISTRIBUTION",
                      sd_prod = loi,
                      op = 68,
                      fr = "Definitions des lois marginales utilisees par les variables d'entree", 

#====
# Choisir generateur ou charge
#====

##  TypeMachine = SIMP ( statut='o', typ='TXM',
##                      into = ('charge','vent1','vent2','pv','N-1',),
##                      ),
  Activated = SIMP ( statut='o', typ=bool, defaut=True),
  ComponentType = SIMP (statut='o', typ='TXM',
                      into = ('Generator','Load','Line','Transformer'),),
  b_gener = BLOC (condition = "ComponentType == 'Generator'",
        Generator   = SIMP(statut='o',typ=sd_generateur,max="**", homo="SansOrdreNiDoublon"),),
  b_charge = BLOC (condition = "ComponentType == 'Load'",
        Load       = SIMP(statut='o',typ=sd_charge,max="**", homo="SansOrdreNiDoublon"),),
  b_ligne = BLOC (condition = "ComponentType == 'Line'",
        Line   = SIMP(statut='o',typ=sd_ligne,max="**", homo="SansOrdreNiDoublon"),),
  b_transfo = BLOC (condition = "ComponentType == 'Transformer'",
        Transformer       = SIMP(statut='o',typ=sd_transfo,max="**", homo="SansOrdreNiDoublon"),),
##  b_gener = BLOC (condition = "TypeComposant == 'Generateur'",
##        Generateur   = SIMP(statut='o',typ=sd_generateur,max="**", homo="SansOrdreNiDoublon"),),
##  b_charge = BLOC (condition = "TypeComposant == 'Charge'",
##        charge       = SIMP(statut='o',typ=sd_charge,max="**", homo="SansOrdreNiDoublon"),),  
                      
#====
# Type de distribution
#====

  Kind = SIMP ( statut = "o", typ = "TXM",
                into = ( "NonParametrique", 
                         #"Beta",
                         "Exponential",
                         #"Gamma",
                         #"Geometric",
                         #"Gumbel",
                         "Histogram",
                         #"Laplace",
                         #"Logistic",
                         #"LogNormal",
                         #"MultiNomial",
                         #"NonCentralStudent",
                         "Normal",
                         #"Poisson",
                         #"Rayleigh",
                         #"Student",
                         "PDF_from_file",
                         #"Triangular",
                         "TruncatedNormal",
                         "Uniform",
                         "UserDefined",
                         "Weibull",
                         ),
                fr = "Choix du type de la loi marginale",
                ang = "1D marginal distribution",
                ),

                      
#====
# Definition des parametres selon le type de la loi
#====

  NONPARAM = BLOC ( condition = " Kind in ( 'NonParametrique', ) ",
             
  FileName = SIMP ( statut = "o",
                    typ = ('Fichier', 'Wrapper Files (*.csv);;All Files (*)',),
                    fr = "Nom du modele physique",
                    ang = "Physical model identifier",
                    ),
              ),

#  BETA = BLOC ( condition = " Kind in ( 'Beta', ) ",
#
#                  Settings = SIMP ( statut = "o",
#                                       typ = "TXM",
#                                       max = 1,
#                                       into = ( "RT", "MuSigma" ),
#                                       defaut = "RT",
#                                       fr = "Parametrage de la loi beta",
#                                       ang = "Beta distribution parameter set",
#                                       ),
#
#                  RT_Parameters = BLOC ( condition = " Settings in ( 'RT', ) ",
#
#                                      R = SIMP ( statut = "o",
#                                                 typ = "R",
#                                                 max = 1,
#                                                 val_min = 0.,
#                                                 fr = "Parametre R de la loi | R > 0",
#                                                 ang = "R parameter | R > 0",
#                                                 ),
#
#                                      # T > R
#                                      T = SIMP ( statut = "o",
#                                                 typ = "R",
#                                                 max = 1,
#                                                 val_min = 0.,
#                                                 fr = "Parametre T de la loi | T > R",
#                                                 ang = "T parameter | T > R",
#                                                 ),
#
#                                      ), # Fin BLOC RT_Parameters
#
#
#                  MuSigma_Parameters = BLOC ( condition = " Settings in ( 'MuSigma', ) ",
#
#                                      Mu = SIMP ( statut = "o",
#                                                  typ = "R",
#                                                  max = 1,
#                                                  fr = "Moyenne de la loi",
#                                                  ang = "Mean value",
#                                                  ),
#
#                                      Sigma = SIMP ( statut = "o",
#                                                     typ = "R",
#                                                     max = 1,
#                                                     val_min = 0.,
#                                                     fr = "Ecart type de la loi",
#                                                     ang = "Standard deviation",
#                                                     ),
#
#                                      ), # Fin BLOC MuSigma_Parameters
#
#
#                  A = SIMP ( statut = "o",
#                             typ = "R",
#                             max = 1,
#                             fr = "Borne inferieure du support de la loi",
#                             ang = "Support lower bound",
#                             ),
#
#                  # B > A
#                  B = SIMP ( statut = "o",
#                             typ = "R",
#                             max = 1,
#                             fr = "Borne superieure du support de la loi",
#                             ang = "Support upper bound",
#                             ),
#
#  ), # Fin BLOC BETA



  EXPONENTIAL = BLOC ( condition = " Kind in ( 'Exponential', ) ",

                         Lambda = SIMP ( statut = "o",
                                         typ = "R",
                                         max = 1,
                                         val_min = 0.,
                                         fr = "Parametre Lambda | Lambda > 0",
                                         ang = "Lambda parameter | Lambda > 0",
                                         ),

                         Gamma = SIMP ( statut = "o",
                                        typ = "R",
                                        max = 1,
                                        fr = "Borne inferieure du support de la loi",
                                        ang = "Support lower bound",
                                        ),

  ), # Fin BLOC EXPONENTIAL



#  GAMMA = BLOC ( condition = " Kind in ( 'Gamma', ) ",
#
#                   Settings = SIMP ( statut = "o",
#                                        typ = "TXM",
#                                        max = 1,
#                                        into = ( "KLambda", "MuSigma" ),
#                                        defaut = "KLambda",
#                                        fr = "Parametrage de la loi gamma",
#                                        ang = "Gamma distribution parameter set",
#                                        ),
#
#                   KLambda_Parameters = BLOC ( condition = " Settings in ( 'KLambda', ) ",
#
#                                       K = SIMP ( statut = "o",
#                                                  typ = "R",
#                                                  max = 1,
#                                                  val_min = 0.,
#                                                  fr = "Parametre K de la loi | K > 0",
#                                                  ang = "K parameter | K > 0",
#                                                  ),
#
#                                       Lambda = SIMP ( statut = "o",
#                                                       typ = "R",
#                                                       max = 1,
#                                                       val_min = 0.,
#                                                       fr = "Parametre Lambda de la loi | Lambda > 0",
#                                                       ang = "Lambda parameter | Lambda > 0",
#                                                       ),
#
#                                       ), # Fin BLOC KLambda_Parameters
#
#
#                   MuSigma_Parameters = BLOC ( condition = " Settings in ( 'MuSigma', ) ",
#
#                                       Mu = SIMP ( statut = "o",
#                                                   typ = "R",
#                                                   max = 1,
#                                                   fr = "Moyenne de la loi",
#                                                   ang = "Mean value",
#                                                   ),
#
#                                       Sigma = SIMP ( statut = "o",
#                                                      typ = "R",
#                                                      max = 1,
#                                                      val_min = 0.,
#                                                      fr = "Ecart type de la loi",
#                                                      ang = "Standard deviation",
#                                                      ),
#
#                                       ), # Fin BLOC MuSigma_Parameters
#
#                   Gamma = SIMP ( statut = "o",
#                                  typ = "R",
#                                  max = 1,
#                                  fr = "Borne inferieure du supoport de la loi",
#                                  ang = "Support lower bound",
#                                  ),
#
#
#  ), # Fin BLOC GAMMA


#
#  GEOMETRIC = BLOC ( condition = " Kind in ( 'Geometric', ) ",
#
#                       P = SIMP ( statut = "o",
#                                  typ = "R",
#                                  max = 1,
#                                  val_min = 0.,
#                                  val_max = 1.,
#                                  fr = "Parametre P | 0 < P < 1",
#                                  ang = "P parameter | 0 < P < 1",
#                                  ),
#
#  ), # Fin BLOC GEOMETRIC
#
#
#
#  GUMBEL = BLOC ( condition = " Kind in ( 'Gumbel', ) ",
#
#                    Settings = SIMP ( statut = "o",
#                                         typ = "TXM",
#                                         max = 1,
#                                         into = ( "AlphaBeta", "MuSigma" ),
#                                         defaut = "AlphaBeta",
#                                         fr = "Parametrage de la loi gumbel",
#                                         ang = "Gumbel distribution parameter set",
#                                         ),
#
#                    AlphaBeta_Parameters = BLOC ( condition = " Settings in ( 'AlphaBeta', ) ",
#
#                                        Alpha = SIMP ( statut = "o",
#                                                       typ = "R",
#                                                       max = 1,
#                                                       val_min = 0.,
#                                                       fr = "Parametre Alpha de la loi | Alpha > 0",
#                                                       ang = "Alpha parameter | Alpha > 0",
#                                                       ),
#
#                                        Beta = SIMP ( statut = "o",
#                                                      typ = "R",
#                                                      max = 1,
#                                                      fr = "Parametre Beta de la loi",
#                                                      ang = "Beta parameter",
#                                                      ),
#
#                                        ), # Fin BLOC AlphaBeta_Parameters
#
#
#                    MuSigma_Parameters = BLOC ( condition = " Settings in ( 'MuSigma', ) ",
#
#                                        Mu = SIMP ( statut = "o",
#                                                    typ = "R",
#                                                    max = 1,
#                                                    fr = "Moyenne de la loi",
#                                                    ang = "Mean value",
#                                                    ),
#
#                                        Sigma = SIMP ( statut = "o",
#                                                       typ = "R",
#                                                       max = 1,
#                                                       val_min = 0.,
#                                                       fr = "Ecart type de la loi",
#                                                       ang = "Standard deviation",
#                                                       ),
#
#                                        ), # Fin BLOC MuSigma_Parameters
#
#  ), # Fin BLOC GUMBEL



  HISTOGRAM = BLOC ( condition = " Kind in ( 'Histogram', ) ",

                       First = SIMP ( statut = "o",
                                    typ = "R",
                                    max = 1,
                                    fr = "Borne inferieure du supoport de la loi",
                                    ang = "Support lower bound",
                                    ),

                       # Il faut definir une collection de couples ( x,p ) 
                       Values = SIMP ( statut = 'o',
                                       typ = Tuple(2),
                                       max = '**', 
                                       fr = "Liste de couples : largeur de classe, hauteur de classe",
                                       ang = "Class bandwidth, class height couple list",
                                       validators=VerifTypeTuple(('R','R')),
                                       ),


  ), # Fin BLOC HISTOGRAM



#  LAPLACE = BLOC ( condition = " Kind in ( 'Laplace', ) ",
#
#                   Lambda = SIMP ( statut = "o",
#                                   typ = "R",
#                                   max = 1,
#                                   val_min = 0.,
#                                   fr = "Parametre Lambda | Lambda > 0",
#                                   ang = "Lambda parameter | Lambda > 0",
#                                   ),
#                   
#                   Mu = SIMP ( statut = "o",
#                               typ = "R",
#                               max = 1,
#                               fr = "Moyenne de la loi",
#                               ang = "Mean value",
#                              ),
#
#  ), # Fin BLOC LAPLACE
#
#  LOGNORMAL = BLOC ( condition = " Kind in ( 'LogNormal', ) ",
#
#                     Settings = SIMP ( statut = "o",
#                                       typ = "TXM",
#                                       max = 1,
#                                       into = ( "MuSigmaLog", "MuSigma", "MuSigmaOverMu" ),
#                                       defaut = "MuSigmaLog",
#                                       fr = "Parametrage de la loi lognormale",
#                                       ang = "Lognormal distribution parameter set",
#                                       ),
#
#                     MuSigma_Parameters = BLOC ( condition = " Settings in ( 'MuSigma', ) ",
#
#                                                 Mu = SIMP ( statut = "o",
#                                                             typ = "R",
#                                                             max = 1,
#                                                             fr = "Moyenne de la loi",
#                                                             ang = "Mean value",
#                                                             ),
#
#                                                 Sigma = SIMP ( statut = "o",
#                                                                typ = "R",
#                                                                max = 1,
#                                                                val_min = 0.,
#                                                                fr = "Ecart type de la loi",
#                                                                ang = "Standard deviation",
#                                                                ),
#
#                                                 ), # Fin BLOC MuSigma_Parameters
#
#                     MuSigmaOverMu_Parameters = BLOC ( condition = " Settings in ( 'MuSigmaOverMu', ) ",
#
#                                                 Mu = SIMP ( statut = "o",
#                                                             typ = "R",
#                                                             max = 1,
#                                                             fr = "Moyenne de la loi",
#                                                             ang = "Mean value",
#                                                             ),
#
#                                                 SigmaOverMu = SIMP ( statut = "o",
#                                                                typ = "R",
#                                                                max = 1,
#                                                                val_min = 0.,
#                                                                fr = "Rapport ecart type / moyenne de la loi",
#                                                                ang = "Standard deviation / mean value ratio",
#                                                                ),
#
#                                                 ), # Fin BLOC MuSigmaOverMu_Parameters
#
#                     MuSigmaLog_Parameters = BLOC ( condition = " Settings in ( 'MuSigmaLog', ) ",
#
#                                                    MuLog = SIMP ( statut = "o",
#                                                                   typ = "R",
#                                                                   max = 1,
#                                                                   fr = "Moyenne du log",
#                                                                   ang = "Log mean value",
#                                                                   ),
#
#                                                    SigmaLog = SIMP ( statut = "o",
#                                                                      typ = "R",
#                                                                      max = 1,
#                                                                      val_min = 0.,
#                                                                      fr = "Ecart type du log",
#                                                                      ang = "Log standard deviation",
#                                                                      ),
#                                            
#                                                    ), # Fin BLOC MuSigmaLog_Parameters
#
#                     Gamma = SIMP ( statut = "o",
#                                    typ = "R",
#                                    max = 1,
#                                    fr = "Borne inferieure du support de la loi",
#                                    ang = "Support lower bound",
#                                    ),
#
#   ), # Fin BLOC LOGNORMAL
#
#
#
#   LOGISTIC = BLOC ( condition = " Kind in ( 'Logistic', ) ",
#
#                       Alpha = SIMP ( statut = "o",
#                                      typ = "R",
#                                      max = 1,
#                                      fr = "Borne inferieure du supoport de la loi",
#                                      ang = "Support lower bound",
#                                      ),
#
#                       Beta = SIMP ( statut = "o",
#                                     typ = "R",
#                                     max = 1,
#                                     val_min = 0.,
#                                     fr = "Parametre Beta de la loi | Beta > 0",
#                                     ang = "Beta parameter | Beta > 0",
#                                     ),
#
#   ), # Fin BLOC LOGISTIC
#
#
#
#   MULTINOMIAL = BLOC ( condition = " Kind in ( 'MultiNomial', ) ",
#                         
#                         N = SIMP ( statut = "o",
#                                    typ = "I",
#                                    max = 1,
#                                    fr = "Parametre N de la loi | N > 0",
#                                    ang = "N parameter | N > 0",
#                                    ),
#
#                       # Il faut definir une collection de couples ( x,p ) 
#                       Values = SIMP ( statut = 'o',
#                                       typ = "R",
#                                       max = '**',
#                                       fr = "Liste de probabilités",
#                                       ang = "Probability list",
#                                       validators=VerifTypeTuple(('R','R')),
#                                       ),
#
#   ), # Fin BLOC MULTINOMIAL
#
#
#  NONCENTRALSTUDENT = BLOC ( condition = " Kind in ( 'NonCentralStudent', ) ",
#
#                   Nu = SIMP ( statut = "o",
#                               typ = "R",
#                               max = 1,
#                               fr = "Parametre Nu de la loi | Nu > 0",
#                               ang = "Nu parameter | Nu > 0",
#                              ),
#
#                   Delta = SIMP ( statut = "o",
#                                  typ = "R",
#                                  max = 1,
#                                  fr = "Parametre Delta de la loi | Delta > 0",
#                                  ang = "Delta parameter | Delta > 0",
#                                  ),
#                   
#                   Gamma = SIMP ( statut = "o",
#                                  typ = "R",
#                                  max = 1,
#                                  fr = "Parametre Gamma de centrage de la loi",
#                                  ang = "Gamma parameter",
#                                  ),
#
#  ), # Fin BLOC NONCENTRALSTUDENT


   NORMAL = BLOC ( condition = " Kind in ( 'Normal', ) ",

                    Mu = SIMP ( statut = "o",
                                typ = "R",
                                max = 1,
                                fr = "Moyenne de la loi",
                                ang = "Mean value",
                                ),

                   Sigma = SIMP ( statut = "o",
                                  typ = "R",
                                  max = 1,
                                  val_min = 0.,
                                  fr = "Ecart type de la loi",
                                  ang = "Standard deviation",
                                  ),

   ), # Fin BLOC NORMAL


#
#   POISSON = BLOC ( condition = " Kind in ( 'Poisson', ) ",
#
#                     Lambda = SIMP ( statut = "o",
#                                     typ = "R",
#                                     max = 1,
#                                     val_min = 0.,
#                                     fr = "Parametre Lambda de la loi | Lambda > 0",
#                                     ang = "Lambda parameter | Lambda > 0",
#                                     ),
#
#   ), # Fin BLOC POISSON
#
#
#
#  RAYLEIGH = BLOC ( condition = " Kind in ( 'Rayleigh', ) ",
#
#                   Sigma = SIMP ( statut = "o",
#                                  typ = "R",
#                                  max = 1,
#                                  fr = "Parametre Sigma de la loi | Sigma > 0",
#                                  ang = "Sigma parameter | Sigma > 0",
#                                  ),
#
#                   Gamma = SIMP ( statut = "o",
#                                  typ = "R",
#                                  max = 1,
#                                  fr = "Borne inferieure du support de la loi",
#                                  ang = "Support lower bound",
#                                  ),
# ), # Fin BLOC RAYLEIGH

  PDF = BLOC ( condition = " Kind in ( 'PDF_from_file', ) ",
             
  FileName = SIMP ( statut = "o",
                    typ = ('Fichier', 'Wrapper Files (*.csv);;All Files (*)',),
                    fr = "Nom du modele physique",
                    ang = "Physical model identifier",
                    ),
              ),
              
#   STUDENT = BLOC ( condition = " Kind in ( 'Student', ) ",
#
#                     Mu = SIMP ( statut = "o",
#                                 typ = "R",
#                                 max = 1,
#                                 fr = "Parametre Mu de la loi",
#                                 ang = "Mu parameter",
#                                 ),
#
#                     Nu = SIMP ( statut = "o",
#                                 typ = "R",
#                                 max = 1,
#                                 val_min = 2.,
#                                 fr = "Parametre Nu de la loi | Nu > 2",
#                                 ang = "Nu parameter | Nu > 2",
#                                 ),
#
#                   Sigma = SIMP ( statut = "o",
#                                  typ = "R",
#                                  max = 1,
#                                  fr = "Parametre Sigma de la loi",
#                                  ang = "Sigma parameter",
#                                  ),
#
#   ), # Fin BLOC STUDENT
#
#
#
#   TRIANGULAR = BLOC ( condition = " Kind in ( 'Triangular', ) ",
#
#                         A = SIMP ( statut = "o",
#                                    typ = "R",
#                                    max = 1,
#                                    fr = "Borne inferieure du support de la loi | A < M < B",
#                                    ang = "Support lower bound | A < M < B",
#                                    ),
#
#                         M = SIMP ( statut = "o",
#                                    typ = "R",
#                                    max = 1,
#                                    fr = "Mode de la loi | A < M < B",
#                                    ang = "Mode | A < M < B",
#                                    ),
#
#                         B = SIMP ( statut = "o",
#                                    typ = "R",
#                                    max = 1,
#                                    fr = "Borne superieure du support de la loi | A < M < B",
#                                    ang = "Support upper bound | A < M < B",
#                                    ),
#
#   ), # Fin BLOC TRIANGULAR
#
#

   TRUNCATEDNORMAL = BLOC ( condition = " Kind in ( 'TruncatedNormal', ) ",

                             MuN = SIMP ( statut = "o",
                                          typ = "R",
                                          max = 1,
                                          fr = "Moyenne de la loi Normale non tronquée",
                                          ang = "Mean value of the associated non truncated normal distribution",
                                          ),

                             SigmaN = SIMP ( statut = "o",
                                             typ = "R",
                                             max = 1,
                                             val_min = 0.,
                                             fr = "Ecart-type de la loi Normale non tronquée",
                                             ang = "Standard deviation of the associated non truncated normal distribution",
                                             ),

                             A = SIMP ( statut = "o",
                                        typ = "R",
                                        max = 1,
                                        fr = "Borne inferieure de la loi | A < B",
                                        ang = "Lower bound | A < B",
                                        ),

                             B = SIMP ( statut = "o",
                                        typ = "R",
                                        max = 1,
                                        fr = "Borne superieure de la loi | A < B",
                                        ang = "Upper bound | A < B",
                                        ),

   ), # Fin BLOC TRUNCATEDNORMAL



   UNIFORM = BLOC ( condition = " Kind in ( 'Uniform', ) ",

                     A = SIMP ( statut = "o",
                                typ = "R",
                                max = 1,
                                fr = "Borne inferieure du support de la loi | A < B",
                                ang = "Support lower bound | A < B",
                                ),

                     B = SIMP ( statut = "o",
                                typ = "R",
                                max = 1,
                                fr = "Borne superieure du support de la loi | A < B",
                                ang = "Support upper bound | A < B",
                                ),

   ), # Fin BLOC UNIFORM



   USERDEFINED = BLOC ( condition = " Kind in ( 'UserDefined', ) ",

                           # Il faut definir une collection de couples ( x,p ) 
                         Fichier = SIMP ( statut = 'o',
                                         typ =( 'Fichier', 'CSV (*.csv);;All Files (*)',),
                                      
                                         ),

   ), # Fin BLOC USERDEFINED



   WEIBULL = BLOC ( condition = " Kind in ( 'Weibull', ) ",

                     Settings = SIMP ( statut = "o",
                                          typ = "TXM",
                                          max = 1,
                                          into = ( "AlphaBeta", "MuSigma" ),
                                          defaut = "AlphaBeta",
                                          fr = "Parametrage de la loi weibull",
                                          ang = "Weibull distribution parameter set",
                                          ),

                     AlphaBeta_Parameters = BLOC ( condition = " Settings in ( 'AlphaBeta', ) ",

                                         Alpha = SIMP ( statut = "o",
                                                        typ = "R",
                                                        max = 1,
                                                        val_min = 0.,
                                                        fr = "Parametre Alpha de la loi | Alpha > 0",
                                                        ang = "Alpha parameter | Alpha > 0",
                                                        ),

                                         Beta = SIMP ( statut = "o",
                                                       typ = "R",
                                                       max = 1,
                                                       val_min = 0.,
                                                       fr = "Parametre Beta de la loi | Beta > 0",
                                                       ang = "Beta parameter | Beta > 0",
                                                       ),

                                         ), # Fin BLOC AlphaBeta_Parameters


                     MuSigma_Parameters = BLOC ( condition = " Settings in ( 'MuSigma', ) ",

                                         Mu = SIMP ( statut = "o",
                                                     typ = "R",
                                                     max = 1,
                                                     fr = "Moyenne de la loi",
                                                     ang = "Mean value",
                                                     ),

                                         Sigma = SIMP ( statut = "o",
                                                        typ = "R",
                                                        max = 1,
                                                        val_min = 0.,
                                                        fr = "Ecart type de la loi",
                                                        ang = "Standard deviation",
                                                        ),

                                         ), # Fin BLOC MuSigma_Parameters

                     Gamma = SIMP ( statut = "o",
                                    typ = "R",
                                    max = 1,
                                    fr = "Borne inferieure du support de la loi",
                                    ang = "Support lower bound",
                                    ),

    ), # Fin BLOC WEIBULL

) 



#================================
# Definition du modele physique
#================================



CORRELATION = PROC ( nom = 'CORRELATION',
                     op = None,
                     docu = "",
                     fr = "Correlation entre variables",
                     ang = "Variable correlation",

####  Copula = SIMP ( statut = "o",
####                  typ = 'TXM',
####                  into = ( "Independent", "Normal" ),
####                  defaut = "Independent",
####                  fr = "Type de la copule",
####                  ang = "Copula kind",
####                  ),
##
## # Matrix = BLOC ( condition = "Copula in ( 'Normal', )",
##                  
    CorrelationMatrix = SIMP ( statut = "o",
                               typ = Matrice(nbLigs=None,
                                             nbCols=None,
                                             methodeCalculTaille='NbDeDistributions',
                                             structure="symetrique"),
                               fr = "Matrice de correlation entre les variables d'entree",
                               ang = "Correlation matrix for input variables",
                               ),
##  #), # Fin BLOC Matrix
##
##
) 

DIRECTORY = MACRO ( nom = 'DIRECTORY',
        op=None,
        fr = "Chargement des generateurs et des charges",
        ang = "Physical model wrapper load",
                sd_prod = opsPSEN.INCLUDE,
                op_init = opsPSEN.INCLUDE_context,
                #sd_prod=None,
                fichier_ini = 1,
        
        sav_file=SIMP(statut="o", typ = ('Fichier', 'Wrapper Files (*.sav);;All Files (*)',),),
        results_folder=SIMP(statut="o",typ='Repertoire'),
        #lines_file=SIMP(statut="o" ,typ = ('Fichier', 'Wrapper Files (*.csv);;All Files (*)',),),
        #groups_file=SIMP(statut="o", typ = ('Fichier', 'Wrapper Files (*.csv);;All Files (*)',),),
        #generationsystem_file=SIMP(statut="o" ,typ = ('Fichier', 'Wrapper Files (*.csv);;All Files (*)',),),        
        PSSE_path=SIMP(statut="o",typ='Repertoire'),
) 

Classement_Commandes_Ds_Arbre=('DIRECTORY','DISTRIBUTION','CORRELATION')


