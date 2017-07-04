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
from __future__ import print_function
try :
   from builtins import str
   from builtins import range
except : pass

import types,os,sys

# Modules Eficas
from Extensions.i18n import tr
from .feuille         import Feuille


from desWidgetMatrice  import Ui_desWidgetMatrice 

from six.moves import range
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QIcon


class MonWidgetMatrice (Ui_desWidgetMatrice,Feuille):
# c est juste la taille des differents widgets de base qui change

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.monType= self.node.item.object.definition.type[0]
        parentQt.commandesLayout.insertWidget(-1,self)
        self.nbLigs=0
        self.nbCols=0
        self.nomVariables={}
        self.creeColonnes()
        self.connecterSignaux()
        if self.node.item.get_valeur()== None:  self.initialSsValeur()
        else :
           try    : self.initialValeur()
           except : self.initialSsValeur()
        if sys.platform[0:5]!="linux" : 
          repIcon=self.node.editor.appliEficas.repIcon
          fichier=os.path.join(repIcon, 'update.png')
          icon = QIcon(fichier)
          self.PBrefresh.setIcon(icon)
          self.PBrefresh.setIconSize(QSize(32, 32))



  def connecterSignauxQT4(self) :
      self.connect(self.TBMatrice,SIGNAL("itemChanged(QTableWidgetItem *)"),self.itemChanged)
      self.connect(self.PBrefresh,SIGNAL("clicked()"), self.afficheEntete)

  def connecterSignaux(self) :
      self.TBMatrice.itemChanged.connect(self.itemChanged)
      self.PBrefresh.clicked.connect( self.afficheEntete)

  def afficheEntete(self):
      self.objSimp.changeEnteteMatrice()
      self.TBMatrice.clear()
      if self.node.item.get_valeur()== None:  self.initialSsValeur()
      else :
         try    : self.initialValeur()
         except : self.initialSsValeur()
      self.node.item.object.state='changed'
      self.node.item.object.parent.state='changed'
      self.setValide()
      self.parentQt.setValide()
      self.node.item.jdc.isvalid()


  def itemChanged(self):
      monItem=self.TBMatrice.currentItem()
      if monItem==None : return
      texte=monItem.text()
      if texte=="" : return
      #try :
      if 1 :
        val=float(str(texte))
        ok=True
      #except :
      else :
        ok=False
      if ok == False :
	self.editor.affiche_infos(tr("Entrer un float SVP"),Qt.red)
        monItem.setText("")
        return
      if self.monType.valSup != None :
         if val > self.monType.valSup :
	    self.editor.affiche_infos(tr("Entrer un float inferieur a ") + repr(self.monType.valSup),Qt.red)
            monItem.setText("")
            return
      if self.monType.valMin != None :
         if val < self.monType.valMin :
	    self.editor.affiche_infos(tr("Entrer un float superieur a ") + repr(self.monType.valMin),Qt.red)
            monItem.setText("")
            return
      self.editor.affiche_infos("")
      if self.monType.structure != None: MonWidgetMatrice.__dict__[self.monType.structure](*(self,))
      self.acceptVal()


  def symetrique(self):
      monItem=self.TBMatrice.currentItem()
      texte=monItem.text()
      if monItem.row() != monItem.column():
         print(monItem.row(), monItem.column())
         monItemSym=self.TBMatrice.item(monItem.column(), monItem.row())
         monItemSym.setText(texte)

  def creeColonnes(self):
      if self.monType.methodeCalculTaille != None :
	 #try:
         if 1 :
           MonWidgetMatrice.__dict__[self.monType.methodeCalculTaille](*(self,))
         else :
         #except :
           QMessageBox.critical( self, tr("Mauvaise execution "),tr( "impossible d executer la methode ") + monType.methodeCalculTaille )
           return
      else :
         self.nbLigs=self.monType.nbLigs
         self.nbCols=self.monType.nbCols


  def  NbDeVariables(self):
       jdc=self.node.item.object.jdc
       etape=self.node.item.object.etape
       self.listeVariables=jdc.get_variables(etape)
       if self.listeVariables == [] :
           QMessageBox.critical( self, tr("Mauvaise Commande "),tr( "Aucune variable connue"))
           return
       self.TBMatrice.setColumnCount(len(self.listeVariables))
       self.TBMatrice.setRowCount(len(self.listeVariables))
       self.nbLigs=len(self.listeVariables)
       self.nbCols=len(self.listeVariables)

  def  NbDeDistributions(self):
       jdc=self.node.item.object.jdc
       etape=self.node.item.object.etape
       self.listeVariables=jdc.get_distributions(etape)
       if self.listeVariables == [] :
           QMessageBox.critical( self, tr("Mauvaise Commande "),tr( "Aucune variable connue"))
           return
       self.TBMatrice.setColumnCount(len(self.listeVariables))
       self.TBMatrice.setRowCount(len(self.listeVariables))
       self.nbLigs=len(self.listeVariables)
       self.nbCols=len(self.listeVariables)

  def  initialSsValeur(self):
       for row in range(self.nbLigs):
	   for column in range(self.nbCols):
	       if row == column :
	          initialFloat=1
               else :
	          initialFloat=0
               self.TBMatrice.setItem(row,column,QTableWidgetItem(str(initialFloat)))
       #header=QStringList()
       header=[]
       for var in self.listeVariables :
