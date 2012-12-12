# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
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
import traceback
from PyQt4 import *
from PyQt4.QtGui  import *
from PyQt4.QtCore import *
import time
from datetime import date


# Modules Eficas

import convert, generator
from Editeur     import session
from Editeur     import comploader
from Editeur     import Objecttreeitem
import browser
import readercata
import qtCommun

DictExtensions= {"MAP" : ".map"}



class JDCEditor(QSplitter):
# -------------------------- #
    """
       Editeur de jdc
    """        

    def __init__ (self,appli,fichier = None, jdc = None, QWParent=None, units = None, include=0 , vm=None):          
    #----------------------------------------------------------------------------------------------------------#

        QSplitter.__init__(self, QWParent)
	self.appliEficas = appli
	self.appli       = appli  #---- attendu par IHM
        self.vm          = vm
        self.fichier     = fichier
        self.jdc         = jdc
        self.QWParent    = QWParent

        if appli != None :
           self.salome =  self.appliEficas.salome
        else :
           self.salome=0
           print "dans JDC pas d appli ????????"

        # ces attributs sont mis a jour par definitCode appelee par newEditor
        self.code = self.appliEficas.CONFIGURATION.code
        self.version_code = session.d_env.cata

        if not hasattr ( self.appliEficas, 'readercata') or  self.appliEficas.multi==True:
           self.readercata  = readercata.READERCATA( self, self.appliEficas )
           self.appliEficas.readercata=self.readercata
        else :
           self.readercata=self.appliEficas.readercata
        if self.readercata.fic_cata == None : return    #Sortie Salome

        self.format =  self.appliEficas.format_fichier
        self.titre=self.appliEficas.VERSION_EFICAS + ' pour '+ self.code

        self.dict_reels={}
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
        self.tree = None
        self.node_selected = []
        self.deplier = True
        self.message=''
        
        self.Commandes_Ordre_Catalogue =self.readercata.Commandes_Ordre_Catalogue
        
        #------- construction du jdc --------------

        jdc_item = None
        self.mode_nouv_commande=self.readercata.mode_nouv_commande
                        
        self.nouveau=0
        if self.fichier is not None:        #  fichier jdc fourni
            self.fileInfo = QFileInfo(self.fichier)
            self.fileInfo.setCaching(0)
            if jdc==None :
               self.jdc = self.readFile(self.fichier)
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
            self.jdc.lang    = self.appli.CONFIGURATION.lang
            txt_exception  = None
            if not jdc:
                self.jdc.analyse()            
                txt_exception = self.jdc.cr.get_mess_exception()            
            if txt_exception:
                self.jdc = None
                qApp.restoreOverrideCursor()
                self.affiche_infos("Erreur fatale au chargement de %s" %fichier,Qt.red)                
                QMessageBox.critical( self, "Erreur fatale au chargement d'un fichier", txt_exception)                
            else:
                comploader.charger_composants("QT")
                jdc_item=Objecttreeitem.make_objecttreeitem( self, "nom", self.jdc )

                if (not self.jdc.isvalid()) and (not self.nouveau) :
                    self.viewJdcRapport()
        if jdc_item:                        
            self.tree = browser.JDCTree( jdc_item,  self )
        self.appliEficas.construitMenu()
        
    #--------------------------------#
    def _newJDC( self ,units = None):        
    #--------------------------------#
        """
        Initialise un nouveau JDC vierge
        """
        CONTEXT.unset_current_step()        

        jdc=self.readercata.cata[0].JdC( procedure ="",
                                         appli=self,
                                         cata=self.readercata.cata,
                                         cata_ord_dico=self.readercata.cata_ordonne_dico,
                                         rep_mat=self.CONFIGURATION.rep_mat
                                        )                         
        if units is not None:
           jdc.recorded_units=units
           jdc.old_recorded_units=units
        jdc.analyse()        
        jdc.lang    = self.appli.CONFIGURATION.lang
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
             if pareil == False and (self.QWParent != None) :
                QMessageBox.warning( self, "fichier modifie","Attention! fichier change hors EFICAS")
             p.text=texteNew
             memeVersion,texteNew=self.verifieVersionCataDuJDC(p.text)
             if memeVersion == 0 : texteNew=self.traduitCatalogue(texteNew)
             p.text=texteNew
             text=p.convert('exec',self.appliEficas)
             if not p.cr.estvide():                 
                self.affiche_infos("Erreur a la conversion",Qt.red)
        else :
            self.affiche_infos("Type de fichier non reconnu",Qt.red)
            QMessageBox.critical( self, "Type de fichier non reconnu","EFICAS ne sait pas ouvrir le type de fichier %s" % self.appliEficas.format_fichier_in)            
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
            QMessageBox.critical( self, "Type de fichier non reconnu","EFICAS ne sait pas ouvrir ce type de fichier")            
            return None

    #----------------------------------------------#
    def _viewText(self, txt, caption = "FILE_VIEWER"):    
    #----------------------------------------------#
        w = qtCommun.ViewText( self.QWParent )
        w.setWindowTitle( caption )
        w.setText(txt)
        w.show()

    #--------------------------------#
    def _viewTextExecute(self, txt):    
    #--------------------------------#
        self.w = qtCommun.ViewText( self.QWParent )
        self.w.setWindowTitle( "execution" )
        self.monExe=QProcess(self.w)
        pid=self.monExe.pid()
        nomFichier='/tmp/map_'+str(pid)+'.py'
        f=open(nomFichier,'w')
        f.write(txt)
        f.close()
        self.connect(self.monExe, SIGNAL("readyReadStandardOutput()"), self.readFromStdOut )
        self.connect(self.monExe, SIGNAL("readyReadStandardError()"), self.readFromStdErr )
        exe='python ' + nomFichier
        self.monExe.start(exe)
        self.monExe.closeWriteChannel()
        self.w.show()


    def readFromStdErr(self):
        a=self.monExe.readAllStandardError()
        self.w.view.append(QString.fromUtf8(a.data(),len(a))) ;

    def readFromStdOut(self) :
        a=self.monExe.readAllStandardOutput()
        self.w.view.append(QString.fromUtf8(a.data(),len(a))) ;


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
        self._viewText(strRapport, "JDC_RAPPORT")        
        
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
           from PyQt4.QtGui import QPalette
	   mapalette.setColor( QPalette.WindowText, couleur )
	   self.sb.setPalette( mapalette );
           self.sb.showMessage(QString.fromUtf8(message))#,2000)
           #if couleur==Qt.red :
           #   QToolTip.showText(QPoint(0,0),'tttttttttttt',self.sb)

    #------------------------------#
    def affiche_alerte(self,titre,message):
    #------------------------------#
    # appele par I_MACRO_ETAPE
        QMessageBox.information( self, titre, message)

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
    
    #---------------------#
    def handleDeplier(self):
    #---------------------#
       if self.tree == None : return
       self.deplier = False
       self.tree.collapseAll()
       self.tree.expandItem(self.tree.topLevelItem(0))
    
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
                      "Copie impossible",
                      "Veuillez selectionner un objet � copier")
          return
      if len(self.node_selected) != 1 : 
          QMessageBox.information( self, 
                      "Copie impossible",
                      "Veuillez selectionner un seul objet : la copie se fera apr�s le noeud selectionn�")
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
         indexNoeudOuColler=noeudOuColler.treeParent.children.index(noeudOuColler)

      try :
       noeudACopier=self.QWParent.noeud_a_editer[0]
       indexNoeudACopier=noeudACopier.treeParent.children.index(noeudACopier)
      except :
       QMessageBox.information( self, "Copie impossible", "Aucun Objet n a ete copie ou coupe ")
       return

      if (self.QWParent.edit != "couper"):
        try:
           child=noeudACopier.doPaste(noeudOuColler,pos)
           if child==None or child==0:
               QMessageBox.critical( self, "Copie refusee",'Eficas n a pas r�ussi � copier l objet')
               self.message = ''
               self.affiche_infos("Copie refusee",Qt.red)
           return
           self.init_modif()
           child.select()
        except  :
           traceback.print_exc()
           QMessageBox.critical( self, "Copie refusee",'Copie refusee pour ce type d objet')
           self.message = ''
           self.affiche_infos("Copie refusee",Qt.red)
           return
    
      # il faut declarer le JDCDisplay_courant modifie
      # suppression eventuelle du noeud selectionne
      # si possible on renomme l objet comme le noeud couper

      if (self.QWParent.edit == "couper"):
         #try :
         if noeudACopier.treeParent != noeudOuColler.treeParent:
           QMessageBox.critical( self, "Deplacement refuse",'Deplacement refuse entre 2 fichiers. Seule la copie est autoris�e ')

         #if 1:
         try :
            indexNoeudACopier=noeudACopier.treeParent.children.index(noeudACopier)
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
                  "Copie impossible a cet endroit",
                  "Veuillez selectionner une commande, un parametre, un commentaire ou une macro")
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
     # on les cree � l'envers parcequ'on ajoute � NoeudOuColler
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
     titre = "Choix d'un fichier XML"
     texte = "Le fichier contient une commande MODEL\n"
     texte = texte+'Donnez le nom du fichier XML qui contient la description des variables'
     QMessageBox.information( self, titre,texte)
                                        
     fichier = QFileDialog.getOpenFileName(self.appliEficas,
                   self.appliEficas.trUtf8('Ouvrir Fichier'),
                   self.appliEficas.CONFIGURATION.savedir,
                   self.appliEficas.trUtf8('Wrapper Files (*.xml);;''All Files (*)'))
     return  fichier
      
    #----------------------------------#
    def writeFile(self, fn, txt = None):
    #----------------------------------#
        """
        Public slot to write the text to a file.
        
        @param fn filename to write to (string or QString)
        @return flag indicating success
        """

        fn = unicode(fn)

        if txt == None :
            txt = self.get_text_JDC(self.format)
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
            QMessageBox.critical(self, self.trUtf8('Save File'),
                self.trUtf8('The file <b>%1</b> could not be saved.<br>Reason: %2')
                    .arg(unicode(fn)).arg(str(why)))
            return 0

    #-----------------------------#
    def get_text_JDC(self,format):
    #-----------------------------#
      if self.code == "MAP" and not(generator.plugins.has_key(format)):
         format = "MAP"
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         self.generator=generator.plugins[format]()
         jdc_formate=self.generator.gener(self.jdc,format='beautifie',config=self.appliEficas.CONFIGURATION)
         if not self.generator.cr.estvide():
            self.affiche_infos("Erreur a la generation",Qt.red)
            QMessageBox.critical( self, "Erreur a la generation","EFICAS ne sait pas convertir ce JDC")
            return ""
         else:
            return jdc_formate
      else:
         # Il n'existe pas c'est une erreur
         self.affiche_infos("Format %s non reconnu" % self.format,Qt.red)
         QMessageBox.critical( self, "Format "+self.format+" non reconnu","EFICAS ne sait pas convertir le JDC selon le format "+self.format)
         return ""

    #-----------------------------#
    def run(self,execution="oui"):
    #-----------------------------#
      if self.code == "MAP" and not(generator.plugins.has_key(format)):
         self.format="MAP"
      if generator.plugins.has_key(self.format):
         self.generator=generator.plugins[self.format]()
      else :
         QMessageBox.critical( self, "Execution impossible ","EFICAS ne sait pas executer ce JDC ")
         return "" 

      # 
      self.textePython =self.generator.generRUN(self.jdc,self.appli.ssCode)
      if execution=="oui" :
         self._viewTextExecute( self.textePython)    
      return self.textePython


    #-----------------------------------------------------#
    def determineNomFichier(self,path,extension):
    #-----------------------------------------------------#
      if DictExtensions.has_key(self.appli.code) :
         chaine1="JDC (*"+DictExtensions[self.appli.code]+");;"
         extensions= self.trUtf8(chaine1+ "All Files (*)")
      else :
         extensions= self.trUtf8("JDC (*.comm);;" "All Files (*)")

      if self.appli.code == "MAP" :
         extensions = extensions + ";;Schema Yacs (*.xml);; Run (*.py);;"

      fn = QFileDialog.getSaveFileName( self,
             self.trUtf8("sauvegarde"), path,
             extensions,None,
             QFileDialog.DontConfirmOverwrite)
      if fn.isNull(): return (0, None)
      ext = QFileInfo(fn).suffix()
      if ext.isEmpty(): fn.append(extension)

      if QFileInfo(fn).exists():
           abort = QMessageBox.warning(self,
                   self.trUtf8("Sauvegarde du Fichier"),
                   self.trUtf8("Le fichier <b>%1</b> existe deja.").arg(fn),
                   self.trUtf8("&Ecraser"),
                   self.trUtf8("&Abandonner"))
           if abort == 1 :  return (0, "")
      return (1,fn)

    #-----------------#
    def saveRun(self):
    #-----------------#
        texte=self.run(execution="non")
        extension=".py"

        if hasattr(self,'fichierRun'):
           self.writeFile( self.fichierRun, txt = texte)
           return

        if self.fichier == None :
           path=self.CONFIGURATION.savedir
        else :
          path=QFileInfo(self.fichier).absolutePath()+"/"+QFileInfo(self.fichier).baseName()+".py"
        bOK, fn=self.determineNomFichier(path,extension)
        if fn == "" : return
        self.fichierRun = unicode(QDir.convertSeparators(fn))
        self.writeFile( self.fichierRun, txt = texte)
    

      
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
        return Dico

    #-----------------------------------------#
    def handleAjoutGroup(self,listeGroup):
    #-----------------------------------------#
        #try :
        if 1:
           from ajoutGroupe import handleAjoutGroupFiltre
           listeSource,listeMateriaux=handleAjoutGroupFiltre(listeGroup)
           print listeSource,listeMateriaux
        #except :
        else :
           pass

    #-----------------------------------------#
    def saveFile(self, path = None, saveas= 0):
    #-----------------------------------------#
        """
        Public slot to save the text to a file.
        
        @param path directory to save the file in (string or QString)
        @return tuple of two values (boolean, string) giving a success indicator and
            the name of the saved file
        """        
                
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
          if path is None: 
             path=self.CONFIGURATION.savedir
          bOK, fn=self.determineNomFichier(path,extension)
          if fn == None : return (0, None)
          if fn.isNull(): return (0, None)

          ulfile = os.path.abspath(unicode(fn))
          self.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
          fn = unicode(QDir.convertSeparators(fn))
          newName = fn

        if not (self.writeFile(fn)): return (0, None)
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

        if self.salome : 
               self.appliEficas.addJdcInSalome( self.fichier)
        return (1, self.fichier)
