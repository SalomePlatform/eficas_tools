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
try :
   from builtins import str
except : pass

import types,os

# Modules Eficas
from Extensions.i18n import tr

from .feuille               import Feuille
from .politiquesValidation  import PolitiqueUnique
from .qtSaisie              import SaisieValeur
from desWidgetCBIntoSug     import Ui_WidgetCBIntoSug

from PyQt5.QtWidgets import QComboBox, QCompleter
from PyQt5.QtCore import Qt

from monWidgetCB            import MonWidgetCBCommun
from monWidgetIntoSug       import GereAjoutDsPossible

      
class MonWidgetCBIntoSug (MonWidgetCBCommun, Ui_WidgetCBIntoSug,GereAjoutDsPossible):
  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
      self.maListeDeValeur=monSimpDef.into
      if node.item.hasIntoSug()          : self.maListeDeValeur  = node.item.getListePossibleAvecSug([])
      if hasattr(node.item,'suggestion') : self.maListeDeValeur +=  node.item.suggestion
      MonWidgetCBCommun. __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
      self.lineEditVal.returnPressed.connect(self.LEValeurAjouteDsPossible)

  def ajouteValeurPossible(self,valeur):
      self.CBChoix.addItem(valeur)
      # on ne sait pas si on a deja ajouté une valeur
      try    : self.node.item.suggestion.append(valeur)
      except : self.node.item.suggestion = (valeur,)
      self.lineEditVal.setText('')
      self.CBChoix.setCurrentIndex(self.CBChoix.findText(valeur));
      

