"""
   Ce module contient la classe mixin PROC_ETAPE qui porte les méthodes
   nécessaires pour réaliser la validation d'un objet de type PROC_ETAPE
   dérivé de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilisée par héritage multiple pour composer les traitements.
"""
# Modules Python
import string,types

# Modules EFICAS
import V_ETAPE
from Noyau.N_Exception import AsException
from Noyau.N_utils import AsType

class PROC_ETAPE(V_ETAPE.ETAPE):
   """
      On réutilise les méthodes report,verif_regles 
      de ETAPE par héritage.
   """

   def isvalid(self,sd='oui',cr='non'):
      """ 
         Methode pour verifier la validité de l'objet PROC_ETAPE. Cette méthode
         peut etre appelée selon plusieurs modes en fonction de la valeur
         de sd et de cr (sd n'est pas utilisé).

         Si cr vaut oui elle crée en plus un compte-rendu.

         Cette méthode a plusieurs fonctions :

          - retourner un indicateur de validité 0=non, 1=oui

          - produire un compte-rendu : self.cr

          - propager l'éventuel changement d'état au parent

      """
      if CONTEXT.debug : print "ETAPE.isvalid ",self.nom
      if self.state == 'unchanged' :
        return self.valid
      else:
        valid = 1
        if hasattr(self,'valid'):
          old_valid = self.valid
        else:
          old_valid = None
        # on teste les enfants
        for child in self.mc_liste :
          if not child.isvalid():
            valid = 0
            break
        # on teste les règles de self
        text_erreurs,test_regles = self.verif_regles()
        if not test_regles :
          if cr == 'oui' : self.cr.fatal(string.join(("Règle(s) non respectée(s) :", text_erreurs)))
          valid = 0
        if self.reste_val != {}:
          if cr == 'oui' :
            self.cr.fatal("Mots cles inconnus :" + string.join(self.reste_val.keys(),','))
          valid=0
        self.valid = valid
        self.state = 'unchanged'
        if old_valid:
          if old_valid != self.valid : self.init_modif_up()
        return self.valid


