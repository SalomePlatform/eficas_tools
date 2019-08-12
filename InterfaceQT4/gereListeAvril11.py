# -*- coding: utf-8 -*-
# Copyright (C) 2007-2017   EDF R&D
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

from __future__ import absolute_import
try :
   from builtins import str
   from builtins import range
   from builtins import object
except : pass

import types,os
import traceback


import six
from six.moves import range
from PyQt5.QtWidgets import QLineEdit, QLabel, QFileDialog, QWidget
from PyQt5.QtCore    import QEvent, Qt, QTimer
from PyQt5.QtGui     import QIcon, QPalette

from Extensions.i18n import tr
from InterfaceQT4.monViewTexte   import ViewText


# ---------------------- #
class LECustom(QLineEdit):
# ---------------------- #
 def __init__(self,parent,parentQt,i):
        """
        Constructor
        """
        QLineEdit.__init__(self,parent)
        
        self.valeur=None
        self.aEuLeFocus=False
        self.parentQt=parentQt
        self.parent=parent
        self.num=i
        self.dansUnTuple=False
        self.numDsLaListe=-1
        self.returnPressed.connect(self.litValeur)

 def focusInEvent(self,event):
     #print ("dans focusInEvent de LECustom",self.parentQt)
     print ("dans focusInEvent de LECustom",self.num,self.numDsLaListe)
     self.parentQt.aEuLeFocus=True
     self.aEuLeFocus=True
     self.parentQt.LineEditEnCours=self
     self.parentQt.numLineEditEnCours=self.num
     self.parentQt.textSelected=self.text()
     self.setStyleSheet("border: 2px solid gray")
     QLineEdit.focusInEvent(self,event)

 def focusOutEvent(self,event):
     #print ("dans focusOutEvent de LECustom",self.num,self.numDsLaListe, self.aEuLeFocus)
     self.setStyleSheet("border: 0px")
     if self.dansUnTuple    : self.setStyleSheet("background:rgb(235,235,235); border: 0px;")
     elif self.num % 2 == 1 : self.setStyleSheet("background:rgb(210,210,210)")
     else                   : self.setStyleSheet("background:rgb(235,235,235)")
     
     if self.aEuLeFocus:
       self.aEuLeFocus=False
       self.litValeur()
     QLineEdit.focusOutEvent(self,event)

 def litValeur(self):
     self.aEuLeFocus=False
     val=str(self.text())
     if str(val)=="" or val==None : 
        self.valeur=None 
        return
     try :
       valeur=eval(val,{})
     except :
       try :
          d=self.parentQt.parentQt.objSimp.jdc.getContexteAvant(self.parentQt.objSimp. etape)
          valeur=eval(val,d)
       except :
          valeur=val

     self.valeur=valeur

 def clean(self):
     self.setText("")

 def getValeur(self):
     return self.text()

 def setValeur(self,valeur):
     self.setText(valeur)
     self.valeur=valeur

 #def leaveEvent(self,event):
 #   ne sert a rien. quand on modifie la valeur on prend le focus

    

# --------------------------- #
class LECustomTuple(LECustom):
# --------------------------- #
 def __init__(self,parent):
   #  index sera mis a jour par TupleCustom
   parentQt=parent.parent().parent().parent()
   LECustom. __init__(self,parent,parentQt,0)
   #print (dir(self))

# ---------------------------- #
class MonLabelListeClic(QLabel):
# ---------------------------- #
     def __init__(self,parent):
        QLabel.__init__(self,parent)
        self.parent=parent

     def event(self,event) :
         if event.type() == QEvent.MouseButtonRelease:
            self.texte=self.text()
            self.parent.traiteClicSurLabelListe(self.texte)
         return QLabel.event(self,event)




