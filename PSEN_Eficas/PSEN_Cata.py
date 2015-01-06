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

class loi      ( ASSD ) : pass
class variable ( ASSD ) : pass

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
JdC = JDC_CATA ( code = 'OPENTURNS_STUDY',
                 execmodul = None,
##                 regles = ( AU_MOINS_UN ( 'CRITERIA' ),
##                            AU_MOINS_UN ( 'MODEL' ),
##                            AVANT ( ('DISTRIBUTION', 'MODEL'), 'VARIABLE' ),
#                            A_CLASSER ( 'VARIABLE',                'CORRELATION' ),
#                            A_CLASSER ( 'VARIABLE',                'CRITERIA' ),
#                            A_CLASSER ( 'CORRELATION',             'CRITERIA' ),
                            #),
                 ) # Fin JDC_CATA


# --------------------------------------------------
# fin entete
# --------------------------------------------------

SIMULATION = PROC ( nom = "SIMULATION",
             op = None,
             docu = "",
               
  SAMPLE = SIMP ( statut = "o",
                 typ = "R",
                 val_min=0,
                  
                 ),
               
  STUDY = SIMP ( statut = "o",
                 typ = "TXM",
                 into = ( 'N-1', 'Load', 'Wind-1', 'Wind-2', 'PV' ),
                 max=5,
                 fr = "Affichage du niveau de wrapper de la bibliotheque Open TURNS",
                 ang = "Open TURNS library debug level print",
                 ), 
) 


OPF_Parameters = PROC ( nom = "OPF_Parameters",
             op = None,
             docu = "",
               
  Minimize_fuel_cost = SIMP ( statut = "o",
                 typ = "TXM",
                 into=('True','False'),
                 defaut='False',
                 fr="Choix cout fuel"
                 ),
  Minimize_adj_bus_shunt = SIMP ( statut = "o",
                 typ = "TXM",
                 into=('True','False'),
                 defaut='False',
                 fr="Choix minimize bus shunts"
                 ),
  Minimize_adj_bus_loads = SIMP ( statut = "o",
                 typ = "TXM",
                 into=('True','False'),
                 defaut='False',
                 fr="Choix minimize bus loads"
                 ),

)

