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

from PyQt5.QtWidgets import QLabel, QSizePolicy, QSpacerItem
from PyQt5.QtCore    import QSize

from InterfaceQT4.feuille                  import Feuille
from InterfaceQT4.monWidgetPlusieursTuple  import MonWidgetPlusieursTuple
from desWidgetPlusieursTuple               import Ui_WidgetPlusieursTuple
from desWidgetTableau                      import Ui_WidgetTableau

maxLen=3


class MonWidgetTableau (Ui_WidgetTableau,MonWidgetPlusieursTuple):
    def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        self.nbValeurs=len(monSimpDef.homo)
        MonWidgetPlusieursTuple.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        for i in range(len(monSimpDef.homo)):
            nomCol='LECol'+str(i+1)
            objCol=QLabel(self)
            objCol.setMinimumSize(QSize(80, 25))
            objCol.setText(monSimpDef.homo[i])
            self.LATitre.addWidget(objCol)
            setattr(self,nomCol,objCol)
            spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            self.LATitre.addItem(spacerItem)



#            monObjTitreCol=getattr(self,nomCol)
#            monObjTitreCol.setText(monSimpDef.homo[i])

#        for i in range(maxLen-len(monSimpDef.homo)):
#            index=i+len(monSimpDef.homo)+1
#            nomCol='LECol'+str(index)
#            monObjTitreCol=getattr(self,nomCol)
#            monObjTitreCol.close()

        self.resize(self.width(),1800)

    def ajoutLineEdit(self,valeur=None,inInit=False):
        hauteurAvant=(self.frame.height())
        MonWidgetPlusieursTuple.ajoutLineEdit(self,valeur,inInit)
