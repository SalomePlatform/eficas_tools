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



JdC = JDC_CATA(code='Atmos',regles = (UN_PARMI('Wind',)),
                        )


Wind = PROC( nom="Wind", op = None,
    Wind_Speed1 = SIMP(statut = "o", typ = 'I'),
    Mesure1 = FACT( statut='f',
       Value1 = SIMP(statut = "o", typ = 'I'),
       Unit1 = SIMP(statut = "o", typ = 'I'),
    ),
    B_enter_mesure = BLOC(condition = 'Wind_Speed1 == 1',
       Wind_Speed = SIMP(statut = "o", typ = 'I'),
       Mesure = FACT( statut='f', max='**',
           Value = SIMP(statut = "o", typ = 'I'),
           Unit = SIMP(statut = "o", typ = 'I'),
                   ),
       ),
)

