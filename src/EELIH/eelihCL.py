import salome
import eficasCL

Tag_RefOnShape = 1
dict_CL={}

class CLinit(eficasCL.CLinit):
    def traiteCL(self):
       self.get_geoms()
       self.get_maillages()
       salome.sg.updateObjBrowser(0)
