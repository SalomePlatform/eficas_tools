# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# modules panneau modelisation
from modelisation import *
# modules panneau materiau
from materiau import *
# modules panneau ddl
from ddl import *
# modules panneau pression
from pression import *
# modules panneau publication
from publication import *
# modules panneau geometrie
from geometrie import *
# modules panneau maillage
from maillage import *

class MainWindow(QMainWindow):
    """
    Définit la fenêtre principale de l'application
    - ws = widgetStack (pile des panneaux à afficher)
    - listePanels = liste de l'ordre d'affichage des panneaux
    """
    def __init__(self, appli):
        self.appli = appli
        QMainWindow.__init__(self, None, "Etude élastique linéaire isotrope homogène", Qt.WDestructiveClose)
        self.setCaption("Etude élastique linéaire isotrope homogène")
        self.resize(800, 400)
        
        # création de la pile des panneaux
        self.ws = QWidgetStack(self)        
        self.ws.show()
        self.setCentralWidget(self.ws)
        
        # création des différents panneaux
        self.modelisation = Modelisation(self.ws, self.appli)
        self.materiau = Materiau(self.ws, self.appli)
        self.geometrie = Geometrie(self.ws, self.appli)
        self.ddl = Ddl(self.ws, self.appli)
        self.pression = Pression(self.ws, self.appli)
        #self.maillage = Maillage(self.ws, self.appli)
        self.publication = Publication(self.ws, self.appli, self.appli.salome)
        
        # liste d'ordre d'affichage des panneaux
        self.listePanels = [1, self.modelisation, self.materiau, self.geometrie, self.ddl, self.pression, self.publication]

        # ajout des panneaux dans la pile
        for wid in self.listePanels[1:]:
            self.ws.addWidget(wid)
        
        # affichage du premier panneau
        self.ws.raiseWidget(self.listePanels[1])
