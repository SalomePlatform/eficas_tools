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
#  Liste des mots cles de config remplaces dans les fichiers à trous 
#
CONFIGliste=('NAME_SCHEME', 'PATH_ASTER', 'PATH_BENHUR', 'PATH_MODULE', 'PATH_PYGMEE', 'PATH_STUDY', 'repIni', 'PATH_FDVGRID' ,'PATH_GMSH')

#_____________________________________________________________________
# Attention les variables suivantes sont nécessaires entre les codes :
# finesse et taille

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 's_poly_st_1',
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
       self.ssRepertoire=self.config.appli.readercata.fic_cata.split("/")[-1].split(".")[0]
       liste=[]
       for i in self.listeCODE:
           liste.append(i.keys()[0])
       if len(liste) != len(set(liste)):
           raise AsException("il n'est pas prevu d avoir deux fois le meme code dans ce schema")


   def PYGMEE(self,execution) :
   #--------------------------------------------------------------------
   # utilisation d un fichier a trous pour generer le fichier de l etude

       # on recupere les valeurs de PYGMEE 
       # qui seront utilisés par d autres codes
       # en particulier Benhur et Aster 
       dicoPygmee=self.dictMCVal["PYGMEE"]
       self.taillePYGMEE=dicoPygmee['_PYGMEE_TAILLE']

       monFichierInput=self.config.INSTALLDIR+"/MAP/Templates/"+self.ssRepertoire+"/pygmee_input_template.txt"
       monFichierOutput=self.nom_racine+"/pygmee_input.txt"

       f = file(monFichierInput,"r")
       chaine = f.read()  
       f.close()   

       chaine2=self.remplaceCONFIG(chaine,CONFIGliste)
       chaine=self.remplaceDICO(chaine2,dicoPygmee)

       if  os.path.isfile(monFichierOutput) :
           print "je detruis pygmee_input.txt"
           commande="rm -rf " + monFichierOutput
           os.system (commande)
       f=open(monFichierOutput,'wb')
       f.write(chaine)
       f.close()

       if execution=="non" : return ""

       if ('_PYGMEE_LANCEMENT' in dicoPygmee.keys()) and  dicoPygmee['_PYGMEE_LANCEMENT'] == 'oui':
           commande="echo '__________________';\n"
           commande=commande + "echo 'execution de PYGMEE';\n"
           commande=commande + "cd "+self.nom_racine+";\n"
           commande=commande + "python "+self.config.PATH_PYGMEE+"/pygmee_v1.py;\n"
           commande=commande + "echo 'fin execution de PYGMEE';\n"
           commande=commande + "echo '_____________________';\n\n\n"
           return commande
       else:
           return ""

   def BENHUR(self,execution) :
   #--------------------------------------------------------------------
   #
       dicoBenhur=self.dictMCVal["BENHUR"]
       if hasattr(self,'taillePYGMEE'):
           dicoBenhur["_PYGMEE_TAILLE"]=self.taillePYGMEE
       else :
           dicoBenhur["_PYGMEE_TAILLE"]=0
           print "Attention la variable Taille_VER non definie"
       
       finesse=str(dicoBenhur["_BENHUR_FINESSE"])
       self.finesseBENHUR=finesse

       #Lecture du fichier a trous
       monFichierInput=self.config.INSTALLDIR+"/MAP/Templates/"+self.ssRepertoire+"/benhur_pygmee_template.txt"
       monFichierOutput=self.config.PATH_STUDY+"/"+self.config.NAME_SCHEME+"/"+self.config.NAME_SCHEME+"_benhur_"+finesse+".bhr"
       f = file(monFichierInput)
       chaine = f.read()  
       f.close()   
       chaine2=self.remplaceCONFIG(chaine,CONFIGliste)
       chaine=self.remplaceDICO(chaine2,dicoBenhur)
       f=open(monFichierOutput,'wb')
       f.write(chaine)
       f.close()

       nom_BHR_Files=self.config.PATH_BENHUR+"/BHR_files.txt"
       f=open(nom_BHR_Files,'wb')
       f.write(monFichierOutput)
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
   #--------------------------------------------------------------------
   # utilisation de deux fichiers a trous pour generer les .comm et .export
      print "Generation de ASTER"
      dicoAster=self.dictMCVal["ASTER"]

      try :
         dicoAster["_PYGMEE_TAILLE"]=self.taillePYGMEE
      except :
         print "Necessite de definir PYGMEE"
      try :
         dicoAster["_BENHUR_FINESSE"]=self.finesseBENHUR
      except :
         print "Necessite de definir BENHUR"

      monFichierCommOutput=self.nom_racine+"s_poly_st_1_aster.comm"
      monFichierExportOutput=self.nom_racine+"s_poly_st_1_aster.export"
      self.monFichierMSH=self.nom_racine+"/"+self.config.NAME_SCHEME+"_aster.resu.msh"

      monFichierCommInput=self.config.INSTALLDIR+"/MAP/Templates/"+self.ssRepertoire+"/s_poly_st_1_aster_template.comm"
      monFichierExportInput=self.config.INSTALLDIR+"/MAP/Templates/"+self.ssRepertoire+"/s_poly_st_1_aster_template.export"

      #Lecture du fichier a trous a pour le fichier export
      f = file(monFichierExportInput)
      chaine = f.read()  
      f.close()   
      chaine2=self.remplaceCONFIG(chaine,CONFIGliste)
      chaine=self.remplaceDICO(chaine2,dicoAster)
      f=open(monFichierExportOutput,'wb')
      f.write(chaine)
      f.close()

      #Lecture du fichier a trous a pour le fichier comm
      f = file(monFichierCommInput)
      chaine = f.read()  
      f.close()   
      chaine2=self.remplaceCONFIG(chaine,CONFIGliste)
      chaine=self.remplaceDICO(chaine2,dicoAster)
      f=open(monFichierCommOutput,'wb')
      f.write(chaine)
      f.close()

      if ('_ASTER_LANCEMENT' in dicoAster.keys()) and  dicoAster['_ASTER_LANCEMENT'] == 'oui':
         commande="cd "+self.config.PATH_MODULE+";"
         commande=commande + self.config.PATH_ASTER + "bin/as_run "+monFichierExportOutput +";\n"
         return commande
      else:
         return ""

   def FDVGRID(self,execution) :
   #--------------------------------------------------------------------
   #
       dicoFdvgrid=self.dictMCVal["FDVGRID"]
       if execution=="non" : return ""
       fichierInput=self.config.PATH_FDVGRID+'../user/boules_15_B11_2024.txt'
       chaine="%_PATH_FDVGRID%/fdvgrid %_FDVGRID_DIMENSION% %_FDVGRID_DIFFUSION_COMPOX% %_FDVGRID_DIFFUSION_COMPOY% "
       chaine=chaine +"%_FDVGRID_DIFFUSION_COMPOZ% %_FDVGRID_FORMULATION% %_FDVGRID_CL% "
       chaine=chaine +"%_FDVGRID_DISCRET% %_FDVGRID_SOLVER% %_FDVGRID_RESIDU%"
       chaine2=self.remplaceCONFIG(chaine,CONFIGliste)
       chaine=self.remplaceDICO(chaine2,dicoFdvgrid)
       return chaine
      #  ./fdvgrid 3D 1.0 0.0 0.0 v t 100 cross 1.e-4


   def GMSH(self,execution) :
      dicoGmsh=self.dictMCVal["GMSH"]
      if ('_GMSH_LANCEMENT' in dicoGmsh.keys()) and  dicoGmsh['_GMSH_LANCEMENT'] == 'oui':
         commande=self.config.PATH_GMSH+"/gmsh "
         commande=commande + self.monFichierMSH+";\n"
         return commande
      else:
         return ""


