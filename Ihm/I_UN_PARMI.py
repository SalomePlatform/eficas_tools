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

class UN_PARMI(I_REGLE.REGLE):

  def purgeListe(self,liste_a_purger,listeMcPresents):
     regle_active=0
     for mc_present in listeMcPresents:
        if mc_present in self.mcs:
           regle_active=1
           break
     if not regle_active : return liste_a_purger

     # Si un des mots cles est present, on les enleve tous
     # sauf celui ci
     for mc in self.mcs:
        if mc in liste_a_purger and mc not in listeMcPresents:
           liste_a_purger.remove(mc)
     return liste_a_purger

