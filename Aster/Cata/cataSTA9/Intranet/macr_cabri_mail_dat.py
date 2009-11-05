#@ MODIF macr_cabri_mail_dat Intranet  DATE 28/01/2008   AUTEUR PELLET J.PELLET 
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

# Donn�es pour les brides standards



# Pour ajouter une bride x:
#  D�finir un dico_bride_x comme ci-dessous puis ajoutez-le � dico_bride_std

# dictionnaire pour la description des variables
dico_var_geo = {'nbgouj':'Nombre de goujons de la jonction boulonn�e (GOUJ_N_GOUJON)',
            'dint':'Diam�tre int�rieur de la bride (BRID_D_INT)',
            'dex1':'Diam�tre ext�rieur de la conduite (TUBU_D_EXT)',
            'dex2':'Position (diam�tre) du cong� de la bride (BRID_D_CONGE)',
            'dex3':'Diam�tre de l''�paulement de la bride au niveau de l''interface d''�tanch�it� (BRID_D_EPAUL)',
            'dtrou':'Position des al�sages de la bride permettant l''introduction des goujons (BRID_P_ALESAG)',
            'dext':'Diam�tre ext�rieur de la bride (BRID_D_EXT)',
            'dt':'Diam�tre des al�sages de la bride permettant l''introduction des goujons (BRID_D_ALESAG)',
            'drd':'Diam�tre de la rondelle (GOUJ_D_RONDEL)',
            'dg':'Diam�tre des goujons de la jonction boulonn�e (GOUJ_D_GOUJON)',
            'dec':'Diam�tre de l''�crou (GOUJ_D_ECROU)',
            'rcong':'Rayon du cong� de la bride (BRID_R_CONGE)',
            'he':'Epaisseur de la rondelle (GOUJ_E_RONDEL)',
            'e':'Epaisseur de l''�crou (GOUJ_E_ECROU)',
            'hc1':'Hauteur de la bride (BRID_H)',
            'hcg1':'Hauteur de conduite (TUBU_H)',
            'hb':'Hauteur de l''�paulement de la bride au niveau de l''interface d''�tanch�it� (BRID_H_EPAUL)',
            'htrou':'Hauteur des al�sages de la bride permettant l''introduction des goujons (BRID_H_ALESAG)',
            'pf':'Profondeur (�paisseur) des filets des goujons (GOUJ_E_FILET)',
            'j':'Epaisseur du joint au niveau de l''interface d''�tanch�it� (ETAN_E_JOINT)'}

dico_var_msh = {'nrad':'Nombre d''�l�ments radiaux (NBR_RAD)',
            'ncir':'Nombre d''�l�ments circonf�rentiels (NBR_CIR)',
            'nver':'Nombre d''�l�ments verticaux (NBR_VER)',
            'nsect':'Nombre d''�l�ments de l''al�sage (NBR_ALE)',
            'temps':'Temps d''analyse'}

# dictionnaires des brides standards
dico_bride_A = {'nbgouj': 4,
                'dint':   15.76,
                'dex1':   21.3,
                'dex2':   38.,
                'dex3':   48.,
                'dtrou':  67.,
                'dext':   95.,
                'dt':     14.,
                'drd':    25.,
                'dg':     12.,
                'dec':    18.,
                'rcong':  3.,
                'he':     12.,
                'e':      2.5,
                'hc1':    46.5,
                'hcg1':   20,
                'hb':     1.5,
                'htrou':  20.,
                'pf':     1.5,
                'j':      2}

dico_bride_AA = {'nbgouj': 32,
                'dint':   336.5,
                'dex1':   355.6,
                'dex2':   395.,
                'dex3':   415.,
                'dtrou':  460.,
                'dext':   515.,
                'dt':     22.,
                'drd':    36.,
                'dg':     20.,
                'dec':    30.,
                'rcong':  5.,
                'he':     20.,
                'e':      3.,
                'hc1':    115.,
                'hcg1':   115./2.,
                'hb':     3.,
                'htrou':  47.,
                'pf':     2.2,
                'j':      2}

