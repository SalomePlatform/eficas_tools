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
# Modules Eficas

from desFormule import DFormule
from qtCommun import QTPanel
from qtCommun import QTPanelTBW2
from qt import *


# Import des panels

class MonFormulePanel(DFormule,QTPanelTBW2):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        DFormule.__init__(self,parent,name,fl)
        QTPanel.__init__(self,node,parent)
        QTPanelTBW2.__init__(self,node,parent)
        self.LENomFormule.setText(node.item.get_nom())
        self.LECorpsFormule.setText(node.item.get_corps())
        texte_args=""
        if node.item.get_args() != None :
            for i in node.item.get_args() :
                if texte_args != "" :
                   texte_args = texte_args +","
                texte_args=texte_args + i
        self.LENomsArgs.setText(texte_args)

        
        self.parent=parent

  def BSupPressed(self):
      QTPanel.BSupPressed(self)

  def BOkPressed(self):
      QTPanel.BOkPressed(self)

  def ViewDoc(self):
      QTPanel.ViewDoc(self)

  def BNextPressed(self):
      QTPanelTBW2.BNextPressed(self)

  def BuildTabCommand(self):
      QTPanelTBW2.BuildLBNouvCommande(self)

  def LEFiltreTextChanged(self):
      QTPanelTBW2.LEFiltreTextChanged(self)

  def LEfiltreReturnPressed(self):
      QTPanelTBW2.LEfiltreReturnPressed(self)

  def LBNouvCommandeClicked(self):
      QTPanelTBW2.LBNouvCommandeClicked(self)

  def NomFormuleSaisi(self):
      nomFormule = self.LENomFormule.text().latin1()
      if nomFormule == '' : return
      test,erreur = self.node.item.verif_nom(nomFormule)
      if test :
         commentaire=nomFormule+" est un nom valide pour une FORMULE"
      else :
         commentaire=nomFormule+" n'est pas un nom valide pour une FORMULE"
      self.editor.affiche_infos(commentaire) 

  def argsSaisis(self):
      arguments = self.LENomsArgs.text().latin1()
      if arguments == '' : return

      test,erreur = self.node.item.verif_arguments(arguments)
      if test:
         commentaire="Argument(s) valide(s) pour une FORMULE"
      else:
         commentaire="Argument(s) invalide(s) pour une FORMULE"
      self.editor.affiche_infos(commentaire) 

  def FormuleSaisie(self):
      nomFormule = self.LENomFormule.text().latin1()
      arguments  = self.LENomsArgs.text().latin1()
      expression = self.LECorpsFormule.text().latin1()
      if expression == '' : return
      test,erreur = self.node.item.verif_formule_python((nomFormule,"REEL",arguments,expression))

      if test:
         commentaire="Corps de FORMULE valide"
      else:
         commentaire="Corps de FORMULE invalide"
      self.editor.affiche_infos(commentaire) 


  def BOkPressedFormule(self):
      if self.parent.modified == 'n' : self.parent.init_modif()

      nomFormule = self.LENomFormule.text().latin1()
      test,erreur = self.node.item.verif_nom(nomFormule)
      if not test :
         self.editor.affiche_infos(erreur)
         return

      arguments  = self.LENomsArgs.text().latin1()
      test,erreur = self.node.item.verif_arguments(arguments)
      if not test :
         self.editor.affiche_infos(erreur)
         return

      expression = self.LECorpsFormule.text().latin1()
      test,erreur = self.node.item.verif_formule_python((nomFormule,"REEL",arguments,expression))
      if not test :
         self.editor.affiche_infos(erreur)
         return

      test=self.node.item.object.update_formule_python(formule=(nomFormule,"REEL",arguments,expression))
      test,erreur = self.node.item.save_formule(nomFormule,"REEL",arguments,expression)
      if test :
         #self.node.update_texte()
         #self.node.update_label()
         #self.node.update_node()
         self.node.onValid()
         self.node.update_valid()
         commentaire = "Formule modifiée"
      else:
         commentaire ="Formule incorrecte : " + erreur 
      self.editor.init_modif()
      self.editor.affiche_infos(commentaire)
