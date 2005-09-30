# -*- coding: iso-8859-1 -*-

class C_suppressionLigneTable:
    """
    controleur des tables des panneaux ddl et pression, permet la suppression d'une ligne
    - c_table : controleur d'une table
    - widgetMoins = r�f�rence sur le bouton moins
    - widgetSousGeom = r�f�rence sur le combobox
    - controleurSousGeom = r�f�rence sur le controleur g�om�trie
    """
    def __init__(self, c_table, widgetMoins, widgetSousGeom, controleurSousGeom):
        self.controleurTable = c_table
        self.widgetMoins = widgetMoins
        self.widgetSousGeom = widgetSousGeom
        self.controleurSousGeom = controleurSousGeom
    
    def supprimeLigne(self):
        """
        supprime les r�f�rences sur les boutons et les controleurs associ�s des listes
        qui contiennent tous les boutons et controleurs associ�s � une table,
        supprime �galement la ligne de la table
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
