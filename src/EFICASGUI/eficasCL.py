import salome
import SALOMEDS
import SMESH
import SalomePyQt
import MonChoixMaillage

Tag_RefOnShape = 1
dict_CL={}

class CLinit:
    def __init__(self):
       self.smesh=None
       self._d = SalomePyQt.SalomePyQt().getDesktop()
       self.get_maillages()
       self.listeDejaTraites= []
       self.Liste_Shape = {}
       self.correspondanceNomIOR = {}
       self.name="CL"

    def GetOrCreateCL(self,myShapeName):
       if not (dict_CL.has_key(myShapeName)):
          dict_CL[myShapeName] = CL()
       return dict_CL[myShapeName]

    def chercheAtraiter(self):
        atraiter=-1
	curseur=0
	print dict_CL.keys()
	print self.listeDejaTraites
	while curseur < len(dict_CL):
       	   GEOMIor=self.Liste_Shape[curseur]
	   if GEOMIor not in self.listeDejaTraites:
	      atraiter=curseur
	      break
	   curseur=curseur+1
	return atraiter

    def traiteCL(self):
       # Récupere tous les Mesh
       if self.Liste_Shape == {}:
          self.Liste_Shape = dict_CL.keys()
       atraiter=self.chercheAtraiter()
       if atraiter >= 0:
          Choix=MonChoixMaillage.MonChoixMaillage(self,atraiter,self._d)
       salome.sg.updateObjBrowser(0)

    def traiteMaillage(self,indiceIOR,NomMaillage):
       MeshIOR = self.correspondanceNomIOR[str(NomMaillage)]
       Mesh = salome.orb.string_to_object(MeshIOR)
       GEOMIor =self.Liste_Shape[indiceIOR]
       for monIOR in dict_CL[GEOMIor].CLOnNode.keys():
       	   GEOMShape = salome.orb.string_to_object(monIOR)
           aShapeSO = salome.myStudy.FindObjectIOR(monIOR)
           attrName  = aShapeSO.FindAttribute("AttributeName")[1]
       	   anAttr = attrName._narrow(SALOMEDS.AttributeName)
           Name = anAttr.Value()
           Mesh.CreateGroupFromGEOM(SMESH.NODE,Name,GEOMShape)
       for monIOR in dict_CL[GEOMIor].CLOnCell.keys():
       	   GEOMShape = salome.orb.string_to_object(monIOR)
           aShapeSO = salome.myStudy.FindObjectIOR(monIOR)
           attrName  = aShapeSO.FindAttribute("AttributeName")[1]
       	   anAttr = attrName._narrow(SALOMEDS.AttributeName)
           Name = anAttr.Value()
           Mesh.CreateGroupFromGEOM(SMESH.FACE,Name,GEOMShape)
       self.listeDejaTraites.append(GEOMIor)
           

    def traiteNewMaillage(self,indiceIOR,NomMaillage):
       GEOMIor =self.Liste_Shape[indiceIOR]
       print GEOMIor
       print dict_CL[GEOMIor].CLOnNode.keys()
       print dict_CL[GEOMIor].CLOnCell.keys()
       shape = salome.orb.string_to_object(GEOMIor)
       if self.smesh == None :
         self.smesh = salome.lcc.FindOrLoadComponent("FactoryServer", "SMESH")
	 self.smesh.SetCurrentStudy(salome.myStudy)
       assert (self.smesh)
       newMesh  = self.smesh.CreateMesh(shape)
       self.SetName(salome.ObjectToID(newMesh),NomMaillage)
       for monIOR in dict_CL[GEOMIor].CLOnNode.keys():
           GEOMShape = salome.orb.string_to_object(monIOR)
	   aShapeSO = salome.myStudy.FindObjectIOR(monIOR)
	   attrName  = aShapeSO.FindAttribute("AttributeName")[1]
	   anAttr = attrName._narrow(SALOMEDS.AttributeName)
	   Name = anAttr.Value()
	   newMesh.CreateGroupFromGEOM(SMESH.NODE,Name,GEOMShape)
       for monIOR in dict_CL[GEOMIor].CLOnCell.keys():
       	   GEOMShape = salome.orb.string_to_object(monIOR)
           aShapeSO = salome.myStudy.FindObjectIOR(monIOR)
           attrName  = aShapeSO.FindAttribute("AttributeName")[1]
       	   anAttr = attrName._narrow(SALOMEDS.AttributeName)
           Name = anAttr.Value()
           newMesh.CreateGroupFromGEOM(SMESH.FACE,Name,GEOMShape)
       self.listeDejaTraites.append(GEOMIor)

    def NomShape(self,numero):
       GEOMIor=self.Liste_Shape[numero]
       aShapeSO = salome.myStudy.FindObjectIOR(GEOMIor)
       attrName  = aShapeSO.FindAttribute("AttributeName")[1]
       anAttr = attrName._narrow(SALOMEDS.AttributeName)
       Name = anAttr.Value()
       return Name

