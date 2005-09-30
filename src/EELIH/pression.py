# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
from qttable import QTable
# module de gestion des panneaux
from panelbase import *
# modules validateur lineedit
from validationlineedit import *
# modules de gestion des tables
from c_suppressionLigneTable import *
from c_nouvelleLigneTablePression import *
from c_table import *
# modules de base
import commands

class Pression(PanelBase):
    """
    Hérite de la classe mère PanelBase
    Définit le panneau pour le choix des pressions à appliquer pour les sous-géométries :
    - tbl = table pour l'affichage des pressions
    - controleurTable = controleur de la table
    - controleurNouvelleLigneTable = controleur pour l'ajout d'une ligne dans la table
    """
    def __init__(self, parent, appli):
        # hérite de la classe mère des panneaux
        PanelBase.__init__(self, parent, appli)
        
        # on modifie le label titre
        self.lblTitre.setText('Pressions imposés')
        
        # on modifie l'explication
        self.lblExplication.setText("Définissez le(s) groupe(s) de mailles et les pressions à appliquer :")
        
        # bouton suivant toujurs actif
        self.btnSuivant.setEnabled(1)
        
        # espacement
        self.sp2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp2, 3, 0)
        
        # création d'une QGridLayout
        self.glProprietes = QGridLayout(self.parent, 1, 2, 5)
        self.gl.addLayout(self.glProprietes, 4, 0)
        
        # ---------------- création et ajout du QTable ----------------
        self.tbl = QTable(1, 3, self.parent)
        self.tbl.setMinimumHeight(150)
        self.tbl.setMaximumHeight(200)
        self.tbl.setColumnWidth(2, 30)
        self.tbl.setRowHeight(0, 30)
        
        self.th = self.tbl.horizontalHeader()
        self.th.setLabel(0, 'Objet')
        self.th.setLabel(1, 'Pression')
        self.th.setLabel(2, '')
        
        self.tbl.verticalHeader().hide()
        self.tbl.setLeftMargin(0)
        
        self.glProprietes.addWidget(self.tbl, 0, 0)
        
        # création du controleur table
        self.controleurTable = C_table(self.tbl)

        # création du controleur pour ajout d'une nouvelle ligne dans la table
        self.controleurNouvelleLigneTable = C_nouvelleLigneTablePression(self.appli, self.controleurTable, self)
        self.controleurNouvelleLigneTable.creeBoutons()
        
        # bouton plus = nouvelle ligne
        px = QPixmap(os.path.join(os.getenv("EFICAS_ROOT_DIR"), 'share/salome/resources/plus.png'))
        icon = QIconSet(px)
        self.boutonPlus = QPushButton(icon, '', self.parent)
        self.glProprietes.addWidget(self.boutonPlus, 0, 1, Qt.AlignCenter)
        
        self.connect(self.boutonPlus, SIGNAL('clicked()'), self.controleurNouvelleLigneTable.nouvelleLigne)
    
    def suivant(self):
        """
        met à jour l'étude avec les valeurs de pressions saisies
        affiche le panneau suivant
        affiche les valeurs de l'étude (simple fonction d'aide)
        """
        self.appli.etude.setChargements(self.tbl)
        PanelBase.suivant(self)
        self.appli.etude.affiche()
