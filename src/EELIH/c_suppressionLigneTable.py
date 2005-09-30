# -*- coding: iso-8859-1 -*-

class C_suppressionLigneTable:
    """
    controleur des tables des panneaux ddl et pression, permet la suppression d'une ligne
    - c_table : controleur d'une table
    - widgetMoins = référence sur le bouton moins
    - widgetSousGeom = référence sur le combobox
    - controleurSousGeom = référence sur le controleur géométrie
    """
    def __init__(self, c_table, widgetMoins, widgetSousGeom, controleurSousGeom):
        self.controleurTable = c_table
        self.widgetMoins = widgetMoins
        self.widgetSousGeom = widgetSousGeom
        self.controleurSousGeom = controleurSousGeom
    
    def supprimeLigne(self):
        """
        supprime les références sur les boutons et les controleurs associés des listes
        qui contiennent tous les boutons et controleurs associés à une table,
        supprime également la ligne de la table
        """
        indice = self.controleurTable.listeBoutonsMoins.index(self.widgetMoins)
        
        # suppression des listes
        self.controleurTable.listeBoutonsMoins.remove(self.widgetMoins)
        if self.widgetSousGeom != None:
            self.controleurTable.listeComboGeom.remove(self.widgetSousGeom)
        self.controleurTable.listeControleursMoins.remove(self)
        if self.controleurSousGeom != None:
            self.controleurTable.listeControleursGeoms.remove(self.controleurSousGeom)
        # suppression de la ligne de la table
        self.controleurTable.tbl.removeRow(indice)
