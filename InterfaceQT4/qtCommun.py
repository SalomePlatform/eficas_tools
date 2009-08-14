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
import traceback

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# Import des panels

# ---------- #
class QTPanel:
# ---------- #
  """
  Classe contenant les m�thodes Qt communes a tous les panneaux droits
  Tous les panneaux Mon...Panel h�ritent de cette classe
  G�re plus pr�cisement :
     - l affichage de la doc
     - le bouton Suppression (BSupPressed)
     - la mutualisation de l affichage des regles
  """
  def __init__(self,node, parent = None):
        self.editor    = parent
        self.node      = node
        
  def BOkPressed(self):
        """ Impossible d utiliser les vrais labels avec designer ?? """
        label=self.TWChoix.tabText(self.TWChoix.currentIndex())
        print label
        if label==QString("Nouvelle Commande"):
           self.DefCmd()
        if label==QString("Nommer Concept"):
           self.LENomConceptReturnPressed()
        if label==QString("Ajouter Mot-Clef"):
           if self.LBMCPermis.currentItem() == None : return
           self.DefMC(self.LBMCPermis.currentItem())
        if label==QString("D�finition Formule"):
           self.BOkPressedFormule()
        if label==QString("Valeur Parametre"):
           self.BOkParamPressed()
        if label==QString("Fichier Include"):
           self.BOkIncPressed()

  def BParametresPressed(self):
        liste=self.node.item.get_liste_param_possible()
        from monListeParamPanel import MonListeParamPanel
        MonListeParamPanel(liste=liste,parent=self).show()
       
  def AppelleBuildLBRegles(self):
        listeRegles     = self.node.item.get_regles()
        listeNomsEtapes = self.node.item.get_mc_presents()
        self.BuildLBRegles(listeRegles,listeNomsEtapes)


  def BuildLBRegles(self,listeRegles,listeNomsEtapes):
        self.LBRegles.clear()
        if len(listeRegles) > 0:
           for regle in listeRegles :
              texteRegle=regle.gettext()
              texteMauvais,test = regle.verif(listeNomsEtapes)
              for ligne in texteRegle.split("\n") :
                 if ligne == "" :
                    self.LBRegles.addItem(ligne)
                    continue
                 if ligne[0]=="\t" :
                    ligne="     "+ligne[1:]
                 if test :
                    self.LBRegles.addItem(ligne)
                 else :
                    
                    monItem=QListWidgetItem(ligne)
                    monItem.setForeground(Qt.red)
                    self.LBRegles.addItem(monItem)


# ----------------------- #
class QTPanelTBW1(QTPanel):
# ----------------------- #
  """
  Classe contenant les m�thodes n�cessaires a l onglet "Ajouter Mot-Clef"  
  h�rite de QTPanel  # Attention n appelle pas le __init__
  G�re plus pr�cisement :
  """
  def __init__(self,node, parent = None):
        self.editor    = parent
        self.node      = node
        self.BuildLBMCPermis()
        self.AppelleBuildLBRegles()

  def BuildLBMCPermis(self):
        self.LBMCPermis.clear()
        QObject.connect(self.LBMCPermis,SIGNAL("itemDoubleClicked(QListWidgetItem*)"),self.DefMC)
        jdc = self.node.item.get_jdc()
        genea =self.node.item.get_genealogie()
        liste_mc=self.node.item.get_liste_mc_ordonnee(genea,jdc.cata_ordonne_dico)
        for aMc in liste_mc:
           self.LBMCPermis.addItem( aMc)


  def DefMC(self,item):
        """ On ajoute un mot-cl� �  la commande : subnode """
        name=str(item.text())
        self.editor.init_modif()
        self.node.append_child(name)

