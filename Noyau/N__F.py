import UserDict

class _F(UserDict.UserDict):
   """
       Cette classe a un comportement semblable à un 
       dictionnaire Python et permet de donner
       la valeur d'un mot-clé facteur avec pour les sous 
       mots-clés la syntaxe motcle=valeur
   """

   def __init__(self,**args):
      self.data=args

   def supprime(self):
      self.data={}

   def __cmp__(self, dict):
      if type(dict) == type(self.data):
        return cmp(self.data, dict)
      elif hasattr(dict,"data"):
        return cmp(self.data, dict.data)
      else:
        return cmp(self.data, dict)

   def copy(self):
      import copy
      c= copy.copy(self)
      c.data=self.data.copy()
      return c


   
