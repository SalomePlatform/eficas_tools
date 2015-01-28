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
    Ce package fournit les classes de base d'EFICAS.
    Ces classes permettent d'effectuer quelques opérations basiques :

      - la création

      - la vérification des définitions

      - la création d'objets de type OBJECT à partir d'une définition de type ENTITE
"""
# Avant toutes choses, on met le module context dans le global de l'interpreteur (__builtin__)
# sous le nom CONTEXT afin d'avoir accès aux fonctions
# get_current_step, set_current_step et unset_current_step de n'importe où
import context
import __builtin__
__builtin__.CONTEXT = context


def _(msg):
    """Differs translation."""
    # 'codex' should install its translation functions later
    return msg
__builtin__._ = _

# Classes de base
from N_SIMP import SIMP
from N_FACT import FACT

# structures de données
import asojb
from asojb import AsBase

# Only the first MAXSIZE objects will be checked
# This is used for the number of MCFACT, the number of MCSIMP and the number of
# values in a MCSIMP.
MAXSIZE = 500

MAXSIZE_MSGCHK = ' <A> Only the first {0} occurrences (total: {1}) have been checked.'
MAXSIZE_MSGKEEP = ' <A> Only the first {0} occurrences (total: {1}) have been kept.'
