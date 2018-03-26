# -*- coding: utf-8 -*-
#
#  Copyright (C) 2012-2013 EDF
#
#  This file is part of SALOME HYDRO module.
#
#  SALOME HYDRO module is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SALOME HYDRO module is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SALOME HYDRO module.  If not, see <http://www.gnu.org/licenses/>.

import types
from Accas import *


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

JdC = JDC_CATA(regles = (UN_PARMI('TELEMAC2D',)),
                        )



Atmos = PROC(
    nom = "Atmos", op = None,
    fr = u"Définition d'un cas d'étude Atmosphérique",
    ang = u"Definition of  study case",
    Wind = FACT( statut='o',
    Wind_Speed = SIMP(statut = "o", typ = 'I', sug=20),
    Speed_Unit = SIMP(statut = "o", typ = 'TXM',
                      into = ('knots','mph','m/s'),
                      defaut = 'mph'),
    Measurement = SIMP(statut = "o", typ = 'TXM',
                   into = ( 'Manual', 'TypeA', 'TypeB'),),
    b_enter_mesure = BLOC(condition = 'MEASUREMENT == "Manual"',
           Value = SIMP(statut = "o", typ = 'I'),
           Unit = SIMP(statut = "o", typ = 'TXM', into = ('feet', 'meters')),
                     ),
    ),
    Ground = FACT( statut='o',
    Ground_Roughness = SIMP(statut='o',typ='TXM',
         into=('Open Country', 'Urban Or Forest', 'Open Water', 'Manual')
         ),
    b_enter_ground = BLOC(condition = 'Ground_Roughness == "Manual"',
          Input_Roughness = SIMP(statut = "o", typ = 'I'),
          Unit = SIMP(statut = "o", typ = 'TXM', into = ('in', 'cm'), defaut='cm')
                ),
    
    ),
    Cover = FACT( statut='o',
    Cover_type = SIMP(statut='o',typ='TXM', into=('Manual', 'Clear','Partly Cloudy','Complete Cover',),),
    b_enter_cover = BLOC(condition = 'Cover_type == "Manual"',
          Cover_Value = SIMP(statut = "o", typ = 'I',val_max=10),
                       ),
    ),

)
