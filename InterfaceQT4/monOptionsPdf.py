# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
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

from PyQt4.QtGui  import *
from PyQt4.QtCore import *

from OptionsPdf import Ui_desPdf

class desPdf(Ui_desPdf,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.setupUi(self)
       self.setModal(modal)
     

class OptionPdf(desPdf):
   def __init__(self,parent = None,modal = 0,configuration=None):
       #print "OptionsPdf"
       desPdf.__init__(self,parent,modal)
       self.configuration=configuration
       self.initVal()
       self.connecterSignaux()

   def connecterSignaux(self) :
       self.connect(self.BCancel,SIGNAL("clicked()"),self.reject)
       self.connect(self.LERepPdf,SIGNAL("returnPressed()"),self.LeRepPdfPressed)
       self.connect(self.Bok,SIGNAL("clicked()"),self.BokClicked)

   def initVal(self):
       if hasattr(self.configuration,'exec_acrobat'):
          self.LERepPdf.setText(self.configuration.exec_acrobat)
       else :
          self.LERepPdf.clear()
   
   def LeRepPdfPressed(self):
       nouveau=str(self.LERepPdf.text())
       self.configuration.exec_acrobat=nouveau
       self.configuration.save_params()

   def BokClicked(self):
       self.LeRepPdfPressed()
       self.close()
