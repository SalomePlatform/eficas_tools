import qt
import notifqt
# -----------------------------------------------------------------------------
import sys, os



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
import studyManager

#from qxembed import QXEmbed

import SalomePyQt



# message utilisateur
msgWarning                 = "Attention"
msgSubShapeBadMainShape    = "La sélection géométrique SALOME ne correspond pas à une sous-géométrie de la géométrie principale : "
msgMeshGroupBadMainShape   = "Le groupe de maillage sélectionné dans SALOME ne référence pas la bonne géométrie principale : "
msgIncompleteSelection     = "Tous les éléments de la sélection SALOME n'ont pu étre ajoutée"
msgUnAuthorizedSelecion    = "Sélection SALOME non authorisé. Autorisé : sous-géométrie, groupe de maille"
msgErrorAddJdcInSalome     = "Erreur dans l'export du fichier de commande dans l'arbre d'étude Salome"
msgErrorDisplayShape       = "Erreur dans l'affichage de la forme géométrique sélectionnée"





#class MyEficas( Tkinter.Toplevel, eficas.EFICAS, QXEmbed ):
class MyEficas( Tkinter.Toplevel, eficas.EFICAS ):
    """
    Classe de lancement du logiciel EFICAS dans SALOME.
    Cette classe spécialise le logiciel Eficas par l'ajout de:        
    a)la création de groupes de mailles dans le composant SMESH de SALOME
    b)la visualisation d'éléments géométrique dans le coposant GEOM de SALOME par sélection dans EFICAS
    """
    def __init__(self, parent, palStudyManager, code = None, fichier = None ):
        """
        Constructeur.
                
        @type   parent: 
        @param  parent: widget Qt parent
        
        @type   palStudyManager: studyManager.SalomeStudy
        @param  palStudyManager: gestionnaire d'étude SALOME
        
        @type   code: string
        @param  code: catalogue à lancer ( ASTER, HOMARD ). optionnel ( défaut = ASTER ).
        
        @type   fichier: string
        @param  fichier: chemin absolu du fichier eficas à ouvrir à dès le lancement. optionnel
        """
        #QXEmbed.__init__( self, parent, "", qt.Qt.WDestructiveClose | qt.Qt.WStyle_Customize | qt.Qt.WStyle_StaysOnTop )        
        Tkinter.Toplevel.__init__( self )
        
        #----------------------------  initialisation EFICAS  -----------------  
        splash.init_splash( self, code = code, titre = "Lancement d'EFICAS pour %s" %code )
        splash._splash.configure( text="Chargement d'EFICAS en cours.\n Veuillez patienter ..." )
        # différence eficas 1.7 et 1.8
        if Editeur.__dict__.has_key( 'session' ):
            print 'CS_pbruno has_key session'
            from Editeur import session
            eficasArg = sys.argv
            if fichier:
                eficasArg += [ fichier ]
            session.parse( eficasArg )            
               
        eficas.EFICAS.__init__( self,  self, code = code )
        #----------------------------------------------------------------------
        
        
        """
        #------  embarcation dans une fenêtre qt pour mise au premier plan  ---
        #embedded = QXEmbed( parent, "", qt.Qt.WDestructiveClose | qt.Qt.WStyle_Customize | qt.Qt.WStyle_StaysOnTop )        
        embedded = QXEmbed( parent, "" )
        embedded.initialize()        
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
        self.salome = True                     #active les parties de code spécifique dans Salome
        self.palStudyManager = palStudyManager # gestionnaire étude SALOME
        
        # donnée pour la création de groupe de maille
        self.mainShapeNames   = {} #dictionnaire pour gérer les multiples fichiers possibles ouverts par 
        self.mainShapeEntries = {} #eficas ( clé = identifiant du JDC ), une mainshape par fichier ouvert.    
        self.subShapes        = {} #dictionnaire des sous-géométrie de la géométrie principale ( clé = entry, valeur = name ) 
        #----------------------------------------------------------------------
    
        
    def quit(self): 
        global appli        
        self.destroy()
        appli = None                
            
        

    def __selectShape( self, jdcID, selectedEntry ):
        """
        sélection sous-géométrie dans Salome:
        -test1) si c'est un élément géométrique.
        -test2) si appartient à la géométrie principale.
        
        met à jours la liste self.subShapes si test ok
        """
        print 'CS_pbruno __selectShape'
        name, msgError = '',''        
                
        selectedMainShapeEntry = self.palStudyManager.getMainShapeEntry( selectedEntry )
        
        if selectedMainShapeEntry: #ok test1)        
            if not self.mainShapeEntries.has_key( jdcID ):
                self.mainShapeEntries[ jdcID ] = selectedMainShapeEntry
            if selectedMainShapeEntry == self.mainShapeEntries[ jdcID ]:
                name = self.palStudyManager.getNameAttribute( selectedEntry )
                self.subShapes[ selectedEntry ] = name
            else:
                print 'CS_pbruno pas la même mainshape selectedEntry->',selectedEntry
                if not self.mainShapeNames.has_key( jdcID ):
                    self.mainShapeNames[ jdcID ] = self.palStudyManager.getNameAttribute( self.mainShapeEntries[ jdcID ] )
                msgError = msgSubShapeBadMainShape + self.mainShapeNames[ jdcID ]

        return name, msgError 
        
        
        
    def __selectMeshGroup( self, jdcID, selectedEntry ):
        """
        sélection groupe de maille dans Salome:
        -test 1) si c'est un groupe de maille 
        -test 2) si le maillage fait référence à la géométrie principale 
        """
        print 'CS_pbruno __selectMeshGroup'
        name, msgError = '',''
                
        selectedMeshEntry = self.palStudyManager.getMesh( selectedEntry )
                
        if selectedMeshEntry: # ok test 1)
            print 'CS_pbruno __selectMeshGroup selectedMeshEntry',selectedMeshEntry
            selectedMainShapeEntry = self.palStudyManager.getShapeFromMesh( selectedMeshEntry )
            
            if selectedMainShapeEntry: #test 2)
                print 'CS_pbruno __selectMeshGroup selectedMainShapeEntry',selectedMainShapeEntry
                if not self.mainShapeEntries.has_key( jdcID ):
                    self.mainShapeEntries[ jdcID ] = selectedMainShapeEntry
                if selectedMainShapeEntry == self.mainShapeEntries[ jdcID ]:
                    name = self.palStudyManager.getNameAttribute( selectedEntry  )  #ok test 2)
                else:
                    print 'CS_pbruno pas la même mainshape selectedEntry ->',selectedEntry
                    if not self.mainShapeNames.has_key( jdcID ):
                        self.mainShapeNames[ jdcID ] = self.palStudyManager.getNameAttribute( self.mainShapeEntries[ jdcID ] )
                    msgError = msgMeshGroupBadMainShape + self.mainShapeNames[ jdcID ]                   
                                
        return name, msgError 
        
        
    
        
    def __updateSubShapes( self, jdcID, groupeNames ):
        """
        mise à jours de la liste self.subShapes à partir de la liste des noms de groupe fourni en entré
        """
        for name in groupeNames:
            entries = self.palStudyManager.getEntriesFromName( studyManager.SGeom, name )
            for entry in entries:
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
            #print 'CS_pbruno itemName',itemName             
            if itemName == 'GROUP_MA':
                itemValue = item.get_valeur()
                print 'CS_pbruno trouvé! GROUP_MA->', itemValue
                if type( itemValue ) == str:
                    groupMa += ( itemValue , )
                elif type( itemValue ) == tuple:
                    groupMa += itemValue                
            else:
                children = item.GetSubList()
                for child in children:            
                    groupMa +=  self.__getAllGroupeMa( child )
        except: # à cause de GetSubList()...
            pass
        print 'CS_pbruno groupMa',groupMa
        return groupMa                
        
   
    def __getAllGroupeNo(self, item ):
        """
        Récupère tous les GROUPE_NO dans le JDC courant
        """
        groupNo = ()                
        try:
            itemName  = item.get_nom()
            print 'CS_pbruno itemName',itemName            
            if itemName == 'GROUP_NO':
                itemValue = item.get_valeur()
                print 'CS_pbruno trouvé! GROUP_NO->', itemValue
                if type( itemValue ) == str:
                    groupNo += ( itemValue , )
                elif type( itemValue ) == tuple:
                    groupNo += itemValue
            else:
                children = item.GetSubList()
                for child in children:            
                    groupNo += self.__getAllGroupeNo( child )
        except: # à cause de GetSubList()...
            pass 
        return groupNo
        
    #-----------------------  LISTE DES NOUVEAUX CAS D'UTILISATIONS -----------
    def selectGroupFromSalome( self ):
        """
        Sélection d'élément(s) d'une géométrie ( sub-shape ) ou d'élément(s) de maillage ( groupe de maille) à partir de l'arbre salome
        retourne ( la liste des noms des groupes, message d'erreur )
        
        Note: Appelé par EFICAS lorsqu'on clique sur le bouton ajouter à la liste du panel AFF_CHAR_MECA        
        """
        print 'CS_pbruno selectGroupFromSalome'
        names, msg = [], ''
        try:
            # récupère toutes les sélections de l'utilsateur dans l'arbre Salome
            entries = salome.sg.getAllSelected()
            print 'CS_pbruno entries->',entries
            nbEntries = len( entries )
            if nbEntries >= 1:
                print 'CS_pbruno len( entries ) >= 1:'
                jdcID = self.bureau.nb.getcurselection()
                for entry in entries:
                    if self.palStudyManager.isMeshGroup( entry ): #sélection d'un groupe de maille
                        name, msg = self.__selectMeshGroup( jdcID, entry )
                    elif self.palStudyManager.isShape( entry ): #sélection d'une sous-géométrie
                        name, msg = self.__selectShape( jdcID, entry )
                    else:
                        name, msg = '', msgUnAuthorizedSelecion
                    if name:
                        names.append( name )                    
                        
            if names and len( names ) < nbEntries:                        
                msg = msgIncompleteSelection
        except:
            pass
        salome.sg.EraseAll()
        print 'CS_pbruno selectGroupFromSalome names = ',names        
        return names, msg                
        
        
    def addJdcInSalome(  self, jdcPath ):
        """
        Ajoute le Jeu De Commande ASTER ou HOMARD dans l'arbre d'étude Salome dans la rubrique EFICAS
        """
        ok, msgError = False, ''
                
        if self.bureau.code == 'ASTER':
            ok = self.palStudyManager.addEficasItem( jdcPath, studyManager.FICHIER_EFICAS_ASTER )
        elif self.bureau.code == 'HOMARD':
            ok = self.palStudyManager.addEficasItem( jdcPath, studyManager.FICHIER_EFICAS_HOMARD )
            #ok = self.palStudyManager.addEficasItem( jdcPath, studyManager.FICHIER_EFICAS_HOMARD_CONF ) CS_pbruno ?????
        if not ok:
            msgError = msgErrorAddJdcInSalome
        return ok, msgError        
        
                
    def createOrUpdateMesh( self ):
            """
            Ouverture d'une boite de dialogue : Creation de groupes de mailles dans un maillage existant ou un nouveau maillage.                         
            Note: Appelé par EFICAS à la sauvegarde du JDC.
            """
            
            jdcID   = self.bureau.nb.getcurselection()
            
            groupeMaNames = self.__getAllGroupeMa( self.bureau.JDCDisplay_courant.tree.item )
            groupeNoNames = self.__getAllGroupeNo( self.bureau.JDCDisplay_courant.tree.item )            
            
            print 'CS_pbruno createOrUpdateMesh groupeMaNames', groupeMaNames
            print 'CS_pbruno createOrUpdateMesh groupeNoNames', groupeNoNames
                        
            # mise à jours de la liste des sous-géométrie ( self.subShapes )
            self.__updateSubShapes( jdcID, groupeMaNames )
            self.__updateSubShapes( jdcID, groupeNoNames )
            
            
            # recupération des identifiants( entries ) associés aux noms des groupes        
            groupeMaEntries = []
            groupeNoEntries = []                            
            
            for entry, name in self.subShapes.items():
                if name in groupeMaNames:                
                    groupeMaEntries.append( entry )
                if name in groupeNoNames:                
                    groupeNoEntries.append( entry )
                    
                    
            print 'CS_pbruno groupeMaEntries ->',groupeMaEntries 
            print 'CS_pbruno groupeNoEntries ->',groupeNoEntries
            if groupeMaEntries or groupeNoEntries:
                print 'if groupeMaEntries or groupeNoEntries:'
                diag = meshGui.MeshUpdateDialogImpl( self.mainShapeEntries[jdcID], groupeMaEntries, groupeNoEntries, self.palStudyManager,
                                                     self.parent )
                diag.show()
        
                
    def displayShape(  self, shapeName ):
        """
        visualisation géométrie de nom shapeName dans salome
        """
        ok, msgError = False, ''        
        salome.sg.EraseAll()
        print 'displayShapestrGeomShape shapeName -> ', shapeName 
        ok = self.palStudyManager.displayShapeByName( shapeName )
        if not ok:
            msgError = msgErrorDisplayShape
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
        
        
    
        
        
        
        
        
#def runEficas( palStudyManager, code="ASTER", fichier=None, studyId=None):
def runEficas( parent = SalomePyQt.SalomePyQt().getDesktop(), palStudyManager = studyManager.study, code="ASTER", fichier=None ):
    global appli    
    if not appli: #une seul instance possible!                        
        appli = MyEficas( parent, palStudyManager, code = code, fichier = fichier )
        
    
def runHomard( parent = SalomePyQt.SalomePyQt().getDesktop(), palStudyManager = studyManager.study, code="HOMARD", fichier=None ):    
    global appli    
    if not appli: #une seul instance possible!                        
        appli = MyEficas( parent, palStudyManager, code = code, fichier = fichier )

        
"""        
def runAster(parent = SalomePyQt.SalomePyQt().getDesktop(), palStudyManager = studyManager.study, code="ASTER", fichier=None ) :
    global appli    
    if not appli: #une seul instance possible!                        
        appli = MyEficas( parent, palStudyManager, code = code, fichier = fichier )
"""    

    
     
# Init globale du module
root = Tkinter.Tk()
root.withdraw()

appli = None








"""
        #embedded.showMaximized()
        #embedded.embed( appli.winfo_id() )        
        
        embedded.setWFlags( qt.Qt.WStyle_Customize | qt.Qt.WStyle_StaysOnTop )
        embedded.setFocus()
        
        if embedded.hasFocus () :
            print 'hasfocus'
        else:
            print 'pas  focus'
            
            
        if embedded.isFocusEnabled():
            print 'isFocusEnabled()'
        else:
            print 'not isFocusEnabled()'
        
        focusP = embedded.focusPolicy()
        
        if focusP == qt.QWidget.TabFocus:
            print 'qt.QWidgetTabFocus' 
        elif focusP == qt.QWidget.ClickFocus:
            print 'qt.ClickFocus'
        elif focusP == qt.QWidget.StrongFocus:
            print 'qt.StrongFocus' 
        elif focusP == qt.QWidget.WheelFocus:
            print 'qt.WheelFocus'
        elif focusP == qt.QWidget.NoFocus:
            print 'qt.NoFocus'
        else:
            print 'bizarre'
        
        embedded.grabKeyboard()
        """