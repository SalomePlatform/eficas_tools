#=============================================================================
# File      : SMESH_utils.py
# Created   : jeu f�v 20 18:53:34 CET 2003
# Author    : Paul RASCLE, EDF
# Project   : SALOME
# Copyright : EDF 2003
#  $Header: /home/salome/PlateFormePAL/Bases_CVS_EDF/Modules_EDF/ASTER_SRC/src/ASTER/SMESH_utils.py,v 1.1.1.1.2.1 2004/05/18 11:40:20 salome Exp $
#=============================================================================

from omniORB import CORBA
import LifeCycleCORBA
import SALOMEDS
import GEOM
import SMESH

# initialise the ORB
orb = CORBA.ORB_init([''], CORBA.ORB_ID)

# create an LifeCycleCORBA instance
lcc = LifeCycleCORBA.LifeCycleCORBA(orb)

geom = lcc.FindOrLoadComponent("FactoryServer", "GEOM")
smesh = lcc.FindOrLoadComponent("FactoryServer", "SMESH")

    #--------------------------------------------------------------------------

def entryToIor(myStudy,entry):
    myBuilder = myStudy.NewBuilder()
    ior = None
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
            print iorString
            ior = orb.string_to_object(iorString)
    return ior

    #--------------------------------------------------------------------------

def entryToName2(myStudy,entry):
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

def entryToName(myStudy,entryList):
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


    #--------------------------------------------------------------------------

def getMainShape(myStudy,entry):
    anObject=entryToIor(myStudy,entry)
    subShape=anObject._narrow(GEOM.GEOM_Shape)
    if subShape == None:
        print "entry does not give a shape: ", entry
        return None
    isMain=subShape._get_IsMainShape()
    if isMain:
        iorMain=subShape
    else:
        iorStringMain=subShape._get_MainName()
        iorMain = orb.string_to_object(iorStringMain)
    return iorMain
        

def getMainShapeName(myStudy,entry):
    anObject=entryToIor(myStudy,entry)
    subShape=anObject._narrow(GEOM.GEOM_Shape)
    if subShape == None:
        print "entry does not give a shape: ", entry
        return None
    isMain=subShape._get_IsMainShape()
    if isMain:
        iorMain=subShape
    else:
        iorStringMain=subShape._get_MainName()
        iorMain = orb.string_to_object(iorStringMain)
    stringior=  orb.object_to_string(iorMain)
    return stringior
    #--------------------------------------------------------------------------

def getSMESHSubShapeIndexes(myStudy, entryList, typenoeudorcell = 0):
    # typenoeudorcell = 0 on traite des noeuds
    # typenoeudorcell = 1 on traite des faces
    refList = []
    subShapeIndexes = []
    if len(entryList) > 0:
        iorMain = getMainShapeName(myStudy, entryList[0])

    myCL=smesh.GetOrCreateCL(str(iorMain))

    if len(entryList) > 0:
         for idShape in entryList:
             print "idShape"
             print idShape
             refShape = entryToName2(myStudy,idShape)
             if refShape != None:
                  for Shape in refShape:
                      refList.append(Shape)
             IORShape = entryToIor(myStudy,idShape)
             myCL.SetIdAsCL(orb.object_to_string(IORShape),typenoeudorcell)
            
    studyId = myStudy._get_StudyId()
    return refList

    #--------------------------------------------------------------------------

def getAsterGroupNo(myStudy,entryList):
    typenoeudorcell = 0
    subShapeIndexes = getSMESHSubShapeIndexes(myStudy, entryList,typenoeudorcell)
    labelGroupNo = []
    for val in subShapeIndexes:
        labelGroupNo.append(val)
    return labelGroupNo

    #--------------------------------------------------------------------------

def getAsterGroupMa(myStudy,entryList):
    typenoeudorcell = 1
    subShapeIndexes = getSMESHSubShapeIndexes(myStudy, entryList,typenoeudorcell)
    labelGroupMa = []
    for val in subShapeIndexes:
        #label="GMM%d"%(val)
        labelGroupMa.append(val)
    print labelGroupMa
    return labelGroupMa

    #--------------------------------------------------------------------------

