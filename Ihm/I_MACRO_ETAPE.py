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
import sys
import traceback,types,string

# Modules Eficas
import I_ETAPE
from Noyau.N_ASSD import ASSD

# import rajoutés suite à l'ajout de Build_sd --> à résorber
import Noyau, Validation.V_MACRO_ETAPE
from Noyau import N_Exception
from Noyau.N_Exception import AsException
# fin import à résorber

class MACRO_ETAPE(I_ETAPE.ETAPE):

  def __init__(self):
      self.typret=None

  def get_sdprods(self,nom_sd):
    """ 
         Fonction : retourne le concept produit par l etape de nom nom_sd
                    s il existe sinon None
    """
    if self.sd and self.sd.nom == nom_sd :return self.sd
    for co in self.sdprods:
      if co.nom == nom_sd:return co
    if type(self.definition.op_init) == types.FunctionType:
      d={}
      apply(self.definition.op_init,(self,d))
      return d.get(nom_sd,None)
    return None

  def get_contexte_jdc(self,fichier,text):
    """ 
         Interprète text comme un texte de jdc et retourne le 
         contexte final
         cad le dictionnaire des sd disponibles à la dernière étape
         Si text n'est pas un texte de jdc valide, retourne None
         ou leve une exception
         --> utilisée par ops.POURSUITE et INCLUDE
    """
    try:
       # on essaie de créer un objet JDC auxiliaire avec un contexte initial
       context_ini = self.parent.get_contexte_avant(self)

       # Indispensable avant de creer un nouveau JDC
       CONTEXT.unset_current_step()
       args=self.jdc.args
       prefix_include=None
       if hasattr(self,'prefix'):
          prefix_include=self.prefix

       j=self.JdC_aux( procedure=text,cata=self.jdc.cata,
                                nom=fichier,
                                context_ini = context_ini,
                                appli=self.jdc.appli,
                                jdc_pere=self.jdc,etape_include=self,
                                prefix_include=prefix_include,**args)

       j.analyse()
    except:
       traceback.print_exc()
       # On force le contexte (etape courante) à self
       CONTEXT.unset_current_step()
       CONTEXT.set_current_step(self)
       return None

    if not j.cr.estvide():
       # On force le contexte (etape courante) à self
       CONTEXT.unset_current_step()
       CONTEXT.set_current_step(self)
       # Erreurs dans l'INCLUDE. On garde la memoire du fichier mais on n'insere pas les concepts
       # et les etapes. Ce traitement doit etre fait par l'appelant qui recoit l'exception
       raise Exception("Impossible de relire le fichier\n"+str(j.cr))

    cr=j.report()
    if not cr.estvide():
       # On force le contexte (etape courante) à self
       CONTEXT.unset_current_step()
       CONTEXT.set_current_step(self)
       raise Exception("Le fichier include contient des erreurs\n"+str(j.cr))

    # Cette verification n'est plus necessaire elle est integree dans le JDC_INCLUDE
    #self.verif_contexte(j_context)

    # On recupere le contexte apres la derniere etape
    j_context=j.get_contexte_avant(None)

    # On remplit le dictionnaire des concepts produits inclus
    # en retirant les concepts présents dans le  contexte initial
    # On ajoute egalement le concept produit dans le sds_dict du parent
    # sans verification car on est sur (verification integrée) que le nommage est possible
    self.g_context.clear()
    for k,v in j_context.items():
       if not context_ini.has_key(k) or context_ini[k] != v:
           self.g_context[k]=v
           self.parent.sds_dict[k]=v

    # On récupère les étapes internes (pour validation)
    self.etapes=j.etapes

    # ainsi que le contexte courant
    self.current_context=j.current_context
    self.index_etape_courante=j.index_etape_courante

    # XXX j.supprime() ???
    # On force le contexte (etape courante) à self
    CONTEXT.unset_current_step()
    CONTEXT.set_current_step(self)

    return j_context

  def verif_contexte(self,context):
     """
         On verifie que le contexte context peut etre inséré dans le jeu
         de commandes à la position de self
     """
     for nom_sd,sd in context.items():
        if not isinstance(sd,ASSD):continue
        if self.parent.get_sd_apres_etape(nom_sd,etape=self):
           # Il existe un concept apres self => impossible d'inserer
           raise Exception("Impossible d'inclure le fichier. Un concept de nom " + 
                           "%s existe déjà dans le jeu de commandes." % nom_sd)

  def reevalue_sd_jdc(self):
     """
         Avec la liste des SD qui ont été supprimées, propage la 
         disparition de ces SD dans toutes les étapes et descendants
     """
     l_sd_supp,l_sd_repl = self.diff_contextes()
     for sd in l_sd_supp:
        self.parent.delete_concept_after_etape(self,sd)
     for old_sd,sd in l_sd_repl:
        self.parent.replace_concept_after_etape(self,old_sd,sd)

  def diff_contextes(self):
     """ 
         Réalise la différence entre les 2 contextes 
         old_contexte_fichier_init et contexte_fichier_init
         cad retourne la liste des sd qui ont disparu ou ne derivent pas de la meme classe
         et des sd qui ont ete remplacees
     """
     if not hasattr(self,'old_contexte_fichier_init'):return [],[]
     l_sd_suppressed = []
     l_sd_replaced = []
     for old_key in self.old_contexte_fichier_init.keys():
       if not self.contexte_fichier_init.has_key(old_key):
         if isinstance(self.old_contexte_fichier_init[old_key],ASSD):
           l_sd_suppressed.append(self.old_contexte_fichier_init[old_key])
       else:
         if isinstance(self.old_contexte_fichier_init[old_key],ASSD):
            # Un concept de meme nom existe
            old_class=self.old_contexte_fichier_init[old_key].__class__
            if not isinstance(self.contexte_fichier_init[old_key],old_class):
               # S'il n'est pas d'une classe derivee, on le supprime
               l_sd_suppressed.append(self.old_contexte_fichier_init[old_key])
            else:
               l_sd_replaced.append((self.old_contexte_fichier_init[old_key],self.contexte_fichier_init[old_key]))
     return l_sd_suppressed,l_sd_replaced
      
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
      # On verifie les concepts a droite du signe =
      for co in self.sdprods:
        if d.has_key(co.nom) and co is not d[co.nom] :
           self.delete_concept(co)
        else:
           d[co.nom]=co
       

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
      # On détruit les concepts à droite du signe =
      for co in self.sdprods:
         self.parent.del_sdprod(co)
         self.parent.delete_concept(co)
      # Si la macro a des etapes et des concepts inclus, on les detruit
      for nom_sd,co in self.g_context.items():
         if not isinstance(co,ASSD):continue
         self.parent.del_sdprod(co)
         self.parent.delete_concept(co)
      # On met g_context à blanc
      self.g_context={}
         
