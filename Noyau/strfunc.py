# coding=utf-8
# Copyright (C) 2007-2021   EDF R&D
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

"""Module rassemblant des fonctions utilitaires de manipulations
de chaines de caractères
"""
# module identique à Execution/strfunc.py pour usage dans Eficas

from __future__ import absolute_import
try :
    from builtins import str
except : pass

import locale
import six

_encoding = None


def getEncoding():
    """Return local encoding
    """
    global _encoding
    if _encoding is None:
        try:
            _encoding = locale.getpreferredencoding() or 'ascii'
        except locale.Error:
            _encoding = 'ascii'
    return _encoding


def toUnicode(string):
    """Try to convert string into a unicode string."""
    if type(string) is six.text_type:
        return string
    elif type(string) is dict:
        new = {}
        for k, v in list(string.items()):
            new[k] = toUnicode(v)
        return new
    elif type(string) is list:
        return [toUnicode(elt) for elt in string]
    elif type(string) is tuple:
        return tuple(toUnicode(list(string)))
    elif type(string) is not str:
        return string
    assert type(string) is str, u"unsupported object: %s" % string
    for encoding in ('utf-8', 'iso-8859-15', 'cp1252'):
        try:
            s = six.text_type(string, encoding)
            return s
        except UnicodeDecodeError:
            pass
    return six.text_type(string, 'utf-8', 'replace')


#def fromUnicode(ustring, encoding, errors='replace'):
#    """Try to encode a unicode string using encoding."""
#    try:
#        return ustring.encode(encoding)
#    except UnicodeError:
#        pass
#    return ustring.encode(encoding, errors)
#
#
#def convert(content, encoding=None, errors='replace'):
#    """Convert content using encoding or default encoding if None."""
#    if type(content) not in (str, six.text_type):
#        content = six.text_type(content)
#    if type(content) == str:
#        content = toUnicode(content)
#    return fromUnicode(content, encoding or getEncoding(), errors)
#
#
#def ufmt(uformat, *args):
#    """Helper function to format a string by converting all its arguments to unicode"""
#    if type(uformat) is not six.text_type:
#        uformat = toUnicode(uformat)
#    if len(args) == 1 and type(args[0]) is dict:
#        arguments = toUnicode(args[0])
#    else:
#        nargs = []
#        for arg in args:
#            if type(arg) in (str, six.text_type, list, tuple, dict):
#                nargs.append(toUnicode(arg))
#            elif type(arg) not in (int, int, float):
#                nargs.append(toUnicode(str(arg)))
#            else:
#                nargs.append(arg)
#        arguments = tuple(nargs)
#    formatted_string=""
#    try:
#        formatted_string = uformat % arguments
#    #except UnicodeDecodeError:
#    #    print type(uformat), uformat
#    #    print type(arguments), arguments
#        #raise
#    except :
#        pass
#    return formatted_string
