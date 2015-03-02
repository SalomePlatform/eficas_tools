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
"""Ce module contient le plugin generateur de fichier au format  Code_Carmel3D pour EFICAS.
"""

import traceback
import types,string,re,os
from Extensions.i18n import tr
from generator_python import PythonGenerator

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins
      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'dicoImbrique',
        # La factory pour creer une instance du plugin
          'factory' : DicoImbriqueGenerator,
          }


class DicoImbriqueGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 
      un texte au format dictionnaire

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

#----------------------------------------------------------------------------------------
   def gener(self,obj,format='brut',config=None):
       
      self.initDico()
      
      # Cette instruction genere le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)
      return self.text


#----------------------------------------------------------------------------------------
# initialisations
#----------------------------------------------------------------------------------------
   
   def initDico(self) :
 
      self.Dico={}


#----------------------------------------------------------------------------------------
# ecriture
#----------------------------------------------------------------------------------------

   def writeDefault(self,fn) :
       print "je passe par writeDefault"
       fileDico = fn[:fn.rfind(".")] + '.py'
       f = open( str(fileDico), 'wb')
       f.write( str(self.Dico) )
       f.close()

#----------------------------------------------------------------------------------------
#  analyse de chaque noeud de l'arbre 
#----------------------------------------------------------------------------------------

   def generMCSIMP(self,obj) :
        """recuperation de l objet MCSIMP"""
        s=PythonGenerator.generMCSIMP(self,obj)
        liste=obj.get_genealogie() 
        dicoCourant=self.Dico
        for i in liste [0:-1]:
            if not(dicoCourant.has_key(i)) : dicoCourant[i]={}
            dicoCourant=dicoCourant[i] 
        dicoCourant[liste[-1]]=obj.valeur
        return s

  
