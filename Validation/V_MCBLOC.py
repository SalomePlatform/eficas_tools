"""
   Ce module contient la classe mixin MCBLOC qui porte les m�thodes
   n�cessaires pour r�aliser la validation d'un objet de type MCBLOC
   d�riv� de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilis�e par h�ritage multiple pour composer les traitements.
"""
# Modules Python
import string

# Modules EFICAS
import V_MCCOMPO

class MCBLOC(V_MCCOMPO.MCCOMPO):
   """
      Cette classe a un attribut de classe :

      - txt_nat qui sert pour les comptes-rendus li�s � cette classe
   """

   txt_nat="Bloc :"

   def isvalid(self,sd='oui',cr='non'):
      """ 
         Methode pour verifier la validit� du MCBLOC. Cette m�thode
         peut etre appel�e selon plusieurs modes en fonction de la valeur
         de sd et de cr.

         Si cr vaut oui elle cr�e en plus un compte-rendu
         sd est pr�sent pour compatibilit� de l'interface mais ne sert pas
      """
      if self.state == 'unchanged' :
        return self.valid
      else:
        valid = 1
        if hasattr(self,'valid'):
          old_valid = self.valid
        else:
          old_valid = None
        for child in self.mc_liste :
          if not child.isvalid():
            valid = 0
            break
        # Apr�s avoir v�rifi� la validit� de tous les sous-objets, on v�rifie
        # la validit� des r�gles
        text_erreurs,test_regles = self.verif_regles()
        if not test_regles :
          if cr == 'oui' : self.cr.fatal(string.join(("R�gle(s) non respect�e(s) :", text_erreurs)))
          valid = 0
        self.valid = valid
        self.state = 'unchanged'
        if old_valid:
          if old_valid != self.valid : self.init_modif_up()
        return self.valid