#	   header << var
           header.append(var)
       self.TBMatrice.setVerticalHeaderLabels(header)
       self.TBMatrice.setHorizontalHeaderLabels(header)

  def  initialValeur(self):
      liste=self.node.item.get_valeur()
      dejaAffiche=0
      if (len(liste)) != self.nbLigs +1  :
         QMessageBox.critical( self,tr( "Mauvaise dimension de matrice"),tr( "le nombre de ligne n est pas egal a ") + str(self.nbLigs))
         dejaAffiche=1
         raise  EficasException('dimension')
      for i in range(self.nbLigs):
          inter=liste[i+1]
          if (len(inter)) != self.nbCols and (dejaAffiche == 0 ) :
             QMessageBox.critical( self, tr("Mauvaise dimension de matrice"), tr("le nombre de colonne n est pas egal a ") + str(self.nbCols))
             dejaAffiche=1
             raise  EficasException('dimension')
          for j in range(self.nbCols):
              self.TBMatrice.setItem(i,j,QTableWidgetItem(str(liste[i+1][j])))
      header=QStringList()
      for var in liste[0]:
	   header << var
      self.TBMatrice.setVerticalHeaderLabels(header)
      self.TBMatrice.setHorizontalHeaderLabels(header)
              
  def acceptVal(self):
      liste=[]
      liste.append(self.listeVariables)
      if self.TBMatrice.rowCount() != self.nbLigs :
         QMessageBox.critical( self, tr("Mauvaise dimension de matrice"),tr( "le nombre de ligne n est pas egal a ") + str(self.nbLigs))
      if self.TBMatrice.columnCount() != self.nbCols :
         QMessageBox.critical( self, tr("Mauvaise dimension de matrice"), tr("le nombre de colonne n est pas egal a ") + str(self.nbCols))
      for i in range(self.nbLigs):
          listeCol=[]
          for j in range(self.nbCols):
              monItem=self.TBMatrice.item(i,j)       
              texte=monItem.text()
              try :
                 val=float(str(texte))
                 ok=True
              except :
                 ok=False
              #val,ok=texte.toDouble() 
              if ok == False :
                 QMessageBox.critical( self, tr("Mauvaise Valeur"),tr( "l element ") + str(i) + "," +str(j) +tr("n est pas correct"))
              listeCol.append(val)
          liste.append(listeCol)
      # on ajoute l ordre des variables aux valeurs
      self.node.item.set_valeur(liste)
