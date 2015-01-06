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

"""
from N_ASSD import ASSD

class GEOM(ASSD):
   """
      Cette classe sert � d�finir les types de concepts
      g�om�triques comme GROUP_NO, GROUP_MA,NOEUD et MAILLE

   """
   def __init__(self,nom,etape=None,sd=None,reg='oui'):
      """
      """
      self.etape=etape
      self.sd=sd
      if etape:
        self.parent=etape.parent
      else:
        self.parent=CONTEXT.get_current_step()
      if self.parent :
         self.jdc = self.parent.get_jdc_root()
      else:
         self.jdc = None

      if not self.parent:
        self.id=None
      elif reg == 'oui' :
        self.id = self.parent.reg_sd(self)
      self.nom=nom

   def get_name(self):
      return self.nom

   def __convert__(cls,valeur):
      if isinstance(valeur, (str,unicode)) and len(valeur.strip()) <= 8:
         return valeur.strip()
      raise ValueError(_(u'On attend une chaine de caract�res (de longueur < 8).'))
   __convert__=classmethod(__convert__)

class geom(GEOM):pass

