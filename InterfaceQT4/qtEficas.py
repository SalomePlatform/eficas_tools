# -*- coding: iso-8859-1 -*-

import os, sys

from PyQt4.QtGui  import *
from PyQt4.QtCore import *
from PyQt4.QtAssistant import *
from myMain import Ui_Eficas
from viewManager import MyTabview

from Editeur import session


class Appli(Ui_Eficas,QMainWindow):    
    """
    Class implementing the main user interface.
    """
    def __init__(self,code="ASTER",salome=0,parent=None,ssCode=None):
        """
        Constructor
        """
        self.VERSION_EFICAS="Eficas QT4 V2.1"

        self.ihm="QT"
        self.code=code
        self.ssCode=ssCode
        self.salome=salome
	self.top = self #(pour CONFIGURATION)
        self.QWParent=None #(Pour lancement sans IHM)
        self.indice=0
        self.dict_reels={}

        import prefs
        prefs.code=code
        name='prefs_'+prefs.code
        prefsCode=__import__(name)
        self.REPINI=prefsCode.REPINI
        self.RepIcon=prefsCode.INSTALLDIR+"/Editeur/icons"
        self.INSTALLDIR=prefsCode.INSTALLDIR
        if ssCode != None :
           self.format_fichier= ssCode	#par defaut
           prefsCode.NAME_SCHEME=ssCode
        else :
           self.format_fichier="python"	#par defaut

        if salome :
           import sys
        nameConf='configuration_'+prefs.code
        configuration=__import__(nameConf)
        self.CONFIGURATION = configuration.make_config(self,prefsCode.REPINI)
        self.CONFIGStyle = None
        if hasattr(configuration,'make_config_style'):
           self.CONFIGStyle = configuration.make_config_style(self,prefsCode.REPINI)
        if hasattr(prefsCode,'encoding'):
           import sys
           reload(sys)
           sys.setdefaultencoding(prefsCode.encoding)

        QMainWindow.__init__(self,parent)
        Ui_Eficas.__init__(self)
        self.setupUi(self)
        self.ajoutIcones()
        if code in Appli.__dict__.keys():
          listeTexte=apply(Appli.__dict__[code],(self,))

        self.viewmanager = MyTabview(self) 
        self.recentMenu=self.menuFichier.addMenu(self.trUtf8('&Recents'))
        self.connecterSignaux() 


        #if self.salome :
        #   from Editeur import session
        #   self.ouvreFichiers()

        self.recent =  QStringList()
        self.ficPatrons={}
        self.initPatrons()
        self.ficRecents={}
        self.initRecents()

        self.ouvreFichiers()
        self.setWindowTitle(self.VERSION_EFICAS)
        
    def ASTER(self) :
        self.menuTraduction = self.menubar.addMenu("menuTraduction")
        self.actionTraduitV7V8 = QAction(self)
        self.actionTraduitV7V8.setObjectName("actionTraduitV7V8")
        self.actionTraduitV8V9 = QAction(self)
        self.actionTraduitV8V9.setObjectName("actionTraduitV8V9")
        self.menuTraduction.addAction(self.actionTraduitV7V8)
        self.menuTraduction.addAction(self.actionTraduitV8V9)
        self.menuTraduction.setTitle(QApplication.translate("Eficas", "Traduction", None, QApplication.UnicodeUTF8))
        self.actionTraduitV7V8.setText(QApplication.translate("Eficas","TraduitV7V8", None, QApplication.UnicodeUTF8))
        self.actionTraduitV8V9.setText(QApplication.translate("Eficas","TraduitV8V9", None, QApplication.UnicodeUTF8))
        self.connect(self.actionTraduitV7V8,SIGNAL("activated()"),self.traductionV7V8)
        self.connect(self.actionTraduitV8V9,SIGNAL("activated()"),self.traductionV8V9)



    def MAP(self): 
        self.menuExecution = self.menubar.addMenu(QApplication.translate("Eficas", "Execution", None, QApplication.UnicodeUTF8))
        self.menuExecution.setObjectName("menuExecution")
        self.menuJdC.setTitle(QApplication.translate("Eficas", "Rapports", None, QApplication.UnicodeUTF8))

        self.actionExecution = QAction(self)
        icon6 = QIcon(self.RepIcon+"/compute.png")
        self.actionExecution.setIcon(icon6)
        self.actionExecution.setObjectName("actionExecution")
        self.menuExecution.addAction(self.actionExecution)
        self.toolBar.addAction(self.actionExecution)
        self.actionExecution.setText(QApplication.translate("Eficas", "Execution Python", None, QApplication.UnicodeUTF8))
        self.connect(self.actionExecution,SIGNAL("activated()"),self.run)

        self.actionEnregistrer_Python = QAction(self)
        self.actionEnregistrer_Python.setObjectName("actionEnregistrer_Python")
        self.menuFichier.addAction(self.actionEnregistrer_Python)
        self.actionEnregistrer_Python.setText(QApplication.translate("Eficas", "Sauve Python", None,QApplication.UnicodeUTF8))
        self.connect(self.actionEnregistrer_Python,SIGNAL("activated()"),self.saveRun)

        self.actionEnregistrerYACS = QAction(self)
        self.actionEnregistrerYACS.setObjectName("actionEnregistrerYACS")
        self.menuFichier.addAction(self.actionEnregistrerYACS)
        self.actionEnregistrerYACS.setText(QApplication.translate("Eficas", "Sauve Schema YACS", None,QApplication.UnicodeUTF8))
        self.connect(self.actionEnregistrerYACS,SIGNAL("activated()"),self.saveYACS)

        self.actionExecutionYACS = QAction(self)
        icon7 = QIcon(self.RepIcon+"/application.gif")
        self.actionExecutionYACS.setIcon(icon7)
        self.actionExecutionYACS.setObjectName("actionExecutionYACS")
        self.menuExecution.addAction(self.actionExecutionYACS)
        self.toolBar.addAction(self.actionExecutionYACS)
        self.actionExecutionYACS.setText(QApplication.translate("Eficas", "Execution YACS", None, QApplication.UnicodeUTF8))
        self.connect(self.actionExecutionYACS,SIGNAL("activated()"),self.runYACS)

    def ajoutIcones(self) :
        # Pour pallier les soucis de repertoire d icone
        icon = QIcon(self.RepIcon+"/New24.png")
        self.action_Nouveau.setIcon(icon)
        icon1 = QIcon(self.RepIcon+"/Open24.png")
        self.action_Ouvrir.setIcon(icon1)
        icon2 = QIcon(self.RepIcon+"/Save24.png")
        self.actionEnregistrer.setIcon(icon2)
        icon3 = QIcon(self.RepIcon+"/Cut24.png")
        self.actionCouper.setIcon(icon3)
        icon4 = QIcon(self.RepIcon+"/Copy24.png")
        self.actionCopier.setIcon(icon4)
        icon5 = QIcon(self.RepIcon+"/Paste24.png")
        self.actionColler.setIcon(icon5)


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

        self.connect(self.actionEficas,SIGNAL("activated()"),self.aidePPal)
        self.connect(self.actionVersion,SIGNAL("activated()"),self.version)

        self.connect(self.actionCouper,SIGNAL("activated()"),self.editCut)
        self.connect(self.actionCopier,SIGNAL("activated()"),self.editCopy)
        self.connect(self.actionColler,SIGNAL("activated()"),self.editPaste)
        self.connect(self.actionSupprimer,SIGNAL("activated()"),self.supprimer)

        self.connect(self.actionRapport_de_Validation,SIGNAL("activated()"),self.jdcRapport)
        self.connect(self.actionFichier_Source,SIGNAL("activated()"),self.jdcFichierSource)
        self.connect(self.actionFichier_Resultat,SIGNAL("activated()"),self.visuJdcPy)

        self.connect(self.actionParametres_Eficas,SIGNAL("activated()"),self.optionEditeur)
        self.connect(self.actionLecteur_Pdf,SIGNAL("activated()"),self.optionPdf)

        #self.connect(self.helpIndexAction,SIGNAL("activated()"),self.helpIndex)
        #self.connect(self.helpContentsAction,SIGNAL("activated()"),self.helpContents)
                             

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
        traduction(self.CONFIGURATION.rep_ini,self.viewmanager,"V7V8")

    def traductionV8V9(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.rep_ini,self.viewmanager,"V8V9")

    def version(self) :
        from monVisu import DVisu
        titre = "version "
        monVisuDialg=DVisu(parent=self,fl=0)
        monVisuDialg.setWindowTitle(titre)
        monVisuDialg.TB.setText(self.VERSION_EFICAS +QString(" pour ") + self.code)
        monVisuDialg.adjustSize()
        monVisuDialg.show()

    def aidePPal(self) :
        maD=self.INSTALLDIR+"/Aide"
        docsPath = QDir(maD).absolutePath()
        try :
          monAssistant=QAssistantClient(QString(""), self)
          arguments=QStringList()
          arguments << "-profile" <<docsPath+QDir.separator()+QString("eficas_")+QString(self.code)+QString(".adp");
          monAssistant.setArguments(arguments);
          monAssistant.showPage(docsPath+QDir.separator()+QString("fichiers_"+QString(self.code)+QString("/index.html")))
        except:
           QMessageBox.warning( self, "Aide Indisponible", "QT Assistant n est pas installe ")


    def optionEditeur(self) :
        name='monOptions_'+self.code
        try :
           optionCode=__import__(name)
        except :
           QMessageBox.critical( self, "Parametrage", "Pas de possibilite de personnalisation de la configuration ")
           return
        monOption=optionCode.Options(parent=self,modal = 0 ,configuration=self.CONFIGURATION)
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
        self.sauveRecents()
        
    def fileNew(self):        
        self.viewmanager.newEditor()        
        
    def fileOpen(self ):
        self.viewmanager.handleOpen()        
        
    def fileSave(self):
        self.viewmanager.saveCurrentEditor()
        
    def fileSaveAs(self):
        self.viewmanager.saveAsCurrentEditor()
        
    def fileClose(self):
        self.viewmanager.handleClose(texte='&Fermer')
        
    def fileCloseAll(self):
        self.viewmanager.handleCloseAll(texte='&Fermer')
        
    def fileExit(self):
        # On peut sortir sur Abort
        res=self.viewmanager.handleCloseAll()
        if (res != 2) : 
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
        
    def run(self):
        self.viewmanager.run()
        
    def saveRun(self):
        self.viewmanager.saveRun()
        
    def runYACS(self):
        self.viewmanager.runYACS()
        
    def saveYACS(self):
        self.viewmanager.saveYACS()
        
    def supprimer(self):
        self.viewmanager.handleSupprimer()
        
    def jdcFichierSource(self):
        self.viewmanager.handleViewJdcFichierSource()
        
    def jdcRapport(self):
        self.viewmanager.handleViewJdcRapport()
        
    def visuJdcPy(self):
        self.viewmanager.handleViewJdcPy()


    def NewInclude(self):
        self.viewmanager.newIncludeEditor()

    def getName(self):
        self.indice=self.indice+1
        texte="tempo"+str(self.indice)
        return texte
        

if __name__=='__main__':

    # Modules Eficas
    sys.path.append(INSTALLDIR+"/Aster")
    from Aster import prefsCode
    if hasattr(prefsCode,'encoding'):
       # Hack pour changer le codage par defaut des strings
       import sys
       reload(sys)
       sys.setdefaultencoding(prefsCode.encoding)
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
