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

import traceback
import types,string,re,os
from Extensions.i18n import tr
from generator_python import PythonGenerator
import Accas

debutTextePhys ="[VERSION\n  NUM      1\n  FILETYPE PHYS\n]\n"
debutTextePhys+="[MATERIALS\n   [CONDUCTOR\n"
texteConductor ="      [CONDUCTIVITY\n         LAW LINEAR\n"
texteConductor+="         HOMOGENEOUS TRUE\n"
texteConductor+="         ISOTROPIC  TRUE\n"
texteConducto2 ="  0.0000000000000000E+00\n      ]\n"
texteConducto2+="      [PERMEABILITY\n         LAW LINEAR\n"
texteConducto2+="         HOMOGENEOUS TRUE\n"
texteConducto2+="         ISOTROPIC  TRUE\n"
texteNoCond ="      [PERMITTIVITY\n         LAW LINEAR\n"
texteNoCond+="         HOMOGENEOUS TRUE\n         ISOTROPIC TRUE\n"
texteNoCond+="         VALUE COMPLEX  0.1000000000000000E+01  0.0000000000000000E+00\n"
texteNoCond+="      ]\n      [PERMEABILITY\n         LAW LINEAR\n"
texteNoCond+="         HOMOGENEOUS TRUE\n         ISOTROPIC TRUE\n"

debutTexteParam ="[VERSION\n   NUM     1\n   FILETYPE PARAM\n]\n"
debutTexteParam+="[PROBLEM\n   NAME HARMONIC\n]\n"
debutTexteParam+="[CAR_FILES\n   NAME "


def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins
      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'CARMELSARA',
        # La factory pour creer une instance du plugin
          'factory' : CARMELSARAGenerator,
          }


class CARMELSARAGenerator(PythonGenerator):
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
      self.racine=obj
      return self.text


#----------------------------------------------------------------------------------------
# initialisations
#----------------------------------------------------------------------------------------
   
   def initDico(self) :
 
      self.dictMCVal={}

#----------------------------------------------------------------------------------------
# ecriture
#----------------------------------------------------------------------------------------

   def writeDefault(self,fn) :

       self.texteIngendof=""
       self.texteParam=debutTexteParam
       self.chercheFichier()
       self.traiteSourceVCut()
       fileIngendof = fn[:fn.rfind(".")] + '.ingendof'
       f = open( str(fileIngendof), 'wb')
       f.write( self.texteIngendof )
       f.close()

       self.textePhys=debutTextePhys
       self.traiteMateriaux()
       filePhys = fn[:fn.rfind(".")] + '.phys'
       f = open( str(filePhys), 'wb')
       f.write( self.textePhys )
       f.close()

       fileParam = fn[:fn.rfind(".")] + '.param'
       self.traiteParam()
       f = open( str(fileParam), 'wb')
       f.write( self.texteParam )
       f.close()
       
       self.texteCMD="[ \n    GLOBAL \n] \n[ \nVISU \nDomaine \nMED \nELEMENT \n] "
       fileCMD = fn[:fn.rfind(".")] + '.cmd'
       f = open( str(fileCMD), 'wb')
       f.write( self.texteCMD )
       f.close()
       
       nomBaseFichier=os.path.basename(fileParam).split(".med")[0]
       
       self.texteInfcarmel=nomBaseFichier
       fileInfcarmel = fn[:fn.rfind(".")] + '.infcarmel'
       f = open( str(fileInfcarmel), 'wb')
       f.write( self.texteInfcarmel )
       f.close()
       
       self.texteInpostpro=nomBaseFichier+"\n"+nomBaseFichier.split(".param")[0]+'.xmat\n'+nomBaseFichier.split(".param")[0]+'.cmd'
       fileInpostpro = fn[:fn.rfind(".")] + '.inpostprocess'
       f = open( str(fileInpostpro), 'wb')
       f.write( self.texteInpostpro )
       f.close()

#----------------------------------------------------------------------------------------
#  analyse des commentaires pour trouver le nom du fichier
#----------------------------------------------------------------------------------------

   def chercheFichier(self) :
       nomFichier="inconnu"
       for e in self.racine.etapes:
           if  isinstance(e,Accas.COMMENTAIRE):
               print 'ùmasdkfh=',e.valeur[0:17]
               if e.valeur[0:17]=="Cree - fichier : ":
                  debut=e.valeur[17:]
                  liste=debut.split(" - ")
                  nomFichier=liste[0]
                  print 'nom=',nomFichier
                  print 'e.va=',e.valeur.split(" ")[-1]
                  print 'liste=',liste
                  nomDomaine=e.valeur.split(" ")[-1]
                  break
       self.texteIngendof =os.path.basename(nomFichier)+"\n"
       self.texteParam += os.path.basename(nomFichier).split(".med")[0]+".car\n]\n"
       self.texteParam +="[PHYS_FILES\n   NAME "+os.path.basename(nomFichier).split(".med")[0]+".phys\n]\n"

