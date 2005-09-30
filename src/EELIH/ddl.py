# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
from qttable import QTable
# modules de gestion des panneaux
from panelbase import *
# modules validateur lineedit
from validationlineedit import *
# modules controles des tables
from c_suppressionLigneTable import *
from c_nouvelleLigneTableDdl import *
from c_table import *
# modules de base
import commands

class Ddl(PanelBase):
    """
    Hérite de la classe mère PanelBase
    Définit le panneau pour le choix des degrés de liberté d'un groupe de faces :
        - tbl = table d'affichage des degrés de liberté
        - controleurTable = controleur de gestion de la table
        - controleurNouvelleLigneTable = controleur pour l'ajout d'une nouvelle ligne dans la table
        - boutonPlus = permet de créer une nouvelle ligne quand on clique dessus
    """
    def __init__(self, parent, appli):
        # hérite de la classe mère des panneaux
        PanelBase.__init__(self, parent, appli)
        
        # on modifie le label titre
        self.lblTitre.setText('Degrés de liberté imposés')
        
        # on modifie l'explication
        self.lblExplication.setText("Définissez le(s) groupe(s) de mailles et les ddls à appliquer :")
        
        # bouton suivant toujours actif
        self.btnSuivant.setEnabled(1)
        
        # espacement
        self.sp2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp2, 3, 0)
        
        # création d'une QGridLayout
        self.glProprietes = QGridLayout(self.parent, 1, 2, 5)
        self.gl.addLayout(self.glProprietes, 4, 0)
        
        # ---------------- création et ajout du QTable ----------------
        self.tbl = QTable(1, 5, self.parent)
        self.tbl.setMinimumHeight(150)
        self.tbl.setMaximumHeight(200)
        self.tbl.setColumnWidth(4, 30)
        self.tbl.setRowHeight(0, 30)
        
        self.th = self.tbl.horizontalHeader()
        self.th.setLabel(0, 'Objet')
        self.th.setLabel(1, 'DX')
        self.th.setLabel(2, 'DY')
        self.th.setLabel(3, 'DZ')
        self.th.setLabel(4, '')
        
        self.tbl.verticalHeader().hide()
        self.tbl.setLeftMargin(0)
        
        self.glProprietes.addWidget(self.tbl, 0, 0)
        
        # création du controleur de la table
        self.controleurTable = C_table(self.tbl)

        # création du controleur pour l'ajout d'une nouvelle ligne
        self.controleurNouvelleLigneTable = C_nouvelleLigneTableDdl(self.appli, self.controleurTable, self)
        # ajout de la première ligne
        self.controleurNouvelleLigneTable.creeBoutons()
        
        # bouton plus = nouvelle ligne
        px = QPixmap(os.path.join(os.getenv("EFICAS_ROOT_DIR"), 'share/salome/resources/plus.png'))
        icon = QIconSet(px)
        self.boutonPlus = QPushButton(icon, '', self.parent)
        self.glProprietes.addWidget(self.boutonPlus, 0, 1, Qt.AlignCenter)
        
        self.connect(self.boutonPlus, SIGNAL('clicked()'), self.controleurNouvelleLigneTable.nouvelleLigne)
    
    def suivant(self):
        """
        met à jour l'étude avec les valeurs des ddls saisies
        passe au panneau suivant
        affiche les valeurs mises à jour (simple fonction d'aide)
        """
        self.appli.etude.setDdls(self.tbl)
        PanelBase.suivant(self)
        self.appli.etude.affiche()
