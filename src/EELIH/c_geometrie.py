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
