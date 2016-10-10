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
    from PyQt5.QtWidgets import QCheckBox, QWidget
    from PyQt5.QtCore import Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *

from Extensions.i18n import tr
from desWidgetOptionnel import Ui_WidgetOptionnel
from monGroupeOptionnel import MonGroupeOptionnel

    
# Import des panels
class  MonWidgetOptionnel (QWidget,Ui_WidgetOptionnel):
  def __init__(self,parentQt):
     #print "dans init de monWidgetOptionnel ", parentQt, parentQt.node.item.nom
     QWidget.__init__(self,None)
     self.setupUi(self)
     self.dicoMCWidgetOptionnel={}
     self.parentQt=parentQt
     self.parentQt.editor.splitterSizes[1]-=self.parentQt.editor.splitterSizes[2]
     self.parentQt.editor.splitterSizes[2]=self.parentQt.editor.oldSizeWidgetOptionnel
     if self.parentQt.editor.splitterSizes[2] == 0 : self.parentQt.editor.splitterSizes[2] = 400
     self.parentQt.editor.restoreSplitterSizes()
     self.show()

  def afficheOptionnel(self,liste,MC):
     #print "dans Optionnel ____ affiche", liste 
     self.vireLesAutres(MC)
     if self.dicoMCWidgetOptionnel.has_key(MC.node.item.nom) :
        self.dicoMCWidgetOptionnel[MC.node.item.nom].setParent(None)
        self.dicoMCWidgetOptionnel[MC.node.item.nom].close()
     groupe = MonGroupeOptionnel(liste,self,MC)
     self.groupesOptionnelsLayout.insertWidget(0,groupe)
     self.dicoMCWidgetOptionnel[MC.node.item.nom]=groupe
     return groupe

  def vireLesAutres(self,MC):
      #print "je passe dans vireLesAutres"
      genea =MC.obj.get_genealogie()
      #print genea
      for k in self.dicoMCWidgetOptionnel.keys():
          if k not in genea :  
             self.dicoMCWidgetOptionnel[k].close()
             del self.dicoMCWidgetOptionnel[k]
          #if k not in genea :  print k
      #print "________"
      
  def afficheOptionnelVide(self):
      self.GeneaLabel.setText("")
      for k in self.dicoMCWidgetOptionnel.keys():
            self.dicoMCWidgetOptionnel[k].close()
            del self.dicoMCWidgetOptionnel[k]

  def titre(self,MC):
     labeltext,fonte,couleur = self.parentCommande.node.item.GetLabelText()
     l=tr(labeltext)
     li=[]
     while len(l) > 25:
         li.append(l[0:24])
         l=l[24:]
     li.append(l)
     texte=""
     for l in li : texte+=l+"\n"
     texte=texte[0:-2]
     self.GeneaLabel.setText(tr("Options pour \n") +texte)
