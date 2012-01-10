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


def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 's_DIC',
        # La factory pour creer une instance du plugin
          'factory' : s_DICGenerator,
          }


class s_DICGenerator(MapGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et
      un texte au format py

   """
   
   def LIST_IMAGES(self):
       print "je ne sais pas ce qu il faut faire"
       commande="print 'je ne sais pas ce qu il faut faire avec le fichier :"
       commande += str(self.FILE) +" '\n"
       return commande
       
   def RBM(self):
       print self.dico
       if not self.dico.has_key('CSJ')   : self.dico['CSJ']=self.dico['CS']
       if not self.dico.has_key('GSJ')   : self.dico['GSJ']=self.dico['GS']
       if not self.dico.has_key('VMAXJ')   : self.dico['VMAXJ']=self.dico['VMAX']
       commande="execRBM=component_RBM("+str(self.dico['CS'])+","+str(self.dico['CSJ'])+","
       commande+=str(self.dico['GS'])+","+str(self.dico['GSJ'])+","
       commande+=str(self.dico['VMAX'])+","+str(self.dico['VMAXJ'])+",'"+str(self.study_path)+"')\n"
       return commande

   def DISPL(self):
       print self.dico
       if not self.dico.has_key('CSJ')   : self.dico['CSJ']=self.dico['CS']
       if not self.dico.has_key('GSJ')   : self.dico['GSJ']=self.dico['GS']
       if not self.dico.has_key('VMAXJ')   : self.dico['VMAXJ']=self.dico['VMAX']
       commande="execDISPL=component_DISPL("+str(self.dico['CS'])+","+str(self.dico['CSJ'])+","
       commande+=str(self.dico['GS'])+","+str(self.dico['GSJ'])+","
       commande+=str(self.dico['VMAX'])+","+str(self.dico['VMAXJ'])+",'"+str(self.study_path)+"')\n"
       return commande
