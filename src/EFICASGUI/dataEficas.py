import sys,os

eficas_root=os.environ["EFICAS_ROOT"]

sys.path[:0]=[os.path.join(eficas_root,'Aster'),
              os.path.join(eficas_root,'Homard'),
              eficas_root,
#             os.path.join(eficas_root,'Editeur'),
             ]

# Modules Python
import Tkinter

# Modules Eficas
#import import_code
from Editeur import splash
from Editeur import eficas


def init(top,code="ASTER",fichier=None):
    splash.init_splash(top,code=code,titre="Lancement d'EFICAS pour %s" %code)
    splash._splash.configure(text="Chargement d'EFICAS en cours.\n Veuillez patienter ...")
    # Enregistrement dans l étude
    import eficasEtude
    MaRef=eficasEtude.Eficas_In_Study(code)

    #import eficas
    class MyEficas(eficas.EFICAS):
        def quit(self):
            eficas.EFICAS.quit(self)
            self.top.destroy()
        
        def contexte(self):
            self.salome=MaRef

    print code
    moi=MyEficas(top,code=code,fichier=fichier)
    moi.contexte()
