from OptionsPdf import desPdf

class OptionPdf(desPdf):
   def __init__(self,parent = None,name = None,modal = 0,fl = 0,configuration=None):
       desPdf.__init__(self,parent,name,modal,fl)
       self.configuration=configuration
       self.initVal()

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
