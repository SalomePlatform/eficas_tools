# -*- coding: utf-8 -*-
# MODIF  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
# TITRE TEST DE NON REGRESSION DE L IHM EFICAS - DERIVE DE SDND102A
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# Ce cas test est gere en configuration dans la base ASTER, il sert de
# modele pour prononcer la recette de l IHM d EFICAS : l objectif est de
# pouvoir recreer ce test a l identique dans EFICAS a partir d une page
# blanche.
# On a donc essaye d y placer toutes les commandes un peu particulieres
# du langage de commandes d ASTER
#
# Il s agit en fait du test SDND102A auquel on a ajoute :
#      la definition d un parametre (VAL)
#      l inclusion d un fichier (INCLUDE)
#      une poursuite (POURSUITE)
# Il contient ainsi :
# des parametres, des formules, des macros, des mots cles facteurs repetes
# (y compris conditionnes par des regles : calc_fonction / COMB),
# des blocs  (mode_iter_simult,calc_char_seisme), un defi_valeur, un parametre.
#
#
# Il faudra y associer quelques recommandations pour la recette :
# - verifier qu en ouvrant le .com0, il demande bien a browser le .comm puis, en cascade, le .11
# - verifier qu on peut bien supprimer une commande, un mot cle simple et facteur
# - verifier les acces a la doc
#

DEBUT(CODE=_F( NOM = 'EFICA01A'),
    #  PAR_LOT='NON'
         )

MAILLAGE=LIRE_MAILLAGE( )

MAILLA2=LIRE_MAILLAGE(  UNITE=19 )

MODELE=AFFE_MODELE(  MAILLAGE=MAILLAGE,
                     AFFE=(
              _F(  PHENOMENE = 'MECANIQUE', MODELISATION = 'DIS_T',
                   GROUP_MA = 'RESSORT'),
              _F(  PHENOMENE = 'MECANIQUE', MODELISATION = 'DIS_T',
                   GROUP_NO = 'MASSES')    )
                    )

BICHOC=AFFE_MODELE(  MAILLAGE=MAILLA2,
                     AFFE=(
              _F(  PHENOMENE = 'MECANIQUE', MODELISATION = 'DIS_T',
                   GROUP_MA = 'RESSORTS'),
              _F(  PHENOMENE = 'MECANIQUE', MODELISATION = 'DIS_T',
                   GROUP_NO = ( 'MASSES1', 'MASSES2',)))
                    )

VAL = 98696.0

CARA_ELE=AFFE_CARA_ELEM(  MODELE=MODELE,
                          DISCRET=(
           _F(  CARA = 'K_T_D_L',  REPERE = 'GLOBAL', GROUP_MA = 'RESSORT',
                VALE = (VAL, 0., 0., )),
           _F(  CARA = 'M_T_D_N',  GROUP_NO = 'MASSES', VALE = 25.0))
                         )

CARA_BIC=AFFE_CARA_ELEM(  MODELE=BICHOC,
                          DISCRET=(
           _F(  CARA = 'K_T_D_L',  REPERE = 'GLOBAL', GROUP_MA = 'RESSORTS',
                VALE = (VAL, 0., 0., )),
           _F(  CARA = 'M_T_D_N',  GROUP_NO = 'MASSES1', VALE = 25.0),
           _F(  CARA = 'M_T_D_N',  GROUP_NO = 'MASSES2', VALE = 25.0))
                         )


CON_LIM=AFFE_CHAR_MECA(  MODELE=MODELE,DDL_IMPO=(
              _F(  GROUP_NO = 'ENCASTRE',  DX = 0.,  DY = 0.,  DZ = 0.),
              _F(  GROUP_NO = 'MASSES',              DY = 0.,  DZ = 0.))
                       )

CL_BICHO=AFFE_CHAR_MECA(  MODELE=BICHOC,DDL_IMPO=(
              _F(  GROUP_NO = 'ENCBICHO',     DX = 0.,  DY = 0.,  DZ = 0.),
              _F(  GROUP_NO = ( 'MASSES1', 'MASSES2',), DY = 0.,  DZ = 0.))
                       )

MACRO_MATR_ASSE(  MODELE=MODELE,
                  CHARGE=CON_LIM,
                  CARA_ELEM=CARA_ELE,
                  NUME_DDL=CO("NUMEDDL"),
                  MATR_ASSE=(
                 _F(  MATRICE = CO("RIGIDITE"),  OPTION = 'RIGI_MECA'),
                 _F(  MATRICE = CO("MASSE"),     OPTION = 'MASS_MECA'))
               )

MACRO_MATR_ASSE(  MODELE=BICHOC,
                  CHARGE=CL_BICHO,
                  CARA_ELEM=CARA_BIC,
                  NUME_DDL=CO("NUMDDLC"),
                  MATR_ASSE=(
                 _F(  MATRICE = CO("RIGI_BIC"),  OPTION = 'RIGI_MECA'),
                 _F(  MATRICE = CO("MASS_BIC"),  OPTION = 'MASS_MECA'))
               )

MODE_MEC=MODE_ITER_SIMULT(  MATR_A=RIGIDITE,   MATR_B=MASSE )

MODE_MEC=NORM_MODE(reuse=MODE_MEC,  MODE=MODE_MEC,   NORME='MASS_GENE' )

MODE_BIC=MODE_ITER_SIMULT(  MATR_A=RIGI_BIC,   MATR_B=MASS_BIC,
                  METHODE='JACOBI',
                  OPTION='SANS',
                  CALC_FREQ=_F(  OPTION = 'BANDE',  FREQ = (1., 10., ))
                            )

