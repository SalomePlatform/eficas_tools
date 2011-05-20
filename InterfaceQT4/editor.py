# -*- coding: utf-8 -*-
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

import types,sys,os
import traceback
from PyQt4 import *
from PyQt4.QtGui  import *
from PyQt4.QtCore import *
import time
from datetime import date


# Modules Eficas

import convert,generator
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

        #print "fichier", fichier,"jdc",jdc,"units",units,"include",include
        QSplitter.__init__(self, QWParent)
	self.appliEficas = appli
	self.appli       = appli  #---- attendu par IHM
        self.vm          = vm
        self.fichier     = fichier
        self.jdc         = jdc
        self.QWParent    = QWParent

        self.test=0
        VERSION_CODE    = session.d_env.cata
        if appli != None :
           self.salome =  self.appliEficas.salome
           self.format =  self.appliEficas.format_fichier
        else :
           self.salome=0
           print "dans JDC pas d appli ????????"

        self.code = self.appliEficas.CONFIGURATION.code
        self.version_code = VERSION_CODE
        self.titre=self.appliEficas.VERSION_EFICAS + ' pour '+ self.code

        self.dict_reels={}
        self.liste_simp_reel=[]        
        self.ihm="QT"
        
        import prefs
        nameConf='configuration_'+prefs.code
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
        self.node_selected = None
        self.message=''
        
        #if not hasattr( readercata, 'reader' ) :
        #    readercata.reader = readercata.READERCATA( self, self.appliEficas )
        #self.readercata = readercata.reader
        if not hasattr ( self.appliEficas, 'readercata'):
           self.readercata  = readercata.READERCATA( self, self.appliEficas )
           self.appliEficas.readercata=self.readercata
        else :
           self.readercata=self.appliEficas.readercata
        if self.readercata.fic_cata == None : return    #Sortie Salome
        self.Commandes_Ordre_Catalogue =self.readercata.Commandes_Ordre_Catalogue
        
        #------- construction du jdc --------------

        jdc_item = None
        self.mode_nouv_commande=self.readercata.mode_nouv_commande
                        
        nouveau=0
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
                self.affiche_infos("Erreur fatale au chargement de %s" %fichier,Qt.red)                
                QMessageBox.critical( self, "Erreur fatale au chargement d'un fichier", txt_exception)                
            else:
                comploader.charger_composants("QT")
                jdc_item=Objecttreeitem.make_objecttreeitem( self, "nom", self.jdc )

                if (not self.jdc.isvalid()) and (not nouveau) :
                    self.viewJdcRapport()
        if jdc_item:                        
            self.tree = browser.JDCTree( jdc_item,  self )
        
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
             text=p.convert('exec',self.appliEficas)
             if not p.cr.estvide():                 
                self.affiche_infos("Erreur à la conversion",Qt.red)
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
        format=self.appliEficas.format_fichier

        # Il faut convertir le contenu du fichier en fonction du format
        if convert.plugins.has_key(format):
            # Le convertisseur existe on l'utilise
            p=convert.plugins[format]()
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
        
    #-----------------------#
    def viewJdcSource(self):        
    #-----------------------#
        format = self.appliEficas.format_fichier
        f=open(self.fichier,'r')
        texteSource=f.read()
        f.close()
        self._viewText(texteSource, "JDC_SOURCE")
                
    #-----------------------#
    def viewJdcPy(self):        
    #-----------------------#
        format = self.appliEficas.format_fichier
        strSource = str( self.get_text_JDC(format) )       
        self._viewText(strSource, "JDC_RESULTAT")
                 
    #-----------------------#
    def viewJdcRapport(self):
    #-----------------------#
        strRapport = str( self.jdc.report() )
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
      self.node_selected=None
      if len(self.tree.selectedItems()) == 0 : return
      if len(self.tree.selectedItems()) != 1 :
          QMessageBox.information( self, 
                      "Copie impossible",
                      "Cette version d'EFICAS permet uniquement la copie d un seul objet")
          return
      self.node_selected=self.tree.selectedItems()[0]
      if copie == 0 : return
    
    
    #---------------------#
    def handleSupprimer(self):
    #---------------------#
      #print "handleSupprimer"
      self.chercheNoeudSelectionne()
      self.node_selected.delete()
    
    #---------------------#
    def handleEditCut(self):
    #---------------------#
      """
      Stocke dans Eficas.noeud_a_editer le noeud à couper
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
      #print "handleEditCut"
      self.chercheNoeudSelectionne()
      self.QWParent.edit="copier"
      self.QWParent.noeud_a_editer = self.node_selected
    
    #------------------------#
    def handleEditPaste(self):
    #------------------------#
      """
      Lance la copie de l'objet place dans self.QWParent.noeud_a_editer
      Ne permet que la copie d'objets de type Commande ou MCF
      """
      #print "handleEditPaste"
      self.chercheNoeudSelectionne()
      try :
          index_noeud_a_couper=self.QWParent.noeud_a_editer.treeParent.children.index(self.QWParent.noeud_a_editer)
      except :
          QMessageBox.information( self, 
                      "Copie impossible",
                      "Aucun Objet n a ete copie ou coupe ")
          return
      child=0
      try:
         child=self.QWParent.noeud_a_editer.doPaste(self.node_selected)
      except:
         traceback.print_exc()
         QMessageBox.information( self, 
                     "Copie refusee",         
                     "Copie refusee pour ce type d objet a cet endroit")
         self.message = ''
         self.affiche_infos("Copie refusée")
         return
     
      if child == 0 or child == None:
          QMessageBox.critical( self, "Copie refusee",'Copie refusee pour ce type d objet')
          self.message = ''
          self.affiche_infos("Copie refusée",Qt.red)
          return
    
      # il faut declarer le JDCDisplay_courant modifie
      self.init_modif()
      # suppression eventuelle du noeud selectionne
      # si possible on renomme l objet comme le noeud couper

      if self.QWParent.edit == "couper":
         index_ajoute=child.treeParent.children.index(child)
         if index_ajoute <= index_noeud_a_couper :
            index_noeud_a_couper=index_noeud_a_couper + 1
         item=self.QWParent.noeud_a_editer.item
         noeud_a_supprimer=self.QWParent.noeud_a_editer.treeParent.children[index_noeud_a_couper]
         noeud_a_supprimer.delete()
         child.item.update(item)
         #test,mess = child.item.nomme_sd(nom)
         child.select()

      # on rend la copie a nouveau possible en liberant le flag edit
      self.QWParent.edit="copier"
          
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
            txt = self.get_text_JDC(self.appliEficas.format_fichier)
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

    #-----------------------------#
    def get_text_JDC(self,format):
    #-----------------------------#
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         self.generator=generator.plugins[format]()
         jdc_formate=self.generator.gener(self.jdc,format='beautifie',config=self.appliEficas.CONFIGURATION)
         if not self.generator.cr.estvide():            
            self.affiche_infos("Erreur à la generation",Qt.red)
            QMessageBox.critical( self, "Erreur a la generation","EFICAS ne sait pas convertir ce JDC")
            return ""
         else:
            return jdc_formate
      else:         
         # Il n'existe pas c'est une erreur
         self.affiche_infos("Format %s non reconnu" % format,Qt.red)
         QMessageBox.critical( self, "Format "+format+" non reconnu","EFICAS ne sait pas convertir le JDC selon le format "+format)
         return ""

    #-----------------------------#
    def run(self,execution="oui"):
    #-----------------------------#
      format=self.appliEficas.format_fichier
      self.textePython=""
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         self.generator=generator.plugins[format]()
         self.textePython =self.generator.generRUN(self.jdc,format='beautifie',config=self.appliEficas.CONFIGURATION)
      if execution=="oui" :
         exec self.textePython
      else:
         return self.textePython

    #------------------------------------------------#
    def runYACS(self,execution="oui",nomFichier=None):
    #------------------------------------------------#
      format=self.appliEficas.format_fichier
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         self.generator=generator.plugins[format]()
         self.generator.generRUNYACS(self.jdc,format='beautifie',config=self.appliEficas.CONFIGURATION,nomFichier=nomFichier)
      if execution=="oui" :
         print "il faut faire le run dans Salome"
    
    
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
      print fn
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
    
    #-----------------------------#
    def saveYACS(self):
    #-----------------------------#
        if hasattr(self,'fichierYACS'):
           self.runYACS(execution="non",nomFichier=self.fichierYACS)
           return

        today = str(date.today())
        today = today.replace('-', '')
        today+="-"+time.strftime("%H%M%S", time.localtime())
        path=self.CONFIGURATION.PATH_STUDY+"/"+self.CONFIGURATION.NAME_SCHEME+"_"+today+".xml"
        extension=".xml"

        bOK, fn=self.determineNomFichier(path,extension)
        if fn == "" : return
        self.runYACS(execution="non",nomFichier=fn)

      
    #-----------------------------------------#
    def cherche_Groupes(self):
    #-----------------------------------------#
        listeMA,listeNO=self.get_text_JDC("GroupMA")
        return listeMA,listeNO

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
            titre = "Choix unite %d " %unite
            texte = "Le fichier %s contient une commande INCLUDE \n" % fic_origine
            texte = texte+'Donnez le nom du fichier correspondant\n à l unité logique %d' % unite
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
            # On a réussi à convertir le fichier self.ulfile                
            jdcText = source
        else:
            # Une erreur a été rencontrée
            jdcText = ''
        return ulfile, jdcText

        
if __name__=='__main__':    
    import prefs # dans main
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
