"""
   Ce module contient des classes permettant de d�finir des validateurs
   pour EFICAS. Ces classes constituent un compl�ment � des classes existantes
   dans Noyau/N_VALIDATOR.py ou de nouvelles classes de validation.
   Ces classes compl�mentaires ne servent que pour l'IHM d'EFICAS.
   Elles servent essentiellement � ajouter des comportements sp�cifiques
   IHM aux classes existantes dans le Noyau.
   Ces comportements pourront etre rapatries dans le Noyau quand leur
   interface sera stabilis�e.
"""

import types
import Noyau.N_VALIDATOR

class Valid:
   """
        Cette classe est la classe mere de toutes les classes compl�mentaires
        que l'on trouve dans Ihm.
        Elle porte les comportements par d�faut des m�thodes des validateurs.
   """

   def info_erreur_item(self):
       """
          Cette m�thode permet d'avoir un message d'erreur pour un item
          dans une liste dans le cas ou le validateur fait des v�rifications
          sur les items d'une liste. Si le validateur fait des v�rifications 
          sur la liste elle meme et non sur ses items, la m�thode
          doit retourner une chaine vide.
       """
       return " "

   def aide(self):
       """
          Cette methode retourne une chaine de caract�re qui permet � EFICAS de construire
          un message d'aide en ligne
          En g�n�ral, le message retourn� est le meme que celui retourn� par la 
          m�thode info
       """
       return self.info()

   def info_erreur_liste(self):
       """
          Cette m�thode a un comportement compl�mentaire de celui de info_erreur_item.
          Elle retourne un message d'erreur li� uniquement aux v�rifications sur la liste
          elle meme et pas sur ses items. Dans le cas o� le validateur ne fait pas de v�rification
          sur des listes, elle retourne une chaine vide
       """
       return " "

   def is_list(self):
       """
          Cette m�thode retourne un entier qui indique si le validateur permet les listes (valeur 1)
          ou ne les permet pas (valeur 0).
          Par d�faut, un validateur n'autorise que des scalaires.
       """
       return 0

   def has_into(self):
       """
          Cette m�thode retourne un entier qui indique si le validateur propose une liste de choix (valeur 1)
          ou n'en propose pas.
          Par d�faut, un validateur n'en propose pas.
       """
       return 0

   def valide_liste_partielle(self,liste_courante):
       return 0

   def verif_item(self,valeur):
       """
          La methode verif du validateur effectue une validation complete de la valeur.
          valeur peut etre un scalaire ou une liste. Le validateur doit traiter les 2
          aspects s'il accepte des listes (dans ce cas la methode is_list doit retourner 1).
          La methode valid_item sert pour effectuer des validations partielles de liste
          Elle doit uniquement verifier la validite d'un item de liste mais pas les caracteristiques
          de la liste
       """
       return 0

   def get_into(self,liste_courante=None,into_courant=None):
       """
          Cette m�thode retourne la liste de choix propos�e par le validateur. Si le validateur ne propose
          pas de liste de choix, la m�thode retourne None.
          L'argument d'entr�e liste_courante, s'il est diff�rent de None, donne la liste des choix d�j�
          effectu�s par l'utilisateur. Dans ce cas, la m�thode get_into doit calculer la liste des choix
          en en tenant compte. Par exemple, si le validateur n'autorise pas les r�p�titions, la liste des
          choix retourn�e ne doit pas contenir les choix d�j� contenus dans liste_courante.
          L'argument d'entr�e into_courant, s'il est diff�rent de None, donne la liste des choix propos�s
          par d'autres validateurs. Dans ce cas, la m�thode get_into doit calculer la liste des choix � retourner
          en se limitant � cette liste initiale. Par exemple, si into_courant vaut (1,2,3) et que le validateur
          propose la liste de choix (3,4,5), la m�thode ne doit retourner que (3,).

          La m�thode get_into peut retourner une liste vide [], ce qui veut dire qu'il n'y a pas (ou plus) de choix possible
          Cette situation peut etre normale : l''utilisateur a utilis� tous les choix, ou r�sulter d'une incoh�rence 
          des validateurs : choix parmi (1,2,3) ET choix parmi (4,5,6). Il est impossible de faire la diff�rence entre
          ces deux situations.
       """
       return into_courant

   def is_eval(self,valeur):
       """
           Cette m�thode indique si valeur est un objet de type EVAL ou autre
           que l'on ne cherchera pas � evaluer et qui doit etre considere comme toujours valide
           Si c'est un objet de ce type elle retourne la valeur 1 sinon la valeur 0
       """
       if type(valeur) == types.InstanceType :
        if hasattr(valeur,'__class__'):
          if valeur.__class__.__name__ in ('EVAL','entier','reel','chaine','complexe','liste','PARAMETRE_EVAL') :
             return 1
       return 0

   def is_param(self,valeur):
       """
           Cette m�thode indique si valeur est un objet de type PARAMETRE
           dont on cherchera � evaluer la valeur (valeur.valeur)
       """
       if type(valeur) == types.InstanceType :
          if valeur.__class__.__name__ in ('PARAMETRE',):
             return 1
       return 0

   def is_unknown(self,valeur):
       """
           Cette m�thode indique si valeur est un objet de type inconnu
           c'est � dire ni de type EVAL ni de type PARAMETRE
       """
       if type(valeur) == types.InstanceType :
          if not self.is_eval(valeur) and not self.is_param(valeur):
             return 1
       return 0

   def surcharge_verif(self,methode_verif_initiale,valeur):
       if type(valeur) == types.InstanceType :
          #CCAR: pour le moment on fait comme dans is_entier de V_MCSIMP.py
          # mais il serait pr�f�rable d'appeler une m�thode de valeur : valeur.AsType()
          # qui donnerait le type g�n�rique de l'objet.
          # Pour un objet de "type" entier on obtiendrait par exemple 'I'
          if valeur.__class__.__name__ in ('EVAL','entier','reel','chaine','complexe','liste','PARAMETRE_EVAL') :
             # On ne v�rifie pas le type d'un EVAL ou d'un objet de classe entier, .... C'est toujours valide
             return 1
          elif valeur.__class__.__name__ in ('PARAMETRE',):
             # Dans le cas d'un parametre, il faut tester si la valeur du parametre est un entier
             valeur=valeur.valeur
          else:
             # Objet inconnu : invalide
             print "Objet non reconnu dans surcharge_verif : %s" %`valeur`
             return 0

       return methode_verif_initiale(self,valeur)

