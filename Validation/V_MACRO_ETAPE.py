"""
   Ce module contient la classe mixin MACRO_ETAPE qui porte les m�thodes
   n�cessaires pour r�aliser la validation d'un objet de type MACRO_ETAPE
   d�riv� de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilis�e par h�ritage multiple pour composer les traitements.
"""
# Modules Python
import string,types,sys
import traceback

# Modules EFICAS
import V_MCCOMPO
import V_ETAPE
from Noyau.N_Exception import AsException
from Noyau.N_utils import AsType

class MACRO_ETAPE(V_ETAPE.ETAPE):
   """
   """

   def isvalid(self,sd='oui',cr='non'):
      """ 
         Methode pour verifier la validit� de l'objet ETAPE. Cette m�thode
         peut etre appel�e selon plusieurs modes en fonction de la valeur
         de sd et de cr.

         Si cr vaut oui elle cr�e en plus un compte-rendu.

         Cette m�thode a plusieurs fonctions :

          - mettre � jour l'�tat de self (update)

          - retourner un indicateur de validit� 0=non, 1=oui

          - produire un compte-rendu : self.cr

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
        # on teste, si elle existe, le nom de la sd (sa longueur doit �tre <= 8 caract�res)
        if self.sd != None :
          # la SD existe d�j� : on regarde son nom
          if self.sd.get_name() != None :
            if len(self.sd.nom) > 8 :
              if cr == 'oui' :
                self.cr.fatal("Le nom de concept %s est trop long (8 caract�res maxi)" %self.sd.nom)
              valid = 0
          if string.find(self.sd.nom,'sansnom') != -1 :
              # la SD est 'sansnom' : --> erreur
              if cr == 'oui' :
                self.cr.fatal("Pas de nom pour le concept retourn�")
              valid = 0
          elif string.find(self.sd.nom,'SD_') != -1 :
              # la SD est 'SD_' cad son nom = son id donc pas de nom donn� par utilisateur : --> erreur
              if cr == 'oui' :
                self.cr.fatal("Pas de nom pour le concept retourn�")
              valid = 0
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
        if sd == 'oui' and valid:
          valid = self.update_sdprod(cr)
        # Si la macro comprend des etapes internes, on teste leur validite
        for e in self.etapes:
          if not e.isvalid():
            valid=0
            break
        self.valid = valid
        self.state = 'unchanged'
        if old_valid:
          if old_valid != self.valid : self.init_modif_up()
        return self.valid

   def update_sdprod(self,cr='non'):
      """ 
           Cette m�thode met � jour le concept produit en fonction des conditions initiales :

            1- Il n'y a pas de concept retourn� (self.definition.sd_prod == None)

            2- Le concept retourn� n existait pas (self.sd == None)

            3- Le concept retourn� existait. On change alors son type ou on le supprime

           En cas d'erreur (exception) on retourne un indicateur de validit� de 0 sinon de 1
      """
      sd_prod=self.definition.sd_prod
      # On memorise le type retourn� dans l attribut typret
      self.typret=None 
      if type(sd_prod) == types.FunctionType: 
        # Type de concept retourn� calcul�
        d=self.cree_dict_valeurs(self.mc_liste)
        try:
          # la sd_prod d'une macro a l'objet lui meme en premier argument
          # contrairement � une ETAPE ou PROC_ETAPE
          # Comme sd_prod peut invoquer la m�thode type_sdprod qui ajoute
          # les concepts produits dans self.sdprods, il faut le mettre � z�ro
          self.sdprods=[]
          sd_prod= apply(sd_prod,(self,),d)
        except:
          # Erreur pendant le calcul du type retourn�
          if CONTEXT.debug:traceback.print_exc()
          self.sd=None
          if cr == 'oui' : 
             l=traceback.format_exception(sys.exc_info()[0],
                                          sys.exc_info()[1],
                                          sys.exc_info()[2])
             self.cr.fatal('Impossible d affecter un type au r�sultat\n'+string.join(l[2:]))
          return 0
      # on teste maintenant si la SD est r\351utilis\351e ou s'il faut la cr\351er
      if self.reuse:
        if AsType(self.reuse) != sd_prod:
          if cr == 'oui' : self.cr.fatal('Type de concept reutilise incompatible avec type produit')
          return 0
        self.sd=self.reuse
        return 1
      else:
        if sd_prod == None:# Pas de concept retourn�
          # Que faut il faire de l eventuel ancien sd ?
          self.sd = None
        else:
          if self.sd: 
            # Un sd existe deja, on change son type
            self.sd.__class__=sd_prod
            self.typret=sd_prod
          else: 
            # Le sd n existait pas , on ne le cr�e pas
            self.typret=sd_prod
            if cr == 'oui' : self.cr.fatal("Concept retourn� non d�fini")
            return 0
        if self.definition.reentrant == 'o':
          self.reuse = self.sd
        return 1

   def report(self):
      """ 
          Methode pour la generation d un rapport de validation
      """
      V_ETAPE.ETAPE.report(self)
      for e in self.etapes :
        self.cr.add(e.report())
      return self.cr

