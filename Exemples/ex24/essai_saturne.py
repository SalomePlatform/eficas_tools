# -*- coding: utf-8 -*-

sansnom=DEFI_SONDE(Z=45,
                   X=None,
                   Y=None,);
SD_1=DEFI_SONDE(Z=None,
                X=None,
                Y=None,);
sd1=DEFI_SONDE(Z=1.1,
               X=1.2,
               Y=1.3,);
sd2=DEFI_SONDE(Z=2.2,
               X=2.1,
               Y=2.3,);
sd3=DEFI_SONDE(Z=3.1,
               X=3.2,
               Y=3.3,);
temperature=DEFI_SCALA(RESTITUE=_F(NOMVAR='temperature',),
                       MODELE=_F(VALREF=300,
                                 VISLS0=0.1,),
                       NUMERIC=_F(ICONV=1,
                                  BLENCV=0,),);
cb=DEFI_SCALA(RESTITUE=_F(NOMVAR='bore',),
              MODELE=_F(VALREF=1000,
                        VISLS0=0.12,),
              NUMERIC=_F(ICONV=1,
                         BLENCV=0,),);
CALCUL_SATURNE(ENVELOPPE=_F(IFOENV=2,
                            FICEVI='enveloppe_vers_solveur          ',
                            IMPEVI=13,
                            IMPEVO=14,FICEVO='solveur_vers_enveloppe          ',),
               CONSTANTES_PHYSIQUES=_F(FLUIDE=_F(VISCL0=0.12,
                                                 P0=1000000.0,
                                                 RO0=995.3,),
                                       GRAVITE=_F(GX=0,GY=0,GZ=0,),),
               HISTORIQUE_PONCTUEL=_F(),
               EQUATIONS=_F(TURBULENCE=_F(ITURB=1,ISCALT=temperature,IGRAKE=0,),),
               DEFINITION_EQUATION=_F(INC_PRESSION=_F(ICONV=0,),
                                      INC_VITESSEZ=_F(ICONV=1,BLENCV=0,),
                                      INC_VITESSEY=_F(ICONV=1,BLENCV=0,),
                                      INC_VITESSEX=_F(ICONV=1,BLENCV=0,),
                                      INC_K=_F(ICONV=1,BLENCV=0,),
                                      INC_EPS=_F(ICONV=1,BLENCV=0,),),
               VARIABLES=_F(VITESSE_Z=_F(NOMVAR='Vitesse_w1',IHISVR=(sd2,sd3),),
                            VITESSE_X=_F(NOMVAR='Vitesse_u1',),
                            VITESSE_Y=_F(NOMVAR='Vitesse_v1',),
                            PRESSION=_F(NOMVAR='Pression',),
                            MASVOL1=_F(NOMVAR='Masse_vol1',),
                            E_TURB=_F(NOMVAR='Energie_1',IHISVR=sd1,),
                            V_TURB=_F(NOMVAR='Visc_turb1',),
                            D_TURB=_F(NOMVAR='Dissipation',),),
               FICHIERS_CALCUL=_F(),
               GESTION_CALCUL=_F(NTMABS=1000,ISUITE=0,),
               MARCHE_TEMPS=_F(DTREF=0.01,XCFMAX=0.5,),
               );
