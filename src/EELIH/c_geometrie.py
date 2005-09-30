# -*- coding: iso-8859-1 -*-

# module salome
import salome
# module eficas
import SMESH_utils
# module GEOM
import GEOM
# module de bases
import string
# module pour le maillage
import maillage

class C_geometrie:
    """
    controleur de la classe Geometrie, permet la sélection de la géométrie dans l'arbre d'étude
    de Salome. Met à jour les champs correspondants (sous-géométries, ...)
    - geometrie = référence sur le panneau géométrie
    - dicoSousGeom = clé = IORString
                     valeur = name
    """
    def __init__(self, appli, geometrie):
        self.appli = appli
        self.geometrie = geometrie
	self.dicoSousGeom = []
	
    def getGeometrie(self):
        """
        affecte le nom de la géométrie sélectionnée dans l'arbre d'étude de Salome
        à l'instance étude de l'application et au lineedit correspondant
        """
        # récupération de tous les objets sélectionnés dans l'arbre d'étude
        listeSelection = salome.sg.getAllSelected()
        if len(listeSelection) > 1:
            print "----------------------------------------"
            print "1 seule géométrie doit être sélectionnée"
	elif len(listeSelection)  == 0:
	    print "----------------------------------------"
	    print "Sélectionnez une géométrie"
        else:
            # on teste si l'objet sélectionné est une géométrie et s'il possède des fils
            import EFICASGUI
	    import salomedsgui
	    anObject=SMESH_utils.entryToIor(salome.myStudy,listeSelection[0])
            if not anObject: # l'objet n'a pas encore chargé
               strContainer, strComponentName = "FactoryServer", "GEOM"
               myComponent = salome.lcc.FindOrLoadComponent( strContainer, strComponentName )
               SCom=salome.myStudy.FindComponent( strComponentName )
               myBuilder = salome.myStudy.NewBuilder()
               myBuilder.LoadWith( SCom , myComponent  )
               anObject=SMESH_utils.entryToIor(salome.myStudy,listeSelection[0])
            type = None
	    try:
	       type = anObject._narrow(GEOM.GEOM_Object)
	    except:
               pass
	       
	    # le type doit être une géométrie
	    if type == None:
	       print "----------------------------------------"
	       print "Sélectionnez une géométrie"
	    # type = géométrie
	    else:
	      # on vérifie que cette géométrie possède au moins un fils qui soit une géoméotrie 
              geom = salome.lcc.FindOrLoadComponent( "FactoryServer", "GEOM" )
	      group = geom.GetIMeasureOperations(EFICASGUI.currentStudyId)
	      nom = SMESH_utils.entryToName(salome.myStudy, listeSelection)
	      
              # modelisation 3D --> il faut un SOLID
              if self.appli.etude.modelisation == '3D':
	         n = string.find(group.WhatIs(type), 'SOLID')
		 if group.WhatIs(type)[n+8] != 0:
		    liste = []
		    liste = [nom[0], listeSelection[0]]
		    self.geometrie.ln.setText(nom[0])
		    self.appli.etude.setGeometrie(liste)
		    # groupes de mailles = face ou shell
		    self.dicoSousGeom = SMESH_utils.getSubGeometryIorAndName(salome.myStudy, self.appli.etude.geometrie)
		    listeSousGeom = []
		    for maille in self.dicoSousGeom.keys():
		       anObject = SMESH_utils.iorStringToIor(maille)
		       type = anObject._narrow(GEOM.GEOM_Object)
		       n = string.find(group.WhatIs(type), 'FACE')
		       if group.WhatIs(type)[n+7] != 0:
                          listeSousGeom.append(self.dicoSousGeom[maille])
		       else:
		          n = string.find(group.WhatIs(type), 'SHELL')
			  if group.WhatIs(type)[n+8] != 0:
			     listeSousGeom.append(self.dicoSousGeom[maille])
		    
		    listeSousGeom.sort()
		    self.appli.etude.setSousGeometrie(listeSousGeom)
		    
		 else:
		    print "----------------------------------------"
		    print "Pour une modélisation 3D, la géométrie sélectionnée doit être un solide."
	      
	      # modelisation 2D --> SHELL ou FACE
              if string.find(self.appli.etude.modelisation, '2D') != -1:
	         liste = []
                 liste = [nom[0], listeSelection[0]]
                 self.geometrie.ln.setText(nom[0])
                 self.appli.etude.setGeometrie(liste)
		 self.dicoSousGeom = SMESH_utils.getSubGeometryIorAndName(salome.myStudy, self.appli.etude.geometrie)
		 listeSousGeom = []
		 n = string.find(group.WhatIs(type), 'SHELL')
		 if group.WhatIs(type)[n+8] != 0:
		    # groupes de mailles = edge
		    for maille in self.dicoSousGeom.keys():
		       anObject = SMESH_utils.iorStringToIor(maille)
		       type = anObject._narrow(GEOM.GEOM_Object)
		       n = string.find(group.WhatIs(type), 'EDGE')
		       if group.WhatIs(type)[n+7] != 0:
                          listeSousGeom.append(self.dicoSousGeom[maille])
		 else:
		    n = string.find(group.WhatIs(type), 'FACE')
		    if group.WhatIs(type)[n+7] != 0:
		       # groupes de mailles = edge
		       for maille in self.dicoSousGeom.keys():
		          anObject = SMESH_utils.iorStringToIor(maille)
		          type = anObject._narrow(GEOM.GEOM_Object)
		          n = string.find(group.WhatIs(type), 'EDGE')
		          if group.WhatIs(type)[n+7] != 0:
                             listeSousGeom.append(self.dicoSousGeom[maille])
	          
		 listeSousGeom.sort()   
		 self.appli.etude.setSousGeometrie(listeSousGeom)

              # on cree le bon nombre de panneaux maillages : autant qu'il y a de sous geometries
	      #self.createMeshPanel()
	      #print "-----------------------------"
	      #print "-----------------------------"
	      #print "-----------------------------"
	      #print "-----------------------------"
	      #print "-----------------------------"
	      #print "-----------------------------"
	      #print "-----------------------------"
	      #print "liste des panneaux ="
	      #print self.appli.mw.listePanels

