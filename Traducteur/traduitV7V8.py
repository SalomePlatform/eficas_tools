#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
usage="""usage: %prog [options]
Typical use is:
  python traduitV7V8.py --infile=xxxx --outfile=yyyy
"""

import log
import optparse

from load   import getJDC
from mocles import parseKeywords
from removemocle  import *
from renamemocle  import *
from renamemocle  import *
from inseremocle  import *
from changeValeur import *
from movemocle    import *
from dictErreurs  import GenereErreurPourCommande

# Demander a emmanuel pour affe_char_ther et test_resu
import calcG

atraiter=( "IMPR_GENE","CALC_FONCTION", "DEFI_MATERIAU","STAT_NON_LINE",
          "CALC_G_LOCAL_T","CALC_G_THETA_T","CALC_G","AFFE_CHAR_MECA",
          "AFFE_CHAR_THER_F","IMPR_CO","DEFI_SQUELETTE","DEFI_FONCTION",
          "CALC_THETA","AFFE_MODELE","DYNA_NON_LINE","CALC_ELEM",
          "CALC_NO","EXTR_MODE","CALC_META","IMPR_RESU","TEST_RESU",
          "DEFI_THER_JOULE","DYNA_TRAN_EXPLI","DEBUT","CALC_CHAM_ELEM",
          "AFFE_CHAR_THER", "MACR_LIGN_COUPE","POST_RCCM","PROJ_MESU_MODAL",
          "CREA_RESU","CREA_CHAMP","DIST_LIGN_3D","MODI_MAILLAGE","LIRE_TABLE",
          "POST_SIMPLIFIE","AFFE_MATERIAU","DEFI_MAILLAGE","DEPL_INTERNE",
          "POST_DYNA_ALEA","RECU_FONCTION","DYNA_TRAN_MODAL","DEFI_INTERF_DYNA",
          "CALC_PRECONT","DEFI_TEXTURE","TEST_RESU","COMB_CHAM_NO","COMB_CHAM_ELEM",
          "CALC_FATIGUE","IMPR_OAR",
           "MACR_ASCOUF_CALC","MACR_ASPIC_CALC","MACR_CABRI_CALC",
           "MACR_ADAP_MAIL","IMPR_FICO_HOMARD"
        )

#atraiter=( "MACR_ADAP_MAIL",)

