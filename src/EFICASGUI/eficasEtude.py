#=============================================================================
# File      : EficasEtude.py
# Created   : mar fév 25 09:48:34 CET 2003
# Author    : Pascale NOYRET, EDF
# Project   : SALOME
# Copyright : EDF 2003
#  $Header: /home/salome/PlateFormePAL/Bases_CVS_EDF/Modules_EDF/ASTER_SRC/src/ASTERGUI/eficasEtude.py,v 1.1.1.1.2.1 2004/05/18 11:40:21 salome Exp $
#=============================================================================

import salome
import re
from tkFileDialog import asksaveasfilename

import salomedsgui
aGuiDS=salomedsgui.guiDS()

#--------------------------------------------------------------------------

class Eficas_In_Study:

      def __init__(self):
          import SMESH_utils
          self.enregistre()
          self.liste_deja_la=[]
          
      def  enregistre(self):
           self.fatherId=aGuiDS.enregistre("Eficas")
           salome.sg.updateObjBrowser(0)

      def  rangeInStudy(self,fichier):
	   if fichier not in self.liste_deja_la :
	        self.liste_deja_la.append(fichier)
                Nom=re.split("/",fichier)[-1]

                self.commId=aGuiDS.createItemInStudy(self.fatherId,Nom)
                aGuiDS.setExternalFileAttribute(self.commId,"FICHIER_EFICAS",fichier)
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
           
