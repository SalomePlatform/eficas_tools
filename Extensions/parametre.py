"""
    Ce module contient la classe PARAMETRE qui sert à définir
    des objets paramètres qui sont compréhensibles et donc affichables
    par EFICAS.
    Ces objets sont créés à partir de la modification du fichier de commandes
    de l'utilisateur par le parseur de fichiers Python
"""

# import de modules Python
import string,types

# import de modules Eficas
from Noyau.N_CR import CR

class PARAMETRE :
  """
     Cette classe permet de créer des objets de type PARAMETRE
     cad des affectations directes dans le jeu de commandes (ex: a=10.)
     qui sont interprétées par le parseur de fichiers Python.
     Les objets ainsi créés constituent des paramètres pour le jdc
  """

  nature = 'PARAMETRE'
  idracine = 'param'

  def __init__(self,nom,valeur=None):
    # parent ne peut être qu'un objet de type JDC
    self.valeur = self.interprete_valeur(valeur)
    self.val=valeur
    self.nom = nom
    # La classe PARAMETRE n'a pas de définition : on utilise self pour
    # complétude
    self.definition=self
    self.jdc = self.parent = CONTEXT.get_current_step()
    self.niveau=self.parent.niveau
    self.register()

  def interprete_valeur(self,val):
    """
    Essaie d'interpréter val (chaîne de caractères)comme :
    - un entier
    - un réel
    - une chaîne de caractères
    - une liste d'items d'un type qui précède
    Retourne la valeur interprétée
    """
    if not val : return None
    valeur = None
    #  on vérifie si val est un entier
    try :
        valeur = string.atoi(val)       # on a un entier
        return valeur
    except :
        pass
    #  on vérifie si val est un réel
    try:
        valeur = string.atof(val)   # on a un réel
        return valeur
    except :
        pass
    # on vérifie si val est un tuple
    try :
        valeur = eval(val)
    except:
        pass
    if valeur != None :
        if type(valeur) == types.TupleType:
            l_new_val = []
            typ = None
            for v in valeur :
                if not typ:
                    typ = type(v)
                else:
                    if type(v) != typ :
                        # la liste est hétérogène --> on refuse d'interpréter
                        #  self comme une liste
                        # on retourne la string initiale
                        print 'liste hétérogène ',val
                        return val
                l_new_val.append(v)
            return tuple(l_new_val)
        else:
            # on a réussi à évaluer val en autre chose qu'un tuple ...
            print "on a réussi à évaluer %s en autre chose qu'un tuple ..." %val
            print 'on trouve : ',str(valeur),' de type : ',type(valeur)
    # on retourne val comme une string car on n'a pas su l'interpréter
    return val

  def set_valeur(self,new_valeur):
    """
    Remplace la valeur de self par new_valeur interprétée
    """
    self.valeur = self.interprete_valeur(new_valeur)
    self.init_modif()

  def init_modif(self):
    """
    Méthode qui déclare l'objet courant comme modifié et propage
    cet état modifié à ses ascendants
    """
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def register(self):
    """
    Enregistre le paramètre dans la liste des étapes de son parent (JDC)
    """
    self.parent.register_parametre(self)
    self.parent.register(self)

  def isvalid(self,cr='non'):
    """
    Retourne 1 si self est valide, 0 sinon
    Un paramètre est considéré comme valide si :
    - il a un nom
    - il a une valeur
    """
    if self.nom == '' :
        if cr == 'oui':
           self.cr.fatal("Pas de nom donné au paramètre ")
        return 0
    else:
        if self.valeur == None :
            if cr == 'oui' : 
               self.cr.fatal("Le paramètre %s ne peut valoir None" % self.nom)
            return 0
    return 1

  def isoblig(self):
    """
    Indique si self est obligatoire ou non : retourne toujours 0
    """
    return 0

  def isrepetable(self):
    """
    Indique si self est répétable ou non : retourne toujours 1
    """
    return 1

  def liste_mc_presents(self):
    return []

  def supprime(self):
    """
    Méthode qui supprime toutes les boucles de références afin que 
    l'objet puisse être correctement détruit par le garbage collector
    """
    self.parent = None
    self.jdc = None
    self.definition=None

  def active(self):
    """
    Rend l'etape courante active.
    Il faut ajouter le paramètre au contexte global du JDC
    """
    self.actif = 1
    try:
        self.jdc.append_param(self)
    except:
        pass

  def inactive(self):
    """
    Rend l'etape courante inactive
    Il faut supprimer le paramètre du contexte global du JDC
    """
    self.actif = 0
    self.jdc.del_param(self)
    self.jdc.delete_concept_after_etape(self,self)

  def isactif(self):
    """
    Booléenne qui retourne 1 si self est actif, 0 sinon
    """
    return self.actif

  def set_attribut(self,nom_attr,new_valeur):
    """
    Remplace la valeur de self.nom_attr par new_valeur)
    """
    if hasattr(self,nom_attr):
      setattr(self,nom_attr,new_valeur)
      self.init_modif()

  def supprime_sdprods(self):
    """
    Il faut supprimer le paramètre qui a été entré dans la liste des
    paramètres du JDC
    """
    self.jdc.delete_param(self)

  def update_context(self,d):
    """
    Update le dictionnaire d avec le paramètre que produit self
    """
    d[self.nom]=self

  def __repr__(self):
    """
        Donne un echo de self sous la forme nom = valeur
    """
    return self.nom+' = '+str(self.valeur)+'\n'

  def __str__(self):
    """
        Retourne le nom du paramètre comme représentation de self
    """
    return self.nom

  def get_sdprods(self,nom_sd):
     """
         Retourne les concepts produits par la commande
     """
     return None

  def report(self):
    """ Génère l'objet rapport (classe CR) """
    self.cr=CR()
    self.isvalid(cr='oui')
    return self.cr

  def ident(self):
    """
    Retourne le nom interne associé à self
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






