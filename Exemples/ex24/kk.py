

SD1=DEFI_SONDE(X=2,
               Y=3,
               Z=1,);
#

#

_param_1 = 1;

_param_2 = 2 ;

_param_4 = EVAL("""23""")



##SD2=DEFI_SONDE(X=2,
##               Y=3,
##               Z=1,);

SD3=DEFI_SONDE(X=4,
               Y=5,
               Z=3,);

SD4=DEFI_SONDE(X=11,
               Y=10,
               Z=12,);

SD5=DEFI_SONDE(X=21,
               Y=21,
               Z=21,);

temperature=DEFI_SCALA(NUMERIC=_F(ICONV=1,
                                  ISTAT=1,
                                  IDIFF=1,
                                  IDIRCL=0,
                                  BLENCV=0.5,
                                  ISCHCV=1,
                                  NITMAX=1000,
                                  EPSILO=1.0000000000000001E-05,
                                  IMLIGR=1,
                                  NSWRGR=2,
                                  NSWRSM=10,
                                  CLIMGR=1.7,
                                  EPSRGR=1.E-4,),
                       RESTITUE=_F(NOMVAR='temperature',
                                   ICHRVR=1,
                                   ILISVR=1,
                                   IHISVR=SD1,),
                       MODELE=_F(VALREF=300.0,
                                 SCAMIN=270,
                                 SCAMAX=1000,
                                 SIGMAS=0.90000000000000002,
                                 VISLS0=0.050000000000000003,
                                 IVISLS=1,),);

cb=DEFI_SCALA(NUMERIC=_F(ICONV=1,
                         BLENCV=0,),
              RESTITUE=_F(NOMVAR='bore',),
              MODELE=_F(VALREF=1000.0,
                        VISLS0=0.29999999999999999,),);

CALCUL_SATURNE(ENVELOPPE=_F(IFOENV=2,
                            IMPEVI=83,
                            FICEVI='Enveloppe_vers_solveur          ',
                            IMPEVO=84,
                            FICEVO='Solveur_vers_enveloppe          ',),
               FICHIERS_CALCUL=_F(FICHIER_STOP=_F(IMPSTP=82,
                                                  FICSTP='ficstop',),
                                  SUITE_AVAL=_F(IMPAVA=70,
                                                FICAVA='sui_amo',
                                                IFOAVA=1,),),
               POST_PROC_ENSIGHT=_F(IFOENS=1,
                                    NTCHR=3,
                                    ITCHR=10,),
               HISTORIQUE_PONCTUEL=_F(FICHIERS_HISTORIQUES=_F(EMPHIS='./',
                                                              EXTHIS='histo',),
                                      NTHIST=1,
                                      NTHSAV=20,),
               OPTIONS_TURBULENCE=_F(IGRAKE=0,
                                     ISCALT=temperature,),
               MARCHE_TEMPS=_F(DTREF=1.E-3,
                               IDTVAR=2,
                               XCFMAX=0.5,),
               OPTIONS_EQUATIONS=_F(),
               VARIABLES=_F(NTLIST=2,
                            IWARNI=3,
                            MASVOL1=_F(NOMVAR='Masse_vol1',
                                       ICHRVR=0,
                                       ILISVR=1,
                                       IHISVR=SD2,),),
               GESTION_CALCUL=_F(ISUITE=0,
                                 NTPABS=100,
                                 NTMABS=1000,
                                 TTPABS=10.5,),
               CONSTANTES_PHYSIQUES=_F(GRAVITE=_F(GX=0,
                                                  GY=0,
                                                  GZ=0,),
                                       FLUIDE=_F(RO0=1000.0,
                                                 VISCL0=0.10000000000000001,
                                                 P0=1.E4,),),
               );
