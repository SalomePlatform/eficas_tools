
import salome
import salomedsgui
aGuiDS=salomedsgui.guiDS()

# -----------------------------------------------------------------------------

import ChoixMaillage


class MonChoixMaillage(ChoixMaillage.ChoixMaillage):
   """
   adaptation de la classe  generee par pyuic.
   """
   def  __init__(self,CL,monNum,parent = None,name = None,modal = 0,fl = 0,):
      ChoixMaillage.ChoixMaillage.__init__(self,parent,name,modal,fl)
      self._CL=CL
      self._numero=monNum
      self.recupere_info()

      self.NomShape.setText(self._nomShape)
      for item in self._listeMesh:
          self.Maillage.insertItem(item)
      self.show()

   def recupere_info(self):
      self._nomShape  = self._CL.NomShape(self._numero)
      self._listeMesh= self._CL.Possibles(self._numero)

   def Maillage_clicked(self,item) :
      self._CL.traiteMaillage(self._numero,item.text())
      self._CL.traiteCL()
      self.close()


   def NouveauMesh_returnPressed(self):
      self._CL.traiteNewMaillage(self._numero,str(self.NouveauMesh.text()))
      self._CL.traiteCL()
      self.close()