#
    #---------------------------------#
    def saveFileAs(self, path = None):
    #---------------------------------#
        """
        Public slot to save a file with a new name.
        
        @param path directory to save the file in (string or QString)
        @return tuple of two values (boolean, string) giving a success indicator and
            the name of the saved file
        """
        return self.saveFile(path,1)

   
        
    #---------------------------------------------#
    def get_file(self,unite=None,fic_origine = ''):
    #---------------------------------------------#
    # appele par I_JDC
        ulfile  = None
        jdcText = ""
      
        titre  = ""
        
        if unite :
            titre = "Choix unit� %d " %unite
            texte = "Le fichier %s contient une commande INCLUDE \n" % fic_origine
            texte = texte+'Donnez le nom du fichier correspondant\n � l unit� logique %d' % unite
            labeltexte = 'Fichier pour unite %d :' % unite
        else:
            titre = "Choix d'un fichier de poursuite"
            texte = "Le fichier %s contient une commande %s\n" %(fic_origine,'POURSUITE')
            texte = texte+'Donnez le nom du fichier dont vous \n voulez faire une poursuite'
                                        
        QMessageBox.information( self, titre,QString.fromUtf8(texte))
        fn = QFileDialog.getOpenFileName(self.appliEficas,
                   titre,
                   self.appliEficas.CONFIGURATION.savedir)
        
        if fn.isNull(): 
        # ce retour est impose par le get_file d'I_JDC
           return None," "
            
        ulfile = os.path.abspath(unicode(fn))
        self.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
       
        # On utilise le convertisseur défini par format_fichier
        source=self.get_source(ulfile)
        if source:
            # On a réussia convertir le fichier self.ulfile                
            jdcText = source
        else:
            # Une erreur a été rencontrée
            jdcText = ''
        return ulfile, jdcText

    #-------------------------------------#
    def ajoutVersionCataDsJDC(self,txt):
    #-------------------------------------#
        if not hasattr(self.readercata.cata[0],'LABEL_TRADUCTION'): return txt
        ligneVersion="#LABEL_TRADUCTION:"+self.readercata.cata[0].version_cata+":FIN LABEL_TRADUCTION\n"
        texte=txt+ligneVersion
        return texte

    #-------------------------------------#
    def verifieVersionCataDuJDC(self,text):
    #-------------------------------------#
        memeVersion=False
        indexDeb=text.find("#LABEL_TRADUCTION:")
        indexFin=text.find(":FIN LABEL_TRADUCTION")
        if indexDeb < 0 : 
           self.versionCataDuJDC="sans"
           textJDC=text
        else :
           self.versionCataDuJDC=text[indexDeb+17:indexFin]
           textJDC=text[0:indexDeb]+text[indexFin+21:-1]
     
        self.versionCata="sans"
        if hasattr(self.readercata.cata[0],'version_cata'): self.versionCata=self.readercata.cata[0].version_cata

        if self.versionCata==self.versionCataDuJDC : memeVersion=True
        return memeVersion,textJDC
        
    #-------------------------------#
    def traduitCatalogue(self,texte):
    #-------------------------------#
        nomTraducteur="traduit"+self.readercata.code+self.versionCataDuJDC+"To"+self.versionCata
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../Traducteur")))
        print nomTraducteur
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
        
if __name__=='__main__':    
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

#    #CS_pbruno note: fait implicitement des trucs ces imports (grr)
#    import styles
#    import import_code
#    import session
#
#    # Analyse des arguments de la ligne de commande
#    options=session.parse(sys.argv)
#    code=options.code
#        
    app = QApplication(sys.argv)    
    mw = JDCEditor(None,'azAster.comm')
    app.setMainWidget(mw)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    mw.show()
            
    res = app.exec_loop()
    sys.exit(res)
