# coding: utf-8
# PNPNPNPN

from Accas import *
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



JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
# ======================================================================
# Catalog entry for the MAP function : c_pre_interfaceBody_mesh
# ======================================================================
INITIALIZATION=PROC(nom="INITIALIZATION",op=None,
Control_Of_Limits = SIMP( statut='o',typ='bool',
    defaut=False ,
    fr = 'UTILISER AVEC LE MOT-CLE : VALEURS LIMITES, LE PROGRAMME SARRETE SI LES LIMITES SUR U,V,H OU T SONT DEPASSEES',
    ang= 'USE WITH THE KEY-WORD : LIMIT VALUES, THE PROGRAM IS STOPPED IF THE LIMITS ON U,V,H, OR T ARE TRESPASSED',
     ),

Limit_Values = SIMP( statut='o',typ='R',
    defaut=(-1000.0, 9000.0, -1000.0, 1000.0, -1000.0, 1000.0, -1000.0, 1000.0) ,
    max=8 ,
    fr = 'Utilise avec le mot-cle CONTROLE DES LIMITES  valeurs mini et maxi acceptables pour H,U,V et T dans lordre suivant : min(H) max(H) min(U) max(U) min(V) max(V) min(T) max(T)',
    ang= 'To be used with the key-word CONTROL OF LIMITS min and max acceptable values for H,U,V et T in the following order   : min(H) max(H) min(U) max(U) min(V) max(V) min(T) max(T)',
     ),

Number_Of_Time_Steps = SIMP( statut='o',typ='I',
    defaut=1 ,
    fr = 'Definit le nombre de pas de temps effectues lors de lexecution du code.',
    ang= 'Specifies the number of time steps performed when running the code.',
     ),

Psi_Scheme_Option = SIMP( statut='o',typ='I',
    defaut=1 ,
    fr = '1: explicite 2: predicteur-correcteur',
    ang= '1: explicit 2: predictor-corrector',
     ),

Type_Of_Advection = SIMP( statut='o',typ='I',
    defaut=(1, 5, 1, 1) ,
    max=4 ,
   into =('1="CHARACTERISTICS"', '2="SUPG"', '3="CONSERVATIVE N-SCHEME"', '4="CONSERVATIVE N-SCHEME"', '5="CONSERVATIVE PSI-SCHEME"', '6="NON CONSERVATIVE PSI SCHEME"', '7="IMPLICIT NON CONSERVATIVE N SCHEME"', '13="EDGE-BASED N-SCHEME"', '14="EDGE-BASED N-SCHEME"'),
    fr = 'Choix du schema de convection pour chaque variable ces coefficients sont respectivement appliques a 1) U et V     2) H     3) T     4) K ET EPSILON 1 : caracteristiques sur h 2 : SUPG 3 : Schema N conservatif 4 : Schema N conservatif    5 : Schema PSI conservatif 6 : Schema PSI non conservatif 7 : schema N implicite non conservatif 13 : Schema N par segment 14 : Schema N par segment Second integer must be 5',
    ang= 'Choice of advection schemes for every variable These coefficients are applied respectively to 1) U et V     2) H     3) T     4) K and EPSILON 1: characteristics 2: SUPG 3: Conservative N-scheme  4: Conservative N-scheme  5: Conservative PSI-scheme  6 : Non conservative PSI scheme 7 : Implicit non conservative N scheme 13 : Edge-based N-scheme 14 : Edge-based N-scheme Second integer must be 5',
     ),

Preconditioning = SIMP( statut='o',typ='I',
    defaut=2 ,
   into =('2="diagonal"', '0="no preconditioning"', '3="diagonal condensee"', '7="crout"', '11="gauss-seidel"', '14="diagonal and crout"', '21="diagonal condensed and crout"'),
    fr = 'Permet de preconditionner le systeme de letape de propagation afin daccelerer la convergence lors de sa resolution.  - 0 : pas de preconditionnement, - 2 : preconditionnement diagonal.  - 3 : preconditionnement diagonal-bloc - 7 : preconditionnement de Crout par element ou segment -11 : preconditionnement de Gauss-Seidel par element ou segment Certains preconditionnements sont cumulables (les diagonaux 2 ou 3 avec les autres) Pour cette raison on ne retient que les nombres premiers pour designer les preconditionnements. Si lon souhaite en cumuler plusieurs on formera le produit des options correspondantes.',
    ang= 'Choice of the preconditioning in the propagation step linear system that the convergence is speeded up when it is being solved.  0: no preconditioning 2: diagonal preconditioning 3: diagonal preconditioning with the condensed matrix 7: Crouts preconditioning per element or segment 11: Gauss-Seidels preconditioning per element or segment Some operations (either 2 or 3 diagonal preconditioning) can be performed concurrently with the others.  Only prime numbers are therefore kept to denote the preconditioning operations. When several of them are to be performed concurrently, the product of relevant options shall be made.',
     ),

Maximum_Number_Of_Iterations_For_Solver = SIMP( statut='o',typ='I',
    defaut=100 ,
    fr = 'Les algorithmes utilises pour la resolution de letape de propagation etant iteratifs, il est necessaire de limiter le nombre diterations autorisees.  Remarque : un maximum de 40 iterations par pas de temps semble raisonnable.',
    ang= 'Since the algorithms used for solving the propagation step are iterative, the allowed number of iterations should be limited.  NOTE: a maximum number of 40 iterations per time step seems to be reasonable.',
     ),


Maximum_Number_Of_Iterations_For_Diffusion_Of_Tracers = SIMP( statut='o',typ='I',
    defaut=60 ,
    fr = 'Limite le nombre diterations du solveur a chaque pas de temps pour le calcul de la diffusion du traceur.',
    ang= 'Limits the number of solver iterations at each time step for the diffusion of tracer.',
     ),

Solver_For_Diffusion_Of_Tracers = SIMP( statut='o',typ='I',
    defaut=1 ,
   into =('1="conjugate gradient"', '2="conjugate residual"', '3="conjugate gradient on a normal equation"', '4="minimum error"', '5="squared conjugate gradient"', '6="cgstab"', '7="gmres (see option for the solver for tracer diffusion)"', '8="direct"'),
    fr = '1 : gradient conjugue 2 : residu conjugue 3 : gradient conjugue sur equation normale 4 : erreur minimale 5 : gradient conjugue carre',
    ang= '1 : conjugate gradient 2 : conjugate gradient 3 :  conjugate gradient on a normal equation 4 : minimum error 5 : squared conjugate gradient 6 : cgstab 7 : gmres (see option for the solver for tracer diffusion) 8 : direct',
     ),



Number_Of_First_Time_Step_For_Graphic_Printouts = SIMP( statut='o',typ='I',
    defaut=0 ,
    fr = 'Determine le nombre de pas de temps a partir duquel debute lecriture des resultats dans le FICHIER DES RESULTATS.',
    ang= 'Determines the number of time steps after which the results are first written into the RESULTS FILE.',
     ),

Number_Of_First_Time_Step_For_Listing_Printouts = SIMP( statut='o',typ='I',
    defaut=0 ,
    fr = 'Determine le nombre de pas de temps a partir duquel debute lecriture des resultats dans le listing.',
    ang= 'Determines the number of time steps after which the results are first written into the listing.',
     ),

Preconditioning_For_Diffusion_Of_Tracers = SIMP( statut='o',typ='I',
    defaut=2 ,
   into =('2="diagonal"', '0="no preconditioning "', '3="diagonal condensed"', '7="crout"', '14="diagonal and crout"', '21="diagonal condensed and crout"'),
    fr = 'Permet de preconditionner le systeme relatif au traceur.  Memes definition et possibilites que pour le mot-cle PRECONDITIONNEMENT.  0 : pas de preconditionnement, 2 : preconditionnement diagonal.  3 : preconditionnement diagonal avec la matrice conde',
    ang= 'Preconditioning of the linear system in the tracer diffusion step.  Same definition and possibilities as for the keyword  PRECONDITIONING 0: no preconditioning 2: diagonal preconditioning 3: diagonal preconditioning with the condensed matrix 7: Crouts preconditioning per element.',
     ),



Number_Of_Drogues = SIMP( statut='o',typ='I',
    defaut=0 ,
    fr = 'Permet deffectuer un suivi de flotteurs',
    ang= 'Number of drogues in the computation.  The user must then fill the subroutine FLOT specifying the coordinates of the starting points, their departure and arrival times.  The trajectory of drogues is recorded in the BINARY RESULTS FILE that must be given in the steering file',
     ),

Printout_Period_For_Drogues = SIMP( statut='o',typ='I',
    defaut=1 ,
    fr = 'Nombre de pas de temps entre 2 sorties de positions de flotteurs dans le fichier des resultats binaire supplementaire N affecte pas la qualite du calcul de la trajectoire',
    ang= 'Number of time steps between 2 outputs of drogues positions in the binary file',
     ),

Number_Of_Lagrangian_Drifts = SIMP( statut='o',typ='I',
    defaut=0 ,
    fr = 'Permet deffectuer simultanement plusieurs calculs de derives lagrangiennes initiees a des pas differents',
    ang= 'Provided for performing several computations of lagrangian drifts starting at different times.  Add A and G in the VARIABLES FOR GRAPHIC PRINTOUTS key-word',
     ),


Solver_Option_For_Tracers_Diffusion = SIMP( statut='o',typ='I',
    defaut=2 ,
    fr = 'si le solveur est GMRES (7) le mot cle est la dimension de lespace de KRILOV (valeurs conseillees entre 2 et 15)',
    ang= 'WHEN GMRES (7) IS CHOSEN, DIMENSION OF THE KRYLOV SPACE TRY VALUES BETWEEN 2 AND 15',
     ),



Initial_Values_Of_Tracers = SIMP( statut='o',typ='R',
    defaut=(0.0, 0.0) ,
    max=2 ,
    fr = 'Fixe la valeur initiale du traceur.',
    ang= 'Sets the initial value of the tracer.',
     ),

Coefficient_For_Diffusion_Of_Tracers = SIMP( statut='o',typ='R',
    defaut=1e-06 ,
    fr = 'Fixe la valeur du coefficient de diffusion du traceur.  Linfluence de ce parametre sur levolution du traceur dans le temps est importante.',
    ang= 'Sets the value of the tracer diffusivity.',
     ),

Accuracy_For_Diffusion_Of_Tracers = SIMP( statut='o',typ='R',
    defaut=1e-06 ,
    fr = 'Fixe la precision demandee pour le calcul de la diffusion du traceur.',
    ang= 'Sets the required accuracy for computing the tracer diffusion.',
     ),

Implicitation_Coefficient_Of_Tracers = SIMP( statut='o',typ='R',
    defaut=0.6 ,
    fr = 'Fixe la valeur du coefficient dimplicitation du traceur',
    ang= 'Sets the value of the implicitation coefficient for the tracer',
     ),

Velocity_Diffusivity = SIMP( statut='o',typ='R',
    defaut=1e-06 ,
    fr = 'Fixe de facon uniforme pour lensemble du domaine, la valeur du coefficient de diffusion de viscosite globale (dynamique + turbulente). Cette valeur peut avoir une influence non negligeable sur la forme et la taille des recirculations.',
    ang= 'Sets, in an even way for the whole domain, the value of the coefficient of global (dynamic+turbulent) viscosity. this value may have a significant effect both on the shapes and sizes of recirculation zones.',
     ),




Mean_Depth_For_Linearization = SIMP( statut='o',typ='R',
    defaut=0.0 ,
    fr = 'Fixe la hauteur deau autour de laquelle seffectue la linearisation lorsque loption PROPAGATION LINEARISEE est choisie.',
    ang= 'Sets the water depth about which the linearization is made when the LINEARIZED PROPAGATION OPTION is selected.',
     ),


Prescribed_Velocities = SIMP( statut='o',typ='R',
    max=2 ,
    fr = 'Valeurs des vitesses imposees aux frontieres liquides entrantes.  Lire la partie du mode demploi consacree aux conditions aux limites',
    ang= 'Values of prescribed velocities at the liquid inflow boundaries.  Refer to the section dealing with the boundary conditions',
     ),

Prescribed_Tracers_Values = SIMP( statut='o',typ='R',
    max=2 ,
    fr = 'Valeurs du traceur imposees aux frontieres liquides entrantes.  Lire la partie du mode demploi consacree aux conditions aux limites',
    ang= 'Tracer values prescribed at the inflow boundaries.  Read the usermanual section dealing with the boundary conditions',
     ),



Values_Of_The_Tracers_At_The_Sources = SIMP( statut='o',typ='R',
    max=2 ,
    fr = 'Valeurs des traceurs a chacune des sources',
    ang= 'Values of the tracers at the sources',
     ),


Upwind_Coefficients = SIMP( statut='o',typ='R',
    defaut=(1.0, 1.0, 1.0, 1) ,
    max=4 ,
    fr = 'Coefficients utilises par la methode S.U.P.G.  ces coefficients sont respectivement appliques a 1) U et V 2) H ou C 3) T 4) K ET EPSILON  ',
    ang= 'Upwind coefficients used by the S.U.P.G. method These coefficients are applied respectively to 1) U and V 2) H  or C 3) T 4) K and epsilon  ',
     ),

Steering_File = SIMP( statut='o',typ='TXM',
    fr = 'Nom du fichier contenant les parametres du calcul a realiser.',
    ang= 'Name of the file containing the parameters of the computation Written by the user.',
     ),

Boundary_Conditions_File = SIMP( statut='o',typ='TXM',
    fr = 'Nom du fichier contenant les types de conditions aux limites.  Ce fichier est rempli de facon automatique par le mailleur au moyen de couleurs affectees aux noeuds des frontieres du domaine de calcul.',
    ang= 'Name of the file containing the types of boundary conditions.  This file is filled automatically by the mesh generator through through colours that are assigned to the boundary nodes.',
     ),

Release = SIMP( statut='o',typ='TXM',
    defaut='V7P0' ,
    fr = 'Numero de version des bibliotheques utilisees par TELEMAC.  SUR UNE STATION DE TRAVAIL 5 versions sont donnees correspondant a : TELEMAC,DAMO,UTILE,BIEF,HP',
    ang= 'version number of the libraries used by TELEMAC.  ON A WORKSTATION 5 numbers are given, corresponding to the libraries called: TELEMAC,DAMO,UTILE,BIEF,HP',
     ),

Account_Number = SIMP( statut='o',typ='TXM',
    fr = 'Numero du compte calcul sur lequel sera impute le cout du calcul.',
    ang= 'Account number to which the cost of computation shall be charged.',
     ),


Destination = SIMP( statut='o',typ='TXM',
    defaut='CHE43A' ,
    fr = 'Nom eventuel dune station de travail sur laquelle lutilisateur desire rediriger le fichier des resultats du calcul.',
    ang= 'Possible name of a workstation to which the user wants to reroute the result file.',
     ),

User_On_Destination = SIMP( statut='o',typ='TXM',
    defaut='JMH' ,
    fr = 'Nom de lUSER de lutilisateur sur la station de travail ou lon desire rediriger le fichier de resultts.',
    ang= 'Users name of USER at the workstation onto which the results file shall desirebly be rerouted.',
     ),

Names_Of_Clandestine_Variables = SIMP( statut='o',typ='TXM',
    max=2 ,
    fr = 'Noms de variables qui ne sont pas utilisees par TELEMAC, mais qui doivent etre conservees lors de son execution.  Ceci peut etre utilise entre autres lors du couplage de TELEMAC avec un autre code.  Les variables clandestines sont alors des variables propres a lautre code et sont rendues dans le fichier de resultats.',
    ang= 'Names of variables that are not used by TELEMAC, but should be preserved when it is being run. This keyword may be used, for instance when it if TELEMAC is coupled with another code. Thus, the clandestine variables belong to the other code and are given back in the results file.',
     ),







Threshold_Depth_For_Wind = SIMP( statut='o',typ='R',
    defaut=1.0 ,
    fr = 'Retire la force due au vent dans les petites profondeurs',
    ang= 'Wind is not taken into account for small depths',
     ),


Origin_Coordinates = SIMP( statut='o',typ='I',
    defaut=(0, 0) ,
    max=2 ,
    fr = 'Valeur en metres, utilise pour eviter les trops grands nombres, transmis dans le format Selafin mais pas dautre traitement pour linstant',
    ang= 'Value in metres, used to avoid large real numbers,  added in Selafin format, but so far no other treatment',
     ),

Delwaq_Printout_Period = SIMP( statut='o',typ='I',
    defaut=1 ,
    fr = 'Periode de sortie des resultats pour Delwaq',
    ang= 'Printout period for Delwaq file',
     ),

Volumes_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Exchange_Areas_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Vertical_Fluxes_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Salinity_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Bottom_Surfaces_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Exchanges_Between_Nodes_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Nodes_Distances_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Temperature_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Velocity_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Diffusivity_Delwaq_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Delwaq_Steering_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier de resultats pour le couplage avec Delwaq',
    ang= 'Results file for coupling with Delwaq',
     ),

