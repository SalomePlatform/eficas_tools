
# -*- coding: latin-1 -*-

from Accas import *
class DateJJMMAAAA:
  def __init__(self):
    self.ntuple=3

  def __convert__(self,valeur):
    if type(valeur) == types.StringType: return None
    if len(valeur) != self.ntuple: return None
    return valeur

  def info(self):
    return "Date : jj/mm/aaaa "

  __repr__=info
  __str__=info

class grma(GEOM):
  pass

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



JdC = JDC_CATA (code = 'KHIONE',
                execmodul = None,
                )
# =======================================================================
# Catalog entry for the MAP function : c_pre_interfaceBody_mesh
# =======================================================================

VERSION_CATALOGUE="TRUNK_20201028"
# -----------------------------------------------------------------------
COMPUTATION_ENVIRONMENT = PROC(nom= "COMPUTATION_ENVIRONMENT",op = None,
# -----------------------------------------------------------------------
#   -----------------------------------
    INPUT = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        DATA = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            STEERING_FILE = SIMP(statut ='f',
#           -----------------------------------
                typ = ('Fichier','All Files (*)'),
                defaut = '',
                fr = """Nom du fichier contenant les parametres du calcul
des glaces a realiser. Donne par l''utilisateur.""",
                ang = """Name of the file containing parameters of the ice
computation. Provided by the user.""",
            ),
#           -----------------------------------
            FORTRAN_FILE = SIMP(statut ='f',
#           -----------------------------------
                typ = ('Fichier','All Files (*)'), max='**',
                defaut = '',
                fr = """Nom du fichier ou repertoire FORTRAN a soumettre,
contenant les sous-programmes specifiques au modele.""",
                ang = """Name of the FORTRAN file or directory to be submitted,
including specific subroutines of the model.""",
            ),
#           -----------------------------------
            BOUNDARY_CONDITIONS_FILE = SIMP(statut ='f',
#           -----------------------------------
                typ = ('Fichier','All Files (*)'), max='**',
                fr = """Nom du fichier contenant les types de conditions aux limites.
Ce fichier est rempli de facon automatique par le mailleur au moyen de
couleurs affectees aux noeuds des frontieres du domaine de calcul.""",
                ang = """Name of the file containing the types of boundary conditions.
This file is filled automatically by the mesh generator through
colours that are assigned to the boundary nodes.""",
            ),
#           -----------------------------------
            GEOMETRY_FILE = SIMP(statut ='f',
#           -----------------------------------
                typ = ('Fichier','All Files (*)'), max='**',
                defaut = '',
                fr = """Fichier de geometrie, identique a celui de \telemac{2D}.""",
                ang = """Geometry file identical to the \telemac{2D} one.""",
            ),
#           -----------------------------------
            GEOMETRY_FILE_FORMAT = SIMP(statut ='f',
#           -----------------------------------
                typ = 'TXM',
                into = ['SERAFIN','SERAFIND','MED'],
                defaut = 'SERAFIN',
                fr = """Format du \telkey{FICHIER DE GEOMETRIE}.
Les valeurs possibles sont :
\begin{itemize}
\item SERAFIN : format standard simple precision pour \tel ;
\item SERAFIND: format standard double precision pour \tel ;
\item MED     : format MED double precision base sur HDF5.
\end{itemize}""",
                ang = """Format of the \telkey{GEOMETRY FILE}.
Possible choices are:
\begin{itemize}
\item SERAFIN : classical single precision format in \tel,
\item SERAFIND: classical double precision format in \tel,
\item MED     : MED double precision format based on HDF5.
\end{itemize}""",
            ),
#           -----------------------------------
            REFERENCE_FILE = SIMP(statut ='f',
#           -----------------------------------
                typ = ('Fichier','All Files (*)'), max='**',
                defaut = '',
                fr = """Nom du fichier de resultats de reference pour la validation.
Si \telkey{VALIDATION} = OUI, les resultats du calcul vont etre
compares aux valeurs contenues dans ce fichier.
La comparaison est effectuee par le sous-programme \telfile{VALIDA}.""",
                ang = """Name of the binary-coded result file used to validate the compuation.
If \telkey{VALIDATION} = YES, the results of the computation will be
compared with the values of this file.
The comparison is done by the subroutine \telfile{BIEF\_VALIDA}.""",
            ),
#           -----------------------------------
            REFERENCE_FILE_FORMAT = SIMP(statut ='o',
#           -----------------------------------
                typ = 'TXM',
                into = ['SERAFIN','SERAFIND','MED'],
                defaut = 'SERAFIN',
                fr = """Format du \telkey{FICHIER DE REFERENCE}.
Les valeurs possibles sont :
\begin{itemize}
\item SERAFIN : format standard simple precision pour \tel ;
\item SERAFIND: format standard double precision pour \tel ;
\item MED     : format MED double precision base sur HDF5.
\end{itemize}""",
                ang = """Format of the \telkey{REFERENCE FILE}.
Possible choices are:
\begin{itemize}
\item SERAFIN : classical single precision format in \tel,
\item SERAFIND: classical double precision format in \tel,
\item MED     : MED double precision format based on HDF5.
\end{itemize}""",
            ),
#           -----------------------------------
            VALIDATION = SIMP(statut ='f',
#           -----------------------------------
                typ = bool,
                defaut = False,
                fr = """Option utilisee principalement pour le dossier de validation.
Si ce mot-cle vaut OUI, les resultats du calcul vont alors etre
compares aux valeurs du \telkey{FICHIER DE REFERENCE}.
Le \telkey{FICHIER DE REFERENCE} est alors considere comme une
reference a laquelle on va comparer le calcul. La comparaison est
effectuee par le sous-programme \telfile{BIEF\_VALIDA}
qui peut etre une comparaison avec une solution exacte par exemple.""",
                ang = """This option is primarily used for the validation documents.
If this keyword is equal to YES, the \telkey{REFERENCE FILE}
is then considered as a reference which the computation is
going to be compared with.
The \telkey{REFERENCE FILE} is then considered as a reference
which the computation is going to be compared with.
The comparison is done by the subroutine \telfile{BIEF\_VALIDA},
which can be modified so as to include, for example,
a comparison with an exact solution.""",
            ),
        ),
    ),
