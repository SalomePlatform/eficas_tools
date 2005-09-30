# -*- coding: iso-8859-1 -*-

class C_table:
    """
    controleur des tables, permet de g�rer l'ajout et la suppression d'une ligne dans une table
    - listeBoutonsMoins = liste des boutons moins cr��s pour la table
    - listeComboGeom = liste des combobox cr��s pour la table
    - listeEditDx = liste des lineedit DX cr��s pour la table
    - listeEditDy = liste des lineedit DY cr��s pour la table
    - listeEditDz = liste des lineedit DZ cr��s pour la table
    - listeEditPression = liste des lineedit Pression cr��s pour la table
    - listeControleursMoins = liste des controleurs C_suppressionLigneTable
    - listeControleursDx = liste des controleurs Validationlineedit pour Dx
    - listeControleursDy = liste des controleurs Validationlineedit pour Dy
    - listeControleursDz = liste des controleurs Validationlineedit pour Dz
    - listeControleursPression = liste des controleurs Validationlineedit pour Pression
    - listeControleursGeoms = liste des controleurs pour r�cup�rer les sous-g�om�tries dans les combobox
    - tbl = r�f�rence sur la table
    """
    def __init__(self, table):
        self.listeBoutonsMoins             = []
        self.listeComboGeom               = []
        self.listeEditDx                           = []
        self.listeEditDy                           = []
        self.listeEditDz                           = []
        self.listeEditPression                 = []
        self.listeControleursMoins        = []
        self.listeControleursDx              = []
        self.listeControleursDy              = []
        self.listeControleursDz              = []
        self.listeControleursPression    = []
        self.listeControleursGeoms      = []
        self.tbl                                          = table
    
  
