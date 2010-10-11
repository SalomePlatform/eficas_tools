# -*- coding: utf-8 -*-

import os

"""
    Interface PyQt
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import salome
import SalomePyQt

from salome.kernel.studyedit import getStudyEditor

sgPyQt=SalomePyQt.SalomePyQt()

# -----------------------------------------------------------------------------

print "EFicasGUI :: :::::::::::::::::::::::::::::::::::::::::::::::::::::"

# Test Eficas directory
eficasRoot = os.getenv("EFICAS_ROOT")
if eficasRoot is None:
    QMessageBox.critical(sgPyQt.getDesktop(), "Error",
                         "Cannot initialize EFICAS module. Environment "
                         "variable EFICAS_ROOT is not set.")
elif not os.path.isdir(eficasRoot):
    QMessageBox.critical(sgPyQt.getDesktop(), "Error",
                         "Cannot initialize EFICAS module. Directory %s does "
                         "not exist (check EFICAS_ROOT environment "
                         "variable)." % eficasRoot)


################################################
# GUI context class
# Used to store actions, menus, toolbars, etc...
################################################

class GUIcontext:
    # menus/toolbars/actions IDs
    EFICAS_MENU_ID = 90
    ASTER_ID       = 941
    OM_ID          = 942
    MAP_ID         = 943
    OT_STUDY_ID    = 944
    OT_WRAPPER_ID  = 945

    # constructor
    def __init__(self):
        # create top-level menu
        self.mid = sgPyQt.createMenu("Eficas", -1, GUIcontext.EFICAS_MENU_ID,
                                     sgPyQt.defaultMenuGroup())
        # create toolbar
        self.tid = sgPyQt.createTool("Eficas")

        # create actions conditionally and fill menu and toolbar with actions
        self.addActionConditionally("Aster/prefs.py", GUIcontext.ASTER_ID,
                                    "Eficas pour Code_Aster",
                                    "Editer un jeu de commande ASTER avec Eficas",
                                    "eficaster.png")
        self.addActionConditionally("Sep/prefs.py", GUIcontext.OM_ID,
                                    "Eficas pour Outils Metier",
                                    "Editer un jeu de commande Outils Metier avec Eficas",
                                    "eficasOM.png")
        self.addActionConditionally("Map/prefs.py", GUIcontext.MAP_ID,
                                    "Eficas pour Map",
                                    "Editer un jeu de commande Map avec Eficas",
                                    "plus.png")
        self.addActionConditionally("Openturns_Study/prefs.py", GUIcontext.OT_STUDY_ID,
                                    "Eficas pour Openturns Study",
                                    "Editer un jeu de commande Openturns Study avec Eficas",
                                    "eficasotstd.png")
        self.addActionConditionally("Openturns_Wrapper/prefs.py", GUIcontext.OT_WRAPPER_ID,
                                    "Eficas pour Openturns Wrapper",
                                    "Editer un jeu de commande Openturns Wrapper avec Eficas",
                                    "eficasotwrp.png")

    def addActionConditionally(self, fileToTest, commandId, menuLabel, tipLabel, icon):
        global eficasRoot
        if os.path.isfile(os.path.join(eficasRoot, fileToTest)):
            a = sgPyQt.createAction(commandId, menuLabel, tipLabel, tipLabel, icon)
            sgPyQt.createMenu(a, self.mid)
            sgPyQt.createTool(a, self.tid)

################################################
# Global variables
################################################

# study-to-context map
__study2context__   = {}
# current context
__current_context__ = None

###
# set and return current GUI context
# study ID is passed as parameter
###
def _setContext( studyID ):
    global eficasRoot
    if eficasRoot is None:
        return
    global __study2context__, __current_context__
    if not __study2context__.has_key(studyID):
        __study2context__[studyID] = GUIcontext()
        pass
    __current_context__ = __study2context__[studyID]
    return __current_context__


# -----------------------------------------------------------------------------

def OnGUIEvent(commandID) :
   if dict_command.has_key(commandID):
      print "OnGUIEvent ::::::::::  commande associée  : ",commandID      
      dict_command[commandID]()
   else:
      print "Pas de commande associée a : ",commandID

# -----------------------------------------------------------------------------

def setSettings():
   """
   Cette méthode permet les initialisations.
   """
   _setContext(sgPyQt.getStudyId())

def activate():
   """
   Cette méthode permet l'activation du module, s'il a été chargé mais pas encore
   activé dans une étude précédente.
   
   Portage V3.
   """
   setSettings()


# -----------------------------------------------------------------------------

def activeStudyChanged(ID):
   _setContext(ID)


#def definePopup(theContext, theObject, theParent):    
#   print "EFICASGUI --- definePopup"
#   print "EFICASGUI --- definePopup"
#   theContext= ""
#   theObject = "100"
#   theParent = "ObjectBrowser"
#   a=salome.sg.getAllSelected()
    
#   selectedEntry = a[0]
#   mySO = monEditor.study.FindObjectID(selectedEntry);
#   aType = monEditor.getFileType(mySO)
#   print aType
#   return (theContext, theObject, theParent)


#def customPopup(popup, theContext, theObject, theParent):
#   a=salome.sg.getAllSelected()

#   selectedEntry = a[0]
#   mySO = monEditor.study.FindObjectID(selectedEntry);
#   aType = monEditor.getFileType(mySO)

#   print "EFICASGUI --- customPopup"
#   print "EFICASGUI --- customPopup"
#   print "EFICASGUI --- customPopup"
#   print "EFICASGUI --- customPopup"
#   print "EFICASGUI --- customPopup"
#   print "EFICASGUI --- customPopup"
#   print "EFICASGUI --- customPopup"
#   print "EFICASGUI --- customPopup"
#   popup.removeItem(99003)



# -----------------------------------------------------------------------------

def runEficas():
   print "-------------------------EFICASGUI::runEficas-------------------------"
   import eficasSalome
   eficasSalome.runEficas( "ASTER" )
   
   
def runEficaspourOpenturnsStudy():
   print "runEficas Pour Openturns Study"
   import eficasSalome
   eficasSalome.runEficas( "OPENTURNS_STUDY" ) 
   
def runEficaspourOpenturnsWrapper():
   print "runEficas Pour Openturns Wrapper"
   import eficasSalome
   eficasSalome.runEficas( "OPENTURNS_WRAPPER" ) 
   
def runEficaspourOM():
   print "runEficas Pour Outils Metier"
   import eficasSalome
   eficasSalome.runEficas( "SEP" )
   
def runEficaspourMap():
   print "runEficas Pour Map "
   import eficasSalome
   eficasSalome.runEficas( "MAP" )
   
   

def runEficasFichier(version=None):
   """
   Lancement d'eficas pour ASTER
   si un fichier est sélectionné, il est ouvert dans eficas
   """
   fileName = None
   code     = None
   a=salome.sg.getAllSelected()
   if len(a) == 1:
      selectedEntry = a[0]
      
      editor = getStudyEditor()
      mySO = editor.study.FindObjectID(selectedEntry);
      aType = editor.getFileType(mySO)
      aValue = editor.getFileName(mySO)
      if aType !=  None :
        fileName = aValue
        code     = aType[15:]
   else:        
      QMessageBox.critical(None, "Selection Invalide",
             "Selectionner un seul fichier SVP") 
      return;
 
   import eficasSalome        
   if code:
        if version :
            eficasSalome.runEficas( code, fileName, version=version)
        else :
            eficasSalome.runEficas( code, fileName)
        

# Partie applicative

dict_command={
                GUIcontext.ASTER_ID      : runEficas,
                GUIcontext.OM_ID         : runEficaspourOM,
                GUIcontext.MAP_ID        : runEficaspourMap,
                GUIcontext.OT_STUDY_ID   : runEficaspourOpenturnsStudy,
                GUIcontext.OT_WRAPPER_ID : runEficaspourOpenturnsWrapper,

                9041:runEficasFichier,
             }
