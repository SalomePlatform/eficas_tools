# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
# Modules Python
import string,types,os
import traceback

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

# Import des panels

# ---------- #
class QTPanel:
# ---------- #
  """
  Classe contenant les methodes Qt communes a tous les panneaux droits
  Tous les panneaux Mon...Panel heritent de cette classe
  Gere plus precisement :
     - l affichage de la doc
     - le bouton Suppression (BSupPressed)
     - la mutualisation de l affichage des regles
  """
  def __init__(self,node, parent = None):
        self.editor    = parent
        self.node      = node
        if hasattr(self,'TWChoix'):
           self.connect(self.TWChoix, SIGNAL("currentChanged(QWidget *)"), self.GestionBALpha)

  def keyReleaseEvent(self,event):
        if event.matches(QKeySequence.Copy): self.editor.appliEficas.editCopy() 
        if event.matches(QKeySequence.Cut): self.editor.appliEficas.editCut() 
        if event.matches(QKeySequence.Paste): self.editor.appliEficas.editPaste() 


  def GestionBALpha(self,fenetre):
        if self.TWChoix.currentIndex()!=0:
           if hasattr(self,'BAlpha'): #pour include materiau
              self.BAlpha.hide()
        else :
           self.BAlpha.setVisible(True)
           self.BuildLBMCPermis()

  def BOkPressed(self):
        """ Impossible d utiliser les vrais labels avec designer ?? """
        label=self.TWChoix.tabText(self.TWChoix.currentIndex())
        if label==tr("Nouvelle Commande"):
           self.DefCmd()
        if label==tr("Nommer Concept"):
           self.LENomConceptReturnPressed()
        if label==tr("Ajouter Mot-Clef"):
           if self.LBMCPermis.currentItem() == None : return
           self.DefMC(self.LBMCPermis.currentItem())
        if label==tr("Definition Formule"):
           self.BOkPressedFormule()
        if label==tr("Valeur Parametre"):
           self.BOkParamPressed()
        if label==tr("Fichier Include"):
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
  Classe contenant les methodes necessaires a l onglet "Ajouter Mot-Clef"  
  herite de QTPanel  # Attention n appelle pas le __init__
  Gere plus precisement :
  """
  def __init__(self,node, parent = None):
        self.editor    = parent
        self.node      = node
        if not(hasattr(self.node,'alpha')): self.node.alpha  = 0
        self.BuildLBMCPermis()
        self.AppelleBuildLBRegles()
        if hasattr(self,'BAlpha'):
           self.connect(self.BAlpha,SIGNAL("clicked()"),self.BAlphaPressed)

  def BAlphaPressed (self):
        if self.node.alpha == 0 :
           self.node.alpha=1
           self.BAlpha.setText(tr("Tri Cata"))
        else :
           self.node.alpha=0
           self.BAlpha.setText(tr("Tri Alpha"))
        self.BuildLBMCPermis()

           
  def BuildLBMCPermis(self):
        self.LBMCPermis.clear()
        QObject.connect(self.LBMCPermis,SIGNAL("itemDoubleClicked(QListWidgetItem*)"),self.DefMC)
        jdc = self.node.item.get_jdc()
        genea =self.node.item.get_genealogie()
        liste_mc=self.node.item.get_liste_mc_ordonnee(genea,jdc.cata_ordonne_dico)
        if ((len(liste_mc) < 10) and (hasattr(self,'BAlpha'))):
           self.BAlpha.hide()
        if self.node.alpha == 1 : liste_mc.sort()
        for aMc in liste_mc: self.LBMCPermis.addItem( aMc)
        if len(liste_mc) !=0: self.LBMCPermis.setCurrentItem(self.LBMCPermis.item(0))


  def DefMC(self,item):
        """ On ajoute un mot-cle à  la commande : subnode """
        name=str(item.text())
        self.editor.init_modif()
        self.node.append_child(name)

# ---------------------------- #
class QTPanelTBW2(QTPanel):
# ---------------------------- #
  """
  Classe contenant les methodes necessaires a l onglet "Nouvelle Commande"  
  herite de QTPanel  # Attention n appelle pas le __init__
  Gere plus precisement :
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
          if label==tr("Nouvelle Commande"):
            self.LEFiltre.setFocus()
          if label==tr("Nommer Concept"):
           self.LENomConcept.setFocus()
          if label==tr("Definition Formule"):
           self.LENomFormule.setFocus()
          if label==tr("Valeur Parametre"):
           self.lineEditNom.setFocus()
          if label==tr("Fichier Include"):
           self.LENomFichier.setFocus()
          if label==tr("Ajouter Mot-Clef"):
           self.LBMCPermis.setCurrentItem(self.LBMCPermis.item(0))
        except :
          pass

      
  def BuildLBNouvCommande(self):
        self.LBNouvCommande.clear()

        jdc=self.node.item.object.get_jdc_root()

        listeGroupes,dictGroupes=jdc.get_groups()
        if "CACHE" in dictGroupes.keys():
           aExclure=dictGroupes["CACHE"]
        else:
           aExclure=()
        if self.editor.mode_nouv_commande == "alpha":
           self.RBalpha.setChecked(True)
           self.RBGroupe.setChecked(False)
           listeCmd = jdc.get_liste_cmd()
           for aCmd in listeCmd:
              if aCmd not in aExclure :
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
                if aCmd not in aExclure :
                 self.LBNouvCommande.addItem( aCmd)
              self.LBNouvCommande.addItem( " " )
        elif self.editor.mode_nouv_commande== "initial" :
           listeCmd =  self.editor.Commandes_Ordre_Catalogue
           listeCmd2=jdc.get_liste_cmd()
           if len(listeCmd) != len(listeCmd2):
               listeCmd	= listeCmd2
           for aCmd in listeCmd:
              if aCmd not in aExclure :
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
  Classe contenant les methodes necessaires a l onglet "Nommer Concept"  
  si non reentrant
  herite de QTPanel                   # Attention n appelle pas le __init__
  Gere plus precisement :
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
        self.Label1.setText(tr("<font size=\"+1\"><p align=\"center\">Structures de donnees à enrichir\n"
" par l\'operateur courant :</p></font>"))
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
    def __init__(self,parent,editor=None,entete=None):
        QDialog.__init__(self,parent)
        self.editor=editor
        self.setupUi(self)

        self.resize( QSize(600,600).expandedTo(self.minimumSizeHint()) )
        self.connect( self.bclose,SIGNAL("clicked()"), self, SLOT("close()") )
        self.connect( self.bsave,SIGNAL("clicked()"), self.saveFile )
        if entete != None : self.setWindowTitle (entete)

        
    def setText(self, txt ):    
        self.view.setText(txt)
        
    def saveFile(self):
        #recuperation du nom du fichier
        if self.editor != None :
           dir=self.editor.appliEficas.CONFIGURATION.savedir
        else:
           dir='/tmp'
        fn = QFileDialog.getSaveFileName(None,
                tr("Sauvegarder le fichier"),
                dir)
        if fn.isNull() : return
        ulfile = os.path.abspath(unicode(fn))
        if self.editor != None :
           self.editor.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
        try:
           f = open(fn, 'wb')
           f.write(str(self.view.toPlainText()))
           f.close()
           return 1
        except IOError, why:
           QMessageBox.critical(self, tr("Sauvegarder le fichier"),
                tr("Le fichier <b>%(v_1)s</b> n'a pu etre sauvegarde. <br>Raison : %(v_2)s", {'v_1': unicode(fn), 'v_2': unicode(why)}))
           return

