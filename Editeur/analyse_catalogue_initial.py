# -*- coding: utf-8 -*-
#                                                CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002        EDF R&D                                                                        WWW.CODE-ASTER.ORG
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
#                1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
from string import split,strip,lowercase,uppercase
import re,string,os


#
__Id__="$Id: analyse_catalogue_initial.py,v 1.2 2010-09-17 13:11:49 pnoyret Exp $"
__version__="$Name: V2_1_1_beta $"
#

                
class Catalogue_initial:
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
                        print "Impossible d'ouvrir le fichier :",self.fichier

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











                                
                                
