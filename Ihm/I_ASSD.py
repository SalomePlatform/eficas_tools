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

#from I_VALIDATOR import ValidException
from Noyau.N_VALIDATOR import ValError

class ASSD:
   def __repr__(self):
      return "concept %s de type %s" % (self.get_name(),self.__class__.__name__)

   def __str__(self):
      return self.get_name() or "<None>"

   #def __del__(self):
   #   print "__del__",self

class assd(ASSD):
   def __convert__(cls,valeur):
      return valeur
   __convert__=classmethod(__convert__)

class GEOM(ASSD):
   def __convert__(cls,valeur):
      return valeur
   __convert__=classmethod(__convert__)

class geom(GEOM):pass

class CO(ASSD):
   def __convert__(cls,valeur):
      if hasattr(valeur,'_etape') :
         # valeur est un concept CO qui a ete transforme par type_sdprod
         if valeur.etape == valeur._etape:
             # le concept est bien produit par l'etape
             return valeur
      raise ValError("Pas un concept CO")
      #raise ValidException("Pas un concept CO")
   __convert__=classmethod(__convert__)

