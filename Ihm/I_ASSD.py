# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

#from I_VALIDATOR import ValidException

from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException
from Noyau.N_VALIDATOR import ValError

class ASSD:
   def __repr__(self):
      return tr("concept %(inst_name)s de type %(class_name)s", \
                       {'inst_name': self.get_name(), \
                        'class_name': self.__class__.__name__})

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

class geom(GEOM):
   pass

class CO(ASSD):
   def __convert__(cls,valeur):
      if hasattr(valeur,'_etape') :
         # valeur est un concept CO qui a ete transforme par type_sdprod
         if valeur.etape == valeur._etape:
             # le concept est bien produit par l'etape
             return valeur
      raise ValError(u"Pas un concept CO")
   __convert__=classmethod(__convert__)

