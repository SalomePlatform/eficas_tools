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
# PYGMEEDict contient une equivalence entre le catalogue Map et les lignes generees
# comme entete (commentaire ?) dans le fichier d'input de pygmee
#

CONFIGliste=('NAME_SCHEME', 'PATH_ASTER', 'PATH_BENHUR', 'PATH_MODULE', 'PATH_PYGMEE', 'PATH_STUDY', 'repIni')
PYGMEEDict={
       "_PYGMEE_FUSEAU1_b_forme_FICHIER"  : "#fuseau 1 (entree de lecfus) format : diametre DCE croissant / fraction cumulee decroisant ",
       "FUSEAU2" :  "#fuseau 2 (entree de lecfus) format : diametre DCE croissant / fraction cumulee decroisant",
       "_PYGMEE_TAILLE" : "# taille du VER en microns ",
       "_PYGMEE_DISTANCE" : "# distance de repulsion :",
           }

#_______________________________________________________________________________________________________
# listeOrdonneeMCPygmee contient une liste (donc ordonnee) des mots clefs pour 
# imposer l'ordre des  lignes generees
listeOrdonneeMCPygmee =('_PYGMEE_FUSEAU1_b_forme_FICHIER', 'FUSEAU2', '_PYGMEE_TAILLE','_PYGMEE_DISTANCE')


BENHURDict={
       "_BENHUR_FINESSE" : "discretisation des arretes du VER ",
           }

ASTERDict={
       "_ASTER_LANCEMENT" : "execution de Code_Aster",
       "_ASTER_CONDUCTIVITE_I" : "conductivite des inclusions",
       "_ASTER_CONDUCTIVITE_M" : "conductivite de la matrice",
           }