#   -----------------------------------
    GLOBAL = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        TITLE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'TXM',
            defaut = '',
            fr = """Titre du cas etudie.""",
            ang = """Title of the case being considered.""",
        ),
#       -----------------------------------
        PARALLEL_PROCESSORS = SIMP(statut ='f',
#       -----------------------------------
            typ = 'I',
            defaut = 0,
            fr = """Nombre de processeurs pour la decomposition en parallele:
\begin{itemize}
\item 0 : 1 machine, compilation sans bibliotheque de parallelisme ;
\item 1 : 1 machine, compilation avec bibliotheque de parallelisme ;
\item 2 : 2 processeurs ou machines en parallele etc...
\end{itemize}""",
            ang = """Number of processors for domain partition.
\begin{itemize}
\item 0: 1 machine, compiling without parallel library,
\item 1: 1 machine, compiling with a parallel library,
\item 2: 2 processors or machines in parallel etc...
\end{itemize}""",
        ),
    ),
#   -----------------------------------
    OUTPUT = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        RESULTS = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            RESULTS_FILE = SIMP(statut ='f',
#           -----------------------------------
                typ = ('Fichier','All Files (*)','Sauvegarde'), max='**',
                fr = """Nom du fichier dans lequel seront ecrits les resultats du
calcul avec la periodicite donnee par le mot cle \telkey{PERIODE DE
SORTIES DES GLACES}.""",
                ang = """Name of the file into which the computation results
are written with a periodicity given by the keyword
\telkey{ICE PRINTOUT PERIOD}.""",
            ),
#           -----------------------------------
            RESULTS_FILE_FORMAT = SIMP(statut ='o',
#           -----------------------------------
                typ = 'TXM',
                into = ['SERAFIN','SERAFIND','MED'],
                defaut = 'SERAFIN',
                fr = """Format du \telkey{FICHIER DES RESULTATS}.
Les valeurs possibles sont :
\begin{itemize}
\item SERAFIN : format standard simple precision pour \tel ;
\item SERAFIND: format standard double precision pour \tel ;
\item MED     : format MED double precision base sur HDF5.
\end{itemize}""",
                ang = """Format of the \telkey{RESULTS FILE}. Possible choices are:
\begin{itemize}
\item SERAFIN : classical single precision format in \tel,
\item SERAFIND: classical double precision format in \tel,
\item MED     : MED double precision format based on HDF5.
\end{itemize}""",
            ),
#           -----------------------------------
            VARIABLES_FOR_GRAPHIC_PRINTOUTS = SIMP(statut ='f',
#           -----------------------------------
                typ = 'TXM', max='**',
                into = ["SOLRAD CLEAR SKY","SOLRAD CLOUDY","NET SOLRAD","EFFECTIVE SOLRAD","EVAPO HEAT FLUX","CONDUC HEAT FLUX","PRECIP HEAT FLUX","FRAZIL THETA0","FRAZIL THETA1","REENTRAINMENT","SETTLING VEL.",""SOLID ICE CONC.,"SOLID ICE THICK.","FRAZIL THICKNESS","UNDER ICE THICK.","EQUIV. SURFACE","TOP ICE COVER","BOTTOM ICE COVERM","TOTAL ICE THICK.M ","CARACTERISTIQUES","TOTAL NUMBER OF PARTICLES","TOTAL CONCENTRATION OF FRAZIL","CONCENTRATION OF FRAZIL BY CLASS","PARTICLE NUMBER OF FRAZIL BY CLASS","WATER TEMPERATURE","SALINITY OF WATER"],
                defaut = '',
                fr = """Noms des variables que l''utilisateur veut ecrire dans
le \telkey{FICHIER DES RESULTATS DES GLACES}.
Chaque variable est representee par une lettre.
Le choix des separateurs est libre.""",
                ang = """Names of variables that may be written in the
\telkey{ICE RESULTS FILE}.
Every variable is represented by a group of letters with
any separator between them , ; or blank.""",
            ),
#           -----------------------------------
            GRAPHIC_PRINTOUT_PERIOD = SIMP(statut ='f',
#           -----------------------------------
                typ = 'I',
                defaut = [1],
                fr = """Determine la periode en nombre de pas de temps d''impression des
\telkey{VARIABLES POUR LES SORTIES GRAPHIQUES}
(voir ce mot-cle) dans le \telkey{FICHIER DES RESULTATS}.""",
                ang = """Determines, in number of time steps, the printout period for the
\telkey{VARIABLES FOR GRAPHIC PRINTOUTS}
in the \telkey{RESULTS FILE}.""",
            ),
#           -----------------------------------
            CLOGGING_RESULTS_FILE = SIMP(statut ='f',
#           -----------------------------------
                typ = ('Fichier','All Files (*)','Sauvegarde'),
                defaut = '',
                fr = """Fichier ASCII de resultats de la glace accumulee aux prises d eau.""",
                ang = """ASCII file of results for clogged ice parameters at water intakes.""",
            ),
        ),
