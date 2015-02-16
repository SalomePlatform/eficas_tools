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
from desWidgetParam import Ui_desWidgetParam


class MonWidgetParam(Ui_desWidgetParam,QDialog):
  """
  """
  def __init__(self,editor, name = None,fl = 0):
       self.editor=editor
       QDialog.__init__(self,editor)
       self.setupUi(self)
       self.connecterSignaux()
       self.dejaExistant=0
       self.listeTousParam=self.editor.jdc.params
       self.dictListe={}
       self.initToutesVal()

  def connecterSignaux(self) :
        self.connect(self.lineEditVal,SIGNAL("returnPressed()"),self.lineEditValReturnPressed)
        self.connect(self.lineEditNom,SIGNAL("returnPressed()"),self.lineEditNomReturnPressed)


  def CreeParametre(self):
        nom=str(self.lineEditNom.text())
        val=str(self.lineEditVal.text())
        if val == "" or None : return
        if nom == "" or None : return
        print self.editor.tree
        if len(self.editor.tree.selectedItems()) == 0 : itemAvant=self.editor.tree.racine 
        else :                                          itemAvant=self.editor.tree.selectedItems()[0]
        param=itemAvant.addParameters(True)
        param.item.set_nom(nom)
        param.item.set_valeur(val)
        param.update_node_texte()


  def lineEditValReturnPressed(self):
        qtVal=self.lineEditVal.text()
        valString=str(self.lineEditVal.text())
        contexte={}
        exec "from math import *" in contexte
        jdc=self.editor.jdc
        if jdc == None : 
          self.editor.affiche_infos(tr("La Creation de parametre n est possible que dans un jeu de données"),Qt.red)
          return

        for p in jdc.params :
           try:
              tp=p.nom+'='+str(p.val)
              exec tp  in contexte
           except :
              pass
        monTexte="monParam="+valString
        try :
          exec monTexte in contexte
        except :
          self.editor.affiche_infos(tr("Valeur incorrecte"),Qt.red)
        if self.lineEditNom.text()!="" and self.dejaExistant==False : self.CreeParametre()


  def lineEditNomReturnPressed(self):
        qtNom=self.lineEditNom.text()
        nom=str(qtNom)
        numDebutPattern=re.compile('[a-zA-Z"_"]')
        if not (numDebutPattern.match(nom)) :
           commentaire=tr("Les noms de parametre doivent commencer par une lettre ou un souligne")
           self.lineEditNom.setText("")
           self.editor.affiche_infos(commentaire,Qt.red)
        if self.lineEditVal.text()!="" : self.CreeParametre()
        self.lineEditVal.setFocus(Qt.OtherFocusReason)


  def initToutesVal(self):
        self.LBParam.clear()
        for param in self.listeTousParam :
            self.LBParam.addItem(QString(repr(param)))
            self.dictListe[QString(repr(param))] = param

  def valideParam(self):
        if self.LBParam.selectedItems()== None : return
        lParam=[]
        for indice in range(len(self.LBParam.selectedItems())):
            i=self.LBParam.selectedItems()[indice].text()
            param=self.dictListe[i]
            lParam.append(param)

        try :
          self.panel.AjoutNValeur(lParam)
        except :
          for p in lParam :
             self.panel.Ajout1Valeur(p)
        self.close()

