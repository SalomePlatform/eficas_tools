"""

"""
import string

class ASSD:
   """
      Classe de base pour definir des types de structures de donnees ASTER
      equivalent d un concept ASTER
   """
   idracine="SD"

   def __init__(self,etape=None,sd=None,reg='oui'):
      """
        reg est un param�tre qui vaut oui ou non :
          - si oui (d�faut) : on enregistre la SD aupr�s du JDC
          - si non : on ne l'enregistre pas
      """
      self.etape=etape
      self.sd=sd
      self.nom=None
      if etape:
        self.parent=etape.parent
      else:
        self.parent=CONTEXT.get_current_step()
      if self.parent :
         self.jdc = self.parent.get_jdc_root()
      else:
         self.jdc = None

      if not self.parent:
        self.id=None
      elif reg == 'oui' :
        self.id = self.parent.reg_sd(self)
      else :
        self.id = self.parent.o_register(self)

   def __getitem__(self,key):
      return self.etape[key]

   def is_object(valeur):
      """
          Indique si valeur est d'un type conforme � la classe (retourne 1) 
          ou non conforme (retourne 0)
      """
      return 0

   def get_name(self):
      """
          Retourne le nom de self, �ventuellement en le demandant au JDC
      """
      if not self.nom :
        try:
          self.nom=self.parent.get_name(self) or self.id
        except:
          self.nom=""
      if string.find(self.nom,'sansnom') != -1 or self.nom == '':
        self.nom = self.id
      return self.nom

   def supprime(self):
      """ 
          Cassage des boucles de r�f�rences pour destruction du JDC 
      """
      self.etape = None
      self.sd = None
      self.jdc = None
      self.parent = None

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitASSD(self)


class assd(ASSD):
   def is_object(valeur):
      """
          Indique si valeur est d'un type conforme � la classe (1) 
          ou non conforme (0)
          La classe assd est utilis�e pour valider tout objet
      """
      return 1


