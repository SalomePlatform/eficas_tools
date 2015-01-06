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

texte_debut="int main() \n{ \n   init_var();\n"
texte_debut+='   format="med";\n'
import traceback
import types,string,re,os
from Extensions.i18n import tr
from generator_python import PythonGenerator
ListeConcatene=('ridge_names','topo_names','geom_names','elset_names','faset_names','liset_names','nset_names','center','normal','dir')

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins
      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'ZCRACKS',
        # La factory pour creer une instance du plugin
          'factory' : ZCrackGenerator,
          }


class ZCrackGenerator(PythonGenerator):
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
      self.textePourRun = texte_debut


#----------------------------------------------------------------------------------------
# ecriture
#----------------------------------------------------------------------------------------

   def writeDefault(self,fn) :
        fileZcrack = fn[:fn.rfind(".")] + '.z7p'
        f = open( str(fileZcrack), 'wb')
        print self.textePourRun
      
        self.ajoutRun()
        self.textePourRunAvecDouble=self.textePourRun.replace("'",'"')
        f.write( self.textePourRunAvecDouble)
        f.close()

   def ajoutRun(self) :
        self.textePourRun+="   write_mesh_crack();\n"
        self.textePourRun+="   do_mesh_crack(0);\n"
        self.textePourRun+="   nice_cut(20.);\n"
        self.textePourRun+='   export_mesh("'+self.cracked_name+'","med");\n'
        self.textePourRun+="}"

#----------------------------------------------------------------------------------------
#  analyse de chaque noeud de l'arbre 
#----------------------------------------------------------------------------------------

   def generMCSIMP(self,obj) :
        """recuperation de l objet MCSIMP"""
        #print dir(obj)
        s=PythonGenerator.generMCSIMP(self,obj)
        if obj.nom in ListeConcatene : 
           stringListe=""
           for val in obj.val:
               stringListe+=str(val)+" "
           self.textePourRun+="   "+obj.nom+ "='"+ stringListe[0:-1]+ "';\n"
           return s
        if obj.nom=="elset_radius"  :
           self.textePourRun+="   if_must_define_elset=1;\n"
        if obj.nom=="sane_name" and obj.val!=None :
           self.textePourRun+='   import_mesh("'+obj.val+'");\n'

        if obj.nom=="cracked_name" and obj.val!=None : self.cracked_name=obj.val
        if obj.nom=="repertoire" : 
           print "PNPNPN a traiter"
           return s
        self.textePourRun+="   "+obj.nom+ "=" + s[0:-1]+ ";\n"
        return s

  
# si repertoire on change tous les noms de fichier
# exple repertoire='/home' __> fichier='/home/crack.med
