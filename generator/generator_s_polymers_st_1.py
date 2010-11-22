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
   
   def verifie(self):
       liste=[]
       for i in self.listeCODE:
           liste.append(i.keys()[0])
       if len(liste) != len(set(liste)):
           raise AsException("il n'est pas prevu d avoir deux fois le meme code dans ce schema")

# I - YACS functions
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

   def METHODEYACS(self, SchemaYacs, proc):
      self.PYGMEEYACS(SchemaYacs, proc)
      if (self.CHOIX=="FD+grid") : self.FDVGRIDYACS(SchemaYacs,proc)

# II - shell functions
   def ETUDE(self,execution) :
      self.dicoETUDE=self.dictMCVal["ETUDE"]
      print "_____________________"
      print self.dicoETUDE
      print "ETUDE Ok"
      print "_____________________\n"
      return ""
   
   def MATERIAUX(self,execution) :
      self.dicoMATERIAUX=self.dictMCVal["MATERIAUX"]
      print "_____________________"
      print self.dicoMATERIAUX
      print "MATERIAUX Ok"
      print "_____________________\n"
      return ""

   def DISCRETISATION(self,execution) :
      self.dicoDISCRETISATION=self.dictMCVal["DISCRETISATION"]
      print "_____________________"
      print self.dicoDISCRETISATION
      print "DISCRETISATION Ok"
      print "_____________________\n"
      return ""

   def METHODE(self,execution) :
      self.dicoMETHODE=self.dictMCVal["METHODE"]
      print "_____________________"
      print self.dicoMETHODE
      print "METHODE Ok"
      print "_____________________\n"

      if (self.LANCEMENT =='oui') :
         pass
      if (self.LANCEMENT =='non') :
         return ""

      commande=self.PYGMEE()
      if (self.CHOIX=="FD+grid") :
          print "option fdvgrid"
          commande+= self.FDVGRID()
          return commande
      if (choix=="FEM+mesh") :
          print "option Code_Aster"
          commande+= self.BENHUR()
          commande+= self.ASTER()
          commande+= self.GMSH()
          return commande

# III - code and component functions
   def PYGMEE(self) :
      commande_python="import os,sys;\n"
      commande_python+="sys.path.append(os.path.join(os.getenv('MAP_DIRECTORY'), '../EficasV1/MAP/Templates/s_polymers_st_1'));\n"
      commande_python+="from s_polymers_st_1_YACS_nodes import *;\n"
      commande_python+="component_pygmee_v2("+str(self.rve_size)+",1,"+str(self.sieve_curve_in)+","+str(self.sieve_curve_out)+","+str(self.repulsion_distance)+","+str(self.study_name)+","+str(self.study_path)+","+str(self.inclusion_name)+","+str(self.rve_name)+");\n"
      return 'python -c "'+commande_python+'"\n'

   def FDVGRID(self):
      commande_python="import os,sys;\n"
      commande_python+="sys.path.append(os.path.join(os.getenv('MAP_DIRECTORY'), '../EficasV1/MAP/Templates/s_polymers_st_1'));\n"
      commande_python+="from s_polymers_st_1_YACS_nodes import *;\n"
      commande_python+="lambda_x=component_fdvgrid("+str(self.lambda_I)+","+str(self.lambda_M)+","+str(self.rve_size)+",'"+str(self.inclusion_name)+"',"+str(self.finesse)+");\n"
      return 'python -c "'+commande_python+'"\n'

   def BENHUR(self):
      commande="echo 'execution de BENHUR';\n"
      #Lecture du fichier a trous
      print "name_SCHEME =", self.config.NAME_SCHEME
      monFichierInput=self.config.INSTALLDIR+"/MAP/Templates/"+self.config.NAME_SCHEME+"/benhur_template.txt"
      monFichierOutput=self.config.PATH_STUDY+"/"+self.config.NAME_SCHEME+"_benhur_"+str(finesse)+".bhr"

      f = file(monFichierInput)
      string_0 = f.read()  
      f.close()
      # find and replace with CONFIG idctionnary
      string_1=self.remplaceCONFIG(string_0,CONFIGliste)
      dicoBenhur=dict()
      dicoBenhur["_RVE_SIZE"]=self.size
      dicoBenhur["_MESH_SIZE"]=finesse
      dicoBenhur["_INCLUSION_FILE"]=self.inclusion_name
      # find and replace with BENHUR dictionnary
      string_2=self.remplaceDICO(string_1,dicoBenhur)
      # write into ouput file
      f=open(monFichierOutput,'wb')
      f.write(string_2)
      f.close()
      # launch of BENHUR on the previous file
      commande=commande + "cd "+self.config.PATH_BENHUR+"/bin;\n"
      commande=commande + "./benhur -i "+monFichierOutput+";\n"
      commande=commande + "echo 'fin execution de BENHUR';\n"
      return commande

   def ASTER(self,execution) :
      commande="echo 'execution de CODE_ASTER';\n"
      monFichierCommInput=self.config.INSTALLDIR+"/MAP/Templates/"+self.config.NAME_SCHEME+"/s_polymers_st_1_aster_template.comm"
      monFichierExportInput=self.config.INSTALLDIR+"/MAP/Templates/"+self.config.NAME_SCHEME+"/s_polymers_st_1_aster_template.export"

      monFichierCommOutput=self.config.PATH_STUDY+"/s_polymers_st_1_aster.comm"
      monFichierExportOutput=self.config.PATH_STUDY+"/s_polymers_st_1_aster.export"
      # Lecture du fichier a trous a pour le fichier export
      f = file(monFichierExportInput)
      string_0 = f.read()  
      f.close()
      # find and replace with CONFIG dictionnary
      string_1=self.remplaceCONFIG(string_0,CONFIGliste)            
      # find and replace with CODE_ASTER dictionnary
      dicoAster=dict()
      dicoAster["_MESH_SIZE"]=finesse
      dicoAster["_ASTER_VERSION"]="STA10"
      dicoAster["_NAME_STUDY"]="s_polymers_st_1"
      string_2=self.remplaceDICO(string_1,dicoAster)
      # write into output file
      f=open(monFichierExportOutput,'wb')
      f.write(string_2)
      f.close()

      # Lecture du fichier a trous a pour le fichier comm
      f = file(monFichierCommInput)
      string_0 = f.read()  
      f.close()
      # find and replace with CONFIG dictionnary
      string_1=self.remplaceCONFIG(string_0,CONFIGliste)       
      # find and replace with CODE_ASTER dictionnary
      dicoAster=dict()
      dicoAster["_RVE_SIZE"]=self.size
      dicoAster["_CONDUCTIVITE_I"]=self.dicoMATERIAUX["_MATERIAUX_CONDUCTIVITE_I"]
      dicoAster["_CONDUCTIVITE_M"]=self.dicoMATERIAUX["_MATERIAUX_CONDUCTIVITE_M"]
      string_2=self.remplaceDICO(string_1,dicoAster)
      # write into output file
      f=open(monFichierCommOutput,'wb')
      f.write(string_2)
      f.close()
      # launch of CODE_ASTER on the study
      commande=commande + "cd "+self.config.PATH_STUDY+";"
      commande=commande + self.config.PATH_ASTER + "/as_run "+monFichierExportOutput +";\n"
      commande=commande + "echo 'fin execution de CODE_ASTER';\n"
      return commande

   def GMSH(self,execution) :
      commande="echo 'execution de GMSH';\n"
      commande+= "gmsh "+self.config.PATH_STUDY+"/s_polymers_st_1_aster.resu.msh;\n"
      commande+= "echo 'fin execution de GMSH';\n"
      return commande
