# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
"""
    Ce module contient la classe PARAMETRE qui sert a definir
    des objets parametres qui sont comprehensibles et donc affichables
    par EFICAS.
    Ces objets sont crees a partir de la modification du fichier de commandes
    de l'utilisateur par le parseur de fichiers Python
"""

# import de modules Python
import string,types
from math import *
import traceback

# import de modules Eficas
from Noyau.N_CR import CR
from Noyau import N_OBJECT
from Ihm import I_OBJECT
from param2 import *
from Ihm import CONNECTOR
from Extensions.i18n import tr

class PARAMETRE(N_OBJECT.OBJECT,I_OBJECT.OBJECT,Formula) :
  """
     Cette classe permet de creer des objets de type PARAMETRE
     cad des affectations directes dans le jeu de commandes (ex: a=10.)
     qui sont interpretees par le parseur de fichiers Python.
     Les objets ainsi crees constituent des parametres pour le jdc
  """

  nature = 'PARAMETRE'
  idracine = 'param'

  def __init__(self,nom,valeur=None):
    self.nom = nom
    # La classe PARAMETRE n'a pas de definition : on utilise self pour
    # completude
    self.definition=self
    # parent ne peut �tre qu'un objet de type JDC
    self.jdc = self.parent = CONTEXT.get_current_step()
    self.niveau=self.parent.niveau
    self.actif=1
    self.state='undetermined'
    self.register()
    self.dict_valeur=[]
    #self.valeur = self.interprete_valeur(valeur)
    #self.val=valeur
    self.valeur = valeur
    self.val=repr(valeur)

  def interprete_valeur(self,val):
    """
    Essaie d'interpreter val (cha�ne de caracteres)comme :
    - un entier
    - un reel
    - une cha�ne de caracteres
    - une liste d'items d'un type qui precede
    Retourne la valeur interpretee
    """
    #if not val : return None
    valeur = None

    if type(val) == types.ListType:
    # Un premier traitement a ete fait lors de la saisie
    # permet de tester les parametres qui sont des listes
       l_new_val = []
       for v in val :
           try :
               valeur=eval(str(v))
               l_new_val.append(v)
           except :
               return None
       return l_new_val

    if type(val) == types.StringType:
       # on tente l'evaluation dans un contexte fourni par le parent s'il existe
       if self.parent:
          valeur=self.parent.eval_in_context(val,self)
       else:
          try :
              valeur = eval(val)
          except:
              #traceback.print_exc()
              pass
    #PN je n ose pas modifier je rajoute
    # refus des listes heterogenes : ne dvrait pas etre la
    if valeur != None :
        if type(valeur) == types.TupleType:
            l_new_val = []
            typ = None
            for v in valeur :
                if not typ:
                    typ = type(v)
                else:
                    if type(v) != typ :
                        # la liste est heterogene --> on refuse d'interpreter
                        #  self comme une liste
                        # on retourne la string initiale
                        print ('liste heterogene ',val)
                        return val
                l_new_val.append(v)
            return tuple(l_new_val)

    if valeur != None :
       if type(valeur).__name__ == 'list':
          self.dict_valeur=[]
          for i in range(len(valeur)):
             self.dict_valeur.append(valeur[i])
       return valeur
    # on retourne val comme une string car on n'a pas su l'interpreter
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
    Remplace la valeur de self par new_valeur interpretee
    """
    self.valeur = self.interprete_valeur(new_valeur)
    self.val=repr(self.valeur)
    self.parent.update_concept_after_etape(self,self)
    self.init_modif()

  def set_nom(self,new_nom):
    """
    Change le nom du parametre
    """
    self.init_modif()
    self.nom=new_nom
    self.fin_modif()

  def init_modif(self):
    """
    Methode qui declare l'objet courant comme modifie et propage
    cet etat modifie a ses ascendants
    """
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def get_jdc_root(self):
    if self.parent:
      return self.parent.get_jdc_root()
    else:
      return self

  def register(self):
    """
    Enregistre le parametre dans la liste des etapes de son parent (JDC)
    """
    self.parent.register_parametre(self)
    self.parent.register(self)

  def isvalid(self,cr='non'):
    """
    Retourne 1 si self est valide, 0 sinon
    Un parametre est considere comme valide si :
      - il a un nom
      - il a une valeur
    """
    if self.nom == '' :
        if cr == 'oui':
           self.cr.fatal(tr("Pas de nom donne au parametre "))
        return 0
    else:
        if self.valeur == None :
            if cr == 'oui' : 
               self.cr.fatal(tr("Le parametre %s ne peut valoir None" , self.nom))
            return 0
    return 1

  def isoblig(self):
    """
    Indique si self est obligatoire ou non : retourne toujours 0
    """
    return 0

  def isrepetable(self):
    """
    Indique si self est repetable ou non : retourne toujours 1
    """
    return 1

  def liste_mc_presents(self):
    return []

  def supprime(self):
    """
    Methode qui supprime toutes les boucles de references afin que 
    l'objet puisse �tre correctement detruit par le garbage collector
    """
    self.parent = None
    self.jdc = None
    self.definition=None
    self.niveau=None

  def active(self):
    """
    Rend l'etape courante active.
    Il faut ajouter le parametre au contexte global du JDC
    """
    self.actif = 1
    try:
        self.jdc.append_param(self)
    except:
        pass
    CONNECTOR.Emit(self,"add",None)
    CONNECTOR.Emit(self,"valid")

  def inactive(self):
    """
    Rend l'etape courante inactive
    Il faut supprimer le parametre du contexte global du JDC
    """
    self.actif = 0
    self.jdc.del_param(self)
    self.jdc.delete_concept_after_etape(self,self)
    CONNECTOR.Emit(self,"supp",None)
    CONNECTOR.Emit(self,"valid")

  def isactif(self):
    """
    Booleenne qui retourne 1 si self est actif, 0 sinon
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
    Il faut supprimer le parametre qui a ete entre dans la liste des
    parametres du JDC
    """
    self.jdc.delete_param(self)
    self.parent.delete_concept(self)

  def update_context(self,d):
    """
    Update le dictionnaire d avec le parametre que produit self
    """
    d[self.nom]=self

  def __repr__(self):
    """
        Donne un echo de self sous la forme nom = valeur
    """
    if type(self.valeur) == types.StringType:
         if self.valeur.find('\n') == -1:
            # pas de retour chariot, on utilise repr
            return self.nom+' = '+ repr(self.valeur)
         elif self.valeur.find('"""') == -1:
            # retour chariot mais pas de triple ", on formatte
            return self.nom+' = """'+self.valeur+'"""'
         else:
            return self.nom+' = '+ repr(self.valeur)
    else:
       if type(self.valeur) == types.ListType :
          aRetourner=self.nom+' = ['
          for l in self.valeur :
            aRetourner=aRetourner+str(l) +","
          aRetourner=aRetourner[0:-1]+']'
          return aRetourner
       return self.nom+' = '+ str(self.valeur)

  def __str__(self):
    """
        Retourne le nom du parametre comme representation de self
    """
    return self.nom

  def get_sdprods(self,nom_sd):
     """
         Retourne les concepts produits par la commande
     """
     return None

  def report(self):
    """ Genere l'objet rapport (classe CR) """
    self.cr=CR()
    self.isvalid(cr='oui')
    return self.cr

  def ident(self):
    """
    Retourne le nom interne associe a self
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
        (en fonction du catalogue donc de la definition) de self et
        retourne deux listes :
          - la premiere contient les noms des blocs a rajouter
          - la seconde contient les noms des blocs a supprimer
    """
    return [],[]

  def verif_condition_regles(self,liste_presents):
    """
        Retourne la liste des mots-cles a rajouter pour satisfaire les regles
        en fonction de la liste des mots-cles presents
    """
    return []

  def verif_existence_sd(self):
     pass

  def control_sdprods(self,d):
      """sans objet """
      pass

  def close(self):
      pass

  def reset_context(self):
      pass

  def eval(self):
      if isinstance(self.valeur,Formula):
         return self.valeur.eval()
      else:
         return self.valeur

  def __adapt__(self,validator):
      return validator.adapt(self.eval())

class COMBI_PARAMETRE :
  def __init__(self,chainevaleur,valeur):
      self.chainevaleur=chainevaleur
      self.valeur=valeur

  def __repr__(self):
      return self.chainevaleur

  def isvalid(self):
      if self.valeur and self.chainevaleur:
         return 1

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
