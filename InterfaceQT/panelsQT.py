# -*- coding: utf-8 -*-
import string
import os

import traceback

from qt import *
from qtCommun import QTPanel
from desInactif import DInactif


SEPARATEUR = '-'*30

      
class PanelInactif( QTPanel, DInactif ):   
    def __init__(self,node,parent=None ):
        DInactif.__init__(self,parent)
        QTPanel.__init__(self,node,parent)
                
        
class NoPanel( QWidget ):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)
        self.textLabel = QLabel(self)
        self.textLabel.setText(QString("PANNEAU A IMPLEMENTER"))
        self.textLabel.setGeometry(QRect(130,150,219,17))
        self.resize(QSize(600,480).expandedTo(self.minimumSizeHint()))
        
