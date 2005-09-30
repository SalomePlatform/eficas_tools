# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# modules de gestions des tables
from c_suppressionLigneTable import *
# modules controleur géométrie
from c_geometrie import *
# modules de base
import commands
import os
# modules validateur de lineedit
from validationlineedit import *

class C_nouvelleLigneTablePression(QWidget):
    """
    controleur de la table du panneau pression, permet la création d'une ligne de cette table
    - appli = référence sur l'application
    - controleurTable = référence sur le controleur de la table
    - pression = référence sur le panneau pression
    """
    def __init__(self, appli, c_table, pression):
        self.appli = appli
        self.controleurTable = c_table
        self.pression = pression
    
    def nouvelleLigne(self):
        """
        insère une nouvelle ligne dans la table
        """
        # création de la ligne
        self.controleurTable.tbl.insertRows(len(self.controleurTable.listeBoutonsMoins))
        self.controleurTable.tbl.setRowHeight(len(self.controleurTable.listeBoutonsMoins), 30)
        # création des boutons associés à cette nouvelle ligne
        self.creeBoutons()
    
    def creeBoutons(self):
        """
        crée les boutons associés à une ligne
        """
        # ajout du combobox pour le choix des sous-géométries
        cmb = QComboBox(self.controleurTable.tbl)
        cmb.setMinimumWidth(50)
        cmb.setMaximumWidth(200)
        # méthode pour récupérer les sous géométries
        self.controleurTable.listeComboGeom.append(cmb)
        controleurSousGeom = C_geometrie(self.appli, self.pression)
        self.controleurTable.listeControleursGeoms.append(controleurSousGeom)
        liste = self.appli.etude.sousGeometrie
        cmb.insertStrList(liste)
        # ajout du combobox géométrie dans la nouvelle ligne
        self.controleurTable.tbl.setCellWidget(len(self.controleurTable.listeBoutonsMoins), 0, cmb)
        self.controleurTable.tbl.adjustColumn(0)
        
        # ajout du lineedit Pression dans la nouvelle ligne
        lnf = QLineEdit('', self.controleurTable.tbl)
        lnf.setPaletteBackgroundColor(QColor(255, 170, 255))
        self.controleurTable.listeEditPression.append(lnf)
        validateur = ValidationLineEdit(None, None, None, lnf)
        self.controleurTable.listeControleursPression.append(validateur)
        self.connect(lnf, SIGNAL('textChanged(const QString&)'), self.controleurTable.listeControleursPression[self.controleurTable.listeEditPression.index(lnf)].isValid) 
        self.controleurTable.tbl.setCellWidget(len(self.controleurTable.listeBoutonsMoins), 1, lnf)
        
        # ajout du bouton moins dans la liste
        px = QPixmap(os.path.join(os.getenv("EFICAS_ROOT_DIR"), 'share/salome/resources/moins.png'))
        icon = QIconSet(px)
        pbMoins = QPushButton(icon, '', self.controleurTable.tbl)
        pbMoins.setFixedWidth(30)
        pbMoins.setFixedHeight(30)
        self.controleurTable.listeBoutonsMoins.append(pbMoins)
        controleurLigne = C_suppressionLigneTable(self.controleurTable, pbMoins, cmb, controleurSousGeom)
        self.controleurTable.listeControleursMoins.append(controleurLigne)
        self.connect(pbMoins, SIGNAL('clicked()'), self.controleurTable.listeControleursMoins[self.controleurTable.listeBoutonsMoins.index(pbMoins)].supprimeLigne)
        # ajout du bouton moins dans la nouvelle ligne
        self.controleurTable.tbl.setCellWidget(len(self.controleurTable.listeBoutonsMoins) - 1, 2, pbMoins)
