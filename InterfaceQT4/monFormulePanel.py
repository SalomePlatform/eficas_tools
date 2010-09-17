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

from desFormule import Ui_DFormule
from qtCommun import QTPanel
from qtCommun import QTPanelTBW2

from PyQt4.QtGui  import *
from PyQt4.QtCore import *


class DFormule(Ui_DFormule,QDialog):
   def __init__(self,parent ,modal ) :
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



# Import des panels

class MonFormulePanel(DFormule,QTPanelTBW2):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonFormulePanel"
        DFormule.__init__(self,parent,fl)
        QTPanel.__init__(self,node,parent)
        QTPanelTBW2.__init__(self,node,parent)
        self.connecterSignaux()
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

  def connecterSignaux(self):
        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListBoxItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.BNext,SIGNAL("clicked()"),self.BNextPressed)
        self.connect(self.LENomFormule,SIGNAL("returnPressed()"),self.NomFormuleSaisi)
        self.connect(self.LENomsArgs,SIGNAL("returnPressed()"),self.argsSaisis)
        self.connect(self.LECorpsFormule,SIGNAL("returnPressed()"),self.FormuleSaisie)


  def BOkPressed(self):
      QTPanel.BOkPressed(self)

  def BNextPressed(self):
      QTPanelTBW2.BNextPressed(self)

  def BuildTabCommandChanged(self):
      QTPanelTBW2.BuildLBNouvCommandChanged(self)


  def LEFiltreTextChanged(self):
      QTPanelTBW2.LEFiltreTextChanged(self)

  def LEfiltreReturnPressed(self):
      QTPanelTBW2.LEfiltreReturnPressed(self)

  def LBNouvCommandeClicked(self):
      QTPanelTBW2.LBNouvCommandeClicked(self)

  def NomFormuleSaisi(self):
      nomFormule = str(self.LENomFormule.text())
      if nomFormule == '' : return
      test,erreur = self.node.item.verif_nom(nomFormule)
      if test :
         commentaire=nomFormule+" est un nom valide pour une FORMULE"
         self.editor.affiche_infos(commentaire) 
      else :
         commentaire=nomFormule+" n'est pas un nom valide pour une FORMULE"
         self.editor.affiche_infos(commentaire,Qt.red) 

  def argsSaisis(self):
      arguments = str(self.LENomsArgs.text())
      if arguments == '' : return
      test,erreur = self.node.item.verif_arguments(arguments)
      if test:
         commentaire="Argument(s) valide(s) pour une FORMULE"
         self.editor.affiche_infos(commentaire) 
      else:
         commentaire="Argument(s) invalide(s) pour une FORMULE"
         self.editor.affiche_infos(commentaire,Qt.red) 

  def FormuleSaisie(self):
      nomFormule = str(self.LENomFormule.text())
      arguments  = str(self.LENomsArgs.text())
      expression = str(self.LECorpsFormule.text())
      if expression == '' : return
      test,erreur = self.node.item.verif_formule_python((nomFormule,"REEL",arguments,expression))

      if test:
         commentaire="Corps de FORMULE valide"
         self.editor.affiche_infos(commentaire) 
      else:
         commentaire="Corps de FORMULE invalide"
         self.editor.affiche_infos(commentaire,Qt.red) 


  def BOkPressedFormule(self):
      if self.parent.modified == 'n' : self.parent.init_modif()

      nomFormule = str(self.LENomFormule.text())
      test,erreur = self.node.item.verif_nom(nomFormule)
      if not test :
         self.editor.affiche_infos(erreur,Qt.red)
         return

      arguments  = str(self.LENomsArgs.text())
      test,erreur = self.node.item.verif_arguments(arguments)
      if not test :
         self.editor.affiche_infos(erreur,Qt.red)
         return

      expression = str(self.LECorpsFormule.text())
      test,erreur = self.node.item.verif_formule_python((nomFormule,"REEL",arguments,expression))
      if not test :
         self.editor.affiche_infos(erreur,Qt.red)
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
         self.editor.affiche_infos(commentaire)
      else:
         commentaire ="Formule incorrecte : " + erreur 
         self.editor.affiche_infos(commentaire,Qt.red)
      self.editor.init_modif()
