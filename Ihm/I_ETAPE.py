#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
"""
# Modules Python
import sys,re
import string,types
from copy import copy

# Objet re pour controler les identificateurs Python
concept_re=re.compile(r'[a-zA-Z_]\w*$')

# import rajoutés suite à l'ajout de Build_sd --> à résorber
import traceback
import Noyau
from Noyau import N_Exception
from Noyau.N_Exception import AsException
# fin import à résorber

# Modules EFICAS
import I_MCCOMPO

class ETAPE(I_MCCOMPO.MCCOMPO):

   def ident(self):
      return self.nom

   def get_sdname(self):
      if CONTEXT.debug : print "SDNAME ",self.reuse,self.sd,self.sd.get_name()
      sdname=''
      if self.reuse != None:
        sdname= self.reuse.get_name()
      else:
        if self.sd:sdname=self.sd.get_name()
      if string.find(sdname,'sansnom') != -1 or string.find(sdname,'SD_') != -1:
        # dans le cas où la SD est 'sansnom' ou 'SD_' on retourne la chaîne vide
        return ''
      return sdname

   def is_reentrant(self):
      """ 
          Indique si la commande est reentrante
      """
      return self.definition.reentrant == 'o' 

   def init_modif(self):
      """
         Met l'état de l'étape à : modifié
         Propage la modification au parent
      """
      # Une action
      # doit etre realisée apres init_modif et la validite reevaluée
      # apres cette action. L'état modified de tous les objets doit etre
      # preservé.
      self.state = 'modified'
      if self.parent:
        self.parent.init_modif()

   def fin_modif(self):
      """
          Méthode appelée une fois qu'une modification a été faite afin de 
          déclencher d'éventuels traitements post-modification
          ex : INCLUDE et POURSUITE
      """
      if self.isvalid() :
         d=self.parent.get_contexte_apres(self)
      if self.parent:
        self.parent.fin_modif()

   def nomme_sd(self,nom) :
      """
          Cette méthode a pour fonction de donner un nom (nom) au concept 
          produit par l'étape (self).
            - si le concept n'existe pas, on essaye de le créer (à condition que l'étape soit valide ET non réentrante)
            - si il existe déjà, on le renomme et on répercute les changements dans les autres étapes    
          Les valeurs de retour sont :
            - 0 si le nommage n'a pas pu etre mené à son terme,
            - 1 dans le cas contraire
      """
      # Le nom d'un concept doit etre un identificateur Python (toujours vrai ?)
      if not concept_re.match(nom):
         return 0,"Un nom de concept doit etre un identificateur Python"

      if len(nom) > 8 and self.jdc.definition.code == 'ASTER':
        return 0,"Nom de concept trop long (maxi 8 caractères)"

      self.init_modif()
      #
      # On verifie d'abord si les mots cles sont valides
      #
      if not self.isvalid(sd='non') : return 0,"Nommage du concept refusé : l'opérateur n'est pas valide"
      #
      # Cas particulier des opérateurs obligatoirement réentrants
      #
      if self.definition.reentrant == 'o':
	self.sd = self.reuse = self.jdc.get_sd_avant_etape(nom,self)
        if self.sd != None :
          self.sdnom=self.sd.nom
          return 1,"Concept existant"
        else:
          return 0,"Opérateur réentrant mais concept non existant"
      #
      # Cas particulier des opérateurs facultativement réentrants
      #
      old_reuse=None
      if self.definition.reentrant == 'f' :
        sd = self.jdc.get_sd_avant_etape(nom,self)
        if sd != None :
	  # FR : il faut tester que la sd trouvée est du bon type !!!!!!!!!!!!!!!!!
	  if isinstance(sd,self.get_type_produit()) :
             self.sd = self.reuse = sd
             self.sdnom = sd.nom
             return 1,"Opérateur facultativement réentrant et concept existant trouvé"
	  else:
	     return 0,"Concept déjà existant et de mauvais type"
        else :
          # il faut enlever le lien vers une SD existante car si on passe ici
	  # cela signifie que l'opérateur n'est pas utilisé en mode réentrant.
	  # Si on ne fait pas cela, on risque de modifier une SD produite par un autre opérateur
	  if self.reuse :
             old_reuse=self.reuse
	     self.sd = self.reuse = self.sdnom = None
      #
      # On est dans le cas ou l'opérateur n'est pas réentrant ou est facultativement reentrant
      # mais est utilisé en mode non réentrant
      #
      if self.sd == None :
          if self.parent.get_sd_autour_etape(nom,self):
            # Un concept de ce nom existe dans le voisinage de l'etape courante
            # On retablit l'ancien concept reentrant s'il existait
            if old_reuse:
               self.sd=self.reuse=old_reuse
               self.sdnom=old_reuse.nom
            return 0,"Nommage du concept refuse : un concept de meme nom existe deja"
          else:
            # Il n'existe pas de concept de ce nom dans le voisinage de l'etape courante
            # On peut donc créer le concept retourné.
            # Il est créé sans nom mais enregistré dans la liste des concepts existants
            self.get_sd_prod()
            # Il suffit de changer son attribut nom pour le nommer
            self.sd.nom = nom
            self.sdnom=nom
            return 1,"Nommage du concept effectué"
      else :
          old_nom=self.sd.nom
          if string.find(old_nom,'sansnom') :
            # Dans le cas où old_nom == sansnom, isvalid retourne 0 alors que ...
	    # par contre si le concept existe et qu'il s'appelle sansnom c'est que l'étape est valide
	    # on peut donc le nommer sans test préalable
            if self.parent.get_sd_autour_etape(nom,self):
              return 0,"Nommage du concept refuse : un concept de meme nom existe deja"
            else:
	      self.sd.nom=nom
              self.sdnom=nom
              return 1,"Nommage du concept effectué"
          if self.isvalid() :
            # Normalement l appel de isvalid a mis a jour le concept produit (son type)
            # Il suffit de spécifier l attribut nom de sd pour le nommer si le nom n est pas
            # deja attribué
            if self.parent.get_sd_autour_etape(nom,self):
              return 0,"Nommage du concept refuse : un concept de meme nom existe deja"
            else:
              self.sd.nom=nom
              self.sdnom=nom
              return 1,"Nommage du concept effectué"
          else:
            # Normalement on ne devrait pas passer ici
            return 0,'Normalement on ne devrait pas passer ici'

   def get_sdprods(self,nom_sd):
      """ 
         Fonction : retourne le concept produit par l etape de nom nom_sd
         s il existe sinon None
      """
      if self.sd:
        if self.sd.nom == nom_sd:return self.sd

   def active(self):
      """
          Rend l'etape courante active.
          Il faut ajouter la sd si elle existe au contexte global du JDC
          et à la liste des sd
      """
      if self.actif:return
      self.actif = 1
      if not self.sd : return
      try:
        self.jdc.append_sdprod(self.sd)
      except:
        pass

   def inactive(self):
      """
          Rend l'etape courante inactive
          Il faut supprimer la sd du contexte global du JDC
          et de la liste des sd
      """
      self.actif = 0
      if not self.sd : return
      self.jdc.del_sdprod(self.sd)
      self.jdc.delete_concept_after_etape(self,self.sd)

   def control_sdprods(self,d):
      """
          Cette methode doit updater le contexte fournit par
          l'appelant en argument (d) en fonction de sa definition
          tout en verifiant que ses concepts produits ne sont pas 
          deja definis dans le contexte
      """
      if type(self.definition.op_init) == types.FunctionType:
        apply(self.definition.op_init,(self,d))
      if self.sd:
        if d.has_key(self.sd.nom):
           # Le concept est deja defini
           if self.reuse and self.reuse is d[self.sd.nom]:
              # Le concept est reutilise : situation normale
              pass
           else:
              # Redefinition du concept, on l'annule
              #XXX on pourrait simplement annuler son nom pour conserver les objets
              # l'utilisateur n'aurait alors qu'a renommer le concept (faisable??)
              self.sd=self.reuse=self.sdnom=None
              self.init_modif()
        else:
           # Le concept n'est pas defini, on peut updater d
           d[self.sd.nom]=self.sd

   def supprime_sdprods(self):
      """ 
            Fonction:
            Lors d'une destruction d'etape, detruit tous les concepts produits
            Un opérateur n a qu un concept produit 
            Une procedure n'en a aucun
            Une macro en a en général plus d'un
      """
      if not self.is_reentrant() :
        # l'étape n'est pas réentrante
        # le concept retourné par l'étape est à supprimer car il était 
        # créé par l'étape
        if self.sd != None :
          self.parent.del_sdprod(self.sd)
          self.parent.delete_concept(self.sd)

   def delete_concept(self,sd):
      """ 
          Inputs :
             - sd=concept detruit
          Fonction :
          Mettre a jour les mots cles de l etape et eventuellement 
          le concept produit si reuse
          suite à la disparition du concept sd
          Seuls les mots cles simples MCSIMP font un traitement autre 
          que de transmettre aux fils
      """
      if self.reuse and self.reuse == sd:
        self.sd=self.reuse=None
        self.init_modif()
      for child in self.mc_liste :
        child.delete_concept(sd)

   def replace_concept(self,old_sd,sd):
      """
          Inputs :
             - old_sd=concept remplace
             - sd = nouveau concept 
          Fonction :
          Mettre a jour les mots cles de l etape et eventuellement
          le concept produit si reuse
          suite au remplacement  du concept old_sd
      """
      if self.reuse and self.reuse == old_sd:
        self.sd=self.reuse=sd
        self.init_modif()
      for child in self.mc_liste :
        child.replace_concept(old_sd,sd)

#ATTENTION SURCHARGE: cette methode doit etre gardée en synchronisation avec Noyau
   def make_register(self):
      """
         Initialise les attributs jdc, id, niveau et réalise les
         enregistrements nécessaires
         Pour EFICAS, on tient compte des niveaux
         Surcharge la methode make_register du package Noyau
      """
      if self.parent :
         self.jdc = self.parent.get_jdc_root()
         self.id=   self.parent.register(self)
         if self.definition.niveau :
            # La définition est dans un niveau. En plus on
            # l'enregistre dans le niveau
            self.nom_niveau_definition = self.definition.niveau.nom
            self.niveau = self.parent.dict_niveaux[self.nom_niveau_definition]
            self.niveau.register(self)
         else:
            # La définition est au niveau global
            self.nom_niveau_definition = 'JDC'
            self.niveau=self.parent
      else:
         self.jdc = self.parent =None
         self.id=None
         self.niveau=None

   def copy(self):
      """ Méthode qui retourne une copie de self non enregistrée auprès du JDC
          et sans sd 
      """
      etape = copy(self)
      etape.sd = None
      etape.state = 'modified'
      etape.reuse = None
      etape.sdnom = None
      etape.etape=etape
      etape.mc_liste=[]
      for objet in self.mc_liste:
        new_obj = objet.copy()
        new_obj.reparent(etape)
        etape.mc_liste.append(new_obj)
      return etape

   def get_noms_sd_oper_reentrant(self):
      """ 
          Retourne la liste des noms de concepts utilisés à l'intérieur de la commande
          qui sont du type que peut retourner cette commande 
      """
      liste_sd = self.get_sd_utilisees()
      l_noms = []
      if type(self.definition.sd_prod) == types.FunctionType:
        d=self.cree_dict_valeurs(self.mc_liste)
        try:
          classe_sd_prod = apply(self.definition.sd_prod,(),d)
        except:
          return []
      else:
        classe_sd_prod = self.definition.sd_prod
      for sd in liste_sd :
        if sd.__class__ is classe_sd_prod : l_noms.append(sd.nom)
      l_noms.sort()
      return l_noms

   def get_sd_utilisees(self):
      """ 
          Retourne la liste des concepts qui sont utilisés à l'intérieur d'une commande
          ( comme valorisation d'un MCS) 
      """
      l=[]
      for child in self.mc_liste:
        l.extend(child.get_sd_utilisees())
      return l

   def get_genealogie(self):
      """ 
          Retourne la liste des noms des ascendants de l'objet self
          en s'arretant à la première ETAPE rencontrée
      """
      return [self.nom]

   def reparent(self,parent):
     """
         Cette methode sert a reinitialiser la parente de l'objet
     """
     self.parent=parent
     self.jdc=parent.get_jdc_root()
     self.etape=self
     for mocle in self.mc_liste:
        mocle.reparent(self)

   def verif_existence_sd(self):
     """
        Vérifie que les structures de données utilisées dans self existent bien dans le contexte
	avant étape, sinon enlève la référence à ces concepts
     """
     for motcle in self.mc_liste :
         motcle.verif_existence_sd()
     
#ATTENTION SURCHARGE: a garder en synchro ou a reintegrer dans le Noyau
   def Build_sd(self,nom):
      """
           Methode de Noyau surchargee pour poursuivre malgre tout
           si une erreur se produit pendant la creation du concept produit
      """
      try:
         sd=Noyau.N_ETAPE.ETAPE.Build_sd(self,nom)
      except AsException,e:
         # Une erreur s'est produite lors de la construction du concept
         # Comme on est dans EFICAS, on essaie de poursuivre quand meme
         # Si on poursuit, on a le choix entre deux possibilités :
         # 1. on annule la sd associée à self
         # 2. on la conserve mais il faut la retourner
         # En plus il faut rendre coherents sdnom et sd.nom
         self.sd=None
         self.sdnom=None
         self.state="unchanged"
         self.valid=0

      return self.sd

   def Build_sd_old(self,nom):
      """
         Construit le concept produit de l'opérateur. Deux cas 
         peuvent se présenter :
        
           - le parent n'est pas défini. Dans ce cas, l'étape prend en charge la création 
             et le nommage du concept.

           - le parent est défini. Dans ce cas, l'étape demande au parent la création et 
             le nommage du concept.

      """
      if not self.isactif():return
      # FR : attention cette méthode ne devrait pas se trouver là car elle surcharge celle qui 
      # se trouve dans N_ETAPE.py et elle est partie intégrante du noyau, mais, suite à l'absence de 
      # test de validité de l'opérateur avant d'essayer de déterminer la sd produite, on n'arrivait
      # pas à relire avec EFICAS un fichier contenant une étape encore incomplète du style :
      #  sansnom = AFFE_CHAR_CINE(MODELE=None)
      # Suite à la stabilisation du noyau d'Aster, je n'ai pas eu d'autre solution que de surcharger
      # cette méthode ici en rajoutant le test manquant ...
      # CCAR : cette modification ne corrige le probleme qu'en partie. Il faudrait probablement
      # supprimer les erreurs fatales (exception ) et retourner systematiquement un objet produit
      # meme en cas d'erreur et reporter l'emission du message d'erreur a la phase de validation
      #
      if not self.isvalid(sd='non') : return
      self.sdnom=nom
      try:
         if self.parent:
            sd= self.parent.create_sdprod(self,nom)
            if type(self.definition.op_init) == types.FunctionType: 
               apply(self.definition.op_init,(self,self.parent.g_context))
         else:
            sd=self.get_sd_prod()
            # On n'utilise pas self.definition.op_init car self.parent 
            # n'existe pas
            if sd != None and self.reuse == None:
               # On ne nomme le concept que dans le cas de non reutilisation 
               # d un concept
               sd.nom=nom
         if self.jdc and self.jdc.par_lot == "NON" :
            self.Execute()
         return sd
      except AsException,e:
         # Une erreur s'est produite lors de la construction du concept
         # Comme on est dans EFICAS, on essaie de poursuivre quand meme
         # Si on poursuit, on a le choix entre deux possibilités :
         # 1. on annule la sd associée à self
         # 2. on la conserve mais il faut la retourner
         # En plus il faut rendre coherents sdnom et sd.nom
         self.sd=None
         self.sdnom=None
         self.state="unchanged"
         self.valid=0
         return self.sd

         #raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
         #                     'fichier : ',self.appel[1],e)
      except EOFError:
         # XXX Normalement le contexte courant doit etre le parent.
         # Il n'y a pas de raison de remettre le contexte au parent
         #self.reset_current_step()
         raise
      except :
         l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
         raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                           'fichier : ',self.appel[1]+'\n',
                            string.join(l))
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        
     
