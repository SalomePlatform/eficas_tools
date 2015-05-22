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

from feuille               import Feuille
from desWidgetUniqueSDCO   import Ui_WidgetUniqueSDCO 
from politiquesValidation  import PolitiqueUnique
from qtSaisie              import SaisieSDCO




class MonWidgetUniqueSDCO (Ui_WidgetUniqueSDCO,Feuille,SaisieSDCO):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        print "dans MonWidgetSDCO"
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.politique=PolitiqueUnique(self.node,self.editor)
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.maCommande.listeAffichageWidget.append(self.LESDCO)
        self.AAficher=self.LESDCO

        valeur = self.node.item.get_valeur()
        if valeur  != "" and valeur != None : self.LESDCO.setText(valeur.nom)
        self.connect(self.LESDCO,SIGNAL("returnPressed()"),self.LESDCOReturnPressed)

