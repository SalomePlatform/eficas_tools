# -*- coding: utf-8 -*-

from pal.logger import ExtLogger
logger=ExtLogger( "EFICAS_SRC.EFICASGUI.eficasSalome.py" )

# -----------------------------------------------------------------------------
import sys, os, re,types



"""
# Remplacement de la fonction exit standard par une fonction
# qui n'interrompt pas l'execution

sys._exit=sys.exit

def exit(ier):
   print "appel de exit: ",ier


# Fin remplacement
"""


import eficasConfig

# lignes de path ajoutees pour acceder aux packages python du
# logiciel Eficas. Le package Aster est ajoute explicitement pour
# acceder au module prefs.py. A
sys.path[:0]=[eficasConfig.eficasPath,
              os.path.join( eficasConfig.eficasPath,'Editeur'),
              os.path.join( eficasConfig.eficasPath,'UiQT4'),
              eficasConfig.eficasPath,
             ]

print sys.path



# mode de lancement Eficas
ASTER  = "ASTER"
HOMARD = "HOMARD"
OPENTURNS = "OPENTURNS"
SEP = "SEP"


import Editeur    
from InterfaceQT4 import qtEficas

import salome
import visuDriver
import SalomePyQt


from pal.studyedit import StudyEditor
monEditor=StudyEditor()

# message utilisateur
msgWarning                 = "Attention"
msgMainShapeSelection      = "On travaille sur la geometrie principale : "
msgSubShapeBadMainShape    = "La selection geometrique SALOME ne correspond pas a une sous-geometrie de la geometrie principale : "
msgMeshGroupBadMainShape   = "Le groupe de maillage selectionne dans SALOME ne reference pas la bonne geometrie principale : "
msgIncompleteSelection     = "Tous les elements de la selection SALOME n'ont pu etre ajoutee"
msgUnAuthorizedSelecion    = "Selection SALOME non authorise. Autorise : sous-geometrie, groupe de maille"
msgErrorAddJdcInSalome     = "Erreur dans l'export du fichier de commande dans l'arbre d'etude Salome"
msgErrorDisplayShape       = "Erreur dans l'affichage de la forme geometrique selectionnee"
msgErrorDisplayMeshGroup   = "Erreur dans l'affichage du groupe de maillage selectionne"
msgErrorNeedSubShape       = "Selection d'un element sous geometrique seulement"


msgErrorGroupMaSelection    = "Selection GROUP_MA ne peut pas prendre un point ou un noeud"
msgWarningGroupNoSelection  = "Attention, GROUP_NO devrait prendre un point ou un noeud"



# couleur pour visualisation des geometries 

import colors
COLORS = ( colors.RED, 
         colors.GREEN,
         colors.BLUE,
         colors.SANDY,
         colors.ORANGE,
         colors.PURPLE,
         colors.DARK_RED,
         colors.DARK_GREEN,
         colors.DARK_BLUE,
         colors.YELLOW,
         colors.PINK,
         colors.CYAN )

LEN_COLORS = len( COLORS )


