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

from desWidgetCommande import Ui_WidgetCommande
from groupe import Groupe
from gereIcones import FacultatifOuOptionnel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
import Accas 
import os
import string

    
# Import des panels

class MonWidgetCommande(Ui_WidgetCommande,Groupe):
  """
  """
  def __init__(self,node,editor,etape):
      print "MonWidgetCommande ", self
      Groupe.__init__(self,node,editor,None,etape.definition,etape,1)
      if (etape.get_type_produit()==None): self.LENom.close()
      elif (hasattr (etape, 'sdnom')) and etape.sdnom != "sansnom" : self.LENom.setText(etape.sdnom) 
      else : self.LENom.setText("")
      maPolice= QFont("Times", 10,)
      self.setFont(maPolice)
      self.repIcon=self.appliEficas.repIcon
      self.labelNomCommande.setText(self.obj.nom)
      self.commandesLayout.addStretch()
      self.commandesLayout.focusInEvent=self.focusInEvent
      self.scrollAreaCommandes.focusInEvent=self.focusInEvent
      #self.RBValide.focusInEvent=FacultatifOuOptionnel.focusInEvent
      self.connect(self.bCatalogue,SIGNAL("clicked()"), self.afficheCatalogue)
      self.connect(self.LENom,SIGNAL("returnPressed()"),self.nomChange)
      self.racine=self.node.tree.racine
      if self.node.item.GetIconName() == "ast-red-square" : self.LENom.setDisabled(True)

      self.setAcceptDrops(True)
      from monWidgetOptionnel import MonWidgetOptionnel
      if hasattr(self.editor,'widgetOptionnel') : 
        self.monOptionnel=self.editor.widgetOptionnel
      else :
        self.monOptionnel=MonWidgetOptionnel(self)
        self.editor.widgetOptionnel=self.monOptionnel
        self.editor.splitter.addWidget(self.monOptionnel)
      self.afficheOptionnel()


  def nomChange(self):
      nom = str(self.LENom.text())
      nom = string.strip(nom)
      if nom == '' : return                  # si pas de nom, on ressort sans rien faire
      test,mess = self.node.item.nomme_sd(nom)
      self.editor.affiche_infos(mess)

      #Notation scientifique
      if test :
        from politiquesValidation import Validation
        validation=Validation(self.node,self.editor)
        validation.AjoutDsDictReelEtape()

  def afficheOptionnel(self):
      # N a pas de parentQt. doit donc etre redefini
      liste=self.ajouteMCOptionnelDesBlocs()
      self.monOptionnel.parentMC=self
      self.monOptionnel.affiche(liste)

  def focusInEvent(self,event):
      #print "je mets a jour dans focusInEvent de monWidget Commande "
      self.afficheOptionnel()


  def reaffiche(self,nodeAVoir=None):
      self.node.affichePanneau()
      if nodeAVoir != None:
        f=nodeAVoir.fenetre
        qApp.processEvents()
        self.editor.fenetreCentraleAffichee.scrollAreaCommandes.ensureWidgetVisible(f)

  def afficheCatalogue(self):
      self.monOptionnel.hide()
      self.racine.affichePanneau()
      if self.node : self.node.select()
      else : self.racine.select()

  def setValide(self):
      if not(hasattr (self,'RBValide')) : return
      icon = QIcon()
      print self.repIcon
      if self.node.item.object.isvalid() :
         icon=QIcon(self.repIcon+"/ast-green-ball.png")
      else :
         icon=QIcon(self.repIcon+"/ast-red-ball.png")
      if self.node.item.GetIconName() == "ast-yellow-square" :
         icon=QIcon(self.repIcon+"/ast-yel-ball.png")
      self.RBValide.setIcon(icon)
