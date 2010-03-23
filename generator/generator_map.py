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

CONFIGliste=('NAME_SCHEME', 'PATH_ASTER', 'PATH_BENHUR', 'PATH_MODULE', 'PATH_PYGMEE', 'PATH_STUDY', 'REPINI')
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

   def gener(self,obj,format='brut',config=None):
      self.config=config
      self.dictMCVal={}
      self.listeTemp=[]
      self.text=PythonGenerator.gener(self,obj,format)
      self.generePythonMap()
      return self.text

   def generRUN(self,obj,format='brut',config=None):
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
          print txt
          return txt
       else :
          return ""

   def BENHUR(self) :
       print "Generation de BENHUR"
       dicoBenhur=self.dictMCVal["BENHUR"]
       if ("PYGMEE" in self.dictMCVal.keys()) and '_PYGMEE_TAILLE' in self.dictMCVal['PYGMEE']:
           dicoBenhur["_PYGMEE_TAILLE"]=self.dictMCVal["PYGMEE"]['_PYGMEE_TAILLE']
       else :
           dicoBenhur["_PYGMEE_TAILLE"]=0
           print "Attention la variable Taille_VER non definie"
       
       nom_fichier_BHR=self.config.PATH_STUDY+"/"+self.config.NAME_SCHEME+"_benhur_"+str(dicoBenhur["_BENHUR_FINESSE"])+".bhr"

       #Lecture du fichier a trous
       f = file(self.config.REPINI+"/benhur_pygmee.txt","r")
       chaine = f.read()  
       f.close()   
       chaine2=self.remplaceCONFIG(chaine)
       chaine=self.remplaceDICO(chaine2,dicoBenhur)
       if ('_BENHUR_LANCEMENT' in dicoBenhur.keys()) and  dicoBenhur['_BENHUR_LANCEMENT'] == 'oui':
           return(nom_fichier_BHR,chaine)
       else:
          return ""

   def  remplaceCONFIG(self,chaine) :
       for mot in CONFIGliste :
           rplact="%_"+mot+"%"
           result=chaine.replace(rplact,self.config.__dict__[mot])
           chaine=result
       return chaine

   def  remplaceDICO(self,chaine,dico) :
       for mot in dico.keys() :
           rplact="%"+mot+"%"
           result=chaine.replace(rplact,str(dico[mot]))
           print rplact 
           print str(dico[mot])
           chaine=result
       return chaine


   def ASTER(self) :
      print "Generation de ASTER"
      dicoAster=self.dictMCVal["ASTER"]
      nom_racine=self.config.PATH_MODULE+"/"+self.config.NAME_SCHEME+"/"+self.config.NAME_SCHEME
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
         commande="cd "+self.config.PATH_MODULE+";"
         commande=commande + self.config.PATH_ASTER + "/as_run "+self.config.PATH_MODULE
         commande=commande + "/"+self.config.NAME_SCHEME+"/"+self.config.NAME_SCHEME+"_aster.export"
         print commande
         os.system(commande)
      else:
         return ""

   def GMSH(self) :
      print "Generation de GMSH"
      dicoGmsh=self.dictMCVal["GMSH"]
      if ('_GMSH_LANCEMENT' in dicoGmsh.keys()) and  dicoGmsh['_GMSH_LANCEMENT'] == 'oui':
         commande="cd "+self.config.PATH_MODULE+";"
         commande=commande + "gmsh "+self.config.PATH_MODULE+"/"+self.config.NAME_SCHEME+"/"+self.config.NAME_SCHEME+"_aster.resu.msh"
         print commande
         os.system(commande)
      else:
         return ""
