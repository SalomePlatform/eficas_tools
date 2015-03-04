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
import string,types,os

# Modules Eficas
from PyQt4 import *
from PyQt4.QtGui import *

from Extensions.i18n import tr
from desUniqueSDCOInto    import Ui_DUnSDCOInto
from qtCommun             import QTPanel
from qtSaisie             import SaisieSDCO
from politiquesValidation import PolitiqueUnique

# Import des panels

class MonUniqueSDCOIntoPanel(Ui_DUnSDCOInto,QTPanel,SaisieSDCO, QDialog):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonUniqueSDCOIntoPanel"
        QTPanel.__init__(self,node,parent)
        #DUnSDCOInto.__init__(self,parent,name,fl)
        QDialog.__init__(self,parent)
        if hasattr(parent,"leLayout"):
           parent.leLayout.removeWidget(parent.leLayout.widgetActive)
           parent.leLayout.widgetActive.close()
           parent.leLayout.addWidget(self)
           parent.leLayout.widgetActive=self
        else:
           parent.partieDroite=QWidget()
           parent.leLayout=QGridLayout(parent.partieDroite)
           parent.leLayout.addWidget(self)
           parent.addWidget(parent.partieDroite)
           parent.leLayout.widgetActive=self
	self.setupUi(self)
        self.initLBSDCO()

  def initLBSDCO(self):
        listeNomsSDCO = self.node.item.get_sd_avant_du_bon_type()
        for aSDCO in listeNomsSDCO:
            self.LBSDCO.insertItem( aSDCO)
        valeur = self.node.item.get_valeur()
        if valeur  != "" and valeur != None :
           self.LESDCO.setText(QString(valeur.nom))


  def LBSDCOReturnPressed(self):
        """
         Teste si la valeur fournie par l'utilisateur est une valeur permise :
          - si oui, l'enregistre
          - si non, restaure l'ancienne valeur
        """
        nomConcept=str(self.LBSDCO.currentText())
        self.LESDCO.clear()
        self.editor.init_modif()
        anc_val = self.node.item.get_valeur()
        test_CO=self.node.item.is_CO(anc_val)

        valeur,validite=self.node.item.eval_valeur(nomConcept)
        test = self.node.item.set_valeur(valeur)
        if not test :
          commentaire = tr("impossible d'evaluer : ") +  valeur
        elif validite:
          commentaire = tr("Valeur du mot-clef enregistree")
          if test_CO:
             # il faut egalement propager la destruction de l'ancien concept
             self.node.item.delete_valeur_co(valeur=anc_val)
             self.node.item.object.etape.get_type_produit(force=1)
             self.node.item.object.etape.parent.reset_context()
        else :
          commentaire = self.node.item.get_cr()
          self.reset_old_valeur(anc_val,mess=mess)
          self.editor.affiche_infos(commentaire,Qt.red)
        self.Commentaire.setText(tr(commentaire))

  def LESDCOReturnPressed(self) :
        self.LBSDCO.clearSelection()
        SaisieSDCO.LESDCOReturnPressed(self)

  def BOkPressed(self):
        self.LESDCOReturnPressed()