#ATTENTION : cette methode surcharge celle de Noyau (a garder en synchro)
  def Build_sd(self,nom):
     """
        Construit le concept produit de l'opérateur. Deux cas 
        peuvent se présenter :

        - le parent n'est pas défini. Dans ce cas, l'étape prend en charge 
          la création et le nommage du concept.

        - le parent est défini. Dans ce cas, l'étape demande au parent la 
          création et le nommage du concept.

     """
     if not self.isactif():return
     # CCAR : meme modification que dans I_ETAPE
     if not self.isvalid(sd='non') : return
     self.sdnom=nom
     try:
        # On positionne la macro self en tant que current_step pour que les 
        # étapes créées lors de l'appel à sd_prod et à op_init aient la macro
        #  comme parent 
        self.set_current_step()
        if self.parent:
           sd= self.parent.create_sdprod(self,nom)
           if type(self.definition.op_init) == types.FunctionType: 
              apply(self.definition.op_init,(self,self.parent.g_context))
        else:
           sd=self.get_sd_prod()
           if sd != None and self.reuse == None:
              # On ne nomme le concept que dans le cas de non reutilisation 
              # d un concept
              sd.nom=nom
        self.reset_current_step()
        if self.jdc and self.jdc.par_lot == "NON" :
           self.Execute()
        return sd
     except AsException,e:
        self.reset_current_step()
        # Une erreur s'est produite lors de la construction du concept
        # Comme on est dans EFICAS, on essaie de poursuivre quand meme
        # Si on poursuit, on a le choix entre deux possibilités :
        # 1. on annule la sd associée à self
        # 2. on la conserve mais il faut qu'elle soit correcte et la retourner
        # En plus il faut rendre coherents sdnom et sd.nom
        # On choisit de retourner None et de mettre l'etape invalide 
        self.sd=None
        self.sdnom=None
        self.state="unchanged"
        self.valid=0
        return self.sd
        #raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
        #                     'fichier : ',self.appel[1],e)
     except EOFError:
        raise
     except :
        self.reset_current_step()
        l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
        raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                          'fichier : ',self.appel[1]+'\n',
                           string.join(l))

  def make_contexte_include(self,fichier,text):
    """
        Cette méthode sert à créer un contexte en interprétant un texte source
        Python
    """
    # on récupère le contexte d'un nouveau jdc dans lequel on interprete text
    contexte = self.get_contexte_jdc(fichier,text)
    if contexte == None :
      raise Exception("Impossible de construire le jeu de commandes correspondant au fichier")
    else:
      # Pour les macros de type include : INCLUDE, INCLUDE_MATERIAU et POURSUITE
      # l'attribut g_context est un dictionnaire qui contient les concepts produits par inclusion
      # l'attribut contexte_fichier_init est un dictionnaire qui contient les concepts produits
      # en sortie de macro. g_context est obtenu en retirant de contexte_fichier_init les concepts
      # existants en debut de macro contenus dans context_ini (dans get_contexte_jdc)
      # g_context est utilisé pour avoir les concepts produits par la macro
      # contexte_fichier_init est utilisé pour avoir les concepts supprimés par la macro
      self.contexte_fichier_init = contexte

  def reevalue_fichier_init(self):
      """Recalcule les concepts produits par le fichier enregistre"""
      old_context=self.contexte_fichier_init
      try:
         self.make_contexte_include(self.fichier_ini ,self.fichier_text)
      except:
         l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
         self.fichier_err = string.join(l)
         self.etapes=[]
         self.g_context={}

         self.old_contexte_fichier_init=old_context
         self.contexte_fichier_init={}
         self.reevalue_sd_jdc()
         return

      # L'evaluation s'est bien passee
      self.fichier_err = None
      self.old_contexte_fichier_init=old_context
      self.reevalue_sd_jdc()

  def make_poursuite(self):
      """ Cette methode est appelée par la fonction sd_prod de la macro POURSUITE
      """
      if not hasattr(self,'fichier_ini') :
         # Si le fichier n'est pas defini on le demande
         f,text=self.get_file(fic_origine=self.parent.nom)
         # On memorise le fichier retourne
         self.fichier_ini = f
         self.fichier_text = text
         import Extensions.jdc_include
         self.JdC_aux=Extensions.jdc_include.JdC_poursuite
         self.contexte_fichier_init={}
         if f is None:
             self.fichier_err="Le fichier POURSUITE n'est pas defini"
         else:
             self.fichier_err=None

         if self.fichier_err is not None: raise Exception(self.fichier_err)

         try:
           self.make_contexte_include(self.fichier_ini,self.fichier_text)
         except:
           l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
           if self.jdc.appli:
              self.jdc.appli.affiche_alerte("Erreur lors de l'evaluation du fichier poursuite",
                                            message="Ce fichier ne sera pas pris en compte\n"+string.join(l)
                                           )
           self.g_context={}
           self.etapes=[]
           self.fichier_err = string.join(l)
           self.contexte_fichier_init={}
           raise

      else:
         # Si le fichier est deja defini on ne reevalue pas le fichier
         # et on leve une exception si une erreur a été enregistrée
         if self.fichier_err is not None: raise Exception(self.fichier_err)


