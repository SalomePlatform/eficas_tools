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
import types,sys,os, re
import  subprocess
import traceback

from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QSplitter
    from PyQt5.QtGui import QPalette
    from PyQt5.QtCore import QProcess, QFileInfo, QTimer, Qt, QDir, QSize
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *
import time
import pdb
from datetime import date
from Extensions.i18n import tr


# Modules Eficas

import convert, generator
from Editeur        import session
from Editeur        import comploader
from Editeur        import Objecttreeitem
from desBaseWidget  import Ui_baseWidget
from monViewTexte   import ViewText 
from monWidgetCreeParam import MonWidgetCreeParam 
import browser
import readercata

DictExtensions= {"MAP" : ".map"}

    


class JDCEditor(Ui_baseWidget,QWidget):
# ----------------------------------------- #
    """
       Editeur de jdc
    """

    def __init__ (self,appli,fichier = None, jdc = None, QWParent=None, units = None, include=0 , vm=None):
    #----------------------------------------------------------------------------------------------------------#

        QWidget.__init__(self,None)
        self.i=0
        self.setupUi(self)
        self.inhibeSplitter=0
        self.widgetOptionnel=None
        self.fenetreCentraleAffichee=None
        self.dejaDansPlieTout=False
        self.afficheCommandesPliees = True
        self.listeDesListesOuvertes=set()
        self.appliEficas = appli
        self.appli       = appli  #---- attendu par IHM
        self.vm          = vm
        self.fichier     = fichier
        self.jdc         = jdc
        self.first	 = True
        self.QWParent    = QWParent
        self.couleur     = Qt.black
         
        if appli != None :
           self.salome =  self.appliEficas.salome
        else :
           self.salome=0
           print "dans JDC pas d appli ????????"

        # ces attributs sont mis a jour par definitCode appelee par newEditor
        self.code = self.appliEficas.CONFIGURATION.code

        #self.afficheListesPliees=False
        self.afficheListesPliees=True
        if self.code == "ASTER" or self.code == "monCode" : self.afficheListesPliees =True
        if self.code == 'PSEN_N1' : self.afficheListesPliees = False

        self.mode_nouv_commande=self.appliEficas.CONFIGURATION.mode_nouv_commande
        self.affiche=self.appliEficas.CONFIGURATION.affiche
        #if self.code in ['MAP','CARMELCND','PSEN'] : self.afficheCommandesPliees=False
        if self.code in ['MAP','CARMELCND'] : self.afficheCommandesPliees=False
        if self.code in ['MAP',] : 
           self.widgetTree.close()
           self.widgetTree=None
           self.appliEficas.resize(1440,self.appliEficas.height())
        else :
           self.appliEficas.resize(1800,self.appliEficas.height())

        self.version_code = session.d_env.cata

        if not hasattr ( self.appliEficas, 'readercata') or  self.appliEficas.multi==True:
           self.readercata  = readercata.READERCATA( self, self.appliEficas )
           self.appliEficas.readercata=self.readercata
           self.appliEficas.code=self.code
        else :
           self.readercata=self.appliEficas.readercata
        if self.readercata.fic_cata == None : return    #Sortie Salome
        self.titre=self.readercata.titre
        self.Ordre_Des_Commandes=self.readercata.Ordre_Des_Commandes
        self.Classement_Commandes_Ds_Arbre=self.readercata.Classement_Commandes_Ds_Arbre

        self.format =  self.appliEficas.format_fichier

        self.dict_reels={}
        self.splitterSizes =  [320,1320,320]
        self.oldSizeWidgetOptionnel = 320
        self.liste_simp_reel=[]
        self.ihm="QT"

        nameConf='configuration_'+self.code
        configuration=__import__(nameConf)
        self.CONFIGURATION = self.appliEficas.CONFIGURATION
        self.CONFIGStyle =   self.appliEficas.CONFIGStyle

        try:
          self.CONFIGURATION.generator_module
          _module = __import__(self.CONFIGURATION.generator_module)
          info = _module.entryPoint()
          generator.plugins.addEntryPoint(info)
        except:
          pass

        try:
          self.CONFIGURATION.convert_module
          print self.CONFIGURATION.convert_module
          _module = __import__(self.CONFIGURATION.convert_module)
          info = _module.entryPoint()
          convert.plugins.addEntryPoint(info)
        except :
          pass

        self.sb = None
        if hasattr(self.appliEficas,"statusBar"):
           self.sb = self.appliEficas.statusBar()

        self.fileInfo       = None
        self.lastModified   = 0

        self.modified   = False
        self.isReadOnly = False
        self.node_selected = []
        self.deplier = True
        self.message=''
        if self.code in ['Adao','MAP'] : self.afficheApresInsert=True
        else :  self.afficheApresInsert=False
        if self.code in ['TELEMAC',] : self.enteteQTree='premier'
        else : self.enteteQTree='complet'
        if self.code in ['Adao','TELEMAC'] : self.affichePlie=True
        else : self.affichePlie=False

        self.Commandes_Ordre_Catalogue =self.readercata.Commandes_Ordre_Catalogue

        #------- construction du jdc --------------

        jdc_item = None

        self.nouveau=0
        if self.fichier is not None:        #  fichier jdc fourni
            self.fileInfo = QFileInfo(self.fichier)
            self.fileInfo.setCaching(0)
            if jdc==None :
              # try :
              if 1:
                   self.jdc = self.readFile(self.fichier)
               #except :
              else :
                   print "mauvaise lecture"
            else :
               self.jdc=jdc
            if self.jdc is not None and units is not None:
               self.jdc.recorded_units=units
               self.jdc.old_recorded_units=units
        else:
            if not self.jdc:                   #  nouveau jdc
                if not include :
                   self.jdc = self._newJDC(units=units)
                else :
                   self.jdc = self._newJDCInclude(units=units)
                self.nouveau=1

        if self.jdc:
            self.jdc.appli = self
            self.jdc.lang    = self.appli.langue
            self.jdc.aReafficher=False
            txt_exception  = None
            if not jdc:
                self.jdc.analyse()
                txt_exception = self.jdc.cr.get_mess_exception()
            if txt_exception:
                self.jdc = None
                QApplication.restoreOverrideCursor()
                self.affiche_infos(tr("Erreur fatale au chargement de %s",str(fichier)),Qt.red)
                if (self.appliEficas.ssIhm == False) : QMessageBox.critical( self, tr("Erreur fatale au chargement d'un fichier"), txt_exception)
            else:
                comploader.charger_composants("QT")
                jdc_item=Objecttreeitem.make_objecttreeitem( self, "nom", self.jdc )
                if (not self.jdc.isvalid()) and (not self.nouveau) and (self.appliEficas.ssIhm == False):
                    self.viewJdcRapport()
 


        if jdc_item and self.appliEficas.ssIhm==False:
            self.tree = browser.JDCTree( jdc_item,  self )
        self.appliEficas.construitMenu()

        #############
        self.splitterSizes =  [320,1320,320]
        self.splitter.setSizes(self.splitterSizes)
        self.saveSplitterSizes()


    #-------------------#  Pour execution avec output et error dans le bash
    def runPSEN(self):
    #-------------------#
      if self.modified or self.fichier==None  : self.saveFile()
        
      #lancement avec le .bat
      path1 = os.path.abspath(os.path.join(os.path.abspath(__file__), '../','../','PSEN_Eficas','PSEN'))
      WrapperFilePath = os.path.join(path1, 'PSSEWrapper.py') 
      import subprocess
      p = subprocess.Popen(['python',WrapperFilePath])
      (out,err)=p.communicate()        
      print out
      print err

    #-------------------#  Pour execution avec output et error dans le bash
    def runPSEN_N1(self):
    #-------------------#
      #cmd = os.path.abspath(os.path.join(os.path.abspath(__file__), '../','../','PSEN_N1','run.py'))
      #cmd = "from run import runPSEN_N1; dico="+str(dico)
      
      #textePython=("python "+ cmd + " "+ str(dico))
      #print textePython
      #self._viewTextExecute( textePython,"psen_run",".sh")
      if generator.plugins.has_key('dicoImbrique'):
         self.generator=generator.plugins['dicoImbrique']()
         jdc_formate=self.generator.gener(self.jdc)
         dico=self.generator.Dico 
         from variablesPSENN1 import PSEN_N1_Variables
         mesVariables= PSEN_N1_Variables()
         mesVariables.raz()
         mesVariables.setValues(dico)
         mesVariables.imprime()
         
      from eficas_go import getJdcParameters
      from run import runPSEN_N1
      res,txt_exception=runPSEN_N1(dico)
      if res : QMessageBox.information( self, tr("fin de script run"), txt_exception)
      else  : QMessageBox.critical( self, tr("Erreur fatale script run"), txt_exception)
       
      

    #--------------------------------#
    def _newJDC( self ,units = None):
    #--------------------------------#
        """
        Initialise un nouveau JDC vierge
        """
        self.modified=1
        CONTEXT.unset_current_step()

        texte=""
        if self.code == "CARMELCND" : texte=self._newJDCCND()
        if self.code == "ZCRACKS" : texte=self._newZCRACKS()
        if self.code == "TELEMAC" : texte=self._newTELEMAC()
        if self.code == "PSEN" : texte = self._newPSEN()
        if self.code == "PSEN_N1" : texte = self._newPSEN_N1()
        #   texte=self.newTexteCND
       
        jdc=self.readercata.cata[0].JdC( procedure =texte,
                                         appli=self,
                                         cata=self.readercata.cata,
                                         cata_ord_dico=self.readercata.cata_ordonne_dico,
                                         rep_mat=self.CONFIGURATION.rep_mat
                                        )
        jdc.lang    = self.appli.langue
        if units is not None:
           jdc.recorded_units=units
           jdc.old_recorded_units=units
        ## PNPN est ce que la ligne suivante est bien utile ?
        if texte == "" :jdc.analyse()
        return jdc

    #--------------------------------#
    def _newJDCInclude( self ,units = None):
    #--------------------------------#
        """
        Initialise un nouveau JDC vierge
        """
        import Extensions.jdc_include
        JdC_aux=Extensions.jdc_include.JdC_include
        CONTEXT.unset_current_step()

        jaux=self.readercata.cata[0].JdC( procedure="",
                               appli=self,
                               cata=self.readercata.cata,
                               cata_ord_dico=self.readercata.cata_ordonne_dico,
                               rep_mat=self.CONFIGURATION.rep_mat,
                              )
        jaux.analyse()

        J=JdC_aux( procedure="",
                   appli=self,
                   cata=self.readercata.cata,
                   cata_ord_dico=self.readercata.cata_ordonne_dico,
                   jdc_pere=jaux,
                   rep_mat=self.CONFIGURATION.rep_mat,
                   )
        J.analyse()
        if units is not None:
           J.recorded_units=units
           J.old_recorded_units=units
        return J


    #-------------------------------#
    def readFile(self, fn):
    #--------------------------------#
        """
        Public slot to read the text from a file.
        @param fn filename to read from (string or QString)
        """
        fn = unicode(fn)

        # ------------------------------------------------------------------------------------
        #                         charge le JDC
        # ------------------------------------------------------------------------------------

        jdcName=os.path.basename(fn)
        # Il faut convertir le contenu du fichier en fonction du format
        if convert.plugins.has_key( self.appliEficas.format_fichier_in ):
             # Le convertisseur existe on l'utilise
             #appli = self
             p=convert.plugins[self.appliEficas.format_fichier_in]()
             p.readfile(fn)
             if p.text=="" : self.nouveau=1
             pareil,texteNew=self.verifieCHECKSUM(p.text)
             #if texteNew == ""
             if pareil == False and (self.appliEficas.ssIhm == False) :
                QMessageBox.warning( self, tr("fichier modifie"),tr("Attention! fichier change hors EFICAS"))
             p.text=texteNew
             memeVersion,texteNew=self.verifieVersionCataDuJDC(p.text)
             if memeVersion == 0 : texteNew=self.traduitCatalogue(texteNew)
             p.text=texteNew
             text=p.convert('exec',self.appliEficas)
             if not p.cr.estvide():
                self.affiche_infos("Erreur a la conversion",Qt.red)
        else :
            self.affiche_infos("Type de fichier non reconnu",Qt.red)
            if self.appliEficas.ssIhm == False:
                    QMessageBox.critical( self, tr("Type de fichier non reconnu"),
                    tr("EFICAS ne sait pas ouvrir le type de fichier %s" ,self.appliEficas.format_fichier_in))
            return None

        CONTEXT.unset_current_step()
        jdc=self.readercata.cata[0].JdC(procedure=text,
                                    appli=self,
                                    cata=self.readercata.cata,
                                    cata_ord_dico=self.readercata.cata_ordonne_dico,
                                    nom=jdcName,
                                    rep_mat=self.CONFIGURATION.rep_mat
                                   )
        # ----------------------------------------------------
        #      charge le JDC fin
        # ----------------------------------------------------
        self.modified = False

