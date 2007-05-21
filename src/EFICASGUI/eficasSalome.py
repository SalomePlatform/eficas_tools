# -*- coding: utf-8 -*-

from Logger import ExtLogger

import qt
import notifqt
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

sys.path[:0]=[os.path.join( eficasConfig.eficasPath,'Aster'),
              os.path.join( eficasConfig.eficasPath,'Homard'),
              os.path.join( eficasConfig.eficasPath,'Editeur'),
              eficasConfig.eficasPath,
             ]


import Tkinter


# mode de lancement Eficas
ASTER  = "ASTER"
HOMARD = "HOMARD"


import Editeur    
from Editeur import eficas
from Editeur import splash

import salome
import meshGui
import visuDriver
import PALGUI_API
import studyManager

#from qxembed import QXEmbed

import SalomePyQt


from SelectMainShapeDiag_ui import SelectMainShapeDiag
from SelectMeshDiag_ui import SelectMeshDiag



# message utilisateur
msgWarning                 = "Attention"
msgMainShapeSelection      = "On travaille sur la géométrie principale : "
msgSubShapeBadMainShape    = "La sélection géométrique SALOME ne correspond pas à une sous-géométrie de la géométrie principale : "
msgMeshGroupBadMainShape   = "Le groupe de maillage sélectionné dans SALOME ne référence pas la bonne géométrie principale : "
msgIncompleteSelection     = "Tous les éléments de la sélection SALOME n'ont pu étre ajoutée"
msgUnAuthorizedSelecion    = "Sélection SALOME non authorisé. Autorisé : sous-géométrie, groupe de maille"
msgErrorAddJdcInSalome     = "Erreur dans l'export du fichier de commande dans l'arbre d'étude Salome"
msgErrorDisplayShape       = "Erreur dans l'affichage de la forme géométrique sélectionnée"
msgErrorDisplayMeshGroup   = "Erreur dans l'affichage du groupe de maillage sélectionné"
msgErrorNeedSubShape       = "Sélection d'un élément sous géométrique seulement"


msgErrorGroupMaSelection    = "Sélection GROUP_MA ne peut pas prendre un point ou un noeud"
msgWarningGroupNoSelection  = "Attention, GROUP_NO devrait prendre un point ou un noeud"




# couleur pour visualisation des géometrie CS_CBO
COLORS = ( studyManager.RED, 
         studyManager.GREEN,
         studyManager.BLUE,
         studyManager.SANDY,
         studyManager.ORANGE,
         studyManager.PURPLE,
         studyManager.DARK_RED,
         studyManager.DARK_GREEN,
         studyManager.DARK_BLUE,
         studyManager.YELLOW,
         studyManager.PINK,
         studyManager.CYAN )

LEN_COLORS = len( COLORS )




class SelectMainShapeDiagImpl( SelectMainShapeDiag ):
    def __init__( self, mainShapeEntries, parent = None,name = None,modal = 1,fl = 0 ):
        SelectMainShapeDiag.__init__( self,parent,name,modal,fl )
        
        self.mainShapes = {} # ( entry, value )
        for entry in mainShapeEntries:
            name = studyManager.palStudy.getName( entry )
            self.mainShapes[entry] = name
            
        self.lbMainShapes.clear()
        for entry,name in self.mainShapes.items():
            self.lbMainShapes.insertItem( name )
        self.lbMainShapes.setCurrentItem( 0 )

                                    
    def getUserSelection( self ):
        mainShapeEntry = None
        
        item = self.lbMainShapes.selectedItem()
        mainShapeName = str( item.text() )        
        
        for entry, name in self.mainShapes.items():
            if mainShapeName == name:
                mainShapeEntry = entry
                break                
            
        return mainShapeEntry 

        
