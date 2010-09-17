# -* coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
   Ce module contient le plugin generateur de fichier au format
   SEP pour EFICAS.

"""
import traceback
import types,string,re,os

from generator_map import MapGenerator

import sys
sys.path.append('/local00/bin/MAP/classes/python/')
try :
  from class_MAP_parameters import *
except :
  pass

dico_post={"analyse statistique classique":("c_post_distribution_properties","PDF"),
"analyse statistique de la qualite":("",""),
"analyse de la dispersion suivant la distance au joint":("c_post_distribution_properties","dgb"),
"analyse de la dispersion suivant la distance a la pointe de fissure":("",""),
"visualisation dans le triangle standard":("","")}

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 's_scc_st_2',
        # La factory pour creer une instance du plugin
          'factory' : s_scc_st_2Generator,
          }


class s_scc_st_2Generator(MapGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et
      un texte au format py

   """
   
   def TABLEAU(self,execution):
       dico=self.dictMCVal["TABLEAU"]
       self.file_in_name=dico['_TABLEAU_FICHIER']
       return ""
       
   def TRAITEMENT(self, execution):
       dico=self.dictMCVal["TRAITEMENT"]
       post=dico['_TRAITEMENT_TYPE']
       variable=dico['_TRAITEMENT_VARIABLE']
       composant=dico_post[post][0]
       maDirectory=self.config.PATH_MAP+'/components/'+composant+'/'
       monFichier=self.config.PATH_STUDY+'/'+composant+'_'+dico_post[post][1]+'_'+variable+'.input'

       parameter=MAP_parameters()
       parameter.add_component(composant)
       parameter.add_parameter(composant, 'file_in_name', self.file_in_name)
       parameter.add_parameter(composant, 'variable_name', variable)
       parameter.add_parameter(composant, 'post', dico_post[post][1])
       parameter.add_parameter(composant, 'study_name', self.config.appli.ssCode)
       parameter.add_parameter(composant, 'study_path', self.config.PATH_STUDY)
       parameter.write(monFichier)

       command='cd '+maDirectory+'src/'+'\n'+'python '+composant+'.py -i '+monFichier+';'
       print "command = ", command
       if (execution=="oui") :
          return command

       return ""