PSSe_Irate = PROC ( nom = "PSSe_Irate",
             op = None,
             docu = "",
               
  Rate_A = SIMP ( statut = "o",
                 typ = "TXM",
                 into=('True','False'),
                 defaut='False',
                 fr="Choix rate A"
                 ),
  Rate_B = SIMP ( statut = "o",
                 typ = "TXM",
                 into=('True','False'),
                 defaut='False',
                 fr="Choix rate B"
                 ),
  Rate_C = SIMP ( statut = "o",
                 typ = "TXM",
                 into=('True','False'),
                 defaut='False',
                 fr="Choix rate C"
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
# Type de distribution
#====

  Kind = SIMP ( statut = "o", typ = "TXM",
                into = ( "Beta",
                         "Exponential",
                         "Gamma",
                         "Geometric",
                         "Gumbel",
                         "Histogram",
                         "Laplace",
                         "Logistic",
                         "LogNormal",
                         "MultiNomial",
                         "NonCentralStudent",
                         "Normal",
                         "Poisson",
                         "Rayleigh",
                         "Student",
                         "Triangular",
                         "TruncatedNormal",
                         "Uniform",
                         "UserDefined",
                         "Weibull",
                         ),
                fr = "Choix du type de la loi marginale",
                ang = "1D marginal distribution",
                ),
  Type_Model = SIMP ( statut='o', typ='TXM',
                      into = ('type_1','type_2','type_3','type_4',
                              ),
                      ),

#====
# Definition des parametres selon le type de la loi
#====

  BETA = BLOC ( condition = " Kind in ( 'Beta', ) ",

                  Settings = SIMP ( statut = "o",
                                       typ = "TXM",
                                       max = 1,
                                       into = ( "RT", "MuSigma" ),
                                       defaut = "RT",
                                       fr = "Parametrage de la loi beta",
                                       ang = "Beta distribution parameter set",
                                       ),

                  RT_Parameters = BLOC ( condition = " Settings in ( 'RT', ) ",

                                      R = SIMP ( statut = "o",
                                                 typ = "R",
                                                 max = 1,
                                                 val_min = 0.,
                                                 fr = "Parametre R de la loi | R > 0",
                                                 ang = "R parameter | R > 0",
                                                 ),

                                      # T > R
                                      T = SIMP ( statut = "o",
                                                 typ = "R",
                                                 max = 1,
                                                 val_min = 0.,
                                                 fr = "Parametre T de la loi | T > R",
                                                 ang = "T parameter | T > R",
                                                 ),

                                      ), # Fin BLOC RT_Parameters


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


                  A = SIMP ( statut = "o",
                             typ = "R",
                             max = 1,
                             fr = "Borne inferieure du support de la loi",
                             ang = "Support lower bound",
                             ),

                  # B > A
                  B = SIMP ( statut = "o",
                             typ = "R",
                             max = 1,
                             fr = "Borne superieure du support de la loi",
                             ang = "Support upper bound",
                             ),

  ), # Fin BLOC BETA



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



  GAMMA = BLOC ( condition = " Kind in ( 'Gamma', ) ",

                   Settings = SIMP ( statut = "o",
                                        typ = "TXM",
                                        max = 1,
                                        into = ( "KLambda", "MuSigma" ),
                                        defaut = "KLambda",
                                        fr = "Parametrage de la loi gamma",
                                        ang = "Gamma distribution parameter set",
                                        ),

                   KLambda_Parameters = BLOC ( condition = " Settings in ( 'KLambda', ) ",

                                       K = SIMP ( statut = "o",
                                                  typ = "R",
                                                  max = 1,
                                                  val_min = 0.,
                                                  fr = "Parametre K de la loi | K > 0",
                                                  ang = "K parameter | K > 0",
                                                  ),

                                       Lambda = SIMP ( statut = "o",
                                                       typ = "R",
                                                       max = 1,
                                                       val_min = 0.,
                                                       fr = "Parametre Lambda de la loi | Lambda > 0",
                                                       ang = "Lambda parameter | Lambda > 0",
                                                       ),

                                       ), # Fin BLOC KLambda_Parameters


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
                                  fr = "Borne inferieure du supoport de la loi",
                                  ang = "Support lower bound",
                                  ),


  ), # Fin BLOC GAMMA



  GEOMETRIC = BLOC ( condition = " Kind in ( 'Geometric', ) ",

                       P = SIMP ( statut = "o",
                                  typ = "R",
                                  max = 1,
                                  val_min = 0.,
                                  val_max = 1.,
                                  fr = "Parametre P | 0 < P < 1",
                                  ang = "P parameter | 0 < P < 1",
                                  ),

  ), # Fin BLOC GEOMETRIC



  GUMBEL = BLOC ( condition = " Kind in ( 'Gumbel', ) ",

                    Settings = SIMP ( statut = "o",
                                         typ = "TXM",
                                         max = 1,
                                         into = ( "AlphaBeta", "MuSigma" ),
                                         defaut = "AlphaBeta",
                                         fr = "Parametrage de la loi gumbel",
                                         ang = "Gumbel distribution parameter set",
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
                                                      fr = "Parametre Beta de la loi",
                                                      ang = "Beta parameter",
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

  ), # Fin BLOC GUMBEL



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



  LAPLACE = BLOC ( condition = " Kind in ( 'Laplace', ) ",

                   Lambda = SIMP ( statut = "o",
                                   typ = "R",
                                   max = 1,
                                   val_min = 0.,
                                   fr = "Parametre Lambda | Lambda > 0",
                                   ang = "Lambda parameter | Lambda > 0",
                                   ),
                   
                   Mu = SIMP ( statut = "o",
                               typ = "R",
                               max = 1,
                               fr = "Moyenne de la loi",
                               ang = "Mean value",
                              ),

  ), # Fin BLOC LAPLACE

  LOGNORMAL = BLOC ( condition = " Kind in ( 'LogNormal', ) ",

                     Settings = SIMP ( statut = "o",
                                       typ = "TXM",
                                       max = 1,
                                       into = ( "MuSigmaLog", "MuSigma", "MuSigmaOverMu" ),
                                       defaut = "MuSigmaLog",
                                       fr = "Parametrage de la loi lognormale",
                                       ang = "Lognormal distribution parameter set",
                                       ),

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

                     MuSigmaOverMu_Parameters = BLOC ( condition = " Settings in ( 'MuSigmaOverMu', ) ",

                                                 Mu = SIMP ( statut = "o",
                                                             typ = "R",
                                                             max = 1,
                                                             fr = "Moyenne de la loi",
                                                             ang = "Mean value",
                                                             ),

                                                 SigmaOverMu = SIMP ( statut = "o",
                                                                typ = "R",
                                                                max = 1,
                                                                val_min = 0.,
                                                                fr = "Rapport ecart type / moyenne de la loi",
                                                                ang = "Standard deviation / mean value ratio",
                                                                ),

                                                 ), # Fin BLOC MuSigmaOverMu_Parameters

                     MuSigmaLog_Parameters = BLOC ( condition = " Settings in ( 'MuSigmaLog', ) ",

                                                    MuLog = SIMP ( statut = "o",
                                                                   typ = "R",
                                                                   max = 1,
                                                                   fr = "Moyenne du log",
                                                                   ang = "Log mean value",
                                                                   ),

                                                    SigmaLog = SIMP ( statut = "o",
                                                                      typ = "R",
                                                                      max = 1,
                                                                      val_min = 0.,
                                                                      fr = "Ecart type du log",
                                                                      ang = "Log standard deviation",
                                                                      ),
                                            
                                                    ), # Fin BLOC MuSigmaLog_Parameters

                     Gamma = SIMP ( statut = "o",
                                    typ = "R",
                                    max = 1,
                                    fr = "Borne inferieure du support de la loi",
                                    ang = "Support lower bound",
                                    ),

   ), # Fin BLOC LOGNORMAL



   LOGISTIC = BLOC ( condition = " Kind in ( 'Logistic', ) ",

                       Alpha = SIMP ( statut = "o",
                                      typ = "R",
                                      max = 1,
                                      fr = "Borne inferieure du supoport de la loi",
                                      ang = "Support lower bound",
                                      ),

                       Beta = SIMP ( statut = "o",
                                     typ = "R",
                                     max = 1,
                                     val_min = 0.,
                                     fr = "Parametre Beta de la loi | Beta > 0",
                                     ang = "Beta parameter | Beta > 0",
                                     ),

   ), # Fin BLOC LOGISTIC



   MULTINOMIAL = BLOC ( condition = " Kind in ( 'MultiNomial', ) ",
                         
                         N = SIMP ( statut = "o",
                                    typ = "I",
                                    max = 1,
                                    fr = "Parametre N de la loi | N > 0",
                                    ang = "N parameter | N > 0",
                                    ),

                       # Il faut definir une collection de couples ( x,p ) 
                       Values = SIMP ( statut = 'o',
                                       typ = "R",
                                       max = '**',
                                       fr = "Liste de probabilités",
                                       ang = "Probability list",
                                       validators=VerifTypeTuple(('R','R')),
                                       ),

   ), # Fin BLOC MULTINOMIAL


  NONCENTRALSTUDENT = BLOC ( condition = " Kind in ( 'NonCentralStudent', ) ",

                   Nu = SIMP ( statut = "o",
                               typ = "R",
                               max = 1,
                               fr = "Parametre Nu de la loi | Nu > 0",
                               ang = "Nu parameter | Nu > 0",
                              ),

                   Delta = SIMP ( statut = "o",
                                  typ = "R",
                                  max = 1,
                                  fr = "Parametre Delta de la loi | Delta > 0",
                                  ang = "Delta parameter | Delta > 0",
                                  ),
                   
                   Gamma = SIMP ( statut = "o",
                                  typ = "R",
                                  max = 1,
                                  fr = "Parametre Gamma de centrage de la loi",
                                  ang = "Gamma parameter",
                                  ),

  ), # Fin BLOC NONCENTRALSTUDENT


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



   POISSON = BLOC ( condition = " Kind in ( 'Poisson', ) ",

                     Lambda = SIMP ( statut = "o",
                                     typ = "R",
                                     max = 1,
                                     val_min = 0.,
                                     fr = "Parametre Lambda de la loi | Lambda > 0",
                                     ang = "Lambda parameter | Lambda > 0",
                                     ),

   ), # Fin BLOC POISSON



  RAYLEIGH = BLOC ( condition = " Kind in ( 'Rayleigh', ) ",

                   Sigma = SIMP ( statut = "o",
                                  typ = "R",
                                  max = 1,
                                  fr = "Parametre Sigma de la loi | Sigma > 0",
                                  ang = "Sigma parameter | Sigma > 0",
                                  ),

                   Gamma = SIMP ( statut = "o",
                                  typ = "R",
                                  max = 1,
                                  fr = "Borne inferieure du support de la loi",
                                  ang = "Support lower bound",
                                  ),
 ), # Fin BLOC RAYLEIGH


   STUDENT = BLOC ( condition = " Kind in ( 'Student', ) ",

                     Mu = SIMP ( statut = "o",
                                 typ = "R",
                                 max = 1,
                                 fr = "Parametre Mu de la loi",
                                 ang = "Mu parameter",
                                 ),

                     Nu = SIMP ( statut = "o",
                                 typ = "R",
                                 max = 1,
                                 val_min = 2.,
                                 fr = "Parametre Nu de la loi | Nu > 2",
                                 ang = "Nu parameter | Nu > 2",
                                 ),

                   Sigma = SIMP ( statut = "o",
                                  typ = "R",
                                  max = 1,
                                  fr = "Parametre Sigma de la loi",
                                  ang = "Sigma parameter",
                                  ),

   ), # Fin BLOC STUDENT



   TRIANGULAR = BLOC ( condition = " Kind in ( 'Triangular', ) ",

                         A = SIMP ( statut = "o",
                                    typ = "R",
                                    max = 1,
                                    fr = "Borne inferieure du support de la loi | A < M < B",
                                    ang = "Support lower bound | A < M < B",
                                    ),

                         M = SIMP ( statut = "o",
                                    typ = "R",
                                    max = 1,
                                    fr = "Mode de la loi | A < M < B",
                                    ang = "Mode | A < M < B",
                                    ),

                         B = SIMP ( statut = "o",
                                    typ = "R",
                                    max = 1,
                                    fr = "Borne superieure du support de la loi | A < M < B",
                                    ang = "Support upper bound | A < M < B",
                                    ),

   ), # Fin BLOC TRIANGULAR



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











