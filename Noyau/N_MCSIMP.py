""" 
    Ce module contient la classe MCSIMP qui sert � controler la valeur
    d'un mot-cl� simple par rapport � sa d�finition port�e par un objet
    de type ENTITE
"""

import N_OBJECT

class MCSIMP(N_OBJECT.OBJECT):
   """
   """
   nature = 'MCSIMP'
   def __init__(self,val,definition,nom,parent):
      """
         Attributs :

          - val : valeur du mot cl� simple

          - definition

          - nom

          - parent

        Autres attributs :

          - valeur : valeur du mot-cl� simple en tenant compte de la valeur par d�faut

      """
      self.definition=definition
      self.nom=nom
      self.val = val
      self.parent = parent
      self.valeur = self.GETVAL(self.val)
      if parent :
         self.jdc = self.parent.jdc
         self.niveau = self.parent.niveau
         self.etape = self.parent.etape
      else:
         # Le mot cle simple a �t� cr�� sans parent
         self.jdc = None
         self.niveau = None
         self.etape = None
         
   def GETVAL(self,val):
      """ 
          Retourne la valeur effective du mot-cl� en fonction
          de la valeur donn�e. Defaut si val == None
      """
      if (val is None and hasattr(self.definition,'defaut')) :
        return self.definition.defaut
      else:
        return val

   def get_valeur(self):
      """
          Retourne la "valeur" d'un mot-cl� simple.
          Cette valeur est utilis�e lors de la cr�ation d'un contexte 
          d'�valuation d'expressions � l'aide d'un interpr�teur Python
      """
      return self.valeur

   def get_val(self):
      """
          Une autre m�thode qui retourne une "autre" valeur du mot cl� simple.
          Elle est utilis�e par la m�thode get_mocle
      """
      return self.valeur

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitMCSIMP(self)

