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
try :
   from builtins import str
   from builtins import object
except : pass

import os
from Extensions.i18n import tr
import six
from  PyQt5.QtWidgets  import QFileDialog, QMessageBox
from  PyQt5.QtCore     import QFileInfo

# --------------------------------
class JdcSsIhmHandler(object):
# --------------------------------
# retourne a l utilisateur

   def __init__(self,viewManager):
#  --------------------------------------
       self.viewManagerSsIhm=viewManager

   def viewJdcPy(self) :
#  ---------------------
       self.viewManagerSsIhm.handleViewJdcPy(self)

   def viewJdcSource(self) :
#  ---------------------
       self.viewManagerSsIhm.handleViewJdcSource(self)

   def getFileName(self):
#  ---------------------
       self.viewManagerSsIhm.getFileName(self)





#--------------------------------
class MyViewManagerSsIhm(object):
#--------------------------------
# Symetrique de ViewManager mais pas d heritage entre les 2
# dans le viewManager pas de souci pour savoir qui est le jdc sur lequel on travaille
# ici en revanche.... c est moins sur

#  --------------------------------
   def __init__(self,appliEficas):
#  --------------------------------
       self.appliEficas=appliEficas
       self.tabWidgets = []
       self.mesIndexes = {}
       self.dictEditors={}
       self.untitledCount = 0
       self.doubles = {}

#  ------------------------------------------------------
   def handleOpen(self,fichier=None, units=None):
#  ------------------------------------------------------
       result = None
       if fichier is None: 
             print ('nom de fichier obligatoire')
             return None

       for handler in self.dictEditors :
           editor=self.dictEditors[handler]
           if self.samePath(fichier, editor.getFileName()):
              print ('fichier deja ouvert . pas de nouvel editor')
              return handler

       monNewHandler = self.getNewEditor(fichier,units)
       return monNewHandler

#  ----------------------------------------------------------------------
   def getNewEditor(self,fichier = None,jdc = None, units = None,include=0):
#  ----------------------------------------------------------------------

       from InterfaceQT4.editorSsIhm import JDCEditorSsIhm
       editor = JDCEditorSsIhm(self.appliEficas,fichier,jdc, units=units,include=include)

       if editor.jdc: # le fichier est bien un jdc
          monHandler = JdcSsIhmHandler(self)
          self.dictEditors[monHandler]=editor
          return monHandler
       else:
          print ('impossible de construire le jdc') 
          return None

#  -----------------------------
   def samePath(self,f1, f2):
#  ------------------------------
    """
    compare two paths.
    """
    if f1 is None or f2 is None: return 0
    if os.path.normcase(os.path.normpath(f1)) == os.path.normcase(os.path.normpath(f2)) : return 1
    return 0

#  ---------------------------------
   def handleViewJdcPy(self,handler):
#  ---------------------------------
        if not (handler in self.dictEditors) :
           print ('editor non trouve')
           return
        self.dictEditors[handler].viewJdcPy()

#  ---------------------------------
   def getFileName(self,handler):
#  ---------------------------------
        if not (handler in self.dictEditors) :
           print ('editor non trouve')
           return
        return self.dictEditors[handler].getFileName()


#  ---------------------------------------------
   def handleViewJdcSource(self,handler):
#  ---------------------------------------------
        print (handler)
        if not (handler in self.dictEditors) :
           print ('editor non trouve')
           return
        self.dictEditors[handler].viewJdcSource()


#   def handleClose(self,doitSauverRecent = 1,texte=tr('&Quitter')):
#       if doitSauverRecent : self.appliEficas.sauveRecents()
#       index=self.myQtab.currentIndex()
#       if index < 0 : return
#       res=self.checkDirty(self.dict_editors[index],texte)
#       if res == 2 : return 2             # l utilisateur a annule
#       index=self.myQtab.currentIndex()
#       idx=index
#       while idx < len(self.dict_editors) -1 :
#             self.dict_editors[idx]=self.dict_editors[idx+1]
#             idx = idx + 1
#       del self.dict_editors[len (self.dict_editors) -1]
#       try :
#           del self.doubles[self.dict_editors[index]]
#       except :
#           pass
#       self.myQtab.removeTab(index)
#       return res
#       

#
#   def handleCloseAll(self,texte=tr('Quitter')):
#       res=0
#       self.appliEficas.sauveRecents()
#       while len(self.dict_editors) > 0 :
#             self.myQtab.setCurrentIndex(0)
#             res=self.handleClose(0,texte)
#             if res==2 : return res   # l utilsateur a annule
#       return res
#        
#
#
#   def newEditor(self,include=0):
#       if self.appliEficas.demande==True : 
#           self.appliEficas.definitCode(None,None)
#           if self.appliEficas.code == None:return
#       maPage=self.getEditor(include=include)
#

