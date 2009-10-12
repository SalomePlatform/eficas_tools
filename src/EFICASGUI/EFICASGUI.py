# -*- coding: utf-8 -*-

"""
    Interface PyQt
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import libSALOME_Swig
import SalomePyQt

# Variable globale pour stocker le Workspace de Salome

WORKSPACE=None
currentStudyId=None
desktop=None

# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------

import salome

sg=salome.sg
sgPyQt=SalomePyQt.SalomePyQt()

from pal.studyedit import StudyEditor
monEditor=StudyEditor()

print "EFicasGUI :: :::::::::::::::::::::::::::::::::::::::::::::::::::::"



# -----------------------------------------------------------------------------

def OnGUIEvent(commandID) :
   print "EficasGUI :: OnGUIEvent :::::::::::::::::::::::::::::::::commandID = ",commandID
   if dict_command.has_key(commandID):
      print "OnGUIEvent ::::::::::  commande associée  : ",commandID      
      dict_command[commandID]()
   else:
      print "Pas de commande associée a : ",commandID

# -----------------------------------------------------------------------------

def setSettings():
   """
   Cette méthode permet les initialisations. On définit en particulier
   l'identifiant de l'étude courante.
   """
   # le desktop
   desktop=sgPyQt.getDesktop()
   global currentStudyId
   currentStudyId = sgPyQt.getStudyId()

def activate():
   """
   Cette méthode permet l'activation du module, s'il a été chargé mais pas encore
   activé dans une étude précédente.
   
   Portage V3.
   """
   print "--------EFICASGUI:: activate"
   setSettings()


# -----------------------------------------------------------------------------

def activeStudyChanged(ID):
   # le desktop
   desktop=sgPyQt.getDesktop()
   global currentStudyId
   currentStudyId=ID
   
   

def definePopup(theContext, theObject, theParent):    
   theContext= ""
   theObject = "100"
   theParent = "ObjectBrowser"
   a=salome.sg.getAllSelected()
    
   selectedEntry = a[0]
   mySO = monEditor.study.FindObjectID(selectedEntry);
   aType = monEditor.getFileType(mySO)
   if aType == "FICHIER_EFICAS_ASTER" :
        theObject="73"    
            
   return (theContext, theObject, theParent)


def customPopup(popup, theContext, theObject, theParent):
   print "EFICASGUI --- customPopup TODO"
   print "EFICASGUI --- customPopup"
   print "EFICASGUI --- customPopup"
   print "EFICASGUI --- customPopup"
   print "EFICASGUI --- customPopup"
   print "EFICASGUI --- customPopup"
   print "EFICASGUI --- customPopup"
   print "EFICASGUI --- customPopup"
   print "EFICASGUI --- customPopup"
#   popup.removeItem(99003)



# -----------------------------------------------------------------------------

import eficasSalome

def runEficas():
   print "-------------------------EFICASGUI::runEficas-------------------------"
   print currentStudyId      
   eficasSalome.runEficas( "ASTER" )
   

   
def runEficaspourOpenturnsStudy():
   print "runEficas Pour Openturns Study"
   desktop=sgPyQt.getDesktop()
   eficasSalome.runEficas( "OPENTURNS_STUDY" ) 
   
def runEficaspourOpenturnsWrapper():
   print "runEficas Pour Openturns Wrapper"
   desktop=sgPyQt.getDesktop()
   eficasSalome.runEficas( "OPENTURNS_WRAPPER" ) 
   
def runEficaspourOM():
   print "runEficas Pour Outils Metier"
   desktop=sgPyQt.getDesktop()
   eficasSalome.runEficas( "SEP" )
   
   

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
      
      mySO = monEditor.study.FindObjectID(selectedEntry);
      aType = monEditor.getFileType(mySO)
      aValue = monEditor.getFileName(mySO)
      if aType == "FICHIER_EFICAS_ASTER":        
        fileName = aValue
        code     = "ASTER"
      elif aType == "FICHIER_EFICAS_SEP":        
        fileName = aValue
        code     = "SEP"
      elif aType == "FICHIER_EFICAS_OPENTURNS":        
        fileName = aValue
        code     = "OPENTURNS"
      else:
        fileName=None
        code = "ASTER"
   else:        
        code = "ASTER"            
        
   if code:
        #eficasSalome.runEficas(code,attr,studyId=currentStudyId)         
        #desktop=sgPyQt.getDesktop()        
        if version :
            eficasSalome.runEficas( code, fileName, version=version)
        else :
            eficasSalome.runEficas( code, fileName)
        

# Partie applicative

dict_command={
                941:runEficasFichier,# runEficas,
                942:runEficaspourOM,# runEficas,
                947:runEficaspourOpenturnsStudy,
                948:runEficaspourOpenturnsWrapper,

                4041:runEficasFichier, #runEficas,
                4042:runEficaspourOM,# runEficas,
                4047:runEficaspourOpenturnsStudy,
                4048:runEficaspourOpenturnsWrapper,

                9041:runEficasFichier,
                9042:runEficaspourOM,# runEficas,
                9047:runEficaspourOpenturnsStudy,
                9048:runEficaspourOpenturnsWrapper,
             }
             
