from copy import copy

class MCList:
  def isMCList(self):
    """ 
       Retourne 1 si self est une MCList (liste de mots-clés), 0 sinon (défaut) 
    """
    return 1

  def get_index(self,objet):
    """
        Retourne la position d'objet dans la liste self
    """
    return self.data.index(objet)

  def ajout_possible(self):
    """ 
        Méthode booléenne qui retourne 1 si on peut encore ajouter une occurrence
        de l'élément que contient self, 0 sinon 
    """
    max = self.data[0].definition.max
    if max == '**':
      return 1
    else:
      if len(self) < max :
        return 1
      else:
        return 0

  def isoblig(self):
    for i in self.data:
      if i.isoblig():return 1
    return 0

  def liste_mc_presents(self):
    return []

  def delete_concept(self,sd):
    """ 
        Inputs :
           sd=concept detruit
        Fonction :
           Mettre a jour les fils de l objet suite à la disparition 
           du concept sd
           Seuls les mots cles simples MCSIMP font un traitement autre 
           que de transmettre aux fils
    """
    for child in self.data :
      child.delete_concept(sd)

  def copy(self):
    liste = self.data[0].definition.list_instance()
    # XXX Pas de parent ??
    liste.init(self.nom)
    for objet in self:
      new_obj = objet.copy()
      liste.append(new_obj)
    return liste

  def get_docu(self):
    return self.data[0].definition.get_docu()

  def get_liste_mc_inconnus(self):
     """
     Retourne la liste des mots-clés inconnus dans self
     """
     l_mc = []
     for mcfact in self.data :
        if mcfact.isvalid() : continue
        l_child = mcfact.get_liste_mc_inconnus()
	if l_child :
	   l = [self]
	   l.extend(l_child)
	   l_mc.append(l)
     return l_mc

  def verif_condition_regles(self,liste_presents):
    """
        Retourne la liste des mots-clés à rajouter pour satisfaire les règles
        en fonction de la liste des mots-clés présents
    """
    # Sans objet pour une liste de mots clés facteurs
    return []

  def verif_condition_bloc(self):
    """ 
        Evalue les conditions de tous les blocs fils possibles 
        (en fonction du catalogue donc de la définition) de self et 
        retourne deux listes :
        - la première contient les noms des blocs à rajouter
        - la seconde contient les noms des blocs à supprimer
    """
    # Sans objet pour une liste de mots clés facteurs
    return [],[]

