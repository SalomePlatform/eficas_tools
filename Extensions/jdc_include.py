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
   Ce module contient la classe JDC_INCLUDE qui sert a inclure
   dans un jeu de commandes une partie de jeu de commandes
   au moyen de la fonctionnalite INCLUDE ou INCLUDE_MATERIAU
   Quand l'utilisateur veut inclure un fichier il faut versifier
   que le jeu de commandes inclus est valide et compatible
   avec le contexte avant et apres l'insertion
"""
from Accas import JDC,ASSD,AsException,JDC_CATA
from Ihm import CONNECTOR

class JDC_POURSUITE(JDC):
   def __init__(self,definition=None,procedure=None,cata=None,
                     cata_ord_dico=None,parent=None,
                     nom='SansNom',appli=None,context_ini=None,
                     jdc_pere=None,etape_include=None,prefix_include=None,
                     recorded_units=None,old_recorded_units=None,**args):

      JDC.__init__(self, definition=definition,
                         procedure=procedure,
                         cata=cata,
                         cata_ord_dico=cata_ord_dico,
                         parent=parent,
                         nom=nom,
                         appli=appli,
                         context_ini=context_ini,
                         **args
                         )
      self.jdc_pere=jdc_pere
      self.etape_include=etape_include
      self.prefix_include=prefix_include
      if recorded_units is not None:self.recorded_units=recorded_units
      if old_recorded_units is not None:self.old_recorded_units=old_recorded_units

   def NommerSdprod(self,sd,sdnom,restrict='non'):
      """
          Nomme la SD apres avoir verifie que le nommage est possible : nom
          non utilise
          Ajoute un prefixe s'il est specifie (INCLUDE_MATERIAU)
          Si le nom est deja utilise, leve une exception
          Met le concept créé dans le contexe global g_context
      """
      #print "NommerSdprod",sd,sdnom,restrict
      if self.prefix_include:
          if sdnom != self.prefix_include:sdnom=self.prefix_include+sdnom
      o=self.sds_dict.get(sdnom,None)
      if isinstance(o,ASSD):
         raise AsException("Nom de concept deja defini : %s" % sdnom)

      # On pourrait verifier que le jdc_pere apres l'etape etape_include
      # ne contient pas deja un concept de ce nom
      #if self.jdc_pere.get_sd_apres_etape_avec_detruire(sdnom,etape=self.etape_include):
         # Il existe un concept apres self => impossible d'inserer
      #   raise AsException("Nom de concept deja defini : %s" % sdnom)
      # On a choisi de ne pas faire ce test ici mais de le faire en bloc
      # si necessaire apres en appelant la methode verif_contexte

      # ATTENTION : Il ne faut pas ajouter sd dans sds car il s y trouve deja.
      # Ajoute a la creation (appel de reg_sd).
      self.sds_dict[sdnom]=sd
      sd.nom=sdnom

      # En plus si restrict vaut 'non', on insere le concept dans le contexte du JDC
      if restrict == 'non':
         self.g_context[sdnom]=sd

   def get_verif_contexte(self):
      #print "get_verif_contexte"
      j_context=self.get_contexte_avant(None)
      self.verif_contexte(j_context)
      return j_context

   def force_contexte(self,contexte):
      for nom_sd,sd in contexte.items():
        if not isinstance(sd,ASSD):continue
        if self.jdc_pere.get_sd_apres_etape_avec_detruire(nom_sd,sd,
                                                       etape=self.etape_include):
           # Il existe un autre concept de meme nom produit par une etape apres self 
           # on detruit ce concept pour pouvoir inserer les etapes du jdc_include
           #print "force_contexte",sd.etape,sd.nom,sd.etape.nom
           if sd.etape:
              sd.etape.supprime_sdprod(sd)

      return contexte

   def verif_contexte(self,context):
      """
         Cette methode verifie si le contexte passé en argument (context)
         peut etre inséré dans le jdc pere de l'include.
         Elle verifie que les concepts contenus dans ce contexte n'entrent
         pas en conflit avec les concepts produits dans le jdc pere
         apres l'include.
         Si le contexte ne peut pas etre inséré, la méthode leve une
         exception sinon elle retourne le contexte inchangé
      """
      #print "verif_contexte"
      for nom_sd,sd in context.items():
        if not isinstance(sd,ASSD):continue
        autre_sd= self.jdc_pere.get_sd_apres_etape_avec_detruire(nom_sd,sd,
                                                       etape=self.etape_include)
        if sd and sd is not autre_sd:
           # Il existe un concept produit par une etape apres self 
           # => impossible d'inserer
           raise Exception("Impossible d'inclure le fichier. Un concept de nom " +
                           "%s existe déjà dans le jeu de commandes." % nom_sd)

      return context

   def get_liste_cmd(self):
      """
          Retourne la liste des commandes du catalogue
      """
      if self.jdc_pere is None:
         return JDC.get_liste_cmd(self)
      return self.jdc_pere.get_liste_cmd()

   def get_groups(self):
      """
          Retourne la liste des commandes du catalogue par groupes
      """
      if self.jdc_pere is None:
         return JDC.get_groups(self)
      return self.jdc_pere.get_groups()

   def init_modif(self):
      """
         Met l'état de l'étape à : modifié
         Propage la modification au parent

         Attention : init_modif doit etre appelé avant de réaliser une modification
         La validité devra etre recalculée apres cette modification
         mais par un appel à fin_modif pour préserver l'état modified
         de tous les objets entre temps
      """
      #print "jdc_include.init_modif",self,self.etape_include
      self.state = 'modified'
      if self.etape_include:
         self.etape_include.init_modif()

   def fin_modif(self):
      """
          Méthode appelée une fois qu'une modification a été faite afin de
          déclencher d'éventuels traitements post-modification
          ex : INCLUDE et POURSUITE
      """
      #print "jdc_include.fin_modif",self,self.etape_include
      if not self.etape_include:
         CONNECTOR.Emit(self,"valid")
         return
      # Mise a jour du contexte en fin d'include
      # On suppose que toutes les modifications sont valides
      # On recupere le contexte final dans j_context
      j_context=self.get_contexte_avant(None) #get_verif_contexte ???
      # On remplit le dictionnaire des concepts produits de l'etape macro INCLUDE
      # sans y mettre les concepts présents dans le  contexte initial (context_ini)
      # On ajoute egalement les concepts produits dans le sds_dict du parent
      # sans verification car on est sur (verification integrée) que
      # le nommage est possible
      self.etape_include.g_context.clear()
      for k,v in j_context.items():
         if not self.context_ini.has_key(k) or self.context_ini[k] != v:
            self.etape_include.g_context[k]=v
            self.etape_include.parent.sds_dict[k]=v

      CONNECTOR.Emit(self,"valid")
      self.etape_include.fin_modif()
      #print "jdc_include.fin_modif.context_ini",self.context_ini

   def supprime(self):
      """
          On ne supprime rien pour un jdc auxiliaire d'include ou de poursuite
      """
      pass

   def get_contexte_avant(self,etape):
      """
         Retourne le dictionnaire des concepts connus avant etape
         On tient compte des concepts produits par le jdc pere
         en reactualisant le contexte initial context_ini
         On tient compte des commandes qui modifient le contexte
         comme DETRUIRE ou les macros
         Si etape == None, on retourne le contexte en fin de JDC
      """
      if self.etape_include:
         self.context_ini = self.etape_include.parent.get_contexte_avant(self.etape_include).copy()
      return JDC.get_contexte_avant(self,etape)

   #def get_sd_avant_etape(self,nom_sd,etape):
      #sd=self.etape_include.parent.get_sd_avant_etape(nom_sd,self.etape_include)
      #if sd:return sd
      #return JDC.get_sd_avant_etape(self,nom_sd,etape)

   #def get_sd_avant_du_bon_type(self,etape,types_permis):
      #"""
      #    Retourne la liste des concepts avant etape d'un type acceptable
      #"""
      #l1=self.etape_include.parent.get_sd_avant_du_bon_type(self.etape_include,types_permis)
      #l2=JDC.get_sd_avant_du_bon_type(self,etape,types_permis)
      #return l1+l2

   def get_sd_apres_etape(self,nom_sd,etape,avec='non'):
      """
           Cette méthode retourne la SD de nom nom_sd qui est éventuellement
           définie apres etape
           Si avec vaut 'non' exclut etape de la recherche
      """
      if self.etape_include:
         sd=self.etape_include.parent.get_sd_apres_etape(nom_sd,self.etape_include,'non')
         if sd:return sd
      return JDC.get_sd_apres_etape(self,nom_sd,etape,avec)

   def get_sd_apres_etape_avec_detruire(self,nom_sd,sd,etape,avec='non'):
      """
           On veut savoir ce que devient le concept sd de nom nom_sd apres etape.
           Il peut etre detruit, remplacé ou conservé
           Cette méthode retourne la SD sd de nom nom_sd qui est éventuellement
           définie apres etape en tenant compte des concepts detruits
           Si avec vaut 'non' exclut etape de la recherche
      """
      #print "jdc_include.get_sd_apres_etape_avec_detruire",nom_sd,sd,id(sd)
      autre_sd=JDC.get_sd_apres_etape_avec_detruire(self,nom_sd,sd,etape,avec)
      #print autre_sd,id(autre_sd)
      # si autre_sd vaut None le concept sd a ete detruit. On peut terminer
      # la recherche en retournant None
      # Si autre_sd ne vaut pas sd, le concept a ete redefini. On peut terminer
      # la recherche en retournant le concept nouvellement defini
      # Sinon, on poursuit la recherche dans les etapes du niveau superieur.
      if autre_sd is None or autre_sd is not sd :return autre_sd
      return self.etape_include.parent.get_sd_apres_etape_avec_detruire(nom_sd,sd,self.etape_include,'non')

   def delete_concept(self,sd):
      """
          Fonction : Mettre a jour les etapes du JDC suite à la disparition du
          concept sd
          Seuls les mots cles simples MCSIMP font un traitement autre
          que de transmettre aux fils
      """
      # Nettoyage des etapes de l'include
      JDC.delete_concept(self,sd)
      # Nettoyage des etapes du parent
      if self.etape_include:
         self.etape_include.parent.delete_concept_after_etape(self.etape_include,sd)

   def delete_concept_after_etape(self,etape,sd):
      """
          Fonction : Mettre à jour les étapes du JDC qui sont après etape suite à
          la disparition du concept sd
      """
      # Nettoyage des etapes de l'include
      JDC.delete_concept_after_etape(self,etape,sd)
      # Nettoyage des etapes du parent
      if self.etape_include:
         self.etape_include.parent.delete_concept_after_etape(self.etape_include,sd)

   def replace_concept_after_etape(self,etape,old_sd,sd):
      """
          Fonction : Mettre à jour les étapes du JDC qui sont après etape suite au
          remplacement du concept old_sd par sd
      """
      # Nettoyage des etapes de l'include
      JDC.replace_concept_after_etape(self,etape,old_sd,sd)
      # Nettoyage des etapes du parent
      if self.etape_include:
         self.etape_include.parent.replace_concept_after_etape(self.etape_include,old_sd,sd)

class JDC_INCLUDE(JDC_POURSUITE):
   def get_liste_cmd(self):
      """
          Retourne la liste des commandes du catalogue
      """
      if self.jdc_pere is None:
         return JDC.get_liste_cmd(self)
      return [e for e in self.jdc_pere.get_liste_cmd() if e not in ("DEBUT","POURSUITE","FIN") ]

   def active_etapes(self):
      for e in self.etapes:
         e.active()

class JDC_CATA_INCLUDE(JDC_CATA):
   class_instance=JDC_INCLUDE

class JDC_CATA_POURSUITE(JDC_CATA):
   class_instance=JDC_POURSUITE

from Accas import AU_MOINS_UN,A_CLASSER

JdC_include=JDC_CATA_INCLUDE(code='ASTER', execmodul=None)

JdC_poursuite=JDC_CATA_POURSUITE(code='ASTER', execmodul=None,
                                 regles = (AU_MOINS_UN('DEBUT','POURSUITE'),
                                           AU_MOINS_UN('FIN'),
                                           A_CLASSER(('DEBUT','POURSUITE'),'FIN')
                                          )
                               )


