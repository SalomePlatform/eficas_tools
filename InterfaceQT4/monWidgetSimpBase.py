# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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
from __future__ import absolute_import
try :
    from builtins import str
except : pass

import types,os

# Modules Eficas
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import  Qt
from Extensions.i18n import tr

from .feuille               import Feuille
from desWidgetSimpBase     import Ui_WidgetSimpBase
from .politiquesValidation  import PolitiqueUnique
from .qtSaisie              import SaisieValeur


class MonWidgetSimpBase (Ui_WidgetSimpBase,Feuille):

    def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        if 'R' or 'I' in self.monSimpDef.type  : self.lineEditVal.setMinimumWidth(525)
        self.parentQt.commandesLayout.insertWidget(-1,self,1)
        self.setFocusPolicy(Qt.StrongFocus)
        if monSimpDef.homo == 'constant' : self.lineEditVal.setReadOnly(True)
        if monSimpDef.homo == 'constant' : self.lineEditVal.setStyleSheet("background:rgb(210,235,235);\n" "border:0px;")
        else : self.lineEditVal.returnPressed.connect(self.LEvaleurPressed)
        self.AAfficher=self.lineEditVal
        self.maCommande.listeAffichageWidget.append(self.lineEditVal)
        self.lineEditVal.focusInEvent=self.monFocusInEvent
        self.lineEditVal.focusOutEvent=self.monFocusOutEvent


    def monFocusInEvent(self,event):
        self.editor.nodeEnCours = self
        QLineEdit.focusInEvent(self.lineEditVal,event)

    def monFocusOutEvent(self,event):
        if self.oldValeurTexte != self.lineEditVal.text():
            self.oldValeurTexte= self.lineEditVal.text()
            self.LEvaleurPressed()
        QLineEdit.focusOutEvent(self.lineEditVal,event)


    def setValeurs(self):
        #print ("dans setValeurs")
        self.politique=PolitiqueUnique(self.node,self.editor)
        valeur=self.node.item.getValeur()
        valeurTexte=self.politique.getValeurTexte(valeur)
        chaine=""

        if valeurTexte != None :
            from decimal import Decimal
            if isinstance(valeurTexte,Decimal):
                chaine=str(valeurTexte)
            elif repr(valeurTexte.__class__).find("PARAMETRE") > 0:
                chaine = repr(valeur)
            else :
                #PN ????
                #try :
                #  chaine=QString("").setNum(valeurTexte)
                #except :
                chaine=str(valeurTexte)
        self.oldValeurTexte=chaine
        self.lineEditVal.setText(chaine)


    def finCommentaire(self):
        mc = self.objSimp.definition
        d_aides = { 'TXM' : tr(u"Une chaine de caracteres est attendue.  "),
                    'R'   : tr(u"Un reel est attendu. "),
                    'I'   : tr(u"Un entier est attendu.  "),
                    'Matrice' : tr(u'Une Matrice est attendue.  '),
                    'Fichier' : tr(u'Un fichier est attendu.  '),
                    'FichierNoAbs' : tr(u'Un fichier est attendu.  '),
                    'Repertoire' : tr(u'Un repertoire est attendu.  '),
                    'FichierOuRepertoire' : tr(u'Un repertoire ou un fichier est attendu.  '),
                    'Heure' : tr(u'Heure sous la forme HH:MM'),
                    'Date' :  tr(u'Date sous la forme JJ/MM/AA')}
        if mc.type[0] != type:
            commentaire = d_aides.get(mc.type[0], tr("Type de base inconnu"))
        else : commentaire=""
        return commentaire


    def LEvaleurPressed(self):
        # pour les soucis d encoding
        try :
            if str(self.lineEditVal.text())=="" or str(self.lineEditVal.text())==None : return
        except : pass
        SaisieValeur.LEvaleurPressed(self)
        self.parentQt.donneFocus()
        self.setValeurs()
        self.reaffiche()
