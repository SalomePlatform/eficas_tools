#!/usr/bin/env python

import pilot
import SALOMERuntime
import loader
import logging
import traceback
import os

class CreeSchemaYacs :
     def __init__(self,config):
        print "dans le init de CreeSchemaYacs " 
        self.config=config
        self.ssCode=config.appli.ssCode
        self.setUp()
        self.addCatalog()
        self.nodeAvant=None

     def setUp(self):
        SALOMERuntime.RuntimeSALOME_setRuntime()
        self.runtime = pilot.getRuntime()
        self.loader  = loader.YACSLoader()
        self.loader.registerProcCataLoader()

     def addCatalog(self):
        try:
           monCataFile= os.environ["EFICAS_ROOT_DIR"]
           monCataFile=monCataFile+"/share/salome/resources/eficas/cata"
           monCataFile=monCataFile+self.ssCode+".xml"
           print monCataFile
           self.monCata = self.runtime.loadCatalog("proc",monCataFile)
        except:
           logging.fatal("Exception in loading MAP catalog")
           traceback.print_exc()
           sys.exit(1)

     def createProc(self):
        proc = self.runtime.createProc("proc")
        proc.setTypeCode("pyobj", self.runtime.getTypeCode("pyobj"))
        t_pyobj  = proc.getTypeCode("pyobj")
        t_string = proc.getTypeCode("string")
        return proc

     def write_yacs_proc(self,proc, yacs_schema_filename):
         proc.saveSchema(yacs_schema_filename)

class s_poly_st_1(CreeSchemaYacs) :

     def BENHURYACS(self,proc,dico):
         monFichierInput=self.config.PATH_BENHUR+"/BHR_files.txt"
         factoryNode = self.monCata._nodeMap["benhur"]
         self.benhurNode = factoryNode.cloneNode("benhur")
         self.benhurNode.getInputPort("fileInput").edInitPy(monFichierInput)
         self.benhurNode.getInputPort("pathBenhur").edInitPy(self.config.PATH_BENHUR)
         proc.edAddChild(self.benhurNode)
         if self.nodeAvant != None :
            proc.edAddCFLink(self.nodeAvant,self.benhurNode)
         self.nodeAvant=self.benhurNode

     def PYGMEEYACS(self,proc,dico):
         monFichierInput=self.config.PATH_STUDY+"/"+self.config.NAME_SCHEME+"/pygmee_input.txt"
         factoryNode = self.monCata._nodeMap["pygmee"]
         self.pygmeeNode = factoryNode.cloneNode("pygmee")
         self.pygmeeNode.getInputPort("pathPygmee").edInitPy(self.config.PATH_PYGMEE)
         self. pygmeeNode.getInputPort("fileInput").edInitPy(monFichierInput)
         proc.edAddChild(self.pygmeeNode)
         if self.nodeAvant != None :
            proc.edAddCFLink(self.nodeAvant,self.pygmeeNode)
         self.nodeAvant=self.pygmeeNode

     def ASTERYACS(self,proc,dico):
         factoryNode = self.monCata._nodeMap["asterRun"]
         self.asterNode = factoryNode.cloneNode("asterRun")
         nom_racine=self.config.PATH_STUDY+"/"+self.config.NAME_SCHEME+"/"
         monFichierExport=nom_racine+"s_poly_st_1_aster.export"
         monFichierMed=nom_racine+"s_poly_st_1_aster.resu.med"
         self.asterNode.getInputPort("pathAster").edInitPy(self.config.PATH_ASTER+"/bin")
         self.asterNode.getInputPort("fileExport").edInitPy(monFichierExport)
         self.asterNode.getInputPort("fileMed").edInitPy(monFichierMed)

         proc.edAddChild(self.asterNode)
         if self.nodeAvant != None :
            proc.edAddCFLink(self.nodeAvant,self.asterNode)
         self.nodeAvant=self.asterNode

dictKlass={'s_poly_st_1':s_poly_st_1}
def getSchema(config):
     schema=config.appli.ssCode
     return dictKlass[schema](config)


if __name__ == "__main__":
     monCreator=getSchema('s_poly_st_1')
     proc=monCreator.createProc()
     monCreator.ajoutPygmee(proc)
     monCreator.ajoutBenhur(proc)
     monCreator.write_yacs_proc(proc,"/tmp/toto.xml")
     
