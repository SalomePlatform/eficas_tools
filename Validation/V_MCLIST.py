"""
   Ce module contient la classe mixin MCList qui porte les m�thodes
   n�cessaires pour r�aliser la validation d'un objet de type MCList
   d�riv� de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilis�e par h�ritage multiple pour composer les traitements.
"""
# Modules Python
import string
import traceback

# Modules EFICAS
from Noyau import N_CR
from Noyau.N_Exception import AsException

class MCList:
   """
      Cette classe a deux attributs de classe :

      - CR qui sert � construire l'objet compte-rendu

      - txt_nat qui sert pour les comptes-rendus li�s � cette classe
   """

   CR=N_CR.CR
   txt_nat="Mot cle Facteur Multiple :"

   def isvalid(self,cr='non'):
      """ 
         Methode pour verifier la validit� du MCList. Cette m�thode
         peut etre appel�e selon plusieurs modes en fonction de la valeur
         de cr.

         Si cr vaut oui elle cr�e en plus un compte-rendu.

         On n'utilise pas d'attribut pour stocker l'�tat et on ne remonte pas 
         le changement d'�tat au parent (pourquoi ??)
      """
      if len(self.data) == 0 : return 0
      num = 0
      test = 1
      for i in self.data:
        num = num+1
        if not i.isvalid():
          if cr=='oui':
            self.cr.fatal(string.join(["L'occurrence n�",`num`," du mot-cl� facteur :",self.nom," n'est pas valide"]))
          test = 0
      return test

   def report(self):
      """ 
          G�n�re le rapport de validation de self 
      """
      self.cr=self.CR( debut = "Mot-cl� facteur multiple : "+self.nom,
                  fin = "Fin Mot-cl� facteur multiple : "+self.nom)
      # XXX j'ai mis l'�tat en commentaire car il n'est utilis� ensuite
      #self.state = 'modified'
      try :
        self.isvalid(cr='oui')
      except AsException,e:
        if CONTEXT.debug : traceback.print_exc()
        self.cr.fatal(string.join(["Mot-cl� facteur multiple : ",self.nom,str(e)]))
      for i in self.data:
        self.cr.add(i.report())
      return self.cr

