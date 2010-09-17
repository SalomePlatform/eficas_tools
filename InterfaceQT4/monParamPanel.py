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
import string,types,os,re

# Modules Eficas

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from desParam import Ui_DParam
from qtCommun import QTPanel
from qtCommun import QTPanelTBW2

class DParam(Ui_DParam,QDialog):
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

class MonParamPanel(DParam,QTPanelTBW2,QTPanel):
  """
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonParamPanel"
        DParam.__init__(self,parent,fl)
        QTPanel.__init__(self,node,parent)
        QTPanelTBW2.__init__(self,node,parent)
        self.InitLEs()
        self.connecterSignaux()
        self.lineEditNom.setFocus()

  def connecterSignaux(self) :
        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListBoxItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkParamPressed)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.BNext,SIGNAL("pressed()"),self.BNextPressed)
        self.connect(self.lineEditVal,SIGNAL("returnPressed()"),self.BOkParamPressed)

  def InitLEs(self):
        nom=self.node.item.get_nom()
        self.lineEditNom.setText(nom)
        valeur=self.node.item.get_valeur()
        if valeur != None:
           #str=QString("").setNum(valeur)
           self.lineEditVal.setText(str(valeur))
        else :
           self.lineEditVal.clear()

  def BOkParamPressed(self):
        val=self.LEValeurPressed() 
        nom,commentaire=self.LENomPressed()
        if not nom :
           if commentaire == None :
              commentaire="Entrer un nom de parametre"
           self.Commentaire.setText(QString(commentaire))
           self.editor.affiche_infos(commentaire,Qt.red)
           return
        if str(val) == "" :
           return
        self.node.item.set_nom(nom)
        self.node.item.set_valeur(val)
        self.node.update_texte()
        self.node.update_node_valid()
        self.editor.init_modif()
        self.InitLEs()


  def LEValeurPressed(self):
        self.Commentaire.setText(QString(""))
        commentaire="Valeur incorrecte"
        qtVal=self.lineEditVal.text()
        valString=str(self.lineEditVal.text())
        if (valString.find(' ') > -1) or (valString.find(',') > -1) :
           commentaire="Valeur incorrecte"
           self.Commentaire.setText(QString(commentaire))
           self.editor.affiche_infos(commentaire,Qt.red)
           return None
        boul=2
        try :
            val,boul=QString.toInt(qtVal)
            if boul : valString=val
        except :
            pass
        if boul == 0 :
            try :
                val,boul=QString.toDouble(qtVal)
                if boul : valString=val
            except :
                pass
        if boul == 0 :
            try :
                val=str(qtVal)
                boul=1
            except :
                pass
        if boul: commentaire="Valeur correcte"
        self.Commentaire.setText(QString(commentaire))
        self.editor.affiche_infos(commentaire)
        return valString

  def LENomPressed(self):
        self.Commentaire.setText(QString(""))
        qtNom=self.lineEditNom.text()
        nom=str(qtNom)
        numDebutPattern=re.compile('[a-zA-Z"_"]')
        if numDebutPattern.match(nom) :
           return nom,None
        else :
           commentaire="Les noms de parametre doivent commencer par une lettre ou un souligne"
           return None,commentaire

  def BuildTabCommandChanged(self):
      QTPanelTBW2.BuildLBNouvCommandChanged(self)

  def LEFiltreTextChanged(self):
      QTPanelTBW2.LEFiltreTextChanged(self)

  def LEfiltreReturnPressed(self):
      QTPanelTBW2.LEfiltreReturnPressed(self)

  def LBNouvCommandeClicked(self):
      QTPanelTBW2.LBNouvCommandeClicked(self)

  def AppelleBuildLBRegles(self):
      listeRegles=self.node.item.get_regles()
      listeNomsEtapes = self.node.item.get_l_noms_etapes()
      self.BuildLBRegles(listeRegles,listeNomsEtapes)

  def BNextPressed(self) :
      QTPanelTBW2.BNextPressed(self)

  def BOkPressed(self):
      QTPanel.BOkPressed(self)

