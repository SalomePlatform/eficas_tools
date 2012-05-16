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
# Modules Eficas

from desListeParam import Ui_DLisParam
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# Import des panels
class DLisParam(Ui_DLisParam,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.setupUi(self)

class MonListeParamPanel(DLisParam):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,liste,parent,name = None,fl = 0):
        #print "MonListeParamPanel"
        self.panel=parent
        DLisParam.__init__(self,parent,fl)
        self.liste=liste
        self.dictListe={}
        self.initVal()
        self.connecterSignaux()

  def connecterSignaux(self) :
  #     self.connect(self.LBParam,SIGNAL("itemPressed(QListWidgetItem*)"),self.LBParamItemPressed)
        self.connect(self.BOk,SIGNAL("clicked()"),self.valideParam)

  def initVal(self):
        self.LBParam.clear()
        for param in self.liste :
            self.LBParam.addItem(QString(repr(param)))
            self.dictListe[QString(repr(param))] = param

  def valideParam(self):
        if self.LBParam.selectedItems()== None : return
        lParam=[]
        for indice in range(len(self.LBParam.selectedItems())):
            i=self.LBParam.selectedItems()[indice].text()
            param=self.dictListe[i]
            lParam.append(param)
           
        try :
          self.panel.AjoutNValeur(lParam)
        except :
          for p in lParam :
             self.panel.Ajout1Valeur(p)
        self.close()


