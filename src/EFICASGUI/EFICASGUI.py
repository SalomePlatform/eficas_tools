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
import salomedsgui
aGuiDS=salomedsgui.guiDS()
print "EFicasGUI :: :::::::::::::::::::::::::::::::::::::::::::::::::::::"

# -----------------------------------------------------------------------------

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
   print "EficasGUI :: OnGUIEvent :::::::::::::::::::::::::::::::::commandID,WORKSPACE = ",commandID,WORKSPACE
   if dict_command.has_key(commandID):
      print "OnGUIEvent ::::::::::  commande associée  : ",commandID      
      dict_command[commandID](WORKSPACE)
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

def definePopup(theContext, theObject, theParent):
   print "EFICASGUI --- definePopup"
   theContext = ""
   theParent = "ObjectBrowser"
   a=salome.sg.getAllSelected()
   if len(a) >0:
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

def runEficas(ws):
   eficasSalome.runEficas(ws,"ASTER",studyId=currentStudyId)
   
def runEficaspourHomard(ws):
   print "runEficas"
   eficasSalome.runEficas(ws,"HOMARD")
    
def runEficasHomard(ws):
   print "runEficas"
   eficasSalome.runEficas(None,"HOMARD")

def runEficasFichier(ws):
   """
   Lancement d'eficas à partir d'un fichier sélectionné dans l'arbre
   d'étude. 
   """
   print "runEficasFichier"
   attr=None
   code="ASTER"
   a=salome.sg.getAllSelected()
   if len(a) == 1:
      aGuiDS.setCurrentStudy(currentStudyId)
      boo,attr=aGuiDS.getExternalFileAttribute("FICHIER_EFICAS_ASTER",a[0])
      if boo :
         code = "ASTER" 
      else :
         boo,attr=aGuiDS.getExternalFileAttribute("FICHIER_EFICAS_HOMARD",a[0])
   	 code = "HOMARD"
   
   eficasSalome.runEficas(ws,code,attr,studyId=currentStudyId)

# Partie applicative

dict_command={
               941:runEficas,
               946:runEficaspourHomard,
               4041:runEficas,
               4046:runEficaspourHomard,
               9042:runEficasFichier,
             }

