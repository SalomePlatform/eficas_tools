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
from Noyau import N_ETAPE
from Validation import V_ETAPE
from Ihm import I_ETAPE
from Efi2Xsd.MCAccasXML  import X_ETAPE

class ETAPE(I_ETAPE.ETAPE,V_ETAPE.ETAPE,X_ETAPE,N_ETAPE.ETAPE):
   def __init__(self,oper=None,reuse=None,args={}):
      N_ETAPE.ETAPE.__init__(self,oper,reuse,args)
      V_ETAPE.ETAPE.__init__(self)
