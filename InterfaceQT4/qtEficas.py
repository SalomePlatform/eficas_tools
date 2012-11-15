# -*- coding: iso-8859-1 -*-
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

import os, sys

from PyQt4.QtGui  import *
from PyQt4.QtCore import *
from myMain import Ui_Eficas
from viewManager import MyTabview

from Editeur import session


class Appli(Ui_Eficas,QMainWindow):    
    """
    Class implementing the main user interface.
    """
    def __init__(self,code=None,salome=0,parent=None,ssCode=None,multi=False):
        """
        Constructor
        """
        QMainWindow.__init__(self,parent)
        Ui_Eficas.__init__(self)
        self.setupUi(self)

        self.VERSION_EFICAS="Eficas QT4 V6.6"
        self.salome=salome
        self.ihm="QT"
	self.top = self    #(pour CONFIGURATION)
        self.QWParent=None #(Pour lancement sans IHM)
        self.indice=0
        self.dict_reels={}
        self.code=code
        self.listeAEnlever=[]
        self.ListeCode=['Aster','Carmel3D','Cuve2dg','Openturns_Study','Openturns_Wrapper','MAP']

        self.RepIcon=os.path.join( os.path.dirname(os.path.abspath(__file__)),'../Editeur/icons')
        self.multi=multi
        if self.multi == False :
             self.definitCode(code,ssCode)
             if code==None: return
        
        eficas_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ajoutIcones()

        self.viewmanager = MyTabview(self) 
        self.recentMenu=self.menuFichier.addMenu(self.trUtf8('&Recents'))
        self.connecterSignaux() 

        self.recent =  QStringList()
        self.ficPatrons={}
        self.initRecents()

        self.ouvreFichiers()
        self.setWindowTitle(self.VERSION_EFICAS)
        
    def definitCode(self,code,ssCode) :
        self.code=code
        self.ssCode=ssCode
        self.cleanPath()
        if self.code==None :
           from monChoixCode import MonChoixCode
           widgetChoix = MonChoixCode(self)
           ret=widgetChoix.exec_()
        import sys
        if self.code == None:return # pour le cancel de la fenetre choix code
        name='prefs_'+self.code
        prefsCode=__import__(name)

        self.repIni=prefsCode.repIni
        if ssCode != None :
           self.format_fichier= ssCode	#par defaut
           prefsCode.NAME_SCHEME=ssCode
        else :
           self.format_fichier="python"	#par defaut

        nameConf='configuration_'+self.code
        configuration=__import__(nameConf)
        self.CONFIGURATION = configuration.make_config(self,prefsCode.repIni)
        self.CONFIGStyle = None
        if hasattr(configuration,'make_config_style'):
           self.CONFIGStyle = configuration.make_config_style(self,prefsCode.repIni)
        if hasattr(prefsCode,'encoding'):
           import sys
           reload(sys)
           sys.setdefaultencoding(prefsCode.encoding)
        if self.code in Appli.__dict__.keys():
          listeTexte=apply(Appli.__dict__[self.code],(self,))
        self.ficRecents={}

    def reconstruitMenu(self):
        self.initPatrons()
        self.initRecents()
        for intituleMenu in ("menuTraduction","menuOptions"):
           if hasattr(self,intituleMenu):
              menu=getattr(self,intituleMenu)
              menu.setAttribute(Qt.WA_DeleteOnClose)
              menu.close()
              delattr(self,intituleMenu)
        if self.code in Appli.__dict__.keys():
          listeTexte=apply(Appli.__dict__[self.code],(self,))


    def ASTER(self) :
        self.menuTraduction = self.menubar.addMenu("menuTraduction")
        self.actionTraduitV7V8 = QAction(self)
        self.actionTraduitV7V8.setObjectName("actionTraduitV7V8")
        self.actionTraduitV8V9 = QAction(self)
        self.actionTraduitV8V9.setObjectName("actionTraduitV8V9")
        self.actionTraduitV9V10 = QAction(self)
        self.actionTraduitV9V10.setObjectName("actionTraduitV9V10")
        self.menuTraduction.addAction(self.actionTraduitV7V8)
        self.menuTraduction.addAction(self.actionTraduitV8V9)
        self.menuTraduction.addAction(self.actionTraduitV9V10)
        self.menuTraduction.setTitle(QApplication.translate("Eficas", "Traduction", None, QApplication.UnicodeUTF8))
        self.actionTraduitV7V8.setText(QApplication.translate("Eficas","TraduitV7V8", None, QApplication.UnicodeUTF8))
        self.actionTraduitV8V9.setText(QApplication.translate("Eficas","TraduitV8V9", None, QApplication.UnicodeUTF8))
        self.actionTraduitV9V10.setText(QApplication.translate("Eficas","TraduitV9V10", None, QApplication.UnicodeUTF8))
        self.connect(self.actionTraduitV7V8,SIGNAL("activated()"),self.traductionV7V8)
        self.connect(self.actionTraduitV8V9,SIGNAL("activated()"),self.traductionV8V9)
        self.connect(self.actionTraduitV9V10,SIGNAL("activated()"),self.traductionV9V10)



    def CARMEL3D(self):
        if self.salome == 0 : return
        self.menuMesh = self.menubar.addMenu("menuMesh")
        self.menuMesh.setObjectName("Mesh")
    #    self.actionChercheGrpMesh = QAction(self)
    #    self.actionChercheGrpMesh.setText("Acquiert SubMeshes")
    #    self.menuMesh.addAction(self.actionChercheGrpMesh)
    #    self.connect(self.actionChercheGrpMesh,SIGNAL("activated()"),self.ChercheGrpMesh)
        self.actionChercheGrpMaille = QAction(self)
        self.actionChercheGrpMaille.setText("Acquiert Groupe Maille")
        self.menuMesh.addAction(self.actionChercheGrpMaille)
        self.connect(self.actionChercheGrpMaille,SIGNAL("activated()"),self.ChercheGrpMaille)

    def ChercheGrpMesh(self):
        Msg,listeGroup=self.ChercheGrpMeshInSalome()
        if Msg == None :
           self.viewmanager.handleAjoutGroup(listeGroup)
        else :
           print "il faut gerer les erreurs"

    def ChercheGrpMaille(self):
        Msg,listeGroup=self.ChercheGrpMailleInSalome()
        if Msg == None :
           self.viewmanager.handleAjoutGroup(listeGroup)
        else :
           print "il faut gerer les erreurs"


    def MAP(self): 
        pass
        #self.menuExecution = self.menubar.addMenu(QApplication.translate("Eficas", "Execution", None, QApplication.UnicodeUTF8))
        #self.menuExecution.setObjectName("menuExecution")
        #self.menuJdC.setTitle(QApplication.translate("Eficas", "Rapports", None, QApplication.UnicodeUTF8))

        #self.actionExecution = QAction(self)
        #icon6 = QIcon(self.RepIcon+"/compute.png")
        #self.actionExecution.setIcon(icon6)
        #self.actionExecution.setObjectName("actionExecution")
        #self.menuExecution.addAction(self.actionExecution)
        #self.toolBar.addAction(self.actionExecution)
        #self.actionExecution.setText(QApplication.translate("Eficas", "Execution Python", None, QApplication.UnicodeUTF8))
        #self.connect(self.actionExecution,SIGNAL("activated()"),self.run)

        #self.actionEnregistrer_Python = QAction(self)
        #self.actionEnregistrer_Python.setObjectName("actionEnregistrer_Python")
        #self.menuFichier.addAction(self.actionEnregistrer_Python)
        #self.actionEnregistrer_Python.setText(QApplication.translate("Eficas", "Sauve Script Run", None,QApplication.UnicodeUTF8))
        #self.connect(self.actionEnregistrer_Python,SIGNAL("activated()"),self.saveRun)

        #self.actionEnregistrerYACS = QAction(self)
        #self.actionEnregistrerYACS.setObjectName("actionEnregistrerYACS")
        #self.menuFichier.addAction(self.actionEnregistrerYACS)
        #self.actionEnregistrerYACS.setText(QApplication.translate("Eficas", "Sauve Schema YACS", None,QApplication.UnicodeUTF8))
        #self.connect(self.actionEnregistrerYACS,SIGNAL("activated()"),self.saveYACS)

        #self.actionExecutionYACS = QAction(self)
        #icon7 = QIcon(self.RepIcon+"/application.gif")
        #self.actionExecutionYACS.setIcon(icon7)
        #self.actionExecutionYACS.setObjectName("actionExecutionYACS")
        #self.menuExecution.addAction(self.actionExecutionYACS)
        #self.toolBar.addAction(self.actionExecutionYACS)
        #self.actionExecutionYACS.setText(QApplication.translate("Eficas", "Execution YACS", None, QApplication.UnicodeUTF8))
        #self.connect(self.actionExecutionYACS,SIGNAL("activated()"),self.runYACS)

    def OPENTURNS_STUDY(self):
        if hasattr(self,"menuOptions"):
           self.menuOptions.setAttribute(Qt.WA_DeleteOnClose)
           self.menuOptions.close()
           delattr(self,"menuOptions")
    
    def OPENTURNS_WRAPPER(self):
        if hasattr(self,"menuOptions"):
           self.menuOptions.setAttribute(Qt.WA_DeleteOnClose)
           self.menuOptions.close()
           delattr(self,"menuOptions")
    
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
        self.connect(self.actionRechercher,SIGNAL("activated()"),self.rechercher)
        self.connect(self.actionDeplier_replier,SIGNAL("activated()"),self.Deplier)

        self.connect(self.actionRapport_de_Validation,SIGNAL("activated()"),self.jdcRapport)
        self.connect(self.actionFichier_Source,SIGNAL("activated()"),self.jdcFichierSource)
        self.connect(self.actionFichier_Resultat,SIGNAL("activated()"),self.visuJdcPy)

        self.connect(self.actionParametres_Eficas,SIGNAL("activated()"),self.optionEditeur)
        self.connect(self.actionLecteur_Pdf,SIGNAL("activated()"),self.optionPdf)

        #self.connect(self.helpIndexAction,SIGNAL("activated()"),self.helpIndex)
        #self.connect(self.helpContentsAction,SIGNAL("activated()"),self.helpContents)
                             

    def Deplier(self):
        self.viewmanager.handleDeplier()

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
    # Mise a jour du menu des fichiers recemment ouverts
        from Editeur import listePatrons
        if not(self.code in listePatrons.sous_menus.keys()) :
           if hasattr(self,"menuPatrons"):
              self.menuPatrons.setAttribute(Qt.WA_DeleteOnClose)
              self.menuPatrons.close()
              delattr(self,"menuPatrons")
           return
        if (not hasattr(self,"menuPatrons")):
           self.menuPatrons = QMenu(self.menubar)
           self.menuPatrons.setObjectName("menuPatrons")
           self.menubar.addAction(self.menuPatrons.menuAction())
           self.menuPatrons.setTitle(QApplication.translate("Eficas", "Patrons", None, QApplication.UnicodeUTF8))
        else :
           self.menuPatrons.clear()
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
       self.recent.clear()
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
       try :
         rep=self.CONFIGURATION.rep_user
         monFichier=rep+"/listefichiers_"+self.code
       except :
         return
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
        traduction(self.CONFIGURATION.repIni,self.viewmanager,"V7V8")

    def traductionV8V9(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.repIni,self.viewmanager,"V8V9")

    def traductionV9V10(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.repIni,self.viewmanager,"V9V10")

    def version(self) :
        from monVisu import DVisu
        titre = "version "
        monVisuDialg=DVisu(parent=self,fl=0)
        monVisuDialg.setWindowTitle(titre)
        monVisuDialg.TB.setText(self.VERSION_EFICAS +QString(" pour ") + self.code)
        monVisuDialg.adjustSize()
        monVisuDialg.show()

    def aidePPal(self) :
        if self.code==None : return
        repAide=os.path.dirname(os.path.abspath(__file__))
        maD=repAide+"/../Aide"
        docsPath = QDir(maD).absolutePath()
        try :
          from PyQt4.QtAssistant import QAssistantClient
          monAssistant=QAssistantClient(QString(""), self)
          arguments=QStringList()
          arguments << "-profile" <<docsPath+QDir.separator()+QString("eficas_")+QString(self.code)+QString(".adp");
          monAssistant.setArguments(arguments);
          monAssistant.showPage(docsPath+QDir.separator()+QString("fichiers_"+QString(self.code)+QString("/index.html")))
        except:
          QMessageBox.warning( self, "Aide Indisponible", "QT Assistant n est pas installe ")


    def optionEditeur(self) :
        try :
           name='monOptions_'+self.code
        except :
           QMessageBox.critical( self, "Parametrage", "Veuillez d abord choisir un code")
           return
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
        fichier=self.repIni+"/../Editeur/Patrons/"+self.code+"/"+self.ficPatrons[idx]
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
        return self.viewmanager.saveCurrentEditor()
        
    def fileSaveAs(self):
        return self.viewmanager.saveAsCurrentEditor()
        
    def fileClose(self):
        self.viewmanager.handleClose(texte='&Fermer')
        
    def fileCloseAll(self):
        self.viewmanager.handleCloseAll(texte='&Fermer')
        
    def fileExit(self):
        # On peut sortir sur Abort
        res=self.viewmanager.handleCloseAll()
        if (res != 2) : 
            self.close()
        return res
        
    def editCopy(self):
        self.viewmanager.handleEditCopy()
      
    def editCut(self):
        self.viewmanager.handleEditCut()
    
    def editPaste(self):
        self.viewmanager.handleEditPaste()
        
    def rechercher(self):
        self.viewmanager.handleRechercher()
        
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

    def cleanPath(self):
        for pathCode in self.ListeCode:
            try:
            #if 1:
              aEnlever=os.path.abspath(os.path.join(os.path.dirname(__file__),'..',pathCode))
              sys.path.remove(aEnlever)
            except :
              pass
        for pathCode in self.listeAEnlever:
            try:
              sys.path.remove(aEnlever)
            except :
              pass
              

    def closeEvent(self,event):
      res=self.fileExit()
      if res==2 : event.ignore()

if __name__=='__main__':

    # Modules Eficas
    rep=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__),'..','ASTER')))
    sys.path.append(rep)
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