class FunctionVal(Valid):pass

class OrVal(Valid):
   def verif_item(self,valeur):
       for validator in self.validators:
           v=validator.verif_item(valeur)
           if v :
              return 1
       return 0

   def info_erreur_item(self):
       chaine=""
       a=1
       for v in self.validators:
	   if v.info_erreur_item() != " " :
              if a==1:
                 chaine=v.info_erreur_item()
                 a=0
	      else:
                 chaine=chaine+" \n ou "+ v.info_erreur_item()
       return chaine

   def info_erreur_liste(self):
       chaine=""
       a=1
       for v in self.validators:
	   if v.info_erreur_liste() != " " :
              if a==1:
                 chaine=v.info_erreur_liste()
                 a=0
	      else:
                 chaine=chaine+" \n ou "+v.info_erreur_liste()

   def is_list(self):
       """
          Si plusieurs validateurs sont reli�s par un OU
          il suffit qu'un seul des validateurs attende une liste
          pour qu'on consid�re que leur union attende une liste.
       """
       for validator in self.validators:
           v=validator.is_list()
           if v :
              return 1
       return 0

   def has_into(self):
       """
          Dans le cas ou plusieurs validateurs sont reli�s par un OU
          il faut que tous les validateurs proposent un choix pour 
          qu'on consid�re que leur union propose un choix.
          Exemple : Enum(1,2,3) OU entier pair, ne propose pas de choix
          En revanche, Enum(1,2,3) OU Enum(4,5,6) propose un choix (1,2,3,4,5,6)
       """
       for validator in self.validators:
           v=validator.has_into()
           if not v :
              return 0
       return 1

   def get_into(self,liste_courante=None,into_courant=None):
       """
          Dans le cas ou plusieurs validateurs sont reli�s par un OU
          tous les validateurs doivent proposer un choix pour 
          qu'on consid�re que leur union propose un choix.
          Tous les choix propos�s par les validateurs sont r�unis (op�rateur d'union)
          Exemple : Enum(1,2,3) OU entier pair, ne propose pas de choix
          En revanche, Enum(1,2,3) OU Enum(4,5,6) propose un choix (1,2,3,4,5,6)
       """
       validator_into=[]
       for validator in self.validators:
           v_into=validator.get_into(liste_courante,into_courant)
           if v_into is None:
              return v_into
           validator_into.extend(v_into)
       return validator_into
    

