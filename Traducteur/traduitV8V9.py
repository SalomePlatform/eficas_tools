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

import calcG


atraiter=( "DEFI_MAILLAGE","CALC_VECT_ELEM","DYNA_TRAN_EXPLI","DYNA_NON_LINE","STAT_NON_LINE","FACT_LDLT","FACT_GRAD","RESO_LDLT","RESO_GRAD","DYNA_TRAN_MODAL","NORM_MODE","MACRO_MODE_MECA","POST_RCCM","THER_NON_LINE","THER_LINEAIRE","THER_NON_LINE_MO","DEFI_CABLE_BP","GENE_VARI_ALEA","DEFI_MATERIAU","IMPR_MATRICE","CALC_G","CALC_MATR_ELEM","MACR_ADAP_MAIL","MACR_INFO_MAIL","REST_BASE_PHYS","COMB_SISM_MODAL","TEST_FICHIER","MACR_ELEM_DYNA","CREA_CHAMP","AFFE_CHAR_MECA","AFE_CHAR_MECA_F")

def traduc(infile,outfile,flog=None):

    hdlr=log.initialise(flog)
    jdc=getJDC(infile,atraiter)
    root=jdc.root

    #Parse les mocles des commandes
    parseKeywords(root)
    
    ####################### traitement erreurs ########################
    GenereErreurPourCommande(jdc,("POST_RCCM","DEFI_MATERIAU","TEST_FICHIER","DYNA_NON_LINE"))

    ####################### traitement Sous-Structuration  #######################
    renameMotCleInFact(jdc,"DEFI_MAILLAGE","DEFI_SUPER_MAILLE","MACR_ELEM_STAT","MACR_ELEM")
    renameMotCleInFact(jdc,"DYNA_NON_LINE","SOUS_STRUC","MAILLE","SUPER_MAILLE")
    renameMotCleInFact(jdc,"STAT_NON_LINE","SOUS_STRUC","MAILLE","SUPER_MAILLE")
    renameMotCleInFact(jdc,"CALC_VECT_ELEM","SOUS_STRUC","MAILLE","SUPER_MAILLE")
    #########################################################################

    ####################### traitement MACR_ELEM_DYNA #######################
    removeMotCle(jdc,"MACR_ELEM_DYNA","OPTION")
    #########################################################################

    ####################### traitement Resolution lineaire ######################
    renameMotCle(jdc,"RESO_LDLT","MATR_FACT","MATR")
    renameMotCle(jdc,"RESO_GRAD","MATR_ASSE","MATR")
    renameMotCle(jdc,"RESO_GRAD","MATR_FACT","MATR_FACT")
    renameOper(jdc,"RESO_LDLT","RESOUDRE")
    renameOper(jdc,"RESO_GRAD","RESOUDRE")
    renameOper(jdc,"FACT_LDLT","FACTORISER")
    renameOper(jdc,"FACT_GRAD","FACTORISER")
    #########################################################################

    ####################### traitement DYNA_TRAN_MODAL ######################
    removeMotCle(jdc,"DYNA_TRAN_MODAL","NB_MODE_DIAG")
    #########################################################################

    ############# traitement MASS_INER dans NORM_MODE/MACRO_MODE_MECA ##########
    removeMotCle(jdc,"NORM_MODE","MASS_INER")
    removeMotCleInFact(jdc,"MACRO_MODE_MECA","NORM_MODE","MASS_INER")
    #########################################################################

    ####################### traitement POST_RCCM ############################
    removeMotCleInFactSiRegleAvecErreur(jdc,"POST_RCCM","SITUATION","NUME_PASSAGE",((("TYPE_RESU_MECA","TUYAUTERIE",jdc),"MCaPourValeur"),))
    chercheOperInsereFacteurSiRegle(jdc,"POST_RCCM","SEISME", ((("SITUATION","NB_CYCL_SEISME"),"existeMCsousMCF"),))
    moveMotCleFromFactToFact(jdc,"POST_RCCM","SITUATION","NB_CYCL_SEISME","SEISME")
