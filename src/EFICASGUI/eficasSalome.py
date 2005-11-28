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
msgSubShapeBadMainShape    = "La s�lection g�om�trique SALOME ne correspond pas � une sous-g�om�trie de la g�om�trie principale : "
msgMeshGroupBadMainShape   = "Le groupe de maillage s�lectionn� dans SALOME ne r�f�rence pas la bonne g�om�trie principale : "
msgIncompleteSelection     = "Tous les �l�ments de la s�lection SALOME n'ont pu �tre ajout�e"
msgUnAuthorizedSelecion    = "S�lection SALOME non authoris�. Autoris� : sous-g�om�trie, groupe de maille"
msgErrorAddJdcInSalome     = "Erreur dans l'export du fichier de commande dans l'arbre d'�tude Salome"
msgErrorDisplayShape       = "Erreur dans l'affichage de la forme g�om�trique s�lectionn�e"





#class MyEficas( Tkinter.Toplevel, eficas.EFICAS, QXEmbed ):
class MyEficas( Tkinter.Toplevel, eficas.EFICAS ):
    """
    Classe de lancement du logiciel EFICAS dans SALOME.
    Cette classe sp�cialise le logiciel Eficas par l'ajout de:        
    a)la cr�ation de groupes de mailles dans le composant SMESH de SALOME
    b)la visualisation d'�l�ments g�om�trique dans le coposant GEOM de SALOME par s�lection dans EFICAS
    """
    def __init__(self, parent, palStudyManager, code = None, fichier = None ):
        """
        Constructeur.
                
        @type   parent: 
        @param  parent: widget Qt parent
        
        @type   palStudyManager: studyManager.SalomeStudy
        @param  palStudyManager: gestionnaire d'�tude SALOME
        
        @type   code: string
        @param  code: catalogue � lancer ( ASTER, HOMARD ). optionnel ( d�faut = ASTER ).
        
        @type   fichier: string
        @param  fichier: chemin absolu du fichier eficas � ouvrir � d�s le lancement. optionnel
        """
        #QXEmbed.__init__( self, parent, "", qt.Qt.WDestructiveClose | qt.Qt.WStyle_Customize | qt.Qt.WStyle_StaysOnTop )        
        Tkinter.Toplevel.__init__( self )
        
        #----------------------------  initialisation EFICAS  -----------------  
        splash.init_splash( self, code = code, titre = "Lancement d'EFICAS pour %s" %code )
        splash._splash.configure( text="Chargement d'EFICAS en cours.\n Veuillez patienter ..." )
        # diff�rence eficas 1.7 et 1.8
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
        #------  embarcation dans une fen�tre qt pour mise au premier plan  ---
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
        
        #--------------- sp�cialisation EFICAS dans SALOME  -------------------                
        self.parent = parent        
        self.salome = True                     #active les parties de code sp�cifique dans Salome
        self.palStudyManager = palStudyManager # gestionnaire �tude SALOME
        
        # donn�e pour la cr�ation de groupe de maille
        self.mainShapeNames   = {} #dictionnaire pour g�rer les multiples fichiers possibles ouverts par 
        self.mainShapeEntries = {} #eficas ( cl� = identifiant du JDC ), une mainshape par fichier ouvert.    
        self.subShapes        = {} #dictionnaire des sous-g�om�trie de la g�om�trie principale ( cl� = entry, valeur = name ) 
        #----------------------------------------------------------------------
    
        
    def quit(self): 
        global appli        
        self.destroy()
        appli = None                
            
        

    def __selectShape( self, jdcID, selectedEntry ):
        """
        s�lection sous-g�om�trie dans Salome:
        -test1) si c'est un �l�ment g�om�trique.
        -test2) si appartient � la g�om�trie principale.
        
        met � jours la liste self.subShapes si test ok
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
                print 'CS_pbruno pas la m�me mainshape selectedEntry->',selectedEntry
                if not self.mainShapeNames.has_key( jdcID ):
                    self.mainShapeNames[ jdcID ] = self.palStudyManager.getNameAttribute( self.mainShapeEntries[ jdcID ] )
                msgError = msgSubShapeBadMainShape + self.mainShapeNames[ jdcID ]

        return name, msgError 
        
        
        
    def __selectMeshGroup( self, jdcID, selectedEntry ):
        """
        s�lection groupe de maille dans Salome:
        -test 1) si c'est un groupe de maille 
        -test 2) si le maillage fait r�f�rence � la g�om�trie principale 
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
                    print 'CS_pbruno pas la m�me mainshape selectedEntry ->',selectedEntry
                    if not self.mainShapeNames.has_key( jdcID ):
                        self.mainShapeNames[ jdcID ] = self.palStudyManager.getNameAttribute( self.mainShapeEntries[ jdcID ] )
                    msgError = msgMeshGroupBadMainShape + self.mainShapeNames[ jdcID ]                   
                                
        return name, msgError 
        
        
    
        
    def __updateSubShapes( self, jdcID, groupeNames ):
        """
        mise � jours de la liste self.subShapes � partir de la liste des noms de groupe fourni en entr�
        """
        for name in groupeNames:
            entries = self.palStudyManager.getEntriesFromName( studyManager.SGeom, name )
            for entry in entries:
                ok, msgError = self.__selectShape( jdcID, entry ) # filtre
                if ok:
                    self.subShapes[ entry ] = name
                    
        
    def __getAllGroupeMa(self, item ):
        """
        R�cup�re tous les GROUPE_MA dans le JDC courant
        """
        groupMa = ()                
        try:
            itemName  = item.get_nom()
            #print 'CS_pbruno itemName',itemName             
            if itemName == 'GROUP_MA':
                itemValue = item.get_valeur()
                print 'CS_pbruno trouv�! GROUP_MA->', itemValue
                if type( itemValue ) == str:
                    groupMa += ( itemValue , )
                elif type( itemValue ) == tuple:
                    groupMa += itemValue                
            else:
                children = item.GetSubList()
                for child in children:            
                    groupMa +=  self.__getAllGroupeMa( child )
        except: # � cause de GetSubList()...
            pass
        print 'CS_pbruno groupMa',groupMa
        return groupMa                
        
   
    def __getAllGroupeNo(self, item ):
        """
        R�cup�re tous les GROUPE_NO dans le JDC courant
        """
        groupNo = ()                
        try:
            itemName  = item.get_nom()
            print 'CS_pbruno itemName',itemName            
            if itemName == 'GROUP_NO':
                itemValue = item.get_valeur()
                print 'CS_pbruno trouv�! GROUP_NO->', itemValue
                if type( itemValue ) == str:
                    groupNo += ( itemValue , )
                elif type( itemValue ) == tuple:
                    groupNo += itemValue
            else:
                children = item.GetSubList()
                for child in children:            
                    groupNo += self.__getAllGroupeNo( child )
        except: # � cause de GetSubList()...
            pass 
        return groupNo
        
    #-----------------------  LISTE DES NOUVEAUX CAS D'UTILISATIONS -----------
    def selectGroupFromSalome( self ):
        """
        S�lection d'�l�ment(s) d'une g�om�trie ( sub-shape ) ou d'�l�ment(s) de maillage ( groupe de maille) � partir de l'arbre salome
        retourne ( la liste des noms des groupes, message d'erreur )
        
        Note: Appel� par EFICAS lorsqu'on clique sur le bouton ajouter � la liste du panel AFF_CHAR_MECA        
        """
        print 'CS_pbruno selectGroupFromSalome'
        names, msg = [], ''
        try:
            # r�cup�re toutes les s�lections de l'utilsateur dans l'arbre Salome
            entries = salome.sg.getAllSelected()
            print 'CS_pbruno entries->',entries
            nbEntries = len( entries )
            if nbEntries >= 1:
                print 'CS_pbruno len( entries ) >= 1:'
                jdcID = self.bureau.nb.getcurselection()
                for entry in entries:
                    if self.palStudyManager.isMeshGroup( entry ): #s�lection d'un groupe de maille
                        name, msg = self.__selectMeshGroup( jdcID, entry )
                    elif self.palStudyManager.isShape( entry ): #s�lection d'une sous-g�om�trie
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
        Ajoute le Jeu De Commande ASTER ou HOMARD dans l'arbre d'�tude Salome dans la rubrique EFICAS
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
            Note: Appel� par EFICAS � la sauvegarde du JDC.
            """
            
            jdcID   = self.bureau.nb.getcurselection()
            
            groupeMaNames = self.__getAllGroupeMa( self.bureau.JDCDisplay_courant.tree.item )
            groupeNoNames = self.__getAllGroupeNo( self.bureau.JDCDisplay_courant.tree.item )            
            
            print 'CS_pbruno createOrUpdateMesh groupeMaNames', groupeMaNames
            print 'CS_pbruno createOrUpdateMesh groupeNoNames', groupeNoNames
                        
            # mise � jours de la liste des sous-g�om�trie ( self.subShapes )
            self.__updateSubShapes( jdcID, groupeMaNames )
            self.__updateSubShapes( jdcID, groupeNoNames )
            
            
            # recup�ration des identifiants( entries ) associ�s aux noms des groupes        
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
        visualisation g�om�trie de nom shapeName dans salome
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
        pass #CS_pbruno � impl�menter
        
        
    
        
        
        
        
        
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