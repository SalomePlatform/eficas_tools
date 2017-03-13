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

from __future__ import absolute_import
try :
   from builtins import object
except :
   pass
from .N_utils import import_object


class OPS(object):

    """Wrapper to ops functions.
    This allows to import them only when they are needed."""

    def __init__(self, uri):
        """Initialization"""
        self.uri = uri

    def __call__(self, *args, **kwargs):
        """Import the real function and call it."""
        func = import_object(self.uri)
        return func(*args, **kwargs)


# utilisé par exemple par des macros où tout est fait dans l'init.
class NOTHING(OPS):

    """OPS which does nothing."""

    def __call__(self, macro, *args, **kwargs):
        macro.set_icmd(1)
        return 0

EMPTY_OPS = NOTHING(None)