#    def createMeshPanel(self):
#       """
#       cree autant de panneaux maillages que de sous geometries
#       """
#       self.listeMaillages = []
#       for i in self.appli.etude.sousGeometrie:
#          mesh = maillage.Maillage(self.appli.mw.ws, self.appli)
#	  self.listeMaillages.append(mesh)
#          self.appli.mw.listePanels.append(mesh)
#	  #self.appli.mw.listePanels.insert(0, self.appli.mw.listePanels[0] + 1)
#          #del self.appli.mw.listePanels[1]
	  
#	  self.updateGeomMaillage(mesh, i)

    def getSousGeometrie(self):
        """
        retourne les sous-géométries de la géométrie sélectionnée dans l'arbre d'étude de Salome
        """
        liste = SMESH_utils.getSubGeometry(salome.myStudy, self.geometrie.appli.etude.geometrie)
	liste.sort()
        return liste
    
    def updateComboSousGeom(self):
        """
        affecte les combobox des tables des panneaux ddl et pression avec les valeurs
        des sous-géométries
        """
        # insertion pour le panneau ddl
        for cmb in self.geometrie.appli.mw.ddl.controleurNouvelleLigneTable.controleurTable.listeComboGeom:
            cmb.insertStrList(self.geometrie.appli.etude.sousGeometrie)
        
        # insertion pour le panneau pression
        for cmb in self.geometrie.appli.mw.pression.controleurNouvelleLigneTable.controleurTable.listeComboGeom:
            cmb.insertStrList(self.geometrie.appli.etude.sousGeometrie)
    
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
	for iorSousGeom in self.dicoSousGeom.keys():
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
	
	
	# liste des faces sélectionnées dans ddl et pression
#	liste_faces = []
#	for face in self.appli.etude.ddls:
#	   if face[0] not in liste_faces:
#	      liste_faces.append(face[0])

#	for face in self.appli.etude.chargements:
#	   if face[0] not in liste_faces:
#	      liste_faces.append(face[0])
#        if liste_faces != '':
        liste_faces = []
	#liste_faces.append('0:1:2:1:1')
	#liste_faces.append('0:1:2:1:2')
        
	# récupération de toutes les sous géométries
	for sousGeom in self.appli.etude.sousGeometrie:
           SO = salome.myStudy.FindObject(str(sousGeom))
	   liste_faces.append(SO.GetID())
	
        touteslesvaleurs = self.convertit_entrees_en_valeurs(liste_faces)
	#liste_faces = []
	#liste_faces.append('0:1:2:1:2')
	#touteslesvaleurs = self.convertit_entrees_en_valeurs(liste_faces)
        return touteslesvaleurs
    
dict_geom_numgroupe = { }
dict_geom_numface = { }
