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
# Modules Eficas

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
from desWidgetOptionnel import Ui_WidgetOptionnel

    
# Import des panels

class monButtonCustom(QCheckBox):

   def __init__(self,texte,monOptionnel,parent=None):
      QCheckBox.__init__(self,texte,parent)
      self.monOptionnel=monOptionnel

   def mouseDoubleClickEvent(self, event):
      #print "dans mouseDoubleClickEvent"
      if self not in self.monOptionnel.dicoCb.keys() : return
      listeCheckedMC="+"+self.monOptionnel.dicoCb[self]
      self.monOptionnel.parentMC.ajoutMC(listeCheckedMC)
      self.setChecked(False)

   def mousePressEvent(self, event):
      #print "dans mousePressEvent"
      self.mousePressed=True
      if not( event.button() != Qt.RightButton)  : return
      QCheckBox.mousePressEvent(self, event)


class MonWidgetOptionnel (QWidget,Ui_WidgetOptionnel):
  """
  """
  def __init__(self,parentQt):
     #print "dans init de monWidgetOptionnel ", parentQt, parentQt.node.item.nom
     QWidget.__init__(self,None)
     self.setupUi(self)
     self.dicoCb={}
     self.parentMC=None
     self.listeChecked=[]
     self.mousePressed=False
     self.cbPressed=None
     self.cb=None
     self.parentQt=parentQt
     self.connect(self.bAjoutMC,SIGNAL("clicked()"), self.ajoutMC)

     

  def affiche(self,liste):
     self.show()
     labeltext,fonte,couleur = self.parentMC.node.item.GetLabelText()
     self.GeneaLabel.setText(tr("Options pour \n") +labeltext)

     for cb in self.dicoCb.keys():
         cb.close()
     self.dicoCb={}
     #print liste
     liste.reverse()
     for mot in liste :
         cb = monButtonCustom(QString(mot),self)
         self.dicoCb[cb]=mot
         self.commandesOptionnellesLayout.insertWidget(0,cb)

  def CBChecked(self):
      # ordre ?
      #print "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
      return
      for cb in self.dicoCb.keys() :
          if cb.isChecked()      and self.dicoCb[cb] not in self.listeChecked : self.listeChecked.append(self.dicoCb[cb])
          if not(cb.isChecked()) and self.dicoCb[cb] in self.listeChecked     : self.listeChecked.remove(self.dicoCb[cb])
      self.parentMC.recalculeListeMC(self.listeChecked)


  def ajoutMC(self):
     maListe=""
     for cb in self.dicoCb.keys():
         if cb.isChecked() : maListe+="+"+str(cb.text())
     if maListe=="":return
     self.parentMC.ajoutMC(maListe)