dico_bride_B = {'nbgouj': 4,
                'dint':   26.64,
                'dex1':   33.4,
                'dex2':   53.,
                'dex3':   63.,
                'dtrou':  88.,
                'dext':   123.,
                'dt':     16.,
                'drd':    27.,
                'dg':     14.,
                'dec':    21.,
                'rcong':  4.,
                'he':     14.,
                'e':      2.5,
                'hc1':    59.,
                'hcg1':   59./2.,
                'hb':     1.5,
                'htrou':  27.5,
                'pf':     1.7,
                'j':      2}
dico_bride_B1 = {'nbgouj': 4,
                'dint':   24.3,
                'dex1':   33.4,
                'dex2':   53.,
                'dex3':   63.,
                'dtrou':  88.,
                'dext':   123.,
                'dt':     16.,
                'drd':    27.,
                'dg':     14.,
                'dec':    21.,
                'rcong':  4.,
                'he':     14.,
                'e':      2.5,
                'hc1':    59.,
                'hcg1':   59./2.,
                'hb':     1.5,
                'htrou':  27.5,
                'pf':     1.7,
                'j':      2}
dico_bride_C = {'nbgouj': 8,
                'dint':   52.48,
                'dex1':   60.3,
                'dex2':   84.,
                'dex3':   100.,
                'dtrou':  127.,
                'dext':   165.,
                'dt':     18.,
                'drd':    30,
                'dg':     16.,
                'dec':    24.,
                'rcong':  4.,
                'he':     16.,
                'e':      3,
                'hc1':    70.,
                'hcg1':   70./2.,
                'hb':     1.5,
                'htrou':  21.,
                'pf':     1.7,
                'j':      2}
dico_bride_D = {'nbgouj': 8,
                'dint':   42.9,
                'dex1':   60.3,
                'dex2':   84.,
                'dex3':   100.,
                'dtrou':  127.,
                'dext':   165.,
                'dt':     18.,
                'drd':    30,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    87.6,
                'hcg1':   87.6/2.,
                'hb':     1.5,
                'htrou':  38.5,
                'pf':     1.7,
                'j':      2}
dico_bride_D1 = {'nbgouj': 8,
                'dint':   49.22,
                'dex1':   60.3,
                'dex2':   84.,
                'dex3':   100.,
                'dtrou':  127.,
                'dext':   165.,
                'dt':     18.,
                'drd':    30,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    87.6,
                'hcg1':   87.6/2.,
                'hb':     1.5,
                'htrou':  38.5,
                'pf':     1.7,
                'j':      2}
dico_bride_E = {'nbgouj': 8,
                'dint':   83.1,
                'dex1':   88.9,
                'dex2':   117.5,
                'dex3':   135.,
                'dtrou':  165.,
                'dext':   209.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    80.,
                'hcg1':   80./2.,
                'hb':     2.,
                'htrou':  27.,
                'pf':     1.7,
                'j':      2}
dico_bride_F = {'nbgouj': 8,
                'dint':   73.66,
                'dex1':   88.9,
                'dex2':   117.5,
                'dex3':   135.,
                'dtrou':  165.,
                'dext':   209.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    89.,
                'hcg1':   89./2.,
                'hb':     2.,
                'htrou':  36.,
                'pf':     1.7,
                'j':      2}
dico_bride_FF = {'nbgouj': 32,
                'dint':   396.99,
                'dex1':   406.4,
                'dex2':   440.,
                'dex3':   455.,
                'dtrou':  485.,
                'dext':   535.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    99.,
                'hcg1':   99./2.,
                'hb':     3.,
                'htrou':  40.,
                'pf':     1.7,
                'j':      2}
dico_bride_G = {'nbgouj': 12,
                'dint':   66.7,
                'dex1':   88.9,
                'dex2':   117.5,
                'dex3':   135.,
                'dtrou':  165.,
                'dext':   209.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    98.,
                'hcg1':   98./2.,
                'hb':     2.,
                'htrou':  45.,
                'pf':     1.7,
                'j':      2}
dico_bride_GG = {'nbgouj': 36,
                'dint':   381.,
                'dex1':   406.4,
                'dex2':   445.,
                'dex3':   460.,
                'dtrou':  495.,
                'dext':   545.,
                'dt':     22.,
                'drd':    36,
                'dg':     20.,
                'dec':    30.,
                'rcong':  5.,
                'he':     20.,
                'e':      3.,
                'hc1':    129.,
                'hcg1':   129./2.,
                'hb':     3.,
                'htrou':  63.,
                'pf':     2.2,
                'j':      2}
