# -*- coding: utf-8 -*-
# copyright 2012 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
"""
Creates the ``EficasException`` class for the EDF Eficas application.
This class supports the internationalization mechanism provided in
the ``i18n`` module.
"""

from __future__ import absolute_import
class EficasException(Exception):
    """
    ``EficasException`` class, which embeds the translation mechanism.
    In case the input message is already passed through the translation
    mechanism, the translation mechanism defined in this class would
    have no effect, since its input would not be among the source
    strings to be translated.
    """
    def __init__(self, msg=""):
        """
        Initializes the EficasException instances. The output message,
        stored in the ``args`` attribute, is fitted with the translation
        mechanism.
        """
        Exception.__init__(self)
        #import sys, os
        #sys.path.append(os.path.realpath(".."))
        from Extensions.i18n import tr
        self.args = (tr(msg),)


if __name__ == "__main__":
    import sys
    raise EficasException(sys.argv[1])
