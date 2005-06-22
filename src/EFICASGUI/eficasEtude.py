#=============================================================================
# File      : EficasEtude.py
# Created   : mar fév 25 09:48:34 CET 2003
# Author    : Pascale NOYRET, EDF
# Project   : SALOME
# Copyright : EDF 2003
#  $Header: /home/salome/PlateFormePAL/Bases_CVS_EDF/Modules_EDF/EFICAS_SRC/src/EFICASGUI/eficasEtude.py,v 1.3 2005/06/03 07:25:24 salome Exp $
#=============================================================================

import salome
import re
from tkFileDialog import asksaveasfilename

import salomedsgui
aGuiDS=salomedsgui.guiDS()

#--------------------------------------------------------------------------

class Eficas_In_Study:

      def __init__(self,code,studyId=None):
          print "#######################################################"
          print "#######################################################"
          print "#######################################################"
          print "_CS_GBO_ : Eficas_In_Study:init: studyId = ", studyId
          print "#######################################################"
          print "#######################################################"        
          import SMESH_utils
          self.aGuiDS=salomedsgui.guiDS(studyId=studyId)
          self.enregistre()
	  self.code=code
          self.liste_deja_la=[]
          
      def  enregistre(self):
           self.fatherId=self.aGuiDS.enregistre("Eficas")
           salome.sg.updateObjBrowser(0)

      def rangeInStudy(self,fichier, suf=""):
	   if fichier not in self.liste_deja_la :
	        self.liste_deja_la.append(fichier)
                Nom=re.split("/",fichier)[-1]

                self.commId=self.aGuiDS.createItemInStudy(self.fatherId,Nom)
		if self.commId != None:
                   self.aGuiDS.setExternalFileAttribute(self.commId,"FICHIER_EFICAS_"+self.code+suf,fichier)
                   salome.sg.updateObjBrowser(0)

      def creeConfigTxt(self,fichier,dico):
           sauvegarde = asksaveasfilename(title="fichier config.txt",
                                     defaultextension='.txt',
                                     initialdir = fichier)
           f=open(sauvegarde,'w+')
           for unite in dico.keys():
                print unite
                type=dico[unite][0]
                fic=dico[unite][1:]
                ligne="fort."+str(unite)+" "+type+" "+fic
                f.write(ligne)
           f.close()
           self.rangeInStudy(sauvegarde)
           
