""" 
    Ce module contient la classe OBJECT classe mère de tous les objets
    servant à controler les valeurs par rapport aux définitions
"""

class OBJECT:
   """
      Classe OBJECT : cette classe est virtuelle et sert de classe mère
      aux classes de type ETAPE et MOCLES.
      Elle ne peut etre instanciée.
      Une sous classe doit obligatoirement implémenter les méthodes :

      - __init__

   """

   def get_etape(self):
      """
         Retourne l'étape à laquelle appartient self
         Un objet de la catégorie etape doit retourner self pour indiquer que
         l'étape a été trouvée
         XXX double emploi avec self.etape ???
      """
      if self.parent == None: return None
      return self.parent.get_etape()

   def supprime(self):
      """ 
         Méthode qui supprime les références arrières suffisantes pour
         que l'objet puisse être correctement détruit par le 
         garbage collector
      """
      self.parent = None
      self.etape = None
      self.jdc = None
      self.niveau = None

   def get_val(self):
      """
          Retourne la valeur de l'objet. Cette méthode fournit
          une valeur par defaut. Elle doit etre dérivée pour chaque 
          type d'objet
      """
      return self

   def isBLOC(self):
      """
          Indique si l'objet est un BLOC
      """
      return 0

   def get_jdc_root(self):
      """
          Cette méthode doit retourner l'objet racine c'est à dire celui qui
          n'a pas de parent
      """
      if self.parent:
         return self.parent.get_jdc_root()
      else:
         return self

   def GETVAL(self,val):
      """
          Retourne la valeur effective du mot-clé en fonction
          de la valeur donnée. Defaut si val == None
      """
      if (val is None and hasattr(self.definition,'defaut')) :
        return self.definition.defaut
      else:
        return val

