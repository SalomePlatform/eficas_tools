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
#Cette méthode est obsolète en V3
#En V2, si on n'implémente pas cette méthode, le composant fonctionne
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
   print "setSettings: currentStudyId = " + str(currentStudyId)
   # _CS_gbo_ Voir si on peut utiliser directement sgPyQt.getStudyId()
   # dans salomedsgui?
   
   studyManager.palStudy.setCurrentStudyID( currentStudyId ) #CS_pbruno   

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
   # ne marche pas car sg est supposé résider dans une etude
   # studyId=sg.getActiveStudyId()
   currentStudyId=ID
   print "_CS_GBO_ : EFICASGUI.activeStudyChanged : currentStudyId = ", currentStudyId
   print "_CS_GBO_ : EFICASGUI.activeStudyChanged : sgPyQt.getStudyId() = ", sgPyQt.getStudyId()
   
   studyManager.palStudy.setCurrentStudyID( currentStudyId ) #CS_pbruno
   

def definePopup(theContext, theObject, theParent):    
   print "EFICASGUI --- definePopup"
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
   si un fichier est sélectionné, il est ouvert dans eficas
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
             



