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
from Extensions.i18n import tr

from desMatrice           import Ui_desMatrice


class MonMatricePanel(Ui_desMatrice,QDialog):
  """
  Classe dÃ©finissant le panel Matrice
  Attention n herite pas de QtPanel
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
       QDialog.__init__(self,parent)
       self.node=node
       self.editor = parent
       self.nbLigs=0
       self.nbCols=0
       self.monType= self.node.item.object.definition.type[0]
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
       self.initVal()
       self.creeColonnes()
       self.connecterSignaux()
       if self.node.item.get_valeur()== None:
          self.initialSsValeur()
       else :
          try :
             self.initialValeur()
          except :
             self.initialSsValeur()

  def initVal(self):
      self.nomVariables={}

  def connecterSignaux(self) :
      self.connect(self.TBMatrice,SIGNAL("itemChanged(QTableWidgetItem *)"),self.itemChanged)
      self.connect(self.BOk,SIGNAL("clicked()"),self.acceptVal)

  def itemChanged(self):
      monItem=self.TBMatrice.currentItem()
      if monItem==None : return
      texte=monItem.text()
      if texte=="" : return
      val,ok=texte.toDouble() 
      if ok == False :
	self.editor.affiche_infos(tr("Entrer un float SVP"),Qt.red)
        monItem.setText("")
        return
      if self.monType.valSup != None :
         if val > self.monType.valSup :
	    self.editor.affiche_infos(tr("Entrer un float inférieur à ") + repr(self.monType.valSup),Qt.red)
            monItem.setText("")
            return
      if self.monType.valMin != None :
         if val < self.monType.valMin :
	    self.editor.affiche_infos(tr("Entrer un float superieur a ") + repr(self.monType.valMin),Qt.red)
            monItem.setText("")
            return
      self.editor.affiche_infos("")
      if self.monType.structure != None:
           apply (MonMatricePanel.__dict__[self.monType.structure],(self,))


  def symetrique(self):
      monItem=self.TBMatrice.currentItem()
      texte=monItem.text()
      if monItem.row() != monItem.column():
         monItemSym=self.TBMatrice.item(monItem.column(), monItem.row())
         monItemSym.setText(texte)

  def creeColonnes(self):
      if self.monType.methodeCalculTaille != None :
	 #try:
         if 1 :
           apply (MonMatricePanel.__dict__[self.monType.methodeCalculTaille],(self,))
         else :
         #except :
           QMessageBox.critical( self, tr("Mauvaise execution "),tr( "impossible d executer la méthode ") + monType.methodeCalculTaille )
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

  def  initialSsValeur(self):
       for row in range(self.nbLigs):
	   for column in range(self.nbCols):
	       if row == column :
	          initialFloat=1
               else :
	          initialFloat=0
               self.TBMatrice.setItem(row,column,QTableWidgetItem(str(initialFloat)))
       header=QStringList()
       for var in self.listeVariables :
	   header << var
       self.TBMatrice.setVerticalHeaderLabels(header)
       self.TBMatrice.setHorizontalHeaderLabels(header)

  def  initialValeur(self):
      liste=self.node.item.get_valeur()
      dejaAffiche=0
      if (len(liste)) != self.nbLigs +1  :
         QMessageBox.critical( self,tr( "Mauvaise dimension de matrice"),tr( "le nombre de ligne n est pas egal a ") + str(self.nbLigs))
         dejaAffiche=1
      for i in range(self.nbLigs):
          inter=liste[i+1]
          if (len(inter)) != self.nbCols and (dejaAffiche == 0 ) :
             QMessageBox.critical( self, tr("Mauvaise dimension de matrice"), tr("le nombre de colonne n est pas egal a ") + str(self.nbCols))
             dejaAffiche=1
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
              val,ok=texte.toDouble() 
              if ok == False :
                 QMessageBox.critical( self, tr("Mauvaise Valeur"),tr( "l element ") + str(i) + "," +str(j) +tr("n est pas correct"))
              listeCol.append(val)
          liste.append(listeCol)
      # on ajoute l ordre des variables aux valeurs
      self.node.item.set_valeur(liste)
