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

extensions=('.comm',)
listeSupprime=('Jour','Mois','An','Heure','Minute','Seconde')
DicoTransforme= {'MASS LUMPING':'MASS-LUMPING','MATRIX VECTOR' : 'MATRIX-VECTOR' , 
                  'C U PRECON':'C-U PRECON','STAGE DISCHARGE' : 'STAGE-DISCHARGE'}

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins
      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'TELEMAC',
        # La factory pour creer une instance du plugin
          'factory' : TELEMACGenerator,
          }


class TELEMACGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 
      un texte au format dictionnaire

   """

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
 
      self.texteDico = ""


#----------------------------------------------------------------------------------------
# ecriture
#----------------------------------------------------------------------------------------

   def writeDefault(self,fn) :
       fileDico = fn[:fn.rfind(".")] + '.py'
       f = open( str(fileDico), 'wb')
       f.write( self.texteDico )
       print self.texteDico
       f.close()

#----------------------------------------------------------------------------------------
#  analyse de chaque noeud de l'arbre 
#----------------------------------------------------------------------------------------

   def generMCSIMP(self,obj) :
        """recuperation de l objet MCSIMP"""
        s=PythonGenerator.generMCSIMP(self,obj)
        nomMajuscule=obj.nom.upper()
        nom=nomMajuscule.replace('_',' ') 
        if nom in listeSupprime : return s
        nomNouveau=nom
        for k in DicoTransforme.keys() :
            if k in nom :
               nomNouveau=nom.replace(k,DicoTransforme[k])
        self.texteDico+=nomNouveau+ "=" + s[0:-1]+ "\n"
        return s

   def generMCFACT(self,obj):
      """
        Recalule les jours et les heures
      """
      s=PythonGenerator.generMCFACT(self,obj)
      return s

  
