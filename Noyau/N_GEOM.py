"""

"""
from N_ASSD import ASSD

class GEOM(ASSD):
   """
      Cette classe sert à définir les types de concepts
      géométriques comme GROUP_NO, GROUP_MA,NOEUD et MAILLE

   """
   def __init__(self,nom,etape=None,sd=None,reg='oui'):
      """
      """
      self.etape=etape
      self.sd=sd
      if etape:
        self.parent=etape.parent
      else:
        self.parent=CONTEXT.get_current_step()
      if self.parent :
         self.jdc = self.parent.get_jdc_root()
      else:
         self.jdc = None

      if not self.parent:
        self.id=None
      elif reg == 'oui' :
        self.id = self.parent.reg_sd(self)
      self.nom=nom

   def get_name(self):
      return self.nom

   def is_object(valeur):
      """
          Indique si valeur est d'un type conforme à la classe (1) 
          ou non conforme (0)
          La classe GEOM est utilisée pour tous les objets géométriques
          Elle valide tout objet
      """
      return 1


class geom(GEOM):pass

