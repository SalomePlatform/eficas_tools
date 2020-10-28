#/usr/bin/env python
# -*- coding: latin-1 -*-
TelemacdicoEn = {
'VARIABLES_TO_BE_PRINTED' : {
    'U':"velocity along x axis (m/s)",
    'V':"velocity along y axis (m/s)",
    'C':"wawe celerity (m/s)",
    'H':"water depth (m)",
    'S':"free surface elevation (m)",
    'B':"bottom elevation (m)",
    'F':"Froude number",
    'Q':"scalar flowrate of fluid (m2/s)",
    'I':"flowrate along x axis (m2/s)",
    'J':"flowrate along y axis (m2/s)",
    'M':"bed-load discharge (m2/s)",
    'N':"bed-load discharge along x axis (m2/s)",
    'P':"bed-load discharge along y axis (m2/s)",
    'E':"bottom evolution (m)",
    'R':"non erodable bottom",
    'KS':"bed friction coefficient (m if Nikuradse)",
    'TOB':"mean bottom friction (N/m2)",
    'THETAW':"wave angle with axis Oy (deg)",
    'W':"wave height",
    'X':"wave period",
    '1Ai':"fraction of sediment of class i in the first layer",
    '2Ai':"fraction of sediment of class i in the second layer",
    'QSi':"bed load transport rate of sediment of class i",
    '*ES': "thicknes of bed layer i",
    '*CONC': "concentration of bed layer i ",
    'CSi':"concentration for class i",
    'CSAT':"saturated concentration (kg/m3)",
    'A':"supplementary variable A",
    'G':"supplementary variable G",
    'L':"supplementary variable L",
    'O':"supplementary variable O",
    'ZRL':"reference level for Nestor ",
  },
'VARIABLES_FOR_GRAPHIC_PRINTOUTS' : {
    'U':"velocity along x axis (m/s)",
    'V':"velocity along y axis (m/s)",
    'C':"wawe celerity (m/s)",
    'H':"water depth (m)",
    'S':"free surface elevation (m)",
    'B':"bottom elevation (m)",
    'F':"Froude number",
    'Q':"scalar flowrate of fluid (m2/s)",
    'I':"flowrate along x axis (m2/s)",
    'J':"flowrate along y axis (m2/s)",
    'M':"bed-load discharge (m2/s)",
    'N':"bed-load discharge along x axis (m2/s)",
    'P':"bed-load discharge along y axis (m2/s)",
    'E':"bottom evolution (m)",
    'R':"non erodable bottom",
    'KS':"total bed roughness (m)",
    'TOB':"Bed Shear stress (Totalfriction) (N/m2)",
    'MU':"Skin friction correction factor",
    'D50':"Mean grain diameter",
    'THETAW':"wave angle with axis Oy (deg)",
    'QSSUSP':"suspended load transport rate (m2/s)",
    'QSBL':"bed load transport rate (m2/s)",
    'W':"wave height",
    'X':"wave period",
    'UWB':"wave orbital velocity (m/s)",
    '1Ai':"fraction of sediment of class i in the first layer",
    '2Ai':"fraction of sediment of class i in the second layer",
    'kAi':"fraction of sediment of class i in the k layer",
    'kES':"thickness of the k layer",
    'kCONC':"concentration of bed layer k",
    'QSi':"bed load transport rate of sediment of class i",
    'CSi':"concentration volumic or mass concentration for class i",
    'CSAT':"saturated concentration (kg/m3)",
    'A':"supplementary variable A",
    'G':"supplementary variable G",
    'L':"supplementary variable L",
    'O':"supplementary variable O",
    'ZRL':"reference level for Nestor ",
  },
'SOLVER' : {
    3:"conjugate gradient on a normal equation",
    1:"conjugate gradient",
    2:"conjugate residual",
    4:"minimum error",
    6:"cgstab",
    7:"gmres",
    8:"direct",
  },
'PRECONDITIONING' : {
    2:"diagonal",
    0:"no preconditioning",
    3:"diagonal condensee",
    7:"crout",
    14:"diagonal and crout",
    21:"diagonal condensed  and crout",
  },
'PRECONDITIONING_FOR_SUSPENSION' : {
    2:"diagonal",
    0:"no preconditioning",
    3:"diagonal condensee",
    7:"crout",
  },
'TYPE_OF_ADVECTION' : {
    1:"CHARACTERISTICS",
    2:"SUPG",
    3:"CONSERVATIVE N-SCHEME",
    4:"CONSERVATIVE N-SCHEME",
    5:"CONSERVATIVE PSI-SCHEME",
    6:"NON CONSERVATIVE PSI SCHEME",
    7:"IMPLICIT NON CONSERVATIVE N SCHEME",
    13:"EDGE-BASED N-SCHEME",
    14:"EDGE-BASED N-SCHEME",
    15:"ERIA SCHEME",
  },
'OPTION_FOR_THE_DIFFUSION_OF_TRACER' : {
    1:"div( nu grad(T) )",
    2:"1/h div ( h nu grad(T)",
  },
'TREATMENT_OF_FLUXES_AT_THE_BOUNDARIES' : {
    1:"Priority to prescribed values",
    2:"Priority to fluxes",
  },
'SOLVER_FOR_SUSPENSION' : {
    1:"conjugate gradient",
    2:"conjugate residual",
    3:"conjugate gradient on a normal equation",
    4:"minimum error",
    7:"gmres (see option for the solver for tracer diffusion)",
    8:"direct",
  },
'LAW_OF_BOTTOM_FRICTION' : {
    0:"FLAT BOTTOM",
    1:"EQUILIBRIUM SAND RIPPLES (WAVES ONLY) KS=(MAX 3D50,ETA)",
    2:"CHEZY",
    3:"STRICKLER",
    4:"MANNING",
    5:"NIKURADSE",
  },
}
TelemacdicoFr = {
'VARIABLES_TO_BE_PRINTED' : {
    'U':"vitesse suivant l axe des x (m/s)",
    'V':"vitesse suivant l axe des y (m/s)",
    'C':"celerite",
    'H':"hauteur d eau (m)",
    'S':"cote de la surface libre (m)",
    'B':"cote du fond (m)",
    'F':"nombre de Froude",
    'Q':"debit",
    'I':"composante du debit selon l axe des x",
    'J':"composante du debit selon l axe des y",
    'M':"debit solide",
    'N':"composante du debit solide selon l axe des x",
    'P':"composante du debit solide selon l axe des y",
    'E':"evolution du fond",
    'R':"fonds non erodables",
    'W':"hauteur de houle",
    'X':"periode de houle",
    'KS':"coefficient de frottement (m)",
    'TOB':"frottement moyen (N/m2)",
    'THETAW':"angle entre la houle et l'axe Oy (deg)",
    '1Ai':"fraction de sediment de la classe i dans la premiere couche",
    '2Ai':"fraction de sediment de la classe i dans la deuxieme couche",
    'QSi':"debit solide pour la classe i",
    'CSi':"concentration pour la classe i",
    '*ES': "thicknes of bed layer i",
    '*CONC': "concentration of bed layer i ",
    'CSAT':"saturated concentration (kg/m3)",
    'A':"variable supplementaire A",
    'G':"variable supplementaire G",
    'L':"variable supplementaire L",
    'O':"variable supplementaire O",
    'ZRL':"reference level for Nestor",
  },
'VARIABLES_FOR_GRAPHIC_PRINTOUTS' : {
    'U':"vitesse suivant l axe des x (m/s)",
    'V':"vitesse suivant l axe des y (m/s)",
    'C':"celerite",
    'H':"hauteur d eau (m)",
    'S':"cote de la surface libre (m)",
    'B':"cote du fond (m)",
    'F':"nombre de Froude",
    'Q':"debit",
    'I':"composante du debit selon l axe des x",
    'J':"composante du debit selon l axe des y",
    'M':"debit solide",
    'N':"composante du debit solide selon l axe des x",
    'P':"composante du debit solide selon l axe des y",
    'E':"evolution du fond",
    'R':"fonds non erodables",
    'W':"hauteur de houle",
    'X':"periode de houle",
    'UWB':"wave orbital velocity (m/s)",
    'KS':"coefficient de Rugosite totale (m)",
    'TOB':"Contrainte de frottement(N/m2)",
    'MU':"Coefficient de correction pour frottement de peau",
    'D50':"Diametre moyen du sediment",
    'THETAW':"angle entre la houle et l'axe Oy (deg)",
    'QSSUSP':"taux de transport en suspension",
    'QSBL':"taux de transport par charriage",
    '1Ai':"fraction de sediment de la classe i dans la premiere couche",
    '2Ai':"fraction de sediment de la classe i dans la deuxieme couche",
    'kAi':"fraction of sediment of class i in the k layer",
    'kES':"thickness of the k layer",
    'kCONC':"concentration of bed layer k",
    'QSi':"debit solide pour la classe i",
    'CSi':"concentration volumique ou g/l pour la classe i",
    'CSAT':"concentration volumique equil ou g/l",
    'A':"variable supplementaire A",
    'G':"variable supplementaire G",
    'L':"variable supplementaire L",
    'O':"variable supplementaire O",
    'ZRL':"reference level for Nestor ",
  },
'SOLVER' : {
    3:"equation normale",
    1:"gradient conjuge",
    2:"residu conjuge",
    4:"erreur minimale",
    6:"cgstab",
    7:"gmres",
    8:"direct",
  },
'PRECONDITIONING' : {
    2:"diagonal",
    0:"aucun",
    3:"diagonal condensee",
    7:"crout",
    14:"diagonal et crout",
    21:"diagonal condense et crout",
  },
'PRECONDITIONING_FOR_SUSPENSION' : {
    2:"diagonal",
    0:"aucun",
    3:"diagonal condensee",
    7:"crout",
  },
'TYPE_OF_ADVECTION' : {
    1:"CARACTERISTIQUES",
    2:"SUPG",
    3:"SCHEMA N CONSERVATIF",
    4:"SCHEMA N CONSERVATIF",
    5:"SCHEMA PSI CONSERVATIF",
    6:"SCHEMA PSI NON CONSERVATIF",
    7:"SCHEMA N IMPLICITE NON CONSERVATIF",
    13:"SCHEMA N PAR SEGMENTS",
    14:"SCHEMA N PAR SEGMENTS",
    15:"SCHEMA ERIA",
  },
'OPTION_FOR_THE_DIFFUSION_OF_TRACER' : {
    1:"div( nu grad(T) )",
    2:"1/h div ( h nu grad(T)",
  },
'TREATMENT_OF_FLUXES_AT_THE_BOUNDARIES' : {
    1:"Priorite aux valeurs imposees",
    2:"Priorite aux flux",
  },
'SOLVER_FOR_SUSPENSION' : {
    1:"gradient conjuge",
    2:"residu conjuge",
    3:"gradient conjuge sur equation normale",
    4:"erreur minimale",
    7:"gmres (voir ausi option du solveur)",
    8:"direct",
  },
'LAW_OF_BOTTOM_FRICTION' : {
    0:"FLAT BOTTOM",
    1:"EQUILIBRIUM SAND RIPPLES (WAVES ONLY) KS=(MAX 3D50,ETA)",
    2:"CHEZY",
    3:"STRICKLER",
    4:"MANNING",
    5:"NIKURADSE",
  },
}

