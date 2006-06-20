# -*- coding: utf-8 -*-

import log

from load import getJDC
from mocles import parseKeywords
import removemocle
import renamemocle
import movemocle

#atraiter=("DEBUT","LIRE_MAILLAGE","AFFE_MODELE","DEFI_GROUP",
#          "AFFE_MATERIAU","DEFI_MATERIAU","STAT_NONLINE",
#        )

atraiter=("CALC_FONCTION","IMPR_GENE","STAT_NON_LINE","DEFI_MATERIAU")
filename="toto.comm"
jdc=getJDC(filename,atraiter)
root=jdc.root

#Parse les mocles des commandes
parseKeywords(root)

#removemocle.removemocleinfact(jdc,"AFFE_MATERIAU","AFFE","TOUT")
#removemocle.removemocle(jdc,"STAT_NONLINE","SOLVEUR")
#renamemocle.renamemocleinfact(jdc,"AFFE_MODELE","AFFE","PHENOMENE","TOTO")
#renamemocle.renamemocleinfact(jdc,"AFFE_MODELE","AFFE","MODELISATION","TITI")
#renamemocle.renamemocleinfact(jdc,"DEFI_GROUP","CREA_GROUP_NO","GROUP_MA","TUTU")
#removemocle.removemocle(jdc,"LIRE_MAILLAGE","INFO")
#removemocle.removemocle(jdc,"LIRE_MAILLAGE","UNITE")
#renamemocle.renamemocle(jdc,"DEFI_MATERIAU","ELAS","ELASTIC")
#renamemocle.renamemocle(jdc,"AFFE_MATERIAU","MAILLAGE","MAILL")
#removemocle.removemocleinfact(jdc,"STAT_NONLINE","SOLV","METHOD")
#removemocle.removemocle(jdc,"STAT_NONLINE","AFFE")
#renamemocle.renamecommande(jdc,"AFFE_CHAR_MECA","AFFE_CHAR_MECA_PN")
#renamemocle.renamecommande(jdc,"DEBUT","DEBUT_PN")

#          les arguments sont jdc,ancien-nom-de-commande,nouveau-nom-de-commande
renamemocle.renamecommande(jdc,"CALC_FONCTION","INFO_FONCTION")

#          Les arguments sont  - jdc,
#			       - nom de la procedure (pas teste avec autre chose)
#			       - nom du mot clef facteur contenant, 
#			       - nom du mot cle simple
#          Attention ne fonctionne pas pour l instant avec +sieurs occurences du mot cle à déplacer
movemocle.movemoclefromfacttofather(jdc,"IMPR_GENE","GENE","UNITE")
movemocle.movemoclefromfacttofather(jdc,"IMPR_GENE","GENE","FORMAT")

#          Les arguments sont  - jdc
#			       - nom de l operateur (pas teste avec autre chose)
#			       - nom du mot clef facteur source, 
#			       - nom du mot cle simple
#			       - liste de  mots clef facteur arrivée possible
#          Attention ne fonctionne pas pour l instant avec +sieurs occurences du mot cle à déplacer
movemocle.movemoclefromfacttofactmulti(jdc,"STAT_NON_LINE","CONVERGENCE","RESI_INTE_RELA",("COMP_INCR","COMP_ELAS"))


renamemocle.renamemocle(jdc,"DEFI_MATERIAU","LEMAITRE","LEMAITRE_IRRA")
movemocle.movemoclefromfacttofactmulti(jdc,"DEFI_MATERIAU","FLU_IRRA","QSR_K",("LEMAITRE_IRRA",))
movemocle.movemoclefromfacttofactmulti(jdc,"DEFI_MATERIAU","FLU_IRRA","BETA",("LEMAITRE_IRRA",))
movemocle.movemoclefromfacttofactmulti(jdc,"DEFI_MATERIAU","FLU_IRRA","PHI_ZERO",("LEMAITRE_IRRA",))
movemocle.movemoclefromfacttofactmulti(jdc,"DEFI_MATERIAU","FLU_IRRA","L",("LEMAITRE_IRRA",))
removemocle.removemocle(jdc,"DEFI_MATERIAU","FLU_IRRA")

renamemocle.renamemocleinfact(jdc,"DEFI_MATERIAU","GRAN_IRRA","A","GRAN_A")
renamemocle.renamemocleinfact(jdc,"DEFI_MATERIAU","GRAN_IRRA","B","GRAN_B")
renamemocle.renamemocleinfact(jdc,"DEFI_MATERIAU","GRAN_IRRA","S","GRAN_S")
movemocle.movemoclefromfacttofactmulti(jdc,"DEFI_MATERIAU","GRAN_IRRA","GRAN_A",("LEMAITRE_IRRA",))
movemocle.movemoclefromfacttofactmulti(jdc,"DEFI_MATERIAU","GRAN_IRRA","GRAN_B",("LEMAITRE_IRRA",))
movemocle.movemoclefromfacttofactmulti(jdc,"DEFI_MATERIAU","GRAN_IRRA","GRAN_S",("LEMAITRE_IRRA",))
removemocle.removemocle(jdc,"DEFI_MATERIAU","GRAN_IRRA")


f=open("tutu.comm",'w')
f.write(jdc.getSource())
f.close()
