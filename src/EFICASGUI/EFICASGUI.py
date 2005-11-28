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
   
   palStudyManager.setCurrentStudyID( currentStudyId ) #CS_pbruno   

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
   print "_CS_GBO_ : EFICASGUI.activeStudyChanged : currentStudyId = ", currentStudyId
   print "_CS_GBO_ : EFICASGUI.activeStudyChanged : sgPyQt.getStudyId() = ", sgPyQt.getStudyId()
   
   palStudyManager.setCurrentStudyID( currentStudyId ) #CS_pbruno
   

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

def runEficas():
   print "-------------------------EFICASGUI::runEficas-------------------------"
   print currentStudyId      
   #eficasSalome.runEficas("ASTER",studyId=currentStudyId)   
   #ws = sgPyQt.getMainFrame()   
   desktop=sgPyQt.getDesktop()   
   eficasSalome.runEficas( desktop, palStudyManager, "ASTER" )
   

def runEficaspourHomard():
   print "runEficas"
   #eficasSalome.runEficas("HOMARD")
   desktop=sgPyQt.getDesktop()
   eficasSalome.runEficas( desktop, palStudyManager, "HOMARD" ) 
   
   
    
def runEficasHomard():
   print "runEficas"
   #eficasSalome.runEficas("HOMARD")
   desktop=sgPyQt.getDesktop()
   eficasSalome.runEficas( desktop, palStudyManager, "HOMARD" )
   
   

def runEficasFichier():
   """
   Lancement d'eficas � partir d'un fichier s�lectionn� dans l'arbre
   d'�tude. 
   """
   print "runEficasFichier"
   attr=None
   code=None
   a=salome.sg.getAllSelected()
   if len(a) == 1:
      aGuiDS.setCurrentStudy(currentStudyId)
      boo,attr=aGuiDS.getExternalFileAttribute("FICHIER_EFICAS_ASTER",a[0])
      if boo :
         code = "ASTER" 
      else :
         boo,attr=aGuiDS.getExternalFileAttribute("FICHIER_EFICAS_HOMARD",a[0])         
         if boo:
   	    code = "HOMARD"
   if code:
        #eficasSalome.runEficas(code,attr,studyId=currentStudyId)         
        desktop=sgPyQt.getDesktop()   
        eficasSalome.runEficas( desktop, palStudyManager, code, attr )
   

# Partie applicative

dict_command={
                941:runEficas,                
                946:runEficaspourHomard,
                4041:runEficas,                
                4046:runEficaspourHomard,
                9042:runEficasFichier,
             }
             
#CS_pbruno temporaire
import studyManager #from PAL
palStudyManager = studyManager.SalomeStudy()