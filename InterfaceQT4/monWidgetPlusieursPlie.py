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
from __future__ import absolute_import
try :
   from builtins import str
except : pass

import types,os,sys,re

from PyQt5.QtWidgets  import   QFrame
from PyQt5.QtCore import QTimer, QSize, Qt
from PyQt5.QtGui  import QIcon, QBrush, QColor

from Extensions.i18n import tr

from .feuille                import Feuille
from desWidgetPlusieursPlie import Ui_WidgetPlusieursPlie 

from .politiquesValidation   import PolitiquePlusieurs
from .qtSaisie               import SaisieValeur

pattern_blanc = re.compile(r"^\s*$")


class MonWidgetPlusieursPlie (Ui_WidgetPlusieursPlie,Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        #print ("MonWidgetPlusieursBase", nom)
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.AAfficher=self.lineEditVal
        self.maCommande.listeAffichageWidget.append(self.lineEditVal)
        if self.node.item.has_into() : 
           self.lineEditVal.setReadOnly(True)
           self.lineEditVal.setStyleSheet("background:rgb(235,235,235);\n")
           self.lineEditVal.setToolTip("Ensemble discret de valeurs possibles, pas de Saisie Manuelle")
           #self.lineEditVal.setPen(QtGui.QColor(0,0,200))
	   #b=QBrush(Qt.DiagCrossPattern)
           #b.setColor(QColor(255,100,0))
           #self.lineEditVal.setBrush(b)
        else :
           self.lineEditVal.returnPressed.connect(self.valeurEntree)
        self.BVisuListe.clicked.connect(self.selectWidgetDeplie)


  def setValeurs(self):
       self.listeValeursCourantes=self.node.item.GetListeValeurs()
       if self.listeValeursCourantes != []  :  self.lineEditVal.setText(str(self.listeValeursCourantes))
       else : self.lineEditVal.setText("")
       self.politique=PolitiquePlusieurs(self.node,self.editor)
       return

  def selectWidgetDeplie(self):
      self.editor.listeDesListesOuvertes.add(self.node.item)
      self.reaffichePourDeplier()

  def valeurEntree(self):
      valeurTexte=self.lineEditVal.text()
      print (valeurTexte[0])
      print (valeurTexte[-1])
      if valeurTexte[0] == '[' or valeurTexte[0] == '('   : valeurTexte = valeurTexte[1:]
      if valeurTexte[-1] == ']' or valeurTexte[-1] == ')' : valeurTexte = valeurTexte[:-1]
      print (valeurTexte)
      listeValeursBrutes=valeurTexte.split(',')
      if listeValeursBrutes == [] or listeValeursBrutes == None : 
         self.lineEditVal.setText(str(self.listeValeursCourantes))
         return
      listeValeur=[]
      for v in listeValeursBrutes: 
          if v == None or pattern_blanc.match(v) : 
             self.editor.affiche_infos(str(listeValeur)+'   Valeurs saisies incorrectes',Qt.red)
             return
          liste,validite=SaisieValeur.TraiteLEValeur(self,str(v))
          if not validite : 
             self.editor.affiche_infos(str(listeValeur) +'   Valeurs saisies incorrectes',Qt.red)
             return
          listeValeur.append(liste[0])
      validite,comm,comm2,listeRetour=self.politique.AjoutValeurs(listeValeur,-1,[])
      if validite : 
         self.node.item.set_valeur(listeValeur)
         self.node.item.isvalid()
         self.setValeurs()
      else :
         self.editor.affiche_infos(str(listeValeur) + '   ' +comm,Qt.red)
         self.lineEditVal.setText('')
       