Time_Range_For_Fourier_Analysis = SIMP( statut='o',typ='R',
    defaut=(0.0, 0.0) ,
    max=2 ,
    fr = 'Pour le calcul du marnage et de la phase de la maree',
    ang= 'For computing tidal range and phase of tide',
     ),

Number_Of_Tracers = SIMP( statut='o',typ='I',
    defaut=0 ,
    fr = 'Definit le nombre de traceurs.',
    ang= 'Defines the number of tracers',
     ),

Names_Of_Tracers = SIMP( statut='o',typ='TXM',
    max=2 ,
    fr = 'Noms des traceurs en 32 caracteres, 16 pour le nom 16 pour lunite',
    ang= 'Name of tracers in 32 characters, 16 for the name, 16 for the unit.',
     ),

Salinity_For_Delwaq = SIMP( statut='o',typ='bool',
    defaut=False ,
    fr = 'Decide de la sortie de la salinite pour Delwaq',
    ang= 'Triggers output of salinity for Delwaq',
     ),

Temperature_For_Delwaq = SIMP( statut='o',typ='bool',
    defaut=False ,
    fr = 'Decide de la sortie de la temperature pour Delwaq',
    ang= 'Triggers output of temperature for Delwaq',
     ),

Velocity_For_Delwaq = SIMP( statut='o',typ='bool',
    defaut=False ,
    fr = 'Decide de la sortie de la vitesse pour Delwaq',
    ang= 'Triggers output of velocity for Delwaq',
     ),

