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


   def PYGMEE(self,execution) :
       dicoPygmee=self.dictMCVal["PYGMEE"]
       self.dictPYGMEE=dicoPygmee
       monFichier=self.config.PATH_PYGMEE+"/pygmee_input.txt"

       #Lecture du fichier a trous
       f = file(self.config.repIni+"/pygmee_input.txt","r")
       chaine = f.read()  
       f.close()   
       chaine2=self.remplaceCONFIG(chaine,CONFIGliste)
       chaine=self.remplaceDICO(chaine2,dicoPygmee)

       if  os.path.isfile(monFichier) :
           print "je detruis pygmee_input.txt"
           commande="rm -rf " + monFichier
           os.system (commande)
       f=open(monFichier,'wb')
       f.write(chaine)
       f.close()
       if execution=="non" : return ""

       if ('_PYGMEE_LANCEMENT' in dicoPygmee.keys()) and  dicoPygmee['_PYGMEE_LANCEMENT'] == 'oui':
           commande="echo '__________________';\n"
           commande=commande + "echo 'execution de PYGMEE';\n"
           commande=commande + "cd "+self.config.PATH_PYGMEE+";\n"
           commande=commande + "python "+self.config.PATH_PYGMEE+"/pygmee_v1.py;\n"
           commande=commande + "echo 'fin execution de PYGMEE';\n"
           commande=commande + "echo '_____________________';\n\n\n"
           return commande
       else:
           return ""

   def BENHUR(self,execution) :
       dicoBenhur=self.dictMCVal["BENHUR"]
       if hasattr(self,'dictPYGMEE') and '_PYGMEE_TAILLE' in self.dictMCVal['PYGMEE']:
           dicoBenhur["_PYGMEE_TAILLE"]=self.dictPYGMEE['_PYGMEE_TAILLE']
       else :
           dicoBenhur["_PYGMEE_TAILLE"]=0
           print "Attention la variable Taille_VER non definie"
       
       finesse=str(dicoBenhur["_BENHUR_FINESSE"])
       nom_fichier_BHR=self.config.PATH_STUDY+"/"+self.config.NAME_SCHEME+"_benhur_"+finesse+".bhr"
       nom_BHR_Files=self.config.PATH_BENHUR+"/BHR_files.txt"

       #Lecture du fichier a trous
       f = file(self.config.repIni+"/benhur_pygmee.txt","r")
       chaine = f.read()  
       f.close()   
       chaine2=self.remplaceCONFIG(chaine,CONFIGliste)
       chaine=self.remplaceDICO(chaine2,dicoBenhur)

       try :
          f=open(nom_fichier_BHR,'wb')
       except :
          print "Pb de Generation de BENHUR"
          return ""
       f.write(chaine)
       f.close()

       f=open(nom_BHR_Files,'wb')
       f.write(nom_fichier_BHR)
       f.write("\n\n\n")
       f.close()

       if execution=="non" : return ""
       if ('_BENHUR_LANCEMENT' in dicoBenhur.keys()) and  dicoBenhur['_BENHUR_LANCEMENT'] == 'oui':
           commande="echo '__________________';\n"
           commande=commande + "echo 'execution de BENHUR';\n"
           commande=commande + "cd "+self.config.PATH_BENHUR+";\n"
           commande=commande + "./benhur;\n"
           commande=commande + "echo 'fin execution de BENHUR';\n"
           commande=commande + "echo '________________________';\n\n\n"
           return commande
       else:
          return ""



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
      print "METHODE"
      return ""

   def MATERIAUX(self,execution) :
      print "MATERIAUX"
      return ""

   def DISCRETISATION(self,execution) :
      print "DISCRETISATION"
      return ""
