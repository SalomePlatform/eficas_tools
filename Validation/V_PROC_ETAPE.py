"""
   Ce module contient la classe mixin PROC_ETAPE qui porte les m�thodes
   n�cessaires pour r�aliser la validation d'un objet de type PROC_ETAPE
   d�riv� de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilis�e par h�ritage multiple pour composer les traitements.
"""
# Modules Python
import string,types

# Modules EFICAS
import V_ETAPE
from Noyau.N_Exception import AsException
from Noyau.N_utils import AsType

class PROC_ETAPE(V_ETAPE.ETAPE):
   """
      On r�utilise les m�thodes report,verif_regles 
      de ETAPE par h�ritage.
   """

   def isvalid(self,sd='oui',cr='non'):
      """ 
         Methode pour verifier la validit� de l'objet PROC_ETAPE. Cette m�thode
         peut etre appel�e selon plusieurs modes en fonction de la valeur
         de sd et de cr (sd n'est pas utilis�).

         Si cr vaut oui elle cr�e en plus un compte-rendu.

         Cette m�thode a plusieurs fonctions :

          - retourner un indicateur de validit� 0=non, 1=oui

          - produire un compte-rendu : self.cr

          - propager l'�ventuel changement d'�tat au parent

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
        # on teste les r�gles de self
        text_erreurs,test_regles = self.verif_regles()
        if not test_regles :
          if cr == 'oui' : self.cr.fatal(string.join(("R�gle(s) non respect�e(s) :", text_erreurs)))
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


