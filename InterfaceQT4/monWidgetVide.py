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

from .feuille                           import Feuille
from desWidgetVide                      import Ui_WidgetVide 
from InterfaceQT4.politiquesValidation  import PolitiqueUnique

class MonWidgetVide (Ui_WidgetVide,Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.politique=PolitiqueUnique(self.node,self.editor)
        t=self.node.item.object.definition.type[0].__name__
        self.lineEditVal.setText('Attend un objet de type '+t+'. Il faut en créer')
        self.parentQt.commandesLayout.insertWidget(-1,self)
        #PN il faut remplir le type
