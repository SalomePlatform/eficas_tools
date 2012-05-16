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
# Modules Python
import string,types,os

# Modules Eficas

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from desUniqueASSD import Ui_DUnASSD
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiqueUnique

class DUnASSD(Ui_DUnASSD,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
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

# Import des panels

class MonUniqueASSDPanel(DUnASSD,QTPanel,SaisieValeur):
  """
  Classe definissant le panel associe aux mots-cles qui demandent
  a l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discretes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonUniqueASSDPanel"
        self.editor=parent
        QTPanel.__init__(self,node,parent)
        DUnASSD.__init__(self,parent,fl)
        self.politique=PolitiqueUnique(node,parent)
        self.InitListBoxASSD()
        self.InitCommentaire()
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.listBoxASSD,SIGNAL("itemDoubleClicked(QListWidgetItem*)"),self.ClicASSD)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)


  def BOkPressed(self):
        self.ClicASSD()


  def InitCommentaire(self): 
      mc = self.node.item.get_definition()
      try :
          type = mc.type[0].__name__
      except :
          type = str(mc.type[0])
      if len(mc.type)>1 :
          for typ in mc.type[1:] :
            try :
                l=typ.__name__
            except:
                l=str(typ)
            type = type + ' ou '+l
      commentaire="Un objet de type "+type+" est attendu"
      aideval=self.node.item.aide()
      commentaire=commentaire +QString.toUtf8(QString("   "))+ QString.toUtf8(QString(aideval))
      self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))