#       -----------------------------------
        LISTING = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            VARIABLES_TO_BE_PRINTED = SIMP(statut ='o',
#           -----------------------------------
                typ = 'TXM', max='**',
                into = ['TO BE EDITED'],
                defaut = '',
                fr = """Mot cle necessaire mais qui ne fait rien.""",
                ang = """Necessary keyword but does not do much.""",
            ),
#           -----------------------------------
            LISTING_PRINTOUT_PERIOD = SIMP(statut ='f',
#           -----------------------------------
                typ = 'I',
                defaut = [1],
                fr = """Determine la periode en nombre de pas de temps d''impression des
\telkey{VARIABLES A IMPRIMER} (voir ce mot-cle).
Pour la mise au point, il faut
savoir que la sortie des resultats est effectuee systematiquement sur le
listing (CAS.SORTIE sur station de travail).""",
                ang = """Determines, in number of time steps, the printout period of the
\telkey{VARIABLES TO BE PRINTED}.
The results are systematically printed out on
the listing file (file CAS.SORTIE at the workstation).""",
            ),
#           -----------------------------------
            MASS_BALANCE = SIMP(statut ='f',
#           -----------------------------------
                typ = bool,
                defaut = False,
                fr = """Determine si l''on effectue ou non le bilan de masse
sur le domaine.""",
                ang = """Determines whether a check of the mass-balance over
the domain is done or not.""",
            ),
        ),
    ),
#   -----------------------------------
    RESTART = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        PREVIOUS_ICE_COVER_COMPUTATION_FILE = SIMP(statut ='o',
#       -----------------------------------
            typ = ('Fichier','All Files (*)'),
            defaut = '',
            fr = """Nom d''un fichier contenant les resultats d''un calcul de couvert de
glace precedent realise sur le meme maillage et dont le dernier pas de
temps enregistre va fournir les conditions initiales pour une suite de
de calcul.""",
            ang = """Name of a file containing the results of an earlier ice cover
computation which was made on the same mesh. The last recorded time
step will provide the initial conditions for the new computation.""",
        ),
#       -----------------------------------
        PREVIOUS_ICE_COVER_COMPUTATION_FILE_FORMAT = SIMP(statut ='o',
#       -----------------------------------
            typ = 'TXM',
            into = ['SERAFIN','SERAFIND'],
            defaut = 'SERAFIN',
            fr = """Format du fichier de resultats du calcul de couvert de glace precedent.
Les valeurs possibles sont :
\begin{itemize}
\item SERAFIN : format standard simple precision pour \tel ;
\item SERAFIND: format standard double precision pour \tel.
\end{itemize}""",
            ang = """Previous ice cover computation results file format.
Possible values are:
\begin{itemize}
\item SERAFIN : classical single precision format in \tel,
\item SERAFIND: classical double precision format in \tel.
\end{itemize}""",
        ),
#       -----------------------------------
        PREVIOUS_ICE_BLOCKS_COMPUTATION_FILE = SIMP(statut ='o',
#       -----------------------------------
            typ = ('Fichier','All Files (*)'),
            defaut = '',
            fr = """Nom d''un fichier contenant les resultats d''un calcul Lagrangien de
couvert de blocs de glace precedent et dont le dernier pas de
temps enregistre va fournir les conditions initiales pour une suite de
de calcul.""",
            ang = """Name of a file containing the results of ice blocks from an earlier
Lagrangian computation. The last recorded time step will provide the
initial conditions for the new computation.""",
        ),
#       -----------------------------------
        PREVIOUS_ICE_BLOCKS_COMPUTATION_FILE_FORMAT = SIMP(statut ='o',
#       -----------------------------------
            typ = 'TXM',
            into = ['SERAFIN','SERAFIND'],
            defaut = 'SERAFIN',
            fr = """Format du fichier de resultats Lagrangien du calcul de couvert
de glace precedent.
Les valeurs possibles sont :
\begin{itemize}
\item UNKNOWN : format non-defini simple precision pour \tel ;
\item UNKNOWND: format non-defini double precision pour \tel.
\end{itemize}""",
            ang = """Previous ice cover blocks computation results file format.
Possible values are:
\begin{itemize}
\item UNKNOWN : not-yet-defined single precision format in \tel,
\item UNKNOWND: not-yet-defined double precision format in \tel.
\end{itemize}""",
        ),
    ),
