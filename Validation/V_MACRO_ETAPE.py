"""
   Ce module contient la classe mixin MACRO_ETAPE qui porte les méthodes
   nécessaires pour réaliser la validation d'un objet de type MACRO_ETAPE
   dérivé de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilisée par héritage multiple pour composer les traitements.
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
         Methode pour verifier la validité de l'objet ETAPE. Cette méthode
         peut etre appelée selon plusieurs modes en fonction de la valeur
         de sd et de cr.

         Si cr vaut oui elle crée en plus un compte-rendu.

         Cette méthode a plusieurs fonctions :

          - mettre à jour l'état de self (update)

          - retourner un indicateur de validité 0=non, 1=oui

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
        # on teste, si elle existe, le nom de la sd (sa longueur doit être <= 8 caractères)
        if self.sd != None :
          # la SD existe déjà : on regarde son nom
          if self.sd.get_name() != None :
            if len(self.sd.nom) > 8 :
              if cr == 'oui' :
                self.cr.fatal("Le nom de concept %s est trop long (8 caractères maxi)" %self.sd.nom)
              valid = 0
          if string.find(self.sd.nom,'sansnom') != -1 :
              # la SD est 'sansnom' : --> erreur
              if cr == 'oui' :
                self.cr.fatal("Pas de nom pour le concept retourné")
              valid = 0
          elif string.find(self.sd.nom,'SD_') != -1 :
              # la SD est 'SD_' cad son nom = son id donc pas de nom donné par utilisateur : --> erreur
              if cr == 'oui' :
                self.cr.fatal("Pas de nom pour le concept retourné")
              valid = 0
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
           Cette méthode met à jour le concept produit en fonction des conditions initiales :

            1- Il n'y a pas de concept retourné (self.definition.sd_prod == None)

            2- Le concept retourné n existait pas (self.sd == None)

            3- Le concept retourné existait. On change alors son type ou on le supprime

           En cas d'erreur (exception) on retourne un indicateur de validité de 0 sinon de 1
      """
      sd_prod=self.definition.sd_prod
      # On memorise le type retourné dans l attribut typret
      self.typret=None 
      if type(sd_prod) == types.FunctionType: 
        # Type de concept retourné calculé
        d=self.cree_dict_valeurs(self.mc_liste)
        try:
          # la sd_prod d'une macro a l'objet lui meme en premier argument
          # contrairement à une ETAPE ou PROC_ETAPE
          # Comme sd_prod peut invoquer la méthode type_sdprod qui ajoute
          # les concepts produits dans self.sdprods, il faut le mettre à zéro
          self.sdprods=[]
          sd_prod= apply(sd_prod,(self,),d)
        except:
          # Erreur pendant le calcul du type retourné
          if CONTEXT.debug:traceback.print_exc()
          self.sd=None
          if cr == 'oui' : 
             l=traceback.format_exception(sys.exc_info()[0],
                                          sys.exc_info()[1],
                                          sys.exc_info()[2])
             self.cr.fatal('Impossible d affecter un type au résultat\n'+string.join(l[2:]))
          return 0
      # on teste maintenant si la SD est r\351utilis\351e ou s'il faut la cr\351er
      if self.reuse:
        if AsType(self.reuse) != sd_prod:
          if cr == 'oui' : self.cr.fatal('Type de concept reutilise incompatible avec type produit')
          return 0
        self.sd=self.reuse
        return 1
      else:
        if sd_prod == None:# Pas de concept retourné
          # Que faut il faire de l eventuel ancien sd ?
          self.sd = None
        else:
          if self.sd: 
            # Un sd existe deja, on change son type
            self.sd.__class__=sd_prod
            self.typret=sd_prod
          else: 
            # Le sd n existait pas , on ne le crée pas
            self.typret=sd_prod
            if cr == 'oui' : self.cr.fatal("Concept retourné non défini")
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

