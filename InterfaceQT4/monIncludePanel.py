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
from qtCommun import QTPanel
from qtCommun import QTPanelTBW1
from qtCommun import QTPanelTBW2
from qtCommun import QTPanelTBW3
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from  desInclude import Ui_DInc1
import convert

class DInc(Ui_DInc1,QDialog):
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

class MonIncludePanel(DInc,QTPanelTBW1,QTPanelTBW2,QTPanelTBW3):
  """
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonIncludePanel"
        DInc.__init__(self,parent,fl)
        QTPanel.__init__(self,node,parent)
        QTPanelTBW2.__init__(self,node,parent)
        QTPanelTBW1.__init__(self,node,parent)
        self.connecterSignaux()

        self.node=node
        #if (self.node.item.object.nom == "DICTDATA"):
        #   self.pageOk()
        #   return

        if not hasattr(self.node.item.object,'fichier_unite'):
           self.pageBad()
        else:
           self.pageOk()

  def pageOk(self):
        self.TWChoix.removeTab(3)
        self.TWChoix.setCurrentIndex(2)
        self.LENomFichier.setText(self.node.item.object.fichier_ini)


  def pageBad(self) :
        self.TWChoix.removeTab(2)
        self.TWChoix.setCurrentIndex(2)

  def BBrowsePressed(self):
      self.node.makeEdit()

  def BOkIncPressed (self):
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

        self.editor.init_modif()

        try :
           self.node.item.object.change_fichier_init(nomFichier,text)
           commentaire = "Fichier modifie  : " + self.node.item.get_nom()
           self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))
           self.editor.affiche_infos(commentaire)
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
       format=self.editor.format
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


  def BChangeFilePressed(self):
      userDir=self.node.appliEficas.CONFIGURATION.savedir
      fn = QFileDialog.getOpenFileName(self.node.appliEficas,
                self.node.appliEficas.trUtf8('Fichier Include'),
                userDir,
                self.node.appliEficas.trUtf8('All Files (*);;''JDC Files (*.comm);;'))

      if fn.isNull():
         return

      fn = os.path.abspath((unicode(fn)))
      ulfile = os.path.abspath(unicode(fn))
      self.node.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
      self.LENomFichier.setText(fn)
      self.LENomFichReturnPressed()

  def connecterSignaux(self):
        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListWidgetItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommandChanged)
        self.connect(self.BNext,SIGNAL("pressed()"),self.BNextPressed)
        self.connect(self.BBrowse,SIGNAL("clicked()"),self.BBrowsePressed)
        try :
           self.connect(self.BChangeFile,SIGNAL("clicked()"),self.BChangeFilePressed)
           self.connect(self.LENomFichier,SIGNAL("returnPressed()"),self.LENomFichReturnPressed)
        except :
           pass


  def BOkPressed(self):
      QTPanel.BOkPressed(self)

  def BNextPressed(self):
      QTPanelTBW2.BNextPressed(self)

  def BuildTabCommandChanged(self):
      QTPanelTBW2.BuildLBNouvCommandChanged(self)

  def LEFiltreTextChanged(self):
      QTPanelTBW2.LEFiltreTextChanged(self)

  def LEfiltreReturnPressed(self):
      QTPanelTBW2.LEfiltreReturnPressed(self)

  def LBNouvCommandeClicked(self):
      QTPanelTBW2.LBNouvCommandeClicked(self)

  def LENomConceptReturnPressed(self):
      QTPanelTBW3.LENomConceptReturnPressed(self)