class MyEficas( qtEficas.Appli ):
    """
    Classe de lancement du logiciel EFICAS dans SALOME.
    Cette classe specialise le logiciel Eficas par l'ajout de:        
    a)la creation de groupes de mailles dans le composant SMESH de SALOME
    b)la visualisation d'elements geometrique dans le coposant GEOM de SALOME par selection dans EFICAS
    """
    def __init__( self, parent, code = "ASTER", fichier = None, module = "Eficas", version=None):
        """
        Constructeur.
        @type   parent: 
        @param  parent: widget Qt parent
        @type   code: string
        @param  code: catalogue a lancer ( ASTER, HOMARD OPENTURNS ). optionnel ( defaut = ASTER ).
        @type   fichier: string
        @param  fichier: chemin absolu du fichier eficas a ouvrir a das le lancement. optionnel
        """

        pathCode=code[0]+code[1:].lower()
        sys.path[:0]=[os.path.join(eficasConfig.eficasPath,pathCode)]
        
        if Editeur.__dict__.has_key( 'session' ):
            from Editeur import session
            eficasArg = []
            eficasArg += sys.argv            
            if fichier:
                eficasArg += [ fichier ]
            if version:
                eficasArg += [ "-c", version ]
            else :
                print "noversion"
            session.parse( eficasArg )
                        
        qtEficas.Appli.__init__( self,code=code,salome=1,parent=parent)
        
        #--------------- specialisation EFICAS dans SALOME  -------------------                
        self.parent = parent        
        self.salome = True      #active les parties de code specifique dans Salome( pour le logiciel Eficas )
        self.module = module    #indique sous quel module dans l'arbre d'etude ajouter le JDC.
        
        
        # donnee pour la creation de groupe de maille
        self.mainShapeNames   = {} #dictionnaire pour gerer les multiples fichiers possibles ouverts par 
        self.mainShapeEntries = {} #eficas ( cle = identifiant du JDC ), une mainshape par fichier ouvert.    
        self.subShapes        = {} #dictionnaire des sous-geometrie de la geometrie principale ( cle = entry, valeur = name ) 
        #----------------------------------------------------------------------    
        
        # visualisation groupes de mailles
        self.workingMesh = {} #dictionnaire cle = identifiant JDC / valeur = entry Mesh
        #----------------------------------------------------------------------        
        
        self.icolor = 0  # compteur pour memoriser la couleur courante
        self.show()
        
        
    def closeEvent(self,event):
        import InterfaceQT4.readercata
        if hasattr(InterfaceQT4.readercata,'reader') :
           del InterfaceQT4.readercata.reader
        global appli
        appli = None
        event.accept()
     
        
                        
    def __selectWorkingMesh( self, meshGroupEntries ):
        """
        Selection interactive du maillage sur lequel on travail
        """
        selMeshEntry, keep = None, False
        diag = SelectMeshDiagImpl( meshGroupEntries, self.parent  )
    
        if diag.exec_loop() == qt.QDialog.Accepted:
            selMeshEntry, keep = diag.getUserSelection()
        return selMeshEntry, keep    
            


    def __selectMainShape( self, groupeMaNamesIn, groupeNoNamesIn, editor ):
        """
        Selection interactive de la main shape
        """
        groupeMaNamesOut, groupeNoNamesOut = [], []
        selectedMainShape  =  None
        mainShapes = {}
        mainShapeEntries = []

        # liste des main shape possibles
        for groups in ( groupeMaNamesIn, groupeNoNamesIn ):
            for subShapeName in groups:
                entries = getEntriesFromName(self, "GEOM", subShapeName )
           
                for entry in entries:
                    mainShapeEntry = self.getMainShapeEntry( entry )
                    if mainShapeEntry != entry:
                        if mainShapes.has_key(subShapeName):
                            mainShapes[ subShapeName ].append( mainShapeEntry )
                        else:
                            mainShapes[ subShapeName ] = [ mainShapeEntry ]
                        if not mainShapeEntry in mainShapeEntries:
                            mainShapeEntries += [ mainShapeEntry ]
        
        if mainShapes:
            if len(mainShapeEntries)>1:
                diag = SelectMainShapeDiagImpl( mainShapeEntries, self.parent  )
        
                if diag.exec_loop() == qt.QDialog.Accepted:
                    selectedMainShape = diag.getUserSelection()                
                    print 'main shape user selection ->',selectedMainShape

            else:
                selectedMainShape = mainShapeEntries[0]
            
            self.mainShapeEntries[ editor ] = selectedMainShape
                    
            # filtre sur la main shape selectionnee
            for name in groupeMaNamesIn:
                try:
                    if selectedMainShape in mainShapes[ name ] :
                        groupeMaNamesOut += [ name ]
                except:
                    pass
            
            for name in groupeNoNamesIn:
                try:
                    if selectedMainShape in mainShapes[ name ] :
                        groupeNoNamesOut += [ name ]
                except:
                    pass
                        
        return groupeMaNamesOut, groupeNoNamesOut




    def __selectShape( self, editor, selectedEntry, kwType = None ):
        """
        selection sous-geometrie dans Salome:
        -test1) si c'est un element sous-geometrique .
        -test2) si appartient a la geometrie principale.
        
        met a jours la liste self.subShapes si test ok
        """        
        name, msgError = '',''
        
        selectedMainShapeEntry = self.getMainShapeEntry( selectedEntry )
        if selectedMainShapeEntry and selectedMainShapeEntry != selectedEntry: #ok test1)
            
            #PNPNPNPN a Revoir
            tgeo=self.getShapeType(  selectedEntry )
            if kwType == "GROUP_NO" and tGeo != "VERTEX":                
                msgError = msgWarningGroupNoSelection
            elif kwType == "GROUP_MA" and tGeo == "VERTEX":
                name, msgError = '', msgErrorGroupMaSelection                
                return name, msgError            
                            
            if not self.mainShapeEntries.has_key( editor ):
                self.mainShapeEntries[ editor ] = selectedMainShapeEntry
                mySO=monEditor.study.FindObjectID(selectedMainShapeEntry )
                if  mySO:
                    name = mySO.GetName()
                msgError = msgMainShapeSelection + name
            if selectedMainShapeEntry == self.mainShapeEntries[ editor ]:
                mySO=monEditor.study.FindObjectID(selectedMainShapeEntry )
                if  mySO:
                    name = mySO.GetName()
                self.subShapes[ selectedEntry ] = name                
            else:                
                if not self.mainShapeNames.has_key( editor ):
                    mySO=monEditor.study.FindObjectID(self.mainShapeEntries[ editor ])
                    if  mySO:
                        self.mainShapeNames[ editor ] = mySO.GetName()
                msgError = msgSubShapeBadMainShape + self.mainShapeNames[ editor ]                
        else:
            name, msgError = '', msgErrorNeedSubShape

        return name, msgError 
        
        
        
    def __selectMeshGroup( self, editor, selectedEntry, kwType = None ):
        """
        selection groupe de maille dans Salome:
        -test 1) si c'est un groupe de maille 
        -test 2) si le maillage fait reference a la geometrie principale 
        """        
        name, msgError = '',''                
                
        mySO=monEditor.study.FindObjectID(selectedEntry )
        from pal.smeshstudytools import SMeshStudyTools
        monSMeshStudyTools=SMeshStudyTools(monEditor)
        selectedMeshEntry = monSMeshStudyTools.getMeshFromGroup(mySO)

                
        if selectedMeshEntry: # ok test 1)            
            tGroup = ""
            mySO = self._myStudy.FindObjectID(selectedEntry)
            if mySO:
                groupObject = mySO.GetObject()
                if not groupObject:
                    mycomponent = salome.lcc.FindOrLoadComponent("FactoryServer", "SMESH")
                    SCom        = monEditor.study.FindComponent( "SMESH" )
                    monEditor.builder.LoadWith( SCom , myComponent  )
                    groupObject      = mySO.GetObject()
            if not groupObject :
               logger.debug("selectedMeshEntry: An error occurs")
               
            
            import SMESH
            aGroup = groupObject._narrow( SMESH.SMESH_GroupBase )
            if aGroup: tGroup = aGroup.GetType()

            #PNPNPNPN bizarre
            if kwType == "GROUP_NO" and tGroup != SMESH.NODE:                
                msgError = msgWarningGroupNoSelection
            elif kwType == "GROUP_MA" and tGroup == SMESH.NODE:
                name, msgError = '', msgErrorGroupMaSelection                
                return name, msgError                        
                        
            mySO = self._myStudy.FindObjectID(selectedMeshEntry)
            if mySO:
                object = mySO.GetObject()
                if not object:
                    mycomponent = salome.lcc.FindOrLoadComponent("FactoryServer", "SMESH")
                    SCom        = monEditor.study.FindComponent( "SMESH" )
                    monEditor.builder.LoadWith( SCom , myComponent  )
                    object      = mySO.GetObject()
            if not object :
               logger.debug("selectedMainShapeEntry: An error occurs")

            mesh     = object._narrow( SMESH.SMESH_Mesh  )
            if mesh: #Ok, c'est bien un objet maillage
                shape = mesh.GetShapeToMesh()
                if shape:
                    ior = salome.orb.object_to_string( shape )
                    if ior:
                       sObject   = currentStudy.FindObjectIOR(  ior )
                       selectedMainShapeEntry = sObject.GetID()
                else:
                    selectedMainShapeEntry=0
                    logger.debug( 'SalomeStudy.getShapeFromMesh( meshEntry = %s ) ' %meshEntry )

            
            if selectedMainShapeEntry: #test 2)                
                if not self.mainShapeEntries.has_key( editor ):
                    self.mainShapeEntries[ editor ] = selectedMainShapeEntry
                    mySO=monEditor.study.FindObjectID(selectedMainShapeEntry )
                    if  mySO:
                        name = mySO.GetName()
                    msgError = msgMainShapeSelection + name                    
                if selectedMainShapeEntry == self.mainShapeEntries[ editor ]:
                    mySO=monEditor.study.FindObjectID(selectedEntry )
                    if  mySO:
                        name = mySO.GetName()
                else:                    
                    if not self.mainShapeNames.has_key( editor ):
                       mySO=monEditor.study.FindObjectID(self.mainShapeEntries[ editor ])
                       if  mySO:
                            self.mainShapeNames[ editor ] = mySO.GetName()
                    msgError = msgMeshGroupBadMainShape + self.mainShapeNames[ editor ]
            else:
                # on authorise quand meme les groupes de maillage ne faisant 
                # pas reference a une geometrie principale (dixit CS_CBO )
                mySO=monEditor.study.FindObjectID(selectedEntry )
                if  mySO:
                    name = mySO.GetName()
                                          
        return name, msgError
        
    
        
    def __getAllGroupeMa(self, item ):
        """
        Recupere tous les GROUPE_MA dans le JDC courant
        """
        groupMa = ()                
        try:
        #if 1 :
            itemName  = item.get_nom()
            if 'GROUP_MA' in itemName:
                itemValue = item.get_valeur()
                if type( itemValue ) == str:
                    groupMa += ( itemValue , )
                elif type( itemValue ) == tuple:
                    groupMa += itemValue                
		elif type( itemValue ) == list:
		    groupMa += tuple(itemValue)
	        elif type( itemValue ) == types.InstanceType and itemValue.has_key('GROUP_MA'):
                    # pour creer le groupe de mailles dans DEFI_GROUP> CREA_GROUP_MA> GROUP_MA
		    groupMa += ( itemValue['GROUP_MA'], )
                else :
                   # sert pour DEFI_GROUP_MA / UNION
                   mc=item.get_definition()
                   if  type( mc ) == types.InstanceType :
                       children = item._GetSubList()
                       for child in children:            
                           try :
                             if 'grma' in repr(child.get_definition().type[0]) :
                                 val=tuple(child.get_valeur())
                                 groupMa += val
                           except :
                               pass
            else:
                children = item._GetSubList()
                for child in children:            
                    groupMa +=  self.__getAllGroupeMa( child )
        except:
        #else :
	# traitement des MCLIST Pour CREA_GROUP_MA
            try:
                itemName  = item.get_nom()
                if 'GROUP_MA' in itemName:
	            children = item._GetSubList()
	            for child in children:
	                groupMa +=  self.__getAllGroupeMa( child )
            except:
	        pass
        return groupMa                
        
   
    def __getAllGroupeNo(self, item ):
        """
        Recupere tous les GROUPE_NO dans le JDC courant
        """
        groupNo = ()                
        try:
            itemName  = item.get_nom()            
            if 'GROUP_NO' in itemName:
                itemValue = item.get_valeur()                
                if type( itemValue ) == str:
                    groupNo += ( itemValue , )
                elif type( itemValue ) == tuple:
                    groupNo += itemValue
		elif type( itemValue ) == list:
		    groupNo += tuple(itemValue)
	        elif type( itemValue ) == types.InstanceType and itemValue.has_key('GROUP_NO'):
                    # pour creer le groupe de Noeuds dans DEFI_GROUP> CREA_GROUP_NO> GROUP_NO
		    groupNo += ( itemValue['GROUP_NO'], )
            else:
                children = item._GetSubList()
                for child in children:            
                    groupNo += self.__getAllGroupeNo( child )
        except:
	# traitement des MCLIST Pour CREA_GROUP_NO dans DEFI_GROUP
            try:
                itemName  = item.get_nom()
                if 'GROUP_NO' in itemName:
	            children = item._GetSubList()
	            for child in children:
	                groupNo +=  self.__getAllGroupeNo( child )
            except:
	        pass
        return groupNo

        
    # ___________________________ Methodes de l ex Pal __________________________________
    def getEntriesFromName(self, componentName, subShapeName ):
        entries = []
        try :
           listSO  = self._myStudy.FindObjectByName( objectName, componentName )
           for SObjet in listSO :
               entry = SObjet.GetID()
               entries.append( entry )
        except :
           logger.debug("getEntriesFromName: An error occurs")
           entries = None
        return entries

    def getMainShapeEntry(self,entry):
        result=None
        try:
           mainShapeEntry = entry.split(':')[:4]

           if len(mainShapeEntry) == 4:
                strMainShapeEntry = '%s:%s:%s:%s'%tuple(mainShapeEntry)
                if self.isMainShape(strMainShapeEntry):
                    result = strMainShapeEntry
        except:
            logger.debug( 'Erreur pour SalomeStudy.getMainShapeEntry( entry = %s ) ' %entry )
            result = None
        return result

    def isMainShape(self,entry):
        result = False
        try:
            anObject=None
            mySO=monEditor.study.FindObjectID(entry )
            if  mySO:
                anObject = mySO.GetObject()
                if not anObject :
                   strContainer, strComponentName = "FactoryServer", "GEOM"
                   myComponent = salome.lcc.FindOrLoadComponent( strContainer, strComponentName )
                   SCom        = monEditor.study.FindComponent( strComponentName )
                   monEditor.builder.LoadWith( SCom , myComponent  )
                   anObject = mySO.GetObject()

            shape    = anObject._narrow( GEOM.GEOM_Object )
            if shape.IsMainShape():
                result = True
        except:
            logger.debug( 'Errreur pour SalomeStudy.isMainShape( entry = %s ) ' %entry )
            result = False
        return result

        
    #-----------------------  LISTE DES NOUVEAUX CAS D'UTILISATIONS -----------    
    def selectGroupFromSalome( self, kwType = None, editor=None):
        """
        Selection d'element(s) d'une geometrie ( sub-shape ) ou d'element(s) de maillage ( groupe de maille) à partir de l'arbre salome
        retourne ( la liste des noms des groupes, message d'erreur )
        
        Note: Appele par EFICAS lorsqu'on clique sur le bouton ajouter à la liste du panel AFF_CHAR_MECA        
        """
        names, msg = [], ''
        try:            
            self.editor=editor
            atLeastOneStudy = monEditor.study
            if not atLeastOneStudy:
                return names, msg
            # recupere toutes les selections de l'utilsateur dans l'arbre Salome
            entries = salome.sg.getAllSelected()
            nbEntries = len( entries )
            #if nbEntries >= 1:
            #    for entry in entries:
            #        if studyManager.palStudy.isMeshGroup( entry ): #selection d'un groupe de maille
            #            name, msg = self.__selectMeshGroup( editor, entry, kwType )
            #        elif studyManager.palStudy.isShape( entry ): #selection d'une sous-geometrie
            #            name, msg = self.__selectShape( editor, entry, kwType )
            #        else:
            #            name, msg = '', msgUnAuthorizedSelecion
            #        if name:
            #            names.append( name )                    
                        
            if names and len( names ) < nbEntries:                        
                msg = msgIncompleteSelection
        except:            
            logger.debug("selectGroupFromSalome: An error occurs")
        return names, msg                
        
        
    def addJdcInSalome(  self, jdcPath ):
        """
        Ajoute le Jeu De Commande ASTER ou HOMARD dans l'arbre d'etude Salome dans la rubrique EFICAS
        """
        ok, msgError = False, msgErrorAddJdcInSalome
        #try:            
        if 1:
            atLeastOneStudy = monEditor.study
            if not atLeastOneStudy:
                return ok, msgError
                        
            fileType = { 'ASTER'    : "FICHIER_EFICAS_ASTER",
                         'SEP'      : "FICHIER_EFICAS_SEP",
                         'OPENTURNS': "FICHIER_EFICAS_OPENTURNS",
                         'OPENTURNS_STUDY': "FICHIER_EFICAS_OPENTURNS",
                         'OPENTURNS_WRAPPER': "FICHIER_EFICAS_OPENTURNS",
                        }
                        
            folderName = {  'ASTER'    :  'AsterFiles',
                            'SEP'       : 'OMFiles' ,
                            'OPENTURNS_STUDY': 'OpenturnsFiles',                                    
                            'OPENTURNS_WRAPPER': 'OpenturnsFiles'}                                    

            folderType = { 'ASTER':    "ASTER_FILE_FOLDER",
                           'SEP':      "SEP_FILE_FOLDER",
                           'OPENTURNS_STUDY':"OPENTURNS_FILE_FOLDER",
                           'OPENTURNS_WRAPPER': "OPENTURNS_FILE_FOLDER"}

                        
            moduleEntry = monEditor.findOrCreateComponent(self.module)
            itemName    = re.split("/",jdcPath)[-1]
            
            fatherEntry = monEditor.findOrCreateItem(
                                    moduleEntry,
                                    name = folderName[self.code],
                                    #icon = "ICON_COMM_FOLDER",
                                    fileType = folderType[self.code])
                                                                        
            commEntry = monEditor.findOrCreateItem( fatherEntry ,
                                           name = itemName,
                                           fileType = fileType[ self.code ],
                                           fileName = jdcPath,
                                           #icon    = "ICON_COMM_FILE",
                                           comment = str( jdcPath ))

            salome.sg.updateObjBrowser()

            print 'addJdcInSalome commEntry->', commEntry            
            if commEntry:
                ok, msgError = True, ''        
        #except:                    
        #    logger.debug(50*'=' Erreur au AddJDC)
        return ok, msgError        
        
                
                
    def displayMeshGroups(self, meshGroupName):
        """
        visualisation group de maille de nom meshGroupName dans salome
        """
        ok, msgError = False, ''
        try:
            sg = salome.ImportComponentGUI('SMESH')
            currentjdcID = self.editor.nb.getcurselection()
            meshGroupEntries = []
            selMeshEntry = None
            selMeshGroupEntry = None
            
            # liste des groupes de maille de nom meshGroupName
            listSO = monEditor.study.FindObjectByName(meshGroupName, "SMESH")
            print "liste des groupes de maille de nom %s: "%(meshGroupName), listSO
            
            if len(listSO)>0:
                for SObjet in listSO:
                    groupEntry = SObjet.GetID()                
                    meshGroupEntries += [groupEntry]                    
                
                if len(meshGroupEntries)>1:
                
                    # choix d'un maillage
                    if not self.workingMesh.has_key(currentjdcID): # aucun maillage de defini par defaut encore
                        #selMeshEntry = "0:1:3:5" #CS_pbruno todo : choix maillage + test si c un maillage
                        selMeshEntry, keep = self.__selectWorkingMesh(meshGroupEntries)
                        if keep:
                            self.workingMesh[currentjdcID] = selMeshEntry
                    else: # deja un de defini par defaut
                        selMeshEntry = self.workingMesh[currentjdcID]
                            
                    # le groupe de maille est il ds ce maillage?
                    lselMeshEntry = len(selMeshEntry)            
                    for groupEntry in meshGroupEntries:                
                        if selMeshEntry == groupEntry[0:lselMeshEntry]:
                            selMeshGroupEntry = groupEntry
                            break
    
                else:
                    selMeshGroupEntry = meshGroupEntries[0]
                    
                # on affiche le groupe ds la vue VTK
                if selMeshGroupEntry:
                    #CS_pbruno: marche QUE si le module SMESH est active
                    myComponent = salome.lcc.FindOrLoadComponent("FactoryServer", "SMESH")
                    SCom        = monEditor.study.FindComponent("SMESH")
                    monEditor.builder.LoadWith( SCom , myComponent  )                             
                    sg.CreateAndDisplayActor(selMeshGroupEntry)
                    salome.sg.Display(selMeshGroupEntry)
                    salome.sg.FitAll()                
                    ok = True                
        except:
            msgError = msgErrorDisplayMeshGroup
            logger.debug(50*'=')
        return ok, msgError

            
    def displayShape(  self, shapeName ):
        """
        visualisation geometrie de nom shapeName dans salome
        """
        ok, msgError = False, ''
        try:
            import VISU            
            import visu_gui
            currentViewType = None            
            m = visu_gui.myVisu.GetViewManager()
            v = m.GetCurrentView()
            if v:
                currentViewType = v.GetType()
            
            atLeastOneStudy = monEditor.study
            if not atLeastOneStudy:
                return ok, msgError            
                                     
            print 'displayShapestrGeomShape shapeName -> ', shapeName
            
            if currentViewType == VISU.TVIEW3D: # maillage
                print 'Vue courante = VTK : affichage groupe de maille'                
                ok, msgError = self.displayMeshGroups(shapeName)
            else: #geometrie
                print 'Vue courante = OCC : affichage element geometrique'
                current_color = COLORS[ self.icolor % LEN_COLORS ]                
                ##### PNPNPNPN dans visuPal
                #ok = studyManager.palStudy.displayShapeByName( shapeName, current_color )
                salome.sg.FitAll()
                self.icolor = self.icolor + 1             
                if not ok:
                    msgError = msgErrorDisplayShape
        except:            
            logger.debug(50*'=')
        return ok, msgError    
        
        
    def creeConfigTxt(self,fichier,dico):        
        """
           sauvegarde = asksaveasfilename(title="fichier config.txt",
                                     defaultextension='.txt',
                                     initialdir = fichier)
           f=open(sauvegarde,'w+')
           for unite in dico.keys():
                type=dico[unite][0]
                fic=dico[unite][1:]
                ligne="fort."+str(unite)+" "+type+" "+fic
                f.write(ligne)
           f.close()
           self.rangeInStudy(sauvegarde)
	   print "==============================="
        """
        pass #CS_pbruno a implementer
           
           
    def buildCabriGeom( self, name, **param ):
        """
        visualisation dans GEOM d'une geometrie CABRI
        """
        import cabri        
        qt.QApplication.setOverrideCursor( qt.QCursor.waitCursor )
        cabri.tetra( name, **param )
        qt.QApplication.restoreOverrideCursor()
        
        
        
