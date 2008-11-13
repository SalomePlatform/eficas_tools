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
import prefs 

from qt import *

from desParam import DParam
from qtCommun import QTPanel
from qtCommun import QTPanelTBW2

# Import des panels

class MonParamPanel(DParam,QTPanelTBW2,QTPanel):
  """
  Classe d�finissant le panel associ� aux mots-cl�s qui demandent
  � l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discr�tes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        DParam.__init__(self,parent,name,fl)
        QTPanel.__init__(self,node,parent)
        QTPanelTBW2.__init__(self,node,parent)
        self.InitLEs()

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
        nom=self.LENomPressed()
        if not nom :
           commentaire="Entrer un nom de parametre"
           self.Commentaire.setText(QString(commentaire))
           self.editor.affiche_infos(commentaire)
           return
        self.node.item.set_nom(nom)
        self.node.item.set_valeur(val)
        self.node.update_texte()
        self.node.update_valid()
        self.editor.init_modif()
        self.InitLEs()

  def BSupPressed(self):
        QTPanel.BSupPressed(self)

  def LEValeurPressed(self):
        self.Commentaire.setText(QString(""))
        commentaire="Valeur incorrecte"
        qtVal=self.lineEditVal.text()
        boul=2
        try :
            val,boul=QString.toInt(qtVal)
        except :
            pass
        if boul == 0 :
            try :
                val,boul=QString.toDouble(qtVal)
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
        valString=str(self.lineEditVal.text())
        return valString

  def LENomPressed(self):
        self.Commentaire.setText(QString(""))
        qtNom=self.lineEditNom.text()
        nom=str(qtNom)
        numDebutPattern=re.compile('[a-zA-Z]')
        if numDebutPattern.match(nom) :
           return nom
        else :
           commentaire="Les noms de parametre doivent commencer par une lettre"
           self.Commentaire.setText(QString(commentaire))
           self.editor.affiche_infos(commentaire)
           return None

  def BuildTabCommand(self):
      QTPanelTBW2.BuildLBNouvCommande(self)

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

  def ViewDoc(self):
      QTPanel.ViewDoc(self)

