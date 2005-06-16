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
    #print "get_contexte_jdc",self,self.nom
    try:
       # on essaie de créer un objet JDC auxiliaire avec un contexte initial
       # Attention get_contexte_avant retourne un dictionnaire qui contient
       # le contexte courant. Ce dictionnaire est reactualise regulierement.
       # Si on veut garder l'etat du contexte fige, il faut en faire une copie.
       context_ini = self.parent.get_contexte_avant(self).copy()
       #print "get_contexte_jdc",context_ini.keys()

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

       if fichier is None:fichier="SansNom"
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
    except:
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
    try:
       j_context=j.get_verif_contexte()
    except:
       CONTEXT.unset_current_step()
       CONTEXT.set_current_step(self)
       raise

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

    # On rétablit le contexte (etape courante) à self
    CONTEXT.unset_current_step()
    CONTEXT.set_current_step(self)

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
          Cette methode doit verifier que les concepts produits par la 
          commande ne sont pas incompatibles avec le contexte fourni (d).
          Si c'est le cas, le concept produit doit etre supprime
          Si la macro a elle meme des etapes, elle doit propager
          le traitement (voir methode control_jdc_context_apres de I_JDC)
      """
      #print "I_MACRO_ETAPE.control_sdprods",d.keys(),self.nom,self.sd and self.sd.nom
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
              self.init_modif()
              sd=self.sd
              self.sd=self.reuse=self.sdnom=None
              self.parent.delete_concept_after_etape(self,sd)
              self.fin_modif()

      # On verifie les concepts a droite du signe =
      self.init_modif()
      sdprods=self.sdprods[:]
      self.sdprods=[]
      for co in sdprods:
        if d.has_key(co.nom) and co is not d[co.nom] :
           #nettoie les mots cles de l'étape qui ont comme valeur co
           self.delete_concept(co)
           #supprime les references a co dans les etapes suivantes
           self.parent.delete_concept_after_etape(self,co)
        else:
           self.sdprods.append(co)
      self.fin_modif()
       
      for e in self.etapes:
          e.control_sdprods(d)
          e.update_context(d)

  def supprime_sdprod(self,sd):
      """
         Supprime le concept produit sd s'il est produit par l'etape
      """
      if sd in self.sdprods:
         self.init_modif()
         self.parent.del_sdprod(sd)
         self.sdprods.remove(sd)
         self.fin_modif()
         self.parent.delete_concept(sd)
         return

      if sd is not self.sd :return
      if self.sd is not None :
         self.init_modif()
         self.parent.del_sdprod(sd)
         self.sd=None
         self.fin_modif()
         self.parent.delete_concept(sd)

  def supprime_sdprods(self):
      """
          Fonction: Lors de la destruction de la macro-etape, detruit tous les concepts produits
          Un opérateur n a qu un concept produit
          Une procedure n'en a aucun
          Une macro en a en général plus d'un
      """
      #print "supprime_sdprods"
      if self.reuse is not self.sd :
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

  def close(self):
      if hasattr(self,"jdc_aux") and self.jdc_aux:
         # La macro a un jdc auxiliaire inclus. On demande sa fermeture
         self.jdc_aux.close()

  def reset_context(self):
      if hasattr(self,"jdc_aux") and self.jdc_aux:
         # La macro a un jdc auxiliaire inclus. On demande la reinitialisation du contexte
         self.jdc_aux.reset_context()

  def update_concept(self,sd):
      I_ETAPE.ETAPE.update_concept(self,sd)
      for etape in self.etapes:
          etape.update_concept(sd)

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
         etape.replace_concept(old_sd,sd)
         
  def change_fichier_init(self,new_fic,text):
    """
       Tente de changer le fichier include. Le precedent include est conservé
       dans old_xxx
    """
    #print "change_fichier_init",new_fic
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
    if self.old_jdc_aux:
       self.old_jdc_aux.close()

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
       Force le remplacement du fichier init meme si le remplacant est en erreur
    """
    # Reinitialisation complete du compte-rendu d'erreurs
    self.jdc_aux.cr=self.jdc_aux.CR()
    # On remplit le dictionnaire des concepts produits inclus
    # en retirant les concepts présents dans le  contexte initial
    # On ajoute egalement le concept produit dans le sds_dict du parent
    # sans verification car on est sur (verification integrée) que
    # le nommage est possible
    j_context=self.jdc_aux.get_contexte_avant(None)
    self.g_context.clear()
    context_ini=self.jdc_aux.context_ini
    for k,v in j_context.items():
       if not context_ini.has_key(k) or context_ini[k] != v:
           self.g_context[k]=v
           self.parent.sds_dict[k]=v
    # On recupere le contexte courant
    self.current_context=self.jdc_aux.current_context
    self.index_etape_courante=self.jdc_aux.index_etape_courante
    self.contexte_fichier_init = j_context
    self.fichier_err = None

    # On enregistre la modification de fichier
    self.init_modif()
    self.state="undetermined"
    self.record_unite()
    # Le contexte du parent doit etre reinitialise car les concepts produits ont changé
    self.parent.reset_context()

    # On remplace les anciens concepts par les nouveaux (y compris ajouts 
    # et suppression) et on propage les modifications aux etapes precedentes et suivantes
    # reevalue_sd_jdc construit la liste des differences entre les contextes contexte_fichier_init
    # et old_contexte_fichier_init et effectue les destructions et remplacements de concept
    # necessaires
    self.old_contexte_fichier_init=self.old_context
    self.reevalue_sd_jdc()
    self.fin_modif()
    if self.old_jdc_aux:
       self.old_jdc_aux.close()

    self.jdc_aux.force_contexte(self.g_context)

  def build_include(self,fichier,text):
    import Extensions.jdc_include
    self.JdC_aux=Extensions.jdc_include.JdC_include
    # un include partage la table des unites avec son parent (jdc)
    self.recorded_units=self.parent.recorded_units
    self.build_jdcaux(fichier,text)

  def build_poursuite(self,fichier,text):
    import Extensions.jdc_include
    self.JdC_aux=Extensions.jdc_include.JdC_poursuite
    # une poursuite a sa propre table d'unites
    self.recorded_units={}
    self.build_jdcaux(fichier,text)

  def build_jdcaux(self,fichier,text):
    """
         Cree un jdc auxiliaire initialise avec text. 
         Initialise le nom du fichier associé avec fichier
         N'enregistre pas d'association unite <-> fichier
    """
    self.fichier_ini = fichier
    self.fichier_text= text
    self.fichier_unite=None
    self.fichier_err = None
    try:
       contexte = self.get_contexte_jdc(fichier,text)
       if contexte is None :
          # Impossible de construire le jdc auxiliaire (sortie par None)
          # On simule une sortie par exception
          raise Exception("Impossible de construire le jeu de commandes correspondant au fichier")
       else:
          # La construction du jdc auxiliaire est allée au bout
          self.contexte_fichier_init = contexte
       self.init_modif()
       self.fin_modif()
    except:
       # Impossible de construire le jdc auxiliaire (sortie par exception)
       l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
       if self.jdc.appli:
          self.jdc.appli.affiche_alerte("Erreur lors de l'evaluation du fichier inclus",
                                        message="Ce fichier ne sera pas pris en compte\n"+string.join(l)
                                       )
       self.g_context={}
       self.etapes=[]
       self.jdc_aux=None
       self.fichier_err = string.join(l)
       self.contexte_fichier_init={}
       self.init_modif()
       self.fin_modif()
       raise

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
         self.g_context={}
         self.etapes=[]
         self.jdc_aux=None
         self.old_contexte_fichier_init=old_context
         self.contexte_fichier_init={}
         self.reevalue_sd_jdc()
         return

      # L'evaluation s'est bien passee
      self.fichier_err = None
      self.old_contexte_fichier_init=old_context
      self.reevalue_sd_jdc()

  def update_fichier_init(self,unite):
      """Reevalue le fichier init sans demander (dans la mesure du possible) a l'utilisateur 
         les noms des fichiers
         Ceci suppose que les relations entre unites et noms ont été memorisees préalablement
         L'include a été initialisé précédemment. Le jdc auxiliaire existe.
      """
      #print "update_fichier_init",unite,self.fichier_unite 
      self.old_contexte_fichier_init=self.contexte_fichier_init
      old_fichier_ini=self.fichier_ini
      if not hasattr(self,"jdc_aux"):self.jdc_aux=None
      old_jdc_aux=self.jdc_aux

      #print "update_fichier_init",self,self.parent,self.parent.recorded_units

      if self.fichier_unite is None:
         # L'unité n'était pas définie précédemment. On ne change que l'unite
         #print "update_fichier_init","pas de changement dans include"
         self.fichier_unite=unite
         return
      elif unite == self.fichier_unite :
         # L'unité n'a pas changé
         #print "update_fichier_init","pas de changement dans include 3"
         return
      elif unite != self.fichier_unite :
         # L'unité était définie précédemment. On remplace l'include 
         #
         f,text=self.get_file_memo(unite=unite,fic_origine=self.parent.nom)
         if f is None:
            # Le fichier associé n'a pas pu etre defini
            # on change l'unite associée mais pas l'include
            #print "update_fichier_init","pas de changement dans include 2"
            self.fichier_unite=unite
            return
         else:
            self.fichier_ini = f
            self.fichier_text=text
            self.fichier_unite=unite
         #print "update_fichier_init",self.recorded_units

      #print "update_fichier_init",self.fichier_ini,self.fichier_text,self.fichier_unite

      if old_fichier_ini == self.fichier_ini:
         # Le fichier inclus n'a pas changé. On ne recrée pas le contexte
         # mais on enregistre le changement d'association unite <-> fichier
         #print "update_fichier_init.fichier inchange",self.jdc_aux.context_ini
         self.parent.record_unit(unite,self)
         return

      try:
        self.fichier_err=None
        self.make_contexte_include(self.fichier_ini,self.fichier_text)
        # Les 3 attributs fichier_ini fichier_text recorded_units doivent etre corrects
        # avant d'appeler change_unit
      except:
        # Erreurs lors de l'evaluation de text dans un JDC auxiliaire
        l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
        # On conserve la memoire du nouveau fichier
        # mais on n'utilise pas les concepts crees par ce fichier
        # on met l'etape en erreur : fichier_err=string.join(l)
        self.fichier_err=string.join(l)
        self.g_context={}
        self.etapes=[]
        self.jdc_aux=None
        self.contexte_fichier_init={}

      if old_jdc_aux:
         old_jdc_aux.close()
      self.parent.record_unit(unite,self)
      # Le contexte du parent doit etre reinitialise car les concepts 
      # produits ont changé
      self.parent.reset_context()
      # Si des concepts ont disparu lors du changement de fichier, on 
      # demande leur suppression
      self.reevalue_sd_jdc()
      #print "update_fichier_init",self.jdc_aux.context_ini.keys()

  def record_unite(self):
      #print "record_unite",self.nom
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
      #print self.parent.recorded_units
      if unite is None:
         # On est dans le cas d'une poursuite. On ne reutilise aucune unite de parent
         units={}
      else:
         # On est dans le cas d'un include. On reutilise toutes les unites de parent
         units=self.parent.recorded_units

      if self.parent.recorded_units.has_key(unite):
         f,text,units=self.parent.recorded_units[unite]
      elif self.jdc :
         f,text=self.jdc.get_file(unite=unite,fic_origine=fic_origine)
      else:
         f,text=None,None

      self.recorded_units=units
      if f is None and self.jdc.appli:
         self.jdc.appli.affiche_alerte("Erreur lors de l'evaluation du fichier inclus",
                          message="Ce fichier ne sera pas pris en compte\n"+"Le fichier associé n'est pas défini")
      return f,text

  def update_context(self,d):
      """
         Met à jour le contexte contenu dans le dictionnaire d
         Une MACRO_ETAPE peut ajouter plusieurs concepts dans le contexte
         Une fonction enregistree dans op_init peut egalement modifier le contexte
      """
      #print "update_context",self,self.nom,d.keys()
      if hasattr(self,"jdc_aux") and self.jdc_aux:
            #ATTENTION: update_context NE DOIT PAS appeler reset_context
            # car il appelle directement ou indirectement update_context
            # equivalent a reset_context. Evite les recursions
            self.jdc_aux.context_ini=d.copy()
            self.jdc_aux.current_context={}
            self.jdc_aux.index_etape_courante=0
            #ATTENTION: il ne faut pas utiliser self.jdc_aux.get_contexte_avant
            #car cet appel conduit a des remontées multiples incohérentes dans le
            # ou les parents. 
            #get_context_avant appelle update_context qui NE DOIT PAS appeler get_contexte_avant
            #On n'a besoin que d'un update local connaissant
            # le contexte amont : d qui sert a reinitialiser self.context_ini
            for e in self.etapes:
                e.update_context(d)
            return

      if type(self.definition.op_init) == types.FunctionType:
        apply(self.definition.op_init,(self,d))
      if self.sd != None:d[self.sd.nom]=self.sd
      for co in self.sdprods:
        d[co.nom]=co
      #print "update_context.fin",d.keys()