Diffusivity_For_Delwaq = SIMP( statut='o',typ='bool',
    defaut=False ,
    fr = 'Decide de la sortie du coefficient de diffusion pour Delwaq',
    ang= 'Triggers output of diffusion for Delwaq',
     ),






Tomawac_Steering_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier des parametres de Tomawac en cas de couplage interne',
    ang= 'Tomawac parameter file in case of internal coupling',
     ),

Coupling_Period_For_Tomawac = SIMP( statut='o',typ='I',
    defaut=1 ,
    fr = 'pour eviter de faire le couplage a chaque pas de temps',
    ang= 'to avoid coupling at every time-step',
     ),

Finite_Volume_Scheme = SIMP( statut='o',typ='TXM',
#CHoix de 0 a 6
      into=[ "Roe scheme", "kinetic order 1", "kinetic order 2", "Zokagoa scheme order 1", "Tchamen scheme order 1", "HLLC scheme order 1", "WAF scheme order 2"],

      defaut="kinetic order 1",
),
Newmark_Time_Integration_Coefficient = SIMP( statut='o',typ='R',
    defaut=1.0 ,
    fr = '1. : Euler explicite 0.5 : ordre 2 en temps',
    ang= '1. : Euler explicit 0.5 : order 2 in time',
     ),