DicoCasFrToCata = {
  "TITRE":"TITLE",
  "PROCESSEURS PARALLELES":"PARALLEL_PROCESSORS",
  "VALIDATION":"VALIDATION",
  "NOMBRE DE TABLEAUX PRIVES":"NUMBER_OF_PRIVATE_ARRAYS",
  "COORDONNEES DE L'ORIGINE":"ORIGIN_COORDINATES",
  "DEBUGGER":"DEBUGGER",
  "OPTION DE TRAITEMENT DES BANCS DECOUVRANTS":"OPTION_FOR_THE_TREATMENT_OF_TIDAL_FLATS",
  "NESTOR":"NESTOR",
  "FICHIER DE NESTOR ACTION":"NESTOR_ACTION_FILE",
  "FICHIER DE NESTOR POLYGON":"NESTOR_POLYGON_FILE",
  "FICHIER DE NESTOR RESTART":"NESTOR_RESTART_FILE",
  "FICHIER DE NESTOR DE SURFACE REFERENCE":"NESTOR_SURFACE_REFERENCE_FILE",
  "VERIFICATION DU MAILLAGE":"CHECKING_THE_MESH",
  "NOMBRE MAXIMUM DE FRONTIERES":"MAXIMUM_NUMBER_OF_BOUNDARIES",
  "FICHIER DE FLUXLINE":"FLUXLINE_INPUT_FILE",
  "FLUXLINE":"FLUXLINE",
  "SECTIONS DE CONTROLE":"CONTROL_SECTIONS",
  "STATIONARY MODE":"STATIONARY_MODE",
  "PARAMETRES DE SHIELDS":"SHIELDS_PARAMETERS",
  "OPTION DE TRAITEMENT DES FONDS NON ERODABLES":"OPTION_FOR_THE_TREATMENT_OF_NON_ERODABLE_BEDS",
  "VALEUR MINIMUM DE H":"MINIMAL_VALUE_OF_THE_WATER_HEIGHT",
  "BANCS DECOUVRANTS":"TIDAL_FLATS",
  "COURANTS SECONDAIRES":"SECONDARY_CURRENTS",
  "FICHIER DE COURANTS SECONDAIRES":"SECONDARY_CURRENTS_FILE",
  "GRAIN-FEEDING":"GRAIN_FEEDING",
  "CAS PERMANENT":"STEADY_CASE",
  "CONSTANT FLOW DISCHARGE":"CONSTANT_FLOW_DISCHARGE",
  "NOMBRE D'ITERATIONS POUR TELEMAC":"NUMBER_OF_ITERATIONS_FOR_TELEMAC",
  "CRITERE POUR METTRE A JOUR L'HYDRODYNAMIQUE":"CRITERION_TO_UPDATE_THE_FLOW",
  "RAPPORT D'EVOLUTION CRITIQUE":"CRITICAL_EVOLUTION_RATIO",
  "NOMBRE DE COUCHES POUR GRANULO ETENDUE":"NUMBER_OF_BED_LOAD_MODEL_LAYERS",
  "CONCENTRATION MASSIQUE":"MASS_CONCENTRATION",
  "PRISE EN COMPTE DE LA HOULE":"EFFECT_OF_WAVES",
  "SEDIMENT MIXTE":"MIXED_SEDIMENT",
  "LONGUEUR DU VECTEUR":"VECTOR_LENGTH",
  "FICHIER DES PARAMETRES":"STEERING_FILE",
  "DIAMETRE MOYEN DES GRAINS":"MEAN_DIAMETER_OF_THE_SEDIMENT",
  "STANDARD DU FICHIER DE GEOMETRIE":"GEOMETRY_FILE_BINARY",
  "STANDARD DU FICHIER HYDRODYNAMIQUE":"HYDRODYNAMIC_FILE_BINARY",
  "STANDARD DU FICHIER PRECEDENT SEDIMENTOLOGIQUE":"BINARY_OF_THE_PREVIOUS_SEDIMENTOLOGICAL_COMPUTATION_FILE",
  "STANDARD DU FICHIER RESULTAT":"RESULTS_FILE_BINARY",
  "STANDARD DU FICHIER DE REFERENCE":"REFERENCE_FILE_BINARY",
  "FORMAT DU FICHIER DE GEOMETRIE":"GEOMETRY_FILE_FORMAT",
  "FICHIER DE GEOMETRIE":"GEOMETRY_FILE",
  "FICHIER HYDRODYNAMIQUE":"HYDRODYNAMIC_FILE",
  "NOMS DES VARIABLES PRIVEES":"NAMES_OF_PRIVATE_VARIABLES",
  "FICHIER DES FRONTIERES LIQUIDES":"LIQUID_BOUNDARIES_FILE",
  "FORMAT DU FICHIER DES RESULTATS":"RESULTS_FILE_FORMAT",
  "FICHIER DES RESULTATS":"RESULTS_FILE",
  "VARIABLES A IMPRIMER":"VARIABLES_TO_BE_PRINTED",
  "PERIODE DE SORTIE GRAPHIQUE":"GRAPHIC_PRINTOUT_PERIOD",
  "PERIODE DE SORTIE LISTING":"LISTING_PRINTOUT_PERIOD",
  "BILAN DE MASSE":"MASS_BALANCE",
  "SECTIONS OUTPUT FILE":"SECTIONS_OUTPUT_FILE",
  "FICHIER DES RESULTATS C-VSM":"C_VSM_RESULTS_FILE",
  "FORMAT DU FICHIER DES C-VSM RESULTATS":"C_VSM_RESULTS_FILE_FORMAT",
  "FORMAT DU FICHIER HYDRODYNAMIQUE":"HYDRODYNAMIC_FILE_FORMAT",
  "FORMAT DU FICHIER DE REFERENCE":"REFERENCE_FILE_FORMAT",
  "FORMAT DU FICHIER DE HOULE":"WAVE_FILE_FORMAT",
  "FICHIER FORTRAN":"FORTRAN_FILE",
  "FICHIER DES CONDITIONS AUX LIMITES":"BOUNDARY_CONDITIONS_FILE",
  "FICHIER DE HOULE":"WAVE_FILE",
  "FICHIER DE REFERENCE":"REFERENCE_FILE",
  "FICHIER DES FONDS":"BOTTOM_TOPOGRAPHY_FILE",
  "FICHIER DES SECTIONS DE CONTROLE":"SECTIONS_INPUT_FILE",
  "FORMAT DU FICHIER PRECEDENT SEDIMENTOLOGIQUE":"PREVIOUS_SEDIMENTOLOGICAL_COMPUTATION_FILE_FORMAT",
  "FICHIER PRECEDENT SEDIMENTOLOGIQUE":"PREVIOUS_SEDIMENTOLOGICAL_COMPUTATION_FILE",
  "SUITE DE CALCUL":"COMPUTATION_CONTINUED",
  "VARIABLES POUR LES SORTIES GRAPHIQUES":"VARIABLES_FOR_GRAPHIC_PRINTOUTS",
  "TEMPS D'ORIGINE DE L'HYDROGRAMME":"STARTING_TIME_OF_THE_HYDROGRAM",
  "NOMBRE DE PAS DE TEMPS":"NUMBER_OF_TIME_STEPS",
  "PAS DE TEMPS":"TIME_STEP",
  "NOMBRE DE SOUS-ITERATIONS":"NUMBER_OF_SUB_ITERATIONS",
  "NOMBRE DE MAREES OU CRUES":"NUMBER_OF_TIDES_OR_FLOODS",
  "HEURE DE L'ORIGINE DES TEMPS":"ORIGINAL_HOUR_OF_TIME",
  "DATE DE L'ORIGINE DES TEMPS":"ORIGINAL_DATE_OF_TIME",
  "PERIODE DE LA MAREE":"TIDE_PERIOD",
  "DEBITS SOLIDES IMPOSES":"PRESCRIBED_SOLID_DISCHARGES",
  "SOLVEUR":"SOLVER",
  "OPTION DU SOLVEUR":"SOLVER_OPTION",
  "PRECONDITIONNEMENT":"PRECONDITIONING",
  "MAXIMUM D'ITERATIONS POUR LE SOLVEUR":"MAXIMUM_NUMBER_OF_ITERATIONS_FOR_SOLVER",
  "OPTION DU SOLVEUR POUR LA SUSPENSION":"SOLVER_OPTION_FOR_SUSPENSION",
  "MAXIMUM D'ITERATIONS POUR LE SOLVEUR POUR LA SUSPENSION":"MAXIMUM_NUMBER_OF_ITERATIONS_FOR_SOLVER_FOR_SUSPENSION",
  "PRECISION DU SOLVEUR":"SOLVER_ACCURACY",
  "PRECISION DU SOLVEUR POUR LA SUSPENSION":"SOLVER_ACCURACY_FOR_SUSPENSION",
  "PRECONDITIONNEMENT POUR LA SUSPENSION":"PRECONDITIONING_FOR_SUSPENSION",
  "MASS-LUMPING":"MASS_LUMPING",
  "TETA":"TETA",
  "ZERO":"ZERO",
  "VOLUMES FINIS":"FINITE_VOLUMES",
  "FORME DE LA CONVECTION":"TYPE_OF_ADVECTION",
  "OPTION DE SUPG":"SUPG_OPTION",
  "PRODUIT MATRICE-VECTEUR":"MATRIX_VECTOR_PRODUCT",
  "STOCKAGE DES MATRICES":"MATRIX_STORAGE",
  "OPTION POUR LA DIFFUSION DU TRACEUR":"OPTION_FOR_THE_DIFFUSION_OF_TRACER",
  "MAXIMUM D'ITERATIONS POUR LES SCHEMAS DE CONVECTION":"MAXIMUM_NUMBER_OF_ITERATIONS_FOR_ADVECTION_SCHEMES",
  "PARTITIONNEUR":"PARTITIONING_TOOL",
  "NOMBRE DE CORRECTIONS DES SCHEMAS DISTRIBUTIFS":"NUMBER_OF_CORRECTIONS_OF_DISTRIBUTIVE_SCHEMES",
  "NOMBRE DE SOUS-PAS DES SCHEMAS DISTRIBUTIFS":"NUMBER_OF_SUB_STEPS_OF_DISTRIBUTIVE_SCHEMES",
  "TRAITEMENT DES FLUX AUX FRONTIERES":"TREATMENT_OF_FLUXES_AT_THE_BOUNDARIES",
  "OPTION DU PREDICTEUR DE RUGOSITE":"BED_ROUGHNESS_PREDICTOR_OPTION",
  "SOLVEUR POUR LA SUSPENSION":"SOLVER_FOR_SUSPENSION",
  "AD NOMBRE DE DERIVEES":"AD_NUMBER_OF_DERIVATIVES",
  "AD NOMS DES DERIVEES":"AD_NAMES_OF_DERIVATIVES",
  "AD NOMBRE DE DIRECTIONS":"AD_NUMBER_OF_DIRECTIONS",
  "AD SOLVEUR LINEAIRE SYMBOLIQUE":"AD_SYMBOLIC_LINEAR_SOLVER",
  "AD REMISE A ZERO DES DERIVEES DU SOLVEUR LINEAIRE":"AD_LINEAR_SOLVER_RESET_DERIVATIVES",
  "AD CONVERGENCE DES DERIVEES POUR LE SOLVEUR LINEAIRE":"AD_LINEAR_SOLVER_DERIVATIVE_CONVERGENCE",
  "MASSE VOLUMIQUE DE L'EAU":"WATER_DENSITY",
  "MASSE VOLUMIQUE DU SEDIMENT":"SEDIMENT_DENSITY",
  "POROSITE DU LIT NON COHESIF":"NON_COHESIVE_BED_POROSITY",
  "GRAVITE":"GRAVITY_ACCELERATION",
  "VISCOSITE CINEMATIQUE EAU":"WATER_VISCOSITY",
  "SETTLING LAG":"SETTLING_LAG",
  "VITESSES DE CHUTE":"SETTLING_VELOCITIES",
  "SUSPENSION":"SUSPENSION",
  "DISPERSION LONGITUDINALE":"DISPERSION_ALONG_THE_FLOW",
  "DISPERSION TRANSVERSALE":"DISPERSION_ACROSS_THE_FLOW",
  "CONCENTRATION D'EQUILIBRE EN ENTREE":"EQUILIBRIUM_INFLOW_CONCENTRATION",
  "FORMULE POUR LA CONCENTRATION DE REFERENCE":"REFERENCE_CONCENTRATION_FORMULA",
  "CORRECTION DU CHAMP CONVECTEUR":"CORRECTION_ON_CONVECTION_VELOCITY",
  "CONCENTRATIONS INITIALES EN SUSPENSION":"INITIAL_SUSPENSION_CONCENTRATIONS",
  "CONCENTRATIONS PAR CLASSE AUX FRONTIERES":"CONCENTRATION_PER_CLASS_AT_BOUNDARIES",
  "DIFFUSION":"DIFFUSION",
  "OPTION POUR LA DISPERSION":"OPTION_FOR_THE_DISPERSION",
  "TETA SUSPENSION":"TETA_SUSPENSION",
  "VITESSE CRITIQUE DE DEPOT DE LA VASE":"CRITICAL_SHEAR_VELOCITY_FOR_MUD_DEPOSITION",
  "CONSTANTE DE PARTHENIADES":"PARTHENIADES_CONSTANT",
  "D90":"D90",
  "DIAMETRES DES GRAINS":"SEDIMENT_DIAMETERS",
  "HIDING FACTOR PAR CLASSE GRANULO":"HIDING_FACTOR_FOR_PARTICULAR_SIZE_CLASS",
  "NOMBRE DE CLASSES GRANULOMETRIQUES":"NUMBER_OF_SIZE_CLASSES_OF_BED_MATERIAL",
  "FRACTION INITIALE PAR CLASSE SEDIMENTOLOGIQUE":"INITIAL_FRACTION_FOR_PARTICULAR_SIZE_CLASS",
  "EPAISSEUR DE COUCHE ACTIVE":"ACTIVE_LAYER_THICKNESS",
  "HIDING FACTOR FORMULA":"HIDING_FACTOR_FORMULA",
  "EPAISSEUR DE COUCHE ACTIVE CONSTANTE":"CONSTANT_ACTIVE_LAYER_THICKNESS",
  "SEDIMENTS COHESIFS":"COHESIVE_SEDIMENTS",
  "VERTICAL GRAIN SORTING MODEL":"VERTICAL_GRAIN_SORTING_MODEL",
  "C-VSM MAXIMUM SECTIONS":"C_VSM_MAXIMUM_SECTIONS",
  "C-VSM FULL PRINTOUT PERIOD":"C_VSM_FULL_PRINTOUT_PERIOD",
  "C-VSM PRINTOUT SELECTION":"C_VSM_PRINTOUT_SELECTION",
  "C-VSM DYNAMIC ALT MODEL":"C_VSM_DYNAMIC_ALT_MODEL",
  "RATIO ENTRE LA RUGOSITE DE PEAU ET LE DIAMETRE MOYEN":"RATIO_BETWEEN_SKIN_FRICTION_AND_MEAN_DIAMETER",
  "CORRECTION FROTTEMENT DE PEAU":"SKIN_FRICTION_CORRECTION",
  "COEFFICIENT DE FROTTEMENT":"FRICTION_COEFFICIENT",
  "LOI DE FROTTEMENT SUR LE FOND":"LAW_OF_BOTTOM_FRICTION",
  "FORMULE POUR EFFET DE PENTE":"FORMULA_FOR_SLOPE_EFFECT",
  "ANGLE DE FROTTEMENT DU SEDIMENT":"FRICTION_ANGLE_OF_THE_SEDIMENT",
  "FORMULE POUR LA DEVIATION":"FORMULA_FOR_DEVIATION",
  "PARAMETRE POUR LA DEVIATION":"PARAMETER_FOR_DEVIATION",
  "GLISSEMENT DU SEDIMENT":"SEDIMENT_SLIDE",
  "EFFET DE PENTE":"SLOPE_EFFECT",
  "BETA":"BETA",
  "PREDICTION DE LA RUGOSITE":"BED_ROUGHNESS_PREDICTION",
  "SECONDARY CURRENTS ALPHA COEFFICIENT":"SECONDARY_CURRENTS_ALPHA_COEFFICIENT",
  "FACTEUR MORPHOLOGIQUE":"MORPHOLOGICAL_FACTOR",
  "PROFONDEUR MINIMUM POUR LE CHARRIAGE":"MINIMUM_DEPTH_FOR_BEDLOAD",
  "CHARRIAGE":"BED_LOAD",
  "FORMULE DE TRANSPORT SOLIDE":"BED_LOAD_TRANSPORT_FORMULA",
  "COEFFICIENT B DE LA FORMULE DE BIJKER":"B_VALUE_FOR_THE_BIJKER_FORMULA",
  "MPM COEFFICIENT":"MPM_COEFFICIENT",
  "OPTION DU SCHEMA POUR LA CONVECTION":"SCHEME_OPTION_FOR_ADVECTION",
  "OPTION DU MODELE DE TASSEMENT":"CONSOLIDATION_MODEL",
  "CONCENTRATION GEL":"GEL_CONCENTRATION",
  "CONCENTRATION MAXIMALE":"MAXIMUM_CONCENTRATION",
  "COEFFICIENT DE PERMEABILITE":"PERMEABILITY_COEFFICIENT",
  "TASSEMENT DU LIT COHESIF":"MUD_CONSOLIDATION",
  "NOMBRE DE COUCHES POUR LE TASSEMENT":"NUMBER_OF_LAYERS_OF_THE_CONSOLIDATION_MODEL",
  "TRANSFERT DE MASSE PAR COUCHE":"MASS_TRANSFER_PER_LAYER",
  "CONCENTRATIONS DU LIT DE VASE":"MUD_CONCENTRATION_PER_LAYER",
  "CONTRAINTE CRITIQUE D'EROSION DE LA VASE":"CRITICAL_EROSION_SHEAR_STRESS_OF_THE_MUD",
  "CONCATENATION SORTIE PARTEL":"CONCATENATE_PARTEL_OUTPUT",
  "DICTIONNAIRE":"DICTIONARY",
}

