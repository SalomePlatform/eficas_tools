"""
    Ce module permet de lancer l'application EFICAS en affichant
    un ecran Splash pour faire patentier l'utilisateur
"""
# Modules Python
import Tkinter

# Modules Eficas
import import_code
import splash

def lance_eficas(code,fichier=None):
    """
        Lance l'appli EFICAS
    """
    root = Tkinter.Tk()
    splash.init_splash(root,code=code,titre="Lancement d'EFICAS pour %s" %code)
    splash._splash.configure(text="Chargement d'EFICAS en cours.\n Veuillez patienter ...")
    import eficas
    if fichier :
        eficas.EFICAS(root,code=code,fichier = fichier)
    else:
        eficas.EFICAS(root,code=code)

    root.mainloop()

