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

from __future__ import absolute_import
from PyQt5.QtWidgets import QCheckBox, QWidget
from PyQt5.QtCore import Qt

from Extensions.i18n import tr
from desWidgetOptionnel import Ui_WidgetOptionnel
from .monGroupeOptionnel import MonGroupeOptionnel

    
# Import des panels
class  MonWidgetOptionnel (QWidget,Ui_WidgetOptionnel):
  def __init__(self,parentQt):
     #print "dans init de monWidgetOptionnel ", parentQt, parentQt.node.item.nom
     QWidget.__init__(self,None)
     self.setupUi(self)
     self.dicoMCWidgetOptionnel={}
     self.parentQt=parentQt

  def afficheOptionnel(self,liste,MC):
     #print "dans Optionnel ____ affiche", liste 
     self.vireLesAutres(MC)
     if MC.node.item.nom in self.dicoMCWidgetOptionnel :
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
      for k in list(self.dicoMCWidgetOptionnel.keys()):
          if k not in genea :  
             self.dicoMCWidgetOptionnel[k].close()
             del self.dicoMCWidgetOptionnel[k]
          #if k not in genea :  print k
      #print "________"
      
  def afficheOptionnelVide(self):
      self.GeneaLabel.setText("")
      for k in list(self.dicoMCWidgetOptionnel.keys()):
            self.dicoMCWidgetOptionnel[k].close()
            del self.dicoMCWidgetOptionnel[k]

  def titre(self,MC):
     if self.parentCommande.node.editor.code in ['Adao','ADAO'] and self.parentCommande.node.editor.closeFrameRechercheCommande==True :
        self.frameLabelCommande.close()
        return
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
