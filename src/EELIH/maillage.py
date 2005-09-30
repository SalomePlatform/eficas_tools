# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# module de gestion des panneaux
from panelbase import *
# modules controleur g�om�trie
from c_geometrie import *
# modules controleur maillage
from c_maillage import *
# modules eficas conditions aux limites
import eelihCL

class Maillage(PanelBase):
    """
    H�rite de la classe m�re PanelBase
    D�finit le panneau pour le choix du maillage :
        - lblGeom2 = label qui donne le nom de la g�om�trie s�lectionn�e
        - lbMaillage = listbox qui donne le(s) maillage(s) �quivalent(s) � la g�om�trie s'il(s) existe(nt)
        - lnNouveauMaillage = lineedit pour saisir le nom du nouveau maillage si le maillage n'existe pas
        - cl = conditions aux limites
        - controleurMaillage = controleur du panneau maillage
    """
    def __init__(self, parent, appli):
        # h�rite de la classe m�re des panneaux
        PanelBase.__init__(self, parent, appli)
        
        # on modifie le label titre
        self.lblTitre.setText('D�finition du maillage')
        
        # on modifie l'explication
        self.lblExplication.setText("D�finissez un maillage sur lequel s'appliquent les conditions aux limites \nsi celui-ci n'existe pas encore :")
        
        # espacement
        self.sp2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp2, 3, 0)
        
        # cr�ation d'une QGridLayout
        self.glProprietes = QGridLayout(self.parent, 4, 3, 5)
        self.gl.addLayout(self.glProprietes, 4, 0)
        
        # ajout du label g�om�trie choisie
        self.lblGeom1 = QLabel('G�om�trie choisie :', self.parent)
        self.glProprietes.addWidget(self.lblGeom1, 0, 0, Qt.AlignRight)
        
        self.lblGeom2 = QLabel('', self.parent)
        self.lblGeom2.setPaletteBackgroundColor(QColor(255, 255, 255))
        self.lblGeom2.setMinimumWidth(200)
        self.lblGeom2.setMaximumWidth(200)
        self.lblGeom2.setFrameShape(QFrame.LineEditPanel)
        self.glProprietes.addWidget(self.lblGeom2, 0, 1, Qt.AlignLeft)
        
	# ajout du label sous g�om�trie
	self.lblSousGeom1 = QLabel('Sous-g�om�trie :', self.parent)
	self.glProprietes.addWidget(self.lblSousGeom1, 1, 0, Qt.AlignRight)

	self.lblSousGeom2 = QLabel('', self.parent)
        self.lblSousGeom2.setPaletteBackgroundColor(QColor(255, 255, 255))
        self.lblSousGeom2.setMinimumWidth(200)
        self.lblSousGeom2.setMaximumWidth(200)
        self.lblSousGeom2.setFrameShape(QFrame.LineEditPanel)
        self.glProprietes.addWidget(self.lblSousGeom2, 1, 1, Qt.AlignLeft)
	
        # ajout de la listbox des maillages correspondant � la g�om�trie
        self.lblMaillage =QLabel('S�lectionnez le(s) maillage(s) correspondant(s) :', self.parent)
        self.glProprietes.addWidget(self.lblMaillage, 2, 0, Qt.AlignRight)
        
        self.lbMaillage = QListBox(self.parent)
        self.lbMaillage.setMinimumWidth(200)
        self.lbMaillage.setMaximumWidth(200)
        self.glProprietes.addWidget(self.lbMaillage, 2, 1, Qt.AlignLeft)
        
        # ajout du lineedit pour le nom du nouveau maillage si n�cessaire
        self.lblNouveauMaillage = QLabel('Nom du nouveau maillage :', self.parent)
        self.glProprietes.addWidget(self.lblNouveauMaillage, 3, 0, Qt.AlignRight)
        
        self.lnNouveauMaillage = QLineEdit(self.parent)
        self.lnNouveauMaillage.setMinimumWidth(200)
        self.lnNouveauMaillage.setMaximumWidth(200)
        self.glProprietes.addWidget(self.lnNouveauMaillage, 3, 1, Qt.AlignLeft)
       
        self.pb = QPushButton('essai', self.parent)
        self.glProprietes.addWidget(self.pb, 3, 2, Qt.AlignCenter)
       
        # c'est le dernier panneau de l'application --> le bouton suivant devient terminer
        self.btnSuivant.setText('Terminer')
        
        # conditions aux limites
        self.cl = None
        
        # cr�ation d'un controleur maillage
        self.controleurMaillage = C_maillage(self)
        
        #self.connect(self.btnSuivant, SIGNAL('pressed()'), self.controleurMaillage.traiteMaillage)
        self.connect(self.pb, SIGNAL('clicked()'), self.controleurMaillage.traiteMaillage)
	self.connect(self.lbMaillage, SIGNAL('highlighted(int)'), self.controleurMaillage.enableBtnSuivant)
        self.connect(self.lnNouveauMaillage, SIGNAL('textChanged(const QString&)'), self.controleurMaillage.enableBtnSuivant)

    def suivant(self):
        """
        affiche le panneau suivant
        """
	print "suivant ------------------------------"
	PanelBase.suivant(self)

