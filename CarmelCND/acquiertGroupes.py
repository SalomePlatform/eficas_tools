#! /usr/bin/env python
# -*- coding:utf-8 -*-
# /*  This file is part of MED.
#  *
#  *  COPYRIGHT (C) 1999 - 2013  EDF R&D, CEA/DEN
#  *  MED is free software: you can redistribute it and/or modify
#  *  it under the terms of the GNU Lesser General Public License as published by
#  *  the Free Software Foundation, either version 3 of the License, or
#  *  (at your option) any later version.
#  *
#  *  MED is distributed in the hope that it will be useful,
#  *  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  *  GNU Lesser General Public License for more details.
#  *
#  *  You should have received a copy of the GNU Lesser General Public License
#  *  along with MED.  If not, see <http://www.gnu.org/licenses/>.
#  */


import sys
sys.path.append('/home/A96028/Salome/V7_main/tools/install/Medfichier-307-hdf51810/lib/python2.7/site-packages')

from med.medfile import *
from med.medmesh import *
from med.medfamily import *


def getGroupes(filename,debug=0) :
    listeGroupes=[]
    maa=""
    
    try :
        fid = MEDfileOpen(filename,MED_ACC_RDONLY)
    except :
        return ("Pb a la lecture du fichier", listeGroupes,maa)

   
    # /* Lecture des infos concernant le premier maillage */
    maa, sdim, mdim, type, desc, dtunit, sort, nstep, rep, nomcoo,unicoo = MEDmeshInfo(fid, 1)
    if debug :
   	print "Maillage de nom : |%s| de dimension : %ld , et de type %s\n"%(maa,mdim,type)
   	print "Maillage de nom : |%s| , de dimension : %ld , et de type %s\n"%(maa,mdim,type)
   	print "\t -Dimension de l'espace : %ld\n"%(sdim)
   	print "\t -Description du maillage : %s\n"%(desc)
   	print "\t -Noms des axes : |%s|\n"%(nomcoo)
   	print "\t -Unités des axes : |%s|\n"%(unicoo)
   	print "\t -Type de repère : %s\n"%(rep)
   	print "\t -Nombre d'étape de calcul : %ld\n"%(nstep)
   	print "\t -Unité des dates : |%s|\n"%(dtunit)
   
    # /* Lecture du nombre de familles */
    nfam = MEDnFamily(fid,maa)
    if debug :
   	print "Nombre de familles : %d \n"%(nfam)
   
    # /* Lecture de chaque famille */
    for i in xrange(0,nfam):
   
        # /* Lecture du nombre de groupe */
        ngro = MEDnFamilyGroup(fid,maa,i+1)
        if debug :
     	    print "Famille %d a %d groupes \n"%(i+1,ngro)
   
        gro  = MEDCHAR(MED_LNAME_SIZE*ngro+1)
         
        nomfam,numfam,gro = MEDfamilyInfo(fid,maa,i+1,gro)
        if debug :
            print "Famille de nom %s et de numero %d : \n"%(nomfam,numfam)
            print "Attributs : \n"
    
        for j in xrange(0,ngro):
        # print "gro = %s\n"%(gro[j*MED_LNAME_SIZE:j*MED_LNAME_SIZE+MED_LNAME_SIZE])
            groupSplit=gro[j*MED_LNAME_SIZE:j*MED_LNAME_SIZE+MED_LNAME_SIZE]
            groupeName="".join(groupSplit).split("\x00")[0]
            print groupeName,  numfam
            if groupeName not in listeGroupes : listeGroupes.append(groupeName) 

   
   
    print listeGroupes
    MEDfileClose(fid)
    return ("",listeGroupes,maa)

if __name__ == "__main__":
    filename="/home/A96028/Carmel/Pascale/Domaine_Bidouille.med"
    print getGroupes(filename)
