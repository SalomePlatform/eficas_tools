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
from PyQt4.QtCore import *
from PyQt4.QtGui import *

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
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
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
        commentaire="expression valide"
        valeur = str(self.LEcomp.text())
        d={}
        try :
          v=eval(valeur,d)
        except :
          commentaire="expression invalide"
          self.editor.affiche_infos(commentaire,Qt.red)
          return
        try :
          i=v.imag
          self.editor.affiche_infos(commentaire)
        except :
          commentaire="expression n est pas de la forme a+bj"
          self.editor.affiche_infos(commentaire,Qt.red)
          
  def LEReelRPressed(self):
        self.LEcomp.clear()
        commentaire="expression valide"
        valeur = str(self.LEReel.text())
        try :
          a=string.atof(valeur)
          self.editor.affiche_infos(commentaire)
        except :
          commentaire="expression invalide"
          self.editor.affiche_infos(commentaire,Qt.red)

  def LEImagRPressed(self):
        self.LEcomp.clear()
        commentaire="expression valide"
        valeur = str(self.LEImag.text())
        try :
          a=string.atof(valeur)
          self.editor.affiche_infos(commentaire)
        except :
          commentaire="expression invalide"
          self.editor.affiche_infos(commentaire,Qt.red)

  def BOkPressed(self):
        if self.LEcomp.text()== "" : 
           valeur = self.getValeurAster()
        else :
           if self.LEReel.text() != "" or self.LEImag.text() != "" :
              commentaire="entrer une seule valeur SVP"
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
         commentaire="saisir le type de complexe"
         self.editor.affiche_infos(commentaire,Qt.red)
         return None
      try :
         l.append(string.atof(str(self.LEReel.text())))
         l.append(string.atof(str(self.LEImag.text())))
      except :
         return None
      return `tuple(l)`

  def getValeurComp(self):
        commentaire="expression valide"
        valeur = str(self.LEcomp.text())
        d={}
        try :
          v=eval(valeur,d)
        except :
          commentaire="expression invalide"
          self.editor.affiche_infos(commentaire,Qt.red)
          return None
        try :
          i=v.imag
        except :
          commentaire="expression n est pas de la forme a+bj"
          self.editor.affiche_infos(commentaire,Qt.red)
          return None
        return v

  def InitCommentaire(self):
        commentaire='Un complexe est attendu'
        aideval=self.node.item.aide()
        commentaire=commentaire +"   "+ QString.toUtf8(QString(aideval))
        self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))


