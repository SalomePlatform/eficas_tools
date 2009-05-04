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
# Modules Eficas

import os,traceback,sys
from qt import *
from desMacro import DMacro

from monMacroPanel import MonMacroPanel
import convert


# Import des panels

class MonIncludePanel(MonMacroPanel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        MonMacroPanel.__init__(self,node,parent,name,fl)
        #Version TK ??
        #if not hasattr(self.node.item.object,'fichier_ini'):
        if not hasattr(self.node.item.object,'fichier_ini'):
           self.ajoutPageBad()
        else:
           self.ajoutPageOk()

  def ajoutPageOk(self):
        self.TabPage = QWidget(self.TWChoix,"TabPage")
        self.LENomFichier = QLineEdit(self.TabPage,"LENomFichier")
        self.LENomFichier.setGeometry(QRect(18,127,450,30))
        self.textLabel1_3 = QLabel(self.TabPage,"textLabel1_3")
        self.textLabel1_3.setGeometry(QRect(70,50,350,41))
        self.BBrowse = QPushButton(self.TabPage,"BBrowse")
        self.BBrowse.setGeometry(QRect(288,306,161,41))
        self.TWChoix.insertTab(self.TabPage,QString(""))
        self.textLabel1_3.setText(self._DMacro__tr("<font size=\"+1\">La commande INCLUDE requiert un nom de Fichier :</font>"))
        self.BBrowse.setText(self._DMacro__tr("Edit"))
        self.TWChoix.changeTab(self.TabPage,self._DMacro__tr("Fichier Include"))
        self.TWChoix.setCurrentPage(2)
        if hasattr(self.node.item.object,'fichier_ini'):
           self.LENomFichier.setText(self.node.item.object.fichier_ini)
        else :
           self.LENomFichier.setText("")
        self.LENomFichier.setText(self.node.item.object.fichier_ini)


        self.BChangeFile = QPushButton(self.TabPage,"BChangeFile")
        self.BChangeFile.setGeometry(QRect(290,350,161,41))
        #self.BChangeFile.setSizePolicy(QSizePolicy(0,0,0,0,self.BChangeFile.sizePolicy().hasHeightForWidth()))
        self.BChangeFile.setText(self._DMacro__tr("Autre Fichier"))

        self.connect(self.BBrowse,SIGNAL("clicked()"),self.BBrowsePressed)
        self.connect(self.BChangeFile,SIGNAL("clicked()"),self.BChangeFilePressed)
        self.connect(self.LENomFichier,SIGNAL("returnPressed()"),self.LENomFichReturnPressed)


  def ajoutPageBad(self) :
        self.TabPage = QWidget(self.TWChoix,"TabPage")
	self.textLabel1_5 = QLabel(self.TabPage,"textLabel1_5")
	TabPageLayout = QGridLayout(self.TabPage,1,1,11,6,"TabPageLayout")
	TabPageLayout.addWidget(self.textLabel1_5,0,0)
        self.TWChoix.insertTab(self.TabPage,QString(""))
	self.resize(QSize(521,499).expandedTo(self.minimumSizeHint()))
	self.clearWState(Qt.WState_Polished)
        self.textLabel1_5.setText(self._DMacro__trUtf8("\x3c\x66\x6f\x6e\x74\x20\x73\x69\x7a\x65\x3d\x22\x2b\x31\x22\x3e\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x63\x65\x6e\x74\x65\x72\x22\x3e\x4c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x49\x4e\x43\x4c\x55\x44\x45\x20\x6e\x27\x61\x20\x70\x61\x73\x20\x64\x65\x20\x66\x69\x63\x68\x69\x65\x72\x20\x61\x73\x73\x6f\x63\x69\xc3\xa9\x2e\x0a\x49\x6c\x20\x66\x61\x75\x74\x20\x64\x27\x61\x62\x6f\x72\x64\x20\x63\x68\x6f\x69\x73\x69\x72\x20\x75\x6e\x20\x6e\x75\x6d\xc3\xa9\x72\x6f\x20\x64\x27\x75\x6e\x69\x74\xc3\xa9\x3c\x2f\x70\x3e\x3c\x2f\x66\x6f\x6e\x74\x3e"))
        self.TWChoix.changeTab(self.TabPage,self._DMacro__tr("Fichier Include"))
        self.TWChoix.setCurrentPage(2)


  def BBrowsePressed(self):
      self.node.makeEdit()

  def BOkIncPressed (self):
      self.LENomFichReturnPressed()

  def LENomFichReturnPressed(self):
        nomFichier=str(self.LENomFichier.text())
        if not os.path.isfile(nomFichier) :
           commentaire = "Fichier introuvable"
           self.Commentaire.setText(QString(commentaire))
           self.editor.affiche_infos(commentaire)
           return

        text=self.convert_file(nomFichier)

        # Si probleme a la lecture-conversion on arrete le traitement
        if not text:
           return

        try :
           self.node.item.object.change_fichier_init(nomFichier,text)
           commentaire = "Fichier modifie  : " + self.node.item.get_nom()
           self.Commentaire.setText(QString(commentaire))
           self.editor.affiche_infos(commentaire)
        except: 
           l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
           QMessageBox.critical( self, "Erreur fatale au chargement du fichier Include", l[0])
           commentaire = "Fichier invalide" 
           self.Commentaire.setText(QString(commentaire))
           self.editor.affiche_infos(commentaire)
           return


  def convert_file(self,file):
       """
         Methode pour convertir le fichier file dans le format courant
       """
       format=self.editor.format_fichier
       text=None
       if convert.plugins.has_key(format):
          # Le convertisseur existe on l'utilise
          p=convert.plugins[format]()
          p.readfile(file)
          text=p.convert('execnoparseur')
       else :
            commentaire = "Impossible de lire le fichier : Format inconnu"
            self.Commentaire.setText(QString(commentaire))
            self.editor.affiche_infos(commentaire)
       return text


  def BChangeFilePressed(self):
      userDir=os.path.expanduser("~/Eficas_install/")
      fn = QFileDialog.getOpenFileName(userDir,
                        self.trUtf8('All Files (*);;''JDC Files (*.comm);;'), self.editor)

      if fn.isNull():
         return

      fn = os.path.abspath((unicode(fn)))
      self.LENomFichier.setText(fn)
      self.LENomFichReturnPressed()
