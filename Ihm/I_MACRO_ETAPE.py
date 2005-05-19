# -*- coding: utf-8 -*-
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
import Accas # attention aux imports circulaires
# fin import à résorber

class MACRO_ETAPE(I_ETAPE.ETAPE):

  def __init__(self):
      self.typret=None
      self.recorded_units={}

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
    #print "get_contexte_jdc"
    try:
       # on essaie de créer un objet JDC auxiliaire avec un contexte initial
       # Attention get_contexte_avant retourne un dictionnaire qui contient
       # le contexte courant. Ce dictionnaire est reactualise regulierement.
       # Si on veut garder l'etat du contexte fige, il faut en faire une copie.
       context_ini = self.parent.get_contexte_avant(self).copy()

       # Indispensable avant de creer un nouveau JDC
       CONTEXT.unset_current_step()
       args=self.jdc.args
       prefix_include=None
       if hasattr(self,'prefix'):
          prefix_include=self.prefix
       # ATTENTION : le dictionnaire recorded_units sert à memoriser les unites des 
       # fichiers inclus. Il est preferable de garder le meme dictionnaire pendant
       # tout le traitement et de ne pas le reinitialiser brutalement (utiliser 
       # clear plutot) si on ne veut pas perdre la memoire des unites.
       # En principe si la memorisation est faite au bon moment il n'est pas necessaire
       # de prendre cette precaution mais ce n'est pas vrai partout.
       old_recorded_units=self.recorded_units.copy()
       #print "get_contexte_jdc",id(self.recorded_units)
       #self.recorded_units.clear()

       j=self.JdC_aux( procedure=text, nom=fichier,
                                appli=self.jdc.appli,
                                cata=self.jdc.cata,
                                cata_ord_dico=self.jdc.cata_ordonne_dico,
                                context_ini = context_ini,
                                jdc_pere=self.jdc,etape_include=self,
                                prefix_include=prefix_include,
                                recorded_units=self.recorded_units,
                                old_recorded_units=old_recorded_units,**args)

       j.analyse()
       # On récupère les étapes internes (pour validation)
       self.etapes=j.etapes
       self.jdc_aux=j
       #print "get_contexte_jdc",id(self.etapes)
    except:
       traceback.print_exc()
       # On force le contexte (etape courante) à self
       CONTEXT.unset_current_step()
       CONTEXT.set_current_step(self)
       return None

    if not j.cr.estvide():
       # Erreurs dans l'INCLUDE. On garde la memoire du fichier 
       # mais on n'insere pas les concepts
       # On force le contexte (etape courante) à self
       CONTEXT.unset_current_step()
       CONTEXT.set_current_step(self)
       raise Exception("Impossible de relire le fichier\n"+str(j.cr))

    if not j.isvalid():
       # L'INCLUDE n'est pas valide.
       # on produit un rapport d'erreurs
       # On force le contexte (etape courante) à self
       cr=j.report()
       CONTEXT.unset_current_step()
       CONTEXT.set_current_step(self)
       raise Exception("Le fichier include contient des erreurs\n"+str(cr))

    # Si aucune erreur rencontrée
    # On recupere le contexte de l'include verifie
    #print "context_ini",j.context_ini
    #print "g_context",j.g_context
    try:
       j_context=j.get_verif_contexte()
    except:
       CONTEXT.unset_current_step()
       CONTEXT.set_current_step(self)
       raise

    #print "context_ini",j.context_ini

    # On remplit le dictionnaire des concepts produits inclus
    # en retirant les concepts présents dans le  contexte initial
    # On ajoute egalement le concept produit dans le sds_dict du parent
    # sans verification car on est sur (verification integrée) que 
    # le nommage est possible
    self.g_context.clear()
    for k,v in j_context.items():
       if not context_ini.has_key(k) or context_ini[k] != v:
           self.g_context[k]=v
           self.parent.sds_dict[k]=v


    # On recupere le contexte courant
    self.current_context=j.current_context
    self.index_etape_courante=j.index_etape_courante
    self.jdc_aux=j

    # XXX j.supprime() ???
    # On rétablit le contexte (etape courante) à self
    CONTEXT.unset_current_step()
    CONTEXT.set_current_step(self)
    #print "context_ini",self.jdc_aux.context_ini

    return j_context

  def reevalue_sd_jdc(self):
     """
         Avec la liste des SD qui ont été supprimées, propage la 
         disparition de ces SD dans toutes les étapes et descendants
     """
     #print "reevalue_sd_jdc"
     l_sd_supp,l_sd_repl = self.diff_contextes()
     for sd in l_sd_supp:
        self.parent.delete_concept_after_etape(self,sd)
     for old_sd,sd in l_sd_repl:
        self.parent.replace_concept_after_etape(self,old_sd,sd)

  def diff_contextes(self):
     """ 
         Réalise la différence entre les 2 contextes 
         old_contexte_fichier_init et contexte_fichier_init
         cad retourne la liste des sd qui ont disparu ou ne derivent pas 
         de la meme classe et des sd qui ont ete remplacees
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
      if hasattr(self,"fichier_unite"):
         self.update_fichier_init(self.fichier_unite)
         self.init_modif()

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
          Fonction: Lors de la destruction de la macro-etape, detruit tous les concepts produits
          Un opérateur n a qu un concept produit
          Une procedure n'en a aucun
          Une macro en a en général plus d'un
      """
      #print "supprime_sdprods"
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

  def delete_concept(self,sd):
      """
          Fonction : Mettre a jour les mots cles de l etape et eventuellement
          le concept produit si reuse suite à la disparition du concept sd
          Seuls les mots cles simples MCSIMP font un traitement autre
          que de transmettre aux fils
      """
      #print "delete_concept",sd
      I_ETAPE.ETAPE.delete_concept(self,sd)
      for etape in self.etapes:
         etape.delete_concept(sd)

  def replace_concept(self,old_sd,sd):
      """
          Fonction : Mettre a jour les mots cles de l etape et le concept produit si reuse 
          suite au remplacement  du concept old_sd par sd
      """
      #print "replace_concept",old_sd,sd
      I_ETAPE.ETAPE.replace_concept(self,old_sd,sd)
      for etape in self.etapes:
         etape.replace_concept(sd)
         
  def change_fichier_init(self,new_fic,text):
    """
       Tente de changer le fichier include. Le precedent include est conservé
       dans old_xxx
    """
    if not hasattr(self,'fichier_ini'):
       self.fichier_ini=None
       self.fichier_text=None
       self.fichier_err="Le fichier n'est pas defini"
       self.contexte_fichier_init={}
       self.recorded_units={}
       self.jdc_aux=None
       self.fichier_unite="PasDefini"
       import Extensions.jdc_include
       self.JdC_aux=Extensions.jdc_include.JdC_include

    self.old_fic = self.fichier_ini
    self.old_text = self.fichier_text
    self.old_err = self.fichier_err
    self.old_context=self.contexte_fichier_init
    self.old_units=self.recorded_units
    self.old_etapes=self.etapes
    self.old_jdc_aux=self.jdc_aux

    self.fichier_ini = new_fic
    self.fichier_text=text

    try:
       self.make_contexte_include(new_fic,text)
    except:
       l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
       self.fichier_err=string.join(l)
       raise

    # L'evaluation de text dans un JDC auxiliaire s'est bien passé
    # on peut poursuivre le traitement
    self.init_modif()
    self.state="undetermined"
    self.fichier_err=None
    # On enregistre la modification de fichier
    self.record_unite()
    # Le contexte du parent doit etre reinitialise car les concepts produits ont changé
    self.parent.reset_context()

    # Si des concepts ont disparu lors du changement de fichier, on demande leur suppression
    self.old_contexte_fichier_init=self.old_context
    self.reevalue_sd_jdc()

    self.fin_modif()

  def restore_fichier_init(self):
    """
       Restaure le fichier init enregistre dans old_xxx
    """
    self.fichier_ini=self.old_fic
    self.fichier_text=self.old_text
    self.fichier_err=self.old_err
    self.contexte_fichier_init=self.old_context
    self.recorded_units=self.old_units
    self.etapes=self.old_etapes
    self.jdc_aux=self.old_jdc_aux

  def force_fichier_init(self):
    """
       Force le fichier init en erreur
    """
    # On conserve la memoire du nouveau fichier
    # mais on n'utilise pas les concepts crees par ce fichier
    # on met l'etape en erreur : fichier_err=string.join(l)
    self.init_modif()
    # On enregistre la modification de fichier
    self.record_unite()
    #self.etapes=[]
    self.g_context={}
    # Le contexte du parent doit etre reinitialise car les concepts produits ont changé
    self.parent.reset_context()

    self.old_contexte_fichier_init=self.old_context
    self.contexte_fichier_init={}
    self.reevalue_sd_jdc()

    self.fin_modif()

  def make_contexte_include(self,fichier,text):
    """
        Cette méthode sert à créer un contexte en interprétant un texte source
        Python
    """
    #print "make_contexte_include"
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

  def reevalue_fichier_init_OBSOLETE(self):
      """Recalcule les concepts produits par le fichier enregistre"""
      #print "reevalue_fichier_init"
      old_context=self.contexte_fichier_init
      try:
         self.make_contexte_include(self.fichier_ini ,self.fichier_text)
      except:
         l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
         self.fichier_err = string.join(l)
         #self.etapes=[]
         self.g_context={}

         self.old_contexte_fichier_init=old_context
         self.contexte_fichier_init={}
         self.reevalue_sd_jdc()
         return

      # L'evaluation s'est bien passee
      self.fichier_err = None
      self.old_contexte_fichier_init=old_context
      self.reevalue_sd_jdc()
      #print "reevalue_fichier_init",self.jdc_aux.context_ini

  def update_fichier_init(self,unite):
      """Reevalue le fichier init sans demander (dans la mesure du possible) a l'utilisateur 
         les noms des fichiers
         Ceci suppose que les relations entre unites et noms ont été memorisees préalablement
      """
      #print "update_fichier_init",unite
      self.fichier_err=None
      self.old_contexte_fichier_init=self.contexte_fichier_init
      old_fichier_ini=self.fichier_ini

      #print "update_fichier_init",self,self.parent,self.parent.recorded_units

      #if unite != self.fichier_unite or not self.parent.recorded_units.has_key(unite):
      if not self.parent.recorded_units.has_key(unite):
         # Nouvelle unite
         f,text=self.get_file(unite=unite,fic_origine=self.parent.nom)
         units={}
         if f is not None:
            self.fichier_ini = f
            self.fichier_text=text
         self.recorded_units=units
         if self.fichier_ini is None and self.jdc.appli:
            self.jdc.appli.affiche_alerte("Erreur lors de l'evaluation du fichier inclus",
                     message="Ce fichier ne sera pas pris en compte\n"+"Le fichier associé n'est pas défini")
      else:
         # Unite existante
         f,text,units=self.parent.recorded_units[unite]
         self.fichier_ini = f
         self.fichier_text=text
         self.recorded_units=units

      if self.fichier_ini is None:
         # Le fichier n'est pas défini
         self.fichier_err="Le fichier associé n'est pas défini"
         self.parent.change_unit(unite,self,self.fichier_unite)
         self.g_context={}
         self.contexte_fichier_init={}
         self.parent.reset_context()
         self.reevalue_sd_jdc()
         return

      if old_fichier_ini == self.fichier_ini:
         # Le fichier inclus n'a pas changé. On ne recrée pas le contexte
         #print "update_fichier_init.fichier inchange",self.jdc_aux.context_ini
         return

      try:
        self.make_contexte_include(self.fichier_ini,self.fichier_text)
        # Les 3 attributs fichier_ini fichier_text recorded_units doivent etre corrects
        # avant d'appeler change_unit
        self.parent.change_unit(unite,self,self.fichier_unite)
      except:
        # Erreurs lors de l'evaluation de text dans un JDC auxiliaire
        l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
        # On conserve la memoire du nouveau fichier
        # mais on n'utilise pas les concepts crees par ce fichier
        # on met l'etape en erreur : fichier_err=string.join(l)
        self.fichier_err=string.join(l)
        self.parent.change_unit(unite,self,self.fichier_unite)
        self.g_context={}
        self.contexte_fichier_init={}

      # Le contexte du parent doit etre reinitialise car les concepts 
      # produits ont changé
      self.parent.reset_context()
      # Si des concepts ont disparu lors du changement de fichier, on 
      # demande leur suppression
      self.reevalue_sd_jdc()
      #print "update_fichier_init",self.jdc_aux.context_ini

  def record_unite(self):
      if self.nom == "POURSUITE":
         self.parent.record_unit(None,self)
      else:
         if hasattr(self,'fichier_unite') : 
            self.parent.record_unit(self.fichier_unite,self)

  def get_file_memo(self,unite=None,fic_origine=''):
      """Retourne le nom du fichier et le source correspondant a l'unite unite
         Initialise en plus recorded_units
      """
      #print "get_file_memo",unite,fic_origine,self,self.parent
      #print self.parent.old_recorded_units
      #print self.parent.recorded_units
      if unite is None:
         units={}
      else:
         units=self.parent.recorded_units
      if self.parent.old_recorded_units.has_key(unite):
         f,text,units=self.parent.old_recorded_units[unite]
         #print id(self.recorded_units)
         self.recorded_units=units
         #print id(self.recorded_units)
         return f,text
      elif self.jdc :
         f,text=self.jdc.get_file(unite=unite,fic_origine=fic_origine)
      else:
         f,text=None,None
      self.recorded_units=units
      if f is None and self.jdc.appli:
         self.jdc.appli.affiche_alerte("Erreur lors de l'evaluation du fichier inclus",
                          message="Ce fichier ne sera pas pris en compte\n"+"Le fichier associé n'est pas défini")
      return f,text

