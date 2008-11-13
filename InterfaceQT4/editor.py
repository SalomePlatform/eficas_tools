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

# Modules Eficas

import convert,generator
from Editeur     import session
from Editeur     import comploader
from Editeur     import Objecttreeitem
#import panelsQT
import browser
import readercata
import qtCommun

import prefs

VERSION_EFICAS  = "EFICAS v1.14"


class JDCEditor(QSplitter):
# -------------------------- #
    """
       Editeur de jdc
    """        

    def __init__ (self,fichier = None, jdc = None, QWParent=None, units = None, include=0 ,appli=None, vm=None):          
    #----------------------------------------------------------------------------------------------------------#

        #print "debut JDCEditor __init__"
        print "fichier", fichier,"jdc",jdc,"units",units,"include",include
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
        else :
           self.salome=0

        self.code = prefs.code
        self.version_code = VERSION_CODE
        self.titre=VERSION_EFICAS + ' pour '+ self.code

        self.dict_reels={}
        self.liste_simp_reel=[]        
        self.format_fichier='python' # par defaut
	self.jdc_openturn_xml=""
	self.jdc_openturn_std=""
        self.ihm="QT"
        
        from Editeur import configuration
        self.CONFIGURATION = self.appliEficas.CONFIGURATION
        self.CONFIGStyle =   self.appliEficas.CONFIGStyle

        self.sb = None
        if hasattr(self.appliEficas,"statusBar"):
           self.sb = self.appliEficas.statusBar()
      
        self.fileInfo       = None
        self.lastModified   = 0
        
        self.modified   = False
        self.isReadOnly = False
        self.tree = None
        self.node_selected = None
        
        if not hasattr( readercata, 'reader' ) :
            readercata.reader = readercata.READERCATA( self, self.appliEficas )
        self.readercata = readercata.reader
        
        #------- construction du jdc --------------

        jdc_item = None
                        
        nouveau=0
        if self.fichier is not None:        #  fichier jdc fourni
            self.fileInfo = QFileInfo(self.fichier)
            self.fileInfo.setCaching(0)
            if jdc==None :
               self.jdc = self.readFile(self.fichier)
            else :
               self.jdc=jdc
            if units is not None:
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
                self.affiche_infos("Erreur fatale au chargement de %s" %fichier)                
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
        print JdC_aux
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
        if convert.plugins.has_key( self.format_fichier ):
             # Le convertisseur existe on l'utilise
             appli = self 
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
                        
#        qApp.restoreOverrideCursor()        
        if self.fileInfo!= None : 
           self.lastModified = self.fileInfo.lastModified()
        else :
           self.lastModified = 1
        return jdc
        
    #-----------------------#
    def get_source(self,file):
    #-----------------------#
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
        format = self.format_fichier
        f=open(self.fichier,'r')
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
        if self.sb:
            self.sb.showMessage(message)#,2000)

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
      if not self.node_selected.item.iscopiable():
          QMessageBox.information( self, 
                      "Copie impossible",
                      "Cette version d'EFICAS ne permet pas la copie de cet Objet")
          self.node_selected=None
          return
    
    
    #---------------------#
    def handleEditCut(self):
    #---------------------#
      """
      Stocke dans Eficas.noeud_a_editer le noeud à couper
      """
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
      print "noeud a copier", self.node_selected.item.GetLabelText()[0]
      print "noued apres " ,self.QWParent.noeud_a_editer.item.GetLabelText()[0]
      if self.QWParent.noeud_a_editer == None :
          QMessageBox.information( self, 
                      "Copie impossible",
                      "Aucun Objet n a ete copie ou colle ")
          return
      try:
         child=self.QWParent.noeud_a_editer.doPaste(self.node_selected)
      except:
         traceback.print_exc()
         QMessageBox.information( self, 
                     "Copie impossible",         
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

      if self.QWParent.edit == "couper":
         #nom = self.QWParent.noeud_a_editer.item.object.sd.nom
         print self.QWParent.noeud_a_editer.item.object.sd.nom
         item=self.QWParent.noeud_a_editer.item
         self.QWParent.noeud_a_editer.delete()
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

#    #------------------------------------ 
#    def writeFilesOpenturns(self,fn) :
#    #------------------------------------ 
#	base=fn[:fn.rfind(".")]
#	fileXML=base + '.xml'
#	fileSTD=base + '_std.py'
#        self.writeFile(fileXML,self.jdc_openturn_xml)
#        self.writeFile(fileSTD,self.jdc_openturn_std)
#
#
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
            
        newName = None
        if self.fichier is None or saveas:
          if path is None: 
             #PN --> modifier selon les prefs
             path="/tmp"
          selectedFilter = QString('')
          fn = QFileDialog.getSaveFileName( self,
               self.trUtf8("sauvegarde"), path,
               self.trUtf8("JDC (*.comm);;" "All Files (*)"),None,
               QFileDialog.DontConfirmOverwrite)
          if fn.isNull(): return (0, None)

          ext = QFileInfo(fn).suffix()
          if ext.isEmpty(): fn.append(".comm")

          if QFileInfo(fn).exists():
                abort = QMessageBox.warning(self,
                       self.trUtf8("Sauvegarde du Fichier"),
                       self.trUtf8("Le fichier <b>%1</b> existe deja.").arg(fn),
                       self.trUtf8("&Ecraser"),
                       self.trUtf8("&Abandonner"))
                if abort == 1 :  return (0, None)

          fn = unicode(QDir.convertSeparators(fn))
          newName = fn

        else:
            fn = self.fichier
        
        if self.writeFile(fn):
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
#	    if self.code == "OPENTURNS" :
#	       self.writeFilesOpenturns(fn)
#            if self.salome : 
#               self.QWParent.appli.addJdcInSalome( self.fichier)
#               if self.code == 'ASTER':
#                  self.QWParent.appli.createOrUpdateMesh(self)
#               #PN ; TODO
#
            return (1, self.fichier)
        else:
            return (0, None)
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
                                        
        QMessageBox.information( self, titre,texte)
        #PN --> les prefs
        fn = QFileDialog.getOpenFileName( self, titre)
        
        if fn.isNull(): 
        # ce retour est impose par le get_file d'I_JDC
           return None," "
            
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
        
if __name__=='__main__':    
    if hasattr(prefs,'encoding'):
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
    mw = JDCEditor('azAster.comm')
    app.setMainWidget(mw)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    mw.show()
            
    res = app.exec_loop()
    sys.exit(res)