DicoCasEnToCata = {
  'TITLE':'TITLE',
  'PARALLEL PROCESSORS':'PARALLEL_PROCESSORS',
  'VALIDATION':'VALIDATION',
  'NUMBER OF PRIVATE ARRAYS':'NUMBER_OF_PRIVATE_ARRAYS',
  'ORIGIN COORDINATES':'ORIGIN_COORDINATES',
  'DEBUGGER':'DEBUGGER',
  'OPTION FOR THE TREATMENT OF TIDAL FLATS':'OPTION_FOR_THE_TREATMENT_OF_TIDAL_FLATS',
  'NESTOR':'NESTOR',
  'NESTOR ACTION FILE':'NESTOR_ACTION_FILE',
  'NESTOR POLYGON FILE':'NESTOR_POLYGON_FILE',
  'NESTOR RESTART FILE':'NESTOR_RESTART_FILE',
  'NESTOR SURFACE REFERENCE FILE':'NESTOR_SURFACE_REFERENCE_FILE',
  'CHECKING THE MESH':'CHECKING_THE_MESH',
  'MAXIMUM NUMBER OF BOUNDARIES':'MAXIMUM_NUMBER_OF_BOUNDARIES',
  'FLUXLINE INPUT FILE':'FLUXLINE_INPUT_FILE',
  'FLUXLINE':'FLUXLINE',
  'CONTROL SECTIONS':'CONTROL_SECTIONS',
  'STATIONARY MODE':'STATIONARY_MODE',
  'SHIELDS PARAMETERS':'SHIELDS_PARAMETERS',
  'OPTION FOR THE TREATMENT OF NON ERODABLE BEDS':'OPTION_FOR_THE_TREATMENT_OF_NON_ERODABLE_BEDS',
  'MINIMAL VALUE OF THE WATER HEIGHT':'MINIMAL_VALUE_OF_THE_WATER_HEIGHT',
  'TIDAL FLATS':'TIDAL_FLATS',
  'SECONDARY CURRENTS':'SECONDARY_CURRENTS',
  'SECONDARY CURRENTS FILE':'SECONDARY_CURRENTS_FILE',
  'GRAIN-FEEDING':'GRAIN_FEEDING',
  'STEADY CASE':'STEADY_CASE',
  'CONSTANT FLOW DISCHARGE':'CONSTANT_FLOW_DISCHARGE',
  'NUMBER OF ITERATIONS FOR TELEMAC':'NUMBER_OF_ITERATIONS_FOR_TELEMAC',
  'CRITERION TO UPDATE THE FLOW':'CRITERION_TO_UPDATE_THE_FLOW',
  'CRITICAL EVOLUTION RATIO':'CRITICAL_EVOLUTION_RATIO',
  'NUMBER OF BED LOAD MODEL LAYERS':'NUMBER_OF_BED_LOAD_MODEL_LAYERS',
  'MASS CONCENTRATION':'MASS_CONCENTRATION',
  'EFFECT OF WAVES':'EFFECT_OF_WAVES',
  'MIXED SEDIMENT':'MIXED_SEDIMENT',
  'VECTOR LENGTH':'VECTOR_LENGTH',
  'STEERING FILE':'STEERING_FILE',
  'MEAN DIAMETER OF THE SEDIMENT':'MEAN_DIAMETER_OF_THE_SEDIMENT',
  'GEOMETRY FILE BINARY':'GEOMETRY_FILE_BINARY',
  'HYDRODYNAMIC FILE BINARY':'HYDRODYNAMIC_FILE_BINARY',
  'BINARY OF THE PREVIOUS SEDIMENTOLOGICAL COMPUTATION FILE':'BINARY_OF_THE_PREVIOUS_SEDIMENTOLOGICAL_COMPUTATION_FILE',
  'RESULTS FILE BINARY':'RESULTS_FILE_BINARY',
  'REFERENCE FILE BINARY':'REFERENCE_FILE_BINARY',
  'GEOMETRY FILE FORMAT':'GEOMETRY_FILE_FORMAT',
  'GEOMETRY FILE':'GEOMETRY_FILE',
  'HYDRODYNAMIC FILE':'HYDRODYNAMIC_FILE',
  'NAMES OF PRIVATE VARIABLES':'NAMES_OF_PRIVATE_VARIABLES',
  'LIQUID BOUNDARIES FILE':'LIQUID_BOUNDARIES_FILE',
  'RESULTS FILE FORMAT':'RESULTS_FILE_FORMAT',
  'RESULTS FILE':'RESULTS_FILE',
  'VARIABLES TO BE PRINTED':'VARIABLES_TO_BE_PRINTED',
  'GRAPHIC PRINTOUT PERIOD':'GRAPHIC_PRINTOUT_PERIOD',
  'LISTING PRINTOUT PERIOD':'LISTING_PRINTOUT_PERIOD',
  'MASS-BALANCE':'MASS_BALANCE',
  'SECTIONS OUTPUT FILE':'SECTIONS_OUTPUT_FILE',
  'C-VSM RESULTS FILE':'C_VSM_RESULTS_FILE',
  'C-VSM RESULTS FILE FORMAT':'C_VSM_RESULTS_FILE_FORMAT',
  'HYDRODYNAMIC FILE FORMAT':'HYDRODYNAMIC_FILE_FORMAT',
  'REFERENCE FILE FORMAT':'REFERENCE_FILE_FORMAT',
  'WAVE FILE FORMAT':'WAVE_FILE_FORMAT',
  'FORTRAN FILE':'FORTRAN_FILE',
  'BOUNDARY CONDITIONS FILE':'BOUNDARY_CONDITIONS_FILE',
  'WAVE FILE':'WAVE_FILE',
  'REFERENCE FILE':'REFERENCE_FILE',
  'BOTTOM TOPOGRAPHY FILE':'BOTTOM_TOPOGRAPHY_FILE',
  'SECTIONS INPUT FILE':'SECTIONS_INPUT_FILE',
  'PREVIOUS SEDIMENTOLOGICAL COMPUTATION FILE FORMAT':'PREVIOUS_SEDIMENTOLOGICAL_COMPUTATION_FILE_FORMAT',
  'PREVIOUS SEDIMENTOLOGICAL COMPUTATION FILE':'PREVIOUS_SEDIMENTOLOGICAL_COMPUTATION_FILE',
  'COMPUTATION CONTINUED':'COMPUTATION_CONTINUED',
  'VARIABLES FOR GRAPHIC PRINTOUTS':'VARIABLES_FOR_GRAPHIC_PRINTOUTS',
  'STARTING TIME OF THE HYDROGRAM':'STARTING_TIME_OF_THE_HYDROGRAM',
  'NUMBER OF TIME STEPS':'NUMBER_OF_TIME_STEPS',
  'TIME STEP':'TIME_STEP',
  'NUMBER OF SUB-ITERATIONS':'NUMBER_OF_SUB_ITERATIONS',
  'NUMBER OF TIDES OR FLOODS':'NUMBER_OF_TIDES_OR_FLOODS',
  'ORIGINAL HOUR OF TIME':'ORIGINAL_HOUR_OF_TIME',
  'ORIGINAL DATE OF TIME':'ORIGINAL_DATE_OF_TIME',
  'TIDE PERIOD':'TIDE_PERIOD',
  'PRESCRIBED SOLID DISCHARGES':'PRESCRIBED_SOLID_DISCHARGES',
  'SOLVER':'SOLVER',
  'SOLVER OPTION':'SOLVER_OPTION',
  'PRECONDITIONING':'PRECONDITIONING',
  'MAXIMUM NUMBER OF ITERATIONS FOR SOLVER':'MAXIMUM_NUMBER_OF_ITERATIONS_FOR_SOLVER',
  'SOLVER OPTION FOR SUSPENSION':'SOLVER_OPTION_FOR_SUSPENSION',
  'MAXIMUM NUMBER OF ITERATIONS FOR SOLVER FOR SUSPENSION':'MAXIMUM_NUMBER_OF_ITERATIONS_FOR_SOLVER_FOR_SUSPENSION',
  'SOLVER ACCURACY':'SOLVER_ACCURACY',
  'SOLVER ACCURACY FOR SUSPENSION':'SOLVER_ACCURACY_FOR_SUSPENSION',
  'PRECONDITIONING FOR SUSPENSION':'PRECONDITIONING_FOR_SUSPENSION',
  'MASS-LUMPING':'MASS_LUMPING',
  'TETA':'TETA',
  'ZERO':'ZERO',
  'FINITE VOLUMES':'FINITE_VOLUMES',
  'TYPE OF ADVECTION':'TYPE_OF_ADVECTION',
  'SUPG OPTION':'SUPG_OPTION',
  'MATRIX-VECTOR PRODUCT':'MATRIX_VECTOR_PRODUCT',
  'MATRIX STORAGE':'MATRIX_STORAGE',
  'OPTION FOR THE DIFFUSION OF TRACER':'OPTION_FOR_THE_DIFFUSION_OF_TRACER',
  'MAXIMUM NUMBER OF ITERATIONS FOR ADVECTION SCHEMES':'MAXIMUM_NUMBER_OF_ITERATIONS_FOR_ADVECTION_SCHEMES',
  'PARTITIONING TOOL':'PARTITIONING_TOOL',
  'NUMBER OF CORRECTIONS OF DISTRIBUTIVE SCHEMES':'NUMBER_OF_CORRECTIONS_OF_DISTRIBUTIVE_SCHEMES',
  'NUMBER OF SUB-STEPS OF DISTRIBUTIVE SCHEMES':'NUMBER_OF_SUB_STEPS_OF_DISTRIBUTIVE_SCHEMES',
  'TREATMENT OF FLUXES AT THE BOUNDARIES':'TREATMENT_OF_FLUXES_AT_THE_BOUNDARIES',
  'BED ROUGHNESS PREDICTOR OPTION':'BED_ROUGHNESS_PREDICTOR_OPTION',
  'SOLVER FOR SUSPENSION':'SOLVER_FOR_SUSPENSION',
  'AD NUMBER OF DERIVATIVES':'AD_NUMBER_OF_DERIVATIVES',
  'AD NAMES OF DERIVATIVES':'AD_NAMES_OF_DERIVATIVES',
  'AD NUMBER OF DIRECTIONS':'AD_NUMBER_OF_DIRECTIONS',
  'AD SYMBOLIC LINEAR SOLVER':'AD_SYMBOLIC_LINEAR_SOLVER',
  'AD LINEAR SOLVER RESET DERIVATIVES':'AD_LINEAR_SOLVER_RESET_DERIVATIVES',
  'AD LINEAR SOLVER DERIVATIVE CONVERGENCE':'AD_LINEAR_SOLVER_DERIVATIVE_CONVERGENCE',
  'WATER DENSITY':'WATER_DENSITY',
  'SEDIMENT DENSITY':'SEDIMENT_DENSITY',
  'NON COHESIVE BED POROSITY':'NON_COHESIVE_BED_POROSITY',
  'GRAVITY ACCELERATION':'GRAVITY_ACCELERATION',
  'WATER VISCOSITY':'WATER_VISCOSITY',
  'SETTLING LAG':'SETTLING_LAG',
  'SETTLING VELOCITIES':'SETTLING_VELOCITIES',
  'SUSPENSION':'SUSPENSION',
  'DISPERSION ALONG THE FLOW':'DISPERSION_ALONG_THE_FLOW',
  'DISPERSION ACROSS THE FLOW':'DISPERSION_ACROSS_THE_FLOW',
  'EQUILIBRIUM INFLOW CONCENTRATION':'EQUILIBRIUM_INFLOW_CONCENTRATION',
  'REFERENCE CONCENTRATION FORMULA':'REFERENCE_CONCENTRATION_FORMULA',
  'CORRECTION ON CONVECTION VELOCITY':'CORRECTION_ON_CONVECTION_VELOCITY',
  'INITIAL SUSPENSION CONCENTRATIONS':'INITIAL_SUSPENSION_CONCENTRATIONS',
  'CONCENTRATION PER CLASS AT BOUNDARIES':'CONCENTRATION_PER_CLASS_AT_BOUNDARIES',
  'DIFFUSION':'DIFFUSION',
  'OPTION FOR THE DISPERSION':'OPTION_FOR_THE_DISPERSION',
  'TETA SUSPENSION':'TETA_SUSPENSION',
  'CRITICAL SHEAR VELOCITY FOR MUD DEPOSITION':'CRITICAL_SHEAR_VELOCITY_FOR_MUD_DEPOSITION',
  'PARTHENIADES CONSTANT':'PARTHENIADES_CONSTANT',
  'D90':'D90',
  'SEDIMENT DIAMETERS':'SEDIMENT_DIAMETERS',
  'HIDING FACTOR FOR PARTICULAR SIZE CLASS':'HIDING_FACTOR_FOR_PARTICULAR_SIZE_CLASS',
  'NUMBER OF SIZE-CLASSES OF BED MATERIAL':'NUMBER_OF_SIZE_CLASSES_OF_BED_MATERIAL',
  'INITIAL FRACTION FOR PARTICULAR SIZE CLASS':'INITIAL_FRACTION_FOR_PARTICULAR_SIZE_CLASS',
  'ACTIVE LAYER THICKNESS':'ACTIVE_LAYER_THICKNESS',
  'HIDING FACTOR FORMULA':'HIDING_FACTOR_FORMULA',
  'CONSTANT ACTIVE LAYER THICKNESS':'CONSTANT_ACTIVE_LAYER_THICKNESS',
  'COHESIVE SEDIMENTS':'COHESIVE_SEDIMENTS',
  'VERTICAL GRAIN SORTING MODEL':'VERTICAL_GRAIN_SORTING_MODEL',
  'C-VSM MAXIMUM SECTIONS':'C_VSM_MAXIMUM_SECTIONS',
  'C-VSM FULL PRINTOUT PERIOD':'C_VSM_FULL_PRINTOUT_PERIOD',
  'C-VSM PRINTOUT SELECTION':'C_VSM_PRINTOUT_SELECTION',
  'C-VSM DYNAMIC ALT MODEL':'C_VSM_DYNAMIC_ALT_MODEL',
  'RATIO BETWEEN SKIN FRICTION AND MEAN DIAMETER':'RATIO_BETWEEN_SKIN_FRICTION_AND_MEAN_DIAMETER',
  'SKIN FRICTION CORRECTION':'SKIN_FRICTION_CORRECTION',
  'FRICTION COEFFICIENT':'FRICTION_COEFFICIENT',
  'LAW OF BOTTOM FRICTION':'LAW_OF_BOTTOM_FRICTION',
  'FORMULA FOR SLOPE EFFECT':'FORMULA_FOR_SLOPE_EFFECT',
  'FRICTION ANGLE OF THE SEDIMENT':'FRICTION_ANGLE_OF_THE_SEDIMENT',
  'FORMULA FOR DEVIATION':'FORMULA_FOR_DEVIATION',
  'PARAMETER FOR DEVIATION':'PARAMETER_FOR_DEVIATION',
  'SEDIMENT SLIDE':'SEDIMENT_SLIDE',
  'SLOPE EFFECT':'SLOPE_EFFECT',
  'BETA':'BETA',
  'BED ROUGHNESS PREDICTION':'BED_ROUGHNESS_PREDICTION',
  'SECONDARY CURRENTS ALPHA COEFFICIENT':'SECONDARY_CURRENTS_ALPHA_COEFFICIENT',
  'MORPHOLOGICAL FACTOR':'MORPHOLOGICAL_FACTOR',
  'MINIMUM DEPTH FOR BEDLOAD':'MINIMUM_DEPTH_FOR_BEDLOAD',
  'BED LOAD':'BED_LOAD',
  'BED-LOAD TRANSPORT FORMULA':'BED_LOAD_TRANSPORT_FORMULA',
  'B VALUE FOR THE BIJKER FORMULA':'B_VALUE_FOR_THE_BIJKER_FORMULA',
  'MPM COEFFICIENT':'MPM_COEFFICIENT',
  'SCHEME OPTION FOR ADVECTION':'SCHEME_OPTION_FOR_ADVECTION',
  'CONSOLIDATION MODEL':'CONSOLIDATION_MODEL',
  'GEL CONCENTRATION':'GEL_CONCENTRATION',
  'MAXIMUM CONCENTRATION':'MAXIMUM_CONCENTRATION',
  'PERMEABILITY COEFFICIENT':'PERMEABILITY_COEFFICIENT',
  'MUD CONSOLIDATION':'MUD_CONSOLIDATION',
  'NUMBER OF LAYERS OF THE CONSOLIDATION MODEL':'NUMBER_OF_LAYERS_OF_THE_CONSOLIDATION_MODEL',
  'MASS TRANSFER PER LAYER':'MASS_TRANSFER_PER_LAYER',
  'MUD CONCENTRATION PER LAYER':'MUD_CONCENTRATION_PER_LAYER',
  'CRITICAL EROSION SHEAR STRESS OF THE MUD':'CRITICAL_EROSION_SHEAR_STRESS_OF_THE_MUD',
  'CONCATENATE PARTEL OUTPUT':'CONCATENATE_PARTEL_OUTPUT',
  'DICTIONARY':'DICTIONARY',
}
DicoEnumCasFrToEnumCasEn = {
'GEOMETRY_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'RESULTS_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'C_VSM_RESULTS_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'HYDRODYNAMIC_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'REFERENCE_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'WAVE_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'PREVIOUS_SEDIMENTOLOGICAL_COMPUTATION_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'PARTITIONING_TOOL':{
  "METIS":"METIS",
  "SCOTCH":"SCOTCH",
  "PARMETIS":"PARMETIS",
  "PTSCOTCH":"PTSCOTCH",
},

}
