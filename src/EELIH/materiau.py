# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# module de gestion des panneaux
from panelbase import *
# modules validateur lineedit
from validationlineedit import *

class Materiau(PanelBase):
    """
    Hérite de la classe mère PanelBase
    Définit le panneau pour le choix des propriétés du matériau :
        - lnE : lineedit du module d'Young
        - lnNU : lineedit du coefficient de Poisson
    """
    def __init__(self, parent, appli):
        # hérite de la classe mère des panneaux
        PanelBase.__init__(self, parent, appli)
        
        # on modifie le label titre
        self.lblTitre.setText('Propriétés du matériau')
        
        # on modifie l'explication
        self.lblExplication.setText("Définissez le module d'Young et le coefficient de Poisson :")
        
        # espacement
        self.sp2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp2, 3, 0)
        
        # création d'une QGridLayout
        self.glProprietes = QGridLayout(self.parent, 2, 3, 5)
        self.gl.addLayout(self.glProprietes, 4, 0)
        
        # ---------------- création et ajout de E ----------------
        # ajout du label E
        self.lblE = QLabel("E (module d'Young) :", self.parent)
        self.glProprietes.addWidget(self.lblE, 0, 0, Qt.AlignRight)
        # ajout du lineedit E
        self.lnE = QLineEdit(self.parent)
        self.lnE.setMaximumHeight(30)
        self.lnE.setMaximumWidth(150)
        self.lnE.setMaxLength(10)
        self.lnE.setPaletteBackgroundColor(QColor(255, 170, 255))
        self.glProprietes.addWidget(self.lnE, 0, 1)
        # ajout du label aide E
        self.lblAideE = QLabel("( E >= 0 )", self.parent)
        self.glProprietes.addWidget(self.lblAideE, 0, 2)
        
        # ---------------- création et ajout de NU ----------------
        # ajout du label NU
        self.lblNU = QLabel("NU (coefficient de Poisson) :", self.parent)
        self.glProprietes.addWidget(self.lblNU, 1, 0, Qt.AlignRight)
        # ajout du lineedit NU
        self.lnNU = QLineEdit(self.parent)
        self.lnNU.setMaximumHeight(30)
        self.lnNU.setMaximumWidth(150)
        self.lnNU.setMaxLength(10)
        self.lnNU.setPaletteBackgroundColor(QColor(255, 170, 255))
        self.glProprietes.addWidget(self.lnNU, 1, 1)
        # ajout du label aide NU
        self.lblAideNU = QLabel("( -1 <= NU <= 0.5 )", self.parent)
        self.glProprietes.addWidget(self.lblAideNU, 1, 2)
        
        # connexion des signaux et des slots
        # dès qu'une valeur est saisie, on teste sa validité
        # pour E --> ajout du validateur
        self.validE = ValidationLineEdit(0, 10000000000000, 10000000, self.lnE)
        self.connect(self.lnE, SIGNAL('textChanged(const QString&)'), self.validE.isValid)
        self.connect(self.lnE, SIGNAL('textChanged(const QString&)'), self.valid)
        # pour NU --> ajout du validateur
        self.validNU = ValidationLineEdit(-1, 0.5, 10, self.lnNU)
        self.connect(self.lnNU, SIGNAL('textChanged(const QString&)'), self.validNU.isValid)
        self.connect(self.lnNU, SIGNAL('textChanged(const QString&)'), self.valid)
    
    def suivant(self):
        """
        met à jour l'étude avec les nouvelles valeurs saisies
        affiche le panneau suivant
        affiche les nouvelles valeurs de l'étude (simple fonction d'aide)
        """
        self.appli.etude.setMateriau_e(self.lnE.text())
        self.appli.etude.setMateriau_nu(self.lnNU.text())
        PanelBase.suivant(self)
        self.appli.etude.affiche()
    
    def valid(self):
        """
        rend valide le bouton suivant si les valeurs saisies sont valides
        """
        if self.validE.isValid() and self.validNU.isValid():
            self.btnSuivant.setEnabled(1)
        else:
            self.btnSuivant.setEnabled(0)
