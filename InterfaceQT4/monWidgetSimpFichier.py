# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
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
import string,types,os

# Modules Eficas
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

from desWidgetSimpFichier  import Ui_WidgetSimpFichier 
from monWidgetSimpBase     import MonWidgetSimpBase


class MonWidgetSimpFichier (Ui_WidgetSimpFichier,MonWidgetSimpBase):
# c est juste la taille des differents widgets de base qui change

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        MonWidgetSimpBase.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        # deja fait dans MonWidgetSimpBase
        #self.maCommande.listeAffichageWidget.append(self.lineEditVal)