class AndVal(Valid):
   def info(self):
       return "\n et ".join([v.info() for v in self.validators])

   def info_erreur_item(self):
       chaine=""
       a=1
       for v in self.validators:
	   if v.info_erreur_item() != " " :
              if a==1:
                 chaine=v.info_erreur_item()
                 a=0
	      else:
                 chaine=chaine+" \n et "+v.info_erreur_item()
       return chaine

   def info_erreur_liste(self):
       a=1
       for v in self.validators:
	   if v.info_erreur_liste() != " " :
              if a==1:
                 chaine=v.info_erreur_liste()
                 a=0
	      else:
                 chaine=chaine+" \n et "+v.info_erreur_liste()
       return chaine

   def verif_item(self,valeur):
       for validator in self.validators:
           v=validator.verif_item(valeur)
           if not v :
              # L'info n'est probablement pas la meme que pour verif ???
              self.local_info=validator.info()
              return 0
       return 1

   def is_list(self):
       """
          Si plusieurs validateurs sont reli�s par un ET
          il faut que tous les validateurs attendent une liste
          pour qu'on consid�re que leur intersection attende une liste.
          Exemple Range(2,5) ET Card(1) n'attend pas une liste
          Range(2,5) ET Pair attend une liste
       """
       for validator in self.validators:
           v=validator.is_list()
           if v == 0 :
              return 0
       return 1

   def has_into(self):
       """
          Dans le cas ou plusieurs validateurs sont reli�s par un ET
          il suffit qu'un seul validateur propose un choix pour 
          qu'on consid�re que leur intersection propose un choix.
          Exemple : Enum(1,2,3) ET entier pair, propose un choix
          En revanche, entier pair ET superieur � 10 ne propose pas de choix 
       """
       for validator in self.validators:
           v=validator.has_into()
           if v :
              return 1
       return 0


   def get_into(self,liste_courante=None,into_courant=None):
       """
          Dans le cas ou plusieurs validateurs sont reli�s par un ET
          il suffit qu'un seul validateur propose un choix pour 
          qu'on consid�re que leur intersection propose un choix.

          Tous les choix propos�s par les validateurs sont crois�s (op�rateur d'intersection)
          Exemple : Enum(1,2,3) ET entier pair, propose un choix (2,)
          En revanche, Enum(1,2,3) ET Enum(4,5,6) ne propose pas de choix
       """
       for validator in self.validators:
           into_courant=validator.get_into(liste_courante,into_courant)
           if into_courant in ([],None):
              return into_courant
       return into_courant

class CardVal(Valid):
   def info(self):
       return "longueur de liste comprise entre  %s et %s" % (self.min,self.max)

   def is_list(self):
       if self.max == '**' or self.max > 1:
             return 1
       else:
             return 0

   def verif_item(self,valeur):
       return 1

   def valide_liste_partielle(self,liste_courante=None):
	validite=1
        print liste_courante
        if liste_courante != None :
           if len(liste_courante) > self.max :
              validite=0
        return validite

   def get_into(self,liste_courante=None,into_courant=None):
       if into_courant is None:
          return None
       elif liste_courante is None:
          return into_courant
       elif self.max == '**':
          return into_courant
       elif len(liste_courante) < self.max:
          return into_courant
       else:
          return []

   def info_erreur_liste(self):
       return "La cardinalit� de la liste doit �tre comprise entre %s et %s" % (self.min,self.max)

class ListVal(Valid):
   def is_list(self):
       return 1

   def get_into(self,liste_courante=None,into_courant=None):
       """
          Cette m�thode get_into effectue un traitement g�n�ral qui consiste
          a filtrer la liste de choix into_courant, si elle existe, en ne conservant
          que les valeurs valides (appel de la m�thode valid)
       """
       if into_courant is None:
          return None
       else:
          liste_choix=[]
          for e in into_courant:
              if self.verif(e):
                 liste_choix.append(e)
          return liste_choix

