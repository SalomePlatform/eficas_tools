# -*- coding: iso-8859-1 -*-
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
This package provides Qt-based string internationalization functionality
for the ``Eficas`` application of EDF.
It is usable from both Qt and non-Qt environments.
``PyQt4`` is currently supported.
"""
from __future__ import absolute_import
from .translation import tr, tr_qt
from .localisation import localise

__all__ = ['tr', 'tr_qt', 'localise']