#-------------------------------------------------------------------------------------------------------
#    Pilotage de la Visu des elements de structures
#


    def envoievisu(self,liste_commandes):
        import traceback
        try:
            atLeastOneStudy = monEditor.study
            if not atLeastOneStudy:
                return
            logger.debug(10*'#'+":envoievisu: creating a visuDriver instance")
            monDriver=visuDriver.visuDriver(studyManager.palStudy,liste_commandes)

            logger.debug(10*'#'+":envoievisu: analyse visu commandes using the visuDriver "+str(monDriver))
            monId = monDriver.analyse()
            logger.debug(10*'#'+":envoievisu: display the structural elements using PALGUI")
            PALGUI_API.displaySE(monId)
        except:
            traceback.print_exc()
            logger.debug(10*'#'+":pb dans envoievisu")


        
#-------------------------------------------------------------------------------------------------------        
#           Point d'entree lancement EFICAS
#
def runEficas( code="ASTER", fichier=None, module = "Eficas", version=None ):
    logger.debug(10*'#'+":runEficas: START")
    global appli    
    logger.debug(10*'#'+":runEficas: code="+str(code))
    logger.debug(10*'#'+":runEficas: fichier="+str(fichier))
    logger.debug(10*'#'+":runEficas: module="+str(module))
    logger.debug(10*'#'+":runEficas: version="+str(version))

    if not appli: #une seul instance possible!        
        appli = MyEficas( SalomePyQt.SalomePyQt().getDesktop(), code = code, fichier = fichier, module = module, version=version )
    logger.debug(10*'#'+":runEficas: END")

        
        
 
# pour compatibilitee           
def runHomard( code="HOMARD", fichier=None ):
    global appli    
    if not appli: #une seul instance possible!                        
        appli = MyEficas( SalomePyQt.SalomePyQt().getDesktop(), code = code, fichier = fichier )
        

        
        
"""        
def runAster(parent = SalomePyQt.SalomePyQt().getDesktop(),  code="ASTER", fichier=None ) :
    global appli    
    if not appli: #une seul instance possible!                        
        appli = MyEficas( parent,  code = code, fichier = fichier )
"""    

appli = None






