from Noyau import N_JDC_CATA

class JDC_CATA:
  def __init__(self):
    self.l_noms_entites=[]

  def enregistre(self,commande):
    """ 
        Cette m�thode surcharge la m�thode de la classe du Noyau
        Marche avec Noyau mais si un autre package l'a d�j� surcharg�e ???
    """
    N_JDC_CATA.JDC_CATA.enregistre(self,commande)
    self.l_noms_entites.append(commande.nom)

  def get_liste_cmd(self):
    self.l_noms_entites.sort()
    return self.l_noms_entites

