# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# module de gestion des panneaux
from panelbase import *
# modules controleur de la g�om�trie
from c_geometrie import *
# modules de base
import commands
import os

class Geometrie(PanelBase):
    """
    H�rite de la classe m�re PanelBase
    D�finit le panneau pour le choix de la g�om�trie sur laquelle on veut travailler
    """
    def __init__(self, parent, appli):
        # h�rite de la classe m�re des panneaux
        PanelBase.__init__(self, parent, appli)
        
        # on modifie le label titre
        self.lblTitre.setText('S�lection de la g�om�trie')
        
        # on modifie l'explication
        self.lblExplication.setText("S�lectionnez la g�om�trie sur laquelle vous souhaitez travailler :")
        
        # espacement
        self.sp2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp2, 3, 0)
        
        # cr�ation d'une QGridLayout
        self.glProprietes = QGridLayout(self.parent, 1, 4, 5)
        self.gl.addLayout(self.glProprietes, 4, 0)
        
        # cr�ation d'un horizontalboxlayout
        self.hbl = QHBoxLayout(self.glProprietes)
        
        # cr�ation du bouton s�lection
        px = QPixmap(os.path.join(os.getenv("EFICAS_ROOT_DIR"), 'share/salome/resources/select1.png'))
        icon = QIconSet(px)
        self.pbSelection = QPushButton(icon, '', self.parent)
        self.pbSelection.setFixedWidth(30)
        self.pbSelection.setFixedHeight(30)
        self.hbl.addWidget(self.pbSelection)
        
        # cr�ation du lineedit d'affichage de la g�om�trie s�lectionn�e
        self.ln = QLineEdit('', self.parent)
        self.ln.setReadOnly(1)
        self.ln.setMaximumWidth(300)
        self.hbl.addWidget(self.ln)
        self.connect(self.ln, SIGNAL('textChanged(const QString&)'), self.valid)
        
        # cr�ation du controleur g�om�trie
        self.controleurGeom = C_geometrie(self.appli, self)
        self.connect(self.pbSelection, SIGNAL('clicked()'), self.controleurGeom.getGeometrie)
    
    def valid(self):
        """
        rend actif le bouton suivant si une g�om�trie est s�lectionn�e et si des sous-g�om�tries existent
        """
        if self.ln.text() != '': 
            self.btnSuivant.setEnabled(1)
        else:
            self.btnSuivant.setEnabled(0)

    def suivant(self):
        """
        met � jour les combobox des sous-g�om�tries des tables des panneaux ddl et pression
        met � jour les maillages associ�s � cette g�om�trie dans le panneau maillage
        affiche le panneau suivant
        affiche les valeurs saisies (simple fonction d'aide)
        """
        self.controleurGeom.updateComboSousGeom()
        #self.controleurGeom.updateGeomMaillage()
	#self.controleurGeom.add_selection()
        PanelBase.suivant(self)
        self.appli.etude.affiche()
