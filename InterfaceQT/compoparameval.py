# -*- coding: utf-8 -*-

"""
Ce module contient les classes permettant de définir les objets graphiques
représentant un objet de type PARAMETRE_EVAL, cad le panneau et l'item de l'arbre
d'EFICAS
"""

# import modules Python
import string

# import modules EFICAS

from Editeur import Objecttreeitem


import browser
from qt import *

class Node(browser.JDCNode): pass
##    def getPanel(self):
##        """        
##        """    
##        return PARAM_EVALPanel( self, self.editor )


class PARAM_EVALTreeItem(Objecttreeitem.ObjectTreeItem):
    """
    Classe servant a définir l'item porté par le noeud de l'arbre d'EFICAS
    qui représente le PARAMETRE
    """
    itemNode=Node
##    panel = PARAM_EVALPanel

    def init(self):
      self.setfunction = self.set_valeur

# ---------------------------------------------------------------------------
#                   API du PARAMETRE pour l'arbre 
# ---------------------------------------------------------------------------

    def GetIconName(self):
      """
      Retourne le nom de l'icone associée au noeud qui porte self,
      dépendant de la validité de l'objet
      NB : un PARAMETRE est toujours valide ...
      """
      if self.isactif():
          if self.isvalid():
              return "ast-green-square"
          else:
              return "ast-red-square"
      else:
          return "ast-white-square"

    def GetLabelText(self):
        """ Retourne 3 valeurs :
        - le texte a afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return 'EVAL',Fonte_PARAMETRE,None

    def GetText(self):
      """
      Retourne le texte a afficher apres le nom de la commande (ici apres 'parametre')
      Ce texte est tronqué a 25 caracteres
      """
      texte = repr(self.object)
      texte = string.split(texte,'\n')[0]
      if len(texte) < 25 :
          return texte
      else :
          return texte[0:24]+'...'

    def GetSubList(self):
      """
      Retourne la liste des fils de self
      """
      return []
    
# ---------------------------------------------------------------------------
#       Méthodes permettant la modification et la lecture des attributs
#       du parametre = API graphique du PARAMETRE pour Panel et EFICAS
# ---------------------------------------------------------------------------

    def isvalid(self):
      """
      Indique si l'objet pointé par self est valide
      """
      return self.object.isvalid()
    
    def get_valeur(self):
      """
      Retourne une chaine représentant la valeur de l'objet PARAMETRE
      cad de l'objet class_eval.EVAL
      """
      return self.object.get_valeur() or ''

    def get_nom(self):
      """
      Retourne le nom du parametre
      """
      return self.object.get_nom()

    def set_valeur(self,new_valeur):
      """
      Affecte new_valeur a l'objet PARAMETRE_EVAL
      """
      # on construit le texte de la nouvelle valeur
      new_valeur = 'EVAL("""'+new_valeur+'""")'
      # on affecte la nouvelle valeur a self.object
      self.object.set_valeur(new_valeur)

    def set_nom(self,new_nom):
      """
      Renomme le parametre
      """
      self.object.set_nom(new_nom)

    def get_fr(self):
      """
      Retourne le fr associé au parametre, cad la bulle d'aide pour EFICAS
      """
      return "Définition d'un parametre de type EVAL"

    def verif_nom(self,nom):
      """
      Lance la vérification de validité du nom passé en argument
      """
      return self.object.verif_nom(nom = nom)

    def verif_eval(self,valeur):
      """
      Lance la vérification de validité de l'expression EVAL passée en argument
      """
      return self.object.verif_eval(exp_eval = valeur)

    def save_parametre_eval(self,new_nom,new_val):
      """
      Vérifie si (new_nom,new_val) définit bien un EVAL licite :
          - si oui, stocke ces parametres comme nouveaux parametres de l'EVAL courant et retourne 1
          - si non, laisse les parametres anciens de EVAL inchangés et retourne 0
      """
      test,erreur = self.object.verif_parametre_eval(param=(new_nom,new_val))
      if test :
          # la formule est bien correcte : on sauve les nouveaux parametres
          self.object.update(param=(new_nom,new_val))
      return test,erreur
      
import Extensions.parametre_eval
treeitem =PARAM_EVALTreeItem
objet = Extensions.parametre_eval.PARAMETRE_EVAL
