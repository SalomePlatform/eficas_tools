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

# This empty class is replaced by the class eficas.SalomeEntry
# (defined in Salome EFICAS module) when Eficas is launched in Salome context.
# It handles the objects that can be selected from Salome object browser.

from __future__ import absolute_import
from Ihm import I_FICHIER

class Fichier (I_FICHIER.Fichier):
    def __init__(self,*tup,**args):
        I_FICHIER.FICHIER.__init__(self,*tup,**args)