#ATTENTION SURCHARGE : cette methode surcharge celle de Noyau (a garder en synchro)
  def get_file(self,unite=None,fic_origine=''):
      """Retourne le nom du fichier et le source correspondant a l'unite unite
      """
      if self.jdc :
         f,text=self.jdc.get_file(unite=unite,fic_origine=fic_origine)
      else:
         f,text=None,None
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

         #print "make_include",self.fichier_ini,self.fichier_text 
         if f is None and not text:
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
                                            message="Le contenu de ce fichier ne sera pas pris en compte\n"+string.join(l)
                                           )
           self.parent.record_unit(unite,self)
           self.g_context={}
           self.etapes=[]
           self.jdc_aux=None
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
       #self.parent.record_unit(self.fichier_unite,self)
    except:
       l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
       self.fichier_err = string.join(l)
       #self.parent.record_unit(self.fichier_unite,self)
       self.g_context={}
       self.etapes=[]
       self.jdc_aux=None
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
         #print "make_poursuite",self.fichier_ini,self.fichier_text

         if f is None:
             self.fichier_err="Le fichier POURSUITE n'est pas defini"
             self.jdc_aux=None
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
           self.etapes=[]
           self.jdc_aux=None
           self.fichier_err = string.join(l)
           self.contexte_fichier_init={}
           raise

      else:
         # Si le fichier est deja defini on ne reevalue pas le fichier
         # et on leve une exception si une erreur a été enregistrée
         self.update_fichier_init(None)
         if self.fichier_err is not None: raise Exception(self.fichier_err)
