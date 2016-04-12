DicoEnumCasEn={
'PSI SCHEME OPTION' : { 
    1 : "Explicit",
    2 : "Predictor-corrector"
  },

'TYPE OF ADVECTION' : {
    1 : "Characteristics", 
    2 : "SUPG", 
    3 : "Conservative N-scheme", 
    4 : "Conservative N-scheme", 
    5 : "Conservative PSI-scheme", 
    6 : "Non conservative PSI-scheme", 
    7 : "Implicit non conservative N-scheme", 
    13 : "Edge-based N-scheme", 
    14 : "Edge-based N-scheme" 
  },
 
'GEOMETRY FILE FORMAT' : {
    'SERAFIN': 'Serafin',
    'MED': 'MED',
    'SERAFIND': 'SerafinD',
  },

'PREVIOUS COMPUTATION FILE FORMAT' : {
    'SERAFIN': 'Serafin',
    'MED': 'MED',
    'SERAFIND': 'SerafinD',
  },
 
'REFERENCE FILE FORMAT' : {
    'SERAFIN': 'Serafin',
    'MED': 'MED',
    'SERAFIND': 'SerafinD',
  },

'RESULTS FILE FORMAT' : {
    'SERAFIN': 'Serafin',
    'MED': 'MED',
    'SERAFIND': 'SerafinD',
     },

'PRECONDITIONING'  : {
    0 : "No preconditioning", 
    2 : "Diagonal",
    3 : "Diagonal condensee",
    7 : "Crout",
    11 : "Gauss-Seidel", 
    14 : "Diagonal and Crout", 
    21 : "Diagonal condensed and Crout"
   },

'INITIAL GUESS FOR H'  : {
    1 : "Previous", 
    0 : "Zero", 
    2 : "Extrapolation" 
  },
 
'LAW OF BOTTOM FRICTION' : {
    0 : "No friction", 
    1 : "Haaland", 
    2 : "Chezy", 
    3 : "Strickler", 
    4 : "Manning", 
    5 : "Nikuradse" 
  },
 
'SOLVER FOR DIFFUSION OF TRACERS' : {
    1 : "Conjugate gradient", 
    2 : "Conjugate residual", 
    3 : "Conjugate gradient on a normal equation", 
    4 : "Minimum error", 
    5 : "Squared conjugate gradient", 
    6 : "CGSTAB", 
    7 : "GMRES", 
    8 : "Direct" 
  },

'SOLVER' : {
    3 : "Conjugate gradient on a normal equation", 
    1 : "Conjugate gradient", 
    2 : "Conjugate residual", 
    4 : "Minimum error", 
    6 : "CGSTAB", 
    7 : "GMRES", 
    8 : "Direct" 
  },
 
'PRECONDITIONING FOR DIFFUSION OF TRACERS' : {
    2 : "Diagonal",
    0 : "No preconditioning", 
    3 : "Diagonal condensed",
    7 : "Crout", 
    14 : "Diagonal and Crout",
    21 : "Diagonal condensed and Crout" 
  },

'SOLVER FOR K-EPSILON MODEL' : {
    1 : "Conjugate gradient", 
    2 : "Conjugate residuals", 
    3 : "Conjugate gradient on normal equation", 
    4 : "Minimum error", 
    5 : "Conjugate gradient squared", 
    6 : "Conjugate gradient squared stabilised (CGSTAB)", 
    7 : "GMRES", 
    8 : "Direct" 
  },

'PRECONDITIONING FOR K-EPSILON MODEL' : {
    2 : "Diagonal",
    0 : "No preconditioning", 
    3 : "Diagonal condensed",
    7 : "Crout", 
    14 : "Diagonal and Crout",
    21 : "Diagonal condensed and Crout" 
  },

'TURBULENCE MODEL FOR SOLID BOUNDARIES' : {
    1 : "Smooth",
    2 : "Rough" 
  },

'FRICTION COEFFICIENT' : {
    1 : "Linear coefficient",
    2 : "Chezy coefficient",
    3 : "Strickler coefficient",
    4 : "Manning coefficient",
    5 : "Nikuradse grain size",
  },
 

'TURBULENCE MODEL' : {
    1 : "Constant viscosity",
    2 : "Elder",
    3 : "K-Epsilon Model", 
    4 : "Smagorinski",
  },
 

 
'ROUGHNESS COEFFICIENT OF BOUNDARIES' : {
    1 : "Non programme",
    2 : "Coefficient de Chezy",
    3 : "Coefficient de Strickler",
    4 : "Coefficient de Manning",
    5 : "Hauteur de rugosite de Nikuradse",
  },
 

'VARIABLES FOR GRAPHIC PRINTOUTS' : {
    "U" : "Velocity along X axis  (m/s)", 
    "V" : "Velocity along Y axis  (m/s)", 
    "C" : "Wave celerity  (m/s)", 
    "H" : "Water depth  (m)", 
    "S" : "Free surface elevation  (m)", 
    "B" : "Bottom elevation  (m)", 
    "F" : "Froude number  ", 
    "Q" : "Scalar flowrate of fluid  (m2/s)", 
    "T1" : "Tracer 1 etc. ", 
    "K" : "Turbulent kinetic energy in k-epsilon model  (J/kg)", 
    "E" : "Dissipation of turbulent energy  (W/kg)", 
    "D" : "Turbulent viscosity of k-epsilon model  (m2/s)", 
    "I" : "Flowrate along X axis  (m2/s)", 
    "J" : "Flowrate along Y axis  (m2/s)", 
    "M" : "Scalar velocity  (m/s)", 
    "X" : "Wind along X axis  (m/s)", 
    "Y" : "Wind along Y axis  (m/s)", 
    "P" : "Air pressure  (Pa)", 
    "W" : "Friction coefficient", 
    "A" : "Drift along X  (m)", 
    "G" : "Drift along Y  (m)", 
    "L" : "Courant number", 
    "N" : "Supplementary variable N ", 
    "O" : "Supplementary variable O ", 
    "R" : "Supplementary variable R ", 
    "Z" : "Supplementary variable Z  ", 
    "MAXZ" : "Maximum elevation", 
    "TMXZ" : "Time of maximum elevation ", 
    "MAXV" : "Maximum velocity", 
    "TMXV" : "Time of maximum velocity", 
    "US" : "Friction velocity  " 
  },
 
'VARIABLES TO BE PRINTED' : {
    "U" : "Velocity along X axis (m/s)", 
    "V" : "Velocity along Y axis (m/s)", 
    "C" : "Wave celerity (m/s)", 
    "H" : "Water depth (m)", 
    "S" : "Free surface elevation (m)", 
    "B" : "Bottom elevation (m)", 
    "F" : "Froude number", 
    "Q" : "Scalar flowrate of fluid (m2/s)", 
    "T" : "Tracer", 
    "K" : "Turbulent kinetic energy in k-epsilon model (J/kg)", 
    "E" : "Dissipation of turbulent energy (W/kg)", 
    "D" : "Turbulent viscosity of k-epsilon model (m2/s)", 
    "I" : "Flowrate along X axis (m2/s)", 
    "J" : "Flowrate along Y axis (m2/s)", 
    "M" : "Scalar velocity (m/s)", 
    "X" : "Wind along X axis (m/s)", 
    "Y" : "Wind along Y axis (m/s)", 
    "P" : "Air pressure (Pa)", 
    "W" : "Friction coefficient", 
    "A" : "Drift along X  (m)", 
    "G" : "Drift along Y  (m)", 
    "L" : "Nombre de courants ", 
    "N" : "Supplementary variable N", 
    "O" : "Supplementary variable O", 
    "R" : "Supplementary variable R", 
    "Z" : "Supplementary variable Z" 
  },
 
 
'INITIAL CONDITIONS' : {
    "ZERO ELEVATION" : "Zero elevation",
    "CONSTANT ELEVATION" :  "Constant elevation", 
    "ZERO DEPTH" : "Zero depth",
    "CONSTANT DEPTH" : "Constant depth",
    "SPECIAL"  : "Special" ,
    "TPXO SATELLITE ALTIMETRY" : "TPXO satellite altimetry",
  },
 
'SUPG_OPTION_U_AND_V' : {
   0 : "No upwinding", 
   1 : "Classical SUPG",
   2 : "Modified SUPG"
  }, 

'OPTION FOR THE TREATMENT OF TIDAL FLATS' : {
    1 : "Equations solved everywhere with correction on tidal flats",
    2 : "Dry elements frozen",
    3 : "1 but with porosity (defina method)",
  },
 
'INITIAL GUESS FOR U' : {
    0 : "Zero",
    1 : "Previous",
    2 : "Extrapolation", 
  },
 
'DISCRETIZATIONS IN SPACE' : {
    11 : "Linear",
    12 : "Quasi-bubble",
    13 : "Quadratic",
  },
 
'MATRIX VECTOR PRODUCT' : {
    1 : "Classic", 
    2 : "Frontal"
  },

'MATRIX STORAGE' : {
    1 : "Classical EBE" , 
    3 : "Edge-based storage" 
  },
'OPTION FOR LIQUID BOUNDARIES' : {
    1 : "Classical boundary conditions",
    2 : "Thompson method based on characteristics",
  },
 
'TREATMENT OF THE LINEAR SYSTEM' : {
    1 : "Coupled",
    2 : "Wave equation"
},
 
'EQUATIONS' : {
   "SAINT-VENANT EF" : "Saint-Venant EF",
   "SAINT-VENANT VF" : "Saint-Venant VF",
   "BOUSSINESQ" : "Boussinesq" 
  },

'VELOCITY PROFILES' : {
    1 : "Constant normal profile",
    2 : "U and V given in the conlim file",
    3 : "Normal velocity given in ubor in the conlim file",
    4 : "Velocity proportional to square root of depth",
    5 : "Velocity proportional to square root of depth, variant",
    5 : "QRT(depth) profile, variant",
  },
                                                                    
'OPTION FOR THE DIFFUSION OF TRACERS' : {
    1 : "Div( nu grad(T) )",                                           
    2 : "1/h Div ( h nu grad(T)" ,                                              
  },

'OPTION FOR THE DIFFUSION OF VELOCITIES' : { 
    1 : "Normal",
    2 : "Dirac"                                            
  },
 
 
'PARAMETER ESTIMATION' : {
    "FRICTION" : "Friction",
    "FROTTEMENT" : "Frottement", 
    "STEADY" : "Steady" 
  },
 

'IDENTIFICATION METHOD' : {
    0 : "List of tests",  
    1 : "Gradient simple", 
    2 : "Conj gradient", 
    3 : "Lagrange interp." 
  },
 

'FINITE VOLUME SCHEME' : {
    0 : "Roe scheme",
    1 : "kinetic order 1", 
    2 : "kinetic order 2", 
    3 : "Zokagoa scheme order 1", 
    4 : "Tchamen scheme order 1", 
    5 : "HLLC scheme order 1", 
    6 : "WAF scheme order 2"
  },

'STAGE-DISCHARGE CURVES' : {
    0 : "No one",
    1 : "Z(Q)",
    2 : "Q(Z)" 
  },

'TREATMENT OF NEGATIVE DEPTHS' : {
    0 : "No treatment",
    1 : "Smoothing",
    2 : "Flux control",
  },

'DEPTH IN FRICTION TERMS' : {
    1 : "Nodal",
    2 : "Average", 
  },

'LAW OF FRICTION ON LATERAL BOUNDARIES' : {
    0 : "No friction", 
    1 : "Haaland", 
    2 : "Chezy", 
    3 : "Strickler", 
    4 : "Manning", 
    5 : "Nikuradse", 
    6 : "Log law", 
    7 : "Colebrook-white" 
  },
 

'TREATMENT OF FLUXES AT THE BOUNDARIES': {
    1 : "Priority to prescribed values",
    2 : "Priority to fluxes",
  },

'OPTION FOR TIDAL BOUNDARY CONDITIONS': {
    0 : "No tide",
    1 : "Real tide (recommended methodology)",
    2 : "Astronomical tide",
    3 : "Mean spring tide",
    4 : "Mean tide",
    5 : "Mean neap tide",
    6 : "Astronomical neap tide",
    7 : "Real tide (methodology before 2010)"
  },

'OPTION FOR TSUNAMI GENERATION': {
    0 : "No Tsunami",
    1 : "Tsunami generated on the basis of the Okada model 1992"
  },

#'PHYSICAL CHARACTERISTICS OF THE TSUNAMI': {
#AIDE1  :      '
#    Physical characteristics of the chosen Tsunami model:
# - the focal depth (HH),
# - the fault length (L),
# - the fault width (W)
# - the dislocation (D),
# - the strike direction (TH),
# - the dip angle (DL),
# - the slip (RD),
# - the epicentre latitude (Y0) and
# - the epicentre longitude (X0)
# - the ellipse ( WxL ) area of influence    
# },

'TIDAL DATA BASE': {
    1 : "JMJ",
    2 : "TPXO",
    3 : "Miscellaneous (LEGOS-NEA, FES20XX, PREVIMER...)"
  },

'GEOGRAPHIC SYSTEM': {
    0 : "Defined by user",
    1 : "WGS84 longitude/latitude in real degrees",
    2 : "WGS84 northern UTM",
    3 : "WGS84 southern UTM",
    4 : "Lambert",
    5 : "Mercator"
  },


'ZONE NUMBER IN GEOGRAPHIC SYSTEM': {
    1 : "Lambert 1 north",
    2 : "Lambert 2 center",
    3 : "Lambert 3 south",
    4 : "Lambert 4 corsica",
    22 : "Lambert 2 extended",
    30 : "UTM zone, E.G."
  },


'LAW OF TRACERS DEGRADATION': {
    0 : "No degradation",
    1 : "F(T90) law"
  },

'SPATIAL PROJECTION TYPE': {
    1 : "Cartesian, not georeferenced",
    2 : "Mercator",
    3 : "Latitude longitude"
  },

'ALGAE TYPE': {
    1 : "Sphere",
    2 : "Iridaea flaccida (close to ulva)",
    3 : "Pelvetiopsis limitata",
    4 : "Gigartina leptorhynchos"
  },

'OPTION FOR CHARACTERISTICS': {
    1 : "Strong",
    2 : "Weak"
  },

'STOCHASTIC DIFFUSION MODEL' : {
    0 : "No model",    
    2 : "??"
  },

'NUMBER OF GAUSS POINTS FOR WEAK CHARACTERISTICS' : {
    1 : "1 point",
    3 : "3 points",
    6 : "6 points"
  },

'TYPE OF WEIRS': {
    1 : "Horizontal with same number of nodes upstream/downstream (Historical solution with bord)",
    2 : "General (New solution with sources points)"
  },

'SCHEME FOR ADVECTION OF VELOCITIES': {
    1 : "Characteristics",
    2 : "Explicit + SUPG",
    3 : "Explicit leo postma",
    4 : "Explicit + murd scheme N",
    5 : "Explicit + murd scheme PSI",
    13 : "N-scheme for tidal flats",
    14 : "N-scheme for tidal flats"
  },

'SCHEME FOR ADVECTION OF TRACERS': {
    0 : "No advection",
    1 : "Characteristics",
    2 : "Explicit + SUPG",
    3 : "Explicit leo postma",
    4 : "Explicit + murd scheme N",
    5 : "Explicit + murd scheme PSI",
    13 : "Leo postma for tidal flats",
    14 : "N-scheme for tidal flats"
  },


'SCHEME FOR ADVECTION OF K-EPSILON': {
    0 : "No advection",
    1 : "Characteristics",
    2 : "Explicit + SUPG",
    3 : "Explicit leo postma",
    4 : "Explicit + murd scheme N",
    5 : "Explicit + murd scheme PSI",
    13 : "Leo postma for tidal flats",
    14 : "N-scheme for tidal flats"
  },


'SCHEME OPTION FOR ADVECTION OF TRACERS': {
    1 : "explicit",
    2 : "predictor-corrector",
  },


'SCHEME OPTION FOR ADVECTION OF VELOCITIES': {
    1 : "Explicit",
    2 : "Predictor-corrector",
  },

'SCHEME OPTION FOR ADVECTION OF K-EPSILON': {
    1 : "Explicit",
    2 : "Predictor-corrector",
  },

'OPTION FOR WIND': {
    0 :  "No wind",
    1 :  "Constant in time and space",
    2 :  "Variable in time and (constant in space)",
    3 :  "Variable in time and space"  
  },

'NEWMARK TIME INTEGRATION COEFFICIENT' :{
   1. :  "Euler explicit",
   0.5 : "order 2 in time",
  },
}
