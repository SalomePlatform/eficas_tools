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

class MonPoursuitePanel(MonMacroPanel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        MonMacroPanel.__init__(self,node,parent,name,fl)
        #Version TK ??
        self.ajoutPageOk()

  def ajoutPageOk(self) :
        self.TabPage = QWidget(self.TWChoix,"TabPage")
        self.LENomFichier = QLineEdit(self.TabPage,"LENomFichier")
        self.LENomFichier.setGeometry(QRect(18,127,450,30))
        self.textLabel1_3 = QLabel(self.TabPage,"textLabel1_3")
        self.textLabel1_3.setGeometry(QRect(70,50,350,41))
        self.BBrowse = QPushButton(self.TabPage,"BBrowse")
        self.BBrowse.setGeometry(QRect(288,306,161,41))
        self.TWChoix.insertTab(self.TabPage,QString(""))
        self.textLabel1_3.setText(self._DMacro__tr("<font size=\"+1\">La commande POURSUITE requiert un nom de Fichier :</font>"))
        self.BBrowse.setText(self._DMacro__tr("Edit"))
        self.TWChoix.changeTab(self.TabPage,self._DMacro__tr("Fichier Poursuite"))
        self.TWChoix.setCurrentPage(2)
        if hasattr(self.node.item.object,'fichier_ini'):
           self.LENomFichier.setText(self.node.item.object.fichier_ini)
        else :
           self.LENomFichier.setText("")
        self.connect(self.BBrowse,SIGNAL("clicked()"),self.BBrowsePressed)
        self.connect(self.LENomFichier,SIGNAL("returnPressed()"),self.LENomFichReturnPressed)


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

