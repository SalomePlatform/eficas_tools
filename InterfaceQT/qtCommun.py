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

from qt import *
import prefsQT

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
        
  def BSupPressed(self):
        self.editor.init_modif()
        self.node.delete()
        
  def ViewDoc(self) :
      cle_doc = self.node.item.get_docu()
      if cle_doc == None :
         QMessageBox.information( self.editor, "Documentation Vide", \
                                  "Aucune documentation Aster n'est associée à ce noeud")
         return
      cle_doc = string.replace(cle_doc,'.','')
      cle_doc = string.replace(cle_doc,'-','')
      commande = self.editor.appliEficas.CONFIGURATION.exec_acrobat
      try :
         f=open(commande,"rb")
      except :
         texte="impossible de trouver la commande  " + commande
         QMessageBox.information( self.editor, "Lecteur PDF", texte)
         return
      nom_fichier = cle_doc+".pdf"
      fichier = os.path.abspath(os.path.join(self.editor.CONFIGURATION.path_doc,
                                       nom_fichier))
      try :
         f=open(fichier,"rb")
      except :
         texte="impossible d'ouvrir " + fichier
         QMessageBox.information( self.editor, "Documentation Vide", texte)
         return
      if os.name == 'nt':
          os.spawnv(os.P_NOWAIT,commande,(commande,fichier,))
      elif os.name == 'posix':
          script ="#!/usr/bin/sh \n%s %s&" %(commande,fichier)
          pid = os.system(script)

  def BOkPressed(self):
        """ Impossible d utiliser les vrais labels avec designer ?? """
        label=self.TWChoix.tabLabel(self.TWChoix.currentPage())
        if label==QString("Nouvelle Commande"):
           self.DefCmd()
        if label==QString("Nommer Concept"):
           self.LENomConceptReturnPressed()
        if label==QString("Ajouter Mot-Clef"):
           self.DefMC()
        if label==QString("Définition Formule"):
           self.BOkPressedFormule()
        if label==QString("Valeur Parametre"):
           self.BOkParamPressed()
        if label==QString("Fichier Include"):
           self.BOkIncPressed()
        if label==QString("Commentaire"):
           self.TexteCommentaireEntre()

  def BParametresPressed(self):
        liste=self.node.item.get_liste_param_possible()
        from monListeParamPanel import MonListeParamPanel
        MonListeParamPanel(liste=liste,parent=self).show()
       
  def AppelleBuildLBRegles(self):
        listeRegles     = self.node.item.get_regles()
        listeNomsEtapes = self.node.item.get_mc_presents()
        self.BuildLBRegles(listeRegles,listeNomsEtapes)


  def BuildLBRegles(self,listeRegles,listeNomsEtapes):
        if len(listeRegles) > 0:
           for regle in listeRegles :
              texteRegle=regle.gettext()
              texteMauvais,test = regle.verif(listeNomsEtapes)
              for ligne in texteRegle.split("\n") :
                 if ligne == "" :
                    self.LBRegles.insertItem(ligne)
                    continue
                 if ligne[0]=="\t" :
                    ligne="     "+ligne[1:]
                 if test :
                    self.LBRegles.insertItem(ligne)
                 else :
                    self.LBRegles.insertItem(itemColore(ligne))


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
        self.BuildLBMCPermis()
        self.AppelleBuildLBRegles()

  def BuildLBMCPermis(self):
        self.LBMCPermis.clear()
        try :
           QObject.disconnect(self.LBMCPermis,SIGNAL("doubleClicked(QListBoxItem*)"),self.DefMC)
        except :
           # normal pour la première fois qu on passe
           # peut-etre inutile selon le connect ??
           pass
        QObject.connect(self.LBMCPermis,SIGNAL("doubleClicked(QListBoxItem*)"),self.DefMC)

        jdc = self.node.item.get_jdc()
        genea =self.node.item.get_genealogie()
        liste_mc=self.node.item.get_liste_mc_ordonnee(genea,jdc.cata_ordonne_dico)
        for aMc in liste_mc:
           self.LBMCPermis.insertItem( aMc)


  def DefMC(self):
        """ On ajoute un mot-clé à  la commande : subnode """
        if self.LBMCPermis.selectedItem() == None : return
        name=str(self.LBMCPermis.selectedItem().text())
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
        if racine == 1 : self.AppelleBuildLBRegles()

      
  def BuildLBNouvCommande(self):
        self.LBNouvCommande.clear()
        try :
           QObject.disconnect(self.LBNouvCommande,SIGNAL("doubleClicked(QListBoxItem*)"),self.DefCmd)
        except :
           # normal pour la première fois qu on passe
           # peut-etre inutile selon le connect ??
           pass

        jdc=self.node.item.object.get_jdc_root()
        if self.RBalpha.isOn():
           listeCmd = jdc.get_liste_cmd()
           for aCmd in listeCmd:
              self.LBNouvCommande.insertItem( aCmd )
        else :
           listeGroupes,dictGroupes=jdc.get_groups()
           for grp in listeGroupes:
              if grp == "CACHE":continue
              listeCmd=dictGroupes[grp]
              texte="GROUPE : "+grp
              self.LBNouvCommande.insertItem( texte )
              self.LBNouvCommande.insertItem( " " )
              for aCmd in listeCmd:
                 self.LBNouvCommande.insertItem( aCmd)
              self.LBNouvCommande.insertItem( " " )
        QObject.connect( self.LBNouvCommande, SIGNAL("doubleClicked(QListBoxItem*)"),self.DefCmd )
        QObject.connect( self.LBNouvCommande, SIGNAL("returnPressed(QListBoxItem*)"),self.DefCmd )

  def DefCmd(self):
        if (self.editor.focusWidget())!=self.LBNouvCommande :
            return 
        if self.LBNouvCommande.selectedItem()== 0 : return
        if self.LBNouvCommande.selectedItem()== None : return
        name=str(self.LBNouvCommande.selectedItem().text())
        if name==QString(" "):
	   return
        if name.find("GROUPE :")==0 :
	   return
        self.editor.init_modif()
        new_node = self.node.append_brother(name,'after')


  def LEFiltreTextChanged(self):
        MonItem=self.LBNouvCommande.findItem(self.LEFiltre.text().upper(),Qt.Contains)
	if MonItem != None :
	   self.LBNouvCommande.setCurrentItem(MonItem)
	   self.LBNouvCommande.setSelected(MonItem,1)
        try :
           QObject.disconnect(self.LBNouvCommande,SIGNAL("returnPressed(QListBoxItem*)"),self.DefCmd)
        except :
           pass

  def LEfiltreReturnPressed(self):
        self.DefCmd()

  def BNextPressed(self):
        MonItem=self.LBNouvCommande.findItem(self.LEFiltre.text().upper(),Qt.Contains)
        if MonItem != None :
           self.LBNouvCommande.setCurrentItem(self.LBNouvCommande.currentItem()+1)
           self.LEFiltreTextChanged()

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
        


  def LENomConceptReturnPressed(self):
        """
        Nomme le concept SD retourne par l'etape
        """
        nom = str(self.LENomConcept.text())
        nom = string.strip(nom)

        if nom == '' : return                  # si pas de nom, on ressort sans rien faire

        self.editor.init_modif()
        test,mess = self.node.item.nomme_sd(nom)
        self.editor.affiche_infos(mess)

