from copy import copy

class MCList:
  def isMCList(self):
    """ 
       Retourne 1 si self est une MCList (liste de mots-cl�s), 0 sinon (d�faut) 
    """
    return 1

  def get_index(self,objet):
    """
        Retourne la position d'objet dans la liste self
    """
    return self.data.index(objet)

  def ajout_possible(self):
    """ 
        M�thode bool�enne qui retourne 1 si on peut encore ajouter une occurrence
        de l'�l�ment que contient self, 0 sinon 
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
           Mettre a jour les fils de l objet suite � la disparition 
           du concept sd
           Seuls les mots cles simples MCSIMP font un traitement autre 
           que de transmettre aux fils
    """
    for child in self.data :
      child.delete_concept(sd)

  def copy(self):
    """
       R�alise la copie d'une MCList
    """
    liste = self.data[0].definition.list_instance()
    # FR -->Il faut sp�cifier un parent pour la m�thode init qui attend 2 arguments ...
    liste.init(self.nom,self.parent)
    for objet in self:
      new_obj = objet.copy()
      # Pour etre coherent avec le constructeur de mots cles facteurs N_FACT.__call__
      # dans lequel le parent de l'element d'une MCList est le parent de la MCList
      new_obj.reparent(self.parent)
      liste.append(new_obj)
    return liste

  def get_docu(self):
    return self.data[0].definition.get_docu()

  def get_liste_mc_inconnus(self):
     """
     Retourne la liste des mots-cl�s inconnus dans self
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
        Retourne la liste des mots-cl�s � rajouter pour satisfaire les r�gles
        en fonction de la liste des mots-cl�s pr�sents
    """
    # Sans objet pour une liste de mots cl�s facteurs
    return []

  def verif_condition_bloc(self):
    """ 
        Evalue les conditions de tous les blocs fils possibles 
        (en fonction du catalogue donc de la d�finition) de self et 
        retourne deux listes :
        - la premi�re contient les noms des blocs � rajouter
        - la seconde contient les noms des blocs � supprimer
    """
    # Sans objet pour une liste de mots cl�s facteurs
    return [],[]

  def init_modif(self):
    """
       Met l'�tat de l'objet � modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def get_etape(self):
     """
        Retourne l'�tape � laquelle appartient self
        Un objet de la cat�gorie etape doit retourner self pour indiquer que
        l'�tape a �t� trouv�e
        XXX double emploi avec self.etape ???
     """
     if self.parent == None: return None
     return self.parent.get_etape()

  def get_genealogie(self):
     """
         Retourne la liste des noms des ascendants.
         Un objet MCList n'est pas enregistr� dans la genealogie.
         XXX Meme si le MCFACT fils ne l'est pas lui non plus ????
     """
     if self.parent: 
        return self.parent.get_genealogie()
     else:
        return []

  def get_liste_mc_ordonnee_brute(self,liste,dico):
     """
         Retourne la liste ordonn�e (suivant le catalogue) BRUTE des mots-cl�s
         d'une entit� compos�e dont le chemin complet est donn� sous forme
         d'une liste du type :ETAPE + MCFACT ou MCBLOC + ...
     """
     for arg in liste:
        objet_cata = dico[arg]
        dico=objet_cata.dico
     return objet_cata.liste

  def reparent(self,parent):
     """
         Cette methode sert a reinitialiser la parente de l'objet
     """
     self.parent=parent
     self.jdc=parent.jdc
     self.etape=etape
     for mcfact in self.data:
        mcfact.reparent(parent)

