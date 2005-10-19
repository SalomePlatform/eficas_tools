# -*- coding: iso-8859-1 -*-
from qt import *
from meshdialog  import MeshDialog
from EficasStudy import study, SMesh



#CS_pbruno c'est à partir de ces données que la boite de dialogue est crée ( paramètres obligatoires )
mainShapeEntry = ''
groupeMaEntries = []
groupeNoEntries = []



# CS_pbruno message à placer dans un module approprié( EficasMsg.py àcréer )
warning = 'Attention!'
msg1 = "erreur création maillage dans Salome"
msg2 = "erreur mise à jours maillage dans Salome"

msg3 = "géométrie principale indéterminée"
msg4 = "liste des sous-géométries indéterminée"


class MeshDialogImpl( MeshDialog ):
    def __init__(self, parent = None,name = None,modal = 0,fl = 0):
        MeshDialog.__init__(self,parent,name,modal,fl)
        self.meshEntries = {}        
        if not mainShapeEntry:
            QMessageBox.warning( self, warning,  msg3 )
        else:
            self.__fillLbMeshes( mainShapeEntry )            
        if not ( groupeMaEntries or groupeNoEntries ):
            QMessageBox.warning( self, warning,  msg4 )
        self.show()        
        

    def enableOK( self):
        self.buttonOk.setEnabled( 1 )


    def accept( self ):
        global mainShapeEntry, groupeMaEntries, groupeNoEntries

        if self.rbNewMesh.isChecked(): # l'utilisateur choisi de crée un nouveau maillage
            self.__createSalomeMesh( mainShapeEntry, groupeMaEntries, groupeNoEntries )
        else:   # l'utilisateur choisi un maillage existant
            self.__updateSalomeMesh( groupeMaEntries, groupeNoEntries )
        self.close()

        # réinit obligatoire des variables globales pour prochaine utilisation
        mainShapeEntry = ''
        groupeMaEntries = []
        groupeNoEntries = []


        
        

    def __fillLbMeshes( self, mainShapeEntryIn ):
        """
        Rempli la liste des maillages possibles à modifier ( ceux référencant
        la géométrie principale indiquée en paramètre d'entrée )
        """
        self.lbMeshes.clear()
        meshEntries = study.getAllMeshReferencingMainShape( mainShapeEntryIn )

        if meshEntries: # il existe au moins un maillage dans l'arbre d'étude Salome référençant la géométrie principale
            for aMeshEntry in meshEntries:
                aMeshName = study.getNameAttribute( aMeshEntry )
                self.lbMeshes.insertItem( aMeshName )
                self.meshEntries[ aMeshName ] = aMeshEntry                
        else:           # pas de maillages, il faudra obligatoirment en crée une nouvelle
            self.rbUpdateMesh.setEnabled(0)
            self.lbMeshes.setEnabled(0)


    def __meshUniqueName( self, nameIn ):
        """
        Contrôle si objet du composant 'Mesh' possède déjà le nom fourni en paramètre
        retourne le même nom si ce n'est pas le cas, le même nom avec un suffixe sinon
        """        
        uniqueName  = nameIn
        suffix      = 0
        strSuffix   = ''
                        
        while study.hasName( SMesh, uniqueName + strSuffix  ):
            suffix += 1
            strSuffix = str( suffix )
            
        uniqueName = uniqueName + strSuffix
        
        return uniqueName
        
           

    def __createSalomeMesh( self, mainShapeEntryIn, groupeMaEntriesIn, groupeNoEntriesIn ):
        """
        Fonction de création d'un nouveau maillage dans Salome
        """
        ok = False
        try:
            mainShapeName = study.getNameAttribute( mainShapeEntryIn )
            newMeshName   = str( mainShapeName ) +  '_Mesh'            
            newMeshName   = self.__meshUniqueName( newMeshName )            
            study.createMesh( newMeshName, mainShapeEntryIn,  groupeMaEntriesIn, groupeNoEntriesIn )
            study.refresh()
            ok = True
        except:
            QMessageBox.warning( self, warning,  msg1 )
        return ok
        

    def __updateSalomeMesh( self, groupeMaEntriesIn, groupeNoEntriesIn  ):
        """
        Fonction de mise à jours d'un maillage existant( séléctionné par l'utilisateur ds la listBox ) dans Salome
        """
        ok = False
        try:                            
            item = self.lbMeshes.selectedItem()            
            selectedMeshName = str( item.text() )
            meshEntry = self.meshEntries[ selectedMeshName ]
            study.updateMesh( meshEntry, groupeMaEntriesIn, groupeNoEntriesIn )
            study.refresh()
            ok = True
        except:
            QMessageBox.warning( self, warning,  msg2 )
        return ok
      



