#!/usr/bin/env python
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
"""
"""
usage="""usage: %prog [options]
Typical use is:
  python traduitV9V10.py --infile=xxxx --outfile=yyyy
"""

import log
import optparse
import sys

from load   import getJDC
from mocles import parseKeywords
from removemocle  import *
from renamemocle  import *
from renamemocle  import *
from inseremocle  import *
from changeValeur import *
from movemocle    import *
from dictErreurs  import * 
from regles import pasDeRegle

atraiter=("AFFE_CARA_ELEM","AFFE_CHAR_CINE","AFFE_CHAR_MECA","AFFE_CHAR_MECA_F","AFFE_MATERIAU","AFFE_MODELE",
          "CALC_CHAM_ELEM","CALC_ELEM","CALC_G","CALC_META","CALC_MODAL","CALC_PRECONT","CALCUL","CALC_MISS","CALC_NO",
          "COMB_FOURIER","COMB_SISM_MODAL","CREA_CHAMP","CREA_RESU",
          "DEFI_BASE_MODALE","DEFI_COMPOR","DEFI_CONTACT","DEFI_GLRC","DEFI_LIST_INST","DEFI_MATERIAU",
          "DYNA_ISS_VARI","DYNA_LINE_HARM","DYNA_LINE_TRAN","DYNA_NON_LINE","DYNA_TRAN_MODAL",
          "EXTR_RESU","IMPR_MACR_ELEM","IMPR_MATRICE","IMPR_RESU","LIRE_RESU",
          "MACR_ADAP_MAIL","MACR_ASCOUF_CALC","MACR_ASPIC_CALC","MACR_ECREVISSE",
          "MACR_INFO_MAIL","MACR_LIGN_COUPE","MACRO_ELAS_MULT","MACRO_MATR_AJOU","MACRO_MISS_3D",
          "MECA_STATIQUE","MODE_ITER_INV","MODE_ITER_SIMULT","MODE_STATIQUE","MODI_REPERE",
          "POST_CHAM_XFEM","POST_ELEM","POST_GP","POST_K1_K2_K3","POST_RCCM","POST_RELEVE_T","POST_ZAC",
          "PROJ_CHAMP","PROJ_MESU_MODAL","RECU_FONCTION","REST_SOUS_STRUC","REST_GENE_PHYS","REST_SPEC_PHYS",
          "STAT_NON_LINE","SIMU_POINT_MAT","TEST_RESU","THER_LINEAIRE","THER_NON_LINE","THER_NON_LINE_MO",)

dict_erreurs={
# STA10
#
             "AFFE_CHAR_MECA_CONTACT":"Attention, modification de la définition du CONTACT : nommer DEFI_CONTACT,verifier les paramètres globaux et le mettre dans le calcul",
             "AFFE_CHAR_MECA_LIAISON_UNILATER":"Attention, modification de la définition du CONTACT : nommer DEFI_CONTACT,verifier les paramètres globaux et le mettre dans le calcul",
             "AFFE_CHAR_MECA_F_LIAISON_UNILATER":"Attention, modification de la définition du CONTACT : nommer DEFI_CONTACT,verifier les paramètres globaux et le mettre dans le calcul",
             "AFFE_CHAR_MECA_GRAPPE_FLUIDE":"Resorption de GRAPPE_FLUIDE en version 10",
             "DEFI_MATERIAU_LMARC":"Resorption loi LMARC en version 10",
             "DEFI_MATERIAU_LMARC_FO":"Resorption loi LMARC en version 10",
             "POST_ZAC":"Resorption POST_ZAC en version 10",
             "AFFE_CHAR_MECA_ARLEQUIN":"Resorption ARLEQUIN en version 10",
             
             "PROJ_CHAMP_CHAM_NO":"Attention, verifier pour PROJ_CHAMP la présence de MODELE1/MAILLAGE1 et MODELE2/MAILLAGE2",

             "COMB_SISM_MODAL_COMB_MULT_APPUI":"Attention, verifier GROUP_APPUI pour COMB_SISM_MODAL car on est dans le cas MULTI_APPUI=DECORRELE",

             "CALC_PRECONT_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "CALC_PRECONT_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "DYNA_LINE_HARM_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "DYNA_LINE_HARM_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "DYNA_LINE_TRAN_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "DYNA_LINE_TRAN_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "DYNA_TRAN_MODAL_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "DYNA_TRAN_MODAL_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MACR_ASCOUF_CALC_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MACR_ASCOUF_CALC_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MACR_ASPIQ_CALC_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MACR_ASPIQ_CALC_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MACRO_MATR_AJOU_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MACRO_MATR_AJOU_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MECA_STATIQUE_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MECA_STATIQUE_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MODE_STATIQUE_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "MODE_STATIQUE_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "STAT_NON_LINE_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "STAT_NON_LINE_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "THER_LINEAIRE_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "THER_LINEAIRE_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "THER_NON_LINE_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "THER_NON_LINE_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "DYNA_NON_LINE_SOLVEUR_PARALLELISME":"Modification du PARALLELISME qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",
             "DYNA_NON_LINE_SOLVEUR_PARTITION":"Modification de PARTITION qui se definit au niveau de AFFE_MODELE ou MODI_MODELE",

             "STAT_NON_LINE_INCREMENT":"Attention, modification de la subdivision des pas : nommer DEFI_LIST_INST et verifier son appel dans STAT_NON_LINE",
             "CALC_PRECONT_INCREMENT":"Attention, modification de la subdivision des pas : nommer DEFI_LIST_INST et verifier son appel dans CALC_PRECONT",
             "DYNA_NON_LINE_INCREMENT":"Attention, modification de la subdivision des pas : nommer DEFI_LIST_INST et verifier son appel dans DYNA_NON_LINE",
             "MACR_ASCOUF_CALC_INCREMENT":"Attention, modification de la subdivision des pas : nommer DEFI_LIST_INST et verifier son appel dans MACR_ASCOUF_CALC",
             "MACR_ASPIQ_CALC_INCREMENT":"Attention, modification de la subdivision des pas : nommer DEFI_LIST_INST et verifier son appel dans MACR_ASPIQ_CALC",
             "SIMU_POINT_MAT_INCREMENT":"Attention, modification de la subdivision des pas : nommer DEFI_LIST_INST et verifier son appel dans SIMU_POINT_MAT",

             "CALC_ELEM_SENSIBILITE":"Le post-traitement SENSIBILITE est à supprimer de CALC_ELEM et à faire via CALC_SENSI",

             "CALC_MISS_OPTION":"Attention, transfert MACRO_MISS_3D en CALC_MISS : utiliser un DEFI_SOL_MISS pour obtenir TABLE_SOL",
              }

sys.dict_erreurs=dict_erreurs

