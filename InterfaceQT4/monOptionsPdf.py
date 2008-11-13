# -*- coding: utf-8 -*-

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
