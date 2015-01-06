# -*- coding: utf-8 -*-
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

import os, string
from PyQt4.QtGui  import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

DictExtensions= {"MAP" : ".map"}
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

       self.myQtab = self.appliEficas.myQtab
       if self.appliEficas.multi== True:
          self.myQtab.connect(self.myQtab,SIGNAL("currentChanged(int)"),self.indexChanged)
        
   def indexChanged(self):
       index=self.myQtab.currentIndex()
       if  self.dict_editors.has_key(index):
           editor=self.dict_editors[index]
           self.appliEficas.CONFIGURATION=editor.CONFIGURATION
           self.appliEficas.code=editor.CONFIGURATION.code
           self.appliEficas.setWindowTitle(editor.titre)
           self.appliEficas.construitMenu()

   def handleOpen(self,fichier=None,patron=0,units=None):
       result = None
       if fichier is None:
            if self.appliEficas.multi==True : 
               self.appliEficas.definitCode(None,None)
               if self.appliEficas.code == None:return
            
            if DictExtensions.has_key(self.appliEficas.code) :
               chaine="JDC (*"+DictExtensions[self.appliEficas.code]+");;"
               extensions=tr(chaine+ "All Files (*)")
            else :
               extensions=tr('Fichiers JDC (*.comm);;''Tous les Fichiers (*)')

            fichier = QFileDialog.getOpenFileName(self.appliEficas,
                        tr('Ouvrir Fichier'),
                        self.appliEficas.CONFIGURATION.savedir,
                         extensions)
            if fichier.isNull(): 
              return result
       fichier = os.path.abspath(unicode(fichier))
       ulfile = os.path.abspath(unicode(fichier))
       self.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
       self.appliEficas.addToRecentList(fichier)
       maPage=self.getEditor( fichier,units=units)
       if maPage: result = maPage
       if maPage : self.myQtab.setTabText(self.myQtab.indexOf(maPage),os.path.basename(fichier))
       return result

   def handleClose(self,doitSauverRecent = 1,texte=tr('&Quitter')):
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

   def handleCloseAll(self,texte=tr('Quitter')):
       res=0
       self.appliEficas.sauveRecents()
       while len(self.dict_editors) > 0 :
             self.myQtab.setCurrentIndex(0)
             res=self.handleClose(0,texte)
             if res==2 : return res   # l utilsateur a annule
       return res
        
   def handleRechercher(self):
       #print "passage dans handleRechercher"
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.handleRechercher()

   def handleDeplier(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.handleDeplier()
   
   def handleEditCopy(self):
       #print "passage dans handleEditCopy"
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.handleEditCopy()

   def handleEditCut(self):
       #print "passage dans handleEditCut"
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.handleEditCut()

   def handleEditPaste(self):
       #print "passage dans handleEditPaste"
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.handleEditPaste()

   def handleSupprimer(self):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.handleSupprimer()

   def newEditor(self,include=0):
       if self.appliEficas.multi==True : 
           self.appliEficas.definitCode(None,None)
           if self.appliEficas.code == None:return
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
                     tr("Fichier Duplique"),
                     tr("Le fichier ne sera pas sauvegarde."),
                     tr("&Annuler"))
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
                        tr("Fichier"),
                        tr("Le fichier <b>%s</b> est deja ouvert.",str(fichier)),
                        tr("&Duplication"),
                        tr("&Abort"))
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
#PNPNPNPN --> a affiner
        if fichier is None:
            self.untitledCount += 1
            self.myQtab.addTab(win, tr("Fichier non encore nommé ", self.untitledCount))
            #self.myQtab.addTab(win, str(self.appliEficas.code))
        else:
            liste=fichier.split('/')
            txt =  liste[-1]
            if not QFileInfo(fichier).isWritable():
                txt = '%s (ro)' % txt
            self.myQtab.addTab(win,txt )
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
                     tr("Fichier Duplique"),
                     tr("Le fichier ne sera pas sauvegarde."),
                     tr(texte), 
                     tr("&Annuler"))
            if res == 0 : return 1
            return 2
        if editor.modified:
            fn = editor.getFileName()
            if fn is None:
                fn = self.appliEficas.trUtf8('Noname')
            res = QMessageBox.warning(self.appliEficas, 
                tr("Fichier Modifie"),
                tr("Le fichier %s n a pas ete sauvegarde.",str(fn)),
                tr("&Sauvegarder"),
                tr(texte),
                tr("&Annuler") )
            if res == 0:
                (ok, newName) = editor.saveFile()
                if ok:
                    fileName=os.path.basename(unicode(newName))
                    index=self.myQtab.currentIndex()
                    self.myQtab.setTabText(index,fileName)
                return ok
        return res

   def handleAjoutGroup(self,listeGroup):
       index=self.myQtab.currentIndex()
       if index < 0 : return
       editor=self.dict_editors[index]
       editor.handleAjoutGroup(listeGroup)
