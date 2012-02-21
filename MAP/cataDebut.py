#)# -*- coding: utf-8 -*-
#
## --------------------------------------------------
## debut entete
## --------------------------------------------------
#
from Accas import *
import os
import sys
import types
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


specter_path=PROC(nom='specter_path',op=None,
      path=SIMP(typ='Fichier',defaut='/home/A28637/SVN_MAP/trunk/vendor/PERFORM_20110225/perfect_dev/tools/bin/specter', statut='o', fr = '', ang = 'A class for the definition of a file', max=1,),
                    )


residual_energy_model=PROC(nom='residual_energy_model',op=None,
          access=SIMP(statut= 'o',typ = 'TXM', defaut="user", max=1),
         beta=FACT(statut='o', max=1, fr = '', ang = 'A class for the definition of a numerical value', 
               value=SIMP(statut= 'o',typ = 'R', defaut=0.779, max=1),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut='None', max=1),
                  ),
          short_doc=SIMP(statut= 'o',typ = 'TXM', defaut="The model which gives the total number of surviving point defects for cascades in iron up to 10 keV. ", max=1),
         alpha=FACT(statut='o', max=1, fr = '', ang = 'A class for the definition of a numerical value', 
               value=SIMP(statut= 'o',typ = 'R', defaut=5.67, max=1),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut='None', max=1),
                  ),
          unit=SIMP(statut= 'o',typ = 'TXM', defaut="", max=1),
      )
mfvisc2_path=PROC(nom='mfvisc2_path',op=None,
      path=SIMP(typ='Fichier',defaut='/home/A28637/SVN_MAP/trunk/vendor/PERFORM_20110225/perfect_dev/tools/bin/mfvisc', statut='o', fr = '', ang = 'A class for the definition of a file', max=1,),
                    )


mfvisc2_parametrisation=PROC(nom='mfvisc2_parametrisation',op=None,
         stop_if_solute_loss=FACT(statut='o', max=1, fr = '', ang = 'Choose Yes if you want the rate-theory calculation to stop when a solute loss (i.e. Cu or He in the case of RPV and INTERN respectively) is detected. Choose No otherwise.', 
               value=SIMP(statut= 'o',typ = 'TXM', defaut="No", max=1,into=['Yes', 'No']),
                  ),
         bound_solute=FACT(statut='o', max=1, fr = '', ang = 'Choose Yes if you want the to artifically impose the solute conservation by imposing a null flux for concentrations at Nob.', 
               value=SIMP(statut= 'o',typ = 'TXM', defaut="Yes", max=1,into=['Yes', 'No']),
                  ),
         numerical_scheme_i=FACT(statut='o', max=1, fr = '', ang = 'Numerical parameters scheme for interstitials', 
            No=FACT(statut='o', max=1, fr = '', ang = 'Number of discrete equations for species i', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=30, max=1,val_min=0),
                        ),
            Nc=FACT(statut='o', max=1, fr = '', ang = 'Number of continuous equations for species i', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=300, max=1,val_min=0),
                        ),
            M=FACT(statut='o', max=1, fr = '', ang = 'Step value for species i', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=30, max=1,val_min=0),
                        ),
            kmet=FACT(statut='o', max=1, fr = '', ang = 'Step value for species i', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=97, max=1,val_min=0),
                        ),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut="", max=1),
         ),
         numerical_scheme_b=FACT(statut='o', max=1, fr = '', ang = 'Numerical parameters scheme for the solute element', 
            No=FACT(statut='o', max=1, fr = '', ang = 'Number of discrete equations for species b', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=0, max=1,val_min=0),
                        ),
            Nc=FACT(statut='o', max=1, fr = '', ang = 'Number of continuous equations for species b', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=0, max=1,val_min=0),
                        ),
            M=FACT(statut='o', max=1, fr = '', ang = 'Step value for species b', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=0, max=1,val_min=0),
                        ),
            kmet=FACT(statut='o', max=1, fr = '', ang = 'Step value for species b', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=0, max=1,val_min=0),
                        ),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut="", max=1),
         ),
          access=SIMP(statut= 'o',typ = 'TXM', defaut="user", max=1),
         solver_absolute_error=FACT(statut='o', max=1, fr = '', ang = 'Absolute error for the rate theory solver', 
               value=SIMP(statut= 'o',typ = 'R', defaut=0.0001, max=1,val_min=0),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut='None', max=1),
                  ),
         solver_relative_error=FACT(statut='o', max=1, fr = '', ang = 'Relative error for the rate theory solver', 
               value=SIMP(statut= 'o',typ = 'R', defaut=0.001, max=1,val_min=0),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut='None', max=1),
                  ),
          short_doc=SIMP(statut= 'o',typ = 'TXM', defaut="Parametrisation of the rate theory code", max=1),
         numerical_scheme_v=FACT(statut='o', max=1, fr = '', ang = 'Numerical parameters scheme for vacancies', 
            No=FACT(statut='o', max=1, fr = '', ang = 'Number of discrete equations for species v', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=30, max=1,val_min=0),
                        ),
            Nc=FACT(statut='o', max=1, fr = '', ang = 'Number of continuous equations for species v', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=300, max=1,val_min=0),
                        ),
            M=FACT(statut='o', max=1, fr = '', ang = 'Step value for species v', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=30, max=1,val_min=0),
                        ),
            kmet=FACT(statut='o', max=1, fr = '', ang = 'Step value for species v', 
                    value=SIMP(statut= 'o',typ = 'I', defaut=55, max=1,val_min=0),
                        ),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut="", max=1),
         ),
         bound_self_defects=FACT(statut='o', max=1, fr = '', ang = 'Choose Yes if you want the to artifically impose self defects conservation by imposing a null flux for concentrations at $(No+Nc)$. Choose stop to stop the calculation in case of leakage.', 
               value=SIMP(statut= 'o',typ = 'TXM', defaut="Stop", max=1,into=['Yes', 'No', 'Stop']),
                  ),
          unit=SIMP(statut= 'o',typ = 'TXM', defaut="", max=1),
      )
