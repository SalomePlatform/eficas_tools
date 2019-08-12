# -*- coding: utf-8 -*-
# Copyright (C) 2007-2017   EDF R&D
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
"""Ce module contient le plugin generateur de fichier au format  Code_Carmel3D pour EFICAS.
"""

from __future__ import absolute_import
from __future__ import print_function
try :
   from builtins import str
except : pass

import traceback
import types,re,os
from Extensions.i18n import tr
from .generator_python import PythonGenerator

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins
      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'xml',
        # La factory pour creer une instance du plugin
          'factory' : XMLGenerator,
          }


class XMLGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

#----------------------------------------------------------------------------------------
   def gener(self,obj,format='brut',config=None,appli=None):
       
      try :
        print (obj)
        self.texteXML=obj.toXml()
      except : 
        self.texteXML='erreur generation'
        pass
      
      # Cette instruction genere le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)
      return self.text


#----------------------------------------------------------------------------------------
# initialisations
#----------------------------------------------------------------------------------------
   
# ecriture
#----------------------------------------------------------------------------------------

   def writeDefault(self,fn) :
       #fileDico = fn[:fn.rfind(".")] + '.py'
       fileDico='/tmp/toto.xml'
       print (self.texteXML)
       f = open( str(fileDico), 'w')
       f.write('Dico = '+str(self.texteXML))
       f.close()