MODE_BIC=NORM_MODE(reuse=MODE_BIC,  MODE=MODE_BIC,   NORME='MASS_GENE' )

MODE_STA=MODE_STATIQUE(  MATR_RIGI=RIGIDITE,   MATR_MASS=MASSE,
                          MODE_STAT=_F(  TOUT = 'OUI', AVEC_CMP = 'DX') )

MSTA_BIC=MODE_STATIQUE(  MATR_RIGI=RIGI_BIC,   MATR_MASS=MASS_BIC,
                          MODE_STAT=_F(  TOUT = 'OUI', AVEC_CMP = 'DX') )


L_INST=DEFI_LIST_REEL(  DEBUT=0.,
                           INTERVALLE=_F(  JUSQU_A = 1., PAS = 0.0001) )

OMEGAA=DEFI_VALEUR( R8=EVAL("""2.*PI*10.""") )

ACCE1 = FORMULE(REEL="""(REEL:INST) = SIN(OMEGAA*INST) """)
ACCELER1=CALC_FONC_INTERP( FONCTION=ACCE1, LIST_PARA=L_INST,
                               PROL_DROITE='LINEAIRE',
                              PROL_GAUCHE='LINEAIRE',
                               NOM_RESU='ACCE'       )

ACCE2 = FORMULE(REEL="""(REEL:INST) =- SIN(OMEGAA*INST) """)
ACCELER2=CALC_FONC_INTERP( FONCTION=ACCE2, LIST_PARA=L_INST,
                               PROL_DROITE='LINEAIRE',
                              PROL_GAUCHE='LINEAIRE',
                               NOM_RESU='ACCE'       )

VITE1 = FORMULE(REEL="""(REEL:INST) =-COS(OMEGAA*INST)/OMEGAA """)
VITESSE1=CALC_FONC_INTERP( FONCTION=VITE1, LIST_PARA=L_INST,
                       PROL_DROITE='LINEAIRE',
                      PROL_GAUCHE='LINEAIRE',
                      NOM_RESU='VITE'       )

DEPL1 = FORMULE(REEL="""(REEL:INST) =-SIN(OMEGAA*INST)/(OMEGAA**2) """)
DEPLACE1=CALC_FONC_INTERP( FONCTION=DEPL1, LIST_PARA=L_INST,
                       PROL_DROITE='LINEAIRE',
                      PROL_GAUCHE='LINEAIRE',
                      NOM_RESU='DEPL'       )

VITE2 = FORMULE(REEL="""(REEL:INST) =COS(OMEGAA*INST)/OMEGAA """)
VITESSE2=CALC_FONC_INTERP( FONCTION=VITE2, LIST_PARA=L_INST,
                       PROL_DROITE='LINEAIRE',
                      PROL_GAUCHE='LINEAIRE',
                      NOM_RESU='VITE'       )

INCLUDE(   UNITE=11,   INFO=1 )

MUR=DEFI_OBSTACLE(   TYPE='PLAN_Z' )

TRAN_GE1=DYNA_TRAN_MODAL(  MASS_GENE=MASS_GEN,   RIGI_GENE=RIGI_GEN,
                METHODE='EULER',
                AMOR_REDUIT=0.07, 
                MODE_STAT=MODE_STA,
                EXCIT=_F(
                       VECT_GENE = VECT_X,
                       ACCE = ACCELER1,
                       VITE = VITESSE1,
                       DEPL = DEPLACE1,
                       MULT_APPUI = 'OUI',
                       DIRECTION = ( 1., 0., 0.,),
                       NOEUD = 'NO1'),
                CHOC=_F(  GROUP_NO_1 = 'MASSES',
                      OBSTACLE = MUR,
                      INTITULE = 'NO2/MUR',
                      ORIG_OBST = ( -1., 0., 0., ),
                      NORM_OBST = (  0., 0., 1., ),
                      JEU = 1.1005,
                      RIGI_NOR = 5.76E7,
                      AMOR_NOR = 0.,
                      RIGI_TAN = 0.,
                      COULOMB = 0.0),
                INCREMENT=_F( INST_INIT = 0.,  INST_FIN = 1.,  PAS = 0.0002),
                ARCHIVAGE=_F(  PAS_ARCH = 8)
                          )


MULT_X1=CALC_CHAR_SEISME(  MATR_MASS=MASS_BIC,  DIRECTION=( 1., 0., 0.,),
                           MODE_STAT=MSTA_BIC,  NOEUD='NO1' )

MULT_X2=CALC_CHAR_SEISME(  MATR_MASS=MASS_BIC,  DIRECTION=( 1., 0., 0.,),
                           MODE_STAT=MSTA_BIC,  NOEUD='NO11' )

MACRO_PROJ_BASE(BASE=MODE_BIC,
                MATR_ASSE_GENE=(
                _F( MATRICE = CO("MGEN_BIC"), MATR_ASSE = MASS_BIC),
                _F( MATRICE = CO("RGEN_BIC"), MATR_ASSE = RIGI_BIC)),
                VECT_ASSE_GENE=(
                _F( VECTEUR = CO("VECT_X1"),  VECT_ASSE = MULT_X1),
                _F( VECTEUR = CO("VECT_X2"),  VECT_ASSE = MULT_X2))
               )


GRILLE=DEFI_OBSTACLE(   TYPE='BI_PLAN_Z' )


FIN()
