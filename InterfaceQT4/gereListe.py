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
from monViewTexte   import ViewText

# ---------------------- #
class LECustom(QLineEdit):
# ---------------------- #
 def __init__(self,parent,parentQt,i):
        """
        Constructor
        """
        QMainWindow.__init__(self,parent)
        self.parentQt=parentQt
        self.num=i

 def focusInEvent(self,event):
     self.parentQt.LineEditEnCours=self
     self.parentQt.NumLineEditEnCours=self.num




# ------------- #
class GereListe:
# ------------- #

   def __init__(self):
       print "GereListe"
       self.connecterSignaux()

   def connecterSignaux(self):
       self.connect(self.RBHaut,SIGNAL("clicked()"),self.hautPushed)
       self.connect(self.RBBas,SIGNAL("clicked()"),self.basPushed)
       self.connect(self.RBMoins,SIGNAL("clicked()"),self.moinsPushed)
       self.connect(self.RBPlus,SIGNAL("clicked()"),self.plusPushed)
       self.connect(self.RBVoisListe,SIGNAL("clicked()"),self.voisListePushed)
       self.connect(self.RBSalome,SIGNAL("clicked()"),self.salomePushed)
       self.connect(self.RBSalomeVue,SIGNAL("clicked()"),self.salomeVuePushed)

   def hautPushed(self):
       if self.NumLineEditEnCours == 1 : return
       else : numEchange=self.NumLineEditEnCours-1
       self.echange(self.NumLineEditEnCours,numEchange)
       self.scrollArea.ensureWidgetVisible(self.LineEditEnCours)


   def basPushed(self):
       if self.NumLineEditEnCours == self.indexDernierLabel : return
       else : numEchange=self.NumLineEditEnCours+1
       self.echange(self.NumLineEditEnCours,numEchange)
       self.scrollArea.ensureWidgetVisible(self.LineEditEnCours)

   def echange(self,num1,num2):
       # on donne le focus au a celui ou on a bouge
       # par convention le 2
       nomLineEdit="lineEditVal"+str(num1)
       #print nomLineEdit
       courant=getattr(self,nomLineEdit)
       valeurAGarder=courant.text()
       nomLineEdit2="lineEditVal"+str(num2)
       #print nomLineEdit2
       courant2=getattr(self,nomLineEdit2)
       courant.setText(courant2.text())
       courant2.setText(valeurAGarder)
       self.changeValeur(changeDePlace=False)
       self.NumLineEditEnCours=num2
       self.LineEditEnCours=courant2

   def moinsPushed(self):
       if self.indexDernierLabel < self.monSimpDef.min:
          self.editor.affiche_infos('nb min de valeurs : '+str(self.monSimpDef.min)+' atteint')
          return
       # on supprime le dernier
       if self.NumLineEditEnCours==self.indexDernierLabel : 
          self.setText("")
       else :
         for i in range (self.NumLineEditEnCours, self.indexDernierLabel):
             aRemonter=i+1
             nomLineEdit="lineEditVal"+str(aRemonter)
             courant=getattr(self,nomLineEdit)
             valeurARemonter=courant.text()
             nomLineEdit="lineEditVal"+str(i)
             courant=getattr(self,nomLineEdit)
             courant.setText(valeurARemonter)
         nomLineEdit="lineEditVal"+str(self.indexDernierLabel)
         courant=getattr(self,nomLineEdit)
         courant.setText("")
       self.changeValeur(changeDePlace=False)

   def plusPushed(self):
       if self.indexDernierLabel == self.monSimpDef.max:
          self.editor.affiche_infos('nb max de valeurs : '+str(self.monSimpDef.max)+' atteint')
          return
       self.ajoutLineEdit()
       if self.NumLineEditEnCours==self.indexDernierLabel : return
       nomLineEdit="lineEditVal"+str(self.NumLineEditEnCours+1)
       courant=getattr(self,nomLineEdit)
       valeurADescendre=courant.text()
       courant.setText("")
       for i in range (self.NumLineEditEnCours+1, self.indexDernierLabel):
             aDescendre=i+1
             nomLineEdit="lineEditVal"+str(aDescendre)
             courant=getattr(self,nomLineEdit)
             valeurAGarder=courant.text()
             courant.setText(valeurADescendre)
             valeurADescendre=valeurAGarder
       self.changeValeur(changeDePlace=False)
       self.scrollArea.ensureWidgetVisible(self.LineEditEnCours)

   def voisListePushed(self):
       print "voisListePushed"
       texteValeurs=""
       for v in self.node.item.GetListeValeurs():
          texteValeurs+=str(v)+", "
       entete="Valeurs pour "+self.nom
       f=ViewText(self,self.editor,entete,texteValeurs[0:-2])
       f.show()

   def salomePushed(self):
       print "salomePushed"

   def salomeVuePushed(self):
       print "salomeVuePushed"

