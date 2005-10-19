# -*- coding: iso-8859-1 -*-
import salomedsgui
import salome

import SALOMEDS
import GEOM
import SMESH

from Logger import Logger
logger=Logger( "EficasStudy" )


#Nom des composants SALOME dans l'arbre d'�tude
SMesh  = "Mesh"
SGeom  = "Geometry"
SVisu  = "Post-Pro"
SAster = "Aster"


class SalomeStudy(   salomedsgui.guiDS ):
    """
    Classe de manipulation de l'arbre d'�tude Salome. Cette classe permet � 
    l'utilisateur de manipuler les objets de 'arbre d'�tude via leurs 
    identifiants( entry ).
    
    Attention : Par d�faut les op�rations r�alis�e par cette classe portent sur 
    une �tude courante ( positionn�e dans le constructeur ou par la m�thode 
    setCurrentStudyID() )
    """    
    def __init__( self, studyID = salome.myStudyId ):        
        salomedsgui.guiDS.__init__( self  )
        self.setCurrentStudy( studyID)
        
        # sp�cifique m�thode __getMeshType() :
        self.groupOp    = None
        self.geomEngine = None
        
        # sp�cifique m�thode createMesh() :
        self.smeshEngine = None 
        
        
                
    # --------------------------------------------------------------------------
    #   fonctions de manipulation g�n�rale ( porte sur toute l'arbre d'�tude )
    def __getCORBAObject( self,  entry ):         
        """
        Retourne l'objet CORBA correspondant son identifiant ( entry ) dans 
        l'arbre d'�tude.
        
        @type   entry : string
        @param  entry : objet Corba 
        
        @rtype  :  objet CORBA
        @return :  l'objet CORBA,   None si erreur.
        """
        object = None
        try:            
            mySO = self._myStudy.FindObjectID( entry )            
            if mySO:            
                object = mySO.GetObject()
                
                if not object: # l'objet n'a pas encore charg�
                    path          = self._myStudy.GetObjectPath( mySO )# recherche du nom du composant
                    componentName = ( path.split('/')[1] ).strip()

                    if componentName == SMesh:
                        strContainer, strComponentName = "FactoryServer", "SMESH"
                    elif componentName == SGeom:
                        strContainer, strComponentName = "FactoryServer", "GEOM"
                    elif componentName == SVisu:
                        strContainer, strComponentName = "FactoryServer", "VISU"
                    elif componentName == SAster:
                        strContainer, strComponentName = "FactoryServerPy", "ASTER"
                    else :
                        logger.debug('>>>>CS_Pbruno StudyTree.__getCORBAObject chargement du composant  %s non impl�ment� ' %componentName)
                        raise 'Erreur'                        
                        
                    myComponent = salome.lcc.FindOrLoadComponent( strContainer, strComponentName )
                    SCom        = self._myStudy.FindComponent( strComponentName )
                    self._myBuilder.LoadWith( SCom , myComponent  )
                    object      = mySO.GetObject()
        except:
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]
            logger.debug( '>>>>CS_Pbruno StudyTree.__getCORBAObject erreur recup�ration  objet corba ( entry = %s ) ' %entry)
            logger.debug( 'type        = %s ,             value       = %s '%( type, value ) )
            object = None
            
        return object
        
        
    def __getEntry( self, corbaObject ):
        """
        Retourne l'identifiant ( entry ) ds l'arbre d'�tude de l'objet CORBA 
        pass� en param�tre.
                
        @type     corbaObject : objet Corba
        @param  corbaObject   : objet Corba 
        
        @rtype  :  string
        @return :  identifiant ( entry ),    None si erreur.
        """
        entry        = None
        currentStudy = self._myStudy
                
        if corbaObject:
            ior = salome.orb.object_to_string( corbaObject )
            if ior:
                sObject = currentStudy.FindObjectIOR(  ior )                
                entry   = sObject.GetID()
        return entry
        
        

    def setCurrentStudyID( self, studyID):
        """
        Fixe l'�tude courante sur laquel vont op�rer toutes les fonctions 
        de la classe.        
        """        
        self._father    = None
        self._component = None
        self._myStudy   = self._myStudyManager.GetStudyByID( studyID)        
        self._myBuilder = self._myStudy.NewBuilder( )
                
        salome.myStudy       = self._myStudy
        salome.myStudyId     = studyID
        salome.myStudyName   = self._myStudy._get_Name()        
    
    def refresh( self ):        
        """
        Rafraichissement de l'arbre d'�tude
        """
        salome.sg.updateObjBrowser(0)
                
    def setName( self, entry, name ):
        """
        Fixe le nom( la valeur de l'attribut 'AttributeName' ) d'un objet de l'arbre d'�tude
        d�sign� par son identifiant( entry )
                
        @type   entry: string
        @param  entry: identifiant de l'objet dans l'arbre d'�tude
        
        @type   name: string
        @param  name: nom � attribuer
        
        @rtype  :  boolean
        @return :  True si Ok, False sinon, None si erreur
        """
        result = False
        try:
            SObject = self._myStudy.FindObjectID( entry )
            A1      = self._myBuilder.FindOrCreateAttribute( SObject, "AttributeName" )
            AName   = A1._narrow(SALOMEDS.AttributeName)
            AName.SetValue( name )
            result = True            
        except:
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]
            logger.debug( '>>>>CS_Pbruno StudyTree.setName ( entry = %s, name = %s )' %( entry, name ) )
            logger.debug( 'type        = %s ,             value       = %s '%( type, value ) )
            result = None
            
        return result

    def hasName( self, componentName, objectName ):
        """
        V�rifie si dans l'arbre d'�tude le commposant de nom componentName
        poss�de un objet de nom objectName.
                
        @type   componentName: string
        @param  componentName: nom du composant Salome
        
        @type   objectName: string
        @param  objectName: nom de l'objet 
        
        @rtype  :  boolean
        @return :  True si Ok, False sinon,  None si erreur
        """
        result = False
        try:
            nom = {            
                SMesh:  "SMESH",
                SGeom:  "GEOM",
                SVisu:  "VISU",
                SAster: "ASTER"            
            }
            componentName = nom[ componentName ]            
            SObjects = self._myStudy.FindObjectByName( objectName, componentName )
            if len( SObjects ) > 0:
                result = True            
        except:
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]
            logger.debug( '>>>>CS_Pbruno StudyTree.setName ( entry = %s, name = %s )' %( entry, name ) )
            logger.debug( 'type        = %s ,             value       = %s '%( type, value ) )
            result = None
            
        return result


        


    # --------------------------------------------------------------------------
    #   fonctions de manipulation des objets g�om�triques dans l'arbre d'�tude
    #   ( �l�ments contenu dans la sous-rubrique "Geometry' )
    def isMainShape(  self,  entry ):
        """
        Teste si l'objet d�sign� par l'identifiant ( entry ) pass� en argument 
        est bien un objet g�om�trique principal.
                
        @type   entry: string
        @param  entry: identifiant de l'objet 
        
        @rtype:   boolean
        @return:  True si Ok, False sinon
        """
        result = False
        try:            
            anObject = self.__getCORBAObject(  entry )
            shape    = anObject._narrow( GEOM.GEOM_Object )            
            if shape.IsMainShape():
                result = True                        
        except:
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]            
            logger.debug( '>>>>CS_Pbruno StudyTree.isMainShape( entry = %s ) ' %entry )
            logger.debug( 'type        = %s ,             value       = %s '%( type, value ) )
            result = False            
        return result
        
    
    def getMainShapeEntry(  self,  entry ):
        """
        Retourne l'identifiant de l'objet g�om�trique principal du sous-objet g�om�trique d�sign� par 
        l'identifiant ( entry ) pass� en param�tre.
        
        @type   entry: string
        @param  entry: identifiant du sous-objet g�om�trique
        
        @rtype  :  string 
        @return :  identifiant de  l'objet g�om�trique principal, None si erreur.
        """
        result = None
        try :
            if self.isMainShape( entry ):
                result = entry
            else:
                anObject = self.__getCORBAObject(  entry )
                shape    = anObject._narrow( GEOM.GEOM_Object )
                objMain  = shape.GetMainShape()                
                result   = self.__getEntry( objMain )                
        except :
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]            
            print '>>>>CS_Pbruno StudyTree.getMainShapeEntry( entry = %s ) ' %entry
            print 'type        = %s ,             value       = %s '%( type, value )
            result = None
           
        return result
        
    def sameMainShape(  self,  shapeEntry1, shapeEntry2 ):
        """
        D�termine si les objets g�ometriques fournis en argument sont les 
        sous-objets d'une m�me g�om�trie principale
                
        @type   shapeEntry1: string
        @param  shapeEntry1: identifiant dans l'arbre d'�tude d'un objet g�om�trique
        
        @type   shapeEntry2: string
        @param  shapeEntry2: identifiant dans l'arbre d'�tude d'un objet g�om�trique
        
        @rtype  :  boolean
        @return :  True si m�me objet principal, False sinon, None si erreur.
        """
        result = None
        try :
            mainShape1 = self.getMainShapeEntry( shapeEntry1 )
            if mainShape1:
                mainShape2 = self.getMainShapeEntry( shapeEntry2 )
                if mainShape2:
                    result = mainShape1 == mainShape2
        except :
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]            
            print '>>>>CS_Pbruno StudyTree.sameMainShape(  shapeEntry1 = %s , shapeEntry2 = %s )'%( shapeEntry1, shapeEntry2 )
            print 'type        = %s ,             value       = %s '%( type, value )
            result = None
           
        return result
                
        
    # --------------------------------------------------------------------------
    #   fonctions de manipulation des objets maillages  dans l'arbre d'�tude
    #   ( �l�ments contenu dans la sous-rubrique 'Mesh' )
    def __getMeshType( self, shapeEntry ):
        """
        Determination du type de maille en fonction de la g�om�trie pour les conditions aux limites.
        
        @type     shapeEntry : string
        @param  shapeEntry : identifiant de l'objet g�om�trique
        
        @rtype:   SMESH::ElementType ( voir SMESH_Mesh.idl )
        @return:  type de maillage, None si erreur.
        """ 
        result = None
        
        try:        
            anObject = self.__getCORBAObject(  shapeEntry )
            shape    = anObject._narrow( GEOM.GEOM_Object )
            
            if shape: #Ok, c'est bien un objet g�om�trique
                tgeo = str( shape.GetShapeType() )
                
                meshTypeStr = {
                    "VERTEX" :         SMESH.NODE,
                    "EDGE":             SMESH.EDGE,
                    "FACE":             SMESH.FACE,
                    "SOLID":            SMESH.VOLUME,
                    "COMPOUND" :  None
                }
                result = meshTypeStr[ tgeo]
                if result == None:                    
                    if not self.geomEngine:
                        self.geomEngine = salome.lcc.FindOrLoadComponent( "FactoryServer", "GEOM" )
                    if not self.GroupOp:
                        self.GroupOp  = self.geomEngine.GetIGroupOperations(  salome.myStudyId )
                        
                    tgeo = self.GroupOp.GetType( shape )
                    meshTypeInt = { #Voir le dictionnnaire ShapeType dans geompy.py pour les correspondances type - numero.
                        7:      SMESH.NODE, 
                        6:      SMESH.EDGE,
                        4:      SMESH.FACE,
                        2:      SMESH.VOLUME
                    }
                    if meshTypeInt.has_key(  int( tgeo ) ):
                        result = meshTypeInt[ tgeo]                    
        except:
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]            
            logger.debug( '>>>>CS_Pbruno StudyTree.__getMeshType( shapeEntry  = %s ) ' %shapeEntry )
            logger.debug( 'type        = %s ,             value       = %s '%( type, value ))
            result = None
            
        return result
        
    def getAllMeshReferencingMainShape( self, mainShapeEntry ):
        """
        Retourne une liste de tous les maillages construits � partir de l'objet
        principal g�om�trique pass� en argument
        
        @type     mainShapeEntry : string
        @param    mainShapeEntry : identifiant( entry ) de l'objet  principal g�om�trique
        
        @rtype:   list
        @return:  liste des identifiants( entry ) des maillages, liste vide si aucun , None si erreur.
        """
        result = []
        
        try:
            if self.isMainShape(  mainShapeEntry ):
                mainShapeSO = salome.IDToSObject( mainShapeEntry )
                SObjectList = self._myStudy.FindDependances( mainShapeSO )
                print '####  mainShapeSO=%s , SObjectList  = %s'%( mainShapeSO, SObjectList )
                if SObjectList: #Ok, il y a des objet r�f�ren�ant la mainShape
                    for SObject in SObjectList: # Recherche du type de chacun des objets
                        SFatherComponent = SObject.GetFatherComponent()
                        print '####  SFatherComponent = %s'%SFatherComponent 
                        if SFatherComponent.GetName() == SMesh: #Ok, l'objet est un objet du composant 'Mesh'
                            SFather = SObject.GetFather()
                            print '####  SFather= %s'%SFather
                            ##CorbaObject = SFather.GetObject()
                            FatherEntry = SFather.GetID()
                            CorbaObject  = self.__getCORBAObject(  FatherEntry )
                            print '####  CorbaObject = %s'%CorbaObject 
                            MeshObject = CorbaObject ._narrow( SMESH.SMESH_Mesh )
                            print '####  MeshObject = %s'%MeshObject 
                            if MeshObject : #Ok, l'objet est un objet 'maillage'
                                MeshObjectEntry = self.__getEntry( MeshObject )
                                print '####  MeshObjectEntry = %s'%MeshObjectEntry 
                                if MeshObjectEntry:
                                    result.append( MeshObjectEntry )  # On l'ajoute ds la liste r�sultat!
            else: # c'est pas une mainShape !
                result = None            
        except :
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]            
            logger.debug( '>>>>CS_Pbruno StudyTree.getAllMeshReferencingMainShape( mainShapeEntry  = %s ) ' %mainShapeEntry )
            logger.debug( 'type        = %s ,             value       = %s '%( type, value ))
            result = None
            
        return result 
        

        
    def updateMesh( self,  meshEntry, groupeMaEntries, groupeNoEntries ):
        """
        Met � jours d'un objet maillage � partir d'une liste de sous-objet g�om�trique.
        L'op�ration consiste � cr�er des groupes dans le maillage correspondant 
        aux sous-objets g�om�trique de la liste.
        
        CS_pbruno Attention: ajoute des groupes sans v�rifier si auparavant ils ont d�j� �t� cr�es
        
        @type   meshEntry : string
        @param  meshEntry : identifiant du maillage
        
        @type   groupeMaEntries : liste de string
        @param  groupeMaEntries : liste contenant les identifiants ( entry ) des sous-objets g�om�triques
                                  sur lesquel on veut construire des groupes de face.

        @type   groupeNoEntries : liste de string
        @param  groupeNoEntries : liste contenant les identifiants ( entry ) des sous-objets g�om�triques
                                  sur lesquel on veut construire des groupes de noeuds.
        
        @rtype:   bool
        @return:  True si update OK, False en cas d'erreur
        """
        result = False
        try:
            #print 'CS_pbruno updateMesh( self,  meshEntry=%s,   groupeMaEntries=%s )'%( meshEntry,   groupeMaEntries )
            corbaObject = self.__getCORBAObject(  meshEntry  )
            mesh        = corbaObject._narrow( SMESH.SMESH_Mesh )
            
            if mesh: # Ok, c'est bien un maillage
                shapeName = ""
                meshType  = None
                
                #cr�ation groupes de noeud
                for shapeEntry in groupeNoEntries:
                    anObject = self.__getCORBAObject(  shapeEntry )
                    shape    = anObject._narrow( GEOM.GEOM_Object )
                    if shape: #Ok, c'est bien un objet g�om�trique
                        shapeName = self.getNameAttribute( shapeEntry )
                        mesh.CreateGroupFromGEOM( SMESH.NODE, shapeName, shape )
                    else:
                        pass            # CS_pbruno au choix: 1)une seule erreur arr�te l'int�gralit� de l'op�ration
                        #return False   #                    2)ou on continue et essaye les suivants ( choix actuel

                #cr�ation groupes de face
                for shapeEntry in groupeMaEntries:
                    meshType = self.__getMeshType( shapeEntry )
                    if meshType:                        
                        anObject = self.__getCORBAObject(  shapeEntry )
                        shape    = anObject._narrow( GEOM.GEOM_Object )
                        if shape: #Ok, c'est bien un objet g�om�trique                            
                            shapeName = self.getNameAttribute( shapeEntry )
                            mesh.CreateGroupFromGEOM( meshType, shapeName, shape )
                        else:
                            pass            #CS_pbruno au choix: 1)une seule erreur arr�te l'int�gralit� de l'op�ration
                            #return False   #                    2)ou on continue et essaye les suivants ( choix actuel )
                    else:
                        pass            #CS_pbruno au choix: 1)une seule erreur arr�te l'int�gralit� de l'op�ration 
                        #return False   #                    2)ou on continue et essaye les suivants ( choix actuel )

                result = True
                        
        except:
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]            
            logger.debug( '>>>>CS_Pbruno StudyTree.updateMesh( meshEntry= %s,   groupeMaEntries = %s )' %( meshEntry, groupeMaEntries))
            logger.debug( 'type        = %s ,             value       = %s '%( type, value ))
            result = None
        return result
        
        
        
    
        
        
    def createMesh( self, newMeshName, mainShapeEntry, groupeMaEntries, groupeNoEntries ):
        """
        Cr�ation d'un objet maillage � partir d'un objet g�om�trique principal
        Les groupes dans le maillage sont cr�e � partir des sous-objets g�om�triques
        contenu dans la liste fourni en param�tre d'entr�.

        @type   newMeshName : string
        @param  newMeshName : nom du nouveau maillage
        
        @type   mainShapeEntry : string
        @param  mainShapeEntry : identifiant de l'objet g�om�trique principal        
        
        @type   groupeMaEntries : liste de string
        @param  groupeMaEntries : liste contenant les identifiants ( entry ) des sous-objets g�om�triques
                                  sur lesquel on veut construire des groupes de face.

        @type   groupeNoEntries : liste de string
        @param  groupeNoEntries : liste contenant les identifiants ( entry ) des sous-objets g�om�triques
                                  sur lesquel on veut construire des groupes de noeuds.
        
        @rtype:   string
        @return:  identifiant( entry ) dans l'arbre d'�tude du nouveau maillage, None en cas d'erreur.
        """        
        result = False
        try:
            #print 'CS_pbruno createMesh( self, newMeshName=%s, mainShapeEntry=%s, groupeMaEntries=%s )'%( newMeshName, mainShapeEntry, groupeMaEntries )
            newMesh = None
            anObject = self.__getCORBAObject(  mainShapeEntry )            
            shape    = anObject._narrow( GEOM.GEOM_Object )            
            if shape:                
                # Cr�ation du nouveau maillage
                if not self.smeshEngine:
                    self.smeshEngine = salome.lcc.FindOrLoadComponent( "FactoryServer", "SMESH" )
                    self.smeshEngine.SetCurrentStudy( salome.myStudy )
                newMesh      = self.smeshEngine.CreateMesh( shape )
                newMeshEntry = self.__getEntry( newMesh )                                
                if newMeshEntry:                    
                    ok = self.setName( newMeshEntry, newMeshName )                    
                    if ok:
                        result = self.updateMesh( newMeshEntry, groupeMaEntries, groupeNoEntries )
        except:
            import sys
            type        = sys.exc_info()[0]
            value       = sys.exc_info()[1]            
            logger.debug( '>>>>CS_Pbruno StudyTree.createMesh( self, newMeshName=%s, mainShapeEntry=%s, groupeMaEntries=%s )'%( newMeshName, mainShapeEntry, groupeMaEntries))
            logger.debug( 'type        = %s ,             value       = %s '%( type, value ))
            result = None
        return result



    
           

    
    
    
# --------------------------------------------------------------------------
#   INIT
study = SalomeStudy()
    