#   -----------------------------------
    INITIALIZATION = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        INITIAL_CONDITIONS = SIMP(statut ='f',
#       -----------------------------------
            typ = 'TXM',
            into = ['"WITHOUT ICE COVER"','"CONSTANT ICE COVER"','"SPECIAL"','"PARTICULIERES"','"PARTICULAR"'],
            defaut = 'WITHOUT ICE COVER',
            fr = """Permet de definir les conditions initiales sur le couvert de glaces.
Les valeurs possibles sont :
\begin{itemize}
\item SANS COUVERT DE GLACE ;
\item COUVERT DE GLACE CONSTANT ;
\item PARTICULIERES. Les conditions initiales sur le couvert de glace
doivent etre precisees dans le sous-programme \telfile{CONDICE}.
\end{itemize}""",
            ang = """Makes it possible to define the initial conditions with ice cover.
The possible values are as follows:
\begin{itemize}
\item WITHOUT ICE COVER,
\item CONSTANT ICE COVER,
\item SPECIAL. The initial conditions with the water depth should be
stated in the \telfile{CONDICE} subroutine.
\end{itemize}""",
        ),
    ),
)
# -----------------------------------------------------------------------
INTERNAL = PROC(nom= "INTERNAL",op = None,
# -----------------------------------------------------------------------
#   -----------------------------------
    DICTIONARY = SIMP(statut ='f',
#   -----------------------------------
        typ = ('Fichier','All Files (*)'),
        defaut = 'KHIONE.DICO',
        fr = """Dictionnaire des mots cles.""",
        ang = """Key word dictionary.""",
    ),
)
# -----------------------------------------------------------------------
ICE_COVER = PROC(nom= "ICE_COVER",op = None,
# -----------------------------------------------------------------------
#   -----------------------------------
    CRITICAL_VELOCITY_FOR_STATIC_BORDER_ICE = SIMP(statut ='f',
#   -----------------------------------
        typ = 'R',
        defaut = [0.07],
        fr = """""",
        ang = """""",
    ),
#   -----------------------------------
    CRITICAL_VELOCITY_FOR_DYNAMIC_BORDER_ICE = SIMP(statut ='f',
#   -----------------------------------
        typ = 'R',
        defaut = [0.4],
        fr = """""",
        ang = """""",
    ),
#   -----------------------------------
    ICE_COVER_IMPACT_ON_HYDRODYNAMIC = SIMP(statut ='f',
#   -----------------------------------
        typ = bool,
        defaut = [False],
        fr = """Prise en compte de l''impact du couvert de glace sur
l''hydrodynamique.""",
        ang = """Computation of ice cover impact on the hydrodynamic.""",
    ),
#   -----------------------------------
    BORDER_ICE_COVER = SIMP(statut ='f',
#   -----------------------------------
        typ = bool,
        defaut = [False],
        fr = """Prise en compte du calcul de glace de bord statique.""",
        ang = """Computation of border ice cover.""",
    ),
#   -----------------------------------
    PHYSICAL_PARAMETERS = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        CRITICAL_WATER_TEMPERATURE_FOR_STATIC_BORDER_ICE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [-1.1],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        CONCENTRATION_OF_SURFACE_ICE_WHEN_FORMATION = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [1.],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        FRICTION = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            LAW_OF_ICE_COVER_FRICTION = SIMP(statut ='o',
#           -----------------------------------
                typ = 'TXM',
                into = ["NO FRICTION","HAALAND","CHEZY","STRICKLER","MANNING","NIKURADSE"],
                defaut = "MANNING",
                fr = """Selectionne le type de formulation utilisee pour le calcul du
frottement sous le couvert de glace. Les lois possibles sont les
suivantes (cf. Note de principe) :
\begin{itemize}
\item 0 : pas de frottement sur le fond ;
\item 1 : formule de Haaland ;
\item 2 : formule de Chezy ;
\item 3 : formule de Strickler ;
\item 4 : formule de Manning ;
\item 5 : formule de Nikuradse.
\end{itemize}""",
                ang = """Selects the type of formulation used for the under ice cover friction.
The possible laws are as follows (refer to the Principle note):
\begin{itemize}
\item 0: no friction against bottom,
\item 1: Haaland formula,
\item 2: Chezy formula,
\item 3: Strickler formula,
\item 4: Manning formula,
\item 5: Nikuradse formula.
\end{itemize}""",
            ),
#           -----------------------------------
            FRICTION_COEFFICIENT = SIMP(statut ='o',
#           -----------------------------------
                typ = 'R',
                defaut = 0.04,
                fr = """Fixe la valeur du coefficient de frottement pour la
formulation choisie.
Attention : la signification de ce chiffre varie suivant la formule
choisie :
\begin{itemize}
\item 1 : coefficient lineaire ;
\item 2 : coefficient de Chezy ;
\item 3 : coefficient de Strickler ;
\item 4 : coefficient de Manning ;
\item 5 : hauteur de rugosite de Nikuradse.
\end{itemize}""",
                ang = """Sets the value of the friction coefficient for the selected
formulation. It is noteworthy that the meaning of this figure changes
according to the selected formula (Chezy, Strickler, etc.):
\begin{itemize}
\item 1: linear coefficient,
\item 2: Chezy coefficient,
\item 3: Strickler coefficient,
\item 4: Manning coefficient,
\item 5: Nikuradse grain size.
\end{itemize}""",
            ),
#           -----------------------------------
            MAXIMAL_FRICTION_COEFFICIENT = SIMP(statut ='o',
#           -----------------------------------
                typ = 'R',
                defaut = 0.04,
                fr = """Fixe le coefficient de frottement maximal lorsque la celui-ci depend
de l''epaisseur du couvert de glace.""",
                ang = """Sets the maximal friction coefficient when it depends linearly on the
ice cover thickness.""",
            ),
#           -----------------------------------
            LAW_FOR_FRICTION_COEFFICIENT = SIMP(statut ='o',
#           -----------------------------------
                typ = 'TXM',
                into = ["CONSTANT FRICTION COEF","LINEAR FRICTION COEF"],
                defaut = "CONSTANT FRICTION COEF",
                fr = """Selectionne entre un coefficient de friction constant ou variable
lineairement en fonction de l''epaisseur du couvert de glace.""",
                ang = """Selection between constant friction coefficient of linearly dependant
on ice cover thickness.""",
            ),
#           -----------------------------------
            EQUIVALENT_SURFACE_ICE_THICKNESS = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [0.001],
                fr = """""",
                ang = """""",
            ),
        ),
    ),