#ATTENTION SURCHARGE : cette methode surcharge celle de Noyau (a garder en synchro)
  def get_file(self,unite=None,fic_origine=''):
      """Retourne le nom du fichier et le source correspondant a l'unite unite
         Initialise en plus recorded_units
      """
      #print "get_file",unite
      units={}
      if self.jdc :
         f,text=self.jdc.get_file(unite=unite,fic_origine=fic_origine)
      else:
         f,text=None,None
      self.recorded_units=units
      return f,text

#ATTENTION SURCHARGE : cette methode surcharge celle de Noyau (a garder en synchro)
  def make_include(self,unite=None):
      """
          Inclut un fichier dont l'unite logique est unite
          Cette methode est appelee par la fonction sd_prod de la macro INCLUDE
          Si l'INCLUDE est invalide, la methode doit produire une exception 
          Sinon on retourne None. Les concepts produits par l'INCLUDE sont
          pris en compte par le JDC parent lors du calcul du contexte (appel de ???)
      """
      #print "make_include",unite
      # On supprime l'attribut unite qui bloque l'evaluation du source de l'INCLUDE
      # car on ne s'appuie pas sur lui dans EFICAS mais sur l'attribut fichier_ini
      del self.unite
      # Si unite n'a pas de valeur, l'etape est forcement invalide. On peut retourner None
      if not unite : return

      if not hasattr(self,'fichier_ini') : 
         # Si le fichier n'est pas defini on le demande
         f,text=self.get_file_memo(unite=unite,fic_origine=self.parent.nom)
         # On memorise le fichier retourne
         self.fichier_ini  = f
         self.fichier_text = text
         self.contexte_fichier_init={}
         self.fichier_unite=unite
         self.fichier_err=None
         try:
           import Extensions.jdc_include
         except:
           traceback.print_exc()
           raise
         self.JdC_aux=Extensions.jdc_include.JdC_include

         if f is None:
             self.fichier_err="Le fichier INCLUDE n est pas defini"
             self.parent.record_unit(unite,self)
             raise Exception(self.fichier_err)

         try:
           self.make_contexte_include(self.fichier_ini ,self.fichier_text)
           self.parent.record_unit(unite,self)
           #print "make_include.context_ini",self.jdc_aux.context_ini
         except:
           l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
           if self.jdc.appli:
              self.jdc.appli.affiche_alerte("Erreur lors de l'evaluation du fichier inclus",
                                            message="Ce fichier ne sera pas pris en compte\n"+string.join(l)
                                           )
           self.parent.record_unit(unite,self)
           self.g_context={}
           self.fichier_err = string.join(l)
           self.contexte_fichier_init={}
           raise

      else:
         # Si le fichier est deja defini on ne reevalue pas le fichier
         # et on leve une exception si une erreur a été enregistrée
         self.update_fichier_init(unite)
         self.fichier_unite=unite
         if self.fichier_err is not None: raise Exception(self.fichier_err)
        

