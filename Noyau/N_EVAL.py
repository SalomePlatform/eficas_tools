"""
"""

class EVAL :
   """
   """
   def __init__(self,str):
      """
         L'objet EVAL est initialise avec une chaine de caracteres (str)
      """
      self.valeur = str
      self.val=None

   def __repr__(self):
      return 'EVAL("""'+self.valeur+'""")'

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitEVAL(self)