dico_bride_H = {'nbgouj': 12,
                'dint':   108.2,
                'dex1':   114.3,
                'dex2':   146.,
                'dex3':   157.,
                'dtrou':  190.,
                'dext':   225.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    89.,
                'hcg1':   89./2.,
                'hb':     2.,
                'htrou':  33.,
                'pf':     1.7,
                'j':      2}
dico_bride_H1 = {'nbgouj': 12,
                'dint':   102.6,
                'dex1':   114.3,
                'dex2':   146.,
                'dex3':   157.,
                'dtrou':  190.,
                'dext':   225.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    89.,
                'hcg1':   89./2.,
                'hb':     2.,
                'htrou':  33.,
                'pf':     1.7,
                'j':      2}
dico_bride_I = {'nbgouj': 18,
                'dint':   92.1,
                'dex1':   114.3,
                'dex2':   146.,
                'dex3':   160.,
                'dtrou':  200.,
                'dext':   255.,
                'dt':     20.,
                'drd':    32.,
                'dg':     18.,
                'dec':    27.,
                'rcong':  5.,
                'he':     18.,
                'e':      3.,
                'hc1':    99.,
                'hcg1':   99./2.,
                'hb':     2.,
                'htrou':  43.,
                'pf':     2.2,
                'j':      2}
dico_bride_J = {'nbgouj': 18,
                'dint':   87.34,
                'dex1':   114.3,
                'dex2':   146.,
                'dex3':   160.,
                'dtrou':  200.,
                'dext':   255.,
                'dt':     20.,
                'drd':    32.,
                'dg':     18.,
                'dec':    27.,
                'rcong':  5.,
                'he':     18.,
                'e':      3.,
                'hc1':    111.,
                'hcg1':   111./2.,
                'hb':     2.,
                'htrou':  55.,
                'pf':     2.2,
                'j':      2}
dico_bride_J1 = {'nbgouj': 18,
                'dint':   87.3,
                'dex1':   114.3,
                'dex2':   146.,
                'dex3':   160.,
                'dtrou':  200.,
                'dext':   255.,
                'dt':     22.,
                'drd':    36.,
                'dg':     20.,
                'dec':    30.,
                'rcong':  5.,
                'he':     20.,
                'e':      3.,
                'hc1':    111.,
                'hcg1':   111./2.,
                'hb':     2.,
                'htrou':  55.,
                'pf':     2.2,
                'j':      2}
dico_bride_K = {'nbgouj': 8,
                'dint':   161.5,
                'dex1':   168.3,
                'dex2':   192.,
                'dex3':   210.,
                'dtrou':  235.,
                'dext':   280.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    84.,
                'hcg1':   84./2.,
                'hb':     2.,
                'htrou':  28.,
                'pf':     1.7,
                'j':      2}
dico_bride_L = {'nbgouj': 16,
                'dint':   154.8,
                'dex1':   168.3,
                'dex2':   206.,
                'dex3':   220.,
                'dtrou':  255.,
                'dext':   317.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    96.,
                'hcg1':   96./2.,
                'hb':     2.,
                'htrou':  40.,
                'pf':     1.7,
                'j':      2}
dico_bride_L1 = {'nbgouj': 16,
                'dint':   154.8,
                'dex1':   168.3,
                'dex2':   206.,
                'dex3':   220.,
                'dtrou':  255.,
                'dext':   317.,
                'dt':     20.,
                'drd':    32.,
                'dg':     18.,
                'dec':    27.,
                'rcong':  5.,
                'he':     18.,
                'e':      3.,
                'hc1':    96.,
                'hcg1':   96./2.,
                'hb':     2.,
                'htrou':  40.,
                'pf':     2.2,
                'j':      2}
dico_bride_M = {'nbgouj': 16,
                'dint':   139.7,
                'dex1':   168.3,
                'dex2':   206.,
                'dex3':   220.,
                'dtrou':  250.,
                'dext':   290.,
                'dt':     24.,
                'drd':    40.,
                'dg':     22.,
                'dec':    32.,
                'rcong':  5.,
                'he':     22.,
                'e':      3.,
                'hc1':    135.,
                'hcg1':   135./2.,
                'hb':     3.,
                'htrou':  62.,
                'pf':     2.2,
                'j':      2}
