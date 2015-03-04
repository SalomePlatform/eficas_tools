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
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

from feuille               import Feuille
from desWidgetSimpBase     import Ui_WidgetSimpBase 
from politiquesValidation  import PolitiqueUnique
from qtSaisie              import SaisieValeur


class MonWidgetSimpBase (Ui_WidgetSimpBase,Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.setFocusPolicy(Qt.StrongFocus)
        self.connect(self.lineEditVal,SIGNAL("returnPressed()"),self.LEValeurPressed)
        self.maCommande.listeAffichageWidget.append(self.lineEditVal)

  def showEvent(self, event):
      if self.prendLeFocus==1 :
         self.activateWindow()
         self.lineEditVal.setFocus()
         self.prendLeFocus=0
      QWidget.showEvent(self,event)

  def setValeurs(self):
       self.politique=PolitiqueUnique(self.node,self.editor)
       valeur=self.node.item.get_valeur()
       valeurTexte=self.politique.GetValeurTexte(valeur)
       chaine=QString("")

       if valeurTexte != None :
          from decimal import Decimal
          if isinstance(valeurTexte,Decimal):
             chaine=str(valeurTexte)
          elif repr(valeurTexte.__class__).find("PARAMETRE") > 0:
             chaine = QString(repr(valeur))
          else :
             #PN ????
             #try :
             #  chaine=QString("").setNum(valeurTexte)
             #except :
             chaine=QString(str(valeurTexte))
       self.lineEditVal.setText(chaine)


  def finCommentaire(self):
      mc = self.objSimp.definition
      d_aides = { 'TXM' : tr(u"Une chaine de caracteres est attendue.  "),
                  'R'   : tr(u"Un reel est attendu. "),
                  'I'   : tr(u"Un entier est attendu.  "),
                  'Matrice' : tr(u'Une Matrice est attendue.  '),
                  'Fichier' : tr(u'Un fichier est attendu.  '),
                  'FichierNoAbs' : tr(u'Un fichier est attendu.  '),
                  'Repertoire' : tr(u'Un repertoire est attendu.  ')}
      if mc.type[0] != types.ClassType:
         commentaire = d_aides.get(mc.type[0], tr("Type de base inconnu"))
      else : commentaire=""
      return commentaire


  def LEValeurPressed(self):
      if str(self.lineEditVal.text())=="" or str(self.lineEditVal.text())==None : return
      SaisieValeur.LEValeurPressed(self)
      self.parentQt.donneFocus()
      self.setValeurs()
      self.reaffiche()
      
      #if self.objSimp.parent.nom == "MODEL" :
      #   if self.objSimp.isvalid():
      #      self.objSimp.parent.change_fichier="1"
            #self.node.item.parent.build_include(None,"")

