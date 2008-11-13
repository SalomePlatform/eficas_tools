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

from desUniqueSDCO        import DUnSDCO
from qtCommun             import QTPanel
from qtSaisie             import SaisieSDCO

# Import des panels

class MonUniqueSDCOPanel(DUnSDCO,QTPanel,SaisieSDCO):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        QTPanel.__init__(self,node,parent)
        DUnSDCO.__init__(self,parent,name,fl)
        valeur = self.node.item.get_valeur()
        if valeur  != "" and valeur != None :
           self.LESDCO.setText(QString(valeur.nom))

  def BOkPressed(self):
        SaisieSDCO.LESDCOReturnPressed(self)

  def BSupPressed(self):
        QTPanel.BSupPressed(self)

  def BOuiPressed(self):
        self.Commentaire.setText("Aucun Objet de ce type n'est defini")
        self.rbOui.setChecked(1)

  def LESDCOReturnPressed(self):
        """
           Lit le nom donné par l'utilisateur au concept de type CO qui doit être
           la valeur du MCS courant et stocke cette valeur
        """
        SaisieSDCO.LESDCOReturnPressed(self)

  def ViewDoc(self):
      QTPanel.ViewDoc(self)

