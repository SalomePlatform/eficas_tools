# -*- coding: utf-8 -*-

import logging
import sets

jdcSet=sets.Set()

dict_erreurs={
#STA8.4
              "DIST_LIGN_3D": "la commande DIST_LIGN_3D a ete supprimee",
              "DEFI_THER_JOULE": "la commande DIST_LIGN_3D a ete supprimee",
              "DIST_LIGN_3D": "la commande DIST_LIGN_3D a ete supprimee",
              "AFFE_MODELE_AFFE": "Les modelisations APPUI_REP, ASSE_GRIL et 3D_JOINT_CT ont ete supprimees",
              "AFFE_CHAR_MECA_CONTACT_FROTTEMENT": "Suppression d un mot clef FROTTEMENT",
              "AFFE_CHAR_MECA_SECH_CALCULEE": "le sechage est maintenant une variable de commande",
              "AFFE_CHAR_MECA_HYDR_CALCULEE": "l'hydratation est maintenant une variable de commande",
              "AFFE_CHAR_MECA_EPSA_CALCULEE":"EPSA est maintenant une variable de commande",
              "AFFE_CHAR_MECA_PRESSION_CALCULEE":"PRESSION_CALCULEE est remplace par EVOL_CHAR",
              "MACR_LIGN_COUPE" : "MACR_LIGN_COUPE demande un traitement manuel",
              "POST_RCCM" : "POST_RCCM demande un traitement manuel",
              "DEFI_MATERIAU_CHABOCHE" : "remplacer la valeur CINx_CHAB",
              "DEFI_MATERIAU_POLY_CFC" : "le materiau POLY_CFC est remplace par le comportement POLYCRISTAL",
              "DEFI_MATERIAU_ECOU_PLAS1" : "le materiau ECOU_PLAS1 est supprime",
              "DEFI_MATERIAU_COMP_THM_ELAS_THM" : "le materiau ELAS_THM a ete supprime",
              "DEFI_MATERIAU_COMP_THM_SURF_ETAT_SATU" : "le materiau SURF_ETAT_SATU a ete supprime",
              "DEFI_MATERIAU_COMP_THM_SURF_ETAT_NSAT" : "le materiau SURF_ETAT_NSAT a ete supprime",
              "DEFI_MATERIAU_COMP_THM_CAM_CLAY_THM" : "le materiau CAM_CLAY_THM a ete supprime",
              "DEFI_MATERIAU_COMP_THM_LIQU_SATU_GAT" : "le materiau LIQU_SATU_GAT a ete supprime",
              "DEFI_MATERIAU_COMP_THM_LIQU_NSAT_GAT" : "le materiau LIQU_NSAT_GAT a ete supprime",
              "DEFI_MATERIAU_GLRC" : "le materiau GLRC a ete remplace par GLRC_DAMAGE",
              "DEFI_MATERIAU_GLRC_FO" : "le materiau GLRC_FO a ete remplace par GLRC_DAMAGE",
              "DEFI_MATERIAU_OHNO" : "le materiau OHNO a ete remplace par TAHERI",
              "DEFI_MATERIAU_OHNO_FO" : "le materiau OHNO a ete remplace par TAHERI",
              "CALC_CHAM_ELEM":"reecrire la partie SOUR_ELGA_ELEC",
              "CALC_G_THETA_T_OPTION_VALEUR":"verifier la valeur d OPTION",
              "CALC_G_THETA_T_OPTION_DEFAUT":"verifier la valeur d OPTION donnee a la place du defaut",
              "CALC_G_MODELE":"Mot Clef MODELE supprimé sous CALC_G",
              "CALC_G_DEPL":"Mot Clef DEPL supprimé sous CALC_G",
              "CALC_G_CHAM_MATER":"Mot Clef CHAM_MATER supprimé sous CALC_G",
              "CALC_G_CARA_ELEM":"Mot Clef CARA_ELEM supprimé sous CALC_G",
              "CALC_G_RESULTAT=XXX,":"Mot Clef RESULTAT à completer sous CALC_G",
              "AFFE_MODELE_AFFE_MODELISATION_VALEUR":"verifier la valeur de MODELISATION",
              "STAT_NON_LINE_COMP_INCR_RELATION_VALEUR":"verifier la valeur de RELATION",
              "STAT_NON_LINE_COMP_INCR_RELATION_KIT_VALEUR":"verifier la valeur de RELATION_KIT",
              "STAT_NON_LINE_VARI_COMM":"suppression des variables de commande",
              "STAT_NON_LINE_INCREMENT_SUBD_PAS":"Si SUBD_PAS=1 il n'y a pas subdivision : le mot est clef est ote du STAT_NON_LINE",
              "DYNA_NON_LINE_COMP_INCR_RELATION_VALEUR":"verifier la valeur de RELATION",
              "DYNA_NON_LINE_COMP_INCR_RELATION_KIT_VALEUR":"verifier la valeur de RELATION_KIT",
              "DYNA_NON_LINE_VARI_COMM":"suppression des variables de commande",
              "DYNA_NON_LINE_INCREMENT_SUBD_PAS":"Si SUBD_PAS=1 il n'y a pas subdivision : le mot est clef est ote du DYNA_NON_LINE",
              "CALC_PRECONT_SUBD_PAS":"Si SUBD_PAS=1 il n'y a pas subdivision : le mot est clef est ote du CALC_PRECONT",
              "TEST_RESU_UNITE":"suppression du mot clef UNITE dans TEST_RESU",
              "POST_SIMPLIFIE":"commande POST_SIMPLIFIE supprimee",
              "POST_DYNA_ALEA_GAUSS":"la methode GAUSS a ete supprimee de POST_DYNA_ALEA",
              "POST_DYNA_ALEA_VANMARCKE":"la methode VANMARCKE a ete supprimee de POST_DYNA_ALEA",
              "POST_DYNA_ALEA_DEPASSEMENT":"la methode DEPASSEMENT a ete supprimee de POST_DYNA_ALEA",
              "POST_DYNA_ALEA_RAYLEIGH":"la methode RAYLEIGH a ete supprimee de POST_DYNA_ALEA",
              "DYNA_TRAN_MODAL_EXCIT_NUME_MODE":"le numero du mode utilise pour EXCIT DYNA_TRAN_MODAL est le numero d'ORDRE",
              "DEFI_INTERF_DYNA_INTERFACE_DDL_ACTIF":"DDL_ACTIF supprime de DEFI_INTERF_DYNA; utiliser MASQUE",
              "DEFI_TEXTURE":"le materiau POLY_CFC est remplace par le comportement POLYCRISTAL",
              "CREA_RESU_NOM_CHAM_VALEUR":"HYDR_ELGA est remplace par HYDR_ELNO_ELGA et HYDR_NOEU_ELGA",
              "COMB_CHAM_NO":"COMB_CHAM_NO est remplace par CREA_CHAMP",
              "COMB_CHAM_ELEM":"COMB_CHAM_ELEM est remplace par CREA_CHAMP",
              "IMPR_OAR":"IMPR_OAR demande un traitement manuel",
              "IMPR_FICO_HOMARD":"IMPR_FICO_HOMARD a ete integre dans MACR_ADPA_MAIL",
# STA9.2
              "POST_RCCM_SITUATION_NUME_PASSAGE":"Utilisation de NUME_PASSAGE pour le type TUYAUTERIE impossible en 9.2. On ne traite pour le moment que les chemins de passage simples.",
              "POST_RCCM_SITUATION_NB_CYCL_SEISME":"POST_RCCM : maintenant les SITUATIONS sismiques ont leur propre mot clef facteur SEISME, attention, traduction incomplete",
              "DEFI_MATERIAU_BAZANT_FD" : "le materiau BAZANT_FD a ete supprime",
              "DEFI_MATERIAU_APPUI_ELAS" : "le materiau APPUI_ELAS a ete supprime",
              "DEFI_MATERIAU_PORO_JOINT" : "le materiau PORO_JOINT a ete supprime",
              "DEFI_MATERIAU_ZIRC_CYRA2" : "le materiau ZIRC_CYRA2 a ete supprime",
              "DEFI_MATERIAU_ZIRC_EPRI" : "le materiau ZIRC_EPRI a ete supprime",
              "IMPR_MATRICE_MATR_ELEM_FORMAT=RESULTAT" : "IMPR_MATRICE au format RESULTAT a ete supprime",
              "IMPR_MATRICE_MATR_ASSE_FORMAT=RESULTAT" : "IMPR_MATRICE au format RESULTAT a ete supprime",
              "CALC_G_OPTION=G_LAGR" : "l'OPTION G_LAGR de CALC_G a ete supprimee",
              "CALC_G_OPTION=G_LAGR_GLOB" : "l'OPTION G_LAGR_GLOB de CALC_G a ete supprimee",
              "CALC_MATR_ELEM_THETA" : "l'OPTION RIGI_MECA_LAGR de CALC_MATR_ELEM a ete supprimee",
              "TEST_FICHIER_NB_CHIFFRE" : "le fonctionnement de TEST_FICHIER a change entre la V8 et la V9, consultez la doc, en particulier pour entrer la bonne valeur de NB_VALE",
              "DYNA_NON_LINE_PILOTAGE" : "le PILOTAGE n'est pas actif dans DYNA_NON_LINE ",
              "DYNA_NON_LINE_RECH_LINEAIRE" : "la RECH_LINEAIRE n'est pas active dans DYNA_NON_LINE ",
             }

def EcritErreur(listeGena,ligne=None) :
    maCle=""
    for Mot in listeGena :
        maCle=maCle+"_"+Mot
    #try :
    if ( 1 == 1) :
	maClef=maCle[1:]
        if maClef in dict_erreurs.keys() :
           if ligne != None :
	      logging.warning("ligne %d : %s ligne ",ligne,dict_erreurs[maClef])
           else :
	      logging.warning("%s",dict_erreurs[maClef])
        else :
           maCle=""
           for Mot in listeGena[:-1] :
              maCle=maCle+"_"+Mot
	   maClef=maCle[1:]
	   maClef=maCle+"_"+"VALEUR"
           if maClef in dict_erreurs.keys() :
              if ligne != None :
	          logging.warning("ligne %d : %s ligne ",ligne,dict_erreurs[maClef])
              else :
	          logging.warning("%s",dict_erreurs[maClef])
    #except :
    #    pass

def GenereErreurPourCommande(jdc,listeCommande) :
    commands= jdc.root.childNodes[:]
    commands.reverse()
    for c in commands:
        jdcSet.add(c.name) 
        for Mot in listeCommande :
           if c.name != Mot :continue
           EcritErreur((Mot,),c.lineno)

