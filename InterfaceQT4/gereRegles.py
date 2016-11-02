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

from determine import monEnvQT5
if monEnvQT5 :
  from PyQt5.QtCore import Qt
else:
  from PyQt4.QtCore import *
from  monViewRegles  import ViewRegles

class GereRegles :

   def AppelleBuildLBRegles(self):
       from browser import JDCTree
       if isinstance(self,JDCTree):
          self.AppelleBuildLBReglesForJdC()
       else :
          self.AppelleBuildLBReglesForCommand()
       self.BuildLBRegles(self.listeRegles,self.listeNomsEtapes)
       self.AfficheRegles()
       
   def AppelleBuildLBReglesForCommand(self):
       self.listeRegles     = self.item.get_regles()
       self.listeNomsEtapes = self.item.get_mc_presents()

   def AppelleBuildLBReglesForJdC(self):
       self.listeRegles=self.item.get_regles()
       self.listeNomsEtapes = self.item.get_l_noms_etapes()


   def BuildLBRegles(self,listeRegles,listeNomsEtapes):
       self.liste=[]
       if len(listeRegles) > 0:
          for regle in listeRegles :
             texteRegle=regle.gettext()
             texteMauvais,test = regle.verif(listeNomsEtapes)
             for ligne in texteRegle.split("\n") :
                if ligne == "" : continue
                if ligne[0]=="\t" :  ligne="     "+ligne[1:]
                if test :
                   self.liste.append((ligne,Qt.black))
                else :
                   self.liste.append((ligne,Qt.red))
             self.liste.append(("",Qt.red))
       if self.liste==[] : self.liste(tr("pas de regle de construction pour ce jeu de commandes",Qt.black))
               

   def AfficheRegles(self):
      titre="Regles pour "+self.item.nom
      w = ViewRegles( self.editor,self.liste,titre  )
      w.exec_()
       

