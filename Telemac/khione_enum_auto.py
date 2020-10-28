#/usr/bin/env python
# -*- coding: latin-1 -*-
TelemacdicoEn = {
'VARIABLES_FOR_GRAPHIC_PRINTOUTS' : {
    'PHCL':"SOLRAD CLEAR SKY",
    'PHRI':"SOLRAD CLOUDY",
    'PHPS':"NET SOLRAD",
    'PHIB':"EFFECTIVE SOLRAD",
    'PHIE':"EVAPO HEAT FLUX",
    'PHIH':"CONDUC HEAT FLUX",
    'PHIP':"PRECIP HEAT FLUX",
    'COV_TH0':"FRAZIL THETA0",
    'COV_TH1':"FRAZIL THETA1",
    'COV_BT1':"REENTRAINMENT",
    'COV_VBB':"SETTLING VEL.",
    'COV_FC':""SOLID ICE CONC.,
    'COV_THS':"SOLID ICE THICK.",
    'COV_THF':"FRAZIL THICKNESS",
    'COV_THUN':"UNDER ICE THICK.",
    'COV_EQ':"EQUIV. SURFACE",
    'COV_ET':"TOP ICE COVER",
    'COV_EB':"BOTTOM ICE COVERM",
    'COV_THT':"TOTAL ICE THICK.M ",
    'ICETYPE':"CARACTERISTIQUES",
    'NTOT':"TOTAL NUMBER OF PARTICLES",
    'CTOT':"TOTAL CONCENTRATION OF FRAZIL",
    'F*':"CONCENTRATION OF FRAZIL BY CLASS",
    'N*':"PARTICLE NUMBER OF FRAZIL BY CLASS",
    'TEMP':"WATER TEMPERATURE",
    'SAL':"SALINITY OF WATER",
  },
'LAW_OF_ICE_COVER_FRICTION' : {
    0:"NO FRICTION",
    1:"HAALAND",
    2:"CHEZY",
    3:"STRICKLER",
    4:"MANNING",
    5:"NIKURADSE",
  },
'LAW_FOR_FRICTION_COEFFICIENT' : {
    0:"CONSTANT FRICTION COEF",
    1:"LINEAR FRICTION COEF",
  },
'MODEL_FOR_THE_BUOYANCY_VELOCITY' : {
    1:"DALY (1984)",
    2:"HAALAND",
    3:"GOSIK & OSTERKAMP (1983)",
  },
'ENERGY_BALANCE_VERSION' : {
    1:"SIMPLIFIED ENERGY BALANCE",
    2:"FULL ENERGY BALANCE",
  },
'SCHEME_OPTION_FOR_THERMAL_GROWTH' : {
    1:"EXPLICIT TIME SCHEME",
    2:"SEMI-IMPLICIT TIME SCHEME",
  },
'MODEL_FOR_THE_SECONDARY_NUCLEATION' : {
    0:"NO MODEL",
    1:"SVENSSON AND OMSTEDT 1994",
    2:"WANG AND DOERING 2005",
  },
'MODEL_FOR_THE_FLOCCULATION_AND_BREAKUP' : {
    0:"NO MODEL",
    1:"SVENSSON AND OMSTEDT 1994",
  },
'MODEL_FOR_FRAZIL_SEEDING' : {
    0:"NO MODEL",
    1:"MINIMUM CONC. THRESHOLD",
    2:"CONSTANT SEEDING RATE",
    3:"BOTH OPTIONS 1 AND 2",
  },
'ATMOSPHERE_WATER_EXCHANGE_MODEL' : {
    0:"LINEARISED FORMULA",
    1:"MODEL WITH COMPLETE BALANCE",
  },
}
TelemacdicoFr = {
'VARIABLES_FOR_GRAPHIC_PRINTOUTS' : {
    'PHCL':"SOLRAD CLEAR SKY",
    'PHRI':"SOLRAD CLOUDY",
    'PHPS':"NET SOLRAD",
    'PHIB':"EFFECTIVE SOLRAD",
    'PHIE':"EVAPO HEAT FLUX",
    'PHIH':"CONDUC HEAT FLUX",
    'PHIP':"PRECIP HEAT FLUX",
    'COV_TH0':"FRAZIL THETA0",
    'COV_TH1':"FRAZIL THETA1",
    'COV_BT1':"REENTRAINMENT",
    'COV_VBB':"SETTLING VEL.",
    'COV_FC':""SOLID ICE CONC.,
    'COV_THS':"SOLID ICE THICK.",
    'COV_THF':"FRAZIL THICKNESS",
    'COV_THUN':"UNDER ICE THICK.",
    'COV_EQ':"EQUIV. SURFACE",
    'COV_ET':"TOP ICE COVER",
    'COV_EB':"BOTTOM ICE COVERM",
    'COV_THT':"TOTAL ICE THICK.M ",
    'ICETYPE':"CARACTERISTIQUES",
    'NTOT':"TOTAL NUMBER OF PARTICLES",
    'CTOT':"TOTAL CONCENTRATION OF FRAZIL",
    'F*':"CONCENTRATION OF FRAZIL BY CLASS",
    'N*':"PARTICLE NUMBER OF FRAZIL BY CLASS",
    'TEMP':"WATER TEMPERATURE",
    'SAL':"SALINITY OF WATER",
  },
'LAW_OF_ICE_COVER_FRICTION' : {
    0:"PAS DE FROTTEMENT",
    1:"HAALAND",
    2:"CHEZY",
    3:"STRICKLER",
    4:"MANNING",
    5:"NIKURADSE",
  },
'LAW_FOR_FRICTION_COEFFICIENT' : {
    0:"COEF DE FRICTION CONSTANT",
    1:"COEF DE FRICTION LINEAIRE",
  },
'MODEL_FOR_THE_BUOYANCY_VELOCITY' : {
    1:"DALY (1984)",
    2:"MATOUSEK (1992)",
    3:"GOSIK & OSTERKAMP (1983)",
  },
'ENERGY_BALANCE_VERSION' : {
    1:"SIMPLIFIED ENERGY BALANCE",
    2:"FULL ENERGY BALANCE",
  },
'SCHEME_OPTION_FOR_THERMAL_GROWTH' : {
    1:"EXPLICIT TIME SCHEME",
    2:"SEMI-IMPLICIT TIME SCHEME",
  },
'MODEL_FOR_THE_SECONDARY_NUCLEATION' : {
    0:"PAS DE MODELE",
    1:"SVENSSON ET OMSTEDT 1994",
    2:"WANG ET DOERING 2005",
  },
'MODEL_FOR_THE_FLOCCULATION_AND_BREAKUP' : {
    0:"PAS DE MODELE",
    1:"SVENSSON ET OMSTEDT 1994",
  },
'MODEL_FOR_FRAZIL_SEEDING' : {
    0:"PAS DE MODELE",
    1:"SEUIL MINIMUM DE CONC.",
    2:"TAUX D'ENSEMENCEMENT CONSTANT",
    3:"OPTIONS 1 AND 2",
  },
'ATMOSPHERE_WATER_EXCHANGE_MODEL' : {
    0:"FORMULE LINEARISEE",
    1:"MODELE A BILAN COMPLET",
  },
}

