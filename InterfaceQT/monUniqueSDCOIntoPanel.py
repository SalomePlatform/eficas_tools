# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
# Modules Python
import string,types,os

# Modules Eficas
import prefs 

from qt import *

from desUniqueSDCOInto    import DUnSDCOInto
from qtCommun             import QTPanel
from qtSaisie             import SaisieSDCO
from politiquesValidation import PolitiqueUnique

# Import des panels

class MonUniqueSDCOIntoPanel(DUnSDCOInto,QTPanel,SaisieSDCO):
  """
  Classe d�finissant le panel associ� aux mots-cl�s qui demandent
  � l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discr�tes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        QTPanel.__init__(self,node,parent)
        DUnSDCOInto.__init__(self,parent,name,fl)
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
          commentaire = "impossible d'�valuer : %s " %`valeur`
        elif validite:
          commentaire = "Valeur du mot-cl� enregistr�e"
          if test_CO:
             # il faut egalement propager la destruction de l'ancien concept
             self.node.item.delete_valeur_co(valeur=anc_val)
             self.node.item.object.etape.get_type_produit(force=1)
             self.node.item.object.etape.parent.reset_context()
        else :
          commentaire = self.node.item.get_cr()
          self.reset_old_valeur(anc_val,mess=mess)
          self.editor.affiche_infos(commentaire)
        self.Commentaire.setText(commentaire)

  def LESDCOReturnPressed(self) :
        self.LBSDCO.clearSelection()
        SaisieSDCO.LESDCOReturnPressed(self)

  def BOkPressed(self):
        self.LESDCOReturnPressed()

  def BSupPressed(self):
        QTPanel.BSupPressed(self)

  def ViewDoc(self):
      QTPanel.ViewDoc(self)