Rain_Or_Evaporation = SIMP( statut='o',typ='bool',
    defaut=False ,
    fr = 'Pour ajouter un apport ou une perte deau en surface.  Voir le mot-cle PLUIE OU EVAPORATION EN MM PAR JOUR',
    ang= 'to add or remove water at the free surface. See the key-word RAIN OR EVAPORATION IN MM PER DAY',
     ),

Rain_Or_Evaporation_In_Mm_Per_Day = SIMP( statut='o',typ='R',
    defaut=0 ,
    fr = 'Pour ajouter un apport ou une perte deau en surface',
    ang= 'to add or remove water at the free surface',
     ),

Binary_Database_1_For_Tide = SIMP( statut='o',typ='TXM',
    fr = 'Base de donnees binaire 1 tiree du fichier du modele de maree.  Dans le cas des donnees satellitaires de TPXO, ce fichier correspond aux donnees de niveau deau, par exemple h_tpxo7.2',
    ang= 'Binary database 1 extracted from the tidal model file.  In the case of the TPXO satellite altimetry model, this file should be for free surface level, for instance h_tpxo7.2',
     ),

Binary_Database_2_For_Tide = SIMP( statut='o',typ='TXM',
    fr = 'Base de donnees binaire 2 tiree du fichier du modele de maree.  Dans le cas des donnees satellitaires de TPXO, ce fichier correspond aux donnees de vitesse de marrees, par exemple u_tpxo7.2',
    ang= 'Binary database 2 extracted from the tidal model file.  In the case of the TPXO satellite altimetry model, this file should be for tidal velocities, for instance u_tpxo7.2',
     ),

