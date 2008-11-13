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


atraiter=( "DEFI_MAILLAGE","CALC_VECT_ELEM","DYNA_NON_LINE","STAT_NON_LINE","FACT_LDLT","FACT_GRAD","RESO_LDLT","RESO_GRAD","DYNA_TRAN_MODAL","NORM_MODE","MACRO_MODE_MECA","POST_RCCM","THER_NON_LINE","THER_LINEAIRE","THER_NON_LINE_MO","DEFI_CABLE_BP","GENE_VARI_ALEA","DEFI_MATERIAU","IMPR_MATRICE","CALC_G","CALC_MATR_ELEM")

def traduc(infile,outfile,flog=None):

    hdlr=log.initialise(flog)
    jdc=getJDC(infile,atraiter)
    root=jdc.root

    #Parse les mocles des commandes
    parseKeywords(root)
    
    ####################### traitement erreurs ########################
    GenereErreurPourCommande(jdc,("POST_RCCM"))

    ####################### traitement Sous-Structuration  #######################
    renameMotCleInFact(jdc,"DEFI_MAILLAGE","DEFI_SUPER_MAILLE","MACR_ELEM_STAT","MACR_ELEM")
    renameMotCleInFact(jdc,"DYNA_NON_LINE","SOUS_STRUC","MAILLE","SUPER_MAILLE")
    renameMotCleInFact(jdc,"STAT_NON_LINE","SOUS_STRUC","MAILLE","SUPER_MAILLE")
    renameMotCleInFact(jdc,"CALC_VECT_ELEM","SOUS_STRUC","MAILLE","SUPER_MAILLE")
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

    ####################### traitement MASS_INER dans NORM_MODE ##########
    removeMotCle(jdc,"NORM_MODE","MASSE_INER")
    removeMotCleInFact(jdc,"MACRO_MODE_MECA","NORM_MODE","MASSE_INER")
    #########################################################################

    ####################### traitement POST_RCCM ############################
    removeMotCleInFactSiRegleAvecErreur(jdc,"POST_RCCM","SITUATION","NUME_PASSAGE",((("TYPE_RESU_MECA","TUYAUTERIE",jdc),"MCaPourValeur"),))
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
    #########################################################################

    ####################### traitement IMPR_MATRICE ######################
    removeCommandeSiRegleAvecErreur(jdc,"IMPR_MATRICE",((("MATR_ELEM","FORMAT","RESULTAT",jdc),"MCsousMCFaPourValeur"),))
    removeCommandeSiRegleAvecErreur(jdc,"IMPR_MATRICE",((("MATR_ASSE","FORMAT","RESULTAT",jdc),"MCsousMCFaPourValeur"),))
    #########################################################################


    ####################### traitement CALC_G ######################
    removeMotCleSiRegleAvecErreur(jdc,"CALC_G","OPTION",((("OPTION","G_LAGR",jdc),"MCaPourValeur"),))
    removeMotCleSiRegleAvecErreur(jdc,"CALC_G","OPTION",((("OPTION","G_LAGR_GLOB",jdc),"MCaPourValeur"),))
    removeMotCle(jdc,"CALC_G","PROPAGATION")
    removeMotCle(jdc,"CALC_G","THETA_LAGR")
    removeMotCle(jdc,"CALC_G","DIRE_THETA_LAGR")
    #########################################################################

    ####################### traitement CALC_MATR_ELEM ######################
    removeMotCleSiRegle(jdc,"CALC_MATR_ELEM","OPTION",((("OPTION","RIGI_MECA_LAGR",jdc),"MCaPourValeur"),))
    removeMotCleAvecErreur(jdc,"CALC_MATR_ELEM","PROPAGATION")
    removeMotCle(jdc,"CALC_MATR_ELEM","THETA")
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

    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","RECHERCHE")
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","VECT_Y")
    removeMotCleInFact(jdc,"AFFE_CHAR_MECA","CONTACT","VECT_ORIE_POU")

    renameCommandeSiRegle(jdc,"AFFE_CHAR_MECA_F","AFFE_CHAR_MECA",((("CONTACT",),"existeMCFParmi"),))
    #########################################################################

    ####################### traitement CAM_CLAY ######################
    AjouteMotClefDansFacteur(jdc,"DEFI_MATERIAU","CAM_CLAY","MU=xxx",)
    #########################################################################

    ####################### traitement GLRC ######################
    renameCommandeSiRegle(jdc,"DEFI_MATERIAU","DEFI_GLRC", ((("GLRC_DAMAGE","GLRC_ACIER",),"existeMCFParmi"),))
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

