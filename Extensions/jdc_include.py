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
      j_context=self.get_contexte_avant(None)
      self.verif_contexte(j_context)
      return j_context

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
      for nom_sd,sd in context.items():
        if not isinstance(sd,ASSD):continue
        if self.jdc_pere.get_sd_apres_etape_avec_detruire(nom_sd,sd,
                                                       etape=self.etape_include):
           # Il existe un concept produit par une etape apres self 
           # => impossible d'inserer
           raise Exception("Impossible d'inclure le fichier. Un concept de nom " +
                           "%s existe déjà dans le jeu de commandes." % nom_sd)

      return context


class JDC_INCLUDE(JDC_POURSUITE):
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


