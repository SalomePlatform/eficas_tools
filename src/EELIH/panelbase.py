# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *

class PanelBase(QWidget):
    """
    Panneau mère pour tous les panneaux de l'application, se compose de tous les widgets
    en commun dans tous les panneaux de l'application
    - lblTitre : titre du panneau
    - lblExplication : label explication des fonctions du panneau
    - btnPrecedent : charge le panneau précédent
    - btnSuivant : charge le panneau suivant
    """
    def __init__(self, parent, appli):
        self.appli = appli
        QWidget.__init__(self, parent)
        self.parent =self
        # création d'une gridlayout pour tous les widgets
        self.gl = QGridLayout(self.parent, 8, 1)
        
        # définition et création du label titre
        self.lblTitre = QLabel("Titre", self.parent)
        self.lblTitre.setPaletteBackgroundColor(QColor(85, 85, 127))
        self.lblTitre.setPaletteForegroundColor(QColor(255, 255, 255))
        self.lblTitre.setAlignment(Qt.AlignCenter)
        self.lblTitre.setMinimumHeight(60)
        self.gl.addWidget(self.lblTitre, 0, 0)
        
        # espacement
        self.sp1 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp1, 1, 0)
        
        # définition et création du label explication
        self.lblExplication = QLabel("Explications", self.parent)
        self.lblExplication.setAlignment(Qt.AlignCenter)
        self.lblExplication.setMinimumHeight(60)
        self.gl.addWidget(self.lblExplication, 2, 0)
        
        # espacement
        self.sp3 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp3, 5, 0)
        
        # création d'un gridlayout pour les boutons précédent et suivant
        self.glBoutons = QGridLayout(self.parent, 1, 5)
        self.gl.addLayout(self.glBoutons, 6, 0)
        self.glBoutons.setColSpacing(0, 20)
        
        # définition et création du bouton précédent
        self.btnPrecedent = QPushButton("Précédent", self.parent)
        self.btnPrecedent.setMaximumWidth(100)
        self.glBoutons.addWidget(self.btnPrecedent, 0, 1)
        self.glBoutons.setColSpacing(2, 200)
        
        # définition et création du bouton suivant
        self.btnSuivant = QPushButton("Suivant", self.parent)
        self.btnSuivant.setMaximumWidth(100)
        self.btnSuivant.setEnabled(0)
        self.glBoutons.addWidget(self.btnSuivant, 0, 3)
        self.glBoutons.setColSpacing(4, 20)
        
        # espacement
        self.sp4 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp4, 7, 0)
        
        # slots et connexions
        self.connect(self.btnPrecedent, SIGNAL('clicked()'), self.precedent)
        self.connect(self.btnSuivant, SIGNAL('clicked()'), self.suivant)
    
    def precedent(self):
        """
        affiche le panneau précédent
        """
        # on est au premier panneau ->on ne fait rien
        if self.parentWidget().parentWidget().listePanels[0] <= 1 :
            pass
        # sinon on affiche le panneau précédent
        else:
            self.parentWidget().parentWidget().listePanels.insert(0, self.parentWidget().parentWidget().listePanels[0] - 1)
            del self.parentWidget().parentWidget().listePanels[1]
            self.parentWidget().raiseWidget(self.parentWidget().parentWidget().listePanels[self.parentWidget().parentWidget().listePanels[0]])
    
    def suivant(self):
        """
        affiche le panneau suivant
        """
        # on est au dernier niveau -> on close
        if self.parentWidget().parentWidget().listePanels[0] >= len(self.parentWidget().parentWidget().listePanels) - 1 :
           self.parentWidget().parentWidget().close()
        # sinon on affiche le panneau suivant
        else:
            self.parentWidget().parentWidget().listePanels.insert(0, self.parentWidget().parentWidget().listePanels[0] + 1)
            del self.parentWidget().parentWidget().listePanels[1]
            self.parentWidget().raiseWidget(self.parentWidget().parentWidget().listePanels[self.parentWidget().parentWidget().listePanels[0]])