class SelectMeshDiagImpl( SelectMeshDiag ):
    def __init__( self, meshGroupEntries, parent = None,name = None,modal = 1,fl = 0 ):
        SelectMeshDiag.__init__( self,parent,name,modal,fl )
        
        self.meshes = {} # ( entry, value )         
        
        for meshGroupEntry in meshGroupEntries:
            meshEntry = studyManager.palStudy.getMesh(meshGroupEntry)
            meshName  = studyManager.palStudy.getName(meshEntry)            
            self.meshes[meshEntry] = meshName 
                        
        self.lbMeshes.clear()
        for entry,name in self.meshes .items():
            self.lbMeshes.insertItem( name )
        self.lbMeshes.setCurrentItem( 0 )        
                                    
    def getUserSelection( self ):
        selMeshEntry, keep = None, False
        
        item = self.lbMeshes.selectedItem()
        meshName = str( item.text() )        
        for entry, name in self.meshes.items():
            if meshName == name:
                selMeshEntry = entry
                break
            
        keep = self.cbAgain.isChecked()
            
        return selMeshEntry, keep         




#class MyEficas( Tkinter.Toplevel, eficas.EFICAS, QXEmbed ):
class MyEficas( Tkinter.Toplevel, eficas.EFICAS ):
    """
    Classe de lancement du logiciel EFICAS dans SALOME.
    Cette classe spécialise le logiciel Eficas par l'ajout de:        
    a)la création de groupes de mailles dans le composant SMESH de SALOME
    b)la visualisation d'éléments géométrique dans le coposant GEOM de SALOME par sélection dans EFICAS
    """
    def __init__( self, parent, code = None, fichier = None, module = studyManager.SEficas ):
        """
        Constructeur.
                
        @type   parent: 
        @param  parent: widget Qt parent
                
        
        @type   code: string
        @param  code: catalogue à lancer ( ASTER, HOMARD ). optionnel ( défaut = ASTER ).
        
        @type   fichier: string
        @param  fichier: chemin absolu du fichier eficas à ouvrir à dès le lancement. optionnel
        """
        #QXEmbed.__init__( self, parent, "", qt.Qt.WDestructiveClose | qt.Qt.WStyle_Customize | qt.Qt.WStyle_StaysOnTop )        
        Tkinter.Toplevel.__init__( self )
                        
        if Editeur.__dict__.has_key( 'session' ):
            print 'CS_pbruno has_key session'
            from Editeur import session
            eficasArg = []
            eficasArg += sys.argv            
            if fichier:
                eficasArg += [ fichier ]
            session.parse( eficasArg )
                        
        
        #----------------------------  initialisation EFICAS  -----------------  
        splash.init_splash( self, code = code, titre = "Lancement d'EFICAS pour %s" %code )
        splash._splash.configure( text="Chargement d'EFICAS en cours.\n Veuillez patienter ..." )
        # différence eficas 1.7 et 1.8
        
               
        eficas.EFICAS.__init__( self, self, code = code )
        
        
        #----------------------------------------------------------------------
        
        
        """
        #------  embarcation dans une fenêtre qt pour mise au premier plan  ---
        #embedded = QXEmbed( parent, "", qt.Qt.WDestructiveClose | qt.Qt.WStyle_Customize | qt.Qt.WStyle_StaysOnTop )        
        embedded = QXEmbed( parent, "" )
        #embedded.initialize()        
        embedded.show()
        embedded.embedTk( self.winfo_id() )        
        size = embedded.sizeHint()
        print 'CS_pbruno size (%s, %s )'%( size.width(), size.height () )
        embedded.resize( size.width(), size.height () )
        embedded.setWFlags(  qt.Qt.WDestructiveClose | qt.Qt.WStyle_Customize | qt.Qt.WStyle_StaysOnTop )
        #----------------------------------------------------------------------
        """
        
        #--------------- spécialisation EFICAS dans SALOME  -------------------                
        self.parent = parent        
        self.salome = True      #active les parties de code spécifique dans Salome( pour le logiciel Eficas )
        self.module = module    #indique sous quel module dans l'arbre d'étude ajouter le JDC.
        
        
        # donnée pour la création de groupe de maille
        self.mainShapeNames   = {} #dictionnaire pour gérer les multiples fichiers possibles ouverts par 
        self.mainShapeEntries = {} #eficas ( clé = identifiant du JDC ), une mainshape par fichier ouvert.    
        self.subShapes        = {} #dictionnaire des sous-géométrie de la géométrie principale ( clé = entry, valeur = name ) 
        #----------------------------------------------------------------------    
        
        # visualisation groupes de mailles
        self.workingMesh = {} #dictionnaire clé = identifiant JDC / valeur = entry Mesh
        #----------------------------------------------------------------------        
        
        self.icolor = 0  # compteur pour mémoriser la couleur courante
        
        
    def quit(self): 
        global appli        
        appli = None
        self.destroy()

    def destroy(self):
        global appli
        appli = None
        Tkinter.Toplevel.destroy(self)
                    
    def __studySync( self ):
        """
        IMPORTANT( à appeler préalablement à chaque appel du gestionnaire d'étude ) : spécifique au lancement de Eficas dans Salome,
        permet au gestionnaire d'étude ( studyManager.palStudy ) de pointer sur la bonne étude.
        
        Un retour à False indique qu'il n'y a aucune étude active, dans ce cas ne faire aucune opération avec le gestionnaire d'étude( 
        gros plantage sinon )
        """                
        activeStudyId = salome.sg.getActiveStudyId()
        #print 50*'='
        #print 'activeStudyId->',activeStudyId
        #print 'salome.myStudyId->',salome.myStudyId
        #print 50*'='
        
        if activeStudyId == 0: # pas d'étude active
            return False
        
        if activeStudyId != salome.myStudyId:
            studyManager.palStudy.setCurrentStudyID( activeStudyId )            
            
        return True

        
    def __createOCCView( self ):
        """
        Création vue Occ
        """        
        #salome.salome_init()
        import iparameters

        # On détermine le nombre de GUI states déjà présents dans l'arbre d'étude
        GUIStateID = 1

        ipar = iparameters.IParameters(salome.myStudy.GetCommonParameters("Interface Applicative", GUIStateID))
        properties = ipar.getProperties()

        while properties != []:
            GUIStateID += 1
            ipar = iparameters.IParameters(salome.myStudy.GetCommonParameters("Interface Applicative", GUIStateID))
            properties = ipar.getProperties()
   
        print "GUIStateID: ", GUIStateID

        #Set up visual properties:
        ipar.setProperty("AP_ACTIVE_VIEW", "OCCViewer_0_0")
        ipar.setProperty("AP_WORKSTACK_INFO", "(splitter orientation=0 sizes=1045 (views active='OCCViewer_0_0' 'OCCViewer_0_0'))")
        ipar.setProperty("AP_SAVEPOINT_NAME", "GUI state: %i"%(GUIStateID))

        #Set up lists:
        # fill list AP_VIEWERS_LIST
        ipar.append("AP_VIEWERS_LIST", "OCCViewer_1")
        # fill list OCCViewer_1
        ipar.append("OCCViewer_1", "OCC scene:1 - viewer:1")
        ipar.append("OCCViewer_1", "1.000000000000e+00*0.000000000000e+00*0.000000000000e+00*5.773502588272e-01*-5.773502588272e-01*5.773502588272e-01*0.000000000000e+00*0.000000000000e+00*0.000000000000e+00*0.000000000000e+00*2.886751294136e+02*-2.886751294136e+02*2.886751294136e+02")

        if salome.sg.hasDesktop():
            salome.sg.updateObjBrowser(1)
            iparameters.getSession().restoreVisualState(GUIStateID)
        
                        
    def __selectWorkingMesh( self, meshGroupEntries ):
        """
        Sélection intéractive du maillage sur lequel on travail
        """
        selMeshEntry, keep = None, False
        diag = SelectMeshDiagImpl( meshGroupEntries, self.parent  )
    
        if diag.exec_loop() == qt.QDialog.Accepted:
            selMeshEntry, keep = diag.getUserSelection()
        return selMeshEntry, keep    
            


    def __selectMainShape( self, groupeMaNamesIn, groupeNoNamesIn, jdcID ):
        """
        Sélection intéractive de la main shape
        """
        groupeMaNamesOut, groupeNoNamesOut = [], []
        selectedMainShape  =  None
        mainShapes = {}
        mainShapeEntries = []

        # liste des main shape possibles
        for groups in ( groupeMaNamesIn, groupeNoNamesIn ):
            for subShapeName in groups:
                entries = studyManager.palStudy.getEntriesFromName( studyManager.SGeom, subShapeName )
                for entry in entries:
                    mainShapeEntry = studyManager.palStudy.getMainShapeEntry( entry )
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
            
            self.mainShapeEntries[ jdcID ] = selectedMainShape
                    
            # filtre sur la main shape sélectionnée
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




    def __selectShape( self, jdcID, selectedEntry, kwType = None ):
        """
        sélection sous-géométrie dans Salome:
        -test1) si c'est un élément sous-géométrique .
        -test2) si appartient à la géométrie principale.
        
        met à jours la liste self.subShapes si test ok
        """        
        name, msgError = '',''
        
        selectedMainShapeEntry = studyManager.palStudy.getMainShapeEntry( selectedEntry )
        
        if selectedMainShapeEntry and selectedMainShapeEntry != selectedEntry: #ok test1)
            
            tGeo = studyManager.palStudy.getRealShapeType( selectedEntry )
            if kwType == "GROUP_NO" and tGeo != studyManager.VERTEX:                
                msgError = msgWarningGroupNoSelection
            elif kwType == "GROUP_MA" and tGeo == studyManager.VERTEX:
                name, msgError = '', msgErrorGroupMaSelection                
                return name, msgError            
                            
            if not self.mainShapeEntries.has_key( jdcID ):
                self.mainShapeEntries[ jdcID ] = selectedMainShapeEntry
                name = studyManager.palStudy.getName( selectedMainShapeEntry )
                msgError = msgMainShapeSelection + name
            if selectedMainShapeEntry == self.mainShapeEntries[ jdcID ]:
                name = studyManager.palStudy.getName( selectedEntry )
                self.subShapes[ selectedEntry ] = name                
            else:                
                if not self.mainShapeNames.has_key( jdcID ):
                    self.mainShapeNames[ jdcID ] = studyManager.palStudy.getName( self.mainShapeEntries[ jdcID ] )
                msgError = msgSubShapeBadMainShape + self.mainShapeNames[ jdcID ]                
        else:
            name, msgError = '', msgErrorNeedSubShape

        return name, msgError 
        
        
        
    def __selectMeshGroup( self, jdcID, selectedEntry, kwType = None ):
        """
        sélection groupe de maille dans Salome:
        -test 1) si c'est un groupe de maille 
        -test 2) si le maillage fait référence à la géométrie principale 
        """        
        name, msgError = '',''                
                
        selectedMeshEntry = studyManager.palStudy.getMesh( selectedEntry )
                
        if selectedMeshEntry: # ok test 1)            
            tGroup = studyManager.palStudy.getGroupType( selectedEntry )
            if kwType == "GROUP_NO" and tGroup != studyManager.NodeGroups:                
                msgError = msgWarningGroupNoSelection
            elif kwType == "GROUP_MA" and tGroup == studyManager.NodeGroups:
                name, msgError = '', msgErrorGroupMaSelection                
                return name, msgError                        
                        
            selectedMainShapeEntry = studyManager.palStudy.getShapeFromMesh( selectedMeshEntry )
            
            if selectedMainShapeEntry: #test 2)                
                if not self.mainShapeEntries.has_key( jdcID ):
                    self.mainShapeEntries[ jdcID ] = selectedMainShapeEntry
                    name = studyManager.palStudy.getName( selectedMainShapeEntry )
                    msgError = msgMainShapeSelection + name                    
                if selectedMainShapeEntry == self.mainShapeEntries[ jdcID ]:
                    name = studyManager.palStudy.getName( selectedEntry  )  #ok test 2)
                else:                    
                    if not self.mainShapeNames.has_key( jdcID ):
                        self.mainShapeNames[ jdcID ] = studyManager.palStudy.getName(
                                                            self.mainShapeEntries[ jdcID ] )
                    msgError = msgMeshGroupBadMainShape + self.mainShapeNames[ jdcID ]
            else:
                # on authorise quand même les groupes de maillage ne faisant 
                # pas référence à une géométrie principale (dixit CS_CBO )
                name = studyManager.palStudy.getName( selectedEntry )
                                          
        return name, msgError
        
        
    
        
    def __updateSubShapes( self, jdcID, groupeNames ):
        """
        mise à jours de la liste self.subShapes à partir de la liste des noms de groupe fourni en entré
        """
        for name in groupeNames:
            entries = studyManager.palStudy.getEntriesFromName( studyManager.SGeom, name )            
            for entry in entries:
                if not self.subShapes.has_key( entry ):                    
                    ok, msgError = self.__selectShape( jdcID, entry ) # filtre
                    if ok:
                        self.subShapes[ entry ] = name                    
        
    def __getAllGroupeMa(self, item ):
        """
        Récupère tous les GROUPE_MA dans le JDC courant
        """
        groupMa = ()                
        try:
            itemName  = item.get_nom()
            if 'GROUP_MA' in itemName:
                #print 'CS_pbruno itemName',itemName             
                itemValue = item.get_valeur()
                if type( itemValue ) == str:
                    groupMa += ( itemValue , )
                elif type( itemValue ) == tuple:
                    groupMa += itemValue                
		elif type( itemValue ) == list:
		    groupMa += tuple(itemValue)
	        elif type( itemValue ) == types.InstanceType and itemValue.has_key('GROUP_MA'):
                    # pour créer le groupe de mailles dans DEFI_GROUP> CREA_GROUP_MA> GROUP_MA
		    groupMa += ( itemValue['GROUP_MA'], )
            else:
                children = item._GetSubList()
                for child in children:            
                    groupMa +=  self.__getAllGroupeMa( child )
        except:
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
        Récupère tous les GROUPE_NO dans le JDC courant
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
                    # pour créer le groupe de Noeuds dans DEFI_GROUP> CREA_GROUP_NO> GROUP_NO
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

        
    #-----------------------  LISTE DES NOUVEAUX CAS D'UTILISATIONS -----------    
    def selectGroupFromSalome( self, kwType = None):
        """
        Sélection d'élément(s) d'une géométrie ( sub-shape ) ou d'élément(s) de maillage ( groupe de maille) à partir de l'arbre salome
        retourne ( la liste des noms des groupes, message d'erreur )
        
        Note: Appelé par EFICAS lorsqu'on clique sur le bouton ajouter à la liste du panel AFF_CHAR_MECA        
        """
        names, msg = [], ''
        try:            
            atLeastOneStudy = self.__studySync()
            if not atLeastOneStudy:
                return names, msg
            # récupère toutes les sélections de l'utilsateur dans l'arbre Salome
            entries = salome.sg.getAllSelected()
            nbEntries = len( entries )
            if nbEntries >= 1:
#                 jdcID = self.bureau.nb.getcurselection()
                jdcID = self.bureau.JDCDisplay_courant                
                for entry in entries:
                    if studyManager.palStudy.isMeshGroup( entry ): #sélection d'un groupe de maille
                        name, msg = self.__selectMeshGroup( jdcID, entry, kwType )
                    elif studyManager.palStudy.isShape( entry ): #sélection d'une sous-géométrie
                        name, msg = self.__selectShape( jdcID, entry, kwType )
                    else:
                        name, msg = '', msgUnAuthorizedSelecion
                    if name:
                        names.append( name )                    
                        
            if names and len( names ) < nbEntries:                        
                msg = msgIncompleteSelection
            salome.sg.EraseAll()
        except:            
            logger.debug(50*'=')
        return names, msg                
        
        
    def addJdcInSalome(  self, jdcPath ):
        """
        Ajoute le Jeu De Commande ASTER ou HOMARD dans l'arbre d'étude Salome dans la rubrique EFICAS
        """
        ok, msgError = False, msgErrorAddJdcInSalome
        try:            
            atLeastOneStudy = self.__studySync()
            if not atLeastOneStudy:
                return ok, msgError
                        
            fileType = { 'ASTER':  studyManager.FICHIER_EFICAS_ASTER,
                        'HOMARD': studyManager.FICHIER_EFICAS_HOMARD }
                        
            folderName = {  'ASTER':  'AsterFiles',
                            'HOMARD': 'HomardFiles' }                                    
                        
            moduleEntry = studyManager.palStudy.addComponent(self.module)
            itemName    = re.split("/",jdcPath)[-1]
            
            fatherEntry = studyManager.palStudy.addItem(
                                    moduleEntry,
                                    itemName = folderName[self.bureau.code],
                                    itemIcon = "ICON_COMM_FOLDER",
                                    itemType = studyManager.ASTER_FILE_FOLDER,
                                    bDoublonCheck = True  )
                                                                        
            commEntry = studyManager.palStudy.addItem( fatherEntry ,
                                                        itemName = itemName,
                                                        itemType = fileType[ self.bureau.code ],
                                                        itemValue = jdcPath,
                                                        itemComment = str( jdcPath ),
                                                        itemIcon    = "ICON_COMM_FILE",
                                                        bDoublonCheck = True )
            studyManager.palStudy.refresh()                                                       
            print 'addJdcInSalome commEntry->', commEntry            
            if commEntry:
                ok, msgError = True, ''        
        except:                    
            logger.debug(50*'=')
        return ok, msgError        
        
                
    def createOrUpdateMesh( self ):
        """
            Ouverture d'une boite de dialogue : Creation de groupes de mailles dans un maillage existant ou un nouveau maillage.                         
            Note: Appelé par EFICAS à la sauvegarde du JDC.
        """
        try:            
            atLeastOneStudy = self.__studySync()
            if not atLeastOneStudy:
                return
            
