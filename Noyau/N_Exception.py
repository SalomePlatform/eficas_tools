# coding=utf-8
# ======================================================================
# COPYRIGHT (C) 2007-2021  EDF R&D                  
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
   Ce module contient la classe AsException
"""

# Modules EFICAS
from __future__ import absolute_import
from .strfunc import getEncoding, toUnicode
import six


class AsException(Exception):

    def __unicode__(self):
        args = []
        for x in self.args:
            ustr = toUnicode(x)
            if type(ustr) is not six.text_type:
                ustr = six.text_type( repr(x) )
            args.append(ustr)
        return " ".join(args)

    def __str__(self):
        return six.text_type(self).encode(getEncoding())


class InterruptParsingError(Exception):

    """Exception used to interrupt the parsing of the command file
    without raising an error (see N_JDC.execCompile for usage)"""
