import sys,os

eficas_root=os.environ["EFICAS_ROOT"]

sys.path[:0]=[os.path.join(eficas_root,'Aster'),
              os.path.join(eficas_root,'Homard'),
              eficas_root,
#             os.path.join(eficas_root,'Editeur'),
             ]

# Modules Python
import Tkinter
import sys

# Modules Eficas
#import import_code
from Editeur import splash
from Editeur import eficas

# _CS_gbo Gestion du versionning entre eficas 1.7 et 1.8 (différence
# en ce qui concerne la session).
try:
    from Editeur import session
except:
    session=None

def init(top,code="ASTER",fichier=None,studyId=None):
    splash.init_splash(top,code=code,titre="Lancement d'EFICAS pour %s" %code)
    splash._splash.configure(text="Chargement d'EFICAS en cours.\n Veuillez patienter ...")
    # Enregistrement dans l étude
    import eficasEtude
    MaRef=eficasEtude.Eficas_In_Study(code,studyId=studyId)

    #import eficas
    class MyEficas(eficas.EFICAS):
        def quit(self):
            eficas.EFICAS.quit(self)
            self.top.destroy()
        
        def contexte(self):
            self.salome=MaRef

    # _CS_gbo Gestion du versionning 1.7 et 1.8
    if session is not None:
        if fichier != None :
            options=session.parse(sys.argv+[fichier])
        else :
            options=session.parse(sys.argv)
    
    moi=MyEficas(top,code=code)
    moi.contexte()