# ----------------------- #
class ViewText(QDialog):
# ----------------------- #
    """
    Classe permettant la visualisation de texte
    """
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)
        
        l1 = QVBoxLayout(self,11,6,)
        self.view = QTextEdit(self)
        self.view.setReadOnly(True)

        l2 = QHBoxLayout(None,0,6)
        Horizontal_Spacing2 = QSpacerItem(220,20,QSizePolicy.Expanding,QSizePolicy.Minimum)                
        bclose= QPushButton(self)
        bclose.setText(self.trUtf8( "Fermer"))
        bsave= QPushButton(self)
        bsave.setText(self.trUtf8( "Sauver"))
        l2.addItem(Horizontal_Spacing2)
        l2.addWidget(bsave)
        l2.addWidget(bclose)
                
        l1.addWidget(self.view)        
        l1.addLayout(l2)

        self.resize( QSize(600,507).expandedTo(self.minimumSizeHint()) )
        self.connect( bclose,SIGNAL("clicked()"), self, SLOT("close()") )
        self.connect( bsave,SIGNAL("clicked()"), self.saveFile )
        
    def setText(self, txt ):    
        self.view.setText(txt)
        
    def saveFile(self):
        #recuperation du nom du fichier
        fn = QFileDialog.getSaveFileName(None,
                self.trUtf8("All Files (*)"), self, None,
                self.trUtf8("Save File"), '', 0)                
        if not fn.isNull():                
           if QFileInfo(fn).exists():
              abort = QMessageBox.warning(self,
                        self.trUtf8("Save File"),
                        self.trUtf8("The file <b>%1</b> already exists.")
                            .arg(fn),
                        self.trUtf8("&Overwrite"),
                        self.trUtf8("&Abort"), None, 1)
              if abort:
                 return
           fn = unicode(QDir.convertSeparators(fn))                
        else:
           return

        #ecriture du fichier
        try:
           f = open(fn, 'wb')
           f.write(str(self.view.text()))
           f.close()
           return 1
        except IOError, why:
           QMessageBox.critical(self, self.trUtf8('Save File'),
                self.trUtf8('The file <b>%1</b> could not be saved.<br>Reason: %2')
                    .arg(unicode(fn)).arg(str(why)))
           return


#-------------------------------
class itemColore(QListBoxText):
#-------------------------------
    def paint(self,p):
        p.setPen(Qt.red)
        QListBoxText.paint(self,p);
