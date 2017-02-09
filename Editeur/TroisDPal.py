# -*- coding: utf-8 -*-
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
   Ce module contient la classe 3Dpilote qui va creer les ordres 
   de pilotage de l idl PAL pour un element de structure
"""
import generator
from Extensions.i18n import tr

class TroisDPilote:

   def __init__(self,node,appli):
      self.node=node
      self.appli=appli

   def envoievisu(self):
      """ 
      """
      format="vers3DSalome"
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         g=generator.plugins[format]()
         g.init_jdc(self.node.get_jdc())
         texte=g.gener(self.node)
      else:
         print ("Le generateur n'a pas ete trouve")
         print ("Erreur ! Erreur!")
         return ""
      from Extensions.param2 import originalMath
      originalMath.toOriginal()
      self.appli.envoievisu(texte)
      originalMath.toSurcharge()
  
