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
Ce module génère un objet INDEX par lecture et interprétation du fichier texte
le décrivant (ex : index_aide.py)
"""

import os

class ITEM_INDEX :
   """
   Construit un objet ITEM_INDEX
   """
   def __init__(self,t_item):
       self.t_item = t_item
       self.init()

   def init(self):
       """
       Initialise les structures de données de l'item
       """
       self.titre = ""
       self.fichier = ""
       self.l_items = []
              
   def build(self):
       """
       Construit les sous-items de self s'il y a lieu et retoruve le label et le fichier de l'item
       dans le tuple
       """
       self.titre = self.t_item[0]
       self.fichier = self.t_item[1]
       l_items = self.t_item[2]
       if l_items :
          for item in l_items :
             o = ITEM_INDEX(item)
             o.build()
             self.l_items.append(o)

class INDEX :
   """
   Construit un objet INDEX (non graphique) à partir de l'interprétation du fichier d'index
   (type index_aide.py) passé en argument
   """
   def __init__(self,fichier_index):
       self.fichier_index = fichier_index
       self.init()
       
   def init(self):
      """
      Initialise les structures de données propres à l'index
      """
      self.titre = ""
      self.fichier = None
      self.l_items = []
      
   def build(self):
      """
      Lit le fichier index et l'interprète
      """
      txt = open(self.fichier_index,'r').read()
      d = {}
      d['repertoire']=os.path.dirname(self.fichier_index)
      #txt = "items ="+txt
      #print txt
      exec txt in d
      items = d.get("items",None)
      if items :
         self.titre = items[0]
         self.fichier = items[1]
         l_items = items[2]
         for item in l_items :
            o = ITEM_INDEX(item)
            o.build()
            self.l_items.append(o)

      
       