neutron_spectrum=PROC(nom='neutron_spectrum',op=None,
         spectrum=FACT(statut='o', max=1, fr = '', ang = 'Neutron spectrum table', 
         values=SIMP(statut= 'o',typ = Tuple(2), defaut=[[0.0465, 21000000000000.0], [0.10000000000000001, 24300000000000.0], [0.20000000000000001, 27300000000000.0], [0.40000000000000002, 37800000000000.0], [0.80000000000000004, 46600000000000.0], [1.0, 16400000000000.0], [1.3999999999999999, 25800000000000.0], [2.5, 41200000000000.0]], min=1, max='**'),
         ),
          unit=SIMP(statut= 'o',typ = 'TXM', defaut="", max=1),
          spectrum_time=SIMP(statut= 'o',typ = 'TXM', defaut="None", max=1),
          access=SIMP(statut= 'o',typ = 'TXM', defaut="user", max=1),
          short_doc=SIMP(statut= 'o',typ = 'TXM', defaut="Data object containing the neutron spectrum table.", max=1),
      )
material_content=PROC(nom='material_content',op=None,
      valeur=FACT(statut='o', max=1, fr = '', ang = 'Chemical composition of the steel', 
          Cu=SIMP(statut= 'o',typ = 'R', defaut=0.0, max=1,val_min=0.0,val_max=0.1),
          unit=SIMP(statut= 'o',typ = 'TXM', defaut='atomic percent', max=1),
            ),
      )
experimental_resolutions=PROC(nom='experimental_resolutions',op=None,
          short_doc=SIMP(statut= 'o',typ = 'TXM', defaut="A base class for the minimum radius of interstitial and vacancy clusters taken into account in number densities calculations.", max=1),
          unit=SIMP(statut= 'o',typ = 'TXM', defaut="", max=1),
         R_min_V=FACT(statut='o', max=1, fr = '', ang = 'Minimum radius of vacancy clusters taken into account in number densities calculations.', 
               value=SIMP(statut= 'o',typ = 'R', defaut=0.0, max=1),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut='nm', max=1),
                  ),
          access=SIMP(statut= 'o',typ = 'TXM', defaut="user", max=1),
         interstitial_cluster_shape=FACT(statut='o', max=1, fr = '', ang = 'Choice for the shape of interstitials clusters, disks or spheres.  This only impacts the calculation of the radius of the cluster and associated radial density.', 
               value=SIMP(statut= 'o',typ = 'TXM', defaut="disk", max=1,into=['disk', 'sphere']),
                  ),
         R_min_B=FACT(statut='o', max=1, fr = '', ang = 'Minimum radius of copper precipitates taken into account in number densities calculations.                            ', 
               value=SIMP(statut= 'o',typ = 'R', defaut=0.0, max=1),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut='nm', max=1),
                  ),
         R_min_I=FACT(statut='o', max=1, fr = '', ang = 'Minimum radius of interstitial clusters taken into account in number densities calculations.                            ', 
               value=SIMP(statut= 'o',typ = 'R', defaut=0.0, max=1),
               unit=SIMP(statut= 'o',typ = 'TXM', defaut='nm', max=1),
                  ),
      )
damage_energy_model=PROC(nom='damage_energy_model',op=None,
          a=SIMP(statut= 'o',typ = 'R', defaut=1.11787605409e-09, max=1),
          elect=SIMP(statut= 'o',typ = 'R', defaut=4.8e-10, max=1),
          r_bohr=SIMP(statut= 'o',typ = 'R', defaut=5.29e-09, max=1),
          unit=SIMP(statut= 'o',typ = 'TXM', defaut="", max=1),
          z_p=SIMP(statut= 'o',typ = 'R', defaut=26.0, max=1),
          z_t=SIMP(statut= 'o',typ = 'R', defaut=26.0, max=1),
          access=SIMP(statut= 'o',typ = 'TXM', defaut="expert", max=1),
          short_doc=SIMP(statut= 'o',typ = 'TXM', defaut="Lindhard damage energy model", max=1),
          m_p=SIMP(statut= 'o',typ = 'R', defaut=55.0, max=1),
          m_t=SIMP(statut= 'o',typ = 'R', defaut=55.0, max=1),
      )

