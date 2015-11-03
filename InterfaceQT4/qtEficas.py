# -*- coding: iso-8859-1 -*-
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

import os, sys

from PyQt4.QtGui  import *
from PyQt4.QtCore import *
from myMain import Ui_Eficas
from viewManager import MyTabview
from getVersion import getEficasVersion

from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException

from Editeur import session


class Appli(Ui_Eficas,QMainWindow):
    """
    Class implementing the main user interface.
    """
    def __init__(self,code=None,salome=0,parent=None,ssCode=None,multi=False,langue='fr',ssIhm=False):
        """
        Constructor
        """
        QMainWindow.__init__(self,parent)
        Ui_Eficas.__init__(self)


        version=getEficasVersion()
        self.VERSION_EFICAS="Eficas QT4 "+version
        self.salome=salome
        self.ihm="QT"
        self.ssIhm=ssIhm
        self.top = self    #(pour CONFIGURATION)
        self.QWParent=None #(Pour lancement sans IHM)
        self.code=code
        self.indice=0
        self.dict_reels={}
        self.recent =  QStringList()
        self.ficRecents={}
        self.listeAEnlever=[]
        self.ListeCode=['Aster','Carmel3D','Cuve2dg','Openturns_Study','Openturns_Wrapper','MAP','ZCracks', 'CarmelCND','MT']
        self.repIcon=os.path.join( os.path.dirname(os.path.abspath(__file__)),'..','Editeur','icons')

        if self.salome:
          import Accas
          import eficasSalome
          Accas.SalomeEntry = eficasSalome.SalomeEntry

        self.multi=multi
        if self.multi == False :
             self.definitCode(code,ssCode)
             if code==None: return

        if not self.salome and hasattr(self.CONFIGURATION,'lang') : langue=self.CONFIGURATION.lang
        if langue=='fr': self.langue=langue
        else           : self.langue="ang"

        from Extensions import localisation
        app=QApplication
        localisation.localise(app,langue)

        self.setupUi(self)

        self.myQtab.removeTab(0)
        self.blEntete= QBoxLayout(0,self.frameEntete)
        self.blEntete.insertWidget(0,self.toolBar)
        self.blEntete.insertWidget(0,self.menubar)


        eficas_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.viewmanager = MyTabview(self)
        #self.recentMenu=self.menuFichier.addMenu(tr('&Recents'))
        self.recentMenu=QMenu(tr('&Recents'))
        #self.menuFichier.insertMenu(self.actionOuvrir,self.recentMenu)
        # actionARemplacer ne sert que pour l insert Menu
        self.menuFichier.insertMenu(self.actionARemplacer ,self.recentMenu)
        self.menuFichier.removeAction(self.actionARemplacer)
        self.connecterSignaux()
        self.toolBar.addSeparator()
        if self.code != None : self.construitMenu()

        self.setWindowTitle(self.VERSION_EFICAS)
        self.ouvreFichiers()



    def definitCode(self,code,ssCode) :
        self.code=code
        self.ssCode=ssCode
        if self.code==None :
           self.cleanPath()
           from monChoixCode import MonChoixCode
           widgetChoix = MonChoixCode(self)
           ret=widgetChoix.exec_()
        import sys
        if self.code == None:return # pour le cancel de la fenetre choix code
        name='prefs_'+self.code
        prefsCode=__import__(name)

        self.repIni=prefsCode.repIni
        if ssCode != None :
           self.format_fichier= ssCode  #par defaut
           prefsCode.NAME_SCHEME=ssCode
        else :
           self.format_fichier="python" #par defaut

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

    def construitMenu(self):
        self.initPatrons()
        self.initRecents()
        self.initAides()
        for intituleMenu in ("menuTraduction","menuOptions","menuMesh","menuExecution"):
              if hasattr(self,intituleMenu):
                 menu=getattr(self,intituleMenu)
                 menu.setAttribute(Qt.WA_DeleteOnClose)
                 menu.close()
                 delattr(self,intituleMenu)
        for intituleAction in ("actionExecution","actionSaveRun",):
            if hasattr(self,intituleAction):
              action=getattr(self,intituleAction)
              self.toolBar.removeAction(action)
        if self.code.upper() in Appli.__dict__.keys():
          listeTexte=apply(Appli.__dict__[self.code.upper()],(self,))

    def initAides(self):
        #print "je passe la"
        repAide=os.path.dirname(os.path.abspath(__file__))
        fileName='index.html'
        self.docPath=repAide+"/../Aide"
        if hasattr(self,'CONFIGURATION') and hasattr(self.CONFIGURATION,'docPath') : self.docPath=self.CONFIGURATION.docPath
        if hasattr(self,'CONFIGURATION') and hasattr(self.CONFIGURATION,'fileName'):fileName=self.CONFIGURATION.fileName
        self.fileDoc=os.path.join(self.docPath,fileName)
        self.actionCode.setText(tr("Aide specifique ")+str(self.code))
        if not os.path.isfile(self.fileDoc) :
               self.fileDoc=""
               self.docPath=""
               self.actionCode.setEnabled(False)
               return

        self.actionCode.setEnabled(True)
        self.menuAide.addAction(self.actionCode)


    def ajoutExecution(self):
        self.menuExecution = self.menubar.addMenu(QApplication.translate("Eficas", "Execution", None, QApplication.UnicodeUTF8))
        self.actionExecution = QAction(self)
        if sys.platform[0:5]=="linux":
          icon6 = QIcon(self.repIcon+"/roue.png")
          self.actionExecution.setIcon(icon6)
        else :
          self.actionExecution.setText(QApplication.translate("Eficas", "Run", None))
        self.actionExecution.setObjectName("actionExecution")
        self.menuExecution.addAction(self.actionExecution)
        if not(self.actionExecution in self.toolBar.actions()):
           self.toolBar.addAction(self.actionExecution)
        self.actionExecution.setText(QApplication.translate("Eficas", "Execution ", None, QApplication.UnicodeUTF8))
        self.connect(self.actionExecution,SIGNAL("triggered()"),self.run)

    def ajoutSauveExecution(self):
        self.actionSaveRun = QAction(self)
        icon7 = QIcon(self.repIcon+"/export_MAP.png")
        self.actionSaveRun.setIcon(icon7)
        self.actionSaveRun.setObjectName("actionSaveRun")
        self.menuExecution.addAction(self.actionSaveRun)
        if not(self.actionSaveRun in self.toolBar.actions()):
           self.toolBar.addAction(self.actionSaveRun)
        self.actionSaveRun.setText(QApplication.translate("Eficas", "Save Run", None, QApplication.UnicodeUTF8))
        self.connect(self.actionSaveRun,SIGNAL("triggered()"),self.saveRun)

    def griserActionsStructures(self):
        self.actionCouper.setEnabled(False)
        self.actionColler.setEnabled(False)
        self.actionCopier.setEnabled(False)
        self.actionSupprimer.setEnabled(False)

    def enleverActionsStructures(self):
        self.toolBar.removeAction(self.actionCopier)
        self.toolBar.removeAction(self.actionColler)
        self.toolBar.removeAction(self.actionCouper)
        self.menuEdition.removeAction(self.actionCouper)
        self.menuEdition.removeAction(self.actionCopier)
        self.menuEdition.removeAction(self.actionColler)


    def enleverParametres(self):
        self.toolBar.removeAction(self.actionParametres)
        self.menuJdC.removeAction(self.actionParametres)


    def enleverNewInclude(self):
        self.actionNouvel_Include.setVisible(False)

    def enleverRechercherDsCatalogue(self):
        self.actionRechercherDsCatalogue.setVisible(False)

    def ZCRACKS(self):
        self.enleverNewInclude()
        self.toolBar.addSeparator()
        self.ajoutExecution()

        self.menuOptions = self.menubar.addMenu("menuOptions")
        self.menuOptions.addAction(self.actionParametres_Eficas)
        self.menuOptions.setTitle(tr("Options"))

    def ADAO(self):
        self.enleverActionsStructures()
        self.enleverNewInclude()
        self.enleverRechercherDsCatalogue()

    def ASTER(self) :
        self.menuTraduction = self.menubar.addMenu("menuTraduction")
        self.menuTraduction.addAction(self.actionTraduitV11V12)
        self.menuTraduction.addAction(self.actionTraduitV10V11)
        self.menuTraduction.addAction(self.actionTraduitV9V10)
        self.menuTraduction.setTitle(tr("Traduction"))

        self.menuFichier.addAction(self.actionSauveLigne)

        self.menuOptions = self.menubar.addMenu("menuOptions")
        self.menuOptions.addAction(self.actionParametres_Eficas)
        self.menuOptions.addAction(self.actionLecteur_Pdf)
        self.menuOptions.setTitle(tr("Options"))

    def CARMEL3D(self):
        #if self.salome == 0 : return
        self.enleverNewInclude()
        self.menuMesh = self.menubar.addMenu(tr("Gestion Maillage"))
        self.menuMesh.setObjectName("Mesh")
        self.menuMesh.addAction(self.actionChercheGrpMaille)
        self.griserActionsStructures()

    def CARMELCND(self):
        self.enleverNewInclude()
        self.enleverRechercherDsCatalogue()
        self.ajoutExecution()
        self.ajoutSauveExecution()
        self.griserActionsStructures()
        
    def MAP(self):
        self.enleverNewInclude()
        self.toolBar.addSeparator()
        self.ajoutExecution()
        self.ajoutSauveExecution()
        self.menuOptions = self.menubar.addMenu("menuOptions")
        self.menuOptions.addAction(self.actionParametres_Eficas)
        self.menuOptions.setTitle(tr("Options"))

    def PSEN(self):
        self.enleverActionsStructures()
        self.enleverParametres()
        self.enleverRechercherDsCatalogue()
        self.enleverNewInclude()
        self.ajoutExecution()

    def TELEMAC(self):
        self.enleverActionsStructures()
        self.enleverNewInclude()

    def ChercheGrpMesh(self):
        Msg,listeGroup=self.ChercheGrpMeshInSalome()
        if Msg == None :
           self.viewmanager.handleAjoutGroup(listeGroup)
        else :
           print "il faut gerer les erreurs"

    def ChercheGrpMaille(self):
        # Normalement la variable self.salome permet de savoir si on est ou non dans Salome
        try:
            Msg,listeGroup=self.ChercheGrpMailleInSalome() # recherche dans Salomé
            #Msg = None; listeGroup = None # recherche manuelle, i.e., sans Salomé si ligne précédente commentée
        except:
            raise ValueError('Salome non ouvert')
        if Msg == None :
           self.viewmanager.handleAjoutGroup(listeGroup)
        else :
           print "il faut gerer les erreurs"


    def ChercheGrp(self):
        #Msg,listeGroup=self.ChercheGrpMailleInSalome()
        #if Msg == None :
        #   self.viewmanager.handleAjoutGroup(listeGroup)
        #else :
        print "il faut gerer "


    def ajoutIcones(self) :
        # Pour pallier les soucis de repertoire d icone
        icon = QIcon(self.repIcon+"/New24.png")
        self.action_Nouveau.setIcon(icon)
        icon1 = QIcon(self.repIcon+"/Open24.png")
        self.actionOuvrir.setIcon(icon1)
        icon2 = QIcon(self.repIcon+"/Save24.png")
        self.actionEnregistrer.setIcon(icon2)
        icon3 = QIcon(self.repIcon+"/Cut24.png")
        self.actionCouper.setIcon(icon3)
        icon4 = QIcon(self.repIcon+"/Copy24.png")
        self.actionCopier.setIcon(icon4)
        icon5 = QIcon(self.repIcon+"/Paste24.png")
        self.actionColler.setIcon(icon5)
        icon6 = QIcon(self.repIcon+"/Delete24.png")
        self.actionSupprimer.setIcon(icon6)



    def connecterSignaux(self) :
        self.connect(self.recentMenu,SIGNAL('aboutToShow()'),self.handleShowRecentMenu)

        self.connect(self.action_Nouveau,SIGNAL("triggered()"),self.fileNew)
        self.connect(self.actionNouvel_Include,SIGNAL("triggered()"),self.NewInclude)
        self.connect(self.actionOuvrir,SIGNAL("triggered()"),self.fileOpen)
        self.connect(self.actionEnregistrer,SIGNAL("triggered()"),self.fileSave)
        self.connect(self.actionEnregistrer_sous,SIGNAL("triggered()"),self.fileSaveAs)
        self.connect(self.actionFermer,SIGNAL("triggered()"),self.fileClose)
        self.connect(self.actionFermer_tout,SIGNAL("triggered()"),self.fileCloseAll)
        self.connect(self.actionQuitter,SIGNAL("triggered()"),self.fileExit)

        self.connect(self.actionEficas,SIGNAL("triggered()"),self.aidePPal)
        self.connect(self.actionVersion,SIGNAL("triggered()"),self.version)
        self.connect(self.actionParametres,SIGNAL("triggered()"),self.gestionParam)

        self.connect(self.actionCouper,SIGNAL("triggered()"),self.editCut)
        self.connect(self.actionCopier,SIGNAL("triggered()"),self.editCopy)
        self.connect(self.actionColler,SIGNAL("triggered()"),self.editPaste)
        self.connect(self.actionSupprimer,SIGNAL("triggered()"),self.supprimer)
        self.connect(self.actionRechercher,SIGNAL("triggered()"),self.rechercher)
        self.connect(self.actionDeplier_replier,SIGNAL("triggered()"),self.Deplier)

        self.connect(self.actionRapport_de_Validation,SIGNAL("triggered()"),self.jdcRapport)
        self.connect(self.actionRegles_du_JdC,SIGNAL("triggered()"),self.jdcRegles)
        self.connect(self.actionFichier_Source,SIGNAL("triggered()"),self.jdcFichierSource)
        self.connect(self.actionFichier_Resultat,SIGNAL("triggered()"),self.visuJdcPy)


        #self.connect(self.helpIndexAction,SIGNAL("triggered()"),self.helpIndex)
        #self.connect(self.helpContentsAction,SIGNAL("triggered()"),self.helpContents)

        # Pour Aster
        self.actionTraduitV9V10 = QAction(self)
        self.actionTraduitV9V10.setObjectName("actionTraduitV9V10")
        self.actionTraduitV9V10.setText(tr("TraduitV9V10"))
        self.actionTraduitV10V11 = QAction(self)
        self.actionTraduitV10V11.setObjectName("actionTraduitV10V11")
        self.actionTraduitV10V11.setText(tr("TraduitV10V11"))
        self.actionTraduitV11V12 = QAction(self)
        self.actionTraduitV11V12.setObjectName("actionTraduitV11V12")
        self.actionTraduitV11V12.setText(tr("TraduitV11V12"))
        self.actionSauveLigne = QAction(self)
        self.actionSauveLigne.setText(tr("Sauve Format Ligne"))

        self.connect(self.actionParametres_Eficas,SIGNAL("triggered()"),self.optionEditeur)
        self.connect(self.actionLecteur_Pdf,SIGNAL("triggered()"),self.optionPdf)
        self.connect(self.actionTraduitV9V10,SIGNAL("triggered()"),self.traductionV9V10)
        self.connect(self.actionTraduitV10V11,SIGNAL("triggered()"),self.traductionV10V11)
        self.connect(self.actionTraduitV11V12,SIGNAL("triggered()"),self.traductionV11V12)
        self.connect(self.actionSauveLigne,SIGNAL("triggered()"),self.sauveLigne)


        # Pour Carmel
        self.actionChercheGrpMaille = QAction(self)
        self.actionChercheGrpMaille.setText(tr("Acquiert groupe mailles"))
        self.connect(self.actionChercheGrpMaille,SIGNAL("triggered()"),self.ChercheGrpMaille)

        # Pour CarmelCND
        self.actionChercheGrp = QAction(self)
        self.actionChercheGrp.setText(tr("Acquisition Groupe Maille"))
        self.connect(self.actionChercheGrp,SIGNAL("triggered()"),self.ChercheGrp)

        # Pour Aide
        self.actionCode = QAction(self)
        self.actionCode.setText(tr("Specificites Maille"))
        self.connect(self.actionCode,SIGNAL("triggered()"),self.aideCode)

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
       self.recent =  QStringList()
       try :
       #if 1 :
           if sys.platform[0:5]=="linux" :
              rep=os.path.join(os.environ['HOME'],'.config/Eficas',self.code)
           else :
              rep=os.path.join('C:/','.config/Eficas',self.code)
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
       #else :
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
        index=0
        self.sauveRecents()

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



    def traductionV11V12(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.repIni,self.viewmanager,"V11V12")

    def traductionV10V11(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.repIni,self.viewmanager,"V10V11")

    def traductionV9V10(self):
        from gereTraduction import traduction
        traduction(self.CONFIGURATION.repIni,self.viewmanager,"V9V10")

    def version(self) :
        from monVisu import DVisu
        titre = tr("version ")
        monVisuDialg=DVisu(parent=self,fl=0)
        monVisuDialg.setWindowTitle(titre)
        monVisuDialg.TB.setText(self.VERSION_EFICAS +tr(" pour ") + self.code)
        monVisuDialg.adjustSize()
        monVisuDialg.show()

    def aidePPal(self) :
        if self.code==None : return
        repAide=os.path.dirname(os.path.abspath(__file__))
        maD=repAide+"/../Aide"
        try :
          indexAide=maD+"/fichiers_EFICAS/index.html"
          if sys.platform[0:5]=="linux" : cmd="xdg-open "+indexAide
          else                          : cmd="start "+indexAide
          os.system(cmd)
        except:
          QMessageBox.warning( self,tr( "Aide Indisponible"),tr( "l'aide n est pas installee "))


    def aideCode(self) :
        if self.code==None : return
        try :
        #if 1 :
          if sys.platform[0:5]=="linux" : cmd="xdg-open "+self.fileDoc
          else                          : cmd="start "+self.fileDoc
          os.system(cmd)
        except:
        #else:
          QMessageBox.warning( self,tr( "Aide Indisponible"),tr( "l'aide n est pas installee "))


    def optionEditeur(self) :
        try :
           name='monOptions_'+self.code
        except :
           QMessageBox.critical( self,tr( "Parametrage"),tr( "Veuillez d abord choisir un code"))
           return
        try :
        #if 1:
           optionCode=__import__(name)
        except :
        #else :
           QMessageBox.critical( self, tr("Parametrage"), tr("Pas de possibilite de personnalisation de la configuration "))
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
        self.recentMenu.addAction(tr('&Effacer'), self.handleClearRecent)

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
        try:
            self.viewmanager.newEditor()
        except EficasException, exc:
            msg = unicode(exc)
            if msg != "":
                QMessageBox.warning(self, tr(u"Erreur"), msg)

    def fileOpen(self):
        try:
            self.viewmanager.handleOpen()
        except EficasException, exc:
            msg = unicode(exc)
            if msg != "":
                QMessageBox.warning(self, tr(u"Erreur"), msg)

    def sauveLigne(self):
        return self.viewmanager.sauveLigneCurrentEditor()

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


    def supprimer(self):
        self.viewmanager.handleSupprimer()

    def jdcFichierSource(self):
        self.viewmanager.handleViewJdcFichierSource()

    def jdcRapport(self):
        self.viewmanager.handleViewJdcRapport()

    def jdcRegles(self):
        self.viewmanager.handleViewJdcRegles()

    def gestionParam(self):
        self.viewmanager.handlegestionParam()

    def visuJdcPy(self):
        self.viewmanager.handleViewJdcPy()


    def NewInclude(self):
        self.viewmanager.newIncludeEditor()

    def cleanPath(self):
        for pathCode in self.ListeCode:
            try:
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
