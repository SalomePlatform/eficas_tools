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

# import rajout�s suite � l'ajout de Build_sd --> � r�sorber
import traceback
import Noyau
from Noyau import N_Exception
from Noyau.N_Exception import AsException
# fin import � r�sorber

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
        # dans le cas o� la SD est 'sansnom' ou 'SD_' on retourne la cha�ne vide
        return ''
      return sdname

   def is_reentrant(self):
      """ 
          Indique si la commande est reentrante
      """
      return self.definition.reentrant == 'o' 

   def init_modif(self):
      """
         Met l'�tat de l'�tape � : modifi�
         Propage la modification au parent
      """
      # Une action
      # doit etre realis�e apres init_modif et la validite reevalu�e
      # apres cette action. L'�tat modified de tous les objets doit etre
      # preserv�.
      self.state = 'modified'
      if self.parent:
        self.parent.init_modif()

   def fin_modif(self):
      """
          M�thode appel�e une fois qu'une modification a �t� faite afin de 
          d�clencher d'�ventuels traitements post-modification
          ex : INCLUDE et POURSUITE
      """
      if self.isvalid() :
         d=self.parent.get_contexte_apres(self)
      if self.parent:
        self.parent.fin_modif()

   def nomme_sd(self,nom) :
      """
          Cette m�thode a pour fonction de donner un nom (nom) au concept 
          produit par l'�tape (self).
            - si le concept n'existe pas, on essaye de le cr�er (� condition que l'�tape soit valide ET non r�entrante)
            - si il existe d�j�, on le renomme et on r�percute les changements dans les autres �tapes    
          Les valeurs de retour sont :
            - 0 si le nommage n'a pas pu etre men� � son terme,
            - 1 dans le cas contraire
      """
      # Le nom d'un concept doit etre un identificateur Python (toujours vrai ?)
      if not concept_re.match(nom):
         return 0,"Un nom de concept doit etre un identificateur Python"

      if len(nom) > 8 and self.jdc.definition.code == 'ASTER':
        return 0,"Nom de concept trop long (maxi 8 caract�res)"

      self.init_modif()
      #
      # On verifie d'abord si les mots cles sont valides
      #
      if not self.isvalid(sd='non') : return 0,"Nommage du concept refus� : l'op�rateur n'est pas valide"
      #
      # Cas particulier des op�rateurs obligatoirement r�entrants
      #
      if self.definition.reentrant == 'o':
	self.sd = self.reuse = self.jdc.get_sd_avant_etape(nom,self)
        if self.sd != None :
          self.sdnom=self.sd.nom
          return 1,"Concept existant"
        else:
          return 0,"Op�rateur r�entrant mais concept non existant"
      #
      # Cas particulier des op�rateurs facultativement r�entrants
      #
      old_reuse=None
      if self.definition.reentrant == 'f' :
        sd = self.jdc.get_sd_avant_etape(nom,self)
        if sd != None :
	  # FR : il faut tester que la sd trouv�e est du bon type !!!!!!!!!!!!!!!!!
	  if isinstance(sd,self.get_type_produit()) :
             self.sd = self.reuse = sd
             self.sdnom = sd.nom
             return 1,"Op�rateur facultativement r�entrant et concept existant trouv�"
	  else:
	     return 0,"Concept d�j� existant et de mauvais type"
        else :
          # il faut enlever le lien vers une SD existante car si on passe ici
	  # cela signifie que l'op�rateur n'est pas utilis� en mode r�entrant.
	  # Si on ne fait pas cela, on risque de modifier une SD produite par un autre op�rateur
	  if self.reuse :
             old_reuse=self.reuse
	     self.sd = self.reuse = self.sdnom = None
      #
      # On est dans le cas ou l'op�rateur n'est pas r�entrant ou est facultativement reentrant
      # mais est utilis� en mode non r�entrant
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
            # On peut donc cr�er le concept retourn�.
            # Il est cr�� sans nom mais enregistr� dans la liste des concepts existants
            self.get_sd_prod()
            # Il suffit de changer son attribut nom pour le nommer
            self.sd.nom = nom
            self.sdnom=nom
            return 1,"Nommage du concept effectu�"
      else :
          old_nom=self.sd.nom
          if string.find(old_nom,'sansnom') :
            # Dans le cas o� old_nom == sansnom, isvalid retourne 0 alors que ...
	    # par contre si le concept existe et qu'il s'appelle sansnom c'est que l'�tape est valide
	    # on peut donc le nommer sans test pr�alable
            if self.parent.get_sd_autour_etape(nom,self):
              return 0,"Nommage du concept refuse : un concept de meme nom existe deja"
            else:
	      self.sd.nom=nom
              self.sdnom=nom
              return 1,"Nommage du concept effectu�"
          if self.isvalid() :
            # Normalement l appel de isvalid a mis a jour le concept produit (son type)
            # Il suffit de sp�cifier l attribut nom de sd pour le nommer si le nom n est pas
            # deja attribu�
            if self.parent.get_sd_autour_etape(nom,self):
              return 0,"Nommage du concept refuse : un concept de meme nom existe deja"
            else:
              self.sd.nom=nom
              self.sdnom=nom
              return 1,"Nommage du concept effectu�"
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
          et � la liste des sd
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
            Un op�rateur n a qu un concept produit 
            Une procedure n'en a aucun
            Une macro en a en g�n�ral plus d'un
      """
      if not self.is_reentrant() :
        # l'�tape n'est pas r�entrante
        # le concept retourn� par l'�tape est � supprimer car il �tait 
        # cr�� par l'�tape
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
          suite � la disparition du concept sd
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

#ATTENTION SURCHARGE: cette methode doit etre gard�e en synchronisation avec Noyau
   def make_register(self):
      """
         Initialise les attributs jdc, id, niveau et r�alise les
         enregistrements n�cessaires
         Pour EFICAS, on tient compte des niveaux
         Surcharge la methode make_register du package Noyau
      """
      if self.parent :
         self.jdc = self.parent.get_jdc_root()
         self.id=   self.parent.register(self)
         if self.definition.niveau :
            # La d�finition est dans un niveau. En plus on
            # l'enregistre dans le niveau
            self.nom_niveau_definition = self.definition.niveau.nom
            self.niveau = self.parent.dict_niveaux[self.nom_niveau_definition]
            self.niveau.register(self)
         else:
            # La d�finition est au niveau global
            self.nom_niveau_definition = 'JDC'
            self.niveau=self.parent
      else:
         self.jdc = self.parent =None
         self.id=None
         self.niveau=None

   def copy(self):
      """ M�thode qui retourne une copie de self non enregistr�e aupr�s du JDC
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
          Retourne la liste des noms de concepts utilis�s � l'int�rieur de la commande
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
          Retourne la liste des concepts qui sont utilis�s � l'int�rieur d'une commande
          ( comme valorisation d'un MCS) 
      """
      l=[]
      for child in self.mc_liste:
        l.extend(child.get_sd_utilisees())
      return l

   def get_genealogie(self):
      """ 
          Retourne la liste des noms des ascendants de l'objet self
          en s'arretant � la premi�re ETAPE rencontr�e
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
        V�rifie que les structures de donn�es utilis�es dans self existent bien dans le contexte
	avant �tape, sinon enl�ve la r�f�rence � ces concepts
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
         # Si on poursuit, on a le choix entre deux possibilit�s :
         # 1. on annule la sd associ�e � self
         # 2. on la conserve mais il faut la retourner
         # En plus il faut rendre coherents sdnom et sd.nom
         self.sd=None
         self.sdnom=None
         self.state="unchanged"
         self.valid=0

      return self.sd

   def Build_sd_old(self,nom):
      """
         Construit le concept produit de l'op�rateur. Deux cas 
         peuvent se pr�senter :
        
           - le parent n'est pas d�fini. Dans ce cas, l'�tape prend en charge la cr�ation 
             et le nommage du concept.

           - le parent est d�fini. Dans ce cas, l'�tape demande au parent la cr�ation et 
             le nommage du concept.

      """
      if not self.isactif():return
      # FR : attention cette m�thode ne devrait pas se trouver l� car elle surcharge celle qui 
      # se trouve dans N_ETAPE.py et elle est partie int�grante du noyau, mais, suite � l'absence de 
      # test de validit� de l'op�rateur avant d'essayer de d�terminer la sd produite, on n'arrivait
      # pas � relire avec EFICAS un fichier contenant une �tape encore incompl�te du style :
      #  sansnom = AFFE_CHAR_CINE(MODELE=None)
      # Suite � la stabilisation du noyau d'Aster, je n'ai pas eu d'autre solution que de surcharger
      # cette m�thode ici en rajoutant le test manquant ...
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
         # Si on poursuit, on a le choix entre deux possibilit�s :
         # 1. on annule la sd associ�e � self
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
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        
     
