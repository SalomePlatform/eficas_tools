# -*- coding: utf-8 -*-

from panelbase import *
 

class C_maillage:
    """
    controleur de la classe Maillage, traite les maillages correspondants à la géométrie
    sélectionnée ou crée un maillage avec le nom saisi
    - maillage = référence sur le panneau maillage
    """
    def __init__(self, maillage):
        self.maillage = maillage
    
    def traiteMaillage(self):
        """
        si un maillage est sélectionné dans la listbox traite ce maillage
        sinon crée un nouveau maillage avec comme nom le nom saisi
        """
        # nouveau maillage
        if self.maillage.lbMaillage.currentItem() == -1:
            self.maillage.cl.traiteNewMaillage(0, str(self.maillage.lblGeom2.text()), str(self.maillage.lnNouveauMaillage.text()))
            self.maillage.cl.traiteCL()
	    # met � jour les autres listbox des autres maillages -> ajoute le maillage cree
	    self.updateMeshList()
		    
        # sélection d'un maillage existant
        else:
            self.maillage.cl.traiteMaillage(0, str(self.maillage.lbMaillage.currentText().latin1()))
            self.maillage.cl.traiteCL()
       
        print "traitemaillage -------------------------"

    def enableBtnSuivant(self):
        """
        rend actif le bouton suivant (terminer) si un maillage a été sélectionné ou
        si un nom de nouveau maillage a été saisi
        """
        # nouveau maillage
        if self.maillage.lblNouveauMaillage.isEnabled():
            if self.maillage.lblNouveauMaillage.text().latin1() != str(''):
                self.maillage.btnSuivant.setEnabled(1)
            else:
                self.maillage.btnSuivant.setEnabled(0)
        # sélection d'un maillage existant
        elif self.maillage.lbMaillage.currentItem() != -1:
            self.maillage.btnSuivant.setEnabled(1)
        else:
            self.maillage.btnSuivant.setEnabled(0)
    
    def close(self):
        """
        ferme l'application quand on clique sur le bouton suivant (terminer)
        """
        self.maillage.appli.mw.close()

    def updateMeshList(self):
       """
       met � jour la liste des maillages dans tous les panneaux maillages
       quand un nouveau maillage est cree
       """
       for maillage in self.maillage.appli.mw.publication.listeMaillages:
          try:
             maillage.cl.get_geoms()
             maillage.cl.get_maillages()
        
             maillage.cl.MainShapes(0)
       
             listeMaillage = maillage.cl.Possibles(0, str(self.maillage.appli.etude.geometrie[0]))

	     maillage.lbMaillage.insertStrList(listeMaillage)
          except:
	     pass


       
