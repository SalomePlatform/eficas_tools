# -*- coding: utf-8 -*-

import salome
import SMESH_utils

class C_selectionGeometrie:
    def __init__(self, c_table, widget):
        self.controleurTable = c_table
        self.widget = widget
    
    def convertit_group_maille_from_salome(self,liste_in):
        newr=[]
        if [ 1 == 1 ]:
            print liste_in
            for entree in liste_in :
                travail=[]
                travail.append(entree)
                entryname_list=SMESH_utils.entryToName(salome.myStudy,travail)
                entreeName=entryname_list[0]
                if dict_geom_numgroupe.has_key(entreeName):
                    r=dict_geom_numgroupe[entreeName]
                else:
                    r=SMESH_utils.getAsterGroupMa(salome.myStudy,travail)
                    dict_geom_numgroupe[entreeName]=r
                for i in r :
                    newr.append(i)
        else :
            print "pas de groupe de maille associé"
            showerror("Pas de groupe associé","Cet Objet ne peut pas être défini comme un ensemble de groupe de maille")
        return newr

    def convertit_entrees_en_valeurs(self,entrychaine):
        valeur=self.convertit_group_maille_from_salome(entrychaine)
        if valeur == []:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "Pb pas de fonction de conversion de la valeur Salome en valeur Aster"
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "VALEUR", valeur
        if len(valeur) == 1:
            valeur = "'" + str(valeur[0]) + "'"
        return valeur
   
    def add_selection(self):
        entrychaine=salome.sg.getAllSelected()
        if entrychaine != '':
            # apparemment inutile
            #entryname_list=SMESH_utils.entryToName(salome.myStudy,entrychaine)
            touteslesvaleurs = self.convertit_entrees_en_valeurs(entrychaine)
        if touteslesvaleurs != []: 
            # on recherche dans quelle ligne on insère la valeur sélectionnée dans Salome
            indice = self.controleurTable.listeBoutonsSelections.index(self.widget)
            # on modifie le texte du lineedit de cette ligne et de la colonne objet
            self.controleurTable.tbl.setText(indice, 1, str(touteslesvaleurs))
            self.controleurTable.tbl.adjustColumn(1)
    
dict_geom_numgroupe = { }
dict_geom_numface = { }