DicoCasFrToCata = {
  "FICHIER DES PARAMETRES":"STEERING_FILE",
  "FICHIER FORTRAN":"FORTRAN_FILE",
  "TITRE":"TITLE",
  "FICHIER DES CONDITIONS AUX LIMITES":"BOUNDARY_CONDITIONS_FILE",
  "FICHIER DE GEOMETRIE":"GEOMETRY_FILE",
  "FORMAT DU FICHIER DE GEOMETRIE":"GEOMETRY_FILE_FORMAT",
  "FICHIER DE REFERENCE":"REFERENCE_FILE",
  "FORMAT DU FICHIER DE REFERENCE":"REFERENCE_FILE_FORMAT",
  "FICHIER DES RESULTATS":"RESULTS_FILE",
  "FORMAT DU FICHIER DES RESULTATS":"RESULTS_FILE_FORMAT",
  "FICHIER COUVERT DE GLACE DU CALCUL PRECEDENT":"PREVIOUS_ICE_COVER_COMPUTATION_FILE",
  "FORMAT DU FICHIER COUVERT DE GLACE DU CALCUL PRECEDENT":"PREVIOUS_ICE_COVER_COMPUTATION_FILE_FORMAT",
  "FICHIER BLOCS DE GLACE DU CALCUL PRECEDENT":"PREVIOUS_ICE_BLOCKS_COMPUTATION_FILE",
  "FORMAT DU FICHIER BLOCS DE GLACE DU CALCUL PRECEDENT":"PREVIOUS_ICE_BLOCKS_COMPUTATION_FILE_FORMAT",
  "DICTIONNAIRE":"DICTIONARY",
  "CONDITIONS INITIALES":"INITIAL_CONDITIONS",
  "VARIABLES POUR LES SORTIES GRAPHIQUES":"VARIABLES_FOR_GRAPHIC_PRINTOUTS",
  "VARIABLES A IMPRIMER":"VARIABLES_TO_BE_PRINTED",
  "PERIODE POUR LES SORTIES GRAPHIQUES":"GRAPHIC_PRINTOUT_PERIOD",
  "PERIODE DE SORTIE LISTING":"LISTING_PRINTOUT_PERIOD",
  "BILAN DE MASSE":"MASS_BALANCE",
  "VALIDATION":"VALIDATION",
  "LOI DE FROTTEMENT SOUS LE COUVERT DE GLACE":"LAW_OF_ICE_COVER_FRICTION",
  "COEFFICIENT DE FROTTEMENT":"FRICTION_COEFFICIENT",
  "COEFFICIENT DE FROTTEMENT MAXIMAL":"MAXIMAL_FRICTION_COEFFICIENT",
  "LOI POUR LE COEFFICIENT DE FROTTEMENT":"LAW_FOR_FRICTION_COEFFICIENT",
  "EPAISSEUR DE COUVERT DE GLACE CARACTERISTIQUE":"EQUIVALENT_SURFACE_ICE_THICKNESS",
  "MASSE VOLUMIQUE DE L'AIR":"AIR_DENSITY",
  "MASSE VOLUMIQUE DE LA GLACE":"ICE_DENSITY",
  "CHALEUR SPECIFIQUE DE L'EAU":"WATER_SPECIFIC_HEAT",
  "CHALEUR SPECIFIQUE DE LA GLACE":"SPECIFIC_HEAT_OF_ICE",
  "CHALEUR LATENTE DE LA GLACE":"LATENT_HEAT_OF_ICE",
  "COEFFICIENT D'ECHANGE THERMIQUE EAU-AIR":"WATER_AIR_HEAT_EXCHANGE_COEFFICIENT",
  "CONSTANTE D'ECHANGE THERMIQUE EAU-AIR":"WATER_AIR_HEAT_EXCHANGE_CONSTANT",
  "COEFFICIENT D'ECHANGE THERMIQUE GLACE-AIR":"ICE_AIR_HEAT_EXCHANGE_COEFFICIENT",
  "CONSTANTE D'ECHANGE THERMIQUE GLACE-AIR":"ICE_AIR_HEAT_EXCHANGE_CONSTANT",
  "COEFFICIENT DE CALAGE DU FLUX RADIATIF ATMOSPHERIQUE":"COEFFICIENT_FOR_CALIBRATION_OF_BACK_RADIATION",
  "COEFFICIENT DE CALAGE DU TRANSFERT EVAPORATIF":"COEFFICIENT_FOR_CALIBRATION_OF_EVAPORATIVE_HEAT_TRANSFERT",
  "COEFFICIENT DE CALAGE DU TRANSFERT CONDUCTIF":"COEFFICIENT_FOR_CALIBRATION_OF_CONDUCTIVE_HEAT_TRANSFERT",
  "COEFFICIENT DE CALAGE DU TRANSFERT LIE AUX PRECIPITATIONS":"COEFFICIENT_FOR_CALIBRATION_OF_PRECIPITATION_HEAT_TRANSFERT",
  "CONDUCTIVITE THERMIQUE ENTRE EAU ET FRASIL":"THERMAL_CONDUCTIVITY_BETWEEN_WATER_AND_FRAZIL",
  "CONDUCTIVITE THERMIQUE DE LA GLACE SOMBRE":"THERMAL_CONDUCTIVITY_OF_BLACK_ICE",
  "CONDUCTIVITE THERMIQUE DE LA NEIGE":"THERMAL_CONDUCTIVITY_OF_SNOW",
  "POROSITE DE LA GLACE DE SURFACE":"POROSITY_OF_SURFACE_ICE",
  "NOMBRE DE CLASSES POUR LA SUSPENSION DE FRASIL":"NUMBER_OF_CLASSES_FOR_SUSPENDED_FRAZIL_ICE",
  "NOMBRE DE NUSSELT":"NUSSELT_NUMBER",
  "MODELE POUR LE CALCUL DU NOMBRE DE NUSSELT":"MODEL_FOR_THE_NUSSELT_NUMBER",
  "RAYON DES CRISTAUX DE FRASIL":"FRAZIL_CRYSTALS_RADIUS",
  "RATIO DIAMETRE EPAISSEUR D'UN CRISTAL DE FRASIL":"FRAZIL_CRYSTALS_DIAMETER_THICKNESS_RATIO",
  "MODELE POUR LE CALCUL DE LA VITESSE DE FLOTTABILITE":"MODEL_FOR_THE_BUOYANCY_VELOCITY",
  "COEFFICIENT DE DEPOSITION DES GLACES SUR BARRES":"SETTLING_COEFFICIENT_OF_FRAZIL_ON_BARS",
  "POROSITE DE LA GLACE ACCUMULEE":"POROSITY_OF_ACCUMULATED_ICE",
  "ANGLE D ACCUMULATION DE LA GLACE":"ANGLE_OF_ACCUMULATED_ICE",
  "PARAMETRES PHYSIQUES DE LA GRILLE D ENTREE":"PHYSICAL_CHARACTERISTICS_OF_THE_INTAKE_RACK",
  "NUMEROS DES FRONTIERES GLACEES":"CLOGGED_BOUNDARY_NUMBERS",
  "SECTIONS COLMATEES":"CLOGGED_SECTIONS",
  "FICHIER DE RESULTATS DE LA GLACE ACCUMULEE":"CLOGGING_RESULTS_FILE",
  "VITESSE CRITIQUE POUR LA GLACE DE BORD STATIQUE":"CRITICAL_VELOCITY_FOR_STATIC_BORDER_ICE",
  "VITESSE CRITIQUE POUR LA GLACE DE BORD DYNAMIQUE":"CRITICAL_VELOCITY_FOR_DYNAMIC_BORDER_ICE",
  "HAUTEUR DE MESURE DU VENT":"HEIGHT_OF_MEASURED_WIND",
  "ELEVATION DU MODELE RELATIVE AU NIVEAU MOYEN DES OCEANS":"RELATIVE_MODEL_ELEVATION_FROM_MEAN_SEA_LEVEL",
  "ANGLE DU SOLEIL COUCHANT":"SUN_SET_ANGLE",
  "ANGLE DU SOLEIL LEVANT":"SUN_RISE_ANGLE",
  "CONSTANTE SOLAIRE":"SOLAR_CONSTANT",
  "ALBEDO DES GLACES":"ALBEDO_OF_ICE",
  "TEMPERATURE DE ROSEE":"DEWPOINT_TEMPERATURE",
  "VISIBILITE":"VISIBILITY",
  "LONGITUDE GLOBALE, EN DEGRES":"GLOBAL_LONGITUDE__IN_DEGREES",
  "LONGITUDE LOCALE, EN  DEGRES":"LOCAL_LONGITUDE__IN__DEGREES",
  "LONGITUDE EST OU OUEST":"EAST_OR_WEST_LONGITUDE",
  "INCLURE LA DYNAMIQUE DES GLACES":"INCLUDE_ICE_DYNAMICS",
  "AD NOMBRE DE DERIVEES":"AD_NUMBER_OF_DERIVATIVES",
  "AD NOMS DES DERIVEES":"AD_NAMES_OF_DERIVATIVES",
  "MASSE VOLUMIQUE DE L'EAU":"WATER_DENSITY",
  "VISCOSITE CINEMATIQUE DE L'EAU":"KINEMATIC_WATER_VISCOSITY",
  "CONST. POUR LE TRANSFERT THERMIQUE ENTRE L'EAU ET LA GLACE":"CONSTANT_FOR_HEAT_TRANSFER_BETWEEN_TURBULENT_WATER_AND_ICE",
  "CONST. POUR LE TRANSFERT THERMIQUE POUR L'EAU EN SURFUSION":"CONSTANT_FOR_HEAT_TRANSFER_FOR_SUPERCOOLED_TURBULENT_FLOW",
  "NOMBRE DE NUSSELT POUR LE TRANFERT THERMIQUE LAMINAIRE":"NUSSELT_NUMBER_FOR_HEAT_TRANSFER_BETWEEN_LAMINAR_WATER_AND_ICE",
  "CONSTANTE DE BOLTZMANN":"BOLTZMANN_CONSTANT__WM_2K_4_",
  "TEMPERATURE DE CONGELATION DE L'EAU":"FREEZING_POINT_OF_WATER",
  "TEMPERATURE D'EAU CRITIQUE POUR LA GLACE DE BORD STATIQUE":"CRITICAL_WATER_TEMPERATURE_FOR_STATIC_BORDER_ICE",
  "LARGEUR DU CHENAL POUR LE CALCUL DE LA TEMPERATURE DE SURFACE":"CHANNEL_WIDTH_FOR_THE_COMPUTATION_OF_SURFACE_TEMPERATURE",
  "CONCENTRATION MAXIMALE DU COUVERT DE GLACE":"CONCENTRATION_OF_SURFACE_ICE_WHEN_FORMATION",
  "PROCESSEURS PARALLELES":"PARALLEL_PROCESSORS",
  "BILAN THERMIQUE":"HEAT_BUDGET",
  "IMPACT DU COUVERT SUR L'HYDRODYNAMIQUE":"ICE_COVER_IMPACT_ON_HYDRODYNAMIC",
  "COLMATAGE DES GRILLES":"CLOGGING_ON_BARS",
  "GLACE DE BORD STATIQUE":"BORDER_ICE_COVER",
  "SALINITE":"SALINITY",
  "VERSION DU BILAN ENERGETIQUE":"ENERGY_BALANCE_VERSION",
  "OPTION DU SCHEMA POUR LA CROISSANCE THERMIQUE":"SCHEME_OPTION_FOR_THERMAL_GROWTH",
  "MODELE POUR LA NUCLEATION SECONDAIRE":"MODEL_FOR_THE_SECONDARY_NUCLEATION",
  "PARAMETRE NMAX POUR LA NUCLEATION SECONDAIRE":"SECONDARY_NUCLEATION_NMAX_PARAMETER",
  "MODELE POUR LA FLOCULATION ET RUPTURE":"MODEL_FOR_THE_FLOCCULATION_AND_BREAKUP",
  "PARAMETRE AFLOC POUR LA FLOCULATION":"FLOCCULATION_AFLOC_PARAMETER",
  "MODELE POUR L'ENSEMENCEMENT DU FRASIL":"MODEL_FOR_FRAZIL_SEEDING",
  "TAUX D'ENSEMENCEMENT DE FRASIL":"FRAZIL_SEEDING_RATE",
  "NOMBRE MINIMUM DE CRISTAUX DE FRASIL":"MINIMUM_NUMBER_OF_FRAZIL_CRYSTALS",
  "MODELE D'ECHANGES EAU-ATMOSPHERE":"ATMOSPHERE_WATER_EXCHANGE_MODEL",
  "MODELE POUR L'ESTIMATION DES PARAMETRES DE TURBULENCE":"MODEL_FOR_ESTIMATION_OF_TURBULENCE_PARAMETERS",
  "PRECIPITATION DU FRASIL":"FRAZIL_PRECIPITATION",
}