# NodeorCell = 0 on traite des noeuds
# NodeorCell = 1 on traite des mailles

    def Possibles(self,numero):
       GEOMIor=self.Liste_Shape[numero]
       liste=[]
       for MeshIor in self.Liste_maillages[GEOMIor]:
	   aMeshSO = salome.myStudy.FindObjectIOR(MeshIor)
           attrName  = aMeshSO.FindAttribute("AttributeName")[1]
           anAttr = attrName._narrow(SALOMEDS.AttributeName)
           Name = anAttr.Value()
	   self.correspondanceNomIOR[Name] = MeshIor
           liste.append(Name)
       return liste

    def get_maillages(self):
       self.Liste_maillages={}
       if self.smesh == None :
         self.smesh = salome.lcc.FindOrLoadComponent("FactoryServer", "SMESH")
	 self.smesh.SetCurrentStudy(salome.myStudy)
       stringIOR=salome.orb.object_to_string(self.smesh)
       SO_smesh=salome.myStudy.FindObjectIOR(stringIOR)
       if SO_smesh != None:
         ChildIterator = salome.myStudy.NewChildIterator(SO_smesh)
	 while ChildIterator.More() :
	    aSObj = ChildIterator.Value()
	    ChildIterator.Next()
	    anAttr =aSObj.FindAttribute("AttributeName")[1]
	    anAttr = anAttr._narrow(SALOMEDS.AttributeName)
	    Name = anAttr.Value()
            if (Name != "Hypotheses" and Name != "Algorithms"):
	       res, Ref = aSObj.FindSubObject( Tag_RefOnShape )
	       if res == 1 :
	          ok,MyShapeSO = Ref.ReferencedObject()
		  if ok :
	            IORAttr = MyShapeSO.FindAttribute("AttributeIOR")[1]
	            anAttr  = IORAttr._narrow(SALOMEDS.AttributeIOR)
	            GEOMShapeIOR  = anAttr.Value()

	            IORAttr2 = aSObj.FindAttribute("AttributeIOR")[1]
	            anAttr2  = IORAttr2._narrow(SALOMEDS.AttributeIOR)
	            MeshIOR  = anAttr2.Value()

	            if GEOMShapeIOR in self.Liste_maillages.keys():
		     self.Liste_maillages[GEOMShapeIOR].append(MeshIOR)
		    else :
		     self.Liste_maillages[GEOMShapeIOR]=[MeshIOR]

    def SetName(self,Entry, Name):
       SO = salome.myStudy.FindObjectID( Entry )
       if SO != None :
	  myStudyBuilder = salome.myStudy.NewBuilder()
	  aName = myStudyBuilder.FindOrCreateAttribute(SO, "AttributeName")
	  aName.SetValue(Name)

class CL:

   def __init__(self):
      self.CLOnCell={}
      self.CLOnNode={}

# nodeOrCell = 0 on traite des noeuds
# nodeOrCell = 1 on traite des faces

   def SetIdAsCL(self,CLName,nodeOrCell):
      if (nodeOrCell == 0) :
          if self.CLOnNode.has_key(CLName):
	     self.CLOnNode[CLName] = self.CLOnNode[CLName] + 1
	  else :
	     self.CLOnNode[CLName] = 1
      if (nodeOrCell == 1) :
          if self.CLOnCell.has_key(CLName):
	     self.CLOnCell[CLName] = self.CLOnCell[CLName] + 1
	  else :
	     self.CLOnCell[CLName] = 1

   def UnSetIdAsCL(self,CLName,nodeOrCell):
      if (nodeOrCell == 0) :
          if self.CLOnNode.has_key(CLName):
	     self.CLOnNode[CLName] = self.CLOnNode[CLName] - 1
      if (nodeOrCell == 1) :
          if self.CLOnCell.has_key(CLName):
	     self.CLOnCell[CLName] = self.CLOnCell[CLName] - 1


