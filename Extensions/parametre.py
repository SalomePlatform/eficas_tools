# -*- coding: utf-8 -*-
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
"""
    Ce module contient la classe PARAMETRE qui sert � d�finir
    des objets param�tres qui sont compr�hensibles et donc affichables
    par EFICAS.
    Ces objets sont cr��s � partir de la modification du fichier de commandes
    de l'utilisateur par le parseur de fichiers Python
"""

# import de modules Python
import string,types
from math import *

# import de modules Eficas
from Noyau.N_CR import CR
from Noyau import N_OBJECT
from Ihm import I_OBJECT

class PARAMETRE(N_OBJECT.OBJECT,I_OBJECT.OBJECT) :
  """
     Cette classe permet de cr�er des objets de type PARAMETRE
     cad des affectations directes dans le jeu de commandes (ex: a=10.)
     qui sont interpr�t�es par le parseur de fichiers Python.
     Les objets ainsi cr��s constituent des param�tres pour le jdc
  """

  nature = 'PARAMETRE'
  idracine = 'param'

  def __init__(self,nom,valeur=None):
    # parent ne peut �tre qu'un objet de type JDC
    self.dict_valeur=[]
    self.valeur = self.interprete_valeur(valeur)
    self.val=valeur
    self.nom = nom
    # La classe PARAMETRE n'a pas de d�finition : on utilise self pour
    # compl�tude
    self.definition=self
    self.jdc = self.parent = CONTEXT.get_current_step()
    self.niveau=self.parent.niveau
    self.actif=1
    self.state='undetermined'
    self.register()

  def __getitem__(self,key):
    param_item=ITEM_PARAMETRE(self,key)
    return param_item

  def __neg__(self):
    try:
      return -1*self.valeur
    except:
      print "******* Probleme : pas de valeur n�gative"
      return None
    
  def __add__(self,a):
    try :
      return self.valeur+a.valeur
    except :
      print "******* Probleme : a l addition"
      return None

  def __radd__(self,a):
    try :
      return self.valeur+a.valeur
    except :
      print "******* Probleme : a l addition"
      return None

  def __sub__(self,a):
    try :
      return self.valeur  - a.valeur
    except :
      print "******* Probleme : a la soustraction"
      return None

  def __rsub__(self,a):
    try :
      return a.valeur - self.valeur
    except :
      print "******* Probleme : a la soustraction"
      return None

  def __mul__(self,a):
    try :
      return self.valeur*a.valeur
    except :
      print "******* Probleme : a la multiplication"
      return None

  def __rmul__(self,a):
    try :
      return self.valeur*a.valeur
    except :
      print "******* Probleme : a la multiplication"
      return None

  def __mul__(self,a):
    try :
      return self.valeur*a.valeur
    except :
      print "******* Probleme : a la multiplication"
      return None

  def __rmul__(self,a):
    try :
      return self.valeur*a.valeur
    except :
      print "******* Probleme : a la multiplication"
      return None

  def __add__(self,other):
    try :
      return self.valeur+other
    except :
      print "******* Probleme : a l addition"
      return None

  def __radd__(self,other):
    try :
      return self.valeur+other
    except :
      print "******* Probleme : a l addition"
      return None

  def __sub__(self,other):
    try :
      return self.valeur  - other
    except :
      print "******* Probleme : a la soustraction"
      return None

  def __rsub__(self,other):
    try :
      return other - self.valeur
    except :
      print "******* Probleme : a la soustraction"
      return None

  def  __mul__ (self,other):
    retour=None
    try :
      retour = eval(self.valeur) * other
    except :
      try :
         retour = self.valeur * other
      except :
         print "******* Probleme : a la multiplication"
    return retour

  def __rmul__ (self,other):
    retour=None
    try :
      retour = eval(self.valeur) * other
    except :
      try :
         retour = self.valeur * other
      except :
         print "******* Probleme : a la multiplication"
    return retour


  def interprete_valeur(self,val):
    """
    Essaie d'interpr�ter val (cha�ne de caract�res)comme :
    - un entier
    - un r�el
    - une cha�ne de caract�res
    - une liste d'items d'un type qui pr�c�de
    Retourne la valeur interpr�t�e
    """
    if not val : return None
    valeur = None
    #  on v�rifie si val est un entier
    try :
        valeur = string.atoi(val)       # on a un entier
        return valeur
    except :
        pass
    #  on v�rifie si val est un r�el
    try:
        valeur = string.atof(val)   # on a un r�el
        return valeur
    except :
        pass
    # on v�rifie si val est un tuple
    try :
        valeur = eval(val)
    except:
        pass
    #PN je n ose pas modifier je rajoute
    if valeur != None :
        if type(valeur) == types.TupleType:
            l_new_val = []
            typ = None
            for v in valeur :
                if not typ:
                    typ = type(v)
                else:
                    if type(v) != typ :
                        # la liste est h�t�rog�ne --> on refuse d'interpr�ter
                        #  self comme une liste
                        # on retourne la string initiale
                        print 'liste h�t�rog�ne ',val
                        return val
                l_new_val.append(v)
            return tuple(l_new_val)
	# PN : commente le print
        #else:
            # on a r�ussi � �valuer val en autre chose qu'un tuple ...
            #print "on a r�ussi � �valuer %s en autre chose qu'un tuple ..." %val
            #print 'on trouve : ',str(valeur),' de type : ',type(valeur)
    # on retourne val comme une string car on n'a pas su l'interpr�ter
    if valeur != None :
       if type(valeur).__name__ == 'list':
          self.dict_valeur=[]
          for i in range(len(valeur)):
	      self.dict_valeur.append(valeur[i])
    return val

  def get_valeurs(self):
    valeurretour=[]
    if self.dict_valeur != []:
       for val in self.dict_valeur:
           valeurretour.append(val)
    else:
        valeurretour.append(self.valeur)
    return valeurretour

  def set_valeur(self,new_valeur):
    """
    Remplace la valeur de self par new_valeur interpr�t�e
    """
    self.valeur = self.interprete_valeur(new_valeur)
    self.init_modif()

  def init_modif(self):
    """
    M�thode qui d�clare l'objet courant comme modifi� et propage
    cet �tat modifi� � ses ascendants
    """
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def register(self):
    """
    Enregistre le param�tre dans la liste des �tapes de son parent (JDC)
    """
    self.parent.register_parametre(self)
    self.parent.register(self)

  def isvalid(self,cr='non'):
    """
    Retourne 1 si self est valide, 0 sinon
    Un param�tre est consid�r� comme valide si :
      - il a un nom
      - il a une valeur
    """
    if self.nom == '' :
        if cr == 'oui':
           self.cr.fatal("Pas de nom donn� au param�tre ")
        return 0
    else:
        if self.valeur == None :
            if cr == 'oui' : 
               self.cr.fatal("Le param�tre %s ne peut valoir None" % self.nom)
            return 0
    return 1

  def isoblig(self):
    """
    Indique si self est obligatoire ou non : retourne toujours 0
    """
    return 0

  def isrepetable(self):
    """
    Indique si self est r�p�table ou non : retourne toujours 1
    """
    return 1

  def liste_mc_presents(self):
    return []

  def supprime(self):
    """
    M�thode qui supprime toutes les boucles de r�f�rences afin que 
    l'objet puisse �tre correctement d�truit par le garbage collector
    """
    self.parent = None
    self.jdc = None
    self.definition=None

  def active(self):
    """
    Rend l'etape courante active.
    Il faut ajouter le param�tre au contexte global du JDC
    """
    self.actif = 1
    try:
        self.jdc.append_param(self)
    except:
        pass

  def inactive(self):
    """
    Rend l'etape courante inactive
    Il faut supprimer le param�tre du contexte global du JDC
    """
    self.actif = 0
    self.jdc.del_param(self)
    self.jdc.delete_concept_after_etape(self,self)

  def isactif(self):
    """
    Bool�enne qui retourne 1 si self est actif, 0 sinon
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
    Il faut supprimer le param�tre qui a �t� entr� dans la liste des
    param�tres du JDC
    """
    self.jdc.delete_param(self)

  def update_context(self,d):
    """
    Update le dictionnaire d avec le param�tre que produit self
    """
    d[self.nom]=self

  def __repr__(self):
    """
        Donne un echo de self sous la forme nom = valeur
    """
    return self.nom+' = '+str(self.valeur)

  def __str__(self):
    """
        Retourne le nom du param�tre comme repr�sentation de self
    """
    return self.nom

  def get_sdprods(self,nom_sd):
     """
         Retourne les concepts produits par la commande
     """
     return None

  def report(self):
    """ G�n�re l'objet rapport (classe CR) """
    self.cr=CR()
    self.isvalid(cr='oui')
    return self.cr

  def ident(self):
    """
    Retourne le nom interne associ� � self
    Ce nom n'est jamais vu par l'utilisateur dans EFICAS
    """
    return self.nom

  def delete_concept(self,sd):
    pass

  def replace_concept(self,old_sd,sd):
    pass

  def verif_condition_bloc(self):
    """
        Evalue les conditions de tous les blocs fils possibles
        (en fonction du catalogue donc de la d�finition) de self et
        retourne deux listes :
          - la premi�re contient les noms des blocs � rajouter
          - la seconde contient les noms des blocs � supprimer
    """
    return [],[]

  def verif_condition_regles(self,liste_presents):
    """
        Retourne la liste des mots-cl�s � rajouter pour satisfaire les r�gles
        en fonction de la liste des mots-cl�s pr�sents
    """
    return []

  def verif_existence_sd(self):
     pass

  def control_sdprods(self,d):
      """sans objet """
      pass



class ITEM_PARAMETRE :
  def __init__(self,param_pere,item=None):
      self.param_pere = param_pere
      self.item = item
      

  def __repr__(self):
    return self.param_pere.nom+'['+str(self.item)+']'


  def isvalid(self):
      isvalid = 1
      if self.item < 0:
         isvalid =  0
      try:
	 longueur= len(self.param_pere.dict_valeur) - 1
      except:
         longueur=0
      if self.item > longueur :
         isvalid= 0
      return isvalid
