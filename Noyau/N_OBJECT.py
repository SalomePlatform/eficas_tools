""" 
    Ce module contient la classe OBJECT classe m�re de tous les objets
    servant � controler les valeurs par rapport aux d�finitions
"""

class OBJECT:
   """
      Classe OBJECT : cette classe est virtuelle et sert de classe m�re
      aux classes de type ETAPE et MOCLES.
      Elle ne peut etre instanci�e.
      Une sous classe doit obligatoirement impl�menter les m�thodes :

      - __init__

   """

   def get_etape(self):
      """
         Retourne l'�tape � laquelle appartient self
         Un objet de la cat�gorie etape doit retourner self pour indiquer que
         l'�tape a �t� trouv�e
         XXX double emploi avec self.etape ???
      """
      if self.parent == None: return None
      return self.parent.get_etape()

   def supprime(self):
      """ 
         M�thode qui supprime les r�f�rences arri�res suffisantes pour
         que l'objet puisse �tre correctement d�truit par le 
         garbage collector
      """
      self.parent = None
      self.etape = None
      self.jdc = None
      self.niveau = None

   def get_val(self):
      """
          Retourne la valeur de l'objet. Cette m�thode fournit
          une valeur par defaut. Elle doit etre d�riv�e pour chaque 
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
          Cette m�thode doit retourner l'objet racine c'est � dire celui qui
          n'a pas de parent
      """
      if self.parent:
         return self.parent.get_jdc_root()
      else:
         return self

   def GETVAL(self,val):
      """
          Retourne la valeur effective du mot-cl� en fonction
          de la valeur donn�e. Defaut si val == None
      """
      if (val is None and hasattr(self.definition,'defaut')) :
        return self.definition.defaut
      else:
        return val

