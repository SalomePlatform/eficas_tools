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

from desWidgetCommentaire import Ui_WidgetCommentaire
from gereIcones import FacultatifOuOptionnel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
import Accas 
import os
import string

    
# Import des panels

class MonWidgetCommentaire(QWidget,Ui_WidgetCommentaire,FacultatifOuOptionnel):
  """
  """
  def __init__(self,node,editor,commentaire):
      QWidget.__init__(self,None)
      self.node=node
      self.node.fenetre=self
      self.setupUi(self)
      self.editor=editor
      self.setIconePoubelle()
      self.remplitTexte()
      if self.editor.code in ['MAP','CARMELCND'] : self.bCatalogue.close()
      else : self.connect(self.bCatalogue,SIGNAL("clicked()"), self.afficheCatalogue)
      self.connect(self.commentaireLE,SIGNAL("returnPressed()"),self.TexteCommentaireEntre)
       
  def afficheCatalogue(self):
      if self.editor.code != "CARMELCND" : self.monOptionnel.hide()
      self.node.tree.racine.affichePanneau()
      if self.node : self.node.select()
      else : self.node.tree.racine.select()

  def remplitTexte(self):
      texte=self.node.item.get_valeur()
      self.commentaireLE.setText(texte)
      if self.editor.code == "CARMELCND" and texte[0:16]=="Cree - fichier :" :
         self.commentaireLE.setDisabled(True)
         self.commentaireLE.setStyleSheet(QString.fromUtf8("background:rgb(244,244,244);\n" "border:0px;\n"))
         self.commentaireLE.setToolTip(tr("Valeur non modifiable"))

  def donnePremier(self):
      self.commentaireLE.setFocus(7)


  def TexteCommentaireEntre(self):
      texte=str(self.commentaireLE.text())
      self.editor.init_modif()
      self.node.item.set_valeur(texte)
      self.node.update_node()

