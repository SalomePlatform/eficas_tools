# -*- coding: utf-8 -*-
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
"""
import string

class REGLE:

  def gettext(self):
    text = self.__class__.__name__+ ' :\n'
    for mc in self.mcs :
      text = text + '\t' + string.strip(mc) + '\n'
    return text

  def purge_liste(self,liste_a_purger,liste_mc_presents):
    """
         Cette m�thode doit retirer de la liste liste_a_purger
         les �l�ments qui ne doivent plus apparaitre en fonction du contexte
    """
    # Dans le cas g�n�ral on ne touche pas � la liste
    return liste_a_purger

  def has_operande(self,nom):
    # On peut faire aussi try:self.mcs.index(nom);return 1;except:return 0
    for mc in self.mcs:
      if mc==nom : return 1
    return 0

  def verif_condition_regle(self,liste,l_mc_presents):
    return []



