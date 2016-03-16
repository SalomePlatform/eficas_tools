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
import string,types,os,sys

# Modules Eficas
from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets  import Qicon, QScrollbar, QFrame
    from PyQt5.QtCore import QTimer, QSize, QT
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import

from Extensions.i18n import tr

from feuille                import Feuille
from desWidgetPlusieursPlie import Ui_WidgetPlusieursPlie 


class MonWidgetPlusieursPlie (Ui_WidgetPlusieursPlie,Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        #print "MonWidgetPlusieursBase", nom
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.AAfficher=self.lineEditVal
        self.maCommande.listeAffichageWidget.append(self.lineEditVal)
        
        if monEnvQT5 :
           self.BVisuListe.clicked(self.selectWidgetDeplie)
        else :
           self.connect(self.BVisuListe,SIGNAL("clicked()"), self.selectWidgetDeplie)


  def setValeurs(self):
       self.listeValeursCourantes=self.node.item.GetListeValeurs()
       if self.listeValeursCourantes != []  :  self.lineEditVal.setText(str(self.listeValeursCourantes))
       else : self.lineEditVal.setText("")
       self.lineEditVal.setReadOnly(True)
       return

  def selectWidgetDeplie(self):
      self.editor.listeDesListesOuvertes.add(self.node.item)
      self.reaffichePourDeplier()

       
