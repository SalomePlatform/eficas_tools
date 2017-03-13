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
from __future__ import absolute_import
from __future__ import print_function
try :
  from builtins import str
  from builtins import object
except :
  pass
import re,os

from Extensions.i18n import tr
#
__Id__="$Id: analyse_catalogue_initial.py,v 1.2.4.1.2.2.2.4 2013-04-09 14:04:44 pnoyret Exp $"
__version__="$Name: V7_main $"
#

                
class Catalogue_initial(object):
        def __init__(self,fichier):
                self.liste_commandes=[]
                self.lignes=[]
                self.fichier=fichier
                self.ouvrir_fichier()
                self.constr_list_txt_cmd()

        def ouvrir_fichier(self):
                try :
                        f=open(self.fichier,'r')
                        self.lignes=f.readlines()
                        f.close()
                except :
                        print(tr("Impossible d'ouvrir le fichier : %s", str(self.fichier)))

        def constr_list_txt_cmd(self):
                pattern = '^# Ordre Catalogue '
                for i in self.lignes :
                    if (re.search(pattern,i)):
                        i=i.replace('# Ordre Catalogue ','')
                        i=i.replace('\n','')
                        self.liste_commandes.append(i)


def analyse_catalogue(nom_cata):
        cata = Catalogue_initial(nom_cata)
        return cata.liste_commandes


if __name__ == "__main__" :
        monCata="/local/noyret/Install_Eficas/EficasQT4/Openturns_StudyOpenTURNS_Cata_Study_V4.py"
        analyse_catalogue(monCata)











                                
                                