#   -----------------------------------
    ICE_DYNAMICS = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        INCLUDE_ICE_DYNAMICS = SIMP(statut ='f',
#       -----------------------------------
            typ = bool,
            defaut = [False],
            fr = """Active les processessus de dynamique des glaces de surfaces.""",
            ang = """Switch the surface ice dynamics processes.""",
        ),
    ),
)
# -----------------------------------------------------------------------
GENERAL = PROC(nom= "GENERAL",op = None,
# -----------------------------------------------------------------------
#   -----------------------------------
    SALINITY = SIMP(statut ='o',
#   -----------------------------------
        typ = bool,
        defaut = [False],
        fr = """Ajoute la salinite et modifie le point de congelation de la glace en
fonction.""",
        ang = """Add salinity tracer and modify freezing point of water accordingly.""",
    ),
#   -----------------------------------
    ENERGY_BALANCE_VERSION = SIMP(statut ='o',
#   -----------------------------------
        typ = 'TXM',
        into = ["SIMPLIFIED ENERGY BALANCE","FULL ENERGY BALANCE"],
        defaut = ["SIMPLIFIED ENERGY BALANCE"],
        fr = """Choix de la version du bilan energetique.""",
        ang = """Choice of the energy balance version.""",
    ),
#   -----------------------------------
    PHYSICAL_PARAMETERS = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        AIR_DENSITY = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = 1.225,
            fr = """Fixe la valeur de la masse volumique de l''air.""",
            ang = """Sets the value of air density.""",
        ),
#       -----------------------------------
        ICE_DENSITY = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = 916.8,
            fr = """Fixe la valeur de la masse volumique de la glace, en kg/m$^3$.""",
            ang = """Sets the value of ice density, in kg/m$^3$.""",
        ),
#       -----------------------------------
        POROSITY_OF_SURFACE_ICE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [0.4],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        WATER_DENSITY = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = 999.972,
            fr = """Fixe la valeur de la masse volumique de l''eau, en kg/m$^3$.""",
            ang = """Sets the value of water density, in kg/m$^3$.""",
        ),
#       -----------------------------------
        KINEMATIC_WATER_VISCOSITY = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = 1.792E-6,
            fr = """Definit la viscosite cinematique de l''eau. En m/s$^2$.""",
            ang = """Specifies the water kinematic viscosity. In m/s$^2$.""",
        ),
    ),
)
# -----------------------------------------------------------------------
THERMAL_BUDGET = PROC(nom= "THERMAL_BUDGET",op = None,
# -----------------------------------------------------------------------
#   -----------------------------------
    HEAT_BUDGET = SIMP(statut ='f',
#   -----------------------------------
        typ = bool,
        defaut = [True ],
        fr = """Prise en compte des echanges thermiques dans le calcul.""",
        ang = """Computation of the thermal exchanges in \khione.""",
    ),
#   -----------------------------------
    PHYSICAL_PARAMETERS = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        WATER_SPECIFIC_HEAT = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [4180.],
            fr = """Fixe la valeur de la chaleur specifique de l eau, en J/kg/K.""",
            ang = """Sets the value of the specific heat of water, in J/kg/K.""",
        ),
#       -----------------------------------
        SPECIFIC_HEAT_OF_ICE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = 2.04E+03,
            fr = """Fixe la valeur de la chaleur specifique de la glace,
en J/kg/K.""",
            ang = """Sets the value of the specific heat of ice,
in J/kg/K.""",
        ),
#       -----------------------------------
        LATENT_HEAT_OF_ICE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = 3.34E5,
            fr = """Fixe la valeur de la chaleur latente de la glace.""",
            ang = """Sets the value of the latent heat of ice.""",
        ),
#       -----------------------------------
        WATER_AIR_HEAT_EXCHANGE_COEFFICIENT = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [20.],
            fr = """Fixe la valeur du coefficient d''echange thermique entre
 l''eau et l''air.""",
            ang = """Sets the heat exchange coefficient between water and air.""",
        ),
    ),
#   -----------------------------------
    CONSTANT = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        WATER_AIR_HEAT_EXCHANGE_CONSTANT = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [50.],
            fr = """Fixe la valeur de la constante d''echange thermique entre
 l''eau et l''air.""",
            ang = """Sets the heat exchange constant between water and air.""",
        ),
#       -----------------------------------
        ICE_AIR_HEAT_EXCHANGE_COEFFICIENT = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [12.189],
            fr = """Fixe la valeur du coefficient d''echange thermique lineaire
 entre la glace et l''air.""",
            ang = """Sets the linearised heat flux exchange coefficient between
 ice and air.""",
        ),
#       -----------------------------------
        ICE_AIR_HEAT_EXCHANGE_CONSTANT = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [32.547],
            fr = """Fixe la valeur de la constante d''echange thermique lineaire
 entre la glace et l''air.""",
            ang = """Sets the linearised heat flux exchange constant between ice and air.""",
        ),
#       -----------------------------------
        CONSTANT_FOR_HEAT_TRANSFER_BETWEEN_TURBULENT_WATER_AND_ICE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [1448.],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        CONSTANT_FOR_HEAT_TRANSFER_FOR_SUPERCOOLED_TURBULENT_FLOW = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [1118.],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        BOLTZMANN_CONSTANT__WM_2K_4_ = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [5.67D-8],
            fr = """""",
            ang = """""",
        ),
    ),
#   -----------------------------------
    CALIBRATION_COEFFICIENT = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        COEFFICIENT_FOR_CALIBRATION_OF_BACK_RADIATION = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [1.],
            fr = """Fixe la valeur du coefficient de calage du flux radiatif
entre l''atmosphere et la surface libre.""",
            ang = """Sets heat flux calibration coefficient for effective back
radiation on the free surface.""",
        ),
#       -----------------------------------
        COEFFICIENT_FOR_CALIBRATION_OF_EVAPORATIVE_HEAT_TRANSFERT = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [1.],
            fr = """Fixe la valeur du coefficient de calage du transfert de chaleur
evaporatif entre l''atmosphere et la surface libre.""",
            ang = """Sets heat flux calibration coefficient for evaporative heat
transfert between air and atmosphere.""",
        ),
