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
     print "dans focusInEvent de LECustom"
     self.parentQt.LineEditEnCours=self
     self.parentQt.NumLineEditEnCours=self.num
     QLineEdit.focusInEvent(self,event)




# ------------- #
class GereListe:
# ------------- #

   def __init__(self):
       self.connecterSignaux()

   def connecterSignaux(self):
       self.connect(self.RBHaut,SIGNAL("clicked()"),self.hautPushed)
       self.connect(self.RBBas,SIGNAL("clicked()"),self.basPushed)
       self.connect(self.RBMoins,SIGNAL("clicked()"),self.moinsPushed)
       self.connect(self.RBPlus,SIGNAL("clicked()"),self.plusPushed)
       self.connect(self.RBVoisListe,SIGNAL("clicked()"),self.voisListePushed)

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
       nomLineEdit=self.nomLine+str(num1)
       #print nomLineEdit
       courant=getattr(self,nomLineEdit)
       valeurAGarder=courant.text()
       nomLineEdit2=self.nomLine+str(num2)
       #print nomLineEdit2
       courant2=getattr(self,nomLineEdit2)
       courant.setText(courant2.text())
       courant2.setText(valeurAGarder)
       self.changeValeur(changeDePlace=False)
       self.NumLineEditEnCours=num2
       self.LineEditEnCours=courant2

   def moinsPushed(self):
       # on supprime le dernier
       if self.NumLineEditEnCours==self.indexDernierLabel : 
          nomLineEdit=self.nomLine+str(aRemonter)
          courant=getattr(self,nomLineEdit)
          courant.setText("")
       else :
         for i in range (self.NumLineEditEnCours, self.indexDernierLabel):
             aRemonter=i+1
             nomLineEdit=self.nomLine+str(aRemonter)
             courant=getattr(self,nomLineEdit)
             valeurARemonter=courant.text()
             nomLineEdit=self.nomLine+str(i)
             courant=getattr(self,nomLineEdit)
             courant.setText(valeurARemonter)
         nomLineEdit=self.nomLine+str(self.indexDernierLabel)
         courant=getattr(self,nomLineEdit)
         courant.setText("")
       self.changeValeur(changeDePlace=False,oblige=True)
       self.setValide()

   def plusPushed(self):
       if self.indexDernierLabel == self.monSimpDef.max:
          self.editor.affiche_infos('nb max de valeurs : '+str(self.monSimpDef.max)+' atteint')
          return
       self.ajoutLineEdit()
       if self.NumLineEditEnCours==self.indexDernierLabel : return
       nomLineEdit=self.nomLine+str(self.NumLineEditEnCours+1)
       courant=getattr(self,nomLineEdit)
       valeurADescendre=courant.text()
       courant.setText("")
       for i in range (self.NumLineEditEnCours+1, self.indexDernierLabel):
             aDescendre=i+1
             nomLineEdit=self.nomLine+str(aDescendre)
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


   def selectInFile(self):
       print "selectInFile"
       init=QString( self.editor.CONFIGURATION.savedir)
       fn = QFileDialog.getOpenFileName(self.node.appliEficas,
                                         tr("Fichier de donnees"),
                                         init,
                                         tr('Tous les  Fichiers (*)',))
       if fn == None : return
       if fn == "" : return
       ulfile = os.path.abspath(unicode(fn))
       self.editor.CONFIGURATION.savedir=os.path.split(ulfile)[0]

       from monSelectVal import MonSelectVal
       MonSelectVal(file=fn,parent=self).show()

  
