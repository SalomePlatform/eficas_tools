#)# -*- coding: utf-8 -*-
#
## --------------------------------------------------
## debut entete
## --------------------------------------------------
#
from Accas import *
import os
import sys
from prefs_MAP import PATH_MAP


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
                #regles=(AU_MOINS_UN('DISPL',),A_CLASSER('RBM','DISPL'))
                       )# Fin JDC_CATA
#
specter_path=PROC(nom="specter_path",op= None,
              path = SIMP ( typ = 'TXM', defaut=PATH_MAP+"perfect_dev/tools/bin/specter",
                            statut='o', fr = "", ang = "specter_path ", max=1,
                          ),
)
residual_energy_model=PROC(nom="residual_energy_model",op= None,
              beta =  FACT (statut='o', max=1,
                      ang = "total number of surviving point defects for cascades in iron up",
                      name= SIMP(statut= "f",typ = 'TXM', ang = "",max=1),
                      value=SIMP(statut= "o",typ = 'R', defaut=0.779, max=1),
                      unit= SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                      ),
              alpha =  FACT (statut='o', max=1,
                      name= SIMP(statut= "f",typ = 'TXM', ang = "",max=1),
                      value=SIMP(statut= "o",typ = 'R', defaut=5.67, ang = "",max=1,),
                      unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                      ),
)
mfvisc2_path=PROC(nom="mfvisc2_path",op= None,
              path = SIMP ( typ = 'TXM', defaut=PATH_MAP+"perfect_dev/tools/bin/mfvisc",
                            statut='o', fr = "", ang = "specter_path ", max=1,
                          ),
)