#       -----------------------------------
        COEFFICIENT_FOR_CALIBRATION_OF_CONDUCTIVE_HEAT_TRANSFERT = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [1.],
            fr = """Fixe la valeur du coefficient de calage du transfert de chaleur
conductif entre l''atmosphere et la surface libre.""",
            ang = """Sets heat flux calibration coefficient for conductive heat
transfert between air and atmosphere.""",
        ),
#       -----------------------------------
        COEFFICIENT_FOR_CALIBRATION_OF_PRECIPITATION_HEAT_TRANSFERT = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [1.],
            fr = """Fixe la valeur du coefficient de calage du transfert de chaleur
entre l''atmosphere et la surface libre lie aux precipitations.""",
            ang = """Sets heat flux calibration coefficient for precipitation heat
transfert between air and atmosphere.""",
        ),
    ),
#   -----------------------------------
    THERMAL_CONDUCTIVITY = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        THERMAL_CONDUCTIVITY_BETWEEN_WATER_AND_FRAZIL = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [0.56594],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        THERMAL_CONDUCTIVITY_OF_BLACK_ICE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [2.24],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        THERMAL_CONDUCTIVITY_OF_SNOW = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [0.3],
            fr = """""",
            ang = """""",
        ),
    ),
#   -----------------------------------
    TURBULENCE = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        NUSSELT_NUMBER_FOR_HEAT_TRANSFER_BETWEEN_LAMINAR_WATER_AND_ICE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [7.541],
            fr = """""",
            ang = """""",
        ),
    ),
#   -----------------------------------
    METEOROLOGICAL_PROCESSES = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        ALBEDO_OF_ICE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [0.2],
            fr = """Fixe la constante albedo des glaces.""",
            ang = """Sets the albedo of ice.""",
        ),
#       -----------------------------------
        ATMOSPHERE_WATER_EXCHANGE_MODEL = SIMP(statut ='f',
#       -----------------------------------
            typ = 'TXM',
            into = ["LINEARISED FORMULA","MODEL WITH COMPLETE BALANCE"],
            defaut = ["LINEARISED FORMULA"],
            fr = """Choix du modele d echanges entre l eau et l atmosphere.
\begin{itemize}
\item 0: formule linearisee (default) ;
\item 1: modele a bilan complet.
\end{itemize}""",
            ang = """Choice of the atmosphere-water exchange model.
\begin{itemize}
\item 0: linearised formula,
\item 1: model with complete balance.
\end{itemize}""",
        ),
#       -----------------------------------
        WIND = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            HEIGHT_OF_MEASURED_WIND = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [4.5],
                fr = """Fixe la valeur de la hauteur a laquelle le vent est mesure, en metres.""",
                ang = """Sets the height at which the wind is measured, in meters.""",
            ),
        ),
#       -----------------------------------
        SUN = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            RELATIVE_MODEL_ELEVATION_FROM_MEAN_SEA_LEVEL = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [0.],
                fr = """Fixe l''elevation du modele relative au niveau moyen des oceans.""",
                ang = """Sets the relative model elevation from mean sea level.""",
            ),
#           -----------------------------------
            SUN_SET_ANGLE = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [180.],
                fr = """Fixe l''angle du soleil couchant, 180 degres pour l''horizontale.""",
                ang = """Sets the sun set angle, 180 degrees for the horizontal.""",
            ),
#           -----------------------------------
            SUN_RISE_ANGLE = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [0.],
                fr = """Fixe l''angle du soleil levant, 0 degres pour l''horizontale.""",
                ang = """Sets the sun rise angle, 0 degrees for the horizontal.""",
            ),
#           -----------------------------------
            SOLAR_CONSTANT = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [1380.],
                fr = """Fixe la constante solaire.""",
                ang = """Sets the solar constant.
The solar constant, a measure of flux density, is the mean solar
electromagnetic radiation (the solar irradiance) per unit area that
would be incident on a plane perpendicular to the rays, at a distance
of one astronomical unit (AU) from the Sun (roughly the mean distance
from the Sun to the Earth). The solar constant includes all types of
solar radiation, not just the visible light. It is measured by
satellite as being 1.361 kilowatts per square meter (kW/m$^2$) at solar
minimum and approximately 0.1~\% greater (roughly 1.362 kW/m$^2$) at
solar maximum.
The solar "constant" is not a physical constant in scientific
sense; that is, it is not like the Planck constant or the speed of
light, which are absolutely constant in physics. The solar constant is
merely an average of the actually varying value. It has been shown to
vary in the past 400 years over a range of less than 0.2~\%.""",
            ),
        ),
#       -----------------------------------
        AIR = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            DEWPOINT_TEMPERATURE = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [0.],
                fr = """En $^{\circ}$C, temperature de rosee lorsque celle-ci n est pas deja
donnee dans un des fichiers meteo.""",
                ang = """In $^{\circ}$C, dewpoint temperature used when it is not already
provided within one of the meteo files.""",
            ),
#           -----------------------------------
            VISIBILITY = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [1.E13],
                fr = """En metres, visibilite lorsque celle-ci n est pas deja donnee
dans un des fichiers meteo.""",
                ang = """In meters, visibility used when it is not already provided
within one of the meteo files.""",
            ),
        ),
#       -----------------------------------
        POSITION = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            GLOBAL_LONGITUDE__IN_DEGREES = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [75.],
                fr = """Fixe la longitude globale, en degres.""",
                ang = """Sets the global longitude, in degrees.""",
            ),
#           -----------------------------------
            LOCAL_LONGITUDE__IN__DEGREES = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [75.43],
                fr = """Fixe la longitude locale, en degres.""",
                ang = """Sets the local longitude, in degrees.""",
            ),
