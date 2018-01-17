# -*- coding: utf-8 -*-
# Copyright (C) 2007-2017   EDF R&D
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
from __future__ import absolute_import
from __future__ import print_function
try :
   from builtins import str
   from builtins import range
except : pass

import types,sys,os, re
import  subprocess
import traceback
import six


from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QSplitter, QLabel
from PyQt5.QtGui     import QPalette
from PyQt5.QtCore    import QProcess, QFileInfo, QTimer, Qt, QDir, QSize

import traceback

# Modules Eficas
import convert, generator
from Extensions.i18n import tr

from Editeur        import session
from Editeur        import comploader
from Editeur        import Objecttreeitem
from InterfaceQT4   import browser
from InterfaceQT4   import readercata

from desBaseWidget    import Ui_baseWidget
from InterfaceQT4.monViewTexte   import ViewText
from monWidgetCreeParam import MonWidgetCreeParam 

DictExtensions= {"MAP" : ".map", "TELEMAC" : '.cas'}
debug = False

    
from InterfaceQT4.editorSsIhm    import JDCEditorSsIhm


class JDCEditor(JDCEditorSsIhm,Ui_baseWidget,QWidget):
# ----------------------------------------- #
    """
       Editeur de jdc
    """

# ----------------------------------------
# Methodes faisant appel a ssIhm
# ----------------------------------------

    def __init__ (self,appli,fichier = None, jdc=None, QWParent=None, units = None, include=0):
    #------------------------------------------------------------------------------------------


        QWidget.__init__(self,None)
        self.setupUi(self)

        self.inhibeSplitter=0
        self.widgetOptionnel=None
        self.fenetreCentraleAffichee=None
        self.dejaDansPlieTout=False
        self.afficheCommandesPliees = True
        self.listeDesListesOuvertes=set()
        self.afficheListesPliees=True
        if appli!=None and hasattr(appli,"statusBar"): self.sb = appli.statusBar()
        else : self.sb = None
        self.QWParent=QWParent

        JDCEditorSsIhm. __init__ (self,appli,fichier, jdc,units,include)

        # Particularites IHM : met la fenetre a jour

        self.initSplitterSizes()
        if self.code == "ASTER" or self.code == "monCode" : self.afficheListesPliees =True
        if self.code == 'PSEN_N1' : self.afficheListesPliees = False

        #self.affiche=self.appliEficas.maConfiguration.affiche

        if self.code in ['MAP','CARMELCND','PSEN'] : self.afficheCommandesPliees=False
        #if self.code in ['MAP','CARMELCND'] : self.afficheCommandesPliees=False
        if self.code in ['MAP',]: self.fermeArbre()
        #   self.widgetTree.close()
        #   self.widgetTree=None

        if self.maConfiguration.closeArbre: self.fermeArbre()
        if self.maConfiguration.boutonDsMenuBar : self.appliEficas.remplitIconesCommandes()

        self.version_code = session.d_env.cata
     
        self.format =  self.appliEficas.format_fichier

        self.node_selected = []
        self.deplier = True
        self.message=''
        if self.code in ['Adao','ADAO','MAP'] : self.afficheApresInsert=True
        else                                  : self.afficheApresInsert=False
        if self.code in ['TELEMAC',]          : self.enteteQTree='premier'
        else                                  : self.enteteQTree='complet'
        if self.code in ['Adao','ADAO','TELEMAC'] : self.affichePlie=True
        else                                      : self.affichePlie=False

        self.Commandes_Ordre_Catalogue =self.readercata.Commandes_Ordre_Catalogue

        if self.jdc_item and self.appliEficas.ssIhm==False :
            self.tree = browser.JDCTree( self.jdc_item,  self )
        self.appliEficas.construitMenu()

        self.adjustSize()


    #-------------------------------#
    def readFile(self, fn):
    #--------------------------------#
        """
        Public slot to read the text from a file.
        @param fn filename to read from (string or QString)
        """

        jdc=JDCEditorSsIhm.readFile(self, fn)

        # Particularites IHM : met le titre de la fenetre a jour
#        qApp.restoreOverrideCursor()
        if self.fileInfo!= None : self.lastModified = self.fileInfo.lastModified()
        nouveauTitre=self.titre+"              "+os.path.basename(self.fichier)
        self.appliEficas.setWindowTitle(nouveauTitre)

        return jdc

# ---------------------------------------------
# Methodes Inchangees
# ---------------------------------------------
#   _newJDC
#   _newJDCInclude
#   __generateTempFilename
#   getSource
#   generDico
#   viewJdcSource
#   viewJdcPy
#   viewJdcRapport
#   getFileName
#   initModif
#   writeFile
#   getTextJDC
#   verifieChecksum
#   getChecksum
#   getDico
#   chercheGroupes
#   chercheDico
#   saveFileLegerAs