def traduc(infile,outfile,flog=None):

    hdlr=log.initialise(flog)
    jdc=getJDC(infile,atraiter)
    root=jdc.root

    #Parse les mocles des commandes
    parseKeywords(root)

    ####################### initialisation et traitement des erreurs #########################


    #####RESORPTION

    GenereErreurPourCommande(jdc,("POST_ZAC",))
    GenereErreurMCF(jdc,"AFFE_CHAR_MECA","GRAPPE_FLUIDE")
    GenereErreurMCF(jdc,"DEFI_MATERIAU","LMARC")
    GenereErreurMCF(jdc,"DEFI_MATERIAU","LMARC_FO")
    GenereErreurMCF(jdc,"AFFE_CHAR_MECA","ARLEQUIN")


    #####SOLVEUR
    
    ####################### traitement MUMPS/PARALELLISME-PARTITION ##################
    #commandes concernes en plus : CALC_FORC_AJOU?,CALC_MATR_AJOU?
     # */SOLVEUR/CHARGE_PROCO_MA(SD)--> AFFE_MODELE (ou MODI_MODELE)/PARTITION/.
    # */SOLVEUR/PARALLELISME =CENTRALISE--> AFFE_MODELE (ou MODI_MODELE)/PARTITION/PARALLELISME = CENTRALISE
    # */SOLVEUR/PARALLELISME = "DISTRIBUE_MC/MD/SD"--> AFFE_MODELE/PARTITION/PARALLELISME = "MAIL_CONTIGU/MAIL_DISPERSE/SOUS_DOMAINE"
    # */SOLVEUR/PARTITION --> AFFE_MODELE (ou MODI_MODELE)/PARTITION/PARTITION


    GenereErreurMotCleInFact(jdc,"CALC_PRECONT","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"CALC_PRECONT","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"DYNA_LINE_HARM","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"DYNA_LINE_HARM","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"DYNA_LINE_TRAN","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"DYNA_LINE_TRAN","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"DYNA_TRAN_MODAL","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"DYNA_TRAN_MODAL","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"MACR_ASCOUF_CALC","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"MACR_ASCOUF_CALC","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"MACR_ASPIQ_CALC","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"MACR_ASPIQ_CALC","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"MACRO_MATR_AJOU","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"MACRO_MATR_AJOU","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"MECA_STATIQUE","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"MECA_STATIQUE","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"MODE_STATIQUE","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"MODE_STATIQUE","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"STAT_NON_LINE","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"STAT_NON_LINE","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"THER_LINEAIRE","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"THER_LINEAIRE","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"THER_NON_LINE","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"THER_NON_LINE","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"THER_NON_LINE_MO","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"THER_NON_LINE_MO","SOLVEUR","PARTITION")
    GenereErreurMotCleInFact(jdc,"DYNA_NON_LINE","SOLVEUR","PARALLELISME")
    GenereErreurMotCleInFact(jdc,"DYNA_NON_LINE","SOLVEUR","PARTITION")

    ####################### traitement mot cle INCREMENT redecoupage en temps #######################
    renameMotCleSiRegle(jdc,"STAT_NON_LINE","INCREMENT","INCREMENT_NEW",((("INCREMENT","SUBD_METHODE"),"existeMCsousMCF"),),1)
    moveMCFToCommand(jdc,"STAT_NON_LINE","INCREMENT_NEW","DEFI_LIST_INST","ECHEC")
    removeMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT_NEW","SUBD_COEF_PAS_1",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT_NEW","SUBD_ITER_FIN",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT_NEW","SUBD_ITER_IGNO",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT_NEW","SUBD_ITER_PLUS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT_NEW","SUBD_METHODE",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT_NEW","SUBD_NIVEAU",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT_NEW","SUBD_OPTION",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT_NEW","SUBD_PAS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT_NEW","SUBD_PAS_MINI",pasDeRegle(),0)
    renameMotCle(jdc,"STAT_NON_LINE","INCREMENT_NEW","INCREMENT")

    renameMotCleSiRegle(jdc,"CALC_PRECONT","INCREMENT","INCREMENT_NEW",((("INCREMENT","SUBD_METHODE"),"existeMCsousMCF"),),1)
    moveMCFToCommand(jdc,"CALC_PRECONT","INCREMENT_NEW","DEFI_LIST_INST","ECHEC")
    removeMotCleInFact(jdc,"CALC_PRECONT","INCREMENT_NEW","SUBD_COEF_PAS_1",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_PRECONT","INCREMENT_NEW","SUBD_ITER_FIN",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_PRECONT","INCREMENT_NEW","SUBD_ITER_IGNO",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_PRECONT","INCREMENT_NEW","SUBD_ITER_PLUS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_PRECONT","INCREMENT_NEW","SUBD_METHODE",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_PRECONT","INCREMENT_NEW","SUBD_NIVEAU",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_PRECONT","INCREMENT_NEW","SUBD_OPTION",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_PRECONT","INCREMENT_NEW","SUBD_PAS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_PRECONT","INCREMENT_NEW","SUBD_PAS_MINI",pasDeRegle(),0)
    renameMotCle(jdc,"CALC_PRECONT","INCREMENT_NEW","INCREMENT")

    
    renameMotCleSiRegle(jdc,"DYNA_NON_LINE","INCREMENT","INCREMENT_NEW",((("INCREMENT","SUBD_METHODE"),"existeMCsousMCF"),),1)
    moveMCFToCommand(jdc,"DYNA_NON_LINE","INCREMENT_NEW","DEFI_LIST_INST","ECHEC")
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT_NEW","SUBD_COEF_PAS_1",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT_NEW","SUBD_ITER_FIN",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT_NEW","SUBD_ITER_IGNO",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT_NEW","SUBD_ITER_PLUS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT_NEW","SUBD_METHODE",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT_NEW","SUBD_NIVEAU",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT_NEW","SUBD_OPTION",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT_NEW","SUBD_PAS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT_NEW","SUBD_PAS_MINI",pasDeRegle(),0)
    renameMotCle(jdc,"DYNA_NON_LINE","INCREMENT_NEW","INCREMENT")
    
    renameMotCleSiRegle(jdc,"MACR_ASCOUF_CALC","INCREMENT","INCREMENT_NEW",((("INCREMENT","SUBD_METHODE"),"existeMCsousMCF"),),1)
    moveMCFToCommand(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","DEFI_LIST_INST","ECHEC")
    removeMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","SUBD_COEF_PAS_1",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","SUBD_ITER_FIN",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","SUBD_ITER_IGNO",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","SUBD_ITER_PLUS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","SUBD_METHODE",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","SUBD_NIVEAU",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","SUBD_OPTION",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","SUBD_PAS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","SUBD_PAS_MINI",pasDeRegle(),0)
    renameMotCle(jdc,"MACR_ASCOUF_CALC","INCREMENT_NEW","INCREMENT")
    
    renameMotCleSiRegle(jdc,"MACR_ASPIQ_CALC","INCREMENT","INCREMENT_NEW",((("INCREMENT","SUBD_METHODE"),"existeMCsousMCF"),),1)
    moveMCFToCommand(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","DEFI_LIST_INST","ECHEC")
    removeMotCleInFact(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","SUBD_COEF_PAS_1",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","SUBD_ITER_FIN",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","SUBD_ITER_IGNO",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","SUBD_ITER_PLUS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","SUBD_METHODE",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","SUBD_NIVEAU",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","SUBD_OPTION",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","SUBD_PAS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","SUBD_PAS_MINI",pasDeRegle(),0)
    renameMotCle(jdc,"MACR_ASPIQ_CALC","INCREMENT_NEW","INCREMENT")
    
    renameMotCleSiRegle(jdc,"SIMU_POINT_MAT","INCREMENT","INCREMENT_NEW",((("INCREMENT","SUBD_METHODE"),"existeMCsousMCF"),),1)
    moveMCFToCommand(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","DEFI_LIST_INST","ECHEC")
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","SUBD_COEF_PAS_1",pasDeRegle(),0)
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","SUBD_ITER_FIN",pasDeRegle(),0)
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","SUBD_ITER_IGNO",pasDeRegle(),0)
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","SUBD_ITER_PLUS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","SUBD_METHODE",pasDeRegle(),0)
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","SUBD_NIVEAU",pasDeRegle(),0)
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","SUBD_OPTION",pasDeRegle(),0)
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","SUBD_PAS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","SUBD_PAS_MINI",pasDeRegle(),0)  
    renameMotCle(jdc,"SIMU_POINT_MAT","INCREMENT_NEW","INCREMENT")

    removeMotCleInFact(jdc,"DEFI_LIST_INST","ECHEC","INST_INIT")
    removeMotCleInFact(jdc,"DEFI_LIST_INST","ECHEC","INST_FIN")
    removeMotCleInFact(jdc,"DEFI_LIST_INST","ECHEC","NUME_INST_FIN")
    removeMotCleInFact(jdc,"DEFI_LIST_INST","ECHEC","NUME_INST_INIT")
    removeMotCleInFact(jdc,"DEFI_LIST_INST","ECHEC","PRECISION")
    chercheOperInsereFacteur(jdc,"DEFI_LIST_INST","DEFI_LIST",pasDeRegle(),1)
    moveMotCleFromFactToFact(jdc,"DEFI_LIST_INST","ECHEC","LIST_INST","DEFI_LIST")
    removeMotCleInFact(jdc,"DEFI_LIST_INST","ECHEC","LIST_INST")

    ###################### traitement de NPREC_SOLVEUR ##########
    removeMotCleInFact(jdc,"MODE_ITER_SIMULT","CALC_FREQ","NPREC_SOLVEUR",pasDeRegle(),0)
    removeMotCleInFact(jdc,"MODE_ITER_INV","CALC_FREQ","NPREC_SOLVEUR",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_MODAL","CALC_FREQ","NPREC_SOLVEUR",pasDeRegle(),0)
    removeMotCle(jdc,"IMPR_STURM","NPREC_SOLVEUR")
    removeMotCleInFact(jdc,"MACRO_MATR_AJOU","CALC_FREQ","NPREC_SOLVEUR",pasDeRegle(),0)
    
    ###################### traitement CALC_MODAL SOLVEUR ############
    removeMotCle(jdc,"CALC_MODAL","SOLVEUR",pasDeRegle())

    ##################### traitement DYNA_TRAN-MODAL ADAPT #################
    ChangementValeur(jdc,"DYNA_TRAN_MODAL","METHODE",{"ADAPT":"ADAPT_ORDRE2"})

    #################### traitement STAT/DYNA_NON_LINE OBSERVATION SUIVI_DDL=NON ###########
    removeMotCleInFactCourantSiRegle(jdc,"STAT_NON_LINE","OBSERVATION","SUIVI_DDL",((("SUIVI_DDL","NON",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"DYNA_NON_LINE","OBSERVATION","SUIVI_DDL",((("SUIVI_DDL","NON",jdc),"MCsousMCFcourantaPourValeur"),))

    ################### traitement STAT/DYNA_NON_LINE ARCH_ETAT_INIT ###########
    removeMotCleInFact(jdc,"STAT_NON_LINE","ARCHIVAGE","ARCH_ETAT_INIT",pasDeRegle(),0)
    removeMotCleInFact(jdc,"SIMU_POINT_MAT","ARCHIVAGE","ARCH_ETAT_INIT",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","ARCHIVAGE","ARCH_ETAT_INIT",pasDeRegle(),0)

    ################### traitement STAT/DYNA_NON_LINE CRIT_FLAMB ###############
    removeMotCleInFactCourantSiRegle(jdc,"STAT_NON_LINE","CRIT_FLAMB","INST_CALCUL",((("INST_CALCUL","TOUT_PAS",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"DYNA_NON_LINE","CRIT_FLAMB","INST_CALCUL",((("INST_CALCUL","TOUT_PAS",jdc),"MCsousMCFcourantaPourValeur"),))

    #####COMPORTEMENT/CARA

    ###################  traitement AFFE_MODELE/SHB8 ##########################
    ChangementValeurDsMCF(jdc,"AFFE_MODELE","AFFE","MODELISATION",{"SHB8":"SHB"})
    
    ###################  traitement COMP_ELAS et COMP_INCR  DEFORMATION = GREEN ##############"
    dGREEN={"GREEN_GR":"GROT_GDEP","GREEN":"GROT_GDEP","REAC_GEOM":"GROT_GDEP","EULER_ALMANSI":"GROT_GDEP","COROTATIONNEL":"GDEF_HYPO_ELAS"}
    ChangementValeurDsMCF(jdc,"SIMU_POINT_MAT","COMP_ELAS","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"STAT_NON_LINE","COMP_ELAS","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"DYNA_NON_LINE","COMP_ELAS","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"CALCUL","COMP_ELAS","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"POST_GP","COMP_ELAS","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"CALC_G","COMP_ELAS","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"SIMU_POINT_MAT","COMP_INCR","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"STAT_NON_LINE","COMP_INCR","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"DYNA_NON_LINE","COMP_INCR","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"CALCUL","COMP_INCR","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"CALC_PRECONT","COMP_INCR","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"CALC_NO","COMP_INCR","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"LIRE_RESU","COMP_INCR","DEFORMATION",dGREEN)
    ChangementValeurDsMCF(jdc,"MACR_ECREVISSE","COMP_INCR","DEFORMATION",dGREEN)

    ###################### traitement COMP_INCR/COMP_ELAS RESO_INTE ##########
    dALGOI={"RUNGE_KUTTA_2":"RUNGE_KUTTA","RUNGE_KUTTA_4":"RUNGE_KUTTA"}
    removeMotCleInFactCourantSiRegle(jdc,"STAT_NON_LINE","COMP_ELAS","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"STAT_NON_LINE","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"DYNA_NON_LINE","COMP_ELAS","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"DYNA_NON_LINE","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"CALCUL","COMP_ELAS","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"CALCUL","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"MACR_ASCOUF_CALC","COMP_ELAS","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"MACR_ASCOUF_CALC","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"MACR_ASPIQ_CALC","COMP_ELAS","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"MACR_ASPIQ_CALC","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"SIMU_POINT_MAT","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"CALC_PRE_CONT","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"CALC_NO","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"LIRE_RESU","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFactCourantSiRegle(jdc,"MACR_ECREVISSE","COMP_INCR","RESO_INTE",((("RESO_INTE","IMPLICITE",jdc),"MCsousMCFcourantaPourValeur"),))

    ChangementValeurDsMCF(jdc,"STAT_NON_LINE","COMP_ELAS","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"STAT_NON_LINE","COMP_INCR","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"DYNA_NON_LINE","COMP_ELAS","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"DYNA_NON_LINE","COMP_INCR","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"CALCUL","COMP_ELAS","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"CALCUL","COMP_INCR","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"MACR_ASCOUF_CALC","COMP_ELAS","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"MACR_ASCOUF_CALC","COMP_INCR","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"MACR_ASPIQF_CALC","COMP_ELAS","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"MACR_ASPIQ_CALC","COMP_INCR","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"SIMU_POINT_MAT","COMP_INCR","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"CALC_PRECONT","COMP_INCR","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"CALC_NO","COMP_INCR","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"LIRE_RESU","COMP_INCR","RESO_INTE",dALGOI)
    ChangementValeurDsMCF(jdc,"MACR_ECREVISSE","COMP_INCR","RESO_INTE",dALGOI)

    renameMotCleInFact(jdc,"STAT_NON_LINE","COMP_ELAS","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"STAT_NON_LINE","COMP_INCR","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"DYNA_NON_LINE","COMP_ELAS","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"DYNA_NON_LINE","COMP_INCR","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"CALCUL","COMP_ELAS","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"CALCUL","COMP_INCR","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"MACR_ASCOUF_CALC","COMP_ELAS","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"MACR_ASCOUF_CALC","COMP_INCR","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"MACR_ASPIQF_CALC","COMP_ELAS","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"MACR_ASPIQ_CALC","COMP_INCR","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"SIMU_POINT_MAT","COMP_INCR","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"CALC_PRECONT","COMP_INCR","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"CALC_NO","COMP_INCR","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"LIRE_RESU","COMP_INCR","RESO_INTE","ALGO_INTE")
    renameMotCleInFact(jdc,"MACR_ECREVISSE","COMP_INCR","RESO_INTE","ALGO_INTE")

    ###################### traitement COMP_ELAS/ITER_INTE_PAS ######
    removeMotCleInFact(jdc,"CALCUL","COMP_ELAS","ITER_INTE_PAS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","COMP_ELAS","ITER_INTE_PAS",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","COMP_ELAS","ITER_INTE_PAS",pasDeRegle(),0)

    ###################### traitement CALC_G/COMP_INCR/RELATION ELAS_VMIS_PUIS ####
    ChangementValeurDsMCF(jdc,"CALC_G","COMP_INCR","RELATION",{"ELAS_VMIS_PUIS":"VMIS_ISOT_PUIS"})

    ########################" traitement DEFI_COMPOR/MULTIFIBRE/DEFORMATION=REAC_GEOM #########
    ChangementValeurDsMCF(jdc,"DEFI_COMPOR","MULTIFIBRE","DEFORMATION",dGREEN)

    ####################### traitement DEFI_COMPOR/MONOCRISTAL/ECOULEMENT #############
    dECOULEMENT={"ECOU_VISC1":"MONO_VISC1","ECOU_VISC2":"MONO_VISC2","ECOU_VISC3":"MONO_VISC3","KOCKS_RAUCH":"MONO_DD_KR"}
    ChangementValeurDsMCF(jdc,"DEFI_COMPOR","MONOCRISTAL","ECOULEMENT",dECOULEMENT)
    dISOT={"ECRO_ISOT1":"MONO_ISOT1","ECRO_ISOT2":"MONO_ISOT2"}
    dCINE={"ECRO_CINE1":"MONO_CINE1","ECRO_CINE2":"MONO_CINE2"}
    ChangementValeurDsMCF(jdc,"DEFI_COMPOR","MONOCRISTAL","ECRO_ISOT",dISOT)
    ChangementValeurDsMCF(jdc,"DEFI_COMPOR","MONOCRISTAL","ECRO_CINE",dCINE)

    ################### traitement DEFI_MATERIAU monocristallin #######
    renameMotCle(jdc,"DEFI_MATERIAU","ECOU_VISC1","MONO_VISC1")
    renameMotCle(jdc,"DEFI_MATERIAU","ECOU_VISC2","MONO_VISC2")
    renameMotCle(jdc,"DEFI_MATERIAU","ECOU_VISC3","MONO_VISC3")
    renameMotCle(jdc,"DEFI_MATERIAU","ECRO_CINE1","MONO_CINE1")
    renameMotCle(jdc,"DEFI_MATERIAU","ECRO_CINE2","MONO_CINE2")
    renameMotCle(jdc,"DEFI_MATERIAU","ECRO_ISOT1","MONO_ISOT1")
    renameMotCle(jdc,"DEFI_MATERIAU","ECRO_ISOT2","MONO_ISOT2")
    renameMotCle(jdc,"DEFI_MATERIAU","KOCKS_RAUCH","MONO_DD_KR")

    ################ traitement DEFI_MATERIAU/THER_HYDR #######
    removeMotCleInFact(jdc,"DEFI_MATERIAU","THER_HYDR","QSR_K")
     
    ##################### traitement AFFE_CARA_ELEM/DISCRET ###############"
    dDISCRET={"K_T_N_NS":"K_T_N",  "K_T_L_NS":"K_T_L",  "K_TR_N_NS":"K_TR_N",  "K_TR_L_NS":"K_TR_L",
              "M_T_N_NS":"M_T_N",  "M_T_L_NS":"M_T_L",  "M_TR_N_NS":"M_TR_N",  "M_TR_L_NS":"M_TR_L",
              "A_T_N_NS":"A_T_N",  "A_T_L_NS":"A_T_L",   "A_TR_N_NS":"A_TR_N", "A_TR_L_NS":"A_TR_L"}
    dlist_DISCRET=["K_T_N_NS","K_T_L_NS", "K_TR_N_NS","K_TR_L_NS","M_T_N_NS","M_T_L_NS","M_TR_N_NS","M_TR_L_NS","A_T_N_NS","A_T_L_NS","A_TR_N_NS","A_TR_L_NS"]

    removeMotCleInFact(jdc,"AFFE_CARA_ELEM","DISCRET_2D","SYME")
    removeMotCleInFact(jdc,"AFFE_CARA_ELEM","DISCRET","SYME")
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"AFFE_CARA_ELEM","DISCRET","SYME='NON'",((("CARA",dlist_DISCRET,jdc),"MCsousMCFcourantaPourValeurDansListe"),))
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"AFFE_CARA_ELEM","DISCRET_2D","SYME='NON'",((("CARA",dlist_DISCRET,jdc),"MCsousMCFcourantaPourValeurDansListe"),))
    ChangementValeurDsMCF(jdc,"AFFE_CARA_ELEM","DISCRET_2D","CARA",dDISCRET)
    ChangementValeurDsMCF(jdc,"AFFE_CARA_ELEM","DISCRET","CARA",dDISCRET)

    #####CHARGEMENT
    
    ####################### traitement  CONTACT ###############################################


    renameMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","ITER_MULT_MAXI","ITER_CONT_MULT")
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","NB_REAC_GEOM","NB_ITER_GEOM")
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"AFFE_CHAR_MECA","CONTACT","RESOLUTION='NON'",((("METHODE","VERIF",jdc),"MCsousMCFcourantaPourValeur"),))
    copyMotClefInOperToFact(jdc,"AFFE_CHAR_MECA","MODELE","CONTACT")
    moveMCFToCommand(jdc,"AFFE_CHAR_MECA","CONTACT","DEFI_CONTACT","ZONE")
    removeMotCle(jdc,"AFFE_CHAR_MECA","CONTACT",pasDeRegle(),1)

    
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","LIAISON_UNILATER","METHODE")
    AjouteMotClefDansFacteur(jdc,"AFFE_CHAR_MECA","LIAISON_UNILATER","METHODE='LIAISON_UNIL'",pasDeRegle())
    copyMotClefInOperToFact(jdc,"AFFE_CHAR_MECA","MODELE","LIAISON_UNILATER")
    moveMCFToCommand(jdc,"AFFE_CHAR_MECA","LIAISON_UNILATER","DEFI_CONTACT","ZONE")
    removeMotCle(jdc,"AFFE_CHAR_MECA","LIAISON_UNILATER",pasDeRegle(),1)
    
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA_F","LIAISON_UNILATER","METHODE")
    AjouteMotClefDansFacteur(jdc,"AFFE_CHAR_MECA_F","LIAISON_UNILATER","METHODE='LIAISON_UNIL'",pasDeRegle())
    AjouteMotClefDansFacteur(jdc,"AFFE_CHAR_MECA_F","LIAISON_UNILATER","FORMULATION='LIAISON_UNIL'",pasDeRegle())
    copyMotClefInOperToFact(jdc,"AFFE_CHAR_MECA_F","MODELE","LIAISON_UNILATER")
    moveMCFToCommand(jdc,"AFFE_CHAR_MECA_F","LIAISON_UNILATER","DEFI_CONTACT","ZONE")
    removeMotCle(jdc,"AFFE_CHAR_MECA_F","LIAISON_UNILATER",pasDeRegle(),1)

    chercheOperInsereMotCleSiRegle(jdc,"DEFI_CONTACT","FORMULATION='XFEM'",((("ZONE","METHODE","XFEM",jdc),"MCsousMCFaPourValeur"),))
    chercheOperInsereMotCleSiRegle(jdc,"DEFI_CONTACT","FORMULATION='CONTINUE'",((("ZONE","METHODE","CONTINUE",jdc),"MCsousMCFaPourValeur"),))
    chercheOperInsereMotCleSiRegle(jdc,"DEFI_CONTACT","FORMULATION='VERIF'",((("ZONE","METHODE","VERIF",jdc),"MCsousMCFaPourValeur"),))
    chercheOperInsereMotCleSiRegle(jdc,"DEFI_CONTACT","FORMULATION='LIAISON_UNIL'",((("ZONE","METHODE","LIAISON_UNIL",jdc),"MCsousMCFaPourValeur"),))
    liste_meth_ZONE=["GCP","CONTRAINTE","LAGRANGIEN","PENALISATION"]
    chercheOperInsereMotCleSiRegle(jdc,"DEFI_CONTACT","FORMULATION='DISCRETE'",((("ZONE","METHODE",liste_meth_ZONE,jdc),"MCsousMCFaPourValeurDansListe"),))
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"DEFI_CONTACT","ZONE","ALGO_CONT='LAGRANGIEN'",((("METHODE","LAGRANGIEN",jdc),"MCsousMCFcourantaPourValeur"),))
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"DEFI_CONTACT","ZONE","ALGO_FROT='LAGRANGIEN'",((("METHODE","LAGRANGIEN",jdc),"MCsousMCFcourantaPourValeur"),(("COULOMB",),"existeMCsousMCFcourant"),))
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"DEFI_CONTACT","ZONE","ALGO_CONT='GCP'",((("METHODE","GCP",jdc),"MCsousMCFcourantaPourValeur"),))
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"DEFI_CONTACT","ZONE","ALGO_CONT='PENALISATION'",((("METHODE","PENALISATION",jdc),"MCsousMCFcourantaPourValeur"),))
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"DEFI_CONTACT","ZONE","ALGO_FROT='PENALISATION'",((("METHODE","PENALISATION",jdc),"MCsousMCFcourantaPourValeur"),(("COULOMB",),"existeMCsousMCFcourant"),))
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"DEFI_CONTACT","ZONE","ALGO_CONT='CONTRAINTE'",((("METHODE","CONTRAINTE",jdc),"MCsousMCFcourantaPourValeur"),))
    removeMotCleInFact(jdc,"DEFI_CONTACT","ZONE","METHODE")
    
    
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","COEF_RESI")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","FROTTEMENT")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","ITER_CONT_MAXI")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","ITER_FROT_MAXI")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","ITER_GCP_MAXI")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","ITER_GEOM_MAXI")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","LISSAGE")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","NB_RESOL")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","PRE_COND")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","REAC_GEOM")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","REAC_ITER")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","RECH_LINEAIRE")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","STOP_INTERP")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","STOP_SINGULIER")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","RESI_ABSO")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","ITER_CONT_MULT")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","ITER_PRE_MAXI")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","NB_ITER_GEOM")
    moveMotCleFromFactToFather(jdc,"DEFI_CONTACT","ZONE","MODELE")

    
    # FORMULATION = DEPL/VITE
    # Si EXCL_FROT_1
    # Si EXCL_FROT_2


    ####################### traitement DCX/DCY/DCZ #############################
    dDC={"DCX":"DX","DCY":"DY","DCZ":"DZ"}
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA","DDL_IMPO","DCX","DX")
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA","DDL_IMPO","DCY","DY")
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA","DDL_IMPO","DCZ","DZ")
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA_F","DDL_IMPO","DCX","DX")
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA_F","DDL_IMPO","DCY","DY")
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA_F","DDL_IMPO","DCZ","DZ")
    renameMotCleInFact(jdc,"AFFE_CHAR_CINE","MECA_IMPO","DCX","DX")
    renameMotCleInFact(jdc,"AFFE_CHAR_CINE","MECA_IMPO","DCY","DY")
    renameMotCleInFact(jdc,"AFFE_CHAR_CINE","MECA_IMPO","DCZ","DZ")
    # QUESTION Non pris en compte : AFFE_CHAR_MECA/LIAISON_DDL","DDL",Liste de valeurs avec DC*)
    # peut_etre avec changeTouteValeur ?
    
    ######################### traitement COMB_SISM_MODAL APPUI #######################""
    # attention il faut traiter d'abord DECORRELE avant CORRELE sinon CORRELE apparaît dans DECORELLE
    moveMotCleFromFactToFather(jdc,"COMB_SISM_MODAL","EXCIT","MONO_APPUI")
    moveMotCleFromFactToFather(jdc,"COMB_SISM_MODAL","EXCIT","MULTI_APPUI")
    removeMotCleInFactSiRegle(jdc,"COMB_SISM_MODAL","COMB_MULT_APPUI","TYPE_COMBI",((("MULTI_APPUI","DECORRELE",jdc),"MCaPourValeur"),))
    renameMotCleSiRegle(jdc,"COMB_SISM_MODAL","COMB_MULT_APPUI","GROUP_APPUI",((("MULTI_APPUI","DECORRELE",jdc),"MCaPourValeur"),),1)

    ########################  traitement DYNA_TRAN_MODAL ##################
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"DYNA_TRAN_MODAL","CHOC","FROTTEMENT='COULOMB'",((("COULOMB",),"existeMCsousMCFcourant"),))

    ######################### traitement AFFE_CHAR_MECA PESANTEUR ROTATION#################
    EclaMotCleToFact(jdc,"AFFE_CHAR_MECA","PESANTEUR","GRAVITE","DIRECTION")
    EclaMotCleToFact(jdc,"AFFE_CHAR_MECA","ROTATION","VITESSE","AXE")
    moveMotClefInOperToFact(jdc,"AFFE_CHAR_MECA","CENTRE","ROTATION")

    ######################## traitement DEFI_BASE_MODALE ##############
    renameMotCleInFact(jdc,"DEFI_BASE_MODALE","RITZ","MODE_STAT","MODE_INTF")
    renameMotCleInFact(jdc,"DEFI_BASE_MODALE","RITZ","MULT_ELAS","MODE_INTF")

    ####################### traitement DYNA_ISS_VARI #################
    renameMotCle(jdc,"DYNA_ISS_VARI","PAS","FREQ_PAS")


    #####IMPRESSION
    
    #################### traitement IMPR_RESU  #######################
    removeMotCleInFact(jdc,"IMPR_RESU","RESU","INFO_RESU")

    ######################### traitement IMPR_MATRICE ####################
    removeCommande(jdc,"IMPR_MATRICE")

    #######################  traitement PROJ_CHAMP  #####################
    renameMotCle(jdc,"PROJ_CHAMP","CHAM_NO","CHAM_GD",1,pasDeRegle())
    ChangementValeur(jdc,"PROJ_CHAMP","METHODE",{ "ELEM":"COLLOCATION"})

    ####################### traitement MACR_ADAP_MAIL ##############"
    ChangementValeur(jdc,"MACR_ADAP_MAIL","TYPE_VALEUR_INDICA",{"V_ABSOLUE":"ABSOLU","V_RELATIVE":"RELATIF"})
    renameMotCle(jdc,"MACR_ADAP_MAIL","INDICATEUR","NOM_CHAM")
    renameMotCle(jdc,"MACR_ADAP_MAIL","NOM_CMP_INDICA","NOM_CMP")
    renameMotCle(jdc,"MACR_ADAP_MAIL","TYPE_OPER_INDICA","USAGE_CHAMP")
    renameMotCle(jdc,"MACR_ADAP_MAIL","TYPE_VALEUR_INDICA","USAGE_CMP")
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"MACR_ADAP_MAIL","ZONE","TYPE='BOITE'",((("RAYON",),"nexistepasMCsousMCFcourant"),))
    AjouteMotClefDansFacteurCourantSiRegle(jdc,"MACR_ADAP_MAIL","ZONE","TYPE='SPHERE'",((("RAYON",),"existeMCsousMCFcourant"),))
    ChangementValeur(jdc,"MACR_ADAP_MAIL","VERSION_HOMARD",{"V9_5":"V10_1"})
    ChangementValeur(jdc,"MACR_ADAP_MAIL","VERSION_HOMARD",{"V9_N":"V10_1_N"})
    ChangementValeur(jdc,"MACR_INFO_MAIL","VERSION_HOMARD",{"V9_5":"V10_1"})
    ChangementValeur(jdc,"MACR_INFO_MAIL","VERSION_HOMARD",{"V9_N":"V10_1_N"})

    ###################### traitement de POST_CHAM_XFEM  #################
    removeMotCle(jdc,"POST_CHAM_XFEM","MODELE",pasDeRegle(),0)
    removeMotCle(jdc,"POST_CHAM_XFEM","MAILLAGE_FISS",pasDeRegle(),0)
    removeMotCle(jdc,"POST_CHAM_XFEM","NOM_CHAM",pasDeRegle(),0)

    ##################### traitement de SIMU_POINT_MAT/SUPPORT #############
    chercheOperInsereFacteur(jdc,"SIMU_POINT_MAT","SUPPORT='POINT'",pasDeRegle(),0)

    ######################  traitement AFFE_CARA_ELEM/UNITE_EUROPLEXUS ######
    renameMotCleInFact(jdc,"AFFE_CARA_ELEM","RIGI_PARASOL","UNITE_EUROPLEXUS","UNITE",pasDeRegle(),0)

    #################### traitement DEFI_GLRC/IMPRESSION #############
    removeMotCle(jdc,"DEFI_GLRC","IMPRESSION",pasDeRegle(),0)

    ################### traitement AFFICHAGE  #####
    removeMotCleInFact(jdc,"DYNA_NON_LINE","AFFICHAGE","LONG_I",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","AFFICHAGE","LONG_R",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","AFFICHAGE","NOM_COLONNE",pasDeRegle(),0)
    removeMotCleInFact(jdc,"DYNA_NON_LINE","AFFICHAGE","PREC_R",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","AFFICHAGE","LONG_I",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","AFFICHAGE","LONG_R",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","AFFICHAGE","NOM_COLONNE",pasDeRegle(),0)
    removeMotCleInFact(jdc,"STAT_NON_LINE","AFFICHAGE","PREC_R",pasDeRegle(),0)

    ################### traitement CALC_NO *RESU #########
    removeMotCle(jdc,"CALC_NO","GROUP_MA_RESU",pasDeRegle(),0)
    removeMotCle(jdc,"CALC_NO","MAILLE_RESU",pasDeRegle(),0)
    removeMotCle(jdc,"CALC_NO","GROUP_NO_RESU",pasDeRegle(),0)
    removeMotCle(jdc,"CALC_NO","NOEUD_RESU",pasDeRegle(),0)

    ################## traitement POST_K1_K2_K3/MAILLAGE ######
    removeMotCleSiRegle(jdc,"POST_K1_K2_K3","MAILLAGE",((("RESULTAT"),"existeMCFParmi"),))

     ######### traitement CALC_ELEM/TYPE_ESTI ####
    dESTI={"ERRE_ELEM_SIGM":"ERME_ELEM","ERZ1_ELEM_SIGM":"ERZ1_ELEM","ERZ2_ELEM_SIGM":"ERZ2_ELEM",
            "QIRE_ELEM_SIGM":"QIRE_ELEM","QIZ1_ELEM_SIGM":"QIZ1_ELEM","QIZ2_ELEM_SIGM":"QIZ2_ELEM"}
    ChangementValeur(jdc,"CALC_ELEM","TYPE_ESTI",dESTI)

    ######### suppression CALC_ELEM/NORME ######
    removeMotCle(jdc,"CALC_ELEM","NORME",pasDeRegle(),0)

    ########## traitement CALC_ELEM/CALC_NO OPTION
    #dSENSI={"DEDE_ELNO_DLDE":"DEDE_ELNO","DEDE_NOEU_DLDE":"DEDE_NOEU","DESI_ELNO_DLSI":"DESI_ELNO","DESI_NOEU_DLSI":"DESI_NOEU",
    #        "DETE_ELNO_DLTE":"DETE_ELNO","DETE_NOEU_DLTE":"DETE_NOEU"}
    dOPTION={"DEDE_ELNO_DLDE":"DEDE_ELNO","DEDE_NOEU_DLDE":"DEDE_NOEU","DESI_ELNO_DLSI":"DESI_ELNO","DESI_NOEU_DLSI":"DESI_NOEU",
             "DETE_ELNO_DLTE":"DETE_ELNO","DETE_NOEU_DLTE":"DETE_NOEU",
             "INTE_ELNO_ACTI":"INTE_ELNO","INTE_ELNO_REAC":"INTE_ELNO","INTE_NOEU_ACTI":"INTE_NOEU","INTE_NOEU_REAC":"INTE_NOEU",
             "PRES_DBEL_DEPL":"PRME_ELNO","PRES_ELNO_IMAG":"PRAC_ELNO","PRES_ELNO_REEL":"PRAC_ELNO",
             "PRES_NOEU_DBEL":"PRAC_NOEU","PRES_NOEU_IMAG":"PRAC_NOEU","PRES_NOEU_REEL":"PRAC_NOEU",
             "ARCO_ELNO_SIGM":"SIRO_ELEM","ARCO_NOEU_SIGM":"SIRO_ELEM",
             "ENDO_ELNO_ELGA":"ENDO_ELNO","ENDO_ELNO_SIGA":"ENDO_ELNO","ENDO_ELNO_SINO":"ENDO_ELNO","ENDO_NOEU_SINO":"ENDO_NOEU",
             "ERRE_ELEM_SIGM":"ERME_ELEM","ERRE_ELEM_TEMP":"ERTH_ELEM",
             "CRIT_ELNO_RUPT":"CRIT_ELNO","DEGE_ELNO_DEPL":"DEGE_ELNO","DEGE_NOEU_DEPL":"DEGE_NOEU",
             "DURT_ELNO_META":"DURT_ELNO","DURT_NOEU_META":"DURT_NOEU","ECIN_ELEM_DEPL":"ECIN_ELEM","ENEL_ELNO_ELGA":"ENEL_ELNO",
             "ENEL_NOEU_ELGA":"ENEL_NOEU","EPEQ_ELNO_TUYO":"EPTQ_ELNO","EPME_ELGA_DEPL":"EPME_ELGA","EPME_ELNO_DEPL":"EPME_ELNO",
             "EPMG_ELGA_DEPL":"EPMG_ELGA","EPMG_ELNO_DEPL":"EPMG_ELNO","EPMG_NOEU_DEPL":"EPMG_NOEU","EPOT_ELEM_DEPL":"EPOT_ELEM",
             "EPSG_ELGA_DEPL":"EPSG_ELGA","EPSG_ELNO_DEPL":"EPSG_ELNO","EPSG_NOEU_DEPL":"EPSG_NOEU",
             "EPSI_ELGA_DEPL":"EPSI_ELGA","EPSI_NOEU_DEPL":"EPSI_NOEU","EPSI_ELNO_DEPL":"EPSI_ELNO","EPSI_ELNO_TUYO":"EPTU_ELNO",
             "ERZ1_ELEM_SIGM":"ERZ1_ELEM","ERZ2_ELEM_SIGM":"ERZ2_ELEM",
             "ETOT_ELNO_ELGA":"ETOT_ELNO","EXTR_ELGA_VARI":"VAEX_ELGA","EXTR_ELNO_VARI":"VAEX_ELNO","EXTR_NOEU_VARI":"VAEX_NOEU",
             "FLUX_ELGA_TEMP":"FLUX_ELGA","FLUX_ELNO_TEMP":"FLUX_ELNO","FLUX_NOEU_TEMP":"FLUX_NOEU",
             "HYDR_NOEU_ELGA":"HYDR_NOEU","HYDR_ELNO_ELGA":"HYDR_ELNO",
             "META_ELNO_TEMP":"META_ELNO","META_NOEU_TEMP":"META_NOEU",
             "PMPB_ELGA_SIEF":"PMPB_ELGA","PMPB_ELNO_SIEF":"PMPB_ELNO","PMPB_NOEU_SIEF":"PMPB_NOEU",
             "QIRE_ELEM_SIGM":"QIRE_ELEM","QIRE_ELNO_ELEM":"QIRE_ELNO","QIRE_NOEU_ELEM":"QIRE_NOEU",
             "QIZ1_ELEM_SIGM":"QIZ1_ELEM","QIZ2_ELEM_SIGM":"QIZ2_ELEM",
             "SIEF_ELGA_DEPL":"SIEF_ELGA","SIEF_ELNO_ELGA":"SIEF_ELNO","SIEF_NOEU_ELGA":"SIEF_NOEU",
             "SIEQ_ELNO_TUYO":"SITQ_ELNO","SING_ELNO_ELEM":"SING_ELNO","SIPO_ELNO_DEPL":"SIPO_ELNO","SIPO_NOEU_DEPL":"SIPO_NOEU",
             "SOUR_ELGA_ELEC":"SOUR_ELGA",
             "DCHA_ELGA_SIGM":"DERA_ELGA","DCHA_ELNO_SIGM":"DERA_ELNO","DCHA_NOEU_SIGM":"DERA_NOEU",
             "RADI_ELGA_SIGM":"DERA_ELGA","RADI_ELNO_SIGM":"DERA_ELNO","RADI_NOEU_SIGM":"DERA_NOEU",
             "EFGE_ELNO_CART":"EFCA_ELNO","EFGE_NOEU_CART":"EFCA_NOEU","EFGE_ELNO_DEPL":"EFGE_ELNO","EFGE_NOEU_DEPL":"EFGE_NOEU",
             "EQUI_ELGA_EPME":"EPMQ_ELGA","EQUI_ELNO_EPME":"EPMQ_ELNO","EQUI_NOEU_EPME":"EPMQ_NOEU",
             "EQUI_ELGA_EPSI":"EPEQ_ELGA","EQUI_ELNO_EPSI":"EPEQ_ELNO","EQUI_NOEU_EPSI":"EPEQ_NOEU",
             "EQUI_ELGA_SIGM":"SIEQ_ELGA","EQUI_ELNO_SIGM":"SIEQ_ELNO","EQUI_NOEU_SIGM":"SIEQ_NOEU",
             "SIGM_ELNO_CART":"SICA_ELNO","SIGM_NOEU_CART":"SICA_NOEU","SIGM_ELNO_COQU":"SICO_ELNO","SIGM_NOEU_COQU":"SICO_ELNO",
             "SIGM_ELNO_TUYO":"SITU_ELNO",
             "SIGM_ELNO_DEPL":"SIGM_ELNO","SIGM_NOEU_DEPL":"SIGM_NOEU","SIGM_NOZ1_ELGA":"SIZ1_ELGA","SIGM_NOZ2_ELGA":"SIZ2_ELGA",
             "VALE_NCOU_MAXI":"SPMX_ELGA","VARI_ELNO_COQU":"VACO_ELNO","VARI_ELNO_TUYO":"VATU_ELNO",
             "VARI_NOEU_ELGA":"VARI_NOEU","VARI_ELNO_ELGA":"VARI_ELNO",
             "INDI_LOCA_ELGA":"INDL_ELGA"}
    #"FORC_NODA":"FORC_NOEU","REAC_NODA":"REAC_NOEU"
    ChangementValeurDsMCF(jdc,"AFFE_MATERIAU","AFFE_VARC","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"COMB_FOURIER","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"CREA_CHAMP","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"CREA_RESU","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"EXTR_RESU","ARCHIVAGE","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"IMPR_RESU","RESU","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"LIRE_RESU","FORMAT_MED","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"LIRE_RESU","FORMAT_IDEAS","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"LIRE_RESU","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"MACR_ADAP_MAIL","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"MACR_ASPIC_CALC","IMPRESSION","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"MACR_LIGN_COUPE","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"MODI_REPERE","MODI_CHAM","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"POST_ELEM","INTEGRALE","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"POST_ELEM","MINMAX","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"POST_RCCM","RESU_MECA","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"POST_RELEVE_T","ACTION","NOM_CHAM",dOPTION)    
    ChangementValeur(jdc,"PROJ_CHAMP","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"PROJ_MESU_MODAL","MODELE_MESURE","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"RECU_FONCTION","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"REST_GENE_PHYS","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"REST_SOUS_STRUC","NOM_CHAM",dOPTION)
    ChangementValeur(jdc,"REST_SPEC_PHYS","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"TEST_RESU","RESU","NOM_CHAM",dOPTION)
    ChangementValeurDsMCF(jdc,"TEST_RESU","GENE","NOM_CHAM",dOPTION)
    
    ChangementValeur(jdc,"CALC_CHAM_ELEM","OPTION",dOPTION)
    ChangementValeur(jdc,"CALC_ELEM","OPTION",dOPTION)
    ChangementValeur(jdc,"CALC_META","OPTION",dOPTION)
    ChangementValeur(jdc,"CALC_NO","OPTION",dOPTION)
    ChangementValeur(jdc,"COMB_SISM_MODAL","OPTION",dOPTION)
    ChangementValeur(jdc,"MECA_STATIQUE","OPTION",dOPTION)
    ChangementValeurDsMCF(jdc,"MACRO_ELAS_MULT","CAS_CHARGE","OPTION",dOPTION)
    ChangementValeur(jdc,"THER_NON_LINE","OPTION",dOPTION)

    ############ Message si SuppressionValeurs ou Valeurs ambigue CALC_ELEM/OPTION
    rOPTION=("'DEUL_ELGA_DEPL'","'DEUL_ELGA_TEMP'","'DURT_ELGA_META'",
             "'ERRE_ELNO_DEPL'", "'ERRE_NOEU_ELEM'", "'ERRE_ELNO_ELEM'","'EPSP_NOEU_ZAC'","'HYDR_ELNO_ELGA'",
             "'SIGM_NOEU_ZAC'","'SIGM_ELNO_SIEF'","'SIGM_NOEU_SIEF'","'SIPO_ELNO_SIEF'","'SIPO_NOEU_SIEF'",
             "'SIRE_ELNO_DEPL'","'SIRE_NOEU_DEPL'","'SIEF_NOEU'",
             "'PRES_ELNO_DBEL'", "'VARI_NOEU'")
    # Options ambigue :  PRES_ELNO_DBEL --> prac_elno/prme_elno, ERRE* --> ERME_ELNO ou ERTH_ELNO selon PHENOMENE
    # En commentaires les commandes non concernees par rOPTION
    
    GenereErreurValeurDsMCF(jdc,"AFFE_MATERIAU","AFFE_VARC","NOM_CHAM",rOPTION)
    #GenereErreurValeur(jdc,"COMB_FOURIER","NOM_CHAM",rOPTION)
    GenereErreurValeur(jdc,"CREA_CHAMP","NOM_CHAM",rOPTION)
    GenereErreurValeur(jdc,"CREA_RESU","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"EXTR_RESU","ARCHIVAGE","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"IMPR_RESU","RESU","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"LIRE_RESU","FORMAT_MED","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"LIRE_RESU","FORMAT_IDEAS","NOM_CHAM",rOPTION)
    GenereErreurValeur(jdc,"LIRE_RESU","NOM_CHAM",rOPTION)
    GenereErreurValeur(jdc,"MACR_ADAP_MAIL","NOM_CHAM",rOPTION)
    #GenereErreurDsMCF(jdc,"MACR_ASPIC_CALC","IMPRESSION","NOM_CHAM",rOPTION)
    GenereErreurValeur(jdc,"MACR_LIGN_COUPE","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"MODI_REPERE","MODI_CHAM","NOM_CHAM",rOPTION)
    #GenereErreurValeurDsMCF(jdc,"POST_RCCM","RESU_MECA","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"POST_ELEM","INTEGRALE","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"POST_ELEM","MINMAX","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"POST_RELEVE_T","ACTION","NOM_CHAM",rOPTION)    
    GenereErreurValeur(jdc,"PROJ_CHAMP","NOM_CHAM",rOPTION)
    #GenereErreurValeurDsMCF(jdc,"PROJ_MESU_MODAL","MODELE_MESURE","NOM_CHAM",rOPTION)
    GenereErreurValeur(jdc,"RECU_FONCTION","NOM_CHAM",rOPTION)
    #GenereErreurValeur(jdc,"REST_GENE_PHYS","NOM_CHAM",rOPTION)
    #GenereErreurValeur(jdc,"REST_SOUS_STRUC","NOM_CHAM",rOPTION)
    #GenereErreurValeur(jdc,"REST_SPEC_PHYS","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"TEST_RESU","RESU","NOM_CHAM",rOPTION)
    GenereErreurValeurDsMCF(jdc,"TEST_RESU","GENE","NOM_CHAM",rOPTION)
    
    GenereErreurValeur(jdc,"CALC_CHAM_ELEM","OPTION",rOPTION)
    GenereErreurValeur(jdc,"CALC_ELEM","OPTION",rOPTION)
    #GenereErreurValeur(jdc,"CALC_META","OPTION",rOPTION)
    GenereErreurValeur(jdc,"CALC_NO","OPTION",rOPTION)
    #GenereErreurValeur(jdc,"COMB_SISM_MODAL","OPTION",rOPTION)
    #GenereErreurValeur(jdc,"MECA_STATIQUE","OPTION",rOPTION)
    GenereErreurValeurDsMCF(jdc,"MACRO_ELAS_MULT","CAS_CHARGE","OPTION",rOPTION)
    #GenereErreurValeur(jdc,"THER_NON_LINE","OPTION",rOPTION)        
    
    ########### Message si CALC_ELEM/SENSIBILITE
    GenereErreurMCF(jdc,"CALC_ELEM","SENSIBILITE")

    # non fait CALC_NO OPTION=FORC_NODA_NONL

    ########## Traitement MACRO_MISS_3D --> CALC_MISS
    renameCommandeSiRegle(jdc,"MACRO_MISS_3D","CALC_MISS",((("OPTION","MODULE","MISS_IMPE",jdc),"MCsousMCFaPourValeur"),(("PARAMETRE","ISSF"),"nexistepasMCsousMCF"),(("PARAMETRE","DIRE_ONDE"),"nexistepasMCsousMCF"),(("PARAMETRE","CONTR_LISTE"),"nexistepasMCsousMCF"),(("PARAMETRE","CONTR_NB"),"nexistepasMCsousMCF"),))
    renameCommandeSiRegle(jdc,"MACRO_MISS_3D","CALC_MISS",((("OPTION","MODULE","MISS_IMPE",jdc),"MCsousMCFaPourValeur"),(("PARAMETRE","ISSF","NON",jdc),"MCsousMCFaPourValeur"),(("PARAMETRE","DIRE_ONDE"),"nexistepasMCsousMCF"),(("PARAMETRE","CONTR_LISTE"),"nexistepasMCsousMCF"),(("PARAMETRE","CONTR_NB"),"nexistepasMCsousMCF"),))
    removeMotCleInFact(jdc,"CALC_MISS","PARAMETRE","FICH_RESU_IMPE",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_MISS","PARAMETRE","FICH_RESU_FORC",pasDeRegle(),0)
    removeMotCleInFact(jdc,"CALC_MISS","PARAMETRE","FICH_POST_TRAI",pasDeRegle(),0)
    removeMotCle(jdc,"CALC_MISS","UNITE_OPTI_MISS",pasDeRegle())
    removeMotCle(jdc,"CALC_MISS","UNITE_MODELE_SOL",pasDeRegle())
    removeMotCle(jdc,"CALC_MISS","OPTION",pasDeRegle(),1)
    ChangementValeur(jdc,"CALC_MISS","VERSION",{"V1_4":"V6.5"})
    ChangementValeur(jdc,"CALC_MISS","VERSION",{"V1_5":"V6.6"})
    ChangementValeur(jdc,"CALC_MISS","VERSION",{"V1_3":"V6.5"})

    macr=""
    interf=""
    amor=""
    for c in jdc.root.childNodes:
        if c.name != "IMPR_MACR_ELEM" : continue
        for mc in c.childNodes:
             if mc.name == "MACR_ELEM_DYNA" : macr=mc.getText(jdc)
             if mc.name == "GROUP_MA_INTERF": interf=mc.getText(jdc)
             if mc.name == "AMOR_REDUIT": amor=mc.getText(jdc)
    if amor != "" : chercheOperInsereFacteur(jdc,"CALC_MISS",amor,pasDeRegle(),0)
    if interf != "" : chercheOperInsereFacteur(jdc,"CALC_MISS",interf,pasDeRegle(),0)
    if macr != "" : chercheOperInsereFacteur(jdc,"CALC_MISS",macr,pasDeRegle(),0)

    chercheOperInsereFacteur(jdc,"CALC_MISS","TABLE_SOL=''",pasDeRegle(),0)
    chercheOperInsereFacteur(jdc,"CALC_MISS","TYPE_RESU='FICHIER'",pasDeRegle(),0)
    
    #################################################################
    f=open(outfile,'w')
    f.write(jdc.getSource())
    f.close()

    log.ferme(hdlr)

def main():
    parser = optparse.OptionParser(usage=usage)

    parser.add_option('-i','--infile', dest="infile", default='toto.comm',
        help="Le fichier à traduire")
    parser.add_option('-o','--outfile', dest="outfile", default='tutu.comm',
        help="Le fichier traduit")

    options, args = parser.parse_args()
    traduc(options.infile,options.outfile)

if __name__ == '__main__':
    main()