#           -----------------------------------
            EAST_OR_WEST_LONGITUDE = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [-1.],
                fr = """-1., pour les longitudes ouest; +1. pour les longitude est.""",
                ang = """-1., for west longitudes; +1. for east longitudes""",
            ),
        ),
    ),
)
# -----------------------------------------------------------------------
FRAZIL = PROC(nom= "FRAZIL",op = None,
# -----------------------------------------------------------------------
#   -----------------------------------
    SCHEME_OPTION_FOR_THERMAL_GROWTH = SIMP(statut ='o',
#   -----------------------------------
        typ = 'TXM',
        into = ["EXPLICIT TIME SCHEME","SEMI-IMPLICIT TIME SCHEME"],
        defaut = ["EXPLICIT TIME SCHEME"],
        fr = """Choix du schema d''integration en temps pour le terme source
de croissance thermique de frasil.""",
        ang = """Time integration option for the frazil thermal growth source term.""",
    ),
#   -----------------------------------
    MODEL_FOR_THE_SECONDARY_NUCLEATION = SIMP(statut ='o',
#   -----------------------------------
        typ = 'TXM',
        into = ["NO MODEL","SVENSSON AND OMSTEDT 1994","WANG AND DOERING 2005"],
        defaut = ["SVENSSON AND OMSTEDT 1994"],
        fr = """Choix du modele de nucleation secondaire,
valable uniquement pour le modele multi-classes.""",
        ang = """Choice of the model for secondary nucleation,
only for multi-class model.""",
    ),
#   -----------------------------------
    SECONDARY_NUCLEATION_NMAX_PARAMETER = SIMP(statut ='o',
#   -----------------------------------
        typ = 'R',
        defaut = [1.E3],
        fr = """Choix du parametre NMAX pour la nucleation secondaire.""",
        ang = """Choice of secondary nucleation NMAX parameter.""",
    ),
#   -----------------------------------
    MODEL_FOR_THE_FLOCCULATION_AND_BREAKUP = SIMP(statut ='o',
#   -----------------------------------
        typ = 'TXM',
        into = ["NO MODEL","SVENSSON AND OMSTEDT 1994"],
        defaut = ["SVENSSON AND OMSTEDT 1994"],
        fr = """Choix du modele de floculation et rupture,
valable uniquement pour le modele multi-classes.""",
        ang = """Choice of the model for flocculation and breakup,
only for multi-class model.""",
    ),
#   -----------------------------------
    FLOCCULATION_AFLOC_PARAMETER = SIMP(statut ='o',
#   -----------------------------------
        typ = 'R',
        defaut = [1.E3],
        fr = """Choix du parametre \telfile{AFLOC} pour la floculation.""",
        ang = """Choice of flocculation \telfile{AFLOC} parameter.""",
    ),
#   -----------------------------------
    MODEL_FOR_FRAZIL_SEEDING = SIMP(statut ='o',
#   -----------------------------------
        typ = 'TXM',
        into = ["NO MODEL","MINIMUM CONC. THRESHOLD","CONSTANT SEEDING RATE","BOTH OPTIONS 1 AND 2"],
        defaut = ["MINIMUM CONC. THRESHOLD"],
        fr = """Choix du modele d''ensemencement du frasil.""",
        ang = """Choice of the model for frazil seeding.""",
    ),
#   -----------------------------------
    PHYSICAL_PARAMETERS = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        NUMBER_OF_CLASSES_FOR_SUSPENDED_FRAZIL_ICE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'I',
            defaut = [1],
            fr = """Fixe le nombre de classes de particules de frasil en suspension.""",
            ang = """Sets the number of classes of suspended frazil ice granules.""",
        ),
#       -----------------------------------
        FRAZIL_CRYSTALS_RADIUS = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R', min=0, max='**',
            defaut = [1.E-4],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        FRAZIL_CRYSTALS_DIAMETER_THICKNESS_RATIO = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [10.],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        MODEL_FOR_THE_BUOYANCY_VELOCITY = SIMP(statut ='f',
#       -----------------------------------
            typ = 'TXM',
            into = ["DALY (1984)","HAALAND","GOSIK & OSTERKAMP (1983)"],
            defaut = ["DALY (1984)"],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        FREEZING_POINT_OF_WATER = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [0.],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        CHANNEL_WIDTH_FOR_THE_COMPUTATION_OF_SURFACE_TEMPERATURE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [15.],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        FRAZIL_SEEDING_RATE = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [50.],
            fr = """Nombre de cristaux par unite de volume ajoutees par seconde.""",
            ang = """Number of crystals per unit volume added per second.""",
        ),
#       -----------------------------------
        MINIMUM_NUMBER_OF_FRAZIL_CRYSTALS = SIMP(statut ='f',
#       -----------------------------------
            typ = 'I',
            defaut = [1000],
            fr = """Nombre minimum de cristaux par unite de volume.""",
            ang = """Minimum number of crystals per unit volume.""",
        ),
    ),
#   -----------------------------------
    CALIBRATION_COEFFICIENT = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        SETTLING_COEFFICIENT_OF_FRAZIL_ON_BARS = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [1.],
            fr = """""",
            ang = """""",
        ),
    ),
#   -----------------------------------
    TURBULENCE = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        NUSSELT_NUMBER = SIMP(statut ='f',
#       -----------------------------------
            typ = 'R',
            defaut = [4.],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        MODEL_FOR_THE_NUSSELT_NUMBER = SIMP(statut ='f',
#       -----------------------------------
            typ = 'I',
            defaut = [1],
            fr = """""",
            ang = """""",
        ),
#       -----------------------------------
        MODEL_FOR_ESTIMATION_OF_TURBULENCE_PARAMETERS = SIMP(statut ='o',
#       -----------------------------------
            typ = 'I',
            defaut = [0],
            fr = """\begin{itemize}
\item 0: valeurs constantes fixees par defaut dans le code ;
\item 1: valeurs estimees a partir d''une integration verticale
du modele de longueur de melange ;
\item 2: valeurs calculees et donnees par \telemac{2D}.
\end{itemize}""",
            ang = """\begin{itemize}
\item 0: constant values set in the code,
\item 1: values estimated from vertical integration of a mixed length
model,
\item 2: values computed and given by \telemac{2D}.
\end{itemize}""",
        ),
    ),