#----------------------------------------------------------------------------------------
#  analyse du dictionnaire  pour trouver les sources et les VCut
#----------------------------------------------------------------------------------------

   def traiteSourceVCut(self) :
       listeSource=[]
       listeVCut=[]
       self.texteSourcePhys="[SOURCES\n"
       for k in self.dictMCVal.keys():
           if k.find ("______SOURCE__") > -1 :
              noms=k.split("_____")
              if noms[0] not in listeSource : listeSource.append(noms[0])
           if k.find ("______VCUT__") > -1 :
              noms=k.split("_____")
              if noms[0] not in listeVCut : listeVCut.append(noms[0])
       listeSource.sort()
       for source in listeSource:
           debutKey=source+"______SOURCE__"
           texteSource=self.dictMCVal[debutKey+"NomDomaine"]+"\n"
           texteSource+="2\n"
           for val in self.dictMCVal[debutKey+"VecteurDirecteur"] :
               texteSource+=str(val)+" "
           texteSource+="\n"
           for val in self.dictMCVal[debutKey+"Centre"] :
               texteSource+=str(val)+" "
           texteSource+="\n"
           texteSource+=str(self.dictMCVal[debutKey+"SectionDomaine"])+"\n"
           self.texteIngendof+=texteSource
           self.texteSourcePhys+="   [STRANDED_INDUCTOR\n"
           self.texteSourcePhys+="      NAME "+source+"\n"
           self.texteSourcePhys+="      NTURNS "+str(self.dictMCVal[debutKey+"NbdeTours"])+"\n"
           self.texteSourcePhys+="      CURJ POLAR "+str(self.dictMCVal[debutKey+"Amplitude"])
           self.texteSourcePhys+=" 0.0000000000000000E+00\n   ]\n"
         
       self.texteSourcePhys+="]\n"
       for vcut in listeVCut:
           self.texteIngendof+="1\n"
           debutKey=vcut+"______VCUT__"
           if self.dictMCVal[debutKey+"Orientation"] == "Oppose" :self.texteIngendof+="0\n"
           else : self.texteIngendof+="1\n"
       if self.dictMCVal["__PARAMETRES__TypedeFormule"]=="APHI" :self.texteIngendof+="1\n"
       else : self.texteIngendof+="2\n"
       
        
#----------------------------------------------------------------------------------------
   def traiteMateriaux(self) :
#----------------------------------------------------------------------------------------
       listeCond=[]
       listeNoCond=[]
       for k in self.dictMCVal.keys():
           if k.find ("______CONDUCTEUR") > -1 :
              noms=k.split("_____")
              if noms[0] not in listeCond : listeCond.append(noms[0])
           if k.find ("______NOCOND") > -1 :
              noms=k.split("_____")
              if noms[0] not in listeNoCond : listeNoCond.append(noms[0])
   
       for c in listeCond:
           self.textePhys +="      NAME "+c+"\n"
           self.textePhys +=texteConductor
           self.textePhys+="         VALUE COMPLEX "
           self.textePhys+=str(self.dictMCVal[c+"______CONDUCTEUR__Conductivite"])
           self.textePhys+=texteConducto2 
           self.textePhys+="         VALUE COMPLEX "
           self.textePhys+=str(self.dictMCVal[c+"______CONDUCTEUR__Permeabilite"])
           self.textePhys+="  0.0000000000000000E+00\n      ]\n   ]\n"

       for c in listeNoCond:
           self.textePhys+="   [DIELECTRIC\n"
           self.textePhys +="      NAME "+c+"\n"
           self.textePhys += texteNoCond
           self.textePhys+="         VALUE COMPLEX "
           self.textePhys+=str(self.dictMCVal[c+"______NOCOND__Permeabilite"])
           self.textePhys+="  0.0000000000000000E+00\n      ]\n   ]\n"

       self.textePhys+="]\n"
       self.textePhys+=self.texteSourcePhys

#----------------------------------------------------------------------------------------
#  Creation du fichier Param
#----------------------------------------------------------------------------------------
   def traiteParam(self):
       self.texteParam +="[FREQUENCY\n   SINGLE  "+str(self.dictMCVal["__PARAMETRES__Frequence_en_Hz"])+"\n]\n"
       self.texteParam +="[SOLVER\n   NAME BICGCR\n"
       self.texteParam +="   [ITERATIVE_PARAM\n"
       self.texteParam +="      NITERMAX  "+str(self.dictMCVal["__PARAMETRES__Nb_Max_Iterations"])+"\n"
       self.texteParam +="       EPSILON  "+ str(self.dictMCVal["__PARAMETRES__Erreur_Max"])+"\n   ]\n]"


#----------------------------------------------------------------------------------------
#  analyse de chaque noeud de l'arbre 
#----------------------------------------------------------------------------------------

   def generMCSIMP(self,obj) :
        """recuperation de l objet MCSIMP"""
        s=PythonGenerator.generMCSIMP(self,obj)
        if hasattr(obj.etape,'sdnom'): clef=obj.etape.sdnom+"____"
        else: clef=""
        for i in obj.get_genealogie() :
            clef=clef+"__"+i
        self.dictMCVal[clef]=obj.valeur

        return s

  
