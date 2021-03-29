# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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
from __future__ import absolute_import
from Noyau import N_REGLE
from Validation import V_PRESENT_ABSENT
from Ihm import I_PRESENT_ABSENT

class PRESENT_ABSENT(I_PRESENT_ABSENT.PRESENT_ABSENT,V_PRESENT_ABSENT.PRESENT_ABSENT,
                     N_REGLE.REGLE):
   """
       La classe utilise l'initialiseur de REGLE. Il n'est pas 
       necessaire d'expliciter son initialiseur car 
       V_PRESENT_ABSENT.PRESENT_ABSENT n'en a pas 
   """
