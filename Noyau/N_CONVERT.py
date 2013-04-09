# -*- coding: iso-8859-1 -*-
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
"""
   Module de conversion des valeurs saisies par l'utilisateur après vérification.
"""

from N_types import is_int, is_float, is_enum


def has_int_value(real):
   """Est-ce que 'real' a une valeur entière ?
   """
   return abs(int(real) - real) < 1.e-12


class Conversion:
   """Conversion de type.
   """
   def __init__(self, name, typ):
      self.name = name
      self.typ  = typ

   def convert(self, obj):
      """Filtre liste
      """
      in_as_seq = is_sequence(obj)
      if not in_as_seq:
         obj = (obj,)

      result = []
      for o in obj:
         result.append(self.function(o))
      
      if not in_as_seq:
         return result[0]
      else:
         # ne marche pas avec MACR_RECAL qui attend une liste et non un tuple
         return tuple(result)

   def function(self, o):
      raise NotImplementedError, 'cette classe doit être dérivée'


class TypeConversion(Conversion):
   """Conversion de type
   """
   def __init__(self, typ):
      Conversion.__init__(self, 'type', typ)


class IntConversion(TypeConversion):
   """Conversion en entier
   """
   def __init__(self):
      TypeConversion.__init__(self, 'I')

   def function(self, o):
      if is_float(o) and has_int_value(o):
         o = int(o)
      return o


class FloatConversion(TypeConversion):
   """Conversion de type
   """
   def __init__(self):
      TypeConversion.__init__(self, 'R')

   def function(self, o):
      if is_float(o):
         o = float(o)
      return o


_convertI = IntConversion()
_convertR = FloatConversion()

def ConversionFactory(name, typ):
   if name == 'type':
      if 'I' in typ:
         return _convertI
      elif 'R' in typ:
         return _convertR
   return None


