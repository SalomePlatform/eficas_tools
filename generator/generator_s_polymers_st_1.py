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
try :
   sys.path.append(os.path.join(os.getenv('MAP_DIRECTORY'),'classes/python/'))
   from class_MAP_parameters import *
except :
   pass
#____________________________________________________________________________________
#
CONFIGliste=('NAME_SCHEME', 'PATH_ASTER', 'PATH_BENHUR', 'PATH_MODULE', 'PATH_PYGMEE', 'PATH_STUDY', 'repIni')

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 's_polymers_st_1',
        # La factory pour creer une instance du plugin
          'factory' : s_poly_st_1Generator,
          }


class s_poly_st_1Generator(MapGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et
      un texte au format py

   """
   

#_________________________________
#  - YACS functions
#_________________________________

   def PYGMEEYACS(self, SchemaYacs, proc):
      monFichierInput=self.config.PATH_STUDY+"/"+self.config.NAME_SCHEME+"/pygmee_input.txt"
      factoryNode = SchemaYacs.monCata._nodeMap["pygmee_v2"]
      SchemaYacs.pygmeeNode = factoryNode.cloneNode("pygmee_v2")
      SchemaYacs.pygmeeNode.getInputPort("phase_number").edInitPy(1)
      SchemaYacs.pygmeeNode.getInputPort("sieve_curve_in").edInitPy(self.sieve_curve_in)
      SchemaYacs.pygmeeNode.getInputPort("sieve_curve_out").edInitPy(self.sieve_curve_out)
      SchemaYacs.pygmeeNode.getInputPort("repulsion_distance").edInitPy(self.repulsion_distance)
      SchemaYacs.pygmeeNode.getInputPort("file_result_inclusions").edInitPy(self.inclusion_name)
      SchemaYacs.pygmeeNode.getInputPort("file_result_rve").edInitPy(self.rve_name)
      SchemaYacs.pygmeeNode.getInputPort("rve_size").edInitPy(self.rve_size)
      SchemaYacs.pygmeeNode.getInputPort("study_name").edInitPy(self.study_name)
      SchemaYacs.pygmeeNode.getInputPort("study_path").edInitPy(self.study_path)
      proc.edAddChild(SchemaYacs.pygmeeNode)
      if SchemaYacs.nodeAvant != None :
         proc.edAddCFLink(SchemaYacs.nodeAvant,SchemaYacs.pygmeeNode)
      SchemaYacs.nodeAvant=SchemaYacs.pygmeeNode
      print "PYGMEEYACS node Ok"

   def FDVGRIDYACS(self, SchemaYacs, proc):
      factoryNode = SchemaYacs.monCata._nodeMap["fdvgrid"]
      SchemaYacs.fdvgridNode = factoryNode.cloneNode("fdvgrid")

      SchemaYacs.fdvgridNode.getInputPort("rve_size").edInitPy(self.rve_size)
      SchemaYacs.fdvgridNode.getInputPort("lambda_I").edInitPy(self.lambda_I)
      SchemaYacs.fdvgridNode.getInputPort("lambda_M").edInitPy(self.lambda_M)
      SchemaYacs.fdvgridNode.getInputPort("finesse").edInitPy(self.finesse)
      SchemaYacs.fdvgridNode.getInputPort("study_name").edInitPy(self.study_name)
      SchemaYacs.fdvgridNode.getInputPort("study_path").edInitPy(self.study_path)
         
      proc.edAddChild(SchemaYacs.fdvgridNode)
      pout=SchemaYacs.pygmeeNode.getOutputPort("result_inclusions")
      pin=SchemaYacs.fdvgridNode.getInputPort("file_inclusions")
      proc.edAddLink(pout,pin)
         
      if SchemaYacs.nodeAvant != None :
         proc.edAddCFLink(SchemaYacs.nodeAvant,SchemaYacs.fdvgridNode)
      SchemaYacs.nodeAvant=SchemaYacs.fdvgridNode
      print "FDVGRIDYACS node Ok"

   def BENHURYACS(self, SchemaYacs, proc):
      factoryNode = SchemaYacs.monCata._nodeMap["benhur"]
      SchemaYacs.benhurNode = factoryNode.cloneNode("benhur")

      SchemaYacs.benhurNode.getInputPort("rve_size").edInitPy(self.rve_size)
      SchemaYacs.benhurNode.getInputPort("finesse").edInitPy(self.finesse)
      SchemaYacs.benhurNode.getInputPort("study_name").edInitPy(self.study_name)
      SchemaYacs.benhurNode.getInputPort("study_path").edInitPy(self.study_path)
         
      proc.edAddChild(SchemaYacs.benhurNode)
      pout=SchemaYacs.pygmeeNode.getOutputPort("result_inclusions")
      pin=SchemaYacs.benhurNode.getInputPort("file_inclusions")
      proc.edAddLink(pout,pin)
         
      if SchemaYacs.nodeAvant != None :
         proc.edAddCFLink(SchemaYacs.nodeAvant,SchemaYacs.benhurNode)
      SchemaYacs.nodeAvant=SchemaYacs.benhurNode
      print "BENHURYACS node Ok"

   def ASTERYACS(self, SchemaYacs, proc):
      factoryNode = SchemaYacs.monCata._nodeMap["aster_s_polymers_st_1"]
      SchemaYacs.aster_s_polymers_st_1Node = factoryNode.cloneNode("aster_s_polymers_st_1")

      SchemaYacs.aster_s_polymers_st_1Node.getInputPort("lambda_I").edInitPy(self.lambda_I)
      SchemaYacs.aster_s_polymers_st_1Node.getInputPort("lambda_M").edInitPy(self.lambda_M)
      SchemaYacs.aster_s_polymers_st_1Node.getInputPort("study_name").edInitPy(self.study_name)
      SchemaYacs.aster_s_polymers_st_1Node.getInputPort("study_path").edInitPy(self.study_path)
      SchemaYacs.aster_s_polymers_st_1Node.getInputPort("rve_size").edInitPy(self.rve_size)
      SchemaYacs.aster_s_polymers_st_1Node.getInputPort("finesse").edInitPy(self.finesse)
      SchemaYacs.aster_s_polymers_st_1Node.getInputPort("aster_path").edInitPy(self.config.PATH_ASTER)
      
      proc.edAddChild(SchemaYacs.aster_s_polymers_st_1Node)
      pout=SchemaYacs.benhurNode.getOutputPort("result_mesh")
      pin=SchemaYacs.aster_s_polymers_st_1Node.getInputPort("mesh")
      proc.edAddLink(pout,pin)
         
      if SchemaYacs.nodeAvant != None :
         proc.edAddCFLink(SchemaYacs.nodeAvant,SchemaYacs.aster_s_polymers_st_1Node)
      SchemaYacs.nodeAvant=SchemaYacs.aster_s_polymers_st_1Node
      print "ASTERYACS node Ok"

      
   def GMSHYACS(self, SchemaYacs, proc):
      factoryNode = SchemaYacs.monCata._nodeMap["gmsh_post"]
      SchemaYacs.gmsh_postNode = factoryNode.cloneNode("gmsh_post")
      
      proc.edAddChild(SchemaYacs.gmsh_postNode)
      pout=SchemaYacs.aster_s_polymers_st_1Node.getOutputPort("result_gmsh")
      pin=SchemaYacs.gmsh_postNode.getInputPort("result_gmsh")
      proc.edAddLink(pout,pin)
         
      if SchemaYacs.nodeAvant != None :
         proc.edAddCFLink(SchemaYacs.nodeAvant,SchemaYacs.gmsh_postNode)
      SchemaYacs.nodeAvant=SchemaYacs.gmsh_postNode
      print "GMSHYACS node Ok"

   def METHODEYACS(self, SchemaYacs, proc):
      self.PYGMEEYACS(SchemaYacs, proc)
      if (self.CHOIX=="FD+grid") :
         self.FDVGRIDYACS(SchemaYacs,proc)
      if (self.CHOIX=="FEM+mesh") :
         self.BENHURYACS(SchemaYacs,proc)
         self.ASTERYACS(SchemaYacs,proc)
         self.GMSHYACS(SchemaYacs,proc)

#_________________________________
#  - shell functions
#_________________________________

   def METHODE(self) :
      commande=self.PYGMEE()
      if (self.CHOIX=="FD+grid") :
          commande+= self.FDVGRID()
      elif (self.CHOIX=="FEM+mesh") :
          commande+= self.BENHUR()
          commande+= self.ASTER_s_polymers_st_1()
          commande+= self.GMSH()
      return commande

#_________________________________
#  - code and component functions
#_________________________________

   def PYGMEE(self) :
      commande="volume_fraction=component_pygmee_v2("+str(self.rve_size)+",1,'"+str(self.sieve_curve_in)+"','"+str(self.sieve_curve_out)+"',"+str(self.repulsion_distance)+",'"+str(self.study_name)+"','"+str(self.study_path)+"','"+str(self.inclusion_name)+"','"+str(self.rve_name)+"')\n"
      return commande

   def FDVGRID(self):
      commande="lambda_x=component_fdvgrid("+str(self.lambda_I)+","+str(self.lambda_M)+","+str(self.rve_size)+",'"+str(self.inclusion_name)+"',"+str(self.finesse)+",'"+str(self.study_path)+"')\n"
      return commande

   def BENHUR(self):
      commande="component_benhur("+str(self.finesse)+","+str(self.rve_size)+",'"+str(self.inclusion_name)+"','"+str(self.study_name)+"','"+str(self.study_path)+"');\n"
      return commande

   def ASTER_s_polymers_st_1(self) :
      commande="component_aster_s_polymers_st_1("+str(self.rve_size)+","+str(self.finesse)+","+str(self.lambda_I)+","+str(self.lambda_M)+",'"+str(self.study_name)+"','"+str(self.study_path)+"','"+self.config.PATH_ASTER+"');\n"
      return commande

   def GMSH(self) :
      commande="component_gmsh_post('"+str(self.study_path+"/s_polymers_st_1_aster.resu.msh")+"');\n"
      return commande

