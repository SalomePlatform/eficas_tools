import qt
import notifqt
# -----------------------------------------------------------------------------
import sys

# Remplacement de la fonction exit standard par une fonction
# qui n'interrompt pas l'execution
sys._exit=sys.exit

def exit(ier):
   print "appel de exit: ",ier

sys.exit=exit
# Fin remplacement

initialised=0
import Tkinter
root=Tkinter.Tk()
root.withdraw()


def runEficas(ws,code="ASTER",fichier=None):
    global initialised
    if not initialised:
        t=Tkinter.Toplevel()
        t.withdraw()
        print t.geometry()
        print t.winfo_geometry()
        import dataEficas; dataEficas.init(t,code,fichier)
        t.update()
        print t.geometry()
        print t.winfo_geometry()
        t.deiconify()
        t.update()

        #initialised=1

def runHomard() :
    runEficas(None,"HOMARD")

def runAster() :
    runEficas(None,"ASTER")

