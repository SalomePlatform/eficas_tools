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
# Modules Python
from __future__ import absolute_import
import types,os

# Modules Eficas
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
from Extensions.i18n import tr

from .feuille               import Feuille
from .monWidgetSimpTuple    import MonWidgetSimpTuple 
from desWidgetTuple2       import Ui_WidgetTuple2 


class MonWidgetSimpTuple2 (Ui_WidgetTuple2,MonWidgetSimpTuple):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        self.nbValeurs=2
        MonWidgetSimpTuple.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        #self.maCommande.listeAffichageWidget.append(self.lineEditVal2)
        if self.objSimp.isImmuable() :
          self.lineEditVal1.setDisabled(True)
          self.lineEditVal2.setDisabled(True)
          self.lineEditVal1.setStyleSheet("background:rgb(244,244,244);\n" "border:0px;\n")
          self.lineEditVal2.setStyleSheet("background:rgb(244,244,244);\n" "border:0px;\n")
          self.lineEditVal1.setToolTip(tr("Valeur non modifiable"))
          self.lineEditVal2.setToolTip(tr("Valeur non modifiable"))
        else :
          self.maCommande.listeAffichageWidget.append(self.lineEditVal1)
      
