# -*- coding: iso-8859-1 -*-

import os, sys

from PyQt4.QtGui  import *
from PyQt4.QtCore import *
from PyQt4.QtAssistant import *
from myMain import Ui_Eficas
from viewManager import MyTabview

from Editeur import session

dirCode={"ASTER":"Aster","OPENTURNS_WRAPPER":"Openturns_Wrapper"}


class Appli(Ui_Eficas,QMainWindow):    
    """
    Class implementing the main user interface.
    """
    def __init__(self,code="ASTER",salome=0,parent=None):
        """
        Constructor
        """
        self.ihm="QT"
        self.code=code
        self.salome=salome
        self.format_fichier="python"	#par defaut
	self.top = self #(pour CONFIGURATION)

        import prefs
        self.REPINI=prefs.REPINI
        import configuration
        self.CONFIGURATION = configuration.make_config(self,prefs.REPINI)
        self.CONFIGStyle = configuration.make_config_style(self,prefs.REPINI)
        if hasattr(prefs,'encoding'):
           import sys
           reload(sys)
           sys.setdefaultencoding(prefs.encoding)

        QMainWindow.__init__(self)
        Ui_Eficas.__init__(self)
        self.setupUi(self)
        self.viewmanager = MyTabview(self) 
        self.recentMenu=self.menuFichier.addMenu(self.trUtf8('&Recents'))
        self.connecterSignaux() 


        #self.monAssistant=QAssistantClient(QString(""), self.viewmanager)
        #if self.salome :
        #   from Editeur import session
        #   self.ouvreFichiers()

        self.recent =  QStringList()
        self.ficPatrons={}
        self.initPatrons()
        self.ficRecents={}
        self.initRecents()

        self.ouvreFichiers()
        
    def OPENTURNS(self) :
        self.MenuBar.removeItem(5)
        self.MenuBar.removeItem(6)
        self.MenuBar.removeItem(7)


    def connecterSignaux(self) :
        self.connect(self.recentMenu,SIGNAL('aboutToShow()'),self.handleShowRecentMenu)

	self.connect(self.action_Nouveau,SIGNAL("activated()"),self.fileNew)
        self.connect(self.actionNouvel_Include,SIGNAL("activated()"),self.NewInclude)
        self.connect(self.action_Ouvrir,SIGNAL("activated()"),self.fileOpen)
        self.connect(self.actionEnregistrer,SIGNAL("activated()"),self.fileSave)
        self.connect(self.actionEnregistrer_sous,SIGNAL("activated()"),self.fileSaveAs)
        self.connect(self.actionFermer,SIGNAL("activated()"),self.fileClose)
        self.connect(self.actionFermer_tout,SIGNAL("activated()"),self.fileCloseAll)
        self.connect(self.actionQuitter,SIGNAL("activated()"),self.fileExit)

        self.connect(self.actionCouper,SIGNAL("activated()"),self.editCut)
        self.connect(self.actionCopier,SIGNAL("activated()"),self.editCopy)
        self.connect(self.actionColler,SIGNAL("activated()"),self.editPaste)

        self.connect(self.actionRapport_de_Validation,SIGNAL("activated()"),self.jdcRapport)
        self.connect(self.actionFichier_Source,SIGNAL("activated()"),self.jdcFichierSource)
        self.connect(self.actionFichier_Resultat,SIGNAL("activated()"),self.visuJdcPy)

        self.connect(self.actionParametres_Eficas,SIGNAL("activated()"),self.optionEditeur)
        self.connect(self.actionLecteur_Pdf,SIGNAL("activated()"),self.optionPdf)

        self.connect(self.actionTraduitV7V8,SIGNAL("activated()"),self.traductionV7V8)
        self.connect(self.actionTraduitV8V9,SIGNAL("activated()"),self.traductionV8V9)

        #self.connect(self.helpIndexAction,SIGNAL("activated()"),self.helpIndex)
        #self.connect(self.helpContentsAction,SIGNAL("activated()"),self.helpContents)
        #self.connect(self.helpAboutAction,SIGNAL("activated()"),self.helpAbout)
        #self.connect(self.aidenew_itemAction,SIGNAL("activated()"),self.helpAbout)
                             

    def ouvreFichiers(self) :
    # Ouverture des fichiers de commandes donnes sur la ligne de commande
        cwd=os.getcwd()
        self.dir=cwd
        for study in session.d_env.studies:
            os.chdir(cwd)
            d=session.get_unit(study,self)
            self.viewmanager.handleOpen(fichier=study["comm"],units=d)

    def  get_source(self,file):
    # appele par Editeur/session.py
        import convert
        p=convert.plugins['python']()
        p.readfile(file)
        texte=p.convert('execnoparseur')
        return texte


        
    def initPatrons(self) :
    # Mise à jour du menu des fichiers recemment ouverts
        from Editeur import listePatrons
        self.listePatrons = listePatrons.listePatrons(self.code)
        idx = 0
        for nomSsMenu in self.listePatrons.liste.keys():
            ssmenu=self.menuPatrons.addMenu(nomSsMenu)
            for fichier in self.listePatrons.liste[nomSsMenu]:
               id = ssmenu.addAction(fichier)
               self.ficPatrons[id]=fichier
               self.connect(id, SIGNAL('triggered()'),self.handleOpenPatrons)
            #   self.Patrons.setItemParameter(id,idx)
               idx=idx+1

    def initRecents(self):
       try :
           rep=self.CONFIGURATION.rep_user
           monFichier=rep+"/listefichiers_"+self.code
           index=0
           f=open(monFichier)
           while ( index < 9) :
              ligne=f.readline()
              if ligne != "" :
                 l=(ligne.split("\n"))[0]
                 self.recent.append(l)
              index=index+1
       except :
           pass

       try    : f.close()
       except : pass

    def addToRecentList(self, fn):
        """
        Public slot to add a filename to the list of recently opened files.

        @param fn name of the file to be added
        """
        self.recent.removeAll(fn)
        self.recent.prepend(fn)
        if len(self.recent) > 9:
            self.recent = self.recent[:9]

    def sauveRecents(self) :
       rep=self.CONFIGURATION.rep_user
       monFichier=rep+"/listefichiers_"+self.code
       try :
            f=open(monFichier,'w')
            if len(self.recent) == 0 : return
            index=0
            while ( index <  len(self.recent)):
              ligne=str(self.recent[index])+"\n"
              f.write(ligne)
              index=index+1
       except :
            pass
       try :
            f.close()
       except :
            pass



    def traductionV7V8(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.rep_user,self.viewmanager,"V7V8")

    def traductionV8V9(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.rep_user,self.viewmanager,"V8V9")

    def version(self) :
        from desVisu import DVisu
        titre = "version "
        monVisu=DVisu(parent=self.viewmanager)
        monVisu.setCaption(titre)
        monVisu.TB.setText("Eficas V1.13")
        monVisu.adjustSize()
        monVisu.show()

    def aidePPal(self) :
        maD=INSTALLDIR+"/AIDE/fichiers"
        docsPath = QDir(maD).absPath()
        self.monAssistant.showPage( QString("%1/index.html").arg(docsPath) )

    def optionEditeur(self) :
        from monOptionsEditeur import Options
        monOption=Options(parent=self,modal = 0 ,configuration=self.CONFIGURATION)
        monOption.show()
        
    def optionPdf(self) :
        from monOptionsPdf import OptionPdf
        monOption=OptionPdf(parent=self,modal = 0 ,configuration=self.CONFIGURATION)
        monOption.show()
        
    def handleShowRecentMenu(self):
        """
        Private method to set up recent files menu.
        """
        self.recentMenu.clear()
        
        for rp in self.recent:
            id = self.recentMenu.addAction(rp)
            self.ficRecents[id]=rp
            self.connect(id, SIGNAL('triggered()'),self.handleOpenRecent)
        self.recentMenu.addSeparator()
        self.recentMenu.addAction(self.trUtf8('&Clear'), self.handleClearRecent)
        
    def handleOpenPatrons(self):
        idx=self.sender()
        fichier=self.REPINI+"/../Editeur/Patrons/"+self.code+"/"+self.ficPatrons[idx]
        self.viewmanager.handleOpen(fichier=fichier, patron = 1)

    def handleOpenRecent(self):
        idx=self.sender()
        fichier=self.ficRecents[idx]
        self.viewmanager.handleOpen(fichier=fichier, patron =0 )
        
    def handleClearRecent(self):
        self.recent = QStringList()
        
    def fileNew(self):        
        self.viewmanager.newEditor()        
        
    def fileOpen(self ):
        self.viewmanager.handleOpen()        
        
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
        self.viewmanager.handleCloseAll()
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
        self.viewmanager.handleViewJdcPy()

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
    #app.setMainWidget(mw) (qt3)
    Eficas=Appli()
    Eficas.show()

    #app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    #mw.ouvreFichiers()
    #mw.show()

    res=app.exec_()
    sys.exit(res)
