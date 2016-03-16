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
    from PyQt5.QtWidgets import QWidget
    from PyQt5.QtCore    import Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *

from desWidgetCommentaire import Ui_WidgetCommentaire
from gereIcones import FacultatifOuOptionnel
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
      self.appliEficas=self.editor.appliEficas
      self.repIcon=self.appliEficas.repIcon
      self.setIconePoubelle()
      self.remplitTexte()
      self.monOptionnel=None

      if monEnvQT5 :
         self.commentaireTE.textChanged.connect(self.TexteCommentaireEntre)
         if self.editor.code in ['MAP','CARMELCND'] : self.bCatalogue.close()
         else : self.bCatalogue.clicked.connect(self.afficheCatalogue)
         if self.editor.code in ['Adao','MAP'] :
               self.bAvant.close()
               self.bApres.close()
         else :
               self.bAvant.clicked.connect(self.afficheAvant)
               self.bApres.clicked.connect(self.afficheApres)
      else :
         if self.editor.code in ['MAP','CARMELCND'] : self.bCatalogue.close()
         else : self.connect(self.bCatalogue,SIGNAL("clicked()"), self.afficheCatalogue)
         if self.editor.code in ['Adao','MAP'] :
               self.bAvant.close()
               self.bApres.close()
         else :
               self.connect(self.bAvant,SIGNAL("clicked()"), self.afficheAvant)
               self.connect(self.bApres,SIGNAL("clicked()"), self.afficheApres)

  def afficheApres(self):
       self.node.selectApres()

  def afficheAvant(self):
       self.node.selectAvant()

       
  def afficheCatalogue(self):
      self.node.tree.racine.affichePanneau()
      if self.node : self.node.select()
      else : self.node.tree.racine.select()

  def remplitTexte(self):
      texte=self.node.item.get_valeur()
      self.commentaireTE.setText(texte)
      if self.editor.code == "CARMELCND" and texte[0:16]=="Cree - fichier :" :
         self.commentaireTE.setReadOnly(True)
         self.commentaireTE.setStyleSheet("background:rgb(244,244,244);\n" "border:0px;\n")
         self.commentaireTE.setToolTip(tr("Valeur non modifiable"))
      else :
         self.commentaireTE.setReadOnly(False)

  def donnePremier(self):
      self.commentaireTE.setFocus(7)


  def TexteCommentaireEntre(self):
      texte=str(self.commentaireTE.toPlainText())
      print texte
      self.editor.init_modif()
      self.node.item.set_valeur(texte)
      self.node.update_node_texte()

