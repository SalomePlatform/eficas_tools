""" 
    Ce module contient la classe MCSIMP qui sert à controler la valeur
    d'un mot-clé simple par rapport à sa définition portée par un objet
    de type ENTITE
"""

import N_OBJECT

class MCSIMP(N_OBJECT.OBJECT):
   """
   """
   nature = 'MCSIMP'
   def __init__(self,val,definition,nom,parent):
      """
         Attributs :

          - val : valeur du mot clé simple

          - definition

          - nom

          - parent

        Autres attributs :

          - valeur : valeur du mot-clé simple en tenant compte de la valeur par défaut

      """
      self.definition=definition
      self.nom=nom
      self.val = val
      self.parent = parent
      self.valeur = self.GETVAL(self.val)
      if parent :
         self.jdc = self.parent.jdc
         self.niveau = self.parent.niveau
         self.etape = self.parent.etape
      else:
         # Le mot cle simple a été créé sans parent
         self.jdc = None
         self.niveau = None
         self.etape = None
         
   def GETVAL(self,val):
      """ 
          Retourne la valeur effective du mot-clé en fonction
          de la valeur donnée. Defaut si val == None
      """
      if (val is None and hasattr(self.definition,'defaut')) :
        return self.definition.defaut
      else:
        return val

   def get_valeur(self):
      """
          Retourne la "valeur" d'un mot-clé simple.
          Cette valeur est utilisée lors de la création d'un contexte 
          d'évaluation d'expressions à l'aide d'un interpréteur Python
      """
      return self.valeur

   def get_val(self):
      """
          Une autre méthode qui retourne une "autre" valeur du mot clé simple.
          Elle est utilisée par la méthode get_mocle
      """
      return self.valeur

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitMCSIMP(self)