Option_For_Tsunami_Generation = SIMP( statut='o',typ='I',
    defaut=0 ,
    fr = '',
    ang= '',
     ),

Physical_Characteristics_Of_The_Tsunami = SIMP( statut='o',typ='R',
    defaut=(100.0, 210000.0, 75000.0, 13.6, 81.0, 41.0, 110.0, 0.0, 0.0, 3.0) ,
    max=10 ,
    fr = '',
    ang= '',
     ),

Values_Of_Tracers_In_The_Rain = SIMP( statut='o',typ='R',
    max=2 ,
    fr = '',
    ang= '',
     ),


Coefficient_To_Calibrate_Tidal_Velocities = SIMP( statut='o',typ='R',
    defaut=999999.0 ,
    fr = 'Coefficient pour ajuster les composantes de vitesse de londe de maree aux frontieres maritimes.  La valeur par defaut 999999. signifie que cest la racine carree du COEFFICIENT DE CALAGE DU MARNAGE qui est prise',
    ang= 'Coefficient to calibrate the tidal velocities of tidal wave at tidal open boundary conditions.  Default value 999999. means that the square root of COEFFICIENT TO CALIBRATE TIDAL RANGE is taken',
     ),

Zone_Number_In_Geographic_System = SIMP( statut='o',typ='I',
    defaut=-1 ,
    fr = 'Numero de zone (fuseau ou type de projection) lors de lutilisation dune projection plane.  Indiquer le systeme geographique dans lequel est construit le modele numerique avec le mot-cle SYSTEME GEOGRAPHIQUE',
    ang= 'Number of zone when using a plane projection.  Indicate the geographic system in which the numerical model is built with the keyword GEOGRAPHIC SYSTEM',
     ),

