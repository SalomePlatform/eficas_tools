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
import string,types,os

# Modules Eficas
import prefs 

from qt import *

from desUniqueBase import DUnBase
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiqueUnique

# Import des panels

class MonUniqueBasePanel(DUnBase,QTPanel,SaisieValeur):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        self.editor=parent
        QTPanel.__init__(self,node,parent)
        DUnBase.__init__(self,parent,name,fl)
        self.politique=PolitiqueUnique(node,parent)
        self.InitLineEditVal()
        self.InitCommentaire()
        self.detruitBouton()

  def ViewDoc(self):
      QTPanel.ViewDoc(self)

  def detruitBouton(self):
        mc = self.node.item.get_definition()
        type = mc.type[0]
        #if not('grma' in repr(type)):
        #if not('grma' in repr(type)) or not(self.editor.salome) :
        if not(('grma' in repr(type)) or ('grno' in repr(type))) or not(self.editor.salome) :
           self.BSalome.close()
           self.BView2D.close()

  def InitLineEditVal(self):
        valeur=self.node.item.get_valeur()
        valeurTexte=self.politique.GetValeurTexte(valeur)
        if valeurTexte != None:
           try :
               maString=QString("").setNum(valeurTexte)
           except :
               maString=str(valeurTexte)
           self.lineEditVal.setText(maString)


  def InitCommentaire(self):
      mc = self.node.item.get_definition()
      d_aides = { 'TXM' : "Une chaîne de caractères est attendue",
                  'R'   : "Un réel est attendu",
                  'I'   : "Un entier est attendu"}
      type = mc.type[0]
      commentaire=d_aides.get(type,"Type de base inconnu")
      aideval=self.node.item.aide()
      commentaire=commentaire +"\n"+ aideval
      self.Commentaire.setText(QString(commentaire))

  def BOk2Pressed(self):
        SaisieValeur.BOk2Pressed(self)

  def BSupPressed(self):
        QTPanel.BSupPressed(self)

  def LEValeurPressed(self):
        SaisieValeur.LEValeurPressed(self)

  def BParametresPressed(self):
        QTPanel.BParametresPressed(self)

  def Ajout1Valeur(self,valeur):
        SaisieValeur.LEValeurPressed(self,valeur)

  def BSalomePressed(self):
        genea=self.node.item.get_genealogie()
        kwType = None
        for e in genea:
            if "GROUP_NO" in e: kwType = "GROUP_NO"
            if "GROUP_MA" in e: kwType = "GROUP_MA"

        selection, commentaire = self.editor.parent.appliEficas.selectGroupFromSalome(kwType,editor=self.editor)
        if commentaire !="" :
            self.Commentaire.setText(QString(commentaire))
        monTexte=""
        if selection == [] : return
        for geomElt in selection:
            monTexte=geomElt+","
        monTexte= monTexte[0:-1]
        self.LEValeur.setText(QString(monTexte))

  def BView2DPressed(self):
        valeur=self.LEValeur.text()
        if valeur == QString("") : return
        valeur = str(valeur)
        if valeur :
           ok, msgError = self.editor.parent.appliEficas.displayShape(valeur)
           if not ok:
              self.editor.parent.appli.affiche_infos(msgError)