#
#   def handleViewJdcRegles(self):
#       index=self.myQtab.currentIndex()
#       if index < 0 : return
#       self.dict_editors[index].viewJdcRegles()
#
#   def handleGestionParam(self):
#       index=self.myQtab.currentIndex()
#       if index < 0 : 
#          QMessageBox.warning( self.appliEficas,tr(u"Creation Parametre indisponible"),tr(u"les parametres sont lies a un jeu de donnees"))
#          return
#       self.dict_editors[index].gestionParam()
#
#   def handleViewJdcRapport(self):
#       index=self.myQtab.currentIndex()
#       if index < 0 : return
#       self.dict_editors[index].viewJdcRapport()
#
#
#   def saveCurrentEditor(self):
#       index=self.myQtab.currentIndex()
#       if index < 0 : return
#       editor=self.dict_editors[index]
#       if editor in self.doubles :
#           QMessageBox.warning(
#                     None,
#                     tr("Fichier Duplique"),
#                     tr("Le fichier ne sera pas sauvegarde."),)
#           return
#       ok, newName = editor.saveFile()
#       if ok :
#           fileName=os.path.basename(six.text_type(newName))
#           self.myQtab.setTabText(index,fileName)
#       return ok
#
#   def saveLegerCurrentEditor(self):
#       index=self.myQtab.currentIndex()
#       if index < 0 : return
#       editor=self.dict_editors[index]
#       ok, newName = editor.saveFileLeger()
#       return ok
#
#   def sauveLigneCurrentEditor(self):
#       index=self.myQtab.currentIndex()
#       if index < 0 : return
#       editor=self.dict_editors[index]
#       if editor in self.doubles :
#           QMessageBox.warning(
#                     None,
#                     tr("Fichier Duplique"),
#                     tr("Le fichier ne sera pas sauvegarde."),)
#           return
#       ok, newName = editor.sauveLigneFile()
#       if ok :
#           fileName=os.path.basename(six.text_type(newName))
#           self.myQtab.setTabText(index,fileName)
#       return ok
#
#
#   def saveAsCurrentEditor(self):
#       index=self.myQtab.currentIndex()
#       editor=self.dict_editors[index]
#       oldName=editor.fichier
#       ok,newName = editor.saveFileAs()
#       if ok :
#           fileName=os.path.basename(six.text_type(newName))
#           self.myQtab.setTabText(index,fileName)
#       if editor in self.doubles :
#          if oldName != newName :
#             del self.doubles[editor]
#       return ok
#
#   def displayJDC(self,jdc,fn=None):
#        """
#        Public slot to display a file in an editor.
#        @param fn name of file to be opened
#        # insert filename into list of recently opened files
#        """
#        titre=None
#        if fn != None : titre=fn.split("/")[-1]
#        editor = self.getEditor(fichier= fn, jdc = jdc ,include=1)
#        self.appliEficas.addToRecentList(editor.getFileName())
#

##PNPNPNPN --> a affiner
#        if fichier is None:
#            self.untitledCount += 1
#            self.myQtab.addTab(win, tr("Fichier non encore nomme ", self.untitledCount))
#            #self.myQtab.addTab(win, str(self.appliEficas.code))
#        else:
#            liste=fichier.split('/')
#            txt =  liste[-1]
#            if not QFileInfo(fichier).isWritable():
#                txt = '%s (ro)' % txt
#            self.myQtab.addTab(win,txt )
#        self.myQtab.setCurrentWidget(win)
#        self.currentEditor=win
#        win.setFocus()
#
#   def getOpenStartDir(self) :
#       #PN --> Les Preferences
#        try :
#            userDir=os.path.expanduser("~/Eficas_install/")
#            return userDir
#        except :
#            return ""
#
#
#   def checkDirty(self, editor,texte):
#        """
#        Private method to check dirty status and open a message window.
#        
#        @param editor editor window to check
#        @return flag indicating successful reset of the dirty flag (boolean)
#        """        
#        res=1 
#        if (editor.modified) and (editor in self.doubles) :
#            msgBox = QMessageBox(None)
#            msgBox.setWindowTitle(tr("Fichier Duplique"))
#            msgBox.setText(tr("Le fichier ne sera pas sauvegarde."))
#            msgBox.addButton(texte,0)
#            msgBox.addButton(tr("&Annuler"),1)
#            res=msgBox.exec_()
#            if res == 0 : return 1
#            return 2
#        if editor.modified:
#            fn = editor.getFileName()
#            if fn is None: fn = tr('Noname')
#            msgBox = QMessageBox(None)
#            msgBox.setWindowTitle(tr("Fichier Modifie"))
#            msgBox.setText(tr("Le fichier ne sera pas sauvegarde."))
#            msgBox.addButton(tr("&Sauvegarder"),1)
#            msgBox.addButton(tr("&Quitter sans sauvegarder"),0)
#            msgBox.addButton(tr("&Annuler"),2)
#            res=msgBox.exec_()
#            if res == 2 : return res
#            if res == 0:
#                (ok, newName) = editor.saveFile()
#                if ok:
#                    fileName=os.path.basename(six.text_type(newName))
#                    index=self.myQtab.currentIndex()
#                    self.myQtab.setTabText(index,fileName)
#                return ok
#        return res
#
#   def handleAjoutGroup(self,listeGroup):
#       index=self.myQtab.currentIndex()
#       if index < 0 : return
#       editor=self.dict_editors[index]
#       editor.handleAjoutGroup(listeGroup)
