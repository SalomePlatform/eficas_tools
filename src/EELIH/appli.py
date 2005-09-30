# -*- coding: iso-8859-1 -*-

# modules de l'application
from mainwindow import *
from modelisation import *
from materiau import *
import eelih

class Appli:
    """
    D�finit l'application :
    - salome = r�f�rence de l'�tude Salome
    - etude = d�finie les valeurs � saisir
    - mw = interface graphique
    - flagEficasOrAster = E si Eficas a �t� charg� (fichier .comm enregistr� manuellement par l'utilisateur)
                          A si Aster a �t� charg� (fichier .comm enregistr� automatiquement dans /tmp)
    """
    def __init__(self, salomeRef, flag):
        # r�f�rence � Salome
	self.salome = salomeRef
	
        # flag pour l'enregistrement du fichier de commande
	self.flagEficasOrAster = flag
	
        # cr�ation de l'�tude
        self.etude = eelih.Eelih()
        
        # cr�ation de la fen�tre principale
        self.mw = MainWindow(self)
        self.mw.show()