mfvisc2_parametrisation=PROC(nom="mfvisc2_parametrisation",op= None,
              stop_if_solute_loss=SIMP (statut= "f",typ = 'TXM', 
                            ang = "Yes if you want the rate-theory calculation to stop when a solute loss is detected",
                            defaut="No",into=("Yes","No")
                          ),
              bound_solute=SIMP (statut= "f",typ = 'TXM', 
                            ang = "Yes if you want the to artifically impose the solute conservation by imposing a null flux for concentrations at Nob",
                            defaut="Yes",into=("Yes","No") 
                          ),
              numerical_scheme_i =  FACT (statut='o', max=1,
                      ang="Numerical parameters scheme for interstitial",
                      No=FACT(statut='o', max=1,
                         ang='Number of discrete equations for species i',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='No_i', ang = "",max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=30,into=(30,), ang = "",max=1,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      Nc=FACT(statut='o', max=1,
                         ang='Number of continous equations for species i',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='Nc_i', ang = "",max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=300, ang = "",max=1,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      M=FACT(statut='o', max=1, ang='Step value for species i',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='M_i', max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=50, max=1,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      kmet=FACT(statut='o', max=1, ang='Step value for species i',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='kmet_i', max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=97, max=1,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      species=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                      ),
              numerical_scheme_b =  FACT (statut='o', max=1,
                      ang="Numerical parameters scheme for the solute element",
                      No=FACT(statut='o', max=1,
                         ang='Number of discrete equations for species b',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='No_b', ang = "",max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=0, ang = "",max=1,val_min=0,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      Nc=FACT(statut='o', max=1,
                         ang='Number of continous equations for species b',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='Nc_b', ang = "",max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=0, ang = "",max=1,val_min=0,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      M=FACT(statut='o', max=1, ang='Step value for species b',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='M_b', max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=0, max=1,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      kmet=FACT(statut='o', max=1, ang='Step value for species b',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='kmet_b', max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=0, max=1,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      species=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                      ),
              numerical_scheme_v =  FACT (statut='o', max=1,
                      ang="Numerical parameters scheme for vacancies",
                      No=FACT(statut='o', max=1,
                         ang='Number of discrete equations for species v',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='No_v', ang = "",max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=30, ang = "",max=1,val_min=0,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      Nc=FACT(statut='o', max=1,
                         ang='Number of continous equations for species v',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='Nc_v', ang = "",max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=300, ang = "",max=1,val_min=0,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      M=FACT(statut='o', max=1, ang='Step value for species v',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='M_v', max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=30, max=1,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      kmet=FACT(statut='o', max=1, ang='Step value for species v',
                         name=SIMP(statut= "f", typ = 'TXM', defaut='kmet_v', max=1,),
                         value=SIMP(statut= "o",typ = 'I', defaut=55, max=1,),
                         unit=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                              ),
                      species=SIMP (statut= "f",typ = 'TXM', ang = "",max=1),
                      ),

              ignore_Helium = SIMP (statut= "f",typ = 'TXM', ang = "",max=1,
                            defaut="Yes",into=("Yes","No"),),
              bound_self_defects = SIMP (statut= "f",typ = 'TXM', max=1,
                            ang="Yes if you want the to artifically impose self defects conservation by imposing a null flux for concentrations at $(No+Nc)$. Choose 'stop' to stop the calculation in case of leakage.",
                            defaut="Stop",into=("Yes","No","Stop"),)
)

operating_conditions=PROC(nom="operating_conditions",op= None,

            relative_time_increments=SIMP (statut= "o",typ = 'R', min=3, max='**',
                     ang="Relative time increments for the LONG_TERM computation",
                     defaut=(1e-10, 1.0000000000000001e-09, 3e-09, 1e-08, 2.9999999999999997e-08, 9.9999999999999995e-08, 2.9999999999999999e-07, 9.9999999999999995e-07, 3.0000000000000001e-06, 1.0000000000000001e-05, 3.0000000000000001e-05, 0.0001, 0.00029999999999999997, 0.001, 0.0030000000000000001, 0.01, 0.029999999999999999, 0.10000000000000001, 0.29999999999999999, 1.0),
            ),
            rescaling_NRT_damage_rate=FACT(statut='o', max=1, 
               ang="rescaling NRT damage rate (dpa/s)",
               value=SIMP(statut= "o",typ = 'R', defaut=0.0, val_min=0,),
               unit=SIMP (statut= "f",typ = 'TXM', defaut='dpa_per_s',into=('dpa_per_s',)),
            ),
           flux_cut_off_energy=FACT(statut='o', max=1,
               ang="Energy threshold for the calculation of the flux",
               value=SIMP(statut= "o",typ = 'R', defaut=1.0, val_min=0,),
               unit=SIMP (statut= "f",typ = 'TXM', defaut='MeV',into=('MeV',)),
             ),
           toughness_calculation_time_index = SIMP (statut= "o",typ = 'R', defaut=-1,into=(-1,),),
           temp_irrad=FACT(statut='o', max=1,
               ang="Energy threshold for the calculation of the flux",
               name=SIMP(statut= "f", typ = 'TXM', defaut='T', max=1,),
               value=SIMP(statut= "o",typ = 'R',   defaut=573.0, val_min=0,),
               unit=SIMP (statut= "f",typ = 'TXM', defaut='K',into=('K',)),
             ),
           time_irrad=FACT(statut='o', max=1,
               unit=SIMP(statut= "f", typ = 'TXM', defaut='s', max=1,),
               value=SIMP(statut= "o",typ = 'R', defaut=100000.0, val_min=0,),
            ),
           rescaling_flux=FACT(statut='o', max=1,
               unit=SIMP(statut= "f", typ = 'TXM', defaut='n_per_cm2_per_s', max=1,),
               value=SIMP(statut= "o",typ = 'R', defaut=0.0, val_min=0,),
            ),
)

bcc_crystal=PROC(nom="bcc_crystal",op= None,
           lattice_parameter=FACT(statut='o', max=1,
               unit=SIMP(statut= "f", typ = 'TXM', defaut='angstrom', max=1,),
               value=SIMP(statut= "o",typ = 'R', defaut=2.87, ),
            ),
           atomic_volume=FACT(statut='o', max=1,
               unit=SIMP(statut= "f", typ = 'TXM', defaut='m3', max=1,),
               value=SIMP(statut= "o",typ = 'R', defaut=1.18199515e-29, ),
            ),
           structure=SIMP (statut= "f",typ = 'TXM', defaut='bcc',into=('bcc','fcc'),
              ang='Crystalline structure of the considered alloy'),
           atomic_density=FACT(statut='o', max=1,
               unit=SIMP(statut= "f", typ = 'TXM', defaut='at_per_m3', max=1,),
               value=SIMP(statut= "o",typ = 'R', defaut=8.46027160095e+28, ),
            ),
)
           
neutron_spectrum=PROC(nom="neutron_spectrum",op= None,
           spectrum=SIMP(statut= "o",typ = 'R',max='**', defaut=(0.0465, 21000000000000.0, 0.10000000000000001, 24300000000000.0, 0.20000000000000001, 27300000000000.0, 0.40000000000000002, 37800000000000.0, 0.80000000000000004, 46600000000000.0, 1.0, 16400000000000.0, 1.3999999999999999, 25800000000000.0, 2.5, 41200000000000.0)),

           spectrum_description=SIMP(statut= "f", typ = 'TXM', max=1,),
)

diffusion_model=PROC(nom="diffusion_model",op=None,
           mv=FACT(statut='o', max=1,
           value=SIMP(statut= "o",typ = 'R', defaut=5., ),
           unit=SIMP(statut= "f", typ = 'TXM', defaut='atomic percent', max=1,),
)
)
           












