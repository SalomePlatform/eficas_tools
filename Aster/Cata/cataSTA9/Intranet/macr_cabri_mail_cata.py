#@ MODIF macr_cabri_mail_cata Intranet  DATE 28/01/2008   AUTEUR PELLET J.PELLET 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2008  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY  
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY  
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR     
# (AT YOUR OPTION) ANY LATER VERSION.                                                  
#                                                                       
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT   
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF            
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU      
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.                              
#                                                                       
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE     
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,         
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.        
# ======================================================================

from Intranet.macr_cabri_mail_ops import macr_cabri_mail_ops
from Cata.cata import *

MACR_CABRI_MAIL=MACRO(nom="MACR_CABRI_MAIL",
                      op=macr_cabri_mail_ops,
                      sd_prod=maillage_sdaster,
                      fr="maillage d'une jonction boulonn�e de tuyauterie",
                      reentrant='n',
                      UIinfo={"groupes":("Outils m�tier",)},
                      EXEC_MAILLAGE = FACT(statut='o',
                        LOGICIEL      = SIMP(statut = 'o',typ='TXM',into=("GIBI2000",),),
                        UNITE_DATG    = SIMP(statut = 'f',typ='I',defaut=70,),
                        UNITE_MGIB    = SIMP(statut = 'f',typ='I',defaut=19,),
                        NIVE_GIBI     = SIMP(statut = 'f',typ='I',defaut=10,
                                          into = (3,4,5,6,7,8,9,10,11),
                                            ),
                                          ),
                      RAFF_MAILLAGE   = FACT(statut = 'd',
                        NB_RADIAL    = SIMP(statut = 'f',typ='I',defaut=2,),
                        NB_CIRCONF   = SIMP(statut = 'f',typ='I',defaut=3,),
                        NB_VERTICAL  = SIMP(statut = 'f',typ='I',defaut=6,),
                        NB_ALESAGE   = SIMP(statut = 'f',typ='I',defaut=5,),
                                          ),
                      VERI_MAIL     = FACT(statut='d',
                        VERIF         = SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),  
                        APLAT         = SIMP(statut='f',typ='R',defaut= 1.0E-3 ),  
                                          ),                                          
                      GEOM_BRID     = FACT(statut = 'o',
                        NORME         = SIMP(statut = 'o',typ='TXM',into=("OUI","NON"),),
                        b_bride_iso   = BLOC(condition = "NORME == 'OUI'",
                          TYPE           = SIMP(statut='o',typ='TXM',
                                                into=('A','AA','B','B1','C','D','D1','E','F',
                                                      'FF','G','GG','H','H1','I','J','J1',
                                                      'K','L','L1','M','N','O','P','S','T','W'), 
                                               ),
                                            ),
                        b_bride_niso  = BLOC(condition = "NORME == 'NON'",
                          TUBU_D_EXT     = SIMP(statut='o',typ='R',),
                          TUBU_H         = SIMP(statut='o',typ='R',),
                          BRID_D_EXT     = SIMP(statut='o',typ='R',),
                          BRID_D_INT     = SIMP(statut='o',typ='R',),
                          BRID_H         = SIMP(statut='o',typ='R',),
                          BRID_D_CONGE   = SIMP(statut='o',typ='R',),
                          BRID_R_CONGE   = SIMP(statut='o',typ='R',),
                          BRID_D_EPAUL   = SIMP(statut='o',typ='R',),
                          BRID_H_EPAUL   = SIMP(statut='o',typ='R',),
                          BRID_D_ALESAG  = SIMP(statut='o',typ='R',),
                          BRID_P_ALESAG  = SIMP(statut='o',typ='R',),
                          BRID_H_ALESAG  = SIMP(statut='o',typ='R',),
                          GOUJ_N_GOUJON  = SIMP(statut='o',typ='I',),
                          GOUJ_D_GOUJON  = SIMP(statut='o',typ='R',),
                          GOUJ_E_FILET   = SIMP(statut='o',typ='R',),
                          GOUJ_D_RONDEL  = SIMP(statut='o',typ='R',),
                          GOUJ_E_RONDEL  = SIMP(statut='o',typ='R',),
                          GOUJ_D_ECROU   = SIMP(statut='o',typ='R',),
                          GOUJ_E_ECROU   = SIMP(statut='o',typ='R',),
                          ETAN_E_JOINT   = SIMP(statut='o',typ='R',),
                                            ),
                                         ),
                      IMPRESSION    = FACT(statut='d',
                        UNITE          = SIMP(statut='f',typ='I'),
                        FORMAT         = SIMP(statut='f',typ='TXM',defaut="ASTER",    
                                              into=("ASTER","CASTEM","IDEAS"),
                                             ),
                        b_impr_castem = BLOC(condition = "FORMAT == 'CASTEM'",
                          NIVE_GIBI      = SIMP(statut='f',typ='I',defaut=10,into=(3,10),),
                                            ),
                        b_impr_ideas  = BLOC(condition = "FORMAT == 'IDEAS'",
                          VERSION        = SIMP(statut='f',typ='I',defaut=5,into=(4,5),),
                                            ),
                                          ),
                     );