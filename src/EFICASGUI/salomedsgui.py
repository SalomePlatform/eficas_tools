#  Copyright (C) 2003  OPEN CASCADE, EADS/CCR, LIP6, CEA/DEN,
#  CEDRAT, EDF R&D, LEG, PRINCIPIA R&D, BUREAU VERITAS 
# 
#  This library is free software; you can redistribute it and/or 
#  modify it under the terms of the GNU Lesser General Public 
#  License as published by the Free Software Foundation; either 
#  version 2.1 of the License. 
# 
#  This library is distributed in the hope that it will be useful, 
#  but WITHOUT ANY WARRANTY; without even the implied warranty of 
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
#  Lesser General Public License for more details. 
# 
#  You should have received a copy of the GNU Lesser General Public 
#  License along with this library; if not, write to the Free Software 
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA 
# 
#  See http://www.opencascade.org/SALOME/ or email : webmaster.salome@opencascade.org 
#
#
#
#  File   : salomedsgui.py
#  Author : Paul RASCLE, EDF
#  Module : KERNEL
#
#--------------------------------------------------------------------------

import salome
import SALOMEDS
import string,os

class guiDS:
    """
    Study (SALOMEDS) interface from python gui (ex: IAPP embedded PyQt GUI)
    """
    _myStudyManager = None
    _myStudy = None
    _myBuilder = None
    _father = None
    _component = None

    def __init__(self):
        self._myStudyManager = salome.myStudyManager
        self._myStudy = salome.myStudy
        self._myBuilder = self._myStudy.NewBuilder()

    def enregistre(self,myModule):
        if self._father is None:
            father = self._myStudy.FindComponent(myModule)
            if father is None:
                father = self._myBuilder.NewComponent(myModule)
                A1 = self._myBuilder.FindOrCreateAttribute(father,"AttributeName")
                FName = A1._narrow(SALOMEDS.AttributeName)
                FName.SetValue(myModule)
            self._father   = father
            self._component = myModule
        return self._father.GetID()

    def createItemInStudy(self,fatherId,objectName):
        objId = None
        if self._component is not None:
            listSO = self._myStudy.FindObjectByName(objectName,self._component)
            if len(listSO) == 0:
                father = self._myStudy.FindObjectID(fatherId)
                newObj = self._myBuilder.NewObject(father)
                A1= self._myBuilder.FindOrCreateAttribute(newObj,"AttributeName")
                FName = A1._narrow(SALOMEDS.AttributeName)
                FName.SetValue(objectName)
                objId = newObj.GetID()
	    else:
	        objId = listSO[0].GetID()
        return objId

    def getReference(self,objectId):
        mySO = self._myStudy.FindObjectID(objectId)
        boo,RefSO = mySO.ReferencedObject()
        if boo:
            objectId=RefSO.GetID()
        return objectId        

    def addReference(self,fatherId,refId):
        father = self._myStudy.FindObjectID(fatherId)
        ref = self._myStudy.FindObjectID(refId)
        newObj = self._myBuilder.NewObject(father)
	A1 =  self._myBuilder.FindOrCreateAttribute(ref,"AttributeName")
	FName = A1._narrow(SALOMEDS.AttributeName)
	Name_ref = FName.Value()
	path_father , none = string.split(self._myStudy.GetObjectPath(ref),Name_ref)
	path_father , none = os.path.split(path_father)
	#print "salomedsgui::addReference : path_father_ref = ",path_father
	#print "salomedsgui::addReference : Path_father = ",self._myStudy.GetObjectPath(father)
	if self._myStudy.GetObjectPath(father) != path_father :
            self._myBuilder.Addreference(newObj,ref)

    def setExternalFileAttribute(self,objectId,filetype,filename):
        mySO = self._myStudy.FindObjectID(objectId)
        A1 = self._myBuilder.FindOrCreateAttribute(mySO,"AttributeExternalFileDef")
        AFileName = A1._narrow(SALOMEDS.AttributeExternalFileDef)
        AFileName.SetValue(filename)
        print filename
        A2 = self._myBuilder.FindOrCreateAttribute(mySO,"AttributeFileType")
        AFileType = A2._narrow(SALOMEDS.AttributeFileType)
        print filetype
        AFileType.SetValue(filetype)
        print filetype
                          
    def getExternalFileAttribute(self,filetype, objectId):
        print filetype
        print objectId
        mySO = self._myStudy.FindObjectID(objectId)
        boo,RefSO = mySO.ReferencedObject()
        if boo:
            print RefSO
            mySO = RefSO
        print mySO
        val=""
        boo,attr =  self._myBuilder.FindAttribute(mySO,"AttributeFileType")
        print "AttributeFileType ",boo
        if boo:
            boo=0
            val=attr.Value()
            print val
        if val==filetype:
            boo,attr =  self._myBuilder.FindAttribute(mySO,"AttributeExternalFileDef")
        val=""
        if boo: 
             val=attr.Value()
        attribute=val
        return (boo,attribute)

    def getNameAttribute(self, objectId):
        mySO = self._myStudy.FindObjectID(objectId)
        boo,RefSO = mySO.ReferencedObject()
        if boo:
            mySO = RefSO
        boo,attr =  self._myBuilder.FindAttribute(mySO,"AttributeName")
        val=""
        if boo:
            val=attr.Value()
            print val
        return val
            
    def getTypeAttribute(self, objectId):
        mySO = self._myStudy.FindObjectID(objectId)
        boo,RefSO = mySO.ReferencedObject()
        if boo:
            mySO = RefSO
        boo,attr =  self._myBuilder.FindAttribute(mySO,"AttributeFileType")
        val=""
        if boo:
            val=attr.Value()
        return val

    def getChildren(self, objectId):
        children=[]
        mySO = self._myStudy.FindObjectID(objectId)
        boo,RefSO = mySO.ReferencedObject()
        if boo:
            mySO = RefSO
        it = self._myStudy.NewChildIterator(mySO)
        while it.More():
            CSO = it.Value()
            children.append(CSO.GetID())
            it.Next()
        print children
        return children
