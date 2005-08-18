#=============================================================================
# File      : SMESH_utils.py
# Created   : jeu fév 20 18:53:34 CET 2003
# Author    : Paul RASCLE, EDF
# Project   : SALOME
# Copyright : EDF 2003
#  $Header: /home/salome/PlateFormePAL/Bases_CVS_EDF/Modules_EDF/EFICAS_SRC/src/EFICASGUI/SMESH_utils.py,v 1.5 2005/02/03 15:15:09 salome Exp $
#=============================================================================

from omniORB import CORBA
import LifeCycleCORBA
import SALOMEDS
import GEOM
import SMESH
from eficasCL import *

# initialise the ORB
orb = CORBA.ORB_init([''], CORBA.ORB_ID)

# create an LifeCycleCORBA instance
lcc = LifeCycleCORBA.LifeCycleCORBA(orb)

geom = lcc.FindOrLoadComponent("FactoryServer", "GEOM")
smesh = lcc.FindOrLoadComponent("FactoryServer", "SMESH")

    #--------------------------------------------------------------------------

def entryToIor(myStudy,entry):
    """
    Retourne une référence ior de l'entry passée en argument.
    """
    ior = None
    iorString = entryToIorString(myStudy,entry)
    if iorString != None:
        ior = orb.string_to_object(iorString)
    return ior

def entryToIorString(myStudy,entry):
    """
    Retourne la sérialisation de l'ior de l'entry passée en
    argument. Il s'agit de l'attribut AttributeIOR associé à l'entry
    dans l'arbre d'étude.
    """
    myBuilder = myStudy.NewBuilder()
    iorString = None
    SO = None
    try:
        SO = myStudy.FindObjectID(entry)
    except:
        print "invalid entry: ",entry
        SO = None
    if SO != None:
        boo,iorso = myBuilder.FindAttribute(SO,"AttributeIOR")
        if boo == 0:
            print "no IOR attribute on study object: ", entry
        else:
            iorString = iorso.Value()
    return iorString


    #--------------------------------------------------------------------------

def singleEntryToName(myStudy,entry):
    """
    Retourne le nom l'entry passée en argument. Il s'agit de
    l'attribut AttributeName associé à l'entry dans l'arbre d'étude.
    """
    myBuilder = myStudy.NewBuilder()
    name =[] 
    SO = None
    try:
            SO = myStudy.FindObjectID(entry)
    except:
            print "invalid entry: ",entry
            SO = None
    if SO != None:
            boo,nameso = myBuilder.FindAttribute(SO,"AttributeName")
            if boo == 0:
                print "no Name attribute on study object: ", entry
            else:
                name.append(nameso.Value())
    return name

def entryListToName(myStudy,entryList):
    """
    Récupération de la liste des noms à partir d'une liste d'entry.
    """
    myBuilder = myStudy.NewBuilder()
    name =[]
    SO = None
    for entry in entryList:
        try:
            SO = myStudy.FindObjectID(entry)
        except:
            print "invalid entry: ",entry
            SO = None
        if SO != None:
            boo,nameso = myBuilder.FindAttribute(SO,"AttributeName")
            if boo == 0:
                print "no Name attribute on study object: ", entry
            else:
                name.append(nameso.Value())
    return name

def entryToName(myStudy,entryList):
    """
    Cette méthode sert juste à assurer la compatibilité avec le
    logiciel Eficas. Eficas (panelsSalome.py) fait appel à entryToList
    en passant une entryList en argument.
    """
    return entryListToName(myStudy,entryList)


    #--------------------------------------------------------------------------
def getMainShape(anObject):
    """
    Cette méthode retourne une référence ior de l'objet principal qui
    contient l'entry passée en argument.
    """
    try :
       subShape=anObject._narrow(GEOM.GEOM_Object)
       objMain = subShape.GetMainShape()
       IORobjMain = orb.object_to_string(objMain)
    except :
       IORobjMain= None
    return IORobjMain

def getShapeContenante(myStudy,entry):
    try :
       anObject=entryToIor(myStudy,entry)
       Shape=anObject._narrow(GEOM.GEOM_Object)
       ShapeIor=orb.object_to_string(Shape)
    except :
       print "pb avec l IOR: pas un objet"
       return None

    MainShapeIOR=ShapeIor
    while anObject != None :
       iorStringMain = getMainShape(anObject) 
       if iorStringMain == None :
          break
       if ( MainShapeIOR != iorStringMain ):
          anObject =  orb.string_to_object(iorStringMain)
          if anObject :
             MainShapeIOR=iorStringMain
       else : 
          anObject = None
          
    return MainShapeIOR 

    #--------------------------------------------------------------------------

def getSMESHSubShapeIndexes(myStudy, entryList, typenoeudorcell = 0):
    # typenoeudorcell = 0 on traite des noeuds
    # typenoeudorcell = 1 on traite des faces

    refList = []
    iorStringMain = None
    myCLinit=CLinit()

    if len(entryList) > 0:
      for idShape in entryList:
	try:
           anObject=entryToIor(myStudy,idShape)
           Shape=anObject._narrow(GEOM.GEOM_Object)
           iorStringMain=orb.object_to_string(Shape)
        except :
           print "pb avec l IOR: pas un objet"

        if iorStringMain == None:
          # C'est le cas ou on a loade un fichier hdf et on est pas passe par geom
          # par exemple ....
          return refList
    
        myCL=myCLinit.GetOrCreateCL(iorStringMain)
        refShape = singleEntryToName(myStudy,idShape)
        if refShape != None:
           for Shape in refShape:
               refList.append(Shape)
        IORShape = entryToIor(myStudy,idShape)
        myCL.SetIdAsCL(orb.object_to_string(IORShape),typenoeudorcell)
            
    return refList

    #--------------------------------------------------------------------------

def getAsterGroupNo(myStudy,entryList):
    typenoeudorcell = 0
    subShapeIndexes = getSMESHSubShapeIndexes(myStudy, entryList,typenoeudorcell)
    labelGroupNo = []
    if subShapeIndexes == None :
       print "*************************************"
       print "Pb au chargement de Geom --> pas d IOR"
       print "*************************************"
       return
    for val in subShapeIndexes:
        labelGroupNo.append(val)
    return labelGroupNo

    #--------------------------------------------------------------------------

def getAsterGroupMa(myStudy,entryList):
    typenoeudorcell = 1
    subShapeIndexes = getSMESHSubShapeIndexes(myStudy, entryList,typenoeudorcell)
    labelGroupMa = []
    if subShapeIndexes == None :
       print "*************************************"
       print "Pb au chargement de Geom --> pas d IOR"
       print "*************************************"
       return
    for val in subShapeIndexes:
        labelGroupMa.append(val)
    return labelGroupMa

    #--------------------------------------------------------------------------

def VisuGroupe(myStudy,GroupesListe):
    import salomedsgui
    aGuiDS=salomedsgui.guiDS()
    aGuiDS.ClearSelection()
    aGuiDS.DisplayByNameInGeom(GroupesListe)

