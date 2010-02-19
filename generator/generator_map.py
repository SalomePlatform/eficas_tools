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
      self.PATH_ASTER=configuration.PATH_ASTER
      self.PATH_MODULE=configuration.PATH_MODULE
      self.NAME_SCHEME=configuration.NAME_SCHEME
      self.PATH_STUDY=configuration.PATH_STUDY
      self.dictMCVal={}
      self.listeTemp=[]
      self.text=PythonGenerator.gener(self,obj,format)
      self.generePythonMap()
      return self.text

   def generRUN(self,obj,format='brut',configuration=None):
      self.PATH_PYGMEE=configuration.PATH_PYGMEE
      self.PATH_BENHUR=configuration.PATH_BENHUR
      self.PATH_ASTER=configuration.PATH_ASTER
      self.PATH_MODULE=configuration.PATH_MODULE
      self.NAME_SCHEME=configuration.NAME_SCHEME
      self.PATH_STUDY=configuration.PATH_STUDY
      self.dictMCVal={}
      self.listeTemp=[]
      self.text=PythonGenerator.gener(self,obj,format)
      #self.generePythonMap()
      dicoRun={}
      for code in self.dictMCVal.keys():
          listeTexte=apply(MapGenerator.__dict__[code],(self,))
          dicoRun[code]=listeTexte
      return dicoRun


   def generePythonMap(self) :
      '''
         self.dictMCVal est un dictionnaire qui est indexe par le nom du code (exple PYGMEE)
         la valeur associee a la clef est egalement un dictionnaire 
         ce dictionnaire a pour clef la genealogie du MCSimp suivi de sa valeur

      '''
      for code in self.dictMCVal.keys():
          self.texte=apply(MapGenerator.__dict__[code],(self,))

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

       if ('_PYGMEE_LANCEMENT' in dicoPygmee.keys()) and  dicoPygmee['_PYGMEE_LANCEMENT'] == 'oui':
          return txt
       else :
          return ""

   def BENHUR(self) :
       print "Generation de BENHUR"
       dicoBenhur=self.dictMCVal["BENHUR"]
       finesse=str(dicoBenhur['_BENHUR_FINESSE'])
       
       nom_fichier_BHR=self.PATH_STUDY+"/"+self.NAME_SCHEME+"_benhur_"+finesse+".bhr"

       if ("PYGMEE" in self.dictMCVal.keys()) and '_PYGMEE_TAILLE' in self.dictMCVal['PYGMEE']:
           taille_VER=self.dictMCVal["PYGMEE"]['_PYGMEE_TAILLE']
       else :
           taille_VER=0
           print "Attention la variable Taille_VER non definie"

       nom_etude=self.PATH_STUDY+"/"+self.NAME_SCHEME+"_benhur_"+finesse
       nom_GMSH_in=self.PATH_BENHUR+"/regular_mesh_3D_"+finesse+".msh"
       nom_GMSH_out=nom_etude+".msh"
       nom_GMSH_in="regular_mesh_3D_"+finesse+".msh"
       nom_GMSH_out=nom_etude+".msh"
       nom_LOG=nom_etude+".log"
       nom_BMP=nom_etude+".bmp"
       nom_LEVELSET=nom_etude+"_levelset.txt"
       nom_GMSH_out=nom_etude+".msh"
       nom_LOG=nom_etude+".log"
       nom_BMP=nom_etude+".bmp"
       nom_LEVELSET=nom_etude+"_levelset.txt"
       nom_fichier_fuseau=self.PATH_PYGMEE+"/benhur_input.txt"


       txt="OPTIONS\n"
       txt=txt+"3D BENHUR SCALE\n"
       txt=txt+"I - Morphologie (MESSALA)\n"
       txt=txt+"1) dimension du VER cubique [m] (entree)\n"
       txt=txt+str(taille_VER)
       txt=txt+"\n2) fraction volumique seuil écrétant le fuseau (entree)\n"
       txt=txt+".11\n"
       txt=txt+"3) fichier decrivant le fuseau granulaire descendant (entree)\n"
       txt=txt+"-\n"
       txt=txt+"4) fichier decrivant la position et la taille des boules (sortie)\n"
       txt=txt+nom_fichier_fuseau
       txt=txt+"\n5) fichier CAO de la morphologie (sortie)\n"
       txt=txt+"-\n"
       txt=txt+"6) facteur de correction de fraction volumique (entree)\n"
       txt=txt+"1.0\n"
       txt=txt+" \n"
       txt=txt+"II - Maillage (BENHUR)\n"
       txt=txt+"1) fichier entree décrivant le maillage support (entree)\n"
       txt=txt+nom_GMSH_in
       txt=txt+"\n2) fichier sortie du maillage  (sortie)\n"
       txt=txt+nom_GMSH_out
       txt=txt+"\n3) fichier commentaire sur les statistiques décrivant le maillage (sortie)\n"
       txt=txt+nom_LOG
       txt=txt+"\n4) fichier BMP décrivant une coupe binarisée du VER (sortie)\n"
       txt=txt+nom_BMP
       txt=txt+"\n5) fichier TXT donnant la level set du contour aux noeuds (sortie)\n"
       txt=txt+nom_LEVELSET
       txt=txt+"\n\n\n"

       if ('_BENHUR_LANCEMENT' in dicoBenhur.keys()) and  dicoBenhur['_BENHUR_LANCEMENT'] == 'oui':
           return(nom_fichier_BHR,txt)
       else:
          return ""

   def ASTER(self) :
      print "Generation de ASTER"
      dicoAster=self.dictMCVal["ASTER"]
      nom_racine=self.PATH_MODULE+"/"+self.NAME_SCHEME+"/"+self.NAME_SCHEME
      nom_mat=nom_racine+"_aster.mat"
      lambda_matrice=self.dictMCVal["ASTER"]['_ASTER_CONDUCTIVITE_M']
      lambda_inclusions=self.dictMCVal["ASTER"]['_ASTER_CONDUCTIVITE_I']
      contraste=lambda_inclusions/lambda_matrice
      f=open(nom_mat,'wb')
      for i in range(11):
         fraction=(1.0*i/10)
         lambda_local=1.0+fraction
         f.write(str(lambda_local))
         f.write("\n")
      f.close()
      if ('_ASTER_LANCEMENT' in dicoAster.keys()) and  dicoAster['_ASTER_LANCEMENT'] == 'oui':
         commande="cd "+self.PATH_MODULE+";"
         commande=commande + self.PATH_ASTER + "/as_run "+self.PATH_MODULE+"/"+self.NAME_SCHEME+"/"+self.NAME_SCHEME+"_aster.export"
         print commande
         os.system(commande)
      else:
         return ""

   def GMSH(self) :
      print "Generation de GMSH"
      dicoGmsh=self.dictMCVal["GMSH"]
      if ('_GMSH_LANCEMENT' in dicoGmsh.keys()) and  dicoGmsh['_GMSH_LANCEMENT'] == 'oui':
         commande="cd "+self.PATH_MODULE+";"
         commande=commande + "gmsh "+self.PATH_MODULE+"/"+self.NAME_SCHEME+"/"+self.NAME_SCHEME+"_aster.resu.msh"
         print commande
         os.system(commande)
      else:
         return ""
