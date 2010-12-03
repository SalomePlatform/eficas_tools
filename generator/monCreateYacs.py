#!/usr/bin/env python


import sys, os
sys.path.append(os.path.join(os.getenv('YACS_ROOT_DIR'),'lib/python2.5/site-packages/salome/'))

import pilot
import SALOMERuntime
import loader
import logging
import traceback

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
           # modifs CTL 20101121 : generic scheme template name
           monCataFile=self.config.INSTALLDIR+"/MAP/Templates/"
           monCataFile+=self.config.ssCode
           monCataFile+="/cata_"+self.config.ssCode+".xml"
           print 'YACS xml scheme template :', monCataFile
           self.monCata = self.runtime.loadCatalog("proc",monCataFile)
        except:
           logging.fatal("Exception in loading MAP catalog")
           traceback.print_exc()
           sys.exit(1)

     def createProc(self, generator):
        self.generator=generator
        proc = self.runtime.createProc("proc")
        proc.setTypeCode("pyobj", self.runtime.getTypeCode("pyobj"))
        t_pyobj  = proc.getTypeCode("pyobj")
        t_string = proc.getTypeCode("string")
        return proc

     def write_yacs_proc(self,proc, yacs_schema_filename):
         proc.saveSchema(yacs_schema_filename)

# pour l instant on garde cette classe 
# pour pouvoir specialiser si necessaire
# pour d autres schema
class s_polymers_st_1(CreeSchemaYacs) :
     def METHODEYACS(self,proc,dico):
         self.generator.METHODEYACS(self,proc)
         
dictKlass={'s_polymers_st_1':s_polymers_st_1}
def getSchema(config):
     schema=config.appli.ssCode
     return dictKlass[schema](config)


if __name__ == "__main__":
     monCreator=getSchema('s_polymers_st_1')
     proc=monCreator.createProc()
     monCreator.ajoutPygmee(proc)
     monCreator.ajoutBenhur(proc)
     monCreator.write_yacs_proc(proc,"/tmp/toto.xml")
     
