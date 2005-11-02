import qt
import notifqt
# -----------------------------------------------------------------------------
import sys

# Remplacement de la fonction exit standard par une fonction
# qui n'interrompt pas l'execution
sys._exit=sys.exit

def exit(ier):
   print "appel de exit: ",ier

#sys.exit=exit
# Fin remplacement

initialised=0
import Tkinter
root=Tkinter.Tk()
root.withdraw()

def runEficas(code="ASTER",fichier=None,studyId=None):
    global initialised
    if not initialised:
        t=Tkinter.Toplevel()
        t.withdraw()
        import dataEficas; dataEficas.init(t,code,fichier,studyId=studyId)
        t.update()
        t.deiconify()
        t.update()

        #initialised=1

def runHomard() :
    runEficas("HOMARD")

def runAster() :
    runEficas("ASTER")
