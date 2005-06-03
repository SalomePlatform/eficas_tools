
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
      self._GeomChoisie=None

      self.NomShape.setText(self._CL.NomShape(self._numero))
      self.recupere_mainId()
      self.show()

   def Geometrie_clicked(self,item):
       self.Maillage.clear()
       if item == None :
          return
       self._GeomChoisie=item.text()
       self._listeMesh= self._CL.Possibles(self._numero,self._GeomChoisie)
       for item in self._listeMesh:
           self.Maillage.insertItem(item)

   def recupere_mainId(self):
      self._listeGeom= self._CL.MainShapes(self._numero)
      self.MainShape.clear()
      for item in self._listeGeom :
          self.MainShape.insertItem(item)

   def Maillage_clicked(self,item) :
      if item == None :
         return
      self._CL.traiteMaillage(self._numero,item.text())
      self._CL.traiteCL()
      self.close()


   def NouveauMesh_returnPressed(self):
      self._CL.traiteNewMaillage(self._numero,self._GeomChoisie,str(self.NouveauMesh.text()))
      self._CL.traiteCL()
      self.close()

