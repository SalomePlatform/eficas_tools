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

from feuille                import Feuille
from desWidgetSimpComplexe  import Ui_WidgetSimpComplexe 
from politiquesValidation   import PolitiqueUnique
from qtSaisie               import SaisieValeur


class MonWidgetSimpComplexe (Ui_WidgetSimpComplexe,Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt):
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt)
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.setFocusPolicy(Qt.StrongFocus)
        self.connect(self.LEImag,SIGNAL("returnPressed()"),self.LEImagRPressed)
        self.connect(self.LEReel,SIGNAL("returnPressed()"),self.LEReelRPressed)
        self.connect(self.RBRI,SIGNAL("clicked()"), self.ValeurPressed )
        self.connect(self.RBMP,SIGNAL("clicked()"), self.ValeurPressed )
        self.connect(self.LEComp,SIGNAL("returnPressed()"),self.LECompRPressed)


  def setValeurs(self):
       self.politique=PolitiqueUnique(self.node,self.editor)
       valeur=self.node.item.get_valeur()
       if valeur == None or valeur == '' : return
       if type(valeur) not in (types.ListType,types.TupleType) :
           self.LEComp.setText(str(valeur))
       else :
           typ_cplx,x1,x2=valeur
           self.LEReel.setText(str(x1))
           self.LEImag.setText(str(x2))
           if typ_cplx == "RI" :
              self.RBRI.setChecked(1)
           else :
              self.RBMP.setChecked(1)

  def LECompRPressed(self) :
        self.LEReel.clear()
        self.LEImag.clear()
        commentaire=tr("expression valide")
        valeur = str(self.LEComp.text())
        d={}
        try :
          v=eval(valeur,d)
        except :
          commentaire=tr("expression invalide")
          self.editor.affiche_infos(commentaire,Qt.red)
          return
        try :
          i=v.imag
          self.editor.affiche_infos(commentaire)
          self.ValeurPressed()
        except :
          commentaire=tr("l expression n est pas de la forme a+bj")
          self.editor.affiche_infos(commentaire,Qt.red)

  def LEReelRPressed(self):
        self.LEComp.clear()
        commentaire=tr("expression valide")
        valeur = str(self.LEReel.text())
        try :
          a=string.atof(valeur)
          self.editor.affiche_infos(commentaire)
        except :
          commentaire=tr("expression invalide")
          self.editor.affiche_infos(commentaire,Qt.red)
        if self.LEImag.text()!="" : self.ValeurPressed()

  def LEImagRPressed(self):
        self.LEComp.clear()
        commentaire=tr("expression valide")
        valeur = str(self.LEImag.text())
        try :
          a=string.atof(valeur)
          self.editor.affiche_infos(commentaire)
        except :
          commentaire=tr("expression invalide")
          self.editor.affiche_infos(commentaire,Qt.red)
        if self.LEReel.text()!="" : self.ValeurPressed()

  def finCommentaire(self):
      commentaire="valeur de type complexe"
      return commentaire

  def getValeurComp(self):
        commentaire=tr("expression valide")
        valeur = str(self.LEComp.text())
        d={}
        try :
          v=eval(valeur,d)
        except :
          commentaire=tr("expression invalide")
          self.editor.affiche_infos(commentaire,Qt.red)
          return None
        try :
          i=v.imag
        except :
          commentaire=tr("expression n est pas de la forme a+bj")
          self.editor.affiche_infos(commentaire,Qt.red)
          return None
        return v


  def ValeurPressed(self):
      if self.LEComp.text()== ""  and (self.LEReel.text()=="" or self.LEImag.text()=="") :
         return
      if self.LEComp.text()== "" : valeur = self.getValeurRI()
      else :
          if self.LEReel.text() != "" or self.LEImag.text() != "" :
              commentaire=tr("entrer une seule valeur SVP")
              self.editor.affiche_infos(commentaire,Qt.red)
              return
          valeur=  self.getValeurComp()
      self.politique.RecordValeur(valeur)
      self.parentQt.donneFocus()

  def getValeurRI(self):
      """
      Retourne le complexe saisi par l'utilisateur
      """
      l=[]
      if  (self.RBMP.isChecked() == 1 ) :
         l.append("MP")
      elif (self.RBRI.isChecked() == 1) :
         l.append("RI")
      else :
         commentaire=tr("saisir le type de complexe")
         self.editor.affiche_infos(commentaire,Qt.red)
         return None
      try :
         l.append(string.atof(str(self.LEReel.text())))
         l.append(string.atof(str(self.LEImag.text())))
      except :
         return None
      return `tuple(l)`

      
