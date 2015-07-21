# -*- coding: iso-8859-1 -*-
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

import re
#from ExtractGeneratorandLoadList import ExtractGeneratorandLoadList
from ExtractGeneratorandLoadList import ExtractGeneratorandLoadList2

def INCLUDE(self,chemin_psse,fichier_sav,**args):
   """ 
       Fonction sd_prod pour la macro INCLUDE
   """
   
   print "INCLUDE", self
   reevalue=0
   if hasattr(self,'fichier_ini'):
       reevalue=1
       if self.fichier_ini == fichier_sav : return
       if hasattr(self,'old_context_fichier_init' ):
         for concept in self.old_context_fichier_init.values():
             self.jdc.delete_concept(concept)
         self.jdc_aux=None
         self.contexte_fichier_init={}
         self.reevalue_sd_jdc()
         self.jdc.reset_context()

   self.fichier_ini=fichier_sav
   self.contexte_fichier_init = {}
   self.fichier_unite = 999
   self.fichier_err = None
   self.fichier_text=""
    
   unite = 999

   pattern_debut_ligne = re.compile(r'^[0-9].*')
   try:
     MachineListOrigin,LoadListOrigin= ExtractGeneratorandLoadList2(fichier_sav,chemin_psse)
   except :
     if self.jdc.appli is not None:
        self.jdc.appli.affiche_alerte("Error", 'An error happened in ExtractGeneratorandLoadList execution ')
        self.g_context = {}
        self.etapes = []
        self.jdc_aux = None
        self.fichier_err = str(exc)
        self.contexte_fichier_init = {}

   MachineList=[]
   LoadList=[]
   BusBarList=[]
   for m in MachineListOrigin:
       if m in LoadListOrigin : BusBarList.append(m)
       else : MachineList.append(m)

   for m in LoadListOrigin:
       if m not in MachineListOrigin : LoadList.append(m)

   for m in MachineList:
         nouv=m[0].replace(' ','_')
         nouveau=nouv.replace('.','_')
         nom = nouveau+"__"+str(m[1])
         if pattern_debut_ligne.match(nom): nom='_'+nom
         id  = str(m[3])
         self.fichier_text += "%s=MONGENER(ID='%s',);\n" % (nom, id)

   for m in BusBarList:
         nouv=m[0].replace(' ','_')
         nouveau=nouv.replace('.','_')
         nom = nouveau+"__"+str(m[1])
         if pattern_debut_ligne.match(nom): nom='_'+nom
         id  = str(m[3])
         self.fichier_text += "%s=MONBUSBAR(ID='%s',);\n" % (nom, id)

   for m in LoadList:
         nouv=m[0].replace(' ','_')
         nouveau=nouv.replace('.','_')
         nom = nouveau+"__"+str(m[1])
         if pattern_debut_ligne.match(nom): nom='_'+nom
         if pattern_debut_ligne.match(nom): print 'match'
         id  = str(m[3])
         self.fichier_text += "%s=MACHARGE(ID='%s',);\n" % (nom, id)

   import Extensions.jdc_include
   self.JdC_aux = Extensions.jdc_include.JDC_CATA_INCLUDE(code='PSEN', execmodul=None)
   self.make_contexte_include(None, self.fichier_text)
   self.old_context_fichier_init = self.contexte_fichier_init
   self.parent.record_unit(unite, self)


def INCLUDE_context(self,d):
   """ 
       Fonction op_init pour macro INCLUDE
   """
   for k,v in self.g_context.items():
      d[k]=v