def traduc(infile,outfile):

    hdlr=log.initialise()
    jdc=getJDC(infile,atraiter)
    root=jdc.root

    #Parse les mocles des commandes
    parseKeywords(root)
    
    ####################### traitement erreurs ########################
    GenereErreurPourCommande(jdc,("POST_RCCM","DIST_LIGN_3D","IMPR_OAR","COMB_CHAM_NO","COMB_CHAM_ELEM"))

    ####################### traitement CALC_META     #######################
    renameMotCleInFact(jdc,"CALC_META","ETAT_INIT","META_INIT","META_INIT_ELNO")

    ####################### traitement CALC_FONCTION #######################
    removeMotCleSiRegle(jdc,"CALC_FONCTION","NOM_PARA",((("MAX"),"existeMCFParmi"),))
    renameCommandeSiRegle(jdc,"CALC_FONCTION","INFO_FONCTION", ((("RMS","MAX","NOCI_SEISME","NORME","ECART-TYPE"),"existeMCFParmi"),))

    ####################### traitement IMPR_GENE     #######################
    moveMotCleFromFactToFather(jdc,"IMPR_GENE","GENE","UNITE")
    moveMotCleFromFactToFather(jdc,"IMPR_GENE","GENE","FORMAT")

    ####################### traitement STAT/DYNA_NON_LINE #######################
    moveMotCleFromFactToFactMulti(jdc,"STAT_NON_LINE","CONVERGENCE","RESI_INTE_RELA",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"STAT_NON_LINE","CONVERGENCE","ITER_INTE_MAXI",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"STAT_NON_LINE","CONVERGENCE","ITER_INTE_PAS",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"STAT_NON_LINE","CONVERGENCE","RESO_INTE",("COMP_INCR","COMP_ELAS"))
    removeMotCleAvecErreur(jdc,"STAT_NON_LINE","VARI_COMM")
    moveMotCleFromFactToFactMulti(jdc,"DYNA_NON_LINE","CONVERGENCE","RESI_INTE_RELA",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"DYNA_NON_LINE","CONVERGENCE","ITER_INTE_MAXI",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"DYNA_NON_LINE","CONVERGENCE","ITER_INTE_PAS",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"DYNA_NON_LINE","CONVERGENCE","RESO_INTE",("COMP_INCR","COMP_ELAS"))
    removeMotCleAvecErreur(jdc,"DYNA_NON_LINE","VARI_COMM")

    dStatNonLine={"ELAS":"ELAS_THER"}
    lavertit=("ELAS")
    ChangementValeurDsMCFAvecAvertissement(jdc,"STAT_NON_LINE","COMP_INCR","RELATION_KIT",dStatNonLine,lavertit)

    lavertit=("CHABOCHE","ASSE_COMBU","OHNO","GLRC")
    dchaboche={"CHABOCHE":"VMIS_CIN1_CHAB","ASSE_COMBU":"XXX_IRA","OHNO":"VISC_TAHERI","GLRC":"GLRC_DAMAGE"}
    ChangementValeurDsMCFAvecAvertissement(jdc,"STAT_NON_LINE","COMP_INCR","RELATION",dchaboche,lavertit)
    ChangementValeurDsMCFAvecAvertissement(jdc,"DYNA_NON_LINE","COMP_INCR","RELATION",dchaboche,lavertit)

    removeMotCleInFactSiRegle(jdc,"STAT_NON_LINE","INCREMENT","SUBD_PAS_MINI",((("INCREMENT","SUBD_PAS","1",jdc),"MCsousMCFaPourValeur"),))
    removeMotCleInFactSiRegle(jdc,"STAT_NON_LINE","INCREMENT","COEF_SUBD_PAS_1",((("INCREMENT","SUBD_PAS","1",jdc),"MCsousMCFaPourValeur"),))
    removeMotCleInFactSiRegleAvecErreur(jdc,"STAT_NON_LINE","INCREMENT","SUBD_PAS",((("INCREMENT","SUBD_PAS","1",jdc),"MCsousMCFaPourValeur"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"STAT_NON_LINE","INCREMENT","SUBD_METHODE='UNIFORME',",((("INCREMENT","SUBD_PAS"),"existeMCsousMCF"),))
    renameMotCleInFact(jdc,"STAT_NON_LINE","INCREMENT","COEF_SUBD_PAS_1","SUBD_COEF_PAS_1")
    removeMotCleInFactSiRegle(jdc,"DYNA_NON_LINE","INCREMENT","SUBD_PAS_MINI",((("INCREMENT","SUBD_PAS","1",jdc),"MCsousMCFaPourValeur"),))
    removeMotCleInFactSiRegle(jdc,"DYNA_NON_LINE","INCREMENT","COEF_SUBD_PAS_1",((("INCREMENT","SUBD_PAS","1",jdc),"MCsousMCFaPourValeur"),))
    removeMotCleInFactSiRegleAvecErreur(jdc,"DYNA_NON_LINE","INCREMENT","SUBD_PAS",((("INCREMENT","SUBD_PAS","1",jdc),"MCsousMCFaPourValeur"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"DYNA_NON_LINE","INCREMENT","SUBD_METHODE='UNIFORME',",((("INCREMENT","SUBD_PAS"),"existeMCsousMCF"),))
    renameMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT","COEF_SUBD_PAS_1","SUBD_COEF_PAS_1")

    moveMotClefInOperToFact(jdc,"STAT_NON_LINE","PARM_THETA","COMP_INCR")
    moveMotClefInOperToFact(jdc,"DYNA_NON_LINE","PARM_THETA","COMP_INCR")
    moveMotClefInOperToFact(jdc,"DYNA_TRAN_EXPLI","PARM_THETA","COMP_INCR")

    ####################### traitement DEFI_MATERIAU #######################
    renameMotCle(jdc,"DEFI_MATERIAU","LEMAITRE","LEMAITRE_IRRA")
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","FLU_IRRA","QSR_K",("LEMAITRE_IRRA",))
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","FLU_IRRA","BETA",("LEMAITRE_IRRA",))
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","FLU_IRRA","PHI_ZERO",("LEMAITRE_IRRA",))
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","FLU_IRRA","L",("LEMAITRE_IRRA",))
    removeMotCle(jdc,"DEFI_MATERIAU","FLU_IRRA")
    renameMotCleAvecErreur(jdc,"DEFI_MATERIAU","CHABOCHE","CINx_CHAB")
    renameMotCleAvecErreur(jdc,"DEFI_MATERIAU","OHNO","TAHERI")
    renameMotCleAvecErreur(jdc,"DEFI_MATERIAU","OHNO_FO","TAHERI_FO")
    renameMotCleAvecErreur(jdc,"DEFI_MATERIAU","GLRC","GLRC_DAMAGE")

    renameMotCleInFact(jdc,"DEFI_MATERIAU","GRAN_IRRA","A","GRAN_A")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","GRAN_IRRA","B","GRAN_B")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","GRAN_IRRA","S","GRAN_S")
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","GRAN_IRRA","GRAN_A",("LEMAITRE_IRRA",))
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","GRAN_IRRA","GRAN_B",("LEMAITRE_IRRA",))
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","GRAN_IRRA","GRAN_S",("LEMAITRE_IRRA",))
    removeMotCle(jdc,"DEFI_MATERIAU","GRAN_IRRA")

    chercheOperInsereFacteurSiRegle(jdc,"DEFI_MATERIAU","ELAS",((("CABLE",),"existe"),))
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","CABLE","E",  ("ELAS",))
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","CABLE","NU", ("ELAS",))
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","CABLE","RHO",("ELAS",))
    moveMotCleFromFactToFactMulti(jdc,"DEFI_MATERIAU","CABLE","ALPHA",("ELAS",))
    AjouteMotClefDansFacteurSiRegle(jdc,"DEFI_MATERIAU","ELAS","NU=0.,",((("ELAS","NU"),"nexistepasMCsousMCF"),))

    removeMotCleAvecErreur(jdc,"DEFI_MATERIAU","POLY_CFC")
    removeMotCleAvecErreur(jdc,"DEFI_MATERIAU","ECOU_PLAS1")

    lavertit=("ELAS_THM","SURF_ETAT_SATU","SURF_ETAT_NSAT","CAM_CLAY_THM","LIQU_SATU_GAT","LIQU_NSAT_GAT")
    dTHM={"ELAS_THM":"xxx", "SURF_ETAT_SATU":"xxx", "SURF_ETAT_NSAT":"xxx","CAM_CLAY_THM":"xxx","LIQU_SATU_GAT":"xxx","LIQU_NSAT_GAT":"xxx"}
    ChangementValeurAvecAvertissement(jdc,"DEFI_MATERIAU","COMP_THM",dTHM,lavertit)

    dfatigue={"MATAKE":"MATAKE_MODI_AC", "DOMM_MAXI":"MATAKE_MODI_AV", "FATEMI_SOCIE":"FATESOCI_MODI_AV"}
    ChangementValeurDsMCF(jdc,"DEFI_MATERIAU","CISA_PLAN_CRIT","CRITERE",dfatigue)

    ####################### traitement IMPR_CO       #######################
    chercheOperInsereFacteurSiRegle(jdc,"IMPR_CO","CONCEPT",((("CO",),"existe"),))
    moveMotClefInOperToFact(jdc,"IMPR_CO","CO","CONCEPT")
    renameMotCleInFact(jdc,"IMPR_CO","CONCEPT","CO","NOM")

    ####################### traitement DEFI_SQUELETTE #######################
    chercheOperInsereFacteurSiRegle(jdc,"DEFI_SQUELETTE","CYCLIQUE",((("MODE_CYCL",),"existe"),))
    moveMotClefInOperToFact(jdc,"DEFI_SQUELETTE","MODE_CYCL","CYCLIQUE")

    ####################### traitement AFFE_CHAR_*   #######################
    removeMotCle(jdc,"AFFE_CHAR_MECA","VERI_DDL")
    removeMotCle(jdc,"AFFE_CHAR_MECA","SECH_CALCULEE")
    removeMotCle(jdc,"AFFE_CHAR_MECA","HYDR_CALCULEE")
    removeMotCle(jdc,"AFFE_CHAR_MECA","PRESSION_CALCULEE")
    removeMotCleAvecErreur(jdc,"AFFE_CHAR_MECA","EPSA_CALCULEE")
    removeMotCle(jdc,"AFFE_CHAR_THER_F","VERI_DDL")
    removeMotCle(jdc,"AFFE_CHAR_THER","VERI_DDL")

    ####################### traitement AFFE_CHAR_MECA (CONTACT)   #######################
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","COEF_MULT_ESCL","COEF_MULT")
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","NOM_CHAM","NOM_CMP")
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","NOM_CHAM","NOM_CMP")
    renameMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","GROUP_MA_ESCL","GROUP_MA")
    renameMotCleSiRegle(jdc,"AFFE_CHAR_MECA","CONTACT","LIAISON_UNILATER",((("CONTACT","NOM_CMP"),"existeMCsousMCF"),))
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","LIAISON_UNILATER","APPARIEMENT")

    ####################### traitement CALC_G   #######################
    chercheOperInsereFacteurSiRegle(jdc,"CALC_G_LOCAL_T","LISSAGE",((("LISSAGE_G","LISSAGE_THETA","DEGRE"),"existeMCFParmi"),))
    moveMotClefInOperToFact(jdc,"CALC_G_LOCAL_T","LISSAGE_THETA","LISSAGE")
    moveMotClefInOperToFact(jdc,"CALC_G_LOCAL_T","LISSAGE_G","LISSAGE")
    moveMotClefInOperToFact(jdc,"CALC_G_LOCAL_T","DEGRE","LISSAGE")
    
    dlocal={"CALC_G_LGLO":"G_LAGR", "G_BILINEAIRE":"G_BILI", "CALC_G_MAX":"G_MAX"}
    ChangementValeur(jdc,"CALC_G_LOCAL_T","OPTION",dlocal)
    #
    dtheta={"CALC_G_LAGR":"G_LAGR_GLOB", "G_BILINEAIRE":"G_BILI_GLOB", "CALC_G_MAX":"G_MAX_GLOB","CALC_G":"CALC_G_GLOB"}
    # Attention si le defaut doit generer un avertissement Il faut le mettre comme dernier mot de la liste
    lavertit=("CALC_G_LAGR","CALC_G","defaut")
    ChangementValeurAvecAvertissement(jdc,"CALC_G_THETA_T","OPTION",dtheta,lavertit)
    renameOper(jdc,"CALC_G_LOCAL_T","CALC_G")
    renameOper(jdc,"CALC_G_THETA_T","CALC_G")

    # Attention cela necessite un traitement particulier et ne peut pas etre generalise tel quel
    # Attention egalement doit etre fait avant le regroupement dans THETA 
    calcG.traitementRayon(jdc)
    renameMotCle(jdc,"CALC_G","THETA","THETA_OLD")
    chercheOperInsereFacteur(jdc,"CALC_G","THETA")
    moveMotClefInOperToFact(jdc,"CALC_G","THETA_OLD","THETA")
    renameMotCleInFact(jdc,"CALC_G","THETA","THETA_OLD","THETA")
    
    moveMotClefInOperToFact(jdc,"CALC_G","FOND_FISS","THETA")
    moveMotClefInOperToFact(jdc,"CALC_G","R_INF_FO","THETA")
    moveMotClefInOperToFact(jdc,"CALC_G","R_SUP_FO","THETA")
    moveMotClefInOperToFact(jdc,"CALC_G","R_INF","THETA")
    moveMotClefInOperToFact(jdc,"CALC_G","R_SUP","THETA")
    moveMotClefInOperToFact(jdc,"CALC_G","FISSURE","THETA")
    renameMotCleInFactSiRegle(jdc,"CALC_G","THETA","THETA","THETA_LAGR",((("THETA","R_INF"),"existeMCsousMCF"),))
    renameMotCleInFactSiRegle(jdc,"CALC_G","THETA","THETA","THETA_LAGR",((("THETA","R_SUP"),"existeMCsousMCF"),))
    moveMotCleFromFactToFather(jdc,"CALC_G","THETA","THETA_LAGR")
    removeMotCleAvecErreur(jdc,"CALC_G","MODELE")
    removeMotCleAvecErreur(jdc,"CALC_G","DEPL")
    removeMotCleAvecErreur(jdc,"CALC_G","CHAM_MATER")
    removeMotCleAvecErreur(jdc,"CALC_G","CARA_ELEM")
    chercheOperInsereFacteurSiRegleAvecAvertissement(jdc,"CALC_G","RESULTAT=XXX,",((("THETA_LAGR",),"existeMCFParmi"),),0)

    ####################### traitement AFFE_MODELE   #######################
    daffeModele={"PLAN_FISSURE":"PLAN_JOINT", "AXIS_FISSURE":"AXIS_JOINT"}
    ChangementValeurDsMCF(jdc,"AFFE_MODELE","AFFE","MODELISATION",daffeModele)
    removeMotCleSiRegleAvecErreur(jdc,"AFFE_MODELE","AFFE",((("AFFE","MODELISATION","APPUI_REP",jdc),"MCsousMCFaPourValeur"),))
    removeMotCleSiRegleAvecErreur(jdc,"AFFE_MODELE","AFFE",((("AFFE","MODELISATION","ASSE_GRIL",jdc),"MCsousMCFaPourValeur"),))
    removeMotCleSiRegleAvecErreur(jdc,"AFFE_MODELE","AFFE",((("AFFE","MODELISATION","3D_JOINT_CT",jdc),"MCsousMCFaPourValeur"),))
    renameMotCleInFact(jdc,"AFFE_MODELE","AFFE_SOUS_STRUC","MAILLE","SUPER_MAILLE")
 
    ####################### traitement PROJ_MESU_MODAL #######################
    removeMotCleInFact(jdc,"PROJ_MESU_MODAL","MODELE_MESURE","NOM_PARA")
    removeMotCleInFactSiRegleAvecErreur(jdc,"AFFE_CHAR_MECA","CONTACT","FROTTEMENT",((("CONTACT","METHODE","CONTRAINTE",jdc),"MCsousMCFaPourValeur"),))

    ####################### traitement CALC_ELEM / CALC_NO #######################
    dcalcelemno={"ERRE_ELGA_NORE":"ERRE_ELEM_SIGM","ERRE_ELEM_NOZ1":"ERZ1_ELEM_SIGM","ERRE_ELEM_NOZ2":"ERZ2_ELEM_SIGM","ERRE_ELNO_ELGA":"ERRE_ELNO_ELEM","ERRE_NOEU_ELGA":"ERRE_NOEU_ELEM","ERTH_ELEM_TEMP":"ERRE_ELEM_TEMP","ERTH_ELNO_ELEM":"ERRE_ELNO_ELEM","EPGR_ELNO":"EPFP_ELNO","EPGR_ELGA":"EPFP_ELGA","DURT_ELGA_TEMP":"DURT_ELNO_TEMP"}
    ChangementValeur(jdc,"CALC_ELEM","OPTION",dcalcelemno)
    ChangementValeur(jdc,"CALC_NO","OPTION",dcalcelemno)
    ChangementValeurDsMCF(jdc,"IMPR_RESU","RESU","NOM_CHAM",dcalcelemno)
    ChangementValeur(jdc,"TEST_RESU","RESU",dcalcelemno)
    removeMotCleAvecErreur(jdc,"TEST_RESU","UNITE")

    chercheOperInsereFacteurSiRegle(jdc,"CALC_ELEM","REPE_COQUE",((("NUME_COUCHE","NIVE_COUCHE","ANGLE","PLAN"),"existeMCFParmi"),))
    moveMotClefInOperToFact(jdc,"CALC_ELEM","NIVE_COUCHE","REPE_COQUE")
    moveMotClefInOperToFact(jdc,"CALC_ELEM","NUME_COUCHE","REPE_COQUE")
    moveMotClefInOperToFact(jdc,"CALC_ELEM","ANGLE","REPE_COQUE")
    moveMotClefInOperToFact(jdc,"CALC_ELEM","PLAN","REPE_COQUE")

    
    ####################### traitement EXTR_MODE #######################
    AjouteMotClefDansFacteurSiRegle(jdc,"EXTR_MODE","FILTRE_MODE","SEUIL=1.E-3", ((("FILTRE_MODE","CRIT_EXTR",),"existeMCsousMCF"),(("FILTRE_MODE","SEUIL",),"nexistepasMCsousMCF")))

    ####################### traitement DYNA_TRAN_EXPLI #######################
    removeMotCle(jdc,"DYNA_TRAN_EXPLI","NEWMARK")
    removeMotCle(jdc,"DYNA_TRAN_EXPLI","HHT")
    chercheOperInsereFacteur(jdc,"DYNA_TRAN_EXPLI","DIFF_CENT")

    ####################### traitement CREA_RESU #######################
    dcrearesu={"HYDR_ELGA":"HYDR_NOEU_ELGA"}
    lavertit=("HYDR_ELGA",)
    ChangementValeur(jdc,"CREA_RESU","NOM_CHAM",dcrearesu,lavertit)

    ####################### traitement CREA_CHAMP #######################
    dcrearesu={"HYDR_ELGA":"HYDR_ELNO_ELGA"}
    lavertit=("HYDR_ELGA",)
    ChangementValeur(jdc,"CREA_CHAMP","NOM_CHAM",dcrearesu,lavertit)
    ChangementValeur(jdc,"CREA_CHAMP","TYPE_CHAM",dcrearesu,lavertit)

    ####################### traitement TEST_RESU #######################
    dcrearesu={"HYDR_ELGA":"HYDR_NOEU_ELGA"}
    lavertit=("HYDR_ELGA",)
    ChangementValeurDsMCFAvecAvertissement(jdc,"TEST_RESU","RESU","NOM_CHAM",dcrearesu,lavertit)

    ####################### traitement DEBUT #######################
    removeMotCleSiRegle(jdc,"DEBUT","BASE",((("BASE","FICHIER","LOCALE",jdc),"MCsousMCFaPourValeur"),))

    ####################### traitement DEFI_THER_JOULE #######################
    removeCommande(jdc,"DEFI_THER_JOULE")

    ####################### traitement CALC_CHAM_ELEM #######################
    removeCommandeSiRegleAvecErreur(jdc,"CALC_CHAM_ELEM",((("OPTION","SOUR_ELGA_ELEC",jdc),"MCaPourValeur"),))

    ####################### traitement MACR_LIGNE_COUPE #######################
    AppelleMacroSelonValeurConcept(jdc,"MACR_LIGN_COUPE",("LIGN_COUPE","TABLE"))
    removeMotCleInFact(jdc,"MACR_LIGN_COUPE","LIGN_COUPE","TABLE")

    ####################### traitement MODI_MAILLAGE #######################
    removeMotCle(jdc,"MODI_MAILLAGE","MODELE")

    ####################### traitement LIRE_TABLE #######################
    removeMotCle(jdc,"LIRE_TABLE","TYPE_TABLE")

    ####################### traitement POST_SIMPLIFIE #######################
    removeCommande(jdc,"POST_SIMPLIFIE")

    ####################### traitement AFFE_MATERIAU #######################
    removeMotCleInFact(jdc,"AFFE_MATERIAU","AFFE","SECH_REF")

    ####################### traitement DEFI_MAILLAGE #######################
    renameMotCleInFact(jdc,"DEFI_MAILLAGE","DEFI_MAILLE","MAILLE","SUPER_MAILLE")
    renameMotCle(jdc,"DEFI_MAILLAGE","DEFI_MAILLE","DEFI_SUPER_MAILLE")
    renameMotCleInFact(jdc,"DEFI_MAILLAGE","RECO_GLOBAL","MAILLE","SUPER_MAILLE")
    renameMotCleInFact(jdc,"DEFI_MAILLAGE","RECO_MAILLE","MAILLE","SUPER_MAILLE")
    renameMotCle(jdc,"DEFI_MAILLAGE","RECO_MAILLE","RECO_SUPER_MAILLE")
    renameMotCleInFact(jdc,"DEFI_MAILLAGE","DEFI_NOEUD","MAILLE","SUPER_MAILLE")
    renameMotCleInFact(jdc,"DEFI_MAILLAGE","DEFI_GROUP_NO","MAILLE","SUPER_MAILLE")

    ####################### traitement DEPL_INTERNE #######################
    renameMotCle(jdc,"DEPL_INTERNE","MAILLE","SUPER_MAILLE")


    ####################### traitement POST_DYNA_ALEA #######################
    removeMotCleAvecErreur(jdc,"POST_DYNA_ALEA","GAUSS")
    removeMotCleAvecErreur(jdc,"POST_DYNA_ALEA","RAYLEIGH")
    removeMotCleAvecErreur(jdc,"POST_DYNA_ALEA","DEPASSEMENT")
    removeMotCleAvecErreur(jdc,"POST_DYNA_ALEA","VANMARCKE")

    ####################### traitement RECU_FONCTION #######################
# il faut aussi ajouter la regle suivante :
# s'il existe TYPE_RESU='FONCTION_C', renommer NOM_PARA_TABL='FONCTION_C'
    removeMotCleSiRegle(jdc,"RECU_FONCTION","NOM_PARA_TABL",((("TYPE_RESU","FONCTION_C",jdc),"MCaPourValeur"),))
    chercheOperInsereFacteurSiRegle(jdc,"RECU_FONCTION","NOM_PARA_TABL='FONCTION_C',",((("TYPE_RESU","FONCTION_C",jdc),"MCaPourValeur"),),estunFacteur=0)
    removeMotCle(jdc,"RECU_FONCTION","TYPE_RESU")
    chercheOperInsereFacteurSiRegle(jdc,"RECU_FONCTION","NOM_PARA_TABL='FONCTION',",((("OBSTACLE",),"existe"),),estunFacteur=0)
    chercheOperInsereFacteurSiRegle(jdc,"RECU_FONCTION","FILTRE",((("OBSTACLE",),"existe"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"RECU_FONCTION","FILTRE","NOM_PARA='LIEU',",((("OBSTACLE",),"existe"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"RECU_FONCTION","FILTRE","VALE_K='DEFIOBST',",((("OBSTACLE",),"existe"),))
    renameMotCle(jdc,"RECU_FONCTION","OBSTACLE","TABLE")

    ####################### traitement DYNA_TRAN_MODAL #######################
    renameMotCleInFact(jdc,"DYNA_TRAN_MODAL","EXCIT","NUME_MODE","NUME_ORDRE",erreur=1)

    ####################### traitement DEFI_INTERF_DYNA #######################
    removeMotCleInFact(jdc,"DEFI_INTERF_DYNA","INTERFACE","DDL_ACTIF",erreur=1)


    ####################### traitement CALC_PRECONT #######################
    removeMotCleInFactSiRegle(jdc,"CALC_PRECONT","INCREMENT","SUBD_PAS_MINI",((("INCREMENT","SUBD_PAS","1",jdc),"MCsousMCFaPourValeur"),))
    removeMotCleInFactSiRegle(jdc,"CALC_PRECONT","INCREMENT","COEF_SUBD_PAS_1",((("INCREMENT","SUBD_PAS","1",jdc),"MCsousMCFaPourValeur"),))
    removeMotCleInFactSiRegleAvecErreur(jdc,"CALC_PRECONT","INCREMENT","SUBD_PAS",((("INCREMENT","SUBD_PAS","1",jdc),"MCsousMCFaPourValeur"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"CALC_PRECONT","INCREMENT","SUBD_METHODE='UNIFORME',",((("INCREMENT","SUBD_PAS"),"existeMCsousMCF"),))
    moveMotCleFromFactToFactMulti(jdc,"CALC_PRECONT","CONVERGENCE","RESI_INTE_RELA",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"CALC_PRECONT","CONVERGENCE","ITER_INTE_MAXI",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"CALC_PRECONT","CONVERGENCE","ITER_INTE_PAS",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"CALC_PRECONT","CONVERGENCE","RESO_INTE",("COMP_INCR","COMP_ELAS"))
    renameMotCleInFact(jdc,"CALC_PRECONT","INCREMENT","COEF_SUBD_PAS_1","SUBD_COEF_PAS_1")


    ####################### traitement DEFI_TEXTURE #######################
    removeCommande(jdc,"DEFI_TEXTURE")


    ####################### traitement COMB_CHAM_NO #######################
    renameMotCleInFact(jdc,"COMB_CHAM_NO","COMB_C","CHAM_NO","CHAM_GD")
    chercheOperInsereFacteur(jdc,"COMB_CHAM_NO","TYPE_CHAM='xxx',",estunFacteur=0,erreur=1)
    chercheOperInsereFacteur(jdc,"COMB_CHAM_NO","MODELE='xxx',",estunFacteur=0,erreur=1)
    chercheOperInsereFacteur(jdc,"COMB_CHAM_NO","OPERATION='ASSE',",estunFacteur=0,erreur=1)
    renameMotCle(jdc,"COMB_CHAM_NO","COMB_C","ASSE")
    AjouteMotClefDansFacteur(jdc,"COMB_CHAM_NO","ASSE","CUMUL='NON',")
    AjouteMotClefDansFacteur(jdc,"COMB_CHAM_NO","ASSE","TOUT='OUI',")
    renameOper(jdc,"COMB_CHAM_NO","CREA_CHAMP")


    ####################### traitement MACR_ASCOUF_CALC #######################
    AjouteMotClefDansFacteurSiRegle(jdc,"MACR_ASCOUF_CALC","INCREMENT","SUBD_METHODE='UNIFORME',",((("INCREMENT","SUBD_PAS"),"existeMCsousMCF"),))
    renameMotCleInFact(jdc,"MACR_ASCOUF_CALC","INCREMENT","COEF_SUBD_PAS_1","SUBD_COEF_PAS_1")
    moveMotCleFromFactToFactMulti(jdc,"MACR_ASCOUF_CALC","CONVERGENCE","RESI_INTE_RELA",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"MACR_ASCOUF_CALC","CONVERGENCE","ITER_INTE_MAXI",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"MACR_ASCOUF_CALC","CONVERGENCE","ITER_INTE_PAS",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"MACR_ASCOUF_CALC","CONVERGENCE","RESO_INTE",("COMP_INCR","COMP_ELAS"))


    ####################### traitement MACR_ASPIC_CALC #######################
    AjouteMotClefDansFacteurSiRegle(jdc,"MACR_ASPIC_CALC","INCREMENT","SUBD_METHODE='UNIFORME',",((("INCREMENT","SUBD_PAS"),"existeMCsousMCF"),))
    renameMotCleInFact(jdc,"MACR_ASPIC_CALC","INCREMENT","COEF_SUBD_PAS_1","SUBD_COEF_PAS_1")
    moveMotCleFromFactToFactMulti(jdc,"MACR_ASPIC_CALC","CONVERGENCE","RESI_INTE_RELA",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"MACR_ASPIC_CALC","CONVERGENCE","ITER_INTE_MAXI",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"MACR_ASPIC_CALC","CONVERGENCE","ITER_INTE_PAS",("COMP_INCR","COMP_ELAS"))


    ####################### traitement MACR_CABRI_CALC #######################
    AjouteMotClefDansFacteurSiRegle(jdc,"MACR_CABRI_CALC","INCREMENT","SUBD_METHODE='UNIFORME',",((("INCREMENT","SUBD_PAS"),"existeMCsousMCF"),))
    renameMotCleInFact(jdc,"MACR_CABRI_CALC","INCREMENT","COEF_SUBD_PAS_1","SUBD_COEF_PAS_1")
    moveMotCleFromFactToFactMulti(jdc,"MACR_CABRI_CALC","CONVERGENCE","RESI_INTE_RELA",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"MACR_CABRI_CALC","CONVERGENCE","ITER_INTE_MAXI",("COMP_INCR","COMP_ELAS"))
    moveMotCleFromFactToFactMulti(jdc,"MACR_CABRI_CALC","CONVERGENCE","ITER_INTE_PAS",("COMP_INCR","COMP_ELAS"))


    ####################### traitement CALC_FATIGUE #######################
    dfatigue={"MATAKE":"MATAKE_MODI_AC", "DOMM_MAXI":"MATAKE_MODI_AV", "FATEMI_SOCIE":"FATESOCI_MODI_AV"}
    ChangementValeur(jdc,"CALC_FATIGUE","CRITERE",dfatigue)


    ####################### traitement MACR_ADAP_MAIL #######################
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","MAILLAGE_N")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","MAILLAGE_NP1")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","RESULTAT_N")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","INDICATEUR")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","NOM_CMP_INDICA")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","CRIT_RAFF_PE")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","CRIT_RAFF_ABS")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","CRIT_RAFF_REL")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","CRIT_DERA_PE")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","CRIT_DERA_ABS")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","CRIT_DERA_REL")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","NIVE_MAX")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","INST")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","PRECISION")
    moveMotCleFromFactToFather(jdc,"MACR_ADAP_MAIL","ADAPTATION","CRITERE")
    chercheOperInsereFacteurSiRegle(jdc,"MACR_ADAP_MAIL","ADAPTATIONEW='RAFFINEMENT',",((("ADAPTATION","LIBRE","RAFFINEMENT",jdc),"MCsousMCFaPourValeur"),),estunFacteur=0)
    chercheOperInsereFacteurSiRegle(jdc,"MACR_ADAP_MAIL","ADAPTATIONEW='DERAFFINEMENT',",((("ADAPTATION","LIBRE","DERAFFINEMENT",jdc),"MCsousMCFaPourValeur"),),estunFacteur=0)
    chercheOperInsereFacteurSiRegle(jdc,"MACR_ADAP_MAIL","ADAPTATIONEW='RAFF_DERA',",((("ADAPTATION","LIBRE","RAFF_DERA",jdc),"MCsousMCFaPourValeur"),),estunFacteur=0)
    chercheOperInsereFacteurSiRegle(jdc,"MACR_ADAP_MAIL","ADAPTATIONEW='RAFFINEMENT_UNIFORME',",((("ADAPTATION","UNIFORME","RAFFINEMENT",jdc),"MCsousMCFaPourValeur"),),estunFacteur=0)
    chercheOperInsereFacteurSiRegle(jdc,"MACR_ADAP_MAIL","ADAPTATIONEW='DERAFFINEMENT_UNIFORME',",((("ADAPTATION","UNIFORME","DERAFFINEMENT",jdc),"MCsousMCFaPourValeur"),),estunFacteur=0)
    chercheOperInsereFacteurSiRegle(jdc,"MACR_ADAP_MAIL","ADAPTATIONEW='RIEN',",((("ADAPTATION","UNIFORME","RIEN",jdc),"MCsousMCFaPourValeur"),),estunFacteur=0)
    removeMotCle(jdc,"MACR_ADAP_MAIL","ADAPTATION")
    renameMotCle(jdc,"MACR_ADAP_MAIL","ADAPTATIONEW","ADAPTATION")
    dcalcelemno={"ERRE_ELGA_NORE":"ERRE_ELEM_SIGM","ERRE_ELEM_NOZ1":"ERZ1_ELEM_SIGM","ERRE_ELEM_NOZ2":"ERZ2_ELEM_SIGM","ERRE_ELNO_ELGA":"ERRE_ELNO_ELEM","ERRE_NOEU_ELGA":"ERRE_NOEU_ELEM","ERTH_ELEM_TEMP":"ERRE_ELEM_TEMP","ERTH_ELNO_ELEM":"ERRE_ELNO_ELEM","EPGR_ELNO":"EPFP_ELNO","EPGR_ELGA":"EPFP_ELGA","DURT_ELGA_TEMP":"DURT_ELNO_TEMP"}
    ChangementValeur(jdc,"MACR_ADAP_MAIL","ADAPTATION",dcalcelemno)


    ####################### traitement IMPR_FICO_HOMARD #######################
    removeCommande(jdc,"IMPR_FICO_HOMARD")


    #########################################################################


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

