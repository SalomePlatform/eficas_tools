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
import string

class REGLE:

  def gettext(self):
    text = self.__class__.__name__+ ' :\n'
    for mc in self.mcs :
      text = text + '\t' + string.strip(mc) + '\n'
    return text

  def purge_liste(self,liste_a_purger,liste_mc_presents):
    """
         Cette méthode doit retirer de la liste liste_a_purger
         les éléments qui ne doivent plus apparaitre en fonction du contexte
    """
    # Dans le cas général on ne touche pas à la liste
    return liste_a_purger

  def has_operande(self,nom):
    # On peut faire aussi try:self.mcs.index(nom);return 1;except:return 0
    for mc in self.mcs:
      if mc==nom : return 1
    return 0

  def verif_condition_regle(self,liste,l_mc_presents):
    return []