#    AjouteMotClefDansFacteurSiRegle(jdc,"POST_RCCM","SITUATION", "transferez_au_bloc_SEISME_CHAR_ETAT_NB_OCCUR,NUME_SITU,NUME_GROUP_et_eventuellement_NOM_SITU_et_NUME_RESU_THER",((("SITUATION","NB_CYCL_SEISME"),"existeMCsousMCF"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"POST_RCCM","SITUATION","supprimez_a_la_main_ce_bloc",((("SITUATION","NB_CYCL_SEISME"),"existeMCsousMCF"),))
#    removeMotCleInFactSiRegleAvecErreur(jdc,"POST_RCCM","SITUATION","NB_CYCL_SEISME",((("SITUATION","NB_CYCL_SEISME"),"existeMCsousMCF"),))
    removeMotCleInFactSiRegle(jdc,"POST_RCCM","SITUATION","NB_CYCL_SEISME",((("SITUATION","NB_CYCL_SEISME"),"existeMCsousMCF"),))
    removeMotCleInFact(jdc,"POST_RCCM","CHAR_MECA","TYPE_CHAR",)
    removeMotCleInFact(jdc,"POST_RCCM","RESU_MECA","TYPE_CHAR",)
    #########################################################################

    ####################### traitement THER_NON_LINE ############################
    renameMotCleInFact(jdc,"THER_NON_LINE","TEMP_INIT","NUME_INIT","NUME_ORDRE")
    renameMotCle(jdc,"THER_NON_LINE","TEMP_INIT","ETAT_INIT",)
    renameMotCleInFact(jdc,"THER_NON_LINE","INCREMENT","NUME_INIT","NUME_INST_INIT")
    renameMotCleInFact(jdc,"THER_NON_LINE","INCREMENT","NUME_FIN","NUME_INST_FIN")
    #########################################################################

    ####################### traitement THER_LINEAIRE ############################
    renameMotCleInFact(jdc,"THER_LINEAIRE","TEMP_INIT","NUME_INIT","NUME_ORDRE")
    renameMotCle(jdc,"THER_LINEAIRE","TEMP_INIT","ETAT_INIT",)
    renameMotCleInFact(jdc,"THER_LINEAIRE","INCREMENT","NUME_INIT","NUME_INST_INIT")
    renameMotCleInFact(jdc,"THER_LINEAIRE","INCREMENT","NUME_FIN","NUME_INST_FIN")
    #########################################################################

    ####################### traitement THER_NON_LINE ############################
    renameMotCleInFact(jdc,"THER_NON_LINE","TEMP_INIT","NUME_INIT","NUME_ORDRE")
    renameMotCle(jdc,"THER_NON_LINE","TEMP_INIT","ETAT_INIT",)
    #########################################################################

    ####################### traitement DEFI_CABLE_BP ######################
    removeMotCle(jdc,"DEFI_CABLE_BP","MAILLAGE")
    #########################################################################

    ####################### traitement GENE_VARI_ALEA ######################
    removeMotCleSiRegle(jdc,"GENE_VARI_ALEA","COEF_VAR",((("TYPE","EXPONENTIELLE",jdc),"MCaPourValeur"),))
    #########################################################################

    ####################### traitement DEFI_MATERIAU ######################
    removeMotCleAvecErreur(jdc,"DEFI_MATERIAU","BAZANT_FD")
    removeMotCleAvecErreur(jdc,"DEFI_MATERIAU","PORO_JOINT")
    removeMotCleAvecErreur(jdc,"DEFI_MATERIAU","APPUI_ELAS")
    removeMotCleAvecErreur(jdc,"DEFI_MATERIAU","ZIRC_EPRI")
    removeMotCleAvecErreur(jdc,"DEFI_MATERIAU","ZIRC_CYRA2")
    # BARCELONE
    moveMotCleFromFactToFact(jdc,"DEFI_MATERIAU","CAM_CLAY","MU","BARCELONE")
    moveMotCleFromFactToFact(jdc,"DEFI_MATERIAU","CAM_CLAY","PORO","BARCELONE")
    moveMotCleFromFactToFact(jdc,"DEFI_MATERIAU","CAM_CLAY","LAMBDA","BARCELONE")
    moveMotCleFromFactToFact(jdc,"DEFI_MATERIAU","CAM_CLAY","KAPPA","BARCELONE")
    moveMotCleFromFactToFact(jdc,"DEFI_MATERIAU","CAM_CLAY","M","BARCELONE")
    moveMotCleFromFactToFact(jdc,"DEFI_MATERIAU","CAM_CLAY","PRES_CRIT","BARCELONE")
    moveMotCleFromFactToFact(jdc,"DEFI_MATERIAU","CAM_CLAY","PA","BARCELONE")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","CAM_CLAY","PA","KCAM")
    # CAM_CLAY
    AjouteMotClefDansFacteur(jdc,"DEFI_MATERIAU","CAM_CLAY","MU=xxx",)
    AjouteMotClefDansFacteurSiRegle(jdc,"DEFI_MATERIAU","CAM_CLAY","PTRAC=XXX",((("CAM_CLAY","KCAM"),"existeMCsousMCF"),))
    # VENDOCHAB
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB","S_VP","S")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB","N_VP","N")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB","M_VP","UN_SUR_M", erreur=1)
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB","K_VP","UN_SUR_K")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB","SEDVP1","ALPHA_D")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB","SEDVP2","BETA_D")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB_FO","S_VP","S")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB_FO","N_VP","N")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB_FO","M_VP","UN_SUR_M", erreur=1)
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB_FO","K_VP","UN_SUR_K")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB_FO","SEDVP1","ALPHA_D")
    renameMotCleInFact(jdc,"DEFI_MATERIAU","VENDOCHAB_FO","SEDVP2","BETA_D")
    # GLRC 
    renameCommandeSiRegle(jdc,"DEFI_MATERIAU","DEFI_GLRC", ((("GLRC_DAMAGE","GLRC_ACIER",),"existeMCFParmi"),))
    #########################################################################

    ####################### traitement IMPR_MATRICE ######################
    removeCommandeSiRegleAvecErreur(jdc,"IMPR_MATRICE",((("MATR_ELEM","FORMAT","RESULTAT",jdc),"MCsousMCFaPourValeur"),))
    removeCommandeSiRegleAvecErreur(jdc,"IMPR_MATRICE",((("MATR_ASSE","FORMAT","RESULTAT",jdc),"MCsousMCFaPourValeur"),))
    #########################################################################

    ####################### traitement MACR_ADAP/INFO_MAIL ######################
    dadap_mail={"V8_11":"V9_5", "V8_N":"V9_N", "V8_N_PERSO":"V9_N_PERSO"}
    ChangementValeur(jdc,"MACR_ADAP_MAIL","VERSION_HOMARD",dadap_mail)
    ChangementValeur(jdc,"MACR_INFO_MAIL","VERSION_HOMARD",dadap_mail)
    #########################################################################

    ####################### traitement REST_BASE_PHYS ######################
    renameCommandeSiRegle(jdc,"REST_BASE_PHYS","REST_SOUS_STRUC", ((("RESULTAT","SQUELETTE","SOUS_STRUC","BASE_MODALE","CYCLIQUE","SECTEUR"),"existeMCFParmi"),))
    renameCommandeSiRegle(jdc,"REST_BASE_PHYS","REST_COND_TRAN", ((("MACR_ELEM_DYNA","RESU_PHYS"),"existeMCFParmi"),))
    renameCommande(jdc,"REST_BASE_PHYS","REST_GENE_PHYS", )
    #########################################################################

    ####################### traitement CALC_G ######################
    removeMotCleSiRegleAvecErreur(jdc,"CALC_G","OPTION",((("OPTION","G_LAGR",jdc),"MCaPourValeur"),))
    removeMotCleSiRegleAvecErreur(jdc,"CALC_G","OPTION",((("OPTION","G_LAGR_GLOB",jdc),"MCaPourValeur"),))
    removeMotCle(jdc,"CALC_G","PROPAGATION")
    removeMotCle(jdc,"CALC_G","THETA_LAGR")
    removeMotCle(jdc,"CALC_G","DIRE_THETA_LAGR")
    #########################################################################

    ####################### traitement COMB_SISM_MODAL ######################
    AjouteMotClefDansFacteurSiRegle(jdc,"COMB_SISM_MODAL","EXCIT","MULTI_APPUI='DECORRELE'", ((("EXCIT","MONO_APPUI"),"nexistepasMCsousMCF"),))
    #########################################################################

    ####################### traitement TEST_FICHIER ######################
    renameMotCleAvecErreur(jdc,"TEST_FICHIER","NB_CHIFFRE","NB_VALE")
    removeMotCle(jdc,"TEST_FICHIER","EPSILON")
    #########################################################################

    ####################### traitement CALC_MATR_ELEM ######################
    removeMotCleSiRegle(jdc,"CALC_MATR_ELEM","OPTION",((("OPTION","RIGI_MECA_LAGR",jdc),"MCaPourValeur"),))
    removeMotCleAvecErreur(jdc,"CALC_MATR_ELEM","PROPAGATION")
    removeMotCle(jdc,"CALC_MATR_ELEM","THETA")
    #########################################################################

    ####################### traitement ITER_INTE_PAS ######################
    removeMotCleInFactSiRegle(jdc,"STAT_NON_LINE","COMP_INCR","ITER_INTE_PAS",((("COMP_INCR","DEFORMATION","SIMO_MIEHE",jdc),"MCsousMCFaPourValeur"),))
    removeMotCleInFactSiRegle(jdc,"DYNA_NON_LINE","COMP_INCR","ITER_INTE_PAS",((("COMP_INCR","DEFORMATION","SIMO_MIEHE",jdc),"MCsousMCFaPourValeur"),))
    #########################################################################

    ################## traitement RECH_LINEAIRE et PILOTAGE dans DYNA_NON_LINE #################
    removeMotCleAvecErreur(jdc,"DYNA_NON_LINE","RECH_LINEAIRE")
    removeMotCleAvecErreur(jdc,"DYNA_NON_LINE","PILOTAGE")
    #########################################################################

    ####################### traitement DYNA_TRAN_EXPLI ######################
    renameOper(jdc,"DYNA_TRAN_EXPLI","DYNA_NON_LINE")
    AjouteMotClefDansFacteur(jdc,"DYNA_NON_LINE","TCHAMWA","FORMULATION='ACCELERATION'")
    AjouteMotClefDansFacteur(jdc,"DYNA_NON_LINE","DIFF_CENT","FORMULATION='ACCELERATION'")
    #########################################################################

    ####################### traitement SCHEMA_TEMPS dans DYNA_NON_LINE ######################
    AjouteMotClefDansFacteur(jdc,"DYNA_NON_LINE","NEWMARK","FORMULATION='DEPLACEMENT'")
    AjouteMotClefDansFacteur(jdc,"DYNA_NON_LINE","HHT","FORMULATION='DEPLACEMENT'")
    AjouteMotClefDansFacteur(jdc,"DYNA_NON_LINE","TETA_METHODE","FORMULATION='DEPLACEMENT'")
    renameMotCleInFact(jdc,"DYNA_NON_LINE","NEWMARK","ALPHA","BETA",)
    renameMotCleInFact(jdc,"DYNA_NON_LINE","NEWMARK","DELTA","GAMMA",)
    renameMotCleInFact(jdc,"DYNA_NON_LINE","TETA_METHODE","TETA","THETA",)
    AjouteMotClefDansFacteurSiRegle(jdc,"DYNA_NON_LINE","NEWMARK","SCHEMA='NEWMARK'",((("NEWMARK",),"existeMCFParmi"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"DYNA_NON_LINE","TETA_METHODE","SCHEMA='THETA_METHODE'",((("TETA_METHODE",),"existeMCFParmi"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"DYNA_NON_LINE","HHT","SCHEMA='HHT'",((("HHT",),"existeMCFParmi"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"DYNA_NON_LINE","TCHAMWA","SCHEMA='TCHAMWA'",((("TCHAMWA",),"existeMCFParmi"),))
    AjouteMotClefDansFacteurSiRegle(jdc,"DYNA_NON_LINE","DIFF_CENT","SCHEMA='DIFF_CENT'",((("DIFF_CENT",),"existeMCFParmi"),))
    renameMotCle(jdc,"DYNA_NON_LINE","NEWMARK","SCHEMA_TEMPS")
    renameMotCle(jdc,"DYNA_NON_LINE","TETA_METHODE","SCHEMA_TEMPS")
    renameMotCle(jdc,"DYNA_NON_LINE","HHT","SCHEMA_TEMPS")
    renameMotCle(jdc,"DYNA_NON_LINE","DIFF_CENT","SCHEMA_TEMPS")
    renameMotCle(jdc,"DYNA_NON_LINE","TCHAMWA","SCHEMA_TEMPS")
    removeMotCleInFact(jdc,"DYNA_NON_LINE","INCREMENT","EVOLUTION")
    moveMotClefInOperToFact(jdc,"DYNA_NON_LINE","STOP_CFL","SCHEMA_TEMPS")
    #########################################################################

    ####################### traitement CONTACT ######################
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","KT_ULTM")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","EFFO_N_INIT")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","RIGI_N_IRRA")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","RIGI_N_FO")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","RIGI_MZ")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","ANGLE_1")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","ANGLE_2")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","ANGLE_3")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","ANGLE_4")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","MOMENT_1")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","MOMENT_2")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","MOMENT_3")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","MOMENT_4")
    removeMotCleInFact(jdc,"DEFI_MATERIAU","DIS_CONTACT","C_PRAGER_MZ")
    dDis_Choc={"DIS_CONTACT":"DIS_CHOC"}
    ChangementValeurDsMCF(jdc,"STAT_NON_LINE","COMP_INCR","RELATION",dDis_Choc)
    ChangementValeurDsMCF(jdc,"DYNA_NON_LINE","COMP_INCR","RELATION",dDis_Choc)
    renameMotCleInFact(jdc,"STAT_NON_LINE","COMP_INCR","DIS_CONTACT","DIS_CHOC")
    renameMotCleInFact(jdc,"DYNA_NON_LINE","COMP_INCR","DIS_CONTACT","DIS_CHOC")
    dGrilles={"DIS_GRICRA":"GRILLE_CRAYONS"}
    ChangementValeurDsMCF(jdc,"STAT_NON_LINE","COMP_INCR","RELATION",dGrilles)
    ChangementValeurDsMCF(jdc,"DYNA_NON_LINE","COMP_INCR","RELATION",dGrilles)

    renameCommandeSiRegle(jdc,"AFFE_CHAR_MECA_F","AFFE_CHAR_MECA",((("CONTACT",),"existeMCFParmi"),))
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","RECHERCHE")
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","PROJECTION")
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","VECT_Y")
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","VECT_ORIE_POU")
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","MODL_AXIS")
    dAppariement={"MAIT_ESCL_SYME":"MAIT_ESCL"}
    ChangementValeurDsMCF(jdc,"AFFE_CHAR_MECA","CONTACT","APPARIEMENT",dAppariement)

    #########################################################################

    ####################### traitement CREA_CHAMP ######################
    chercheOperInsereFacteurSiRegle(jdc,"CREA_CHAMP","PRECISION=1.E-3,", ((("PRECISION",),"nexistepas"),(("CRITERE",),"existe"),),0)
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