# ---------------------------------------------
# Methodes Surchargees 
# ---------------------------------------------

    #-----------------------------------------------------------------------#
    def _viewText(self, txt, caption = "FILE_VIEWER",largeur=1200,hauteur=600):
    #--------------------------------------------------------------------#
        w = ViewText( self.QWParent,self ,caption,txt,largeur,hauteur)
        w.show()

    #--------------------------------#
    def informe(self,titre,txt,critique=True):
    #--------------------------------#
       if  critique :
           self.afficheInfos(tr(txt),Qt.red)
           QMessageBox.critical( self, tr(titre), tr(txt))
       else :
           QMessageBox.warning( self, tr(titre),tr(txt))

    #--------------------------------#
    def ajoutCommentaire(self):
    #--------------------------------#
        if self.tree.selectedItems()==[] :
          QMessageBox.warning( self, tr("Pas de noeud selectionne"),tr("Selectionnez un Noeud \nLe commentaire sera place apres le noeud selectionne"))
          return 
        noeudAvantCommentaire=self.tree.selectedItems()[0]
        if noeudAvantCommentaire ==self.tree.racine : 
            self.tree.racine.appendChild("COMMENTAIRE",pos=0)
            return
        noeudAvantCommentaire.addComment(True)


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
        self.monExe.readyReadStandardOutput.connect( self.readFromStdOut)
        self.monExe.readyReadStandardError.connect( self.readFromStdErr)
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
        self.w.view.append(str(a.data()))

    def readFromStdOut(self) :
        a=self.monExe.readAllStandardOutput()
        self.w.view.append(str(a.data()))

        
    #-----------------------#
    def gestionParam(self):
    #-----------------------#
        w = MonWidgetCreeParam( self)
        w.show()


    #----------------#
    def closeIt(self):
    #----------------#
        """
        Public method called by the viewmanager to finally get rid of us.
        """
        if self.jdc: self.jdc.supprime()
        self.close()

    #----------------------------------------------#
    def afficheInfos(self,message,couleur=Qt.black):
    #----------------------------------------------#
        if couleur=='red' : couleur = Qt.red
        if self.sb:
           mapalette=self.sb.palette()
           mapalette.setColor( QPalette.WindowText, couleur )
           self.sb.setPalette( mapalette );
           self.sb.showMessage(message,4000)
           self.couleur=couleur

    #------------------------------#
    def afficheAlerte(self,titre,message):
    #------------------------------#
    # appele par I_MACRO_ETAPE
        QMessageBox.information( self, titre, message)

    #-----------------------------------#
    def afficheCommentaire(self,message):
    #-----------------------------------#
        self.labelCommentaire.setText(message)
        QTimer.singleShot(6000, self.rendInvisible)

    #----------------------#
    def rendInvisible(self):
    #----------------------#
        self.labelCommentaire.setText("")

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
      from .monRecherche import DRecherche
      monRechercheDialg=DRecherche(parent=self,fl=0)
      monRechercheDialg.show()


    #--------------------------------#
    def handleRechercherDsCatalogue(self):
    #-----------------------------#
      from .monRechercheCatalogue import DRechercheCatalogue
      monRechercheDialg=DRechercheCatalogue(self.QWParent,self)
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
      if len(self.node_selected) == 1 : self.node_selected[0].updateNodeLabelInBlue()
      else :  self.node_selected[0].updatePlusieursNodeLabelInBlue(self.node_selected)
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
      noeudOuColler=self.node_selected[0]

      if len(self.QWParent.noeud_a_editer)!=1:
         #self.handleEditPasteMultiple()
         QMessageBox.information( self, tr("Copie impossible"), tr("Aucun Objet n a ete copie ou coupe"))
         return

      noeudACopier=self.QWParent.noeud_a_editer[0]

      if (self.QWParent.edit != "couper"):
        #print   (noeudOuColler.item.parent.getChild(noeudOuColler.item.nom)) 
        try:
           if noeudOuColler == self.tree.racine :
               child=noeudOuColler.doPastePremier(noeudACopier)
           else :
               child=noeudACopier.doPaste(noeudOuColler,'after')

           if child==None or child==0:
               QMessageBox.critical( self,tr( "Copie refusee"),tr('Eficas n a pas reussi a copier l objet'))
               self.message = ''
               self.afficheInfos("Copie refusee",Qt.red)
           if noeudACopier.treeParent.editor != noeudOuColler.treeParent.editor:
               try :
                 nom=noeudACopier.item.sd.nom
                 child.item.nommeSd(nom)
               except :
                 pass
           return
           self.initModif()
           child.select()
        except  :
           traceback.print_exc()
           QMessageBox.critical( self,tr( "Copie refusee"),tr('Copie refusee pour ce type d objet'))
           self.message = ''
           self.afficheInfos("Copie refusee",Qt.red)
           return

      # il faut declarer le JDCDisplay_courant modifie
      # suppression eventuelle du noeud selectionne
      # si possible on renomme l objet comme le noeud couper

      if (self.QWParent.edit == "couper"):
         print ('je pass la')
         if noeudACopier.treeParent.editor != noeudOuColler.treeParent.editor:
           QMessageBox.critical( self, tr("Deplacement refuse"),tr('Deplacement refuse entre 2 fichiers. Seule la copie est autorisee '))

         #if 1:
         try :
           # indexNoeudACopier=noeudACopier.treeParent.children.index(noeudACopier)
            indexNoeudACopier=self.getTreeIndex(noeudACopier)
            noeudACopier.treeParent.item.deplaceEntite(indexNoeudACopier,indexNoeudOuColler,pos)
            noeudACopier.treeParent.buildChildren()

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
         self.tree.item.suppItem(listeItem[i])
         listeChild[i].item.update(listeItem[i])

     self.QWParent.noeud_a_editer = []

    #----------------------------------#
    def handleAjoutEtape(self,nomEtape):
    #----------------------------------#
      self.chercheNoeudSelectionne()
      if len(self.node_selected) == 0 or self.node_selected[0] == self.tree.racine : 
         nodeOuAjouter=self.tree.racine
         nouveau=nodeOuAjouter.appendChild(nomEtape,pos='first')
      else :               
         nodeOuAjouter=self.node_selected[0]
         if nodeOuAjouter != self.tree.racine :
            while  nodeOuAjouter.treeParent != self.tree.racine:
                   print (nodeOuAjouter)
                   nodeOuAjouter=nodeOuAjouter.treeParent
                   print (nodeOuAjouter.parent == self.tree.racine)
         nouveau=nodeOuAjouter.appendBrother(nomEtape)
      try : 
        self.node_selected[0].setSelected(False)
      except : pass
      nouveau.setSelected(True)
      nouveau.affichePanneau()


    #---------------------------#
    def getFileVariable(self) :
    #---------------------------#
     titre = tr("Choix d'un fichier XML")
     texte = tr("Le fichier contient une commande MODEL\n")
     texte = texte+tr('Donnez le nom du fichier XML qui contient la description des variables')
     QMessageBox.information( self, titre,tr(texte))

     fichier = QFileDialog.getOpenFileName(self.appliEficas,
                   tr('Ouvrir Fichier'),
                   self.appliEficas.maConfiguration.savedir,
                   tr('Wrapper Files (*.xml);;''All Files (*)'))
     return  fichier

    #------------#
    def run(self):
    #------------#
      fonction="run"+self.code
      #print fonction
      if fonction in JDCEditor.__dict__: JDCEditor.__dict__[fonction](self,)

    #------------#
    def saveRun(self):
    #------------#
      fonction="saveRun"+self.code
      if fonction in JDCEditor.__dict__: JDCEditor.__dict__[fonction](self,)


