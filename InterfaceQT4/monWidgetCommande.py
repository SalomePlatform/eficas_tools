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

    
# Import des panels

class MonWidgetCommande(Ui_WidgetCommande,Groupe):
  """
  """
  def __init__(self,node,editor,etape):
      print "MonWidgetCommande ", self
      Groupe.__init__(self,node,editor,None,etape.definition,etape,1)
      if (etape.get_type_produit()==None): self.LENom.close()
      elif (hasattr (etape, 'sdnom')) : self.LENom.setText(etape.sdnom) 
      maPolice= QFont("Times", 10,)
      self.setFont(maPolice)
      self.repIcon=self.appliEficas.repIcon
      self.labelNomCommande.setText(self.obj.nom)
      self.commandesLayout.addStretch()
      self.commandesLayout.focusInEvent=self.focusInEvent
      self.scrollAreaCommandes.focusInEvent=self.focusInEvent
      #self.RBValide.focusInEvent=FacultatifOuOptionnel.focusInEvent
      self.connect(self.bCatalogue,SIGNAL("clicked()"), self.afficheCatalogue)
      self.racine=self.node.tree.racine
       

      self.setAcceptDrops(True)
      from monWidgetOptionnel import MonWidgetOptionnel
      if hasattr(self.editor,'widgetOptionnel') : 
        self.monOptionnel=self.editor.widgetOptionnel
      else :
        self.monOptionnel=MonWidgetOptionnel(self)
        self.editor.widgetOptionnel=self.monOptionnel
        self.editor.splitter.addWidget(self.monOptionnel)
      self.afficheOptionnel()


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