#ATTENTION SURCHARGE : cette methode surcharge celle de Noyau (a garder en synchro)
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
    self.fichier_unite =fichier
    self.fichier_text=text
    self.fichier_err=None 
    self.contexte_fichier_init={}
    # On specifie la classe a utiliser pour le JDC auxiliaire
    try:
      import Extensions.jdc_include
    except:
      traceback.print_exc()
      raise
    self.JdC_aux=Extensions.jdc_include.JdC_include
    try:
       self.make_contexte_include(self.fichier_ini ,self.fichier_text)
       self.parent.record_unit(self.fichier_unite,self)
    except:
       l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
       self.fichier_err = string.join(l)
       self.parent.record_unit(self.fichier_unite,self)
       self.g_context={}
       self.contexte_fichier_init={}
       raise

#ATTENTION SURCHARGE : cette methode surcharge celle de Noyau (a garder en synchro)
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

#ATTENTION SURCHARGE: cette methode surcharge celle de Noyau a garder en synchro 
  def Build_sd(self,nom):
      """
           Methode de Noyau surchargee pour poursuivre malgre tout
           si une erreur se produit pendant la creation du concept produit
      """
      try:
         sd=Noyau.N_MACRO_ETAPE.MACRO_ETAPE.Build_sd(self,nom)
      except AsException,e:
         # Une erreur s'est produite lors de la construction du concept
         # Comme on est dans EFICAS, on essaie de poursuivre quand meme
         # Si on poursuit, on a le choix entre deux possibilités :
         # 1. on annule la sd associée à self
         # 2. on la conserve mais il faut la retourner
         # On choisit de l'annuler
         # En plus il faut rendre coherents sdnom et sd.nom
         self.sd=None
         self.sdnom=None
         self.state="unchanged"
         self.valid=0

      return self.sd

