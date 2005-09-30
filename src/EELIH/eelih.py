# -*- coding: utf-8 -*-

class Eelih:
    """
    représente les données de l'étude :
    - modelisation = type de modélisation choisie
    - materiau_e = module d'Young choisi
    - materiau_nu = coefficient de Poisson choisi
    - chargements = liste réprésentant les pressions choisies pour les sous-géométries
    - ddls = liste représentant les valeurs pour les ddls pour les sous-géométries
    - geometrie = nom de la géométrie sélectionnée dans l'arbre d'étude Salome
    - sousGeometrie = liste des sous-géométries de la géométrie choisie
    """
    def __init__(self):
      self.modelisation = None
      self.materiau_e = None
      self.materiau_nu = None
      self.chargements = None
      self.ddls = None
      self.geometrie = None
      self.sousGeometrie = None
   
    def setModelisation(self, val):
        """
        fixe la valeur de la modélisation choisie
        """
        self.modelisation = val.latin1()
   
    def setMateriau_e(self, val):
        """
        fixe la valeur du module d'Young choisi
        """
        self.materiau_e = val
    
    def setMateriau_nu(self, val):
        """
        fixe la valeur du coefficient de Poisson choisi
        """
        self.materiau_nu = val
    
    def setChargements(self, table):
        """
        crée la liste des pressions choisies
        un item de la liste est composé du nom de la sous-géométrie choisie et de la pression à appliquer
        """
        self.chargements = []
        for ligne in range(table.numRows()):
            # création d'un item
            liste = []
            cmb = table.cellWidget(ligne, 0)
            liste.append(cmb.currentText().latin1())
            liste.append(table.cellWidget(ligne, 1).text().latin1())
            # ajout de l'item dans la liste
            self.chargements.append(liste)
    
    def setDdls(self, table):
        """
        crée la liste des ddls choisies
        un item de la liste est composé du nom de la sous-géométrie choisie, de l'axe de liberté et de sa valeur
        """
        self.ddls = []
        for ligne in range(table.numRows()):
            for i in range(1, 4):
                # création d'un item
                liste = []
                cmb = table.cellWidget(ligne, 0)
                liste.append(cmb.currentText().latin1())
                th = table.horizontalHeader()
                liste.append(th.label(i).latin1())
                liste.append(table.cellWidget(ligne, i).text().latin1())
                # ajout de l'item dans la liste
                self.ddls.append(liste)
    
    def setGeometrie(self, val):
        """
        fixe le nom de la géométrie sélectionnée dans l'arbre d'étude
        """
        self.geometrie = val
    
    def setSousGeometrie(self, liste):
        """
        crée la liste des sous-géométries de la géométrie sélectionnée
        """
        self.sousGeometrie = []
        for val in liste:
            if val != '':
                self.sousGeometrie.append(val)
    
    def affiche(self):
        """
        affiche les différentes valeurs de l'étude
        (simple fonction d'aide)
        """
        print "***********************"
        print "***** ETUDE ***********"
        print "***********************"
        print "modélisation       = " + str(self.modelisation)
        print "module d'Young     = " + str(self.materiau_e)
        print "coeff. de Poisson  = " + str(self.materiau_nu)
        print "géométrie          = " + str(self.geometrie)
        print "sous géométries    = " + str(self.sousGeometrie)
        print "chargements        = " + str(self.chargements)
        print "degrés de libertés = " + str(self.ddls)
