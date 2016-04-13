DicoEnumCasEn={
'Psi_Scheme_Option' : { 
    1 : "Explicit",
    2 : "Predictor-corrector"
  },

'Type_Of_Advection' : {
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
 
'Geometry_File_Format' : {
    'SERAFIN': 'Serafin',
    'MED': 'MED',
    'SERAFIND': 'SerafinD',
  },

'Previous_Computation_File_Format' : {
    'SERAFIN': 'Serafin',
    'MED': 'MED',
    'SERAFIND': 'SerafinD',
  },
 
'Reference_File_Format' : {
    'SERAFIN': 'Serafin',
    'MED': 'MED',
    'SERAFIND': 'SerafinD',
  },

'Results_File_Format' : {
    'SERAFIN': 'Serafin',
    'MED': 'MED',
    'SERAFIND': 'SerafinD',
     },

'Preconditioning'  : {
    0 : "No preconditioning", 
    2 : "Diagonal",
    3 : "Diagonal condensee",
    7 : "Crout",
    11 : "Gauss-Seidel", 
    14 : "Diagonal and Crout", 
    21 : "Diagonal condensed and Crout"
   },

'Initial_Guess_For_H'  : {
    1 : "Previous", 
    0 : "Zero", 
    2 : "Extrapolation" 
  },
 
'Law_Of_Bottom_Friction' : {
    0 : "No friction", 
    1 : "Haaland", 
    2 : "Chezy", 
    3 : "Strickler", 
    4 : "Manning", 
    5 : "Nikuradse" 
  },
 
'Solver_For_Diffusion_Of_Tracers' : {
    1 : "Conjugate gradient", 
    2 : "Conjugate residual", 
    3 : "Conjugate gradient on a normal equation", 
    4 : "Minimum error", 
    5 : "Squared conjugate gradient", 
    6 : "CGSTAB", 
    7 : "GMRES", 
    8 : "Direct" 
  },

'Solver' : {
    3 : "Conjugate gradient on a normal equation", 
    1 : "Conjugate gradient", 
    2 : "Conjugate residual", 
    4 : "Minimum error", 
    6 : "CGSTAB", 
    7 : "GMRES", 
    8 : "Direct" 
  },
 
'Preconditioning_For_Diffusion_Of_Tracers' : {
    2 : "Diagonal",
    0 : "No preconditioning", 
    3 : "Diagonal condensed",
    7 : "Crout", 
    14 : "Diagonal and Crout",
    21 : "Diagonal condensed and Crout" 
  },

'Solver_For_K_Epsilon_Model' : {
    1 : "Conjugate gradient", 
    2 : "Conjugate residuals", 
    3 : "Conjugate gradient on normal equation", 
    4 : "Minimum error", 
    5 : "Conjugate gradient squared", 
    6 : "Conjugate gradient squared stabilised (CGSTAB)", 
    7 : "GMRES", 
    8 : "Direct" 
  },

'Preconditioning_For_K_Epsilon_Model' : {
    2 : "Diagonal",
    0 : "No preconditioning", 
    3 : "Diagonal condensed",
    7 : "Crout", 
    14 : "Diagonal and Crout",
    21 : "Diagonal condensed and Crout" 
  },

'Turbulence_Model_For_Solid_Boundaries' : {
    1 : "Smooth",
    2 : "Rough" 
  },

'PNPN_Friction_Coefficient' : {
    1 : "Linear coefficient",
    2 : "Chezy coefficient",
    3 : "Strickler coefficient",
    4 : "Manning coefficient",
    5 : "Nikuradse grain size",
  },
 

'Turbulence_Model' : {
    1 : "Constant viscosity",
    2 : "Elder",
    3 : "K-Epsilon Model", 
    4 : "Smagorinski",
  },
 

 
'Roughness_Coefficient_Of_Boundaries' : {
    1 : "Non programme",
    2 : "Coefficient de Chezy",
    3 : "Coefficient de Strickler",
    4 : "Coefficient de Manning",
    5 : "Hauteur de rugosite de Nikuradse",
  },
 

'Variables_For_Graphic_Printouts' : {
    "U" : "Velocity along X axis (m/s)", 
    "V" : "Velocity along Y axis (m/s)", 
    "C" : "Wave celerity (m/s)", 
    "H" : "Water depth (m)", 
    "S" : "Free surface elevation (m)", 
    "B" : "Bottom elevation (m)", 
    "F" : "Froude number", 
    "Q" : "Scalar flowrate of fluid (m2/s)", 
    "T1" : "Tracer 1 etc. ", 
    "K" : "Turbulent kinetic energy in K-Epsilon model (J/kg)", 
    "E" : "Dissipation of turbulent energy (W/kg)", 
    "D" : "Turbulent viscosity of K-Epsilon model (m2/s)", 
    "I" : "Flowrate along X axis (m2/s)", 
    "J" : "Flowrate along Y axis (m2/s)", 
    "M" : "Scalar velocity (m/s)", 
    "X" : "Wind along X axis (m/s)", 
    "Y" : "Wind along Y axis (m/s)", 
    "P" : "Air pressure (Pa)", 
    "W" : "Friction coefficient", 
    "A" : "Drift along X (m)", 
    "G" : "Drift along Y (m)", 
    "L" : "Courant number", 
    "N" : "Supplementary variable N", 
    "O" : "Supplementary variable O", 
    "R" : "Supplementary variable R", 
    "Z" : "Supplementary variable Z", 
    "MAXZ" : "Maximum elevation", 
    "TMXZ" : "Time of maximum elevation", 
    "MAXV" : "Maximum velocity", 
    "TMXV" : "Time of maximum velocity", 
    "US" : "Friction velocity" 
  },
 
'Variables_TO_Be_Printed' : {
    "U" : "Velocity along X axis (m/s)", 
    "V" : "Velocity along Y axis (m/s)", 
    "C" : "Wave celerity (m/s)", 
    "H" : "Water depth (m)", 
    "S" : "Free surface elevation (m)", 
    "B" : "Bottom elevation (m)", 
    "F" : "Froude number", 
    "Q" : "Scalar flowrate of fluid (m2/s)", 
    "T" : "Tracer", 
    "K" : "Turbulent kinetic energy in K-Epsilon model (J/kg)", 
    "E" : "Dissipation of turbulent energy (W/kg)", 
    "D" : "Turbulent viscosity of K-Epsilon model (m2/s)", 
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
 
 
'Initial_Conditions' : {
    "ZERO ELEVATION" : "Zero elevation",
    "CONSTANT ELEVATION" :  "Constant elevation", 
    "ZERO Depth" : "Zero depth",
    "CONSTANT Depth" : "Constant depth",
    "SPECIAL"  : "Special" ,
    "TPXO SATELLITE ALTIMETRY" : "TPXO satellite altimetry",
  },
 
'Supg_Option_U_And_V' : {
   0 : "No upwinding", 
   1 : "Classical SUPG",
   2 : "Modified SUPG"
  }, 

'Option_For_The_Treatment_Of_Tidal_Flats' : {
    1 : "Equations solved everywhere with correction on tidal flats",
    2 : "Dry elements frozen",
    3 : "1 but with porosity (defina method)",
  },
 
'Initial_Guess_For_U' : {
    0 : "Zero",
    1 : "Previous",
    2 : "Extrapolation", 
  },
 
'Discretizations_In_Space' : {
    11 : "Linear",
    12 : "Quasi-bubble",
    13 : "Quadratic",
  },
 
'Matrix_Vector_Product' : {
    1 : "Classic", 
    2 : "Frontal"
  },

'Matrix_Storage' : {
    1 : "Classical EBE" , 
    3 : "Edge-based storage" 
  },
'Option_For_Liquid_Boundaries' : {
    1 : "Classical boundary conditions",
    2 : "Thompson method based on characteristics",
  },
 
'Treatment_Of_The_Linear_System' : {
    1 : "Coupled",
    2 : "Wave equation"
},
 
'Equations' : {
   "SAINT-VENANT EF" : "Saint-Venant EF",
   "SAINT-VENANT VF" : "Saint-Venant VF",
   "BOUSSINESQ" : "Boussinesq" 
  },

'Velocity_ProFiles' : {
    1 : "Constant normal profile",
    2 : "U and V given in the conlim file",
    3 : "Normal velocity given in ubor in the conlim file",
    4 : "Velocity proportional to square root of depth",
    5 : "Velocity proportional to square root of depth, variant",
    5 : "QRT(depth) profile, variant",
  },
                                                                    
'Option_For_The_Diffusion_Of_Tracers' : {
    1 : "Div( nu grad(T) )",                                           
    2 : "1/h Div ( h nu grad(T)" ,                                              
  },

'Option_For_The_Diffusion_Of_Velocities' : { 
    1 : "Normal",
    2 : "Dirac"                                            
  },
 
 
'Parameter_Estimation' : {
    "Friction" : "Friction",
    "FROTTEMENT" : "Frottement", 
    "STEADY" : "Steady" 
  },
 

'Identification_Method' : {
    0 : "List of tests",  
    1 : "Gradient simple", 
    2 : "Conj gradient", 
    3 : "Lagrange interp." 
  },
 

'Finite_Volume_Scheme' : {
    0 : "Roe scheme",
    1 : "kinetic order 1", 
    2 : "kinetic order 2", 
    3 : "Zokagoa scheme order 1", 
    4 : "Tchamen scheme order 1", 
    5 : "HLLC scheme order 1", 
    6 : "WAF scheme order 2"
  },

'Stage-Discharge_Curves' : {
    0 : "No one",
    1 : "Z(Q)",
    2 : "Q(Z)" 
  },

'Treatment_Of_Negative_Depths' : {
    0 : "No treatment",
    1 : "Smoothing",
    2 : "Flux control",
  },

'Depth_In_Friction_Terms' : {
    1 : "Nodal",
    2 : "Average", 
  },

'Law_Of_Friction_On_Lateral_Boundaries' : {
    0 : "No friction", 
    1 : "Haaland", 
    2 : "Chezy", 
    3 : "Strickler", 
    4 : "Manning", 
    5 : "Nikuradse", 
    6 : "Log law", 
    7 : "Colebrook-white" 
  },
 

'Treatment_Of_Fluxes_AT_The_Boundaries': {
    1 : "Priority to prescribed values",
    2 : "Priority to fluxes",
  },

'Option_For_Tidal_Boundary_Conditions': {
    0 : "No tide",
    1 : "Real tide (recommended methodology)",
    2 : "Astronomical tide",
    3 : "Mean spring tide",
    4 : "Mean tide",
    5 : "Mean neap tide",
    6 : "Astronomical neap tide",
    7 : "Real tide (methodology before 2010)"
  },

'Option_For_Tsunami_Generation': {
    0 : "No Tsunami",
    1 : "Tsunami generated on the basis of the Okada model 1992"
  },

#'PHYSICAL Characteristics Of The TSUNAMI': {
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

'Tidal_Data_Base': {
    1 : "JMJ",
    2 : "TPXO",
    3 : "Miscellaneous (LEGOS-NEA, FES20XX, PREVIMER...)"
  },

'Geographic_System': {
    0 : "Defined by user",
    1 : "WGS84 longitude/latitude in real degrees",
    2 : "WGS84 northern UTM",
    3 : "WGS84 southern UTM",
    4 : "Lambert",
    5 : "Mercator"
  },


'Zone_Number_In_Geographic_System': {
    1 : "Lambert 1 north",
    2 : "Lambert 2 center",
    3 : "Lambert 3 south",
    4 : "Lambert 4 corsica",
    22 : "Lambert 2 extended",
    30 : "UTM zone, E.G."
  },


'Law_Of_Tracers_Degradation': {
    0 : "No degradation",
    1 : "F(T90) law"
  },

'Spatial_Projection_Type': {
    1 : "Cartesian, not georeferenced",
    2 : "Mercator",
    3 : "Latitude longitude"
  },

'Algae_Type': {
    1 : "Sphere",
    2 : "Iridaea flaccida (close to ulva)",
    3 : "Pelvetiopsis limitata",
    4 : "Gigartina leptorhynchos"
  },

'Option_For_Characteristics': {
    1 : "Strong",
    2 : "Weak"
  },

'Stochastic_Diffusion_Model' : {
    0 : "No model",    
    2 : "??"
  },

'Number_Of_Gauss_Points_For_Weak_Characteristics' : {
    1 : "1 point",
    3 : "3 points",
    6 : "6 points"
  },

'Type_Of_Weirs': {
    1 : "Horizontal with same number of nodes upstream/downstream (Historical solution with bord)",
    2 : "General (New solution with sources points)"
  },

'Scheme_For_Advection_Of_Velocities': {
    1 : "Characteristics",
    2 : "Explicit + SUPG",
    3 : "Explicit leo postma",
    4 : "Explicit + murd scheme N",
    5 : "Explicit + murd scheme PSI",
    13 : "N-scheme for tidal flats",
    14 : "N-scheme for tidal flats"
  },

'Scheme_For_Advection_Of_Tracers': {
    0 : "No advection",
    1 : "Characteristics",
    2 : "Explicit + SUPG",
    3 : "Explicit leo postma",
    4 : "Explicit + murd scheme N",
    5 : "Explicit + murd scheme PSI",
    13 : "Leo postma for tidal flats",
    14 : "N-scheme for tidal flats"
  },


'Scheme_For_Advection_Of_K_Epsilon': {
    0 : "No advection",
    1 : "Characteristics",
    2 : "Explicit + SUPG",
    3 : "Explicit leo postma",
    4 : "Explicit + murd scheme N",
    5 : "Explicit + murd scheme PSI",
    13 : "Leo postma for tidal flats",
    14 : "N-scheme for tidal flats"
  },


'Scheme_Option_For_Advection_Of_Tracers': {
    1 : "explicit",
    2 : "predictor-corrector",
  },


'Scheme_Option_For_Advection_Of_Velocities': {
    1 : "Explicit",
    2 : "Predictor-corrector",
  },

'Scheme_Option_For_Advection_Of_K_Epsilon': {
    1 : "Explicit",
    2 : "Predictor-corrector",
  },

'Option_For_Wind': {
    0 :  "No wind",
    1 :  "Constant in time and space",
    2 :  "Variable in time and (constant in space)",
    3 :  "Variable in time and space"  
  },

'Newmark_Time_Integration_Coefficient' :{
   1. :  "Euler explicit",
   0.5 : "order 2 in time",
  },
}
