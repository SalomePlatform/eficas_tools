import I_MCCOMPO
class MCFACT(I_MCCOMPO.MCCOMPO):
  def isrepetable(self):
     """ 
         Indique si l'objet est r�p�table.
         Retourne 1 si le mot-cl� facteur self peut �tre r�p�t�
         Retourne 0 dans le cas contraire
     """
     if self.definition.max > 1:
       # marche avec '**'
       return 1
     else :
       return 0

  def makeobjet(self):
     return self.definition(val = None, nom = self.nom,parent = self.parent)

