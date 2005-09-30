# -*- coding: iso-8859-1 -*-

class C_table:
    """
    controleur des tables, permet de gérer l'ajout et la suppression d'une ligne dans une table
    - listeBoutonsMoins = liste des boutons moins créés pour la table
    - listeComboGeom = liste des combobox créés pour la table
    - listeEditDx = liste des lineedit DX créés pour la table
    - listeEditDy = liste des lineedit DY créés pour la table
    - listeEditDz = liste des lineedit DZ créés pour la table
    - listeEditPression = liste des lineedit Pression créés pour la table
    - listeControleursMoins = liste des controleurs C_suppressionLigneTable
    - listeControleursDx = liste des controleurs Validationlineedit pour Dx
    - listeControleursDy = liste des controleurs Validationlineedit pour Dy
    - listeControleursDz = liste des controleurs Validationlineedit pour Dz
    - listeControleursPression = liste des controleurs Validationlineedit pour Pression
    - listeControleursGeoms = liste des controleurs pour récupérer les sous-géométries dans les combobox
    - tbl = référence sur la table
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
    
  