# ------------- #
class GereListe(object):
# ------------- #

   def __init__(self):
       self.aEuLeFocus=False
       self.connecterSignaux()


   def leaveEvent(self,event):
       if self.aEuLeFocus : 
          print ('appel de changeValeur')
          self.changeValeur()
          self.aEuLeFocus=False
       QWidget.leaveEvent(self,event)

   def connecterSignaux(self):
       if hasattr(self,'RBHaut'):
          self.RBHaut.clicked.connect(self.hautPushed)
          self.RBBas.clicked.connect(self.basPushed)
          self.RBMoins.clicked.connect(self.moinsPushed)
          self.RBPlus.clicked.connect(self.plusPushed)
          self.RBVoisListe.clicked.connect(self.voisListePushed)
       if hasattr(self,'PBAlpha'):
          self.PBCata.clicked.connect(self.cataPushed)
          self.PBAlpha.clicked.connect(self.alphaPushed)
          self.PBFind.clicked.connect(self.findPushed)
          self.LEFiltre.returnPressed.connect(self.LEFiltreReturnPressed)

   def filtreListe(self):
       l=[]
       if self.filtre != "" :
          for i in self.listeAAfficher :
              if i.find(self.filtre) == 0 :l.append(i)
          self.listeAAfficher=l
       if self.alpha : self.listeAAfficher.sort()
      
   def LEFiltreReturnPressed(self):
       self.filtre= self.LEFiltre.text()
       self.prepareListeResultatFiltre()

   def findPushed(self):
       self.filtre= self.LEFiltre.text()
       self.prepareListeResultatFiltre()

   def alphaPushed(self):
       #print "alphaPushed" ,self.alpha
       if self.alpha == 1 : return
       self.alpha=1
       self.prepareListeResultat()

   def cataPushed(self):
       if self.alpha == 0 : return
       self.alpha=0
       self.prepareListeResultat()

   def hautPushed(self):
       if self.numLineEditEnCours == 1 : return
       else : numEchange=self.numLineEditEnCours-1
       self.echange(self.numLineEditEnCours,numEchange)
       self.LineEditEnCours.setFocus(True)
       self.scrollArea.ensureWidgetVisible(self.LineEditEnCours)


   def basPushed(self):
       if self.numLineEditEnCours == self.indexDernierLabel : return
       else : numEchange=self.numLineEditEnCours+1
       self.echange(self.numLineEditEnCours,numEchange)
       self.LineEditEnCours.setFocus(True)
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
       self.numLineEditEnCours=num2
       self.LineEditEnCours=courant2
       self.LineEditEnCours.setFocus(True)

   def moinsPushed(self):
       # on supprime le dernier
       if self.numLineEditEnCours == 0 : return
       if self.indexDernierLabel == 0 : return
       if self.numLineEditEnCours==self.indexDernierLabel : 
          nomLineEdit=self.nomLine+str(self.indexDernierLabel)
          courant=getattr(self,nomLineEdit)
          courant.clean()
       else :
         for i in range (self.numLineEditEnCours, self.indexDernierLabel):
             aRemonter=i+1
             nomLineEdit=self.nomLine+str(aRemonter)
             courant=getattr(self,nomLineEdit)
             valeurARemonter=courant.getValeur()
             nomLineEdit=self.nomLine+str(i)
             courant=getattr(self,nomLineEdit)
             if valeurARemonter != None : courant.setValeur(valeurARemonter)
             else : courant.clean()
         nomLineEdit=self.nomLine+str(self.indexDernierLabel)
         courant=getattr(self,nomLineEdit)
         courant.clean()
       self.changeValeur(changeDePlace=False,oblige=True)
       self.setValide()

   def plusPushed(self):
       if self.indexDernierLabel == self.monSimpDef.max:
          if len(self.listeValeursCourantes) < self.monSimpDef.max : self.chercheLigneVide()
          else : self.editor.afficheInfos('nb max de valeurs : '+str(self.monSimpDef.max)+' atteint',Qt.red)
          return
       self.ajoutLineEdit()
       self.descendLesLignes()
       self.chercheLigneVide()
       QTimer.singleShot(1, self.rendVisibleLigne)

   def chercheLigneVide(self):
       for i in range(self.indexDernierLabel) :
          nomLineEdit=self.nomLine+str(i+1)
          courant=getattr(self,nomLineEdit)
          valeur=courant.getValeur()
          if valeur=="" : 
             courant.setFocus(True)
             self.estVisible=courant
             return


   def descendLesLignes(self):
       if self.numLineEditEnCours==self.indexDernierLabel : return
       nomLineEdit=self.nomLine+str(self.numLineEditEnCours+1)
       courant=getattr(self,nomLineEdit)
       valeurADescendre=courant.getValeur()
       courant.clean()
       for i in range (self.numLineEditEnCours+1, self.indexDernierLabel):
             aDescendre=i+1
             nomLineEdit=self.nomLine+str(aDescendre)
             courant=getattr(self,nomLineEdit)
             valeurAGarder=courant.getValeur()
             courant.setValeur(valeurADescendre)
             valeurADescendre=valeurAGarder
       self.changeValeur(changeDePlace=False)
       if hasattr (self, 'LineEditEnCours') :self.scrollArea.ensureWidgetVisible(self.LineEditEnCours)

   def voisListePushed(self):
       texteValeurs=""
       for v in self.node.item.getListeValeurs():
          texteValeurs+=str(v)+", "
       entete="Valeurs pour "+self.nom
       f=ViewText(self,self.editor,entete,texteValeurs[0:-2])
       f.show()


   def selectInFile(self):
       init=str( self.editor.maConfiguration.savedir)
       fn = QFileDialog.getOpenFileName(self.node.appliEficas,
                                         tr("Fichier de donnees"),
                                         init,
                                         tr('Tous les  Fichiers (*)',))
       fn=fn[0]
       if fn == None : return
       if fn == "" : return
       ulfile = os.path.abspath(six.text_type(fn))
       self.editor.maConfiguration.savedir=os.path.split(ulfile)[0]

       from .monSelectVal import MonSelectVal
       MonSelectVal(file=fn,parent=self).show()

   def noircirResultatFiltre(self):
      filtre=str(self.LEFiltre.text())
      for cb in self.listeCbRouge:
          palette = QPalette(Qt.red)
	  palette.setColor(QPalette.WindowText,Qt.black)
	  cb.setPalette(palette)
          t=cb.text()
          cb.setText(t)
      self.LEFiltre.setText("")
      self.listeCbRouge = []

  
# ----------- #
class GerePlie(object):
# ----------- #

   def gereIconePlier(self):
      if not(hasattr(self,'BFermeListe')) : return
      self.editor.listeDesListesOuvertes.add(self.node.item)
      repIcon=self.node.editor.appliEficas.repIcon
      if not (self.editor.afficheListesPliees):
         fichier=os.path.join(repIcon, 'empty.png')
         icon = QIcon(fichier)
         self.BFermeListe.setIcon(icon)
         return
      fichier=os.path.join(repIcon, 'minusnode.png')
      icon = QIcon(fichier)
      self.BFermeListe.setIcon(icon)
      self.BFermeListe.clicked.connect( self.selectWidgetPlie)

   def selectWidgetPlie(self):
      self.editor.listeDesListesOuvertes.remove(self.node.item)
      self.reaffichePourDeplier()

        
     