#ATTENTION SURCHARGE: cette methode surcharge celle de Noyau a garder en synchro 
  def make_poursuite(self):
      """ Cette methode est appelée par la fonction sd_prod de la macro POURSUITE
      """
      #print "make_poursuite"
      if not hasattr(self,'fichier_ini') :
         # Si le fichier n'est pas defini on le demande
         f,text=self.get_file_memo(fic_origine=self.parent.nom)
         # On memorise le fichier retourne
         self.fichier_ini = f
         self.fichier_unite = None
         self.fichier_text = text
         self.fichier_err=None
         try:
           import Extensions.jdc_include
         except:
           traceback.print_exc()
           raise
         self.JdC_aux=Extensions.jdc_include.JdC_poursuite
         self.contexte_fichier_init={}

         if f is None:
             self.fichier_err="Le fichier POURSUITE n'est pas defini"
             self.parent.record_unit(None,self)
             raise Exception(self.fichier_err)

         try:
           self.make_contexte_include(self.fichier_ini,self.fichier_text)
           self.parent.record_unit(None,self)
         except:
           l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
           if self.jdc.appli:
              self.jdc.appli.affiche_alerte("Erreur lors de l'evaluation du fichier poursuite",
                                            message="Ce fichier ne sera pas pris en compte\n"+string.join(l)
                                           )
           self.parent.record_unit(None,self)
           self.g_context={}
           self.fichier_err = string.join(l)
           self.contexte_fichier_init={}
           raise

      else:
         # Si le fichier est deja defini on ne reevalue pas le fichier
         # et on leve une exception si une erreur a été enregistrée
         self.update_fichier_init(None)
         if self.fichier_err is not None: raise Exception(self.fichier_err)

