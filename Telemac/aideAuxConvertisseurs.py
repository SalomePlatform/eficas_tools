# -*- coding: utf-8 -*-
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
"""Ce module contient le plugin generateur de fichier au format  Code_Carmel3D pour EFICAS.
"""

listeSupprime  = ( 'DAY', 'MONTH', 'YEAR', 'HOUR', 'MINUTE', 'SECOND', 'CONSIGNE'
                   'LIMIT VALUES H', 'LIMIT VALUES U', 'LIMIT VALUES V', 'LIMIT VALUES T',
                   'SISYPHE', 'TOMAWAC', 'DELWAQ',
                   'ADVECTION U AND V', 'ADVECTION H',
                   'ADVECTION TRACERS', 'ADVECTION K AND EPSILON',
                   'TOLERANCE FOR H', 'TOLERANCE FOR U', 'TOLERANCE FOR V', 'TOLERANCE FOR COUT',
                   'SUPG OPTION U AND V', 'SUPG OPTION H', 'SUPG OPTION TRACERS', 'SUPG OPTION K AND EPSILON',
                   'UPWIND COEFFICIENTS Of U AND V', 'UPWIND COEFFICIENTS OF H', 
)

DicoAglomere= {
'LIMIT VALUES'        : ( 'Limit_Values_H', 'Limit_Values_U', 'Limit_Values_V', 'Limit_Values_T'),
'COUPLING WITH'       : ( 'Sisyphe', 'Tomawac', 'Delwaq'),
'TYPE OF ADVECTION'   : ( 'Advection_U_And_V', 'Advection_H', 'Advection_Tracers','Advection_K_And_Epsilon'),
'TOLERANCE'           : ( 'Tolerance_For_H', 'Tolerance_For_U', 'Tolerance_For_V', 'Tolerance_For_cout',),
'SUPG OPTION'         : ( 'Supg_Option_U_And_V', 'Supg_Option_H', 'Supg_Option_Tracers', 'Supg_Option_K_And_Epsilon',),
'UPWIND COEFFICIENTS' : ( 'Upwind_Coefficients_Of_U_And_V', 'Upwind_Coefficients_Of_H', ),
}

DicoEficasToCas= {
 'C U PRECONDITIONING'                           : 'C-U PRECONDITIONING' ,
 'INFORMATION ABOUT K EPSILON MODEL'             : 'INFORMATION ABOUT K-EPSILON MODEL' ,
 'MANNING DEFAULT VALUE FOR COLEBROOK WHITE LAW' : 'MANNING DEFAULT VALUE FOR COLEBROOK-WHITE LAW' ,
 'MASS BALANCE'                                  : 'MASS-BALANCE' ,
 'MASS LUMPING FOR WEAK CHARACTERISTICS'         : 'MASS-LUMPING FOR WEAK CHARACTERISTICS',
 'MASS LUMPING ON H'                             : 'MASS-LUMPING ON H' ,
 'MASS LUMPING ON TRACERS'                       : 'MASS-LUMPING ON TRACERS' ,
 'MASS LUMPING ON VELOCITY'                      : 'MASS-LUMPING ON VELOCITY' ,
 'MATRIX VECTOR PRODUCT'                         : 'MATRIX-VECTOR PRODUCT' ,
 'NON DIMENSIONAL DISPERSION COEFFICIENTS'       : 'NON-DIMENSIONAL DISPERSION COEFFICIENTS' ,
 'NON SUBMERGED VEGETATION FRICTION'             : 'NON-SUBMERGED VEGETATION FRICTION' ,
 'NUMBER OF SUB ITERATIONS FOR NON LINEARITIES'  : 'NUMBER OF SUB-ITERATIONS FOR NON-LINEARITIES' ,
 'OPTION FOR THE SOLVER FOR K EPSILON MODEL'     : 'OPTION FOR THE SOLVER FOR K-EPSILON MODEL' ,
 'PRECONDITIONING FOR K EPSILON MODEL'           : 'PRECONDITIONING FOR K-EPSILON MODEL' ,
 'SOLVER FOR K EPSILON MODEL'                    : 'SOLVER FOR K-EPSILON MODEL' ,
 'STAGE DISCHARGE CURVES FILE'                   : 'STAGE-DISCHARGE CURVES FILE' ,
 'STAGE DISCHARGE CURVES'                        : 'STAGE-DISCHARGE CURVES' ,
 'TIME STEP REDUCTION FOR K EPSILON MODEL'       : 'TIME STEP REDUCTION FOR K-EPSILON MODEL' ,
 'VARIABLE TIME STEP'                            : 'VARIABLE TIME-STEP' ,

}

DicoCasToEficas = {}
for k in DicoCasToEficas.keys() : DicoCasToEficas[DicoEficasToCas[k]]=k


DicoFrancaisAvecApostrophe= {
      "Coordonnees_De_L_Origine"                             : "Coordonnees_De_L'origine",
      "Modele_De_Nappes_D_Hydrocarbures"                     : "Modele_De_Nappes_D'hydrocarbures",
      "Maximum_D_Iterations_Pour_La_Diffusion_Des_Traceurs"  : "Maximum_D'iterations_Pour_La_Diffusion_Des_Traceurs",
      "Coefficient_D_Implicitation_Des_Traceurs"             : "Coefficient_D'implicitation_Des_Traceurs",
      "Coefficient_D_Influence_Du_Vent"                      : "Coefficient_D'influence_Du_Vent",
      "Date_De_L_Origine_Des_Temps"                          : "Date_De_L'origine_Des_Temps",
      "Elements_Masques_Par_L_Utilisateur"                   : "Elements_Masques_Par_L'utilisateur",
      "Maximum_D_Iterations_Pour_L_Identification"           : "Maximum_D'iterations_Pour_L'identification",
      "Heure_De_L_Origine_Des_Temps"                         : "Heure_De_L'origine_Des_Temps",
      "Methode_D_Identification"                             : "Methode_D'identification",
      "Masse_Volumique_De_L_Eau"                             : "Masse_Volumique_De_L'eau",
      "Coefficient_D_Integration_En_Temps_De_Newmark"        : "Coefficient_D'integration_En_Temps_De_Newmark",
      "Bornes_En_Temps_Pour_L_Analyse_De_Fourier"            : "Bornes_En_Temps_Pour_L'analyse_De_Fourier",
      "Periodes_D_Analyse_De_Fourier"                        : "Periodes_D'analyse_De_Fourier",
      "Precisions_Pour_L_Identification"                     : "Precisions_Pour_L'identification",
      "Maximum_D_Iterations_Pour_K_Et_Epsilon"               : "Maximum_D'iterations_Pour_K_Et_Epsilon",
      "Maximum_D_Iterations_Pour_Les_Schemas_De_Convection"  : "Maximum_D'iterations_Pour_Les_Schemas_De_Convection",
      "Numero_De_L_Enregistrement_Dans_Le_Fichier_De_Houle"  : "Numero_De_L'enregistrement_Dans_Le_Fichier_De_Houle",
      "Criteres_D_Arret"  : "Criteres_D'arret",
}

ListeSupprimeCasToEficas = ('Validation','Parallel_Processors')
ListeCalculEficasToCas   = ('Validation',)
ListeCalculCasToEficas   = ('Option_De_Supg', 'Forme_De_La_Convection')

DicoAvecMajuscules={
  'WGS84' : 'WGS84', 
  'TPXO'  : 'TPXO', 
  'Saint-venant ef' : 'Saint-venant EF'}
