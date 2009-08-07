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
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from desUniqueBase import Ui_DUnBase
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiqueUnique

class DUnBase(Ui_DUnBase,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.appliEficas=parent.appliEficas
       self.RepIcon=parent.appliEficas.RepIcon
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

class MonUniqueBasePanel(DUnBase,QTPanel,SaisieValeur):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonUniqueBasePanel"
        self.editor=parent
        QTPanel.__init__(self,node,parent)
        DUnBase.__init__(self,parent,fl)
        self.politique=PolitiqueUnique(node,parent)
        self.InitLineEditVal()
        self.InitCommentaire()
        self.detruitBouton()
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOk2Pressed)
        self.connect(self.lineEditVal,SIGNAL("returnPressed()"),self.LEValeurPressed)
        self.connect(self.bParametres,SIGNAL("pressed()"),self.BParametresPressed)
        self.connect(self.BSalome,SIGNAL("pressed()"),self.BSalomePressed)
        self.connect(self.BView2D,SIGNAL("clicked()"),self.BView2DPressed)
        self.connect(self.BFichier,SIGNAL("clicked()"),self.BFichierPressed)


  def detruitBouton(self):
        icon = QIcon(self.RepIcon+"/image240.png")
        self.BSalome.setIcon(icon)
        mc = self.node.item.get_definition()
        if self.node.item.get_nom() != "FileName" :
           self.BFichier.close()
        else :
	   self.bParametres.close()
        type = mc.type[0]
        #if not('grma' in repr(type)) or not(self.editor.salome) :
        if not(('grma' in repr(type)) or ('grno' in repr(type))) or not(self.editor.salome) :
           self.BSalome.close()
           self.BView2D.close()

  def InitLineEditVal(self):
        valeur=self.node.item.get_valeur()
        valeurTexte=self.politique.GetValeurTexte(valeur)
        if valeurTexte != None :
           if repr(valeurTexte.__class__).find("PARAMETRE") > 0:
               str = QString(repr(valeur)) 
           else :
               try :
                   str=QString("").setNum(valeurTexte)
               except :
                   str=QString(valeurTexte)
           self.lineEditVal.setText(str)


  def InitCommentaire(self):
      mc = self.node.item.get_definition()
      d_aides = { 'TXM' : "Une chaîne de caractères est attendue",
                  'R'   : "Un réel est attendu",
                  'I'   : "Un entier est attendu",
                  'Matrice' : 'Une Matrice est attendue',
                  'Fichier' : 'Un fichier est attendu'}
      type = mc.type[0]
      commentaire=d_aides.get(type,"Type de base inconnu")
      aideval=self.node.item.aide()
      commentaire=commentaire +"\n"+ aideval
      self.Commentaire.setText(QString(commentaire))

  def BOk2Pressed(self):
        SaisieValeur.BOk2Pressed(self)

  def BFichierPressed(self):
      fichier = QFileDialog.getOpenFileName(self.appliEficas,
                        self.appliEficas.trUtf8('Ouvrir Fichier'),
                        self.appliEficas.CONFIGURATION.savedir,
                        self.appliEficas.trUtf8('Wrapper Files (*.xml);;''All Files (*)'))
      if not(fichier.isNull()):
         self.lineEditVal.setText(fichier)

         
  def LEValeurPressed(self):
        SaisieValeur.LEValeurPressed(self)
        if self.node.item.parent.nom == "MODEL" : 
           if self.node.item.isvalid():
		   self.node.item.parent.change_fichier="1"
                   self.node.item.parent.build_include(None,"")

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

