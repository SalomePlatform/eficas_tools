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
  Classe contenant les méthodes Qt communes a tous les panneaux droits
  Tous les panneaux Mon...Panel héritent de cette classe
  Gére plus précisement :
     - l affichage de la doc
     - le bouton Suppression (BSupPressed)
     - la mutualisation de l affichage des regles
  """
  def __init__(self,node, parent = None):
        self.editor    = parent
        self.node      = node
        if hasattr(self,'TWChoix'):
           self.connect(self.TWChoix, SIGNAL("currentChanged(QWidget *)"), self.GestionBALpha)

  def GestionBALpha(self,fenetre):
        if self.TWChoix.currentIndex()!=0:
           self.BAlpha.hide()
        else :
           self.BAlpha.setVisible(True)
           self.BuildLBMCPermis()

  def BOkPressed(self):
        """ Impossible d utiliser les vrais labels avec designer ?? """
        label=self.TWChoix.tabText(self.TWChoix.currentIndex())
        if label==QString("Nouvelle Commande"):
           self.DefCmd()
        if label==QString("Nommer Concept"):
           self.LENomConceptReturnPressed()
        if label==QString("Ajouter Mot-Clef"):
           if self.LBMCPermis.currentItem() == None : return
           self.DefMC(self.LBMCPermis.currentItem())
        if label==QString("Définition Formule"):
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
  Classe contenant les méthodes nécessaires a l onglet "Ajouter Mot-Clef"  
  hérite de QTPanel  # Attention n appelle pas le __init__
  Gére plus précisement :
  """
  def __init__(self,node, parent = None):
        self.editor    = parent
        self.node      = node
        self.alpha     = 0
        self.BuildLBMCPermis()
        self.AppelleBuildLBRegles()
        if hasattr(self,'BAlpha'):
           self.connect(self.BAlpha,SIGNAL("clicked()"),self.BAlphaPressed)

  def BAlphaPressed (self):
        if self.alpha == 0 :
           self.alpha=1
           self.BAlpha.setText("Tri Cata")
        else :
           self.alpha=0
           self.BAlpha.setText("Tri Alpha")
        self.BuildLBMCPermis()

           
  def BuildLBMCPermis(self):
        self.LBMCPermis.clear()
        QObject.connect(self.LBMCPermis,SIGNAL("itemDoubleClicked(QListWidgetItem*)"),self.DefMC)
        jdc = self.node.item.get_jdc()
        genea =self.node.item.get_genealogie()
        liste_mc=self.node.item.get_liste_mc_ordonnee(genea,jdc.cata_ordonne_dico)
        if ((len(liste_mc) < 10) and (hasattr(self,'BAlpha'))):
           self.BAlpha.hide()
        if self.alpha == 1 :
           liste_mc.sort()
        for aMc in liste_mc:
           self.LBMCPermis.addItem( aMc)
        if len(liste_mc) !=0:
           self.LBMCPermis.setCurrentItem(self.LBMCPermis.item(0))


  def DefMC(self,item):
        """ On ajoute un mot-clé à  la commande : subnode """
        name=str(item.text())
        self.editor.init_modif()
        self.node.append_child(name)

# ---------------------------- #
class QTPanelTBW2(QTPanel):
# ---------------------------- #
  """
  Classe contenant les méthodes nécessaires a l onglet "Nouvelle Commande"  
  hérite de QTPanel  # Attention n appelle pas le __init__
  Gére plus précisement :
  """

  def __init__(self,node, parent = None, racine = 0):
        self.editor    = parent
        self.node      = node
        self.BuildLBNouvCommande()
        self.LEFiltre.setFocus()
        self.NbRecherches = 0
        if racine == 1 :
           self.AppelleBuildLBRegles()
           self.LEFiltre.setFocus()
        else :
           self.connect(self.TWChoix, SIGNAL("currentChanged(QWidget *)"), self.handleCurrentChanged)
            


  def handleCurrentChanged(self):
        try :
          label=self.TWChoix.tabText(self.TWChoix.currentIndex())
          if label==QString("Nouvelle Commande"):
            self.LEFiltre.setFocus()
          if label==QString("Nommer Concept"):
           self.LENomConcept.setFocus()
          if label==QString("Définition Formule"):
           self.LENomFormule.setFocus()
          if label==QString("Valeur Parametre"):
           self.lineEditNom.setFocus()
          if label==QString("Fichier Include"):
           self.LENomFichier.setFocus()
          if label==QString("Ajouter Mot-Clef"):
           self.LBMCPermis.setCurrentItem(self.LBMCPermis.item(0))
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
        self.LEFiltre.setFocus()

  def DefCmd(self):
        if self.LBNouvCommande.currentItem()== 0 : return
        if self.LBNouvCommande.currentItem()== None : return
        name=str(self.LBNouvCommande.currentItem().text())
        if name==QString(" "):
	   return
        if name.find("GROUPE :")==0 :
	   return
        self.editor.init_modif()
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
  Classe contenant les méthodes nécessaires a l onglet "Nommer Concept"  
  si non réentrant
  hérite de QTPanel                   # Attention n appelle pas le __init__
  Gére plus précisement :
  """

  def __init__(self,node, parent = None):
        self.editor    = parent
        self.node      = node
        type_sd = self.node.item.get_type_sd_prod()
        nomConcept = self.node.item.GetText()
        self.typeConcept.setText(type_sd)
        self.LENomConcept.setText("")
        self.LENomConcept.setText(nomConcept)
        self.LENomConcept.setFocus()
        if self.node.item.is_reentrant():
           self.makeConceptPage_reentrant()
        else :
           self.listBoxASSD.close()

  def makeConceptPage_reentrant(self):
        self.bOk.close()
        self.LENomConcept.close()
        self.Label2.close()
        self.Label3.close()
        self.typeConcept.close()
        self.LENomConcept.close()
        self.Label1.setText(QtGui.QApplication.translate("DUnASSD", "<font size=\"+1\"><p align=\"center\">Structures de données à enrichir\n"
" par l\'operateur courant :</p></font>", None, QtGui.QApplication.CodecForTr))
        listeNomsSD = self.node.item.get_noms_sd_oper_reentrant()
        for aSD in listeNomsSD:
            self.listBoxASSD.addItem( aSD)
        QObject.connect(self.listBoxASSD, SIGNAL("itemDoubleClicked(QListWidgetItem*)" ), self.ClicASSD )

        
  def ClicASSD(self):
        if self.listBoxASSD.currentItem()== None : return
        val=self.listBoxASSD.currentItem().text()
        nom=str(val)
        nom = string.strip(nom)
        test,mess = self.node.item.nomme_sd(nom)
        if (test== 0):
           self.editor.affiche_infos(mess,Qt.red)

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
    def __init__(self,parent,editor=None):
        QDialog.__init__(self,parent)
        self.editor=editor
        self.setupUi(self)

        self.resize( QSize(600,600).expandedTo(self.minimumSizeHint()) )
        self.connect( self.bclose,SIGNAL("clicked()"), self, SLOT("close()") )
        self.connect( self.bsave,SIGNAL("clicked()"), self.saveFile )
        
    def setText(self, txt ):    
        self.view.setText(txt)
        
    def saveFile(self):
        #recuperation du nom du fichier
        fn = QFileDialog.getSaveFileName(None,
                self.trUtf8("Save File"),
                self.editor.appliEficas.CONFIGURATION.savedir)
        if fn.isNull() : return
        ulfile = os.path.abspath(unicode(fn))
        self.editor.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
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