# ---------------------------- #
class QTPanelTBW2(QTPanel):
# ---------------------------- #
  """
  Classe contenant les m�thodes n�cessaires a l onglet "Nouvelle Commande"  
  h�rite de QTPanel  # Attention n appelle pas le __init__
  G�re plus pr�cisement :
  """

  def __init__(self,node, parent = None, racine = 0):
        self.editor    = parent
        self.node      = node
        self.BuildLBNouvCommande()
        self.LEFiltre.setFocus()
        self.NbRecherches = 0
        if racine == 1 :
           self.AppelleBuildLBRegles()
        else :
           self.connect(self.TWChoix, SIGNAL("currentChanged(QWidget *)"), self.handleCurrentChanged)


  def handleCurrentChanged(self):
        try :
            self.LEFiltre.setFocus()
        except :
            pass

      
  def BuildLBNouvCommande(self):
        self.LBNouvCommande.clear()

        jdc=self.node.item.object.get_jdc_root()
        if self.editor.mode_nouv_commande == "alpha":
           self.RBalpha.setChecked(True)
           self.RBGroupe.setChecked(False)
           listeCmd = jdc.get_liste_cmd()
           for aCmd in listeCmd:
              self.LBNouvCommande.addItem( aCmd )
        elif self.editor.mode_nouv_commande== "groupe" :
           self.RBGroupe.setChecked(True)
           self.RBalpha.setChecked(False)

           listeGroupes,dictGroupes=jdc.get_groups()
           for grp in listeGroupes:
              if grp == "CACHE":continue
              listeCmd=dictGroupes[grp]
              texte="GROUPE : "+grp
              self.LBNouvCommande.addItem( texte )
              self.LBNouvCommande.addItem( " " )
              for aCmd in listeCmd:
                 self.LBNouvCommande.addItem( aCmd)
              self.LBNouvCommande.addItem( " " )
        elif self.editor.mode_nouv_commande== "initial" :
           listeCmd =  self.editor.Commandes_Ordre_Catalogue
           listeCmd2=jdc.get_liste_cmd()
           if len(listeCmd) != len(listeCmd2):
               listeCmd	= listeCmd2
           for aCmd in listeCmd:
              self.LBNouvCommande.addItem( aCmd )
        #QObject.connect( self.LBNouvCommande, SIGNAL("itemClicked(QListWidgetItem*)"),self.DefCmd )
        QObject.connect( self.LBNouvCommande, SIGNAL("itemDoubleClicked(QListWidgetItem*)"),self.DefCmd )

  def BuildLBNouvCommandChanged(self) :
        if self.RBalpha.isChecked():
           self.editor.mode_nouv_commande="alpha"
        else :
           self.editor.mode_nouv_commande="groupe"
        self.BuildLBNouvCommande()

  def DefCmd(self):
        if self.LBNouvCommande.currentItem()== 0 : return
        if self.LBNouvCommande.currentItem()== None : return
        name=str(self.LBNouvCommande.currentItem().text())
        if name==QString(" "):
	   return
        if name.find("GROUPE :")==0 :
	   return
        self.editor.init_modif()
        print self.node
        print name
        new_node = self.node.append_brother(name,'after')


  def LEFiltreTextChanged(self):
        self.NbRecherches = 0
        try :
           MonItem=self.LBNouvCommande.findItems(self.LEFiltre.text().toUpper(),Qt.MatchContains)[0]
	   self.LBNouvCommande.setCurrentItem(MonItem)
        except :
           pass

  def LEfiltreReturnPressed(self):
        self.DefCmd()

  def BNextPressed(self):
        self.NbRecherches = self.NbRecherches + 1
        monItem = None
        try :
            MonItem=self.LBNouvCommande.findItems(self.LEFiltre.text().toUpper(),Qt.MatchContains)[self.NbRecherches]
        except :
            try : # ce try sert si la liste est vide
               MonItem=self.LBNouvCommande.findItems(self.LEFiltre.text().toUpper(),Qt.MatchContains)[0]
               self.NbRecherches = 0
            except :
               return
	self.LBNouvCommande.setCurrentItem(MonItem)

  def LBNouvCommandeClicked(self):
        name=str(self.LBNouvCommande.currentText())


# ---------------------------- #
class QTPanelTBW3(QTPanel):
# ---------------------------- #

  """
  Classe contenant les m�thodes n�cessaires a l onglet "Nommer Concept"  
  si non r�entrant
  h�rite de QTPanel                   # Attention n appelle pas le __init__
  G�re plus pr�cisement :
  """

  def __init__(self,node, parent = None):
        self.editor    = parent
        self.node      = node
        type_sd = self.node.item.get_type_sd_prod()
        nomConcept = self.node.item.GetText()
        self.typeConcept.setText(type_sd)
        self.LENomConcept.setText("")
        self.LENomConcept.setText(nomConcept)
        
  def LENomConceptReturnPressed(self):
        """
        Nomme le concept SD retourne par l'etape
        """
        nom = str(self.LENomConcept.text())
        nom = string.strip(nom)
        if nom == '' : return                  # si pas de nom, on ressort sans rien faire
        self.editor.init_modif()
        test,mess = self.node.item.nomme_sd(nom)
        #Notation scientifique
        from politiquesValidation import Validation
        validation=Validation(self.node,self.editor)
        validation.AjoutDsDictReelEtape()
        self.editor.affiche_infos(mess)

# ------------------------------- #
from desViewTexte import Ui_dView
class ViewText(Ui_dView,QDialog):
# ------------------------------- #
    """
    Classe permettant la visualisation de texte
    """
    def __init__(self,parent):
        QDialog.__init__(self,parent)
        self.parent=parent
        self.setupUi(self)

        self.resize( QSize(600,600).expandedTo(self.minimumSizeHint()) )
        self.connect( self.bclose,SIGNAL("clicked()"), self, SLOT("close()") )
        self.connect( self.bsave,SIGNAL("clicked()"), self.saveFile )
        
    def setText(self, txt ):    
        self.view.setText(txt)
        
    def saveFile(self):
        #recuperation du nom du fichier
        userDir=os.path.expanduser("~/.Eficas_install/")
        fn = QFileDialog.getSaveFileName(None,
                self.trUtf8("Save File"),
                self.trUtf8(userDir))
        if fn.isNull() : return
        try:
           f = open(fn, 'wb')
           f.write(str(self.view.toPlainText()))
           f.close()
           return 1
        except IOError, why:
           QMessageBox.critical(self, self.trUtf8('Save File'),
                self.trUtf8('The file <b>%1</b> could not be saved.<br>Reason: %2')
                    .arg(unicode(fn)).arg(str(why)))
           return

