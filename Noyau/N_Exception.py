# -*- coding: iso-8859-1 -*-
# Copyright (C) 2007-2012   EDF R&D
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
   Ce module contient la classe AsException
"""

# Modules Python
import types

class AsException(Exception):
  def __str__(self):
    if not self.args:
      return ''
    elif len(self.args) == 1:
      return str(self.args[0])
    else:
      s=''
      for e in self.args:
        if type(e) == types.StringType: s=s+ ' ' + e
        else:s=s+ ' ' + str(e)
      return s

