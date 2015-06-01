# coding=utf-8
# Copyright (C) 2007-2015   EDF R&D
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

# Modules EFICAS
from strfunc import get_encoding, to_unicode


class AsException(Exception):

    def __unicode__(self):
        args = []
        for x in self.args:
            ustr = to_unicode(x)
            if type(ustr) is not unicode:
                ustr = unicode( repr(x) )
            args.append(ustr)
        return " ".join(args)

    def __str__(self):
        return unicode(self).encode(get_encoding())


class InterruptParsingError(Exception):

    """Exception used to interrupt the parsing of the command file
    without raising an error (see N_JDC.exec_compile for usage)"""
