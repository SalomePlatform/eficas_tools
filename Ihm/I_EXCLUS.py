# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
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

import I_REGLE

class EXCLUS(I_REGLE.REGLE):
  def purge_liste(self,liste_a_purger,liste_mc_presents):
     regle_active=0
     for mc_present in liste_mc_presents:
        if mc_present in self.mcs:
           regle_active=1
           break
     if not regle_active : return liste_a_purger

     for mc in self.mcs:
        # Il ne faut pas purger un mot cle present. Sa cardinalite est verifiee par ailleurs
        if mc in liste_a_purger and mc not in liste_mc_presents:
           liste_a_purger.remove(mc)
     return liste_a_purger

