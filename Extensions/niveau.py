"""
    Ce module contient la classe NIVEAU qui sert à définir
    des groupes de commandes dans le catalogue
"""

class NIVEAU:
  def __init__(self,nom='',label='',niveaux=(),valide_vide=1,actif=1):
    self.nom = nom
    self.label = label
    self.statut='o'
    self.min = 1
    self.max = 1
    self.entites = []
    self.l_noms_entites=[]
    self.valide_vide = valide_vide
    self.actif = actif
    self.d_niveaux = {}
    self.l_niveaux = niveaux
    for niveau in niveaux:
      self.d_niveaux[niveau.nom]=niveau
      self.d_niveaux.update(niveau.d_niveaux)

  def enregistre(self,commande):
    self.entites.append(commande)
    self.l_noms_entites.append(commande.nom)

  def get_liste_cmd(self):
    self.l_noms_entites.sort()
    return self.l_noms_entites

