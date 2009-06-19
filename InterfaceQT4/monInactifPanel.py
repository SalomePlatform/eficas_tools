# -*- coding: utf-8 -*-


from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qtCommun import QTPanel
from desInactif import Ui_DInactif


SEPARATEUR = '-'*30

      
class PanelInactif( QTPanel, Ui_DInactif,QDialog ):   
    def __init__(self,node,parent ):
        #print "PanelInactif"
        QDialog.__init__(self,parent)
        QTPanel.__init__(self,node,parent)
        Ui_DInactif.__init__(self,parent)
        if hasattr(parent,"leLayout"):
           parent.leLayout.removeWidget(parent.leLayout.widgetActive)
           parent.leLayout.widgetActive.close()
           parent.leLayout.addWidget(self)
           parent.leLayout.widgetActive=self
        else:
           parent.partieDroite=QWidget()
           parent.leLayout=QGridLayout(parent.partieDroite)
           parent.leLayout.addWidget(self)
           parent.addWidget(parent.partieDroite)
           parent.leLayout.widgetActive=self
        self.setupUi(self)
        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)              

    def BSupPressed(self):
        self.editor.init_modif()
        self.node.delete()
        
