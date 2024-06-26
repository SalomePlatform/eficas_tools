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
# Modules Python
from __future__ import absolute_import
import types,os

# Modules Eficas
from Extensions.i18n import tr

from desWidgetSimpTxt  import Ui_WidgetSimpTxt
from .monWidgetSimpBase     import MonWidgetSimpBase


class MonWidgetSimpTxt (Ui_WidgetSimpTxt,MonWidgetSimpBase):
# c est juste la taille des differents widgets de base qui change

    def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        MonWidgetSimpBase.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
