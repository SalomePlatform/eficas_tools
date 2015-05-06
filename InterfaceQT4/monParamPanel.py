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
import string,types,os,re

# Modules Eficas

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

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
        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListWidgetItem*)"),self.LBNouvCommandeClicked)
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
        texte="["
        if valeur == None :
           self.lineEditVal.clear()
           return
        if type(valeur) == types.ListType :
           for l in valeur :
                texte=texte+str(l) +","
           texte=texte[0:-1]+"]"
           self.lineEditVal.setText(texte)
        else :
             self.lineEditVal.setText(str(valeur))

  def BOkParamPressed(self):
        val=self.LEValeurPressed() 
        nom,commentaire=self.LENomPressed()
        if not nom :
           if commentaire == None :
              commentaire=tr("Entrer un nom de parametre")
           self.Commentaire.setText(QString(commentaire))
           self.editor.affiche_infos(commentaire,Qt.red)
           return
        if str(val) == "" : return
        if val == None : return
        self.node.item.set_nom(nom)
        self.node.item.set_valeur(val)
        print dir(self.node.item)
        #print self.node.item.get_val()
        #print self.node.item.get_valeur()
        self.node.update_texte()
        self.node.update_node_valid()
        self.editor.init_modif()
        self.InitLEs()


  def LEValeurPressed(self):
        self.Commentaire.setText(QString(""))
        qtVal=self.lineEditVal.text()
        valString=str(self.lineEditVal.text())
            
        contexte={}
        #exec "from originalMath import *" in contexte
        exec "from Extensions.param2 import originalMath" in contexte
        jdc=self.node.item.get_jdc()
        for p in jdc.params :
           try:
              tp=p.nom+'='+str(repr(p.valeur))
           except :
              pass

        monTexte="monParam="+valString
        exec monTexte in contexte
        try :
          exec monTexte in contexte
        except :
          self.Commentaire.setText(tr("Valeur incorrecte"))
          self.editor.affiche_infos(tr("Valeur incorrecte"),Qt.red)
          return None

        self.Commentaire.setText(tr("Valeur correcte"))
        self.editor.affiche_infos(tr("Valeur correcte"))
        return valString

  def LENomPressed(self):
        self.Commentaire.setText(QString(""))
        qtNom=self.lineEditNom.text()
        nom=str(qtNom)
        numDebutPattern=re.compile('[a-zA-Z"_"]')
        if numDebutPattern.match(nom) :
           return nom,None
        else :
           commentaire=tr("Les noms de parametre doivent commencer par une lettre ou un souligne")
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