class EnumVal(ListVal):
   def verif_item(self,valeur):
       if valeur not in self.into:return 0
       return 1

   def has_into(self):
       return 1
 
   def get_into(self,liste_courante=None,into_courant=None):
       if into_courant is None:
          liste_choix= list(self.into)
       else:
          liste_choix=[]
          for e in into_courant:
              if e in self.into:
                 liste_choix.append(e)
       return liste_choix

   def info_erreur_item(self):
       return "La valeur n'est pas dans la liste des choix possibles"
          
class LongStr(ListVal):
   def info_erreur_item(self):
       return "Longueur de la chaine incorrecte"

   def verif_item(self,valeur):
       low=self.low
       high=self.high
       if valeur[0]=="'" and valeur[-1]=="'" :
          low=low+2
          high=high+2
       if len(valeur) < low :return 0
       if len(valeur) > high:return 0
       return 1
 
class RangeVal(ListVal):
   def verif_item(self,valeur):
       if valeur < self.low :return 0
       if valeur > self.high:return 0
       return 1

   def info_erreur_item(self) :
       return "La valeur doit �tre comprise entre %s et %s" % (self.low,self.high)

class TypeVal(ListVal):
   def verif_item(self,valeur):
       try:
          self.coerce(valeur)
       except:
          return 0
       return 1

class PairVal(ListVal):

   def info_erreur_item(self):
       return "La valeur saisie doit �tre paire"

   #ATTENTION METHODE SURCHARGEE: a resorber dans une future version
   def verif_item(self,valeur):
       if self.is_eval(valeur):
          return 1
       elif self.is_param(valeur):
          valeur=valeur.valeur
       elif self.is_unknown(valeur):
          return 0
       return valeur % 2 == 0

   def verif(self,valeur):
          if self.is_param(valeur):
             valeur=valeur.valeur
          if type(valeur) in (types.ListType,types.TupleType):
             for val in valeur:
                if not self.verif_item(val):
                   return 0
             return 1
          else:
             return self.verif_item(valeur)

   def verif_old(self,valeur):
       print "Ihm.I_MCSIMP.PairVal.verif: ",valeur
       return self.surcharge_verif(Noyau.N_VALIDATOR.PairVal.verif,valeur)

class InstanceVal(ListVal):
   def verif_item(self,valeur):
       if not isinstance(valeur,self.aClass): return 0
       return 1

class NoRepeat(ListVal):
   def info(self):
       return "pas de presence de doublon dans la liste"

   def info_erreur_liste(self):
       return "Les doublons ne sont pas permis"

   def verif_item(self,valeur):
       return 1

   def get_into(self,liste_courante=None,into_courant=None):
       """
          Methode get_into sp�cifique pour validateur NoRepeat
          on retourne une liste de choix qui ne contient aucune valeur de into_courant
          d�j� contenue dans liste_courante
       """
       if into_courant is None:
          return None
       else:
          liste_choix=[]
          for e in into_courant:
              if e in liste_choix: continue
              if liste_courante is not None and e in liste_courante: continue
              liste_choix.append(e)
          return liste_choix
 
class OrdList(ListVal):
   def verif_item(self,valeur):
       return 1

   def get_into(self,liste_courante=None,into_courant=None):
       """
          Methode get_into sp�cifique pour validateur OrdList 
          on retourne une liste de choix qui ne contient aucune valeur de into_courant
          dont la valeur est inf�rieure � la derni�re valeur de liste_courante, si
          elle est diff�rente de None.
       """
       if into_courant is None:
          return None
       elif not liste_courante :
          return into_courant
       else:
          liste_choix=[]
          last_val=liste_choix[-1]
          for e in into_courant:
              if self.ord=='croissant' and e <= last_val:continue
              if self.ord=='decroissant' and e >= last_val:continue
              liste_choix.append(e)
          return liste_choix

   def info_erreur_liste(self) :
       return "La liste doit �tre en ordre "+self.ord
          
