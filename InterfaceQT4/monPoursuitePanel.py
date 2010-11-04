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
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import convert


from monMacroPanel import MonMacroPanel


# Import des panels
# La page est ajoutee a partir du python genere par designer

class MonPoursuitePanel(MonMacroPanel):
  """
  Classe d�finissant le panel associ� aux mots-cl�s qui demandent
  � l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discr�tes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        MonMacroPanel.__init__(self,node,parent,name,fl)
        self.node=node
        self.ajoutPageOk()

  def ajoutPageOk(self) :
        self.TabPage = QtGui.QWidget()
        self.TabPage.setObjectName("TabPage")
        self.textLabel1_3 = QtGui.QLabel(self.TabPage)
        self.textLabel1_3.setGeometry(QtCore.QRect(9, 9, 481, 19))
        self.textLabel1_3.setWordWrap(False)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.LENomFichier = QtGui.QLineEdit(self.TabPage)
        self.LENomFichier.setGeometry(QtCore.QRect(9, 33, 481, 40))
        self.LENomFichier.setMinimumSize(QtCore.QSize(470, 40))
        self.LENomFichier.setObjectName("LENomFichier")
        self.BFichier = QtGui.QPushButton(self.TabPage)
        self.BFichier.setGeometry(QtCore.QRect(330, 170, 140, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BFichier.sizePolicy().hasHeightForWidth())
        self.BFichier.setSizePolicy(sizePolicy)
        self.BFichier.setMinimumSize(QtCore.QSize(140, 50))
        self.BFichier.setObjectName("BFichier")
        self.BBrowse = QtGui.QPushButton(self.TabPage)
        self.BBrowse.setGeometry(QtCore.QRect(330, 110, 140, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BBrowse.sizePolicy().hasHeightForWidth())
        self.BBrowse.setSizePolicy(sizePolicy)
        self.BBrowse.setMinimumSize(QtCore.QSize(140, 50))
        self.BBrowse.setObjectName("BBrowse")
        self.TWChoix.addTab(self.TabPage, "")

        self.BFichier.setText(QtGui.QApplication.translate("DPour", "Autre Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.BBrowse.setText(QtGui.QApplication.translate("DPour", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.TabPage), QtGui.QApplication.translate("DPour", "Fichier Poursuite", None, QtGui.QApplication.UnicodeUTF8))

        if hasattr(self.node.item.object,"fichier_ini"):
           self.LENomFichier.setText(self.node.item.object.fichier_ini)

        self.connect(self.BBrowse,SIGNAL("clicked()"),self.BBrowsePressed)
        self.connect(self.BFichier,SIGNAL("clicked()"),self.BFichierPressed)
        self.connect(self.LENomFichier,SIGNAL("returnPressed()"),self.LENomFichReturnPressed)



  def BBrowsePressed(self):
      if hasattr(self.node.item,'object'):
         self.node.makeEdit()

  def BFichierPressed(self):
      fichier = QFileDialog.getOpenFileName(self.appliEficas,
                        self.appliEficas.trUtf8('Ouvrir Fichier'),
                        self.appliEficas.CONFIGURATION.savedir,
                        self.appliEficas.trUtf8('JDC Files (*.comm);;''All Files (*)'))
      if not(fichier.isNull()):
        ulfile = os.path.abspath(unicode(fichier))
        self.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
        self.LENomFichier.setText(fichier)
      self.LENomFichReturnPressed()

  def LENomFichReturnPressed(self):
        nomFichier=str(self.LENomFichier.text())
        if not os.path.isfile(nomFichier) :
           commentaire = "Fichier introuvable"
           self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))
           self.editor.affiche_infos(commentaire,Qt.red)
           return

        text=self.convert_file(nomFichier)

        # Si probleme a la lecture-conversion on arrete le traitement
        if not text:
           return

        try :
           self.node.item.object.change_fichier_init(nomFichier,text)
           commentaire = "Fichier modifie  : " + self.node.item.get_nom()
           self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))
        except: 
           l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
           QMessageBox.critical( self, "Erreur fatale au chargement du fichier Include", l[0])
           commentaire = "Fichier invalide" 
           self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))
           self.editor.affiche_infos(commentaire,Qt.red)
           return


  def convert_file(self,file):
       """
         Methode pour convertir le fichier file dans le format courant
       """
       try :
          format=self.editor.format_fichier
       except :
          format="python"
       text=None
       if convert.plugins.has_key(format):
          # Le convertisseur existe on l'utilise
          p=convert.plugins[format]()
          p.readfile(file)
          text=p.convert('execnoparseur')
       else :
            commentaire = "Impossible de lire le fichier : Format inconnu"
            self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))
            self.editor.affiche_infos(commentaire,Qt.red)
       return text
