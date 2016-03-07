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
from Extensions.i18n import tr

from monWidgetRadioButton  import MonWidgetRadioButtonCommun 
from desWidget4a6RadioButton  import Ui_Widget4a6RadioButton 


class MonWidget4a6RadioButtonSD (Ui_Widget4a6RadioButton,MonWidgetRadioButtonCommun):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        #print "dans le init de MonWidget4a6RadioButton",self
        self.maListeDeValeur=node.item.get_sd_avant_du_bon_type()
        MonWidgetRadioButtonCommun.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)

  def setMaxI(self):
        self.maxI=6

