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

from Noyau.N_VALIDATOR import *

class Compulsory(Compulsory):
      def has_into(self):
          return 0
      def valide_liste_partielle(self,liste_courante=None):
          return 1

class OrdList(OrdList):
      def valide_liste_partielle(self,liste_courante=None):
          """
           M�thode de validation de liste partielle pour le validateur OrdList
          """
          try:
             self.convert(liste_courante)
             valid=1
          except:
             valid=0
          return valid

