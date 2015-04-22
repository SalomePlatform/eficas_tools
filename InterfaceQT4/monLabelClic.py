#!/usr/bin/env python
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

import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#from Extensions.i18n import tr

class MonLabelClic(QLabel) :

     def __init__(self,parent):
        QLabel.__init__(self,parent)
        # Pas propre mais impossible de faire fonctionner isinstance sur Groupe, MonWidgetCommande 
        # PNPNPN ? a ameliorer
        if isinstance (parent,QFrame):
           parent=parent.parent()
        self.parent=parent


     def event(self,event) :
         if event.type() == QEvent.MouseButtonRelease:
            self.texte=self.text()
            self.parent.traiteClicSurLabel(self.texte)
         return QLabel.event(self,event)

