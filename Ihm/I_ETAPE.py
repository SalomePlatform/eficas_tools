"""
"""
# Modules Python
import string,types
from copy import copy

# Modules EFICAS
import I_MCCOMPO

class ETAPE(I_MCCOMPO.MCCOMPO):

   def __init__(self):
      self.niveau=self.jdc

   def ident(self):
      return self.nom

   def get_fr(self):
      """ 
         Retourne l'attribut fr de self.definition 
      """
      try:
         return self.definition.fr
      except:
         return ''

   def get_sdname(self):
      if CONTEXT.debug : print "SDNAME ",self.reuse,self.sd,self.sd.get_name()
      if self.reuse != None:
        sdname= self.reuse.get_name()
      else:
        sdname=self.sd.get_name()
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
         Si la fonction op_init existe, l'active
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
         if type(self.definition.op_init) == types.FunctionType :
            apply(self.definition.op_init,(self,self.master.g_context))   
      self.state = 'modified'
    
   def nomme_sd(self,nom) :
      """
          Cette m�thode a pour fonction de donner un nom (nom) au concept 
          produit par l'�tape (self).
          - si le concept n'existe pas, on essaye de le cr�er (� condition que l'�tape soit valide ET non r�entrante)
          - si il existe d�j�, on le renomme et on r�percute les changements dans les autres �tapes    
          Les valeurs de retour sont :
           0 si le nommage n'a pas pu etre men� � son terme,
           1 dans le cas contraire
      """
      if len(nom) > 8 and self.jdc.definition.code == 'ASTER':
        return 0,"Nom de concept trop long (maxi 8 caract�res)"
      self.init_modif()
      # Cas particulier des op�rateurs r�entrants
      if not self.isvalid(sd='non') : return 0,"Nommage du concept refus� : l'op�rateur n'est pas valide"
      if self.definition.reentrant == 'o':
        self.sd = self.reuse = self.jdc.get_sdprod(nom)
        if self.sd != None :
          return 1,"Concept existant"
        else:
          return 0,"Op�rateur r�entrant mais concept non existant"
      if self.definition.reentrant == 'f' :
        sd = self.jdc.get_sd_avant_etape(nom,self)
        if sd != None :
          self.sd = self.reuse = sd
          return 1,"Op�rateur facultativement r�entrant et concept existant trouv�"
        else :
          # il faut �ventuellement enlever le lien vers une SD existante car si on passe ici
	  # cela signifie que l'op�rateur n'est pas utilis� en mode r�entrant.
	  # Si on ne fait pas cela, le nom de l'op�rateur r�utilis� est aussi modifi�
	  # et on ne peut plus modifier la SD de l'op�rateur
	  if self.reuse :
	     self.sd = self.reuse = None
      # l'op�rateur n'est pas r�entrant ou facultativement reentrant mais pas dans ce cas
      if self.sd == None :
          if self.parent.get_sd_autour_etape(nom,self):
            # On force self.valid a 0 car l appel a isvalid precedent l a mis a 1
            # mais ceci indique seulement une validit� partielle
            # isvalid ne devrait peut etre pas mettre l attribut valid � 1 si sd == 'non'
            self.valid=0
            return 0,"Nommage du concept refuse : un concept de meme nom existe deja"
          # Il n'existe pas de sd de nom sdnom. On peut donc cr�er le concept retourn�.
          # Il est cr�� sans nom mais enregistr� dans la liste des concepts existants
          self.get_sd_prod()
          self.sd.nom = nom
          return 1,"Nommage du concept effectu�"
      else :
        old_nom=self.sd.nom
        if string.find(old_nom,'sansnom') :
           # Dans le cas o� old_nom == sansnom, isvalid retourne 0 alors que ...
	   # par contre si le concept existe et qu'il s'appelle sansnom c'est que l'�tape est valide
	   # on peut donc le nommer sans test pr�alable
	   self.sd.nom=nom
           return 1,"Nommage du concept effectu�"
        if self.isvalid() :
          # Normalement l appel de isvalid a mis a jour le concept produit (son type)
          # Il suffit de sp�cifier l attribut nom de sd pour le nommer si le nom n est pas
          # deja attribu�
          if self.parent.get_sd_autour_etape(nom,self):
            return 0,"Nommage du concept refuse : un concept de meme nom existe deja"
          else:
            self.sd.nom=nom
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
      self.actif = 1
      if not self.sd : return
      # XXX Pourquoi faut-il faire ce qui suit ??? par defaut les etapes sont actives
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

   def supprime_sdprods(self):
      """ 
          Fonction:
            Lors d'une destruction d'etape, detruit tous les concepts produits
            Un op�rateur n a qu un concept produit 
            Une procedure n'en a aucun
            Une macro en a en g�n�ral plus d'un
      """
      # XXX pour les macros il faudrait peut etre aussi 
      #     supprimer les concepts a droite du = ???
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
             sd=concept detruit
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

   def make_register(self):
      """
         Initialise les attributs jdc, id, niveau et r�alise les
         enregistrements n�cessaires
         Pour EFICAS, on tient compte des niveaux
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
      etape.mc_liste=[]
      for objet in self.mc_liste:
        new_obj = objet.copy()
	new_obj.parent = etape
	if hasattr(new_obj,'isMcList') :
	   if new_obj.isMCList() :
	      new_obj.init(new_obj.nom,etape)
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

