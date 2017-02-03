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
# Modules Eficas

from desRechercheCatalogue import Ui_desRechercheCatalogue
from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets import QDialog, QCompleter
    from PyQt5.QtCore import Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *

from Extensions.i18n import tr

# Import des panels

class DRechercheCatalogue (Ui_desRechercheCatalogue ,QDialog):
  """
  Classe d�finissant le panel associ� aux mots-cl�s qui demandent
  � l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discr�tes
  """
  def __init__(self,parent,editor ):
      QDialog.__init__(self,parent)
      #self.setModal(True)
      self.setupUi(self)
      self.editor=editor
      self.CBRecherche.setEditable(True)
      if monEnvQT5 :
         self.CBRecherche.lineEdit().returnPressed.connect(self.rechercheCB)
         self.CBRecherche.currentIndexChanged.connect(self.rechercheCB)
      else :
         self.connect(self.CBRecherche.lineEdit(),SIGNAL("returnPressed()"),self.rechercheCB)
         self.connect(self.CBRecherche,SIGNAL("currentIndexChanged(int)"),self.rechercheCB)

      self.initRecherche()

  def initRecherche(self):
      listeChoix=self.editor.readercata.dicoInverse.keys()
      self.CBRecherche.addItem("")
      for choix in listeChoix:
          self.CBRecherche.addItem(choix)
      monCompleteur=QCompleter(listeChoix,self)
      monCompleteur.setCompletionMode(QCompleter.PopupCompletion)
      self.CBRecherche.setCompleter(monCompleteur)


  def rechercheCB(self):
      motAChercher=self.CBRecherche.lineEdit().text()
      self.recherche(motAChercher)


  def recherche(self,motAChercher):
      if str(motAChercher)=="" or str(motAChercher) == None : return
      if str(motAChercher) not in self.editor.readercata.dicoInverse.keys():return
      try :
      #if 1  :
        genea= self.editor.readercata.dicoInverse[str(motAChercher)]
        listeGenea=[]
        for t in genea : listeGenea.append(t[0])
        listeGenea.reverse()
        texte=''
        i=0
        for mc in listeGenea :
         ligne = i*'   '+str(mc) + ' / '+tr(str(mc))+'\n' 
         i=i+1
         texte += ligne
        self.teGenea.setText(texte)
        self.teDoc.setText(getattr(genea[0][1],self.editor.appliEficas.langue))
        
        
      except :
        pass