#ATTENTION : cette methode surcharge celle de Noyau (a garder en synchro)
  def make_include(self,unite=None):
      """
          Inclut un fichier dont l'unite logique est unite
          Cette methode est appelee par la fonction sd_prod de la macro INCLUDE
          Si l'INCLUDE est invalide, la methode doit produire une exception 
          Sinon on retourne None. Les concepts produits par l'INCLUDE sont
          pris en compte par le JDC parent lors du calcul du contexte (appel de ???)
      """

      # On supprime l'attribut unite qui bloque l'evaluation du source de l'INCLUDE
      # car on ne s'appuie pas sur lui dans EFICAS mais sur l'attribut fichier_ini
      del self.unite
      # Si unite n'a pas de valeur, l'etape est forcement invalide. On peut retourner None
      if not unite : return

      if not hasattr(self,'fichier_ini') : 
         # Si le fichier n'est pas defini on le demande
         f,text=self.get_file(unite=unite,fic_origine=self.parent.nom)
         # On memorise le fichier retourne
         self.fichier_ini  = f
         self.fichier_text = text
         self.contexte_fichier_init={}
         if f is None:
             self.fichier_err="Le fichier INCLUDE n est pas defini"
         else:
             self.fichier_err=None
         import Extensions.jdc_include
         self.JdC_aux=Extensions.jdc_include.JdC_include

         if self.fichier_err is not None: raise Exception(self.fichier_err)

         try:
           self.make_contexte_include(self.fichier_ini ,self.fichier_text)
         except:
           l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
           if self.jdc.appli:
              self.jdc.appli.affiche_alerte("Erreur lors de l'evaluation du fichier inclus",
                                            message="Ce fichier ne sera pas pris en compte\n"+string.join(l)
                                           )
           self.g_context={}
           self.etapes=[]
           self.fichier_err = string.join(l)
           self.contexte_fichier_init={}
           raise

      else:
         # Si le fichier est deja defini on ne reevalue pas le fichier
         # et on leve une exception si une erreur a été enregistrée
         #self.reevalue_fichier_init()
         if self.fichier_err is not None: raise Exception(self.fichier_err)
        

