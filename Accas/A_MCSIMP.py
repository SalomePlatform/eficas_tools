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
from __future__ import absolute_import
from Noyau import N_MCSIMP
from Validation import V_MCSIMP
from Ihm import I_MCSIMP
from Efi2Xsd.MCAccasXML  import X_MCSIMP

class MCSIMP(I_MCSIMP.MCSIMP,N_MCSIMP.MCSIMP,X_MCSIMP,V_MCSIMP.MCSIMP):
   def __init__(self,val,definition,nom,parent,objPyxbDeConstruction=None):
   #def __init__(self,val,definition,nom,parent,objPyxbDeConstruction) quand cela sera correct dans les update_etape. pour l instant on laisse le defaut a None : 9 Aout 18:
      N_MCSIMP.MCSIMP.__init__(self,val,definition,nom,parent,objPyxbDeConstruction)
      V_MCSIMP.MCSIMP.__init__(self)
