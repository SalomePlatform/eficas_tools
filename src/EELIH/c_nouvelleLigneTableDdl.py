# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# modules de gestion des tables
from c_suppressionLigneTable import *
# modules controleur de la g�om�trie
from c_geometrie import *
# modules de base
import commands
import os
# modules validateur de lineedit
from validationlineedit import *

class C_nouvelleLigneTableDdl(QWidget):
    """
    controleur de la table du panneau ddl, permet la cr�ation d'une ligne de cette table
    - appli = r�f�rence sur l'application
    - c_table = r�f�rence sur le controleur table (permet le contr�le de la table)
    - ddl = r�f�rence sur le panneau ddl
    """
    def __init__(self, appli, c_table, ddl):
        self.appli = appli
        self.controleurTable = c_table
        self.ddl = ddl
    
    def nouvelleLigne(self):
        """
        ins�re une nouvelle ligne dans la table
        """
        # insertion de la ligne
        self.controleurTable.tbl.insertRows(len(self.controleurTable.listeBoutonsMoins))
        self.controleurTable.tbl.setRowHeight(len(self.controleurTable.listeBoutonsMoins), 30)
        # cr�ation des boutons associ�s � cette nouvelle ligne
        self.creeBoutons()
    
    def creeBoutons(self):
        """
        cr�e les boutons associ�s � une ligne
        """
        # ajout du combobox pour le choix des sous-g�om�tries
        cmb = QComboBox(self.controleurTable.tbl)
        cmb.setMinimumWidth(100)
        cmb.setMaximumWidth(200)
        # m�thode pour r�cup�rer les sous g�om�tries
        self.controleurTable.listeComboGeom.append(cmb)
        controleurSousGeom = C_geometrie(self.appli, self.ddl)
        self.controleurTable.listeControleursGeoms.append(controleurSousGeom)
        liste = self.appli.etude.sousGeometrie
        cmb.insertStrList(liste)
        # ajout du combobox g�om�trie dans la nouvelle ligne
        self.controleurTable.tbl.setCellWidget(len(self.controleurTable.listeBoutonsMoins), 0, cmb)
        self.controleurTable.tbl.adjustColumn(0)
        
        # ajout du lineedit dx dans la nouvelle ligne
        lnx = QLineEdit('', self.controleurTable.tbl)
        lnx.setPaletteBackgroundColor(QColor(255, 170, 255))
        self.controleurTable.listeEditDx.append(lnx)
        validateur = ValidationLineEdit(None, None, None, lnx)
        self.controleurTable.listeControleursDx.append(validateur)
        self.connect(lnx, SIGNAL('textChanged(const QString&)'), self.controleurTable.listeControleursDx[self.controleurTable.listeEditDx.index(lnx)].isValid) 
        self.controleurTable.tbl.setCellWidget(len(self.controleurTable.listeBoutonsMoins), 1, lnx)
        
        # ajout du lineedit dy dans la nouvelle ligne
        lny = QLineEdit('', self.controleurTable.tbl)
        lny.setPaletteBackgroundColor(QColor(255, 170, 255))
        self.controleurTable.listeEditDy.append(lny)
        validateur = ValidationLineEdit(None, None, None, lny)
        self.controleurTable.listeControleursDy.append(validateur)
        self.connect(lny, SIGNAL('textChanged(const QString&)'), self.controleurTable.listeControleursDy[self.controleurTable.listeEditDy.index(lny)].isValid) 
        self.controleurTable.tbl.setCellWidget(len(self.controleurTable.listeBoutonsMoins), 2, lny)
        
        # ajout du lineedit dz dans la nouvelle ligne
        lnz = QLineEdit('', self.controleurTable.tbl)
        lnz.setPaletteBackgroundColor(QColor(255, 170, 255))
        self.controleurTable.listeEditDz.append(lnz)
        validateur = ValidationLineEdit(None, None, None, lnz)
        self.controleurTable.listeControleursDz.append(validateur)
        self.connect(lnz, SIGNAL('textChanged(const QString&)'), self.controleurTable.listeControleursDz[self.controleurTable.listeEditDz.index(lnz)].isValid) 
        self.controleurTable.tbl.setCellWidget(len(self.controleurTable.listeBoutonsMoins), 3, lnz)
        
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
        self.controleurTable.tbl.setCellWidget(len(self.controleurTable.listeBoutonsMoins) - 1, 4, pbMoins)