Law_Of_Tracers_Degradation = SIMP( statut='o',typ='I',
    defaut=(0, 0) ,
    max=2 ,
    fr = 'Prise en compte dune loi de decroissance des traceurs',
    ang= 'Take in account a law for tracers decrease',
     ),

Coefficient_1_For_Law_Of_Tracers_Degradation = SIMP( statut='o',typ='R',
    max=2 ,
    fr = 'Coefficient 1 de la loi de decroissance des traceurs',
    ang= 'Coefficient 1 of law for tracers decrease',
     ),


Spatial_Projection_Type = SIMP( statut='o',typ='I',
    defaut=1 ,
   into =('1="CARTESIAN, NOT GEOREFERENCED"', '2="MERCATOR"', '3="LATITUDE LONGITUDE"'),
    fr = 'Option 2 ou 3 obligatoire pour les coordonnees spheriques Option 3 : latitude et longitude en degres !',
    ang= 'Option 2 or 3 mandatory for spherical coordinates Option 3: latitude and longitude in degrees!',
     ),

Option_For_Characteristics = SIMP( statut='o',typ='I',
    defaut=1 ,
    fr = '1: forme forte 2: forme faible',
    ang= '1: strong form 2: weak form',
     ),

Maximum_Number_Of_Iterations_For_Advection_Schemes = SIMP( statut='o',typ='I',
    defaut=10 ,
    fr = 'Seulement pour schemes 13 et 14',
    ang= 'Only for schemes 13 and 14',
     ),


Number_Of_Gauss_Points_For_Weak_Characteristics = SIMP( statut='o',typ='I',
    defaut=3 ,
    fr = 'Voir les release notes 6.3',
    ang= 'See release notes 6.3',
     ),

Mass_lumping_For_Weak_Characteristics = SIMP( statut='o',typ='R',
    defaut=0.0 ,
    fr = 'Applique a la matrice de masse',
    ang= 'To be applied to the mass matrix',
     ),


Zones_File = SIMP( statut='o',typ='TXM',
    fr = 'Fichier des zones avec sur chaque ligne numero de point  numero de zone',
    ang= 'Zones file, with on every line: point number   zone number',
     ),

Scheme_For_Advection_Of_Velocities = SIMP( statut='o',typ='I',
    defaut=1 ,
   into =('0="NO ADVECTION"', '1="CHARACTERISTICS"', '2="EXPLICIT + SUPG"', '3="EXPLICIT LEO POSTMA"', '4="EXPLICIT + MURD SCHEME N"', '5="EXPLICIT + MURD SCHEME PSI"', '13="N-SCHEME FOR TIDAL FLATS"', '14="N-SCHEME FOR TIDAL FLATS"'),
    fr = 'Choix du schema de convection pour les vitesses, remplace FORME DE LA CONVECTION',
    ang= 'Choice of the advection scheme for the velocities, replaces TYPE OF ADVECTION',
     ),

