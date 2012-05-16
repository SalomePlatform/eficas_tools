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
_root=None
_cata=None
debug=0
from Noyau.N_info import message, SUPERV

# Le "current step" est l'étape courante.
# Une macro se déclare étape courante dans sa méthode Build avant de construire
# ses étapes filles ou dans BuildExec avant de les exécuter.
# Les étapes simples le font aussi : dans Execute et BuildExec.
# (Build ne fait rien pour une étape)

def set_current_step(step):
   """
      Fonction qui permet de changer la valeur de l'étape courante
   """
   global _root
   if _root : raise Exception("Impossible d'affecter _root. Il devrait valoir None")
   _root=step
   #message.debug(SUPERV, "current_step = %s", step and step.nom, stack_id=-1)

def get_current_step():
   """
      Fonction qui permet d'obtenir la valeur de l'étape courante
   """
   return _root

def unset_current_step():
   """
      Fonction qui permet de remettre à None l'étape courante
   """
   global _root
   _root=None

def set_current_cata(cata):
   """
      Fonction qui permet de changer l'objet catalogue courant
   """
   global _cata
   if _cata : raise Exception("Impossible d'affecter _cata. Il devrait valoir None")
   _cata=cata

def get_current_cata():
   """
      Fonction qui retourne l'objet catalogue courant
   """
   return _cata

def unset_current_cata():
   """
      Fonction qui permet de remettre à None le catalogue courant
   """
   global _cata
   _cata=None