GMSHDict={
       "_GMSH_LANCEMENT" : "execution de GMSH",
           }

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

   def ASTER(self,execution) :
      print "Generation de ASTER"
      dicoAster=self.dictMCVal["ASTER"]
      nom_racine=self.config.PATH_MODULE+"/"+self.config.NAME_SCHEME+"/"+self.config.NAME_SCHEME
      nom_fichier_ASTER=nom_racine+"_aster.comm"

      #Lecture du fichier a trous
      f = file(self.config.repIni+"/s_poly_st_1_aster_template.comm","r")
      chaine = f.read()  
      f.close()   
      chaine2=self.remplaceDICO(chaine,self.dictPYGMEE)
      chaine=self.remplaceDICO(chaine2,dicoAster)

      f=open(nom_fichier_ASTER,'wb')
      f.write(chaine)
      f.close()

      if ('_ASTER_LANCEMENT' in dicoAster.keys()) and  dicoAster['_ASTER_LANCEMENT'] == 'oui':
         commande="cd "+self.config.PATH_MODULE+";"
         commande=commande + self.config.PATH_ASTER + "/as_run "+self.config.PATH_MODULE
         commande=commande + "/"+self.config.NAME_SCHEME+"/"+self.config.NAME_SCHEME+"_aster.export"
         os.system(commande)
      else:
         return ""

   def GMSH(self,execution) :
      dicoGmsh=self.dictMCVal["GMSH"]
      if ('_GMSH_LANCEMENT' in dicoGmsh.keys()) and  dicoGmsh['_GMSH_LANCEMENT'] == 'oui':
         commande="cd "+self.config.PATH_MODULE+";"
         commande=commande + "gmsh "+self.config.PATH_MODULE+"/"+self.config.NAME_SCHEME+"/"+self.config.NAME_SCHEME+"_aster.resu.msh"
         print commande
         os.system(commande)
      else:
         return ""

   def METHODE(self,execution) :
      self.config.PATH_STUDY=self.config.PATH_MAP+"/studies/demonstrateur_s_polymers_st_1"
      print "self.config.PATH_STUDY has been forced to :", self.config.PATH_STUDY
      self.dicoMETHODE=self.dictMCVal["METHODE"]
      print "_____________________"
      print self.dicoMETHODE
      result=self.dicoMETHODE['_METHODE_LANCEMENT']
      print '_METHODE_LANCEMENT =', result
      if (result=='oui') :
         composant="pygmee_v2"
         self.size=float(self.dicoMATERIAUX['_MATERIAUX_TAILLE'])
         self.sieve_in=self.config.PATH_PYGMEE+"/tests/pygmee_v2_test_1.sieve_in"
         self.sieve_out=self.config.PATH_STUDY+"/pygmee_v2.sieve_out"
         self.distance=self.dicoMATERIAUX['_MATERIAUX_DISTANCE']
         self.inclusion_name=self.config.PATH_STUDY+"/pygmee_v2_test_1.inclusions"
         self.rve_name=self.config.PATH_STUDY+"/pygmee_v2_test_1.rve"
         pygmee_v2_input=self.config.PATH_STUDY+"/pygmee_v2.input"
         print "pygmee_v2_input =", pygmee_v2_input
         parameter=MAP_parameters()
         parameter.add_component(composant)
         parameter.add_parameter(composant, 'rve_size', self.size)
         parameter.add_parameter(composant, 'phase_number', 1)
         parameter.add_parameter(composant, 'sieve_curve_in', self.sieve_in)
         parameter.add_parameter(composant, 'sieve_curve_out',  self.sieve_out)
         parameter.add_parameter(composant, 'repulsion_distance', self.distance)
         parameter.add_parameter(composant, 'study_name', "study")
         parameter.add_parameter(composant, 'file_result_inclusions', self.inclusion_name)
         parameter.add_parameter(composant, 'file_result_rve', self.rve_name)
         commande_python=parameter.write_for_shell(pygmee_v2_input)
         commande="echo 'parametres de PYGMEE v2';\n"

         commande+= commande_python
         
         commande+= "echo 'execution de PYGMEE v2';\n"
         commande+= "cd "+self.config.PATH_PYGMEE+"/src;\n"
         commande+= "python pygmee_v2.py -i "+pygmee_v2_input+";\n"
         commande+= "echo 'fin execution de PYGMEE v2';\n"

         self.contrast=float(self.dicoMATERIAUX['_MATERIAUX_CONDUCTIVITE_I']/self.dicoMATERIAUX['_MATERIAUX_CONDUCTIVITE_M'])
         choix=self.dicoMETHODE['_METHODE_CHOIX']

         finesse=int(self.dicoDISCRETISATION['_DISCRETISATION_FINESSE'])

         if (choix=="FD+grid") :
            commande+= "echo 'execution de FDVGRID';\n"
            commande+= "cd "+self.config.PATH_FDVGRID+";\n"
            if (finesse<32):
               finesse=32
            commande+= "echo "+str(self.size)+" > "+"rve.input"+";\n"
            commande+= "cp "+str(self.config.PATH_STUDY+"/pygmee_v2_test_1.inclusions")+" "+"inclusions.input"+";\n"
            commande+= "echo "+str(self.contrast)+" > "+"contrast.input"+";\n"         
            commande+= "./fdvgrid 3D 1.0 0.0 0.0 v t "+str(finesse)+" cross 1e-6 "+";\n"
            commande+= "echo 'fin execution de FDVGRID';\n"
            print "commande issue du generator :", commande
            
         if (choix=="FEM+mesh") :
            print "option Code_Aster"
            commande+= "echo 'execution de BENHUR';\n"

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
            # find and replace with BENHUR idctionnary
            string_2=self.remplaceDICO(string_1,dicoBenhur)
            # write into ouput file
            f=open(monFichierOutput,'wb')
            f.write(string_2)
            f.close()
            # launch of BENHUR on the previous file
            commande=commande + "cd "+self.config.PATH_BENHUR+"/bin;\n"
            commande=commande + "./benhur -i "+monFichierOutput+";\n"
            commande=commande + "echo 'fin execution de BENHUR';\n"
       
            commande+= "echo 'execution de CODE_ASTER';\n"
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
       
            commande+= "echo 'execution de GMSH';\n"
            commande+= "gmsh "+self.config.PATH_STUDY+"/s_polymers_st_1_aster.resu.msh;\n"
            commande+= "echo 'fin execution de GMSH';\n"
            
            print commande
            
      print "METHODE Ok - 20101105"
      print "_____________________\n"
      return commande

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