Scheme_For_Advection_Of_Tracers = SIMP( statut='o',typ='I',
    defaut=1 ,
   into =('0="NO ADVECTION"', '1="CHARACTERISTICS"', '2="EXPLICIT + SUPG"', '3="EXPLICIT LEO POSTMA"', '4="EXPLICIT + MURD SCHEME N"', '5="EXPLICIT + MURD SCHEME PSI"', '13="LEO POSTMA FOR TIDAL FLATS"', '14="N-SCHEME FOR TIDAL FLATS"'),
    fr = 'Choix du schema de convection pour les traceurs, remplace FORME DE LA CONVECTION',
    ang= 'Choice of the advection scheme for the tracers, replaces TYPE OF ADVECTION',
     ),

Scheme_For_Advection_Of_K_epsilon = SIMP( statut='o',typ='I',
    defaut=1 ,
   into =('0="NO ADVECTION"', '1="CHARACTERISTICS"', '2="EXPLICIT + SUPG"', '3="EXPLICIT LEO POSTMA"', '4="EXPLICIT + MURD SCHEME N"', '5="EXPLICIT + MURD SCHEME PSI"', '13="LEO POSTMA FOR TIDAL FLATS"', '14="N-SCHEME FOR TIDAL FLATS"'),
    fr = 'Choix du schema de convection pour k et epsilon, remplace FORME DE LA CONVECTION',
    ang= 'Choice of the advection scheme for k and epsilon, replaces TYPE OF ADVECTION',
     ),

Scheme_Option_For_Advection_Of_Tracers = SIMP( statut='o',typ='I',
    defaut=1 ,
    fr = 'Si present remplace et a priorite sur : OPTION POUR LES CARACTERISTIQUES OPTION DE SUPG Si schema PSI : 1=explicite 2=predicteur-correcteur pour les traceurs',
    ang= 'If present replaces and has priority over: OPTION FOR CHARACTERISTICS SUPG OPTION IF PSI SCHEME: 1=explicit 2=predictor-corrector for tracers',
     ),

Scheme_Option_For_Advection_Of_Velocities = SIMP( statut='o',typ='I',
    defaut=1 ,
    fr = 'Si present remplace et a priorite sur : OPTION POUR LES CARACTERISTIQUES OPTION DE SUPG Si schema PSI : 1=explicite 2=predicteur-correcteur pour les traceurs',
    ang= 'If present replaces and has priority over: OPTION FOR CHARACTERISTICS SUPG OPTION IF PSI SCHEME: 1=explicit 2=predictor-corrector for velocities',
     ),

Scheme_Option_For_Advection_Of_K_epsilon = SIMP( statut='o',typ='I',
    defaut=1 ,
    fr = 'Si present remplace et a priorite sur : OPTION POUR LES CARACTERISTIQUES OPTION DE SUPG Si schema PSI : 1=explicite 2=predicteur-correcteur pour k et epsilon',
    ang= 'If present replaces and has priority over: OPTION FOR CHARACTERISTICS SUPG OPTION IF PSI SCHEME: 1=explicit 2=predictor-corrector for k and epsilon',
     ),

Secondary_Currents = SIMP( statut='o',typ='bool',
    defaut=False ,
    fr = 'Pour prendre en compte les courants secondaires',
    ang= 'Using the parametrisation for secondary currents',
     ),

Production_Coefficient_For_Secondary_Currents = SIMP( statut='o',typ='R',
    defaut=7.071 ,
    fr = 'Une constante dans les termes de creation de Omega',
    ang= 'A constant in the production terms of Omega',
     ),

Dissipation_Coefficient_For_Secondary_Currents = SIMP( statut='o',typ='R',
    defaut=0.5 ,
    fr = 'Coefficient de dissipation de Omega',
    ang= 'Coefficient of dissipation term of Omega',
     ),

Water_Quality = SIMP( statut='o',typ='bool',
    defaut=False ,
    fr = 'Prise en compte ou non de qualite d eau',
    ang= 'waq effects are to be taken into account or not.',
     ),

Value_Of_Atmospheric_Pressure = SIMP( statut='o',typ='R',
    defaut=100000.0 ,
    fr = 'donne la valeur de la pression atmospherique lorsquelle est constante en temps et en espace',
    ang= 'gives the value of atmospheric pressure when it is contant in time and space',
     ),


)
