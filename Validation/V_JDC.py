"""
   Ce module contient la classe mixin JDC qui porte les méthodes
   nécessaires pour réaliser la validation d'un objet de type JDC
   dérivé de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilisée par héritage multiple pour composer les traitements.
"""
# Modules Python
import string,types

# Modules EFICAS
import V_MCCOMPO
from Noyau.N_Exception import AsException
from Noyau.N_utils import AsType

class JDC(V_MCCOMPO.MCCOMPO):
   """
   """

   def report(self):
      """ 
          Methode pour generation d un rapport de validite
      """
      self.cr.purge()
      self.cr.debut="DEBUT CR validation : "+self.nom
      self.cr.fin="FIN CR validation :"+self.nom
      self.state = 'modified'
      self.isvalid(cr='oui')
      for e in self.etapes :
        if e.isactif():
          self.cr.add(e.report())
      return self.cr

   def isvalid(self,cr='non'):
      """
        Méthode booléenne qui retourne 0 si le JDC est invalide, 1 sinon
      """
      # FR : on prend en compte l'état du JDC ('unchanged','modified','undetermined')
      # afin d'accélérer le test de validité du JDC 
      if self.state == 'unchanged':
        return self.valid
      else:
        valid = 1
        texte,test = self.verif_regles()
        if test == 0:
          if cr == 'oui': self.cr.fatal(string.strip(texte))
          valid = 0
        if valid :
          for e in self.etapes:
            if not e.isactif() : continue
            if not e.isvalid():
              valid = 0
              break
        self.valid = valid
        return self.valid

   def verif_regles(self):
      """ 
         Effectue la vérification de validité des règles du jeu de commandes 
      """
      l_noms_etapes=self.get_l_noms_etapes()
      texte_global = ''
      test_global = 1
      for regle in self.regles :
        texte,test = regle.verif(l_noms_etapes)
        texte_global = texte_global + texte
        test_global = test_global*test
      return texte_global,test_global

   def get_l_noms_etapes(self):
      """ 
          Retourne la liste des noms des étapes de self 
      """
      l=[]
      for etape in self.etapes:
        l.append(etape.nom)
      return l

