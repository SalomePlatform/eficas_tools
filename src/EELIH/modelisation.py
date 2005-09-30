# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# module de gestion des panneaux
from panelbase import *
# modules panneau materiau
from materiau import *
# modules controleur panneau modelisation
from c_modelisation import *

class Modelisation(PanelBase):
    """
    Hérite de la classe mère PanelBase
    Définit le panneau pour le choix de la modélisation :
    - cmb = combobox pour choisir le type de modélisation
    """
    def __init__(self, parent, appli):
        # hérite de la classe mère des panneaux
        PanelBase.__init__(self, parent, appli)
        
        # liste des choix possibles
        self.listeChoix = ['3D', '2D_CONTRAINTES_PLANES', '2D_DEFORMATIONS_PLANES', '2D_AXISYMETRIQUE']
        
        # on modifie le label titre
        self.lblTitre.setText("Modélisation")
        
        # on modifie l'explication
        self.lblExplication.setText("Quelle type de modélisation souhaitez-vous réaliser ?")
        
        # bouton suivant toujours valide
        self.btnSuivant.setEnabled(1)
        
        # espacement
        self.sp2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp2, 3, 0)
        #self.gl.setRowSpacing(3, 100)
        
        # création et ajout du combobox
        self.cmb = QComboBox(0, self.parent)
        self.cmb.insertStrList(self.listeChoix)
        self.cmb.setMaximumWidth(250)
        self.gl.addWidget(self.cmb, 4, 0, Qt.AlignCenter)
        
        # création du controleur modelisation
        self.controleurModelisation = C_modelisation(self)
        
        self.connect(self.cmb, SIGNAL('activated(const QString&)'), self.controleurModelisation.enableDZ)
    
    def suivant(self):
        """
        met à jour l'étude avec la valeur de la modélisation choisie
        affiche le panneau suivant
        affiche les valeurs de l'étude (simple fonction d'aide)
        """
        self.appli.etude.setModelisation(self.cmb.currentText())
        PanelBase.suivant(self)
        self.appli.etude.affiche()
