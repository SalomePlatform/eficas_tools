#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
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
     """
     Une MCList n'est jamais obligatoire (même si le MCFACT qu'elle représente l'est
     """
     return 0
     #for i in self.data:
     #  if i.isoblig():return 1
     #return 0

  def liste_mc_presents(self):
    return []

  def delete_concept(self,sd):
    """ 
        Inputs :
           - sd=concept detruit
        Fonction : Mettre a jour les fils de l objet suite à la disparition 
        du concept sd
        Seuls les mots cles simples MCSIMP font un traitement autre 
        que de transmettre aux fils
    """
    for child in self.data :
      child.delete_concept(sd)

  def replace_concept(self,old_sd,sd):
    """
        Inputs :
           - old_sd=concept remplacé
           - sd=nouveau concept
        Fonction : Mettre a jour les fils de l objet suite au remplacement 
        du concept old_sd
    """
    for child in self.data :
      child.replace_concept(old_sd,sd)

  def copy(self):
    """
       Réalise la copie d'une MCList
    """
    liste = self.data[0].definition.list_instance()
    # FR -->Il faut spécifier un parent pour la méthode init qui attend 2 arguments ...
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
     Retourne la liste des mots-clés inconnus dans self
     """
     l_mc = []
     for mcfact in self.data :
        if mcfact.isvalid() : continue
        l_child = mcfact.get_liste_mc_inconnus()
        for mc in l_child:
           l = [self]
           l.extend(mc)
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

  def init_modif(self):
    """
       Met l'état de l'objet à modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def get_etape(self):
     """
        Retourne l'étape à laquelle appartient self
        Un objet de la catégorie etape doit retourner self pour indiquer que
        l'étape a été trouvée
        XXX double emploi avec self.etape ???
     """
     if self.parent == None: return None
     return self.parent.get_etape()

  def get_genealogie(self):
     """
         Retourne la liste des noms des ascendants.
         Un objet MCList n'est pas enregistré dans la genealogie.
         XXX Meme si le MCFACT fils ne l'est pas lui non plus ????
     """
     if self.parent: 
        return self.parent.get_genealogie()
     else:
        return []

  def get_liste_mc_ordonnee_brute(self,liste,dico):
     """
         Retourne la liste ordonnée (suivant le catalogue) BRUTE des mots-clés
         d'une entité composée dont le chemin complet est donné sous forme
         d'une liste du type :ETAPE + MCFACT ou MCBLOC + ...
     """
     for arg in liste:
        objet_cata = dico[arg]
        dico=objet_cata.entites
     return objet_cata.ordre_mc

  def reparent(self,parent):
     """
         Cette methode sert a reinitialiser la parente de l'objet
     """
     self.parent=parent
     self.jdc=parent.jdc
     self.etape=parent.etape
     for mcfact in self.data:
        mcfact.reparent(parent)

  def verif_existence_sd(self):
     """
        Vérifie que les structures de données utilisées dans self existent bien dans le contexte
	avant étape, sinon enlève la référence à ces concepts
     """
     for motcle in self.data :
         motcle.verif_existence_sd()

  def get_sd_utilisees(self):
    """
        Retourne la liste des concepts qui sont utilisés à l'intérieur de self
        ( comme valorisation d'un MCS)
    """
    l=[]
    for motcle in self.data:
      l.extend(motcle.get_sd_utilisees())
    return l

  def get_fr(self):
     """
         Retourne la chaine d'aide contenue dans le catalogue
         en tenant compte de la langue
     """
     try :
        return self.data[0].get_fr()
     except:
        return ''

