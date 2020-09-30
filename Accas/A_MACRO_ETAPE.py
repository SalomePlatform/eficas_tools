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
from Noyau import N_MACRO_ETAPE
from Validation import V_MACRO_ETAPE
from Ihm import I_MACRO_ETAPE
from .A_ASSD import CO
from Efi2Xsd.MCAccasXML  import X_MCCOMPO

class MACRO_ETAPE(I_MACRO_ETAPE.MACRO_ETAPE,
                  X_MCCOMPO,
                  V_MACRO_ETAPE.MACRO_ETAPE,
                  N_MACRO_ETAPE.MACRO_ETAPE):
   typeCO=CO
   def __init__(self,oper=None,reuse=None,args={}):
      N_MACRO_ETAPE.MACRO_ETAPE.__init__(self,oper,reuse,args)
      V_MACRO_ETAPE.MACRO_ETAPE.__init__(self)
      I_MACRO_ETAPE.MACRO_ETAPE.__init__(self)