#        qApp.restoreOverrideCursor()
        if self.fileInfo!= None :
           self.lastModified = self.fileInfo.lastModified()
        else :
           self.lastModified = 1
        nouveauTitre=self.titre+"              "+str(os.path.basename(self.fichier))
        self.appliEficas.setWindowTitle(nouveauTitre)
        return jdc


    #-----------------------#
    def get_source(self,file):
    #-----------------------#

        # Il faut convertir le contenu du fichier en fonction du format
        if convert.plugins.has_key(self.format):
            # Le convertisseur existe on l'utilise
            p=convert.plugins[self.format]()
            p.readfile(file)
            text=p.convert('execnoparseur')
            if not p.cr.estvide():
                self.affiche_infos("Erreur a la conversion",Qt.red)
            return text
        else:
            # Il n'existe pas c'est une erreur
            self.affiche_infos("Type de fichier non reconnu",Qt.red)
            QMessageBox.critical( self, tr("Type de fichier non reconnu"),tr("EFICAS ne sait pas ouvrir ce type de fichier"))
            return None

    #-----------------------------------------------------------------------#
    def _viewText(self, txt, caption = "FILE_VIEWER",largeur=1200,hauteur=600):
    #--------------------------------------------------------------------#
        w = ViewText( self.QWParent,self ,caption,txt,largeur,hauteur)
        w.show()
    #

    #----------------------------------------------#
    def __generateTempFilename(self, prefix, suffix):
    #----------------------------------------------#
        import tempfile
        (fd, filename) = tempfile.mkstemp(prefix=prefix, suffix=suffix)
        os.close(fd)
        return filename
    #


    #----------------------------------------------#
    def _viewTextExecute(self, txt, prefix, suffix):
    #----------------------------------------------#
        self.w = ViewText( self.QWParent )
        self.w.setWindowTitle( "execution" )
        self.monExe=QProcess(self.w)
        pid=self.monExe.pid()
        nomFichier = self.__generateTempFilename(prefix, suffix = ".sh")
        f=open(nomFichier,'w')
        f.write(txt)
        f.close()
        if monEnvQT5 :
           self.monExe.readyReadStandardOutput.connect( self.readFromStdOut)
           self.monExe.readyReadStandardError.connect( self.readFromStdErr)
        else :
           self.connect(self.monExe, SIGNAL("readyReadStandardOutput()"), self.readFromStdOutQT4 )
           self.connect(self.monExe, SIGNAL("readyReadStandardError()"), self.readFromStdErrQT4 )
        exe='sh ' + nomFichier
        self.monExe.start(exe)
        self.monExe.closeWriteChannel()
        self.w.exec_()
        try:
          commande="rm  "+ nomFichier
          os.system(commande)
        except :
          pass

    def readFromStdErr(self):
        a=self.monExe.readAllStandardError()
        self.w.view.append(str(a.data(),len(a)))

    def readFromStdErr(self) :
        a=self.monExe.readAllStandardOutput()
        self.w.view.append(str(a.data(),len(a)))

    def readFromStdErrQT4(self):
        a=self.monExe.readAllStandardError()
        self.w.view.append(QString.fromUtf8(a.data(),len(a))) ;

    def readFromStdOutQT4(self) :
        a=self.monExe.readAllStandardOutput()
        self.w.view.append(QString.fromUtf8(a.data(),len(a))) ;
        


    #-----------------------#
    def gestionParam(self):
    #-----------------------#
        w = MonWidgetCreeParam( self)
        w.show()

    #-----------------------#
    def viewJdcSource(self):
    #-----------------------#
        f=open(self.fichier,'r')
        texteSource=f.read()
        f.close()
        self._viewText(texteSource, "JDC_SOURCE")

    #-----------------------#
    def viewJdcPy(self):
    #-----------------------#
        strSource = str( self.get_text_JDC(self.format) )
        self._viewText(strSource, "JDC_RESULTAT")

    #-----------------------#
    def viewJdcRapport(self):
    #-----------------------#
        strRapport = unicode( self.jdc.report() )
        # on ajoute les regles
        
        self._viewText(strRapport, "JDC_RAPPORT")

    #-----------------------#
    def viewJdcRegles(self):
    #-----------------------#
        if self.tree :self.tree.AppelleBuildLBRegles()


    #----------------#
    def closeIt(self):
    #----------------#
        """
        Public method called by the viewmanager to finally get rid of us.
        """
        if self.jdc:
            self.jdc.supprime()
        self.close()

    #----------------------------------------------#
    def affiche_infos(self,message,couleur=Qt.black):
    #----------------------------------------------#
        if self.sb:
           mapalette=self.sb.palette()
           mapalette.setColor( QPalette.WindowText, couleur )
           self.sb.setPalette( mapalette );
           self.sb.showMessage(message,4000)
           self.couleur=couleur

    #------------------------------#
    def affiche_alerte(self,titre,message):
    #------------------------------#
    # appele par I_MACRO_ETAPE
        QMessageBox.information( self, titre, message)

    #-----------------------------------#
    def affiche_commentaire(self,message):
    #-----------------------------------#
        self.labelCommentaire.setText(message)
        QTimer.singleShot(6000, self.rendInvisible)

    #----------------------#
    def rendInvisible(self):
    #----------------------#
        self.labelCommentaire.setText("")

    #-------------------#
    def init_modif(self):
    #-------------------#
      """
          Met l'attribut modified a 'o' : utilise par Eficas pour savoir
          si un JDC doit etre sauvegarde avant destruction ou non
      """
      self.modified = True

    #---------------------------------------#
    def chercheNoeudSelectionne(self,copie=1):
    #---------------------------------------#
      """
        appele par Cut et Copy pour positionner self.node_selected
      """
      self.node_selected=[]
      if len(self.tree.selectedItems()) == 0 : return
      self.node_selected=self.tree.selectedItems()


    #---------------------#
    def handleSupprimer(self):
    #---------------------#
      self.chercheNoeudSelectionne()
      if len(self.node_selected) == 0 : return
      self.QWParent.noeud_a_editer = []
      if self.node_selected[0]==self.tree.racine: return
      if len(self.node_selected) == 1 : self.node_selected[0].delete()
      else : self.node_selected[0].deleteMultiple(self.node_selected)

    #---------------------#
    def handleRechercher(self):
    #---------------------#
      from monRecherche import DRecherche
      monRechercheDialg=DRecherche(parent=self,fl=0)
      monRechercheDialg.show()

    #---------------------#
    def handleDeplier(self):
    #---------------------#
       if self.tree == None : return
       #self.tree.collapseAll()
       if self.deplier :
          #print "je plie"
          self.tree.expandItem(self.tree.topLevelItem(0))
          self.deplier = False
          if self.fenetreCentraleAffichee != None  :
             if hasattr(self.fenetreCentraleAffichee.node,'plieToutEtReaffiche'):
                 self.fenetreCentraleAffichee.node.plieToutEtReaffiche()
       else:
          #print "je deplie"
          self.tree.expandItem(self.tree.topLevelItem(0))
          self.deplier = True
          if self.fenetreCentraleAffichee != None  :
             if hasattr(self.fenetreCentraleAffichee.node,'deplieToutEtReaffiche'):
                 self.fenetreCentraleAffichee.node.deplieToutEtReaffiche()

    #---------------------#
    def handleEditCut(self):
    #---------------------#
      """
      Stocke dans Eficas.noeud_a_editer le noeud a couper
      """
      #print "handleEditCut"
      self.chercheNoeudSelectionne()
      self.QWParent.edit="couper"
      self.QWParent.noeud_a_editer = self.node_selected

    #-----------------------#
    def handleEditCopy(self):
    #-----------------------#
      """
      Stocke dans Eficas.noeud_a_editer le noeud a copier
      """
      self.chercheNoeudSelectionne()
      if len(self.node_selected) == 0 : return
      if len(self.node_selected) == 1 : self.node_selected[0].update_node_label_in_blue()
      else :  self.node_selected[0].update_plusieurs_node_label_in_blue(self.node_selected)
      self.QWParent.edit="copier"
      self.QWParent.noeud_a_editer = self.node_selected

    #------------------------#
    def handleEditPaste(self):
    #------------------------#
      """
      Lance la copie de l'objet place dans self.QWParent.noeud_a_editer
      Ne permet que la copie d'objets de type Commande ou MCF
      """
      self.chercheNoeudSelectionne()
      if (not(hasattr(self.QWParent,'noeud_a_editer'))) or len(self.QWParent.noeud_a_editer)==0:
          QMessageBox.information( self,
                      tr("Copie impossible"),
                      tr("Veuillez selectionner un objet a copier"))
          return
      if len(self.node_selected) != 1 :
          QMessageBox.information( self,
                      tr("Copie impossible"),
                      tr("Veuillez selectionner un seul objet : la copie se fera apres le noeud selectionne"))
          return

      if len(self.QWParent.noeud_a_editer)!=1:
         self.handleEditPasteMultiple()
         return

      noeudOuColler=self.node_selected[0]
      pos='after'
      if noeudOuColler == self.tree.racine:
         indexNoeudOuColler=0
         pos='before'
      else :
         #indexNoeudOuColler=noeudOuColler.treeParent.children.index(noeudOuColler)
         indexNoeudOuColler=self.getTreeIndex(noeudOuColler)

      try :
       noeudACopier=self.QWParent.noeud_a_editer[0]
       #indexNoeudACopier=noeudACopier.treeParent.children.index(noeudACopier)
       indexNoeudACopier=self.getTreeIndex(noeudACopier)
      except :
       QMessageBox.information( self, tr("Copie impossible"), tr("Aucun Objet n a ete copie ou coupe"))
       return

      if (self.QWParent.edit != "couper"):
        try:
           if noeudOuColler == self.tree.racine :
              child=noeudOuColler.doPastePremier(noeudACopier)
           else :
              child=noeudACopier.doPaste(noeudOuColler,pos)
           if child==None or child==0:
               QMessageBox.critical( self,tr( "Copie refusee"),tr('Eficas n a pas reussi a copier l objet'))
               self.message = ''
               self.affiche_infos("Copie refusee",Qt.red)
           if noeudACopier.treeParent.editor != noeudOuColler.treeParent.editor:
               try :
                 nom=noeudACopier.item.sd.nom
                 child.item.nomme_sd(nom)
               except :
                 pass
           return
           self.init_modif()
           child.select()
        except  :
           traceback.print_exc()
           QMessageBox.critical( self,tr( "Copie refusee"),tr('Copie refusee pour ce type d objet'))
           self.message = ''
           self.affiche_infos("Copie refusee",Qt.red)
           return

      # il faut declarer le JDCDisplay_courant modifie
      # suppression eventuelle du noeud selectionne
      # si possible on renomme l objet comme le noeud couper

      if (self.QWParent.edit == "couper"):
         #try :
         if noeudACopier.treeParent.editor != noeudOuColler.treeParent.editor:
           QMessageBox.critical( self, tr("Deplacement refuse"),tr('Deplacement refuse entre 2 fichiers. Seule la copie est autorisee '))

         #if 1:
         try :
           # indexNoeudACopier=noeudACopier.treeParent.children.index(noeudACopier)
            indexNoeudACopier=self.getTreeIndex(noeudACopier)
            noeudACopier.treeParent.item.deplaceEntite(indexNoeudACopier,indexNoeudOuColler,pos)
            noeudACopier.treeParent.build_children()

         #else:
         except:
            pass
         self.QWParent.noeud_a_editer=[]

      # on rend la copie a nouveau possible en liberant le flag edit
      self.QWParent.edit="copier"
      noeudACopier.select()

    #----------------------------------#
    def handleDeplaceMultiple(self):
    #----------------------------------#
       pass

    #----------------------------------#
    def handleEditPasteMultiple(self):
    #----------------------------------#

    # On ne garde que les niveaux "Etape"
    # On insere dans l'ordre du JDC
     listeNoeudsACouper=[]
     listeIndex=[]
     listeChild=[]
     listeItem=[]
     from InterfaceQT4 import compojdc
     noeudOuColler=self.node_selected[0]
     if not (isinstance(noeudOuColler.treeParent, compojdc.Node)):
        QMessageBox.information( self,
                  tr("Copie impossible a cet endroit",),
                  tr("Veuillez selectionner une commande, un parametre, un commentaire ou une macro"))
        return
     indexNoeudOuColler=noeudOuColler.treeParent.children.index(noeudOuColler)

     for noeud in self.QWParent.noeud_a_editer :
        if not (isinstance(noeud.treeParent, compojdc.Node)): continue
        indexInTree=noeud.treeParent.children.index(noeud)
        indice = 0
        for index in listeIndex:
            if index < indexInTree : indice = indice +1
        listeIndex.insert(indice, indexInTree)
        listeNoeudsACouper.insert(indice, noeud)

     noeudJdc=noeudOuColler.treeParent
     dejaCrees=0
     # on les cree a l'envers parcequ'on ajoute a NoeudOuColler
     listeIndex.reverse()
     for index in listeIndex:
         indexTravail=index
         if indexNoeudOuColler < index:
            indexTravail=indexTravail+dejaCrees
         noeudOuColler=noeudJdc.children[indexNoeudOuColler]
         noeud=noeudJdc.children[indexTravail]
         child=noeud.doPaste(noeudOuColler)
         listeChild.append(child)
         dejaCrees=dejaCrees+1

     self.QWParent.noeud_a_editer = []
     for i in range(len(listeIndex)):
        noeud=noeudJdc.children[indexNoeudOuColler+1+i]
        self.QWParent.noeud_a_editer.append(noeud)

     listeASupprimer=[]
     if self.QWParent.edit !="couper" : return

     for index in listeIndex:
         indexTravail=index
         if indexNoeudOuColler < index:
            indexTravail=indexTravail+(len(listeIndex))
         noeud=noeudJdc.children[indexTravail]

         listeItem.append(noeud.item)
         listeASupprimer.append(noeud)

     for i in range(len(listeChild)):
         self.tree.item.suppitem(listeItem[i])
         listeChild[i].item.update(listeItem[i])

     self.QWParent.noeud_a_editer = []


    #---------------------#
    def getFileName(self):
    #---------------------#
      return self.fichier

    #---------------------------#
    def get_file_variable(self) :
    #---------------------------#
     titre = tr("Choix d'un fichier XML")
     texte = tr("Le fichier contient une commande MODEL\n")
     texte = texte+tr('Donnez le nom du fichier XML qui contient la description des variables')
     QMessageBox.information( self, titre,tr(texte))

     fichier = QFileDialog.getOpenFileName(self.appliEficas,
                   tr('Ouvrir Fichier'),
                   self.appliEficas.CONFIGURATION.savedir,
                   tr('Wrapper Files (*.xml);;''All Files (*)'))
     return  fichier

    #--------------------------------------------------#
    def writeFile(self, fn, txt = None,formatLigne="beautifie"):
    #--------------------------------------------------#
        """
        Public slot to write the text to a file.

        @param fn filename to write to string
        @return flag indicating success
        """

        fn = unicode(fn)
       
        if txt == None :
            txt = self.get_text_JDC(self.format,formatLigne=formatLigne)
            eol = '\n'
            if len(txt) >= len(eol):
               if txt[-len(eol):] != eol:
                  txt += eol
            else:
                txt += eol
            txt=self.ajoutVersionCataDsJDC(txt)
            checksum=self.get_checksum(txt)
            txt=txt+checksum
        try:
            f = open(fn, 'wb')
            f.write(txt)
            f.close()
            return 1
        except IOError, why:
            QMessageBox.critical(self, tr('Sauvegarde du Fichier'),
                tr('Le fichier')+str(fn) + tr('n a pas pu etre sauvegarde : ') + str(why))
            return 0

    #-----------------------------------------------------------#
    def get_text_JDC(self,format,pourRun=0,formatLigne="beautifie"):
    #-----------------------------------------------------------#
      if self.code == "MAP" and not(generator.plugins.has_key(format)): format = "MAP"
      if generator.plugins.has_key(format):
         
         # Le generateur existe on l'utilise
         self.generator=generator.plugins[format]()
         try :
            jdc_formate=self.generator.gener(self.jdc,format=formatLigne,config=self.appliEficas.CONFIGURATION)
            if pourRun : jdc_formate=self.generator.textePourRun
         except ValueError,e:
            QMessageBox.critical(self, tr("Erreur a la generation"),str(e))
         if not self.generator.cr.estvide():
            self.affiche_infos(tr("Erreur a la generation"),Qt.red)
            QMessageBox.critical( self, tr("Erreur a la generation"),tr("EFICAS ne sait pas convertir ce JDC"))
            return ""
         else:
            return jdc_formate
      else:
         # Il n'existe pas c'est une erreur
         self.affiche_infos(tr("Format %s non reconnu" , self.format),Qt.red)
         QMessageBox.critical( self, "Format  non reconnu" ,tr("EFICAS ne sait pas convertir le JDC selon le format "+ self.format))
         return ""

    #------------#
    def run(self):
    #------------#
      print "kkkkkkkkkk"
      fonction="run"+self.code
      print fonction
      if fonction in JDCEditor.__dict__.keys(): apply(JDCEditor.__dict__[fonction],(self,))

    #------------#
    def saveRun(self):
    #------------#
      fonction="saveRun"+self.code
      if fonction in JDCEditor.__dict__.keys(): apply(JDCEditor.__dict__[fonction],(self,))

    #---------------#
    def runMAP(self):
    #---------------#

      if not(self.jdc.isvalid()):
         QMessageBox.critical( self, tr( "Execution impossible "),tr("le JDC doit etre valide pour une execution MAP"))
         return
      if len(self.jdc.etapes) != 1 :
         QMessageBox.critical( self, tr("Execution impossible "),tr("le JDC doit contenir un et un seul composant"))
         return
      if self.modified or self.fichier==None  :
         self.fichierMapInput = self.__generateTempFilename(prefix = "map_run", suffix = ".map")
         texte=self.get_text_JDC("MAP")
         self.writeFile( self.fichierMapInput, txt = texte)
      else :
         self.fichierMapInput=self.fichier
      composant=self.jdc.etapes[0].nom.lower()[0:-5]


      # :TRICKY: to determine if a component requires SALOME, loads the component from Eficas catalog
      # then instantiate corresponding class and call getUseSalome() method
      try:
          from mapengine.spec import factory
          mapComponent = factory.new(composant)[0]

          command = "map"
          if mapComponent.getUseSalome():
              command += " -r sappli"
          textePython=(command + " run -n "+composant +" -i "+self.fichierMapInput)

          #textePython="ls -l"
          self._viewTextExecute( textePython,"map_run",".sh")
          #try:
          #  commande="rm  "+self.fichierMapInput
          #   os.system(commande)
          #except :
          #   pass
      except Exception, e:
          print traceback.print_exc()

    #-------------------#
    def runZCRACKS(self):
    #-------------------#
      if not(self.jdc.isvalid()):
         QMessageBox.critical( self, tr( "Execution impossible "),tr("le JDC doit etre valide pour une execution "))
         return
      if self.modified or self.fichier==None  :
      #if 1:
         self.fichierZcracksInput = self.__generateTempFilename(prefix = "zcracks_run", suffix = ".z7p")
         texte=self.get_text_JDC("ZCRACKS",pourRun=1)
         self.writeFile( self.fichierZcracksInput, txt = texte)
      else :
         self.fichierZcracksInput=self.fichier
      try :
          #commande ="Zrun -zp "
          commande="more "
          textePython=(commande + self.fichierZcracksInput)
          self._viewTextExecute( textePython,"run_zcracks",".sh")
      except Exception, e:
          print traceback.print_exc()

    #-------------------#
    def runCARMELCND(self):
    #-------------------#
      #if not(self.jdc.isvalid()):
      #   QMessageBox.critical( self, tr( "Execution impossible "),tr("le JDC doit etre valide pour une execution "))
      #   return
      if self.modified or self.fichier==None  :
         QMessageBox.critical( self, tr( "Execution impossible "),tr("Sauvegarder SVP avant l'execution "))
         return
      if not hasattr(self,'generator'): texte=self.get_text_JDC(self.format)
      from PrepareRunCarmel import prepareRunCarmel
      fichierGenerique=os.path.basename(self.fichier).split(".")[0]
      repMed=os.path.dirname(self.fichier)
      repExeCarmel=self.generator.get_repExeCarmel()
      textePython=prepareRunCarmel(repExeCarmel,repMed,fichierGenerique)
      nomFichier = self.__generateTempFilename("carmel_run", suffix = ".sh")
      f=open(nomFichier,'w')
      f.write(textePython)
      f.close()
      commande="xterm -e sh "+nomFichier +"\n"
      os.system(commande)
      #try :
      #    self._viewTextExecute( textePython,"carmel_run",".sh")
      #except Exception, e:
      #    print traceback.print_exc()

    #-------------------#
    def runCarmelCS(self):
    #-------------------#
      try :
          commande="runSession pilotyacsCS.py"
          os.system(commande)
      except Exception, e:
          print traceback.print_exc()

    #-----------------------------------------------------#
    def determineNomFichier(self,path,extension):
    #-----------------------------------------------------#
      if DictExtensions.has_key(self.appli.code) :
         chaine1="JDC (*"+DictExtensions[self.appli.code]+");;"
         extensions= tr(chaine1+ "All Files (*)")
      else :
         extensions= tr("JDC (*.comm);;" "All Files (*)")

      if self.appli.code == "MAP" :
         extensions = extensions + ";; Run (*.input);;"

      fn = QFileDialog.getSaveFileName( self,
             tr("sauvegarde"), path,
             extensions,None,
             QFileDialog.DontConfirmOverwrite)
      if fn == None : return (0, None)
      if monEnvQT5 :  fn=fn[0]
      if fn=='': return (0, None)

      ext = QFileInfo(fn).suffix()
      if ext == '': fn+=extension

      if QFileInfo(fn).exists():
           if monEnvQT5 :
             msgBox = QMessageBox(self)
             msgBox.setWindowTitle(tr("Sauvegarde du Fichier"))
             msgBox.setText(tr("Le fichier <b>%s</b> existe deja.", unicode(fn)))
             msgBox.addButton(tr("&Ecraser"),0)
             msgBox.addButton(tr("&Abandonner"),1)
             abort=msgBox.exec_()
           else :
             abort = QMessageBox.warning(self,
                   tr("Sauvegarde du Fichier"),
                   tr("Le fichier <b>%s</b> existe deja.",str(fn)),
                   tr("&Ecraser"),
                   tr("&Abandonner"))
           if abort == 1 :  return (0, "")
      return (1,fn)

    #-----------------#
    def saveRunMAP(self):
    #-----------------#
        extension=".input"
        if not(self.jdc.isvalid()):
           QMessageBox.critical( self, tr( "Sauvegarde de l'input impossible "),
                                tr("Un JdC valide est necessaire pour creer un .input")
                                 )
           return
        try :
          composant=self.jdc.etapes[0].nom.lower()[0:-5]
        except :
           QMessageBox.critical( self, tr( "Sauvegarde de l'input impossible "),
                                tr("Choix du composant obligatoire")
                                 )
           return
        if hasattr(self.CONFIGURATION, "savedir"): path=self.CONFIGURATION.savedir
        else : path='C:/'

        monNomFichier=""
        if self.fichier is not None and self.fichier != "" :
             maBase=str(QFileInfo(self.fichier).baseName())+".input"
             monPath=str(QFileInfo(self.fichier).absolutePath())
             monNomFichier=os.path.join(monPath,maBase)
        elif hasattr(self,'monNomFichierInput'):
            monNomFichier=self.monNomFichierInput


        monDialog=QFileDialog(self.appliEficas)
        monDialog.setDirectory (path)
        monDialog.setWindowTitle ("Save")

        for c in monDialog.children():
            if isinstance(c,QDialogButtonBox):
               for b in c.children():
                  if isinstance(b,QPushButton):
                     avant=b.text()
                     if (not monEnvQT5) and avant.toLatin1()=="&Open": b.setText("Save")
                     if monEnvQT5 and avant=="&Open": b.setText("Save")
        if monEnvQT5 :
           mesFiltres= "input Map (*.input);;All Files (*)"
        else :
           mesFiltres=QStringList()
           mesFiltres << "input Map (*.input)" << "All Files (*)"
        monDialog.setNameFilters(mesFiltres)
        if monNomFichier!="" : monDialog.selectFile(monNomFichier)
        BOk=monDialog.exec_()
        if BOk==0: return
        if monEnvQT5 : fn=str(monDialog.selectedFiles()[0])
        else : fn=str(monDialog.selectedFiles()[0].toLatin1())
        if fn == "" or fn == None : return
        if not fn.endswith(".input"):
            fn += ".input"
        self.monNomFichierInput=fn

        if not hasattr(self, 'fichierMapInput') or not self.fichierMapInput or not os.path.exists(self.fichierMapInput):
            self.fichierMapInput = self.__generateTempFilename(prefix = "map_run", suffix = ".map")
            texte=self.get_text_JDC("MAP")
            self.writeFile( self.fichierMapInput, txt = texte)

        cmd = ("map gen -t dat -n " + composant + " -i " + self.fichierMapInput + " -o " + fn)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        (output, err) = p.communicate()


    #-----------------#
    def saveRunPSEN(self):
    #-----------------#
        print "saveRunPSEN"
        self.saveFile()
        return
        if not(self.jdc.isvalid()):
           QMessageBox.critical( self, tr( "Sauvegarde de l'input impossible "),
                                tr("Un JdC valide est necessaire pour creer un .input")
                                 )
           return

        print generator.plugins.has_key(self.format)
        if generator.plugins.has_key(self.format):
             # Le generateur existe on l'utilise
             self.generator=generator.plugins[self.format]()
             try :
                self.generator.gener(self.jdc)
                self.generator.writeDefault('')
             except ValueError,e:
                QMessageBox.critical(self, tr("Erreur a la generation"),str(e))
             if not self.generator.cr.estvide():
                self.affiche_infos(tr("Erreur a la generation"),Qt.red)
                QMessageBox.critical( self, tr("Erreur a la generation"),tr("EFICAS ne sait pas convertir ce JDC"))
                return ""
        else:
             # Il n'existe pas c'est une erreur
             self.affiche_infos(tr("Format %s non reconnu" , self.format),Qt.red)
             QMessageBox.critical( self, "Format  non reconnu" ,tr("EFICAS ne sait pas convertir le JDC selon le format "+ self.format))
             return ""
        print "HELLO"
        



    #-----------------------------------------#
    def cherche_Groupes(self):
    #-----------------------------------------#
        listeMA,listeNO=self.get_text_JDC("GroupMA")
        return listeMA,listeNO

    #-----------------------------------------#
    def cherche_Dico(self):
    #-----------------------------------------#
        dicoCourant={}
        format =  self.appliEficas.format_fichier
        if generator.plugins.has_key(format):
           # Le generateur existe on l'utilise
           self.generator=generator.plugins[format]()
           jdc_formate=self.generator.gener(self.jdc,format='beautifie',config=self.appliEficas.CONFIGURATION)
           dicoCourant=self.generator.dico
        return dicoCourant

         

    #-----------------------------------------#
    def handleAjoutGroup(self,listeGroup):
    #-----------------------------------------#
        try :
        #if 1:
           from ajoutGroupe import handleAjoutGroupFiltre
           #print listeGroup
           handleAjoutGroupFiltre(self,listeGroup)
           #print "apres handleAjoutGroupFiltre"
        except :
        #else :
           pass

    #-----------------------------------------------------------------#
    def saveFile(self, path = None, saveas= 0,formatLigne="beautifie"):
    #-----------------------------------------------------------------#
        """
        Public slot to save the text to a file.

        @param path directory to save the file in (string or QString)
        @return tuple of two values (boolean, string) giving a success indicator and
            the name of the saved file
        """

        self.modified=1
        if not self.modified and not saveas:
            return (0, None)      # do nothing if text wasn't changed

        extension='.py'
        if DictExtensions.has_key(self.appli.code) :
           extension=DictExtensions[self.appli.code]
        else :
           extension='.comm'

        newName = None
        fn = self.fichier
        if self.fichier is None or saveas:
          if path is None: path=self.CONFIGURATION.savedir
          bOK, fn=self.determineNomFichier(path,extension)
          if bOK == 0 : return (0, None)
          if fn == None : return (0, None)
          if fn== '' : return (0, None)

          ulfile = os.path.abspath(unicode(fn))
          self.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
          fn = unicode(QDir.toNativeSeparators(fn))
          newName = fn


        if not (self.writeFile(fn,formatLigne=formatLigne)): return (0, None)
        self.fichier = fn
        self.modified  = False
        if self.fileInfo is None or saveas:
           self.fileInfo = QFileInfo(self.fichier)
           self.fileInfo.setCaching(0)
        self.lastModified = self.fileInfo.lastModified()
        if newName is not None:
           self.appliEficas.addToRecentList(newName)
           self.tree.racine.item.getObject().nom=os.path.basename(newName)
           self.tree.racine.update_node_label()

        if self.jdc.isvalid() != 0 and hasattr(self.generator, "writeDefault"):
            self.generator.writeDefault(fn)
        if self.code=="TELEMAC" and hasattr(self.generator, "writeDefault"):
            self.generator.writeDefault(fn)

        if self.salome :
               self.appliEficas.addJdcInSalome( self.fichier)
        self.modified = 0
        nouveauTitre=self.titre+"              "+str(os.path.basename(self.fichier))
        self.appliEficas.setWindowTitle(nouveauTitre)

        return (1, self.fichier)
