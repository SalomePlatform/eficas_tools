# coding=utf-8
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

"""
   Ce module contient des fonctions utilitaires pour tester les types
"""

# eficas sentinel
from __future__ import absolute_import
import six
try:
    import numpy as NP
    _np_arr = NP.ndarray
except ImportError:
    _np_arr = None

# use isinstance() instead of type() because objects returned from numpy arrays
# inherit from python scalars but are numpy.float64 or numpy.int32...


def is_int(obj):
    return isinstance(obj, int) or type(obj) is int


def is_float(obj):
    return isinstance(obj, float)


def is_complex(obj):
    return isinstance(obj, complex)

from decimal import Decimal


def is_float_or_int(obj):
    return is_float(obj) or is_int(obj) or isinstance(obj, Decimal)


def is_number(obj):
    return is_float_or_int(obj) or is_complex(obj)


def is_str(obj):
    return isinstance(obj, (str, six.text_type))


def is_list(obj):
    return type(obj) is list


def is_tuple(obj):
    return type(obj) is tuple


def is_array(obj):
    """a numpy array ?"""
    return type(obj) is _np_arr


def is_sequence(obj):
    """a sequence (allow iteration, not a string) ?"""
    return is_list(obj) or is_tuple(obj) or is_array(obj)


def is_assd(obj):
    from .N_ASSD import ASSD
    return isinstance(obj, ASSD)


def force_list(obj):
    """Retourne `obj` si c'est une liste ou un tuple,
    sinon retourne [obj,] (en tant que list).
    """
    if not is_sequence(obj):
        obj = [obj, ]
    return list(obj)


def force_tuple(obj):
    """Return `obj` as a tuple."""
    return tuple(force_list(obj))

# backward compatibility
from warnings import warn


def is_enum(obj):
    """same as is_sequence"""
    warn("'is_enum' is deprecated, use 'is_sequence'",
         DeprecationWarning, stacklevel=2)
    return is_sequence(obj)
