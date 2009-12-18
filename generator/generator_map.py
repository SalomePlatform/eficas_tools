# -*- coding: utf-8 -*-
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

from generator_python import PythonGenerator

#____________________________________________________________________________________
# PYGMEEDict contient une equivalence entre le catalogue Map et les lignes generees
# comme entete (commentaire ?) dans le fichier d'input de pygmee
#
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


def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'map',
        # La factory pour creer une instance du plugin
          'factory' : MapGenerator,
          }


class MapGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et
      un texte au format py

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

   def gener(self,obj,format='brut',configuration=None):
      self.PATH_PYGMEE=configuration.PATH_PYGMEE
      self.PATH_BENHUR=configuration.PATH_BENHUR
      self.dictMCVal={}
      self.listeTemp=[]
      self.text=PythonGenerator.gener(self,obj,format)
      self.generePythonMap()
      return self.text

   def generePythonMap(self) :
      '''
         self.dictMCVal est un dictionnaire qui est indexe par le nom du code (exple PYGMEE)
         la valeur associee a la clef est egalement un dictionnaire 
         ce dictionnaire a pour clef la genealogie du MCSimp suivi de sa valeur

      '''
      for code in self.dictMCVal.keys():
          self.texte=apply(MapGenerator.__dict__[code],(self,))
      return 'a faire'

   def generPROC_ETAPE(self,obj):
      #print "PN: generPROC_ETAPE dans generatorMap"
      self.clefDico=obj.nom
      if not( self.dictMCVal.has_key(self.clefDico)):
         self.dictMCVal[self.clefDico]={}
         self.DictTemp=self.dictMCVal[self.clefDico]
      s=PythonGenerator.generPROC_ETAPE(self,obj)
      return s


   def generMCSIMP(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      Remplit le dictionnaire des MCSIMP si nous ne sommes ni dans une loi, ni dans une variable
      """
      s=PythonGenerator.generMCSIMP(self,obj)
      clef=""
      for i in obj.get_genealogie() :
           clef=clef+"_"+i
      self.DictTemp[clef]=obj.valeur
      return s

   def PYGMEE(self) :
       print "Generation de PYGMEE"
       dicoPygmee=self.dictMCVal["PYGMEE"]
       dicoPygmee['FUSEAU2']='toto.txt'

       txt="# fichier de mise en donnee de la generation du VER MOX" +"\n"
       txt=txt+"# nombre de phases"+"\n"
       txt=txt+"1"+"\n"
       for mot in listeOrdonneeMCPygmee :
           if mot in dicoPygmee.keys() :
              txt=txt+PYGMEEDict[mot]+"\n"
              txt=txt+str(dicoPygmee[mot])+"\n"

       monFichier=self.PATH_PYGMEE+"/pygmee_input.txt"
       if  os.path.isfile(monFichier) :
           #print "je detruis pygmee_input.txt"
           commande="rm -rf " + monFichier
           os.system (commande)
       f=open(monFichier,'wb')
       f.write(txt)
       f.close()
       if ('_PYGMEE_LANCEMENT' in dicoPygmee.keys()) and  dicoPygmee['_PYGMEE_LANCEMENT'] == 'oui':
           commande="cd "+self.PATH_PYGMEE+";"
           commande=commande + "python "+self.PATH_PYGMEE+"/pygmee_v1.py"
           #print commande
           os.system(commande)
       else:
          return ""

   def BENHUR(self) :
       print "Generation de BENHUR"
       dicoBenhur=self.dictMCVal["BENHUR"]
       nom_fichier_fuseau=self.PATH_BENHUR+"/benhur_input.txt"
       
       nom_fichier_BHR=self.PATH_BENHUR+"/test_module.bhr"
       nom_BHR_Files=self.PATH_BENHUR+"/BHR_files.txt"

       finesse=str(dicoBenhur['_BENHUR_FINESSE'])
       if ("PYGMEE" in self.dictMCVal.keys()) and '_PYGMEE_TAILLE' in self.dictMCVal['PYGMEE']:
           taille_VER=self.dictMCVal["PYGMEE"]['_PYGMEE_TAILLE']
       else :
           taille_VER=0
           print "Attention la variable Taille_VER non definie"
       nom_GMSH_in=self.PATH_BENHUR+"/regular_mesh_3D_i"+finesse+".msh"
       nom_etude=self.PATH_BENHUR+"/test_module_"+finesse
       nom_GMSH_out=nom_etude+".msh"
       nom_LOG=nom_etude+".log"
       nom_BMP=nom_etude+".bmp"
       nom_LEVELSET=nom_etude+"_levelset.txt"
       nom_GMSH_out=nom_etude+".msh"
       nom_LOG=nom_etude+".log"
       nom_BMP=nom_etude+".bmp"
       nom_LEVELSET=nom_etude+"_levelset.txt"
       f=open(nom_BHR_Files,'wb')
       f.write(nom_fichier_BHR)
       f.write("\n")
       f.write("\n")
       f.write("\n")
       f.close()
       f=open(nom_fichier_BHR,'wb')
       f.write("3D BENHUR SCALE\n")
       f.write("I - Morphologie (MESSALA)\n")
       f.write("1) dimension du VER cubique [m] (entree)\n")
       f.write(str(taille_VER))
       f.write("\n2) fraction volumique seuil écrétant le fuseau (entree)\n")
       f.write(".11\n")
       f.write("3) fichier decrivant le fuseau granulaire descendant (entree)\n")
       f.write("-\n")
       f.write("4) fichier decrivant la position et la taille des boules (sortie)\n")
       f.write(nom_fichier_fuseau)
       f.write("\n5) fichier CAO de la morphologie (sortie)\n")
       f.write("-\n")
       f.write("6) facteur de correction de fraction volumique (entree)\n")
       f.write("1.0\n")
       f.write(" \n")
       f.write("II - Maillage (BENHUR)\n")
       f.write("1) fichier entree décrivant le maillage support (entree)\n")
       f.write(nom_GMSH_in);
       f.write("\n2) fichier sortie du maillage  (sortie)\n")
       f.write(nom_GMSH_out);
       f.write("\n3) fichier commentaire sur les statistiques décrivant le maillage (sortie)\n")
       f.write(nom_LOG);
       f.write("\n4) fichier BMP décrivant une coupe binarisée du VER (sortie)\n")
       f.write(nom_BMP);
       f.write("\n5) fichier TXT donnant la level set du contour aux noeuds (sortie)\n")
       f.write(nom_LEVELSET)
       f.write("\n")
       f.write("\n")
       f.write("\n")
       f.close()

       if ('_BENHUR_LANCEMENT' in dicoBenhur.keys()) and  dicoBenhur['_BENHUR_LANCEMENT'] == 'oui':
           commande="cd "+self.PATH_BENHUR+";"
           commande=commande + "./benhur"
           print commande
           os.system(commande)
       else:
          return ""

   def ASTER(self) :
       print "Generation de ASTER"

