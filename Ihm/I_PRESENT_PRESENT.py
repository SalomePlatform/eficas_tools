# -*- coding: utf-8 -*-
# Copyright (C) 2007-2017   EDF R&D
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
"""
"""

from __future__ import absolute_import
from . import I_REGLE

class PRESENT_PRESENT(I_REGLE.REGLE):
  def verifConditionRegle(self,liste,l_mc_presents):
    mc0=self.mcs[0]
    for mc_present in l_mc_presents:
      if mc_present == mc0 :
        for mc in self.mcs[1:]:
          nb = l_mc_presents.count(mc)
          if nb == 0 : liste.append(mc)
        return liste
    return liste


