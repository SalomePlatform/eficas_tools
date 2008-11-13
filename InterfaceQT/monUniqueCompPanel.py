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

from desUniqueComp import DUnComp
from qtCommun      import QTPanel
from politiquesValidation import PolitiqueUnique

# Import des panels

#class MonUniqueCompPanel(DUnComp,QTPanel,SaisieValeur):
class MonUniqueCompPanel(DUnComp,QTPanel,PolitiqueUnique):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        QTPanel.__init__(self,node,parent)
        DUnComp.__init__(self,parent,name,fl)
        self.politique=PolitiqueUnique(node,parent)
        self.InitLinesVal()
        self.InitCommentaire()

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
              self.buttonGroup1.setButton(1)
           else :
              self.buttonGroup1.setButton(0)
      

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
          self.editor.affiche_infos(commentaire)
          return
        try :
          i=v.imag
        except :
          commentaire="expression n est pas de la forme a+bj"
        self.editor.affiche_infos(commentaire)
          
  def LEReelRPressed(self):
        self.LEcomp.clear()
        commentaire="expression valide"
        valeur = str(self.LEReel.text())
        try :
          a=string.atof(valeur)
        except :
          commentaire="expression invalide"
        self.editor.affiche_infos(commentaire)

  def LEImagRPressed(self):
        self.LEcomp.clear()
        commentaire="expression valide"
        valeur = str(self.LEImag.text())
        try :
          a=string.atof(valeur)
        except :
          commentaire="expression invalide"
        self.editor.affiche_infos(commentaire)

  def BOkPressed(self):
        if self.LEcomp.text()== "" : 
           valeur = self.getValeurAster()
        else :
           if self.LEReel.text() != "" or self.LEImag.text() != "" :
              commentaire="entrer une seule valeur SVP"
              self.editor.affiche_infos(commentaire)
              return
           valeur=  self.getValeurComp()
        self.politique.RecordValeur(valeur)

  def getValeurAster(self):
      """
      Retourne le complexe saisi par l'utilisateur
      """
      l=[]
      if  (self.buttonGroup1.selectedId() == 1 ) :
         l.append("MP")
      elif (self.buttonGroup1.selectedId() == 0) :
         l.append("RI")
      else :
         commentaire="saisir le type de complexe"
         self.editor.affiche_infos(commentaire)
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
          self.editor.affiche_infos(commentaire)
          return None
        try :
          i=v.imag
        except :
          commentaire="expression n est pas de la forme a+bj"
          self.editor.affiche_infos(commentaire)
          return None
        return v

  def InitCommentaire(self):
        commentaire='Un complexe est attendu'
        aideval=self.node.item.aide()
        commentaire=commentaire +"\n"+ aideval
        self.Commentaire.setText(QString(commentaire))


  def BSupPressed(self):
        QTPanel.BSupPressed(self)

  def ViewDoc(self):
      QTPanel.ViewDoc(self)