# ---------------------------------------------
# Methodes Non Crees dans ssIHM 
# ---------------------------------------------

    #---------------#
    def runMAP(self):
    #---------------#

      if not(self.jdc.isValid()):
         QMessageBox.critical( self, tr( "Execution impossible "),tr("le JDC doit etre valide pour une execution MAP"))
         return
      if len(self.jdc.etapes) != 1 :
         QMessageBox.critical( self, tr("Execution impossible "),tr("le JDC doit contenir un et un seul composant"))
         return
      if self.modified or self.fichier==None  :
         self.fichierMapInput = self.__generateTempFilename(prefix = "map_run", suffix = ".map")
         texte=self.getTextJDC("MAP")
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
      except Exception as e:
          print((traceback.print_exc()))

    #-------------------#
    def runZCRACKS(self):
    #-------------------#
      if not(self.jdc.isValid()):
         QMessageBox.critical( self, tr( "Execution impossible "),tr("le JDC doit etre valide pour une execution "))
         return
      if self.modified or self.fichier==None  :
      #if 1:
         self.fichierZcracksInput = self.__generateTempFilename(prefix = "zcracks_run", suffix = ".z7p")
         texte=self.getTextJDC("ZCRACKS",pourRun=1)
         self.writeFile( self.fichierZcracksInput, txt = texte)
      else :
         self.fichierZcracksInput=self.fichier
      try :
          #commande ="Zrun -zp "
          commande="more "
          textePython=(commande + self.fichierZcracksInput)
          self._viewTextExecute( textePython,"run_zcracks",".sh")
      except Exception as e:
          print((traceback.print_exc()))

    #-------------------#
    def runCARMELCND(self):
    #-------------------#
      #if not(self.jdc.isValid()):
      #   QMessageBox.critical( self, tr( "Execution impossible "),tr("le JDC doit etre valide pour une execution "))
      #   return
      if self.modified or self.fichier==None  :
         QMessageBox.critical( self, tr( "Execution impossible "),tr("Sauvegarder SVP avant l'execution "))
         return
      if not hasattr(self,'generator'): texte=self.getTextJDC(self.format)
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

    #-------------------#
    def runCarmelCS(self):
    #-------------------#
      try :
          commande="runSession pilotyacsCS.py"
          os.system(commande)
      except Exception as e:
          print((traceback.print_exc()))

    #-----------------------------------------------------#
    def determineNomFichier(self,path,extension):
    #-----------------------------------------------------#
      if self.appli.code in DictExtensions:
         chaine1=DictExtensions[self.appli.code]+" (*."+DictExtensions[self.appli.code]+");;"
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
      fn=fn[0]
      if fn=='': return (0, None)

      ext = QFileInfo(fn).suffix()
      if ext == '': fn+=extension

      if QFileInfo(fn).exists():
           msgBox = QMessageBox(self)
           msgBox.setWindowTitle(tr("Sauvegarde du Fichier"))
           msgBox.setText(tr("Le fichier <b>%s</b> existe deja.", six.text_type(fn)))
           msgBox.addButton(tr("&Ecraser"),0)
           msgBox.addButton(tr("&Abandonner"),1)
           abort=msgBox.exec_()
           if abort == 1 :  return (0, "")
      return (1,fn)

    #-----------------#
    def saveRunMAP(self):
    #-----------------#
        extension=".input"
        if not(self.jdc.isValid()):
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
        if hasattr(self.maConfiguration, "savedir"): path=self.maConfiguration.savedir
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
                     if avant=="&Open": b.setText("Save")
        mesFiltres= "input Map (*.input);;All Files (*)"
        monDialog.setNameFilters(mesFiltres)
        if monNomFichier!="" : monDialog.selectFile(monNomFichier)
        BOk=monDialog.exec_()
        if BOk==0: return
        fn=str(monDialog.selectedFiles()[0])
        if fn == "" or fn == None : return
        if not fn.endswith(".input"):
            fn += ".input"
        self.monNomFichierInput=fn

        if not hasattr(self, 'fichierMapInput') or not self.fichierMapInput or not os.path.exists(self.fichierMapInput):
            self.fichierMapInput = self.__generateTempFilename(prefix = "map_run", suffix = ".map")
            texte=self.getTextJDC("MAP")
            self.writeFile( self.fichierMapInput, txt = texte)

        cmd = ("map gen -t dat -n " + composant + " -i " + self.fichierMapInput + " -o " + fn)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        (output, err) = p.communicate()


    #-----------------#
    def saveRunPSEN(self):
    #-----------------#
        #print ("saveRunPSEN")
        self.saveFile()



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
    def saveFileLeger(self, path = None, saveas= 0,formatLigne="beautifie"):
    #-----------------------------------------------------------------#
        extension='.casR'
        fn = self.fichier
        #saveas=True # Pour forcer le nom
        self.generator=generator.plugins[self.format]()
        if self.fichier is None or saveas:
          if path is None: path=self.maConfiguration.savedir
          bOK, fn=self.determineNomFichier(path,extension)
          if bOK == 0 : return (0, None)
          if fn == None : return (0, None)
          if fn== '' : return (0, None)

          ulfile = os.path.abspath(six.text_type(fn))
          self.appliEficas.maConfiguration.savedir=os.path.split(ulfile)[0]
          fn = six.text_type(QDir.toNativeSeparators(fn))

        self.fichier = os.path.splitext(fn)[0]+extension

        if hasattr(self.generator, "writeLeger"):
            self.generator.writeLeger(self.fichier,self.jdc,config=self.appliEficas.maConfiguration,appli=self.appliEficas)

        if self.salome : self.appliEficas.addJdcInSalome( self.fichier)

        self.modified = 0
        nouveauTitre=self.titre+"              "+str(os.path.basename(self.fichier))
        self.appliEficas.setWindowTitle(nouveauTitre)
        return (1, self.fichier)

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

        if self.appli.code in DictExtensions :
           extension=DictExtensions[self.appli.code]
        else :
           extension='.comm'

        newName = None
        fn = self.fichier
        if self.fichier is None or saveas:
          if path is None: path=self.maConfiguration.savedir
          bOK, fn=self.determineNomFichier(path,extension)
          if bOK == 0 : return (0, None)
          if fn == None : return (0, None)
          if fn== '' : return (0, None)

          ulfile = os.path.abspath(six.text_type(fn))
          self.appliEficas.maConfiguration.savedir=os.path.split(ulfile)[0]
          fn = six.text_type(QDir.toNativeSeparators(fn))
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
           self.tree.racine.updateNodeLabel()


        if self.jdc.isValid() != 0 and hasattr(self.generator, "writeDefault"):
        #if hasattr(self.generator, "writeDefault"):
            self.generator.writeDefault(fn)
        elif self.code=="TELEMAC" and hasattr(self.generator, "writeDefault"):
            msgBox = QMessageBox(None)
            msgBox.setWindowTitle(tr("Fichier Cas invalide"))
            msgBox.setText(tr("Le fichier cas est invalide"))
            msgBox.addButton(tr("&Sauvegarder"),1)
            msgBox.addButton(tr("&Quitter sans sauvegarder"),0)
            msgBox.addButton(tr("&Annuler"),2)
            res=msgBox.exec_()
            if res == 0 :
               self.generator.writeDefault(fn)
               return (1, self.fichier)
            if res == 2 : return (0, None)
            if self.appliEficas.salome : self.appliEficas.close()
            else : sys.exit(1)

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
    def getFile(self,unite=None,fic_origine = ''):
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
                   self.appliEficas.maConfiguration.savedir)

        # ce retour est impose par le getFile d'I_JDC
        if fn== '' : return None," "
        if not fn : return (0, " ")
        fn=fn[0]

        ulfile = os.path.abspath(six.text_type(fn))
        self.appliEficas.maConfiguration.savedir=os.path.split(ulfile)[0]

        # On utilise le convertisseur defini par format_fichier
        source=self.getSource(ulfile)
        if source:
            # On a reussia convertir le fichier self.ulfile
            jdcText = source
        else:
            # Une erreur a ete rencontree
            jdcText = ''
        return ulfile, jdcText

    #-----------------------------------#
    def updateJdc(self, itemApres,texte):
    #------------------------------------#
    # ajoute une etape  de JdC a partir d un texte
        monItem=itemApres
        etape=monItem.item.object
        CONTEXT.setCurrentStep(etape)
        etape.buildIncludeInclude(texte)
        self.tree.racine.buildChildren()

    #-----------------------------------#
    def updateJdcEtape(self, itemApres,texte):
    #------------------------------------#
    # ajoute une etape  de JdC a partir d un texte
        monItem=itemApres
        etape=monItem.item.object
         
        CONTEXT.setCurrentStep(etape)
        try :
          ok=etape.buildIncludeEtape(texte)
        except :
          ok=0
        if not ok :
           QMessageBox.information( self,
                      tr("Import texte"),
                      tr("Impossible d importer le texte"))
        self.tree.racine.buildChildren()
        return ok

    #-------------------------------------------#
    def updateJdcAfterEtape(self, etape,texte):
    #--------------------------------------------#
    # ajoute une etape  de JdC a partir d un texte
        CONTEXT.setCurrentStep(etape)
        try :
          ok=etape.buildIncludeEtape(texte,doitEtreValide=0)
        except :
          ok=0
        if not ok :
           QMessageBox.information( self,
                      tr("Import texte"),
                      tr("Impossible d importer le texte"))
        self.tree.racine.buildChildren()
        return ok


    #-------------------------------------#
    def deleteEtape(self,etape):
    #-------------------------------------#
    # dans le JDC
        self.jdc.suppEntite(etape)

    #-------------------------------------#
    def deleteMC(self,etape,MCFils,listeAvant=()):
    #-------------------------------------#
    # dans le JDC
        ouChercher=etape
        for mot in listeAvant :
              ouChercher=ouChercher.getChild(mot,restreint="oui")
        monMC=ouChercher.getChild(MCFils,restreint="oui")
        if monMC != None :  ouChercher.suppEntite(monMC)
        ouChercher.state='changed'
        ouChercher.isValid()

    #-------------------------------------#
    def ajoutMC(self,etape,MCFils,valeurs,listeAvant=()):
    #-------------------------------------#
    # dans le JDC
        ouChercher=etape
        for mot in listeAvant :
              ouChercher=ouChercher.getChild(mot,restreint="oui")
        monMC=etape.getChild(ouChercher,restreint="oui")
        if monMC== None : monMC= ouChercher.addEntite(MCFils)
        monMC.valeur=valeurs
        monMC.val=valeurs
        monMC.state='changed'
        monMC.isValid()

    #----------------------------------------------#
    def ajoutMCFact(self,etape,MCFils,listeAvant=()):
    #----------------------------------------------#
    # dans le JDC
        print ('ajoutMCFact')
        ouChercher=etape
        print (ouChercher)
        for mot in listeAvant :
              ouChercher=ouChercher.getChild(mot,restreint="oui")
              print (mot)
              print (ouChercher)
        monMC=etape.getChild(ouChercher,restreint="oui")
        if monMC== None : monMC= ouChercher.addEntite(MCFils)
        monMC.isValid()

    #-------------------------------------------------#
    def getValeur(self,nomEtape,MCFils,listeAvant=()):
    #-------------------------------------------------#
    # dans le JDC

        ouChercher=None
        for e in self.jdc.etapes:
            if e.nom == nomEtape : ouChercher=e; break
        if debug : print ('etape trouvee', ouChercher)
        if ouChercher==None : return None
        for mot in listeAvant :
              ouChercher=ouChercher.getChild(mot,restreint="oui")
              if debug : print (mot, ouChercher)
              if ouChercher==None : return None
        monMC=ouChercher.getChild(MCFils,restreint="oui")
        if debug : print ('monMC', monMC)
        if monMC== None : return None
        return monMC.valeur

    #-----------------------------------------------------------#
    def setValeur(self,nomEtape,MCFils,valeur,listeAvant=()):
    #--------------------------------------------------------#
    # dans le JDC

        ouChercher=None
        for e in self.jdc.etapes:
            if e.nom == nomEtape : ouChercher=e; break
        if ouChercher==None : return None
        for mot in listeAvant :
              ouChercher=ouChercher.getChild(mot,restreint="oui")
              #print (mot, ouChercher)
              if ouChercher==None : return None
        monMC=ouChercher.getChild(MCFils,restreint="oui")
        monMC.setValeur(valeur)
        monMC.isValid()

    #-----------------------------------------------------------#
    def changeIntoMC(self,etape,MCFils,valeurs, listeAvant=()):
    #-----------------------------------------------------------#
    # dans le JDC
        ouChercher=etape
        if isinstance (etape, str):
           ouChercher=None
           for e in self.jdc.etapes:
              if e.nom == etape : ouChercher=e; break
        if ouChercher==None : return
 
        for mot in listeAvant :
              ouChercher=ouChercher.getChild(mot,restreint="oui")
              if ouChercher==None : return 
        monMC=ouChercher.getChild(MCFils,restreint="oui")
        if monMC== None : monMC= ouChercher.addEntite(MCFils)

        monMC.definition.into=valeurs
        from Noyau.N_VALIDATOR import  IntoProtocol
        monMC.definition.intoProto = IntoProtocol("into", into=monMC.definition.into, val_min=monMC.definition.val_min, val_max=monMC.definition.val_max)
        monMC.state='changed'
        monMC.isValid()

    #-------------------------------------------------------------------#
    def reCalculeValiditeMCApresChgtInto(self,nomEtape,MCFils,listeAvant=()):
    #-------------------------------------------------------------------#
    # dans le JDC
        for e in self.jdc.etapes:
            if e.nom == nomEtape : ouChercher=e; break
        
        for mot in listeAvant :
            try :
              ouChercher=ouChercher.getChild(mot,restreint="oui")
            # Le mot clef n est pas la
            except : return 0
        try :
           monMC=ouChercher.getChild(MCFils,restreint="oui")
        # Le mot clef n est pas la
        except : return 0
        if monMC == None : return 0

        if hasattr(monMC.definition,'into') :
           if type(monMC.definition.into) ==types.FunctionType : maListeDeValeur=monMC.definition.into()
           else : maListeDeValeur=monMC.definition.into
        else :
           return 0
        
        monMC.state='changed'
        return 1

    #-------------------------------------#
    def changeDefautDefMC(self,nomEtape,listeMC,valeurs):
    #-------------------------------------#
    # dans le MDD

        #if isinstance (etape, str):
        #  for e in self.jdc.etapes:
        #    if e.nom == etape : etape=e; break
        #if etape == None : return
        definitionEtape=getattr(self.jdc.cata[0],nomEtape)
        ouChercher=definitionEtape
        if len(listeMC) > 1 :

           for mc in listeMC[0:-1]:
             mcfact=ouChercher.entites[mc]
             ouChercher=mcfact
           
        mcAccas=ouChercher.entites[listeMC[-1]]
        mcAccas.defaut=valeurs
        return 1

    #------------------------------------------------#
    def changeIntoDefMC(self,nomEtape,listeMC,valeurs):
    #------------------------------------------------#
    # dans le MDD
        definitionEtape=getattr(self.jdc.cata[0],nomEtape)
        ouChercher=definitionEtape

        if len(listeMC) > 1 :
           for mc in listeMC[0:-1]:
             mcfact=ouChercher.entites[mc]
             ouChercher=mcfact
        mcAccas=ouChercher.entites[listeMC[-1]]

        if hasattr(mcAccas,'into') : oldValeurs=mcAccas.into
        else : oldValeurs=None
        if oldValeurs==valeurs : return 0

        mcAccas.into=valeurs
        from Noyau.N_VALIDATOR import  IntoProtocol
        mcAccas.intoProto = IntoProtocol("into", into=valeurs, val_min=mcAccas.val_min, val_max=mcAccas.val_max)
        return 1

    #-------------------------------------------------------------#
    def deleteDefinitionMC(self,etape,listeAvant,nomDuMC):
    #-------------------------------------------------------------#
    # dans le MDD
        #print 'in deleteDefinitionMC', etape,listeAvant,nomDuMC
        if isinstance (etape, str):
          for e in self.jdc.etapes:
            if e.nom == etape : etape=e; break
        if etape == None : return
        definitionEtape=getattr(self.jdc.cata[0],etape)
        ouChercher=definitionEtape
        for k in listeAvant : 
            ouChercher=ouChercher.entites[k]
        MCADetruire=ouChercher.entites[nomDuMC]
        ouChercher.ordre_mc.remove(nomDuMC)
        print ('remove de ', nomDuMC)
        del ouChercher.entites[nomDuMC]
        del self.dicoNouveauxMC[nomDuMC]


    #-------------------------------------------------------------#
    def ajoutDefinitionMC(self,nomEtape,listeAvant,nomDuMC,typ,**args):
    #-------------------------------------------------------------#
    # dans le MDD
        definitionEtape=getattr(self.jdc.cata[0],nomEtape)
        ouChercher=definitionEtape
        for k in listeAvant : 
            ouChercher=ouChercher.entites[k]
        from Accas import A_SIMP
        Nouveau=A_SIMP.SIMP(typ,**args)
        Nouveau.pere=ouChercher
        Nouveau.nom=nomDuMC
        #Nouveau.ordre_mc=[]
        ouChercher.entites[nomDuMC]=Nouveau
        ouChercher.ordre_mc.append(nomDuMC)
        #print ('ajout de ', nomDuMC)
        #traceback.print_stack()
        # ajout CIST sauvegarde
        if nomDuMC in self.dicoNouveauxMC : del self.dicoNouveauxMC[nomDuMC]
        self.dicoNouveauxMC[nomDuMC]=('ajoutDefinitionMC',nomEtape,listeAvant,nomDuMC,typ,args)
        #print self.dicoNouveauxMC

    #---------------------------------------------------------------------#
    def ajoutDefinitionMCFact(self,nomEtape,listeAvant,nomDuMC,listeMC,**args):
    #---------------------------------------------------------------------#
    # dans le MDD
        print ('ajoutDefinitionMCFact', nomDuMC)
        definitionEtape=getattr(self.jdc.cata[0],nomEtape)
        ouChercher=definitionEtape
        for k in listeAvant : 
            ouChercher=ouChercher.entites[k]
        from Accas import A_SIMP
        for mc in listeMC :
            nomMC=mc[0]
            typMC=mc[1]
            argsMC=mc[2]
            nouveauMC=A_SIMP.SIMP(typMC,**argsMC)
            nouveauMC.nom=nomMC
            args[nomMC]=nouveauMC
        from Accas import A_FACT
        nouveauFact=A_FACT.FACT(**args)
        nouveauFact.pere=ouChercher
        nouveauFact.nom=nomDuMC
        from Editeur.autre_analyse_cata import traiteEntite
        traiteEntite(nouveauFact,[])
        ouChercher.entites[nomDuMC]=nouveauFact
        ouChercher.ordre_mc.append(nomDuMC)
        self.dicoNouveauxFact[nomDuMC]=('ajoutDefinitionMC',nomEtape,listeAvant,nomDuMC,listeMC,args)
        #print self.dicoNouveauxMC

    #----------------------------------------------------#

    #----------------------------------------------------#
    def changeIntoMCandSet(self,etape,listeMC,into,valeurs):
    #----------------------------------------------------#
    # dans le MDD et le JDC

        self.changeIntoDefMC(etape,listeMC,into)

        if isinstance (etape, str):
          for e in self.jdc.etapes:
            if e.nom == etape : etape=e; break
        if etape == None : return

        ouChercher = etape
        for mot in listeMC[:-1] :
            ouChercher=ouChercher.getChild(mot,restreint="oui")
            if ouChercher==None : return 
        MCFils=listeMC[-1]
        monMC=ouChercher.getChild(MCFils,restreint="oui")
        if monMC== None : monMC= etape.addEntite(MCFils)

        monMC.definition.into=into
        monMC.valeur=valeurs
        monMC.val=valeurs
        monMC.state='changed'
        monMC.isValid() 

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



    #-----------------------------------------
    def initSplitterSizes(self, nbWidget=3):
    #-----------------------------------------
       #print ("je passe ds initSplitterSizes", nbWidget)

       if   self.code in [ 'Adao', 'ADAO','MAP' ] : self.splitterSizes3=[1,1550,150]
       #elif self.code in [ 'MAP']            : self.splitterSizes3=[700,300]
       else                                  : self.splitterSizes3=[150,1000,300]

       if   self.code in [ 'Adao', 'ADAO','MAP' ] : self.splitterSizes2=[5,1500]
       else                                  : self.splitterSizes2=[300,1000]


    #-----------------------------------------
    def restoreSplitterSizes(self,nbWidget=3):
    #----------------------------------------
      
      #traceback.print_stack()
      #print ("je passe ds restoreSplitterSizes")
      if not(hasattr(self,'splitter')) : return
      if nbWidget==2  : newSizes=self.splitterSizes2
      if nbWidget==3  : newSizes=self.splitterSizes3
      #self.inhibeSplitter = 1
      self.splitter.setSizes(newSizes)
      #self.inhibeSplitter = 0
      QApplication.processEvents()
      # seule la fentetre du milieu est necessaire
      self.splitter.widget(1).resizeEvent=self.saveSplitterSizes
   
    #-----------------------------------------
    def saveSplitterSizes(self,event):
    #-----------------------------------------
      #print ("je passe ds saveSplitterSizes")
      if self.inhibeSplitter : return
      if self.widgetOptionnel == None  : self.splitterSizes2 = self.splitter.sizes()[0:2]
      else                             : self.splitterSizes3 = self.splitter.sizes()[0:3]

    #------------------------
    def fermeOptionnel(self):
    #------------------------
      if self.widgetOptionnel == None : return

      self.inhibeSplitter=1
      self.widgetOptionnel.setParent(None)
      self.widgetOptionnel.close()
      self.widgetOptionnel.deleteLater()
      self.widgetOptionnel=None
      self.inhibeSplitter=0
      self.restoreSplitterSizes(2)

    #------------------------
    def ajoutOptionnel(self):
    #------------------------
      #if len(self.splitterSizes) == 2 : self.splitterSizes.append(self.oldSizeWidgetOptionnel)
      #else : self.splitterSizes[2] = self.oldSizeWidgetOptionnel # ceinture pour les close bizarres
      #self.splitterSizes[1] = self.splitterSizes[1] - self.splitterSizes[2]
      
      self.restoreSplitterSizes(3)


    #------------------------
    def fermeArbre(self):
    #------------------------
       #print (self.widgetTree)
       self.oldWidgetTree=self.widgetTree
       self.widgetTree.hide()
       #self.widgetTree=None

    #------------------------
    def ouvreArbre(self):
    #------------------------
       #print ('je passe la')
       #print (self.widgetTree)
       #self.widgetTree=self.oldWidgetTree
       self.widgetTree.show()
       #self.restoreSplitterSizes(3)

    #-----------------------
    def getEtapeCourante(self) :
    #-----------------------
      print (self.tree.selectedItems())
      if len(self.tree.selectedItems()) != 1 : return None
      etape=self.tree.selectedItems()[0].item.object.getEtape()
      return etape
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

    #-------------------#  Pour execution avec output et error dans le bash
    def runPSEN(self):
    #-------------------#
    
      #if self.modified or self.fichier==None  : self.saveFile()
      self.saveFile()
        
      #lancement avec le .bat
      path1 = os.path.abspath(os.path.join(os.path.abspath(__file__), '../','../','PSEN_Eficas','PSEN'))
      WrapperFilePath = os.path.join(path1, 'PSSEWrapper.py') 
      import subprocess
      p = subprocess.Popen(['python',WrapperFilePath])
      (out,err)=p.communicate()        
      print (out)
      print (err)

    #-------------------#  Pour execution avec output et error dans le bash
    def runPSEN_N1(self):
    #-------------------#
      

      self.saveFile()
      path1 = os.path.abspath(os.path.join(os.path.abspath(__file__), '../','../','ProcessOutputs_Eficas','TreatOutputs'))
      sys.path.append(path1)

      if not(self.jdc.isValid()):
         QMessageBox.information( self, tr( "Unvalid JDC"),tr("incorrect keywords will be ignored"))
      if 'dicoImbrique' in generator.plugins:
         self.generator=generator.plugins['dicoImbrique']()
         jdc_formate=self.generator.gener(self.jdc)
         dico=self.generator.Dico 
         
         ###to delete
         #fileDico =  r'C:\Logiciels DER\PSEN_V16\Code\ProcessOutputs_Eficas\TreatOutputs\dicoN1.py'
         fileDico =  os.path.join(path1, 'dicoN1.py') #r'C:\Logiciels DER\PSEN_V16\Code\ProcessOutputs_Eficas\TreatOutputs\dicoN1.py'
         f = open( str(fileDico), 'w')
         f.write("Dico =" + str(dico) )
         f.close()
         ###
         
      
      print ('in runPSEN_N1', dico)
      print (dico)
      from Run import run 
      run(dico)
      #res,txt_exception=run(dico)
      #if res : QMessageBox.information( self, tr("fin de script run"), txt_exception)
      #else  : QMessageBox.critical( self, tr("Erreur fatale script run"), txt_exception)
       
    #-------------------#  Pour execution avec output et error dans le bash
    def process_N1(self):
    #-------------------#

      path1 = os.path.abspath(os.path.join(os.path.abspath(__file__), '../','../','ProcessOutputs_Eficas','TreatOutputs'))
      sys.path.append(path1)


      if 'dicoImbrique' in generator.plugins:
         self.generator=generator.plugins['dicoImbrique']()
         jdc_formate=self.generator.gener(self.jdc)
         dico=self.getDico() #generator.Dico


         for k in dico['CONTINGENCY_PROCESSING']:
             #print (k)
             if k[0:19] == 'Component_List_For_' or k[0:21] =='Contingency_List_For_' :
                newK=k.replace('__',' ')
                l="'"+str(newK)+"'"
                dico['CONTINGENCY_PROCESSING'][l]=dico['CONTINGENCY_PROCESSING'][k]
                del dico['CONTINGENCY_PROCESSING'][k]

         ###to delete
         fileDico =  os.path.join(path1, 'dicoN1_process.py')
         f = open( str(fileDico), 'w')
         f.write("Dico =" + str(dico) )
         f.close()
         ###
         return dico

        #return self.getDico()

    #-------------------#  Pour execution avec output et error dans le bash
    def process_VP(self):
    #-------------------#
      if 'dicoImbrique' in generator.plugins:
         self.generator=generator.plugins['dicoImbrique']()
         jdc_formate=self.generator.gener(self.jdc)
         dico=self.getDico() #generator.Dico
         return dico

if __name__ == "__main__":
    print ('in main')