#ATTENTION SURCHARGE: cette methode surcharge celle de Noyau a garder en synchro 
  def type_sdprod(self,co,t):
      """
           Cette methode a pour fonction de typer le concept co avec le type t
            dans les conditions suivantes
            1- co est un concept produit de self
            2- co est un concept libre : on le type et on l attribue à self
           Elle enregistre egalement les concepts produits (on fait l hypothese
            que la liste sdprods a été correctement initialisee, vide probablement)
      """
      #print "type_sdprod",co,t
      if not hasattr(co,'etape'):
         # Le concept vaut None probablement. On ignore l'appel
         return
      #
      # On cherche a discriminer les differents cas de typage d'un concept
      # produit par une macro qui est specifie dans un mot cle simple.
      # On peut passer plusieurs fois par type_sdprod ce qui explique
      # le nombre important de cas.
      #
      # Cas 1 : Le concept est libre. Il vient d'etre cree par CO(nom)
      # Cas 2 : Le concept est produit par la macro. On est deja passe par type_sdprod.
      #         Cas semblable a Cas 1.
      # Cas 3 : Le concept est produit par la macro englobante (parent). On transfere
      #         la propriete du concept de la macro parent a la macro courante (self)
      #         en verifiant que le type est valide
      # Cas 4 : La concept est la propriete d'une etape fille. Ceci veut dire qu'on est
      #         deja passe par type_sdprod et que la propriete a ete transfere a une
      #         etape fille. Cas semblable a Cas 3.
      # Cas 5 : Le concept est produit par une etape externe a la macro.
      #
      if co.etape == None:
         # Cas 1 : le concept est libre
         # On l'attache a la macro et on change son type dans le type demande
         # Recherche du mot cle simple associe au concept
         mcs=self.get_mcs_with_co(co)
         if len(mcs) != 1:
            raise AsException("""Erreur interne.
Il ne devrait y avoir qu'un seul mot cle porteur du concept CO (%s)""" % co)
         mcs=mcs[0]
         #
         # Attention : la seule modif est ici : Accas.CO au lieu de CO
         #
         if not Accas.CO in mcs.definition.type:
            raise AsException("""Erreur interne.
Impossible de changer le type du concept (%s). Le mot cle associe ne supporte pas CO mais seulement (%s)""" %(co,mcs.definition.type))
         co.etape=self
         co.__class__ = t
         self.sdprods.append(co)

      elif co.etape== self:
         # Cas 2 : le concept est produit par la macro (self)
         # On est deja passe par type_sdprod (Cas 1 ou 3).
         # Il suffit de le mettre dans la liste des concepts produits (self.sdprods)
         # Le type du concept doit etre coherent avec le type demande (seulement derive)
         if not isinstance(co,t):
            raise AsException("""Erreur interne.
Le type demande (%s) et le type du concept (%s) devraient etre derives""" %(t,co.__class__))
         self.sdprods.append(co)

      elif co.etape== self.parent:
         # Cas 3 : le concept est produit par la macro parente (self.parent)
         # on transfere la propriete du concept a la macro fille
         # et on change le type du concept comme demande
         # Au prealable, on verifie que le concept existant (co) est une instance
         # possible du type demande (t)
         # Cette règle est normalement cohérente avec les règles de vérification des mots-clés
         if not isinstance(co,t):
            raise AsException("""
Impossible de changer le type du concept produit (%s) en (%s).
Le type actuel (%s) devrait etre une classe derivee du nouveau type (%s)""" % (co,t,co.__class__,t))
         mcs=self.get_mcs_with_co(co)
         if len(mcs) != 1:
            raise AsException("""Erreur interne.
Il ne devrait y avoir qu'un seul mot cle porteur du concept CO (%s)""" % co)
         mcs=mcs[0]
         if not Accas.CO in mcs.definition.type:
            raise AsException("""Erreur interne.
Impossible de changer le type du concept (%s). Le mot cle associe ne supporte pas CO mais seulement (%s)""" %(co,mcs.definition.type))
         co.etape=self
         # On ne change pas le type car il respecte la condition isinstance(co,t)
         #co.__class__ = t
         self.sdprods.append(co)

      elif self.issubstep(co.etape):
         # Cas 4 : Le concept est propriété d'une sous etape de la macro (self).
         # On est deja passe par type_sdprod (Cas 3 ou 1).
         # Il suffit de le mettre dans la liste des concepts produits (self.sdprods)
         # Le type du concept et t doivent etre derives.
         # Il n'y a aucune raison pour que la condition ne soit pas verifiee.
         if not isinstance(co,t):
            raise AsException("""Erreur interne.
Le type demande (%s) et le type du concept (%s) devraient etre derives""" %(t,co.__class__))
         self.sdprods.append(co)

      else:
         # Cas 5 : le concept est produit par une autre étape
         # On ne fait rien
         return

