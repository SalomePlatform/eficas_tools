# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Extensions.i18n import tr


from desUniqueComp import Ui_DUnComp
from qtCommun      import QTPanel
from politiquesValidation import PolitiqueUnique

class DUnComp(Ui_DUnComp,QDialog):
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

class MonUniqueCompPanel(DUnComp,QTPanel,PolitiqueUnique):
  """
  Classe d�finissant le panel associ� aux mots-cl�s qui demandent
  � l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discr�tes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonUniqueCompPanel"
        QTPanel.__init__(self,node,parent)
        DUnComp.__init__(self,parent,fl)
        self.politique=PolitiqueUnique(node,parent)
        self.InitLinesVal()
        self.InitCommentaire()
        self.connecterSignaux()

  def connecterSignaux(self):
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.LEImag,SIGNAL("returnPressed()"),self.LEImagRPressed)
        self.connect(self.LEReel,SIGNAL("returnPressed()"),self.LEReelRPressed)
        self.connect(self.LEcomp,SIGNAL("returnPressed()"),self.LEcompRPressed)


  def InitLinesVal(self):
        valeur=self.node.item.get_valeur()
        if valeur == None or valeur == '' : return
        if type(valeur) not in (types.ListType,types.TupleType) :
           self.LEcomp.setText(str(valeur))
        else :
           typ_cplx,x1,x2=valeur
           self.LEReel.setText(str(x1))
           self.LEImag.setText(str(x2))
           if typ_cplx == "RI" :
              self.RBRI.setChecked(1)
           else :
              self.RBMP.setChecked(1)
      

  def LEcompRPressed(self) :
        self.LEReel.clear()
        self.LEImag.clear()
        commentaire=tr("expression valide")
        valeur = str(self.LEcomp.text())
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
        except :
          commentaire=tr("expression n est pas de la forme a+bj")
          self.editor.affiche_infos(commentaire,Qt.red)
          
  def LEReelRPressed(self):
        self.LEcomp.clear()
        commentaire=tr("expression valide")
        valeur = str(self.LEReel.text())
        try :
          a=string.atof(valeur)
          self.editor.affiche_infos(commentaire)
        except :
          commentaire=tr("expression invalide")
          self.editor.affiche_infos(commentaire,Qt.red)

  def LEImagRPressed(self):
        self.LEcomp.clear()
        commentaire=tr("expression valide")
        valeur = str(self.LEImag.text())
        try :
          a=string.atof(valeur)
          self.editor.affiche_infos(commentaire)
        except :
          commentaire=tr("expression invalide")
          self.editor.affiche_infos(commentaire,Qt.red)

  def BOkPressed(self):
        if self.LEcomp.text()== "" : 
           valeur = self.getValeurAster()
        else :
           if self.LEReel.text() != "" or self.LEImag.text() != "" :
              commentaire=tr("entrer une seule valeur SVP")
              self.editor.affiche_infos(commentaire,Qt.red)
              return
           valeur=  self.getValeurComp()
        self.politique.RecordValeur(valeur)

  def getValeurAster(self):
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

  def getValeurComp(self):
        commentaire=tr("expression valide")
        valeur = str(self.LEcomp.text())
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

  def InitCommentaire(self):
        commentaire=tr('Un complexe est attendu')
        aideval=self.node.item.aide()
        commentaire=commentaire +"   "+ QString.toUtf8(QString(aideval))
        self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))


