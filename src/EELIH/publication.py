# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *
# module de gestion des panneaux
from panelbase import *
# modules de création du fichier de commande
from fichier import *
# modules de base
import commands

import salome
import SMESH_utils
import maillage

class Publication(PanelBase):
    """
    Hérite de la classe mère PanelBase
    Définit le panneau pour publier le fichier de commandes dans l'arbre d'études de Salome :
    """
    def __init__(self, parent, appli, salomeRef):
        # hérite de la classe mère des panneaux
        PanelBase.__init__(self, parent, appli)
        
        # initialisation pour la publication dans l'arbre d'étude
	self.salome = salomeRef
	
        # on modifie le label titre
        self.lblTitre.setText('Lancement du calcul')
        
        # on modifie l'explication
        self.lblExplication.setText("Etes-vous sûr de souhaiter lancer le calcul ?")
        
        # espacement
        self.sp2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gl.addItem(self.sp2, 3, 0)
        
        # changement du bouton suivant
        self.btnSuivant.setText("Lancer le calcul")
        self.btnSuivant.setMaximumWidth(150)
        
        # bouton suivant toujours actif
        self.btnSuivant.setEnabled(1)
    
    def suivant(self):
        """
        affiche le panneau suivant
        crée le fichier de commandes associé aux valeurs saisies
        """
        # création des groupes de mailles
        self.add_selection()
	
	# panneau suivant
        PanelBase.suivant(self)
        
        # remplissage du fichier
        fichier = Fichier(self.appli, self.salome)
        fichier.creer()

    def convertit_group_maille_from_salome(self,liste_in):
        """
        convertit les groupes de maille
        """
        newr=[]
        if [ 1 == 1 ]:
            for entree in liste_in :
                travail=[]
                travail.append(entree)
                if dict_geom_numgroupe.has_key(entree):
                    r=dict_geom_numgroupe[entree]
                else:
                    r=SMESH_utils.getAsterGroupMa(salome.myStudy,travail)
                    dict_geom_numgroupe[entree]=r
                for i in r :
                    newr.append(i)
        else :
            print "pas de groupe de maille associé"
            showerror("Pas de groupe associé","Cet Objet ne peut pas être défini comme un ensemble de groupe de maille")
        return newr

    def convertit_entrees_en_valeurs(self,liste_faces):
        """
        convertit les entry de l'arbre d'étude en valeur
        """
        valeur=self.convertit_group_maille_from_salome(liste_faces)
        if valeur == []:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "Pb pas de fonction de conversion de la valeur Salome en valeur Aster"
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "VALEUR", valeur
        if len(valeur) == 1:
            valeur = "'" + str(valeur[0]) + "'"
        return valeur
   
    def add_selection(self):
        """
        retourne le nom des objets sélectionnés dans l'arbre d'étude
        """
        entrychaine=salome.sg.getAllSelected()
	if len(entrychaine) >= 1:
	   print "1 seule géométrie doit être sélectionnée"
	
        liste_faces = []
        
        # récupération des sous géométries sélectionnées
	liste_select = []
	for sousGeomDdl in self.appli.etude.ddls:
	   if sousGeomDdl[0] not in liste_select:
	      liste_select.append(sousGeomDdl[0])
	for sousGeomPression in self.appli.etude.chargements:
	   if sousGeomPression[0] not in liste_select:
	      liste_select.append(sousGeomPression[0])
       
	# transformation des sous geometries en entry
	for sousGeom in liste_select:
           SO = salome.myStudy.FindObject(str(sousGeom))
	   liste_faces.append(SO.GetID())

        print "----------------------------------> ", liste_faces
	self.createMeshPanel(liste_select)

        touteslesvaleurs = self.convertit_entrees_en_valeurs(liste_faces)

        return touteslesvaleurs

    def createMeshPanel(self, listeSousGeomName):
       """
       cree autant de panneaux maillages que de sous geometries
       """
       self.listeMaillages = []
       for i in listeSousGeomName:
          mesh = maillage.Maillage(self.appli.mw.ws, self.appli)
	  self.listeMaillages.append(mesh)
          self.appli.mw.listePanels.append(mesh)
	  #self.appli.mw.listePanels.insert(0, self.appli.mw.listePanels[0] + 1)
          #del self.appli.mw.listePanels[1]
	  
	  self.updateGeomMaillage(mesh, i)

    def updateGeomMaillage(self, maillage, sousGeom):
        """
        affecte le label indiquant la géométrie sélectionnée du panneau maillage
        affecte la listbox du panneau maillage avec les valeurs des maillages trouvés dans l'arbre d'étude
        Salome correspondant à la géométrie sélectionnée
        """
        # affectation de la géométrie sélectionnée au label du panneau maillage
        maillage.lblGeom2.setText(str(self.appli.etude.geometrie[0]))
        
        # affectation de la sous géométrie au label du panneau maillage
	maillage.lblSousGeom2.setText(str(sousGeom))
	
        # récupération des mailles correspondants
        import eelihCL
	maillage.cl=eelihCL.CLinit()
	# récupération de l'IOR des sous géométries
	GEOMIor = []
	for iorSousGeom in self.appli.mw.geometrie.controleurGeom.dicoSousGeom.keys():
	   GEOMIor.append(iorSousGeom)
           maillage.cl.GetOrCreateCL(iorSousGeom)
           #self.appli.mw.maillage.cl.traiteCL()
	maillage.cl.get_geoms()
	maillage.cl.get_maillages()
#        
        maillage.cl.MainShapes(0)
#       
        listeMaillage = maillage.cl.Possibles(0, str(self.appli.etude.geometrie[0]))
        # insertion des maillages trouvés dans la listbox du panneau maillage
        # si aucun maillage on disable la listbox
        # sinon on disable le lineedit pour donner le nom d'un nouveau maillage
        if listeMaillage != []:
            maillage.lbMaillage.insertStrList(listeMaillage)
            #maillage.lbMaillage.setEnabled(1)
            #maillage.lblMaillage.setEnabled(1)
            #maillage.lblNouveauMaillage.setEnabled(0)
            #maillage.lnNouveauMaillage.setEnabled(0)
        #else:
            #maillage.lnNouveauMaillage.setEnabled(1)
            #maillage.lblNouveauMaillage.setEnabled(1)
            #maillage.lbMaillage.setEnabled(0)
            #maillage.lblMaillage.setEnabled(0)
 


dict_geom_numgroupe = { }
dict_geom_numface = { }
