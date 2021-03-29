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
from Noyau import N_BLOC
from Ihm import I_ENTITE
from Accas import A_MCBLOC
from Efi2Xsd.AccasXsd  import X_BLOC


class BLOC(N_BLOC.BLOC,X_BLOC,I_ENTITE.ENTITE):
   class_instance=A_MCBLOC.MCBLOC
   def __init__(self,*tup,**args):
      I_ENTITE.ENTITE.__init__(self)
      N_BLOC.BLOC.__init__(self,*tup,**args)

