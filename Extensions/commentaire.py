"""
   Ce module contient la classe COMMENTAIRE qui sert dans EFICAS
   pour gérer les commentaires dans un JDC
"""

from Noyau.N_CR import CR

class COMMENTAIRE :
  """ 
      Cette classe permet de créer des objets de type COMMENTAIRE 
  """
  nature = 'COMMENTAIRE'
  idracine = '_comm'

  def __init__(self,valeur,parent=None):
    # parent est un objet de type OBJECT (ETAPE ou MC ou JDC...)
    self.valeur=valeur
    if not parent :
      self.jdc = self.parent = CONTEXT.get_current_step()
    else:
      self.jdc = self.parent = parent
    # La classe COMMENTAIRE n'a pas de définition. On utilise self
    # pour complétude
    self.definition=self
    self.nom=''
    self.niveau = self.parent.niveau
    self.actif=1
    self.register()

  def register(self):
    """ 
        Enregistre le commentaire dans la liste des étapes de son parent
        lorsque celui-ci est un JDC 
    """
    if self.parent.nature == 'JDC':
      # le commentaire est entre deux commandes:
      # il faut l'enregistrer dans la liste des étapes
      self.parent.register(self)

  def isvalid(self):
    """
    Retourne 1 si self est valide, 0 sinon
    Retourne toujours 1 car un commentaire est toujours valide
    """
    return 1

  def isoblig(self):
    """ Indique si self est obligatoire ou non : retourne toujours 0 """
    return 0

  def isrepetable(self):
    """ Indique si self est répétable ou non : retourne toujours 1 """
    return 1

  def active(self):
      """
      Rend l'etape courante active
      """
      self.actif = 1

  def inactive(self):
      """
      Rend l'etape courante inactive
      NB : un commentaire est toujours actif !
      """
      self.actif = 1

  def isactif(self):
      """
      Booléenne qui retourne 1 si self est valide, 0 sinon
      """
      return self.actif

  def supprime(self):
      """
      Méthode qui supprime toutes les boucles de références afin que 
      l'objet puisse être correctement détruit par le garbage collector
      """
      self.parent=None
      self.jdc=None
      self.definition = None
      self.niveau = None

  def liste_mc_presents(self):
      return []

  def get_valeur(self) :
    """ Retourne la valeur de self, cad le contenu du commentaire """
    try :
      return self.valeur
    except:
      return None

  def set_valeur(self,new_valeur):
    """ 
        Remplace la valeur de self(si elle existe) par new_valeur
    """
    self.valeur = new_valeur
    self.init_modif()

  def init_modif(self):
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def supprime_sdprods(self):
    pass

  def update_context(self,d):
    """
        Update le dictionnaire d avec les concepts ou objets produits par self
        --> ne fait rien pour un commentaire
    """
    pass

  def report(self):
    """ Génère l'objet rapport (classe CR) """
    self.cr=CR()
    if not self.isvalid(): self.cr.warn("Objet commentaire non valorisé")
    return self.cr

  def ident(self):
    """ Retourne le nom interne associé à self
        Ce nom n'est jamais vu par l'utilisateur dans EFICAS
    """
    return self.nom

  def delete_concept(self,sd):
    pass

  def verif_condition_bloc(self):
    """
        Evalue les conditions de tous les blocs fils possibles
        (en fonction du catalogue donc de la définition) de self et
        retourne deux listes :
        - la première contient les noms des blocs à rajouter
        - la seconde contient les noms des blocs à supprimer
    """
    return [],[]

  def verif_condition_regles(self,liste_presents):
    """
        Retourne la liste des mots-clés à rajouter pour satisfaire les règles
        en fonction de la liste des mots-clés présents
    """
    return []



