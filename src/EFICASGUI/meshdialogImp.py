# -*- coding: iso-8859-1 -*-
from qt import *
from meshdialog  import MeshDialog
from EficasStudy import study, SMesh



#CS_pbruno c'est � partir de ces donn�es que la boite de dialogue est cr�e ( param�tres obligatoires )
mainShapeEntry = ''
groupeMaEntries = []
groupeNoEntries = []



# CS_pbruno message � placer dans un module appropri�( EficasMsg.py �cr�er )
warning = 'Attention!'
msg1 = "erreur cr�ation maillage dans Salome"
msg2 = "erreur mise � jours maillage dans Salome"

msg3 = "g�om�trie principale ind�termin�e"
msg4 = "liste des sous-g�om�tries ind�termin�e"


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

        if self.rbNewMesh.isChecked(): # l'utilisateur choisi de cr�e un nouveau maillage
            self.__createSalomeMesh( mainShapeEntry, groupeMaEntries, groupeNoEntries )
        else:   # l'utilisateur choisi un maillage existant
            self.__updateSalomeMesh( groupeMaEntries, groupeNoEntries )
        self.close()

        # r�init obligatoire des variables globales pour prochaine utilisation
        mainShapeEntry = ''
        groupeMaEntries = []
        groupeNoEntries = []


        
        

    def __fillLbMeshes( self, mainShapeEntryIn ):
        """
        Rempli la liste des maillages possibles � modifier ( ceux r�f�rencant
        la g�om�trie principale indiqu�e en param�tre d'entr�e )
        """
        self.lbMeshes.clear()
        meshEntries = study.getAllMeshReferencingMainShape( mainShapeEntryIn )

        if meshEntries: # il existe au moins un maillage dans l'arbre d'�tude Salome r�f�ren�ant la g�om�trie principale
            for aMeshEntry in meshEntries:
                aMeshName = study.getNameAttribute( aMeshEntry )
                self.lbMeshes.insertItem( aMeshName )
                self.meshEntries[ aMeshName ] = aMeshEntry                
        else:           # pas de maillages, il faudra obligatoirment en cr�e une nouvelle
            self.rbUpdateMesh.setEnabled(0)
            self.lbMeshes.setEnabled(0)


    def __meshUniqueName( self, nameIn ):
        """
        Contr�le si objet du composant 'Mesh' poss�de d�j� le nom fourni en param�tre
        retourne le m�me nom si ce n'est pas le cas, le m�me nom avec un suffixe sinon
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
        Fonction de cr�ation d'un nouveau maillage dans Salome
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
        Fonction de mise � jours d'un maillage existant( s�l�ctionn� par l'utilisateur ds la listBox ) dans Salome
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
      



