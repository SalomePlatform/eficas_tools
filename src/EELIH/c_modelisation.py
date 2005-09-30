# -*- coding: utf-8 -*-

class C_modelisation:
    """
    controleur de la classe Modelisation, si la modélisation est 2D on cache la colonne DZ
    de la table du panneau ddl
    - modelisation = référence sur le panneau modélisation
    """
    def __init__(self, modelisation):
        self.modelisation = modelisation
    
    def enableDZ(self):
        """
        si la modélisation est 2D on cache la colonne DZ de la table du panneau ddl
        """
        # modélisation 2D --> on cache
        if self.modelisation.cmb.currentText().latin1() != '3D':
            self.modelisation.appli.mw.ddl.tbl.hideColumn(3)
        # modélisation 3D --> on montre
        else:
            self.modelisation.appli.mw.ddl.tbl.showColumn(3)
