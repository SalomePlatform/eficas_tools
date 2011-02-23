# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
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

import os, string
from PyQt4.QtGui  import *
from PyQt4.QtCore import *

class MyTabview:

   def __init__(self,appliEficas):
       self.appliEficas=appliEficas
       self.tabWidgets = []
       self.mesIndexes = {}
       self.appliEficas=appliEficas
       self.editors = []
       self.dict_editors={}
       self.untitledCount = 0
       self.doubles = {}

       self.gridLayout = QGridLayout(self.appliEficas.centralWidget())
       self.myQtab = QTabWidget(self.appliEficas.centralWidget())
       self.gridLayout.addWidget(self.myQtab)
        

   def handleOpen(self,fichier=None,patron=0,units=None):
       if fichier is None:
            fichier = QFileDialog.getOpenFileName(self.appliEficas,
                        self.appliEficas.trUtf8('Ouvrir Fichier'),
                        self.appliEficas.CONFIGURATION.savedir,
                        self.appliEficas.trUtf8('JDC Files (*.comm);;''All Files (*)'))
            if fichier.isNull(): return
       fichier = os.path.abspath(unicode(fichier))
       ulfile = os.path.abspath(unicode(fichier))
       self.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
       self.appliEficas.addToRecentList(fichier)
       maPage=self.getEditor( fichier,units=units)

   def handleClose(self,doitSauverRecent = 1,texte='&Quitter'):
       if doitSauverRecent : self.appliEficas.sauveRecents()
       index=self.myQtab.currentIndex()
       if index < 0 : return
       res=self.checkDirty(self.dict_editors[index],texte)
       if res == 2 : return 2             # l utilisateur a annule
       index=self.myQtab.currentIndex()
       idx=index
       while idx < len(self.dict_editors) -1 :
             self.dict_editors[idx]=self.dict_editors[idx+1]
             idx = idx + 1
       del self.dict_editors[len (self.dict_editors) -1]
       try :
           del self.doubles[self.dict_editors[index]]
       except :
           pass
       self.myQtab.removeTab(index)
       return res
       

   def run(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.run()

   def saveRun(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.saveRun()

   def runYACS(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.runYACS()

   def saveYACS(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.saveYACS()

   def handleCloseAll(self,texte='Quitter'):
       res=0
       self.appliEficas.sauveRecents()
       while len(self.dict_editors) > 0 :
             self.myQtab.setCurrentIndex(0)
             res=self.handleClose(0,texte)
             if res==2 : return res   # l utilsateur a annule
       return res
        
   def handleEditCopy(self):
       #print "passage dans handleEditCopy"
       index=self.myQtab.currentIndex()
       editor=self.dict_editors[index]
       editor.handleEditCopy()

   def handleEditCut(self):
       #print "passage dans handleEditCut"
       index=self.myQtab.currentIndex()
       editor=self.dict_editors[index]
       editor.handleEditCut()

   def handleEditPaste(self):
       #print "passage dans handleEditPaste"
       index=self.myQtab.currentIndex()
       editor=self.dict_editors[index]
       editor.handleEditPaste()

   def handleSupprimer(self):
       index=self.myQtab.currentIndex()
       editor=self.dict_editors[index]
       editor.handleSupprimer()

   def newEditor(self,include=0):
       maPage=self.getEditor(include=include)

   def newIncludeEditor(self):
       self.newEditor(include=1)

   def handleViewJdcFichierSource(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       self.dict_editors[index].viewJdcSource()

   def handleViewJdcRapport(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       self.dict_editors[index].viewJdcRapport()

   def handleViewJdcPy(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       self.dict_editors[index].viewJdcPy()

   def saveCurrentEditor(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       if editor in self.doubles.keys() :
           QMessageBox.warning(
                     None,
                     self.appliEficas.trUtf8("Fichier Duplique"),
                     self.appliEficas.trUtf8("Le fichier ne sera pas sauvegarde."),
                     self.appliEficas.trUtf8("&Annuler"))
           return
       ok, newName = editor.saveFile()
       if ok :
           fileName=os.path.basename(unicode(newName))
           self.myQtab.setTabText(index,fileName)
       return ok

   def saveAsCurrentEditor(self):
       index=self.myQtab.currentIndex()
       editor=self.dict_editors[index]
       oldName=editor.fichier
       ok,newName = editor.saveFileAs()
       if ok :
           fileName=os.path.basename(unicode(newName))
           self.myQtab.setTabText(index,fileName)
       if editor in self.doubles.keys():
          if oldName != newName :
             del self.doubles[editor]
       return ok

   def displayJDC(self,jdc,fn=None):
        """
        Public slot to display a file in an editor.
        @param fn name of file to be opened
        # insert filename into list of recently opened files
        """
        titre=None
        if fn != None : titre=fn.split("/")[-1]
        editor = self.getEditor(fichier= fn, jdc = jdc ,include=1)
        self.appliEficas.addToRecentList(editor.getFileName())

   def getEditor(self,fichier = None,jdc = None, units = None,include=0):
       newWin = 0
       double = None
       indexEditor=0
       for indexEditor in self.dict_editors.keys():
           editor=self.dict_editors[indexEditor]
           if self.samepath(fichier, editor.getFileName()):
              abort = QMessageBox.warning(self.appliEficas,
                        self.appliEficas.trUtf8("Fichier"),
                        self.appliEficas.trUtf8("Le fichier <b>%1</b> est deja ouvert.").arg(fichier),
                        self.appliEficas.trUtf8("&Duplication"),
                        self.appliEficas.trUtf8("&Abort"))
              if abort: break
              double=editor
       else :
            from editor import JDCEditor
            editor = JDCEditor(self.appliEficas,fichier, jdc, self.myQtab,units=units,vm = self,include=include)
            if double != None : 
               self.doubles[editor]=double
            if editor.jdc: # le fichier est bien un jdc
                self.editors.append(editor)
                newWin = 1
            else:
                editor.closeIt()

       if newWin:
            self.addView(editor, fichier)
       elif editor.jdc:
            self.myQtab.setCurrentIndex(indexEditor)

       index=self.myQtab.currentIndex()
       if index != -1 :
          self.dict_editors[index]=editor
       return editor

   def addView(self, win, fichier=None):
        if fichier is None:
            self.untitledCount += 1
            self.myQtab.addTab(win, self.appliEficas.trUtf8("Untitled %1").arg(self.untitledCount))
        else:
            liste=fichier.split('/')
            txt =  liste[-1]
            if not QFileInfo(fichier).isWritable():
                txt = '%s (ro)' % txt
            self.myQtab.addTab(win, txt)
        self.myQtab.setCurrentWidget(win)
        self.currentEditor=win
        win.setFocus()

   def getOpenStartDir(self) :
       #PN --> Les Preferences
        try :
            userDir=os.path.expanduser("~/Eficas_install/")
            return userDir
        except :
            return ""

   def samepath(self,f1, f2):
    """
    compare two paths.
    """
    if f1 is None or f2 is None: return 0
    if os.path.normcase(os.path.normpath(f1)) == os.path.normcase(os.path.normpath(f2)) : return 1
    return 0


   def checkDirty(self, editor,texte):
        """
        Private method to check dirty status and open a message window.
        
        @param editor editor window to check
        @return flag indicating successful reset of the dirty flag (boolean)
        """        
        res=1 
        if (editor.modified) and (editor in self.doubles.keys()) :
            res = QMessageBox.warning(
                     None,
                     self.appliEficas.trUtf8("Fichier Duplique"),
                     self.appliEficas.trUtf8("Le fichier ne sera pas sauvegarde."),
                     Eficas.trUtf8(texte), 
                     self.appliEficas.trUtf8("&Annuler"))
            if res == 0 : return 1
            return 0
        if editor.modified:
            fn = editor.getFileName()
            if fn is None:
                fn = self.appliEficas.trUtf8('Noname')
            res = QMessageBox.warning(self.appliEficas, 
                self.appliEficas.trUtf8("Fichier Modifie"),
                self.appliEficas.trUtf8("Le fichier <b>%1</b> n a pas ete sauvegarde.") .arg(fn),
                self.appliEficas.trUtf8("&Sauvegarder"),
                self.appliEficas.trUtf8(texte),
                self.appliEficas.trUtf8("&Annuler") )
            if res == 0:
                (ok, newName) = editor.saveFile()
                if ok:
                    fileName=os.path.basename(unicode(newName))
                    index=self.myQtab.currentIndex()
                    self.myQtab.setTabText(index,fileName)
                return ok
        return res
