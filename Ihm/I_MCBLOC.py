import I_MCCOMPO
class MCBLOC(I_MCCOMPO.MCCOMPO):
  def makeobjet(self):
    return self.definition(val = None,  nom = self.nom,parent = self.parent)