dico_bride_N = {'nbgouj': 12,
                'dint':   131.9,
                'dex1':   168.3,
                'dex2':   220.,
                'dex3':   240.,
                'dtrou':  290.,
                'dext':   365.,
                'dt':     30.,
                'drd':    48.,
                'dg':     27.,
                'dec':    41.,
                'rcong':  5.,
                'he':     27.,
                'e':      4.,
                'hc1':    148.,
                'hcg1':   148./2.,
                'hb':     3.,
                'htrou':  75.,
                'pf':     2.6,
                'j':      2}
dico_bride_O = {'nbgouj': 12,
                'dint':   211.58,
                'dex1':   219.1,
                'dex2':   248.,
                'dex3':   260.,
                'dtrou':  292.,
                'dext':   335.,
                'dt':     20.,
                'drd':    32.,
                'dg':     18.,
                'dec':    27.,
                'rcong':  5.,
                'he':     18.,
                'e':      3.,
                'hc1':    87.,
                'hcg1':   87./2.,
                'hb':     3.,
                'htrou':  30.,
                'pf':     2.2,
                'j':      2}
dico_bride_P = {'nbgouj': 16,
                'dint':   202.74,
                'dex1':   219.1,
                'dex2':   248.,
                'dex3':   260.,
                'dtrou':  292.,
                'dext':   335.,
                'dt':     20.,
                'drd':    32,
                'dg':     18.,
                'dec':    27.,
                'rcong':  5.,
                'he':     18.,
                'e':      3.,
                'hc1':    99.,
                'hcg1':   99./2.,
                'hb':     3.,
                'htrou':  42.,
                'pf':     2.2,
                'j':      2}
dico_bride_S = {'nbgouj': 16,
                'dint':   264.62,
                'dex1':   273.,
                'dex2':   305.,
                'dex3':   315.,
                'dtrou':  350.,
                'dext':   390.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    89.,
                'hcg1':   89./2.,
                'hb':     3.,
                'htrou':  32.,
                'pf':     1.7,
                'j':      2}
dico_bride_T = {'nbgouj': 16,
                'dint':   254.56,
                'dex1':   273.,
                'dex2':   320.,
                'dex3':   340.,
                'dtrou':  385.,
                'dext':   444.,
                'dt':     27.,
                'drd':    45.,
                'dg':     24.,
                'dec':    36.,
                'rcong':  5.,
                'he':     24.,
                'e':      4.,
                'hc1':    128.,
                'hcg1':   128./2.,
                'hb':     3.,
                'htrou':  55.,
                'pf':     2.6,
                'j':      2}
dico_bride_W = {'nbgouj': 28,
                'dint':   314.76,
                'dex1':   323.9,
                'dex2':   360.,
                'dex3':   385.,
                'dtrou':  415.,
                'dext':   460.,
                'dt':     18.,
                'drd':    30.,
                'dg':     16.,
                'dec':    24.,
                'rcong':  5.,
                'he':     16.,
                'e':      3.,
                'hc1':    96.,
                'hcg1':   96./2.,
                'hb':     3.,
                'htrou':  37.,
                'pf':     1.7,
                'j':      2}


# dictionnaire pour faire le lien entre l'option de bride et les valeurs normalis�es
dico_bride_std = {'AA':dico_bride_AA,
                  'A':dico_bride_A,
                  'B':dico_bride_B,
                  'B1':dico_bride_B1,
                  'C':dico_bride_C,
                  'D':dico_bride_D,
                  'D1':dico_bride_D1,
                  'E':dico_bride_E,
                  'F':dico_bride_F,
                  'FF':dico_bride_FF,
                  'G':dico_bride_G,
                  'GG':dico_bride_GG,
                  'H':dico_bride_H,
                  'H1':dico_bride_H1,
                  'I':dico_bride_I,
                  'J':dico_bride_J,
                  'J1':dico_bride_J1,
                  'K':dico_bride_K,
                  'L':dico_bride_L,
                  'L1':dico_bride_L1,
                  'M':dico_bride_M,
                  'N':dico_bride_N,
                  'O':dico_bride_O,
                  'P':dico_bride_P,
                  'S':dico_bride_S,
                  'T':dico_bride_T,
                  'W':dico_bride_W}