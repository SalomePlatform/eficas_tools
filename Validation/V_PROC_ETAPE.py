# -*- coding: iso-8859-1 -*-
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
#

"""
   Ce module contient la classe mixin PROC_ETAPE qui porte les méthodes
   nécessaires pour réaliser la validation d'un objet de type PROC_ETAPE
   dérivé de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilisée par héritage multiple pour composer les traitements.
"""
# Modules EFICAS
import V_ETAPE
from Noyau.N_Exception import AsException
from Noyau.N_utils import AsType
from Noyau.strfunc import ufmt


class PROC_ETAPE(V_ETAPE.ETAPE):
   """
      On réutilise les méthodes report,verif_regles
      de ETAPE par héritage.
   """

   def isvalid(self,sd='oui',cr='non'):
      """
         Methode pour verifier la validité de l'objet PROC_ETAPE. Cette méthode
         peut etre appelée selon plusieurs modes en fonction de la valeur
         de sd et de cr (sd n'est pas utilisé).

         Si cr vaut oui elle crée en plus un compte-rendu.

         Cette méthode a plusieurs fonctions :

          - retourner un indicateur de validité 0=non, 1=oui

          - produire un compte-rendu : self.cr

          - propager l'éventuel changement d'état au parent
      """
      if CONTEXT.debug : print "ETAPE.isvalid ",self.nom
      if self.state == 'unchanged' :
        return self.valid
      else:
        valid=self.valid_child()
        valid=valid * self.valid_regles(cr)
        if self.reste_val != {}:
          if cr == 'oui' :
            self.cr.fatal(_(u"Mots clés inconnus : %s"), ','.join(self.reste_val.keys()))
          valid=0
        self.set_valid(valid)
        return self.valid