#   -----------------------------------
    PRECIPITATION = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        FRAZIL_PRECIPITATION = SIMP(statut ='o',
#       -----------------------------------
            typ = bool,
            defaut = [False],
            fr = """Prise en compte de le precipitation du frasil.""",
            ang = """Computation of the frazil precipitation.""",
        ),
    ),
)
# -----------------------------------------------------------------------
CLOGGING = PROC(nom= "CLOGGING",op = None,
# -----------------------------------------------------------------------
#   -----------------------------------
    CLOGGING_ON_BARS = SIMP(statut ='f',
#   -----------------------------------
        typ = bool,
        defaut = [False],
        fr = """Prise en compte de l''impact du colmatage sur les grilles.""",
        ang = """Computation of clogging on grid.""",
    ),
#   -----------------------------------
    PHYSICAL_PARAMETERS = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        GLACE = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            POROSITY_OF_ACCUMULATED_ICE = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [0.67],
                fr = """""",
                ang = """""",
            ),
#           -----------------------------------
            ANGLE_OF_ACCUMULATED_ICE = SIMP(statut ='f',
#           -----------------------------------
                typ = 'R',
                defaut = [35.],
                fr = """""",
                ang = """""",
            ),
        ),
#       -----------------------------------
        GRID = FACT(statut='f',
#       -----------------------------------
#           -----------------------------------
            PHYSICAL_CHARACTERISTICS_OF_THE_INTAKE_RACK = SIMP(statut ='o',
#           -----------------------------------
                typ = 'R', min= 4, max= 4,
                defaut = [0.06,0.01,0.06,0.01],
                fr = """Caracteristiques des barres verticales et horizontales, dans l ordre :
\begin{itemize}
\item 1 : distance entre les centres des barres transversales ;
\item 2 : diametre des barres transversales ;
\item 3 : distance verticale entre les centres des barres verticales ;
\item 4 : diametre des barres verticales.
\end{itemize}
Un diametre de zero pour un certain groupe de barres entrainera la
 supression des barres de ce groupe.""",
                ang = """Characteristics of vertical and transverse bars, in order of
appearance:
\begin{itemize}
\item 1: distance between the centre of the transverse bars,
\item 2: diameter of the transverse bars,
\item 3: distance between the centre of the vertical bars,
\item 4: diameter of the vertical bars.
\end{itemize}
A zero diameter for one particular set of bars will result in not
 having those bars on the rack.""",
            ),
        ),
    ),
#   -----------------------------------
    BOUNDARIES_CONDITION = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        CLOGGED_BOUNDARY_NUMBERS = SIMP(statut ='f',
#       -----------------------------------
            typ = 'I',
            defaut = 0,
            fr = """Liste des numeros de frontieres liquides ou des grilles de prises
d''eau sont presentes.""",
            ang = """List of liquid boundary numbers where intake racks are present.""",
        ),
#       -----------------------------------
        CLOGGED_SECTIONS = SIMP(statut ='f',
#       -----------------------------------
            typ = 'I',
            defaut = 0,
            fr = """Liste des noeuds composant les sections sur lequelles
on a une grille potentiellement colmatee, vont par paire :
sec1\_depart;sec1\_arrivee;sec2\_depart;sec2\_arrivee;...""",
            ang = """List of nodes on which the sections represent
a clogged rack, goes by couple:
sec1\_start;sec1\_end;sec2\_start;sec2\_end;...""",
        ),
    ),
)
# -----------------------------------------------------------------------
NUMERICAL_PARAMETERS = PROC(nom= "NUMERICAL_PARAMETERS",op = None,
# -----------------------------------------------------------------------
#   -----------------------------------
    AUTOMATIC_DIFFERENTIATION = FACT(statut='f',
#   -----------------------------------
#       -----------------------------------
        AD_NUMBER_OF_DERIVATIVES = SIMP(statut ='o',
#       -----------------------------------
            typ = 'I',
            defaut = 0,
            fr = """Definit le nombre de derivees utilisateurs, dans le cadre
de la differentiation algorithmique.""",
            ang = """Defines the number of user derivatives, within the framework
of the algorithmic differentiation.""",
        ),
#       -----------------------------------
        AD_NAMES_OF_DERIVATIVES = SIMP(statut ='o',
#       -----------------------------------
            typ = 'TXM', min= 2, max= 2,
            fr = """Noms des derivees utilisateurs en 32 caracteres,
16 pour le nom, 16 pour l''unite.""",
            ang = """Name of user derivatives in 32 characters,
16 for the name, 16 for the unit.""",
        ),
    ),
)
TEXTE_NEW_JDC = "\
"
Ordre_Des_Commandes = (
'COMPUTATION_ENVIRONMENT',
'INTERNAL',
'ICE_COVER',
'GENERAL',
'THERMAL_BUDGET',
'FRAZIL',
'CLOGGING',
'NUMERICAL_PARAMETERS')
try:
    import TelApy
    source = "eficas"
except Exception as excpt:
    source = "Telemac"
enum = source+'.khione_enum_auto'
dicoCasEn = source+'.khione_dicoCasEnToCata'
dicoCasFr = source+'.khione_dicoCasFrToCata'