#ATTENTION : cette methode surcharge celle de Noyau (a garder en synchro)
  def make_contexte(self,fichier,text):
    """
        Cette méthode sert à créer un contexte pour INCLUDE_MATERIAU
        en interprétant un texte source Python
        Elle est appelee par la fonction sd_prd d'INCLUDE_MATERIAU
    """
    # On supprime l'attribut mat qui bloque l'evaluation du source de l'INCLUDE_MATERIAU
    # car on ne s'appuie pas sur lui dans EFICAS mais sur l'attribut fichier_ini
    if hasattr(self,'mat'):del self.mat
    self.fichier_ini =fichier
    self.fichier_text=text
    self.fichier_err=None 
    self.contexte_fichier_init={}
    # On specifie la classe a utiliser pour le JDC auxiliaire
    import Extensions.jdc_include
    self.JdC_aux=Extensions.jdc_include.JdC_include
    try:
       self.make_contexte_include(self.fichier_ini ,self.fichier_text)
    except:
       l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
       self.g_context={}
       self.etapes=[]
       self.fichier_err = string.join(l)
       self.contexte_fichier_init={}
       raise

#ATTENTION : cette methode surcharge celle de Noyau (a garder en synchro)
  def update_sdprod(self,cr='non'):
     # Cette methode peut etre appelee dans EFICAS avec des mots cles de 
     # la commande modifies. Ceci peut conduire a la construction ou
     # a la reconstruction d'etapes dans le cas d'INCLUDE ou d'INCLUDE_MATERIAU
     # Il faut donc positionner le current_step avant l'appel
     CONTEXT.unset_current_step()
     CONTEXT.set_current_step(self)
     valid=Validation.V_MACRO_ETAPE.MACRO_ETAPE.update_sdprod(self,cr=cr)
     CONTEXT.unset_current_step()
     return valid

