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
# Modules Eficas

from __future__ import absolute_import
from PyQt5.QtWidgets import QCheckBox, QWidget, QLabel, QPushButton
from PyQt5.QtCore    import Qt, QRect
from PyQt5.QtGui     import QPalette

from Extensions.i18n    import tr
from desGroupeOptionnel import Ui_groupeOptionnel
from desPBOptionnelMT   import Ui_customPB

    
# Import des panels

class MonRBButtonCustom(QCheckBox):

   def __init__(self,texte,monOptionnel,parent=None,couleur=None):
      QCheckBox.__init__(self,tr(texte),parent)
      self.mousePressed=True
      self.monOptionnel=monOptionnel
      self.setToolTip(tr("clicker: affichage aide, double-click: ajout"))
      if couleur != None :
         mapalette=self.palette()
         mapalette.setColor( QPalette.WindowText, couleur )
         mapalette.setColor( QPalette.Base, Qt.green )
         self.setPalette( mapalette );
         self.setText(tr(texte))
         try :
           monToolTip=monOptionnel.parentMC.dictToolTipMc[texte]
           self.setToolTip(monToolTip)
         except :
           pass


   def mouseDoubleClickEvent(self, event):
      #print "dans mouseDoubleClickEvent", self
      if self not in self.monOptionnel.dicoCb: 
         event.accept()
         return
      listeCheckedMC="+"+self.monOptionnel.dicoCb[self]
      self.monOptionnel.parentMC.ajoutMC(listeCheckedMC)
      event.accept()
      

   def mousePressEvent(self, event):
      if not( event.button() != Qt.RightButton)  : 
         event.accept()
         return
      if self.monOptionnel.cbPressed != None :
         self.monOptionnel.cbPressed.setChecked(False)
      self.monOptionnel.cbPressed=self
      if self.mousePressed == False :
         self.mousePressed=True
      else :
         self.mousePressed=False
         self.ajoutAideMC()
      QCheckBox.mousePressEvent(self, event)
      event.accept()

   def ajoutAideMC(self):
      try :
        maDefinition = self.monOptionnel.parentMC.definition.entites[self.texte]
        maLangue =  self.monOptionnel.parentMC.jdc.lang
        if hasattr(maDefinition,maLangue): 
          monAide = getattr(maDefinition,self.monOptionnel.parentMC.jdc.lang)
        else : 
          monAide = ""
      except :
          monAide = ""
      self.monOptionnel.parentMC.editor.afficheCommentaire(monAide)
  
class MonPBButtonCustom(QWidget,Ui_customPB):

   def __init__(self,texte,monOptionnel,parent=None,couleur=None):
      QWidget.__init__(self)
      self.setupUi(self)
      if couleur != None :
         print ( 'je change pour ', texte)
         self.monPb.setText(texte)
         self.monPb.setStyleSheet( "background:rgb(229,62,30);\n"
"border-radius : 10px;\n"
"border-width : 30 px;\n"
"border-color : beige;\n"
"\n"
"")


         #mapalette=self.monPb.palette()
         #mapalette.setColor( QPalette.ButtonText, Qt.red )
         #self.monPb.setPalette( mapalette )
         self.monPb.update()
         #self.update()
         try :
           monToolTip=monOptionnel.parentMC.dictToolTipMc[texte]
           self.monPb.setToolTip(monToolTip)
         except :
           pass
      self.monPb.setText(texte)
      self.monPb.clicked.connect(self.ajoutMC)

      self.texte=texte
      self.monOptionnel=monOptionnel
      self.definitAideMC()
      self.setToolTip(self.monAide)

   def ajoutMC (self) :
      listeCheckedMC="+"+self.monOptionnel.dicoCb[self]
      self.monOptionnel.parentMC.ajoutMC(listeCheckedMC)

   def definitAideMC(self):
      try :
        maDefinition = self.monOptionnel.parentMC.definition.entites[self.texte]
        maLangue =  self.monOptionnel.parentMC.jdc.lang
        if hasattr(maDefinition,maLangue): 
          self.monAide = getattr(maDefinition,self.monOptionnel.parentMC.jdc.lang)
      except :
          self.monAide = ""
        
class MonGroupeOptionnel (QWidget,Ui_groupeOptionnel):
  """
  """
  def __init__(self,liste,liste_rouge,parentQt,parentMC):
     #print "dans init de monWidgetOptionnel ", parentQt, liste,parentMC
     QWidget.__init__(self,None)
     self.setupUi(self)
     self.listeChecked=[]
     self.dicoCb={}
     self.mousePressed=False
     self.cbPressed=None
     self.cb=None
     self.parentQt=parentQt
     self.parentMC=parentMC
     

     if liste != [] : 
        self.affiche(liste,liste_rouge)
        self.afficheTitre()
     elif self.parentQt.parentQt.maConfiguration.afficheOptionnelVide != False : 
        self.afficheTitre()
        self.MCOptionnelLayout.insertWidget(0,QLabel(tr('Pas de MC Optionnel')))
     else :
        self.frameLabelMC.close()
     #print "dans fin de monWidgetOptionnel ", parentQt


  def afficheTitre(self):
     labeltext,fonte,couleur = self.parentMC.node.item.getLabelText()
     #print (labeltext)
     l=tr(labeltext)
     li=[]
     while len(l) > 25:
         li.append(l[0:24])
         l=l[24:]
     li.append(l)
     texte=""
     for l in li : texte+=l+"\n"
     texte=texte[0:-1]
     self.MCLabel.setText(texte)

  def affiche(self,liste,liste_rouge):
     #print ("dans Optionnel ____ affiche", liste,liste_rouge)
     self.dicoCb={}
     liste.reverse()
     for mot in liste :
         #if mot in liste_rouge : print ('je dois afficher en rouge' , mot)
         couleur=None
         if mot in liste_rouge : couleur=Qt.red 
         if self.parentQt.parentQt.maConfiguration.simpleClic == False :
            cb = MonRBButtonCustom(mot,self,couleur=couleur)
            cb.clicked.connect(cb.ajoutAideMC)
         else :
            cb = MonPBButtonCustom(mot,self,couleur=couleur)

         self.MCOptionnelLayout.insertWidget(0,cb)
         self.dicoCb[cb]=mot
     self.scrollAreaCommandesOptionnelles.horizontalScrollBar().setSliderPosition(0)

