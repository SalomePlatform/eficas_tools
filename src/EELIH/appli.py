# -*- coding: iso-8859-1 -*-

# modules de l'application
from mainwindow import *
from modelisation import *
from materiau import *
import eelih

class Appli:
    """
    Définit l'application :
    - salome = référence de l'étude Salome
    - etude = définie les valeurs à saisir
    - mw = interface graphique
    - flagEficasOrAster = E si Eficas a été chargé (fichier .comm enregistré manuellement par l'utilisateur)
                          A si Aster a été chargé (fichier .comm enregistré automatiquement dans /tmp)
    """
    def __init__(self, salomeRef, flag):
        # référence à Salome
	self.salome = salomeRef
	
        # flag pour l'enregistrement du fichier de commande
	self.flagEficasOrAster = flag
	
        # création de l'étude
        self.etude = eelih.Eelih()
        
        # création de la fenêtre principale
        self.mw = MainWindow(self)
        self.mw.show()