#

    #----------------------------------------------#
    def sauveLigneFile(self):
    #----------------------------------------------#
        self.modified=1
        return self.saveFile(formatLigne="Ligne")


    #----------------------------------------------#
    def saveFileAs(self, path = None,fileName=None):
    #----------------------------------------------#
        """
        Public slot to save a file with a new name.

        @param path directory to save the file in (string or QString)
        @return tuple of two values (boolean, string) giving a success indicator and
            the name of the saved file
        """
        if fileName != None :
           self.fichier = fileName
           return self.saveFile()
        return self.saveFile(path,1,"beautifie")



    #---------------------------------------------#
    def get_file(self,unite=None,fic_origine = ''):
    #---------------------------------------------#
    # appele par I_JDC
        ulfile  = None
        jdcText = ""

        titre  = ""

        if unite :
            titre = tr("Choix unite %d ", unite)
            texte = tr("Le fichier %s contient une commande INCLUDE \n",  str(fic_origine)) +"\n"
            texte = texte+ tr("Donnez le nom du fichier correspondant a l unite logique ") + repr(unite)
            labeltexte = tr('Fichier pour unite ') + repr( unite)
        else:
            titre = tr("Choix d'un fichier de poursuite")
            texte = tr("Le fichier %s contient une commande POURSUITE\n", fic_origine)
            texte = texte+tr('Donnez le nom du fichier dont vous \n voulez faire une poursuite')

        QMessageBox.information( self, titre,texte)
        fn = QFileDialog.getOpenFileName(self.appliEficas,
                   titre,
                   self.appliEficas.CONFIGURATION.savedir)

        # ce retour est impose par le get_file d'I_JDC
        if fn== '' : return None," "
        if not fn : return (0, " ")
        if monEnvQT5 :  fn=fn[0]

        ulfile = os.path.abspath(unicode(fn))
        self.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]

        # On utilise le convertisseur defini par format_fichier
        source=self.get_source(ulfile)
        if source:
            # On a reussia convertir le fichier self.ulfile
            jdcText = source
        else:
            # Une erreur a ete rencontree
            jdcText = ''
        return ulfile, jdcText

    #-------------------------------#
    def updateJdc(self, itemApres,texte):
    #--------------------------------#
        monItem=itemApres
        etape=monItem.item.object

        CONTEXT.set_current_step(etape)
        etape.build_includeInclude(texte)
        self.tree.racine.build_children()

    #-------------------------------------#
    def deleteMC(self,etape,MCFils):
    #-------------------------------------#
        monMC=etape.get_child(MCFils,restreint="oui")
        if monMC != None : print etape.suppentite(monMC)


    #-------------------------------------#
    def ajoutMC(self,etape,MCFils,valeurs):
    #-------------------------------------#
        print "je passe dans ajoutMC" 
        monMC=etape.get_child(MCFils,restreint="oui")
        if monMC== None : monMC= etape.addentite(MCFils)
        monMC.valeur=valeurs
        monMC.val=valeurs

    #-------------------------------------#
    def changeIntoMC(self,etape,MCFils,valeurs):
    #-------------------------------------#
        print "je passe dans changeIntoMC" 
        monMC=etape.get_child(MCFils,restreint="oui")
        if monMC== None : monMC= etape.addentite(MCFils)
        monMC.definition.into=valeurs

    #-------------------------------------#
    def changeIntoMCandSet(self,etape,MCFils,into,valeurs):
    #-------------------------------------#
        monMC=etape.get_child(MCFils,restreint="oui")
        if monMC== None : monMC= etape.addentite(MCFils)
        monMC.definition.into=into
        monMC.valeur=valeurs
        monMC.val=valeurs
        monMC.state='changed'
        monMC.isvalid() 

    #-------------------------------------#
    def ajoutVersionCataDsJDC(self,txt):
    #-------------------------------------#
        if not hasattr(self.readercata.cata[0],'VERSION_CATALOGUE'): return txt
        ligneVersion="#VERSION_CATALOGUE:"+self.readercata.cata[0].VERSION_CATALOGUE+":FIN VERSION_CATALOGUE\n"
        texte=txt+ligneVersion
        return texte

    #-------------------------------------#
    def verifieVersionCataDuJDC(self,text):
    #-------------------------------------#
        memeVersion=False
        indexDeb=text.find("#VERSION_CATALOGUE:")
        indexFin=text.find(":FIN VERSION_CATALOGUE")
        if indexDeb < 0 :
           self.versionCataDuJDC="sans"
           textJDC=text
        else :
           self.versionCataDuJDC=text[indexDeb+19:indexFin]
           textJDC=text[0:indexDeb]+text[indexFin+23:-1]

        self.versionCata="sans"
        if hasattr(self.readercata.cata[0],'VERSION_CATALOGUE'): self.versionCata=self.readercata.cata[0].VERSION_CATALOGUE

        if self.versionCata==self.versionCataDuJDC : memeVersion=True
        return memeVersion,textJDC

    #-------------------------------#
    def traduitCatalogue(self,texte):
    #-------------------------------#
        nomTraducteur="traduit"+self.readercata.code+self.versionCataDuJDC+"To"+self.versionCata
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../Traducteur")))
        try :
            traducteur=__import__(nomTraducteur)
            monTraducteur=traducteur.MonTraducteur(texte)
            nouveauTexte=monTraducteur.traduit()
            return nouveauTexte
        except :
            return texte


    #------------------------------#
    def verifieCHECKSUM(self,text):
    #------------------------------#
        indexDeb=text.find("#CHECKSUM:")
        if indexDeb < 0 :
           return 1, text
        indexFin=text.find(":FIN CHECKSUM")
        checkAvant=text[indexDeb:indexFin+13]
        textJDC=text[0:indexDeb]+text[indexFin+13:-1]
        checksum=self.get_checksum(textJDC)
        pareil=(checkAvant==checksum)
        return pareil, textJDC

    #---------------------------#
    def get_checksum(self,texte):
    #---------------------------#
        newtexte=texte.replace('"','\\"')
        commande='echo "'+newtexte+'"|md5sum'
        a=os.popen(commande)
        checksum=a.read()
        a.close()
        ligne="#CHECKSUM:"+checksum[0:-1]+":FIN CHECKSUM"
        return ligne


    #---------------------------#
    def _newTELEMAC(self):
    #---------------------------#
        texte="INITIALIZATION();BOUNDARY_CONDITIONS();GENERAL_PARAMETERS();PHYSICAL_PARAMETERS();NUMERICAL_PARAMETERS();"
        #texte=""
        return texte

    #---------------------------#
    def _newPSEN(self):
    #---------------------------#
        texte="DIRECTORY() ; PSSE_PARAMETERS() ; SIMULATION() ; sansnom=DISTRIBUTION() ; sansnom=DISTRIBUTION() ; CORRELATION() ;"
        #texte=""
        return texte

    #---------------------------#
    def _newPSEN_N1(self):
    #---------------------------#
        texte="CASE_SELECTION() ; CONTINGENCY_OPTIONS() ; OUTPUT_OPTIONS() ; "
        #texte=""
        return texte

    #---------------------------#

    #---------------------------#
    def _newZCRACKS(self):
    #---------------------------#
        texte="MAILLAGES();REMESHING();"
        return texte

    #---------------------------#
    def _newJDCCND(self):
    #---------------------------#
      extensions=tr('Fichiers Med (*.med);;''Tous les Fichiers (*)')
      
      #if self.salome == 0 :
      QMessageBox.information( self,
                      tr("Fichier Med"),
                      tr("Veuillez selectionner un fichier Med"))
      QSfichier = QFileDialog.getOpenFileName(self.appliEficas,
                        caption='Fichier Med',
                        filter=extensions)
      if monEnvQT5 : QSfichier=QSfichier[0]
      self.fichierMED=QSfichier
      from acquiertGroupes import getGroupes
      erreur,self.listeGroupes,self.nomMaillage,self.dicoCoord=getGroupes(self.fichierMED)
      if erreur != "" : print "a traiter"
      texteComm="COMMENTAIRE(u'Cree - fichier : "+self.fichierMED +" - Nom Maillage : "+self.nomMaillage+"');\nPARAMETRES()\n"
      texteSources=""
      texteCond=""
      texteNoCond=""
      texteVcut=""
      texteZs=""
      for groupe in self.listeGroupes :
          if groupe[0:8]=='CURRENT_': 
             texteSources +=groupe[8:]+"=SOURCE("
             texteSources +="VecteurDirecteur=(1.0,2.0,3.0,),);\n"
          if groupe[0:5]=='COND_':    texteCond    +=groupe[5:]+"=CONDUCTEUR();\n"
          if groupe[0:7]=='NOCOND_':  texteNoCond  +=groupe[7:]+"=NOCOND();\n"
          if groupe[0:5]=='VCUT_':    texteVcut    +='V_'+groupe[5:]+"=VCUT();\n"
          if groupe[0:3]=='ZS_':      texteZs      +=groupe[3:]+"=ZS();\n"
      texte=texteComm+texteSources+texteCond+texteNoCond+texteVcut+texteZs
      self.newTexteCND=texte
      self.modified=1
      return texte


    #---------------------------#
    def  BoutonFileSelected(self):
    #---------------------------#

      QSfichier=self.openfile.selectedFiles()[0]
      self.fichierMED=str(QSfichier)
      from acquiertGroupes import getGroupes
      erreur,self.listeGroupes,self.nomMaillage=getGroupes(self.fichierMED)
      if erreur != "" : print "a traiter"

    #-----------------------------
    def BoutonSalomePressed(self):
    #----------------------------
      Msg,self.listeGroupes=self.appliEficas.ChercheGrpMailleInSalome()
      self.fichierMED="A_partir_de_SMESH"
      self.nomMaillage="A_partir_de_SMESH"
      self.openfile.close()

    #-------------------------------------
    def saveSplitterSizes(self,event=None):
    #------------------------------------
      if self.inhibeSplitter : return
      if not hasattr(self,'splitter') : return
      if self.splitterSizes[2] != 0 : self.oldSizeWidgetOptionnel = self.splitterSizes[2]
      #print  self.splitterSizes
      #print self.splitter.sizes()
      # PNPNPNPN parfoir self.splitter.sizes() a une longueur de 4...
      nbAGarder=len(self.splitter.sizes())
      if nbAGarder > 3 : nbAGarder=3
      for i in range(nbAGarder):
         self.splitterSizes[i] = self.splitter.sizes()[i]
         self.splitter.widget(i).resizeEvent=self.saveSplitterSizes
      #print self.splitter.sizes()


    #-----------------------------------------
    def restoreSplitterSizes(self,nbWigdet=3):
    #----------------------------------------
      self.inhibeSplitter = 1
      self.i+=1
      if not(hasattr(self,'splitter')) : return
      newSizes=self.splitterSizes[:nbWigdet]
      self.splitter.setSizes(newSizes)
      self.inhibeSplitter = 0
   
    #------------------------
    def fermeOptionnel(self):
    #------------------------
      if self.widgetOptionnel == None : return

      self.inhibeSplitter=1
      self.splitterSizes[1] = self.splitterSizes[1] + self.splitterSizes[2]
      if self.splitterSizes[2]!=0 : self.oldSizeWidgetOptionnel = self.splitterSizes[2]
      self.splitterSizes[2]=0

      self.widgetOptionnel.setParent(None)
      self.widgetOptionnel.close()
      self.widgetOptionnel.deleteLater()
      self.widgetOptionnel=None
      self.inhibeSplitter=0
      self.restoreSplitterSizes(2)
      
    #------------------------
    def ajoutOptionnel(self):
    #------------------------
      #print "ajoutOptionnel"
      #print self.splitterSizes
      self.splitterSizes[2] = self.oldSizeWidgetOptionnel
      self.splitterSizes[1] = self.splitterSizes[1] - self.splitterSizes[2]
      self.inhibeSplitter=0
      self.restoreSplitterSizes(3)


    #-----------------------------
    def getTreeIndex(self,noeud):
    #----------------------------
      indexNoeud=-1
      if noeud in noeud.treeParent.children :
          indexNoeud=noeud.treeParent.children.index(noeud)
      else :
          if hasattr(noeud,'vraiParent') :
              noeudVrai = noeud
              noeudVraiParent = noeud.vraiParent
              while noeudVraiParent != noeud.treeParent and hasattr(noeudVraiParent,'vraiParent') :
                  noeudVrai = noeudVraiParent
                  noeudVraiParent = noeudVraiParent.vraiParent
                  pass
              if noeudVraiParent == noeud.treeParent :
                  indexNoeud=noeud.treeParent.children.index(noeudVrai)
                  pass
              pass
          pass
      return indexNoeud

if __name__ == "__main__":
    self.code='ASTER'
    name='prefs_'+prefs.code
    prefsCode=__import__(name)


    if hasattr(prefsCode,'encoding'):
       # Hack pour changer le codage par defaut des strings
       import sys
       reload(sys)
       sys.setdefaultencoding(prefs.encoding)
       del sys.setdefaultencoding
       # Fin hack

#    code=options.code
#
    app = QApplication(sys.argv)
    mw = JDCEditor(None,'azAster.comm')
    app.setMainWidget(mw)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    mw.show()

    res = app.exec_loop()
    sys.exit(res)
