# -*- coding: utf-8 -*-
#_____________________________________

import sys, os, re,types

from pal.logger import ExtLogger
logger=ExtLogger( "EFICAS_SRC.EFICASGUI.eficasSalome.py" )

import eficasConfig 
# eficasConfig definit le EFICAS_ROOT
# lignes de path ajoutees pour acceder aux packages python du
# logiciel Eficas. Le package Aster est ajoute explicitement pour
# acceder au module prefs.py. A
sys.path[:0]=[eficasConfig.eficasPath,
              os.path.join( eficasConfig.eficasPath,'Editeur'),
              os.path.join( eficasConfig.eficasPath,'UiQT4'),
              eficasConfig.eficasPath,
             ]


import Editeur    
from InterfaceQT4 import qtEficas

import salome
import SalomePyQt


from pal.studyedit import getStudyEditor
from pal.structelem import StructuralElementManager, InvalidParameterError


# couleur pour visualisation des geometries 
import colors
COLORS = colors.ListeColors
LEN_COLORS = len( COLORS )


class MyEficas( qtEficas.Appli ):
    """
    Classe de lancement du logiciel EFICAS dans SALOME
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
        self.editor = getStudyEditor()    # Editeur de l'arbre d'etude

        
        # donnee pour la creation de groupe de maille
        self.mainShapeNames   = {} #dictionnaire pour gerer les multiples fichiers possibles ouverts par 
                                   #eficas ( cle = identifiant du JDC ), une mainshape par fichier ouvert.    
                                   #dictionnaire des sous-geometrie de la geometrie principale ( cle = entry, valeur = name ) 
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
     
 
# ___________________________ Methodes de l ex Pal __________________________________

    #----------------------------------------------------------------
    def getCORBAObjectInComponent( self,  entry, composant ):
    #----------------------------------------------------------------
       object = None
       mySO = self.editor.study.FindObjectID(entry)
       if mySO:
          object = mySO.GetObject()
          if not object:
             myComponent = salome.lcc.FindOrLoadComponent("FactoryServer", composant)
             SCom        = self.editor.study.FindComponent( composant )
             print myComponent , SCom
             self.editor.builder.LoadWith( SCom , myComponent  )
             object      = mySO.GetObject()
       if not object :
             logger.debug("selectedEntry: An error occurs")
       return object


    #-------------------------------------
    def isMeshGroup( self,entry):
    #-------------------------------------
       result=False
       import SMESH
       try:
         monObjet =self.getCORBAObjectInComponent(entry,"SMESH") 
         #print monObjet
         if monObjet != None :                                    # selection d'un groupe de SMESH
            if  monObjet._narrow(SMESH.SMESH_GroupBase):
                result = True 
         #print result
       except :
         logger.debug(' isMeshGroup pb avec ( entry = %s ) ' %entry )          
       return result

    #-------------------------------------
    def isShape( self,entry):
    #-------------------------------------
       result=False
       import GEOM
       try:
         monObjet =self.getCORBAObjectInComponent(entry,"GEOM") 
         if monObjet != None :                                    # selection d'un objet GEOM
            if  monObjet._narrow(GEOM.GEOM_Object ):
                result = True 
       except :
         logger.debug(' isShape pb avec ( entry = %s ) ' %entry )          
       return result

    #-----------------------------------------------------------------
    def getMainShapeEntry(self,entry):
    #-----------------------------------------------------------------
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

    #-----------------------------------------------------------------
    def isMainShape(self,entry):
    #-----------------------------------------------------------------
        result = False
        try:
            monObjet =self.getCORBAObjectInComponent(entry,"GEOM") 
            import GEOM
            shape    = monObjet._narrow( GEOM.GEOM_Object )
            if shape.IsMainShape():
                result = True
        except:
            logger.debug( 'Errreur pour SalomeStudy.isMainShape( entry = %s ) ' %entry )
            result = False
        return result

    
    #-----------------------------------------------------------------
    def ChercheType( self, shape ):
    #-----------------------------------------------------------------
        tgeo =  shape.GetShapeType() 
        geomEngine = salome.lcc.FindOrLoadComponent( "FactoryServer", "GEOM" )
        #print dir(self.editor.study)
        groupIMeasureOp = geomEngine.GetIMeasureOperations(self.editor.study._get_StudyId())
        if tgeo != "COMPOUND" : return tgeo

        strInfo =  groupIMeasureOp.WhatIs( shape )
        dictInfo = {}
        l = strInfo.split('\n')

        for couple in l:
             nom, valeur = couple.split(':')
             dictInfo[ nom.strip() ] = valeur.strip()

        ordre = [ "COMPSOLID", "SOLID", "SHELL", "FACE", "WIRE", "EDGE", "VERTEX" ]
        for t in ordre:
            if dictInfo[ t ] != '0':
               tgeo = t
               return tgeo
        return None


    #-----------------------------------------------------------------
    def selectShape( self, editor, entry, kwType = None ):
    #-----------------------------------------------------------------
        """
        selection sous-geometrie dans Salome:
        -test1) si c'est un element sous-geometrique .
        -test2) si appartient a la geometrie principale.
        """
        name, msgError = '',''
        mySO = self.editor.study.FindObjectID(entry)
        if mySO == None :
           return name, msgError
        object = mySO.GetObject()
        if object == None :
           return name, msgError

        import GEOM
        shape  = object._narrow( GEOM.GEOM_Object )
        if not shape :
           return name, msgError

        tGeo=self.ChercheType(shape)
        if not tGeo :
           return name, msgError
        if kwType == "GROUP_NO" and str(tGeo) != "VERTEX":
            name,msgError = '',"la selection n est pas un Vertex"
            return name, msgError
        elif kwType == "GROUP_MA" and str(tGeo) == "VERTEX":
            name, msgError = '', "la selection n est pas un groupe de maille"
            return name, msgError

        mainShapeEntry = self.getMainShapeEntry( entry )
        if self.mainShapeNames.has_key( editor ):
          #print "------------- self.mainShapeNames[editor]" , self.mainShapeNames[editor]
          if self.mainShapeNames[editor] == mainShapeEntry:
             name=mySO.GetName()
          else :
             msgError="Le groupe reference la geometrie " + mainShapeEntry + " et non " + self.mainShapeNames[editor]
        else :
          self.mainShapeNames[editor] = mainShapeEntry
          name=mySO.GetName()
       
        return name, msgError
        

    #-----------------------------------------------------------------
    def selectMeshGroup( self, editor, selectedEntry, kwType = None ):
    #-----------------------------------------------------------------
        """
        selection groupe de maille dans Salome:
        -test 1) si c'est un groupe de maille
        -test 2) si le maillage fait reference a la geometrie principale
        """
        name, msgError = '',''

        mySO=self.editor.study.FindObjectID(selectedEntry )
        from pal.smeshstudytools import SMeshStudyTools
        monSMeshStudyTools=SMeshStudyTools(self.editor)
        meshSO = monSMeshStudyTools.getMeshFromGroup(mySO)
        if meshSO == None : return name, msgError    

       # on verifie que l entree selectionnee a le bon type (NODE ou EDGE...)
        tGroup = ""
        groupObject = self.getCORBAObjectInComponent(selectedEntry,"SMESH")
        if not groupObject :
           logger.debug("selectedMeshEntry: An error occurs")

        import SMESH
        aGroup = groupObject._narrow( SMESH.SMESH_GroupBase )
        if aGroup: tGroup = aGroup.GetType()

        if kwType == "GROUP_NO" and tGroup != SMESH.NODE:
             msgError = "GROUP_NO attend un groupe de noeud"
        elif kwType == "GROUP_MA" and tGroup == SMESH.NODE:
             msgError = "GROUP_MA attend un point goupe de maille"
             return name, msgError

        # on cherche la shape associee
        #PN PN mesh_Object est un SOject
        meshObject = meshSO.GetObject()
        mesh     = meshObject._narrow( SMESH.SMESH_Mesh  )
        if mesh:         #c'est bien un objet maillage
             shape = mesh.GetShapeToMesh()
             if shape:
                ior = salome.orb.object_to_string( shape )
                if ior:
                   sObject   = self.editor.study.FindObjectIOR(  ior )
                   mainShapeID = sObject.GetID()
             else :
                mainShapeID=0
        else :
             return name, "Type d objet non permis"    

        # on cherche si la shape associee est la bonne
        #print "------------- mainShapeID" , mainShapeID
        if self.mainShapeNames.has_key( editor ):
          #print "------------- self.mainShapeNames[editor]" , self.mainShapeNames[editor]
          if self.mainShapeNames[editor] == mainShapeID:
             name=mySO.GetName()
          else :
             msgError="Le groupe reference la geometrie " + mainShapeID + " et non " + self.mainShapeNames[editor]
        else :
          self.mainShapeNames[editor] = mainShapeID
          name=mySO.GetName()

        #print "------------------------------ name :", name
        #print "------------------------------ name :", name
        #print "------------------------------ name :", name
        return name,msgError


    def displayMeshGroups(self, meshGroupName):
        """
        visualisation group de maille de nom meshGroupName dans salome
        """
        ok, msgError = False, ''
        try:
        #if 1 :
            sg = salome.ImportComponentGUI('SMESH')
            meshGroupEntries = []
            selMeshEntry = None
            selMeshGroupEntry = None
            
            # liste des groupes de maille de nom meshGroupName
            listSO = self.editor.study.FindObjectByName(meshGroupName, "SMESH")
            #print listSO
            #print "liste des groupes de maille de nom %s: "%(meshGroupName), listSO
            
            if len(listSO)>1:
               return 0,'Plusieurs objets  portent ce nom'
            if len(listSO) ==0 :
               return 0,'Aucun objet ne porte ce nom'
            SObjet=listSO[0]
            groupEntry = SObjet.GetID()                
            myComponent = salome.lcc.FindOrLoadComponent("FactoryServer", "SMESH")
            SCom        = self.editor.study.FindComponent("SMESH")
            myBuilder   = self.editor.study.NewBuilder()
            myBuilder.LoadWith( SCom , myComponent  )                             
            sg.CreateAndDisplayActor(groupEntry)
            #color = COLORS[ self.icolor % LEN_COLORS ]                
            #self.icolor = self.icolor + 1
            #sg.SetColor(groupEntry, color[0], color[1], color[2])
            salome.sg.Display(groupEntry)
            salome.sg.FitAll()                
            ok = True                

        except:
        #else :
            msgError = "Impossible d afficher "+shapeName
            logger.debug(50*'=')
        return ok, msgError

# ___________________________ Methodes appelees par EFICAS  __________________________________
    #----------------------------------------------------------------
    def selectGroupFromSalome( self, kwType = None, editor=None):
    #----------------------------------------------------------------
        """
        Selection d'element(s) d'une geometrie ( sub-shape ) ou d'element(s) de maillage ( groupe de maille)  partir de l'arbre salome
        retourne ( la liste des noms des groupes, message d'erreur )
      
        Note: Appele par EFICAS lorsqu'on clique sur le bouton ajouter la liste du panel GROUPMA        
        """
        names, msg = [], ''
        try:            
            atLeastOneStudy = self.editor.study
            if not atLeastOneStudy:
                return names, msg

           # recupere toutes les selections de l'utilsateur dans l'arbre Salome
            entries = salome.sg.getAllSelected()
            nbEntries = len( entries )
            if nbEntries >= 1:
                for entry in entries:
                    if self.isMeshGroup(entry):               # selection d 'un sous maillage
                       name, msg = self.selectMeshGroup( editor, entry, kwType )
                    elif self.isShape(entry):               # selection d'une sous-geometrie
                       name, msg = self.selectShape( editor, entry, kwType )
                    else:
                       name, msg = None, "Selection SALOME non autorisee."
                    if name:
                       names.append( name )                    
                        
        except:            
            logger.debug("selectGroupFromSalome: An error occurs")
        #print "=================== selectGroupFromSalome ", names, msg
        #print "=================== selectGroupFromSalome ", names, msg
        #print "=================== selectGroupFromSalome ", names, msg
        return names, msg                
        
    #---------------------------------------------
    def addJdcInSalome(  self, jdcPath ):
    #---------------------------------------------
        """
        Ajoute le Jeu De Commande dans l'arbre d'etude Salome dans la rubrique EFICAS
        Revu pour QT4
        """
        msgError    = "Erreur dans l'export du fichier de commande dans l'arbre d'etude Salome"
        ok = False
        #try:            
        if 1:
            atLeastOneStudy = self.editor.study
            if not atLeastOneStudy:
                return ok, msgError
                        
            fileType = { 'ASTER'    : "FICHIER_EFICAS_ASTER",
                         'SEP'      : "FICHIER_EFICAS_SEP",
                         'MAP'      : "FICHIER_EFICAS_MAP",
                         'OPENTURNS': "FICHIER_EFICAS_OPENTURNS",
                         'OPENTURNS_STUDY': "FICHIER_EFICAS_OPENTURNS_STUDY",
                         'OPENTURNS_WRAPPER': "FICHIER_EFICAS_OPENTURNS_WRAPPER",
                        }
                        
            folderName = {  'ASTER'    :  'AsterFiles',
                            'SEP'       : 'OMFiles' ,
                            'MAP'       : 'MapFiles' ,
                            'OPENTURNS_STUDY': 'OpenturnsFiles',                                    
                            'OPENTURNS_WRAPPER': 'OpenturnsFiles'}                                    

            folderType = { 'ASTER':    "ASTER_FILE_FOLDER",
                           'SEP':      "SEP_FILE_FOLDER",
                           'MAP':      "MAP_FILE_FOLDER",
                           'OPENTURNS_STUDY':"OPENTURNS_FILE_FOLDER",
                           'OPENTURNS_WRAPPER': "OPENTURNS_FILE_FOLDER"}

                        
            moduleEntry = self.editor.findOrCreateComponent(self.module)
            itemName    = re.split("/",jdcPath)[-1]
            
            fatherEntry = self.editor.findOrCreateItem(
                                    moduleEntry,
                                    name = folderName[self.code],
                                    #icon = "ICON_COMM_FOLDER",
                                    fileType = folderType[self.code])
                                                                        
            commEntry = self.editor.findOrCreateItem( fatherEntry ,
                                           name = itemName,
                                           fileType = fileType[ self.code ],
                                           fileName = jdcPath,
                                           #icon    = "ICON_COMM_FILE",
                                           comment = str( jdcPath ))

            salome.sg.updateObjBrowser(1)

            #print 'addJdcInSalome commEntry->', commEntry            
            if commEntry:
                ok, msgError = True, ''        
        #except:                    
        #    logger.debug(50*'=' Erreur au AddJDC)
        return ok, msgError        
        
           
    #---------------------------------------
    def displayShape(  self, shapeName ):
    #---------------------------------------
        """
        visualisation de nom shapeName dans salome
        """
        ok, msgError = False, ''
        try:
            import VISU
            import visu_gui
            currentViewType = None
            visu_gui.myVisu.SetCurrentStudy(self.editor.study)
            m = visu_gui.myVisu.GetViewManager()
            v = m.GetCurrentView()
            #print v
            if v:
                currentViewType = v.GetType()
            atLeastOneStudy = self.editor.study
            if not atLeastOneStudy:
                return ok, msgError
                                     
            #salome.sg.EraseAll()
            #print 'displayShapestrGeomShape shapeName -> ', shapeName
            #print currentViewType
            
            if currentViewType == VISU.TVIEW3D: # maillage
                #print 'Vue courante = VTK : affichage groupe de maille'                
                ok, msgError = self.displayMeshGroups(shapeName)
            else: #geometrie
                current_color = COLORS[ self.icolor % LEN_COLORS ]                
                from pal.geomtools import GeomStudyTools
                myGeomTools=GeomStudyTools(self.editor)
                ok = myGeomTools.displayShapeByName( shapeName, current_color )
                salome.sg.FitAll()
                self.icolor = self.icolor + 1             
                if not ok:
                    msgError = "Impossible d afficher "+shapeName
        except:            
            logger.debug(50*'=')
        return ok, msgError    
                
           
#    def buildCabriGeom( self, name, **param ):
        """
        visualisation dans GEOM d'une geometrie CABRI
        """
#        import cabri        
#        qt.QApplication.setOverrideCursor( qt.QCursor.waitCursor )
#        cabri.tetra( name, **param )
#        qt.QApplication.restoreOverrideCursor()
        
        
        
#-------------------------------------------------------------------------------------------------------
#    Pilotage de la Visu des elements de structures
#


    def envoievisu(self,liste_commandes):
        import traceback
        try:
            atLeastOneStudy = self.editor.study
            if not atLeastOneStudy:
                return
            logger.debug(10*'#'+":envoievisu: creating a StructuralElementManager instance")
            structElemManager = StructuralElementManager()
            elem = structElemManager.createElement(liste_commandes)
            elem.display()
            salome.sg.updateObjBrowser(True)
        except InvalidParameterError, err:
            from PyQt4.QtGui import QMessageBox
            trStr = self.tr("Invalid parameter for group %(group)s: %(expr)s must be "
                            "greater than %(minval)g (actual value is %(value)g)")
            msg = str(trStr) % {"group": err.groupName, "expr": err.expression,
                                "minval": err.minValue, "value": err.value}
            QMessageBox.warning(self, self.tr("Error"), msg)
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

        
        

appli = None



