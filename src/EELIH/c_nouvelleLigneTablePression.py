# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# modules de gestions des tables
from c_suppressionLigneTable import *
# modules controleur g�om�trie
from c_geometrie import *
# modules de base
import commands
import os
# modules validateur de lineedit
from validationlineedit import *

class C_nouvelleLigneTablePression(QWidget):
    """
    controleur de la table du panneau pression, permet la cr�ation d'une ligne de cette table
    - appli = r�f�rence sur l'application
    - controleurTable = r�f�rence sur le controleur de la table
    - pression = r�f�rence sur le panneau pression
    """
    def __init__(self, appli, c_table, pression):
        self.appli = appli
        self.controleurTable = c_table
        self.pression = pression
    
    def nouvelleLigne(self):
        """
        ins�re une nouvelle ligne dans la table
        """
        # cr�ation de la ligne
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
        cmb.setMinimumWidth(50)
        cmb.setMaximumWidth(200)
        # m�thode pour r�cup�rer les sous g�om�tries
        self.controleurTable.listeComboGeom.append(cmb)
        controleurSousGeom = C_geometrie(self.appli, self.pression)
        self.controleurTable.listeControleursGeoms.append(controleurSousGeom)
        liste = self.appli.etude.sousGeometrie
        cmb.insertStrList(liste)
        # ajout du combobox g�om�trie dans la nouvelle ligne
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
