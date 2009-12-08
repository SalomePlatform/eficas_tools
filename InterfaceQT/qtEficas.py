# -*- coding: iso-8859-1 -*-

import os, sys
REPINI=os.path.dirname(os.path.abspath(__file__))
INSTALLDIR=os.path.join(REPINI,'..')
from Editeur import import_code

from qt import *
from myMain import Eficas
from viewManager import MyTabview

import configuration
from Editeur import session

import utilIcons
utilIcons.initializeMimeSourceFactory()


class Appli(Eficas):    
    """
    Class implementing the main user interface.
    """
    def __init__(self,code="ASTER",salome=0,parent=None):
        """
        Constructor
        
        @param loc locale to be used by the UI (string)
        @param splash reference to the splashscreen (UI.SplashScreen.SplashScreen)
        """
        self.ihm="QT"
        self.code=code
        self.salome=salome
        Eficas.__init__(self,parent,fl=Qt.WType_Dialog)
        #Eficas.__init__(self,parent)

        if code == "ASTER" : 
           from Aster import prefs
           import sys
           sys.path.append(INSTALLDIR+"/Aster")
	else :
	   import prefs 
           #try :
           if 1 :
             apply(Appli.__dict__[code],(self,))
           #except :
           else:
             pass
        if hasattr(prefs,'encoding'):
           import sys
           reload(sys)
           sys.setdefaultencoding(prefs.encoding)
           del sys.setdefaultencoding

        self.top=self
        self.CONFIGURATION = configuration.make_config(self,prefs.REPINI)
        self.CONFIGStyle = configuration.make_config_style(self,prefs.REPINI)

        self.viewmanager = MyTabview(self, self) #MyTabview, MyWorkspace, Listspace
        self.setCentralWidget(self.viewmanager)

        self.recentMenu = QPopupMenu(self.Fichier)
        self.Fichier.insertItem(self.trUtf8('&Recents'), self.recentMenu,99,8)
        self.connect(self.recentMenu,SIGNAL('aboutToShow()'),self.handleShowRecentMenu)
        self.connect(self,PYSIGNAL('preferencesChanged'),
                     self.viewmanager.handlePreferencesChanged)
        
        self.connect(self.viewmanager,PYSIGNAL('lastEditorClosed'),
                     self.handleLastEditorClosed)
                     
        self.connect(self.viewmanager,PYSIGNAL('editorOpened'),
                     self.handleEditorOpened)
                             
        # Initialise the instance variables.
        self.currentProg = None
        self.isProg = 0
        self.utEditorOpen = 0
        self.utProjectOpen = 0
        
        self.inDragDrop = 0
        self.setAcceptDrops(1)
        self.ficPatrons={}
        self.initPatrons()
        self.monAssistant=QAssistantClient(QString(""), self.viewmanager)
        
        if self.salome :
           from Editeur import session
           self.ouvreFichiers()
        
    def OPENTURNS(self) :
        self.MenuBar.removeItem(5)
        self.MenuBar.removeItem(6)
        self.MenuBar.removeItem(7)


    def ouvreFichiers(self) :
    # Ouverture des fichiers de commandes donnes sur la ligne de commande
        cwd=os.getcwd()
        self.dir=cwd
        for study in session.d_env.studies:
            os.chdir(cwd)
            d=session.get_unit(study,self)
            #print study["comm"]
            self.viewmanager.handleOpen(fn=study["comm"],units=d)

        
    def initPatrons(self) :
    # Mise à jour du menu des fichiers recemment ouverts
        from Editeur import listePatrons
        self.listePatrons = listePatrons.listePatrons(self.code)
        idx = 0
        for nomSsMenu in self.listePatrons.liste.keys():
            ssmenu = QPopupMenu(self.Patrons)
            self.Patrons.insertItem(nomSsMenu, ssmenu)
            for fichier in self.listePatrons.liste[nomSsMenu]:
               id = ssmenu.insertItem(fichier, self.handleOpenPatrons)
               self.ficPatrons[idx]=fichier
               self.Patrons.setItemParameter(id,idx)
               idx=idx+1

    def traductionV7V8(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.rep_user,self.viewmanager,"V7V8")

    def traductionV8V9(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.rep_user,self.viewmanager,"V8V9")

    def version(self) :
        from desVisu import DVisu
        titre = "version "
        monVisu=DVisu(parent=self.viewmanager,fl=Qt.WType_Dialog)
        monVisu.setCaption(titre)
        monVisu.TB.setText("Eficas V1.17")
        monVisu.adjustSize()
        monVisu.show()

    def aidePPal(self) :
        maD=INSTALLDIR+"/AIDE/fichiers"
        docsPath = QDir(maD).absPath()
        self.monAssistant.showPage( QString("%1/index.html").arg(docsPath) )

    def optionEditeur(self) :
        from monOptionsEditeur import Options
        monOption=Options(parent=self.viewmanager,fl=Qt.WType_Dialog,configuration=self.CONFIGURATION)
        monOption.show()
        
    def optionPdf(self) :
        from monOptionsPdf import OptionPdf
        monOption=OptionPdf(parent=self.viewmanager,fl=Qt.WType_Dialog,configuration=self.CONFIGURATION)
        monOption.show()
        
    def handleShowRecentMenu(self):
        """
        Private method to set up recent files menu.
        """
        idx = 0
        self.recentMenu.clear()
        
        for rp in self.viewmanager.recent:
            id = self.recentMenu.insertItem('&%d. %s' % (idx+1, unicode(rp)),
                                            self.handleOpenRecent)
            self.recentMenu.setItemParameter(id,idx)
            
            idx = idx + 1
            
        self.recentMenu.insertSeparator()
        self.recentMenu.insertItem(self.trUtf8('&Clear'), self.handleClearRecent)
        
    def handleOpenPatrons(self, idx):
        fichier=REPINI+"/../Editeur/Patrons/"+self.code+"/"+self.ficPatrons[idx]
        self.viewmanager.handleOpen(fn=fichier, patron = 1)


    def handleOpenRecent(self, idx):
        """
        Private method to open a file from the list of rencently opened files.
        
        @param idx index of the selected entry (int)
        """        
        self.viewmanager.handleOpen(unicode(self.viewmanager.recent[idx]))
        
    def handleClearRecent(self):
        """
        Private method to clear the recent files menu.
        """
        self.viewmanager.recent = QStringList()

        
    def handleLastEditorClosed(self):
        """
        Public slot to handle the lastEditorClosed signal.
        """
        pass # CS_pbruno todo griser les parties k'il faut
        
    def handleEditorOpened(self, fn):
        """
        Public slot to handle the editorOpened signal.
        
        @param fn filename of the opened editor (string)
        """
        pass # CS_pbruno todo degriser les parties k'il faut
        
        
    def fileNew(self):        
        self.viewmanager.newEditor()        
        
    def fileOpen(self, prog=None):
        self.viewmanager.handleOpen(prog)        
        
    def fileNewView(self):
        self.viewmanager.handleNewView()
        
    def fileSave(self):
        self.viewmanager.saveCurrentEditor()
        
    def fileSaveAs(self):
        self.viewmanager.saveAsCurrentEditor()
        
    def fileClose(self):
        self.viewmanager.handleClose()
        
    def fileCloseAll(self):
        self.viewmanager.handleCloseAll()
        
    def fileExit(self):
        # On peut sortir sur Abort
        if self.viewmanager.handleCloseAll() ==0 : 
           return
        if self.salome :
           self.close()
        else :
           qApp.closeAllWindows()
        
    def editCopy(self):
        self.viewmanager.handleEditCopy()
      
    def editCut(self):
        self.viewmanager.handleEditCut()
    
    def editPaste(self):
        self.viewmanager.handleEditPaste()
        
    def jdcFichierSource(self):
        self.viewmanager.handleViewJdcFichierSource()
        
    def jdcRapport(self):
        self.viewmanager.handleViewJdcRapport()
        
    def visuJdcPy(self):
        self.viewmanager.handlevisuJdcPy()

    def get_source(self,file):
        from editor import JDCEditor
        monEditeur=JDCEditor()
        texte=monEditeur.get_source(file)
        return texte
    
    def helpAbout(self):
        import AIDE
        AIDE.go3(parent=self)

    def NewInclude(self):
        self.viewmanager.newIncludeEditor()

if __name__=='__main__':

    # Modules Eficas
    sys.path.append(INSTALLDIR+"/Aster")
    from Aster import prefs
    if hasattr(prefs,'encoding'):
       # Hack pour changer le codage par defaut des strings
       import sys
       reload(sys)
       sys.setdefaultencoding(prefs.encoding)
       del sys.setdefaultencoding
       # Fin hack

    from Editeur import import_code
    from Editeur import session

    # Analyse des arguments de la ligne de commande
    options=session.parse(sys.argv)
    code=options.code

    app = QApplication(sys.argv)    
    mw = Appli()
    app.setMainWidget(mw)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    mw.ouvreFichiers()
    mw.show()
            
    res = app.exec_loop()
    sys.exit(res)
