"""
"""
import string

class REGLE:

  def gettext(self):
    text = self.__class__.__name__+ ' :\n'
    for mc in self.mcs :
      text = text + '\t' + string.strip(mc) + '\n'
    return text

  def purge_liste(self,liste_a_purger,liste_mc_presents):
    """
         Cette méthode doit retirer de la liste liste_a_purger
         les éléments qui ne doivent plus apparaitre en fonction du contexte
    """
    # Dans le cas général on ne touche pas à la liste
    return liste_a_purger

  def has_operande(self,nom):
    # On peut faire aussi try:self.mcs.index(nom);return 1;except:return 0
    for mc in self.mcs:
      if mc==nom : return 1
    return 0

  def verif_condition_regle(self,liste,l_mc_presents):
    return []



