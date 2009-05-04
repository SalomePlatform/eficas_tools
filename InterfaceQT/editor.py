#i -*- coding: iso-8859-1 -*-

# Modules Python
import types,sys,os
import traceback
from qt import *

# Modules Eficas

import convert,generator
from Editeur     import session
from Editeur     import comploader
from Editeur     import Objecttreeitem
import panelsQT
import browser
import readercata

import prefs
import qtCommun

VERSION_EFICAS  = "EFICAS v1.15"


# -------------------------- #
#                            #
class JDCEditor(QSplitter):
#                            #
# -------------------------- #
    """
       Editeur de jdc
    """        

    def __init__(self,fn = None, jdc = None ,parent=None, editor = None, units = None, include=0):          
    #-------------------------------------------------------------------------------------------#

        QSplitter.__init__(self, parent,'')
        
        VERSION_CODE    = session.d_env.cata
        self.salome=0
	self.parent         = parent
        if parent != None :
           self.salome         = self.parent.salome
        self.appliEficas = self.parent.appliEficas
        self.top  = None
        self.code = prefs.code
        self.version_code = VERSION_CODE
        self.titre=VERSION_EFICAS + ' pour '+ self.code
        self.dict_reels={}
        self.liste_simp_reel=[]        
        self.format_fichier='python' # par defaut
	self.jdc_openturn_xml=""
	self.jdc_openturn_std=""
        self.ihm="QT"
        
        import configuration
        self.CONFIGURATION = self.appliEficas.CONFIGURATION
        self.CONFIGStyle = self.appliEficas.CONFIGStyle
        self.test=0
        self.sb = None
        if hasattr(qApp.mainWidget(),"statusBar"):
            self.sb = qApp.mainWidget().statusBar()
      
        self.vm             = parent    #viewManager
        self.fileName       = fn
        self.fileInfo       = None
        self.lastModified   = 0
        self.jdc            = jdc
        
        self.fichier=None
        self.panel_courant=None    
        self.node_selected = None
        self.modified   = False
        self.isReadOnly = False
        
        if not hasattr( readercata, 'reader' ) :
            readercata.reader = readercata.READERCATA( self, self )
        self.readercata = readercata.reader
        
        #------- construction du jdc --------------

        jdc_item = None
                        
        nouveau=0
        if self.fileName is not None:        #  fichier jdc fourni
            self.fileInfo = QFileInfo(self.fileName)
            self.fileInfo.setCaching(0)
            if editor is None:
                self.jdc = self.readFile(self.fileName)
                if units is not None:
                   self.jdc.recorded_units=units
                   self.jdc.old_recorded_units=units
            else:
                self.top            = editor.top
                self.code           = editor.code
                self.version_code   = editor.version_code
                self.titre          = editor.titre
                self.dict_reels     = editor.dict_reels
                self.liste_simp_reel= editor.liste_simp_reel
                self.format_fichier = editor.format_fichier
                self.CONFIGURATION  = editor.CONFIGURATION
                self.CONFIGStyle    = editor.CONFIGStyle
                self.jdc            = editor.jdc
                
                self.lastModified = self.fileInfo.lastModified()                
        elif editor is not None: 
            self.jdc = editor.jdc            
        else: 
            if not self.jdc:                   #  nouveau jdc
                if not include :
                   self.jdc = self._newJDC(units=units)
                else :
                   self.jdc = self._newJDCInclude(units=units)
                nouveau=1
        
        if self.jdc:            
            self.jdc.appli = self
            txt_exception  = None
            if not jdc:
                self.jdc.analyse()            
                txt_exception = self.jdc.cr.get_mess_exception()            
            if txt_exception:
                self.jdc = None
                qApp.restoreOverrideCursor()
                self.affiche_infos("Erreur fatale au chargement de %s" %fn)                
                QMessageBox.critical( self, "Erreur fatale au chargement d'un fichier", txt_exception)                
            else:
                comploader.charger_composants("QT")
                jdc_item=Objecttreeitem.make_objecttreeitem( self, "nom", self.jdc )

                if (not self.jdc.isvalid()) and (not nouveau) :
                    self.viewJdcRapport()

        #------- config widget --------------
                
        if jdc_item:                        
            self.tree = browser.JDCTree( jdc_item, self )
            self.connect(self.tree,SIGNAL('selectionChanged(QListViewItem *)'),self.updatePanel)
      
        sh = self.sizeHint()
        if sh.height() < 300:
            sh.setHeight(300)
        self.resize(sh)
            
        # Make sure tabbing through a QWorkspace works.
        self.setFocusPolicy(QWidget.StrongFocus)
        self._updateReadOnly(1)
        
        # Set the editors size if it is too big for the parent.
        if parent is not None:
            req = self.size()
            bnd = req.boundedTo(parent.size())
        
            if bnd.width() < req.width() or bnd.height() < req.height():
                self.resize(bnd)
        
        self.panel = QWidget(self)        
        #self.connect(self, SIGNAL('modificationChanged(bool)'), self.handleModificationChanged)
                
        
    #-------------------------------------------------------------------#
    def _updateReadOnly(self, bForce=1):
    #-------------------------------------------------------------------#
        """
        Private method to update the readOnly information for this editor. 
        
        If bForce is True, then updates everything regardless if
        the attributes have actually changed, such as during
        initialization time.  A signal is emitted after the
        caption change.

        @param bForce 1 to force change, 0 to only update and emit
                signal if there was an attribute change.
        """

        if self.fileName is None:
            return
        readOnly = not QFileInfo(self.fileName).isWritable() and 1 or 0
        if not bForce and (readOnly == self.isReadOnly):
            return
        cap = self.fileName
        if readOnly:
            cap = "%s (ro)" % unicode(cap)
        self.isReadOnly = readOnly
        self.setCaption(cap)
        self.emit(PYSIGNAL('captionChanged'), (cap, self))
        
    #--------------------------------#
    def _newJDC( self ,units = None):        
    #--------------------------------#
        """
        Initialise un nouveau JDC vierge
        """
        CONTEXT.unset_current_step()        
        jdc=self.readercata.cata[0].JdC( procedure="",
                                         appli=self,
                                         cata=self.readercata.cata,
                                         cata_ord_dico=self.readercata.cata_ordonne_dico,
                                         rep_mat=self.CONFIGURATION.rep_mat
                                        )                         
        if units is not None:
           jdc.recorded_units=units
           jdc.old_recorded_units=units
        jdc.analyse()        
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

            
    #-----------------------#
    def get_source(self,file):
    #-----------------------#
        import convert
        format=self.format_fichier

        # Il faut convertir le contenu du fichier en fonction du format
        if convert.plugins.has_key(format):
            # Le convertisseur existe on l'utilise
            p=convert.plugins[format]()
            p.readfile(file)
            text=p.convert('execnoparseur')
            if not p.cr.estvide():
                self.affiche_infos("Erreur a la conversion")
            return text
        else:
            # Il n'existe pas c'est une erreur
            self.affiche_infos("Type de fichier non reconnu")
            QMessageBox.critical( self, "Type de fichier non reconnu","EFICAS ne sait pas ouvrir ce type de fichier")            
            return None
        
    #---------------------------------------------#
    def get_file(self,unite=None,fic_origine = ''):
    #---------------------------------------------#
        ulfile  = None
        jdcText = ""
      
        titre  = ""
        
        if unite :
            titre = "Choix unite %d " %unite
            texte = "Le fichier %s contient une commande INCLUDE \n" % fic_origine
            texte = texte+'Donnez le nom du fichier correspondant à l unité logique %d' % unite
            labeltexte = 'Fichier pour unite %d :' % unite
        else:
            titre = "Choix d'un fichier de poursuite"
            texte = "Le fichier %s contient une commande %s\n" %(fic_origine,'POURSUITE')
            texte = texte+'Donnez le nom du fichier dont vous  voulez faire une poursuite'
                                        
        QMessageBox.information( self, titre,texte)
        fn = QFileDialog.getOpenFileName( self.CONFIGURATION.savedir,"", self, titre, "" )
        
        if fn.isNull():
            return
            
        ulfile = os.path.abspath(unicode(fn))
        # On utilise le convertisseur défini par format_fichier
        source=self.get_source(ulfile)
        if source:
            # On a réussi à convertir le fichier self.ulfile                
            jdcText = source
        else:
            # Une erreur a été rencontrée
            jdcText = ''
        return ulfile, jdcText
        
        
    #-----------------------#
    def readFile(self, fn):
    #-----------------------#
        """
        Public slot to read the text from a file.
        
        @param fn filename to read from (string or QString)
        """        
        fn = unicode(fn)        
            
        qApp.setOverrideCursor(Qt.waitCursor)
                        
        # ------------------------------------------------------------------------------------
        #                         charge le JDC
        # ------------------------------------------------------------------------------------      
        
        jdcName=os.path.basename(fn)
        # Il faut convertir le contenu du fichier en fonction du format
        if convert.plugins.has_key( self.format_fichier ):
             # Le convertisseur existe on l'utilise
             appli = self # CS_pbruno compatiblity parseur_python: self.appli.liste_simp_reel, self.appli.dict_reels
             p=convert.plugins[self.format_fichier]()
             p.readfile(fn)         
             text=p.convert('exec',appli)
             if not p.cr.estvide():                 
                self.affiche_infos("Erreur à la conversion")
        
        CONTEXT.unset_current_step()
        ##   os.chdir(self.initialdir)
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
                        
        qApp.restoreOverrideCursor()        
        if self.fileInfo!= None : 
           self.lastModified = self.fileInfo.lastModified()
        else :
           self.lastModified = 1
        return jdc
        
    #----------------------------------------------#
    def _viewText(self, txt, caption = "FILE_VIEWER"):    
    #----------------------------------------------#
        w = qtCommun.ViewText( self.parent )
        w.setCaption( caption )
        w.setText(txt)
        w.show()
        
    #-----------------------#
    def viewJdcSource(self):        
    #-----------------------#
        format = self.format_fichier
        f=open(self.fileName,'r')
        texteSource=f.read()
        f.close()
        self._viewText(texteSource, "JDC_SOURCE")
                
    #-----------------------#
    def viewJdcPy(self):        
    #-----------------------#
        format = self.format_fichier
        strSource = str( self.get_text_JDC(format) )       
        self._viewText(strSource, "JDC_RESULTAT")
                
    #-----------------------#
    def viewJdcRapport(self):
    #-----------------------#
        strRapport = str( self.jdc.report() )
        self._viewText(strRapport, "JDC_RAPPORT")        
        
    #-----------------------#
    def handleRenamed(self, fn):
    #-----------------------#
        """
        Public slot to handle the editorRenamed signal.
        
        @param fn filename to be set for the editor (QString or string).
        """
        self.fileName = unicode(fn)
        self.setCaption(self.fileName)
        
        if self.fileInfo is None:
            self.fileInfo = QFileInfo(self.fileName)
            self.fileInfo.setCaching(0)
        
        self.lastModified = self.fileInfo.lastModified()
        self.vm.setEditorName(self, self.fileName)
        self._updateReadOnly(1)        

    #-----------------------#
    def handleNewView(self):
    #-----------------------#
        """
        Private slot to create a new view to an open document.
        """
        self.vm.newEditorView(self.fileName, self)#, self.isPythonFile)

    #------------------------------------#
    def handleModificationChanged(self, m):
    #------------------------------------#
        """
        Private slot to handle the modificationChanged signal. 
        
        It emits the signal modificationStatusChanged with parameters
        m and self.
        
        @param m modification status
        """
        if not m and self.fileInfo is not None:
            self.lastModified = self.fileInfo.lastModified()
        self.emit(PYSIGNAL('modificationStatusChanged'), (m, self))
        
    #------------------------#
    def hasSyntaxErrors(self):        
    #------------------------#
        return False #CS_pbruno todo
        
    #----------------#
    def closeIt(self):
    #----------------#
        """
        Public method called by the viewmanager to finally get rid of us.
        """

        if self.jdc:
            self.jdc.supprime()
        self.close()
    

    #------------------------------#
    def affiche_infos(self,message):
    #------------------------------#
        if self.salome :
	   if not hasattr(self.appliEficas,'MessageLabel') :
              self.appliEficas.leLayout=QDockWindow(self.appliEficas)
	      self.appliEficas.MessageLabel = QLabel(self.appliEficas.leLayout,"MessageLabel")
	      self.appliEficas.MessageLabel.setAlignment(Qt.AlignBottom)
              self.appliEficas.leLayout.setWidget(self.appliEficas.MessageLabel)
              self.appliEficas.moveDockWindow(self.appliEficas.leLayout,Qt.DockBottom)
	   self.appliEficas.MessageLabel.setText(message)
	   self.appliEficas.MessageLabel.show()
	   self.appliEficas.leLayout.show()
        if self.sb:
           self.sb.message(message)#,2000)

    #------------------------------#
    def updatePanel(self, jdcNode):
    #------------------------------#
        """
        Appele a chaque changement de noeud
        """
        self.node_selected = jdcNode
        if self.panel:
            self.panel.close()
            del self.panel
            self.panel = None
            
        if jdcNode.item.isactif():
            self.panel = jdcNode.getPanel()
            #print self.panel.__class__
        else:
            self.panel = panelsQT.PanelInactif(self.node_selected,self)
            
        if not self.panel:
            self.panel = panelsQT.NoPanel(self)
        
        self.panel.show()
        
    
    #-------------------#
    def init_modif(self):
    #-------------------#
      """
          Met l'attribut modified a 'o' : utilise par Eficas pour savoir 
          si un JDC doit etre sauvegarde avant destruction ou non
      """
      self.modified = True
      self.emit(PYSIGNAL('modificationStatusChanged'), (True, self))
    
    #-------------------#
    def stop_modif(self):
    #-------------------#
      """
          Met l'attribut modified à 'n' : utilisé par Eficas pour savoir 
          si un JDC doit etre sauvegardé avant destruction ou non
      """      
      self.modified = False
      self.emit(PYSIGNAL('modificationStatusChanged'), (False, self))
    
    
    #-------------------#
    def cut(self):
    #-------------------#
      """
      Stocke dans Eficas.noeud_a_editer le noeud à couper
      """
      if not self.node_selected.item.iscopiable():
          QMessageBox.information( self, "Copie impossible",
                "Cette version d'EFICAS ne permet que la copie d'objets de type 'Commande' ou mot-clé facteur")          
          return
      self.parent.edit="couper"
      self.parent.noeud_a_editer = self.node_selected      
    
    #-------------------#
    def copy(self):
    #-------------------#
      """
      Stocke dans Eficas.noeud_a_editer le noeud a copier
      """
      if not self.node_selected.item.iscopiable():
          QMessageBox.information( self, "Copie impossible",
                   "La copie d'un tel objet n'est pas permise")          
          return
      self.parent.edit="copier"
      self.parent.noeud_a_editer = self.node_selected
    
    #-------------------#
    def paste(self):
    #-------------------#
      """
      Lance la copie de l'objet place dans self.parent.noeud_a_editer
      Ne permet que la copie d'objets de type Commande ou MCF
      """
      try:
         child=self.parent.noeud_a_editer.doPaste(self.node_selected)
      except:
         traceback.print_exc()
         QMessageBox.information( self, "Copie impossible",         
                                        "L'action de coller apres un tel objet n'est pas permise")
         return
    
      if child == 0:
          if self.message != '':             
             QMessageBox.critical( self, "Copie refusee", self.message)
             self.message = ''
          self.affiche_infos("Copie refusée")
          return
    
      # il faut declarer le JDCDisplay_courant modifie
      self.init_modif()
      # suppression eventuelle du noeud selectionne
      # si possible on renomme l objet comme le noeud couper

      if self.parent.edit == "couper":
         #nom = self.parent.noeud_a_editer.item.object.sd.nom
         item=self.parent.noeud_a_editer.item
         self.parent.noeud_a_editer.delete()
         child.item.update(item)
         #test,mess = child.item.nomme_sd(nom)
         child.select()

      # on rend la copie a nouveau possible en liberant le flag edit
      self.parent.edit="copier"
          
    #---------------------#
    def getFileName(self):
    #---------------------#
      return self.fileName
      
    #---------------------------#
    def writeFile(self, fn, txt = None):
    #------------------------------#
        """
        Public slot to write the text to a file.
        
        @param fn filename to write to (string or QString)
        @return flag indicating success
        """

        fn = unicode(fn)

        if txt == None :
            txt = self.get_text_JDC(self.format_fichier)
            eol = '\n'        
            if len(txt) >= len(eol):
               if txt[-len(eol):] != eol:
                  txt += eol
            else:
                txt += eol        

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

    #------------------------------------ 
    def writeFilesOpenturns(self,fn) :
    #------------------------------------ 
	base=fn[:fn.rfind(".")]
	fileXML=base + '.xml'
	fileSTD=base + '_std.py'
        self.writeFile(fileXML,self.jdc_openturn_xml)
        self.writeFile(fileSTD,self.jdc_openturn_std)


    #-----------------------------#
    def get_text_JDC(self,format):
    #-----------------------------#
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         g=generator.plugins[format]()
         jdc_formate=g.gener(self.jdc,format='beautifie')
	 if format == "openturns" :
	    self.jdc_openturn_xml=g.getOpenturnsXML()
	    self.jdc_openturn_std=g.getOpenturnsSTD()
         if not g.cr.estvide():            
            self.affiche_infos("Erreur à la generation")
            QMessageBox.critical( self, "Erreur a la generation","EFICAS ne sait pas convertir ce JDC")
            return
         else:
            return jdc_formate
      else:         
         # Il n'existe pas c'est une erreur
         self.affiche_infos("Format %s non reconnu" % format)
         QMessageBox.critical( self, "Format %s non reconnu" % format,"EFICAS ne sait pas convertir le JDC en format %s "% format)
         return
      
      
    #-------------------------------------------#
    def saveFile(self, saveas = 0, path = None):
    #-------------------------------------------#
        """
        Public slot to save the text to a file.
        
        @param saveas flag indicating a 'save as' action
        @param path directory to save the file in (string or QString)
        @return tuple of two values (boolean, string) giving a success indicator and
            the name of the saved file
        """        
        self.modified = True #CS_pbruno test
                
        if not saveas and not self.modified:#self.isModified():
            return (0, None)      # do nothing if text wasn't changed
            
        newName = None
        if saveas or self.fileName is None:
            if path is None and self.fileName is not None:
                path = os.path.dirname(unicode(self.fileName))
            else :
                path=self.CONFIGURATION.savedir
            fn = QFileDialog.getSaveFileName(path,
                self.trUtf8("JDC (*.comm);;" "All Files (*)"),self, None,
                self.trUtf8("Save File"), '', 0)

            if not fn.isNull():
                ext = QFileInfo(fn).extension()
                if ext.isEmpty():
                    ex =  ".comm"
                    fn.append(ex)
                if QFileInfo(fn).exists():
                    abort = QMessageBox.warning(
			self,
                        self.trUtf8("Save File"),
                        self.trUtf8("The file <b>%1</b> already exists.").arg(fn),
                        self.trUtf8("&Overwrite"),
                        self.trUtf8("&Abort") )
                    print abort
                    if abort:
                        return (0, None)
                fn = unicode(QDir.convertSeparators(fn))
                newName = fn
            else:
                return (0, None)
        else:
            fn = self.fileName
        
        if self.writeFile(fn):
            self.fileName = fn
            self.modified  = False                        
            self.setCaption(self.fileName)                
            if self.fileInfo is None or saveas:
                self.fileInfo = QFileInfo(self.fileName)
                self.fileInfo.setCaching(0)
                self.emit(PYSIGNAL('editorRenamed'), (self.fileName,))
            self.lastModified = self.fileInfo.lastModified()
            if newName is not None:
                self.vm.addToRecentList(newName)
            self.emit(PYSIGNAL('editorSaved'), (self.fileName,))
            self.stop_modif()            
	    if self.code == "OPENTURNS" :
	       self.writeFilesOpenturns(fn)
            if self.salome : 
               self.parent.appli.addJdcInSalome( self.fileName)
               if self.code == 'ASTER':
                  self.parent.appli.createOrUpdateMesh(self)
               #PN ; TODO


            return (1, self.fileName)
        else:
            return (0, None)

    #---------------------------------#
    def saveFileAs(self, path = None):
    #---------------------------------#
        """
        Public slot to save a file with a new name.
        
        @param path directory to save the file in (string or QString)
        @return tuple of two values (boolean, string) giving a success indicator and
            the name of the saved file
        """
        return self.saveFile(1, path)

   
if __name__=='__main__':    
    if hasattr(prefs,'encoding'):
       # Hack pour changer le codage par defaut des strings
       import sys
       reload(sys)
       sys.setdefaultencoding(prefs.encoding)
       del sys.setdefaultencoding
       # Fin hack

    #CS_pbruno note: fait implicitement des trucs ces imports (grr)
    import styles
    import import_code
    import session

    # Analyse des arguments de la ligne de commande
    options=session.parse(sys.argv)
    code=options.code
        
    app = QApplication(sys.argv)    
    mw = JDCEditor('azAster.comm')
    app.setMainWidget(mw)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    mw.show()
            
    res = app.exec_loop()
    sys.exit(res)
    
