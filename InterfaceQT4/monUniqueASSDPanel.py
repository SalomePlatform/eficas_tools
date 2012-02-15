# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
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