#             jdcID = self.bureau.nb.getcurselection()
            jdcID = self.bureau.JDCDisplay_courant
            
            groupeMaNames = self.__getAllGroupeMa( self.bureau.JDCDisplay_courant.tree.item )
            groupeNoNames = self.__getAllGroupeNo( self.bureau.JDCDisplay_courant.tree.item )
            
            # on elimine les doublons de la liste
            groupeMaNames = dict.fromkeys(groupeMaNames).keys()
            groupeNoNames = dict.fromkeys(groupeNoNames).keys()
            
            print 'CS_pbruno createOrUpdateMesh groupeMaNames', groupeMaNames
            print 'CS_pbruno createOrUpdateMesh groupeNoNames', groupeNoNames
                        
            # mise à jours de la liste des sous-géométrie ( self.subShapes )
            if not self.mainShapeEntries.has_key( jdcID ):
                # l'utilisateur n'a sélectionné aucune sous-géométrie et donc pas de géométrie principale
                groupeMaNames, groupeNoNames  = self.__selectMainShape( groupeMaNames, groupeNoNames, jdcID )
                
            if groupeMaNames or groupeNoNames:                                                
                print 'CS_pbruno createOrUpdateMesh groupeMaNames', groupeMaNames
                print 'CS_pbruno createOrUpdateMesh groupeNoNames', groupeNoNames            
                self.__updateSubShapes( jdcID, groupeMaNames + groupeNoNames )
    
                # recupération des identifiants( entries ) associés aux noms des groupes        
                groupeMaEntries = []
                groupeNoEntries = []                            
                
                for entry, name in self.subShapes.items():
                    if name in groupeMaNames:
                        groupeMaEntries.append( entry )
                    if name in groupeNoNames:                
                        groupeNoEntries.append( entry )    

                if groupeMaEntries or groupeNoEntries:                    
                    diag = meshGui.MeshUpdateDialogImpl(
                                self.mainShapeEntries[jdcID],
                                groupeMaEntries,
                                groupeNoEntries,
                                studyManager.palStudy,
                                self.parent )
                    diag.show()
                
            self.subShapes.clear()
            self.mainShapeNames.clear()
            self.mainShapeEntries.clear()                
        except:                    
            logger.debug(50*'=')
        
                
    def displayMeshGroups(self, meshGroupName):
        """
        visualisation group de maille de nom meshGroupName dans salome
        """
        ok, msgError = False, ''
        try:
            sg = salome.ImportComponentGUI('SMESH')
            currentjdcID = self.bureau.nb.getcurselection()
            meshGroupEntries = []
            selMeshEntry = None
            selMeshGroupEntry = None
            
            # liste des groupes de maille de nom meshGroupName
            listSO = studyManager.palStudy._myStudy.FindObjectByName(meshGroupName, "SMESH")
            print "liste des groupes de maille de nom %s: "%(meshGroupName), listSO
            
            if len(listSO)>0:
                for SObjet in listSO:
                    groupEntry = SObjet.GetID()                
                    meshGroupEntries += [groupEntry]                    
                
                if len(meshGroupEntries)>1:
                
                    # choix d'un maillage
                    if not self.workingMesh.has_key(currentjdcID): # aucun maillage de défini par défaut encore
                        #selMeshEntry = "0:1:3:5" #CS_pbruno todo : choix maillage + test si c un maillage
                        selMeshEntry, keep = self.__selectWorkingMesh(meshGroupEntries)
                        if keep:
                            self.workingMesh[currentjdcID] = selMeshEntry
                    else: # déja un de défini par défaut
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
                    #CS_pbruno: marche QUE si le module SMESH est activé
                    myComponent = salome.lcc.FindOrLoadComponent("FactoryServer", "SMESH")
                    SCom        = studyManager.palStudy._myStudy.FindComponent("SMESH")
                    studyManager.palStudy._myBuilder.LoadWith( SCom , myComponent  )                             
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
        visualisation géométrie de nom shapeName dans salome
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
            
            atLeastOneStudy = self.__studySync()
            if not atLeastOneStudy:
                return ok, msgError            
                                     
            #salome.sg.EraseAll()
            print 'displayShapestrGeomShape shapeName -> ', shapeName
            
            if currentViewType == VISU.TVIEW3D: # maillage
                print 'Vue courante = VTK : affichage groupe de maille'                
                ok, msgError = self.displayMeshGroups(shapeName)
            else: #geometrie
                print 'Vue courante = OCC : affichage element geometrique'
                #self.__createOCCView()
                current_color = COLORS[ self.icolor % LEN_COLORS ]                
                ok = studyManager.palStudy.displayShapeByName( shapeName, current_color )
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
                print unite
                type=dico[unite][0]
                fic=dico[unite][1:]
                ligne="fort."+str(unite)+" "+type+" "+fic
                f.write(ligne)
           f.close()
           self.rangeInStudy(sauvegarde)
	   print "==============================="
	   print "fin crreConfigTxt"    
        """
        pass #CS_pbruno à implémenter
           
           
    def buildCabriGeom( self, name, **param ):
        """
        visualisation dans GEOM d'une géométrie CABRI
        """
        import cabri        
        qt.QApplication.setOverrideCursor( qt.QCursor.waitCursor )
        cabri.tetra( name, **param )
        qt.QApplication.restoreOverrideCursor()
        
        

#-------------------------------------------------------------------------------------------------------
#    Pilotage de la Visu des elements de structures
#

    def envoievisu(self,liste_commandes):
        #try:
        if ( 1 == 1 ):
            atLeastOneStudy = self.__studySync()
            if not atLeastOneStudy:
                return
            monDriver=visuDriver.visuDriver(studyManager.palStudy,liste_commandes)
            monId = monDriver.analyse()
            PALGUI_API.displaySE(monId)

        else:
        #except:
            print "boum dans envoievisu"


        
#-------------------------------------------------------------------------------------------------------        
#           Point d'entré lancement EFICAS
#
def runEficas( code="ASTER", fichier=None, module = studyManager.SEficas ):
    global appli    
    if not appli: #une seul instance possible!        
        appli = MyEficas( SalomePyQt.SalomePyQt().getDesktop(), code = code, fichier = fichier, module = module )
        
        
 
# pour compatibilité           
def runHomard( code="HOMARD", fichier=None ):
    global appli    
    if not appli: #une seul instance possible!                        
        appli = MyEficas( SalomePyQt.SalomePyQt().getDesktop(), code = code, fichier = fichier )
        

        
        
"""        
def runAster(parent = SalomePyQt.SalomePyQt().getDesktop(), palStudyManager = studyManager.palStudy, code="ASTER", fichier=None ) :
    global appli    
    if not appli: #une seul instance possible!                        
        appli = MyEficas( parent, palStudyManager, code = code, fichier = fichier )
"""    

    
     
# Init globale du module
root = Tkinter.Tk()
root.withdraw()


appli = None



logger=ExtLogger( "eficasSalome.py" )