DicoCasEnToCata = {
  'STEERING FILE':'STEERING_FILE',
  'FORTRAN FILE':'FORTRAN_FILE',
  'TITLE':'TITLE',
  'BOUNDARY CONDITIONS FILE':'BOUNDARY_CONDITIONS_FILE',
  'GEOMETRY FILE':'GEOMETRY_FILE',
  'GEOMETRY FILE FORMAT':'GEOMETRY_FILE_FORMAT',
  'REFERENCE FILE':'REFERENCE_FILE',
  'REFERENCE FILE FORMAT':'REFERENCE_FILE_FORMAT',
  'RESULTS FILE':'RESULTS_FILE',
  'RESULTS FILE FORMAT':'RESULTS_FILE_FORMAT',
  'PREVIOUS ICE COVER COMPUTATION FILE':'PREVIOUS_ICE_COVER_COMPUTATION_FILE',
  'PREVIOUS ICE COVER COMPUTATION FILE FORMAT':'PREVIOUS_ICE_COVER_COMPUTATION_FILE_FORMAT',
  'PREVIOUS ICE BLOCKS COMPUTATION FILE':'PREVIOUS_ICE_BLOCKS_COMPUTATION_FILE',
  'PREVIOUS ICE BLOCKS COMPUTATION FILE FORMAT':'PREVIOUS_ICE_BLOCKS_COMPUTATION_FILE_FORMAT',
  'DICTIONARY':'DICTIONARY',
  'INITIAL CONDITIONS':'INITIAL_CONDITIONS',
  'VARIABLES FOR GRAPHIC PRINTOUTS':'VARIABLES_FOR_GRAPHIC_PRINTOUTS',
  'VARIABLES TO BE PRINTED':'VARIABLES_TO_BE_PRINTED',
  'GRAPHIC PRINTOUT PERIOD':'GRAPHIC_PRINTOUT_PERIOD',
  'LISTING PRINTOUT PERIOD':'LISTING_PRINTOUT_PERIOD',
  'MASS-BALANCE':'MASS_BALANCE',
  'VALIDATION':'VALIDATION',
  'LAW OF ICE COVER FRICTION':'LAW_OF_ICE_COVER_FRICTION',
  'FRICTION COEFFICIENT':'FRICTION_COEFFICIENT',
  'MAXIMAL FRICTION COEFFICIENT':'MAXIMAL_FRICTION_COEFFICIENT',
  'LAW FOR FRICTION COEFFICIENT':'LAW_FOR_FRICTION_COEFFICIENT',
  'EQUIVALENT SURFACE ICE THICKNESS':'EQUIVALENT_SURFACE_ICE_THICKNESS',
  'AIR DENSITY':'AIR_DENSITY',
  'ICE DENSITY':'ICE_DENSITY',
  'WATER SPECIFIC HEAT':'WATER_SPECIFIC_HEAT',
  'SPECIFIC HEAT OF ICE':'SPECIFIC_HEAT_OF_ICE',
  'LATENT HEAT OF ICE':'LATENT_HEAT_OF_ICE',
  'WATER-AIR HEAT EXCHANGE COEFFICIENT':'WATER_AIR_HEAT_EXCHANGE_COEFFICIENT',
  'WATER-AIR HEAT EXCHANGE CONSTANT':'WATER_AIR_HEAT_EXCHANGE_CONSTANT',
  'ICE-AIR HEAT EXCHANGE COEFFICIENT':'ICE_AIR_HEAT_EXCHANGE_COEFFICIENT',
  'ICE-AIR HEAT EXCHANGE CONSTANT':'ICE_AIR_HEAT_EXCHANGE_CONSTANT',
  'COEFFICIENT FOR CALIBRATION OF BACK RADIATION':'COEFFICIENT_FOR_CALIBRATION_OF_BACK_RADIATION',
  'COEFFICIENT FOR CALIBRATION OF EVAPORATIVE HEAT TRANSFERT':'COEFFICIENT_FOR_CALIBRATION_OF_EVAPORATIVE_HEAT_TRANSFERT',
  'COEFFICIENT FOR CALIBRATION OF CONDUCTIVE HEAT TRANSFERT':'COEFFICIENT_FOR_CALIBRATION_OF_CONDUCTIVE_HEAT_TRANSFERT',
  'COEFFICIENT FOR CALIBRATION OF PRECIPITATION HEAT TRANSFERT':'COEFFICIENT_FOR_CALIBRATION_OF_PRECIPITATION_HEAT_TRANSFERT',
  'THERMAL CONDUCTIVITY BETWEEN WATER AND FRAZIL':'THERMAL_CONDUCTIVITY_BETWEEN_WATER_AND_FRAZIL',
  'THERMAL CONDUCTIVITY OF BLACK ICE':'THERMAL_CONDUCTIVITY_OF_BLACK_ICE',
  'THERMAL CONDUCTIVITY OF SNOW':'THERMAL_CONDUCTIVITY_OF_SNOW',
  'POROSITY OF SURFACE ICE':'POROSITY_OF_SURFACE_ICE',
  'NUMBER OF CLASSES FOR SUSPENDED FRAZIL ICE':'NUMBER_OF_CLASSES_FOR_SUSPENDED_FRAZIL_ICE',
  'NUSSELT NUMBER':'NUSSELT_NUMBER',
  'MODEL FOR THE NUSSELT NUMBER':'MODEL_FOR_THE_NUSSELT_NUMBER',
  'FRAZIL CRYSTALS RADIUS':'FRAZIL_CRYSTALS_RADIUS',
  'FRAZIL CRYSTALS DIAMETER THICKNESS RATIO':'FRAZIL_CRYSTALS_DIAMETER_THICKNESS_RATIO',
  'MODEL FOR THE BUOYANCY VELOCITY':'MODEL_FOR_THE_BUOYANCY_VELOCITY',
  'SETTLING COEFFICIENT OF FRAZIL ON BARS':'SETTLING_COEFFICIENT_OF_FRAZIL_ON_BARS',
  'POROSITY OF ACCUMULATED ICE':'POROSITY_OF_ACCUMULATED_ICE',
  'ANGLE OF ACCUMULATED ICE':'ANGLE_OF_ACCUMULATED_ICE',
  'PHYSICAL CHARACTERISTICS OF THE INTAKE RACK':'PHYSICAL_CHARACTERISTICS_OF_THE_INTAKE_RACK',
  'CLOGGED BOUNDARY NUMBERS':'CLOGGED_BOUNDARY_NUMBERS',
  'CLOGGED SECTIONS':'CLOGGED_SECTIONS',
  'CLOGGING RESULTS FILE':'CLOGGING_RESULTS_FILE',
  'CRITICAL VELOCITY FOR STATIC BORDER ICE':'CRITICAL_VELOCITY_FOR_STATIC_BORDER_ICE',
  'CRITICAL VELOCITY FOR DYNAMIC BORDER ICE':'CRITICAL_VELOCITY_FOR_DYNAMIC_BORDER_ICE',
  'HEIGHT OF MEASURED WIND':'HEIGHT_OF_MEASURED_WIND',
  'RELATIVE MODEL ELEVATION FROM MEAN SEA LEVEL':'RELATIVE_MODEL_ELEVATION_FROM_MEAN_SEA_LEVEL',
  'SUN SET ANGLE':'SUN_SET_ANGLE',
  'SUN RISE ANGLE':'SUN_RISE_ANGLE',
  'SOLAR CONSTANT':'SOLAR_CONSTANT',
  'ALBEDO OF ICE':'ALBEDO_OF_ICE',
  'DEWPOINT TEMPERATURE':'DEWPOINT_TEMPERATURE',
  'VISIBILITY':'VISIBILITY',
  'GLOBAL LONGITUDE, IN DEGREES':'GLOBAL_LONGITUDE__IN_DEGREES',
  'LOCAL LONGITUDE, IN  DEGREES':'LOCAL_LONGITUDE__IN__DEGREES',
  'EAST OR WEST LONGITUDE':'EAST_OR_WEST_LONGITUDE',
  'INCLUDE ICE DYNAMICS':'INCLUDE_ICE_DYNAMICS',
  'AD NUMBER OF DERIVATIVES':'AD_NUMBER_OF_DERIVATIVES',
  'AD NAMES OF DERIVATIVES':'AD_NAMES_OF_DERIVATIVES',
  'WATER DENSITY':'WATER_DENSITY',
  'KINEMATIC WATER VISCOSITY':'KINEMATIC_WATER_VISCOSITY',
  'CONSTANT FOR HEAT TRANSFER BETWEEN TURBULENT WATER AND ICE':'CONSTANT_FOR_HEAT_TRANSFER_BETWEEN_TURBULENT_WATER_AND_ICE',
  'CONSTANT FOR HEAT TRANSFER FOR SUPERCOOLED TURBULENT FLOW':'CONSTANT_FOR_HEAT_TRANSFER_FOR_SUPERCOOLED_TURBULENT_FLOW',
  'NUSSELT NUMBER FOR HEAT TRANSFER BETWEEN LAMINAR WATER AND ICE':'NUSSELT_NUMBER_FOR_HEAT_TRANSFER_BETWEEN_LAMINAR_WATER_AND_ICE',
  'BOLTZMANN CONSTANT (WM-2K-4)':'BOLTZMANN_CONSTANT__WM_2K_4_',
  'FREEZING POINT OF WATER':'FREEZING_POINT_OF_WATER',
  'CRITICAL WATER TEMPERATURE FOR STATIC BORDER ICE':'CRITICAL_WATER_TEMPERATURE_FOR_STATIC_BORDER_ICE',
  'CHANNEL WIDTH FOR THE COMPUTATION OF SURFACE TEMPERATURE':'CHANNEL_WIDTH_FOR_THE_COMPUTATION_OF_SURFACE_TEMPERATURE',
  'CONCENTRATION OF SURFACE ICE WHEN FORMATION':'CONCENTRATION_OF_SURFACE_ICE_WHEN_FORMATION',
  'PARALLEL PROCESSORS':'PARALLEL_PROCESSORS',
  'HEAT BUDGET':'HEAT_BUDGET',
  'ICE COVER IMPACT ON HYDRODYNAMIC':'ICE_COVER_IMPACT_ON_HYDRODYNAMIC',
  'CLOGGING ON BARS':'CLOGGING_ON_BARS',
  'BORDER ICE COVER':'BORDER_ICE_COVER',
  'SALINITY':'SALINITY',
  'ENERGY BALANCE VERSION':'ENERGY_BALANCE_VERSION',
  'SCHEME OPTION FOR THERMAL GROWTH':'SCHEME_OPTION_FOR_THERMAL_GROWTH',
  'MODEL FOR THE SECONDARY NUCLEATION':'MODEL_FOR_THE_SECONDARY_NUCLEATION',
  'SECONDARY NUCLEATION NMAX PARAMETER':'SECONDARY_NUCLEATION_NMAX_PARAMETER',
  'MODEL FOR THE FLOCCULATION AND BREAKUP':'MODEL_FOR_THE_FLOCCULATION_AND_BREAKUP',
  'FLOCCULATION AFLOC PARAMETER':'FLOCCULATION_AFLOC_PARAMETER',
  'MODEL FOR FRAZIL SEEDING':'MODEL_FOR_FRAZIL_SEEDING',
  'FRAZIL SEEDING RATE':'FRAZIL_SEEDING_RATE',
  'MINIMUM NUMBER OF FRAZIL CRYSTALS':'MINIMUM_NUMBER_OF_FRAZIL_CRYSTALS',
  'ATMOSPHERE-WATER EXCHANGE MODEL':'ATMOSPHERE_WATER_EXCHANGE_MODEL',
  'MODEL FOR ESTIMATION OF TURBULENCE PARAMETERS':'MODEL_FOR_ESTIMATION_OF_TURBULENCE_PARAMETERS',
  'FRAZIL PRECIPITATION':'FRAZIL_PRECIPITATION',
}
DicoEnumCasFrToEnumCasEn = {
'GEOMETRY_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'REFERENCE_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'RESULTS_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
  "MED":"MED",
},

'PREVIOUS_ICE_COVER_COMPUTATION_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
},

'PREVIOUS_ICE_BLOCKS_COMPUTATION_FILE_FORMAT':{
  "SERAFIN":"SERAFIN",
  "SERAFIND":"SERAFIND",
},

'INITIAL_CONDITIONS':{
  ""SANS COUVERT DE GLACE"":""WITHOUT ICE COVER"",
  ""COUVERT DE GLACE CONSTANT"":""CONSTANT ICE COVER"",
  ""PARTICULIERES"":""SPECIAL"",
  ""SPECIAL"":""PARTICULIERES"",
  ""PARTICULAR"":""PARTICULAR"",
},

'VARIABLES_TO_BE_PRINTED':{
  "A EDITER":"TO BE EDITED",
},

}
