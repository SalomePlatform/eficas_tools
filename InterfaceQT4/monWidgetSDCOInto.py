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
from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets import QLineEdit
    from PyQt5.QtCore import Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *
from Extensions.i18n import tr

from feuille               import Feuille
from desWidgetSDCOInto     import Ui_WidgetSDCOInto 
from qtSaisie              import SaisieSDCO
from politiquesValidation  import PolitiqueUnique



class MonWidgetSDCOInto (Ui_WidgetSDCOInto,Feuille,SaisieSDCO):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        #print "MonWidgetSDCOInto init"
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.politique=PolitiqueUnique(self.node,self.editor)
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.maCommande.listeAffichageWidget.append(self.LESDCO)
        self.AAficher=self.LESDCO
        self.initLBSDCO()
       
        if monEnvQT5 :
          self.LESDCO.returnPressed.connect(self.LESDCOReturnPressed)
          self.LBSDCO.itemDoubleClicked.connect(self.LBSDCODoubleClicked )
        else :
          self.connect(self.LESDCO, SIGNAL("returnPressed()"),self.LESDCOReturnPressed)
          self.connect(self.LBSDCO, SIGNAL("itemDoubleClicked(QListWidgetItem*)" ), self.LBSDCODoubleClicked )

  def LESDCOReturnPressed(self) :
        self.LBSDCO.clearSelection()
        SaisieSDCO.LESDCOReturnPressed(self)


  def initLBSDCO(self):
        listeNomsSDCO = self.node.item.get_sd_avant_du_bon_type()
        for aSDCO in listeNomsSDCO:
            self.LBSDCO.insertItem( 1,aSDCO)
        valeur = self.node.item.get_valeur()
        if valeur  != "" and valeur != None :
           self.LESDCO.setText(str(valeur.nom))


  def LBSDCODoubleClicked(self):
        """
         Teste si la valeur fournie par l'utilisateur est une valeur permise :
          - si oui, l'enregistre
          - si non, restaure l'ancienne valeur
        """
        nomConcept=str(self.LBSDCO.currentItem().text())
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
             self.LESDCO.setText(nomConcept)
        else :
          commentaire = self.node.item.get_cr()
          self.reset_old_valeur(anc_val,mess=mess)
          self.editor.affiche_infos(commentaire,Qt.red)
        self.Commentaire.setText(tr(commentaire))

