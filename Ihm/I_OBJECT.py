"""
"""

class OBJECT:
  def isMCList(self):
    """ 
        Retourne 1 si self est une MCList (liste de mots-clés), 
                 0 sinon (défaut) 
    """
    return 0

  def get_regles(self):
    """ 
       Retourne les règles de self 
    """
    if hasattr(self,'definition'):
      return self.definition.regles
    elif hasattr(self,'regles'):
      return self.regles
    else :
      return []

  def init_modif(self):
    """
       Met l'état de l'objet à modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def fin_modif(self):
      """
      Méthode appelée après qu'une modification a été faite afin de déclencher
      d'éventuels traitements post-modification
      """
      # pour les objets autres que les commandes, aucun traitement spécifique 
      # on remonte l'info de fin de modif au parent
      if self.parent:
        self.parent.fin_modif()

  def isrepetable(self):
    """
         Indique si l'objet est répétable
    """
    return 0

  def liste_mc_presents(self):
    """
         Retourne la liste des noms des mots clés présents
    """
    return []

  def get_docu(self):
    return self.definition.get_docu()

  def get_liste_mc_inconnus(self):
     """
     Retourne la liste des mots-clés inconnus dans self
     """
     return []

  def verif_condition_regles(self,liste_presents):
    """ 
        Retourne la liste des mots-clés à rajouter pour satisfaire les règles
        en fonction de la liste des mots-clés présents 
    """
    liste=[]
    for regle in self.definition.regles:
        liste=regle.verif_condition_regle(liste,liste_presents)
    return liste

  def verif_condition_bloc(self):
    """ 
        Evalue les conditions de tous les blocs fils possibles 
        (en fonction du catalogue donc de la définition) de self et
        retourne deux listes :
        - la première contient les noms des blocs à rajouter
        - la seconde contient les noms des blocs à supprimer
    """
    return [],[]


