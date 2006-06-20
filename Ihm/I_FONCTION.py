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
import string
from I_ASSD import ASSD

class FONCTION(ASSD):
  def __init__(self,etape=None,sd=None,reg='oui'):
    if reg=='oui':
      self.jdc.register_fonction(self)

  def get_formule(self):
    """
    Retourne une formule décrivant self sous la forme d'un tuple :
    (nom,type_retourne,arguments,corps)
    """
    if hasattr(self.etape,'get_formule'):
      # on est dans le cas d'une formule Aster
      return self.etape.get_formule()
    else:
      # on est dans le cas d'une fonction
      return (self.nom,'REEL','(REEL:x)','''bidon''')

# On ajoute la classe formule pour etre cohérent avec la
# modification de C Durand sur la gestion des formules dans le superviseur
# On conserve l'ancienne classe fonction (ceinture et bretelles)
class fonction(FONCTION) : pass

from Extensions import param2
class formule(FONCTION) : 
   def __call__(self,*val):
      if len(val) != len(self.nompar):
         raise TypeError(" %s() takes exactly %d argument (%d given)" % (self.nom,len(self.nompar),len(val)))
      return param2.Unop2(self.nom,self.real_call,val)

   def real_call(self,*val):
      if hasattr(self.parent,'contexte_fichier_init'):
                        context=self.parent.contexte_fichier_init
      else            : context={}
      i=0
      for param in self.nompar :
         context[param]=val[i]
         i=i+1
      try :
       res=eval(self.expression,self.jdc.const_context, context)
      except :
       print 75*'!'
       print '! '+string.ljust('Erreur evaluation formule '+self.nom,72)+'!'
       print 75*'!'
       raise
      return res


