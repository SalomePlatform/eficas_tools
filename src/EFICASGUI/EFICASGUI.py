# -*- coding: utf-8 -*-

"""
    Interface PyQt
"""
import qt
import libSALOME_Swig
import SalomePyQt

# Variable globale pour stocker le Workspace de Salome

WORKSPACE=None
currentStudyId=None
desktop=None

# -----------------------------------------------------------------------------

import notifqt
#import Tkinter
#root.withdraw()

def g():
   print "lastWindowClosed()"
   import Tkinter
   root=Tkinter.Tk()
   root.destroy()

qt.QObject.connect(qt.qApp,qt.SIGNAL("lastWindowClosed()"),g)

# -----------------------------------------------------------------------------

import salome

sg=salome.sg
sgPyQt=SalomePyQt.SalomePyQt()


import studyManager

print "EFicasGUI :: :::::::::::::::::::::::::::::::::::::::::::::::::::::"



# -----------------------------------------------------------------------------
#Cette m�thode est obsol�te en V3
#En V2, si on n'impl�mente pas cette m�thode, le composant fonctionne
#correctement. Un message "Attribute Error" apparait dans la trace.
def setWorkSpace(workSpace):
   print "EficasGUI --- setWorkSpace"
   global WORKSPACE
   print workSpace
   WORKSPACE=workSpace
   print "WORKSPACE: ",WORKSPACE
   # le desktop
   desktop=sgPyQt.getDesktop()

   # creation d'une message box
   #qt.QMessageBox.information(d,"titre","message")

   # recuperation du workspace
   ws=sgPyQt.getMainFrame()
   print ws

# -----------------------------------------------------------------------------

def OnGUIEvent(commandID) :
   print "EficasGUI :: OnGUIEvent :::::::::::::::::::::::::::::::::commandID = ",commandID
   if dict_command.has_key(commandID):
      print "OnGUIEvent ::::::::::  commande associ�e  : ",commandID      
      dict_command[commandID]()
   else:
      print "Pas de commande associ�e a : ",commandID

# -----------------------------------------------------------------------------

def setSettings():
   """
   Cette m�thode permet les initialisations. On d�finit en particulier
   l'identifiant de l'�tude courante.
   """
   # le desktop
   desktop=sgPyQt.getDesktop()
   global currentStudyId
   currentStudyId = sgPyQt.getStudyId()
   print "setSettings: currentStudyId = " + str(currentStudyId)
   # _CS_gbo_ Voir si on peut utiliser directement sgPyQt.getStudyId()
   # dans salomedsgui?
   
   studyManager.palStudy.setCurrentStudyID( currentStudyId ) #CS_pbruno   

def activate():
   """
   Cette m�thode permet l'activation du module, s'il a �t� charg� mais pas encore
   activ� dans une �tude pr�c�dente.
   
   Portage V3.
   """
   print "--------EFICASGUI:: activate"
   setSettings()


# -----------------------------------------------------------------------------

def activeStudyChanged(ID):
   # le desktop
   desktop=sgPyQt.getDesktop()
   global currentStudyId
   # ne marche pas car sg est suppos� r�sider dans une etude
   # studyId=sg.getActiveStudyId()
   currentStudyId=ID
   
   studyManager.palStudy.setCurrentStudyID( currentStudyId ) #CS_pbruno
   

def definePopup(theContext, theObject, theParent):    
   theContext= ""
   theObject = "100"
   theParent = "ObjectBrowser"
   a=salome.sg.getAllSelected()
   print a
    
   selectedEntry = a[0]
   aType, aValue = studyManager.palStudy.getTypeAndValue( selectedEntry )
   
   if aType == studyManager.FICHIER_EFICAS_ASTER or aType == studyManager.FICHIER_EFICAS_HOMARD:
        theObject="73"    
            
   return (theContext, theObject, theParent)


def customPopup(popup, theContext, theObject, theParent):
   print "EFICASGUI --- customPopup"
   popup.removeItem(99000)
   popup.removeItem(99001)
   popup.removeItem(99002)
   popup.removeItem(99003)


def windows():
    """
    This method is called when GUI module is being created
    and initialized.
    Should return a map of the SALOME dockable windows id's
    needed to be opened when module is activated.
    """
    print "ASTERGUI::windows"
    from qt import Qt
    winMap = {}
    winMap[ SalomePyQt.WT_ObjectBrowser ] = Qt.DockLeft
    winMap[ SalomePyQt.WT_PyConsole ]     = Qt.DockBottom
    return winMap   

# -----------------------------------------------------------------------------

import eficasSalome

def runEficas():
   print "-------------------------EFICASGUI::runEficas-------------------------"
   print currentStudyId      
   #eficasSalome.runEficas("ASTER",studyId=currentStudyId)   
   #ws = sgPyQt.getMainFrame()   
   #desktop=sgPyQt.getDesktop()   
   eficasSalome.runEficas( "ASTER" )
   

def runEficaspourHomard():
   print "runEficas"
   #eficasSalome.runEficas("HOMARD")
   desktop=sgPyQt.getDesktop()
   eficasSalome.runEficas( "HOMARD" ) 
   
   
    
def runEficasHomard():
   print "runEficas"
   #eficasSalome.runEficas("HOMARD")
   #desktop=sgPyQt.getDesktop()
   eficasSalome.runEficas( "HOMARD" )
   
   

def runEficasFichier():
   """
   Lancement d'eficas pour ASTER
   si un fichier est s�lectionn�, il est ouvert dans eficas
   """
   print "runEficasFichier"
   fileName = None
   code     = None
   a=salome.sg.getAllSelected()
   if len(a) == 1:
      #studyManager.palStudy.setCurrentStudyID( currentStudyId )
      #boo,attr=aGuiDS.getExternalFileAttribute("FICHIER_EFICAS_ASTER",a[0])      
      selectedEntry = a[0]
      
      aType, aValue = studyManager.palStudy.getTypeAndValue( selectedEntry )
      if aType == studyManager.FICHIER_EFICAS_ASTER:        
        fileName = aValue
        code     = "ASTER"
      elif aType == studyManager.FICHIER_EFICAS_HOMARD:        
        fileName = aValue
        code     = "HOMARD"
      else:
        fileName=None
        code = "ASTER"
   else:        
        code = "ASTER"            
        
   if code:
        #eficasSalome.runEficas(code,attr,studyId=currentStudyId)         
        #desktop=sgPyQt.getDesktop()        
        eficasSalome.runEficas( code, fileName )
        

   

# Partie applicative

dict_command={
                941:runEficasFichier,# runEficas,
                946:runEficaspourHomard,
                4041:runEficasFichier, #runEficas,
                4046:runEficaspourHomard,
                9042:runEficasFichier,
             }
             



