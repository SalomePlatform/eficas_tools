import I_MCCOMPO
class MCFACT(I_MCCOMPO.MCCOMPO):
  def isrepetable(self):
     """ 
         Indique si l'objet est répétable.
         Retourne 1 si le mot-clé facteur self peut être répété
         Retourne 0 dans le cas contraire
     """
     if self.definition.max > 1:
       # marche avec '**'
       return 1
     else :
       return 0

  def makeobjet(self):
     return self.definition(val = None, nom = self.nom,parent = self.parent)

