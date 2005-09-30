# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# module de gestion des panneaux
from panelbase import *
# modules controleur de la géométrie
from c_geometrie import *
# modules de base
import commands
import os

class Geometrie(PanelBase):
    """
    Hérite de la classe mère PanelBase
    Définit le panneau pour le choix de la géométrie sur laquelle on veut travailler
    """
    def __init__(self, parent, appli):
        # hérite de la classe mère des panneaux
        PanelBase.__init__(self, parent, appli)
        
        # on modifie le label titre
        self.lblTitre.setText('Sélection de la géométrie')
        
        # on modifie l'explication
        self.lblExplication.setText("Sélectionnez la géométrie sur laquelle vous souhaitez travailler :")
        
        # espacement
        self.sp2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp2, 3, 0)
        
        # création d'une QGridLayout
        self.glProprietes = QGridLayout(self.parent, 1, 4, 5)
        self.gl.addLayout(self.glProprietes, 4, 0)
        
        # création d'un horizontalboxlayout
        self.hbl = QHBoxLayout(self.glProprietes)
        
        # création du bouton sélection
        px = QPixmap(os.path.join(os.getenv("EFICAS_ROOT_DIR"), 'share/salome/resources/select1.png'))
        icon = QIconSet(px)
        self.pbSelection = QPushButton(icon, '', self.parent)
        self.pbSelection.setFixedWidth(30)
        self.pbSelection.setFixedHeight(30)
        self.hbl.addWidget(self.pbSelection)
        
        # création du lineedit d'affichage de la géométrie sélectionnée
        self.ln = QLineEdit('', self.parent)
        self.ln.setReadOnly(1)
        self.ln.setMaximumWidth(300)
        self.hbl.addWidget(self.ln)
        self.connect(self.ln, SIGNAL('textChanged(const QString&)'), self.valid)
        
        # création du controleur géométrie
        self.controleurGeom = C_geometrie(self.appli, self)
        self.connect(self.pbSelection, SIGNAL('clicked()'), self.controleurGeom.getGeometrie)
    
    def valid(self):
        """
        rend actif le bouton suivant si une géométrie est sélectionnée et si des sous-géométries existent
        """
        if self.ln.text() != '': 
            self.btnSuivant.setEnabled(1)
        else:
            self.btnSuivant.setEnabled(0)

    def suivant(self):
        """
        met à jour les combobox des sous-géométries des tables des panneaux ddl et pression
        met à jour les maillages associés à cette géométrie dans le panneau maillage
        affiche le panneau suivant
        affiche les valeurs saisies (simple fonction d'aide)
        """
        self.controleurGeom.updateComboSousGeom()
        #self.controleurGeom.updateGeomMaillage()
	#self.controleurGeom.add_selection()
        PanelBase.suivant(self)
        self.appli.etude.affiche()
