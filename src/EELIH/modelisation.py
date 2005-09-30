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
    H�rite de la classe m�re PanelBase
    D�finit le panneau pour le choix de la mod�lisation :
    - cmb = combobox pour choisir le type de mod�lisation
    """
    def __init__(self, parent, appli):
        # h�rite de la classe m�re des panneaux
        PanelBase.__init__(self, parent, appli)
        
        # liste des choix possibles
        self.listeChoix = ['3D', '2D_CONTRAINTES_PLANES', '2D_DEFORMATIONS_PLANES', '2D_AXISYMETRIQUE']
        
        # on modifie le label titre
        self.lblTitre.setText("Mod�lisation")
        
        # on modifie l'explication
        self.lblExplication.setText("Quelle type de mod�lisation souhaitez-vous r�aliser ?")
        
        # bouton suivant toujours valide
        self.btnSuivant.setEnabled(1)
        
        # espacement
        self.sp2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp2, 3, 0)
        #self.gl.setRowSpacing(3, 100)
        
        # cr�ation et ajout du combobox
        self.cmb = QComboBox(0, self.parent)
        self.cmb.insertStrList(self.listeChoix)
        self.cmb.setMaximumWidth(250)
        self.gl.addWidget(self.cmb, 4, 0, Qt.AlignCenter)
        
        # cr�ation du controleur modelisation
        self.controleurModelisation = C_modelisation(self)
        
        self.connect(self.cmb, SIGNAL('activated(const QString&)'), self.controleurModelisation.enableDZ)
    
    def suivant(self):
        """
        met � jour l'�tude avec la valeur de la mod�lisation choisie
        affiche le panneau suivant
        affiche les valeurs de l'�tude (simple fonction d'aide)
        """
        self.appli.etude.setModelisation(self.cmb.currentText())
        PanelBase.suivant(self)
        self.appli.etude.affiche()
