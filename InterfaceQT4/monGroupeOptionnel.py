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

from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets import QCheckBox, QWidget, QLabel
    from PyQt5.QtCore import Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *

from Extensions.i18n import tr
from desGroupeOptionnel import Ui_groupeOptionnel

    
# Import des panels

class monButtonCustom(QCheckBox):

   def __init__(self,texte,monOptionnel,parent=None):
      QCheckBox.__init__(self,tr(texte),parent)
      self.texte=texte
      self.monOptionnel=monOptionnel

   def mouseDoubleClickEvent(self, event):
      #print "dans mouseDoubleClickEvent", self
      if self not in self.monOptionnel.dicoCb.keys() : 
         event.accept()
         return
      listeCheckedMC="+"+self.monOptionnel.dicoCb[self]
      self.monOptionnel.parentMC.ajoutMC(listeCheckedMC)
      event.accept()
      

   def mousePressEvent(self, event):
      #rint "dans mousePressEvent"
      self.mousePressed=True
      if not( event.button() != Qt.RightButton)  : 
         event.accept()
         return
      QCheckBox.mousePressEvent(self, event)
      event.accept()


class MonGroupeOptionnel (QWidget,Ui_groupeOptionnel):
  """
  """
  def __init__(self,liste,parentQt,parentMC):
     #print "dans init de monWidgetOptionnel ", parentQt, parentQt.node.item.nom
     QWidget.__init__(self,None)
     self.setupUi(self)
     self.listeChecked=[]
     self.dicoCb={}
     self.mousePressed=False
     self.cbPressed=None
     self.cb=None
     self.parentQt=parentQt
     self.parentMC=parentMC
     self.afficheTitre()
     if liste != [] : self.affiche(liste)
     else : self.MCOptionnelLayout.insertWidget(0,QLabel(tr('Pas de MC Optionnel')))


  def afficheTitre(self):
     labeltext,fonte,couleur = self.parentMC.node.item.GetLabelText()
     l=tr(labeltext)
     li=[]
     while len(l) > 25:
         li.append(l[0:24])
         l=l[24:]
     li.append(l)
     texte=""
     for l in li : texte+=l+"\n"
     texte=texte[0:-2]
     self.MCLabel.setText(texte)

  def affiche(self,liste):
     #print "dans Optionnel ____ affiche", liste
     self.dicoCb={}
     liste.reverse()
     for mot in liste :
         cb = monButtonCustom(mot,self)
         #if monEnvQT5:
         #  cb.clicked.connect(self.ajoutMC)
         #else :
         #  self.connect(cb,SIGNAL("clicked()"), self.ajoutMC)
         self.MCOptionnelLayout.insertWidget(0,cb)
         self.dicoCb[cb]=mot
     self.scrollAreaCommandesOptionnelles.horizontalScrollBar().setSliderPosition(0)
     #print "Fin Optionnel ____ affiche", liste

  def CBChecked(self):
      # ordre ?
      return
      for cb in self.dicoCb.keys() :
          if cb.isChecked()      and self.dicoCb[cb] not in self.listeChecked : self.listeChecked.append(self.dicoCb[cb])
          if not(cb.isChecked()) and self.dicoCb[cb] in self.listeChecked     : self.listeChecked.remove(self.dicoCb[cb])
      self.parentMC.recalculeListeMC(self.listeChecked)

#
#  def ajoutMC(self):
#     maListe=""
#     for cb in self.dicoCb.keys():
#         if cb.isChecked() : maListe+="+"+str(cb.text())
#     if maListe=="":return
     #print "dans Optionnel __ ajout de ", maListe
#     self.parentMC.ajoutMC(maListe)
#
