""" 
    Ce module contient la classe MCFACT qui sert � controler la valeur
    d'un mot-cl� facteur par rapport � sa d�finition port�e par un objet
    de type ENTITE
"""

import N_MCCOMPO

class MCFACT(N_MCCOMPO.MCCOMPO):
   """
   """
   nature = "MCFACT"
   def __init__(self,val,definition,nom,parent):
      """
         Attributs :
          - val : valeur du mot cl� simple
          - definition
          - nom
          - parent
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
         # Le mot cle a �t� cr�� sans parent
         self.jdc = None
         self.niveau = None
         self.etape = None
      self.mc_liste=self.build_mc()
         
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
          Retourne la "valeur" d'un mot-cl� facteur qui est l'objet lui-meme.
          Cette valeur est utilis�e lors de la cr�ation d'un contexte 
          d'�valuation d'expressions � l'aide d'un interpr�teur Python
      """
      return self

   def get_val(self):
      """
          Une autre m�thode qui retourne une "autre" valeur du mot cl� facteur.
          Elle est utilis�e par la m�thode get_mocle
      """
      return [self]

   def __getitem__(self,key):
      """ 
          Dans le cas d un mot cle facteur unique on simule une liste de 
          longueur 1
      """
      if key == 0:return self
      return self.get_mocle(key)

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitMCFACT(self)

