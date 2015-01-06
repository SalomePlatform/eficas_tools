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
import traceback

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

# ------------- #
class GereListe:
# ------------- #

   def __init__(self):
       print "GereListe"
       self.connecterSignaux()

   def connecterSignaux(self):
       self.connect(self.RBUp,SIGNAL("clicked()"),self.upPushed)
       self.connect(self.RBDown,SIGNAL("clicked()"),self.downPushed)
       self.connect(self.RBPoubelleVal,SIGNAL("clicked()"),self.poubPushed)

   def upPushed(self):
       print "upPushed"

   def downPushed(self):
       print "downPushed"

   def poubPushed(self):
       print "poubPushed"
