# -*- coding: utf-8 -*-
#& MODIF COMMANDE  DATE 30/01/2002   AUTEUR VABHHTS J.TESELET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
import Accas
from Accas import *
from Accas import _F

import ops

try:
  import aster
except:
  pass

#
__version__="$Name:  $"
__Id__="$Id: cata.py,v 1.1.1.1 2002/03/26 09:08:45 eficas Exp $"
#
JdC = JDC_CATA(code='ASTER',
               execmodul=None,
               regles = (AU_MOINS_UN('DEBUT','POURSUITE'),
                         AU_MOINS_UN('FIN'),
                         A_CLASSER(('DEBUT','POURSUITE'),'FIN')))
# Type le plus general
class entier  (ASSD):pass
class reel    (ASSD):pass
class complexe(ASSD):pass
class liste   (ASSD):pass
class chaine  (ASSD):pass

# Type geometriques
class no  (GEOM):pass
class grno(GEOM):pass
class ma  (GEOM):pass
class grma(GEOM):pass



# Autres

class cabl_precont    (ASSD):pass
class cara_elem       (ASSD):pass
class cara_pout       (ASSD):pass
class cham_mater      (ASSD):pass
class char_acou       (ASSD):pass
class char_cine_acou  (ASSD):pass
class char_cine_meca  (ASSD):pass
class char_cine_ther  (ASSD):pass
class char_meca       (ASSD):pass
class char_ther       (ASSD):pass
class courbe          (ASSD):pass
class fond_fiss       (ASSD):pass
class interf_dyna_clas(ASSD):pass
class interspfact     (ASSD):pass
class listis          (ASSD):pass
class listr8          (ASSD):pass
class macr_elem_dyna  (ASSD):pass
class macr_elem_stat  (ASSD):pass
class mater           (ASSD):pass
class melasflu        (ASSD):pass
class modele          (ASSD):pass
class modele_gene     (ASSD):pass
class nume_ddl        (ASSD):pass
class nume_ddl_gene   (ASSD):pass
class obstacle        (ASSD):pass
class spectre         (ASSD):pass
class surface         (ASSD):pass
class tran_gene       (ASSD):pass
class type_flui_stru  (ASSD):pass
class valeur          (ASSD):pass

# maillage :
#--------------------------------
class maillage(ASSD):pass
class squelette     (maillage):pass


# cham_gd (carte,cham_no,cham_elem)
#--------------------------------

class cham_gd(ASSD):pass

# cham_gd/carte :
#--------------------------------
class carte(cham_gd):pass
class carte_dbel_r   (carte):pass
class carte_depl_c   (carte):pass
class carte_depl_f   (carte):pass
class carte_depl_r   (carte):pass
class carte_durt_r   (carte):pass
class carte_ener_r   (carte):pass
class carte_epsi_r   (carte):pass
class carte_erreur   (carte):pass
class carte_flux_r   (carte):pass
class carte_g_depl_r (carte):pass
class carte_geom_r   (carte):pass
class carte_hydr_r   (carte):pass
class carte_inst_r   (carte):pass
class carte_inte_r   (carte):pass
class carte_irra_r   (carte):pass
class carte_meta_r   (carte):pass
class carte_neut_f   (carte):pass
class carte_neut_r   (carte):pass
class carte_pres_r   (carte):pass
class carte_sief_r   (carte):pass
class carte_sour_r   (carte):pass
class carte_temp_f   (carte):pass
class carte_temp_r   (carte):pass
class carte_var2_r   (carte):pass
class carte_vnor_c   (carte):pass


# cham_gd/cham_elem :
#--------------------------------
class cham_elem(cham_gd):pass
class cham_elem_crit_r(cham_elem):pass
class cham_elem_dbel_r(cham_elem):pass
class cham_elem_depl_c(cham_elem):pass
class cham_elem_depl_f(cham_elem):pass
class cham_elem_depl_r(cham_elem):pass
class cham_elem_dommag(cham_elem):pass
class cham_elem_durt_r(cham_elem):pass
class cham_elem_ener_r(cham_elem):pass
class cham_elem_epsi_c(cham_elem):pass
class cham_elem_epsi_r(cham_elem):pass
class cham_elem_erreur(cham_elem):pass
class cham_elem_flux_r(cham_elem):pass
class cham_elem_g_depl(cham_elem):pass
class cham_elem_geom_r(cham_elem):pass
class cham_elem_hydr_r(cham_elem):pass
class cham_elem_inst_r(cham_elem):pass
class cham_elem_inte_r(cham_elem):pass
class cham_elem_irra_r(cham_elem):pass
class cham_elem_meta_r(cham_elem):pass
class cham_elem_neut_f(cham_elem):pass
class cham_elem_neut_r(cham_elem):pass
class cham_elem_pres_r(cham_elem):pass
class cham_elem_sief_c(cham_elem):pass
class cham_elem_sief_r(cham_elem):pass
class cham_elem_sour_r(cham_elem):pass
class cham_elem_temp_f(cham_elem):pass
class cham_elem_temp_r(cham_elem):pass
class cham_elem_vari_r(cham_elem):pass
class cham_elem_vnor_c(cham_elem):pass


# cham_gd/cham_no :
#--------------------------------
class cham_no(cham_gd):pass
class cham_no_dbel_r   (cham_no):pass
class cham_no_depl_c   (cham_no):pass
class cham_no_depl_f   (cham_no):pass
class cham_no_depl_r   (cham_no):pass
class cham_no_durt_r   (cham_no):pass
class cham_no_ener_r   (cham_no):pass
class cham_no_epsi_r   (cham_no):pass
class cham_no_erreur   (cham_no):pass
class cham_no_flux_r   (cham_no):pass
class cham_no_g_depl_r (cham_no):pass
class cham_no_geom_r   (cham_no):pass
class cham_no_hydr_r   (cham_no):pass
class cham_no_inst_r   (cham_no):pass
class cham_no_inte_r   (cham_no):pass
class cham_no_irra_r   (cham_no):pass
class cham_no_meta_r   (cham_no):pass
class cham_no_neut_f   (cham_no):pass
class cham_no_neut_r   (cham_no):pass
class cham_no_pres_c   (cham_no):pass
class cham_no_pres_r   (cham_no):pass
class cham_no_sief_r   (cham_no):pass
class cham_no_sour_r   (cham_no):pass
class cham_no_temp_c   (cham_no):pass
class cham_no_temp_f   (cham_no):pass
class cham_no_temp_r   (cham_no):pass
class cham_no_vanl_r   (cham_no):pass
class cham_no_var2_r   (cham_no):pass
class cham_no_vnor_c   (cham_no):pass


# resultat : (evol,mode_stat,mode_meca)
#--------------------------------

class resultat(ASSD):
  def __getitem__(self,key):
    return aster.getpara(self.get_name(),"RESULTAT",key[0],key[1])

class acou_harmo    (resultat):pass
class base_modale     (resultat):pass
class comb_fourier  (resultat):pass
class dyna_harmo    (resultat):pass
class dyna_trans    (resultat):pass
class fourier_elas  (resultat):pass
class harm_gene     (resultat):pass
class mode_acou     (resultat):pass
class mode_cycl     (resultat):pass
class mode_flamb    (resultat):pass
class mode_gene     (resultat):pass
class mult_elas     (resultat):pass
class theta_geom    (resultat):pass

# resultat/evol :
#--------------------------------
class evol(resultat):pass
class evol_char(evol):pass
class evol_elas(evol):pass
class evol_noli(evol):pass
class evol_ther(evol):pass
class evol_varc(evol):pass

# resultat/mode_stat :
#--------------------------------
class mode_stat(resultat):pass
class mode_stat_depl(mode_stat):pass
class mode_stat_acce(mode_stat):pass
class mode_stat_forc(mode_stat):pass


# resultat/mode_meca :
#--------------------------------
class mode_meca(resultat):pass
class mode_meca_c(mode_meca):pass


# fonction :
#--------------------------------
class para_sensi(fonction):pass
class fonction_c(fonction):pass


# matr_asse :
#--------------------------------
class matr_asse(ASSD):pass
class matr_asse_depl_c(matr_asse):pass
class matr_asse_depl_r(matr_asse):pass
class matr_asse_gene_r(matr_asse):pass
class matr_asse_gene_c(matr_asse):pass
class matr_asse_pres_c(matr_asse):pass
class matr_asse_pres_r(matr_asse):pass
class matr_asse_temp_c(matr_asse):pass
class matr_asse_temp_r(matr_asse):pass

# matr_elem :
#--------------------------------
class matr_elem(ASSD):pass
class matr_elem_depl_c(matr_elem):pass
class matr_elem_depl_r(matr_elem):pass
class matr_elem_pres_c(matr_elem):pass
class matr_elem_temp_r(matr_elem):pass




# table : (tabl_fonc)
#--------------------------------

class table(ASSD):
  def __getitem__(self,key):
    return aster.getpara(self.get_name(),"TABLE",key[0],key[1])

class tabl_aire_int   (table):pass
class tabl_calc_g_loca(table):pass
class tabl_calc_g_th  (table):pass
class tabl_cara_geom  (table):pass
class tabl_char_limite(table):pass
class tabl_ener_elas  (table):pass
class tabl_ener_pot   (table):pass
class tabl_ener_cin   (table):pass
class tabl_ener_ext   (table):pass
class tabl_ener_totale(table):pass
class tabl_indic_ener (table):pass
class tabl_indic_seuil(table):pass
class tabl_intsp      (table):pass
class tabl_mass_iner  (table):pass
class tabl_post_alea  (table):pass
class tabl_post_dyna  (table):pass
class tabl_post_f_alea(table):pass
class tabl_post_fatig (table):pass
class tabl_post_gouj2e(table):pass
class tabl_post_k     (table):pass
class tabl_post_rccm  (table):pass
class tabl_post_rele  (table):pass
class tabl_post_simpli(table):pass
class tabl_post_usur  (table):pass
class tabl_reca_weib  (table):pass
class tabl_rice_tracey(table):pass
class tabl_texture    (table):pass
class tabl_trc        (table):pass
class tabl_weibull    (table):pass

# table/tabl_fonc
#--------------------------------
class tabl_fonc       (table):pass
class tabl_fonc_max   (tabl_fonc):pass
class tabl_fonc_noci  (tabl_fonc):pass
class tabl_fonc_rms   (tabl_fonc):pass


# vect_asse :
#--------------------------------
class vect_asse(ASSD):pass
class vect_asse_gene(vect_asse):pass


# vect_elem :
#--------------------------------
class vect_elem(ASSD):pass
class vect_elem_depl_r(vect_elem):pass
class vect_elem_pres_c(vect_elem):pass
class vect_elem_pres_r(vect_elem):pass
class vect_elem_temp_r(vect_elem):pass

#& MODIF COMMANDE  DATE 22/11/2001   AUTEUR VABHHTS J.PELLET 
AFFE_CARA_ELEM=OPER(nom="AFFE_CARA_ELEM",op=  19,sd_prod=cara_elem,
                    fr="Affectation de caract�ristiques � des �l�ments de structure",
                    docu="U4.42.01-f1",reentrant='n',
         regles=(AU_MOINS_UN('POUTRE','BARRE','COQUE','CABLE','DISCRET','MASSIF',
                             'ASSE_GRIL','GRILLE','AFFE_SECT','AFFE_FIBRE'),),
         MODELE          =SIMP(statut='o',typ=modele ),
         INFO            =SIMP(statut='f',typ='I', defaut= 1 ,into=(1,2) ),
         VERIF           =SIMP(statut='f',typ='TXM',max='**',into=("MAILLE","NOEUD") ),

         POUTRE          =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           SECTION         =SIMP(statut='o',typ='TXM' ,into=("GENERALE","RECTANGLE","CERCLE") ),
           CARA_SECT       =SIMP(statut='f',typ=(cara_pout) ),
           TUYAU_NCOU      =SIMP(statut='f',typ='I',min=1,max=10,defaut=3),
           TUYAU_NSEC      =SIMP(statut='f',typ='I',min=1,max=32,defaut=16),
           b_generale      =BLOC( condition = "SECTION=='GENERALE'",
             CARA            =SIMP(statut='o',typ='TXM',max='**',
                                 into=("A","IY","IZ","AY","AZ","EY","EZ","JX","RY","RZ","RT",
                                                           "AI","JG","IYR2","IZR2","A1",
                                       "IY1","IZ1","AY1","AZ1","EY1","EZ1","JX1","RY1",
                                       "RZ1","RT1","AI1","JG1","IYR21","IZR21","A2",
                                       "IY2","IZ2","AY2","AZ2","EY2","EZ2","JX2","RY2",
                                       "RZ2","RT2","AI2","JG2","IYR22","IZR22","H",
                                       "HZ","HY","EP","EPY","EPZ","H1","HZ1","HY1",
                                       "EP1","EPY1","EPZ1","H2","HZ2","HY2","EP2",
                                       "EPY2","EPZ2","R","R1","R2") ),
             VALE            =SIMP(statut='o',typ='R',max='**'),
             VARI_SECT       =SIMP(statut='f',typ='TXM',into=("HOMOTHETIQUE",) ),
           ),
           b_rectangle     =BLOC( condition = "SECTION=='RECTANGLE'",
             CARA            =SIMP(statut='o',typ='TXM',max='**',
                                 into=("H","EP","HY","HZ","EPY","EPZ",
                                                           "H1","HZ1","HY1","EP1","EPY1","EPZ1",
                                                           "H2","HZ2","HY2","EP2","EPY2","EPZ2") ),
             VALE            =SIMP(statut='o',typ='R',max='**'),
             VARI_SECT       =SIMP(statut='f',typ='TXM',into=("HOMOTHETIQUE","AFFINE"),defaut="HOMOTHETIQUE"),
           ),
           b_cercle        =BLOC( condition = "SECTION=='CERCLE'",
             CARA            =SIMP(statut='o',typ='TXM',max='**',
                                 into=("R","EP","R1","R2","EP1","EP2") ),
             VALE            =SIMP(statut='o',typ='R',max='**'),
             VARI_SECT       =SIMP(statut='f',typ='TXM',into=("HOMOTHETIQUE",) ),
             MODI_METRIQUE   =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           ),
           FCX             =SIMP(statut='f',typ=(fonction) ),
         ),

         BARRE           =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           SECTION         =SIMP(statut='o',typ='TXM',into=("GENERALE","RECTANGLE","CERCLE") ),
           b_generale      =BLOC( condition = "SECTION=='GENERALE'",
             CARA            =SIMP(statut='o',typ='TXM',into=("A",) ),
             VALE            =SIMP(statut='o',typ='R' ),
           ),
           b_rectangle     =BLOC( condition = "SECTION=='RECTANGLE'",
             CARA            =SIMP(statut='o',typ='TXM',into=("H","HZ","HY","EPY","EPZ","EP"),max=6 ),
             VALE            =SIMP(statut='o',typ='R',max=6 ),
           ),
           b_cercle        =BLOC( condition = "SECTION=='CERCLE'",
             CARA            =SIMP(statut='o',typ='TXM',max=2,into=("R","EP") ),
             VALE            =SIMP(statut='o',typ='R',max=2 ),
           ),
           FCX             =SIMP(statut='f',typ=(fonction) ),
         ),

         COQUE           =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA' ),
                   PRESENT_PRESENT( 'EXCENTREMENT','INER_ROTA' ),),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           EPAIS           =SIMP(statut='o',typ='R' ),
           ANGL_REP        =SIMP(statut='f',typ='R',min=2,max=2),
           A_CIS           =SIMP(statut='f',typ='R',defaut= 0.8333333E0),
           COEF_RIGI_DRZ   =SIMP(statut='f',typ='R',defaut= 1.0E-5 ),
           COQUE_NCOU      =SIMP(statut='f',typ='I',defaut= 1 ),
           EXCENTREMENT    =SIMP(statut='f',typ='R' ),
           INER_ROTA       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MODI_METRIQUE   =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         ),

         CABLE           =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),
                   UN_PARMI('A','SECTION') ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           N_INIT          =SIMP(statut='f',typ='R',defaut= 5000. ),
           A               =SIMP(statut='f',typ='R' ),
           SECTION         =SIMP(statut='f',typ='R' ),
           FCX             =SIMP(statut='f',typ=(fonction) ),
         ),

         DISCRET         =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA','NOEUD','GROUP_NO'),),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           REPERE          =SIMP(statut='f',typ='TXM',into=("LOCAL","GLOBAL") ),
           AMOR_HYST       =SIMP(statut='f',typ='R' ),
           CARA            =SIMP(statut='o',typ='TXM',max='**',
                                 into=("K_T_D_N","K_T_D_L","K_TR_D_N","K_TR_D_L",
                                                           "K_T_N",  "K_T_L",  "K_TR_N",  "K_TR_L",
                                                                "M_T_D_N","M_TR_D_N","M_T_N",
                                                           "M_T_L",  "M_TR_N",  "M_TR_L",
                                       "A_T_D_N","A_TR_D_N","A_T_D_L","A_TR_D_L",
                                                           "A_T_N",  "A_T_L",   "A_TR_N", "A_TR_L") ),
           VALE            =SIMP(statut='o',typ='R',max='**'),
         ),

         ORIENTATION     =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA','NOEUD','GROUP_NO' ),),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           CARA            =SIMP(statut='o',typ='TXM',
                                 into=("VECT_Y","ANGL_VRIL","VECT_X_Y","ANGL_NAUT","GENE_TUYAU") ),
           VALE            =SIMP(statut='o',typ='R',max='**'),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-4 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
         ),

         DEFI_ARC        =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),
                   UN_PARMI('ORIE_ARC','CENTRE','NOEUD_CENTRE','GROUP_NO_CENTRE',
                            'POIN_TANG','NOEUD_POIN_TANG','GROUP_NO_POIN_TG'),
                   PRESENT_PRESENT('ORIE_ARC','RAYON'),
                   EXCLUS('COEF_FLEX','COEF_FLEX_XY'),
                   EXCLUS('COEF_FLEX','COEF_FLEX_XZ'),
                   EXCLUS('INDI_SIGM','INDI_SIGM_XY'),
                   EXCLUS('INDI_SIGM','INDI_SIGM_XZ'),
                   PRESENT_PRESENT('COEF_FLEX_XY','COEF_FLEX_XZ'),
                   PRESENT_PRESENT('INDI_SIGM_XY','INDI_SIGM_XZ'),),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           ORIE_ARC        =SIMP(statut='f',typ='R'),
           CENTRE          =SIMP(statut='f',typ='R',max='**'),
           NOEUD_CENTRE    =SIMP(statut='f',typ=no,max=1),
           GROUP_NO_CENTRE =SIMP(statut='f',typ=grno,max=1),
           POIN_TANG       =SIMP(statut='f',typ='R',max='**'),
           NOEUD_POIN_TANG =SIMP(statut='f',typ=no,max=1),
           GROUP_NO_POIN_TG=SIMP(statut='f',typ=grno,max=1),
           RAYON           =SIMP(statut='f',typ='R'),
           COEF_FLEX       =SIMP(statut='f',typ='R'),
           INDI_SIGM       =SIMP(statut='f',typ='R'),
           COEF_FLEX_XY    =SIMP(statut='f',typ='R'),
           INDI_SIGM_XY    =SIMP(statut='f',typ='R'),
           COEF_FLEX_XZ    =SIMP(statut='f',typ='R'),
           INDI_SIGM_XZ    =SIMP(statut='f',typ='R'),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
         ),

         MASSIF          =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),
                   UN_PARMI('ANGL_REP','ANGL_AXE'),
                   EXCLUS('ANGL_REP','ANGL_AXE'),
                   EXCLUS('ANGL_REP','ORIG_AXE'),
                   PRESENT_PRESENT('ANGL_AXE','ORIG_AXE'), ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           ANGL_REP        =SIMP(statut='f',typ='R',max=3),
           ANGL_AXE        =SIMP(statut='f',typ='R',max=2),
           ORIG_AXE        =SIMP(statut='f',typ='R',max=3),
         ),

         POUTRE_FLUI     =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           B_T             =SIMP(statut='o',typ='R'),
           B_N             =SIMP(statut='o',typ='R'),
           B_TN            =SIMP(statut='o',typ='R',defaut= 0.E+0 ),
           A_FLUI          =SIMP(statut='o',typ='R'),
           A_CELL          =SIMP(statut='o',typ='R'),
           COEF_ECHELLE    =SIMP(statut='o',typ='R'),
         ),

         GRILLE          =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),
                   EXCLUS('ANGL_REP','ORIG_AXE'),
                   EXCLUS('EXCENTREMENT','DIST_N'),
                   ENSEMBLE('ORIG_AXE','AXE')),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           SECTION_L       =SIMP(statut='o',typ='R'),
           ANGL_REP        =SIMP(statut='f',typ='R',max=2),
           ANGL_L          =SIMP(statut='f',typ='R'),
           POUR_CENT_L     =SIMP(statut='f',typ='R'),
           POUR_CENT_T     =SIMP(statut='f',typ='R'),
           DIST_N          =SIMP(statut='f',typ='R'),
           EXCENTREMENT    =SIMP(statut='f',typ='R'),
           ORIG_AXE        =SIMP(statut='f',typ='R',max='**'),
           AXE             =SIMP(statut='f',typ='R',max='**'),
           COEF_RIGI_DRZ   =SIMP(statut='f',typ='R',defaut= 1.0E-10 ),
           GRILLE_NCOU     =SIMP(statut='f',typ='I',defaut= 1,min=1,max=1 ),
         ),

         RIGI_PARASOL    =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('COEF_GROUP','FONC_GROUP'),
                   UN_PARMI('COOR_CENTRE','NOEUD_CENTRE','GROUP_NO_CENTRE'),),
           GROUP_MA        =SIMP(statut='o',typ=ma,max='**'),
           FONC_GROUP      =SIMP(statut='f',typ=(fonction) ),
           COEF_GROUP      =SIMP(statut='f',typ='R',max='**'),
           REPERE          =SIMP(statut='f',typ='TXM',into=("LOCAL","GLOBAL") ),
           CARA            =SIMP(statut='o',typ='TXM',max='**',into=("K_TR_D_N","A_TR_D_N") ),
           VALE            =SIMP(statut='o',typ='R',max='**'),
           GROUP_NO_CENTRE =SIMP(statut='f',typ=grno),
           NOEUD_CENTRE    =SIMP(statut='f',typ=no),
           COOR_CENTRE     =SIMP(statut='f',typ='R',max='**'),
         ),

         ASSE_GRIL       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           CARA            =SIMP(statut='o',typ='TXM',max='**',
                                 into=("K_TR_D_N","K_TR_D_L_T","K_TR_D_L_N",) ),
           VALE            =SIMP(statut='o',typ='R',max='**'),
           PAS_T           =SIMP(statut='o',typ='R'),
           PAS_N           =SIMP(statut='o',typ='R'),
           ANGL_REP        =SIMP(statut='o',typ='R',max='**'),
           COEF_ECHELLE    =SIMP(statut='o',typ='R'),
         ),


         AFFE_SECT     =FACT(statut='f',min=1,max='**',
              regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),
                      AU_MOINS_UN('TOUT_SECT','GROUP_MA_SECT','MAILLE_SECT'),
                      PRESENT_ABSENT('TOUT_SECT','GROUP_MA_SECT','MAILLE_SECT'),),

              GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
              MAILLE          =SIMP(statut='f',typ=ma,max='**'),

              TOUT_SECT         =SIMP(statut='f',typ='TXM',into=("OUI",) ),
              GROUP_MA_SECT     =SIMP(statut='f',typ=grma,max='**'),
              MAILLE_SECT       =SIMP(statut='f',typ=ma,max='**'),

              MAILLAGE_SECT     =SIMP(statut='o',typ=maillage),
              COOR_AXE_POUTRE    =SIMP(statut='o',typ='R',min=2,max=2),
         ),


         AFFE_FIBRE     =FACT(statut='f',min=1,max='**',
              regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),),

              GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
              MAILLE          =SIMP(statut='f',typ=ma,max='**'),

              CARA              =SIMP(statut='f',typ='TXM',defaut='SURFACE',into=('SURFACE','DIAMETRE',)),
              VALE              =SIMP(statut='o',typ='R',max='**'),
              COOR_AXE_POUTRE    =SIMP(statut='o',typ='R',min=2,max=2),
         ),


) ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
AFFE_CHAR_ACOU=OPER(nom="AFFE_CHAR_ACOU",op=  68,sd_prod=char_acou,
                    fr="Affectation de charges et conditions aux limites acoustiques constantes",
                    docu="U4.44.04-e",reentrant='n',
         regles=(AU_MOINS_UN('PRES_IMPO','VITE_FACE','IMPE_FACE','LIAISON_UNIF' ),),
         MODELE          =SIMP(statut='o',typ=modele ),
         VERI_DDL        =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         PRES_IMPO       =FACT(statut='f',min=01,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE','GROUP_NO','NOEUD'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           PRES            =SIMP(statut='o',typ='C' ),
         ),
         VITE_FACE       =FACT(statut='f',min=01,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           VNOR            =SIMP(statut='o',typ='C' ),
         ),
         IMPE_FACE       =FACT(statut='f',min=01,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           IMPE            =SIMP(statut='o',typ='C' ),
         ),
         LIAISON_UNIF    =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE' ),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           DDL             =SIMP(statut='o',typ='TXM',max='**'),
         ),
)  ;
#& MODIF COMMANDE  DATE 21/06/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def affe_char_cine_prod(MECA_IMPO,THER_IMPO,ACOU_IMPO,**args):
  if MECA_IMPO != None  : return char_cine_meca
  if THER_IMPO != None  : return char_cine_ther
  if ACOU_IMPO != None  : return char_cine_acou
  raise AsException("type de concept resultat non prevu")

AFFE_CHAR_CINE=OPER(nom="AFFE_CHAR_CINE",op= 101,sd_prod=affe_char_cine_prod
                    ,fr="Affectation de conditions aux limites cin�matiques pour traitement sans dualisation",
                     docu="U4.44.03-e",reentrant='n',
         regles=(AU_MOINS_UN('MECA_IMPO','THER_IMPO','ACOU_IMPO'),
                 EXCLUS('MECA_IMPO','THER_IMPO'),
                 EXCLUS('MECA_IMPO','ACOU_IMPO'),
                 EXCLUS('THER_IMPO','ACOU_IMPO'),),
         MODELE          =SIMP(statut='o',typ=modele ),
         MECA_IMPO       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_NO','NOEUD'),
                   AU_MOINS_UN('DX','DY','DZ','DRX','DRY','DRZ','GRX','PRES','TEMP','PHI'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           DX              =SIMP(statut='f',typ='R' ),
           DY              =SIMP(statut='f',typ='R' ),
           DZ              =SIMP(statut='f',typ='R' ),
           DRX             =SIMP(statut='f',typ='R' ),
           DRY             =SIMP(statut='f',typ='R' ),
           DRZ             =SIMP(statut='f',typ='R' ),
           GRX             =SIMP(statut='f',typ='R' ),
           PRES            =SIMP(statut='f',typ='R' ),
           TEMP            =SIMP(statut='f',typ='R' ),
           PHI             =SIMP(statut='f',typ='R' ),
         ),
         THER_IMPO       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_NO','NOEUD'),
                   AU_MOINS_UN('TEMP','TEMP_INF','TEMP_SUP'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           TEMP_SUP        =SIMP(statut='f',typ='R' ),
           TEMP            =SIMP(statut='f',typ='R' ),
           TEMP_INF        =SIMP(statut='f',typ='R' ),
         ),
         ACOU_IMPO       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_NO','NOEUD' ),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           PRES            =SIMP(statut='o',typ='C' ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def affe_char_cine_f_prod(MECA_IMPO,THER_IMPO,**args):
  if MECA_IMPO != None  : return char_cine_meca
  if THER_IMPO != None  : return char_cine_ther
  raise AsException("type de concept resultat non prevu")

AFFE_CHAR_CINE_F=OPER(nom="AFFE_CHAR_CINE_F",op= 108,sd_prod=affe_char_cine_f_prod
                    ,fr="Affectation de conditions aux limites cin�matiques pour traitement sans dualisation",
                     docu="U4.44.03-e",reentrant='n',
         regles=(AU_MOINS_UN('MECA_IMPO','THER_IMPO'),
                 EXCLUS('MECA_IMPO','THER_IMPO'),),
         MODELE          =SIMP(statut='o',typ=modele ),
         MECA_IMPO       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_NO','NOEUD'),
                   AU_MOINS_UN('DX','DY','DZ','DRX','DRY','DRZ','GRX','PRES','TEMP','PHI'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           DX              =SIMP(statut='f',typ=fonction ),
           DY              =SIMP(statut='f',typ=fonction ),
           DZ              =SIMP(statut='f',typ=fonction ),
           DRX             =SIMP(statut='f',typ=fonction ),
           DRY             =SIMP(statut='f',typ=fonction ),
           DRZ             =SIMP(statut='f',typ=fonction ),
           GRX             =SIMP(statut='f',typ=fonction ),
           PRES            =SIMP(statut='f',typ=fonction ),
           TEMP            =SIMP(statut='f',typ=fonction ),
           PHI             =SIMP(statut='f',typ=fonction ),
         ),
         THER_IMPO       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_NO','NOEUD'),
                   AU_MOINS_UN('TEMP','TEMP_INF','TEMP_SUP' ),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           TEMP_SUP        =SIMP(statut='f',typ=fonction ),
           TEMP            =SIMP(statut='f',typ=fonction ),
           TEMP_INF        =SIMP(statut='f',typ=fonction ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 24/01/2002   AUTEUR SMICHEL S.MICHEL-PONNELLE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
AFFE_CHAR_MECA=OPER(nom="AFFE_CHAR_MECA",op=   7,sd_prod=char_meca
                    ,fr="Affectation de charges et conditions aux limites m�caniques constantes",
                     docu="U4.44.01-f1",reentrant='n',
         regles=(AU_MOINS_UN('DDL_IMPO','FACE_IMPO','LIAISON_DDL','FORCE_NODALE',  
                             'FORCE_FACE','FORCE_ARETE','FORCE_CONTOUR','FORCE_INTERNE',       
                             'PRES_REP','FORCE_POUTRE','FORCE_COQUE','LIAISON_OBLIQUE',        
                             'FORCE_ELEC','INTE_ELEC','PESANTEUR','ROTATION','IMPE_FACE',      
                             'VITE_FACE','TEMP_CALCULEE','RELA_CINE_BP','EPSI_INIT','CONTACT', 
                             'LIAISON_UNIL_NO','LIAISON_GROUP','LIAISON_UNIF','FLUX_THM_REP',  
                             'LIAISON_SOLIDE','LIAISON_ELEM','ONDE_FLUI','PRES_CALCULEE',      
                             'EPSA_CALCULEE','LIAISON_CHAMNO','VECT_ASSE','LIAISON_COQUE',     
                             'LIAISON_MAIL','FORCE_TUYAU','SECH_CALCULEE','HYDR_CALCULEE',     
                             'EFFE_FOND','EVOL_CHAR','ARLEQUIN'),
                 EXCLUS('PRES_CALCULEE','EVOL_CHAR'),
                 EXCLUS('LIAISON_UNIL_NO','CONTACT'),),            
         
         MODELE          =SIMP(statut='o',typ=(modele) ),
         VERI_DDL        =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         VERI_NORM       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
#    A TERME PRES_CALCULEE N'EXISTERA PLUS
         EVOL_CHAR       =SIMP(statut='f',fr="Champ de pression issu d'un autre calcul",
                               typ=evol_char ),
         PRES_CALCULEE   =SIMP(statut='f',fr="Champ de pression issu d'un autre calcul",
                               typ=evol_char ),
         TEMP_CALCULEE   =SIMP(statut='f',fr="Champ de temp�rature issu d'un autre calcul",
                               typ=(evol_ther,cham_no_temp_r,carte_temp_r,carte_temp_f ) ),
         HYDR_CALCULEE   =SIMP(statut='f',fr="Champ d hydratation issu d'un autre calcul",
                               typ=evol_ther ),
         SECH_CALCULEE   =SIMP(statut='f',fr="Champ de s�chage issu d'un autre calcul",
                               typ=(evol_ther,cham_no_temp_r,carte_temp_r,carte_temp_f ) ),
         EPSA_CALCULEE   =SIMP(statut='f',fr="Champ de d�formation an�lastique issu d'un autre calcul",
                               typ=evol_noli ),
         VECT_ASSE       =SIMP(statut='f',typ=cham_no_depl_r ),
         
         ARLEQUIN        =FACT(statut='f',min=1,max='**',
           GROUP_MA_1     =SIMP(statut='o',typ=grma,max='**'),
           GROUP_MA_2     =SIMP(statut='o',typ=grma,max='**'),
           GROUP_MA_COLL  =SIMP(statut='o',typ=grma,max='**'),
           regles        =(UN_PARMI('POIDS_1','POIDS_2'),),
           POIDS_1       =SIMP(statut='f',typ='R'),
           POIDS_2       =SIMP(statut='f',typ='R'),
         ),

         CONTACT         =FACT(statut='f',fr="Imposer du contact avec ou sans frottement",min=1,max='**',
           regles=(UN_PARMI('GROUP_MA_2','MAILLE_2'),),
           APPARIEMENT     =SIMP(statut='f',typ='TXM',defaut="MAIT_ESCL",
                                 into=("NON","NODAL","NODAL_SYME","MAIT_ESCL","MAIT_ESCL_SYME")),
           RECHERCHE       =SIMP(statut='f',typ='TXM',defaut="NOEUD_VOISIN",into=("NOEUD_BOUCLE","NOEUD_VOISIN")),
           LISSAGE         =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),                 
           NORMALE         =SIMP(statut='f',typ='TXM',defaut="MAIT",into=("MAIT","MAIT_ESCL")),
           METHODE         =SIMP(statut='f',typ='TXM',defaut="CONTRAINTE",    
                                 into=("CONTRAINTE","LAGRANGIEN","PENALISATION","CONTINUE") ),           
           PROJECTION      =SIMP(statut='f',typ='TXM',defaut="LINEAIRE",into=("LINEAIRE",) ),
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
           b_active        =BLOC(condition = "METHODE == 'CONTRAINTE' ",
                                 fr="Param�tres de la m�thode des contraintes actives (contact uniquement)",
                regles=(EXCLUS('DIST_2','COEF_IMPO'),
                        EXCLUS('DIST_1','COEF_IMPO'),),
                NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL","PRES","TEMP")),
                FROTTEMENT      =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SANS",) ), 
                REAC_GEOM_INTE  =SIMP(statut='f',typ='I',defaut= 2),
                SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'),
                SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
                COEF_IMPO       =SIMP(statut='f',typ='R'),
                COEF_MULT_2     =SIMP(statut='f',typ='R'),
                VECT_NORM_2     =SIMP(statut='f',typ='R',max=3),
                DIST_1          =SIMP(statut='f',typ='R'),
                DIST_2          =SIMP(statut='f',typ='R'),),
           b_lagrangien    =BLOC(condition = "METHODE == 'LAGRANGIEN' ",
                                 fr="Param�tres de la m�thode Lagrangienne (contact avec ou sans frottement)",
                NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL",)),
                FROTTEMENT      =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SANS","COULOMB",) ), 
                REAC_GEOM_INTE  =SIMP(statut='f',typ='I',defaut= 2),
                SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'),
                SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
                DIST_1          =SIMP(statut='f',typ='R'),
                DIST_2          =SIMP(statut='f',typ='R'),
                b_frottement    =BLOC(condition = "FROTTEMENT == 'COULOMB' ",fr="Param�tres du frottement de Coulomb",
                     COULOMB         =SIMP(statut='o',typ='R',max=1),
                     COEF_MATR_FROT  =SIMP(statut='f',typ='R',defaut=0.E+0),  
                     VECT_Y          =SIMP(statut='f',typ='R',min=3,max=3),),),
           b_penalisation       =BLOC(condition = "METHODE == 'PENALISATION' ",
                                      fr="Param�tres de la m�thode p�nalis�e (contact avec ou sans frottement)",
                NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL",)),
                E_N             =SIMP(statut='f',typ='R'), 
                FROTTEMENT      =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SANS","COULOMB",) ), 
                REAC_GEOM_INTE  =SIMP(statut='f',typ='I',defaut= 2),
                SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'),
                SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
                DIST_1          =SIMP(statut='f',typ='R'),
                DIST_2          =SIMP(statut='f',typ='R'),
                b_frottement    =BLOC(condition = "FROTTEMENT == 'COULOMB' ",fr="Param�tres du frottement de Coulomb",
                     COULOMB         =SIMP(statut='o',typ='R',max=1),
                     E_T             =SIMP(statut='f',typ='R',
                                           fr="Active la p�nalisation sur le frottement et d�finit le coefficient de p�nalisation"),
                     COEF_MATR_FROT  =SIMP(statut='f',typ='R',defaut=0.E+0),  
                     VECT_Y          =SIMP(statut='f',typ='R',min=3,max=3),),),
           b_continue      =BLOC(condition = "METHODE == 'CONTINUE' ",
                                 fr="Param�tres de la m�thode continue (contact avec ou sans frottement)",
                NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL",)),
                FROTTEMENT      =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SANS","COULOMB",) ), 
                INTEGRATION     =SIMP(statut='f',typ='TXM',defaut="NOEUD",into=("GAUSS","NOEUD")),
                COEF_REGU_CONT  =SIMP(statut='f',typ='R',defaut=100.E+0),
                MODL_AXIS       =SIMP(statut='o',typ='TXM',into=("OUI","NON")),
                ITER_GEOM_MAXI  =SIMP(statut='f',typ='I',defaut=2),
                ITER_CONT_MAXI  =SIMP(statut='f',typ='I',defaut=30),
                b_frottement    =BLOC(condition = "FROTTEMENT == 'COULOMB' ",fr="Param�tres du frottement de Coulomb",
                     COULOMB         =SIMP(statut='o',typ='R',max=1),
                     ITER_FROT_MAXI  =SIMP(statut='f',typ='I',defaut=2),
                     COEF_REGU_FROT  =SIMP(statut='f',typ='R',defaut=100.E+0),
                     SEUIL_INIT      =SIMP(statut='f',typ='I',defaut=0),),),
         ),

        DDL_IMPO        =FACT(statut='f',min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE','GROUP_NO','NOEUD'),
                     AU_MOINS_UN('DX','DY','DZ','DRX','DRY','DRZ','GRX','PRES','PHI',
                                 'TEMP','PRE1','PRE2','UI2','UI3','VI2','VI3','WI2','WI3','UO2',
                                 'UO3','VO2','VO3','WO2','WO3','UI4','UI5','VI4','VI5','WI4',
                                 'WI5','UO4','UO5','VO4','VO5','WO4','WO5','UI6','UO6','VI6',
                                 'VO6','WI6','WO6','WO','WI1','WO1','GONF'),),
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             DX              =SIMP(statut='f',typ='R' ),
             DY              =SIMP(statut='f',typ='R' ),
             DZ              =SIMP(statut='f',typ='R' ),
             DRX             =SIMP(statut='f',typ='R' ),
             DRY             =SIMP(statut='f',typ='R' ),
             DRZ             =SIMP(statut='f',typ='R' ),
             GRX             =SIMP(statut='f',typ='R' ),
             PRES            =SIMP(statut='f',typ='R' ),
             PHI             =SIMP(statut='f',typ='R' ),
             TEMP            =SIMP(statut='f',typ='R' ),
             PRE1            =SIMP(statut='f',typ='R' ),
             PRE2            =SIMP(statut='f',typ='R' ),
             UI2             =SIMP(statut='f',typ='R' ),
             UI3             =SIMP(statut='f',typ='R' ),
             UI4             =SIMP(statut='f',typ='R' ),
             UI5             =SIMP(statut='f',typ='R' ),
             UI6             =SIMP(statut='f',typ='R' ),
             UO2             =SIMP(statut='f',typ='R' ),
             UO3             =SIMP(statut='f',typ='R' ),
             UO4             =SIMP(statut='f',typ='R' ),
             UO5             =SIMP(statut='f',typ='R' ),
             UO6             =SIMP(statut='f',typ='R' ),
             VI2             =SIMP(statut='f',typ='R' ),
             VI3             =SIMP(statut='f',typ='R' ),
             VI4             =SIMP(statut='f',typ='R' ),
             VI5             =SIMP(statut='f',typ='R' ),
             VI6             =SIMP(statut='f',typ='R' ),
             VO2             =SIMP(statut='f',typ='R' ),
             VO3             =SIMP(statut='f',typ='R' ),
             VO4             =SIMP(statut='f',typ='R' ),
             VO5             =SIMP(statut='f',typ='R' ),
             VO6             =SIMP(statut='f',typ='R' ),
             WI2             =SIMP(statut='f',typ='R' ),
             WI3             =SIMP(statut='f',typ='R' ),
             WI4             =SIMP(statut='f',typ='R' ),
             WI5             =SIMP(statut='f',typ='R' ),
             WI6             =SIMP(statut='f',typ='R' ),
             WO2             =SIMP(statut='f',typ='R' ),
             WO3             =SIMP(statut='f',typ='R' ),
             WO4             =SIMP(statut='f',typ='R' ),
             WO5             =SIMP(statut='f',typ='R' ),
             WO6             =SIMP(statut='f',typ='R' ),
             WO              =SIMP(statut='f',typ='R' ),
             WI1             =SIMP(statut='f',typ='R' ),
             WO1             =SIMP(statut='f',typ='R' ),
             GONF            =SIMP(statut='f',typ='R' ),
           ),

         EFFE_FOND       =FACT(statut='f',fr="Imposer un effet de fond",min=1,max='**',
           regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),),
           GROUP_MA_INT    =SIMP(statut='o',typ=grma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           PRES            =SIMP(statut='o',typ='R' ),
         ),
         
         EPSI_INIT       =FACT(statut='f',fr="Appliquer un chargement de d�formation initiale � un volume 3D ou 2D",
                                 min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                     AU_MOINS_UN('EPXX','EPYY','EPZZ','EPXY','EPXZ','EPYZ','EPX',
                                 'KY','KZ','EXX','EYY','EXY','KXX','KYY','KXY'),),
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             EPXX            =SIMP(statut='f',typ='R' ),
             EPYY            =SIMP(statut='f',typ='R' ),
             EPZZ            =SIMP(statut='f',typ='R' ),
             EPXY            =SIMP(statut='f',typ='R' ),
             EPXZ            =SIMP(statut='f',typ='R' ),
             EPYZ            =SIMP(statut='f',typ='R' ),
             EPX             =SIMP(statut='f',typ='R' ),
             KY              =SIMP(statut='f',typ='R' ),
             KZ              =SIMP(statut='f',typ='R' ),
             EXX             =SIMP(statut='f',typ='R' ),
             EYY             =SIMP(statut='f',typ='R' ),
             EXY             =SIMP(statut='f',typ='R' ),
             KXX             =SIMP(statut='f',typ='R' ),
             KYY             =SIMP(statut='f',typ='R' ),
             KXY             =SIMP(statut='f',typ='R' ),
           ),
         
           FACE_IMPO       =FACT(statut='f',min=1,max='**',
             regles=(UN_PARMI('GROUP_MA','MAILLE',),
                     AU_MOINS_UN('DX','DY','DZ','DRX','DRY','DRZ','GRX','PRES','PHI',
                                 'TEMP','PRE1','PRE2','DNOR','DTAN'),
                     EXCLUS('DNOR','DX'),
                     EXCLUS('DNOR','DY'),
                     EXCLUS('DNOR','DZ'),
                     EXCLUS('DNOR','DRX'),
                     EXCLUS('DNOR','DRY'),
                     EXCLUS('DNOR','DRZ'),
                     EXCLUS('DTAN','DX'),
                     EXCLUS('DTAN','DY'),
                     EXCLUS('DTAN','DZ'),
                     EXCLUS('DTAN','DRX'),
                     EXCLUS('DTAN','DRY'),
                     EXCLUS('DTAN','DRZ'),),
#  rajout d'un mot cl� REPERE :/ LOCAL /GLOBAL                     
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             DX              =SIMP(statut='f',typ='R' ),
             DY              =SIMP(statut='f',typ='R' ),
             DZ              =SIMP(statut='f',typ='R' ),
             DRX             =SIMP(statut='f',typ='R' ),
             DRY             =SIMP(statut='f',typ='R' ),
             DRZ             =SIMP(statut='f',typ='R' ),
             DNOR            =SIMP(statut='f',typ='R' ),
             DTAN            =SIMP(statut='f',typ='R' ),
             GRX             =SIMP(statut='f',typ='R' ),
             PRES            =SIMP(statut='f',typ='R' ),
             PHI             =SIMP(statut='f',typ='R' ),
             TEMP            =SIMP(statut='f',typ='R' ),
             PRE1            =SIMP(statut='f',typ='R' ),
             PRE2            =SIMP(statut='f',typ='R' ),
           ),

         FLUX_THM_REP    =FACT(statut='f',min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                     AU_MOINS_UN('FLUN','FLUN_HYDR1','FLUN_HYDR2'),),
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             FLUN            =SIMP(statut='f',typ='R' ),
             FLUN_HYDR1      =SIMP(statut='f',typ='R' ),
             FLUN_HYDR2      =SIMP(statut='f',typ='R' ),
           ),
         
         FORCE_ARETE     =FACT(statut='f',fr="Appliquer des forces lin�iques � une arete d �l�ment volumique ou de coque",
                                 min=1,max='**',
             regles=(AU_MOINS_UN('GROUP_MA','MAILLE',),
                     AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ' ),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             FX              =SIMP(statut='f',typ='R' ),
             FY              =SIMP(statut='f',typ='R' ),
             FZ              =SIMP(statut='f',typ='R' ),
             MX              =SIMP(statut='f',typ='R' ),
             MY              =SIMP(statut='f',typ='R' ),
             MZ              =SIMP(statut='f',typ='R' ),
           ), 
         
           FORCE_COQUE     =FACT(statut='f',fr="Appliquer des forces surfaciques sur des coques",min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                     AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ','PRES','F1','F2','F3','MF1','MF2'),               
                     PRESENT_ABSENT('FX','PRES','F1','F2','F3','MF1','MF2'),
                     PRESENT_ABSENT('FY','PRES','F1','F2','F3','MF1','MF2'),
                     PRESENT_ABSENT('FZ','PRES','F1','F2','F3','MF1','MF2'),
                     PRESENT_ABSENT('MX','PRES','F1','F2','F3','MF1','MF2'),
                     PRESENT_ABSENT('MY','PRES','F1','F2','F3','MF1','MF2'),
                     PRESENT_ABSENT('MZ','PRES','F1','F2','F3','MF1','MF2'),
                     PRESENT_ABSENT('F1','FX','FY','FZ','MX','MY','MZ','PRES'),
                     PRESENT_ABSENT('F2','FX','FY','FZ','MX','MY','MZ','PRES'),
                     PRESENT_ABSENT('F3','FX','FY','FZ','MX','MY','MZ','PRES'),
                     PRESENT_ABSENT('MF1','FX','FY','FZ','MX','MY','MZ','PRES'),
                     PRESENT_ABSENT('MF2','FX','FY','FZ','MX','MY','MZ','PRES'),
                     PRESENT_ABSENT('PRES','FX','FY','FZ','MX','MY','MZ','F1','F2','F3','MF1','MF2'),),
#  rajour d'un mot cl� REPERE :/ LOCAL /GLOBAL              
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             
               FX              =SIMP(statut='f',typ='R' ),
               FY              =SIMP(statut='f',typ='R' ),
               FZ              =SIMP(statut='f',typ='R' ),
               MX              =SIMP(statut='f',typ='R' ),
               MY              =SIMP(statut='f',typ='R' ),
               MZ              =SIMP(statut='f',typ='R' ),
             
               F1              =SIMP(statut='f',typ='R' ),
               F2              =SIMP(statut='f',typ='R' ),
               F3              =SIMP(statut='f',typ='R' ),
               MF1             =SIMP(statut='f',typ='R' ),
               MF2             =SIMP(statut='f',typ='R' ),
              
             PRES            =SIMP(statut='f',typ='R' ),
             PLAN            =SIMP(statut='f',typ='TXM',defaut="MAIL",into=("SUP","INF","MOY","MAIL",) ),
           ),

         FORCE_CONTOUR   =FACT(statut='f',fr="Appliquer des forces lin�iques au bord d'un domaine 2D ou AXIS_FOURIER",
                                 min=1,max='**',
             regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),
                     AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ'),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             FX              =SIMP(statut='f',typ='R' ),
             FY              =SIMP(statut='f',typ='R' ),
             FZ              =SIMP(statut='f',typ='R' ),
             MX              =SIMP(statut='f',typ='R' ),
             MY              =SIMP(statut='f',typ='R' ),
             MZ              =SIMP(statut='f',typ='R' ),
           ), 

         FORCE_ELEC      =FACT(statut='f',
                                 fr="Force de Laplace due � la pr�sence d'un conducteur rectiligne secondaire non maill�",
                                 min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                     AU_MOINS_UN('FX','FY','FZ','POSITION'),
                     EXCLUS('FX','POSITION'),
                     EXCLUS('FY','POSITION'),   
                     EXCLUS('FZ','POSITION'),),
#  trop de regles : les blocs conditionnels permettent d en suprimer              
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
              
             FX              =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             FY              =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             FZ              =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             
             POSITION        =SIMP(statut='f',typ='TXM',fr="Direction pr�d�finie",into=("PARA","INFI","FINI",) ),
             b_para     =BLOC ( condition = "POSITION == 'PARA'",
               regles=(UN_PARMI('TRANS','DIST'),),
               TRANS           =SIMP(statut='f',typ='R',max=3),
               DIST            =SIMP(statut='f',typ='R' ),
               b_point2        =BLOC ( condition = "DIST != None", 
                 POINT2           =SIMP(statut='o',typ='R',max=3),
               ),
             ),
             b_fini_infi     =BLOC ( condition = "(POSITION == 'FINI') or (POSITION == 'INFI')",
               POINT1          =SIMP(statut='o',typ='R',max=3),
               POINT2          =SIMP(statut='o',typ='R',max=3),
             ), 
           ),

         FORCE_FACE      =FACT(statut='f',fr="Appliquer des forces surfaciques sur une face d'�l�ments volumiques",
                                 min=1,max='**',
             regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),
                     AU_MOINS_UN('FX','FY','FZ'),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             FX              =SIMP(statut='f',typ='R' ),
             FY              =SIMP(statut='f',typ='R' ),
             FZ              =SIMP(statut='f',typ='R' ),
           ), 

         FORCE_INTERNE   =FACT(statut='f',fr="Appliquer des forces volumiques (2D ou 3D) � un domaine volumique",
                                 min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                     AU_MOINS_UN('FX','FY','FZ' ),),
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             FX              =SIMP(statut='f',typ='R' ),
             FY              =SIMP(statut='f',typ='R' ),
             FZ              =SIMP(statut='f',typ='R' ),
           ), 

         IMPE_FACE       =FACT(statut='f',fr="Appliquer une imp�dance acoustique � une face",min=1,max='**',
             regles=(AU_MOINS_UN('GROUP_MA','MAILLE' ),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             IMPE            =SIMP(statut='o',typ='R' ),
           ),
         
         FORCE_NODALE    =FACT(statut='f',fr="Imposer des forces nodales en des noeuds",min=1,max='**',
           regles=(AU_MOINS_UN('GROUP_NO','NOEUD'),
                   AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ' ),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           FX              =SIMP(statut='f',typ='R' ),
           FY              =SIMP(statut='f',typ='R' ),
           FZ              =SIMP(statut='f',typ='R' ),
           MX              =SIMP(statut='f',typ='R' ),
           MY              =SIMP(statut='f',typ='R' ),
           MZ              =SIMP(statut='f',typ='R' ),
           ANGL_NAUT       =SIMP(statut='f',typ='R',max=3),
         ),

        FORCE_POUTRE    =FACT(statut='f',fr="Appliquer des forces lin�iques sur des poutres",min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                     AU_MOINS_UN('FX','FY','FZ','N','VY','VZ'),
                     PRESENT_ABSENT('FX','N','VY','VZ'),              
                     PRESENT_ABSENT('FY','N','VY','VZ'),
                     PRESENT_ABSENT('FZ','N','VY','VZ'),
                     PRESENT_ABSENT('N','FX','FY','FZ'),
                     PRESENT_ABSENT('VY','FX','FY','FZ'),
                     PRESENT_ABSENT('VZ','FX','FY','FZ'),),
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FORCE",into=("VENT","FORCE",) ),
#  rajour d'un mot cl� REPERE :/ LOCAL /GLOBAL              
               FX              =SIMP(statut='f',typ='R' ),
               FY              =SIMP(statut='f',typ='R' ),
               FZ              =SIMP(statut='f',typ='R' ),
             
               N               =SIMP(statut='f',typ='R' ),
               VY              =SIMP(statut='f',typ='R' ),
               VZ              =SIMP(statut='f',typ='R' ),
              
           ),
         
         FORCE_TUYAU     =FACT(statut='f',fr="imposer une pression dans un �l�ment TUYAU",min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             PRES            =SIMP(statut='f',typ='R' ),
           ),
             
        INTE_ELEC       =FACT(statut='f',fr="Force de Laplace due � la pr�sence d'un conducteur non rectiligne secondaire",
                                 min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                     AU_MOINS_UN('GROUP_MA_2','MAILLE_2','TRANS','SYME'),
                     EXCLUS('TRANS','SYME'),),
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
             MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
             TRANS           =SIMP(statut='f',typ='R',max='**'),
             SYME            =SIMP(statut='f',typ='R',max='**'),
           ),
         
         LIAISON_CHAMNO  =FACT(statut='f',fr="d�finir une relation lin�aire entre tous les ddls d'un concept cham_nno",
                                 min=1,max='**',
#  type de cham_no CO()
             CHAM_NO         =SIMP(statut='o',typ=cham_no), #CO()
             COEF_IMPO       =SIMP(statut='o',typ='R' ),
             NUME_LAGR       =SIMP(statut='f',typ='TXM',defaut="NORMAL",into=("NORMAL","APRES") ),
           ), 

           LIAISON_COQUE   =FACT(statut='f',min=1,max='**',
             GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
             MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
             GROUP_NO_1      =SIMP(statut='f',typ=grno,max='**'),
             NOEUD_1         =SIMP(statut='f',typ=no,max='**'),
             GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
             MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
             GROUP_NO_2      =SIMP(statut='f',typ=grno,max='**'),
             NOEUD_2         =SIMP(statut='f',typ=no,max='**'),
             NUME_LAGR       =SIMP(statut='f',typ='TXM',defaut="NORMAL",into=("NORMAL","APRES") ),
           ),
           LIAISON_DDL     =FACT(statut='f',fr="D�finir une relation lin�aire entre des ddls de deux ou plusieurs noeuds",
                                 min=1,max='**',
             regles=(UN_PARMI('GROUP_NO','NOEUD'),),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             DDL             =SIMP(statut='o',typ='TXM',max='**'),
             COEF_MULT       =SIMP(statut='o',typ='R',max='**'),
             COEF_IMPO       =SIMP(statut='o',typ='R' ),
           ),

           LIAISON_ELEM    =FACT(statut='f',fr="Raccorder une poutre � une partie massive 3D ou une coque", min=1,max='**',
             regles=(UN_PARMI('GROUP_MA_1','MAILLE_1'),
                     UN_PARMI('GROUP_NO_2','NOEUD_2'),),
             OPTION          =SIMP(statut='o',typ='TXM',into=("3D_TUYAU","3D_POU","COQ_POU","COQ_TUYAU") ),
             GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
             MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
             GROUP_NO_2      =SIMP(statut='f',typ=grno,max='**'),
             NOEUD_2         =SIMP(statut='f',typ=no,max='**'),
             NUME_LAGR       =SIMP(statut='f',typ='TXM',defaut="NORMAL",into=("NORMAL","APRES") ),
             CARA_ELEM       =SIMP(statut='f',typ=(cara_elem) ),
             AXE_POUTRE      =SIMP(statut='f',typ='R',max=3),
             ANGL_MAX        =SIMP(statut='f',typ='R',defaut= 1. ),
           ),

           LIAISON_GROUP   =FACT(statut='f',fr="D�finir des relations lin�aires entre certains ddls de couples de noeuds",
                                 min=1,max='**',
             regles=(UN_PARMI('GROUP_MA_1','MAILLE_1','GROUP_NO_1','NOEUD_1'),        
                     UN_PARMI('GROUP_MA_2','MAILLE_2','GROUP_NO_2','NOEUD_2'),
                     EXCLUS('GROUP_MA_1','GROUP_NO_2'),
                     EXCLUS('GROUP_MA_1','NOEUD_2'),      
                     EXCLUS('GROUP_NO_1','GROUP_MA_2'),
                     EXCLUS('GROUP_NO_1','MAILLE_2'),
                     EXCLUS('MAILLE_1','GROUP_NO_2'),
                     EXCLUS('MAILLE_1','NOEUD_2'),
                     EXCLUS('NOEUD_1','GROUP_MA_2'),
                     EXCLUS('NOEUD_1','MAILLE_2'),
                     EXCLUS('SANS_NOEUD','SANS_GROUP_NO'),),
             
               GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
               MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
               GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
               MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
               GROUP_NO_1      =SIMP(statut='f',typ=grno,max='**'),
               NOEUD_1         =SIMP(statut='f',typ=no,max='**'),
               GROUP_NO_2      =SIMP(statut='f',typ=no,max='**'),
               NOEUD_2         =SIMP(statut='f',typ=no,max='**'),
             
             SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'),
             SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
             DDL_1           =SIMP(statut='o',typ='TXM',max='**'),
             COEF_MULT_1     =SIMP(statut='o',typ='R',max='**'),
             DDL_2           =SIMP(statut='o',typ='TXM',max='**'),
             COEF_MULT_2     =SIMP(statut='o',typ='R',max='**'),
             COEF_IMPO       =SIMP(statut='o',typ='R' ),
             SOMMET          =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             TRAN            =SIMP(statut='f',typ='R',max=3),
             ANGL_NAUT       =SIMP(statut='f',typ='R',max=3),
             CENTRE          =SIMP(statut='f',typ='R',max=3),
           ),

           LIAISON_OBLIQUE =FACT(statut='f',fr="Appliquer � des noeuds une valeur de d�placement dans un repere oblique",
                                 min=1,max='**',
             regles=(UN_PARMI('GROUP_NO','NOEUD'),
                     UN_PARMI('DX','DY','DZ','DRX','DRY','DRZ'),),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             ANGL_NAUT       =SIMP(statut='o',typ='R',max=3),
             DX              =SIMP(statut='f',typ='R' ),
             DY              =SIMP(statut='f',typ='R' ),
             DZ              =SIMP(statut='f',typ='R' ),
             DRX             =SIMP(statut='f',typ='R' ),
             DRY             =SIMP(statut='f',typ='R' ),
             DRZ             =SIMP(statut='f',typ='R' ),
           ), 

           LIAISON_SOLIDE  =FACT(statut='f',fr="Mod�liser une partie ind�formable d'une structure",min=1,max='**',
             regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE'),),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             NUME_LAGR       =SIMP(statut='f',typ='TXM',defaut="NORMAL",into=("NORMAL","APRES") ),
           ), 

           LIAISON_UNIF    =FACT(statut='f',fr="Imposer une meme valeur (inconnue) � des ddls d'un emsemble de noeuds",
                                 min=1,max='**',
             regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE'),),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             DDL             =SIMP(statut='o',typ='TXM',max='**'),
           ), 

         LIAISON_UNIL_NO =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('GROUP_MA_1','MAILLE_1'),
                   UN_PARMI('GROUP_MA_2','MAILLE_2'),),
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),# CO()
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),# CO()
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),# CO()
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),# CO()
           SOMMET          =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           TRAN            =SIMP(statut='f',typ='R',max=3 ),  
           ANGL_NAUT       =SIMP(statut='f',typ='R',max=3 ),  
           CENTRE          =SIMP(statut='f',typ='R',max=3 ),  
           ANGLE_MAX       =SIMP(statut='f',typ='R' ),  
           VECT_Y          =SIMP(statut='f',typ='R',min=3,max=3),
           FROTTEMENT      =SIMP(statut='f',typ='TXM',defaut="SANS",   
                                 into=("SANS","TRESCA","COULOMB") ),
           METHODE         =SIMP(statut='f',typ='TXM',defaut="CONTRAINTE",    
                                 into=("CONTRAINTE","LAGRANGIEN","PENALISATION") ),
           COULOMB         =SIMP(statut='f',typ='R' ),  
           TRESCA          =SIMP(statut='f',typ='R' ),  
           E_T             =SIMP(statut='f',typ='R' ),  
           COEF_MATR_FROT  =SIMP(statut='f',typ='R',defaut= 0.E+0 ),  
           CONTACT         =SIMP(statut='f',typ='TXM',into=("MAINTENU",) ),
           JEU             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),  
         ),
         
           LIAISON_MAIL    =FACT(statut='f',min=1,max='**',
             regles=(AU_MOINS_UN('GROUP_MA_MAIT','MAILLE_MAIT'),
                     AU_MOINS_UN('GROUP_MA_ESCL','MAILLE_ESCL','GROUP_NO_ESCL','NOEUD_ESCL'),
                     PRESENT_PRESENT('DDL_MAIT','DDL_ESCL'),),
              GROUP_MA_MAIT   =SIMP(statut='f',typ=grma,max='**'),
              MAILLE_MAIT     =SIMP(statut='f',typ=ma,max='**'), 
              GROUP_MA_ESCL   =SIMP(statut='f',typ=grma,max='**'),
              MAILLE_ESCL     =SIMP(statut='f',typ=ma,max='**'), 
              GROUP_NO_ESCL   =SIMP(statut='f',typ=grno,max='**'),
              NOEUD_ESCL      =SIMP(statut='f',typ=no,max='**'), 
              TRAN            =SIMP(statut='f',typ='R',max=3 ),
              ANGL_NAUT       =SIMP(statut='f',typ='R',max=3 ),
              CENTRE          =SIMP(statut='f',typ='R',max=3 ),
              DDL_MAIT        =SIMP(statut='f',typ='TXM',into=("DNOR",) ),
              DDL_ESCL        =SIMP(statut='f',typ='TXM',into=("DNOR",) ),
         ),
         
         ONDE_FLUI       =FACT(statut='f',fr="Appliquer une amplitude de pression d onde incidente",min=1,max='**',
             regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             PRES            =SIMP(statut='o',typ='R' ),
           ),
         
         PRES_REP        =FACT(statut='f',fr="Appliquer une pression � un domaine de milieu continu 2D ou 3D",
                                 min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                     AU_MOINS_UN('PRES','CISA_2D' ),),
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             PRES            =SIMP(statut='f',typ='R' ),
             CISA_2D         =SIMP(statut='f',typ='R' ),
           ),
         
         PESANTEUR       =SIMP(statut='f',typ='R',fr="Champ de pesanteur",min=4,max=4),

         RELA_CINE_BP    =FACT(statut='f',min=1,max='**',
           CABLE_BP        =SIMP(statut='o',typ=cabl_precont ),
           SIGM_BPEL       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           RELA_CINE       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         ),

        ROTATION        =SIMP(statut='f',typ='R',fr="Champ de rotation",min=4,max=4),
         b_rotation      =BLOC ( condition = "ROTATION != None",
           CENTRE          =SIMP(statut='f',typ='R',defaut=(0.,0.,0.),max=3),),     
         
         VITE_FACE       =FACT(statut='f',fr="Imposer des vitesses acoustiquesnormales � une face",min=1,max='**',
             regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             VNOR            =SIMP(statut='o',typ='R' ),
           ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
AFFE_CHAR_MECA_C=OPER(nom="AFFE_CHAR_MECA_C",op=   7,sd_prod=char_meca,
                     fr="Affectation de charges et conditions aux limites m�caniques complexes",
                     docu="U4.44.05-c",reentrant='n',
         regles=(AU_MOINS_UN('DDL_IMPO','FORCE_POUTRE','LIAISON_DDL', ),),
         MODELE          =SIMP(statut='o',typ=modele ),
         VERI_DDL        =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         DDL_IMPO        =FACT(statut='f',min=01,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE','GROUP_NO','NOEUD',),
                   AU_MOINS_UN('DX','DY','DZ','DRX','DRY','DRZ','GRX','PRES','PHI', ),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           DX              =SIMP(statut='f',typ='C' ),
           DY              =SIMP(statut='f',typ='C' ),
           DZ              =SIMP(statut='f',typ='C' ),
           DRX             =SIMP(statut='f',typ='C' ),
           DRY             =SIMP(statut='f',typ='C' ),
           DRZ             =SIMP(statut='f',typ='C' ),
           GRX             =SIMP(statut='f',typ='C' ),
           PRES            =SIMP(statut='f',typ='C' ),
           PHI             =SIMP(statut='f',typ='C' ),
         ),
         FORCE_POUTRE    =FACT(statut='f',min=01,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FX','FY','FZ','N','VY','VZ',),
                   PRESENT_ABSENT('FX','N','VY','VZ',),
                   PRESENT_ABSENT('FY','N','VY','VZ',),
                   PRESENT_ABSENT('FZ','N','VY','VZ',),
                   PRESENT_ABSENT('N','FX','FY','FZ',),
                   PRESENT_ABSENT('VY', 'FX','FY','FZ',),
                   PRESENT_ABSENT('VZ','FX','FY','FZ', ),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FORCE",into=("VENT","FORCE") ),
           FX              =SIMP(statut='f',typ='C' ),
           FY              =SIMP(statut='f',typ='C' ),
           FZ              =SIMP(statut='f',typ='C' ),
           N               =SIMP(statut='f',typ='C' ),
           VY              =SIMP(statut='f',typ='C' ),
           VZ              =SIMP(statut='f',typ='C' ),
         ),
         LIAISON_DDL     =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('GROUP_NO','NOEUD', ),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           DDL             =SIMP(statut='o',typ='TXM',max='**'),
           COEF_MULT       =SIMP(statut='o',typ='R',max='**'),
           COEF_IMPO       =SIMP(statut='o',typ='C' ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
AFFE_CHAR_MECA_F=OPER(nom="AFFE_CHAR_MECA_F",op=7,sd_prod=char_meca,
                      fr="Affectation de charges et conditions aux limites m�caniques fonction d une grandeur",
                      docu="U4.44.01-f",reentrant='n',
        regles=(AU_MOINS_UN('DDL_IMPO','FACE_IMPO','LIAISON_DDL','FORCE_NODALE',
                            'FORCE_FACE','FORCE_ARETE','FORCE_CONTOUR','FORCE_INTERNE',
                            'PRES_REP','FORCE_POUTRE','VITE_FACE','IMPE_FACE','ONDE_PLANE',
                            'LIAISON_OBLIQUE','EPSI_INIT','LIAISON_GROUP','LIAISON_UNIF',
                            'LIAISON_SOLIDE','FORCE_COQUE','LIAISON_COQUE','FORCE_TUYAU',
                            'CONTACT'),),
         MODELE          =SIMP(statut='o',typ=modele ),
         VERI_DDL        =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         VERI_NORM       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),

         DDL_IMPO        =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE','GROUP_NO','NOEUD'),
                   AU_MOINS_UN('DX','DY','DZ','DRX','DRY','DRZ','GRX','PRES','PHI',
                               'TEMP','PRE1','PRE2'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           DX              =SIMP(statut='f',typ=(fonction) ),
           DY              =SIMP(statut='f',typ=(fonction) ),
           DZ              =SIMP(statut='f',typ=(fonction) ),
           DRX             =SIMP(statut='f',typ=(fonction) ),
           DRY             =SIMP(statut='f',typ=(fonction) ),
           DRZ             =SIMP(statut='f',typ=(fonction) ),
           GRX             =SIMP(statut='f',typ=(fonction) ),
           PRES            =SIMP(statut='f',typ=(fonction) ),
           PHI             =SIMP(statut='f',typ=(fonction) ),
           TEMP            =SIMP(statut='f',typ=(fonction) ),
           PRE1            =SIMP(statut='f',typ=(fonction) ),
           PRE2            =SIMP(statut='f',typ=(fonction) ),
         ),
         LIAISON_UNIF    =FACT(statut='f',min=1,max='**',
                               fr="Imposer une meme valeur (inconnue) a des ddls d un emsemble de noeuds",
           regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE'),),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           DDL             =SIMP(statut='o',typ='TXM',max='**'),
         ),
         LIAISON_SOLIDE  =FACT(statut='f',min=1,max='**',
                               fr="Mod�liser une partie ind�formable d une structure",
           regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE'),),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           NUME_LAGR       =SIMP(statut='f',typ='TXM',defaut="NORMAL",into=("NORMAL","APRES",) ),
         ),
         LIAISON_OBLIQUE =FACT(statut='f',min=1,max='**',
                               fr="D�finir des relations lin�aires entre certains ddls de couples de noeuds",
           regles=(UN_PARMI('GROUP_NO','NOEUD'),
                   UN_PARMI('DX','DY','DZ','DRX','DRY','DRZ'),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           ANGL_NAUT       =SIMP(statut='o',typ='R',max=3),
           DX              =SIMP(statut='f',typ=(fonction) ),
           DY              =SIMP(statut='f',typ=(fonction) ),
           DZ              =SIMP(statut='f',typ=(fonction) ),
           DRX             =SIMP(statut='f',typ=(fonction) ),
           DRY             =SIMP(statut='f',typ=(fonction) ),
           DRZ             =SIMP(statut='f',typ=(fonction) ),
         ),
         LIAISON_COQUE   =FACT(statut='f',min=1,max='**',
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_1      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_1         =SIMP(statut='f',typ=no,max='**'),
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_2      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_2         =SIMP(statut='f',typ=no,max='**'),
           NUME_LAGR       =SIMP(statut='f',typ='TXM',defaut="NORMAL",into=("NORMAL","APRES",) ),
         ),
         FACE_IMPO       =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('GROUP_MA','MAILLE'),
                   AU_MOINS_UN('DX','DY','DZ','DRX','DRY','DRZ','GRX','PRES','PHI','TEMP','PRE1','PRE2','DNOR','DTAN'),
                   EXCLUS('DNOR','DX'),
                   EXCLUS('DNOR','DY'),
                   EXCLUS('DNOR','DZ'),
                   EXCLUS('DNOR','DRX'),
                   EXCLUS('DNOR','DRY'),
                   EXCLUS('DNOR','DRZ'),
                   EXCLUS('DTAN','DX'),
                   EXCLUS('DTAN','DY'),
                   EXCLUS('DTAN','DZ'),
                   EXCLUS('DTAN','DRX'),
                   EXCLUS('DTAN','DRY'),
                   EXCLUS('DTAN','DRZ'),),
#  rajout d un mot cle REPERE : / GLOBAL / LOCAL
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           DX              =SIMP(statut='f',typ=(fonction) ),
           DY              =SIMP(statut='f',typ=(fonction) ),
           DZ              =SIMP(statut='f',typ=(fonction) ),
           DRX             =SIMP(statut='f',typ=(fonction) ),
           DRY             =SIMP(statut='f',typ=(fonction) ),
           DRZ             =SIMP(statut='f',typ=(fonction) ),
           GRX             =SIMP(statut='f',typ=(fonction) ),
           PRES            =SIMP(statut='f',typ=(fonction) ),
           PHI             =SIMP(statut='f',typ=(fonction) ),
           TEMP            =SIMP(statut='f',typ=(fonction) ),
           PRE1            =SIMP(statut='f',typ=(fonction) ),
           PRE2            =SIMP(statut='f',typ=(fonction) ),
           DNOR            =SIMP(statut='f',typ=(fonction) ),
           DTAN            =SIMP(statut='f',typ=(fonction) ),
         ),
         LIAISON_DDL     =FACT(statut='f',min=1,max='**',
                               fr="D�finir une relation lin�aire entre des ddls de deux ou plusieurs noeuds",
           regles=(UN_PARMI('GROUP_NO','NOEUD'),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           DDL             =SIMP(statut='o',typ='TXM',max='**'),
           COEF_MULT       =SIMP(statut='o',typ='R',max='**'),
           COEF_IMPO       =SIMP(statut='o',typ=(fonction) ),
         ),
         LIAISON_GROUP   =FACT(statut='f',min=1,max='**',
                               fr="D�finir des relations lin�aires entre certains ddls de couples de noeuds",
           regles=(UN_PARMI('GROUP_MA_1','MAILLE_1','GROUP_NO_1','NOEUD_1'),
                   UN_PARMI('GROUP_MA_2','MAILLE_2','GROUP_NO_2','NOEUD_2'),
                   EXCLUS('GROUP_MA_1','GROUP_NO_2'),
                   EXCLUS('GROUP_MA_1','NOEUD_2'),
                   EXCLUS('GROUP_NO_1','GROUP_MA_2'),
                   EXCLUS('GROUP_NO_1','MAILLE_2'),
                   EXCLUS('MAILLE_1','GROUP_NO_2'),
                   EXCLUS('MAILLE_1','NOEUD_2'),
                   EXCLUS('NOEUD_1','GROUP_MA_2'),
                   EXCLUS('NOEUD_1','MAILLE_2'),
                   EXCLUS('SANS_NOEUD','SANS_GROUP_NO'),),
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_1      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_1         =SIMP(statut='f',typ=no,max='**'),
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_2      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_2         =SIMP(statut='f',typ=no,max='**'),
           SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'),
           SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
           DDL_1           =SIMP(statut='o',typ='TXM',max='**'),
           COEF_MULT_1     =SIMP(statut='o',typ='R',max='**'),
           DDL_2           =SIMP(statut='o',typ='TXM',max='**'),
           COEF_MULT_2     =SIMP(statut='o',typ='R',max='**'),
           COEF_IMPO       =SIMP(statut='o',typ=(fonction) ),
           SOMMET          =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           TRAN            =SIMP(statut='f',typ='R',max=3),
           ANGL_NAUT       =SIMP(statut='f',typ='R',max=3),
           CENTRE          =SIMP(statut='f',typ='R',max=3),
         ),

         FORCE_NODALE    =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('GROUP_NO','NOEUD'),
                   AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ'),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           FX              =SIMP(statut='f',typ=(fonction) ),
           FY              =SIMP(statut='f',typ=(fonction) ),
           FZ              =SIMP(statut='f',typ=(fonction) ),
           MX              =SIMP(statut='f',typ=(fonction) ),
           MY              =SIMP(statut='f',typ=(fonction) ),
           MZ              =SIMP(statut='f',typ=(fonction) ),
           ANGL_NAUT       =SIMP(statut='f',typ=(fonction),max=3 ),
         ),
         FORCE_INTERNE   =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FX','FY','FZ'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FX              =SIMP(statut='f',typ=(fonction) ),
           FY              =SIMP(statut='f',typ=(fonction) ),
           FZ              =SIMP(statut='f',typ=(fonction) ),
         ),
         FORCE_FACE      =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FX','FY','FZ'),),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FX              =SIMP(statut='f',typ=(fonction) ),
           FY              =SIMP(statut='f',typ=(fonction) ),
           FZ              =SIMP(statut='f',typ=(fonction) ),
         ),
         FORCE_ARETE     =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ'),),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FX              =SIMP(statut='f',typ=(fonction) ),
           FY              =SIMP(statut='f',typ=(fonction) ),
           FZ              =SIMP(statut='f',typ=(fonction) ),
           MX              =SIMP(statut='f',typ=(fonction) ),
           MY              =SIMP(statut='f',typ=(fonction) ),
           MZ              =SIMP(statut='f',typ=(fonction) ),
         ),
         FORCE_CONTOUR   =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ'),),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FX              =SIMP(statut='f',typ=(fonction) ),
           FY              =SIMP(statut='f',typ=(fonction) ),
           FZ              =SIMP(statut='f',typ=(fonction) ),
           MX              =SIMP(statut='f',typ=(fonction) ),
           MY              =SIMP(statut='f',typ=(fonction) ),
           MZ              =SIMP(statut='f',typ=(fonction) ),
         ),
         PRES_REP        =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('PRES','CISA_2D'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           PRES            =SIMP(statut='f',typ=(fonction) ),
           CISA_2D         =SIMP(statut='f',typ=(fonction) ),
         ),

         FORCE_COQUE     =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ','PRES','F1','F2','F3','MF1','MF2'),
                   PRESENT_ABSENT('FX','PRES','F1','F2','F3','MF1','MF2'),
                   PRESENT_ABSENT('FY','PRES','F1','F2','F3','MF1','MF2'),
                   PRESENT_ABSENT('FZ','PRES','F1','F2','F3','MF1','MF2'),
                   PRESENT_ABSENT('MX','PRES','F1','F2','F3','MF1','MF2'),
                   PRESENT_ABSENT('MY','PRES','F1','F2','F3','MF1','MF2'),
                   PRESENT_ABSENT('MZ','PRES','F1','F2','F3','MF1','MF2'),
                   PRESENT_ABSENT('F1','PRES','FX','FY','FZ','MX','MY','MZ'),
                   PRESENT_ABSENT('F2','PRES','FX','FY','FZ','MX','MY','MZ'),
                   PRESENT_ABSENT('F3','PRES','FX','FY','FZ','MX','MY','MZ'),
                   PRESENT_ABSENT('MF1','PRES','FX','FY','FZ','MX','MY','MZ'),
                   PRESENT_ABSENT('MF2','PRES','FX','FY','FZ','MX','MY','MZ'),
                   PRESENT_ABSENT('PRES','FX','FY','FZ','MX','MY','MZ','F1','F2','F3','MF1','MF2'),),
#  rajout d un mot cle REPERE : / GLOBAL / LOCAL
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FX              =SIMP(statut='f',typ=(fonction) ),
           FY              =SIMP(statut='f',typ=(fonction) ),
           FZ              =SIMP(statut='f',typ=(fonction) ),
           MX              =SIMP(statut='f',typ=(fonction) ),
           MY              =SIMP(statut='f',typ=(fonction) ),
           MZ              =SIMP(statut='f',typ=(fonction) ),
           F1              =SIMP(statut='f',typ=(fonction) ),
           F2              =SIMP(statut='f',typ=(fonction) ),
           F3              =SIMP(statut='f',typ=(fonction) ),
           MF1             =SIMP(statut='f',typ=(fonction) ),
           MF2             =SIMP(statut='f',typ=(fonction) ),
           PRES            =SIMP(statut='f',typ=(fonction) ),
           PLAN            =SIMP(statut='f',typ='TXM',defaut="MAIL",
                                 into=("SUP","INF","MOY","MAIL") ),
         ),
         FORCE_POUTRE    =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FX','FY','FZ','N','VY','VZ'),
                   PRESENT_ABSENT('FX','N','VY','VZ'),
                   PRESENT_ABSENT('FY','N','VY','VZ'),
                   PRESENT_ABSENT('FZ','N','VY','VZ'),
                   PRESENT_ABSENT('N','FX','FY','FZ'),
                   PRESENT_ABSENT('VY','FX','FY','FZ'),
                   PRESENT_ABSENT('VZ','FX','FY','FZ'),),
#  rajout d un mot cle REPERE : / GLOBAL / LOCAL
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FORCE",into=("VENT","FORCE") ),
           FX              =SIMP(statut='f',typ=(fonction) ),
           FY              =SIMP(statut='f',typ=(fonction) ),
           FZ              =SIMP(statut='f',typ=(fonction) ),
           N               =SIMP(statut='f',typ=(fonction) ),
           VY              =SIMP(statut='f',typ=(fonction) ),
           VZ              =SIMP(statut='f',typ=(fonction) ),
         ),
         FORCE_TUYAU     =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           PRES            =SIMP(statut='f',typ=(fonction) ),
         ),
         VITE_FACE       =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('GROUP_MA','MAILLE'),),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           VNOR            =SIMP(statut='o',typ=(fonction) ),
         ),
         IMPE_FACE       =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('GROUP_MA','MAILLE'),),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           IMPE            =SIMP(statut='o',typ=(fonction) ),
         ),
         ONDE_PLANE      =FACT(statut='f',min=1,max='**',
           DIRECTION       =SIMP(statut='o',typ='R',max='**'),
           TYPE_ONDE       =SIMP(statut='o',typ='TXM' ),
           FONC_SIGNAL     =SIMP(statut='o',typ=(fonction) ),
           DIST_ORIG       =SIMP(statut='o',typ='R' ),
         ),
         EPSI_INIT       =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('EPXX','EPYY','EPZZ','EPXY','EPXZ','EPYZ'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           EPXX            =SIMP(statut='f',typ=(fonction) ),
           EPYY            =SIMP(statut='f',typ=(fonction) ),
           EPZZ            =SIMP(statut='f',typ=(fonction) ),
           EPXY            =SIMP(statut='f',typ=(fonction) ),
           EPXZ            =SIMP(statut='f',typ=(fonction) ),
           EPYZ            =SIMP(statut='f',typ=(fonction) ),
         ),

         CONTACT         =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('GROUP_MA_2','MAILLE_2'),
                   EXCLUS('DIST_2','COEF_IMPO'),
                   EXCLUS('DIST_1','COEF_IMPO'),
                   EXCLUS('COEF_MULT_2','GROUP_MA_1'),
                   EXCLUS('COEF_MULT_2','MAILLE_1'),
                   EXCLUS('COEF_IMPO','GROUP_MA_1'),
                   EXCLUS('COEF_IMPO','MAILLE_1'),),
           NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL","PRES","TEMP") ),
           APPARIEMENT     =SIMP(statut='f',typ='TXM',defaut="MAIT_ESCL",
                                 into=("NON","NODAL","NODAL_SYME","MAIT_ESCL","MAIT_ESCL_SYME") ),
           RECHERCHE       =SIMP(statut='f',typ='TXM',defaut="NOEUD_VOISIN",
                                 into=("NOEUD_BOUCLE","NOEUD_VOISIN") ),
           INTEGRATION     =SIMP(statut='f',typ='TXM',defaut="NOEUD",into=("GAUSS","NOEUD")),
           COEF_REGU_CONT  =SIMP(statut='f',typ='R',defaut=100.E+0),
           COEF_REGU_FROT  =SIMP(statut='f',typ='R',defaut=100.E+0),
           MODL_AXIS       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
           ITER_GEOM_MAXI  =SIMP(statut='f',typ='I',defaut=2),
           ITER_CONT_MAXI  =SIMP(statut='f',typ='I',defaut=30),
           ITER_FROT_MAXI  =SIMP(statut='f',typ='I',defaut=2),
           LISSAGE         =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
           SEUIL_INIT      =SIMP(statut='f',typ='I',defaut=0),
           REAC_GEOM_INTE  =SIMP(statut='f',typ='I',defaut= 2),
           NORMALE         =SIMP(statut='f',typ='TXM',defaut="MAIT",into=("MAIT","MAIT_ESCL")),
           METHODE         =SIMP(statut='f',typ='TXM',defaut="CONTRAINTE",
                                 into=("CONTRAINTE","LAGRANGIEN","PENALISATION") ),
           FROTTEMENT      =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SANS","COULOMB",) ),
           COULOMB         =SIMP(statut='f',typ='R',max=1,defaut=0.E+0),
           E_N             =SIMP(statut='f',typ='R' ),
           E_T             =SIMP(statut='f',typ='R' ),
           COEF_MATR_FROT  =SIMP(statut='f',typ='R',defaut=0.E+0),
           VECT_Y          =SIMP(statut='f',typ='R',min=3,max=3),
           VECT_NORM_2     =SIMP(statut='f',typ='R',max=3),
           PROJECTION      =SIMP(statut='f',typ='TXM',defaut="LINEAIRE",into=("LINEAIRE",) ),
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'  ),
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'  ),
           SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'  ),
           SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
           DIST_1          =SIMP(statut='f',typ=(fonction) ),
           DIST_2          =SIMP(statut='f',typ=(fonction) ),
           COEF_IMPO       =SIMP(statut='f',typ='R',defaut=0.E+0),
           COEF_MULT_2     =SIMP(statut='f',typ='R',defaut=1.E+0),
         ),
         FLUX_THM_REP    =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FLUN','FLUN_HYDR1','FLUN_HYDR2'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FLUN            =SIMP(statut='f',typ=(fonction) ),
           FLUN_HYDR1      =SIMP(statut='f',typ=(fonction) ),
           FLUN_HYDR2      =SIMP(statut='f',typ=(fonction) ),
         ),

         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
AFFE_CHAR_OPS011=OPER(nom="AFFE_CHAR_OPS011",op= 190,sd_prod=char_ther,
                      fr=" ",
                      docu="",reentrant='n',
         regles=(AU_MOINS_UN('CARA_TORSION', ),),
         MODELE          =SIMP(statut='o',typ=modele ),
         VERI_DDL        =SIMP(statut='f',typ='TXM',defaut="OUI",
                               into=("OUI","NON") ),
         CARA_TORSION    =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_MA'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
AFFE_CHAR_THER=OPER(nom="AFFE_CHAR_THER",op=34,sd_prod=char_ther
                    ,fr="Affectation de charges et conditions aux limites thermiques constantes",
                    docu="U4.44.02-f",reentrant='n',
      regles=(AU_MOINS_UN('TEMP_IMPO','SOURCE','FLUX_REP','ECHANGE',
                          'ECHANGE_PAROI','GRAD_TEMP_INIT','LIAISON_DDL','LIAISON_GROUP',
                          'LIAISON_UNIF','LIAISON_CHAMNO','RAYONNEMENT','LIAISON_MAIL' ),),
         MODELE          =SIMP(statut='o',typ=(modele) ),
         VERI_DDL        =SIMP(statut='f',typ='TXM',into=("OUI","NON"),defaut="OUI"),
         LIAISON_DDL     =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('GROUP_NO','NOEUD', ),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           DDL             =SIMP(statut='f',typ='TXM',max='**',
                                 into=("TEMP","TEMP_INF","TEMP_SUP") ),
           COEF_MULT       =SIMP(statut='o',typ='R',max='**'),
           COEF_IMPO       =SIMP(statut='o',typ='R' ),
         ),
         TEMP_IMPO       =FACT(statut='f',min=01,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE','GROUP_NO','NOEUD'),
                   AU_MOINS_UN('TEMP_SUP','TEMP','TEMP_INF'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           TEMP            =SIMP(statut='f',typ='R'),
           TEMP_INF        =SIMP(statut='f',typ='R'),
           TEMP_SUP        =SIMP(statut='f',typ='R'), ),
         LIAISON_UNIF    =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE'),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           DDL             =SIMP(statut='f',typ='TXM',max='**',defaut="TEMP",
                                 into=("TEMP","TEMP_INF","TEMP_SUP") ),
         ),
         LIAISON_CHAMNO  =FACT(statut='f',min=01,max='**',
           CHAM_NO         =SIMP(statut='o',typ=cham_no),# CO()# "il faut definir une structure de donnee generique chamno"
           COEF_IMPO       =SIMP(statut='o',typ='R' ),
           NUME_LAGR       =SIMP(statut='f',typ='TXM',defaut="NORMAL",into=("NORMAL","APRES") ),
         ),
         SOURCE          =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('SOUR','SOUR_CALCULEE',),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('SOUR_CALCULEE','TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           SOUR            =SIMP(statut='f',typ='R'),
           SOUR_CALCULEE   =SIMP(statut='f',typ=(cham_elem_sour_r) ),
         ),
         FLUX_REP        =FACT(statut='f',min=01,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_PRESENT('CARA_TORSION','GROUP_MA'),
                   AU_MOINS_UN('FLUN','FLUN_INF','FLUN_SUP','CARA_TORSION') ),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FLUN            =SIMP(statut='f',typ='R'),
           FLUN_INF        =SIMP(statut='f',typ='R'),
           FLUN_SUP        =SIMP(statut='f',typ='R'),
           CARA_TORSION    =SIMP(statut='f',typ=tabl_aire_int ),
         ),
         ECHANGE         =FACT(statut='f',min=01,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('COEF_H','COEF_H_INF','COEF_H_SUP'),
                   ENSEMBLE('COEF_H','TEMP_EXT',),
                   ENSEMBLE('COEF_H_INF','TEMP_EXT_INF'),
                             ENSEMBLE('COEF_H_SUP','TEMP_EXT_SUP'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           COEF_H          =SIMP(statut='f',typ='R'),
           TEMP_EXT        =SIMP(statut='f',typ='R'),
           COEF_H_INF      =SIMP(statut='f',typ='R'),
           TEMP_EXT_INF    =SIMP(statut='f',typ='R'),
           COEF_H_SUP      =SIMP(statut='f',typ='R'),
           TEMP_EXT_SUP    =SIMP(statut='f',typ='R'),
         ),
         ECHANGE_PAROI   =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('GROUP_MA_1','MAILLE_1'),
                   UN_PARMI('GROUP_MA_2','MAILLE_2'),),
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
           COEF_H          =SIMP(statut='f',typ='R'),
           TRAN            =SIMP(statut='f',typ='R',min=2,max=3),
           ANGL_NAUT       =SIMP(statut='f',typ='R',min=1,max=3),
           CENTRE          =SIMP(statut='f',typ='R',min=2,max=3),
                         ),
         GRAD_TEMP_INIT  =FACT(statut='f',min=01,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FLUX_X','FLUX_Y','FLUX_Z'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FLUX_X          =SIMP(statut='f',typ='R' ),
           FLUX_Y          =SIMP(statut='f',typ='R' ),
           FLUX_Z          =SIMP(statut='f',typ='R' ),
                         ),
         LIAISON_GROUP   =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('GROUP_MA_1','MAILLE_1','GROUP_NO_1','NOEUD_1'),
                   UN_PARMI('GROUP_MA_2','MAILLE_2','GROUP_NO_2','NOEUD_2'),
                             EXCLUS('GROUP_MA_1','GROUP_NO_2'),
                             EXCLUS('GROUP_MA_1','NOEUD_2'),
                   EXCLUS('GROUP_NO_1','GROUP_MA_2'),
                             EXCLUS('GROUP_NO_1','MAILLE_2'),
                             EXCLUS('MAILLE_1','GROUP_NO_2'),
                             EXCLUS('MAILLE_1','NOEUD_2'),
                             EXCLUS('NOEUD_1','GROUP_MA_2'),
                             EXCLUS('NOEUD_1','MAILLE_2'),
                             EXCLUS('SANS_NOEUD','SANS_GROUP_NO'),),
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_1      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_1         =SIMP(statut='f',typ=no,max='**'),
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_2      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_2         =SIMP(statut='f',typ=no,max='**'),
           SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'),
           SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
           DDL_1           =SIMP(statut='f',typ='TXM',max='**',defaut="TEMP",
                                 into=("TEMP","TEMP_INF","TEMP_SUP") ),
           COEF_MULT_1     =SIMP(statut='o',typ='R',max='**'),
           DDL_2           =SIMP(statut='f',typ='TXM',max='**',defaut="TEMP",
                                 into=("TEMP","TEMP_INF","TEMP_SUP",) ),
           COEF_MULT_2     =SIMP(statut='o',typ='R',max='**'),
           COEF_IMPO       =SIMP(statut='o',typ='R' ),
           SOMMET          =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           TRAN            =SIMP(statut='f',typ='R',max='**'),
           ANGL_NAUT       =SIMP(statut='f',typ='R',max='**'),
           CENTRE          =SIMP(statut='f',typ='R',max='**'),
         ),
         CONVECTION      =FACT(statut='f',min=01,max='**',
           VITESSE         =SIMP(statut='o',typ=(cham_no_depl_r) ),
         ),
         RAYONNEMENT     =FACT(statut='f',min=01,max='**',
           fr="Attention, exprimer les temp�ratures en Celsius si rayonnement",
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           SIGMA           =SIMP(statut='o',typ='R'),
           EPSILON         =SIMP(statut='o',typ='R'),
           TEMP_EXT        =SIMP(statut='o',typ='R'),
         ),
         LIAISON_MAIL    =FACT(statut='f',min=01,max='**',
           regles=(AU_MOINS_UN('GROUP_MA_MAIT','MAILLE_MAIT'),
                   AU_MOINS_UN('GROUP_MA_ESCL','MAILLE_ESCL','GROUP_NO_ESCL',
                               'NOEUD_ESCL'),),
           GROUP_MA_MAIT   =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_MAIT     =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA_ESCL   =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_ESCL     =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_ESCL   =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_ESCL      =SIMP(statut='f',typ=no,max='**'),
           TRAN            =SIMP(statut='f',typ='R',max='**' ),
           ANGL_NAUT       =SIMP(statut='f',typ='R',max='**' ),
           CENTRE          =SIMP(statut='f',typ='R',max='**' ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
AFFE_CHAR_THER_F=OPER(nom="AFFE_CHAR_THER_F",op=33,sd_prod=char_ther,
                     fr="Affectation de charges et conditions aux limites thermiques fonction dune grandeur (temps, ...)",
                     docu="U4.44.02-f",reentrant='n',
      regles=(AU_MOINS_UN('TEMP_IMPO','SOURCE','FLUX_REP','FLUX_NL','ECHANGE',
                          'ECHANGE_PAROI','LIAISON_DDL','LIAISON_GROUP','LIAISON_UNIF',
                          'GRAD_TEMP_INIT','RAYONNEMENT'),),
         MODELE          =SIMP(statut='o',typ=(modele) ),
         VERI_DDL        =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         LIAISON_DDL     =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('GROUP_NO','NOEUD'),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           DDL             =SIMP(statut='f',typ='TXM',max='**',into=("TEMP","TEMP_INF","TEMP_SUP") ),
           COEF_MULT       =SIMP(statut='o',typ='R',max='**'),
           COEF_IMPO       =SIMP(statut='o',typ=(fonction) ),
         ),
         TEMP_IMPO       =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE','GROUP_NO','NOEUD'),
                   AU_MOINS_UN('TEMP_SUP','TEMP','TEMP_INF','EVOL_THER'),
                   PRESENT_ABSENT('EVOL_THER','TEMP','TEMP_INF','TEMP_SUP'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           EVOL_THER       =SIMP(statut='f',typ=(evol_ther) ),
           DDL             =SIMP(statut='f',typ='TXM',into=("TEMP",) ),
           TEMP            =SIMP(statut='f',typ=(fonction) ),
           TEMP_INF        =SIMP(statut='f',typ=(fonction) ),
           TEMP_SUP        =SIMP(statut='f',typ=(fonction) ),
         ),
         LIAISON_UNIF    =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE'),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           DDL             =SIMP(statut='f',typ='TXM',max='**',defaut="TEMP",
                                 into=("TEMP","TEMP_INF","TEMP_SUP") ),
         ),
         SOURCE          =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           SOUR            =SIMP(statut='o',typ=(fonction) ),
         ),
         FLUX_REP        =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FLUN','FLUN_INF','FLUN_SUP','FLUX_X','FLUX_Y','FLUX_Z'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FLUN            =SIMP(statut='f',typ=(fonction) ),
           FLUN_INF        =SIMP(statut='f',typ=(fonction) ),
           FLUN_SUP        =SIMP(statut='f',typ=(fonction) ),
           FLUX_X          =SIMP(statut='f',typ=(fonction) ),
           FLUX_Y          =SIMP(statut='f',typ=(fonction) ),
           FLUX_Z          =SIMP(statut='f',typ=(fonction) ),
         ),
         FLUX_NL         =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FLUN            =SIMP(statut='o',typ=(fonction) ),
         ),
         ECHANGE         =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('COEF_H','COEF_H_INF','COEF_H_SUP'),
                   ENSEMBLE('COEF_H','TEMP_EXT'),
                   ENSEMBLE('COEF_H_INF','TEMP_EXT_INF'),
                   ENSEMBLE('COEF_H_SUP','TEMP_EXT_SUP'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           COEF_H          =SIMP(statut='f',typ=(fonction) ),
           TEMP_EXT        =SIMP(statut='f',typ=(fonction) ),
           COEF_H_INF      =SIMP(statut='f',typ=(fonction) ),
           TEMP_EXT_INF    =SIMP(statut='f',typ=(fonction) ),
           COEF_H_SUP      =SIMP(statut='f',typ=(fonction) ),
           TEMP_EXT_SUP    =SIMP(statut='f',typ=(fonction) ),
         ),
         ECHANGE_PAROI   =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('GROUP_MA_1','MAILLE_1'),
                        UN_PARMI('GROUP_MA_2','MAILLE_2'),),
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
           COEF_H          =SIMP(statut='o',typ=(fonction) ),
           TRAN            =SIMP(statut='f',typ='R',min=2,max=3),
           ANGL_NAUT       =SIMP(statut='f',typ='R',min=1,max=3),
           CENTRE          =SIMP(statut='f',typ='R',min=2,max=3),
         ),
         GRAD_TEMP_INIT  =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                   AU_MOINS_UN('FLUX_X','FLUX_Y','FLUX_Z'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           FLUX_X          =SIMP(statut='f',typ=(fonction) ),
           FLUX_Y          =SIMP(statut='f',typ=(fonction) ),
           FLUX_Z          =SIMP(statut='f',typ=(fonction) ),
         ),
         LIAISON_GROUP   =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('GROUP_MA_1','MAILLE_1','GROUP_NO_1','NOEUD_1'),
                   UN_PARMI('GROUP_MA_2','MAILLE_2','GROUP_NO_2','NOEUD_2'),
                             EXCLUS('GROUP_MA_1','GROUP_NO_2'),
                        EXCLUS('GROUP_MA_1','NOEUD_2'),
                   EXCLUS('GROUP_NO_1','GROUP_MA_2'),
                        EXCLUS('GROUP_NO_1','MAILLE_2'),
                        EXCLUS('MAILLE_1','GROUP_NO_2'),
                        EXCLUS('MAILLE_1','NOEUD_2'),
                        EXCLUS('NOEUD_1','GROUP_MA_2'),
                        EXCLUS('NOEUD_1','MAILLE_2'),
                        EXCLUS('SANS_NOEUD','SANS_GROUP_NO'),),
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_1      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_1         =SIMP(statut='f',typ=no,max='**'),
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_2      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_2         =SIMP(statut='f',typ=no,max='**'),
           SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'),
           SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
           DDL_1           =SIMP(statut='f',typ='TXM',max='**',defaut="TEMP",
                                 into=("TEMP","TEMP_INF","TEMP_SUP") ),
           COEF_MULT_1     =SIMP(statut='o',typ='R',max='**'),
           DDL_2           =SIMP(statut='f',typ='TXM',max='**',defaut="TEMP",
                                 into=("TEMP","TEMP_INF","TEMP_SUP") ),
           COEF_MULT_2     =SIMP(statut='o',typ='R',max='**'),
           COEF_IMPO       =SIMP(statut='o',typ=(fonction) ),
           SOMMET          =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           TRAN            =SIMP(statut='f',typ='R',max='**'),
           ANGL_NAUT       =SIMP(statut='f',typ='R',max='**'),
           CENTRE          =SIMP(statut='f',typ='R',max='**'),
         ),
         CONVECTION      =FACT(statut='f',min=1,max='**',
           VITESSE         =SIMP(statut='o',typ=(cham_no_depl_r) ),
         ),
         RAYONNEMENT     =FACT(statut='f',min=1,max='**',
           fr="Attention, exprimer les temp�ratures en Celsius si rayonnement",
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                   PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           SIGMA           =SIMP(statut='o',typ=(fonction) ),
           EPSILON         =SIMP(statut='o',typ=(fonction) ),
           TEMP_EXT        =SIMP(statut='o',typ=(fonction) ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
AFFE_MATERIAU=OPER(nom="AFFE_MATERIAU",op=6,sd_prod=cham_mater,
                   fr="Affectation de caract�ristiques de mat�riaux � un maillage",
                         docu="U4.43.03-f",reentrant='n',
         MAILLAGE        =SIMP(statut='o',typ=maillage),
         MODELE          =SIMP(statut='f',typ=modele),
         AFFE            =FACT(statut='o',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_MA','MAILLE','GROUP_NO','NOEUD'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           MATER           =SIMP(statut='o',typ=mater),
           TEMP_REF        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),
)  ;
#& MODIF COMMANDE  DATE 30/01/2002   AUTEUR VABHHTS J.TESELET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE JMBHH01 J.M.PROIX
AFFE_MODELE=OPER(nom="AFFE_MODELE",op=18,sd_prod=modele,docu="U4.41.01-f1",
                 fr="Affectation des �l�ments finis sur le maillage",reentrant='n',
         regles=(AU_MOINS_UN('AFFE','AFFE_SOUS_STRUC'),),
         MAILLAGE        =SIMP(statut='o',typ=(maillage) ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
         VERIF           =SIMP(statut='f',typ='TXM',max=2,into=("MAILLE","NOEUD") ),
         AFFE_SOUS_STRUC =FACT(statut='f',min=01,max=01,
           regles=(UN_PARMI('TOUT','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           PHENOMENE       =SIMP(statut='f',typ='TXM',defaut="MECANIQUE",into=("MECANIQUE",) ),
         ),
         AFFE            =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_MA','GROUP_NO','MAILLE','NOEUD'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           PHENOMENE       =SIMP(statut='o',typ='TXM',
                                 into=("MECANIQUE","THERMIQUE","ACOUSTIQUE","NON_LOCAL") ),
                b_mecanique     =BLOC( condition = "PHENOMENE=='MECANIQUE'",
                                        fr="modelisations m�caniques",
                    MODELISATION    =SIMP(statut='o',typ='TXM', into=(
                                                                      "2D_CONTACT",
                                                                      "2D_DIS_T",
                                                                      "2D_DIS_TR",
                                                                      "2D_FLUI_ABSO",
                                                                      "2D_FLUI_PESA",
                                                                      "2D_FLUI_STRU",
                                                                      "2D_FLUIDE",
                                                                      "3D",
                                                                      "3D_ABSO",
                                                                      "3D_CONTACT",
                                                                      "3D_FAISCEAU",
                                                                      "3D_FLUI_ABSO",
                                                                      "3D_FLUIDE",
                                                                      "3D_HHM" ,
                                                                      "3D_HM",
                                                                      "3D_INCO",
                                                                      "3D_JOINT_CT",
                                                                      "3D_SI",
                                                                      "3D_THH",
                                                                      "3D_THHM",
                                                                      "3D_THM",
                                                                      "APPUI_REP",
                                                                      "ASSE_GRIL",
                                                                      "AXIS",
                                                                      "AXIS_FLUI_STRU",
                                                                      "AXIS_FLUIDE",
                                                                      "AXIS_FOURIER",
                                                                      "AXIS_HHM",
                                                                      "AXIS_HM",
                                                                      "AXIS_INCO",
                                                                      "AXIS_SI",
                                                                      "AXIS_THH",
                                                                      "AXIS_THHM",
                                                                      "AXIS_THM",
                                                                      "BARRE",
                                                                      "2D_BARRE",
                                                                      "C_PLAN",
                                                                      "C_PLAN_SI",
                                                                      "CABLE",
                                                                      "CABLE_POULIE",
                                                                      "COQUE_3D",
                                                                      "COQUE_AXIS",
                                                                      "COQUE_C_PLAN",
                                                                      "COQUE_D_PLAN",
                                                                      "CONT_DVP_2D",
                                                                      "CONT_DVP_3D",
                                                                      "D_PLAN",
                                                                      "D_PLAN_ABSO",
                                                                      "D_PLAN_HHM",
                                                                      "D_PLAN_HM",
                                                                      "D_PLAN_INCO",
                                                                      "D_PLAN_SI",
                                                                      "D_PLAN_THH",
                                                                      "D_PLAN_THHM",
                                                                      "D_PLAN_THM",
                                                                      "DIS_T",
                                                                      "DIS_TR",
                                                                      "DKT",
                                                                      "DST",
                                                                      "FLUI_STRU",
                                                                      "GRILLE",
                                                                      "POU_C_T",
                                                                      "POU_D_E",
                                                                      "POU_D_EM",
                                                                      "POU_D_T",
                                                                      "POU_D_T_GD",
                                                                      "POU_D_TG",
                                                                      "Q4G",
                                                                      "TUYAU",
                                                                      "TUYAU_3M",
                                                                      "TUYAU_6M"
                                                                     )  )  ),

                b_thermique     =BLOC( condition = "PHENOMENE=='THERMIQUE'",
                                        fr="modelisations thermiques",
                    MODELISATION    =SIMP(statut='o',typ='TXM',into=(
                                                                      "3D",
                                                                      "3D_DIAG",
                                                                      "AXIS",
                                                                      "AXIS_DIAG",
                                                                      "AXIS_FOURIER",
                                                                      "COQUE",
                                                                      "COQUE_AXIS",
                                                                      "COQUE_PLAN",
                                                                      "PLAN",
                                                                      "PLAN_DIAG",
                                                                      ),),),

                b_acoustique    =BLOC( condition = "PHENOMENE=='ACOUSTIQUE'",
                                        fr="modelisations acoustiques",
                     MODELISATION    =SIMP(statut='o',typ='TXM',into=(
                                                                       "3D",
                                                                       "PLAN"
                                                                       ), ),),

                b_non_local     =BLOC( condition = "PHENOMENE=='NON_LOCAL'",
                                        fr="modelisations non locales",
                     MODELISATION    =SIMP(statut='o',typ='TXM',into=(
                                                                      "3D",
                                                                      "AXIS",
                                                                      "C_PLAN",
                                                                      "D_PLAN",
                                                                     ) ), ),
         ),
) ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
AIDE=PROC(nom="AIDE",op=42,docu="U4.02.01-f",
          fr="Interrogation sur le catalogue des commandes et les concepts produits",
         regles=(AU_MOINS_UN('COMMANDE','CONCEPT','TYPE_ELEM', ),),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT"),
         TYPE_ELEM       =FACT(fr="couple type_elem option",
                               statut='f',min=01,max=01,
           INITEL          =SIMP(statut='f',typ='TXM',defaut="NON",
                                 into=("OUI","NON",) ),
         ),
         COMMANDE        =FACT(statut='f',min=01,max='**',
           NOM             =SIMP(fr="liste des noms de commande", 
                                 statut='f',typ='TXM',max='**',defaut="*"),
           OPTION          =SIMP(fr="option d'�dition de commande",
                                 statut='f',typ='TXM',defaut="CATALOGUE",
                                 into=("CATALOGUE","A_REMPLIR","NUMERO",) ),
         ),
         CONCEPT         =FACT(statut='f',min=01,max='**',
           NOM             =SIMP(fr="liste des noms de concept", 
                                 statut='f',typ='TXM',max='**',defaut="*"),
           OPTION          =SIMP(fr="option d'�dition de concept",
                                 statut='f',typ='TXM',defaut="TOUT_TYPE",
                                 into=("TOUT_TYPE","CREER","A_CREER",) ),
         ),
) ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
ASSE_MAILLAGE=OPER(nom="ASSE_MAILLAGE",op= 105,sd_prod=maillage,
                   fr="Assembler deux maillages sous un seul nom",
                   docu="U4.23.03-e",reentrant='n',
         MAILLAGE        =SIMP(statut='o',typ=maillage,min=2,max=2 ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
ASSE_MATR_GENE=OPER(nom="ASSE_MATR_GENE",op= 128,sd_prod=matr_asse_gene_r,
                    fr="Assemblage des matrices g�n�ralis�es de macro �l�ments pour construction de la matrice globale g�n�ralis�e",
                    docu="U4.65.04-d",reentrant='n',
         NUME_DDL_GENE   =SIMP(statut='o',typ=nume_ddl_gene ),
         OPTION          =SIMP(statut='o',typ='TXM',into=("RIGI_GENE","MASS_GENE","AMOR_GENE") ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def asse_matrice_prod(MATR_ELEM,**args):
  if AsType(MATR_ELEM) == matr_elem_depl_r : return matr_asse_depl_r
  if AsType(MATR_ELEM) == matr_elem_depl_c : return matr_asse_depl_c
  if AsType(MATR_ELEM) == matr_elem_temp_r : return matr_asse_temp_r
  if AsType(MATR_ELEM) == matr_elem_pres_c : return matr_asse_pres_c
  raise AsException("type de concept resultat non prevu")

ASSE_MATRICE=OPER(nom="ASSE_MATRICE",op=12,sd_prod=asse_matrice_prod,
                  fr="Construction d une matrice assembl�e",docu="U4.61.22-f",reentrant='n',
         MATR_ELEM       =SIMP(statut='o',
                               typ=(matr_elem_depl_r,matr_elem_depl_c,matr_elem_temp_r,matr_elem_pres_c) ),
         NUME_DDL        =SIMP(statut='o',typ=nume_ddl),
         CHAR_CINE       =SIMP(statut='f',typ=(char_cine_meca,char_cine_ther,char_cine_acou) ),
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
ASSE_VECT_GENE=OPER(nom="ASSE_VECT_GENE",op= 140,sd_prod=vect_asse_gene,
                    fr="Assemblage de vecteurs de chargement en coordonn�es g�n�ralis�es",
                    docu="U4.65.05-d",reentrant='n',
         NUME_DDL_GENE   =SIMP(statut='o',typ=nume_ddl_gene ),
         CHAR_SOUS_STRUC =FACT(statut='o',min=01,max='**',
           SOUS_STRUC      =SIMP(statut='o',typ='TXM' ),
           VECT_ASSE       =SIMP(statut='o',typ=cham_no_depl_r ),
         ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def asse_vecteur_prod(VECT_ELEM,**args):
  if AsType(VECT_ELEM) == vect_elem_depl_r : return cham_no_depl_r
  if AsType(VECT_ELEM) == vect_elem_temp_r : return cham_no_temp_r
  if AsType(VECT_ELEM) == vect_elem_pres_r : return cham_no_pres_r
  if AsType(VECT_ELEM) == vect_elem_pres_c : return cham_no_pres_c
  raise AsException("type de concept resultat non prevu ")

ASSE_VECTEUR=OPER(nom="ASSE_VECTEUR",op=13,sd_prod=asse_vecteur_prod,
                  fr="Assemblage d un second membre",docu="U4.61.23-f",reentrant='n',
         VECT_ELEM       =SIMP(statut='o',typ=vect_elem,max='**'),
         NUME_DDL        =SIMP(statut='o',typ=nume_ddl ),
         INFO            =SIMP(statut='f',typ='I',into=(1,2,) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_AMOR_MODAL=OPER(nom="CALC_AMOR_MODAL",op= 172,sd_prod=listr8,
                     fr="Cr�ation d'une liste d'amortissements modaux calcul�s selon la r�gle du RCC-G",
                     docu="U4.52.13-c",reentrant='n',
         ENER_SOL        =FACT(statut='o',min=01,max=01,
           regles=(UN_PARMI('GROUP_NO_RADIER','GROUP_MA_RADIER'),
                   PRESENT_ABSENT('COEF_GROUP','FONC_GROUP'),
#  Peut-on remplacer les deux r�gles suivantes par un ENSEMBLE_('KRX','KRY','KRZ')
                   PRESENT_PRESENT('KRX','KRY'),
                   PRESENT_PRESENT('KRX','KRZ'),
                   PRESENT_ABSENT('COOR_CENTRE','NOEUD_CENTRE'),
                   PRESENT_ABSENT('GROUP_NO_CENTRE','NOEUD_CENTRE'),
                   PRESENT_ABSENT('GROUP_NO_CENTRE','COOR_CENTRE'),),
           METHODE         =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL","RIGI_PARASOL") ),
           MODE_MECA       =SIMP(statut='o',typ=mode_meca ),
           GROUP_NO_RADIER =SIMP(statut='f',typ=grno,max='**'),
           GROUP_MA_RADIER =SIMP(statut='f',typ=grma,max='**'),
           FONC_GROUP      =SIMP(statut='f',typ=fonction ),
           COEF_GROUP      =SIMP(statut='f',typ='R',max='**'),
           KX              =SIMP(statut='o',typ='R' ),
           KY              =SIMP(statut='o',typ='R' ),
           KZ              =SIMP(statut='o',typ='R' ),
           KRX             =SIMP(statut='f',typ='R' ),
           KRY             =SIMP(statut='f',typ='R' ),
           KRZ             =SIMP(statut='f',typ='R' ),
           GROUP_NO_CENTRE =SIMP(statut='f',typ=grno),
           NOEUD_CENTRE    =SIMP(statut='f',typ=no),
           COOR_CENTRE     =SIMP(statut='f',typ='R',max=03),
         ),
         AMOR_INTERNE    =FACT(statut='o',min=01,max=01,
           ENER_POT        =SIMP(statut='o',typ=tabl_ener_pot ),
           GROUP_MA        =SIMP(statut='o',typ=grma,max='**'),
           AMOR_REDUIT     =SIMP(statut='o',typ='R',max='**'),
         ),
         AMOR_SOL        =FACT(statut='o',min=01,max=01,
           AMOR_REDUIT     =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           FONC_AMOR_GEO   =SIMP(statut='o',typ=fonction,max='**' ),
           HOMOGENE        =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           SEUIL           =SIMP(statut='f',typ='R',defaut= 0.3 ),
         ),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE JMBHH01 J.M.PROIX
def calc_cham_elem_prod(OPTION,**args):

# options mecaniques
  if OPTION == "DEGE_ELNO_DEPL" : return cham_elem_epsi_r
  if OPTION == "ECIN_ELEM_DEPL" : return cham_elem_ener_r
  if OPTION == "EFGE_ELNO_CART" : return cham_elem_sief_r
  if OPTION == "EFGE_ELNO_DEPL" : return cham_elem_sief_r
  if OPTION == "ENDO_ELNO_SIGM" : return cham_elem_sief_r
  if OPTION == "EPOT_ELEM_DEPL" : return cham_elem_ener_r
  if OPTION == "ENEL_ELGA" :      return cham_elem_ener_r
  if OPTION == "ENEL_ELNO_ELGA" : return cham_elem_ener_r
  if OPTION == "EPSI_ELNO_DEPL" : return cham_elem_epsi_r
  if OPTION == "EQUI_ELGA_EPSI" : return cham_elem_epsi_r
  if OPTION == "EQUI_ELGA_SIGM" : return cham_elem_sief_r
  if OPTION == "EQUI_ELNO_EPSI" : return cham_elem_epsi_r
  if OPTION == "EQUI_ELNO_SIGM" : return cham_elem_sief_r
  if OPTION == "PRES_DBEL_DEPL" : return cham_elem_dbel_r
  if OPTION == "SIEF_ELGA_DEPL" : return cham_elem_sief_r
  if OPTION == "SIEF_ELGA_LAGR" : return cham_elem_sief_r
  if OPTION == "SIGM_ELNO_CART" : return cham_elem_sief_r
  if OPTION == "SIGM_ELNO_DEPL" : return cham_elem_sief_r
  if OPTION == "SIGM_ELNO_LAGR" : return cham_elem_sief_r
  if OPTION == "SIPO_ELNO_DEPL" : return cham_elem_sief_r

# options thermiques

  if OPTION == "FLUX_ELGA_TEMP" : return cham_elem_flux_r
  if OPTION == "FLUX_ELNO_TEMP" : return cham_elem_flux_r
  if OPTION == "SOUR_ELGA_ELEC" : return cham_elem_sour_r

# options acoustiques

  if OPTION == "PRES_ELNO_DBEL" : return cham_elem_dbel_r
  if OPTION == "PRES_ELNO_REEL" : return cham_elem_pres_r
  if OPTION == "PRES_ELNO_IMAG" : return cham_elem_pres_r

# autres options

  if OPTION == "COOR_ELGA" :      return cham_elem_geom_r

  raise AsException("type de concept resultat non prevu")

CALC_CHAM_ELEM=OPER(nom="CALC_CHAM_ELEM",op=38,sd_prod=calc_cham_elem_prod,
                    fr="Calcul de champs par �l�ments � partir de champs solution ou de champs par �l�ments",
                    docu="U4.81.03-f",reentrant='n',
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),

         regles=(EXCLUS('TOUT','GROUP_MA',),EXCLUS('TOUT','MAILLE',),),
         TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         MAILLE          =SIMP(statut='f',typ=ma,max='**'),

#
#
#  introduire un mot cle de type modelisation : m�canique,thermique,...
#

         OPTION          =SIMP(statut='o',typ='TXM',
                               into=("DEGE_ELNO_DEPL","ECIN_ELEM_DEPL","EFGE_ELNO_CART",
                                     "EFGE_ELNO_DEPL","ENDO_ELNO_SIGM","EPOT_ELEM_DEPL",
                                     "ENEL_ELGA",     "ENEL_ELNO_ELGA","EPSI_ELNO_DEPL",
                                     "EQUI_ELGA_EPSI","EQUI_ELGA_SIGM","EQUI_ELNO_EPSI",
                                     "EQUI_ELNO_SIGM","PRES_DBEL_DEPL","SIEF_ELGA_DEPL",
                                     "SIEF_ELGA_LAGR","SIGM_ELNO_CART","SIGM_ELNO_DEPL",
                                     "SIGM_ELNO_LAGR","SIPO_ELNO_DEPL",
                                     "FLUX_ELGA_TEMP","FLUX_ELNO_TEMP","SOUR_ELGA_ELEC",
                                     "PRES_ELNO_DBEL","PRES_ELNO_REEL","PRES_ELNO_IMAG",
                                     "COOR_ELGA"), ),

         b_dege_elno_depl  =BLOC(condition="OPTION=='DEGE_ELNO_DEPL'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_r,)),
           PLAN            =SIMP(statut='o',typ='TXM',defaut="MAIL", into=("SUP","INF","MOY","MAIL"), ),
         ),

         b_ecin_elem_depl  =BLOC(condition="OPTION=='ECIN_ELEM_DEPL'",
           regles=(UN_PARMI('VITE','DEPL',),ENSEMBLE('DEPL','FREQ',),),
           FREQ            =SIMP(statut='f',typ='R'),
           VITE            =SIMP(statut='f',typ=cham_no_depl_r),
           DEPL            =SIMP(statut='f',typ=(cham_no_depl_r,cham_no_depl_c)),
         ),

         b_efge_elno_cart  =BLOC(condition="OPTION=='EFGE_ELNO_CART'",
           CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_sief_r,) ),
           PLAN            =SIMP(statut='o',typ='TXM',defaut="MAIL", into=("SUP","INF","MOY","MAIL"), ),
         ),

         b_efge_elno_depl  =BLOC(condition="OPTION=='EFGE_ELNO_DEPL'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_r,)),
           PLAN            =SIMP(statut='o',typ='TXM',defaut="MAIL", into=("SUP","INF","MOY","MAIL"), ),
         ),

         b_endo_elno_sigm  =BLOC(condition="OPTION=='ENDO_ELNO_SIGM'",
           CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_sief_r,) ),
         ),

         b_epot_elem_depl  =BLOC(condition="OPTION=='EPOT_ELEM_DEPL'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_r,)),
         ),

         b_enel_elga       =BLOC(condition="OPTION=='ENEL_ELGA'",
           CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_sief_r,) ),
         ),

         b_enel_elno_elga  =BLOC(condition="OPTION=='ENEL_ELNO_ELGA'",
           CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_sief_r,) ),
         ),

         b_epsi_elno_depl  =BLOC(condition="OPTION=='EPSI_ELNO_DEPL'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_r,)),
         ),

         b_equi_elga_epsi  =BLOC(condition="OPTION=='EQUI_ELGA_EPSI'",
           CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_epsi_r,) ),
         ),

         b_equi_elga_sigm  =BLOC(condition="OPTION=='EQUI_ELGA_SIGM'",
           CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_sief_r,) ),
         ),

         b_equi_elno_epsi  =BLOC(condition="OPTION=='EQUI_ELNO_EPSI'",
           CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_epsi_r,) ),
         ),

         b_equi_elno_sigm  =BLOC(condition="OPTION=='EQUI_ELNO_SIGM'",
           CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_sief_r,) ),
         ),

         b_pres_dbel_depl  =BLOC(condition="OPTION=='PRES_DBEL_DEPL'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_c,)),
         ),

         b_sief_elga_depl  =BLOC(condition="OPTION=='SIEF_ELGA_DEPL'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_r,)),
         ),

         b_sief_elga_lagr  =BLOC(condition="OPTION=='SIEF_ELGA_LAGR'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_r,)),
           THETA           =SIMP(statut='o',typ=(theta_geom,)),
           PROPAGATION     =SIMP(statut='f',typ='R',defaut=0.E+0),
         ),

         b_sigm_elno_cart  =BLOC(condition="OPTION=='SIGM_ELNO_CART'",
           CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_sief_r,) ),
         ),

         b_sigm_elno_depl  =BLOC(condition="OPTION=='SIGM_ELNO_DEPL'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_r,) ),
         ),

         b_sigm_elno_lagr  =BLOC(condition="OPTION=='SIGM_ELNO_LAGR'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_r,)),
           THETA           =SIMP(statut='o',typ=(theta_geom,)),
           PROPAGATION     =SIMP(statut='f',typ='R',defaut=0.E+0),
         ),

         b_sipo_elno_depl  =BLOC(condition="OPTION=='SIPO_ELNO_DEPL'",
           DEPL            =SIMP(statut='o',typ=(cham_no_depl_r,)),
         ),

         b_thermique  =BLOC(condition="OPTION in ('FLUX_ELNO_TEMP','FLUX_ELGA_TEMP','SOUR_ELGA_ELEC',)",
           TEMP            =SIMP(statut='o',typ=(cham_no_temp_r,)),
         ),

         b_acoustique  =BLOC(condition="OPTION in ('PRES_ELNO_DBEL','PRES_ELNO_REEL','PRES_ELNO_IMAG',)",
           PRES            =SIMP(statut='o',typ=(cham_no_pres_c,)),
         ),



         EXCIT           =FACT(statut='f',min=01,max='**',
               regles=(EXCLUS('FONC_MULT','COEF_MULT', ),),
               CHARGE          =SIMP(statut='o',typ=(char_meca,char_ther,char_acou)),
               FONC_MULT       =SIMP(statut='f',typ=fonction),
               COEF_MULT       =SIMP(statut='f',typ='R'), ),

         INST            =SIMP(statut='f',typ='R',defaut= 0.E+0),
         ACCE            =SIMP(statut='f',typ=cham_no_depl_r),
         NUME_COUCHE     =SIMP(statut='f',typ='I',defaut= 1),
         NIVE_COUCHE     =SIMP(statut='f',typ='TXM',defaut="MOY",into=("SUP","INF","MOY") ),
         MODE_FOURIER    =SIMP(statut='f',typ='I',defaut= 0 ),
         ANGLE           =SIMP(statut='f',typ='I',defaut= 0),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def calc_char_cine_prod(CHAR_CINE,**args):
  if AsType(CHAR_CINE) == char_cine_meca : return cham_no_depl_r
  if AsType(CHAR_CINE) == char_cine_ther : return cham_no_temp_r
  if AsType(CHAR_CINE) == char_cine_acou : return cham_no_pres_c
  raise AsException("type de concept resultat non prevu")

CALC_CHAR_CINE=OPER(nom="CALC_CHAR_CINE",op= 102,sd_prod=calc_char_cine_prod,
                    fr="Calcul des seconds membres associ�s � des charges cin�matiques (conditions aux limites non dualis�es)",
                    docu="U4.61.03-e",reentrant='n',
         NUME_DDL        =SIMP(statut='o',typ=nume_ddl ),
         CHAR_CINE       =SIMP(statut='o',typ=(char_cine_meca,char_cine_ther,char_cine_acou ) ),
         INST            =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ) ),
)  ;
#& MODIF COMMANDE  DATE 28/03/2001   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def calc_char_seisme_prod(MATR_MASS,**args ):
  if AsType(MATR_MASS) == matr_asse_depl_r : return cham_no_depl_r
  raise AsException("type de concept resultat non prevu")

CALC_CHAR_SEISME=OPER(nom="CALC_CHAR_SEISME",op=  92,sd_prod=calc_char_seisme_prod,
                      docu="U4.63.01-e",reentrant='n',
         regles=(UN_PARMI('MONO_APPUI','MODE_STAT' ),),
         MATR_MASS       =SIMP(statut='o',typ=matr_asse_depl_r,fr="Matrice de masse" ),
         DIRECTION       =SIMP(statut='o',typ='R',max=06,fr="Directions du s�isme impos�"),
         MONO_APPUI      =SIMP(statut='f',typ='TXM',into=("OUI",) ),         
         MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc,) ),
         b_mode_stat     =BLOC ( condition = "MODE_STAT != None",
           regles=(UN_PARMI('NOEUD','GROUP_NO' ),),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 04/12/2001   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE JMBHH01 J.M.PROIX
def calc_elem_prod(RESULTAT,**args):
   if AsType(RESULTAT) != None : return AsType(RESULTAT)
   raise AsException("type de concept resultat non prevu")

CALC_ELEM=OPER(nom="CALC_ELEM",op=58,sd_prod=calc_elem_prod,docu="U4.81.01-f1",reentrant='f',
                    fr="Compl�ter un r�sultat en calculant des champs par �l�ments (contraintes, d�formations,... )",
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),

         TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         MAILLE          =SIMP(statut='f',typ=ma,max='**'),

         regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','FREQ','NUME_MODE',
                        'NOEUD_CMP','LIST_INST','LIST_FREQ','LIST_ORDRE','NOM_CAS'),),
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
         NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
         NOEUD_CMP       =SIMP(statut='f',typ='TXM',max='**'),
         NOM_CAS         =SIMP(statut='f',typ='TXM' ),
 
         INST            =SIMP(statut='f',typ='R',max='**'),
         FREQ            =SIMP(statut='f',typ='R',max='**'),
         LIST_INST       =SIMP(statut='f',typ=listr8),
         LIST_FREQ       =SIMP(statut='f',typ=listr8),
         PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3 ),
         CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU",) ),

         LIST_ORDRE      =SIMP(statut='f',typ=listis),

         OPTION          =SIMP(statut='o',typ='TXM',max='**',
                               into=("EFGE_ELNO_DEPL","EPOT_ELEM_DEPL","SIGM_ELNO_DEPL","SIEF_ELGA_DEPL",
                                     "SIGM_ELNO_TUYO","SIGM_ELNO_CART","DEGE_ELNO_DEPL","EFGE_ELNO_CART",
                                     "EPSI_ELNO_DEPL","EPSI_ELGA_DEPL","EPSG_ELNO_DEPL","EPSG_ELGA_DEPL",
                                     "EPME_ELNO_DEPL","EPME_ELGA_DEPL","EPMG_ELNO_DEPL","EPMG_ELGA_DEPL",
                                     "EPSP_ELNO","EPSP_ELGA","ECIN_ELEM_DEPL","SIPO_ELNO_DEPL",
                                     "EPGR_ELNO","EPGR_ELGA","DURT_ELGA_META","DURT_ELNO_META",
                                     "SIGM_ELNO_COQU","SIGM_ELNO_SIEF","SIPO_ELNO_SIEF",
                                     "SIGM_NOZ1_ELGA","ERRE_ELEM_NOZ1","SIGM_NOZ2_ELGA","ERRE_ELEM_NOZ2",
                                     "VNOR_ELEM_DEPL","SIRE_ELNO_DEPL","ERRE_ELGA_NORE","ERRE_ELNO_ELGA",
                                     "VARI_ELNO_ELGA","VARI_ELNO_TUYO","EQUI_ELNO_SIGM","EQUI_ELGA_SIGM",
                                     "EQUI_ELNO_EPSI","EQUI_ELGA_EPSI","EQUI_ELNO_EPME","EQUI_ELGA_EPME",
                                     "DCHA_ELNO_SIGM","DCHA_ELGA_SIGM","RADI_ELNO_SIGM","RADI_ELGA_SIGM",
                                     "ENDO_ELNO_SIGA","ENDO_ELNO_SINO","ENEL_ELGA","ENEL_ELNO_ELGA","SIEF_ELNO_ELGA",
                                     "DEUL_ELGA_TEMP","DETE_ELNO_DLTE","DEUL_ELGA_DEPL","DEDE_ELNO_DLDE",
                                     "DESI_ELNO_DLSI","PMPB_ELNO_SIEF","PMPB_ELGA_SIEF",
                                     "FLUX_ELGA_TEMP","FLUX_ELNO_TEMP","HYDR_ELNO_ELGA",
                                     "SOUR_ELGA_ELEC",
                                     "PRES_ELNO_DBEL","PRES_DBEL_DEPL","PRES_ELNO_REEL","PRES_ELNO_IMAG",
                                     "INTE_ELNO_ACTI","INTE_ELNO_REAC","ERTH_ELEM_TEMP","ERTH_ELNO_ELEM"
                                     ) ),
         RESULTAT        =SIMP(statut='o',typ=(evol_elas,dyna_trans,dyna_harmo,mode_meca,
                                    mode_stat,mode_stat_depl,mode_stat_acce,mode_stat_forc,
                                    evol_noli,mult_elas,fourier_elas,
                                               evol_ther,base_modale,
                                               acou_harmo,mode_acou,mode_flamb) ),
         EXCIT           =FACT(statut='f',min=1,max='**',
             regles=(EXCLUS('FONC_MULT','FONC_MULT_C','COEF_MULT','COEF_MULT_C'),),
             CHARGE          =SIMP(statut='o',typ=(char_meca,char_ther,char_acou) ),
             FONC_MULT       =SIMP(statut='f',typ=fonction),
             FONC_MULT_C     =SIMP(statut='f',typ=fonction_c),
             COEF_MULT       =SIMP(statut='f',typ='R'),
             COEF_MULT_C     =SIMP(statut='f',typ='C'),
             PHAS_DEG        =SIMP(statut='f',typ='R'),
             PUIS_PULS       =SIMP(statut='f',typ='I'),
             TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FIXE",into=("FIXE",) ),
         ),
         NORME           =SIMP(statut='f',typ='TXM',defaut="VMIS",
                               into=("VMIS","TOTAL","VMIS_CINE","TOTAL_CINE") ),
         NUME_COUCHE     =SIMP(statut='f',typ='I',defaut= 1 ),
         NIVE_COUCHE     =SIMP(statut='f',typ='TXM',defaut="MOY",into=("SUP","INF","MOY") ),
          
         ANGLE           =SIMP(statut='f',typ='I',defaut= 0 ),
         PLAN            =SIMP(statut='f',typ='TXM',defaut="MAIL",into=("SUP","INF","MOY","MAIL") ),
         SENSIBILITE     =SIMP(statut='f',typ=(para_sensi,theta_geom),max='**',
                               fr="Liste des param�tres de sensibilit�.",
                               ang="List of sensitivity parameters"),
         TAILLE_BLOC     =SIMP(statut='f',typ='R',defaut= 400.),
         
         TEMP_INIT       =FACT(statut='f',min=1,max='**',
             regles=(EXCLUS('META_INIT','EVOL_THER'),),
             META_INIT       =SIMP(statut='f',typ=carte_meta_r),
             EVOL_THER       =SIMP(statut='f',typ=evol_ther,),
             NUME_INIT       =SIMP(statut='f',typ='I'),
         ),
         PARM_THETA      =SIMP(statut='f',typ='R',defaut= 0.57,),         
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),                 
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_FATIGUE=OPER(nom="CALC_FATIGUE",op= 151,sd_prod=cham_elem_dommag,reentrant='n',
                  fr="Calcul d un champ de dommage subi par une structure",
                  docu="U4.83.02-c",
      regles=(PRESENT_PRESENT('DOMMAGE','MATER', ),),
         OPTION          =SIMP(statut='o',typ='TXM',
                               into=("DOMA_ELNO_SIGM","DOMA_ELGA_SIGM",
                                     "DOMA_ELNO_EPSI","DOMA_ELGA_EPSI",
                                     "DOMA_ELNO_EPME","DOMA_ELGA_EPME") ),
         HISTOIRE        =FACT(statut='o',min=01,max=01,
           RESULTAT        =SIMP(statut='o',typ=(evol_elas,dyna_trans,evol_noli) ),
           EQUI_GD         =SIMP(statut='f',typ='TXM',defaut="VMIS_SG",into=("VMIS_SG","INVA_2_SG") ),
         ),
         DOMMAGE         =SIMP(statut='o',typ='TXM',
                               into=("WOHLER","MANSON_COFFIN","TAHERI_MANSON","TAHERI_MIXTE",) ),
         MATER           =SIMP(statut='o',typ=(mater) ),
         TAHERI_NAPPE    =SIMP(statut='f',typ=(fonction) ),
         TAHERI_FONC     =SIMP(statut='f',typ=(fonction) ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 23/04/2001   AUTEUR MCOURTOI M.COURTOIS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_FLUI_STRU=OPER(nom="CALC_FLUI_STRU",op= 144,sd_prod=melasflu,
                    docu="U4.66.02-d",reentrant='n',
         VITE_FLUI       =FACT(statut='o',min=01,max=01,
                               fr="D�finir la plage de vitesse fluide �tudi�e",
           VITE_MIN        =SIMP(statut='o',typ='R' ),
           VITE_MAX        =SIMP(statut='o',typ='R' ),
           NB_POIN         =SIMP(statut='o',typ='I' ),
         ),
         BASE_MODALE     =FACT(statut='o',min=01,max=01,
                               
           regles=(UN_PARMI('AMOR_REDUIT','AMOR_UNIF'),),
           MODE_MECA       =SIMP(statut='o',typ=mode_meca ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),
           AMOR_UNIF       =SIMP(statut='f',typ='R' ),
         ),
         TYPE_FLUI_STRU  =SIMP(statut='o',typ=type_flui_stru ),
         IMPRESSION      =FACT(statut='f',min=01,max=01,
                               fr="Choix des informations � imprimer dans le fichier RESULTAT",
           PARA_COUPLAGE   =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           DEFORMEE        =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         ),
)  ;
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_FONC_INTERP=OPER(nom="CALC_FONC_INTERP",op= 134,sd_prod=fonction,
                      docu="U4.32.01-d1",reentrant='f',
         regles=(UN_PARMI('VALE_R','LIST_PARA'),),
         FONCTION        =SIMP(statut='o',typ=fonction ),
         NOM_RESU        =SIMP(statut='f',typ='TXM',defaut="TOUTRESU"),
         VALE_R          =SIMP(statut='f',typ='R',max='**'),
         LIST_PARA       =SIMP(statut='f',typ=listr8 ),
         INTERPOL        =SIMP(statut='f',typ='TXM',max=2,defaut="LIN",into=("NON","LIN","LOG","INT") ),
         PROL_DROITE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("EXCLU","CONSTANT","LINEAIRE","INTERPRE") ),
         PROL_GAUCHE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("EXCLU","CONSTANT","LINEAIRE","INTERPRE") ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ) ),
)  ;
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE MCOURTOI M.COURTOIS
def calc_fonction_prod(DERIVE,EXTRACTION,INTEGRE,RMS,NOCI_SEISME,MAX,COMB,COMB_C,ENVELOPPE,SPEC_OSCI,ASSE,FFT,COMPOSE,**args):
  if (RMS != None)        : return tabl_fonc_rms
  if (MAX != None)        : return tabl_fonc_max
  if (NOCI_SEISME != None): return tabl_fonc_noci
  if (INTEGRE != None)    : return fonction
  if (DERIVE != None)     : return fonction
  if (COMB != None)       : return fonction
  if (ENVELOPPE != None)  : return fonction
  if (EXTRACTION != None) : return fonction
  if (SPEC_OSCI != None)  : return fonction
  if (COMB_C != None)     : return fonction_c
  if (COMPOSE != None)    : return fonction
  if (ASSE != None)       : return fonction
  if (FFT != None)        : 
     vale=FFT.get_child('FONCTION').get_valeur()
     if (AsType(vale) == fonction )  : return fonction_c
     if (AsType(vale) == fonction_c) : return fonction
  raise AsException("type de concept resultat non prevu")

CALC_FONCTION=OPER(nom="CALC_FONCTION",op=  91,sd_prod=calc_fonction_prod
                    ,fr="Op�rations math�matiques sur des concepts de type fonction",
                     docu="U4.32.04-e1",reentrant='n',
         regles=(UN_PARMI('DERIVE','INTEGRE','SPEC_OSCI','MAX','COMB','COMB_C','ENVELOPPE','RMS',
                          'NOCI_SEISME','COMPOSE','EXTRACTION','ASSE','FFT' ),),
         FFT             =FACT(statut='f',min=1,max=1,fr="Calcul de la transformee de Fourier ou de son inverse",
           FONCTION        =SIMP(statut='o',typ=(fonction,fonction_c) )
         ),
         DERIVE          =FACT(statut='f',min=1,max=1,fr="Calcul de la d�riv�e d une fonction",
           METHODE         =SIMP(statut='f',typ='TXM',defaut="DIFF_CENTREE",into=("DIFF_CENTREE",) ),
           FONCTION        =SIMP(statut='o',typ=fonction ),
         ),
         INTEGRE         =FACT(statut='f',min=1,max=1,fr="Calcul de l int�grale d une fonction",
           METHODE         =SIMP(statut='f',typ='TXM',defaut="TRAPEZE",into=("SIMPSON","TRAPEZE") ),
           FONCTION        =SIMP(statut='o',typ=fonction),
           COEF            =SIMP(statut='f',typ='R',defaut= 0.E+0,fr="Valeur de la constante d int�gration" ),
         ),
         RMS             =FACT(statut='f',min=1,max=1,fr="Calcul de la valeur RMS d une fonction",
           METHODE         =SIMP(statut='f',typ='TXM',defaut="TRAPEZE",into=("SIMPSON","TRAPEZE") ),
           FONCTION        =SIMP(statut='o',typ=fonction ),
           INST_INIT       =SIMP(statut='f',typ='R',fr="Instant initial d�finissant le d�but du signal" ),
           INST_FIN        =SIMP(statut='f',typ='R',fr="Instant final d�finissant la fin du signal" ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
         ),
         NOCI_SEISME     =FACT(statut='f',min=1,max=1,
           FONCTION        =SIMP(statut='f',typ=fonction ),
           SPEC_OSCI       =SIMP(statut='f',typ=fonction ),
           OPTION          =SIMP(statut='f',typ='TXM',defaut="TOUT",max='**',
                                 into=("INTE_ARIAS","POUV_DEST","INTE_SPEC","VITE_ABSO_CUMU",
                                       "DUREE_PHAS_FORT","MAXI","ACCE_SUR_VITE","TOUT",) ),
           INST_INIT       =SIMP(statut='f',typ='R'),
           INST_FIN        =SIMP(statut='f',typ='R'),
           NATURE          =SIMP(statut='f',typ='TXM',into=("DEPL","VITE","ACCE") ),
           COEF            =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           PESANTEUR       =SIMP(statut='f',typ='R',defaut= 9.81E+0 ),
           FREQ_INIT       =SIMP(statut='f',typ='R',defaut= 4.E-1 ),
           FREQ_FIN        =SIMP(statut='f',typ='R',defaut= 10.E+0 ),
           AMOR_REDUIT     =SIMP(statut='f',typ='R'),
           LIST_FREQ       =SIMP(statut='f',typ=listr8 ),
           FREQ            =SIMP(statut='f',typ='R',max='**'),
           NORME           =SIMP(statut='f',typ='R',defaut= 1.E+0 ),
           BORNE_INF       =SIMP(statut='f',typ='R',defaut= 0.05E+0 ),
           BORNE_SUP       =SIMP(statut='f',typ='R',defaut= 0.95E+0 ),
           b_acce_reel     =BLOC(condition="(INST_INIT != None)or(INST_FIN != None)or(FREQ_INIT != None)or(FREQ_FIN != None)",
             PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           ),
         ),
         SPEC_OSCI       =FACT(statut='f',min=1,max=1,fr="Calcul du spectre d oscillateur",
           METHODE         =SIMP(statut='f',typ='TXM',defaut="NIGAM",into=("NIGAM",) ),
           FONCTION        =SIMP(statut='o',typ=fonction ),
           AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),
           LIST_FREQ       =SIMP(statut='f',typ=listr8 ),
           FREQ            =SIMP(statut='f',typ='R',max='**'),
           NORME           =SIMP(statut='f',typ='R',defaut= 9.81E+0,fr="Valeur de la norme du spectre d oscillateur" ),
           NATURE          =SIMP(statut='f',typ='TXM',defaut="ACCE",into=("DEPL","VITE","ACCE") ),
           NATURE_FONC     =SIMP(statut='f',typ='TXM',defaut="ACCE",into=("DEPL","VITE","ACCE") ),
         ),
         MAX             =FACT(statut='f',min=1,max=1,fr="Calcul des extr�mas locaux d une fonction",
           FONCTION        =SIMP(statut='o',typ=fonction ),
         ),
         COMB            =FACT(statut='f',min=1,max='**',fr="Calcul d une combinaison lin�aire r�elle de fonctions",
           FONCTION        =SIMP(statut='o',typ=fonction ),
           COEF            =SIMP(statut='o',typ='R',fr="Coefficient r�el de la combinaison lin�aire associ�e � la fonction" ),
         ),
         COMB_C          =FACT(statut='f',min=1,max='**',fr="Calcul d une combinaison lin�aire complexe de fonctions",
           regles=(UN_PARMI('COEF_R','COEF_C'),),
           FONCTION        =SIMP(statut='o',typ=(fonction, fonction_c) ),
           COEF_R          =SIMP(statut='f',typ='R',fr="Coefficient r�el de la combinaison lin�aire associ�e � la fonction" ),
           COEF_C          =SIMP(statut='f',typ='C',fr="Coefficient complexe de la combinaison lin�aire associ�e � la fonction" ),
         ),
         b_comb          =BLOC ( condition = " (COMB != None) or (COMB_C != None)",
             LIST_PARA      =SIMP(statut='f',typ=listr8 ),  
         ),
         COMPOSE         =FACT(statut='f',min=1,max=1,fr="Calcul de la composition de deux fonctions FONC_RESU(FONC_PARA)",
           FONC_RESU       =SIMP(statut='o',typ=fonction),
           FONC_PARA       =SIMP(statut='o',typ=fonction),
         ),
         EXTRACTION      =FACT(statut='f',min=1,max=1,fr="Op�ration d extraction sur une fonction complexe",
           FONCTION        =SIMP(statut='o',typ=fonction_c),
           PARTIE          =SIMP(statut='o',typ='TXM',into=("REEL","IMAG","MODULE","PHASE"),fr="Partie � extraire"),
         ),
         ENVELOPPE       =FACT(statut='f',min=1,max=1,fr="Calcul de l enveloppe d une famille de fonctions",
           FONCTION        =SIMP(statut='o',typ=fonction,max='**' ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="SUP",into=("SUP","INF"),fr="Type de l enveloppe" ),
         ),
         ASSE            =FACT(statut='f',min=1,max=1,fr="Cr�ation � partir de la concatenation de fonctions",
           FONCTION        =SIMP(statut='o',typ=fonction,max='**' ),
           SURCHARGE       =SIMP(statut='f',typ='TXM',defaut="DROITE",into=("DROITE","GAUCHE")),
         ),
         NOM_PARA        =SIMP(statut='f',typ='TXM',into=("DX","DY","DZ","DRX","DRY","DRZ","TEMP",
                                                          "INST","X","Y","Z","EPSI","FREQ","PULS",
                                                          "AMOR","ABSC") ),
         NOM_RESU        =SIMP(statut='f',typ='TXM' ),
         INTERPOL        =SIMP(statut='f',typ='TXM',max=2,into=("NON","LIN","LOG") ),
         PROL_DROITE     =SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         PROL_GAUCHE     =SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         NOM_PARA_FONC   =SIMP(statut='f',typ='TXM',into=("DX","DY","DZ","DRX","DRY","DRZ","TEMP",
                                                          "INST","X","Y","Z","EPSI","FREQ","PULS",
                                                          "AMOR","ABSC") ),
         INTERPOL_FONC   =SIMP(statut='f',typ='TXM',max=2,into=("NON","LIN","LOG") ),
         PROL_DROITE_FONC=SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         PROL_GAUCHE_FONC=SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_FORC_AJOU=OPER(nom="CALC_FORC_AJOU",op=199,sd_prod=vect_asse_gene,
                   fr="calcul de la force ajoutee ",
                   docu="U4.66.03-a",reentrant ='n',

        regles=(EXCLUS('MODE_MECA','MODELE_GENE'),
                PRESENT_PRESENT( 'MODELE_GENE','NUME_DDL_GENE'),
                UN_PARMI('MONO_APPUI', 'NOEUD','GROUP_NO'),
                UN_PARMI('MONO_APPUI','MODE_STAT')),

         MODELE_FLUIDE   =SIMP(statut='o',typ=modele ),
         MODELE_INTERFACE=SIMP(statut='o',typ=modele ),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater ),
         CHARGE          =SIMP(statut='o',typ=char_ther ),
         MODE_MECA       =SIMP(statut='f',typ=mode_meca ),
         MODELE_GENE     =SIMP(statut='f',typ=modele_gene ),
         NUME_DDL_GENE   =SIMP(statut='f',typ=nume_ddl_gene ),
         DIST_REFE       =SIMP(statut='f',typ='R',defaut= 1.E-2 ),
         AVEC_MODE_STAT  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         NUME_MODE_MECA  =SIMP(statut='f',typ='I',max='**'),
         POTENTIEL       =SIMP(statut='f',typ=evol_ther ),
         NOEUD_DOUBLE    =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),

         DIRECTION       =SIMP(statut='o',typ='R',max=3),
         MONO_APPUI      =SIMP(statut='f',typ='TXM',into=("OUI",),),
         NOEUD           =SIMP(statut='f',typ=no,max='**'),
         GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
         MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc,),),

         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ) ),

         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    = BLOC ( condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt          =BLOC( condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
           ),
           b_ldlt_mult     =BLOC( condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non iversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
           b_gcpc          =BLOC (condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut=0),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
#  A quoi sert eps
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0),  ),

           ) ;
#& MODIF COMMANDE  DATE 12/09/2001   AUTEUR MCOURTOI M.COURTOIS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_G_LOCAL_T=OPER(nom="CALC_G_LOCAL_T",op=77,sd_prod=tabl_calc_g_loca,
                    fr="Calcul du taux de restitution local d �nergie",docu="U4.82.04-e1",reentrant='n',
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater),
         FOND            =SIMP(statut='o',typ=fond_fiss),
         regles=(UN_PARMI('RESULTAT','DEPL'),
                 UN_PARMI('R_INF','R_INF_FO'),
                 PRESENT_PRESENT('R_INF','R_SUP'),
                 PRESENT_PRESENT('R_INF_FO','R_SUP_FO'), ),
                         
         DEPL            =SIMP(statut='f',typ=cham_no_depl_r),
         RESULTAT        =SIMP(statut='f',typ=(evol_elas,evol_noli),),
         b_extrac        =BLOC(condition="RESULTAT != None",fr="extraction d un champ",
             regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','LIST_ORDRE','INST','LIST_INST'),),
             TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
             LIST_ORDRE      =SIMP(statut='f',typ=listis),
             INST            =SIMP(statut='f',typ='R',max='**'),
             LIST_INST       =SIMP(statut='f',typ=listr8),
             
             b_acce_reel     =BLOC(condition="(INST != None)or(LIST_INST != None)",
               PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-6),
               CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
             ),
         ),
 
         CHARGE          =SIMP(statut='f',typ=char_meca,max='**'),
         SYME_CHAR       =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SYME","ANTI","SANS") ),
 
         COMP_ELAS       =FACT(statut='f',min=01,max=01,
               RELATION        =SIMP(statut='f',typ='TXM',defaut="ELAS",
                                     into=("ELAS","ELAS_VMIS_LINE","ELAS_VMIS_TRAC") ),
               ELAS            =SIMP(statut='f',typ='I',defaut=1,into=(1,) ),
               ELAS_VMIS_LINE  =SIMP(statut='f',typ='I',defaut=1,into=(1,) ),
               ELAS_VMIS_TRAC  =SIMP(statut='f',typ='I',defaut=1,into=(1,) ),
               DEFORMATION     =SIMP(statut='f',typ='TXM',defaut="PETIT",into=("PETIT","GREEN") ),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
               TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
               GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
               MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         ),
 
         COMP_INCR       =FACT(statut='f',min=01,max=01,
               RELATION        =SIMP(statut='f',typ='TXM',defaut="ELAS",
                                     into=("ELAS","VMIS_ISOT_TRAC","VMIS_ISOT_LINE","VMIS_CINE_LINE") ),
               ELAS            =SIMP(statut='f',typ='I',defaut=1,into=(1,) ),
               VMIS_ISOT_TRAC  =SIMP(statut='f',typ='I',defaut=2,into=(2,) ),
               VMIS_ISOT_LINE  =SIMP(statut='f',typ='I',defaut=2,into=(2,) ),
               VMIS_CINE_LINE  =SIMP(statut='f',typ='I',defaut=7,into=(7,) ),
               DEFORMATION     =SIMP(statut='f',typ='TXM',defaut="PETIT",into=("PETIT","PETIT_REAC") ),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
               TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
               GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
               MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         ),
         
         ETAT_INIT       =FACT(statut='f',min=01,max=01,
           SIGM            =SIMP(statut='f',typ=cham_elem_sief_r),
           DEPL            =SIMP(statut='f',typ=cham_no_depl_r),
         ),

         OPTION          =SIMP(statut='f',typ='TXM',defaut="CALC_G",
                               into=("CALC_G","CALC_G_LGLO","G_BILINEAIRE","CALC_G_MAX") ),
         b_g             =BLOC(condition="OPTION=='CALC_G'",
           LISSAGE_THETA   =SIMP(statut='f',typ='TXM',defaut="LEGENDRE",into=("LEGENDRE","LAGRANGE") ),
           LISSAGE_G       =SIMP(statut='f',typ='TXM',defaut="LEGENDRE",into=("LEGENDRE","LAGRANGE","LAGRANGE_NO_NO",) ),
         ), 
         b_g_lglo        =BLOC(condition="OPTION=='CALC_G_LGLO'",
           PROPAGATION     =SIMP(statut='o',typ='R'),
           THETA           =SIMP(statut='o',typ=theta_geom),
           DIRE_THETA      =SIMP(statut='f',typ=cham_no_depl_r),
           LISSAGE_THETA   =SIMP(statut='f',typ='TXM',defaut="LEGENDRE",into=("LEGENDRE","LAGRANGE") ),
           LISSAGE_G       =SIMP(statut='f',typ='TXM',defaut="LEGENDRE",into=("LEGENDRE","LAGRANGE","LAGRANGE_NO_NO",) ),
         ), 
         b_g_bilin       =BLOC(condition="OPTION=='G_BILINEAIRE'",
           LISSAGE_THETA   =SIMP(statut='f',typ='TXM',defaut="LEGENDRE",into=("LEGENDRE","LAGRANGE") ),
           LISSAGE_G       =SIMP(statut='f',typ='TXM',defaut="LEGENDRE",into=("LEGENDRE","LAGRANGE") ),
         ), 
         b_calc_g_max    =BLOC(condition="OPTION=='CALC_G_MAX'",
           BORNES          =FACT(statut='o',min=01,max='**',
              NUME_ORDRE     =SIMP(statut='o',typ='I'),
              VALE_MIN       =SIMP(statut='o',typ='R'),
              VALE_MAX       =SIMP(statut='o',typ='R'),
                                ),
           LISSAGE_THETA   =SIMP(statut='f',typ='TXM',defaut="LEGENDRE",into=("LEGENDRE","LAGRANGE") ),
           LISSAGE_G       =SIMP(statut='f',typ='TXM',defaut="LEGENDRE",into=("LEGENDRE","LAGRANGE") ),
         ),
           
         DEGRE           =SIMP(statut='f',typ='I',defaut=5,into=(0,1,2,3,4,5,6,7) ),

         R_INF           =SIMP(statut='f',typ='R'),
         R_SUP           =SIMP(statut='f',typ='R'),
         R_INF_FO        =SIMP(statut='f',typ=fonction),
         R_SUP_FO        =SIMP(statut='f',typ=fonction),
 
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 12/09/2001   AUTEUR MCOURTOI M.COURTOIS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_G_THETA_T=OPER(nom="CALC_G_THETA_T",op=53,sd_prod=tabl_calc_g_th,
                    fr="Calcul du taux de restitution d �nergie par la m�thode theta en thermo-�lasticit� en 2D ou en 3D",
                    docu="U4.82.03-e1",reentrant='n',
         regles=(UN_PARMI('RESULTAT','DEPL'),
                 EXCLUS('COMP_ELAS','COMP_INCR'),),
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater),
         THETA           =SIMP(statut='o',typ=theta_geom),
         DEPL            =SIMP(statut='f',typ=cham_no_depl_r),
         RESULTAT        =SIMP(statut='f',typ=(evol_elas,evol_noli),),

         b_extrac        =BLOC(condition="RESULTAT != None",fr="extraction d un champ",
           regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','LIST_ORDRE','INST','LIST_INST'),),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           LIST_ORDRE      =SIMP(statut='f',typ=listis),
           INST            =SIMP(statut='f',typ='R',max='**'),
           LIST_INST       =SIMP(statut='f',typ=listr8),
            
           b_acce_reel     =BLOC(condition="(INST != None)or(LIST_INST != None)",
             PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-6),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           ),
         ),

         CHARGE          =SIMP(statut='f',typ=char_meca,max='**'),
         SYME_CHAR       =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SYME","ANTI","SANS") ),
 
         COMP_ELAS       =FACT(statut='f',min=01,max=01,
               RELATION        =SIMP(statut='f',typ='TXM',defaut="ELAS",
                                     into=("ELAS","ELAS_VMIS_LINE","ELAS_VMIS_TRAC") ),
               ELAS            =SIMP(statut='f',typ='I',defaut=1,into=(1,) ),
               ELAS_VMIS_LINE  =SIMP(statut='f',typ='I',defaut=1,into=(1,) ),
               ELAS_VMIS_TRAC  =SIMP(statut='f',typ='I',defaut=1,into=(1,) ),
               DEFORMATION     =SIMP(statut='f',typ='TXM',defaut="PETIT",into=("PETIT","GREEN") ),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
               TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
               GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
               MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         ),  
         COMP_INCR       =FACT(statut='f',min=01,max=01,
               RELATION        =SIMP(statut='f',typ='TXM',defaut="ELAS",
                                     into=("ELAS","VMIS_ISOT_TRAC","VMIS_ISOT_LINE","VMIS_CINE_LINE") ),
               ELAS            =SIMP(statut='f',typ='I',defaut=1,into=(1,) ),
               VMIS_ISOT_TRAC  =SIMP(statut='f',typ='I',defaut=2,into=(2,) ),
               VMIS_ISOT_LINE  =SIMP(statut='f',typ='I',defaut=2,into=(2,) ),
               VMIS_CINE_LINE  =SIMP(statut='f',typ='I',defaut=7,into=(7,) ),
               DEFORMATION     =SIMP(statut='f',typ='TXM',defaut="PETIT",into=("PETIT","PETIT_REAC") ),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
               TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
               GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
               MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         ),
         ETAT_INIT       =FACT(statut='f',min=01,max=01,
           SIGM            =SIMP(statut='f',typ=cham_elem_sief_r),
           DEPL            =SIMP(statut='f',typ=cham_no_depl_r),
         ),
         OPTION          =SIMP(statut='f',typ='TXM',defaut="CALC_G",
                               into=("CALC_G","CALC_G_LAGR","CALC_K_G","G_BILINEAIRE","CALC_G_MAX","CALC_DG",) ),
         b_calc_g_max    =BLOC(condition="OPTION=='CALC_G_MAX'",
           BORNES          =FACT(statut='o',min=01,max='**',
                NUME_ORDRE     =SIMP(statut='o',typ='I'),
                VALE_MIN       =SIMP(statut='o',typ='R'),
                VALE_MAX       =SIMP(statut='o',typ='R'),
                                ),
         ),
         b_calc_k_g      =BLOC(condition="OPTION=='CALC_K_G'",
           FOND            =SIMP(statut='o',typ=fond_fiss),
         ),
         b_calc_g_lagr   =BLOC(condition="OPTION=='CALC_G_LAGR'",
           PROPAGATION     =SIMP(statut='o',typ='R'),
         ),
         b_calc_dg       =BLOC(condition="OPTION=='CALC_DG'",
           SENSIBILITE     =FACT(statut='f',min=01,max=01,
                 THETA          =SIMP(statut='o',typ=theta_geom ),
                               ),  
         ),

         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_INTE_SPEC=OPER(nom="CALC_INTE_SPEC",op= 120,sd_prod=tabl_intsp,
                    fr="Calcul d une matrice interspectrale d une fonction du temps",
                    docu="U4.36.03-e",reentrant='n',
         INST_INIT       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         INST_FIN        =SIMP(statut='o',typ='R' ),
         DUREE_ANALYSE   =SIMP(statut='f',typ='R' ),
         DUREE_DECALAGE  =SIMP(statut='f',typ='R' ),
         NB_POIN         =SIMP(statut='o',typ='I' ),
         FONCTION        =SIMP(statut='o',typ=fonction,max='**' ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_MATR_AJOU=OPER(nom="CALC_MATR_AJOU",op= 152,sd_prod=matr_asse_gene_r,
                    fr="Calcul des matrices de masse, d amortissement ou de raideur ajout�es",
                    docu="U4.66.01-c",reentrant='n',
         regles=(EXCLUS('MODE_MECA','CHAM_NO','MODELE_GENE'),
                 PRESENT_ABSENT('NUME_DDL_GENE','CHAM_NO'),
                 PRESENT_PRESENT('MODELE_GENE','NUME_DDL_GENE'),),
         MODELE_FLUIDE   =SIMP(statut='o',typ=modele ),
         MODELE_INTERFACE=SIMP(statut='o',typ=modele ),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater ),
         CHARGE          =SIMP(statut='o',typ=char_ther ),
         MODE_MECA       =SIMP(statut='f',typ=mode_meca ),
         CHAM_NO         =SIMP(statut='f',typ=cham_no_depl_r ),
         MODELE_GENE     =SIMP(statut='f',typ=modele_gene ),
         NUME_DDL_GENE   =SIMP(statut='f',typ=nume_ddl_gene ),
         DIST_REFE       =SIMP(statut='f',typ='R',defaut= 1.E-2 ),
         AVEC_MODE_STAT  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         NUME_MODE_MECA  =SIMP(statut='f',typ='I',max='**'),
         OPTION          =SIMP(statut='o',typ='TXM',into=("MASS_AJOU","AMOR_AJOU","RIGI_AJOU") ),
         POTENTIEL       =SIMP(statut='f',typ=evol_ther ),
         NOEUD_DOUBLE    =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ) ),

         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    = BLOC ( condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt          =BLOC( condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
           ),
           b_ldlt_mult     =BLOC( condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non iversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
           b_gcpc          =BLOC (condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut=0),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
#  A quoi sert eps
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),
)  ;
#& MODIF COMMANDE  DATE 11/12/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def calc_matr_elem_prod(OPTION,**args):
  if OPTION == "RIGI_MECA"        : return matr_elem_depl_r
  if OPTION == "RIGI_FLUI_STRU"   : return matr_elem_depl_r
  if OPTION == "RIGI_MECA_LAGR"   : return matr_elem_depl_r
  if OPTION == "MASS_ID_MDEP_R"   : return matr_elem_depl_r
  if OPTION == "MASS_ID_MDNS_R"   : return matr_elem_depl_r
  if OPTION == "MASS_ID_MTEM_R"   : return matr_elem_temp_r
  if OPTION == "MASS_ID_MTNS_R"   : return matr_elem_temp_r
  if OPTION == "MASS_MECA"        : return matr_elem_depl_r
  if OPTION == "MASS_FLUI_STRU"   : return matr_elem_depl_r
  if OPTION == "RIGI_GEOM"        : return matr_elem_depl_r
  if OPTION == "RIGI_ROTA"        : return matr_elem_depl_r
  if OPTION == "AMOR_MECA"        : return matr_elem_depl_r
  if OPTION == "IMPE_MECA"        : return matr_elem_depl_r
  if OPTION == "ONDE_FLUI"        : return matr_elem_depl_r
  if OPTION == "RIGI_MECA_HYST"   : return matr_elem_depl_c
  if OPTION == "RIGI_THER"        : return matr_elem_temp_r
  if OPTION == "MASS_THER"        : return matr_elem_temp_r
  if OPTION == "MASS_MECA_DIAG"   : return matr_elem_depl_r
  if OPTION == "RIGI_ACOU"        : return matr_elem_pres_c
  if OPTION == "MASS_ACOU"        : return matr_elem_pres_c
  if OPTION == "AMOR_ACOU"        : return matr_elem_pres_c
  raise AsException("type de concept resultat non prevu")

CALC_MATR_ELEM=OPER(nom="CALC_MATR_ELEM",op=   9,sd_prod=calc_matr_elem_prod
                    ,fr="Calcul des matrices �l�mentaires",docu="U4.61.01-f",reentrant='n',
         OPTION          =SIMP(statut='o',typ='TXM',
                               into=("RIGI_MECA","MASS_MECA","RIGI_GEOM",
                                     "AMOR_MECA","RIGI_THER","MASS_THER","IMPE_MECA",
                                     "ONDE_FLUI","MASS_FLUI_STRU","RIGI_FLUI_STRU",
                                     "RIGI_ROTA","MASS_MECA_DIAG","RIGI_ACOU",
                                     "MASS_ID_MDEP_R","MASS_ID_MDNS_R","MASS_ID_MTEM_R","MASS_ID_MTNS_R",
                                     "MASS_ACOU","AMOR_ACOU","RIGI_MECA_HYST",
                                     "RIGI_MECA_LAGR") ),

         b_rigi_meca = BLOC( condition = "OPTION=='RIGI_MECA'",
           regles=(AU_MOINS_UN('MODELE','CHARGE' ),),
           MODELE          =SIMP(statut='f',typ=modele ),
           b_modele        =BLOC(condition = "MODELE != None",
             CHAM_MATER      =SIMP(statut='f',typ=cham_mater ),
             CARA_ELEM       =SIMP(statut='f',typ=cara_elem ),
             MODE_FOURIER    =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
           CHARGE          =SIMP(statut='f',typ=char_meca,max='**' ),
           b_charge        =BLOC (condition = "CHARGE != None",
             INST            =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
         ),

         b_rigi_meca_lagr  =BLOC(condition = "OPTION=='RIGI_MECA_LAGR'",
           MODELE            =SIMP(statut='o',typ=modele ),
           CHAM_MATER        =SIMP(statut='o',typ=cham_mater ),
           CHARGE            =SIMP(statut='f',typ=char_meca,max='**'  ),
           b_charge        =BLOC(condition = "CHARGE != None",
             INST            =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
           THETA           =SIMP(statut='o',typ=theta_geom ),
           PROPAGATION     =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),

         b_mass_meca       =BLOC(condition = "(OPTION=='MASS_MECA') or (OPTION=='MASS_MECA_DIAG')",
           regles=(AU_MOINS_UN('MODELE','CHARGE'),),
           MODELE          =SIMP(statut='f',typ=modele ),
           b_modele          =BLOC(condition = "MODELE != None",
             CHAM_MATER        =SIMP(statut='f',typ=cham_mater ),
             CARA_ELEM         =SIMP(statut='f',typ=cara_elem ),
           ),
           CHARGE          =SIMP(statut='f',typ=char_meca,max='**' ),
           b_charge        =BLOC(condition = "CHARGE != None",
             INST            =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
         ),

         b_mass_identite   =BLOC(condition = "(OPTION in ('MASS_ID_MDEP_R','MASS_ID_MTEM_R','MASS_ID_MDNS_R','MASS_ID_MTNS_R')) ",
           MODELE            =SIMP(statut='o',typ=modele ),
           # j'ajoute ces 2 mot cl�s inutiles � cause de l'alarme pas assez subtile de MEDOME
           CHAM_MATER        =SIMP(statut='f',typ=cham_mater ),
           CARA_ELEM         =SIMP(statut='f',typ=cara_elem ),
         ),

         b_rigi_geom       =BLOC(condition = "OPTION=='RIGI_GEOM'",
           MODELE            =SIMP(statut='o',typ=modele ),
           CARA_ELEM         =SIMP(statut='f',typ=cara_elem ),
           SIEF_ELGA         =SIMP(statut='o',typ=cham_elem_sief_r ),
           MODE_FOURIER      =SIMP(statut='f',typ='I',defaut= 0 ),
         ),

         b_rigi_rota       =BLOC(condition = "OPTION=='RIGI_ROTA'",
           MODELE            =SIMP(statut='o',typ=modele ),
           CHAM_MATER        =SIMP(statut='o',typ=cham_mater ),
           CHARGE            =SIMP(statut='o',typ=char_meca,max='**' ),
           INST              =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),

         b_amor_meca       =BLOC(condition = "OPTION=='AMOR_MECA'",
           regles=(AU_MOINS_UN('CARA_ELEM','RIGI_MECA'),
                   ENSEMBLE('RIGI_MECA','MASS_MECA','CHAM_MATER'), ),
           MODELE            =SIMP(statut='o',typ=modele ),
           CARA_ELEM         =SIMP(statut='f',typ=cara_elem ),
           CHAM_MATER        =SIMP(statut='f',typ=cham_mater ),
           RIGI_MECA         =SIMP(statut='f',typ=matr_elem_depl_r ),
           MASS_MECA         =SIMP(statut='f',typ=matr_elem_depl_r ),
           CHARGE            =SIMP(statut='f',typ=char_meca,max='**' ),
         ),

         b_rigi_meca_hyst  =BLOC( condition = "OPTION=='RIGI_MECA_HYST'",
           MODELE            =SIMP(statut='o',typ=modele ),
           CHARGE            =SIMP(statut='o',typ=char_meca ,max='**' ),
           CHAM_MATER        =SIMP(statut='f',typ=cham_mater ),
           CARA_ELEM         =SIMP(statut='f',typ=cara_elem ),
           RIGI_MECA         =SIMP(statut='o',typ=matr_elem_depl_r ),
         ),

         b_rigi_ther       =BLOC(condition = "OPTION=='RIGI_THER'",
           regles=(AU_MOINS_UN('MODELE','CHARGE' ),),
           MODELE            =SIMP(statut='f',typ=modele ),
           b_modele          =BLOC(condition = "MODELE != None",
             CHAM_MATER        =SIMP(statut='o',typ=cham_mater ),
             CARA_ELEM         =SIMP(statut='f',typ=cara_elem ),
             MODE_FOURIER      =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
           CHARGE            =SIMP(statut='f',typ=char_ther,max='**' ),
         ),

         b_mass_ther       =BLOC(condition = "OPTION=='MASS_THER'",
           MODELE            =SIMP(statut='o',typ=modele ),
           CHAM_MATER        =SIMP(statut='o',typ=cham_mater ),
           CARA_ELEM         =SIMP(statut='f',typ=cara_elem ),
         ),

         b_rigi_acou       =BLOC(condition = "(OPTION=='RIGI_ACOU') or (OPTION=='MASS_ACOU') or (OPTION=='AMOR_ACOU')",
           MODELE            =SIMP(statut='o',typ=modele ),
           CHAM_MATER        =SIMP(statut='o',typ=cham_mater ),
           CHARGE            =SIMP(statut='f',typ=char_acou ,max='**' ),
         ),

         b_rigi_flui       =BLOC(condition = "(OPTION=='RIGI_FLUI_STRU') or (OPTION=='MASS_FLUI_STRU')",
           MODELE            =SIMP(statut='o',typ=modele ),
           CARA_ELEM         =SIMP(statut='o',typ=cara_elem ),
           CHAM_MATER        =SIMP(statut='o',typ=cham_mater ),
           CHARGE            =SIMP(statut='o',typ=char_meca ,max='**' ),
           INST              =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),

         b_impe_meca       =BLOC(condition = "(OPTION=='IMPE_MECA') or (OPTION=='ONDE_FLUI')",
           MODELE            =SIMP(statut='o',typ=modele ),
           CHARGE            =SIMP(statut='o',typ=char_meca,max='**' ),
           CHAM_MATER        =SIMP(statut='o',typ=cham_mater ),
         ),
)  ;
#& MODIF COMMANDE  DATE 27/06/2001   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_META=OPER(nom="CALC_META",op=194,sd_prod=evol_ther,docu="U4.85.01-a",reentrant='o',
               fr="Calcule la m�tallurgie a partir du r�sultat du calcul thermique",
         MODELE          =SIMP(statut='o',typ=modele ),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater ),
         RESULTAT        =SIMP(statut='o',typ=evol_ther ),
         ETAT_INIT       =FACT(statut='o',min=01,max=01,
      regles=(UN_PARMI('NUME_INIT','META_INIT',),),
           EVOL_THER       =SIMP(statut='f',typ=evol_ther ),
           NUME_INIT       =SIMP(statut='f',typ='I' ),  
           META_INIT       =SIMP(statut='f',typ=carte_var2_r ),
         ),
         COMP_INCR       =FACT(statut='o',min=01,max='**',
           RELATION        =SIMP(statut='o',typ='TXM',into=("ACIER","ZIRC",) ),
           ACIER           =SIMP(statut='c',typ='I',defaut=7,into=(7,) ),
           ZIRC            =SIMP(statut='c',typ='I',defaut=3,into=(3,) ),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma),
           MAILLE          =SIMP(statut='f',typ=ma),
         ),
         OPTION          =SIMP(statut='f',typ='TXM'     
                             ,into=("META_ELNO_TEMP",) ),
)  ;
#& MODIF COMMANDE  DATE 04/12/2001   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
def calc_no_prod(RESULTAT,**args):
   if AsType(RESULTAT) != None : return AsType(RESULTAT)
   raise AsException("type de concept resultat non prevu")

CALC_NO=OPER(nom="CALC_NO",op= 106,sd_prod=calc_no_prod,docu="U4.81.02-e1",reentrant='o',
         RESULTAT        =SIMP(statut='o',typ=(evol_elas,dyna_trans,dyna_harmo,acou_harmo,mode_meca,
                                               mode_acou,mode_stat,mode_stat_depl,mode_stat_acce,
                                              mode_stat_forc,evol_ther,evol_noli,base_modale,
                                               mult_elas,fourier_elas,mode_flamb ) ),
         SENSIBILITE     =SIMP(statut='f',typ=(para_sensi,theta_geom),max='**',
                               fr="Liste des param�tres de sensibilit�.",
                               ang="List of sensitivity parameters"),

         regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','FREQ','NUME_MODE',
                        'NOEUD_CMP','LIST_INST','LIST_FREQ','LIST_ORDRE','NOM_CAS'),),
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
         NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
         NOEUD_CMP       =SIMP(statut='f',typ='TXM',max='**'),
         NOM_CAS         =SIMP(statut='f',typ='TXM' ),
         INST            =SIMP(statut='f',typ='R',max='**'),
         FREQ            =SIMP(statut='f',typ='R',max='**'),
         LIST_INST       =SIMP(statut='f',typ=listr8),
         LIST_FREQ       =SIMP(statut='f',typ=listr8),
         PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3 ),
         CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
         LIST_ORDRE      =SIMP(statut='f',typ=listis),
           
         OPTION          =SIMP(statut='o',typ='TXM',max='**',
                               into=("FORC_NODA","REAC_NODA",
                                     "DCHA_NOEU_SIGM",
                                     "DEGE_NOEU_DEPL",
                                     "DETE_NOEU_DLTE",
                                     "DEDE_NOEU_DLDE",
                                     "DESI_NOEU_DLSI",
                                     "DURT_NOEU_META",
                                     "EFGE_NOEU_CART","EFGE_NOEU_DEPL",
                                     "ENDO_NOEU_SINO",
                                     "ENEL_NOEU_ELGA",
                                     "EPMG_NOEU_DEPL",
                                     "EPSA_NOEU",
                                     "EPSG_NOEU"     ,"EPSG_NOEU_DEPL",
                                     "EPSI_NOEU_DEPL","EPSI_NOEU_DPGE",
                                     "EPSP_NOEU"     ,"EPSP_NOEU_ZAC",
                                     "EQUI_NOEU_EPME","EQUI_NOEU_EPSI","EQUI_NOEU_SIGM",
                                     "ERRE_NOEU_ELGA",
                                     "FLUX_NOEU_TEMP",
                                     "GRAD_NOEU_THETA",
                                     "HYDR_NOEU_ELGA",
                                     "INTE_NOEU_ACTI","INTE_NOEU_REAC",
                                     "META_NOEU_TEMP",
                                     "PMPB_NOEU_SIEF",
                                     "PRES_NOEU_DBEL","PRES_NOEU_IMAG","PRES_NOEU_REEL",
                                     "RADI_NOEU_SIGM",
                                     "SIEF_NOEU"     ,"SIEF_NOEU_ELGA",
                                     "SIGM_NOEU_CART","SIGM_NOEU_COQU","SIGM_NOEU_DEPL","SIGM_NOEU_DPGE",
                                     "SIGM_NOEU_SIEF","SIGM_NOEU_VARI","SIGM_NOEU_ZAC",
                                     "SIPO_NOEU_DEPL","SIPO_NOEU_SIEF",
                                     "SIRE_NOEU_DEPL",
                                     "VARI_NOEU"     ,"VARI_NOEU_ELGA",) ),
         
         b_forc_reac     =BLOC(condition = """(OPTION == 'FORC_NODA') or (type(OPTION) == type(()) and 'FORC_NODA' in OPTION) or\
 (OPTION == 'REAC_NODA') or (type(OPTION) == type(()) and 'REAC_NODA' in OPTION)""",
             MODELE          =SIMP(statut='o',typ=modele),
         ),

         CHAM_MATER      =SIMP(statut='f',typ=cham_mater),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),
         EXCIT           =FACT(statut='f',min=1,max='**',
           CHARGE          =SIMP(statut='f',typ=(char_meca,char_ther,char_acou) ),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
           TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FIXE_CSTE",
                                 into=("FIXE_CSTE","FIXE_PILO","SUIV") ),
         ),
         TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         TAILLE_BLOC     =SIMP(statut='f',typ='R' ,defaut= 400. ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CALC_THETA=OPER(nom="CALC_THETA",op=54,sd_prod=theta_geom,docu="U4.82.02-d",reentrant='n',
                fr="Affectation d un champ sur le maillage (m�canique de la rupture)",
         regles=(UN_PARMI('THETA_2D','THETA_3D','THETA_BANDE'),
                 PRESENT_PRESENT('THETA_3D','FOND_3D'),
                 PRESENT_ABSENT('THETA_2D','DIRE_THETA'),
                 EXCLUS('DIRECTION','DIRE_THETA'),),
         OPTION          =SIMP(statut='f',typ='TXM',defaut="COURONNE",into=("COURONNE","BANDE") ),
         MODELE          =SIMP(statut='o',typ=(modele) ),
         FOND_3D         =SIMP(statut='f',typ=(fond_fiss) ),
         THETA_3D        =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_NO','NOEUD'),
                   UN_PARMI('MODULE','MODULE_FO'),
                   ENSEMBLE('MODULE','R_INF','R_SUP'),
                   ENSEMBLE('MODULE_FO','R_INF_FO','R_SUP_FO'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           MODULE          =SIMP(statut='f',typ='R'),
           R_INF           =SIMP(statut='f',typ='R'),
           R_SUP           =SIMP(statut='f',typ='R'),
           MODULE_FO       =SIMP(statut='f',typ=fonction),
           R_INF_FO        =SIMP(statut='f',typ=fonction),
           R_SUP_FO        =SIMP(statut='f',typ=fonction),
                         ),
         DIRE_THETA      =SIMP(statut='f',typ=(cham_no_depl_r) ),
         DIRECTION       =SIMP(statut='f',typ='R',max='**'),
         THETA_2D        =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('GROUP_NO','NOEUD'),),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           MODULE          =SIMP(statut='o',typ='R'),
           R_INF           =SIMP(statut='o',typ='R'),
           R_SUP           =SIMP(statut='o',typ='R'),
         ),
         THETA_BANDE     =FACT(statut='f',min=01,max='**',
           MODULE          =SIMP(statut='o',typ='R'),
           R_INF           =SIMP(statut='o',typ='R'),
           R_SUP           =SIMP(statut='o',typ='R'),
         ),
         GRAD_NOEU_THETA =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
         IMPRESSION      =FACT(statut='f',min=01,max=01,
           FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT",into=("RESULTAT",) ),
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="EXCEL",into=("EXCEL","AGRAF") ),
         ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def calc_vect_elem_prod(OPTION,**args):
  if OPTION == "CHAR_MECA" :      return vect_elem_depl_r
  if OPTION == "CHAR_MECA_LAGR" : return vect_elem_depl_r
  if OPTION == "CHAR_THER" :      return vect_elem_temp_r
  if OPTION == "CHAR_ACOU" :      return vect_elem_pres_c
  if OPTION == "FORC_NODA" :      return vect_elem_depl_r
  raise AsException("type de concept resultat non prevu")

CALC_VECT_ELEM=OPER(nom="CALC_VECT_ELEM",op=8,sd_prod=calc_vect_elem_prod,docu="U4.61.02-f",reentrant='n',
                    fr="Calcul des seconds membres �l�mentaires",
         OPTION          =SIMP(statut='o',typ='TXM',into=("CHAR_MECA","CHAR_THER","CHAR_ACOU",
                                                           "FORC_NODA","CHAR_MECA_LAGR") ),
         b_char_meca     =BLOC(condition = "OPTION=='CHAR_MECA'",
           regles=(AU_MOINS_UN('CHARGE','MODELE'),),
           CHARGE          =SIMP(statut='f',typ=char_meca,max='**'),
           MODELE          =SIMP(statut='f',typ=modele),
           b_charge     =BLOC(condition = "CHARGE != None", fr="mod�le ne contenant pas de sous-structure",
              CHAM_MATER   =SIMP(statut='f',typ=cham_mater),
              CARA_ELEM    =SIMP(statut='f',typ=cara_elem),
              INST         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
              MODE_FOURIER =SIMP(statut='f',typ='I',defaut= 0 ),
           ),  
           b_modele     =BLOC(condition = "(MODELE != None)",fr="mod�le contenant une sous-structure",
              SOUS_STRUC      =FACT(statut='o',min=01,
                regles=(UN_PARMI('TOUT','MAILLE'),),
                CAS_CHARGE  =SIMP(statut='o',typ='TXM' ),
                TOUT        =SIMP(statut='f',typ='TXM',into=("OUI",) ),
                MAILLE      =SIMP(statut='f',typ=ma,max='**',),
              ),
           ),
         ),
         b_char_ther     =BLOC(condition = "OPTION=='CHAR_THER'",
           CARA_ELEM        =SIMP(statut='f',typ=cara_elem),
           CHARGE           =SIMP(statut='o',typ=char_ther,max='**'),
           INST             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),
              
         b_char_acou     =BLOC(condition = "OPTION=='CHAR_ACOU'",
           CHAM_MATER        =SIMP(statut='o',typ=cham_mater),
           CHARGE            =SIMP(statut='o',typ=char_acou,max='**'),
         ),
         
         b_forc_noda     =BLOC(condition = "OPTION=='FORC_NODA'",
           SIEF_ELGA         =SIMP(statut='o',typ=cham_elem_sief_r),
           CARA_ELEM         =SIMP(statut='f',typ=cara_elem),
           MODELE            =SIMP(statut='f',typ=modele),
         ),
         
         b_meca_lagr     =BLOC(condition = "OPTION=='CHAR_MECA_LAGR'",
           CHAM_MATER        =SIMP(statut='o',typ=cham_mater),
           THETA             =SIMP(statut='o',typ=theta_geom),
           PROPAGATION       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           CHARGE            =SIMP(statut='f',typ=char_meca,max='**'),
           INST              =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),
) ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
def comb_cham_elem_prod(COMB_R=None,COMB_C=None,COMB_FOURIER=None,**args):

  if COMB_R != None:
    vale=COMB_R.get_child('CHAM_ELEM').get_valeur()
  elif COMB_C != None:
    vale=COMB_C.get_child('CHAM_ELEM').get_valeur()
  elif COMB_FOURIER != None:
    vale=COMB_FOURIER.get_child('CHAM_ELEM').get_valeur()
  else :
    raise AsException("type de concept resultat non prevu")

  if AsType(vale) == cham_elem_sief_r : return cham_elem_sief_r
  if AsType(vale) == cham_elem_flux_r : return cham_elem_flux_r
  if AsType(vale) == cham_elem_epsi_r : return cham_elem_epsi_r
  if AsType(vale) == cham_elem_ener_r : return cham_elem_ener_r
  if AsType(vale) == cham_elem_crit_r : return cham_elem_crit_r
  if AsType(vale) == cham_elem_dbel_r : return cham_elem_dbel_r
  if AsType(vale) == cham_elem_pres_r : return cham_elem_pres_r
  if AsType(vale) == cham_elem_sief_c : return cham_elem_sief_c
  raise AsException("type de concept resultat non prevu")

COMB_CHAM_ELEM=OPER(nom="COMB_CHAM_ELEM",op= 139,sd_prod=comb_cham_elem_prod,reentrant='f',
                    fr="Combinaison lin�aire de champs par �l�ments",docu="U4.72.03-e",
      regles=(UN_PARMI('COMB_R','COMB_C','COMB_FOURIER'),
              PRESENT_PRESENT('COMB_FOURIER','ANGL'),),
      COMB_R          =FACT(statut='f',min=01,max='**',
        PARTIE          =SIMP(statut='f',typ='TXM',into=("REEL","IMAG") ),
        COEF_R          =SIMP(statut='o',typ='R'),
        CHAM_ELEM       =SIMP(statut='o',
                              typ=(cham_elem_sief_r,cham_elem_flux_r,cham_elem_epsi_r,
                                   cham_elem_ener_r,cham_elem_crit_r,cham_elem_dbel_r,
                                   cham_elem_pres_r,cham_elem_sief_c ) ),
      ),
      COMB_C          =FACT(statut='f',min=01,max='**',
        regles=(UN_PARMI('COEF_R','COEF_C', ),),
        COEF_R          =SIMP(statut='f',typ='R'),
        COEF_C          =SIMP(statut='f',typ='C'),
        CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_sief_r) ),
      ),
      COMB_FOURIER    =FACT(statut='f',min=01,max='**',
        COEF_R          =SIMP(statut='f',typ='R',defaut= 1.),
        NUME_MODE       =SIMP(statut='o',typ='I'),
        TYPE_MODE       =SIMP(statut='o',typ='TXM',into=("SYME","ANTI") ),
        CHAM_ELEM       =SIMP(statut='o',typ=(cham_elem_sief_r,cham_elem_flux_r,cham_elem_epsi_r ) ),
      ),
      ANGL            =SIMP(statut='f',typ='R' ),
)  ;

#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
def comb_cham_no_prod(COMB_R,COMB_C,COMB_FOURIER,**args):
  if COMB_C != None:
    type_mat = AsType(COMB_C.get_child('CHAM_NO').get_valeur())
    if type_mat in  (cham_no_depl_c,cham_no_depl_r) : return cham_no_depl_c
    if type_mat in  (cham_no_temp_c,cham_no_temp_r) : return cham_no_temp_c
    if type_mat in  (cham_no_pres_c,cham_no_pres_r) : return cham_no_pres_c
  elif COMB_R != None:
    type_mat = AsType(COMB_R.get_child('CHAM_NO').get_valeur())
    if type_mat in  (cham_no_depl_c,cham_no_depl_r) : return cham_no_depl_r
    if type_mat in  (cham_no_temp_c,cham_no_temp_r) : return cham_no_temp_r
    if type_mat in  (cham_no_pres_c,cham_no_pres_r) : return cham_no_pres_r
    if type_mat ==  matr_asse_gene_r : return matr_asse_gene_r
  elif COMB_FOURIER != None:
    type_mat = AsType(COMB_FOURIER.get_child('CHAM_NO').get_valeur())
    if type_mat == cham_no_temp_r : return cham_no_temp_r
    if type_mat == cham_no_depl_r : return cham_no_depl_r
  raise AsException("type de concept resultat non prevu")


COMB_CHAM_NO=OPER(nom="COMB_CHAM_NO",op=  30,sd_prod=comb_cham_no_prod
                    ,fr="Combinaison lin�aire de champs aux noeuds",
                     docu="U4.72.02-f",reentrant='f',
         regles=(UN_PARMI('COMB_R','COMB_C','COMB_FOURIER'),),
         COMB_R          =FACT(statut='f',min=01,max='**',
           PARTIE          =SIMP(statut='f',typ='TXM',into=("REEL","IMAG",) ),
           CHAM_NO         =SIMP(statut='o',typ=(cham_no_temp_r,cham_no_temp_c,cham_no_depl_r,cham_no_depl_c
                                                ,cham_no_pres_r,cham_no_pres_c ) ),
           COEF_R          =SIMP(statut='o',typ='R' ),
         ),
         COMB_C          =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('COEF_R','COEF_C' ),),
           CHAM_NO         =SIMP(statut='o',typ=(cham_no_temp_r,cham_no_depl_r,cham_no_pres_r,cham_no_temp_c
                                                ,cham_no_depl_c,cham_no_pres_c ) ),
           COEF_R          =SIMP(statut='f',typ='R' ),
           COEF_C          =SIMP(statut='f',typ='C' ),
         ),
         COMB_FOURIER    =FACT(statut='f',min=01,max='**',
           CHAM_NO         =SIMP(statut='o',typ=(cham_no_temp_r,cham_no_depl_r) ),
           COEF_R          =SIMP(statut='f',typ='R',defaut= 1. ),
           NUME_MODE       =SIMP(statut='o',typ='I' ),
           TYPE_MODE       =SIMP(statut='o',typ='TXM',into=("SYME","ANTI") ),
         ),
         b_angl = BLOC ( condition = "COMB_FOURIER != None",
           ANGL            =SIMP(statut='o',typ='R' ),
         ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
COMB_FOURIER=OPER(nom="COMB_FOURIER",op= 161,sd_prod=comb_fourier,
                  docu="U4.83.31-c",reentrant='n',
         RESULTAT        =SIMP(statut='o',typ=fourier_elas ),
         ANGL            =SIMP(statut='o',typ='R',max='**'),
         NOM_CHAM        =SIMP(statut='o',typ='TXM',max=05,
                               into=("DEPL","REAC_NODA","SIEF_ELGA_DEPL","EPSI_ELNO_DEPL","SIGM_ELNO_DEPL") ),
)  ;
#& MODIF COMMANDE  DATE 10/07/2001   AUTEUR ACBHHCD G.DEVESA 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def comb_matr_asse_prod(COMB_R,COMB_C,**args):
  if COMB_C != None:
    type_mat = AsType(COMB_C.get_child('MATR_ASSE').get_valeur())
    if type_mat in  (matr_asse_depl_c,matr_asse_depl_r) : return matr_asse_depl_c
    if type_mat in  (matr_asse_gene_c,matr_asse_gene_r) : return matr_asse_gene_c    
    if type_mat in  (matr_asse_temp_c,matr_asse_temp_r) : return matr_asse_temp_c
    if type_mat in  (matr_asse_pres_c,matr_asse_pres_r) : return matr_asse_pres_c
  elif COMB_R != None:
    type_mat = AsType(COMB_R.get_child('MATR_ASSE').get_valeur())
    if type_mat in  (matr_asse_depl_c,matr_asse_depl_r) : return matr_asse_depl_r
    if type_mat in  (matr_asse_temp_c,matr_asse_temp_r) : return matr_asse_temp_r
    if type_mat in  (matr_asse_pres_c,matr_asse_pres_r) : return matr_asse_pres_r
    if type_mat in  (matr_asse_gene_c,matr_asse_gene_r) : return matr_asse_gene_r
  raise AsException("type de concept resultat non prevu")

COMB_MATR_ASSE=OPER(nom="COMB_MATR_ASSE",op=  31,sd_prod=comb_matr_asse_prod,
                    fr="Combinaison lin�aire de matrices assembl�es",
                    docu="U4.72.01-f",reentrant='f',
         regles=(UN_PARMI('COMB_R','COMB_C' ),),
         COMB_R          =FACT(statut='f',min=01,max='**',
           PARTIE          =SIMP(statut='f',typ='TXM',into=("REEL","IMAG") ),
           MATR_ASSE       =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_depl_c,matr_asse_temp_r,matr_asse_temp_c
                                                ,matr_asse_pres_r,matr_asse_pres_c,matr_asse_gene_r,matr_asse_gene_c ) ),
           COEF_R          =SIMP(statut='o',typ='R' ),
         ),
         COMB_C          =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('COEF_R','COEF_C' ),),
           MATR_ASSE       =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_depl_c,matr_asse_temp_r,matr_asse_temp_c
                                                ,matr_asse_pres_r,matr_asse_pres_c,matr_asse_gene_r,matr_asse_gene_c ) ),
           COEF_R          =SIMP(statut='f',typ='R' ),
           COEF_C          =SIMP(statut='f',typ='C' ),
         ),
         SANS_CMP        =SIMP(statut='f',typ='TXM',into=("LAGR",) ),
)  ;
#& MODIF COMMANDE  DATE 28/03/2001   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
COMB_SISM_MODAL=OPER(nom="COMB_SISM_MODAL",op= 109,sd_prod=mode_stat,
                     fr="R�ponse sismique par recombinaison modale par une m�thode spectrale",
                     docu="U4.84.01-d",reentrant='n',
         regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','FREQ','NUME_MODE','LIST_FREQ','LIST_ORDRE'),
                 UN_PARMI('AMOR_REDUIT','LIST_AMOR','AMOR_GENE' ),),
         MODE_MECA       =SIMP(statut='o',typ=mode_meca ),
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
         LIST_ORDRE      =SIMP(statut='f',typ=listis ),
         NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
         FREQ            =SIMP(statut='f',typ='R',max='**'),
         LIST_FREQ       =SIMP(statut='f',typ=listr8 ),
         b_freq          =BLOC(condition = "FREQ != None or LIST_FREQ != None",
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
         ),
         MODE_CORR       =SIMP(statut='f',typ=mode_stat_acce ),
         
         AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),
         LIST_AMOR       =SIMP(statut='f',typ=listr8 ),
         AMOR_GENE       =SIMP(statut='f',typ=matr_asse_gene_r ),
         
         MASS_INER       =SIMP(statut='f',typ=tabl_mass_iner ),
         CORR_FREQ       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         
         EXCIT           =FACT(statut='o',min=01,max='**',
           regles=(UN_PARMI('MONO_APPUI','NOEUD','GROUP_NO'),
                   UN_PARMI('AXE','TRI_AXE','TRI_SPEC' ),),
           
           MONO_APPUI      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           AXE             =SIMP(statut='f',fr="Excitation suivant un seul axe",
                                 typ='R',max=03),  
           TRI_AXE         =SIMP(statut='f',fr="Excitation suivant les trois axes mais avec le meme spectre",
                                 typ='R',max=03),
           TRI_SPEC        =SIMP(statut='f',fr="Excitation suivant les trois axes  avec trois spectres",
                                 typ='TXM',into=("OUI",) ),
           b_axe           =BLOC(condition = "AXE != None",fr="Excitation suivant un seul axe",
             SPEC_OSCI       =SIMP(statut='o',typ=fonction,max=01 ),
             ECHELLE         =SIMP(statut='f',typ='R',max=01),
           ),
           b_tri_axe       =BLOC(condition = "TRI_AXE != None",fr="Excitation suivant les trois axes mais avec le meme spectre",
             SPEC_OSCI       =SIMP(statut='o',typ=fonction,max=01 ),
             ECHELLE         =SIMP(statut='f',typ='R',max=01),
           ),
           b_tri_spec      =BLOC(condition = "TRI_SPEC != None",fr="Excitation suivant les trois axes  avec trois spectres",
             SPEC_OSCI       =SIMP(statut='o',typ=fonction,min=03,max=03 ),
             ECHELLE         =SIMP(statut='f',typ='R',min=03,max=03),
           ),       
           NATURE          =SIMP(statut='f',typ='TXM',defaut="ACCE",into=("ACCE","VITE","DEPL") ),
         ),
         COMB_MODE       =FACT(statut='o',min=01,max=01,
           TYPE            =SIMP(statut='o',typ='TXM',into=("SRSS","CQC","DSC","ABS","DPC") ),
           DUREE           =SIMP(statut='f',typ='R' ),
         ),
         COMB_DIRECTION  =FACT(statut='f',min=01,max=01,
           TYPE            =SIMP(statut='f',typ='TXM',into=("QUAD","NEWMARK") ),
         ),
         COMB_MULT_APPUI =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','NOEUD','GROUP_NO' ),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           TYPE            =SIMP(statut='o',typ='TXM',into=("QUAD","LINE","ABS") ),
         ),
         DEPL_MULT_APPUI =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NOEUD','GROUP_NO'),
                   AU_MOINS_UN('DX','DY','DZ' ),),
           MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,), ),
           NOEUD_REFE      =SIMP(statut='f',typ=no),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           DX              =SIMP(statut='f',typ='R' ),
           DY              =SIMP(statut='f',typ='R' ),
           DZ              =SIMP(statut='f',typ='R' ),
         ),
         OPTION          =SIMP(statut='o',typ='TXM',max=9,
                               into=("DEPL","VITE","ACCE_ABSOLU","SIGM_ELNO_DEPL","SIEF_ELGA_DEPL",
                                     "EFGE_ELNO_DEPL","REAC_NODA","FORC_NODA","EFGE_ELNO_CART",
                                     "SIPO_ELNO_DEPL") ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ) ),
         IMPRESSION      =FACT(statut='f',min=01,max='**',
           regles=(EXCLUS('TOUT','NIVEAU'),),
           TOUT            =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           NIVEAU          =SIMP(statut='f',typ='TXM',into=("SPEC_OSCI","MASS_EFFE","MAXI_GENE"),max=03 ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def crea_champ_prod(TYPE_CHAM,**args):
  if TYPE_CHAM == "CART_DBEL_R" : return carte_dbel_r
  if TYPE_CHAM == "CART_DEPL_C" : return carte_depl_c
  if TYPE_CHAM == "CART_DEPL_F" : return carte_depl_f
  if TYPE_CHAM == "CART_DEPL_R" : return carte_depl_r
  if TYPE_CHAM == "CART_DURT_R" : return carte_durt_r
  if TYPE_CHAM == "CART_ENER_R" : return carte_ener_r 
  if TYPE_CHAM == "CART_EPSI_R" : return carte_epsi_r
  if TYPE_CHAM == "CART_ERREUR" : return carte_erreur
  if TYPE_CHAM == "CART_FLUX_R" : return carte_flux_r
  if TYPE_CHAM == "CART_GEOM_R" : return carte_geom_r
  if TYPE_CHAM == "CART_G_DEPL_R" : return carte_g_depl_r
  if TYPE_CHAM == "CART_HYDR_R" : return carte_hydr_r
  if TYPE_CHAM == "CART_INST_R" : return carte_inst_r
  if TYPE_CHAM == "CART_INTE_R" : return carte_inte_r
  if TYPE_CHAM == "CART_META_R" : return carte_meta_r
  if TYPE_CHAM == "CART_NEUT_F" : return carte_neut_f
  if TYPE_CHAM == "CART_NEUT_R" : return carte_neut_r
  if TYPE_CHAM == "CART_PRES_R" : return carte_pres_r
  if TYPE_CHAM == "CART_SIEF_R" : return carte_sief_r
  if TYPE_CHAM == "CART_SOUR_R" : return carte_sour_r
  if TYPE_CHAM == "CART_TEMP_F" : return carte_temp_f
  if TYPE_CHAM == "CART_TEMP_R" : return carte_temp_r
  if TYPE_CHAM == "CART_VAR2_R" : return carte_var2_r
  if TYPE_CHAM == "CART_VNOR_C" : return carte_vnor_c
  if TYPE_CHAM == "NOEU_DBEL_R" : return cham_no_dbel_r
  if TYPE_CHAM == "NOEU_DEPL_C" : return cham_no_depl_c
  if TYPE_CHAM == "NOEU_DEPL_F" : return cham_no_depl_f
  if TYPE_CHAM == "NOEU_DEPL_R" : return cham_no_depl_r
  if TYPE_CHAM == "NOEU_DURT_R" : return cham_no_durt_r
  if TYPE_CHAM == "NOEU_ENER_R" : return cham_no_ener_r
  if TYPE_CHAM == "NOEU_EPSI_R" : return cham_no_epsi_r
  if TYPE_CHAM == "NOEU_ERREUR" : return cham_no_erreur
  if TYPE_CHAM == "NOEU_FLUX_R" : return cham_no_flux_r
  if TYPE_CHAM == "NOEU_GEOM_R" : return cham_no_geom_r
  if TYPE_CHAM == "NOEU_G_DEPL_R" : return cham_no_g_depl_r
  if TYPE_CHAM == "NOEU_HYDR_R" : return cham_no_hydr_r
  if TYPE_CHAM == "NOEU_INST_R" : return cham_no_inst_r
  if TYPE_CHAM == "NOEU_INTE_R" : return cham_no_inte_r
  if TYPE_CHAM == "NOEU_META_R" : return cham_no_meta_r
  if TYPE_CHAM == "NOEU_NEUT_F" : return cham_no_neut_f
  if TYPE_CHAM == "NOEU_NEUT_R" : return cham_no_neut_r
  if TYPE_CHAM == "NOEU_PRES_R" : return cham_no_pres_r
  if TYPE_CHAM == "NOEU_SIEF_R" : return cham_no_sief_r
  if TYPE_CHAM == "NOEU_SOUR_R" : return cham_no_sour_r
  if TYPE_CHAM == "NOEU_TEMP_F" : return cham_no_temp_f
  if TYPE_CHAM == "NOEU_TEMP_R" : return cham_no_temp_r
  if TYPE_CHAM == "NOEU_VAR2_R" : return cham_no_var2_r
  if TYPE_CHAM == "NOEU_VNOR_C" : return cham_no_vnor_c
  if TYPE_CHAM == "ELEM_DBEL_R" : return cham_elem_dbel_r
  if TYPE_CHAM == "ELEM_DEPL_C" : return cham_elem_depl_c
  if TYPE_CHAM == "ELEM_DEPL_F" : return cham_elem_depl_f
  if TYPE_CHAM == "ELEM_DEPL_R" : return cham_elem_depl_r
  if TYPE_CHAM == "ELEM_DURT_R" : return cham_elem_durt_r
  if TYPE_CHAM == "ELEM_ENER_R" : return cham_elem_ener_r
  if TYPE_CHAM == "ELEM_EPSI_R" : return cham_elem_epsi_r
  if TYPE_CHAM == "ELEM_ERREUR" : return cham_elem_erreur
  if TYPE_CHAM == "ELEM_FLUX_R" : return cham_elem_flux_r
  if TYPE_CHAM == "ELEM_GEOM_R" : return cham_elem_geom_r
  if TYPE_CHAM == "ELEM_G_DEPL_R" : return cham_elem_g_depl
  if TYPE_CHAM == "ELEM_HYDR_R" : return cham_elem_hydr_r
  if TYPE_CHAM == "ELEM_INST_R" : return cham_elem_inst_r
  if TYPE_CHAM == "ELEM_INTE_R" : return cham_elem_inte_r
  if TYPE_CHAM == "ELEM_META_R" : return cham_elem_meta_r
  if TYPE_CHAM == "ELEM_NEUT_F" : return cham_elem_neut_f
  if TYPE_CHAM == "ELEM_NEUT_R" : return cham_elem_neut_r
  if TYPE_CHAM == "ELEM_PRES_R" : return cham_elem_pres_r
  if TYPE_CHAM == "ELEM_SIEF_R" : return cham_elem_sief_r
  if TYPE_CHAM == "ELEM_SOUR_R" : return cham_elem_sour_r
  if TYPE_CHAM == "ELEM_TEMP_F" : return cham_elem_temp_f
  if TYPE_CHAM == "ELEM_TEMP_R" : return cham_elem_temp_r
  if TYPE_CHAM == "ELEM_VARI_R" : return cham_elem_vari_r
  if TYPE_CHAM == "ELEM_VNOR_C" : return cham_elem_vnor_c
  if TYPE_CHAM == "ELNO_DBEL_R" : return cham_elem_dbel_r
  if TYPE_CHAM == "ELNO_DEPL_C" : return cham_elem_depl_c
  if TYPE_CHAM == "ELNO_DEPL_F" : return cham_elem_depl_f
  if TYPE_CHAM == "ELNO_DEPL_R" : return cham_elem_depl_r
  if TYPE_CHAM == "ELNO_DURT_R" : return cham_elem_durt_r
  if TYPE_CHAM == "ELNO_ENER_R" : return cham_elem_ener_r
  if TYPE_CHAM == "ELNO_EPSI_R" : return cham_elem_epsi_r
  if TYPE_CHAM == "ELNO_ERREUR" : return cham_elem_erreur
  if TYPE_CHAM == "ELNO_FLUX_R" : return cham_elem_flux_r
  if TYPE_CHAM == "ELNO_GEOM_R" : return cham_elem_geom_r
  if TYPE_CHAM == "ELNO_G_DEPL_R" : return cham_elem_g_depl
  if TYPE_CHAM == "ELNO_HYDR_R" : return cham_elem_hydr_r
  if TYPE_CHAM == "ELNO_INST_R" : return cham_elem_inst_r
  if TYPE_CHAM == "ELNO_INTE_R" : return cham_elem_inte_r
  if TYPE_CHAM == "ELNO_META_R" : return cham_elem_meta_r
  if TYPE_CHAM == "ELNO_NEUT_F" : return cham_elem_neut_f
  if TYPE_CHAM == "ELNO_NEUT_R" : return cham_elem_neut_r
  if TYPE_CHAM == "ELNO_PRES_R" : return cham_elem_pres_r
  if TYPE_CHAM == "ELNO_SIEF_R" : return cham_elem_sief_r
  if TYPE_CHAM == "ELNO_SOUR_R" : return cham_elem_sour_r
  if TYPE_CHAM == "ELNO_TEMP_F" : return cham_elem_temp_f
  if TYPE_CHAM == "ELNO_TEMP_R" : return cham_elem_temp_r
  if TYPE_CHAM == "ELNO_VARI_R" : return cham_elem_vari_r
  if TYPE_CHAM == "ELNO_VNOR_C" : return cham_elem_vnor_c
  if TYPE_CHAM == "ELGA_DBEL_R" : return cham_elem_dbel_r
  if TYPE_CHAM == "ELGA_DEPL_C" : return cham_elem_depl_c
  if TYPE_CHAM == "ELGA_DEPL_F" : return cham_elem_depl_f
  if TYPE_CHAM == "ELGA_DEPL_R" : return cham_elem_depl_r
  if TYPE_CHAM == "ELGA_DURT_R" : return cham_elem_durt_r
  if TYPE_CHAM == "ELGA_ENER_R" : return cham_elem_ener_r
  if TYPE_CHAM == "ELGA_EPSI_R" : return cham_elem_epsi_r
  if TYPE_CHAM == "ELGA_ERREUR" : return cham_elem_erreur
  if TYPE_CHAM == "ELGA_FLUX_R" : return cham_elem_flux_r
  if TYPE_CHAM == "ELGA_GEOM_R" : return cham_elem_geom_r
  if TYPE_CHAM == "ELGA_G_DEPL_R" : return cham_elem_g_depl
  if TYPE_CHAM == "ELGA_HYDR_R" : return cham_elem_hydr_r
  if TYPE_CHAM == "ELGA_INST_R" : return cham_elem_inst_r
  if TYPE_CHAM == "ELGA_INTE_R" : return cham_elem_inte_r
  if TYPE_CHAM == "ELGA_META_R" : return cham_elem_meta_r
  if TYPE_CHAM == "ELGA_NEUT_F" : return cham_elem_neut_f
  if TYPE_CHAM == "ELGA_NEUT_R" : return cham_elem_neut_r
  if TYPE_CHAM == "ELGA_PRES_R" : return cham_elem_pres_r
  if TYPE_CHAM == "ELGA_SIEF_R" : return cham_elem_sief_r
  if TYPE_CHAM == "ELGA_SOUR_R" : return cham_elem_sour_r
  if TYPE_CHAM == "ELGA_TEMP_F" : return cham_elem_temp_f
  if TYPE_CHAM == "ELGA_TEMP_R" : return cham_elem_temp_r
  if TYPE_CHAM == "ELGA_VARI_R" : return cham_elem_vari_r
  if TYPE_CHAM == "ELGA_VNOR_C" : return cham_elem_vnor_c
  if TYPE_CHAM == "CART_IRRA_R" : return carte_irra_r
  if TYPE_CHAM == "NOEU_IRRA_R" : return cham_no_irra_r
  if TYPE_CHAM == "ELEM_IRRA_R" : return cham_elem_irra_r
  if TYPE_CHAM == "ELNO_IRRA_R" : return cham_elem_irra_r
  if TYPE_CHAM == "ELGA_IRRA_R" : return cham_elem_irra_r
  raise AsException("type de concept resultat non prevu")

CREA_CHAMP=OPER(nom="CREA_CHAMP",op= 195,sd_prod=crea_champ_prod,
                fr="  ",docu="U4.72.04-a1",reentrant='n',
         TYPE_CHAM       =SIMP(statut='o',typ='TXM',     
                        into=("CART_DBEL_R","NOEU_DBEL_R","ELEM_DBEL_R",  
                             "ELNO_DBEL_R","ELGA_DBEL_R","CART_DEPL_C",         
                             "NOEU_DEPL_C","ELEM_DEPL_C","ELNO_DEPL_C",         
                             "ELGA_DEPL_C","CART_DEPL_F","NOEU_DEPL_F",         
                             "ELEM_DEPL_F","ELNO_DEPL_F","ELGA_DEPL_F",         
                             "CART_DEPL_R","NOEU_DEPL_R","ELEM_DEPL_R",         
                             "ELNO_DEPL_R","ELGA_DEPL_R","CART_DURT_R",         
                             "NOEU_DURT_R","ELEM_DURT_R","ELNO_DURT_R",         
                             "ELGA_DURT_R","CART_ENER_R","NOEU_ENER_R",         
                             "ELEM_ENER_R","ELNO_ENER_R","ELGA_ENER_R",         
                             "CART_EPSI_R","NOEU_EPSI_R","ELEM_EPSI_R",         
                             "ELNO_EPSI_R","ELGA_EPSI_R","CART_ERREUR",         
                             "NOEU_ERREUR","ELEM_ERREUR","ELNO_ERREUR",         
                             "ELGA_ERREUR","CART_FLUX_R","NOEU_FLUX_R",         
                             "ELEM_FLUX_R","ELNO_FLUX_R","ELGA_FLUX_R",         
                             "CART_GEOM_R","NOEU_GEOM_R","ELEM_GEOM_R",         
                             "ELNO_GEOM_R","ELGA_GEOM_R","CART_G_DEPL_R",       
                             "NOEU_G_DEPL_R","ELEM_G_DEPL_R","ELNO_G_DEPL_R",   
                             "ELGA_G_DEPL_R","CART_HYDR_R","NOEU_HYDR_R",       
                             "ELEM_HYDR_R","ELNO_HYDR_R","ELGA_HYDR_R",         
                             "CART_INST_R","NOEU_INST_R","ELEM_INST_R",         
                             "ELNO_INST_R","ELGA_INST_R","CART_INTE_R",         
                             "NOEU_INTE_R","ELEM_INTE_R","ELNO_INTE_R",         
                             "ELGA_INTE_R","CART_META_R","NOEU_META_R",         
                             "ELEM_META_R","ELNO_META_R","ELGA_META_R",         
                             "CART_NEUT_F","NOEU_NEUT_F","ELEM_NEUT_F",         
                             "ELNO_NEUT_F","ELGA_NEUT_F","CART_NEUT_R",         
                             "NOEU_NEUT_R","ELEM_NEUT_R","ELNO_NEUT_R",         
                             "ELGA_NEUT_R","CART_PRES_R","NOEU_PRES_R",         
                             "ELEM_PRES_R","ELNO_PRES_R","ELGA_PRES_R",         
                             "CART_SIEF_R","NOEU_SIEF_R","ELEM_SIEF_R",         
                             "ELNO_SIEF_R","ELGA_SIEF_R","CART_SOUR_R",         
                             "NOEU_SOUR_R","ELEM_SOUR_R","ELNO_SOUR_R",         
                             "ELGA_SOUR_R","CART_TEMP_F","NOEU_TEMP_F",         
                             "ELEM_TEMP_F","ELNO_TEMP_F","ELGA_TEMP_F",         
                             "CART_TEMP_R","NOEU_TEMP_R","ELEM_TEMP_R",         
                             "ELNO_TEMP_R","ELGA_TEMP_R","CART_VAR2_R",         
                             "NOEU_VAR2_R","ELEM_VARI_R","ELNO_VARI_R",         
                             "ELGA_VARI_R","CART_VNOR_C","NOEU_VNOR_C",         
                             "ELEM_VNOR_C","ELNO_VNOR_C","ELGA_VNOR_C",
                             "CART_IRRA_R","NOEU_IRRA_R","ELEM_IRRA_R",
                             "ELNO_IRRA_R","ELGA_IRRA_R",) ),

#        SI CREATION D'UN CHAM_NO, POUR IMPOSER LA NUMEROTATION DES DDLS :
#        ------------------------------------------------------------------
         regles=(EXCLUS('NUME_DDL','CHAM_NO',)),         
         NUME_DDL        =SIMP(statut='f',typ=(nume_ddl) ),
         CHAM_NO         =SIMP(statut='f',typ=(cham_no) ),

         OPERATION       =SIMP(statut='o',typ='TXM',into=("AFFE","ASSE","EVAL","EXTR","DISC",) ),

         b_affe          =BLOC(condition = "OPERATION == 'AFFE'", 
             regles=(UN_PARMI('MAILLAGE','MODELE'),EXCLUS('MAILLAGE','PROL_ZERO'),),         
             MAILLAGE        =SIMP(statut='f',typ=(maillage) ),
             MODELE          =SIMP(statut='f',typ=(modele) ),
             PROL_ZERO       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
             AFFE            =FACT(statut='o',min=01,max='**',
                regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE','GROUP_NO','NOEUD',),         
                        UN_PARMI('VALE','VALE_I','VALE_C','VALE_F', ),),
                TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
                GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
                MAILLE          =SIMP(statut='f',typ=ma,max='**'),
                GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
                NOEUD           =SIMP(statut='f',typ=no,max='**'),
                NOM_CMP         =SIMP(statut='o',typ='TXM',max='**' ),  
                VALE            =SIMP(statut='f',typ='R',max='**' ),  
                VALE_I          =SIMP(statut='f',typ='I',max='**' ),  
                VALE_C          =SIMP(statut='f',typ='C',max='**' ),  
                VALE_F          =SIMP(statut='f',typ=fonction,max='**'), 
                                   ),
                             ),
         b_asse          =BLOC(condition = "OPERATION == 'ASSE'", 
             regles=(UN_PARMI('MAILLAGE','MODELE'),EXCLUS('MAILLAGE','PROL_ZERO'),),         
             MAILLAGE        =SIMP(statut='f',typ=(maillage) ),
             MODELE          =SIMP(statut='f',typ=(modele) ),
             PROL_ZERO       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
             ASSE            =FACT(statut='o',min=01,max='**',
                regles=(AU_MOINS_UN('TOUT','GROUP_MA','GROUP_NO','MAILLE','NOEUD',),      
                PRESENT_PRESENT('NOM_CMP_RESU','NOM_CMP', ),),
                TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
                GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
                GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
                MAILLE          =SIMP(statut='f',typ=ma,max='**'),
                NOEUD           =SIMP(statut='f',typ=no,max='**'),
                CHAM_GD         =SIMP(statut='o',typ=(cham_gd)),
                NOM_CMP         =SIMP(statut='f',typ='TXM',max='**' ),  
                NOM_CMP_RESU    =SIMP(statut='f',typ='TXM',max='**' ),  
                CUMUL           =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
                COEF_R          =SIMP(statut='f',typ='R',defaut= 1. ),  
                                    ),
                             ),
         b_eval          =BLOC(condition = "OPERATION == 'EVAL'", 
             CHAM_F          =SIMP(statut='o',typ=(cham_gd)),
             CHAM_PARA       =SIMP(statut='o',typ=(cham_gd),max='**'),
                             ),
         b_disc          =BLOC(condition = "OPERATION == 'DISC'", 
             MODELE          =SIMP(statut='f',typ=(modele) ),
             PROL_ZERO       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
             CHAM_GD         =SIMP(statut='o',typ=(cham_gd)),
                             ),
         b_extr          =BLOC(condition = "OPERATION == 'EXTR'", 
             regles=(UN_PARMI('MAILLAGE','RESULTAT'),),         
             MAILLAGE        =SIMP(statut='f',typ=(maillage) ),
             RESULTAT        =SIMP(statut='f',typ=(resultat) ),
             b_extr_maillage =BLOC(condition = "MAILLAGE != None",
                 NOM_CHAM        =SIMP(statut='o',typ='TXM',into=("GEOMETRIE",)),
                                  ),
             b_extr_resultat =BLOC(condition = "RESULTAT != None",
                 regles=(EXCLUS('TYPE_MAXI','NUME_ORDRE','INST','FREQ','NUME_MODE',        
                                'NOEUD_CMP','NOM_CAS','ANGL', ),),
                 NOM_CHAM        =SIMP(statut='o',typ='TXM',     
                           into=("DEPL","VITE","ACCE",          
                             "DEPL_ABSOLU","VITE_ABSOLU",
                             "TEMP","IRRA","ACCE_ABSOLU",  
                             "FORC_NODA","REAC_NODA","EFGE_NOEU_DEPL",          
                             "EFGE_NOEU_CART","EPSI_NOEU_DEPL",                 
                             "SIGM_NOEU_DEPL","SIGM_NOEU_CART",                 
                             "SIPO_NOEU_DEPL","EQUI_NOEU_SIGM",                 
                             "EQUI_NOEU_EPSI","FLUX_NOEU_TEMP",                 
                             "FLUX_ELGA_TEMP","FLUX_ELNO_TEMP",                 
                             "META_ELGA_TEMP","META_ELNO_TEMP",                 
                             "META_NOEU_TEMP","DURT_ELGA_META",                 
                             "DURT_ELNO_META","DURT_NOEU_META","SIEF_ELGA",     
                             "SIEF_ELNO_ELGA","SIEF_ELGA_DEPL",                 
                             "VARI_ELNO_ELGA","VARI_ELGA","EPOT_ELEM_DEPL",     
                             "ECIN_ELEM_DEPL","SOUR_ELGA_ELEC",                 
                             "PRES_ELNO_REEL","PRES_ELNO_IMAG",                 
                             "PRES_ELNO_DBEL","INTE_ELNO_ACTI",                 
                             "INTE_ELNO_REAC","EFGE_ELNO_DEPL",                 
                             "SIGM_ELNO_DEPL","EFGE_ELNO_CART",                 
                             "SIGM_ELNO_CART","SIPO_ELNO_DEPL",                 
                             "EPSI_ELNO_DEPL","EPSI_ELGA_DEPL",                 
                             "EPSG_ELNO_DEPL","EPSG_ELGA_DEPL","EPSP_ELNO",     
                             "EPSP_ELGA","EQUI_ELNO_SIGM","EQUI_ELGA_SIGM",     
                             "EQUI_ELNO_EPSI","EQUI_ELGA_EPSI",                 
                             "ERRE_ELNO_ELGA","ERRE_ELGA_NORE",                 
                             "ERRE_ELEM_NOZ1","ERRE_ELEM_NOZ2",                 
                             "SIGM_NOZ1_ELGA","SIGM_NOZ2_ELGA",                 
                             "DEGE_ELNO_DEPL","SIRE_ELNO_DEPL",                 
                             "VNOR_ELEM_DEPL","SIEF_ELNO","VARI_ELNO",          
                             "SIEF_NOEU_ELGA","VARI_NOEU_ELGA",                 
                             "PRES_NOEU_DBEL","PRES_NOEU_REEL",                 
                             "PRES_NOEU_IMAG","INTE_NOEU_ACTI",                 
                             "INTE_NOEU_REAC","DCHA_ELGA_SIGM",                 
                             "DCHA_ELNO_SIGM","RADI_ELGA_SIGM",                 
                             "RADI_ELNO_SIGM","ENDO_ELNO_SIGA",                 
                             "ENDO_ELNO_SINO","ENDO_ELNO_SIGM",                 
                             "SIGM_ELNO_VARI","SIGM_NOEU_VARI",                 
                             "EPME_ELNO_DEPL","EPME_ELGA_DEPL",                 
                             "EPME_ELNO_DPGE","EPMG_ELNO_DEPL",                 
                             "EPMG_ELGA_DEPL","GRAD_ELGA_THETA",                
                             "GTHE_ELNO_ELGA","GRAD_NOEU_THETA",
                             "HYDR_ELGA","HYDR_ELNO_ELGA","HYDR_NOEU_ELGA",    
                             "THETA","SIGM_ELNO_SIEF","SIPO_ELNO_SIEF",
                             "VALE_CONT",) ),
                 TYPE_MAXI       =SIMP(statut='f',typ='TXM',into=("MAXI","MINI","MAXI_ABS","MINI_ABS","NORM_TRAN",) ),
                 TYPE_RESU       =SIMP(statut='f',typ='TXM',defaut="VALE",into=("VALE","INST",) ),
                 TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
                 LIST_INST       =SIMP(statut='f',typ=(listr8) ),
                 NUME_ORDRE      =SIMP(statut='f',typ='I'),  
                 INST            =SIMP(statut='f',typ='R'),  
                 FREQ            =SIMP(statut='f',typ='R'),  
                 NUME_MODE       =SIMP(statut='f',typ='I'),  
                 NOEUD_CMP       =SIMP(statut='f',typ='TXM',max='**'),  
                 NOM_CAS         =SIMP(statut='f',typ='TXM'),  
                 ANGL            =SIMP(statut='f',typ='R'),  
                 PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3),  
                 CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU",) ),
                 INTERPOL        =SIMP(statut='f',typ='TXM',defaut="NON",into=("NON","LIN",) ),
                              ),

                ),
# FIN DU CATALOGUE : INFO,TITRE ET TYPAGE DU RESULAT :
#-----------------------------------------------------
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2,) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
CREA_MAILLAGE=OPER(nom="CREA_MAILLAGE",op= 167,sd_prod=maillage,
                     docu="U4.23.02-c",reentrant='n',
         regles=(EXCLUS('ECLA_PG','CREA_MAILLE'),
                 EXCLUS('ECLA_PG','CREA_GROUP_MA'),
                 EXCLUS('ECLA_PG','DETR_GROUP_MA'),
                 EXCLUS('ECLA_PG','MODI_MAILLE'),),
         MAILLAGE        =SIMP(statut='o',typ=maillage ),
         CREA_POI1       =FACT(statut='f',min=01,max='**',fr="Cr�ation de mailles de type POI1 � partir de noeuds",
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE','GROUP_NO','NOEUD' ),),
           NOM_GROUP_MA    =SIMP(statut='f',typ=grma,max='**'),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
         ),
         CREA_MAILLE     =FACT(statut='f',min=01,max='**',fr="Duplication de mailles",
           regles=(AU_MOINS_UN('TOUT','MAILLE','GROUP_MA'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           PREF_MAILLE     =SIMP(statut='o',typ='TXM' ),
           PREF_NUME       =SIMP(statut='f',typ='I' ),
         ),
         CREA_GROUP_MA   =FACT(statut='f',min=01,max='**',fr="Duplication de mailles et cr�ation de groupes de mailles",
           regles=(AU_MOINS_UN('TOUT','MAILLE','GROUP_MA' ),),
           NOM             =SIMP(statut='o',typ='TXM'),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           PREF_MAILLE     =SIMP(statut='o',typ='TXM' ),
           PREF_NUME       =SIMP(statut='f',typ='I' ),
         ),
         DETR_GROUP_MA   =FACT(statut='f',min=01,max=01,fr="Destruction de groupes de mailles",
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           NB_MAILLE       =SIMP(statut='f',typ='I',defaut= 0,
                                 fr="Nombre minimal de mailles que doit contenir le groupe pour etre d�truit",  ),  
         ),
         MODI_MAILLE     =FACT(statut='f',min=01,max='**',fr="Modification du type de mailles",
           regles=(AU_MOINS_UN('TOUT','MAILLE','GROUP_MA' ),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=grma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=ma,max='**'),
           OPTION          =SIMP(statut='o',typ='TXM',into=("TRIA6_7","QUAD8_9","SEG3_4"),fr="Choix de la transformation" ),
           PREF_NOEUD      =SIMP(statut='f',typ='TXM',defaut="NS"),
           PREF_NUME       =SIMP(statut='f',typ='I',defaut= 1 ),
         ),
         REPERE          =FACT(statut='f',min=01,max='**',
                               fr="changement de rep�re servant � d�terminer les caract�ristiques d une section de poutre",
           TABLE           =SIMP(statut='o',typ=tabl_cara_geom,
                                 fr="Nom de la table contenant les caract�ristiques de la section de poutre" ),
           NOM_ORIG        =SIMP(statut='f',typ='TXM',into=("CDG","TORSION"),fr="Origine du nouveau rep�re" ),
           NOM_ROTA        =SIMP(statut='f',typ='TXM',into=("INERTIE",),fr="Direction du rep�re"  ),   
           b_cdg =BLOC(condition = "NOM_ORIG == 'CDG'",
             GROUP_MA        =SIMP(statut='f',typ=grma,
                                   fr="Nom du groupe de mailles dont le centre de gravit� sera l origine du nouveau rep�re"),
           ),
         ),
         ECLA_PG         =FACT(statut='f',min=01,max=01,
                               fr="Eclatement des mailles en petites mailles contenant chacune un seul point de gauss",
           MODELE          =SIMP(statut='o',typ=modele ),
           SHRINK          =SIMP(statut='f',typ='R',defaut= 0.9, fr="Facteur de r�duction" ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 07/01/2002   AUTEUR D6BHHJP J.P.LEFEBVRE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def crea_resu_prod(TYPE_RESU,**args):
  if TYPE_RESU == "EVOL_ELAS"    : return evol_elas
  if TYPE_RESU == "EVOL_NOLI"    : return evol_noli
  if TYPE_RESU == "EVOL_THER"    : return evol_ther
  if TYPE_RESU == "MULT_ELAS"    : return mult_elas
  if TYPE_RESU == "FOURIER_ELAS" : return fourier_elas
  if TYPE_RESU == "EVOL_VARC"    : return evol_varc
  raise AsException("type de concept resultat non prevu")

CREA_RESU=OPER(nom="CREA_RESU",op=124,sd_prod=crea_resu_prod,docu="U4.44.12-d1",reentrant='f',
               fr="Engendrer ou enrichir une structure de donnees en affectant les cham_gd associes",

         OPERATION =SIMP(statut='o',typ='TXM',into=("AFFE","ECLA_PG","PERM_CHAM","PROL_RTZ",),
                         fr="choix de la fonction a activer",),

         b_affe       =BLOC(condition = "OPERATION == 'AFFE'",

           TYPE_RESU    =SIMP(statut='o',typ='TXM',into=("MULT_ELAS","EVOL_ELAS","EVOL_NOLI","FOURIER_ELAS",
                                                         "EVOL_THER","EVOL_VARC",) ),
           NOM_CHAM     =SIMP(statut='f',typ='TXM',into=("DEPL","TEMP","IRRA","HYDR_ELGA",),max=1 ),
           AFFE         =FACT(statut='f',min=01,max='**',
             regles=(UN_PARMI('NOM_CAS','NUME_MODE','LIST_INST','INST',),),
             CHAM_GD         =SIMP(statut='f',typ=(cham_gd)),
             NUME_ORDRE_INIT =SIMP(statut='f',typ='I'),
             NOM_CAS         =SIMP(statut='f',typ='TXM' ),
             NUME_MODE       =SIMP(statut='f',typ='I'),
             TYPE_MODE       =SIMP(statut='f',typ='TXM',defaut="SYME",into=("SYME","ANTI","TOUS") ),
             INST            =SIMP(statut='f',typ='R',max='**'),
             LIST_INST       =SIMP(statut='f',typ=listr8),
             NUME_INIT       =SIMP(statut='f',typ='I'),
             NUME_FIN        =SIMP(statut='f',typ='I'),
           ),  
         ),  

         b_ecla_pg    =BLOC(condition = "OPERATION == 'ECLA_PG'",
           
           TYPE_RESU       =SIMP(statut='o',typ='TXM',into=("EVOL_ELAS","EVOL_NOLI","EVOL_THER"), ),
         
           ECLA_PG         =FACT(statut='f',min=01,max=01,
             regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','LIST_INST','LIST_ORDRE'),),
             NOM_CHAM        =SIMP(statut='o',typ='TXM',max='**',
                                   into=("SIEF_ELGA","VARI_ELGA","SIEF_ELGA_DEPL","FLUX_ELGA_TEMP",) ),
             MODELE_INIT     =SIMP(statut='o',typ=modele),
             RESU_INIT       =SIMP(statut='o',typ=resultat),
             MAILLAGE        =SIMP(statut='o',typ=maillage),
             TOUT_ORDRE      =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI",) ),
             NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
             LIST_ORDRE      =SIMP(statut='f',typ=listis),
             INST            =SIMP(statut='f',typ='R',max='**'),
             LIST_INST       =SIMP(statut='f',typ=listr8),
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU",) ),
           ),
         ),

         b_perm_cham =BLOC(condition = "OPERATION == 'PERM_CHAM'",

           TYPE_RESU       =SIMP(statut='o',typ='TXM',into=("EVOL_NOLI",) ),
           NOM_CHAM        =SIMP(statut='f',typ='TXM',into=("DEPL","SIEF_ELGA","VARI_ELGA",),max='**' ),
           RESU_INIT       =SIMP(statut='o',typ=evol_noli),
           INST_INIT       =SIMP(statut='f',typ='R'),
           PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3),
           CRITERE         =SIMP(statut='f',typ='TXM',into=('RELATIF','ABSOLU'),defaut='RELATIF'),
           MAILLAGE_INIT   =SIMP(statut='o',typ=maillage,),
           RESU_FINAL      =SIMP(statut='o',typ=evol_noli,),
           MAILLAGE_FINAL  =SIMP(statut='o',typ=maillage,),
           PERM_CHAM       =FACT(statut='o',min=01,max=01,
              GROUP_MA_FINAL =SIMP(statut='o',typ=grma),
              GROUP_MA_INIT  =SIMP(statut='o',typ=grma),
              TRAN           =SIMP(statut='o',typ='R',max='**'),
              PRECISION      =SIMP(statut='f',typ='R',defaut=1.0E-3),
           ),
         ),

         b_prol_rtz   =BLOC(condition = "OPERATION == 'PROL_RTZ'",

           TYPE_RESU       =SIMP(statut='o',typ='TXM',into=("EVOL_THER",) ),

           PROL_RTZ        =FACT(statut='f',min=01,max=01,
              regles=(EXCLUS('INST','LIST_INST'),),
              MAILLAGE_FINAL  =SIMP(statut='o',typ=maillage,),
              TABLE           =SIMP(statut='o',typ=tabl_post_rele,fr="Table issue de post_releve_t"),
              INST            =SIMP(statut='f',typ='R',max='**'),
              LIST_INST       =SIMP(statut='f',typ=listr8),
              b_acce_reel     =BLOC(condition="(INST != None)or(LIST_INST != None)",
                 PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-6),
                 CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
              ),
              PROL_DROITE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU",),),
              PROL_GAUCHE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU",),),
              REPERE          =SIMP(statut='o',typ='TXM',into=("CYLINDRIQUE",),),
              ORIGINE         =SIMP(statut='o',typ='R',min=03,max=03),  
              AXE_Z           =SIMP(statut='o',typ='R',min=03,max=03),  
           ),
         ),

)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEBUT=MACRO(nom="DEBUT",op=0 ,docu="U4.11.01-f1",repetable='n',
           fr="Ouverture d une �tude. Allocation des ressources m�moire et disque",
          sd_prod=ops.DEBUT,

         PAR_LOT         =SIMP(fr="mode de traitement des commandes",statut='f',typ='TXM',
                           into=("OUI","NON"),defaut="OUI"),
         BASE            =FACT(fr="d�finition des param�tres associ�s aux bases JEVEUX",
                               statut='f',min=01,max=03,
           FICHIER         =SIMP(fr="nom de la base",statut='o',typ='TXM',
                                 into=('GLOBALE','VOLATILE','LOCALE'),),
           TITRE           =SIMP(statut='f',typ='TXM'),
           CAS             =SIMP(statut='f',typ='TXM'),
           NMAX_ENRE       =SIMP(fr="nombre maximum d enregistrements",statut='f',typ='I'),
           LONG_ENRE       =SIMP(fr="longueur des enregistrements",statut='f',typ='I'),
           LONG_REPE       =SIMP(fr="longueur du r�pertoire",statut='f',typ='I'),
         ),
         IMPRESSION      =FACT(statut='f',min=01,max=03,
           FICHIER         =SIMP(statut='o',typ='TXM'),
           UNITE           =SIMP(statut='o',typ='I'),
         ),
         CATALOGUE       =FACT(statut='f',min=01,max=10,
           FICHIER         =SIMP(statut='o',typ='TXM'),
           TITRE           =SIMP(statut='f',typ='TXM'),
           UNITE           =SIMP(statut='f',typ='I'),
         ),
         CODE            =FACT("d�finition d un nom pour l'esemble d'une �tude",
                               statut='f',min=01,max=01,
           NOM             =SIMP(statut='o',typ='TXM'),
           UNITE           =SIMP(statut='f',typ='I',defaut=15),
         ),
         DEBUG           =FACT(fr="option de d�boggage reserv�e aux d�veloppeurs",
                               statut='f',min=01,max=01,
           JXVERI          =SIMP(fr="v�rifie l int�grit� de la segmentation m�moire",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           JEVEUX          =SIMP(fr="force les d�chargement sur disque",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           ENVIMA          =SIMP(fr="imprime les valeurs d�finies dans ENVIMA",
                                 statut='f',typ='TXM',into=('TEST',)),
         ),
         MEMOIRE         =FACT(fr="mode de gestion m�moire utilis�",statut='f',min=01,max=01,
           GESTION         =SIMP(statut='f',typ='TXM',into=('COMPACTE','RAPIDE'),defaut='RAPIDE'),
           TYPE_ALLOCATION =SIMP(statut='f',typ='I',into=(1,2,3,4),defaut=1),
           TAILLE          =SIMP(statut='f',typ='I'),
           TAILLE_BLOC     =SIMP(statut='f',typ='R',defaut=800.),
           PARTITION       =SIMP(statut='f',typ='R'),
         ),
 );
#& MODIF COMMANDE  DATE 19/12/2001   AUTEUR CIBHHPD D.NUNEZ 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_BASE_MODALE=OPER(nom="DEFI_BASE_MODALE",op=  99,sd_prod=base_modale,
                     docu="U4.64.02-e",reentrant='f',
         regles=(UN_PARMI('CLASSIQUE','RITZ','DIAG_MASS'),),
         CLASSIQUE       =FACT(statut='f',min=01,max=01,
           INTERF_DYNA     =SIMP(statut='o',typ=interf_dyna_clas ),
           MODE_MECA       =SIMP(statut='o',typ=mode_meca,max='**' ),
           NMAX_MODE       =SIMP(statut='f',typ='I',defaut= 10 ),
         ),
         RITZ            =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MODE_STAT','MODE_MECA','MULT_ELAS','BASE_MODALE'),),
           MODE_MECA       =SIMP(statut='f',typ=mode_meca,max='**'  ),
           NMAX_MODE       =SIMP(statut='f',typ='I',defaut= 999 ),
           MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc,) ),
           MULT_ELAS       =SIMP(statut='f',typ=mult_elas ),
           BASE_MODALE     =SIMP(statut='f',typ=base_modale ),
         ),
        DIAG_MASS        =FACT(statut='f',min=01,max='**',
           MODE_MECA       =SIMP(statut='o',typ=mode_meca,max='**'  ),
           MODE_STAT       =SIMP(statut='o',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc,) ),
         ),
#  le bloc conditionnel remplace-t-il PRESENT_PRESENT('RITZ','NUME_REF'),
#                                     PRESENT_ABSENT('INTERF_DYNA','CLASSIQUE'),        
         b_ritz          =BLOC(condition = "RITZ != None",
           INTERF_DYNA     =SIMP(statut='f',typ=interf_dyna_clas ),
           NUME_REF        =SIMP(statut='o',typ=nume_ddl ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_CABLE_BP=OPER(nom="DEFI_CABLE_BP",op= 180,sd_prod=cabl_precont,
                   fr=" ",
                   docu="U4.42.04-a",reentrant='n',
         MODELE          =SIMP(statut='o',typ=modele ),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater ),
         CARA_ELEM       =SIMP(statut='o',typ=cara_elem ),
         GROUP_MA_BETON  =SIMP(statut='o',typ=grma),
         DEFI_CABLE      =FACT(statut='o',min=1,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),
                   UN_PARMI('NOEUD_ANCRAGE','GROUP_NO_ANCRAGE'),),
           MAILLE          =SIMP(statut='f',typ=ma,min=2,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma),
           NOEUD_ANCRAGE   =SIMP(statut='f',typ=no,max=2),
           GROUP_NO_ANCRAGE=SIMP(statut='f',typ=grno,max=2),
           TYPE_ANCRAGE    =SIMP(statut='o',typ='TXM',min=2,max=2,     
                                 into=("ACTIF","PASSIF") ),
         ),
         TENSION_INIT    =SIMP(statut='o',typ='R',val_min=0.E+0 ),  
         RECUL_ANCRAGE   =SIMP(statut='o',typ='R',val_min=0.E+0 ),  
         RELAXATION      =FACT(statut='f',min=0,max=1,
           R_J             =SIMP(statut='o',typ='R',val_min=0.E+0 ),  
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_CONSTANTE=OPER(nom="DEFI_CONSTANTE",op=   2,sd_prod=fonction,
                    fr="D�finition d une fonction constante",
                    docu="U4.31.01-f",reentrant='n',
         NOM_RESU        =SIMP(statut='f',typ='TXM',defaut="TOUTRESU"),
         VALE            =SIMP(statut='o',typ='R',max=01 ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_COQU_MULT=OPER(nom="DEFI_COQU_MULT",op=56,sd_prod=mater,docu="U4.42.03-e",reentrant='n',
                    fr="D�finition d une coque composite couche par couche",
         COUCHE          =FACT(statut='o',min=01,max='**',
           EPAIS           =SIMP(statut='o',typ='R',val_min=0.E+0 ),
           MATER           =SIMP(statut='o',typ=(mater) ),
           ORIENTATION     =SIMP(statut='f',typ='R',defaut= 0.E+0,
                                 val_min=-90.E+0,val_max=90.E+0   ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
         IMPRESSION      =FACT(statut='f',min=01,max=01,
           FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT",
                                 into=("RESULTAT",) ),
         ),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_FLUI_STRU=OPER(nom="DEFI_FLUI_STRU",op= 143,sd_prod=type_flui_stru,
                    docu="U4.25.01-d",reentrant='n',
         regles=(  UN_PARMI('FAISCEAU_TRANS','GRAPPE','FAISCEAU_AXIAL','COQUE_COAX',),),
         FAISCEAU_TRANS  =FACT(statut='f',min=01,max='**',
           COUPLAGE        =SIMP(statut='f',typ='TXM',into=("OUI","NON") ),
           CARA_ELEM       =SIMP(statut='f',typ=cara_elem ),
           PROF_VITE_FLUI  =SIMP(statut='o',typ=fonction ),
           PROF_RHO_F_INT  =SIMP(statut='f',typ=fonction ),
           PROF_RHO_F_EXT  =SIMP(statut='f',typ=fonction ),
           NOM_CMP         =SIMP(statut='f',typ='TXM',into=("DX","DY","DZ") ),
           COEF_MASS_AJOU  =SIMP(statut='f',typ='R' ),
           TYPE_PAS        =SIMP(statut='f',typ='TXM',into=("CARRE_LIGN","TRIA_LIGN") ),
           TYPE_RESEAU     =SIMP(statut='f',typ='I' ),
           UNITE_CD        =SIMP(statut='f',typ='I',defaut=70),
           UNITE_CK        =SIMP(statut='f',typ='I',defaut=71),            
           PAS             =SIMP(statut='f',typ='R' ),
         ),
         GRAPPE          =FACT(statut='f',min=00,max=01,
           regles=(ENSEMBLE('GRAPPE_2','NOEUD','CARA_ELEM','MODELE','RHO_FLUI',),
                   PRESENT_PRESENT('COEF_MASS_AJOU','GRAPPE_2', ),),
#  peut on cr�er un bloc a partir de la valeur de couplage  
           COUPLAGE        =SIMP(statut='o',typ='TXM',into=("OUI","NON") ),
           GRAPPE_2        =SIMP(statut='f',typ='TXM',
                                 into=("ASC_CEN","ASC_EXC","DES_CEN","DES_EXC") ),
           NOEUD           =SIMP(statut='f',typ=no),
           CARA_ELEM       =SIMP(statut='f',typ=cara_elem ),
           MODELE          =SIMP(statut='f',typ=modele ),
           COEF_MASS_AJOU  =SIMP(statut='f',typ='R' ),
           RHO_FLUI        =SIMP(statut='f',typ='R' ),
           UNITE_CA        =SIMP(statut='f',typ='I',defaut=70),
           UNITE_KA        =SIMP(statut='f',typ='I',defaut=71),            
         ),
         FAISCEAU_AXIAL  =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('GROUP_MA','TRI_GROUP_MA'),
                   UN_PARMI('CARA_ELEM','RAYON_TUBE'),
                   ENSEMBLE('RAYON_TUBE','COOR_TUBE'),
                   PRESENT_ABSENT('RAYON_TUBE','TRI_GROUP_MA'),
                   ENSEMBLE('CARA_PAROI','VALE_PAROI'),
                   ENSEMBLE('LONG_TYPG','LARG_TYPG','EPAI_TYPG','RUGO_TYPG','COEF_TRAI_TYPG','COEF_DPOR_TYPG',
                            'COOR_GRILLE','TYPE_GRILLE', ),),
#  on doit pouvoir mettre des blocs conditionnels mais pas assez d infos pour le faire                            
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           TRI_GROUP_MA    =SIMP(statut='f',typ='TXM' ),
           VECT_X          =SIMP(statut='f',typ='R',max=03),
           PROF_RHO_FLUI   =SIMP(statut='f',typ=fonction ),
           PROF_VISC_CINE  =SIMP(statut='f',typ=fonction ),
           CARA_ELEM       =SIMP(statut='f',typ=cara_elem ),
           RAYON_TUBE      =SIMP(statut='f',typ='R' ),
           COOR_TUBE       =SIMP(statut='f',typ='R',max='**'),
           PESANTEUR       =SIMP(statut='f',typ='R',min=04,max=04),
           RUGO_TUBE       =SIMP(statut='f',typ='R' ),
           CARA_PAROI      =SIMP(statut='f',typ='TXM',max=05,
                                 into=("YC","ZC","R","HY","HZ") ),
           VALE_PAROI      =SIMP(statut='f',typ='R',max=05),
           ANGL_VRIL       =SIMP(statut='f',typ='R' ),
           LONG_TYPG       =SIMP(statut='f',typ='R',max='**',val_min=0.E+0),
           LARG_TYPG       =SIMP(statut='f',typ='R',max='**',val_min=0.E+0),
           EPAI_TYPG       =SIMP(statut='f',typ='R',max='**',val_min=0.E+0),
           RUGO_TYPG       =SIMP(statut='f',typ='R',max='**',val_min=0.E+0),
           COEF_TRAI_TYPG  =SIMP(statut='f',typ='R',max='**',val_min=0.E+0),
           COEF_DPOR_TYPG  =SIMP(statut='f',typ='R',max='**'),
           COOR_GRILLE     =SIMP(statut='f',typ='R',max='**'),
           TYPE_GRILLE     =SIMP(statut='f',typ='I',max='**'),
         ),
         COQUE_COAX      =FACT(statut='f',min=00,max=01,
           MASS_AJOU       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           GROUP_MA_INT    =SIMP(statut='o',typ=grma),
           GROUP_MA_EXT    =SIMP(statut='o',typ=grma),
           VECT_X          =SIMP(statut='o',typ='R',max='**'),
           CARA_ELEM       =SIMP(statut='o',typ=cara_elem ),
           MATER_INT       =SIMP(statut='o',typ=mater ),
           MATER_EXT       =SIMP(statut='o',typ=mater ),
           RHO_FLUI        =SIMP(statut='o',typ='R' ),
           VISC_CINE       =SIMP(statut='o',typ='R' ),
           RUGOSITE        =SIMP(statut='o',typ='R' ),
           PDC_MOY_1       =SIMP(statut='o',typ='R' ),
           PDC_DYN_1       =SIMP(statut='o',typ='R' ),
           PDC_MOY_2       =SIMP(statut='o',typ='R' ),
           PDC_DYN_2       =SIMP(statut='o',typ='R' ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 23/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_FONC_ELEC=OPER(nom="DEFI_FONC_ELEC",op=64,sd_prod=fonction,docu="U4.MK.10-e",reentrant='n',
                    fr="D�finition d une fonction du temps pour calculer des forces de LAPLACE",
      regles=(UN_PARMI('COUR_PRIN','COUR'),
              EXCLUS('COUR','COUR_SECO'), ),
         FREQ            =SIMP(statut='f',typ='R',defaut= 50.),
         SIGNAL          =SIMP(statut='f',typ='TXM',defaut="COMPLET",into=("COMPLET","CONTINU") ),
         COUR            =FACT(statut='f',min=1,max='**',
         fr="D�finition du courant de court-circuit",
           regles=(UN_PARMI('PHI_CC_1','INTC_CC_1'),
                   UN_PARMI('PHI_CC_2','INTC_CC_2'),),
           INTE_CC_1       =SIMP(statut='o',typ='R'),
           TAU_CC_1        =SIMP(statut='o',typ='R'),
           PHI_CC_1        =SIMP(statut='f',typ='R'),
           INTC_CC_1       =SIMP(statut='f',typ='R'),
           INTE_CC_2       =SIMP(statut='o',typ='R'),
           TAU_CC_2        =SIMP(statut='o',typ='R'),
           PHI_CC_2        =SIMP(statut='f',typ='R'),
           INTC_CC_2       =SIMP(statut='f',typ='R'),
           INST_CC_INIT    =SIMP(statut='o',typ='R'),
           INST_CC_FIN     =SIMP(statut='o',typ='R'),
         ),
         COUR_PRIN       =FACT(statut='f',min=1,max=1,
         fr="D�finition du courant de court-circuit avec r�enclenchement",
           regles=(UN_PARMI('PHI_CC_1','INTC_CC_1'),),
           INTE_CC_1       =SIMP(statut='o',typ='R'),
           TAU_CC_1        =SIMP(statut='o',typ='R'),
           PHI_CC_1        =SIMP(statut='f',typ='R'),
           INTC_CC_1       =SIMP(statut='f',typ='R'),
           INTE_RENC_1     =SIMP(statut='f',typ='R'),
           TAU_RENC_1      =SIMP(statut='f',typ='R'),
           PHI_RENC_1      =SIMP(statut='f',typ='R'),
           INST_CC_INIT    =SIMP(statut='o',typ='R'),
           INST_CC_FIN     =SIMP(statut='o',typ='R'),
           INST_RENC_INIT  =SIMP(statut='f',typ='R',defaut= 0.0E+0),
           INST_RENC_FIN   =SIMP(statut='f',typ='R',defaut= 0.0E+0),
         ),
         COUR_SECO       =FACT(statut='f',min=1,max='**',
         fr="D�finition du courant de court-circuit avec un intervalle de temps diff�rent de celui de COUR_PRIN",
           regles=(UN_PARMI('PHI_CC_2','INTC_CC_2'),),
           INTE_CC_2       =SIMP(statut='o',typ='R'),
           TAU_CC_2        =SIMP(statut='o',typ='R'),
           PHI_CC_2        =SIMP(statut='f',typ='R'),
           INTC_CC_2       =SIMP(statut='f',typ='R'),
           INTE_RENC_2     =SIMP(statut='f',typ='R'),
           TAU_RENC_2      =SIMP(statut='f',typ='R'),
           PHI_RENC_2      =SIMP(statut='f',typ='R'),
           DIST            =SIMP(statut='f',typ='R',defaut=1.0E+0),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_FONC_FLUI=OPER(nom="DEFI_FONC_FLUI",op= 142,sd_prod=fonction,
                    docu="U4.35.01-c",reentrant='n',
         MAILLAGE        =SIMP(statut='o',typ=(maillage) ),
         NOEUD_INIT      =SIMP(statut='o',typ=no),
         NOEUD_FIN       =SIMP(statut='o',typ=no),
         VITE            =FACT(statut='o',min=1,max=1,
           VALE            =SIMP(statut='f',typ='R',defaut= 1. ),
           PROFIL          =SIMP(statut='o',typ='TXM',into=("UNIFORME","LEONARD") ),
           NB_BAV          =SIMP(statut='f',typ='I',defaut= 0,into=( 0 , 2 , 3 ) ),
         ),
         INTERPOL        =SIMP(statut='f',typ='TXM',max=2,defaut="LIN",
                               into=("NON","LIN","LOG") ),
         PROL_DROITE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",
                               into=("CONSTANT","LINEAIRE","EXCLU") ),
         PROL_GAUCHE     =SIMP(statut='f',typ='TXM' ,defaut="EXCLU",
                               into=("CONSTANT","LINEAIRE","EXCLU") ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE MCOURTOI M.COURTOIS
def defi_fonction_prod(VALE,VALE_PARA,VALE_C,NOEUD_PARA,**args):
  if VALE != None  : return fonction
  if VALE_C != None  : return fonction_c
  if VALE_PARA != None  : return fonction
  if NOEUD_PARA != None  : return fonction
  raise AsException("type de concept resultat non prevu")

DEFI_FONCTION=OPER(nom="DEFI_FONCTION",op=3,sd_prod=defi_fonction_prod
                    ,fr="D�finition des valeurs r�elles ou complexes d une fonction r�elle",
                     docu="U4.31.02-f1",reentrant='n',
         regles=(UN_PARMI('VALE','VALE_C','VALE_PARA','NOEUD_PARA'),),
         NOM_PARA        =SIMP(statut='o',typ='TXM',
                               into=("DX","DY","DZ","DRX","DRY","DRZ","TEMP",
                                     "INST","X","Y","Z","EPSI","META","FREQ","PULS",
                                     "AMOR","ABSC","SIGM","HYDR","SECH","PORO","SAT",
                                     "PGAZ","PCAP","VITE") ),
         NOM_RESU        =SIMP(statut='f',typ='TXM',defaut="TOUTRESU"),
         VALE            =SIMP(statut='f',typ='R',min=2,max='**',
                               fr ="Fonction r�elle d�finie par une liste de couples (abscisse,ordonn�e)"),
         VALE_C          =SIMP(statut='f',typ='R',min=2,max='**',
                               fr ="Fonction complexe d�finie par une liste de couples"),
         VALE_PARA       =SIMP(statut='f',typ=listr8,
                               fr ="Fonction r�elle d�finie par deux concepts de type listr8" ),
         b_vale_para     =BLOC(condition = "VALE_PARA != None",
           VALE_FONC       =SIMP(statut='o',typ=listr8 ),
         ),
         NOEUD_PARA      =SIMP(statut='f',typ=no,max='**',
                               fr ="Fonction r�elle d�finie par une liste de noeuds et un maillage"),
         b_noeud_para    =BLOC(condition = "NOEUD_PARA != None",
           MAILLAGE        =SIMP(statut='o',typ=maillage ),
           VALE_Y          =SIMP(statut='o',typ='R',max='**'),
         ),

         INTERPOL        =SIMP(statut='f',typ='TXM',max=2,defaut="LIN",into=("NON","LIN","LOG") ),
         PROL_DROITE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
         PROL_GAUCHE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
         VERIF           =SIMP(statut='f',typ='TXM',defaut="CROISSANT",into=("CROISSANT","NON") ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_FOND_FISS=OPER(nom="DEFI_FOND_FISS",op=55,sd_prod=fond_fiss,docu="U4.82.01-e",reentrant='n',
                    fr="D�finition de l�vres et d un fond de fissure en 3D",
         regles=(UN_PARMI('FOND','FOND_FERME'),
                 EXCLUS('FOND_FERME','DTAN_ORIG'),
                 EXCLUS('FOND_FERME','DTAN_EXTR'),
                      EXCLUS('FOND_FERME','VECT_GRNO_ORIG'),
                      EXCLUS('FOND_FERME','VECT_GRNO_EXTR'),
                 UN_PARMI('LEVRE_SUP','NORMALE'),
                      EXCLUS('LEVRE_INF','NORMALE'),
                 ENSEMBLE('DTAN_ORIG','DTAN_EXTR'),
                      ENSEMBLE('VECT_GRNO_ORIG','VECT_GRNO_EXTR'),
                      EXCLUS('DTAN_ORIG','VECT_GRNO_ORIG'),
                      EXCLUS('DTAN_EXTR','VECT_GRNO_EXTR') ,),
           MAILLAGE        =SIMP(statut='o',typ=maillage ),
           FOND            =FACT(statut='f',min=01,max=01,
             regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE'),
                     EXCLUS('NOEUD_ORIG','GROUP_NO_ORIG'),
                          EXCLUS('NOEUD_EXTR','GROUP_NO_EXTR'),),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
#  � mettre � jour le max vaut-il 1  
             NOEUD_ORIG      =SIMP(statut='f',typ=no,max=1),
             GROUP_NO_ORIG   =SIMP(statut='f',typ=grno,max=1),
             NOEUD_EXTR      =SIMP(statut='f',typ=no,max=1),
             GROUP_NO_EXTR   =SIMP(statut='f',typ=grno,max=1),
           ),
           FOND_FERME      =FACT(statut='f',min=01,max=01,
             regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE'),
                          EXCLUS('NOEUD_ORIG','GROUP_NO_ORIG'),),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             NOEUD_ORIG      =SIMP(statut='f',typ=no,max=1),
             GROUP_NO_ORIG   =SIMP(statut='f',typ=grno,max=1),
             MAILLE_ORIG     =SIMP(statut='f',typ=ma,max=1),
             GROUP_MA_ORIG   =SIMP(statut='f',typ=ma,max=1),
           ),
           LEVRE_SUP       =FACT(statut='f',min=01,max=01,
             regles=(UN_PARMI('GROUP_MA','MAILLE'),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           ),
           LEVRE_INF       =FACT(statut='f',min=01,max=01,
             regles=(UN_PARMI('GROUP_MA','MAILLE', ),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           ),
           NORMALE         =SIMP(statut='f',typ='R',max='**'),
           DTAN_ORIG       =SIMP(statut='f',typ='R',max='**'),
           DTAN_EXTR       =SIMP(statut='f',typ='R',max='**'),
           VECT_GRNO_ORIG  =SIMP(statut='f',typ=grno,max=2),
           VECT_GRNO_EXTR  =SIMP(statut='f',typ=grno,max=2),
           INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 30/01/2002   AUTEUR VABHHTS J.TESELET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def defi_group_prod(MAILLAGE,**args):
  if AsType(MAILLAGE) == maillage : return maillage
  if AsType(MAILLAGE) == squelette : return squelette
  raise AsException("type de concept resultat non prevu")

DEFI_GROUP=OPER(nom="DEFI_GROUP",op= 104,sd_prod=defi_group_prod,
                fr="D�finition de nouveaux groupes de noeuds et/ou de mailles dans un concept maillage",
                docu="U4.22.01-e",reentrant='o',
         regles=(AU_MOINS_UN('CREA_GROUP_MA','CREA_GROUP_NO'),),            
         MAILLAGE        =SIMP(statut='o',typ=(maillage,squelette) ),
         
         CREA_GROUP_MA   =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','GROUP_MA','MAILLE','INTERSEC','UNION','DIFFE','OPTION'),),
#  quel est le concept attendu deriere NOM
           NOM             =SIMP(statut='o',typ=grma),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           INTERSEC        =SIMP(statut='f',typ=grma,max='**'),
           UNION           =SIMP(statut='f',typ=grma,max='**'),
           DIFFE           =SIMP(statut='f',typ=grma,max='**'),
           OPTION          =SIMP(statut='f',typ='TXM',into=("FACE_NORMALE","SPHERE","CYLINDRE","BANDE") ),
           b_group_ma      =BLOC(condition = "GROUP_MA != None",
             regles=(EXCLUS('POSITION','NUME_INIT'),),
             NUME_INIT       =SIMP(statut='f',typ='I',defaut= 1 ),             
             POSITION        =SIMP(statut='f',typ='TXM',into=("INIT","FIN","MILIEU") ), 
             b_nume_init   =BLOC(condition = "NUME_INIT != None",
               NUME_FIN        =SIMP(statut='f',typ='I' ),
             ),      
           ),
           b_face_normale  =BLOC(condition = "OPTION == 'FACE_NORMALE'",
             regles=(UN_PARMI('ANGL_NAUT','VECT_NORMALE'),),
             ANGL_NAUT       =SIMP(statut='f',typ='R',max=02),
             VECT_NORMALE    =SIMP(statut='f',typ='R',max=03),
             ANGL_PREC       =SIMP(statut='f',typ='R',defaut= 0.5 ),
             VERI_SIGNE      =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),     
           ),
           b_sphere        =BLOC(condition = "OPTION == 'SPHERE'",
             regles=(UN_PARMI('POINT','NOEUD_CENTRE'),),
             POINT           =SIMP(statut='f',typ='R',max=03),
             NOEUD_CENTRE    =SIMP(statut='f',typ=no),
             RAYON           =SIMP(statut='o',typ='R' ),    
           ),
           b_cylindre      =BLOC(condition = "OPTION == 'CYLINDRE'",
             regles=(UN_PARMI('POINT','NOEUD_CENTRE'),
                     UN_PARMI('ANGL_NAUT','VECT_NORMALE'),),
             POINT           =SIMP(statut='f',typ='R',max=03),
             NOEUD_CENTRE    =SIMP(statut='f',typ=no),
             RAYON           =SIMP(statut='o',typ='R' ), 
             ANGL_NAUT       =SIMP(statut='f',typ='R',max=02),
             VECT_NORMALE    =SIMP(statut='f',typ='R',max=03),   
           ),
           b_bande         =BLOC(condition = "OPTION == 'BANDE'",
             regles=(UN_PARMI('POINT','NOEUD_CENTRE'),
                     UN_PARMI('ANGL_NAUT','VECT_NORMALE'),),
             POINT           =SIMP(statut='f',typ='R',max=03),
             NOEUD_CENTRE    =SIMP(statut='f',typ=no),
             DIST            =SIMP(statut='o',typ='R' ),
             ANGL_NAUT       =SIMP(statut='f',typ='R',max=02),
             VECT_NORMALE    =SIMP(statut='f',typ='R',max=03),   
           ),
         ),
         CREA_GROUP_NO   =FACT(statut='f',min=01,max='**',
           regles = (
         AU_MOINS_UN ('TOUT_GROUP_MA','GROUP_MA','NOEUD',
                     'INTERSEC','UNION','DIFFE','GROUP_NO','OPTION'),
                   EXCLUS ('TOUT_GROUP_MA','GROUP_MA','NOEUD','INTERSEC','UNION','DIFFE'),),
           TOUT_GROUP_MA   =SIMP(statut='f',typ='TXM',into=("OUI",) ),               
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           INTERSEC        =SIMP(statut='f',typ=grno,max='**'),
           UNION           =SIMP(statut='f',typ=grno,max='**'),
           DIFFE           =SIMP(statut='f',typ=grno,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           OPTION          =SIMP(statut='f',typ='TXM',into=("ENV_SPHERE","ENV_CYLINDRE","PLAN",
                                                            "SEGM_DROI_ORDO","NOEUD_ORDO") ),  
           b_nom_group_ma  =BLOC(condition = "GROUP_MA != None",
             NOM             =SIMP(statut='f',typ=grma,max='**'),
           ),
           b_crit_noeud    = BLOC(condition = "GROUP_MA != None",
             CRIT_NOEUD    = SIMP(statut='f',typ='TXM',defaut="TOUS",
                            into=("TOUS","SOMMET","MILIEU","CENTRE"),),),
           b_nom =BLOC(condition = "GROUP_MA == None and TOUT_GROUP_MA == None" ,
             NOM             =SIMP(statut='o',typ=geom),
           ),                                                 
           b_group_no      =BLOC(condition = "GROUP_NO != None",
             regles=(EXCLUS('POSITION','NUME_INIT'),),
             NUME_INIT       =SIMP(statut='f',typ='I',defaut= 1 ),
             POSITION        =SIMP(statut='f',typ='TXM',into=("INIT","FIN","MILIEU") ), 
             b_nume_init     =BLOC(condition = "NUME_INIT != None",
               NUME_FIN        =SIMP(statut='f',typ='I' ),
             ),      
           ),
           b_env_sphere    =BLOC(condition = "OPTION == 'ENV_SPHERE'",
             regles=(UN_PARMI('POINT','NOEUD_CENTRE'),),
             POINT           =SIMP(statut='f',typ='R',max=03),
             NOEUD_CENTRE    =SIMP(statut='f',typ=no,max=01),
             RAYON           =SIMP(statut='o',typ='R' ),
             PRECISION       =SIMP(statut='f',typ='R' ),
             CRITERE         =SIMP(statut='f',typ='TXM',into=("ABSOLU","RELATIF") ),
           ),
           b_env_cylindre  =BLOC(condition = "OPTION == 'ENV_CYLINDRE'",
             regles=(UN_PARMI('POINT','NOEUD_CENTRE'),
                     UN_PARMI('ANGL_NAUT','VECT_NORMALE'),),
             POINT           =SIMP(statut='f',typ='R',max=03),
             NOEUD_CENTRE    =SIMP(statut='f',typ=no,max=01),
             RAYON           =SIMP(statut='o',typ='R' ),
             ANGL_NAUT       =SIMP(statut='f',typ='R',max=03),
             VECT_NORMALE    =SIMP(statut='f',typ='R',max=03),
             PRECISION       =SIMP(statut='f',typ='R' ),
             CRITERE         =SIMP(statut='f',typ='TXM',into=("ABSOLU","RELATIF") ),
           ),
           b_env_plan      =BLOC(condition = "OPTION == 'PLAN'",
             regles=(UN_PARMI('POINT','NOEUD_CENTRE'),
                     UN_PARMI('ANGL_NAUT','VECT_NORMALE'),),
             POINT           =SIMP(statut='f',typ='R',max=03),
             NOEUD_CENTRE    =SIMP(statut='f',typ=no,max=01),
             ANGL_NAUT       =SIMP(statut='f',typ='R',max=03),
             VECT_NORMALE    =SIMP(statut='f',typ='R',max=03),
             PRECISION       =SIMP(statut='f',typ='R' ),
             CRITERE         =SIMP(statut='f',typ='TXM',into=("ABSOLU","RELATIF") ),
           ),
           b_segm_droi_ordo=BLOC(condition = "OPTION == 'SEGM_DROI_ORDO'",
             regles=(UN_PARMI('NOEUD_ORIG','GROUP_NO_ORIG'),
                     UN_PARMI('NOEUD_EXTR','GROUP_NO_EXTR'),), 
             NOEUD_ORIG      =SIMP(statut='f',typ=no),
             GROUP_NO_ORIG   =SIMP(statut='f',typ=grno),
             NOEUD_EXTR      =SIMP(statut='f',typ=no),
             GROUP_NO_EXTR   =SIMP(statut='f',typ=grno),
             PRECISION       =SIMP(statut='f',typ='R' ),
             CRITERE         =SIMP(statut='f',typ='TXM',into=("ABSOLU","RELATIF") ),
           ),
           b_noeud_ordo    =BLOC(condition = "OPTION == 'NOEUD_ORDO'",
             regles=(UN_PARMI('NOEUD_ORIG','GROUP_NO_ORIG'),
                     UN_PARMI('NOEUD_EXTR','GROUP_NO_EXTR'),),
             NOEUD_ORIG      =SIMP(statut='f',typ=no),
             GROUP_NO_ORIG   =SIMP(statut='f',typ=grno),
             NOEUD_EXTR      =SIMP(statut='f',typ=no),
             GROUP_NO_EXTR   =SIMP(statut='f',typ=grno),
             PRECISION       =SIMP(statut='f',typ='R' ),
             CRITERE         =SIMP(statut='f',typ='TXM',into=("ABSOLU","RELATIF") ),
           ),      
         ),
         INFO            =SIMP(statut='f',typ='I',into=( 1 , 2 ) ),
)  ;
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_INTE_SPEC=OPER(nom="DEFI_INTE_SPEC",op= 115,sd_prod=tabl_intsp,
                    docu="U4.36.02-e1",reentrant='n',

         DIMENSION       =SIMP(statut='f',typ='I',defaut= 1 ),

         PAR_FONCTION    =FACT(statut='f',min=1,max='**',
           NUME_ORDRE_I    =SIMP(statut='o',typ='I' ),
           NUME_ORDRE_J    =SIMP(statut='o',typ='I' ),
           FONCTION        =SIMP(statut='o',typ=fonction_c ),
         ),
         KANAI_TAJIMI    =FACT(statut='f',min=1,max='**',
           regles=(EXCLUS('VALE_R','VALE_C'),),
           NUME_ORDRE_I    =SIMP(statut='o',typ='I' ),
           NUME_ORDRE_J    =SIMP(statut='o',typ='I' ),
           FREQ_MIN        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           FREQ_MAX        =SIMP(statut='f',typ='R',defaut= 100. ),
           PAS             =SIMP(statut='f',typ='R',defaut= 1. ),
           AMOR_REDUIT     =SIMP(statut='f',typ='R',defaut= 0.6 ),
           FREQ_MOY        =SIMP(statut='f',typ='R',defaut= 5. ),
           VALE_R          =SIMP(statut='f',typ='R' ),
           VALE_C          =SIMP(statut='f',typ='C' ),
           INTERPOL        =SIMP(statut='f',typ='TXM',max=2,defaut="LIN",into=("NON","LIN","LOG") ),
           PROL_DROITE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
           PROL_GAUCHE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
         ),
         CONSTANT        =FACT(statut='f',min=1,max='**',
           regles=(EXCLUS('VALE_R','VALE_C'),),
           NUME_ORDRE_I    =SIMP(statut='o',typ='I' ),
           NUME_ORDRE_J    =SIMP(statut='o',typ='I' ),
           FREQ_MIN        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           FREQ_MAX        =SIMP(statut='f',typ='R',defaut= 100. ),
           PAS             =SIMP(statut='f',typ='R',defaut= 1. ),
           VALE_R          =SIMP(statut='f',typ='R' ),
           VALE_C          =SIMP(statut='f',typ='C' ),
           INTERPOL        =SIMP(statut='f',typ='TXM',max=2,defaut="LIN",into=("NON","LIN","LOG") ),
           PROL_DROITE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
           PROL_GAUCHE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),               
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_INTERF_DYNA=OPER(nom="DEFI_INTERF_DYNA",op=  98,sd_prod=interf_dyna_clas,
                      docu="U4.64.01-e",reentrant='n',
         NUME_DDL        =SIMP(statut='o',typ=nume_ddl ),
         INTERFACE       =FACT(statut='o',min=01,max='**',
           regles=(ENSEMBLE('NOM','TYPE'),
#  erreur doc U sur la condition qui suit
                   UN_PARMI('NOEUD','GROUP_NO'),),
           NOM             =SIMP(statut='f',typ='TXM' ),
           TYPE            =SIMP(statut='f',typ='TXM',into=("MNEAL","CRAIGB","CB_HARMO","AUCUN") ),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           DDL_ACTIF       =SIMP(statut='f',typ='TXM',max='**'),
           MASQUE          =SIMP(statut='f',typ='TXM',max='**'),
         ),
         FREQ            =SIMP(statut='f',typ='R',defaut= 1.),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
DEFI_LIST_ENTI=OPER(nom="DEFI_LIST_ENTI",op=22,sd_prod=listis,
                    fr="D�finition d une suite croissante d entiers",
                    docu="U4.34.02-f",reentrant='n',
         regles=(UN_PARMI('VALE','DEBUT'),
                 EXCLUS('VALE','INTERVALLE'),),
         VALE            =SIMP(statut='f',typ='I',max='**'),
         DEBUT           =SIMP(statut='f',typ='I'),
         INTERVALLE      =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NOMBRE','PAS'),),
           JUSQU_A         =SIMP(statut='o',typ='I'),
           NOMBRE          =SIMP(statut='f',typ='I',val_min=1,),
           PAS             =SIMP(statut='f',typ='I',val_min=1,),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 07/03/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
DEFI_LIST_REEL=OPER(nom="DEFI_LIST_REEL",op=24,sd_prod=listr8,
                    fr="D�finition d une suite croissante de r�els",
                    docu="U4.34.01-f",reentrant='n',
         regles=(UN_PARMI('VALE','DEBUT',),
                 EXCLUS('VALE','INTERVALLE'),
                 ENSEMBLE('DEBUT','INTERVALLE')),
         VALE            =SIMP(statut='f',typ='R',max='**'),
         DEBUT           =SIMP(statut='f',typ='R'),
         INTERVALLE      =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NOMBRE','PAS'),),
           JUSQU_A         =SIMP(statut='o',typ='R'),
           NOMBRE          =SIMP(statut='f',typ='I'),
           PAS             =SIMP(statut='f',typ='R'),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
DEFI_MAILLAGE=OPER(nom="DEFI_MAILLAGE",op=  88,sd_prod=maillage,
                   fr="D�finition d un nouveau maillage � partir de macro �l�ments",
                   docu="U4.23.01-e",reentrant='n',
         DEFI_MAILLE     =FACT(statut='o',min=01,max='**',
           MACR_ELEM_STAT  =SIMP(statut='o',typ=macr_elem_stat,max='**' ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           TRAN            =SIMP(statut='f',typ='R',max=03),
           ANGL_NAUT       =SIMP(statut='f',typ='R',max=03),
           b_angl_naut     =BLOC(condition = "ANGL_NAUT != None",
             CENTRE          =SIMP(statut='f',typ='R',max=03),
           ),
         ),
         RECO_GLOBAL     =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
         ),
         RECO_MAILLE     =FACT(statut='f',min=01,max='**',
           MAILLE          =SIMP(statut='o',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='o',typ=grno,max='**'),
           OPTION          =SIMP(statut='f',typ='TXM',defaut="GEOMETRIQUE",into=("GEOMETRIQUE","NOEUD_A_NOEUD","INVERSE") ),
           geometrique     =BLOC(condition = "OPTION == 'GEOMETRIQUE'",
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           ),
         ),
         DEFI_NOEUD      =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','NOEUD_INIT'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",),
                                 fr="Renommage de tous les noeuds" ),
           NOEUD_INIT      =SIMP(statut='f',typ=no,
                                 fr="Renommage d un seul noeud"),                     
           b_tout          =BLOC(condition = "TOUT != None",
             PREFIXE         =SIMP(statut='f',typ='TXM' ),
             INDEX           =SIMP(statut='o',typ='I',max='**'),
           ),
           b_noeud_init    =BLOC(condition = "NOEUD_INIT != None",
             MAILLE          =SIMP(statut='o',typ=ma),
             NOEUD_FIN       =SIMP(statut='o',typ=no),
           ),        
         ),
         DEFI_GROUP_NO   =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','MAILLE'),
                AU_MOINS_UN('INDEX','GROUP_NO_FIN'),
                   ENSEMBLE('GROUP_NO_INIT','GROUP_NO_FIN'),),
#  la regle ancien catalogue AU_MOINS_UN__: ( INDEX , GROUP_NO_FIN ) incoherente avec doc U           
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",),
                                 fr="Cr�ation de plusieurs groupes de noeuds" ),
           MAILLE          =SIMP(statut='f',typ=ma,
                                 fr="Cr�ation de plusieurs groupes de noeuds"),
           GROUP_NO_INIT   =SIMP(statut='f',typ=grno,
                                 fr="Cr�ation d un seul groupe de noeuds"),
           PREFIXE         =SIMP(statut='f',typ='TXM' ),
           INDEX           =SIMP(statut='f',typ='I',max='**'),
           GROUP_NO_FIN    =SIMP(statut='f',typ=grno),
         ),
)  ;
#& MODIF COMMANDE  DATE 30/01/2002   AUTEUR VABHHTS J.TESELET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_MATERIAU=OPER(nom="DEFI_MATERIAU",op=5,sd_prod=mater,
                   fr="D�finition des param�tres d�crivant le comportement d un mat�riau",
                   docu="U4.43.01-f1",reentrant='n',
       regles=(EXCLUS('ELAS','ELAS_FO','ELAS_FLUI','ELAS_ISTR','ELAS_ISTR_FO','ELAS_ORTH',
                      'ELAS_ORTH_FO','ELAS_COQUE','ELAS_COQUE_FO',
                      'SURF_ETAT_SATU','CAM_CLAY_THM','SURF_ETAT_NSAT'),
               EXCLUS('THER','THER_FO','THER_ORTH','THER_NL'),
               EXCLUS('ECRO_LINE','ECRO_LINE_FO'),
               EXCLUS('TAHERI','TAHERI_FO'),
               EXCLUS('ROUSSELIER','ROUSSELIER_FO'),
               PRESENT_PRESENT('ROUSSELIER','TRACTION'),
               PRESENT_PRESENT('ROUSSELIER_FO','TRACTION'),
               EXCLUS('CIN1_CHAB','CIN1_CHAB_FO'),
               EXCLUS('CIN2_CHAB','CIN2_CHAB_FO'),
               EXCLUS('VISCOCHAB','VISCOCHAB_FO'),
               EXCLUS('POLY_CFC','POLY_CFC_FO'),
               EXCLUS('LEMAITRE','LEMAITRE_FO','ZIRC_CYRA2','ZIRC_EPRI'),
               EXCLUS('OHNO','OHNO_FO'),
               EXCLUS('LMARC','LMARC_FO'),
               EXCLUS('VMIS_POUTRE','VMIS_POUTRE_FO'),
               EXCLUS('VENDOCHAB','VENDOCHAB_FO'),
               PRESENT_PRESENT('BPEL_BETON','ELAS'),
               PRESENT_PRESENT('BPEL_ACIER','ELAS'),
               EXCLUS('RCCM','RCCM_FO'),
               EXCLUS('WEIBULL','WEIBULL_FO'),),
#
# comportement �lastique
#
           ELAS            =FACT(statut='f',min=0,max=1,
             E               =SIMP(statut='o',typ='R',val_min=0.E+0),
             NU              =SIMP(statut='o',typ='R',val_min=-1.E+0,val_max=0.5E+0),
             RHO             =SIMP(statut='f',typ='R'),
             ALPHA           =SIMP(statut='f',typ='R'),
             AMOR_ALPHA      =SIMP(statut='f',typ='R'),
             AMOR_BETA       =SIMP(statut='f',typ='R'),
             AMOR_HYST       =SIMP(statut='f',typ='R'),
           ),
           ELAS_FO         =FACT(statut='f',min=0,max=1,
             E               =SIMP(statut='o',typ=fonction),
             NU              =SIMP(statut='o',typ=fonction),
             RHO             =SIMP(statut='f',typ='R'),
             TEMP_DEF_ALPHA  =SIMP(statut='f',typ='R'),
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.),
             ALPHA           =SIMP(statut='f',typ=fonction),
             AMOR_ALPHA      =SIMP(statut='f',typ=fonction),
             AMOR_BETA       =SIMP(statut='f',typ=fonction),
             AMOR_HYST       =SIMP(statut='f',typ=fonction),
             K_DESSIC        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             B_ENDOGE        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP","INST",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="INST",into=("TEMP","INST",) ),
             VERI_P3         =SIMP(statut='c',typ='TXM',defaut="HYDR",into=("HYDR",) ),
             VERI_P4         =SIMP(statut='c',typ='TXM',defaut="SECH",into=("SECH",) ),
           ),
           ELAS_FLUI       =FACT(statut='f',min=0,max=1,
             E               =SIMP(statut='o',typ='R'),
             NU              =SIMP(statut='o',typ='R'),
             RHO             =SIMP(statut='o',typ='R'),
             PROF_RHO_F_INT  =SIMP(statut='o',typ=fonction),
             PROF_RHO_F_EXT  =SIMP(statut='o',typ=fonction),
             COEF_MASS_AJOU  =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="ABSC",into=("ABSC",) ),
           ),
           ELAS_ISTR       =FACT(statut='f',min=0,max=1,
             E_L             =SIMP(statut='o',typ='R'),
             E_N             =SIMP(statut='o',typ='R'),
             NU_LT           =SIMP(statut='o',typ='R'),
             NU_LN           =SIMP(statut='o',typ='R'),
             G_LN            =SIMP(statut='o',typ='R'),
             RHO             =SIMP(statut='f',typ='R'),
             ALPHA_L         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             ALPHA_N         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
           ELAS_ISTR_FO    =FACT(statut='f',min=0,max=1,
             E_L             =SIMP(statut='o',typ=fonction),
             E_N             =SIMP(statut='o',typ=fonction),
             NU_LT           =SIMP(statut='o',typ=fonction),
             NU_LN           =SIMP(statut='o',typ=fonction),
             G_LN            =SIMP(statut='o',typ=fonction),
             RHO             =SIMP(statut='f',typ='R'),
             TEMP_DEF_ALPHA  =SIMP(statut='f',typ='R'),
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.),
             ALPHA_L         =SIMP(statut='f',typ=fonction),
             ALPHA_N         =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP","INST")),
           ),
           ELAS_ORTH       =FACT(statut='f',min=0,max=1,
             E_L             =SIMP(statut='o',typ='R'),
             E_T             =SIMP(statut='o',typ='R'),
             E_N             =SIMP(statut='f',typ='R'),
             NU_LT           =SIMP(statut='o',typ='R'),
             NU_LN           =SIMP(statut='f',typ='R'),
             NU_TN           =SIMP(statut='f',typ='R'),
             G_LT            =SIMP(statut='o',typ='R'),
             G_LN            =SIMP(statut='f',typ='R'),
             G_TN            =SIMP(statut='f',typ='R'),
             RHO             =SIMP(statut='f',typ='R'),
             ALPHA_L         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             ALPHA_T         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             ALPHA_N         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             XT              =SIMP(statut='f',typ='R',defaut= 1. ),
             XC              =SIMP(statut='f',typ='R',defaut= 1. ),
             YT              =SIMP(statut='f',typ='R',defaut= 1. ),
             YC              =SIMP(statut='f',typ='R',defaut= 1. ),
             S_LT            =SIMP(statut='f',typ='R',defaut= 1. ),
           ),
           ELAS_ORTH_FO    =FACT(statut='f',min=0,max=1,
             E_L             =SIMP(statut='o',typ=fonction),
             E_T             =SIMP(statut='o',typ=fonction),
             E_N             =SIMP(statut='o',typ=fonction),
             NU_LT           =SIMP(statut='o',typ=fonction),
             NU_LN           =SIMP(statut='o',typ=fonction),
             NU_TN           =SIMP(statut='o',typ=fonction),
             G_LT            =SIMP(statut='o',typ=fonction),
             G_LN            =SIMP(statut='o',typ=fonction),
             G_TN            =SIMP(statut='o',typ=fonction),
             RHO             =SIMP(statut='f',typ='R'),
             TEMP_DEF_ALPHA  =SIMP(statut='f',typ='R'),
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1. ),
             ALPHA_L         =SIMP(statut='f',typ=fonction),
             ALPHA_T         =SIMP(statut='f',typ=fonction),
             ALPHA_N         =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP","INST",) ),
           ),
           ELAS_THM        =FACT(statut='f',min=0,max=1,
             RHO_S           =SIMP(statut='o',typ='R'),
             UN_SUR_KS       =SIMP(statut='o',typ='R'),
             E               =SIMP(statut='f',typ='R'),
             KB              =SIMP(statut='f',typ='R'),
             D_KB_T          =SIMP(statut='f',typ='R'),
             ALPHA_S         =SIMP(statut='f',typ='R'),
             ALPHA_D         =SIMP(statut='f',typ='R'),
           ),
           SURF_ETAT_SATU  =FACT(statut='f',min=0,max=1,
             E_CHAR          =SIMP(statut='o',typ='R'),
             E_DECHAR        =SIMP(statut='o',typ='R'),
             XN              =SIMP(statut='f',typ='R'),
             RF              =SIMP(statut='f',typ='R'),
             EV_KB           =SIMP(statut='f',typ='R'),
             EV_XM           =SIMP(statut='f',typ='R'),
             D_E_T           =SIMP(statut='f',typ='R'),
             ALPHA0          =SIMP(statut='f',typ='R'),
             ALPHA1          =SIMP(statut='f',typ='R'),
             ALPHA2          =SIMP(statut='f',typ='R'),
             ALPHA3          =SIMP(statut='f',typ='R'),
             ALPHA_S         =SIMP(statut='f',typ='R'),
             ANG_FRT         =SIMP(statut='o',typ='R'),
             COHE            =SIMP(statut='o',typ='R'),
             RESI_TRAC       =SIMP(statut='o',typ='R'),
           ),
           CAM_CLAY_THM    =FACT(statut='f',min=0,max=1,
             NU              =SIMP(statut='f',typ='R'),
             LAMBDA          =SIMP(statut='o',typ='R'),
             KAPA            =SIMP(statut='o',typ='R'),
             M               =SIMP(statut='f',typ='R'),
             PRES_CRIT       =SIMP(statut='f',typ='R'),
             GAMA            =SIMP(statut='o',typ='R'),
             A0_PC           =SIMP(statut='o',typ='R'),
             A1_PC           =SIMP(statut='f',typ='R'),
             A2_PC           =SIMP(statut='f',typ='R'),
             ALPHA0_PC       =SIMP(statut='f',typ='R'),
             ALPHA1_PC       =SIMP(statut='f',typ='R'),
             ALPHA2_PC       =SIMP(statut='f',typ='R'),
             ALPHA3_PC       =SIMP(statut='f',typ='R'),
             ALPHA_S         =SIMP(statut='f',typ='R'),
                         ),
           SURF_ETAT_NSAT  =FACT(statut='f',min=0,max=1,
             E_CHAR          =SIMP(statut='o',typ='R'),
             E_DECHAR        =SIMP(statut='o',typ='R'),
             XN              =SIMP(statut='f',typ='R'),
             RF              =SIMP(statut='f',typ='R'),
             EV_KB           =SIMP(statut='f',typ='R'),
             EV_XM           =SIMP(statut='f',typ='R'),
             EV_A            =SIMP(statut='f',typ='R'),
             EV_B            =SIMP(statut='f',typ='R'),
             EV_CT           =SIMP(statut='f',typ='R'),
             EV_SIGB         =SIMP(statut='f',typ='R'),
             D_E_T           =SIMP(statut='f',typ='R'),
             D_E_SUCC        =SIMP(statut='f',typ='R'),
             ANG_FRT         =SIMP(statut='o',typ='R'),
             COHE            =SIMP(statut='o',typ='R'),
             D_COEH_SUCC     =SIMP(statut='f',typ='R'),
             ANG_FRT_ULT     =SIMP(statut='f',typ='R'),
             SUCC_ULTM       =SIMP(statut='f',typ='R'),
             RESI_TRAC       =SIMP(statut='f',typ='R'),
             A_SURF_SATU     =SIMP(statut='f',typ='R'),
             B_SURF_SATU     =SIMP(statut='f',typ='R'),
             C_SURF_SATU     =SIMP(statut='f',typ='R'),
             D_SURF_SATU     =SIMP(statut='f',typ='R'),
           ),
           ELAS_COQUE      =FACT(statut='f',min=0,max=1,
             regles=(EXCLUS('MEMB_L','M_LLLL',),
                     PRESENT_PRESENT('MEMB_L','MEMB_LT', 'MEMB_T','MEMB_G_LT','FLEX_L','FLEX_LT',
                                     'FLEX_T','FLEX_G_LT','CISA_L','CISA_T',),
                     PRESENT_PRESENT('M_LLLL','M_LLTT','M_LLLT','M_TTTT','M_TTLT','M_LTLT','F_LLLL',
                                     'F_LLTT','F_LLLT','F_TTTT','F_TTLT','F_LTLT','MF_LLLL',
                                     'MF_LLTT','MF_LLLT','MF_TTTT','MF_TTLT','MF_LTLT','MC_LLLZ',
                                     'MC_LLTZ','MC_TTLZ','MC_TTTZ','MC_LTLZ','MC_LTTZ','FC_LLLZ',
                                     'FC_LLTZ','FC_TTLZ','FC_TTTZ','FC_LTLZ','FC_LTTZ','C_LZLZ',
                                     'C_LZTZ','C_TZTZ'),),
             MEMB_L          =SIMP(statut='f',typ='R'),
             MEMB_LT         =SIMP(statut='f',typ='R'),
             MEMB_T          =SIMP(statut='f',typ='R'),
             MEMB_G_LT       =SIMP(statut='f',typ='R'),
             FLEX_L          =SIMP(statut='f',typ='R'),
             FLEX_LT         =SIMP(statut='f',typ='R'),
             FLEX_T          =SIMP(statut='f',typ='R'),
             FLEX_G_LT       =SIMP(statut='f',typ='R'),
             CISA_L          =SIMP(statut='f',typ='R'),
             CISA_T          =SIMP(statut='f',typ='R'),
             M_LLLL          =SIMP(statut='f',typ='R'),
             M_LLTT          =SIMP(statut='f',typ='R'),
             M_LLLT          =SIMP(statut='f',typ='R'),
             M_TTTT          =SIMP(statut='f',typ='R'),
             M_TTLT          =SIMP(statut='f',typ='R'),
             M_LTLT          =SIMP(statut='f',typ='R'),
             F_LLLL          =SIMP(statut='f',typ='R'),
             F_LLTT          =SIMP(statut='f',typ='R'),
             F_LLLT          =SIMP(statut='f',typ='R'),
             F_TTTT          =SIMP(statut='f',typ='R'),
             F_TTLT          =SIMP(statut='f',typ='R'),
             F_LTLT          =SIMP(statut='f',typ='R'),
             MF_LLLL         =SIMP(statut='f',typ='R'),
             MF_LLTT         =SIMP(statut='f',typ='R'),
             MF_LLLT         =SIMP(statut='f',typ='R'),
             MF_TTTT         =SIMP(statut='f',typ='R'),
             MF_TTLT         =SIMP(statut='f',typ='R'),
             MF_LTLT         =SIMP(statut='f',typ='R'),
             MC_LLLZ         =SIMP(statut='f',typ='R'),
             MC_LLTZ         =SIMP(statut='f',typ='R'),
             MC_TTLZ         =SIMP(statut='f',typ='R'),
             MC_TTTZ         =SIMP(statut='f',typ='R'),
             MC_LTLZ         =SIMP(statut='f',typ='R'),
             MC_LTTZ         =SIMP(statut='f',typ='R'),
             FC_LLLZ         =SIMP(statut='f',typ='R'),
             FC_LLTZ         =SIMP(statut='f',typ='R'),
             FC_TTLZ         =SIMP(statut='f',typ='R'),
             FC_TTTZ         =SIMP(statut='f',typ='R'),
             FC_LTLZ         =SIMP(statut='f',typ='R'),
             FC_LTTZ         =SIMP(statut='f',typ='R'),
             C_LZLZ          =SIMP(statut='f',typ='R'),
             C_LZTZ          =SIMP(statut='f',typ='R'),
             C_TZTZ          =SIMP(statut='f',typ='R'),
             RHO             =SIMP(statut='f',typ='R'),
             ALPHA           =SIMP(statut='f',typ='R'),
           ),
           ELAS_COQUE_FO   =FACT(statut='f',min=0,max=1,
             regles=(EXCLUS('MEMB_L','M_LLLL',),
                     PRESENT_PRESENT('MEMB_L','MEMB_LT','MEMB_T','MEMB_G_LT','FLEX_L','FLEX_LT',
                                     'FLEX_T','FLEX_G_LT','CISA_L','CISA_T',),
                     PRESENT_PRESENT('M_LLLL','M_LLTT','M_LLLT','M_TTTT','M_TTLT','M_LTLT','F_LLLL',
                                     'F_LLTT','F_LLLT','F_TTTT','F_TTLT','F_LTLT','MF_LLLL','MF_LLTT',
                                     'MF_LLLT','MF_TTTT','MF_TTLT','MF_LTLT','MC_LLLZ','MC_LLTZ',
                                     'MC_TTLZ','MC_TTTZ','MC_LTLZ','MC_LTTZ','FC_LLLZ','FC_LLTZ',
                                     'FC_TTLZ','FC_TTTZ','FC_LTLZ','FC_LTTZ','C_LZLZ','C_LZTZ','C_TZTZ'),),
             MEMB_L          =SIMP(statut='f',typ=fonction),
             MEMB_LT         =SIMP(statut='f',typ=fonction),
             MEMB_T          =SIMP(statut='f',typ=fonction),
             MEMB_G_LT       =SIMP(statut='f',typ=fonction),
             FLEX_L          =SIMP(statut='f',typ=fonction),
             FLEX_LT         =SIMP(statut='f',typ=fonction),
             FLEX_T          =SIMP(statut='f',typ=fonction),
             FLEX_G_LT       =SIMP(statut='f',typ=fonction),
             CISA_L          =SIMP(statut='f',typ=fonction),
             CISA_T          =SIMP(statut='f',typ=fonction),
             M_LLLL          =SIMP(statut='f',typ=fonction),
             M_LLTT          =SIMP(statut='f',typ=fonction),
             M_LLLT          =SIMP(statut='f',typ=fonction),
             M_TTTT          =SIMP(statut='f',typ=fonction),
             M_TTLT          =SIMP(statut='f',typ=fonction),
             M_LTLT          =SIMP(statut='f',typ=fonction),
             F_LLLL          =SIMP(statut='f',typ=fonction),
             F_LLTT          =SIMP(statut='f',typ=fonction),
             F_LLLT          =SIMP(statut='f',typ=fonction),
             F_TTTT          =SIMP(statut='f',typ=fonction),
             F_TTLT          =SIMP(statut='f',typ=fonction),
             F_LTLT          =SIMP(statut='f',typ=fonction),
             MF_LLLL         =SIMP(statut='f',typ=fonction),
             MF_LLTT         =SIMP(statut='f',typ=fonction),
             MF_LLLT         =SIMP(statut='f',typ=fonction),
             MF_TTTT         =SIMP(statut='f',typ=fonction),
             MF_TTLT         =SIMP(statut='f',typ=fonction),
             MF_LTLT         =SIMP(statut='f',typ=fonction),
             MC_LLLZ         =SIMP(statut='f',typ=fonction),
             MC_LLTZ         =SIMP(statut='f',typ=fonction),
             MC_TTLZ         =SIMP(statut='f',typ=fonction),
             MC_TTTZ         =SIMP(statut='f',typ=fonction),
             MC_LTLZ         =SIMP(statut='f',typ=fonction),
             MC_LTTZ         =SIMP(statut='f',typ=fonction),
             FC_LLLZ         =SIMP(statut='f',typ=fonction),
             FC_LLTZ         =SIMP(statut='f',typ=fonction),
             FC_TTLZ         =SIMP(statut='f',typ=fonction),
             FC_TTTZ         =SIMP(statut='f',typ=fonction),
             FC_LTLZ         =SIMP(statut='f',typ=fonction),
             FC_LTTZ         =SIMP(statut='f',typ=fonction),
             C_LZLZ          =SIMP(statut='f',typ=fonction),
             C_LZTZ          =SIMP(statut='f',typ=fonction),
             C_TZTZ          =SIMP(statut='f',typ=fonction),
             RHO             =SIMP(statut='f',typ='R'),
             ALPHA           =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP","INST") ),
           ),
           APPUI_ELAS      =FACT(statut='f',min=0,max=1,
             E_N             =SIMP(statut='o',typ='R'),
             E_TAN           =SIMP(statut='f',typ='R',defaut= 0.E+0),
           ),
           CABLE           =FACT(statut='f',min=0,max=1,
             E               =SIMP(statut='o',typ='R'),
             EC_SUR_E        =SIMP(statut='f',typ='R',defaut= 1.E-4 ),
             RHO             =SIMP(statut='f',typ='R'),
             ALPHA           =SIMP(statut='f',typ='R'),
             AMOR_ALPHA      =SIMP(statut='f',typ='R'),
             AMOR_BETA       =SIMP(statut='f',typ='R'),
           ),
#
# comportement m�canique non lin�aire
#
           TRACTION        =FACT(statut='f',min=0,max=1,
             SIGM            =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="EPSI",into=("EPSI",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
             VERI_P3         =SIMP(statut='c',typ='TXM',defaut="HYDR",into=("HYDR",) ),
             VERI_P4         =SIMP(statut='c',typ='TXM',defaut="SECH",into=("SECH",) ),
           ),
           ECRO_LINE       =FACT(statut='f',min=0,max=1,
             D_SIGM_EPSI     =SIMP(statut='o',typ='R'),
             SY              =SIMP(statut='o',typ='R'),
           ),
           ECRO_LINE_FO    =FACT(statut='f',min=0,max=1,
             D_SIGM_EPSI     =SIMP(statut='o',typ=fonction),
             SY              =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           PRAGER          =FACT(statut='f',min=0,max=1,
             C               =SIMP(statut='o',typ='R'),
           ),
           PRAGER_FO       =FACT(statut='f',min=0,max=1,
             C               =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           ECRO_FLEJOU     =FACT(statut='f',min=0,max=1,
             EP              =SIMP(statut='o',typ='R'),
             SY              =SIMP(statut='o',typ='R'),
             SU              =SIMP(statut='o',typ='R'),
             PUISS           =SIMP(statut='o',typ='R'),
           ),
           TAHERI          =FACT(statut='f',min=0,max=1,
             R_0             =SIMP(statut='o',typ='R'),
             ALPHA           =SIMP(statut='o',typ='R'),
             M               =SIMP(statut='o',typ='R'),
             A               =SIMP(statut='o',typ='R'),
             B               =SIMP(statut='o',typ='R'),
             C1              =SIMP(statut='o',typ='R'),
             C_INF           =SIMP(statut='o',typ='R'),
             S               =SIMP(statut='o',typ='R'),
           ),
           TAHERI_FO       =FACT(statut='f',min=0,max=1,
             R_0             =SIMP(statut='o',typ=fonction),
             ALPHA           =SIMP(statut='o',typ=fonction),
             M               =SIMP(statut='o',typ=fonction),
             A               =SIMP(statut='o',typ=fonction),
             B               =SIMP(statut='o',typ=fonction),
             C1              =SIMP(statut='o',typ=fonction),
             C_INF           =SIMP(statut='o',typ=fonction),
             S               =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           ROUSSELIER      =FACT(statut='f',min=0,max=1,
             D               =SIMP(statut='o',typ='R'),
             SIGM_1          =SIMP(statut='o',typ='R'),
             PORO_INIT       =SIMP(statut='o',typ='R'),
             PORO_CRIT       =SIMP(statut='f',typ='R',defaut= 1. ),
             PORO_ACCE       =SIMP(statut='f',typ='R',defaut= 1. ),
             PORO_LIMI       =SIMP(statut='f',typ='R',defaut= 0.999 ),
             D_SIGM_EPSI_NORM=SIMP(statut='f',typ='R',defaut= 1. ),
             AN              =SIMP(statut='f',typ='R',defaut= 0. ),
           ),
           ROUSSELIER_FO   =FACT(statut='f',min=0,max=1,
             D               =SIMP(statut='o',typ=fonction),
             SIGM_1          =SIMP(statut='o',typ=fonction),
             PORO_INIT       =SIMP(statut='o',typ=fonction),
             PORO_CRIT       =SIMP(statut='f',typ='R',defaut= 1. ),
             PORO_ACCE       =SIMP(statut='f',typ='R',defaut= 1. ),
             PORO_LIMI       =SIMP(statut='f',typ='R',defaut= 0.999 ),
             D_SIGM_EPSI_NORM=SIMP(statut='f',typ='R',defaut= 1. ),
             AN              =SIMP(statut='f',typ='R',defaut= 0. ),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           ROUSS_VISC      =FACT(statut='f',min=0,max=1,
             SIGM_0          =SIMP(statut='o',typ='R'),
             EPSI_0          =SIMP(statut='o',typ='R'),
             M               =SIMP(statut='o',typ='R'),
           ),
           CHABOCHE        =FACT(statut='f',min=0,max=1,
             R_I             =SIMP(statut='o',typ='R'),
             R_0             =SIMP(statut='o',typ='R'),
             B               =SIMP(statut='o',typ='R'),
             K               =SIMP(statut='o',typ='R'),
             W               =SIMP(statut='o',typ='R'),
             A1              =SIMP(statut='o',typ='R'),
             A2              =SIMP(statut='o',typ='R'),
             C1              =SIMP(statut='o',typ='R'),
             C2              =SIMP(statut='o',typ='R'),
           ),
           CIN1_CHAB  =FACT(statut='f',min=0,max=1,
             R_0             =SIMP(statut='o',typ='R'),
             R_I             =SIMP(statut='f',typ='R'),
             B               =SIMP(statut='f',typ='R',defaut= 0.0E+0),
             C_I             =SIMP(statut='o',typ='R'),
             K               =SIMP(statut='f',typ='R',defaut= 1.0E+0),
             W               =SIMP(statut='f',typ='R',defaut= 0.0E+0),
             G_0             =SIMP(statut='o',typ='R'),
             A_I             =SIMP(statut='f',typ='R',defaut= 1.0E+0),
           ),
           CIN1_CHAB_FO  =FACT(statut='f',min=0,max=1,
             R_0             =SIMP(statut='o',typ=fonction),
             R_I             =SIMP(statut='o',typ=fonction),
             B               =SIMP(statut='o',typ=fonction),
             C_I             =SIMP(statut='o',typ=fonction),
             K               =SIMP(statut='o',typ=fonction),
             W               =SIMP(statut='o',typ=fonction),
             G_0             =SIMP(statut='o',typ=fonction),
             A_I             =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",)),
           ),
           CIN2_CHAB  =FACT(statut='f',min=0,max=1,
             R_0             =SIMP(statut='o',typ='R'),
             R_I             =SIMP(statut='f',typ='R'),
             B               =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             C1_I            =SIMP(statut='o',typ='R'),
             C2_I            =SIMP(statut='o',typ='R'),
             K               =SIMP(statut='f',typ='R',defaut= 1.),
             W               =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             G1_0            =SIMP(statut='o',typ='R'),
             G2_0            =SIMP(statut='o',typ='R'),
             A_I             =SIMP(statut='f',typ='R',defaut= 1.E+0 ),
           ),
           CIN2_CHAB_FO  =FACT(statut='f',min=0,max=1,
             R_0             =SIMP(statut='o',typ=fonction),
             R_I             =SIMP(statut='o',typ=fonction),
             B               =SIMP(statut='o',typ=fonction),
             C1_I            =SIMP(statut='o',typ=fonction),
             C2_I            =SIMP(statut='o',typ=fonction),
             K               =SIMP(statut='o',typ=fonction),
             W               =SIMP(statut='o',typ=fonction),
             G1_0            =SIMP(statut='o',typ=fonction),
             G2_0            =SIMP(statut='o',typ=fonction),
             A_I             =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           VISCOCHAB       =FACT(statut='f',min=0,max=1,
             K_0             =SIMP(statut='o',typ='R'),
             A_K             =SIMP(statut='o',typ='R'),
             A_R             =SIMP(statut='o',typ='R'),
             K               =SIMP(statut='o',typ='R'),
             N               =SIMP(statut='o',typ='R'),
             ALP             =SIMP(statut='o',typ='R'),
             B               =SIMP(statut='o',typ='R'),
             M_R             =SIMP(statut='o',typ='R'),
             G_R             =SIMP(statut='o',typ='R'),
             MU              =SIMP(statut='o',typ='R'),
             Q_M             =SIMP(statut='o',typ='R'),
             Q_0             =SIMP(statut='o',typ='R'),
             QR_0            =SIMP(statut='o',typ='R'),
             ETA             =SIMP(statut='o',typ='R'),
             C1              =SIMP(statut='o',typ='R'),
             M_1             =SIMP(statut='o',typ='R'),
             D1              =SIMP(statut='o',typ='R'),
             G_X1            =SIMP(statut='o',typ='R'),
             G1_0            =SIMP(statut='o',typ='R'),
             C2              =SIMP(statut='o',typ='R'),
             M_2             =SIMP(statut='o',typ='R'),
             D2              =SIMP(statut='o',typ='R'),
             G_X2            =SIMP(statut='o',typ='R'),
             G2_0            =SIMP(statut='o',typ='R'),
             A_I             =SIMP(statut='o',typ='R'),
           ),
           VISCOCHAB_FO    =FACT(statut='f',min=0,max=1,
             K_0             =SIMP(statut='o',typ=fonction),
             A_K             =SIMP(statut='o',typ=fonction),
             A_R             =SIMP(statut='o',typ=fonction),
             K               =SIMP(statut='o',typ=fonction),
             N               =SIMP(statut='o',typ=fonction),
             ALP             =SIMP(statut='o',typ=fonction),
             B               =SIMP(statut='o',typ=fonction),
             M_R             =SIMP(statut='o',typ=fonction),
             G_R             =SIMP(statut='o',typ=fonction),
             MU              =SIMP(statut='o',typ=fonction),
             Q_M             =SIMP(statut='o',typ=fonction),
             Q_0             =SIMP(statut='o',typ=fonction),
             QR_0            =SIMP(statut='o',typ=fonction),
             ETA             =SIMP(statut='o',typ=fonction),
             C1              =SIMP(statut='o',typ=fonction),
             M_1             =SIMP(statut='o',typ=fonction),
             D1              =SIMP(statut='o',typ=fonction),
             G_X1            =SIMP(statut='o',typ=fonction),
             G1_0            =SIMP(statut='o',typ=fonction),
             C2              =SIMP(statut='o',typ=fonction),
             M_2             =SIMP(statut='o',typ=fonction),
             D2              =SIMP(statut='o',typ=fonction),
             G_X2            =SIMP(statut='o',typ=fonction),
             G2_0            =SIMP(statut='o',typ=fonction),
             A_I             =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           POLY_CFC        =FACT(statut='f',min=0,max=1,
             TEXTURE         =SIMP(statut='o',typ=(tabl_texture) ),
             DL              =SIMP(statut='f',typ='R'),
             DA              =SIMP(statut='f',typ='R'),
             N               =SIMP(statut='o',typ='R'),
             K               =SIMP(statut='o',typ='R'),
             TAU_0           =SIMP(statut='o',typ='R'),
             Q1              =SIMP(statut='o',typ='R'),
             B1              =SIMP(statut='o',typ='R'),
             HL              =SIMP(statut='o',typ='R'),
             Q2              =SIMP(statut='o',typ='R'),
             B2              =SIMP(statut='o',typ='R'),
             C1              =SIMP(statut='o',typ='R'),
             D1              =SIMP(statut='o',typ='R'),
             C2              =SIMP(statut='o',typ='R'),
           ),
           POLY_CFC_FO     =FACT(statut='f',min=0,max=1,
             TEXTURE         =SIMP(statut='o',typ=(tabl_texture) ),
             DL              =SIMP(statut='o',typ=fonction),
             DA              =SIMP(statut='o',typ=fonction),
             N               =SIMP(statut='o',typ=fonction),
             K               =SIMP(statut='o',typ=fonction),
             TAU_0           =SIMP(statut='o',typ=fonction),
             Q1              =SIMP(statut='o',typ=fonction),
             B1              =SIMP(statut='o',typ=fonction),
             HL              =SIMP(statut='o',typ=fonction),
             Q2              =SIMP(statut='o',typ=fonction),
             B2              =SIMP(statut='o',typ=fonction),
             C1              =SIMP(statut='o',typ=fonction),
             D1              =SIMP(statut='o',typ=fonction),
             C2              =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           NORTON_HOFF     =FACT(statut='f',min=0,max=1,
             SY              =SIMP(statut='o',typ='R'),
           ),
           LEMAITRE        =FACT(statut='f',min=0,max=1,
             N               =SIMP(statut='o',typ='R'),
             UN_SUR_K        =SIMP(statut='o',typ='R'),
             UN_SUR_M        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
           ZIRC_CYRA2      =FACT(statut='f',min=0,max=1,
             EPSI_FAB        =SIMP(statut='o',typ=fonction),
             TEMP_RECUIT     =SIMP(statut='o',typ=fonction),
             FLUX_PHI        =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="INST",into=("INST",) ),
           ),
           ZIRC_EPRI       =FACT(statut='f',min=0,max=1,
             FLUX_PHI        =SIMP(statut='o',typ='R'),
             R_P             =SIMP(statut='o',typ='R'),
             THETA_MAX       =SIMP(statut='o',typ='R'),
           ),
           LEMAITRE_FO     =FACT(statut='f',min=0,max=1,
             N               =SIMP(statut='o',typ=fonction),
             UN_SUR_K        =SIMP(statut='o',typ=fonction),
             UN_SUR_M        =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           GRAN_IRRA       =FACT(statut='f',min=0,max=1,
             A               =SIMP(statut='f',typ='R',defaut= 0.E+0),
             B               =SIMP(statut='f',typ='R',defaut= 0.E+0),
             S               =SIMP(statut='f',typ='R',defaut= 0.E+0),
           ),
           FLU_IRRA       =FACT(statut='f',min=0,max=1,
             QSR_K           =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             BETA            =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             PHI_ZERO        =SIMP(statut='f',typ='R',defaut= 1.E+20),
             L               =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
           OHNO            =FACT(statut='f',min=0,max=1,
             R_I             =SIMP(statut='o',typ='R'),
             R_0             =SIMP(statut='o',typ='R'),
             B               =SIMP(statut='o',typ='R'),
             PHI             =SIMP(statut='o',typ='R'),
             A1              =SIMP(statut='o',typ='R'),
             A2              =SIMP(statut='o',typ='R'),
             A3              =SIMP(statut='o',typ='R'),
             A4              =SIMP(statut='o',typ='R'),
             A5              =SIMP(statut='o',typ='R'),
             GAMMA1          =SIMP(statut='o',typ='R'),
             GAMMA2          =SIMP(statut='o',typ='R'),
             GAMMA3          =SIMP(statut='o',typ='R'),
             GAMMA4          =SIMP(statut='o',typ='R'),
             GAMMA5          =SIMP(statut='o',typ='R'),
             M1              =SIMP(statut='o',typ='R'),
             M2              =SIMP(statut='o',typ='R'),
             M3              =SIMP(statut='o',typ='R'),
             M4              =SIMP(statut='o',typ='R'),
             M5              =SIMP(statut='o',typ='R'),
                           ),
           OHNO_FO         =FACT(statut='f',min=0,max=1,
             R_I             =SIMP(statut='o',typ=fonction),
             R_0             =SIMP(statut='o',typ=fonction),
             B               =SIMP(statut='o',typ=fonction),
             PHI             =SIMP(statut='o',typ=fonction),
             A1              =SIMP(statut='o',typ=fonction),
             A2              =SIMP(statut='o',typ=fonction),
             A3              =SIMP(statut='o',typ=fonction),
             A4              =SIMP(statut='o',typ=fonction),
             A5              =SIMP(statut='o',typ=fonction),
             GAMMA1          =SIMP(statut='o',typ=fonction),
             GAMMA2          =SIMP(statut='o',typ=fonction),
             GAMMA3          =SIMP(statut='o',typ=fonction),
             GAMMA4          =SIMP(statut='o',typ=fonction),
             GAMMA5          =SIMP(statut='o',typ=fonction),
             M1              =SIMP(statut='o',typ=fonction),
             M2              =SIMP(statut='o',typ=fonction),
             M3              =SIMP(statut='o',typ=fonction),
             M4              =SIMP(statut='o',typ=fonction),
             M5              =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           LMARC           =FACT(statut='f',min=0,max=1,
             DE_0            =SIMP(statut='o',typ='R'),
             R_0             =SIMP(statut='o',typ='R'),
             N               =SIMP(statut='o',typ='R'),
             K               =SIMP(statut='o',typ='R'),
             Y_I             =SIMP(statut='o',typ='R'),
             Y_0             =SIMP(statut='o',typ='R'),
             B               =SIMP(statut='o',typ='R'),
             A_0             =SIMP(statut='o',typ='R'),
             RM              =SIMP(statut='o',typ='R'),
             M               =SIMP(statut='o',typ='R'),
             P               =SIMP(statut='o',typ='R'),
             P1              =SIMP(statut='o',typ='R'),
             P2              =SIMP(statut='o',typ='R'),
             M11             =SIMP(statut='o',typ='R'),
             M22             =SIMP(statut='o',typ='R'),
             M33             =SIMP(statut='o',typ='R'),
             M66             =SIMP(statut='o',typ='R'),
             N11             =SIMP(statut='o',typ='R'),
             N22             =SIMP(statut='o',typ='R'),
             N33             =SIMP(statut='o',typ='R'),
             N66             =SIMP(statut='o',typ='R'),
             Q11             =SIMP(statut='o',typ='R'),
             Q22             =SIMP(statut='o',typ='R'),
             Q33             =SIMP(statut='o',typ='R'),
             Q66             =SIMP(statut='o',typ='R'),
             R11             =SIMP(statut='o',typ='R'),
             R22             =SIMP(statut='o',typ='R'),
             R33             =SIMP(statut='o',typ='R'),
             R66             =SIMP(statut='o',typ='R'),
           ),
           LMARC_FO        =FACT(statut='f',min=0,max=1,
             DE_0            =SIMP(statut='o',typ=fonction),
             R_0             =SIMP(statut='o',typ=fonction),
             N               =SIMP(statut='o',typ=fonction),
             K               =SIMP(statut='o',typ=fonction),
             Y_I             =SIMP(statut='o',typ=fonction),
             Y_0             =SIMP(statut='o',typ=fonction),
             B               =SIMP(statut='o',typ=fonction),
             A_0             =SIMP(statut='o',typ=fonction),
             RM              =SIMP(statut='o',typ=fonction),
             M               =SIMP(statut='o',typ=fonction),
             P               =SIMP(statut='o',typ=fonction),
             P1              =SIMP(statut='o',typ=fonction),
             P2              =SIMP(statut='o',typ=fonction),
             M11             =SIMP(statut='o',typ=fonction),
             M22             =SIMP(statut='o',typ=fonction),
             M33             =SIMP(statut='o',typ=fonction),
             M66             =SIMP(statut='o',typ=fonction),
             N11             =SIMP(statut='o',typ=fonction),
             N22             =SIMP(statut='o',typ=fonction),
             N33             =SIMP(statut='o',typ=fonction),
             N66             =SIMP(statut='o',typ=fonction),
             Q11             =SIMP(statut='o',typ=fonction),
             Q22             =SIMP(statut='o',typ=fonction),
             Q33             =SIMP(statut='o',typ=fonction),
             Q66             =SIMP(statut='o',typ=fonction),
             R11             =SIMP(statut='o',typ=fonction),
             R22             =SIMP(statut='o',typ=fonction),
             R33             =SIMP(statut='o',typ=fonction),
             R66             =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           VMIS_POUTRE     =FACT(statut='f',min=0,max=1,
             NP              =SIMP(statut='o',typ='R'),
             MEY             =SIMP(statut='o',typ='R'),
             MPY             =SIMP(statut='o',typ='R'),
             CAY             =SIMP(statut='o',typ='R'),
             CBY             =SIMP(statut='o',typ='R'),
             MEZ             =SIMP(statut='o',typ='R'),
             MPZ             =SIMP(statut='o',typ='R'),
             CAZ             =SIMP(statut='o',typ='R'),
             CBZ             =SIMP(statut='o',typ='R'),
             MPX             =SIMP(statut='o',typ='R'),
           ),
           VMIS_POUTRE_FO  =FACT(statut='f',min=0,max=1,
             NP              =SIMP(statut='o',typ=fonction),
             MEY             =SIMP(statut='o',typ=fonction),
             MPY             =SIMP(statut='o',typ=fonction),
             CAY             =SIMP(statut='o',typ=fonction),
             CBY             =SIMP(statut='o',typ=fonction),
             MEZ             =SIMP(statut='o',typ=fonction),
             MPZ             =SIMP(statut='o',typ=fonction),
             CAZ             =SIMP(statut='o',typ=fonction),
             CBZ             =SIMP(statut='o',typ=fonction),
             MPX             =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           ARME            =FACT(statut='f',min=0,max=1,
             KYE             =SIMP(statut='o',typ='R'),
             DLE             =SIMP(statut='o',typ='R'),
             KYP             =SIMP(statut='o',typ='R'),
             DLP             =SIMP(statut='o',typ='R'),
             KYG             =SIMP(statut='o',typ='R'),
           ),
           ASSE_CORN       =FACT(statut='f',min=0,max=1,
             NU_1            =SIMP(statut='o',typ='R'),
             MU_1            =SIMP(statut='o',typ='R'),
             DXU_1           =SIMP(statut='o',typ='R'),
             DRYU_1          =SIMP(statut='o',typ='R'),
             C_1             =SIMP(statut='o',typ='R'),
             NU_2            =SIMP(statut='o',typ='R'),
             MU_2            =SIMP(statut='o',typ='R'),
             DXU_2           =SIMP(statut='o',typ='R'),
             DRYU_2          =SIMP(statut='o',typ='R'),
             C_2             =SIMP(statut='o',typ='R'),
             KY              =SIMP(statut='o',typ='R'),
             KZ              =SIMP(statut='o',typ='R'),
             KRX             =SIMP(statut='o',typ='R'),
             KRZ             =SIMP(statut='o',typ='R'),
           ),
           DIS_CONTACT     =FACT(statut='f',min=0,max=1,
             RIGI_NOR        =SIMP(statut='f',typ='R' ),
             DIST_1          =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             DIST_2          =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             RIGI_TAN        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             AMOR_NOR        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             AMOR_TAN        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             COULOMB         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             JEU             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             KT_ULTM         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             EFFO_N_INIT     =SIMP(statut='f',typ='R'),
             regles=(EXCLUS('RIGI_N_FO','RIGI_N_IRRA',),),
             RIGI_N_IRRA     =SIMP(statut='f',typ=fonction),
             RIGI_N_FO       =SIMP(statut='f',typ=fonction),
             RELA_MZ         =SIMP(statut='f',typ=fonction),
             C_PRAGER_MZ     =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="DRZ",into=("DRZ",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="INST",into=("INST",) ),
           ),
           NADAI_B         =FACT(statut='f',min=0,max=1,
             F_C             =SIMP(statut='o',typ='R'),
             F_T             =SIMP(statut='o',typ='R'),
             CRIT_E_C        =SIMP(statut='o',typ='R'),
             EPSP_P_C        =SIMP(statut='o',typ='R'),
             EPSP_R_C        =SIMP(statut='o',typ='R'),
             EPSI_R_T        =SIMP(statut='o',typ='R'),
             FAC_T_C         =SIMP(statut='o',typ='R'),
           ),
           BETON_DOUBLE_DP =FACT(statut='f',min=0,max=1,
             F_C             =SIMP(statut='o',typ=fonction),
             F_T             =SIMP(statut='o',typ=fonction),
             COEF_BIAX       =SIMP(statut='o',typ=fonction),
             ENER_COMP_RUPT  =SIMP(statut='o',typ=fonction),
             ENER_TRAC_RUPT  =SIMP(statut='o',typ=fonction),
             COEF_ELAS_COMP  =SIMP(statut='o',typ='R'),
             LONG_CARA       =SIMP(statut='f',typ='R'),
             ECRO_COMP_P_PIC =SIMP(statut='f',typ='TXM',defaut="LINEAIRE",into=("LINEAIRE","PARABOLE") ),
             ECRO_TRAC_P_PIC =SIMP(statut='f',typ='TXM',defaut="LINEAIRE",into=("LINEAIRE","EXPONENT") ),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP","INST",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="INST",into=("TEMP","INST",) ),
             VERI_P3         =SIMP(statut='c',typ='TXM',defaut="HYDR",into=("HYDR",) ),
             VERI_P4         =SIMP(statut='c',typ='TXM',defaut="SECH",into=("SECH",) ),
           ),
           LABORD_1D=FACT(statut='f',min=0 ,max=1,
             Y01             =SIMP(statut='o',typ='R'),
             Y02             =SIMP(statut='o',typ='R'),
             A1              =SIMP(statut='o',typ='R'),
             A2              =SIMP(statut='o',typ='R'),
             B1              =SIMP(statut='o',typ='R'),
             B2              =SIMP(statut='o',typ='R'),
             BETA1           =SIMP(statut='o',typ='R'),
             BETA2           =SIMP(statut='o',typ='R'),
             SIGF            =SIMP(statut='o',typ='R'),
           ),

           VENDOCHAB       =FACT(statut='f',min=0,max=1,
             S_VP            =SIMP(statut='o',typ='R'),
             SEDVP1          =SIMP(statut='o',typ='R'),
             SEDVP2          =SIMP(statut='o',typ='R'),
             N_VP            =SIMP(statut='o',typ='R'),
             M_VP            =SIMP(statut='o',typ='R'),
             K_VP            =SIMP(statut='o',typ='R'),
             R_D             =SIMP(statut='o',typ='R'),
             A_D             =SIMP(statut='o',typ='R'),
             K_D             =SIMP(statut='o',typ='R'),
           ),
           VENDOCHAB_FO    =FACT(statut='f',min=0,max=1,
             S_VP            =SIMP(statut='o',typ=fonction),
             SEDVP1          =SIMP(statut='o',typ=fonction),
             SEDVP2          =SIMP(statut='o',typ=fonction),
             N_VP            =SIMP(statut='o',typ=fonction),
             M_VP            =SIMP(statut='o',typ=fonction),
             K_VP            =SIMP(statut='o',typ=fonction),
             R_D             =SIMP(statut='o',typ=fonction),
             A_D             =SIMP(statut='o',typ=fonction),
             K_D             =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="X",into=("X",) ),
           ),
           PINTO_MENEGOTTO =FACT(statut='f',min=0,max=1,
             SY              =SIMP(statut='o',typ='R'),
             EPSI_ULTM       =SIMP(statut='o',typ='R'),
             SIGM_ULTM       =SIMP(statut='o',typ='R'),
             ELAN            =SIMP(statut='f',typ='R',defaut= 4. ),
             EPSP_HARD       =SIMP(statut='o',typ='R'),
             R_PM            =SIMP(statut='f',typ='R',defaut= 20. ),
             EP_SUR_E        =SIMP(statut='f',typ='R'),
             A1_PM           =SIMP(statut='f',typ='R',defaut= 18.5 ),
             A2_PM           =SIMP(statut='f',typ='R',defaut= 0.15 ),
             A6_PM           =SIMP(statut='f',typ='R',defaut= 620. ),
             C_PM            =SIMP(statut='f',typ='R',defaut= 0.5 ),
             A_PM            =SIMP(statut='f',typ='R',defaut= 6.0E-3 ),
           ),
           BPEL_BETON      =FACT(statut='f',min=0,max=1,
             PERT_FLUA       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             PERT_RETR       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
           BPEL_ACIER      =FACT(statut='f',min=0,max=1,
             RELAX_1000      =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             MU0_RELAX       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             SY              =SIMP(statut='o',typ='R'),
             FROT_COURB      =SIMP(statut='o',typ='R'),
             FROT_LINE       =SIMP(statut='o',typ='R'),
           ),
           CJS             =FACT(statut='f',min=0,max=1,
             regles=(ENSEMBLE('B_CJS','C_CJS','MU_CJS','PCO',),
                     ENSEMBLE('N_CJS','KP','RC',),
                     PRESENT_ABSENT('A_CJS','B_CJS',),
                     PRESENT_PRESENT('A_CJS','N_CJS',),
                     PRESENT_PRESENT('B_CJS','N_CJS', ),),
             BETA_CJS        =SIMP(statut='o',typ='R'),
             RM              =SIMP(statut='o',typ='R'),
             N_CJS           =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             KP              =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             RC              =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             A_CJS           =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             B_CJS           =SIMP(statut='f',typ='R',defaut= 1.0E+25 ),
             C_CJS           =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             GAMMA_CJS       =SIMP(statut='o',typ='R'),
             MU_CJS          =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             PCO             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             PA              =SIMP(statut='o',typ='R'),
             Q_INIT          =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
             R_INIT          =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
           ECRO_ASYM_LINE  =FACT(statut='f',min=0,max=1,
             DC_SIGM_EPSI    =SIMP(statut='o',typ='R'),
             SY_C            =SIMP(statut='o',typ='R'),
             DT_SIGM_EPSI    =SIMP(statut='o',typ='R'),
             SY_T            =SIMP(statut='o',typ='R'),
           ),
           GRANGER_FP      =FACT(statut='f',min=0,max=1,
             J1              =SIMP(statut='f',typ='R'),
             J2              =SIMP(statut='f',typ='R'),
             J3              =SIMP(statut='f',typ='R'),
             J4              =SIMP(statut='f',typ='R'),
             J5              =SIMP(statut='f',typ='R'),
             J6              =SIMP(statut='f',typ='R'),
             J7              =SIMP(statut='f',typ='R'),
             J8              =SIMP(statut='f',typ='R'),
             TAUX_1          =SIMP(statut='f',typ='R'),
             TAUX_2          =SIMP(statut='f',typ='R'),
             TAUX_3          =SIMP(statut='f',typ='R'),
             TAUX_4          =SIMP(statut='f',typ='R'),
             TAUX_5          =SIMP(statut='f',typ='R'),
             TAUX_6          =SIMP(statut='f',typ='R'),
             TAUX_7          =SIMP(statut='f',typ='R'),
             TAUX_8          =SIMP(statut='f',typ='R'),
             FONC_DESORP     =SIMP(statut='f',typ=fonction),
             QSR_K           =SIMP(statut='f',typ='R'),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="SECH",into=("SECH",) ),
           ),
           V_GRANGER_FP    =FACT(statut='f',min=0,max=1,
             QSR_VEIL        =SIMP(statut='f',typ='R'),
             FONC_V          =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="INST",into=("INST",) ),
           ),
#
# comportement thermique
#
           THER_NL         =FACT(statut='f',min=0,max=1,
             regles=(UN_PARMI('BETA','RHO_CP', ),),
             LAMBDA          =SIMP(statut='o',typ=fonction),
             BETA            =SIMP(statut='f',typ=fonction),
             RHO_CP          =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           THER_HYDR       =FACT(statut='f',min=0,max=1,
             LAMBDA          =SIMP(statut='o',typ=fonction),
             BETA            =SIMP(statut='f',typ=fonction),
             AFFINITE        =SIMP(statut='o',typ=fonction),
             CHALHYDR        =SIMP(statut='o',typ='R'),
             QSR_K           =SIMP(statut='o',typ='R'),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("HYDR",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="HYDR",into=("HYDR",) ),
           ),
           THER            =FACT(statut='f',min=0,max=1,
             LAMBDA          =SIMP(statut='o',typ='R'),
             RHO_CP          =SIMP(statut='f',typ='R'),
           ),
           THER_FO         =FACT(statut='f',min=0,max=1,
             LAMBDA          =SIMP(statut='o',typ=fonction),
             RHO_CP          =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="INST",into=("INST",) ),
           ),
           THER_ORTH       =FACT(statut='f',min=0,max=1,
             LAMBDA_L        =SIMP(statut='o',typ='R'),
             LAMBDA_T        =SIMP(statut='o',typ='R'),
             LAMBDA_N        =SIMP(statut='f',typ='R'),
             RHO_CP          =SIMP(statut='f',typ='R'),
           ),
           THER_COQUE      =FACT(statut='f',min=0,max=1,
             COND_LMM        =SIMP(statut='o',typ='R'),
             COND_TMM        =SIMP(statut='o',typ='R'),
             COND_LMP        =SIMP(statut='o',typ='R'),
             COND_TMP        =SIMP(statut='o',typ='R'),
             COND_LPP        =SIMP(statut='o',typ='R'),
             COND_TPP        =SIMP(statut='o',typ='R'),
             COND_LSI        =SIMP(statut='o',typ='R'),
             COND_TSI        =SIMP(statut='o',typ='R'),
             COND_NMM        =SIMP(statut='o',typ='R'),
             COND_NMP        =SIMP(statut='o',typ='R'),
             COND_NPP        =SIMP(statut='o',typ='R'),
             COND_NSI        =SIMP(statut='o',typ='R'),
             CMAS_MM         =SIMP(statut='f',typ='R'),
             CMAS_MP         =SIMP(statut='f',typ='R'),
             CMAS_PP         =SIMP(statut='f',typ='R'),
             CMAS_SI         =SIMP(statut='f',typ='R'),
           ),
           THER_COQUE_FO   =FACT(statut='f',min=0,max=1,
             COND_LMM        =SIMP(statut='o',typ=fonction),
             COND_TMM        =SIMP(statut='o',typ=fonction),
             COND_LMP        =SIMP(statut='o',typ=fonction),
             COND_TMP        =SIMP(statut='o',typ=fonction),
             COND_LPP        =SIMP(statut='o',typ=fonction),
             COND_TPP        =SIMP(statut='o',typ=fonction),
             COND_LSI        =SIMP(statut='o',typ=fonction),
             COND_TSI        =SIMP(statut='o',typ=fonction),
             COND_NMM        =SIMP(statut='o',typ=fonction),
             COND_NMP        =SIMP(statut='o',typ=fonction),
             COND_NPP        =SIMP(statut='o',typ=fonction),
             COND_NSI        =SIMP(statut='o',typ=fonction),
             CMAS_MM         =SIMP(statut='f',typ=fonction),
             CMAS_MP         =SIMP(statut='f',typ=fonction),
             CMAS_PP         =SIMP(statut='f',typ=fonction),
             CMAS_SI         =SIMP(statut='f',typ=fonction),
           ),
           SECH_GRANGER    =FACT(statut='f',min=0,max=1,
             A               =SIMP(statut='o',typ='R'),
             B               =SIMP(statut='o',typ='R'),
             QSR_K           =SIMP(statut='o',typ='R'),
             TEMP_0_C        =SIMP(statut='o',typ='R'),
           ),
           SECH_MENSI      =FACT(statut='f',min=0,max=1,
             A               =SIMP(statut='o',typ='R'),
             B               =SIMP(statut='o',typ='R'),
           ),
           SECH_BAZANT     =FACT(statut='f',min=0,max=1,
             D1              =SIMP(statut='o',typ='R'),
             ALPHA_BAZANT    =SIMP(statut='o',typ='R'),
             N               =SIMP(statut='o',typ='R'),
             FONC_DESORP     =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           SECH_NAPPE      =FACT(statut='f',min=0,max=1,
             FONCTION        =SIMP(statut='o',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="TSEC",into=("TSEC",) ),
           ),
#
# comportement m�tallurgique
#
           META_ACIER      =FACT(statut='f',min=0,max=1,
             TRC             =SIMP(statut='o',typ=(tabl_trc) ),
             AR3             =SIMP(statut='o',typ='R'),
             ALPHA           =SIMP(statut='o',typ='R'),
             MS0             =SIMP(statut='o',typ='R'),
             AC1             =SIMP(statut='o',typ='R'),
             AC3             =SIMP(statut='o',typ='R'),
             TAUX_1          =SIMP(statut='o',typ='R'),
             TAUX_3          =SIMP(statut='o',typ='R'),
             LAMBDA0         =SIMP(statut='f',typ='R'),
             QSR_K           =SIMP(statut='f',typ='R'),
             D10             =SIMP(statut='f',typ='R'),
             WSR_K           =SIMP(statut='f',typ='R'),
           ),
           META_ZIRC       =FACT(statut='f',min=0,max=1,
             TDEQ            =SIMP(statut='o',typ='R'),
             N               =SIMP(statut='o',typ='R'),
             K               =SIMP(statut='o',typ='R'),
             TDC             =SIMP(statut='o',typ='R'),
             AC              =SIMP(statut='o',typ='R'),
             M               =SIMP(statut='o',typ='R'),
             QSR_K           =SIMP(statut='f',typ='R'),
             TDR             =SIMP(statut='o',typ='R'),
             AR              =SIMP(statut='o',typ='R'),
             BR              =SIMP(statut='o',typ='R'),
           ),
           DURT_META       =FACT(statut='f',min=0,max=1,
             F1_DURT         =SIMP(statut='o',typ='R'),
             F2_DURT         =SIMP(statut='o',typ='R'),
             F3_DURT         =SIMP(statut='o',typ='R'),
             F4_DURT         =SIMP(statut='o',typ='R'),
             C_DURT          =SIMP(statut='o',typ='R'),
           ),
           ELAS_META       =FACT(statut='f',min=0,max=1,
             E               =SIMP(statut='o',typ='R'),
             NU              =SIMP(statut='o',typ='R'),
             F_ALPHA         =SIMP(statut='o',typ='R'),
             C_ALPHA         =SIMP(statut='o',typ='R'),
             PHASE_REFE      =SIMP(statut='o',typ='TXM',into=("CHAUD","FROID")),
             EPSF_EPSC_TREF  =SIMP(statut='o',typ='R'),
             TEMP_DEF_ALPHA  =SIMP(statut='f',typ='R'),
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E+0),
             F1_SY           =SIMP(statut='f',typ='R'),
             F2_SY           =SIMP(statut='f',typ='R'),
             F3_SY           =SIMP(statut='f',typ='R'),
             F4_SY           =SIMP(statut='f',typ='R'),
             C_SY            =SIMP(statut='f',typ='R'),
             SY_MELANGE      =SIMP(statut='f',typ=fonction),
             F1_S_VP         =SIMP(statut='f',typ='R'),
             F2_S_VP         =SIMP(statut='f',typ='R'),
             F3_S_VP         =SIMP(statut='f',typ='R'),
             F4_S_VP         =SIMP(statut='f',typ='R'),
             C_S_VP          =SIMP(statut='f',typ='R' ),
             S_VP_MELANGE    =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="META",into=("META",)),
           ),
           ELAS_META_FO    =FACT(statut='f',min=0,max=1,
             E               =SIMP(statut='o',typ=fonction),
             NU              =SIMP(statut='o',typ=fonction),
             F_ALPHA         =SIMP(statut='o',typ=fonction),
             C_ALPHA         =SIMP(statut='o',typ=fonction),
             PHASE_REFE      =SIMP(statut='o',typ='TXM',into=("CHAUD","FROID")),
             EPSF_EPSC_TREF  =SIMP(statut='o',typ='R'),
             TEMP_DEF_ALPHA  =SIMP(statut='f',typ='R'),
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E+0),
             F1_SY           =SIMP(statut='f',typ=fonction),
             F2_SY           =SIMP(statut='f',typ=fonction),
             F3_SY           =SIMP(statut='f',typ=fonction),
             F4_SY           =SIMP(statut='f',typ=fonction),
             C_SY            =SIMP(statut='f',typ=fonction),
             SY_MELANGE      =SIMP(statut='f',typ=fonction),
             F1_S_VP         =SIMP(statut='f',typ=fonction),
             F2_S_VP         =SIMP(statut='f',typ=fonction),
             F3_S_VP         =SIMP(statut='f',typ=fonction),
             F4_S_VP         =SIMP(statut='f',typ=fonction),
             C_S_VP          =SIMP(statut='f',typ=fonction),
             S_VP_MELANGE    =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",)),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="META",into=("META",)),
           ),
           META_ECRO_LINE  =FACT(statut='f',min=0,max=1,
             F1_D_SIGM_EPSI  =SIMP(statut='f',typ=fonction),
             F2_D_SIGM_EPSI  =SIMP(statut='f',typ=fonction),
             F3_D_SIGM_EPSI  =SIMP(statut='f',typ=fonction),
             F4_D_SIGM_EPSI  =SIMP(statut='f',typ=fonction),
             C_D_SIGM_EPSI   =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",)),
           ),
           META_TRACTION   =FACT(statut='f',min=0,max=1,
             SIGM_F1         =SIMP(statut='f',typ=fonction),
             SIGM_F2         =SIMP(statut='f',typ=fonction),
             SIGM_F3         =SIMP(statut='f',typ=fonction),
             SIGM_F4         =SIMP(statut='f',typ=fonction),
             SIGM_C          =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="EPSI",into=("EPSI",)),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",)),
           ),
           META_VISC_FO    =FACT(statut='f',min=0,max=1,
             F1_ETA          =SIMP(statut='f',typ=fonction),
             F1_N            =SIMP(statut='f',typ=fonction),
             F1_C            =SIMP(statut='f',typ=fonction),
             F1_M            =SIMP(statut='f',typ=fonction),
             F2_ETA          =SIMP(statut='f',typ=fonction),
             F2_N            =SIMP(statut='f',typ=fonction),
             F2_C            =SIMP(statut='f',typ=fonction),
             F2_M            =SIMP(statut='f',typ=fonction),
             F3_ETA          =SIMP(statut='f',typ=fonction),
             F3_N            =SIMP(statut='f',typ=fonction),
             F3_C            =SIMP(statut='f',typ=fonction),
             F3_M            =SIMP(statut='f',typ=fonction),
             F4_ETA          =SIMP(statut='f',typ=fonction),
             F4_N            =SIMP(statut='f',typ=fonction),
             F4_C            =SIMP(statut='f',typ=fonction),
             F4_M            =SIMP(statut='f',typ=fonction),
             C_ETA           =SIMP(statut='f',typ=fonction),
             C_N             =SIMP(statut='f',typ=fonction),
             C_C             =SIMP(statut='f',typ=fonction),
             C_M             =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           META_PT         =FACT(statut='f',min=0,max=1,
             F1_K            =SIMP(statut='f',typ='R'),
             F2_K            =SIMP(statut='f',typ='R'),
             F3_K            =SIMP(statut='f',typ='R'),
             F4_K            =SIMP(statut='f',typ='R'),
             F1_D_F_META     =SIMP(statut='f',typ=fonction),
             F2_D_F_META     =SIMP(statut='f',typ=fonction),
             F3_D_F_META     =SIMP(statut='f',typ=fonction),
             F4_D_F_META     =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="META",into=("META",) ),
           ),
           META_RE         =FACT(statut='f',min=0,max=1,
             C_F1_THETA      =SIMP(statut='f',typ='R'),
             C_F2_THETA      =SIMP(statut='f',typ='R'),
             C_F3_THETA      =SIMP(statut='f',typ='R'),
             C_F4_THETA      =SIMP(statut='f',typ='R'),
             F1_C_THETA      =SIMP(statut='f',typ='R'),
             F2_C_THETA      =SIMP(statut='f',typ='R'),
             F3_C_THETA      =SIMP(statut='f',typ='R'),
             F4_C_THETA      =SIMP(statut='f',typ='R'),
           ),
#
# comportement fluide
#
           FLUIDE          =FACT(statut='f',min=0,max=1,
             regles=(EXCLUS('CELE_C','CELE_R'),),
             RHO             =SIMP(statut='o',typ='R'),
             CELE_C          =SIMP(statut='f',typ='C'),
             CELE_R          =SIMP(statut='f',typ='R'),
           ),
           PORO_JOINT      =FACT(statut='f',min=0,max=1,
             RHO_FLUI        =SIMP(statut='o',typ='R'),
             ENTRO_FLUI      =SIMP(statut='o',typ='R'),
             BIOT_M          =SIMP(statut='o',typ='R'),
             C_0             =SIMP(statut='o',typ='R'),
             T_R             =SIMP(statut='o',typ='R'),
             ALPHA_M         =SIMP(statut='o',typ='R'),
             LAMBDA_T        =SIMP(statut='o',typ='R'),
             LAMBDA_H        =SIMP(statut='o',typ='R'),
             SOURCE_INIT     =SIMP(statut='o',typ='R'),
             OMEGA_0         =SIMP(statut='o',typ='R'),
           ),
           THM_LIQU        =FACT(statut='f',min=0,max=1,
             RHO             =SIMP(statut='o',typ='R'),
             UN_SUR_K        =SIMP(statut='f',typ='R'),
             ALPHA           =SIMP(statut='f',typ='R'),
             CP              =SIMP(statut='f',typ='R'),
             VISC            =SIMP(statut='f',typ=fonction),
             D_VISC_TEMP     =SIMP(statut='f',typ=fonction),
             LAMBDA          =SIMP(statut='f',typ=fonction),
             D_LAMBDA_TEMP   =SIMP(statut='f',typ=fonction),
             COEF_HENRY      =SIMP(statut='f',typ='R'),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",)),
           ),
           THM_GAZ         =FACT(statut='f',min=0,max=1,
             MASS_MOL        =SIMP(statut='f',typ='R'),
             CP              =SIMP(statut='f',typ='R'),
             VISC            =SIMP(statut='f',typ=fonction),
             D_VISC_TEMP     =SIMP(statut='f',typ=fonction),
             LAMBDA          =SIMP(statut='f',typ=fonction),
             D_LAMBDA_TEMP   =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",)),
           ),
           THM_VAPE_GAZ    =FACT(statut='f',min=0,max=1,
             MASS_MOL        =SIMP(statut='f',typ='R'),
             CP              =SIMP(statut='f',typ='R'),
             VISC            =SIMP(statut='f',typ=fonction),
             D_VISC_TEMP     =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",)),
           ),
           THM_INIT        =FACT(statut='f',min=0,max=1,
             TEMP            =SIMP(statut='o',typ='R'),
             PRE1            =SIMP(statut='o',typ='R'),
             PRE2            =SIMP(statut='o',typ='R'),
             PORO            =SIMP(statut='o',typ='R'),
             PRES_VAPE       =SIMP(statut='o',typ='R'),
             DEGR_SATU       =SIMP(statut='f',typ='R'),
             PRES_ATMO       =SIMP(statut='f',typ='R'),
           ),
           THM_DIFFU       =FACT(statut='f',min=0,max=1,
             R_GAZ           =SIMP(statut='o',typ='R'),
             RHO             =SIMP(statut='f',typ='R'),
             CP              =SIMP(statut='f',typ='R'),
             BIOT_COEF       =SIMP(statut='f',typ='R'),
             SATU_PRES       =SIMP(statut='f',typ=fonction),
             D_SATU_PRES     =SIMP(statut='f',typ=fonction),
             PESA_X          =SIMP(statut='f',typ='R'),
             PESA_Y          =SIMP(statut='f',typ='R'),
             PESA_Z          =SIMP(statut='f',typ='R'),
             PERM_IN         =SIMP(statut='f',typ=fonction),
             PERM_LIQU       =SIMP(statut='f',typ=fonction),
             D_PERM_LIQU_SATU=SIMP(statut='f',typ=fonction),
             PERM_GAZ        =SIMP(statut='f',typ=fonction),
             D_PERM_SATU_GAZ =SIMP(statut='f',typ=fonction),
             D_PERM_PRES_GAZ =SIMP(statut='f',typ=fonction),
             FICK            =SIMP(statut='f',typ=fonction),
             D_FICK_TEMP     =SIMP(statut='f',typ=fonction),
             D_FICK_GAZ_PRES =SIMP(statut='f',typ=fonction),
             LAMBDA          =SIMP(statut='f',typ=fonction),
             D_LAMBDA_TEMP   =SIMP(statut='f',typ=fonction),
             SIGMA_T         =SIMP(statut='f',typ=fonction),
             D_SIGMA_T       =SIMP(statut='f',typ=fonction),
             PERM_G_INTR     =SIMP(statut='f',typ=fonction),
             CHAL_VAPO       =SIMP(statut='f',typ=fonction),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="SAT",into=("SAT",) ),
             VERI_P3         =SIMP(statut='c',typ='TXM',defaut="PORO",into=("PORO",) ),
             VERI_P4         =SIMP(statut='c',typ='TXM',defaut="PGAZ",into=("PGAZ",) ),
             VERI_P5         =SIMP(statut='c',typ='TXM',defaut="PGAP",into=("PGAP",) ),
           ),
#
# courbes et coefficients associ�s � la fatigue et au dommage
#
           FATIGUE         =FACT(statut='f',min=0,max=1,
             regles=(PRESENT_ABSENT('WOHLER','A_BASQUIN','BETA_BASQUIN'),
                     PRESENT_ABSENT('WOHLER','A0','A1','A2','A3','SL'),
                     PRESENT_ABSENT('A_BASQUIN','A0','A1','A2','A3','SL'),
                     ENSEMBLE('A_BASQUIN','BETA_BASQUIN'),
                     ENSEMBLE('A0','A1','A2','A3','SL'),
                     PRESENT_PRESENT('A0','E_REFE'),
                     ENSEMBLE('D0','TAU0'),),
             WOHLER          =SIMP(statut='f',typ=fonction),
             A_BASQUIN       =SIMP(statut='f',typ='R'),
             BETA_BASQUIN    =SIMP(statut='f',typ='R'),
             A0              =SIMP(statut='f',typ='R'),
             A1              =SIMP(statut='f',typ='R'),
             A2              =SIMP(statut='f',typ='R'),
             A3              =SIMP(statut='f',typ='R'),
             SL              =SIMP(statut='f',typ='R'),
             MANSON_COFFIN   =SIMP(statut='f',typ=fonction),
             E_REFE          =SIMP(statut='f',typ='R'),
             D0              =SIMP(statut='f',typ='R'),
             TAU0            =SIMP(statut='f',typ='R'),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="SIGM",into=("SIGM",) ),
             VERI_P2         =SIMP(statut='c',typ='TXM',defaut="EPSI",into=("EPSI",) ),
           ),
           DOMMA_LEMAITRE  =FACT(statut='f',min=0,max=1,
             S               =SIMP(statut='o',typ=fonction),
             EPSP_SEUIL      =SIMP(statut='o',typ='R'),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
#
# autres comportements ...
#
           WEIBULL         =FACT(statut='f',min=0,max=1,
             M               =SIMP(statut='o',typ='R'),
             VOLU_REFE       =SIMP(statut='o',typ='R'),
             SIGM_REFE       =SIMP(statut='o',typ='R'),
             SEUIL_EPSP_CUMU =SIMP(statut='f',typ='R',defaut= 1.0E-6),
           ),
           WEIBULL_FO      =FACT(statut='f',min=0,max=1,
             M               =SIMP(statut='o',typ='R'),
             VOLU_REFE       =SIMP(statut='o',typ='R'),
             SIGM_CNV        =SIMP(statut='o',typ='R'),
             SIGM_REFE       =SIMP(statut='o',typ=fonction),
             SEUIL_EPSP_CUMU =SIMP(statut='f',typ='R',defaut= 1.0E-6),
             VERI_P1         =SIMP(statut='c',typ='TXM',defaut="TEMP",into=("TEMP",) ),
           ),
           CONTACT         =FACT(statut='f',min=0,max=1,
             E_N             =SIMP(statut='o',typ='R'),
             E_T             =SIMP(statut='f',typ='R',defaut= 0.E+0),
             COULOMB         =SIMP(statut='f',typ='R',defaut= 0.E+0),
           ),
           NON_LOCAL       =FACT(statut='f',min=0,max=1,
             LONG_CARA       =SIMP(statut='o',typ='R'),
             COEF_RIGI_MINI  =SIMP(statut='f',typ='R'),
           ),
           RUPT_FRAG       =FACT(statut='f',min=0,max=1,
             GC              =SIMP(statut='o',typ='R'),
           ),
           RCCM            =FACT(statut='f',min=0,max=1,
             SY_02           =SIMP(statut='f',typ='R'),
             SM              =SIMP(statut='f',typ='R'),
             SU              =SIMP(statut='f',typ='R'),
             SC              =SIMP(statut='f',typ='R'),
             SH              =SIMP(statut='f',typ='R'),
             N_KE            =SIMP(statut='f',typ='R'),
             M_KE            =SIMP(statut='f',typ='R'),
           ),
           RCCM_FO         =FACT(statut='f',min=0,max=1,
             SY_02           =SIMP(statut='f',typ=fonction),
             SM              =SIMP(statut='f',typ=fonction),
             SU              =SIMP(statut='f',typ=fonction),
             S               =SIMP(statut='f',typ=fonction),
             N_KE            =SIMP(statut='f',typ=fonction),
             M_KE            =SIMP(statut='f',typ=fonction),
           ),
           INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_MODELE_GENE=OPER(nom="DEFI_MODELE_GENE",op= 126,sd_prod=modele_gene,
                      docu="U4.65.02-d",reentrant='n',
         SOUS_STRUC      =FACT(statut='o',min=01,max='**',
           NOM             =SIMP(statut='o',typ='TXM' ),
           MACR_ELEM_DYNA  =SIMP(statut='o',typ=macr_elem_dyna ),
           ANGL_NAUT       =SIMP(statut='f',typ='R',max=03),
           TRANS           =SIMP(statut='f',typ='R',max=03),
         ),
         LIAISON         =FACT(statut='o',min=01,max='**',
           SOUS_STRUC_1    =SIMP(statut='o',typ='TXM' ),
           INTERFACE_1     =SIMP(statut='o',typ='TXM' ),
           SOUS_STRUC_2    =SIMP(statut='o',typ='TXM' ),
           INTERFACE_2     =SIMP(statut='o',typ='TXM' ),
         ),
         VERIF           =FACT(statut='f',min=01,max='**',
#  dans la doc U stop_erreur est obligatoire         
           STOP_ERREUR     =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
         ),
)  ;
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_NAPPE=OPER(nom="DEFI_NAPPE",op=   4,sd_prod=fonction,
                fr="D�finition des valeurs d une fonction de deux variables r�elles",
                docu="U4.31.03-f1",reentrant='n',
         regles=(UN_PARMI('FONCTION','DEFI_FONCTION'),
                 EXCLUS('FONCTION','NOM_PARA_FONC',),
                 ENSEMBLE('NOM_PARA_FONC','DEFI_FONCTION'),),
         NOM_PARA        =SIMP(statut='o',typ='TXM',into=("TEMP","INST","X","Y","Z","FREQ","PULS",
                                                          "AMOR","EPAIS","TSEC","HYDR","SECH") ),
         NOM_RESU        =SIMP(statut='f',typ='TXM',defaut="TOUTRESU"),       
         PARA            =SIMP(statut='o',typ='R',max='**'),
         FONCTION        =SIMP(statut='f',typ=fonction,max='**' ),
         NOM_PARA_FONC   =SIMP(statut='f',typ='TXM',into=("TEMP","INST","X","Y","Z","EPSI","FREQ",
                                                          "PULS","AMOR","EPAIS") ),
         DEFI_FONCTION   =FACT(statut='f',max='**',
           VALE            =SIMP(statut='o',typ='R',max='**'),
           INTERPOL        =SIMP(statut='f',typ='TXM',max=2,defaut="LIN",into=("NON","LIN","LOG") ),
           PROL_DROITE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
           PROL_GAUCHE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
         ),
         INTERPOL        =SIMP(statut='f',typ='TXM',max=2,defaut="LIN",into=("NON","LIN","LOG") ),
         PROL_DROITE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
         PROL_GAUCHE     =SIMP(statut='f',typ='TXM',defaut="EXCLU",into=("CONSTANT","LINEAIRE","EXCLU") ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
         VERIF           =SIMP(statut='f',typ='TXM',into=("CROISSANT",) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_OBSTACLE=OPER(nom="DEFI_OBSTACLE",op=  73,sd_prod=obstacle
                    ,fr="D�finition d un obstacle plan perpendiculaire � une structure filaire",
                     docu="U4.44.21-e",reentrant='n',
         TYPE            =SIMP(statut='o',typ='TXM',defaut="CERCLE",
                             into=("CERCLE","PLAN_Y","PLAN_Z","DISCRET",
                             "BI_CERCLE","BI_PLAN_Y","BI_PLAN_Z","BI_CERC_INT",
                             "CRAYON_900","CRAYON_1300","GUID_A_CARTE_900",
                             "GUID_B_CARTE_900","GUID_C_CARTE_900",
                             "GUID_D_CARTE_900","GUID_E_CARTE_900",
                             "GUID_F_CARTE_900","GUID_A_CARTE_1300",
                             "GUID_B_CARTE_1300","GUID_C_CARTE_1300",
                             "GUID_D_CARTE_1300","GUID_E_CARTE_1300",
                             "GUID_F_CARTE_1300","GUID_A_CARSP_900",
                             "GUID_B_CARSP_900","GUID_C_CARSP_900",
                             "GUID_D_CARSP_900","GUID_E_CARSP_900",
                             "GUID_F_CARSP_900","GUID_A_CARSP_1300",
                             "GUID_B_CARSP_1300","GUID_C_CARSP_1300",
                             "GUID_D_CARSP_1300","GUID_E_CARSP_1300",
                             "GUID_F_CARSP_1300","GUID_A_GCONT_900",
                             "GUID_B_GCONT_900","GUID_C_GCONT_900",
                             "GUID_D_GCONT_900","GUID_E_GCONT_900",
                             "GUID_F_GCONT_900","GUID_A_GCONT_1300",
                             "GUID_B_GCONT_1300","GUID_C_GCONT_1300",
                             "GUID_D_GCONT_1300","GUID_E_GCONT_1300",
                             "GUID_F_GCONT_1300","GUID_A_GCOMB_900",
                             "GUID_B_GCOMB_900","GUID_C_GCOMB_900",
                             "GUID_D_GCOMB_900","GUID_E_GCOMB_900",
                             "GUID_F_GCOMB_900","GUID_A_GCOMB_1300",
                             "GUID_B_GCOMB_1300","GUID_C_GCOMB_1300",
                             "GUID_D_GCOMB_1300","GUID_E_GCOMB_1300",
                             "GUID_F_GCOMB_1300",) ),
         VALE            =SIMP(statut='f',typ='R',max='**'),
         VERIF           =SIMP(statut='f',typ='TXM',defaut="FERME"),
)  ;
#& MODIF COMMANDE  DATE 10/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE GNICOLAS G.NICOLAS
DEFI_PARA_SENSI=OPER(nom="DEFI_PARA_SENSI",op=   2,sd_prod=para_sensi,
                    fr="D�finition d'un param�tre de sensibilit�",
                    ang="Definition of a sensitive parameter",
                    docu="U4.31.xx-a",reentrant='n',
         NOM_RESU        =SIMP(statut='c',typ='TXM',into=("TOUTRESU",),defaut="TOUTRESU",
                               fr="Nom du concept cr��",
                               ang="Name of the concept"),
         VALE            =SIMP(statut='o',typ='R',max=01,
                               fr="Valeur du parametre",
                               ang="Value of the parameter"),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 07/03/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_SPEC_TURB=OPER(nom="DEFI_SPEC_TURB",op= 145,sd_prod=spectre,
                    fr="D�finition d'un spectre d'excitation turbulente",
                    docu="U4.44.31-c",reentrant='n',
         regles=(UN_PARMI('SPEC_LONG_COR_1','SPEC_LONG_COR_2','SPEC_LONG_COR_3',
                          'SPEC_LONG_COR_4','SPEC_CORR_CONV_1','SPEC_CORR_CONV_2',
                          'SPEC_FONC_FORME','SPEC_EXCI_POINT'),),
         SPEC_LONG_COR_1 =FACT(statut='f',min=00,max=01,
           LONG_COR        =SIMP(statut='o',typ='R' ),
           PROF_VITE_FLUI  =SIMP(statut='o',typ=fonction ),
           VISC_CINE       =SIMP(statut='o',typ='R' ),
         ),
         SPEC_LONG_COR_2 =FACT(statut='f',min=00,max=01,
           regles=(ENSEMBLE('FREQ_COUP','PHI0','BETA' ),),
           LONG_COR        =SIMP(statut='o',typ='R' ),
           PROF_VITE_FLUI  =SIMP(statut='o',typ=fonction ),
           FREQ_COUP       =SIMP(statut='f',typ='R',defaut= 0.1 ),
           PHI0            =SIMP(statut='f',typ='R',defaut= 1.5E-3 ),
           BETA            =SIMP(statut='f',typ='R',defaut= 2.7 ),
         ),
         SPEC_LONG_COR_3 =FACT(statut='f',min=00,max=01,
           regles=(ENSEMBLE('PHI0_1','BETA_1','PHI0_2','BETA_2','FREQ_COUP'),),
           LONG_COR        =SIMP(statut='o',typ='R' ),
           PROF_VITE_FLUI  =SIMP(statut='o',typ=fonction ),
           FREQ_COUP       =SIMP(statut='f',typ='R',defaut= 0.2 ),
           PHI0_1          =SIMP(statut='f',typ='R',defaut= 5.E-3 ),
           BETA_1          =SIMP(statut='f',typ='R',defaut= 0.5 ),
           PHI0_2          =SIMP(statut='f',typ='R',defaut= 4.E-5 ),
           BETA_2          =SIMP(statut='f',typ='R',defaut= 3.5 ),
         ),
         SPEC_LONG_COR_4 =FACT(statut='f',min=00,max=01,
           regles=(ENSEMBLE('BETA','GAMMA'),),
           LONG_COR        =SIMP(statut='o',typ='R' ),
           PROF_VITE_FLUI  =SIMP(statut='o',typ=fonction ),
           TAUX_VIDE       =SIMP(statut='o',typ='R' ),
           BETA            =SIMP(statut='f',typ='R',defaut= 2. ),
           GAMMA           =SIMP(statut='f',typ='R',defaut= 4. ),
         ),
         SPEC_CORR_CONV_1=FACT(statut='f',min=00,max=01,
           LONG_COR_1      =SIMP(statut='o',typ='R' ),
           LONG_COR_2      =SIMP(statut='f',typ='R' ),
           VITE_FLUI       =SIMP(statut='o',typ='R' ),
           RHO_FLUI        =SIMP(statut='o',typ='R' ),
           FREQ_COUP       =SIMP(statut='f',typ='R' ),
           K               =SIMP(statut='f',typ='R',defaut= 5.8E-3 ),
           D_FLUI          =SIMP(statut='o',typ='R' ),
           COEF_VITE_FLUI_A=SIMP(statut='f',typ='R' ),
           COEF_VITE_FLUI_O=SIMP(statut='f',typ='R' ),
           METHODE         =SIMP(statut='f',typ='TXM',defaut="GENERALE",
                                 into=("AU_YANG","GENERALE","CORCOS") ),
         ),
         SPEC_CORR_CONV_2=FACT(statut='f',min=00,max=01,
           FONCTION        =SIMP(statut='o',typ=fonction ),
           VITE_FLUI       =SIMP(statut='o',typ='R' ),
           FREQ_COUP       =SIMP(statut='f',typ='R' ),
           METHODE         =SIMP(statut='f',typ='TXM',defaut="GENERALE",
                                 into=("AU_YANG","GENERALE","CORCOS",) ),
           COEF_VITE_FLUI_A=SIMP(statut='f',typ='R' ),
           COEF_VITE_FLUI_O=SIMP(statut='f',typ='R' ),
         ),
         SPEC_FONC_FORME =FACT(statut='f',min=00,max=01,
           regles=(UN_PARMI('INTE_SPEC','GRAPPE_1'),
                   ENSEMBLE('INTE_SPEC','FONCTION'),),
           INTE_SPEC       =SIMP(statut='f',typ=tabl_intsp ),
           FONCTION        =SIMP(statut='f',typ=fonction,max='**'),
           GRAPPE_1        =SIMP(statut='f',typ='TXM',into=("DEBIT_180","DEBIT_300",) ),
           NOEUD           =SIMP(statut='o',typ=no),
           CARA_ELEM       =SIMP(statut='o',typ=cara_elem ),
           MODELE          =SIMP(statut='o',typ=modele ),
         ),
         SPEC_EXCI_POINT =FACT(statut='f',min=00,max=01,
           regles=(UN_PARMI('INTE_SPEC','GRAPPE_2'),),
           INTE_SPEC       =SIMP(statut='f',typ=tabl_intsp ),
           GRAPPE_2        =SIMP(statut='f',typ='TXM',
                                 into=("ASC_CEN","ASC_EXC","DES_CEN","DES_EXC",) ),
#  Quels sont les statuts des mots cles � l interieur des deux blocs qui suivent
           b_inte_spec =BLOC(condition = "INTE_SPEC != None",
             NATURE          =SIMP(statut='o',typ='TXM',max='**',into=("FORCE","MOMENT",) ),
             ANGL            =SIMP(statut='o',typ='R',max='**'),
             NOEUD           =SIMP(statut='o',typ=no,max='**'),
           ),
           b_grappe_2      =BLOC(condition = "GRAPPE_2 != None",
             RHO_FLUI        =SIMP(statut='o',typ='R' ),
             NOEUD           =SIMP(statut='o',typ=no),
           ),
           CARA_ELEM       =SIMP(statut='o',typ=cara_elem ),
           MODELE          =SIMP(statut='o',typ=modele ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_SQUELETTE=OPER(nom="DEFI_SQUELETTE",op= 110,sd_prod=squelette,
                    fr="D�finition d un maillage de visualisation",
                    docu="U4.24.01-e",reentrant='n',
         regles=(UN_PARMI('MODE_CYCL','MODELE_GENE','MAILLAGE'),
                 PRESENT_PRESENT('MODE_CYCL','SECTEUR'),
                 EXCLUS('SOUS_STRUC','SECTEUR'),
                 PRESENT_PRESENT('NOM_GROUP_MA','MODELE_GENE'),
                 PRESENT_PRESENT('NOM_GROUP_MA','SOUS_STRUC'),),
         MODE_CYCL       =SIMP(statut='f',typ=mode_cycl ),
         MODELE_GENE     =SIMP(statut='f',typ=modele_gene ),
         SQUELETTE       =SIMP(statut='f',typ=squelette ),
         RECO_GLOBAL     =FACT(statut='f',min=01,max='**',
           regles=(EXCLUS('TOUT','GROUP_NO_1'),
                   PRESENT_PRESENT('GROUP_NO_1','GROUP_NO_2'),
                   PRESENT_PRESENT('GROUP_NO_1','SOUS_STRUC_1'),
                   PRESENT_PRESENT('GROUP_NO_2','SOUS_STRUC_2'),
                   PRESENT_PRESENT('SOUS_STRUC_1','SOUS_STRUC_2'),),
           TOUT            =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI",) ),
           GROUP_NO_1      =SIMP(statut='f',typ=grno),
           SOUS_STRUC_1    =SIMP(statut='f',typ='TXM' ),
           GROUP_NO_2      =SIMP(statut='f',typ=grno),
           SOUS_STRUC_2    =SIMP(statut='f',typ='TXM' ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           DIST_REFE       =SIMP(statut='f',typ='R' ),
         ),
         NOM_GROUP_MA    =FACT(statut='f',min=01,max='**',
           NOM             =SIMP(statut='o',typ='TXM' ),
           SOUS_STRUC      =SIMP(statut='o',typ='TXM' ),
           GROUP_MA        =SIMP(statut='o',typ=grma),
         ),
         EXCLUSIF        =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         MAILLAGE        =SIMP(statut='f',typ=maillage ),
         MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         TRANS           =SIMP(statut='f',typ='R',min=3,max=3),
         ANGL_NAUT       =SIMP(statut='f',typ='R',min=3,max=3),
         SOUS_STRUC      =FACT(statut='f',min=01,max='**',
           NOM             =SIMP(statut='f',typ='TXM' ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         ),
         SECTEUR         =FACT(statut='f',min=01,max='**',
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_TEXTURE=OPER(nom="DEFI_TEXTURE",op= 181,sd_prod=tabl_texture,
                  fr=" ",docu="U4.43.05-a",reentrant='n',
         SYST_GLISSEMENT =FACT(statut='o',min=3,max=3,
           N               =SIMP(statut='o',typ='R',min=12,max=12 ),  
           L               =SIMP(statut='o',typ='R',max='**' ),  
         ),
         PLAN            =FACT(statut='o',min=40,max=40,
           ANGL_NAUT       =SIMP(statut='o',typ='R',max='**' ),  
           PROPORTION      =SIMP(statut='o',typ='R' ),  
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_THER_JOULE=OPER(nom="DEFI_THER_JOULE",op= 121,sd_prod=fonction,docu="U4.MK.20-d",reentrant='n',
                    fr="Calculer la fonction d �volution temporelle de temp�rature due � l effet JOULE dans un cable",
         LIST_INST       =SIMP(statut='o',typ=listr8),
         INST_CC_INIT    =SIMP(statut='f',typ='R',defaut= 0.0E+0 ),
         INST_CC_FIN     =SIMP(statut='f',typ='R',defaut= 1.0E+10),
         INST_RENC_INIT  =SIMP(statut='f',typ='R',defaut= 1.0E+10),
         INST_RENC_FIN   =SIMP(statut='f',typ='R',defaut= 1.0E+10),
         TEMP_EXT_POSE   =SIMP(statut='f',typ='R',defaut= 15.0E+0),
         TEMP_EXT        =SIMP(statut='f',typ='R',defaut= 15.0E+0),
         TEMP_RESI_REF   =SIMP(statut='f',typ='R',defaut= 20.0E+0),
         PARA_COND_1D    =FACT(statut='f',min=01,max='**',
           INTE_CC         =SIMP(statut='f',typ='R',defaut= 0.0E+0),
           INTE_RENC       =SIMP(statut='f',typ='R',defaut= 0.0E+0),
           A               =SIMP(statut='f',typ='R',defaut= 1.0E+0),
           SECTION         =SIMP(statut='f',typ='TXM',defaut="CERCLE",into=("CERCLE",) ),
           RESI_R0         =SIMP(statut='f',typ='R',defaut= 0.0E+0),
           RESI_R1         =SIMP(statut='f',typ='R',defaut= 0.E+0),
           RHO_CP          =SIMP(statut='f',typ='R',defaut= 1.0E+0),
           COEF_H          =SIMP(statut='f',typ='R',defaut= 40.0E+0),
           TEMP_INIT       =SIMP(statut='f',typ='R',defaut= 15.0E+0),
         ),
)  ;

#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFI_TRC=OPER(nom="DEFI_TRC",op=94,sd_prod=tabl_trc,docu="U4.43.04-e",reentrant='n',
              fr="D�finition d un diagramme de transformations en refroidissement continu d un acier",
         HIST_EXP        =FACT(statut='o',min=01,max='**',
           VALE            =SIMP(statut='o',typ='R',max='**'),
         ),
         TEMP_MS         =FACT(statut='o',min=01,max='**',
           SEUIL           =SIMP(statut='o',typ='R'),
           AKM             =SIMP(statut='o',typ='R'),
           BKM             =SIMP(statut='o',typ='R'),
           TPLM            =SIMP(statut='o',typ='R'),
         ),
         GRAIN_AUST      =FACT(statut='f',min=01,max='**',
           DREF           =SIMP(statut='f',typ='R'),
           A              =SIMP(statut='f',typ='R'),
         ),
)  ;
#& MODIF COMMANDE  DATE 12/09/2001   AUTEUR MCOURTOI M.COURTOIS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def defi_valeur_prod(self,IS=None,R8=None,TX=None,C8=None,LS=None):
  if IS != None  : return entier
  if R8 != None  : return reel
  if TX != None  : return chaine
  if C8 != None  : return complexe
  if LS != None  : return liste
  raise AsException("type de concept resultat non prevu")

DEFI_VALEUR=MACRO(nom="DEFI_VALEUR",op=-4,sd_prod=defi_valeur_prod,
                 fr="Affectation d une valeur � une variable Superviseur",
                 docu="U4.31.04-e1",reentrant='f',
         regles=(UN_PARMI('IS','R8','TX','C8','LS'),),
         IS              =SIMP(statut='f',typ='I',max='**'),
         R8              =SIMP(statut='f',typ='R',max='**'),
         TX              =SIMP(statut='f',typ='TXM',max='**'),
         C8              =SIMP(statut='f',typ='C',max='**'),
         LS              =SIMP(statut='f',typ='L',max='**'),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEFUFI=PROC(nom="DEFUFI",op=21,docu="U4.12.01-d",
            fr="Modification / ajout d une unit� logique en sortie en compl�ment de celles d�finies dans DEBUT",
         IMPRESSION      =FACT(statut='o',min=01,max='**',
           NOM             =SIMP(statut='o',typ='TXM',max='**'),
           UNITE           =SIMP(statut='o',typ='I' ),
         ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DEPL_INTERNE=OPER(nom="DEPL_INTERNE",op=89,sd_prod=cham_no_depl_r,docu="U4.62.02-e",reentrant='n',
                  fr="R�cup�ration du champ de d�placement interne � une sous-structure",
         DEPL_GLOBAL     =SIMP(statut='o',typ=cham_no_depl_r),
         MAILLE          =SIMP(statut='o',typ=ma,max=1),
         NOM_CAS         =SIMP(statut='f',typ='TXM',defaut=" "),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DETRUIRE=PROC(nom="DETRUIRE",op=-7,docu="U4.14.01-d",
              fr="Destruction d un concept utilisateur dans la base GLOBALE",
             op_init=ops.detruire,
            CONCEPT     =FACT(statut='o',min=01,
            NOM         =SIMP(statut='o',typ=assd,max='**'),
        ),
);
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DIST_LIGN_3D=OPER(nom="DIST_LIGN_3D",op= 133,sd_prod=fonction,docu="U4.MK.30-d",reentrant='n', 
                  fr="Calcul sous forme d une fonction du temps de la distance minimale entre deux structures filaires",
      regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','LIST_ORDRE','INST','LIST_INST'),
              UN_PARMI('GROUP_MA_2','POIN_FIXE'),),
         MODELE          =SIMP(statut='o',typ=modele),
         RESULTAT        =SIMP(statut='o',typ=(evol_elas,dyna_trans,evol_noli) ),
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",)),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
         INST            =SIMP(statut='f',typ='R',max='**'),
         LIST_INST       =SIMP(statut='f',typ=listr8),
         LIST_ORDRE      =SIMP(statut='f',typ=listis),
         PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
         CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
         GROUP_MA_1      =SIMP(statut='o',typ=grma,max='**'),
         GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
         POIN_FIXE       =SIMP(statut='f',typ='R',min=3,max=3),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 28/03/2001   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DYNA_ALEA_MODAL=OPER(nom="DYNA_ALEA_MODAL",op= 131,sd_prod=tabl_intsp
                    ,fr="Calcule la r�ponse spectrale d une structure lin�aire sous une excitation connue par sa DSP",
                     docu="U4.53.22-d",reentrant='n',
         BASE_MODALE     =FACT(statut='o',min=01,max=01,
           regles=(UN_PARMI('NUME_ORDRE','BANDE'),),
           MODE_MECA       =SIMP(statut='o',typ=mode_meca ),
           BANDE           =SIMP(statut='f',typ='R',max=02),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           b_bande =BLOC(condition = "BANDE != None",
             AMOR_UNIF       =SIMP(statut='o',typ='R' ),
           ),
           b_nume_ordre =BLOC(condition = "NUME_ORDRE != None",
             AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),
           ),
         ),
         MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc,)),
         EXCIT           =FACT(statut='o',min=01,max=01,
           regles=(UN_PARMI('NOEUD_I','NUME_ORDRE_I'), 
                   EXCLUS('CHAM_NO','NOEUD'),),
           DERIVATION      =SIMP(statut='f',typ='I',defaut= 0,into=( 0 , 1 , 2 ) ),
           MODAL           =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
#  dans la doc U il y a plus de choix pour GRANDEUR
           GRANDEUR        =SIMP(statut='f',typ='TXM',defaut="DEPL_R",
                                 into=("DEPL_R","EFFO","SOUR_DEBI_VOLU","SOUR_DEBI_MASS","SOUR_PRESS","SOUR_FORCE")),
           INTE_SPEC       =SIMP(statut='o',typ=tabl_intsp ),
           NUME_VITE_FLUI  =SIMP(statut='f',typ='I' ),
           OPTION          =SIMP(statut='f',typ='TXM',defaut="TOUT",into=("TOUT","DIAG",) ),
#  Toutes les regles ne semblent pas avoir �t� ecrites dans la doc U
           NUME_ORDRE_I    =SIMP(statut='f',typ='I',max='**'),
           NOEUD_I         =SIMP(statut='f',typ=no,max='**'),
           b_nume_ordre_i  =BLOC(condition = "NUME_ORDRE_I != None",
             NUME_ORDRE_J    =SIMP(statut='o',typ='I',max='**'),
           ),
           b_noeud_i       =BLOC(condition = "NOEUD_I != None",
             NOEUD_J         =SIMP(statut='o',typ=no,max='**'),
             NOM_CMP_I       =SIMP(statut='o',typ='TXM',max='**'),
             NOM_CMP_J       =SIMP(statut='o',typ='TXM',max='**'),
           ),
           CHAM_NO         =SIMP(statut='f',typ=cham_no),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           b_noeud         =BLOC(condition = "NOEUD != None",
             NOM_CMP         =SIMP(statut='o',typ='TXM',max='**'),
           ),           
         ),
         REPONSE         =FACT(statut='f',min=01,max=01,
           regles=(EXCLUS('FREQ_MIN','NB_POIN_MODE'),
                   EXCLUS('FREQ_MIN','FREQ_EXCIT'),
                   ENSEMBLE('FREQ_MIN','FREQ_MAX'),),
#  Toutes les regles ne semblent pas avoir �t� ecrites dans la doc U
           DERIVATION      =SIMP(statut='f',typ='I',defaut= 0,into=( 0 , 1 , 2 ,) ),
           OPTION          =SIMP(statut='f',typ='TXM',defaut="TOUT",into=("TOUT","DIAG") ),
           FREQ_MIN        =SIMP(statut='f',typ='R' ),
           FREQ_MAX        =SIMP(statut='f',typ='R' ),
           PAS             =SIMP(statut='f',typ='R' ),
           FREQ_EXCIT      =SIMP(statut='f',typ='TXM',defaut="AVEC",into=("AVEC","SANS") ),
           NB_POIN_MODE    =SIMP(statut='f',typ='I',defaut= 50 ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 10/07/2001   AUTEUR ACBHHCD G.DEVESA 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def dyna_line_harm_prod(MATR_MASS,**args):
  if AsType(MATR_MASS) == matr_asse_depl_r : return dyna_harmo
  if AsType(MATR_MASS) == matr_asse_depl_c : return dyna_harmo
  if AsType(MATR_MASS) == matr_asse_pres_c : return acou_harmo
  if AsType(MATR_MASS) == matr_asse_gene_r : return harm_gene
  raise AsException("type de concept resultat non prevu")

DYNA_LINE_HARM=OPER(nom="DYNA_LINE_HARM",op=  60,sd_prod=dyna_line_harm_prod,
                    fr="R�ponse dynamique complexe d un syst�me � une excitation harmonique",
                    docu="U4.53.11-e",reentrant='n',
         regles=(PRESENT_ABSENT('AMOR_REDUIT','MATR_AMOR'),
                 PRESENT_ABSENT('AMOR_REDUIT','LIST_AMOR'),
                 PRESENT_ABSENT('MATR_AMOR','LIST_AMOR'),
                 UN_PARMI('FREQ','LIST_FREQ'),),
         MODELE          =SIMP(statut='f',typ=modele ),
         CHAM_MATER      =SIMP(statut='f',typ=cham_mater ),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem ),
         MATR_MASS       =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_pres_c,matr_asse_gene_r ) ),
         MATR_RIGI       =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_depl_c,matr_asse_pres_c
                                              ,matr_asse_gene_r,matr_asse_gene_c ) ),
         MATR_AMOR       =SIMP(statut='f',typ=(matr_asse_depl_r,matr_asse_pres_c,matr_asse_gene_r ) ),
         AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),
         LIST_AMOR       =SIMP(statut='f',typ=listr8 ),
         MATR_IMPE_PHI   =SIMP(statut='f',typ=(matr_asse_depl_r,matr_asse_gene_r) ),
         FREQ            =SIMP(statut='f',typ='R',max='**'),
         LIST_FREQ       =SIMP(statut='f',typ=listr8 ),
         TOUT_CHAM       =SIMP(statut='f',typ='TXM',into=("OUI",)),
         NOM_CHAM        =SIMP(statut='f',typ='TXM',max=03,into=("DEPL","VITE","ACCE") ),
         EXCIT           =FACT(statut='o',min=01,max='**',
           regles=(UN_PARMI('VECT_ASSE','CHARGE'),
                   UN_PARMI('FONC_MULT','FONC_MULT_C','COEF_MULT','COEF_MULT_C'),),
           VECT_ASSE       =SIMP(statut='f',typ=(cham_no_depl_r,cham_no_pres_c,vect_asse_gene ) ),
           CHARGE          =SIMP(statut='f',typ=char_meca ),
           TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FIXE",into=("FIXE",) ),
           FONC_MULT_C     =SIMP(statut='f',typ=fonction_c ),
           COEF_MULT_C     =SIMP(statut='f',typ='C' ),
           FONC_MULT       =SIMP(statut='f',typ=fonction ),
           COEF_MULT       =SIMP(statut='f',typ='R' ),
           PHAS_DEG        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           PUIS_PULS       =SIMP(statut='f',typ='I',defaut= 0 ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 28/03/2001   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DYNA_LINE_TRAN=OPER(nom="DYNA_LINE_TRAN",op=  48,sd_prod=dyna_trans,
                    fr="R�ponse temporelle d un syst�me � une excitation transitoire",
                    docu="U4.53.02-f",reentrant='f',
         regles=(UN_PARMI('NEWMARK','WILSON','DIFF_CENTRE','ADAPT'),),
         MODELE          =SIMP(statut='f',typ=modele ),
         CHAM_MATER      =SIMP(statut='f',typ=cham_mater ),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem ),
         MATR_MASS       =SIMP(statut='o',typ=matr_asse_depl_r ),
         MATR_RIGI       =SIMP(statut='o',typ=matr_asse_depl_r ),
         MATR_AMOR       =SIMP(statut='f',typ=matr_asse_depl_r ),
         MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc,) ),
         NEWMARK         =FACT(statut='f',min=01,max=01,
           ALPHA           =SIMP(statut='f',typ='R',defaut= 0.25 ),
           DELTA           =SIMP(statut='f',typ='R',defaut= 0.5 ),
         ),
         WILSON          =FACT(statut='f',min=01,max=01,
           THETA           =SIMP(statut='f',typ='R',defaut= 1.4 ),
         ),
         DIFF_CENTRE     =FACT(statut='f',min=01,max=01,
         ),
         ADAPT           =FACT(statut='f',min=01,max=01,
         ),
         ETAT_INIT       =FACT(statut='f',min=01,max=01,
           regles=(EXCLUS('DYNA_TRANS','DEPL_INIT'),
                   EXCLUS('DYNA_TRANS','VITE_INIT'),),
           DYNA_TRANS      =SIMP(statut='f',typ=dyna_trans ),
#  j ai interprete la doc U : est-ce bon           
           b_dyna_trans    =BLOC(condition = "DYNA_TRANS != None",
             regles=(EXCLUS('NUME_INIT','INST_INIT' ),),
             NUME_INIT       =SIMP(statut='f',typ='I' ),
             INST_INIT       =SIMP(statut='f',typ='R' ),
             b_inst_init     =BLOC(condition = "INST_INIT != None",
               PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
               CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
             ),
           ),
           DEPL_INIT       =SIMP(statut='f',typ=(cham_no_depl_r) ),
           VITE_INIT       =SIMP(statut='f',typ=(cham_no_depl_r) ),
         ),
         EXCIT           =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('CHARGE','VECT_ASSE'),
                   EXCLUS('CHARGE','COEF_MULT'),
                   EXCLUS('FONC_MULT','COEF_MULT'),
                   EXCLUS('ACCE','COEF_MULT'),
                   PRESENT_ABSENT('ACCE','FONC_MULT'),
                   PRESENT_PRESENT('ACCE','VITE','DEPL'),
                   PRESENT_ABSENT('MULT_APPUI','FONC_MULT'),),
           VECT_ASSE       =SIMP(statut='f',typ=cham_no_depl_r ),
           CHARGE          =SIMP(statut='f',typ=char_meca ),
           FONC_MULT       =SIMP(statut='f',typ=fonction ),
           COEF_MULT       =SIMP(statut='f',typ='R' ),
           TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FIXE",into=("FIXE",) ),
           ACCE            =SIMP(statut='f',typ=fonction ),
           VITE            =SIMP(statut='f',typ=fonction ),
           DEPL            =SIMP(statut='f',typ=fonction ),
           MULT_APPUI      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
           DIRECTION       =SIMP(statut='f',typ='R',max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
         ),
         AMOR_MODAL      =FACT(statut='f',min=01,max=01,
           MODE_MECA       =SIMP(statut='f',typ=mode_meca ),
           AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),
           NB_MODE         =SIMP(statut='f',typ='I',defaut= 9999 ),
           REAC_VITE       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         ),
#  ce n est pas le mot clesolveur standard
         SOLVEUR         =FACT(statut='d',min=01,max=01,
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
           STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
           NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
         ),
         INCREMENT       =FACT(statut='o',min=01,max='**',
           regles=(UN_PARMI('LIST_INST','FONC_INST','PAS'),),
           LIST_INST       =SIMP(statut='f',typ=listr8 ), 
           FONC_INST       =SIMP(statut='f',typ=fonction ),       
           PAS             =SIMP(statut='f',typ='R' ),
           b_pas           =BLOC(condition = "PAS != None",
               INST_INIT       =SIMP(statut='f',typ='R' ),
               INST_FIN        =SIMP(statut='f',typ='R' ),    
           ),
           b_list_fonc     =BLOC(condition = "LIST_INST != None or FONC_INST != None",
               regles=(EXCLUS('INST_FIN','NUME_FIN'),),
               NUME_FIN        =SIMP(statut='f',typ='I' ), 
               INST_FIN        =SIMP(statut='f',typ='R' ),   
           ),
           VITE_MIN        =SIMP(statut='f',typ='TXM',defaut="NORM",into=("MAXI","NORM") ),
           COEF_MULT_PAS   =SIMP(statut='f',typ='R',defaut= 1.1 ),
           COEF_DIVI_PAS   =SIMP(statut='f',typ='R',defaut= 1.33334 ),
           PAS_LIMI_RELA   =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
           NB_POIN_PERIODE =SIMP(statut='f',typ='I',defaut= 50 ),
           NMAX_ITER_PAS   =SIMP(statut='f',typ='I',defaut= 16 ),
           PAS_CALCUL      =SIMP(statut='f',typ='I',defaut= 1 ),
         ),
         ARCHIVAGE       =FACT(statut='f',min=01,max=01,
           regles=(UN_PARMI('LIST_ARCH','PAS_ARCH', ),),
           LIST_ARCH       =SIMP(statut='f',typ=listis ),
           PAS_ARCH        =SIMP(statut='f',typ='I' ),
           CHAM_EXCLU      =SIMP(statut='f',typ='TXM',max='**',into=("DEPL","VITE","ACCE") ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 30/01/2002   AUTEUR VABHHTS J.TESELET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DYNA_NON_LINE=OPER(nom="DYNA_NON_LINE",op= 70,sd_prod=evol_noli,reentrant='f',
                   fr="Analyse m�canique dynamique non lin�aire",docu="U4.53.01-e1",
         regles=(AU_MOINS_UN('COMP_INCR','COMP_ELAS',),
                 UN_PARMI('NEWMARK','HHT', ),),
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater),
         MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc,)),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),
         EXCIT           =FACT(statut='o',min=1,max='**',
           regles=(PRESENT_ABSENT('FONC_MULT','ACCE'),
                   PRESENT_PRESENT('ACCE','VITE','DEPL'),
                   PRESENT_ABSENT('MULT_APPUI','FONC_MULT'),),
           TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FIXE_CSTE",
                                 into=("FIXE_CSTE","FIXE_PILO","SUIV","DIDI")),
           CHARGE          =SIMP(statut='o',typ=char_meca),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
           DEPL            =SIMP(statut='f',typ=fonction),
           ACCE            =SIMP(statut='f',typ=fonction),
           VITE            =SIMP(statut='f',typ=fonction),
           MULT_APPUI      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           DIRECTION       =SIMP(statut='f',typ='R',max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
         ),
         AMOR_MODAL      =FACT(statut='f',min=1,max=1,
           MODE_MECA       =SIMP(statut='f',typ=mode_meca),
           AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**' ),
           NB_MODE         =SIMP(statut='f',typ='I',defaut= 9999 ),
           REAC_VITE       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         ),
         COMP_INCR       =FACT(statut='f',min=1,max='**',
           RELATION        =SIMP(statut='o',typ='TXM',defaut="VMIS_ISOT_TRAC",
                                 into=( "ELAS",
                                        "VMIS_ISOT_TRAC",
                                        "VMIS_ISOT_LINE",
                                        "VMIS_ECMI_TRAC",
                                        "VMIS_ECMI_LINE",
                                        "LABORD_1D",
                                        "ENDO_LOCAL",
                                        "ENDO_FRAGILE",
                                        "BETON_ENDO_LOCAL",
                                        "RUPT_FRAG",
                                        "PLAS_GRAD_LINE",
                                        "PLAS_GRAD_TRAC",
                                        "DURC_GRAD",
                                        "META_P_IL",
                                        "META_P_IL_PT",
                                        "META_P_IL_RE",
                                        "META_P_IL_PT_RE",
                                        "META_V_IL",
                                        "META_V_IL_PT",
                                        "META_V_IL_RE",
                                        "META_V_IL_PT_RE",
                                        "META_P_INL",
                                        "META_P_INL_PT",
                                        "META_P_INL_RE",
                                        "META_P_INL_PT_RE",
                                        "META_V_INL",
                                        "META_V_INL_PT",
                                        "META_V_INL_RE",
                                        "META_V_INL_PT_RE",
                                        "META_P_CL",
                                        "META_P_CL_PT",
                                        "META_P_CL_RE",
                                        "META_P_CL_PT_RE",
                                        "META_V_CL",
                                        "META_V_CL_PT",
                                        "META_V_CL_RE",
                                        "META_V_CL_PT_RE",
                                        "VMIS_CINE_LINE",
                                        "VISC_TAHERI",
                                        "CHABOCHE",
                                        "VISCOCHAB",
                                        "VMIS_CIN1_CHAB",
                                        "VMIS_CIN2_CHAB",
                                        "POLY_CFC",
                                        "LMARC",
                                        "ROUSSELIER",
                                        "ROUSS_PR",
                                        "ROUSS_VISC",
                                        "VMIS_POU_LINE",
                                        "VMIS_POU_FLEJOU",
                                        "COULOMB",
                                        "ARME",
                                        "ASSE_CORN",
                                        "NORTON_HOFF",
                                        "LEMAITRE",
                                        "ZIRC_CYRA2",
                                        "ZIRC_EPRI",
                                        "ASSE_COMBU",
                                        "VENDOCHAB",
                                        "NADAI_B",
                                        "DIS_CONTACT",
                                        "DIS_CHOC",
                                        "DIS_GOUJ2E_PLAS",
                                        "DIS_GOUJ2E_ELAS",
                                        "GRILLE_ISOT_LINE",
                                        "GRILLE_CINE_LINE",
                                        "GRILLE_PINTO_MEN",
                                        "PINTO_MENEGOTTO",
                                        "CJS",
                                        "OHNO",
                                        "GRANGER_FP",
                                        "GRANGER_FP_V",
                                        "BETON_DOUBLE_DP",
                                        "KIT_HM",
                                        "KIT_HHM",
                                        "KIT_THH",
                                        "KIT_THM",
                                        "KIT_THHM",
                                        "VMIS_ASYM_LINE",
                                        "ELAS_THM",
                                        "SURF_ETAT_NSAT",
                                        "SURF_ETAT_SATU",
                                        "CAM_CLAY_THM",
                                        "KIT_DDI",
                                     ) ),
           ELAS            =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           VMIS_ISOT_TRAC  =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           VMIS_ISOT_LINE  =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           VMIS_ECMI_TRAC  =SIMP(statut='c',typ='I',defaut=8,into=(8,)),
           VMIS_ECMI_LINE  =SIMP(statut='c',typ='I',defaut=8,into=(8,)),
           LABORD_1D   =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           ENDO_LOCAL      =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           ENDO_FRAGILE    =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           BETON_ENDO_LOCAL=SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           RUPT_FRAG       =SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           PLAS_GRAD_LINE  =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           PLAS_GRAD_TRAC  =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           DURC_GRAD       =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           META_P_IL         =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_IL_PT       =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_IL_RE       =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_IL_PT_RE    =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_IL          =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_IL_PT       =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_IL_RE       =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_IL_PT_RE    =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_INL         =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_INL_PT      =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_INL_RE      =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_INL_PT_RE   =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_INL         =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_INL_PT      =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_INL_RE      =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_INL_PT_RE   =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_CL          =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_P_CL_PT       =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_P_CL_RE       =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_P_CL_PT_RE    =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_V_CL          =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_V_CL_PT       =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_V_CL_RE       =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_V_CL_PT_RE    =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
           VMIS_CINE_LINE  =SIMP(statut='c',typ='I',defaut=7,into=(7,)),
           CHABOCHE        =SIMP(statut='c',typ='I',defaut=14,into=(14,)),
           VISCOCHAB       =SIMP(statut='c',typ='I',defaut=28,into=(28,)),
           VMIS_CIN1_CHAB  =SIMP(statut='c',typ='I',defaut=8,into=(8,)),
           VMIS_CIN2_CHAB  =SIMP(statut='c',typ='I',defaut=14,into=(14,)),
           POLY_CFC        =SIMP(statut='c',typ='I',defaut=1688,into=(1688,)),
           LMARC           =SIMP(statut='c',typ='I',defaut=20,into=(20,)),
           VISC_TAHERI     =SIMP(statut='c',typ='I',defaut=9,into=(9,)),
           ROUSSELIER      =SIMP(statut='c',typ='I',defaut=9,into=(9,)),
           ROUSS_PR        =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           ROUSS_VISC      =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           VMIS_POU_LINE   =SIMP(statut='c',typ='I',defaut=9,into=(9,)),
           VMIS_POU_FLEJOU =SIMP(statut='c',typ='I',defaut=9 ,into=(9,)),
           COULOMB         =SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           ASSE_CORN       =SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           ARME            =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           NORTON_HOFF     =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           LEMAITRE        =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           ZIRC_CYRA2      =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           ZIRC_EPRI       =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           ASSE_COMBU      =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           NADAI_B         =SIMP(statut='c',typ='I',defaut=34,into=(34,)),
           VENDOCHAB       =SIMP(statut='c',typ='I',defaut=10,into=(10,)),
           GRILLE_ISOT_LINE=SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           GRILLE_CINE_LINE=SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           GRILLE_PINTO_MEN=SIMP(statut='c',typ='I',defaut=16,into=(16,)),
           DIS_CONTACT     =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
           DIS_CHOC        =SIMP(statut='c',typ='I',defaut=7,into=(7,)),
           DIS_GOUJ2E_PLAS =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           DIS_GOUJ2E_ELAS =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           PINTO_MENEGOTTO =SIMP(statut='c',typ='I',defaut=8,into=(8,)),
           CJS             =SIMP(statut='c',typ='I',defaut=16,into=(16,)),
           OHNO            =SIMP(statut='c',typ='I',defaut=32,into=(32,)),
           GRANGER_FP      =SIMP(statut='c',typ='I',defaut=55,into=(55,)),
           GRANGER_FP_V    =SIMP(statut='c',typ='I',defaut=55,into=(55,)),
           BETON_DOUBLE_DP =SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           KIT_HM          =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           KIT_HHM         =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           KIT_THH         =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           KIT_THM         =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           KIT_THHM        =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           VMIS_ASYM_LINE  =SIMP(statut='c',typ='I',defaut=4,into=(4,)),

           RELATION_KIT    =SIMP(statut='f',typ='TXM',max='**',
                                 into=(
# MECA
                                       "ELAS",
                                       "CJS",
                                       "ELAS_THM",
                                       "SURF_ETAT_NSAT",
                                       "SURF_ETAT_SATU",
                                       "CAM_CLAY_THM",
# THMC
                                       "GAZ",
                                       "LIQU_SATU",
                                       "LIQU_SATU_GAT",
                                       "LIQU_GAZ_ATM",
                                       "LIQU_VAPE_GAZ",
                                       "LIQU_NSAT_GAT",
                                       "LIQU_GAZ",
# THER
                                       "THER_HOMO",
                                       "THER_POLY",
# HYDR
                                       "HYDR_UTIL",
                                       "HYDR",
# MECA_META
                                       "ACIER",
                                       "ZIRC",
# MECA KIT_DDI
                                       "VMIS_ISOT_TRAC",
                                       "VMIS_ISOT_LINE",
                                       "VMIS_ISOT_CINE",
                                       "GRANGER_FP",
                                       "GRANGER_FP_V",
                                       "ROUSSELIER",
                                       "CHABOCHE",
                                       "OHNO",
                                       "NADAI_B",
                                       "BETON_DOUBLE_DP",
                                       ) ),
           ELAS_THM        =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           SURF_ETAT_NSAT  =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           SURF_ETAT_SATU  =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           CAM_CLAY_THM    =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
           GAZ             =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           LIQU_SATU       =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           LIQU_SATU_GAT   =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           LIQU_GAZ_ATM    =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           LIQU_VAPE_GAZ   =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           LIQU_NSAT_GAT   =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           LIQU_GAZ        =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           THER_HOMO       =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           THER_POLY       =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           HYDR_UTIL       =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           HYDR            =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           ACIER           =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           ZIRC            =SIMP(statut='c',typ='I',defaut=3,into=(3,)),

           DEFORMATION     =SIMP(statut='f',typ='TXM',defaut="PETIT",into=("PETIT","PETIT_REAC","SIMO_MIEHE","GREEN_GR","GREEN",)),
           ALGO_C_PLAN     =SIMP(statut='f',typ='TXM',defaut="ANALYTIQUE",into=("DEBORST","ANALYTIQUE",)),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         ),
         COMP_ELAS       =FACT(statut='f',min=1,max='**',
           RELATION        =SIMP(statut='o',typ='TXM',defaut="ELAS",
                                 into=("ELAS","ELAS_VMIS_LINE","ELAS_VMIS_TRAC",
                                       "ELAS_POUTRE_GR","CABLE")),
           ELAS            =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           ELAS_VMIS_TRAC  =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           ELAS_VMIS_LINE  =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           ELAS_POUTRE_GR  =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           CABLE           =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           DEFORMATION     =SIMP(statut='f',typ='TXM',defaut="PETIT" ,into=("PETIT","GREEN","GREEN_GR",) ),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         ),
#-------------------------------------------------------------------
         ETAT_INIT       =FACT(statut='f',min=1,max=1,
           regles=(AU_MOINS_UN('EVOL_NOLI','DEPL','VITE','SIGM','VARI','VARI_NON_LOCAL',),
                   EXCLUS('EVOL_NOLI','DEPL',),
                   EXCLUS('EVOL_NOLI','VITE'),
                   EXCLUS('EVOL_NOLI','SIGM',),
                   EXCLUS('EVOL_NOLI','VARI',),
                   EXCLUS('EVOL_NOLI','VARI_NON_LOCAL',),
                   EXCLUS('NUME_ORDRE','INST'), ),
           DEPL            =SIMP(statut='f',typ=cham_no_depl_r),
           VITE            =SIMP(statut='f',typ=cham_no_depl_r),
           SIGM            =SIMP(statut='f',typ=(cham_elem_sief_r,carte_sief_r)),
           VARI            =SIMP(statut='f',typ=cham_elem_vari_r),
           VARI_NON_LOCAL  =SIMP(statut='f',typ=cham_no_vanl_r),
           EVOL_NOLI       =SIMP(statut='f',typ=evol_noli),
           NUME_ORDRE      =SIMP(statut='f',typ='I'),
           INST            =SIMP(statut='f',typ='R'),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           NUME_DIDI       =SIMP(statut='f',typ='I'),
           INST_ETAT_INIT  =SIMP(statut='f',typ='R'),
         ),
#-------------------------------------------------------------------
         INCREMENT       =FACT(statut='o',min=1,max=1,
           regles=(EXCLUS('NUME_INST_INIT','INST_INIT'),
                   EXCLUS('NUME_INST_FIN','INST_FIN'),),
           LIST_INST       =SIMP(statut='o',typ=listr8),
           EVOLUTION       =SIMP(statut='f',typ='TXM',defaut="CHRONOLOGIQUE",
                                 into=("CHRONOLOGIQUE","RETROGRADE","SANS",) ),
           NUME_INST_INIT  =SIMP(statut='f',typ='I'),
           INST_INIT       =SIMP(statut='f',typ='R'),
           NUME_INST_FIN   =SIMP(statut='f',typ='I'),
           INST_FIN        =SIMP(statut='f',typ='R'),
           PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3 ),
           SUBD_PAS        =SIMP(statut='f',typ='I',defaut=1),
           SUBD_PAS_MINI   =SIMP(statut='f',typ='R'),
           COEF_SUBD_PAS_1 =SIMP(statut='f',typ='R',defaut= 1.0E+0),
         ),
#-------------------------------------------------------------------
         NEWMARK         =FACT(statut='f',min=1,max=1,
           ALPHA           =SIMP(statut='f',typ='R',defaut= 0.25),
           DELTA           =SIMP(statut='f',typ='R',defaut= 0.5),
         ),
         HHT             =FACT(statut='f',min=1,max=1,
           ALPHA           =SIMP(statut='f',typ='R'
                                ,defaut= -0.29999999999999999 ),
         ),
         NEWTON          =FACT(statut='d',min=1,max=1,
           REAC_INCR       =SIMP(statut='f',typ='I',defaut= 1 ),
           PREDICTION      =SIMP(statut='f',typ='TXM',into=("TANGENTE","ELASTIQUE") ),
           MATRICE         =SIMP(statut='f',typ='TXM',defaut="TANGENTE",into=("TANGENTE","ELASTIQUE") ),
           REAC_ITER       =SIMP(statut='f',typ='I',defaut= 0),
           PAS_MINI_ELAS   =SIMP(statut='f',typ='R',defaut=0.0E+0),
         ),
         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    =BLOC(condition= "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt          =BLOC(condition= "METHODE == 'LDLT'",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
           ),
           b_ldlt_mult     =BLOC(condition="METHODE == 'LDLT' or METHODE == 'MULT_FRONT'",
                                   fr="Param�tres relatifs � la non inversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON","DECOUPE") ),
           ),
           b_gcpc          =BLOC(condition="METHODE == 'GCPC'",fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut=0),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           SYME            =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         ),
#-------------------------------------------------------------------
         RECH_LINEAIRE   =FACT(statut='f',min=1,max=1,
           RESI_LINE_RELA  =SIMP(statut='f',typ='R',defaut= 1.0E-1 ),
           ITER_LINE_MAXI  =SIMP(statut='f',typ='I',defaut= 3),
         ),
         PILOTAGE        =FACT(statut='f',min=1,max=1,
           regles=(EXCLUS('NOEUD','GROUP_NO'),PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TYPE            =SIMP(statut='o',typ='TXM',into=("DDL_IMPO","LONG_ARC","PRED_ELAS","PRED_ELAS_INCR","DEFORMATION") ),
           COEF_MULT       =SIMP(statut='f',typ='R',defaut= 1.0E+0),
           ETA_PILO_MAX    =SIMP(statut='f',typ='R'),
           ETA_PILO_MIN    =SIMP(statut='f',typ='R'),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOM_CMP         =SIMP(statut='f',typ='TXM',max='**' ),
                         ),
         CONVERGENCE     =FACT(statut='d',min=1,max=1,
           RESI_GLOB_MAXI  =SIMP(statut='f',typ='R'),
           RESI_GLOB_RELA  =SIMP(statut='f',typ='R'),
           ITER_GLOB_MAXI  =SIMP(statut='f',typ='I',defaut=10),
           ITER_GLOB_ELAS  =SIMP(statut='f',typ='I',defaut=25),
           ARRET           =SIMP(statut='f',typ='TXM',defaut="OUI"),
           RESI_INTE_RELA  =SIMP(statut='f',typ='R'
                                ,defaut= 1.0E-6),
           ITER_INTE_MAXI  =SIMP(statut='f',typ='I',defaut= 10 ),
           ITER_INTE_PAS   =SIMP(statut='f',typ='I',defaut= 0 ),
           TYPE_MATR_COMP  =SIMP(statut='f',typ='TXM',defaut="TANG_VIT",into=("TANG_VIT",)),
           RESO_INTE       =SIMP(statut='f',typ='TXM',defaut="IMPLICITE",
                                 into=("RUNGE_KUTTA_2","RUNGE_KUTTA_4","IMPLICITE")),
         ),
#-------------------------------------------------------------------
         OPTION          =SIMP(statut='f',typ='TXM',max='**',defaut="ELNO",
                               into=("SIEF_ELNO_ELGA","VARI_ELNO_ELGA","EFGE_ELNO_CART","ELNO","SANS") ),
         ARCHIVAGE       =FACT(statut='f',min=1,max=1,
           regles=(EXCLUS('PAS_ARCH','LIST_INST','INST'),
                   EXCLUS('ARCH_ETAT_INIT','NUME_INIT'), ),
           LIST_INST       =SIMP(statut='f',typ=(listr8) ),
           INST            =SIMP(statut='f',typ='R',max='**' ),
           PAS_ARCH        =SIMP(statut='f',typ='I' ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3),
           ARCH_ETAT_INIT  =SIMP(statut='f',typ='TXM',into=("OUI",)),
           NUME_INIT       =SIMP(statut='f',typ='I'),
           DETR_NUME_SUIV  =SIMP(statut='f',typ='TXM',into=("OUI",)),
           CHAM_EXCLU      =SIMP(statut='f',typ='TXM',max='**',
           into=("DEPL","SIEF_ELGA","VARI_ELGA","ACCE","VITE","VARI_NON_LOCAL","LANL_ELGA")),
         ),
         OBSERVATION     =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('NOEUD','GROUP_NO','MAILLE'),
                   PRESENT_PRESENT('MAILLE','POINT'),),
           NOM_CHAM        =SIMP(statut='o',typ='TXM',max='**',

into=("DEPL","VITE","ACCE","SIEF_ELGA","VARI_ELGA","DEPL_ABSOLU","VITE_ABSOLU","ACCE_ABSOLU") ),
           NOM_CMP         =SIMP(statut='o',typ='TXM',max='**' ),
           LIST_ARCH       =SIMP(statut='f',typ=listis),
           LIST_INST       =SIMP(statut='f',typ=listr8),
           INST            =SIMP(statut='f',typ='R',max='**' ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           PAS_OBSE        =SIMP(statut='f',typ='I'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           POINT           =SIMP(statut='f',typ='I',max='**'),
         ),
#-------------------------------------------------------------------
         MODELE_NON_LOCAL=SIMP(statut='f',typ=(modele) ),
         b_non_local = BLOC ( condition = "MODELE_NON_LOCAL != None",
                              fr="Donn�es sp�cifiques au mod�le non local",
           SOLV_NON_LOCAL  =FACT(statut='f',min=1,max=1,
             METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
             b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
               RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
             ),
             b_ldlt         =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
               RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
             ),
             b_ldlt_mult    =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                    fr="Param�tres relatifs � la non inversibilit� de la matrice � factorise",
               NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
               STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
             ),
             b_gcpc         =BLOC(condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
               PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
               NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
               RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
               NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
             ),
             EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
           LAGR_NON_LOCAL  =FACT(statut='f',max=1,
             ITER_DUAL_MAXI  =SIMP(statut='f',typ='I',defaut= 50),
             RESI_DUAL_ABSO  =SIMP(statut='o',typ='R'),
             RESI_PRIM_ABSO  =SIMP(statut='o',typ='R'),
             RHO             =SIMP(statut='f',typ='R',defaut= 1000.),
             ITER_PRIM_MAXI  =SIMP(statut='f',typ='I',defaut= 10),
           ),
         ),
#-------------------------------------------------------------------
         PARM_THETA      =SIMP(statut='f',typ='R'
                              ,defaut= 1. ),
#-------------------------------------------------------------------
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DYNA_SPEC_MODAL=OPER(nom="DYNA_SPEC_MODAL",op= 147,sd_prod=tabl_intsp,
                     fr="Calcul de la r�ponse par recombinaison modale d'une structure lin�aire pour une excitation al�atoire",
                     docu="U4.53.23-c",reentrant='n',
         BASE_ELAS_FLUI  =SIMP(statut='o',typ=melasflu ),
         EXCIT           =FACT(statut='o',min=00,max=01,
           INTE_SPEC_GENE  =SIMP(statut='o',typ=tabl_intsp ),
         ),
         OPTION          =SIMP(statut='f',typ='TXM',defaut="TOUT",into=("TOUT","DIAG") ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
DYNA_TRAN_MODAL=OPER(nom="DYNA_TRAN_MODAL",op=  74,sd_prod=tran_gene,
                     fr="R�ponse dynamique transitoire en coordonn�es g�n�ralis�es par recombinaison modale",
                     docu="U4.53.21-e",reentrant='f',
      regles=(EXCLUS('AMOR_REDUIT','AMOR_GENE','LIST_AMOR'), 
              PRESENT_ABSENT('MODE_STAT','MODE_CORR'),),
         METHODE         =SIMP(statut='f',typ='TXM',defaut="EULER",
                               into=("EULER","NEWMARK","DEVOGE","ADAPT","ITMI") ),
         MASS_GENE       =SIMP(statut='o',typ=matr_asse_gene_r ),
         RIGI_GENE       =SIMP(statut='o',typ=matr_asse_gene_r ),
         AMOR_GENE       =SIMP(statut='f',typ=matr_asse_gene_r ),
         AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),
         LIST_AMOR       =SIMP(statut='f',typ=listr8 ),
         MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc) ),
         MODE_CORR       =SIMP(statut='f',typ=(mult_elas,mode_stat_acce) ,),
         
         ETAT_INIT       =FACT(statut='f',min=01,max=01,
           regles=(EXCLUS('RESU_GENE','DEPL_INIT_GENE'),
                   EXCLUS('RESU_GENE','VITE_INIT_GENE'),),
           RESU_GENE       =SIMP(statut='f',typ=tran_gene ),
           b_resu_gene     =BLOC(condition = "RESU_GENE != None",
             INST_INIT       =SIMP(statut='f',typ='R' ),
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           ),
           DEPL_INIT_GENE  =SIMP(statut='f',typ=vect_asse_gene ),
           VITE_INIT_GENE  =SIMP(statut='f',typ=vect_asse_gene ),
         ),
         INCREMENT       =FACT(statut='o',min=01,max='**',
           INST_INIT       =SIMP(statut='f',typ='R' ),
           INST_FIN        =SIMP(statut='o',typ='R' ),
           PAS             =SIMP(statut='f',typ='R' ),
           VERI_PAS        =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           VITE_MIN        =SIMP(statut='f',typ='TXM',defaut="NORM",into=("MAXI","NORM") ),
           COEF_MULT_PAS   =SIMP(statut='f',typ='R',defaut= 1.1 ),
           COEF_DIVI_PAS   =SIMP(statut='f',typ='R',defaut= 1.3333334 ),
           PAS_LIMI_RELA   =SIMP(statut='f',typ='R',defaut= 1.0E-6 ),
           NB_POIN_PERIODE =SIMP(statut='f',typ='I',defaut= 50 ),
           NMAX_ITER_PAS   =SIMP(statut='f',typ='I',defaut= 16 ),
         ),
         ARCHIVAGE       =FACT(statut='f',min=01,max=01,
           regles=(UN_PARMI('LIST_ARCH','PAS_ARCH'),),
           LIST_ARCH       =SIMP(statut='f',typ=listis ),
           PAS_ARCH        =SIMP(statut='f',typ='I' ),
         ),
         
         NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 20 ),
         RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
         LAMBDA          =SIMP(statut='f',typ='R',defaut= 10. ),
         
         EXCIT           =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('FONC_MULT','COEF_MULT','ACCE'),
                   PRESENT_PRESENT('ACCE','VITE','DEPL'),
                   PRESENT_PRESENT('D_FONC_DT','D_FONC_DT2'),
                   PRESENT_ABSENT('NUME_MODE','VECT_GENE','COEF_MULT'),
                   PRESENT_ABSENT('MULT_APPUI','CORR_STAT'),
                   PRESENT_ABSENT('MULT_APPUI','COEF_MULT'),
                   PRESENT_ABSENT('MULT_APPUI','FONC_MULT'),),
           VECT_GENE       =SIMP(statut='f',typ=vect_asse_gene ),
           NUME_MODE       =SIMP(statut='f',typ='I' ),
           FONC_MULT       =SIMP(statut='f',typ=fonction ),
           COEF_MULT       =SIMP(statut='f',typ='R' ),
           ACCE            =SIMP(statut='f',typ=fonction ),
           VITE            =SIMP(statut='f',typ=fonction ),
           DEPL            =SIMP(statut='f',typ=fonction ),
           MULT_APPUI      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           DIRECTION       =SIMP(statut='f',typ='R',max='**'),
           b_loca          =BLOC(condition= "DIRECTION != None",
             regles=(EXCLUS('NOEUD','GROUP_NO'),),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           ),
           CORR_STAT       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           D_FONC_DT       =SIMP(statut='f',typ=fonction ),
           D_FONC_DT2      =SIMP(statut='f',typ=fonction ),
         ),
         CHOC            =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NOEUD_1','GROUP_NO_1' ),
                   PRESENT_ABSENT('NOEUD_1','GROUP_NO_1'),
                   PRESENT_ABSENT('NOEUD_2','GROUP_NO_2'),),
           INTITULE        =SIMP(statut='f',typ='TXM' ),
           NOEUD_1         =SIMP(statut='f',typ=no),
           NOEUD_2         =SIMP(statut='f',typ=no),
           GROUP_NO_1      =SIMP(statut='f',typ=grno),
           GROUP_NO_2      =SIMP(statut='f',typ=grno),
           OBSTACLE        =SIMP(statut='o',typ=obstacle ),
           ORIG_OBST       =SIMP(statut='f',typ='R',min=3,max=3),
           NORM_OBST       =SIMP(statut='o',typ='R',min=3,max=3),
           ANGL_VRIL       =SIMP(statut='f',typ='R' ),
           JEU             =SIMP(statut='f',typ='R',defaut= 1. ),
           DIST_1          =SIMP(statut='f',typ='R',val_min=0.E+0 ),
           DIST_2          =SIMP(statut='f',typ='R',val_min=0.E+0 ),
           SOUS_STRUC_1    =SIMP(statut='f',typ='TXM' ),
           SOUS_STRUC_2    =SIMP(statut='f',typ='TXM' ),
           REPERE          =SIMP(statut='f',typ='TXM',defaut="GLOBAL"),
           RIGI_NOR        =SIMP(statut='f',typ='R' ),
           AMOR_NOR        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           RIGI_TAN        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           AMOR_TAN        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           COULOMB         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),

           LAME_FLUIDE     =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           b_lame          =BLOC(condition="LAME_FLUIDE=='OUI'",
               ALPHA           =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
               BETA            =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
               CHI             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
               DELTA           =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
         ),
         VERI_CHOC       =FACT(statut='f',min=01,max='**',
           STOP_CRITERE    =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           SEUIL           =SIMP(statut='f',typ='R',defaut= 0.5 ),
         ),
         FLAMBAGE        =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NOEUD_1','GROUP_NO_1'),
                   PRESENT_ABSENT('NOEUD_1','GROUP_NO_1'),
                   PRESENT_ABSENT('NOEUD_2','GROUP_NO_2'),),
           NOEUD_1         =SIMP(statut='f',typ=no),
           NOEUD_2         =SIMP(statut='f',typ=no),
           GROUP_NO_1      =SIMP(statut='f',typ=grno),
           GROUP_NO_2      =SIMP(statut='f',typ=grno),
           OBSTACLE        =SIMP(statut='o',typ=obstacle ),
           ORIG_OBST       =SIMP(statut='f',typ='R',max='**'),
           NORM_OBST       =SIMP(statut='o',typ='R',max='**'),
           ANGL_VRIL       =SIMP(statut='f',typ='R' ),
           JEU             =SIMP(statut='f',typ='R',defaut= 1. ),
           DIST_1          =SIMP(statut='f',typ='R' ),
           DIST_2          =SIMP(statut='f',typ='R' ),
           REPERE          =SIMP(statut='f',typ='TXM',defaut="GLOBAL"),
           RIGI_NOR        =SIMP(statut='f',typ='R' ),
           FNOR_CRIT       =SIMP(statut='f',typ='R' ),
           FNOR_POST_FL    =SIMP(statut='f',typ='R' ),
           RIGI_NOR_POST_FL=SIMP(statut='f',typ='R' ),
         ),
         ANTI_SISM       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NOEUD_1','GROUP_NO_1'),
                   UN_PARMI('NOEUD_2','GROUP_NO_2'),
                   PRESENT_ABSENT('NOEUD_1','GROUP_NO_1'),
                   PRESENT_ABSENT('NOEUD_2','GROUP_NO_2'),),
           NOEUD_1         =SIMP(statut='f',typ=no),
           NOEUD_2         =SIMP(statut='f',typ=no),
           GROUP_NO_1      =SIMP(statut='f',typ=grno),
           GROUP_NO_2      =SIMP(statut='f',typ=grno),
           RIGI_K1         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           RIGI_K2         =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           SEUIL_FX        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           C               =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           PUIS_ALPHA      =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           DX_MAX          =SIMP(statut='f',typ='R',defaut= 1. ),
         ),
         RELA_EFFO_DEPL  =FACT(statut='f',min=01,max='**',
           NOEUD           =SIMP(statut='o',typ=no),
           SOUS_STRUC      =SIMP(statut='f',typ='TXM' ),
           NOM_CMP         =SIMP(statut='f',typ='TXM' ),
           RELATION        =SIMP(statut='o',typ=fonction ),
         ),
         RELA_TRANSIS    =FACT(statut='f',min=01,max='**',
           NOEUD           =SIMP(statut='o',typ=no),
           SOUS_STRUC      =SIMP(statut='f',typ='TXM' ),
           NOM_CMP         =SIMP(statut='f',typ='TXM' ),
           RELATION        =SIMP(statut='o',typ=fonction ),
         ),
         RELA_EFFO_VITE  =FACT(statut='f',min=01,max='**',
           NOEUD           =SIMP(statut='o',typ=no),
           SOUS_STRUC      =SIMP(statut='f',typ='TXM' ),
           NOM_CMP         =SIMP(statut='f',typ='TXM' ),
           RELATION        =SIMP(statut='o',typ=fonction ),
         ),
         b_itmi          =BLOC(condition = "METHODE=='ITMI'",
                regles=(ENSEMBLE('BASE_ELAS_FLUI','NUME_VITE_FLUI'),),
                BASE_ELAS_FLUI  =SIMP(statut='f',typ=melasflu ),
                NUME_VITE_FLUI  =SIMP(statut='f',typ='I' ),
                ETAT_STAT       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
                PREC_DUREE      =SIMP(statut='f',typ='R',defaut= 1.E-2 ),
                CHOC_FLUI       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
                NB_MODE         =SIMP(statut='f',typ='I' ),
                NB_MODE_FLUI    =SIMP(statut='f',typ='I' ),
                NB_MODE_DIAG    =SIMP(statut='f',typ='I' ),
                TS_REG_ETAB     =SIMP(statut='f',typ='R' ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
         IMPRESSION      =FACT(statut='f',min=01,max='**',
           regles=(EXCLUS('TOUT','NIVEAU'),),
           TOUT            =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           NIVEAU          =SIMP(statut='f',typ='TXM',into=("DEPL_LOC","VITE_LOC","FORC_LOC","TAUX_CHOC") ),
           INST_INIT       =SIMP(statut='f',typ='R' ),
           INST_FIN        =SIMP(statut='f',typ='R' ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
 )  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
ENGENDRE_TEST=PROC(nom="ENGENDRE_TEST",op=178,docu="U4.92.11-b",
      regles=(UN_PARMI('TOUT','CO'),),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT"),
         TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         CO              =SIMP(statut='f',typ=assd,max='**'),
         TYPE_TEST       =SIMP(statut='f',typ='TXM',defaut="SOMME",into=("SOMME","RESUME") ),
         FORMAT_R        =SIMP(statut='f',typ='TXM',defaut="1PE12.5"),
         PREC_R          =SIMP(statut='f',typ='TXM',defaut="1.E-5"),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
EXEC_LOGICIEL=PROC(nom="EXEC_LOGICIEL",op= 183,fr="",docu="U7.00.01-a",
         LOGICIEL        =SIMP(statut='f',typ='TXM' ),  
         ARGUMENT        =FACT(statut='f',min=01,max='**',
           NOM_PARA        =SIMP(statut='f',typ='TXM' ),  
         ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
#def extr_mode_prod(FILTRE_MODE,TITRE,IMPRESSION ):
#  Sait-on faire  
def extr_mode_prod(FILTRE_MODE,**args):
  vale=FILTRE_MODE[0]['MODE']
  if AsType(vale) == mode_meca   : return mode_meca
  if AsType(vale) == mode_meca_c : return mode_meca_c
  if AsType(vale) == mode_gene   : return mode_gene
  raise AsException("type de concept resultat non prevu")

EXTR_MODE=OPER(nom="EXTR_MODE",op= 168,sd_prod=extr_mode_prod,
               docu="U4.52.12-c",reentrant='n',
         FILTRE_MODE     =FACT(statut='o',min=01,max='**',
           regles=(UN_PARMI('TOUT_ORDRE','NUME_ORDRE','NUME_MODE','NUME_MODE_EXCLU','FREQ_MIN','CRIT_EXTR',),),
           MODE            =SIMP(statut='o',typ=(mode_meca,mode_meca_c,mode_gene ) ),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI","NON") ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
           NUME_MODE_EXCLU =SIMP(statut='f',typ='I',max='**'),
           FREQ_MIN        =SIMP(statut='f',typ='R' ),
           CRIT_EXTR       =SIMP(statut='f',typ='TXM',defaut="MASS_EFFE_UN"
                                  ,into=("MASS_EFFE_UN","MASS_GENE") ),
           b_freq_min      =BLOC(condition = "FREQ_MIN != None",  
             FREQ_MAX        =SIMP(statut='o',typ='R' ),
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           ),
           b_crit_extr     =BLOC(condition = "CRIT_EXTR != None",
             SEUIL           =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           ),    
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         IMPRESSION      =FACT(statut='f',min=01,max=01,
           CUMUL           =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           CRIT_EXTR       =SIMP(statut='f',typ='TXM',defaut="MASS_EFFE_UN",into=("MASS_EFFE_UN","MASS_GENE") ),
         ),
)  ;
#& MODIF COMMANDE  DATE 23/01/2002   AUTEUR CIBHHAB N.RAHNI 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def extr_resu_prod(RESULTAT,**args):
  if AsType(RESULTAT) == evol_elas    : return evol_elas
  if AsType(RESULTAT) == evol_noli    : return evol_noli
  if AsType(RESULTAT) == evol_ther    : return evol_ther
  if AsType(RESULTAT) == dyna_trans   : return dyna_trans
  if AsType(RESULTAT) == dyna_harmo   : return dyna_harmo
  if AsType(RESULTAT) == acou_harmo   : return acou_harmo
  if AsType(RESULTAT) == mode_meca    : return mode_meca
  if AsType(RESULTAT) == mode_acou    : return mode_acou
  if AsType(RESULTAT) == mode_stat :    return mode_stat
  if AsType(mode_stat) == mode_stat_depl :    return mode_stat_depl
  if AsType(mode_stat) == mode_stat_acce :    return mode_stat_acce
  if AsType(mode_stat) == mode_stat_forc :    return mode_stat_forc
  if AsType(RESULTAT) == mult_elas    : return mult_elas
  if AsType(RESULTAT) == fourier_elas : return fourier_elas
  raise AsException("type de concept resultat non prevu")

EXTR_RESU=OPER(nom="EXTR_RESU",op=176,sd_prod=extr_resu_prod,docu="U4.71.04-b1",reentrant='f',
         RESULTAT        =SIMP(statut='o',typ=(evol_elas,dyna_trans,dyna_harmo,acou_harmo,mode_meca,          
                                               mode_acou,mode_stat_depl,mode_stat_acce,mode_stat_forc,evol_ther,evol_noli,   
                                               mult_elas,fourier_elas ) ),

         ARCHIVAGE       =FACT(statut='f',min=1,max=1,
           regles=(  UN_PARMI('NUME_ORDRE', 'INST', 'FREQ', 'NUME_MODE',
                        'NOEUD_CMP', 'LIST_INST', 'LIST_FREQ', 'LIST_ORDRE',
                        'NOM_CAS', 'LIST_ARCH', 'PAS_ARCH' ),
                     EXCLUS( 'CHAM_EXCLU','NOM_CHAM' ),   ),
           CHAM_EXCLU      =SIMP(statut='f',typ='TXM',max='**'),
           NOM_CHAM        =SIMP(statut='f',typ='TXM',max='**'),
           PRECISION       =SIMP(statut='f',typ='R',defaut=1.E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',into=("RELATIF","ABSOLU"),defaut="RELATIF"),
           LIST_ARCH       =SIMP(statut='f',typ=listis),
           PAS_ARCH        =SIMP(statut='f',typ='I'),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           LIST_ORDRE      =SIMP(statut='f',typ=listis),
           INST            =SIMP(statut='f',typ='R',max='**'),
           LIST_INST       =SIMP(statut='f',typ=listr8),
           FREQ            =SIMP(statut='f',typ='R',max='**'),
           LIST_FREQ       =SIMP(statut='f',typ=listr8),
           NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
           NOEUD_CMP       =SIMP(statut='f',typ='TXM',max='**'),
           NOM_CAS         =SIMP(statut='f',typ='TXM'),
                               ),

         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def fact_grad_prod(MATR_ASSE,**args):
  if AsType(MATR_ASSE) == matr_asse_depl_r : return matr_asse_depl_r
  if AsType(MATR_ASSE) == matr_asse_temp_r : return matr_asse_temp_r
  if AsType(MATR_ASSE) == matr_asse_pres_r : return matr_asse_pres_r
  raise AsException("type de concept resultat non prevu")

FACT_GRAD=OPER(nom="FACT_GRAD",op=85,sd_prod=fact_grad_prod,docu="U4.55.03-e",
               fr="Pr�conditionnement pour r�solution par gradient conjugu�",
               reentrant='n',
         MATR_ASSE       =SIMP(statut='o',
                               typ=(matr_asse_depl_r,matr_asse_temp_r,
                                    matr_asse_pres_r) ),
         PRE_COND        =SIMP(statut='f',typ='TXM',defaut="LDLT_INC",into=("LDLT_INC",) ),
         NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),  
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
FACT_INTE_SPEC=OPER(nom="FACT_INTE_SPEC",op= 117,sd_prod=interspfact,
                    fr="Factorisation d une matrice interspectrale hermitienne",
                    docu="U4.36.04-e",reentrant='n',
         regles=(ENSEMBLE('FREQ_FIN','NB_POIN'),),
#  regle non indiqu�e dans la doc U         
         INTE_SPEC       =SIMP(statut='o',typ=tabl_intsp ),
         NUME_VITE_FLUI  =SIMP(statut='f',typ='I' ),
         FREQ_INIT       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         FREQ_FIN        =SIMP(statut='f',typ='R' ),
         NB_POIN         =SIMP(statut='f',typ='I',defaut= 0 ),
         SUR_ECHAN       =SIMP(statut='f',typ='R',defaut= 1. ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def fact_ldlt_prod(MATR_ASSE,**args):
  if AsType(MATR_ASSE) == matr_asse_depl_r : return matr_asse_depl_r
  if AsType(MATR_ASSE) == matr_asse_depl_c : return matr_asse_depl_c
  if AsType(MATR_ASSE) == matr_asse_temp_r : return matr_asse_temp_r
  if AsType(MATR_ASSE) == matr_asse_temp_c : return matr_asse_temp_c
  if AsType(MATR_ASSE) == matr_asse_pres_r : return matr_asse_pres_r
  if AsType(MATR_ASSE) == matr_asse_pres_c : return matr_asse_pres_c
  raise AsException("type de concept resultat non prevu")

FACT_LDLT=OPER(nom="FACT_LDLT",op=14,sd_prod=fact_ldlt_prod,fr="Factorisation en place ou hors place",
               docu="U4.55.01-f",reentrant='f',
         regles=(EXCLUS('BLOC_DEBUT','DDL_DEBUT'),
                 EXCLUS('BLOC_FIN','DDL_FIN'),),
         MATR_ASSE       =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_depl_c,matr_asse_temp_r,
                                               matr_asse_temp_c,matr_asse_pres_r,matr_asse_pres_c) ),
         STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         NPREC           =SIMP(statut='f',typ='I',defaut=8,val_min=0,),
         PRE_COND        =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SANS","DIAG") ),
         BLOC_DEBUT      =SIMP(statut='f',typ='I',val_min=1,),
         DDL_DEBUT       =SIMP(statut='f',typ='I',val_min=1,),
         BLOC_FIN        =SIMP(statut='f',typ='I',val_min=1,),
         DDL_FIN         =SIMP(statut='f',typ='I',val_min=1,),
#
         EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
#
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# NEW 5.3.23
FERMER=PROC(nom="FERMER",op=  10,fr=" ",
            docu="U4.12.02-a",
         UNITE           =SIMP(statut='o',typ='I',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
FIN=PROC(nom="FIN",op=9999,repetable='n',fr="Fin d'une �tude",
         docu="U4.11.02-f",
         RETASSAGE       =SIMP(fr="provoque le retassage de la base GLOBALE",
                               statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
         PERFORMANCE     =SIMP(fr="provoque l'impression d'un r�sum� des mesures de temps ",
                               statut='f',typ='TXM',defaut="OUI",into=("OUI","NON",) ),
         INFO_RESU       =SIMP(fr="provoque l'impression des informations sur les structures de donn�es",
                               statut='f',typ='TXM',defaut="OUI",into=("OUI","NON",) ),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="MESSAGE"),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
FONC_FLUI_STRU=OPER(nom="FONC_FLUI_STRU",op= 169,sd_prod=fonction,
                    docu="U4.35.02-c",reentrant='n',
         TYPE_FLUI_STRU  =SIMP(statut='o',typ=(type_flui_stru) ),
)  ;
#& MODIF COMMANDE  DATE 17/09/2001   AUTEUR MCOURTOI M.COURTOIS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
FORMULE = FORM( nom='FORMULE',op=-5,sd_prod=fonction,
                fr="D�finition d une fonction",reentrant = 'n',
                regles=(UN_PARMI('REEL','ENTIER','COMPLEXE'),),
                REEL = SIMP(typ = 'shell',max=1),
                ENTIER = SIMP(typ = 'shell',max=1),
                COMPLEXE = SIMP(typ = 'shell',max=1),
) ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
GENE_FONC_ALEA=OPER(nom="GENE_FONC_ALEA",op= 118,sd_prod=tabl_fonc,
                    fr="G�n�ration de la fonction temporelle � partir d une matrice interspectrale factoris�e",
                    docu="U4.36.05-e",reentrant='n',
         INTE_SPEC_FACT  =SIMP(statut='o',typ=interspfact ),
         INIT_ALEA       =SIMP(statut='f',typ='I',defaut= 12312745 ),
         NB_TIRAGE       =SIMP(statut='f',typ='I',defaut= 1 ),
         NB_POIN         =SIMP(statut='f',typ='I' ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
IMPR_CHARGE=PROC(nom="IMPR_CHARGE",op= 158,
                 fr="Impression des charges m�caniques de type ddl impos�s et relations lin�aires entre les ddl",
                 docu="U7.04.31-c",
         FICHIER         =SIMP(statut='f',typ='TXM' ),
         FORMAT          =SIMP(statut='f',typ='TXM',defaut="IDEAS",into=("IDEAS",) ),
         VERSION         =SIMP(statut='f',typ='I',defaut= 5,into=( 5 ,) ),
         CHARGE          =SIMP(statut='o',typ=char_meca,max='**', ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
IMPR_CLASSI=PROC(nom="IMPR_CLASSI",op= 114,docu="U7.04.21-a",
         regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','FREQ','NUME_MODE','LIST_FREQ',
                        'LIST_ORDRE' ),),
         UNITE_CLASSI    =SIMP(statut='o',typ='I' ),
         MODE_MECA       =SIMP(statut='o',typ=mode_meca ),
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
         LIST_ORDRE      =SIMP(statut='f',typ=listis ),
         NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
         FREQ            =SIMP(statut='f',typ='R',max='**'),
         LIST_FREQ       =SIMP(statut='f',typ=listr8 ),
         b_prec_crit     =BLOC(condition = "LIST_FREQ != None or FREQ != None",
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",
                                   into=("RELATIF","ABSOLU") ),
         ),
         IMPRESSION      =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NOEUD','GROUP_NO', ),),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOM_CMP         =SIMP(statut='f',typ='TXM',max='**'),
         ),
         AMOR            =SIMP(statut='o',typ='R',max='**'),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
IMPR_CO=PROC(nom="IMPR_CO",op=17,docu="U4.91.11-f",
             fr="Impression du contenu d un concept utilisateur (pour d�veloppeur)",
         regles=(UN_PARMI('CO','CHAINE', ),),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT"),
         NIVEAU          =SIMP(statut='f',typ='I',defaut=2,into=(0,1,2) ),
         ATTRIBUT        =SIMP(statut='f',typ='TXM',defaut="NON",into=("NON","OUI") ),
         CONTENU         =SIMP(statut='f',typ='TXM',defaut="OUI",into=("NON","OUI") ),
         BASE            =SIMP(statut='f',typ='TXM',defaut="G",into=("","G","V","L") ),
         CO              =SIMP(statut='f',typ=assd,max='**'),
         CHAINE          =SIMP(statut='f',typ='TXM'),
         POSITION        =SIMP(statut='f',typ='I',defaut=1),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE MCOURTOI M.COURTOIS
IMPR_COURBE=PROC(nom="IMPR_COURBE",op= 141,fr="Impression, sur fichiers",
                 docu="U4.33.01-d1",
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT"),
         FORMAT          =SIMP(statut='f',typ='TXM',position='global'
                              ,into=("AGRAF","EXCEL","POSTSCRIPT","RESULTAT","COMMANDE","SEISME") ),
         b_agraf_post =BLOC(condition = "(FORMAT=='AGRAF') or (FORMAT=='POSTSCRIPT')",fr="Mots-cl�s communs AGRAF et POSTCRIPT",
           BORNE_X         =SIMP(statut='f',typ='R',min=2,max=2,fr="Intervalles de variation des abcisses"),
           ECHELLE_X       =SIMP(statut='f',typ='TXM',defaut="LIN",into=("LIN","LOG"),fr="Type d'�chelle pour les abcisses" ),
           BORNE_Y         =SIMP(statut='f',typ='R',min=2,max=2,fr="Intervalles de variation des ordonn�es"),
           ECHELLE_Y       =SIMP(statut='f',typ='TXM',defaut="LIN",into=("LIN","LOG"),fr="Type d'�chelle pour les ordonn�es" ),
         ),
         b_agraf =BLOC(condition = "(FORMAT=='AGRAF')",fr="Mots-cl�s propres � AGRAF",
           TITRE_GRAPHIQUE =SIMP(statut='f',typ='TXM',fr="Titre associ� au graphique" ),
           COMMENTAIRE     =SIMP(statut='f',typ='TXM',max='**',fr="Commentaires associ�s au graphique"),
           LEGENDE_X       =SIMP(statut='f',typ='TXM',fr="L�gende associ�e � l axe des abcisses" ),
           LEGENDE_Y       =SIMP(statut='f',typ='TXM',fr="L�gende associ�e � l axe des ordonn�es" ),
           FREQ_GRILLE_X   =SIMP(statut='f',typ='I',defaut= 0,fr="Fr�quence de tracage du quadrillage vertical" ),
           FREQ_GRILLE_Y   =SIMP(statut='f',typ='I',defaut= 0,fr="Fr�quence de tracage du quadrillage horizontal" ),
         ), 
         b_excel = BLOC(condition = "(FORMAT=='EXCEL')",fr="Mots-cl�s propres au format Excel",
           BORNE_X         =SIMP(statut='f',typ='R',min=2,max=2,fr="Intervalles de variation des abcisses"),
           BORNE_Y         =SIMP(statut='f',typ='R',min=2,max=2,fr="Intervalles de variation des ordonn�es"),
         ),
         b_post = BLOC (  condition = "(FORMAT=='POSTSCRIPT')",fr="Mots-cl�s propres � POSTCRIPT",
           TITRE           =SIMP(statut='f',typ='TXM',fr="Titre associ� au graphique" ),
           LABEL_X         =SIMP(statut='f',typ='TXM',fr="L�gende associ�e � l axe des abcisses" ),
           LABEL_Y         =SIMP(statut='f',typ='TXM',fr="L�gende associ�e � l axe des ordonn�es" ),
           SORTIE          =SIMP(statut='f',typ='TXM',defaut="COULEUR",into=("MONOCHROME","COULEUR"),fr="Type d impression" ),
           DATE            =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON"),fr="Impression de la date" ),
           GRILLE          =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON"),fr="Impression du quadrillage" ),
           AXE_ZERO_X      =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON"),fr="Impression de l axe x �gal z�ro" ),
           AXE_ZERO_Y      =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON"),fr="Impression de l axe y �gal z�ro" ),
           PRESENTATION    =SIMP(statut='f',typ='TXM',defaut="PAYSAGE",into=("PAYSAGE","PORTRAIT"),
                                 fr="Disposition du graphique sur la feuille" ),
           FENETRE         =SIMP(statut='f',typ='TXM',defaut="RECTANGLE",into=("CARREE","RECTANGLE"),
                                 fr="Forme de la fenetre contenant le graphique" ),
         ),  
         COURBE          =FACT(statut='o',min=01,max='**',fr="D�finition de la courbe � tracer",
           regles=(UN_PARMI('FONCTION','LIST_RESU','TABLE','FONC_X','RESU_GENE'),),
           FONCTION        =SIMP(statut='f',typ=(fonction, fonction_c),
                                 fr="Fonction r�elle ou complexe", ),
           LIST_RESU       =SIMP(statut='f',typ=listr8,
                                 fr="Liste des ordonnees d une fonction r�elle d�finie par deux listes", ),
#  creer le type table            
           TABLE           =SIMP(statut='f',typ=table,
                                 fr="Nom de la table dont 2 colonnes d�finissent la fonction",),
           FONC_X          =SIMP(statut='f',typ=fonction,
                                 fr="Fonction abscisses d une fonction param�trique",),
           RESU_GENE       =SIMP(statut='f',typ=tran_gene, ), 
           b_fonction      =BLOC(condition = "FONCTION != None",                          
             LIST_PARA       =SIMP(statut='f',typ=listr8 ),
           ),   
           b_fonction_c  =BLOC(condition = "AsType(FONCTION) == fonction_c",
                                 fr="Fonction complexe d�finie par le mot-cl� fonction",
             PARTIE          =SIMP(statut='f',typ='TXM',into=("REEL","IMAG") ),           
           ),
           b_list_resu     =BLOC(condition = "LIST_RESU != None",                                
             LIST_PARA       =SIMP(statut='o',typ=listr8 ),
           ),  
           b_table         =BLOC(condition = "TABLE != None",                                         
             PARA_X          =SIMP(statut='o',typ='TXM',
                                   fr="Param�tre de la table associ� aux abcisses de la fonction � tracer" ),
             PARA_Y          =SIMP(statut='o',typ='TXM',
                                   fr="Param�tre de la table associ� aux ordonn�es de la fonction � tracer" ),        
           ), 
           b_fonc_x        =BLOC(condition = "FONC_X != None",                                          
             FONC_Y          =SIMP(statut='o',typ=fonction,fr="Fonction ordonn�es d une fonction param�trique" ),
             PARA            =SIMP(statut='f',typ='TXM',defaut="FONC_X",into=("FONC_X","FONC_Y"),
                                   fr="Permutation des roles des deux fonctions" ),
             LIST_PARA       =SIMP(statut='f',typ=listr8 ),                
           ),
           b_resu_gene     =BLOC(condition = "RESU_GENE != None",                                
             regles=(UN_PARMI('NOEUD_CHOC','GROUP_NO_CHOC'),),                      
             NOEUD_CHOC      =SIMP(statut='f',typ=no),
             GROUP_NO_CHOC   =SIMP(statut='f',typ=grno),
             PARA_X          =SIMP(statut='o',typ='TXM'),
             PARA_Y          =SIMP(statut='o',typ='TXM'),
             LIST_PARA       =SIMP(statut='f',typ=listr8 ),   
             SOUS_STRUC      =SIMP(statut='f',typ='TXM' ),
             INTITULE        =SIMP(statut='f',typ='TXM' ),               
           ), 
                 
               
           LEGENDE         =SIMP(statut='f',typ='TXM',fr="L�gende associ�e � la courbe" ),
           STYLE           =SIMP(statut='f',typ='TXM',defaut="LIGNE",fr="Style de la ligne repr�sentant la courbe",
                                 into=("LIGNE","POINTILLE","POINT","POINT_RELIE") ),
           COULEUR         =SIMP(statut='f',typ='TXM',fr="Couleur associ�e � la courbe",
                                 into=("NOIR","ROUGE","VERT_FONCE","BLEU",
                                       "MAGENTA","CYAN","VERT","SIENNE","ORANGE",
                                       "POURPRE","JAUNE","DAIM","TURQUOISE","VIOLET",
                                       "BRUN","CORAIL","MARRON","MAUVE","MARRON_CLAIR") ),
           MARQUEUR        =SIMP(statut='f',typ='TXM',fr="Type du marqueur associ� � la courbe",
                                 into=("POINT_F","CARRE_F","TRIANGLE_F",
                                       "LOSANGE_F","ETOILE_F","FUSEE_F","POINT",
                                       "CARRE","TRIANGLE","LOSANGE","ETOILE","FUSEE",
                                       "PLUS","X","CERCLE","CERCLE_P","CARRE_P",
                                       "LOSANGE_P","CERCLE_P_X","LOSANGE_P_X",
                                       "CERCLE_X","CARRE_X","LOSANGE_X") ),
            b_agraf =BLOC(condition = "(FORMAT=='AGRAF')",fr="Mots-cl�s propres � AGRAF",
              TRI             =SIMP(statut='f',typ='TXM',defaut="N",
                                    fr="Choix du tri effectu� sur les abcisses ou sur les ordonn�es",
                                    into=("N","X","Y","XY","YX") ),
              FREQ_MARQUEUR   =SIMP(statut='f',typ='I',defaut= 0,
                                    fr="Fr�quence d impression du marqueur associ� � la courbe", ),          
            ), 
         ),
)  ;
#& MODIF COMMANDE  DATE 25/01/2002   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE GNICOLAS G.NICOLAS
IMPR_FICO_HOMA=PROC(nom="IMPR_FICO_HOMA",op= 189, docu="U7.04.01-a",
                    fr="Imprime le fichier de configuration de HOMARD.",
                    ang="Writes the configuration file for HOMARD.",
#
# 1. Le niveau d'information
#
         INFO           = SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
#
# 2. LE REPERTOIRE OU AURA LIEU LE CALCUL HOMARD
#
         REP             =SIMP(statut='f',typ='TXM'),  
#
# 3. Langue des messages issus de HOMARD
#
         LANGUE = SIMP(statut='f',typ='TXM',defaut="FRANCAIS",    
                               into=("FRANCAIS","FRENCH","ANGLAIS","ENGLISH",),
                           fr="Langue des messages issus de HOMARD.",
                           ang="Language for HOMARD messages." ),
#
# 4. L'UNITE LOGIQUE D'ECRITURE DU FICHIER DE CONFIGURATION HOMARD
#
         UNITE           =SIMP(statut='f',typ='I',defaut= 71 ),  
#
# 5. LE TYPE DE TRAITEMENT :
#
         TRAITEMENT      =FACT(statut='o',min=01,max=01,
#
# 5.1. QUATRE CHOIX EXCLUSIFS :
#
# 5.1.1.
#      A. ADAPTATION PAR UN INDICATEUR D'ERREUR, AVEC TROIS VARIANTES :
#         . RAFFINEMENT ET DERAFFINEMENT
#         . RAFFINEMENT SEUL
#         . DERAFFINEMENT SEUL
#      B. ADAPTATION UNIFORME, AVEC DEUX VARIANTES :
#         . RAFFINEMENT SEUL
#         . DERAFFINEMENT SEUL
#         . RIEN : LE MAILLAGE EST LE MEME A LA SORTIE ET A L'ENTREE
#      C. INFORMATION SUR UN MAILLAGE
#      D. MISE A JOUR DE SOLUTIONS
#
           regles=( UN_PARMI('ADAPTATION','UNIFORME','INFORMATION','MAJSOLUTION'),),
           ADAPTATION      =SIMP(statut='f',typ='TXM',     
                                 fr="Adaptation libre",
                                 ang="Free adaptation",
                                 into=("RAFFINEMENT","DERAFFINEMENT","RAFF_DERA") ),
           UNIFORME        =SIMP(statut='f',typ='TXM',     
                                 fr="Adaptation uniforme",
                                 ang="Uniforme adaptation",
                                 into=("RAFFINEMENT","DERAFFINEMENT","RIEN") ),
           INFORMATION     =SIMP(statut='f',typ='TXM',
                                 fr="Adaptation libre",
                                 ang="Free adaptation",
                                 into=("OUI",) ),
           MAJSOLUTION     =SIMP(statut='f',typ='TXM',
                                 fr="Mise � jour de solutions",
                                 ang="Solution updating",
                                 into=("OUI",) ),
#
# 5.1.2. LES CONTRAINTES :
#
# 5.1.2.1. POUR DE L'ADAPTATION LIBRE, IL FAUT :
#      A. LE NUMERO D'ITERATION DU MAILLAGE DE DEPART
#      B. LE NOM MED DU MAILLAGE D'ENTREE
#      C. LE NOM MED DE L'INDICATEUR D'ERREUR
#      D. LE NUMERO D'ITERATION DU MAILLAGE DE DEPART
#      E. LA MISE A JOUR DE SOLUTION
#      F. LE NOM MED DU MAILLAGE DE SORTIE
#      REMARQUE : IL FAUT DES CRITERES, MAIS ON NE SAIT PAS LESQUELS
#
# 5.1.2.2. POUR DE L'ADAPTATION UNIFORME
#          IL FAUT :
#      A. LE NUMERO D'ITERATION DU MAILLAGE DE DEPART
#      B. LE NOM MED DU MAILLAGE DE SORTIE
#          IL NE FAUT PAS :
#      A. LE NOM MED DE L'INDICATEUR D'ERREUR
#      B. LE NOM DE LA COMPOSANTE DE L'INDICATEUR D'ERREUR
#      C. LES CRITERES
#      REMARQUE : A L'ITERATION 0, OU AUX ITERATIONS SUIVANTES SI MAJ DE SOLUTION,
#                 IL FAUT LE NOM MED DU MAILLAGE D'ENTREE
#
# 5.1.2.3. POUR DE LA MISE A JOUR DE SOLUTION :
#          IL FAUT :
#      A. LE NUMERO D'ITERATION DU MAILLAGE DE DEPART
#      B. LE NOM MED DU MAILLAGE D'ENTREE
#          IL NE FAUT PAS :
#      A. LE NOM MED DE L'INDICATEUR D'ERREUR
#      B. LE NOM DE LA COMPOSANTE DE L'INDICATEUR D'ERREUR
#      C. LES CRITERES
#
#
# 5.1.2.4. POUR DE L'INFORMATION :
#          IL FAUT :
#      A. LE NOM MED DU MAILLAGE D'ENTREE
#          IL NE FAUT PAS :
#      A. LE NOM MED DE L'INDICATEUR D'ERREUR
#      B. LE NOM DE LA COMPOSANTE DE L'INDICATEUR D'ERREUR
#      C. LES CRITERES
#      D. LE NUMERO D'ITERATION DU MAILLAGE DE DEPART
#      E. LA MISE A JOUR DE SOLUTION
#
           b_maillage_initial =BLOC(condition = "( INFORMATION != None ) or ( ADAPTATION != None ) or "+
                                                   "( MAJSOLUTION != None ) ",
                           fr="Nom MED du maillage en entr�e",
                           ang="MED name of the in-mesh",
                           NOM_MED_MAILLAGE_N   =SIMP(statut='o',typ='TXM',),
                           ) ,
#
           b_maillage_initial_uniforme =BLOC(condition = "( UNIFORME != None ) ",
                           fr="Nom MED du maillage en entr�e",
                           ang="MED name of the in-mesh",
                           NOM_MED_MAILLAGE_N   =SIMP(statut='f',typ='TXM',),
                           ) ,
#
           b_iteration_maj_champ =BLOC(condition = "( UNIFORME != None ) or ( ADAPTATION != None ) or "+
                                                   "( MAJSOLUTION != None ) ",
                           fr="Nom MED du maillage en sortie, numero d'iteration et mise � jour de champs",
                           ang="MED name of the out-mesh, iteration rank and field updating",
                           NITER                =SIMP(statut='o',typ='I',
                           fr="Num�ro d'it�ration.",
                           ang="Iteration #." ),
                           NOM_MED_MAILLAGE_NP1 =SIMP(statut='o',typ='TXM'),
                           MAJ_CHAM             =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
                           ) ,
#
           b_indicateur_d_erreur  =BLOC(condition = "ADAPTATION != None",
                           fr="Indicateur d'erreur",
                           ang="Error indicator",
                           NOM_MED_INDICA  =SIMP(statut='o',typ='TXM',
                           fr="Nom MED de l'indicateur d'erreur.",
                           ang="MED name of error indicator.",),
                           NOM_CMP_INDICA  =SIMP(statut='o',typ='TXM',
                           fr="Nom de la composante de l'indicateur d'erreur retenue.",
                           ang="Name of the selected component of the error indicator.",),
                           NUMDT_INDICA  =SIMP(statut='o',typ='I',
                           fr="Numero du pas de temps de l'indicateur.",
                           ang="Time step # of the error indicator.",),
                           NUMORD_INDICA  =SIMP(statut='o',typ='I',
                           fr="Numero d'ordre de l'indicateur.",
                           ang="Rank # of the error indicator.",),
                           ) ,
#
           b_critere_de_raffinement =BLOC( condition = "( ADAPTATION == 'RAFF_DERA' ) or ( ADAPTATION == 'RAFFINEMENT' )" ,
                           fr="Crit�re de raffinement.",
                           ang="Refinement threshold.",
                           regles=(UN_PARMI ( 'CRIT_RAFF_ABS', 'CRIT_RAFF_REL', 'CRIT_RAFF_PE' ),),
                           CRIT_RAFF_ABS   =SIMP(statut='f',typ='R',
                                                 fr="Crit�re absolu",
                                                 ang="Absolute threshold"  ),
                           CRIT_RAFF_REL   =SIMP(statut='f',typ='R',
                                                 fr="Crit�re relatif",
                                                 ang="Relative threshold" ),
                           CRIT_RAFF_PE    =SIMP(statut='f',typ='R',
                                                 fr="Pourcentage d'�l�ments",
                                                 ang="Percentage of elements" ),
                           ) ,
#
           b_critere_de_deraffinement =BLOC ( condition = "( ADAPTATION == 'RAFF_DERA' ) or ( ADAPTATION == 'DERAFFINEMENT' )" ,
                           fr="Crit�re de d�raffinement.",
                           ang="Unrefinement threshold.",
                           regles=(UN_PARMI ( 'CRIT_DERA_ABS', 'CRIT_DERA_REL', 'CRIT_DERA_PE' ),),
                           CRIT_DERA_ABS   =SIMP(statut='f',typ='R' ,
                                                 fr="Crit�re absolu",
                                                 ang="Absolute threshold" ),
                           CRIT_DERA_REL   =SIMP(statut='f',typ='R',
                                                 fr="Crit�re relatif",
                                                 ang="Relative threshold" ),
                           CRIT_DERA_PE    =SIMP(statut='f',typ='R',
                                                 fr="Pourcentage d'�l�ments",
                                                 ang="Percentage of elements" ),
                           ) ,
#
           b_niveau_maximum =BLOC ( condition = " ( ADAPTATION == 'RAFF_DERA' ) or ( ADAPTATION == 'RAFFINEMENT' ) or "+
                                                " ( UNIFORME == 'RAFFINEMENT' )" ,
                             fr="Niveau maximum de profondeur de raffinement",
                             ang="Maximum level for refinement",
                             NIVE_MAX        =SIMP(statut='f',typ='I' ),
                           ) ,
#
           b_niveau_minimum =BLOC ( condition = " ( ADAPTATION == 'RAFF_DERA' ) or ( ADAPTATION == 'DERAFFINEMENT' ) or"+
                                                " ( UNIFORME == 'DERAFFINEMENT' )" ,
                             fr="Niveau minimum de d�raffinement",
                             ang="Minimum level for unrefinement",
                             NIVE_MIN        =SIMP(statut='f',typ='I' ),
                           ) ,
#
         ),
#
# 6. L'ANALYSE DU MAILLAGE
#
         ANALYSE         =FACT(statut='f',min=01,max=01,
                               fr="Analyse du maillage.",
                               ang="Mesh analysis.",
#
# 6.1. CHOIX NON EXCLUSIFS, AVEC DEUX VARIANTES (OUI/NON) :
#    A. NOMBRE DES ELEMENTS
#    B. QUALITE DES ELEMENTS
#    C. INTERPENETRATION DES ELEMENTS
#    D. CONNEXITE DU MAILLAGE
#    E. TAILLE DES DIFFERENTS SOUS-DOMAINES
#
           regles=(AU_MOINS_UN('NOMBRE','QUALITE','INTERPENETRATION','CONNEXITE','TAILLE'),),
#
         NOMBRE          =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON"),
                          fr="Nombre de noeuds et �l�ments du maillage",
                          ang="Number of nodes and elements in the mesh" ),
#
         QUALITE         =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Qualit� du maillage",
                          ang="Mesh quality" ),
#
         INTERPENETRATION=SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Controle de la non interp�n�tration des �l�ments.",
                          ang="Overlapping checking." ),
#
         CONNEXITE       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Connexit� du maillage.",
                          ang="Mesh connexity." ),
#
         TAILLE          =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Tailles des sous-domaines du maillage.",
                          ang="Sizes of mesh sub-domains." ),
#
         ),
#
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
IMPR_GENE=PROC(nom="IMPR_GENE",op= 157,
               fr="Calcul du dommage subi par une structure soumise � une sollicitation de type al�atoire",
               docu="U4.91.02-c",
         GENE            =FACT(statut='o',min=01,max='**',
           regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','FREQ','NUME_MODE',
                          'LIST_INST','LIST_FREQ','TOUT_MODE','TOUT_INST','LIST_ORDRE'),
                   EXCLUS('TOUT_MODE','NUME_ORDRE','INST','FREQ','NUME_MODE',
                          'LIST_INST','LIST_FREQ','TOUT_ORDRE','TOUT_INST','LIST_ORDRE'),
                   EXCLUS('TOUT_INST','NUME_ORDRE','INST','FREQ','NUME_MODE',
                          'LIST_INST','LIST_FREQ','TOUT_ORDRE','LIST_ORDRE'),
                   EXCLUS('TOUT_CMP_GENE','NUME_CMP_GENE'),
                   EXCLUS('TOUT_CHAM','NOM_CHAM'),
                   EXCLUS('TOUT_PARA','NOM_PARA'),),
#  faut-il faire des blocs selon le type de RESU_GENE                   
           RESU_GENE       =SIMP(statut='o',typ=(vect_asse_gene, tran_gene, mode_gene, harm_gene)),
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="RESULTAT",into=("RESULTAT",) ),
           FICHIER         =SIMP(statut='f',typ='TXM' ),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           LIST_ORDRE      =SIMP(statut='f',typ=listis ),
           TOUT_MODE       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
           INST            =SIMP(statut='f',typ='R',max='**'),
           LIST_INST       =SIMP(statut='f',typ=listr8 ),
           TOUT_INST       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           FREQ            =SIMP(statut='f',typ='R',max='**'),
           LIST_FREQ       =SIMP(statut='f',typ=listr8 ),
           b_prec_crit     =BLOC(condition = "LIST_FREQ != None or FREQ != None",
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",
                                   into=("RELATIF","ABSOLU") ),
           ),
           TOUT_CMP_GENE   =SIMP(statut='f',typ='TXM',into=("OUI","NON") ),
           NUME_CMP_GENE   =SIMP(statut='f',typ='I',max='**'),
           TOUT_CHAM       =SIMP(statut='f',typ='TXM',into=("OUI","NON") ),
           NOM_CHAM        =SIMP(statut='f',typ='TXM',max='**'),
           TOUT_PARA       =SIMP(statut='f',typ='TXM',into=("OUI","NON") ),
           NOM_PARA        =SIMP(statut='f',typ='TXM',max='**'),
           SOUS_TITRE      =SIMP(statut='f',typ='TXM',max='**'),
           INFO_CMP_GENE   =SIMP(statut='f',typ='TXM',into=("OUI","NON") ),
           INFO_GENE       =SIMP(statut='f',typ='TXM',into=("OUI","NON") ),
         ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
IMPR_JEVEUX=PROC(nom="IMPR_JEVEUX",op=16,docu="U4.91.21-f",
                 fr="Impression de caract�ristiques d'objets JEVEUX (pour d�veloppeur)",
         ENTITE          =SIMP(fr="choix de l'observation",statut='o',typ='TXM',
                               into=("DISQUE","MEMOIRE","REPERTOIRE",    
                                     "OBJET","ATTRIBUT","SYSTEME") ),
         b_objet      =BLOC(condition = "(ENTITE=='OBJET')",
            NOMOBJ          =SIMP(fr="nom d'objet",statut='f',typ='TXM' ),  
            NUMOC           =SIMP(fr="num�ro d objet de collection",statut='f',typ='I' ),  
            NOMOC           =SIMP(fr="nom d'objet de collection",statut='f',typ='TXM' ),  
         ),
         b_attribut   =BLOC(condition = "(ENTITE=='ATTRIBUT')",
            NOMOBJ          =SIMP(fr="nom de collection",statut='f',typ='TXM' ),  
            NOMATR          =SIMP(fr="nom d attribut de collection",statut='f',typ='TXM',
                                  into=('$$DESO','$$IADD','$$IADM','$$NOM','$$LONG',
                                      '$$LONO','$$LUTI','$$NUM') ),
         ),
         b_systeme    =BLOC(condition = "(ENTITE=='SYSTEME')",
            CLASSE          =SIMP(statut='o',typ='TXM',into=('G','V','L') ),  
            NOMATR          =SIMP(fr="nom d attribut systeme",statut='f',typ='TXM',   
                                  into=('$$CARA','$$IADD','$$GENR','$$TYPE','$$ETAT',
                                      '$$DOCU','$$ORIG','$$RNOM','$$LTYP','$$LONG',
                                      '$$LONO','$$DATE','$$LUTI','$$HCOD','$$INDX',
                                      '$$TLEC','$$TECR','$$IADM','$$ACCE') ),
         ),
         b_repertoire =BLOC(condition = "(ENTITE=='REPERTOIRE')",
            CLASSE          =SIMP(statut='f',typ='TXM',into=('G','V','L',' '),defaut=' '),  
         ),
         b_disque     =BLOC(condition = "(ENTITE=='DISQUE')",
            CLASSE          =SIMP(statut='f',typ='TXM' ,into=('G','V','L',' '),defaut=' '),  
         ),
         IMPRESSION      =FACT(statut='f',min=01,max=01,
           NOM             =SIMP(statut='f',typ='TXM' ),  
           UNITE           =SIMP(statut='f',typ='I'),  
         ),
         COMMENTAIRE     =SIMP(statut='f',typ='TXM' ),  
)  ;
#& MODIF COMMANDE  DATE 19/12/2001   AUTEUR CIBHHPD D.NUNEZ 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
IMPR_MACR_ELEM=PROC(nom="IMPR_MACR_ELEM",op= 160,
                    docu="U7.04.33-c",
         MACR_ELEM_DYNA  =SIMP(statut='o',typ=macr_elem_dyna ),
         FICHIER         =SIMP(statut='f',typ='TXM' ),
         FORMAT          =SIMP(statut='f',typ='TXM',defaut="IDEAS",
                               into=("MISS_3D","IDEAS","CADYRO","PLEXUS") ),
         b_ideas         =BLOC(condition = "FORMAT == 'PLEXUS'",
           VERSION         =SIMP(statut='f',typ='I',defaut= 5,into=( 5 ,) ),
         ),                      
         b_plexus         =BLOC(condition = "FORMAT == 'IDEAS'",
           VERSION          =SIMP(statut='f',typ='I',defaut= 5,into=( 5 ,) ),
         ),             
         b_miss_3d       =BLOC(condition = "FORMAT == 'MISS_3D'",
           UNITE           =SIMP(statut='f',typ='I',defaut= 26 ),
           SOUS_TITRE      =SIMP(statut='f',typ='TXM',max='**'),
           AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),
           GROUP_MA_INTERF =SIMP(statut='o',typ=grma,max='**'),
#  Ces trois mots cles sont-ils dans le bon bloc et avec le bon statut        
           GROUP_MA_FLU_STR=SIMP(statut='f',typ=grma,max='**'),
           GROUP_MA_FLU_SOL=SIMP(statut='f',typ=grma,max='**'),
           GROUP_MA_SOL_SOL=SIMP(statut='f',typ=grma,max='**'),
           IMPR_MODE_MECA  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           IMPR_MODE_STAT  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         ),
         b_cadyro        =BLOC(condition = "FORMAT == 'CADYRO'",
           SQUELETTE       =SIMP(statut='f',typ=squelette ),
           UNITE_MODE_MECA =SIMP(statut='f',typ='I',defaut= 26 ),
           UNITE_MODE_STAT =SIMP(statut='f',typ='I',defaut= 27 ),
           UNITE_MAILLAGE  =SIMP(statut='f',typ='I',defaut= 28 ),
           IMPR_MODE_MECA  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           IMPR_MODE_STAT  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         ),

)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
IMPR_MATRICE=PROC(nom="IMPR_MATRICE",op= 159,
                  fr="Impression des matrices �l�mentaires et des matrices assembl�es",
                  docu="U7.04.32-c",
         regles=(AU_MOINS_UN('MATR_ELEM','MATR_ASSE'),),
         
         MATR_ELEM       =FACT(statut='f',min=01,max='**',
           FICHIER         =SIMP(statut='f',typ='TXM' ),
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="IDEAS",
                                 into=("IDEAS","RESULTAT") ),
           b_format      =BLOC(condition = "FORMAT == 'IDEAS'",
             VERSION         =SIMP(statut='f',typ='I',defaut= 5,into=( 5 ,) ),
           ),
#  cr�er les types matr_elem  et vect_elem        
           MATRICE         =SIMP(statut='o',typ=(matr_elem, vect_elem)),
#  Quelle regle pour TOUT, NOEUD, GROUP_NO, MAILLE, GROUP_MA           
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           NOM_CMP         =SIMP(statut='f',typ='TXM',max='**'),
           GRAIN           =SIMP(statut='f',typ='TXM',defaut="VALEUR",
                                 into=("VALEUR","NOEUD","MAILLE") ),
           NB_CHIFFRE      =SIMP(statut='f',typ='I',defaut= 4 ),
         ),
         MATR_ASSE       =FACT(statut='f',min=01,max='**',
           FICHIER         =SIMP(statut='f',typ='TXM' ),
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="IDEAS",
                                 into=("IDEAS","RESULTAT") ),
           VERSION         =SIMP(statut='f',typ='I',defaut= 5,into=( 5 ,) ),
#  cr�er le type matr_elem           
           MATRICE         =SIMP(statut='o',typ=matr_asse),
#  Quelle regle pour TOUT, NOEUD, GROUP_NO, MAILLE, GROUP_MA                      
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           OPTION          =SIMP(statut='f',typ='TXM',defaut="SOUS_MATRICE",
                                 into=("SOUS_MATRICE","LIGNE","COLONNE") ),
           NOM_CMP         =SIMP(statut='f',typ='TXM',max='**'),
           GRAIN           =SIMP(statut='f',typ='TXM',defaut="VALEUR",
                                 into=("VALEUR","NOEUD") ),
           NB_CHIFFRE      =SIMP(statut='f',typ='I',defaut= 4 ),
           VALE_ZERO       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
IMPR_MISS_3D=PROC(nom="IMPR_MISS_3D",op= 162,
                  docu="U7.04.11-c",
         regles=(UN_PARMI('INST_INIT','FREQ_INIT'),
                 PRESENT_PRESENT('INST_INIT','INST_FIN'),
                 PRESENT_PRESENT('FREQ_INIT','FREQ_FIN'),),
         MACR_ELEM_DYNA  =SIMP(statut='o',typ=macr_elem_dyna ),
         EXCIT           =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('FONC_MULT','COEF_MULT' ),),
           VECT_ASSE       =SIMP(statut='f',typ=cham_no_depl_r ),
           FONC_MULT       =SIMP(statut='f',typ=fonction ),
           COEF_MULT       =SIMP(statut='f',typ='R' ),
         ),
         EXCIT_SOL       =FACT(statut='f',min=01,max='**',
           DIRECTION       =SIMP(statut='o',typ='R',max='**'),
           FONC_SIGNAL     =SIMP(statut='f',typ=fonction ),
           NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",
                                 into=("DEPL","VITE","ACCE","FORC",) ),
         ),
         INST_INIT       =SIMP(statut='f',typ='R' ),
         INST_FIN        =SIMP(statut='f',typ='R' ),
         FREQ_INIT       =SIMP(statut='f',typ='R' ),
         FREQ_FIN        =SIMP(statut='f',typ='R' ),
         PAS             =SIMP(statut='o',typ='R' ),
         UNITE           =SIMP(statut='f',typ='I',defaut= 26 ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 30/01/2002   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
IMPR_RESU=PROC(nom="IMPR_RESU",op=39,docu="U4.91.01-f1",
               fr="Impression du r�sultat d un calcul (diff�rents formats)",
         MODELE          =SIMP(statut='f',typ=modele),
         RESU            =FACT(statut='o',min=01,max='**',
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="RESULTAT",
                                 into=("RESULTAT","IDEAS","ASTER","CASTEM","ENSIGHT","MED","GMSH") ),

           b_format_ideas  =BLOC(condition="FORMAT=='IDEAS'",fr="version Ideas",
             VERSION         =SIMP(statut='f',typ='I',defaut=5,into=(4,5)),
           ),

           b_format_castem =BLOC(condition="FORMAT=='CASTEM'",fr="version Castem",
             NIVE_GIBI       =SIMP(statut='f',typ='I',defaut=10,into=(3,10)),
           ),

           regles=(AU_MOINS_UN('CHAM_GD','RESULTAT','MAILLAGE'),
                   EXCLUS('CHAM_GD','RESULTAT'),),
           MAILLAGE        =SIMP(statut='f',typ=(maillage,squelette)),
           INFO_MAILLAGE   =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           CHAM_GD         =SIMP(statut='f',typ=cham_gd),
           RESULTAT        =SIMP(statut='f',typ=resultat),# CO() sd a creer !!!

           b_sensibilite   =BLOC(condition="RESULTAT != None",
                                 fr="D�finition des param�tres de sensibilit�",
                                 ang="Definition of sensitivity parameters",
             SENSIBILITE     =SIMP(statut='f',typ=(para_sensi,theta_geom),max='**',
                                   fr="Liste des param�tres de sensibilit�.",
                                   ang="List of sensitivity parameters"),),

           b_extrac        =BLOC(condition="RESULTAT != None",
                                 fr="extraction d un champ de grandeur",
             regles=(EXCLUS('TOUT_CHAM','NOM_CHAM'),
                     EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','FREQ','NUME_MODE','NOEUD_CMP',
                            'LIST_INST','LIST_FREQ','LIST_ORDRE','NOM_CAS','ANGL'),),
             TOUT_CHAM       =SIMP(statut='f',typ='TXM',into=("OUI","NON") ),
             NOM_CHAM        =SIMP(statut='f',typ='TXM',max='**'),

             TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
             NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
             LIST_ORDRE      =SIMP(statut='f',typ=listis),
             NOEUD_CMP       =SIMP(statut='f',typ='TXM',max='**'),
             NOM_CAS         =SIMP(statut='f',typ='TXM',max='**'),
             ANGL            =SIMP(statut='f',typ='R',max='**'),
             FREQ            =SIMP(statut='f',typ='R',max='**'),
             LIST_FREQ       =SIMP(statut='f',typ=listr8),
             INST            =SIMP(statut='f',typ='R',max='**'),
             LIST_INST       =SIMP(statut='f',typ=listr8),

             b_acce_reel     =BLOC(condition="(FREQ != None)or(LIST_FREQ != None)or(INST != None)or(LIST_INST != None)",
               PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3),
               CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
             ),
           ),

           b_parametres    =BLOC(condition="""(RESULTAT != None)and(FORMAT == 'RESULTAT')""",
             regles=(EXCLUS('TOUT_PARA','NOM_PARA'),),
             INFO_RESU       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
             TOUT_PARA       =SIMP(statut='f',typ='TXM',into=("OUI","NON",) ),
             NOM_PARA        =SIMP(statut='f',typ='TXM',max='**'),
             FORM_TABL       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON","EXCEL") ),
           ),

           b_cmp=BLOC(condition="""((CHAM_GD != None)or(RESULTAT != None))and((FORMAT == 'RESULTAT')or(FORMAT == 'ENSIGHT'))""",
                                 fr="s�lection des composantes",
             regles=(EXCLUS('TOUT_CMP','NOM_CMP'),),
             TOUT_CMP        =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             NOM_CMP         =SIMP(statut='f',typ='TXM',max='**'),
           ),

           b_gmsh=BLOC(condition="""((CHAM_GD != None)or(RESULTAT != None))and((FORMAT == 'GMSH'))""",
                                 fr="s�lection des composantes et des entit�s toplogiques",
             NOM_CMP         =SIMP(statut='f',typ='TXM',max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           ),

           b_topologie=BLOC(condition="""((CHAM_GD != None)or(RESULTAT != None))and((FORMAT == 'RESULTAT')or(FORMAT == 'IDEAS'))""",
                                   fr="s�lection des entit�s toplogiques",
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           ),

           b_valeurs         =BLOC(condition="(FORMAT == 'RESULTAT')",
                                   fr="s�lection sur les valeurs",
             VALE_MAX        =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             VALE_MIN        =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             BORNE_SUP       =SIMP(statut='f',typ='R'),
             BORNE_INF       =SIMP(statut='f',typ='R'),
             IMPR_COOR       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
             FORMAT_R        =SIMP(statut='f',typ='TXM',defaut="1PE12.5"),
           ),

           SOUS_TITRE      =SIMP(statut='f',typ='TXM',max='**'),
           FICHIER         =SIMP(statut='f',typ='TXM'),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
) ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
IMPR_STURM=PROC(nom="IMPR_STURM",op=32,fr="Calculer et imprimer le nombre de valeurs propres dans un intervalle donn�",
                docu="U4.52.01-f",
         MATR_A          =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_temp_r,matr_asse_pres_r ) ),
         MATR_B          =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_temp_r,matr_asse_pres_r ) ),
         TYPE_RESU       =SIMP(statut='f',typ='TXM',defaut="DYNAMIQUE",into=("MODE_FLAMB","DYNAMIQUE"),
                               fr="Type d analyse" ),
         b_dynamique  =BLOC(condition = "TYPE_RESU == 'DYNAMIQUE'",
                            fr="Recheche du nombre de fr�quences propres",
             FREQ_MIN        =SIMP(statut='f',typ='R',defaut= 0.E+0 ,fr="Borne inf�rieure de l intervalle" ),
             FREQ_MAX        =SIMP(statut='o',typ='R',fr="Borne sup�rieure de l intervalle" ),
         ),
         b_mode_flamb =BLOC(condition = "TYPE_RESU == 'MODE_FLAMB'",
                            fr="Recherche du nombre de charges critiques",
             CHAR_CRIT_MIN   =SIMP(statut='o',typ='R',fr="Borne inf�rieure de l intervalle" ),
             CHAR_CRIT_MAX   =SIMP(statut='o',typ='R',fr="Borne sup�rieure de l intervalle" ),
         ),
         NPREC_SOLVEUR   =SIMP(statut='f',typ='I',defaut= 8 ),
         NMAX_ITER_SHIFT =SIMP(statut='f',typ='I',defaut= 5 ),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT"),
         PREC_SHIFT      =SIMP(statut='f',typ='R',defaut= 1.E-2 ),
         SEUIL_FREQ      =SIMP(statut='f',typ='R',defaut= 1.E-2 ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
IMPR_TABLE=PROC(nom="IMPR_TABLE",op=155,docu="U4.91.03-c1",
                fr="Impression d un concept de type table",
         TABLE           =SIMP(statut='o',typ=table),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT", ),
         FORMAT          =SIMP(statut='f',typ='TXM',defaut="EXCEL",
                               into=("EXCEL","AGRAF","MOT_CLE","TABLEAU") ),
         FILTRE          =FACT(statut='f',min=1,max='**',
           NOM_PARA        =SIMP(statut='o',typ='TXM'),
           CRIT_COMP       =SIMP(statut='f',typ='TXM',defaut="EQ",
                                 into=("EQ","LT","GT","NE","LE","GE","VIDE",
                                       "NON_VIDE","MAXI","ABS_MAXI","MINI","ABS_MINI") ),
           b_vale          =BLOC(condition = "(CRIT_COMP in ('EQ','NE','GT','LT','GE','LE'))",
              regles=(UN_PARMI('VALE','VALE_I','VALE_K','VALE_C',),),
              VALE            =SIMP(statut='f',typ='R'),
              VALE_I          =SIMP(statut='f',typ='I'),
              VALE_C          =SIMP(statut='f',typ='C'),
              VALE_K          =SIMP(statut='f',typ='TXM'),),

           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
         ),
         TRI             =FACT(statut='f',min=1,max=1,
           NOM_PARA        =SIMP(statut='o',typ='TXM',max='**'),
           ORDRE           =SIMP(statut='f',typ='TXM',max='**',defaut="CROISSANT",
                                 into=("CROISSANT","DECROISSANT") ),
         ),
         PAGINATION      =SIMP(statut='f',typ='TXM',max='**'),
         FORMAT_R        =SIMP(statut='f',typ='TXM',defaut="1PE12.5"),
         FORMAT_C        =SIMP(statut='f',typ='TXM',defaut="MODULE_PHASE",
                                    into=("MODULE_PHASE","REEL_IMAG") ),
         NOM_PARA        =SIMP(statut='f',typ='TXM',max='**'),
         TOUT_PARA       =SIMP(statut='f',typ='TXM',into=("OUI",)),
         IMPR_FONCTION   =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
INCLUDE=MACRO(nom="INCLUDE",op=-1,docu="U4.13.01-e",
             fr="D�branchement vers un fichier de commandes secondaires",
             sd_prod=ops.INCLUDE,op_init=ops.INCLUDE_context,fichier_ini=1,
         UNITE = SIMP(statut='o',typ='I'),
         INFO  = SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
);
#& MODIF COMMANDE  DATE 14/02/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
INCLUDE_MATERIAU=MACRO(nom="INCLUDE_MATERIAU",op=-14,docu="U4.43.02-a",
                       fr=" ",
         sd_prod=ops.INCLUDE_MATERIAU,op_init=ops.INCLUDE_context,fichier_ini=0,
         NOM_AFNOR       =SIMP(statut='o',typ='TXM' ),  
         TYPE_MODELE     =SIMP(statut='o',typ='TXM',into=("REF","PAR") ),
         VARIANTE        =SIMP(statut='o',typ='TXM',     
                               into=("A","B","C","D","E","F","G","H","I","J",    
                                     "K","L","M","N","O","P","Q","R","S","T","U","V",   
                                     "W","X","Y","Z",) ),
         TYPE_VALE       =SIMP(statut='o',typ='TXM',into=("NOMI","MINI","MAXI") ),
         NOM_MATER       =SIMP(statut='o',typ='TXM' ),  
         UNITE           =SIMP(statut='f',typ='I',defaut= 32 ),  
         EXTRACTION      =FACT(statut='f',min=01,max=99,
           COMPOR          =SIMP(statut='o',typ='TXM' ),  
           TEMP_EVAL       =SIMP(statut='o',typ='R' ),  
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
INTE_MAIL_2D=OPER(nom="INTE_MAIL_2D",op=50,sd_prod=courbe,docu="U4.81.11-e",
                  fr="D�finition d une courbe sur un maillage 2D",reentrant='n',

         MAILLAGE        =SIMP(statut='o',typ=(maillage) ),

         regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),
                 AU_MOINS_UN('DEFI_SEGMENT','DEFI_ARC','DEFI_CHEMIN'),
                 PRESENT_ABSENT('DEFI_CHEMIN','DEFI_SEGMENT','DEFI_ARC'),
                 PRESENT_ABSENT('DEFI_SEGMENT','NOEUD_ORIG','GROUP_NO_ORIG'),
                 PRESENT_ABSENT('DEFI_ARC','NOEUD_ORIG','GROUP_NO_ORIG'),
                 EXCLUS('NOEUD_ORIG','GROUP_NO_ORIG'),
                 EXCLUS('DEFI_CHEMIN','DEFI_SEGMENT'),
                 EXCLUS('DEFI_CHEMIN','DEFI_ARC'),),

         TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         MAILLE          =SIMP(statut='f',typ=ma,max='**'),

         DEFI_SEGMENT    =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('ORIGINE','NOEUD_ORIG','GROUP_NO_ORIG'),
                   UN_PARMI('EXTREMITE','NOEUD_EXTR','GROUP_NO_EXTR'),),
           ORIGINE         =SIMP(statut='f',typ='R',min=2,max=2),  
           NOEUD_ORIG      =SIMP(statut='f',typ=no,max=1),
           GROUP_NO_ORIG   =SIMP(statut='f',typ=grno,max=1),
           EXTREMITE       =SIMP(statut='f',typ='R',min=2,max=2),  
           NOEUD_EXTR      =SIMP(statut='f',typ=no,max=1),
           GROUP_NO_EXTR   =SIMP(statut='f',typ=grno,max=1),
         ),

         DEFI_ARC        =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('CENTRE','NOEUD_CENTRE','GROUP_NO_CENTRE'),
                   UN_PARMI('RAYON','ORIGINE','NOEUD_ORIG','GROUP_NO_ORIG'),
                   UN_PARMI('RAYON','EXTREMITE','NOEUD_EXTR','GROUP_NO_EXTR'),               
                   PRESENT_PRESENT('RAYON','SECTEUR'),),
           CENTRE          =SIMP(statut='f',typ='R',min=2,max=2),  
           NOEUD_CENTRE    =SIMP(statut='f',typ=no,max=1),
           GROUP_NO_CENTRE =SIMP(statut='f',typ=grno,max=1),
           RAYON           =SIMP(statut='f',typ='R',max=1,val_min=0.E+0),  
           SECTEUR         =SIMP(statut='f',typ='R',min=2,max=2,
                                 val_min=-180.E+0,val_max=180E+0),  
           ORIGINE         =SIMP(statut='f',typ='R',min=2,max=2),  
           NOEUD_ORIG      =SIMP(statut='f',typ=no,max=1),
           GROUP_NO_ORIG   =SIMP(statut='f',typ=grno,max=1),
           EXTREMITE       =SIMP(statut='f',typ='R',min=2,max=2),  
           NOEUD_EXTR      =SIMP(statut='f',typ=no,max=1),
           GROUP_NO_EXTR   =SIMP(statut='f',typ=grno,max=1),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),  
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",    
                                 into=("RELATIF","ABSOLU",) ),
         ),

         DEFI_CHEMIN     =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','GROUP_MA'),),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         ),

         NOEUD_ORIG      =SIMP(statut='f',typ=no,max=1),
         GROUP_NO_ORIG   =SIMP(statut='f',typ=grno,max=1),
         PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3),  
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
INTE_MAIL_3D=OPER(nom="INTE_MAIL_3D",op=96,sd_prod=surface,docu="U4.81.12-e",
                  fr="D�finition d un chemin sur un maillage 3D",reentrant='n',
         MAILLAGE        =SIMP(statut='o',typ=maillage),
         TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         DEFI_SEGMENT    =FACT(statut='o',min=01,max='**',
           regles=(UN_PARMI('ORIGINE','NOEUD_ORIG','GROUP_NO_ORIG'),
                   UN_PARMI('EXTREMITE','NOEUD_EXTR','GROUP_NO_EXTR'),),
           ORIGINE         =SIMP(statut='f',typ='R',min=3,max=3),  
           NOEUD_ORIG      =SIMP(statut='f',typ=no,max=1),
           GROUP_NO_ORIG   =SIMP(statut='f',typ=grno,max=1),
           EXTREMITE       =SIMP(statut='f',typ='R',min=3,max=3),  
           NOEUD_EXTR      =SIMP(statut='f',typ=no,max=1),
           GROUP_NO_EXTR   =SIMP(statut='f',typ=grno,max=1),
         ),
         PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-6),  
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 25/01/2002   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def lire_champ_prod(TYPE_CHAM=None,**args):
  if TYPE_CHAM == "CHAM_NO_TEMP_R" : return cham_no_temp_r
  if TYPE_CHAM == "CHAM_NO_DEPL_R" : return cham_no_depl_r
  raise AsException("type de concept resultat non prevu")

LIRE_CHAMP=OPER(nom="LIRE_CHAMP",op= 192,sd_prod=lire_champ_prod,
                fr="Lire un champ dans un fichier et le stocker dans un concept.",
                ang="To read a field in a file and to save it in a concept.",
                docu="U7.02.02-a1",reentrant='n',
#
# 1. Le maillage support du champ
#
         MAILLAGE        =SIMP(statut='o',typ=maillage,
                          fr="Nom du maillage support du champ",
                          ang="Name of the mesh on which the field is defined" ),
#
# 2. Format de lecture
#    Remarque : seul MED est operationnel dans cette version.
#
         FORMAT          =SIMP(statut='f',typ='TXM',defaut="MED",into=("MED",),
                          fr="Format du fichier : MED seulement",
                          ang="Format of the file : MED only" ),
#
# 3. L'unite logique du fichier.
#
         UNITE           =SIMP(statut='f',typ='I',defaut= 81,
                          fr="Le fichier est : fort.n.",
                          ang="File is : fort.n" ),  
#
# 4. Pour le format MED, il faut preciser le nom sous lequel le champ est connu dans le fichier
#    et les composantes a lire
#
         b_format =BLOC(condition = "FORMAT == 'MED'",
                        fr="Nom du champ dans le fichier MED",
         regles=(UN_PARMI('NOM_CMP_IDEM','NOM_CMP'),
          PRESENT_PRESENT('NOM_CMP','NOM_CMP_MED' ),),
#
            NOM_MED      =SIMP(statut='o',typ='TXM',
                          fr="Nom du champ dans le fichier MED.",
                          ang="Name of the field in the MED file." ),
#
            NOM_CMP_IDEM =SIMP(statut='f',typ='TXM',into=("OUI",),
                          fr="Les composantes ont le meme nom dans MED et ASTER.",
                          ang="The names of the components are the same in ASTER and MED." ),
            NOM_CMP      =SIMP(statut='f',typ='TXM',max='**',
                          fr="Nom des composantes dans ASTER.",
                          ang="Names of the components in ASTER" ),
            NOM_CMP_MED  =SIMP(statut='f',typ='TXM',max='**',
                          fr="Nom des composantes dans MED.",
                          ang="Names of the components in MED" ),
#
            NUME_ORDRE   =SIMP(statut='f',typ='I',max='**',
                          fr="Numero d'ordre du champ � lire.",
                          ang="Rank number of the field to read."),
#
# Pour une lecture dans un fichier MED, on peut pr�ciser le nom sous lequel
# le maillage associ� au champ y a �t� enregistr�. Par d�faut, on prendra le premier maillage.
#
            NOM_MAIL_MED = SIMP(statut='f',typ='TXM',
                           fr="Nom du maillage dans le fichier MED.",
                           ang="Name of the mesh into the MED file.",),
#
                  ),
#
# 5. Le type du concept lu
#
         TYPE_CHAM       =SIMP(statut='o',typ='TXM',into=("CHAM_NO_TEMP_R","CHAM_NO_DEPL_R"),
                          fr="Type de champ � cr�er.",
                          ang="Type of the field to create." ),
#
# 6. Le niveau d'information
#
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
LIRE_FONCTION=OPER(nom="LIRE_FONCTION",op=  83,sd_prod=fonction,
                   fr="Lecture d une fonction dans un fichier ",
                   docu="U4.32.02-e1",reentrant='n',
         UNITE           =SIMP(statut='o',typ='I' ),
         NOM_PARA        =SIMP(statut='f',typ='TXM',
                               into=("DX","DY","DZ","DRX","DRY","DRZ","TEMP",
                                     "INST","X","Y","Z","EPSI","FREQ","PULS","AMOR","ABSC",) ),
         NOM_RESU        =SIMP(statut='f',typ='TXM' ),
         INTERPOL        =SIMP(statut='f',typ='TXM',max=2,into=("NON","LIN","LOG") ),
         PROL_DROITE     =SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         PROL_GAUCHE     =SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         NOM_PARA_FONC   =SIMP(statut='f',typ='TXM',
                               into=("DX","DY","DZ","DRX","DRY","DRZ","TEMP",
                                     "INST","X","Y","Z","EPSI","FREQ","PULS","AMOR","ABSC",) ),
         INTERPOL_FONC   =SIMP(statut='f',typ='TXM',max=2,into=("NON","LIN","LOG") ),
         PROL_DROITE_FONC=SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         PROL_GAUCHE_FONC=SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         INFO            =SIMP(statut='f',typ='I',defaut= 2,into=( 1 , 2) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
LIRE_INTE_SPEC=OPER(nom="LIRE_INTE_SPEC",op= 116,sd_prod=tabl_intsp,
                    fr="Lecture sur un fichier externe de  fonctions complexes pour cr�er une matrice interspectrale",
                    docu="U4.36.01-e1",reentrant='n',
         UNITE           =SIMP(statut='o',typ='I' ),
         FORMAT          =SIMP(statut='f',typ='TXM',defaut="MODULE_PHASE",into=("REEL_IMAG","MODULE_PHASE") ),
         NOM_PARA        =SIMP(statut='f',typ='TXM',
                               into=("DX","DY","DZ","DRX","DRY","DRZ","TEMP",
                                     "INST","X","Y","Z","EPSI","FREQ","PULS","AMOR","ABSC",) ),
         NOM_RESU        =SIMP(statut='f',typ='TXM' ),
         INTERPOL        =SIMP(statut='f',typ='TXM',max=2,into=("NON","LIN","LOG") ),
         PROL_DROITE     =SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         PROL_GAUCHE     =SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 10/10/2001   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
LIRE_MAILLAGE=OPER(nom="LIRE_MAILLAGE",op=   1,sd_prod=maillage,
                   fr="Lecture d'un fichier de maillage",
                   ang="Readings of a mesh file",
                   docu="U4.21.01-f",reentrant='n',
#
         UNITE           =SIMP(statut='f',typ='I',defaut= 20 ),
#
         FORMAT          =SIMP(statut='f',typ='TXM',defaut="ASTER",into=("ASTER","MED"),
                            fr="Format du fichier : ASTER ou MED.",
                            ang="Format of the file : ASTER or MED.",),
#
         ABSC_CURV       =FACT(statut='f',min=00,max=01,
               TOUT          =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         ),
#
         VERI_MAIL       =FACT(statut='d',min=01,max=01,
               APLAT         =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),  
         ),
#
         b_format_med =BLOC( condition = " ( FORMAT == 'MED' ) " ,
                           fr="Informations compl�mentaires pour la lecture MED.",
                           ang="Further information for MED readings.",
#
# Pour une lecture dans un fichier MED, on peut pr�ciser le nom sous lequel
# le maillage y a �t� enregistr�. Par d�faut, on va le chercher sous le nom du concept � cr�er.
#
              NOM_MED    = SIMP(statut='f',typ='TXM',
                            fr="Nom du maillage dans le fichier MED.",
                            ang="Name of the mesh into the MED file.",),
#
              INFO_MED   = SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
#
                           ) ,
#
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
#
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def lire_miss_3d_prod(TYPE_RESU,**args):
  if TYPE_RESU == "TRANS" : return dyna_trans
  if TYPE_RESU == "HARMO" : return dyna_harmo
  raise AsException("type de concept resultat non prevu")

LIRE_MISS_3D=OPER(nom="LIRE_MISS_3D",op= 163,sd_prod=lire_miss_3d_prod,
                  fr="Restitution au format MISS3D d une �volution harmonique ou transitoire",
                  docu="U7.02.31-c",reentrant='n',
         MACR_ELEM_DYNA  =SIMP(statut='o',typ=macr_elem_dyna ),
         UNITE           =SIMP(statut='f',typ='I',defaut= 27 ),
         TYPE_RESU       =SIMP(statut='f',typ='TXM',defaut="TRANS",into=("TRANS","HARMO") ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
LIRE_PLEXUS=OPER(nom="LIRE_PLEXUS",op= 184,sd_prod=evol_char,
                 fr=" ",
                 docu="U7.02.11-a",reentrant='n',
         regles=(UN_PARMI('TOUT_ORDRE','NUME_ORDRE','INST','LIST_INST','LIST_ORDRE'),),
         UNITE           =SIMP(statut='f',typ='I',defaut= 19 ),
         FORMAT          =SIMP(statut='f',typ='TXM',defaut="IDEAS",into=("IDEAS",)),
         MAIL_PLEXUS     =SIMP(statut='o',typ=maillage ),
         MAILLAGE        =SIMP(statut='o',typ=maillage ),
         MODELE          =SIMP(statut='o',typ=modele ),
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
         LIST_ORDRE      =SIMP(statut='f',typ=listis ),
         INST            =SIMP(statut='f',typ='R',max='**'),
         LIST_INST       =SIMP(statut='f',typ=listr8 ),
         b_prec_crit     =BLOC(condition = "LIST_INST != None or INST != None",
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",
                                   into=("RELATIF","ABSOLU") ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 12/09/2001   AUTEUR MCOURTOI M.COURTOIS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def lire_resu_prod(TYPE_RESU,**args):
  if TYPE_RESU == "EVOL_CHAR" :  return evol_char
  if TYPE_RESU == "EVOL_THER" :  return evol_ther
  if TYPE_RESU == "EVOL_ELAS" :  return evol_elas
  if TYPE_RESU == "EVOL_NOLI" :  return evol_noli
  if TYPE_RESU == "DYNA_TRANS" : return dyna_trans
  if TYPE_RESU == "DYNA_HARMO" : return dyna_harmo
  if TYPE_RESU == "HARM_GENE" :  return harm_gene
  raise AsException("type de concept resultat non prevu")

LIRE_RESU=OPER(nom="LIRE_RESU",op=150,sd_prod=lire_resu_prod,docu="U7.02.01-c1",reentrant='n',
               fr="Lecture de champs aux noeuds ou par �l�ments aux noeuds sur un fichier IDEAS ou EnSight",
         regles=(UN_PARMI('MAILLAGE','MODELE'),),
         FORMAT          =SIMP(statut='f',typ='TXM',defaut="IDEAS",into=("IDEAS","ENSIGHT","MED") ),
         b_unite         =BLOC(condition="FORMAT=='IDEAS'",
           UNITE           =SIMP(statut='f',typ='I',defaut= 19 ),
         ),
         b_nom_fichier     =BLOC(condition="FORMAT=='ENSIGHT'",
           NOM_FICHIER     =SIMP(statut='f',typ='TXM'),
         ),
         TYPE_RESU       =SIMP(statut='o',typ='TXM',into=("EVOL_THER","EVOL_ELAS","EVOL_NOLI",
                                                          "DYNA_TRANS","DYNA_HARMO","HARM_GENE","EVOL_CHAR") ),
         b_evol_elas     =BLOC(condition="TYPE_RESU=='EVOL_ELAS'",
           NOM_CHAM        =SIMP(statut='o',typ='TXM',max='**',
                                 into=("DEPL",) ),
         ),
         b_evol_ther     =BLOC(condition="TYPE_RESU=='EVOL_THER'",
           NOM_CHAM        =SIMP(statut='o',typ='TXM',max='**',
                                 into=("TEMP","TEMP_PEAU") ),
         ),
         b_evol_char     =BLOC(condition="TYPE_RESU=='EVOL_CHAR'",
           NOM_CHAM        =SIMP(statut='o',typ='TXM',max='**',
                                 into=("PRES","VITE_VENT",
                                       "FVOL_3D","FVOL_2D",
                                       "FSUR_3D","FSUR_2D") ),
         ),
         b_evol_noli     =BLOC(condition="TYPE_RESU=='EVOL_NOLI'",
           NOM_CHAM        =SIMP(statut='o',typ='TXM',max='**',
                                 into=("DEPL","VITE","ACCE","VARI_ELNO",
                                       "SIEF_ELNO","EPSA_ELNO") ),
         ),
         b_dyna          =BLOC(condition="(TYPE_RESU=='DYNA_TRANS') or (TYPE_RESU=='DYNA_HARMO') or\
                                          (TYPE_RESU=='HARM_GENE')",
           NOM_CHAM        =SIMP(statut='o',typ='TXM',max='**',
                                 into=("DEPL","VITE","ACCE",) ),
         ),
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
         MAILLAGE        =SIMP(statut='f',typ=maillage),
         MODELE          =SIMP(statut='f',typ=modele),
         NB_VARI         =SIMP(statut='f',typ='I' ),
         FORMAT_IDEAS    =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('POSI_INST','POSI_FREQ'),),
           NOM_CHAM        =SIMP(statut='o',typ='TXM',max='**',into=("TEMP","DEPL","VITE","ACCE","PRES","VARI_ELNO",
                                                                     "SIEF_ELNO","EPSA_ELNO","TEMP_PEAU","VITE_VENT",
                                                                     "FVOL_3D","FVOL_2D","FSUR_3D","FSUR_2D") ),
           NUME_DATASET    =SIMP(statut='f',typ='I',into=(55,57,2414) ),
           RECORD_3        =SIMP(statut='f',typ='I',max='**'),
           RECORD_6        =SIMP(statut='f',typ='I',max='**'),
           RECORD_9        =SIMP(statut='f',typ='I',max='**'),
           POSI_ORDRE      =SIMP(statut='o',typ='I',max='**'),
           POSI_INST       =SIMP(statut='f',typ='I',max='**'),
           POSI_FREQ       =SIMP(statut='f',typ='I',max='**'),
           NOM_CMP         =SIMP(statut='o',typ='TXM',max='**'),
         ),
         b_extrac        =BLOC(condition="1",fr="acc�s � un champ dans la structure de donn�es r�sultat",
           regles=(UN_PARMI('TOUT_ORDRE','NUME_ORDRE','LIST_ORDRE','INST','LIST_INST','FREQ','LIST_FREQ'),),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           INST            =SIMP(statut='f',typ='R',max='**'),
           LIST_INST       =SIMP(statut='f',typ=listr8),
           LIST_ORDRE      =SIMP(statut='f',typ=listis),
           FREQ            =SIMP(statut='f',typ='R',max='**'),
           LIST_FREQ       =SIMP(statut='f',typ=listr8),
             
           b_acce_reel     =BLOC(condition="(INST != None)or(LIST_INST != None)or(FREQ != None)or(LIST_FREQ != None)",
             PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 25/01/2002   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE GNICOLAS G.NICOLAS
def macr_adap_mail_prod(self,MAJ_CHAM,ADAPTATION,**args):
  mail1=ADAPTATION['MAILLAGE_N']
  self.type_sdprod(mail1,maillage)
  mail2=ADAPTATION['MAILLAGE_NP1']
  self.type_sdprod(mail2,maillage)
  if MAJ_CHAM == None:return None
  for ch in MAJ_CHAM:
    t=ch['TYPE_CHAM']
    if t == 'CHAM_NO_TEMP_R':self.type_sdprod(ch['CHAM_MAJ'],cham_no_temp_r)
    if t == 'CHAM_NO_DEPL_R':self.type_sdprod(ch['CHAM_MAJ'],cham_no_depl_r)
  return None

MACR_ADAP_MAIL=MACRO(nom="MACR_ADAP_MAIL",op=-24,sd_prod=macr_adap_mail_prod,
                     fr="Adapter un maillage avec le logiciel HOMARD.",
                     ang="Mesh adaptation with HOMARD software.",
                     docu="U7.03.01-a",
#
# 1. Le niveau d'information
#
         INFO           = SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
#
# 2. Version de HOMARD
#
         VERSION_HOMARD = SIMP(statut='f',typ='TXM',defaut="V5_1",
                               into=("V5_1", "V5_N", "V5_N_PERSO"),
                           fr="Version de HOMARD",
                           ang="HOMARD release"),
#
# 3. Langue des messages issus de HOMARD
#
         LANGUE = SIMP(statut='f',typ='TXM',defaut="FRANCAIS",    
                               into=("FRANCAIS","FRENCH","ANGLAIS","ENGLISH",),
                           fr="Langue des messages issus de HOMARD.",
                           ang="Language for HOMARD messages." ),
#
# 4. LE TYPE DE TRAITEMENT :
#
         ADAPTATION      =FACT(statut='o',min=01,max=01,
                           fr="Type d'adaptation",
                           ang="Type of adaptation",
#
# 4.1. DEUX CHOIX D'ADAPTATION EXCLUSIFS :
#
# 4.1.
#      A. SELON UN INDICATEUR D'ERREUR, AVEC TROIS VARIANTES :
#         . RAFFINEMENT ET DERAFFINEMENT
#         . RAFFINEMENT SEUL
#         . DERAFFINEMENT SEUL
#      B. UNIFORME, AVEC TROIS VARIANTES :
#         . RAFFINEMENT SEUL
#         . DERAFFINEMENT SEUL
#         . RIEN : LE MAILLAGE EST LE MEME A LA SORTIE ET A L'ENTREE
#
           regles=(
                   UN_PARMI('LIBRE','UNIFORME'),
                  ),
           LIBRE          = SIMP(statut='f',typ='TXM',
                                 into=("RAFF_DERA","RAFFINEMENT","DERAFFINEMENT"),    
                           fr="Adaptation selon un indicateur d'erreur.",
                           ang="Adaptation among an error indicator" ),
           UNIFORME       = SIMP(statut='f',typ='TXM',
                                 into=("RAFFINEMENT","DERAFFINEMENT","RIEN"),    
                           fr="Adaptation uniforme.",
                           ang="Uniform adaptation" ),
#
# 4.2. QUEL QUE SOIT LE TYPE DE TRAITEMENT, IL FAUT DONNER  :
#      A. LE CONCEPT DU MAILLAGE INITIAL
#      B. LE CONCEPT DU MAILLAGE FINAL
#
           MAILLAGE_N     = SIMP(statut='o',typ=(CO,maillage),
                           fr="Maillage avant adaptation",
                           ang="Mesh before adaptation" ),
           MAILLAGE_NP1   = SIMP(statut='o',typ=(CO,maillage),
                           fr="Maillage apres adaptation",
                           ang="Mesh after adaptation" ),
#
# 4.3. POUR DE L'ADAPTATION LIBRE, IL FAUT L'INDICATEUR D'ERREUR
#
#
           b_indicateur_d_erreur   =BLOC( condition = " LIBRE != None " ,
                           fr="Indicateur d'erreur",
                           ang="Error indicator",
#
# 4.3.1. LE NOM DU CONCEPT RESULTAT
#
                           RESULTAT_N     = SIMP(statut='o',typ=(evol_elas,evol_noli,evol_ther) ,
                           fr="Resultat contenant l'indicateur d'erreur",
                           ang="Result with error indicator" ),
#
# 4.3.2. LE CHAMP D'INDICATEUR D'ERREUR
#
                           INDICATEUR     = SIMP(statut='o',typ='TXM',     
                           fr="Champ de l'indicateur d'erreur",
                           ang="Error indicator field" ),
#
# 4.3.3. LA COMPOSANTE RETENUE
#
                           NOM_CMP_INDICA = SIMP(statut='o',typ='TXM',
                           fr="Composante retenue",
                           ang="Selected component" ),
#
# 4.3.4. LE NUMERO D'ORDRE
#
                           NUME_ORDRE     = SIMP(statut='f',typ='I' ,
                           fr="Numero d ordre",
                           ang="Rank" ),  
                           ) ,
#
# 4.4. LES CRITERES POUR DE L'ADAPTATION LIBRE :
#        ABSOLU, RELATIF, EN PROPORTION D'ENTITE
# 4.4.1. POUR LE RAFFINEMENT :
#
           b_critere_de_raffinement =BLOC( condition = " ( LIBRE == 'RAFF_DERA' ) or ( LIBRE == 'RAFFINEMENT' ) " ,
                           fr="Crit�re de raffinement.",
                           ang="Refinement threshold.",
                           regles=(UN_PARMI ( 'CRIT_RAFF_ABS', 'CRIT_RAFF_REL', 'CRIT_RAFF_PE' ),),
                           CRIT_RAFF_ABS  = SIMP(statut='f',typ='R',
                                                   fr="Crit�re absolu",
                                                   ang="Absolute threshold" ),  
                           CRIT_RAFF_REL  = SIMP(statut='f',typ='R',
                                                   fr="Crit�re relatif",
                                                   ang="Relative threshold" ),  
                           CRIT_RAFF_PE   = SIMP(statut='f',typ='R',
                                                   fr="Pourcentage d'�l�ments",
                                                   ang="Percentage of elements" ),  
                           ) ,
#
# 4.4.2. POUR LE DERAFFINEMENT :
#
           b_critere_de_deraffinement =BLOC ( condition = " ( LIBRE == 'RAFF_DERA' ) or ( LIBRE == 'DERAFFINEMENT' ) " ,
                           fr="Crit�re de d�raffinement.",
                           ang="Unrefinement threshold.",
                           regles=(UN_PARMI ( 'CRIT_DERA_ABS', 'CRIT_DERA_REL', 'CRIT_DERA_PE' ),),
                           CRIT_DERA_ABS  = SIMP(statut='f',typ='R' ,
                                                 fr="Crit�re absolu",
                                                 ang="Absolute threshold" ),  
                           CRIT_DERA_REL  = SIMP(statut='f',typ='R',
                                                 fr="Crit�re relatif",
                                                 ang="Relative threshold" ),  
                           CRIT_DERA_PE   = SIMP(statut='f',typ='R',
                                                 fr="Pourcentage d'�l�ments",
                                                 ang="Percentage of elements" ),  
                           ) ,
#
# 4.5. LES NIVEAUX EXTREMES POUR LE MAILLAGE ADAPTE
# 4.5.1. POUR LE RAFFINEMENT :
#
           b_niveau_maximum =BLOC ( condition = " ( LIBRE == 'RAFF_DERA' ) or ( LIBRE == 'RAFFINEMENT' ) or "+
                                                " ( UNIFORME == 'RAFFINEMENT' ) " ,
                             fr="Niveau maximum de profondeur de raffinement",
                             ang="Maximum level for refinement",
                             NIVE_MAX       = SIMP(statut='f',typ='I' ),  
                           ) ,
#
# 4.5.2. POUR LE DERAFFINEMENT :
#
           b_niveau_minimum =BLOC ( condition = " ( LIBRE == 'RAFF_DERA' ) or ( LIBRE == 'DERAFFINEMENT' ) or "+
                                                " ( UNIFORME == 'DERAFFINEMENT' ) " ,
                             fr="Niveau minimum de profondeur de d�raffinement",
                             ang="Minimum level for unrefinement",
                             NIVE_MIN       = SIMP(statut='f',typ='I' ),
                           ) ,
         ),
#
# 5. LA MISE A JOUR DE CHAMPS.
#    PAR DEFAUT, RIEN NE SE FAIT
#
         MAJ_CHAM        =FACT(statut='f',min=01,max='**',
                           fr="Mise � jour de champs sur le nouveau maillage.",
                           ang="Updationg of fields over the new mesh.",
#
# 5.1. LE NOM DU RESULTAT DU CHAMP A INTERPOLER
#
           RESULTAT       = SIMP(statut='o',
                                 typ=(evol_elas,evol_noli,evol_ther),
                           fr="Resultat contenant le champ � mettre � jour",
                           ang="Result with field to be updated" ),
#
# 5.2. LE NOM DU CHAMP A INTERPOLER
#
           NOM_CHAM       = SIMP(statut='o',typ='TXM',
                           fr="Nom du champ � mettre � jour",
                           ang="Name of the field to be updated" ),  
#
# 5.3. LE NUMERO D'ORDRE POUR LE CHAMP A INTERPOLER
#
           NUME_ORDRE     = SIMP(statut='f',typ='I',
                           fr="Numero d ordre du champ � mettre � jour",
                           ang="Rank of the field to be updated" ),  
#
# 5.4. LE NOM DU CHAMP QUI CONTIENDRA LE RESULTAT DE LA MISE A JOUR
#
           CHAM_MAJ       = SIMP(statut='o',typ=(CO,cham_gd),
                           fr="Nom du champ qui contiendra le champ mis � jour",
                           ang="Name of the field for the updated field"),
#
# 5.5. LE TYPE DU CHAMP QUI CONTIENDRA LE RESULTAT DE LA MISE A JOUR
#
           TYPE_CHAM      = SIMP(statut='o',typ='TXM',     
                                 into=("CHAM_NO_TEMP_R","CHAM_NO_DEPL_R"),
                           fr="Type du champ qui contiendra le champ mis � jour",
                           ang="Type of the field for the updated field" ),
         ),
#
# 6. INFORMATION SUR LE MAILLAGE : par defaut, on ne fait que les nombres
#    A. NOMBRE DE NOEUDS ET ELEMENTS DU MAILLAGE
#    B. QUALITE DES ELEMENTS DU MAILLAGE
#    C. CONTROLE DE LA NON INTERPENETRATION DES ELEMENTS DU MAILLAGE
#    D. CONNEXITE DU MAILLAGE
#    E. TAILLE DES DIFFERENTS SOUS-DOMAINES
#
         NOMBRE         = SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON"),
                          fr="Nombre de noeuds et �l�ments du maillage",
                          ang="Number of nodes and elements in the mesh" ),
#
         QUALITE        = SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Qualit� du maillage",
                          ang="Mesh quality" ),
#
         INTERPENETRATION=SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Controle de la non interp�n�tration des �l�ments.",
                          ang="Overlapping checking." ),
#
         CONNEXITE      = SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Connexit� du maillage.",
                          ang="Mesh connexity." ),
#
         TAILLE         = SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Tailles des sous-domaines du maillage.",
                          ang="Sizes of mesh sub-domains." ),
#
         MENAGE         = SIMP(statut='f',typ='TXM',into=("MAILLAGE","SOLUTION","TOUT") ),
#
)  ;
#& MODIF COMMANDE  DATE 20/12/2001   AUTEUR F1BHHAJ J.ANGLES 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE F1BHHAJ J.ANGLES
def macr_ascouf_calc_prod(self,MODELE,CHAM_MATER,CARA_ELEM,FOND_FISS,CHARGE,RESU_THER,**args):
  self.type_sdprod(MODELE,modele)
  if CHAM_MATER != None:self.type_sdprod(CHAM_MATER,cham_mater)
  if CARA_ELEM  != None:self.type_sdprod(CARA_ELEM,cara_elem)
  if FOND_FISS  != None:self.type_sdprod(FOND_FISS,fond_fiss)
  if CHARGE     != None:self.type_sdprod(CHARGE,char_meca)
  if RESU_THER  != None:self.type_sdprod(RESU_THER,evol_ther)
  return evol_noli

MACR_ASCOUF_CALC=MACRO(nom="MACR_ASCOUF_CALC",op= -20,sd_prod=macr_ascouf_calc_prod,
                      fr=" ",
                      docu="U4.CF.20-a",reentrant='n',
         regles=(UN_PARMI('COMP_INCR','COMP_ELAS'),),

         TYPE_MAILLAGE   =SIMP(statut='o',typ='TXM',
                               into=("SAIN",
                                     "FISS_COUDE",
                                     "SOUS_EPAIS_COUDE"
                                     ) ),

         CL_BOL_P2_GV    =FACT(statut='f',min=1,max=1,
           ANGLE           =SIMP(statut='o',typ='R' ),
           AZIMUT          =SIMP(statut='f',typ='R',defaut= 90. ),
         ),

         MAILLAGE        =SIMP(statut='o',typ=maillage ),
         MODELE          =SIMP(statut='o',typ=(CO,modele)),
         CHAM_MATER      =SIMP(statut='f',typ=(CO,cham_mater)),
         CARA_ELEM       =SIMP(statut='f',typ=(CO,cara_elem)),
         FOND_FISS       =SIMP(statut='f',typ=(CO,fond_fiss)),
         CHARGE          =SIMP(statut='f',typ=(CO,char_meca)),
         RESU_THER       =SIMP(statut='f',typ=(CO,evol_ther)),

         AFFE_MATERIAU   =FACT(statut='o',min=1,max=3,
           regles=(UN_PARMI('TOUT','GROUP_MA'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ='TXM',into=("COUDE","BOL") ),
           MATER           =SIMP(statut='o',typ=mater ),
           TEMP_REF        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),

         PRES_REP        =FACT(statut='f',min=1,max=1,
           PRES            =SIMP(statut='o',typ='R' ),
           EFFE_FOND_P1    =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           FONC_MULT       =SIMP(statut='f',typ=fonction ),
         ),

         ECHANGE         =FACT(statut='f',min=1,max=1,
           COEF_H          =SIMP(statut='f',typ=fonction ),
           TEMP_EXT        =SIMP(statut='f',typ=fonction ),
         ),

         TORS_P1         =FACT(statut='f',min=1,max=6,
           regles=(AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ'),),
           FX              =SIMP(statut='f',typ='R' ),
           FY              =SIMP(statut='f',typ='R' ),
           FZ              =SIMP(statut='f',typ='R' ),
           MX              =SIMP(statut='f',typ='R' ),
           MY              =SIMP(statut='f',typ='R' ),
           MZ              =SIMP(statut='f',typ='R' ),
           FONC_MULT       =SIMP(statut='f',typ=fonction ),
         ),

         COMP_INCR       =FACT(statut='f',min=1,max=1,
           RELATION        =SIMP(statut='o',typ='TXM',into=("VMIS_ISOT_TRAC",) ),
           VMIS_ISOT_TRAC  =SIMP(statut='c',typ='I',defaut= 2,into=( 2 ,) ),
         ),

         COMP_ELAS       =FACT(statut='f',min=1,max=1,
           RELATION        =SIMP(statut='o',typ='TXM',into=("ELAS","ELAS_VMIS_TRAC") ),
           ELAS            =SIMP(statut='c',typ='I',defaut= 1,into=( 1 ,) ),
           ELAS_VMIS_TRAC  =SIMP(statut='c',typ='I',defaut= 1,into=( 1 ,) ),
         ),

         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt         =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
           ),
           b_ldlt_mult    =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non inversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
           b_gcpc         =BLOC(condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
#  A quoi sert eps
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           SYME            =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         ),

         CONVERGENCE     =FACT(statut='d',min=1,max=1,
           RESI_GLOB_MAXI  =SIMP(statut='f',typ='R'),
           RESI_GLOB_RELA  =SIMP(statut='f',typ='R'),
           ITER_GLOB_MAXI  =SIMP(statut='f',typ='I',defaut=10),
           ARRET           =SIMP(statut='f',typ='TXM',defaut="OUI"),
           RESI_INTE_RELA  =SIMP(statut='f',typ='R'
                                ,defaut= 1.0E-6),
           ITER_INTE_MAXI  =SIMP(statut='f',typ='I',defaut= 10 ),
           ITER_INTE_PAS   =SIMP(statut='f',typ='I',defaut= 0 ),
           TYPE_MATR_COMP  =SIMP(statut='f',typ='TXM',defaut="TANG_VIT",into=("TANG_VIT",)),
           RESO_INTE       =SIMP(statut='f',typ='TXM',defaut="IMPLICITE",into=("RUNGE_KUTTA_2","RUNGE_KUTTA_4","IMPLICITE")),
         ),

         NEWTON          =FACT(statut='d',min=1,max=1,
           REAC_INCR       =SIMP(statut='f',typ='I',defaut= 1 ),
           PREDICTION      =SIMP(statut='f',typ='TXM',into=("DEPL_CALCULE","TANGENTE","ELASTIQUE","EXTRAPOL") ),
           MATRICE         =SIMP(statut='f',typ='TXM',defaut="TANGENTE",into=("TANGENTE","ELASTIQUE") ),
           REAC_ITER       =SIMP(statut='f',typ='I',defaut=0),
           EVOL_NOLI       =SIMP(statut='f',typ=evol_noli),
         ),

         RECH_LINEAIRE   =FACT(statut='f',min=1,max=1,
           RESI_LINE_RELA  =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
           ITER_LINE_MAXI  =SIMP(statut='f',typ='I',defaut= 3),
         ),

         INCREMENT       =FACT(statut='o',min=1,max=1,
           regles=(EXCLUS('NUME_INST_INIT','INST_INIT'),
                   EXCLUS('NUME_INST_FIN','INST_FIN'),),
           LIST_INST       =SIMP(statut='o',typ=listr8),
           EVOLUTION       =SIMP(statut='f',typ='TXM',defaut="CHRONOLOGIQUE",
                                 into=("CHRONOLOGIQUE","RETROGRADE","SANS",) ),
           NUME_INST_INIT  =SIMP(statut='f',typ='I'),
           INST_INIT       =SIMP(statut='f',typ='R'),
           NUME_INST_FIN   =SIMP(statut='f',typ='I'),
           INST_FIN        =SIMP(statut='f',typ='R'),
           PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3 ),
           SUBD_PAS        =SIMP(statut='f',typ='I',defaut=1),
           SUBD_PAS_MINI   =SIMP(statut='f',typ='R'),
           COEF_SUBD_PAS_1 =SIMP(statut='f',typ='R',defaut= 1.0E+0),
         ),

         THETA_3D        =FACT(statut='f',min=1,max='**',
           R_INF           =SIMP(statut='o',typ='R' ),
           R_SUP           =SIMP(statut='o',typ='R' ),
         ),

         IMPR_TABLE      =FACT(statut='f',min=1,max=1,
           regles=(UN_PARMI('TOUT_PARA','NOM_PARA', ),
            PRESENT_PRESENT('TOUT_PARA','ANGLE',    ),
                   UN_PARMI('POSI_CURV_LONGI','POSI_ANGUL',),),
           NOM_PARA        =SIMP(statut='f',typ='TXM',max=4,
                                 into=("TRESCA_MEMBRANE",
                                       "TRESCA_MFLE",
                                       "TRESCA",
                                       "SI_LONG"
                                       ) ),
           TOUT_PARA       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           ANGLE           =SIMP(statut='f',typ='R',max='**' ),
           R_CINTR         =SIMP(statut='f',typ='R',max='**' ),
           POSI_CURV_LONGI =SIMP(statut='f',typ='R',max='**' ),
           POSI_ANGUL      =SIMP(statut='f',typ='R',max='**' ),
         ),

         IMPRESSION      =FACT(statut='f',min=1,max=1,
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="RESULTAT",
                                 into=("RESULTAT","ASTER","IDEAS","CASTEM") ),
                                 
           b_format_ideas  =BLOC(condition="FORMAT=='IDEAS'",fr="version Ideas",
             VERSION         =SIMP(statut='f',typ='I',defaut=5,into=(4,5)),
           ),  

           b_format_castem =BLOC(condition="FORMAT=='CASTEM'",fr="version Castem",
             NIVE_GIBI       =SIMP(statut='f',typ='I',defaut=10,into=(3,10)),
           ),

         ),

         TITRE           =SIMP(statut='f',typ='TXM' ),

         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 20/12/2001   AUTEUR F1BHHAJ J.ANGLES 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE F1BHHAJ J.ANGLES
MACR_ASCOUF_MAIL=MACRO(nom="MACR_ASCOUF_MAIL",op= -19,sd_prod=maillage,
                      fr=" ",docu="U4.CF.10-a",reentrant='n',

         regles=(EXCLUS('SOUS_EPAIS_COUDE','FISS_COUDE','SOUS_EPAIS_MULTI'),),

         EXEC_MAILLAGE   =FACT(statut='o',min=1,max=1,
           LOGICIEL        =SIMP(statut='o',typ='TXM',defaut="GIBI2000",into=("GIBI98","GIBI2000") ),
           UNITE_DATG      =SIMP(statut='f',typ='I',defaut=70),  
           UNITE_MGIB      =SIMP(statut='f',typ='I',defaut=19),  
           NIVE_GIBI       =SIMP(statut='f',typ='I',defaut=10,into=(3,4,5,6,7,8,9,10,11)),
         ),

         TYPE_ELEM       =SIMP(statut='f',typ='TXM',defaut="CU20",into=("CU20","CUB8") ),

         COUDE           =FACT(statut='o',min=1,max=1,
           ANGLE           =SIMP(statut='o',typ='R' ),  
           R_CINTR         =SIMP(statut='o',typ='R' ),  
           L_TUBE_P1       =SIMP(statut='o',typ='R' ),  
           L_TUBE_P2       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),  
           NB_ELEM_EPAIS   =SIMP(statut='f',typ='I',defaut= 3 ),  
           SYME            =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           TRANSFORMEE     =SIMP(statut='o',typ='TXM',defaut="COUDE",into=("COUDE","TUBE") ),
           b_transf_coude  =BLOC(condition = "TRANSFORMEE == 'COUDE' ",
              DEXT            =SIMP(statut='o',typ='R' ),  
              EPAIS           =SIMP(statut='o',typ='R' ),  
              SUR_EPAIS       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),  
              BOL_P2          =SIMP(statut='f',typ='TXM',into=("ASP_MPP","CUVE","GV") ),
           ),
           b_transf_tube   =BLOC(condition = "TRANSFORMEE == 'TUBE' ",
              TRAN_EPAIS      =SIMP(statut='o',typ='TXM',defaut="NON",into=("OUI","NON") ),
              b_trans_epais_oui    =BLOC(condition = "TRAN_EPAIS == 'OUI' ",
                      regles=(ENSEMBLE('ANGL_TETA2','EPAIS_TI'),
                              UN_PARMI('ABSC_CURV_TRAN','POSI_ANGU_TRAN'),),
                      DEXT_T1         =SIMP(statut='o',typ='R' ),  
                      EPAIS_T1        =SIMP(statut='o',typ='R' ),  
                      EPAIS_T2        =SIMP(statut='o',typ='R' ),  
                      EPAIS_TI        =SIMP(statut='f',typ='R' ),  
                      ANGL_TETA1      =SIMP(statut='o',typ='R' ),  
                      ANGL_TETA2      =SIMP(statut='f',typ='R' ),  
                      ABSC_CURV_TRAN  =SIMP(statut='f',typ='R' ),  
                      POSI_ANGU_TRAN  =SIMP(statut='f',typ='R' ),  
              ),
              b_trans_epais_non    =BLOC(condition = "TRAN_EPAIS == 'NON' ",
                      DEXT            =SIMP(statut='o',typ='R' ),  
                      EPAIS           =SIMP(statut='o',typ='R' ),  
                      SUR_EPAIS       =SIMP(statut='f',typ='R',defaut= 0.E+0 ),  
                      BOL_P2          =SIMP(statut='f',typ='TXM',into=("ASP_MPP","CUVE","GV") ),
              ),
           ),
         ),

         SOUS_EPAIS_COUDE=FACT(statut='f',min=1,max=1,
           regles=(UN_PARMI('POSI_CURV_LONGI','POSI_ANGUL'),
                   UN_PARMI('POSI_CURV_CIRC','AZIMUT'),),
           TYPE            =SIMP(statut='o',typ='TXM',into=("AXIS","ELLI") ),
           AXE_CIRC        =SIMP(statut='f',typ='R' ),  
           AXE_LONGI       =SIMP(statut='o',typ='R' ),  
           PROFONDEUR      =SIMP(statut='o',typ='R' ),  
           POSI_CURV_LONGI =SIMP(statut='f',typ='R' ),  
           POSI_ANGUL      =SIMP(statut='f',typ='R' ),  
           POSI_CURV_CIRC  =SIMP(statut='f',typ='R' ),  
           AZIMUT          =SIMP(statut='f',typ='R' ),  
           SOUS_EPAIS      =SIMP(statut='o',typ='TXM',into=("INTERNE","EXTERNE") ),
           NB_ELEM_LONGI   =SIMP(statut='o',typ='I' ),  
           NB_ELEM_CIRC    =SIMP(statut='o',typ='I' ),  
           NB_ELEM_RADI    =SIMP(statut='f',typ='I',defaut= 3 ),  
           EMPREINTE       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         ),

         SOUS_EPAIS_MULTI=FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('POSI_CURV_LONGI','POSI_ANGUL'),
                   UN_PARMI('POSI_CURV_CIRC','AZIMUT'),),
           TYPE            =SIMP(statut='o',typ='TXM',into=("AXIS","ELLI") ),
           AXE_CIRC        =SIMP(statut='f',typ='R' ),  
           AXE_LONGI       =SIMP(statut='o',typ='R' ),  
           PROFONDEUR      =SIMP(statut='o',typ='R' ),  
           POSI_CURV_LONGI =SIMP(statut='f',typ='R' ),  
           POSI_ANGUL      =SIMP(statut='f',typ='R' ),  
           POSI_CURV_CIRC  =SIMP(statut='f',typ='R' ),  
           AZIMUT          =SIMP(statut='f',typ='R' ),  
           SOUS_EPAIS      =SIMP(statut='o',typ='TXM',into=("INTERNE","EXTERNE") ),
           NB_ELEM_LONGI   =SIMP(statut='o',typ='I' ),  
           NB_ELEM_CIRC    =SIMP(statut='o',typ='I' ),  
           EMPREINTE       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         ),

         FISS_COUDE      =FACT(statut='f',min=1,max=1,
           regles=(UN_PARMI('ABSC_CURV','POSI_ANGUL'),),
           AXIS            =SIMP(statut='f',typ='TXM',into=("OUI","NON"),defaut="NON" ),  
           PROFONDEUR      =SIMP(statut='o',typ='R' ),  
           LONGUEUR        =SIMP(statut='o',typ='R' ),  
           ABSC_CURV       =SIMP(statut='f',typ='R' ),  
           POSI_ANGUL      =SIMP(statut='f',typ='R' ),  
           FISSURE         =SIMP(statut='o',typ='TXM',into=("DEB_INT","DEB_EXT") ),
           AZIMUT          =SIMP(statut='f',typ='R',defaut= 90. ),  
           ORIEN           =SIMP(statut='o',typ='R',
                                 into=(45.,-45.,90.,0.E+0) ),
           NB_TRANCHE      =SIMP(statut='o',typ='I' ),  
           NB_SECTEUR      =SIMP(statut='o',typ='I' ),  
           NB_COURONNE     =SIMP(statut='o',typ='I' ),  
           RAYON_TORE      =SIMP(statut='f',typ='R' ),  
           COEF_MULT_RC2   =SIMP(statut='f',typ='R',defaut= 1. ),  
           COEF_MULT_RC3   =SIMP(statut='f',typ='R' ),  
           ANGL_OUVERTURE  =SIMP(statut='f',typ='R',defaut= 0.5 ),  
         ),

         IMPRESSION      =FACT(statut='f',min=1,max='**',
           regles=(PRESENT_PRESENT('FICHIER','UNITE'),),
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="ASTER",   
                                 into=("ASTER","IDEAS","CASTEM") ),
           b_format_ideas  =BLOC(condition="FORMAT=='IDEAS'",fr="version Ideas",
             VERSION         =SIMP(statut='f',typ='I',defaut=5,into=(4,5)),
           ),  
           b_format_castem =BLOC(condition="FORMAT=='CASTEM'",fr="version Castem",
             NIVE_GIBI       =SIMP(statut='f',typ='I',defaut=10,into=(3,10)),
           ),
           FICHIER         =SIMP(statut='f',typ='TXM' ),  
           UNITE           =SIMP(statut='f',typ='I' ),  
         ),

         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 20/12/2001   AUTEUR F1BHHAJ J.ANGLES 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE F1BHHAJ J.ANGLES
def macr_aspic_calc_prod(self,MODELE,CHAM_MATER,CARA_ELEM,FOND_FISS_1,FOND_FISS_2,CHARGE,RESU_THER,**args):
  if MODELE      != None:self.type_sdprod(MODELE,modele)
  if CHAM_MATER  != None:self.type_sdprod(CHAM_MATER,cham_mater)
  if CARA_ELEM   != None:self.type_sdprod(CARA_ELEM,cara_elem)
  if FOND_FISS_1 != None:self.type_sdprod(FOND_FISS_1,fond_fiss)
  if FOND_FISS_2 != None:self.type_sdprod(FOND_FISS_2,fond_fiss)
  if CHARGE      != None:self.type_sdprod(CHARGE,char_meca)
  if RESU_THER   != None:self.type_sdprod(RESU_THER,evol_ther)
  return evol_noli

MACR_ASPIC_CALC=MACRO(nom="MACR_ASPIC_CALC",op=-17,sd_prod=macr_aspic_calc_prod,
                    fr=" ",docu="U4.PC.20-a1",reentrant='n',
         regles=(UN_PARMI('COMP_INCR','COMP_ELAS'),),

         TYPE_MAILLAGE   =SIMP(statut='o',typ='TXM',
                               into=("SAIN_FIN","SAIN_GROS","FISS_COUR_DEB","FISS_COUR_NONDEB","FISS_LONG_DEB",
                                     "FISS_LONG_NONDEB","FISS_AXIS_DEB","FISS_AXIS_NONDEB") ),

         TUBULURE        =FACT(statut='o',min=1,max=1,
           TYPE            =SIMP(statut='o',typ='TXM',into=("TYPE_1","TYPE_2") ),
         ),
         MAILLAGE        =SIMP(statut='o',typ=maillage),
         MODELE          =SIMP(statut='f',typ=(CO,modele)),
         CHAM_MATER      =SIMP(statut='f',typ=(CO,cham_mater)),
         CARA_ELEM       =SIMP(statut='f',typ=(CO,cara_elem)),
         FOND_FISS_1     =SIMP(statut='f',typ=(CO,fond_fiss)),
         FOND_FISS_2     =SIMP(statut='f',typ=(CO,fond_fiss)),
         CHARGE          =SIMP(statut='f',typ=(CO,char_meca)),
         RESU_THER       =SIMP(statut='f',typ=(CO,evol_ther)),

         AFFE_MATERIAU   =FACT(statut='o',min=1,max=3,
           regles=(UN_PARMI('TOUT','GROUP_MA'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",)),
           GROUP_MA        =SIMP(statut='f',typ='TXM',into=("TUBU","CORP","SOUD","SOUDCORP","SOUDTUBU") ),
           MATER           =SIMP(statut='o',typ=mater),
           TEMP_REF        =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           RCCM            =SIMP(statut='o',typ='TXM',into=("OUI","NON")),
         ),

         EQUILIBRE       =FACT(statut='o',min=1,max=1,
           NOEUD           =SIMP(statut='o',typ=no),
         ),

         PRES_REP        =FACT(statut='o',min=1,max=1,
           PRES            =SIMP(statut='o',typ='R'),
           NOEUD           =SIMP(statut='f',typ=no),
           EFFE_FOND       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON")),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
         ),

         ECHANGE         =FACT(statut='f',min=1,max=1,
           COEF_H_TUBU     =SIMP(statut='o',typ=fonction),
           COEF_H_CORP     =SIMP(statut='o',typ=fonction),
           TEMP_EXT        =SIMP(statut='o',typ=fonction),
         ),

         TORS_CORP       =FACT(statut='f',min=1,max=6,
           regles=(AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ'),),
           NOEUD           =SIMP(statut='o',typ=no),
           FX              =SIMP(statut='f',typ='R'),
           FY              =SIMP(statut='f',typ='R'),
           FZ              =SIMP(statut='f',typ='R'),
           MX              =SIMP(statut='f',typ='R'),
           MY              =SIMP(statut='f',typ='R'),
           MZ              =SIMP(statut='f',typ='R'),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
         ),

         TORS_TUBU       =FACT(statut='f',min=1,max=6,
           regles=(AU_MOINS_UN('FX','FY','FZ','MX','MY','MZ'),),
           FX              =SIMP(statut='f',typ='R'),
           FY              =SIMP(statut='f',typ='R'),
           FZ              =SIMP(statut='f',typ='R'),
           MX              =SIMP(statut='f',typ='R'),
           MY              =SIMP(statut='f',typ='R'),
           MZ              =SIMP(statut='f',typ='R'),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
         ),

         COMP_INCR       =FACT(statut='f',min=1,max=1,
           RELATION        =SIMP(statut='o',typ='TXM',into=("VMIS_ISOT_TRAC",) ),
           VMIS_ISOT_TRAC  =SIMP(statut='c',typ='I',defaut= 2,into=( 2 ,) ),
         ),

         COMP_ELAS       =FACT(statut='f',min=1,max=1,
           RELATION        =SIMP(statut='o',typ='TXM',into=("ELAS","ELAS_VMIS_TRAC") ),
           ELAS            =SIMP(statut='c',typ='I',defaut= 1,into=( 1 ,) ),
           ELAS_VMIS_TRAC  =SIMP(statut='c',typ='I',defaut= 1,into=( 1 ,) ),
         ),

         THETA_3D        =FACT(statut='f',min=1,max='**',
           R_INF           =SIMP(statut='o',typ='R'),
           R_SUP           =SIMP(statut='o',typ='R'),
         ),

         OPTION          =SIMP(statut='f',typ='TXM',into=("CALC_G_MAX","CALC_G_MAX_LOCAL") ),
         BORNES          =FACT(statut='f',min=1,max='**',
           NUME_ORDRE      =SIMP(statut='o',typ='I'),
           VALE_MIN        =SIMP(statut='o',typ='R'),
           VALE_MAX        =SIMP(statut='o',typ='R'),
         ),

         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt          =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
           ),
           b_ldlt_mult     =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non iversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
           b_gcpc          =BLOC(condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
#  A quoi sert eps
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           SYME            =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         ),

         CONVERGENCE     =FACT(statut='d',min=1,max=1,
           RESI_GLOB_MAXI  =SIMP(statut='f',typ='R'),
           RESI_GLOB_RELA  =SIMP(statut='f',typ='R'),
           ITER_GLOB_MAXI  =SIMP(statut='f',typ='I',defaut=10),
           ARRET           =SIMP(statut='f',typ='TXM',defaut="OUI"),
           RESI_INTE_RELA  =SIMP(statut='f',typ='R',defaut=1.0E-6),
           ITER_INTE_MAXI  =SIMP(statut='f',typ='I',defaut=10),
           ITER_INTE_PAS   =SIMP(statut='f',typ='I',defaut=0),
           TYPE_MATR_COMP  =SIMP(statut='f',typ='TXM',defaut="TANG_VIT",into=("TANG_VIT",)),
           RESO_INTE       =SIMP(statut='f',typ='TXM',defaut="IMPLICITE",into=("RUNGE_KUTTA_2","RUNGE_KUTTA_4","IMPLICITE")),
         ),

         NEWTON          =FACT(statut='d',min=1,max=1,
           REAC_INCR       =SIMP(statut='f',typ='I',defaut=1),
           PREDICTION      =SIMP(statut='f',typ='TXM',into=("TANGENTE","ELASTIQUE","EXTRAPOL","DEPL_CALCULE")),
           MATRICE         =SIMP(statut='f',typ='TXM',defaut="TANGENTE",into=("TANGENTE","ELASTIQUE")),
           REAC_ITER       =SIMP(statut='f',typ='I',defaut= 0),
         ),

         RECH_LINEAIRE   =FACT(statut='d',min=1,max=1,
           RESI_LINE_RELA  =SIMP(statut='f',typ='R',defaut=1.0E-3),
           ITER_LINE_MAXI  =SIMP(statut='f',typ='I',defaut=3),
         ),

         INCREMENT       =FACT(statut='o',min=1,max=1,
           regles=(EXCLUS('NUME_INST_INIT','INST_INIT'),
                   EXCLUS('NUME_INST_FIN','INST_FIN'),),
           LIST_INST       =SIMP(statut='o',typ=listr8),
           EVOLUTION       =SIMP(statut='f',typ='TXM',defaut="CHRONOLOGIQUE",
                                 into=("CHRONOLOGIQUE","RETROGRADE","SANS",) ),
           NUME_INST_INIT  =SIMP(statut='f',typ='I'),
           INST_INIT       =SIMP(statut='f',typ='R'),
           NUME_INST_FIN   =SIMP(statut='f',typ='I'),
           INST_FIN        =SIMP(statut='f',typ='R'),
           PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3 ),
           SUBD_PAS        =SIMP(statut='f',typ='I',defaut=1),
           SUBD_PAS_MINI   =SIMP(statut='f',typ='R'),
           COEF_SUBD_PAS_1 =SIMP(statut='f',typ='R',defaut= 1.0E+0),
         ),

         PAS_AZIMUT      =SIMP(statut='f',typ='I',defaut=1),

         IMPRESSION      =FACT(statut='f',min=1,max=1,
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="RESULTAT",
                                 into=("RESULTAT","ASTER","CASTEM","IDEAS")),
                                 
           b_format_ideas  =BLOC(condition="FORMAT=='IDEAS'",fr="version Ideas",
             VERSION         =SIMP(statut='f',typ='I',defaut=5,into=(4,5)),
           ),  

           b_format_castem =BLOC(condition="FORMAT=='CASTEM'",fr="version Castem",
             NIVE_GIBI       =SIMP(statut='f',typ='I',defaut=10,into=(3,10)),
           ),

           b_extrac        =BLOC(condition="((FORMAT=='IDEAS')or(FORMAT=='CASTEM'))",
                                 fr="extraction d un champ de grandeur",
             regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST'),),
             NOM_CHAM        =SIMP(statut='f',typ='TXM',max=3,
                                   into=("DEPL","EQUI_ELNO_SIGM","TEMP")),
             
             TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
             INST            =SIMP(statut='f',typ='R',max='**'),
           ),      
         ),

         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),

         TITRE           =SIMP(statut='f',typ='TXM'),
)  ;
# debut entete
#& MODIF COMMANDE  DATE 20/12/2001   AUTEUR F1BHHAJ J.ANGLES 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE F1BHHAJ J.ANGLES
MACR_ASPIC_MAIL=MACRO(nom="MACR_ASPIC_MAIL",op= -16,sd_prod=maillage,reentrant='n',
                    fr=" ",docu="U4.PC.10-a",

         EXEC_MAILLAGE   =FACT(statut='o',min=1,max=1,
           LOGICIEL        =SIMP(statut='o',typ='TXM',defaut="GIBI2000",into=("GIBI98","GIBI2000")),
           UNITE_DATG      =SIMP(statut='f',typ='I',defaut=70),  
           UNITE_MGIB      =SIMP(statut='f',typ='I',defaut=19),  
           NIVE_GIBI       =SIMP(statut='f',typ='I',defaut=10,into=(3,4,5,6,7,8,9,10,11)),
         ),

         TYPE_ELEM       =SIMP(statut='f',typ='TXM',defaut="CU20",into=("CU20","CUB8")),

         RAFF_MAIL       =SIMP(statut='f',typ='TXM',defaut="GROS",into=("GROS","FIN")),

         TUBULURE        =FACT(statut='o',min=1,max=1,
           E_BASE          =SIMP(statut='o',typ='R'),  
           DEXT_BASE       =SIMP(statut='o',typ='R'),  
           L_BASE          =SIMP(statut='o',typ='R'),  
           L_CHANF         =SIMP(statut='o',typ='R'),  
           E_TUBU          =SIMP(statut='o',typ='R'),  
           DEXT_TUBU       =SIMP(statut='o',typ='R'),  
           Z_MAX           =SIMP(statut='o',typ='R'),  
           TYPE            =SIMP(statut='o',typ='TXM',into=("TYPE_1","TYPE_2")),
           L_PENETR        =SIMP(statut='f',typ='R',defaut= 0.0E+0),  
         ),

         SOUDURE         =FACT(statut='o',min=1,max=1,
           H_SOUD          =SIMP(statut='o',typ='R'),  
           ANGL_SOUD       =SIMP(statut='o',typ='R'),  
           JEU_SOUD        =SIMP(statut='o',typ='R'),  
         ),

         CORPS           =FACT(statut='o',min=1,max=1,
           E_CORP          =SIMP(statut='o',typ='R'),  
           DEXT_CORP       =SIMP(statut='o',typ='R'),  
           X_MAX           =SIMP(statut='o',typ='R'),  
         ),

         FISS_SOUDURE    =FACT(statut='f',min=1,max=1,
           TYPE            =SIMP(statut='o',typ='TXM',into=("LONGUE","COURTE")),
           AXIS            =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
           PROFONDEUR      =SIMP(statut='o',typ='R'),  
           LONGUEUR        =SIMP(statut='f',typ='R'),  
           AZIMUT          =SIMP(statut='o',typ='R'),  
           RAYON_TORE      =SIMP(statut='f',typ='R'),  
           POSITION        =SIMP(statut='o',typ='TXM',into=("DROIT","INCLINE")),
           FISSURE         =SIMP(statut='o',typ='TXM',into=("DEB_INT","DEB_EXT","NON_DEB","TRAVERS")),
           LIGA_INT        =SIMP(statut='f',typ='R'),  
           ANGL_OUVERTURE  =SIMP(statut='f',typ='R',defaut= 0.0E+0),  
           COEF_MULT_RC1   =SIMP(statut='f',typ='R'),  
           COEF_MULT_RC2   =SIMP(statut='f',typ='R'),  
           COEF_MULT_RC3   =SIMP(statut='f',typ='R'),  
           NB_TRANCHE      =SIMP(statut='f',typ='I'),  
           NB_SECTEUR      =SIMP(statut='f',typ='I'),  
           NB_COURONNE     =SIMP(statut='f',typ='I'),  
         ),

         IMPRESSION      =FACT(statut='f',min=1,max='**',
           regles=(PRESENT_PRESENT('FICHIER','UNITE'),),
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="ASTER",into=("ASTER","IDEAS","CASTEM")),

           b_format_ideas  =BLOC(condition="FORMAT=='IDEAS'",fr="version Ideas",
             VERSION         =SIMP(statut='f',typ='I',defaut=5,into=(4,5)),
           ),  

           b_format_castem =BLOC(condition="FORMAT=='CASTEM'",fr="version Castem",
             NIVE_GIBI       =SIMP(statut='f',typ='I',defaut=10,into=(3,10)),
           ),
           FICHIER         =SIMP(statut='f',typ='TXM'),  
           UNITE           =SIMP(statut='f',typ='I'),  
         ),

         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 19/12/2001   AUTEUR CIBHHPD D.NUNEZ 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MACR_ELEM_DYNA=OPER(nom="MACR_ELEM_DYNA",op=  81,sd_prod=macr_elem_dyna,
                    fr="D�finition d un macro �l�ment pour analyse modale ou harmonique par sous structuration dynamique",
                    docu="U4.65.01-d",reentrant='n',
         regles=(EXCLUS('MATR_AMOR','AMOR_REDUIT' ),),
         BASE_MODALE     =SIMP(statut='o',typ=base_modale ),
         MATR_RIGI       =SIMP(statut='f',typ=matr_asse_depl_r ),
         MATR_MASS       =SIMP(statut='f',typ=matr_asse_depl_r ),
         MATR_AMOR       =SIMP(statut='f',typ=matr_asse_depl_r ),
         AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),         
         OPTION          =SIMP(statut='f',typ='TXM',defaut="CLASSIQUE",into=("CLASSIQUE","RITZ",
                          "DIAG_MASS") ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MACR_ELEM_STAT=OPER(nom="MACR_ELEM_STAT",op=86,sd_prod=macr_elem_stat,docu="U4.62.01-e",reentrant='f',
                    fr="D�finition d un macro-�l�ment pour l analyse statique par sous structuration",
        regles=(AU_MOINS_UN('DEFINITION','RIGI_MECA','MASS_MECA','CAS_CHARGE'),
                ENSEMBLE('DEFINITION','EXTERIEUR'),),
         DEFINITION      =FACT(statut='f',min=1,max=1,
           MODELE          =SIMP(statut='o',typ=modele),
           CHAM_MATER      =SIMP(statut='f',typ=cham_mater),
           CARA_ELEM       =SIMP(statut='f',typ=cara_elem),
           CHAR_MACR_ELEM  =SIMP(statut='f',typ=char_meca),
           INST            =SIMP(statut='f',typ='R',defaut=0.0E+0 ),
           NMAX_CAS        =SIMP(statut='f',typ='I',defaut=10),
           NMAX_CHAR       =SIMP(statut='f',typ='I',defaut=10),
         ),
         EXTERIEUR       =FACT(statut='f',min=1,max=1,
           regles=(AU_MOINS_UN('NOEUD','GROUP_NO'),),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
         ),
         RIGI_MECA       =FACT(statut='f',min=1,max=1,
         ),
         MASS_MECA       =FACT(statut='f',min=1,max=1,
           BIDO1           =SIMP(statut='f',typ='I',defaut=0),
         ),
         CAS_CHARGE      =FACT(statut='f',min=1,max='**',
           NOM_CAS         =SIMP(statut='o',typ='TXM'),
           SUIV            =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON")),
           CHARGE          =SIMP(statut='f',typ=char_meca,max='**'),
           INST            =SIMP(statut='f',typ='R',defaut=0.E+0),
         ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MACR_GOUJ2E_CALC=MACRO(nom="MACR_GOUJ2E_CALC",op=-23,sd_prod=evol_noli,
                      fr=" ",docu="U4.GJ.20-a",reentrant='n',
         MAILLAGE        =SIMP(statut='o',typ=maillage),
         DEFI_GOUJ       =FACT(statut='o',min=01,max=01,
           TYPE            =SIMP(statut='o',typ='TXM',into=("M33","M64","M90","M115","M155","M180","M186")),
           VARIANTE        =SIMP(statut='o',typ='TXM',into=("A","B","C","D","E","F","G","H","I","J","K","L","M",  
                                                            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z")),
           FILET_TRONQUE   =SIMP(statut='f',typ='I',max='**'),  
           FILET_TRONQA    =SIMP(statut='f',typ='I',max='**'),  
           FILET_TRONQB    =SIMP(statut='f',typ='I',max='**'),  
           FILET_JEU_HT    =SIMP(statut='f',typ='I',max='**'),  
           FILET_JEU_HTA   =SIMP(statut='f',typ='I',max='**'),  
           FILET_JEU_HTB   =SIMP(statut='f',typ='I',max='**'),  
         ),
         EXCIT           =FACT(statut='o',min=01,max=01,
           TYPE_BLOCAGE    =SIMP(statut='o',typ='I',defaut=2,into=(1,2,3)),
           FORCE_GOUJ      =SIMP(statut='o',typ='R'),  
         ),
         CALCUL          =FACT(statut='o',min=01,max=01,
           TYPE_CALCUL     =SIMP(statut='o',typ='TXM',into=("ELASTIQUE","ELASTOPLASTIQUE")),
           NB_INCR         =SIMP(statut='o',typ='I'),  
         ),
         IMPRESSION      =FACT(statut='f',min=01,max=01,
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="TABLE",    
                                 into=("RESULTAT","IDEAS","ASTER","CASTEM","ENSIGHT","MED","TABLE")),
           VERSION         =SIMP(statut='f',typ='I',defaut=5,into=(4,5)),
         ),
         TITRE           =SIMP(statut='f',typ='TXM'),  
         INFO            =SIMP(statut='f',typ='I',defaut=1 ,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 03/10/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MACR_GOUJ2E_MAIL=MACRO(nom="MACR_GOUJ2E_MAIL",op= -22,sd_prod=maillage,
                      fr=" ",docu="U4.GJ.10-a",reentrant='n',
         EXEC_MAILLAGE   =FACT(statut='o',min=1,max=1,
           LOGICIEL        =SIMP(statut='o',typ='TXM',defaut="GIBI2000",into=("GIBI98","GIBI2000") ),
           UNITE_DATG      =SIMP(statut='f',typ='I',defaut=70),  
           UNITE_MGIB      =SIMP(statut='f',typ='I',defaut=19),  
           NIVE_GIBI       =SIMP(statut='f',typ='I',defaut=10,into=(3,4,5,6,7,8,9,10)),
         ),
         DEFI_GOUJ       =FACT(statut='o',min=1,max=1,
           TYPE            =SIMP(statut='o',typ='TXM',into=("M33","M64","M90","M115","M155","M180","M186")),
           VARIANTE        =SIMP(statut='o',typ='TXM',into=("A","B","C","D","E","F","G","H","I","J","K","L","M",  
                                                            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z")), 
         ),
         GEOM_GOUJ_BRID  =FACT(statut='o',min=1,max=1,
           NB_FILET        =SIMP(statut='o',typ='I'),  
           H_CORP_BRID     =SIMP(statut='o',typ='R'),  
           R_EXT_BRID      =SIMP(statut='o',typ='R'),  
           H_HAUT_BRID     =SIMP(statut='f',typ='R',defaut=0.0E+0),  
           H_BAS_BRID      =SIMP(statut='f',typ='R',defaut= 0.0E+0),  
           FILET_ABST      =SIMP(statut='f',typ='I',max='**'),  
         ),
         IMPRESSION      =FACT(statut='f',min=1,max=1,
           regles=(PRESENT_PRESENT('FICHIER','UNITE'),),
           FORMAT          =SIMP(statut='f',typ='TXM',defaut="RESULTAT",    
                                 into=("RESULTAT","IDEAS","ASTER","CASTEM","ENSIGHT","MED")),
           FICHIER         =SIMP(statut='f',typ='TXM'),  
           UNITE           =SIMP(statut='f',typ='I'),  
           VERSION         =SIMP(statut='f',typ='I',defaut=5,into=(4,5)),
           NIVE_GIBI       =SIMP(statut='f',typ='I',defaut=10,into=(3,10)),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 25/01/2002   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE GNICOLAS G.NICOLAS
MACR_INFO_MAIL=MACRO(nom="MACR_INFO_MAIL",op=-24,docu="U7.03.02-a",
                     fr="Donner des informations sur un maillage.",
                     ang="To give information about a mesh.",
#
# 1. Le niveau d'information
#
         INFO           = SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
#
# 2. Version de HOMARD
#
         VERSION_HOMARD = SIMP(statut='f',typ='TXM',defaut="V5_1",
                               into=("V5_1", "V5_N","V5_N_PERSO"),
                           fr="Version de HOMARD",
                           ang="HOMARD release"),
#
# 3. Langue des messages issus de HOMARD
#
         LANGUE = SIMP(statut='f',typ='TXM',defaut="FRANCAIS",    
                               into=("FRANCAIS","FRENCH","ANGLAIS","ENGLISH",),
                           fr="Langue des messages issus de HOMARD.",
                           ang="Language for HOMARD messages." ),
#
# 4. Le nom du maillage a analyser
#
         MAILLAGE       = SIMP(statut='o',typ=maillage,
                           fr="Maillage � analyser.",
                           ang="Mesh to be checked." ),
#
# 5. Les options ; par defaut, on ne fait que les nombres
# 5.1. Nombre de noeuds et elements
#
         NOMBRE         = SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON"),
                          fr="Nombre de noeuds et �l�ments du maillage",
                          ang="Number of nodes and elements in the mesh" ),
#
# 5.2. Determination de la qualite des elements du maillage
#
         QUALITE        = SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Qualit� du maillage",
                          ang="Mesh quality" ),
#
# 5.3. Connexite du maillage
#
         CONNEXITE      = SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Connexit� du maillage.",
                          ang="Mesh connexity." ),
#
# 5.4. Taille des sous-domaines du maillage
#
         TAILLE         = SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Tailles des sous-domaines du maillage.",
                          ang="Sizes of mesh sub-domains." ),
#
# 5.5. Controle de la non-interpenetration des elements
#
         INTERPENETRATION=SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON"),
                          fr="Controle de la non interp�n�tration des �l�ments.",
                          ang="Overlapping checking." ),
#
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE JMBHH01 J.M.PROIX
MACRO_CARA_POUTRE=MACRO(nom="MACRO_CARA_POUTRE",op=-11,sd_prod=tabl_cara_geom,
                       docu="U4.42.02-c",reentrant='n',
                       fr="caract�ristiques d'une section transversale de poutre � partir d'un maillage 2D",
         regles=(EXCLUS('SYME_X','GROUP_MA_BORD'),
                 EXCLUS('SYME_Y','GROUP_MA_BORD'),
                 ENSEMBLE('LONGUEUR','LIAISON','MATERIAU') ,),
         UNITE_MAILLAGE  =SIMP(statut='f',typ='I',defaut= 20 ),  
         SYME_X          =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
         SYME_Y          =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
         GROUP_MA_BORD   =SIMP(statut='f',typ=grma,max='**'),
         GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         ORIG_INER       =SIMP(statut='f',typ='R',max='**'),  
         NOEUD           =SIMP(statut='f',typ=no,max='**'),
         GROUP_MA_INTE   =SIMP(statut='f',typ=grma,max='**'),
         LONGUEUR        =SIMP(statut='f',typ='R'),  
         MATERIAU        =SIMP(statut='f',typ=mater),
         LIAISON         =SIMP(statut='f',typ='TXM',into=("ROTULE","ENCASTREMENT")),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MACRO_CHAR_F_U=MACRO(nom="MACRO_CHAR_F_U",op=-15,sd_prod=char_meca,
                    fr=" ",docu="U4.72.07-a",reentrant='n',
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater),
         CHARGE          =SIMP(statut='o',typ=char_meca),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),
         COEF_IMPO       =SIMP(statut='f',typ='R',defaut=1.0E+0),  
         NUME_LAGR       =SIMP(statut='f',typ='TXM',defaut="APRES",into=("NORMAL","APRES")),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
def macro_elas_mult_prod(self,NUME_DDL,CAS_CHARGE,**args ):
  self.type_sdprod(NUME_DDL,nume_ddl)
  if CAS_CHARGE[0]['NOM_CAS']      != None : return mult_elas
  if CAS_CHARGE[0]['MODE_FOURIER'] != None : return fourier_elas
  raise AsException("type de concept resultat non prevu")

MACRO_ELAS_MULT=MACRO(nom="MACRO_ELAS_MULT",op=-10,sd_prod=macro_elas_mult_prod,docu="U4.51.02-c1",reentrant='f',
         regles=(UN_PARMI('CHAR_MECA_GLOBAL','CHAR_CINE_GLOBAL','LIAISON_DISCRET', ),),
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='f',typ=cham_mater),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),
         NUME_DDL        =SIMP(statut='f',typ=(CO,nume_ddl)),# CO()
         CHAR_MECA_GLOBAL=SIMP(statut='f',typ=char_meca,max='**'),
         CHAR_CINE_GLOBAL=SIMP(statut='f',typ=char_meca,max='**'),
         LIAISON_DISCRET =SIMP(statut='f',typ='TXM',into=("OUI",)),
         CAS_CHARGE      =FACT(statut='o',min=1,max='**',
           regles=(UN_PARMI('NOM_CAS','MODE_FOURIER'),
                   UN_PARMI('CHAR_MECA','CHAR_CINE','VECT_ASSE'),),
           NOM_CAS         =SIMP(statut='f',typ='TXM' ),
           MODE_FOURIER    =SIMP(statut='f',typ='I' ),
           TYPE_MODE       =SIMP(statut='f',typ='TXM',defaut="SYME",into=("SYME","ANTI","TOUS") ),
           CHAR_MECA       =SIMP(statut='f',typ=char_meca,max='**'),
           CHAR_CINE       =SIMP(statut='f',typ=char_meca,max='**'),
           OPTION          =SIMP(statut='f',typ='TXM',max='**',
                                 into=("EFGE_ELNO_DEPL","EPOT_ELEM_DEPL","SIGM_ELNO_DEPL","SIEF_ELGA_DEPL",
                                       "SIGM_ELNO_CART","EFGE_ELNO_CART","DEGE_ELNO_DEPL","EPSI_ELNO_DEPL",
                                       "EPSI_ELGA_DEPL","EPSG_ELNO_DEPL","EPSG_ELGA_DEPL","EPSP_ELNO","EPSP_ELGA",
                                       "ECIN_ELEM_DEPL","FLUX_ELGA_TEMP","FLUX_ELNO_TEMP","SOUR_ELGA_ELEC",
                                       "PRES_ELNO_DBEL","PRES_ELNO_REEL","PRES_ELNO_IMAG","INTE_ELNO_ACTI",
                                       "INTE_ELNO_REAC","SIGM_NOZ1_ELGA","ERRE_ELEM_NOZ1","SIGM_NOZ2_ELGA",
                                       "ERRE_ELEM_NOZ2","VNOR_ELEM_DEPL","ERRE_ELNO_ELGA","SIRE_ELNO_DEPL",
                                       "ERRE_ELGA_NORE","EQUI_ELNO_SIGM","EQUI_ELGA_SIGM","EQUI_ELNO_EPSI",
                                       "EQUI_ELGA_EPSI","FORC_NODA","REAC_NODA","EPSI_NOEU_DEPL","SIGM_NOEU_DEPL",
                                       "EFGE_NOEU_DEPL","EQUI_NOEU_SIGM","EQUI_NOEU_EPSI","FLUX_NOEU_TEMP") ),
           NUME_COUCHE     =SIMP(statut='f',typ='I',defaut=1),
           NIVE_COUCHE     =SIMP(statut='f',typ='TXM',defaut="MOY",into=("SUP","INF","MOY")),
           SOUS_TITRE      =SIMP(statut='f',typ='TXM',max='**'),
           VECT_ASSE       =SIMP(statut='f',typ=cham_no_depl_r),
         ),
#
         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT") ),
           b_mult_front    = BLOC ( condition = "METHODE == 'MULT_FRONT' ",
                                    fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt          =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
            ),
           b_ldlt_mult     =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non inversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2)),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MACRO_MADMACS=MACRO(nom="MACRO_MADMACS",op=-9,docu="U7.03.21-c",
                    fr="Impression au format IDEAS des donn�es pour chainage entre Code_Aster et MADMACS",
         regles=(UN_PARMI('MATR_ELEM_RIGI','MATR_RIGI'),
                 UN_PARMI('MATR_ELEM_MASS','MATR_MASS'),
                 PRESENT_ABSENT('MATR_ELEM_AMOR','MATR_AMOR'),),
         FICHIER         =SIMP(statut='f',typ='TXM' ),  
         FORMAT          =SIMP(statut='f',typ='TXM',defaut="IDEAS",into=("IDEAS",)),
         VERSION         =SIMP(statut='f',typ='I',defaut=5,into=(5,)),
         MAILLAGE        =SIMP(statut='o',typ=maillage),
         NUME_DDL        =SIMP(statut='o',typ=nume_ddl),
         CHARGE          =SIMP(statut='o',typ=char_meca,max='**'),
         MATR_ELEM_RIGI  =SIMP(statut='f',typ=matr_elem_depl_r),
         MATR_RIGI       =SIMP(statut='f',typ=matr_asse_depl_r),
         MATR_ELEM_MASS  =SIMP(statut='f',typ=matr_elem_depl_r),
         MATR_MASS       =SIMP(statut='f',typ=matr_asse_depl_r),
         MATR_ELEM_AMOR  =SIMP(statut='f',typ=matr_elem_depl_r),
         MATR_AMOR       =SIMP(statut='f',typ=matr_asse_depl_r),
         MODE_MECA       =SIMP(statut='o',typ=mode_meca),
         NMAX_MODE       =SIMP(statut='f',typ='I',defaut=10),  
         INTERFACE       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NOEUD','GROUP_NO'),
                   UN_PARMI('DDL_ACTIF','MASQUE'),),
           NOM             =SIMP(statut='o',typ='TXM'),  
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           DDL_ACTIF       =SIMP(statut='f',typ='TXM',max='**'),  
           MASQUE          =SIMP(statut='f',typ='TXM',max='**'),  
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def macro_matr_ajou_prod(self,MATR_AMOR_AJOU,MATR_MASS_AJOU,MATR_RIGI_AJOU,FORC_AJOU,**args):
  self.type_sdprod(MATR_AMOR_AJOU,matr_asse_depl_r)
  self.type_sdprod(MATR_MASS_AJOU,matr_asse_depl_r)
  self.type_sdprod(MATR_RIGI_AJOU,matr_asse_depl_r)
  if FORC_AJOU != None:
    for m in FORC_AJOU:
      self.type_sdprod(m['VECTEUR'],vect_asse_gene)

  return None

MACRO_MATR_AJOU=MACRO(nom="MACRO_MATR_AJOU",op=-13,docu="U4.66.11-b",sd_prod=macro_matr_ajou_prod,
      regles=(AU_MOINS_UN('MODE_MECA','DEPL_IMPO','MODELE_GENE'),
              AU_MOINS_UN('MATR_MASS_AJOU','MATR_AMOR_AJOU','MATR_RIGI_AJOU'),
              EXCLUS('MODE_MECA','DEPL_IMPO','MODELE_GENE'),
              EXCLUS('MONO_APPUI','MODE_STAT',),
             ),
         MAILLAGE        =SIMP(statut='o',typ=maillage),
         GROUP_MA_FLUIDE =SIMP(statut='o',typ=grma),
         GROUP_MA_INTERF =SIMP(statut='o',typ=grma),
         MODELISATION    =SIMP(statut='o',typ='TXM',into=("PLAN","AXIS","3D")),
         FLUIDE          =FACT(statut='o',min=1,max='**',
           RHO             =SIMP(statut='o',typ='R'),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",)),
           GROUP_MA        =SIMP(statut='f',typ=grma),
           MAILLE          =SIMP(statut='f',typ=ma),
         ),
         DDL_IMPO        =FACT(statut='o',min=1,max='**',
           regles=(UN_PARMI('NOEUD','GROUP_NO'),
                   UN_PARMI('PRES_FLUIDE','PRES_SORTIE'),),
           NOEUD           =SIMP(statut='f',typ=no),
           GROUP_NO        =SIMP(statut='f',typ=grno),
           PRES_FLUIDE     =SIMP(statut='f',typ='R'),
           PRES_SORTIE     =SIMP(statut='f',typ='R'),
         ),
         ECOULEMENT      =FACT(statut='f',min=1,max='**',
           GROUP_MA_1      =SIMP(statut='o',typ=grma),
           GROUP_MA_2      =SIMP(statut='o',typ=grma),
           VNOR_1          =SIMP(statut='o',typ='R'),
           VNOR_2          =SIMP(statut='f',typ='R'),
           POTENTIEL       =SIMP(statut='f',typ=evol_ther),
         ),
         MODE_MECA       =SIMP(statut='f',typ=mode_meca),
         DEPL_IMPO       =SIMP(statut='f',typ=cham_no_depl_r),
         MODELE_GENE     =SIMP(statut='f',typ=modele_gene),
         NUME_DDL_GENE   =SIMP(statut='f',typ=nume_ddl_gene),
         DIST_REFE       =SIMP(statut='f',typ='R',defaut= 1.0E-2),
         MATR_MASS_AJOU  =SIMP(statut='f',typ=(CO,matr_asse)),
         MATR_RIGI_AJOU  =SIMP(statut='f',typ=(CO,matr_asse)),
         MATR_AMOR_AJOU  =SIMP(statut='f',typ=(CO,matr_asse)),
         MONO_APPUI      =SIMP(statut='f',typ='TXM',into=("OUI",),),
         MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc,),),
         FORC_AJOU       =FACT(statut='f',min=1,max='**',
           DIRECTION     =SIMP(statut='o',typ='R',max=3),
           NOEUD         =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO      =SIMP(statut='f',typ=grno,max='**'),
           VECTEUR       =SIMP(statut='o',typ=(CO,vect_asse_gene)),
         ),
         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt         =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
           ),
           b_ldlt_mult    =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non iversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
           b_gcpc          =BLOC(condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
#  A quoi sert eps
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
         NOEUD_DOUBLE    =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
         AVEC_MODE_STAT  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON")),
) ;
#& MODIF COMMANDE  DATE 23/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
#% RESPONSABLE VABHHTS J.PELLET

def macro_matr_asse_ops(self,MODELE,CHAM_MATER,CARA_ELEM,MATR_ASSE,
                        SOLVEUR,NUME_DDL,CHARGE,INST,**args):
  """
     Ecriture de la macro MACRO_MATR_ASSE
  """
  ier=0
  # On met le mot cle NUME_DDL dans une variable locale pour le proteger
  numeddl=NUME_DDL
  # On importe les definitions des commandes a utiliser dans la macro
  # Le nom de la variable doit etre obligatoirement le nom de la commande
  CALC_MATR_ELEM=self.get_cmd('CALC_MATR_ELEM')
  NUME_DDL      =self.get_cmd('NUME_DDL')
  ASSE_MATRICE  =self.get_cmd('ASSE_MATRICE')
  # La macro compte pour 1 dans la numerotation des commandes
  self.icmd=1

  if SOLVEUR:
    methode=SOLVEUR['METHODE']
    if methode=='LDLT':
      if SOLVEUR['RENUM']:
         renum=SOLVEUR['RENUM']
      else:
         renum='RCMK'
      if renum not in ('SANS','RCMK'):
        ier=ier+1
        self.cr.fatal("Avec methode LDLT, RENUM doit etre SANS ou RCMK.")
        return ier
    elif methode=='MULT_FRONT':
      if SOLVEUR['RENUM']:
         renum=SOLVEUR['RENUM']
      else:
         renum='MDA'
      if renum not in ('MDA','MD','METIS'):
        ier=ier+1
        self.cr.fatal("Avec methode MULT_FRONT, RENUM doit etre MDA, MD ou RCMK.")
        return ier
    elif methode=='GCPC':
      if SOLVEUR['RENUM']:
         renum=SOLVEUR['RENUM']
      else:
         renum='SANS'
      if renum not in ('SANS','RCMK'):
        ier=ier+1
        self.cr.fatal("Avec methode GCPC, RENUM doit etre SANS ou RCMK.")
        return ier
  else:
    methode='MULT_FRONT'
    renum  ='MDA'

  if numeddl in self.sdprods:
    # Si le concept numeddl est dans self.sdprods
    # il doit etre  produit par la macro
    # il faudra donc appeler la commande NUME_DDL
    lnume = 1
  else:
    lnume = 0
  lrigel = 0
  lmasel = 0

  iocc=0
  for m in MATR_ASSE:
    iocc=iocc+1
    option=m['OPTION']
    if iocc == 1 and lnume == 1 and option not in ('RIGI_MECA','RIGI_MECA_LAGR',
                                                   'RIGI_THER','RIGI_ACOU')      :
      ier=ier+1
      self.cr.fatal("LA PREMIERE OPTION DOIT ETRE RIGI_MECA OU RIGI_THER OU RIGI_ACOU OU RIGI_MECA_LAGR")
      return ier

    if m['SIEF_ELGA']!=None and option!='RIGI_GEOM':
      ier=ier+1
      self.cr.fatal("SIEF_ELGA N EST ADMIS QU AVEC L OPTION RIGI_GEOM")
      return ier

    if m['MODE_FOURIER']!=None and option not in ('RIGI_MECA','RIGI_FLUI_STRU','RIGI_THER'):
      ier=ier+1
      self.cr.fatal("MODE_FOURIER N EST ADMIS QU AVEC UNE DES OPTIONS RIGI_MECA RIGI_FLUI_STRU RIGI_THER")
      return ier

    if (m['THETA']!=None or m['PROPAGATION']!=None) and option!='RIGI_MECA_LAGR':
      ier=ier+1
      self.cr.fatal("PROPAGATION ET,OU THETA NE SONT ADMIS QU AVEC L OPTION RIGI_MECA_LAGR")
      return ier

    motscles={'OPTION':option}
    if option == 'AMOR_MECA':
       if (not lrigel or not lmasel):
          ier=ier+1
          self.cr.fatal("""POUR CALCULER AMOR_MECA, IL FAUT AVOIR CALCULE
                           RIGI_MECA ET MASS_MECA AUPARAVANT (DANS LE MEME APPEL)""")
          return ier
       if CHAM_MATER != None:
          motscles['RIGI_MECA']   =rigel
          motscles['MASS_MECA']   =masel
    if CHARGE     != None:
       if option[0:9] not in ('MASS_THER','RIGI_GEOM','MASS_ID_M'):
                           motscles['CHARGE']      =CHARGE
    if CHAM_MATER != None: motscles['CHAM_MATER']  =CHAM_MATER
    if CARA_ELEM  != None: motscles['CARA_ELEM']   =CARA_ELEM
    if INST       != None: motscles['INST']        =INST
    if m['SIEF_ELGA']   :  motscles['SIEF_ELGA']   =m['SIEF_ELGA']
    if m['MODE_FOURIER']:  motscles['MODE_FOURIER']=m['MODE_FOURIER']
    if m['THETA']       :  motscles['THETA']       =m['THETA']
    if m['PROPAGATION'] :  motscles['PROPAGATION'] =m['PROPAGATION']

    __a=CALC_MATR_ELEM(MODELE=MODELE,**motscles)

    if option == 'RIGI_MECA':
      rigel  = __a
      lrigel = 1
    if option == 'MASS_MECA':
      masel  = __a
      lmasel = 1

    if lnume and option in ('RIGI_MECA','RIGI_THER','RIGI_ACOU','RIGI_MECA_LAGR'):
      self.DeclareOut('num',numeddl)
      # On peut passer des mots cles egaux a None. Ils sont ignores
      num=NUME_DDL(MATR_RIGI=__a,METHODE=methode,RENUM=renum)
    else:
      num=numeddl

    self.DeclareOut('mm',m['MATRICE'])
    mm=ASSE_MATRICE(MATR_ELEM=__a,NUME_DDL=num)
  return ier


def macro_matr_asse_prod(self,NUME_DDL,MATR_ASSE,**args):
  if not MATR_ASSE:  raise AsException("Impossible de typer les concepts resultats")
  if not NUME_DDL:  raise AsException("Impossible de typer les concepts resultats")
  self.type_sdprod(NUME_DDL,nume_ddl)
  for m in MATR_ASSE:
    opti=m['OPTION']

    if opti in ( "RIGI_MECA","RIGI_FLUI_STRU","RIGI_MECA_LAGR" ,
       "MASS_MECA" , "MASS_FLUI_STRU" ,"RIGI_GEOM" ,"RIGI_ROTA",
       "AMOR_MECA","IMPE_MECA","MASS_ID_MDEP_R","MASS_ID_MDNS_R",
       "ONDE_FLUI","MASS_MECA_DIAG" ) : t=matr_asse_depl_r

    if opti in ( "RIGI_ACOU","MASS_ACOU","AMOR_ACOU",) : t=matr_asse_pres_c

    if opti in ( "RIGI_THER","MASS_THER","RIGI_THER_CONV" ,
       "RIGI_THER_CONV_D","MASS_ID_MTEM_R","MASS_ID_MTNS_R",) : t=matr_asse_temp_r

    if opti == "RIGI_MECA_HYST"   : t= matr_asse_depl_c

    self.type_sdprod(m['MATRICE'],t)
  return None

MACRO_MATR_ASSE=MACRO(nom="MACRO_MATR_ASSE",op=macro_matr_asse_ops,docu="U4.61.21-c",
                      sd_prod=macro_matr_asse_prod,
                      fr="Calcul des matrices assembl�es (matr_asse_gd) par exemple de rigidit�, de masse ",
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='f',typ=cham_mater),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),
         CHARGE          =SIMP(statut='f',typ=(char_meca,char_ther,char_acou)),
         INST            =SIMP(statut='f',typ='R'),
         NUME_DDL        =SIMP(statut='o',typ=(nume_ddl,CO)),
         SOLVEUR         =FACT(statut='d',min=01,max=01,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",
                                 into=("LDLT","MULT_FRONT","GCPC")),
           RENUM           =SIMP(statut='f',typ='TXM',into=("SANS","RCMK","MD","MDA","METIS")),
         ),
         MATR_ASSE       =FACT(statut='o',min=01,max='**',
           MATRICE         =SIMP(statut='o',typ=(matr_asse,CO)),
           OPTION          =SIMP(statut='o',typ='TXM',
                                 into=("RIGI_MECA","MASS_MECA","MASS_MECA_DIAG",
                                       "AMOR_MECA","RIGI_MECA_HYST","IMPE_MECA",
                                       "ONDE_FLUI","RIGI_FLUI_STRU","MASS_FLUI_STRU",
                                       "RIGI_ROTA","RIGI_GEOM","RIGI_MECA_LAGR",
                                       "RIGI_THER","MASS_THER",
                                       "RIGI_ACOU","MASS_ACOU","AMOR_ACOU",
                                       "MASS_ID_MTEM_R","MASS_ID_MTNS_R","MASS_ID_MDEP_R","MASS_ID_MDNS_R",)
                                 ),
           SIEF_ELGA       =SIMP(statut='f',typ=cham_elem_sief_r),
           MODE_FOURIER    =SIMP(statut='f',typ='I'),
           THETA           =SIMP(statut='f',typ=theta_geom),
           PROPAGATION     =SIMP(statut='f',typ='R'),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MACRO_MISS_3D=MACRO(nom="MACRO_MISS_3D",op=-18,fr=" ",docu="U7.03.11-a",
         OPTION          =FACT(statut='o',min=01,max=01,
           regles=(UN_PARMI('TOUT','MODULE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",)),
           MODULE          =SIMP(statut='f',typ='TXM',into=("PRE_MISS","MISS_EVOL","MISS_IMPE")),
         ),
         PROJET          =SIMP(statut='o',typ='TXM'),  
         REPERTOIRE      =SIMP(statut='f',typ='TXM'),  
         UNITE_IMPR_ASTER=SIMP(statut='f',typ='I',defaut=25),  
         UNITE_OPTI_MISS =SIMP(statut='f',typ='I',defaut=26),  
         UNITE_MODELE_SOL=SIMP(statut='f',typ='I',defaut=27),  
         UNITE_RESU_IMPE =SIMP(statut='f',typ='I',defaut=30),  
)  ;
#& MODIF COMMANDE  DATE 23/01/2002   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def macro_mode_meca_prod(self,MATR_A,MATR_B,**args ):
  self.type_sdprod(MATR_A,matr_asse_depl_r)
  self.type_sdprod(MATR_B,matr_asse_depl_r)
  return mode_meca

MACRO_MODE_MECA=MACRO(nom="MACRO_MODE_MECA",op= -12,sd_prod=macro_mode_meca_prod,
                     docu="U4.52.02-c",reentrant='n',
         MATR_A          =SIMP(statut='o',typ=(CO,matr_asse_depl_r) ),
         MATR_B          =SIMP(statut='o',typ=(CO,matr_asse_depl_r) ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
#  ce mot cle ne devrait il pas etre dans calc_freq  
         METHODE         =SIMP(statut='f',typ='TXM',defaut="SORENSEN",    
                               into=("TRI_DIAG","JACOBI","SORENSEN",) ),
         OPTION          =SIMP(statut='f',typ='TXM',defaut="SANS",    
                               into=("MODE_RIGIDE","SANS") ),
         CALC_FREQ       =FACT(statut='d',min=00,max=01,
           regles=(UN_PARMI('FREQ','FREQ_MAX'),
                   PRESENT_PRESENT('FREQ_MIN','FREQ_MAX'),
                   PRESENT_PRESENT('FREQ_MAX','NB_BLOC_FREQ'),
                   EXCLUS('DIM_SOUS_ESPACE','COEF_DIM_ESPACE'),),
           FREQ            =SIMP(statut='f',typ='R',max='**' ),  
           FREQ_MIN        =SIMP(statut='f',typ='R' ),  
           FREQ_MAX        =SIMP(statut='f',typ='R' ),  
           NB_BLOC_FREQ    =SIMP(statut='f',typ='I' ),  
           NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 10 ),  
           DIM_SOUS_ESPACE =SIMP(statut='f',typ='I' ),  
           COEF_DIM_ESPACE =SIMP(statut='f',typ='I' ),
           NPREC_SOLVEUR   =SIMP(statut='f',typ='I',defaut= 8 ),  
           NMAX_ITER_SHIFT =SIMP(statut='f',typ='I',defaut= 5 ),  
           PREC_SHIFT      =SIMP(statut='f',typ='R',defaut= 5.E-2 ),  
           PREC_LANCZOS    =SIMP(statut='f',typ='R',defaut= 1.E-10 ),  
           PREC_ORTHO      =SIMP(statut='f',typ='R',defaut= 1.E-12 ),  
           NMAX_ITER_ORTHO =SIMP(statut='f',typ='I',defaut= 5 ),  
           NMAX_ITER_QR    =SIMP(statut='f',typ='I',defaut= 30 ),  
           PREC_BATHE      =SIMP(statut='f',typ='R',defaut= 1.4E-10 ),  
           NMAX_ITER_BATHE =SIMP(statut='f',typ='I' ,defaut= 12 ),  
           PREC_JACOBI     =SIMP(statut='f',typ='R',defaut= 1.E-2 ),  
           NMAX_ITER_JACOBI=SIMP(statut='f',typ='I',defaut= 12 ),  
           PREC_SOREN      =SIMP(statut='f',typ='R',defaut= 0.E0 ),  
           NMAX_ITER_SOREN =SIMP(statut='f',typ='I',defaut= 20 ),  
           PARA_ORTHO_SOREN=SIMP(statut='f',typ='R',defaut= 0.717 ),  
           SEUIL_FREQ      =SIMP(statut='f',typ='R' ,defaut= 1.E-2 ),  
           STOP_FREQ_VIDE  =SIMP(statut='f',typ='TXM',defaut="NON" ,into=("OUI","NON") ),
         ),
         VERI_MODE       =FACT(statut='d',min=00,max=01,
           STOP_ERREUR     =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           SEUIL           =SIMP(statut='f',typ='R',defaut= 1.E-6 ),  
           PREC_SHIFT      =SIMP(statut='f',typ='R',defaut= 5.E-3 ),  
           STURM           =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         ),
         NORM_MODE       =FACT(statut='o',min=01,max='**',
           MASS_INER       =SIMP(statut='o',typ=tabl_mass_iner ),
           NORME           =SIMP(statut='f',typ='TXM',defaut="TRAN_ROTA",    
                                 into=("MASS_GENE","RIGI_GENE","EUCL",           
                                       "EUCL_TRAN","TRAN","TRAN_ROTA") ),
           INFO            =SIMP(statut='f',typ='I',defaut= 1 ,into=(1,2) ),
         ),
         FILTRE_MODE     =FACT(statut='f',min=01,max=01,
           CRIT_EXTR       =SIMP(statut='f',typ='TXM',defaut="MASS_EFFE_UN",    
                                 into=("MASS_EFFE_UN","MASS_GENE") ),
           SEUIL           =SIMP(statut='f',typ='R',defaut= 1.E-3 ),  
         ),
         IMPRESSION      =FACT(statut='d',min=01,max=01,
           TOUT_PARA       =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           CUMUL           =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           CRIT_EXTR       =SIMP(statut='f',typ='TXM',defaut="MASS_EFFE_UN",    
                                 into=("MASS_EFFE_UN","MASS_GENE",) ),
         ),
)  ;
#& MODIF COMMANDE  DATE 23/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def macro_proj_base_ops(self,BASE,NB_VECT,MATR_ASSE_GENE,VECT_ASSE_GENE,**args):
  """
     Ecriture de la macro MACRO_PROJ_BASE
  """
  ier=0
  # On importe les definitions des commandes a utiliser dans la macro
  NUME_DDL_GENE  =self.get_cmd('NUME_DDL_GENE')
  PROJ_MATR_BASE =self.get_cmd('PROJ_MATR_BASE')
  PROJ_VECT_BASE =self.get_cmd('PROJ_VECT_BASE')
  # La macro compte pour 1 dans la numerotation des commandes
  self.icmd=1

  nompro=None
  iocc=0
  if MATR_ASSE_GENE:
    for m in MATR_ASSE_GENE:
      iocc=iocc+1
      if (iocc==1 or (m['PROFIL']!=nompro)):
         _num=NUME_DDL_GENE(BASE=BASE,NB_VECT=NB_VECT,STOCKAGE=m['PROFIL'])
      nompro=m['PROFIL']
      motscles={}
      if   m['MATR_ASSE']     :  motscles['MATR_ASSE']     =m['MATR_ASSE']
      elif m['MATR_ASSE_GENE']:  motscles['MATR_ASSE_GENE']=m['MATR_ASSE_GENE']
      else:
          ier=ier+1
          self.cr.fatal("MATR_ASSE et MATR_ASSE_GENE absents")
          return ier
      self.DeclareOut('mm',m['MATRICE'])
      mm=PROJ_MATR_BASE(BASE=BASE,NUME_DDL_GENE=_num,NB_VECT=NB_VECT,**motscles)

  iocc=0
  if VECT_ASSE_GENE:
    for v in VECT_ASSE_GENE:
      iocc=iocc+1
      if (iocc==1 and not MATR_ASSE_GENE):
         _num=NUME_DDL_GENE(BASE=BASE,NB_VECT=NB_VECT,STOCKAGE='DIAG')
      motscles={}
      if   v['VECT_ASSE']     :  motscles['VECT_ASSE']     =v['VECT_ASSE']
      elif v['VECT_ASSE_GENE']:  motscles['VECT_ASSE_GENE']=v['VECT_ASSE_GENE']
      else:
          ier=ier+1
          self.cr.fatal("MATR_ASSE et MATR_ASSE_GENE absents")
          return ier
      motscles['TYPE_VECT']=v['TYPE_VECT']
      self.DeclareOut('vv',v['VECTEUR'])
      vv=PROJ_VECT_BASE(BASE=BASE,NUME_DDL_GENE=_num,NB_VECT=NB_VECT,**motscles)

  return ier


def macro_proj_base_prod(self,MATR_ASSE_GENE,VECT_ASSE_GENE,**args ):
  if MATR_ASSE_GENE != None:
    for m in MATR_ASSE_GENE:
      self.type_sdprod(m['MATRICE'],matr_asse_gene_r)
      self.type_sdprod(m['MATR_ASSE'],matr_asse_depl_r)
  if VECT_ASSE_GENE != None:
    for v in VECT_ASSE_GENE:
      self.type_sdprod(v['VECTEUR'],vect_asse_gene)
  return None

MACRO_PROJ_BASE=MACRO(nom="MACRO_PROJ_BASE",op=macro_proj_base_ops,docu="U4.63.11-c",
                      sd_prod=macro_proj_base_prod,
                      fr="Projection des matrices et/ou vecteurs assembl�s sur une base de vecteurs",
         BASE            =SIMP(statut='o',typ=(mode_meca,base_modale,mode_gene) ),
         NB_VECT         =SIMP(statut='f',typ='I',defaut= 9999),
         MATR_ASSE_GENE  =FACT(statut='f',min=01,max='**',
           MATRICE         =SIMP(statut='o',typ=(CO,matr_asse)),
           MATR_ASSE       =SIMP(statut='f',typ=matr_asse_depl_r),
           MATR_ASSE_GENE  =SIMP(statut='f',typ=matr_asse_gene_r),
           PROFIL          =SIMP(statut='f',typ='TXM',defaut="DIAG",into=("PLEIN","DIAG") ),
         ),
         VECT_ASSE_GENE  =FACT(statut='f',min=01,max='**',
           VECTEUR         =SIMP(statut='o',typ=(CO,vect_asse)),
           TYPE_VECT       =SIMP(statut='f',typ='TXM',defaut="FORC"),
           VECT_ASSE       =SIMP(statut='f',typ=cham_no_depl_r),
           VECT_ASSE_GENE  =SIMP(statut='f',typ=vect_asse_gene),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MAJ_CATA=PROC(nom="MAJ_CATA",op=20,docu="U4.15.01-d",
              fr="Compilation des catalogues de commandes et d �l�ments",
         regles=(UN_PARMI('COMMANDE','ELEMENT','VALIDATION'),),

         COMMANDE        =FACT(statut='f',min=01,max=01,
           UNITE           =SIMP(statut='o',typ='I',val_min=1,val_max=99, ),
         ),

         ELEMENT         =FACT(statut='f',min=01,max=01,),

         VALIDATION      =FACT(statut='f',min=01,max=01,
           UNITE           =SIMP(statut='o',typ='I',val_min=1,val_max=99, ),
           TOUT            =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI",) ),
         ),
)  ;
#& MODIF COMMANDE  DATE 04/12/2001   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
MECA_STATIQUE=OPER(nom="MECA_STATIQUE",op=46,sd_prod=evol_elas,
                   fr="Analyse m�canique statique lin�aire",docu="U4.51.01-f",reentrant='n',
                   regles=(EXCLUS("INST","LIST_INST"),
                           AU_MOINS_UN('CHAM_MATER','CARA_ELEM',), ),
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='f',typ=cham_mater,
         fr="le CHAM_MATER est n�cessaire, sauf si le mod�le ne contient que des �l�ments discrets (mod�lisations DIS_XXX)",
         ang="CHAM_MATER is compulsory, except if the model contains only discret elements (modelizations DIS_XXX)"),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem,
         fr="le CARA_ELEM est n�cessaire d�s que le mod�le contient des �l�ments de structure : coques, poutres, ...",
         ang="CARA_ELEM is compulsory as soon as the model contains structural elements : plates, beams, ..."),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         EXCIT           =FACT(statut='o',min=1,max='**',
           CHARGE          =SIMP(statut='o',typ=(char_meca,char_cine_meca)),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
           TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FIXE",into=("FIXE",) ),
         ),
         INST            =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         LIST_INST       =SIMP(statut='f',typ=listr8),
         OPTION          =SIMP(statut='f',typ='TXM',max='**',
                               into=("SIEF_ELGA_DEPL","SIGM_ELNO_DEPL","SIPO_ELNO_DEPL","EFGE_ELNO_DEPL",
                                     "EPSI_ELNO_DEPL","EPSI_ELGA_DEPL","EPME_ELNO_DEPL","EPME_ELGA_DEPL",
                                     "EQUI_ELNO_SIGM","EQUI_ELGA_SIGM","EQUI_ELNO_EPSI","EQUI_ELGA_EPSI",
                                     "EQUI_ELNO_EPME","EQUI_ELGA_EPME","DEGE_ELNO_DEPL","EPOT_ELEM_DEPL",
                                     "ENEL_ELGA","ENEL_ELNO_ELGA") ),
         NUME_COUCHE     =SIMP(statut='f',typ='I',defaut=1),
         NIVE_COUCHE     =SIMP(statut='f',typ='TXM',defaut="MOY",into=("SUP","INF","MOY") ),
         ANGLE           =SIMP(statut='f',typ='I',defaut=0),
         PLAN            =SIMP(statut='f',typ='TXM',defaut="MAIL",into=("SUP","INF","MOY","MAIL") ),
         SENSIBILITE     =SIMP(statut='f',typ=(para_sensi,theta_geom),max='**',
                               fr="Liste des param�tres de sensibilit�.",
                               ang="List of sensitivity parameters"),
         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt          =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
             TAILLE_BLOC     =SIMP(statut='f',typ='R',defaut= 400.),
           ),
           b_ldlt_mult     =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non inversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut=8),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
           b_gcpc         =BLOC(condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut=1.E-6),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
#  A quoi sert eps
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 25/09/2001   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE GNICOLAS G.NICOLAS
MEMO_NOM_SENSI=PROC(nom="MEMO_NOM_SENSI",op=129,docu="U4.31.xx-a",
                    fr="M�morisation des noms des concepts d�riv�s.",
                    ang="Memorisation of the names of the sensitive concepts.",
         regles=(AU_MOINS_UN('NOM','NOM_ZERO','NOM_UN'),),

         NOM=FACT(statut='f',max='**',
             NOM_SD=SIMP(statut='o',typ='TXM',
                         fr="Nom de la structure de base",
                         ang="Name of the basic structure"),
             PARA_SENSI=SIMP(statut='o',typ=(para_sensi,theta_geom),
                         fr="Nom du param�tre sensible base",
                         ang="Name of the sensitive parameter"),
             NOM_COMPOSE=SIMP(statut='f',typ='TXM',defaut=" ",
                         fr="Nom de la structure compos�e",
                         ang="Name of the built strcuture"),
         ),

         NOM_ZERO=SIMP(statut='f',typ=fonction,
                       fr="Nom de la fonction nulle",
                       ang="Name of the zero fonction"),
         NOM_UN=SIMP  (statut='f',typ=fonction,
                       fr="Nom de la fonction unit�",
                       ang="Name of the one fonction"),


)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MODE_ITER_CYCL=OPER(nom="MODE_ITER_CYCL",op=  80,sd_prod=mode_cycl,
                    fr="Modes propres d une structure � r�p�titivit� cyclique � partir d une base de modes propres r�els",
                    docu="U4.52.05-e",reentrant='n',
         BASE_MODALE     =SIMP(statut='o',typ=base_modale ),
         NB_MODE         =SIMP(statut='f',typ='I',defaut= 999 ),
         NB_SECTEUR      =SIMP(statut='o',typ='I' ),
         LIAISON         =FACT(statut='o',min=01,max=01,
           DROITE          =SIMP(statut='o',typ='TXM' ),
           GAUCHE          =SIMP(statut='o',typ='TXM' ),
           AXE             =SIMP(statut='f',typ='TXM' ),
         ),
         VERI_CYCL       =FACT(statut='f',min=01,max=01,
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF",) ),
           DIST_REFE       =SIMP(statut='f',typ='R' ),
         ),
         CALCUL          =FACT(statut='o',min=01,max=01,
           TOUT_DIAM       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NB_DIAM         =SIMP(statut='f',typ='I',max='**'),
           OPTION          =SIMP(statut='f',typ='TXM',defaut="PLUS_PETITE"
                                ,into=("PLUS_PETITE","CENTRE","BANDE") ),
           b_centre      =BLOC(condition = "OPTION == 'CENTRE'",
             FREQ            =SIMP(statut='o',typ='R',min=01,max=01),
           ),
           b_bande       =BLOC(condition = "OPTION == 'BANDE'",
             FREQ            =SIMP(statut='o',typ='R',min=02,max=02),
           ),
#  NMAX_FREQ n a-t-il pas un sens qu avec OPTION CENTRE                                
           NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 10 ),
           PREC_SEPARE     =SIMP(statut='f',typ='R',defaut= 100. ),
           PREC_AJUSTE     =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
           NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 50 ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def mode_iter_inv_prod(MATR_A,MATR_C,TYPE_RESU,**args ):
  if TYPE_RESU == "MODE_FLAMB" : return mode_flamb
  if AsType(MATR_C) == matr_asse_depl_r : return mode_meca_c
  if AsType(MATR_A) == matr_asse_depl_r : return mode_meca
  if AsType(MATR_A) == matr_asse_pres_r : return mode_acou
  if AsType(MATR_A) == matr_asse_gene_r : return mode_gene
  raise AsException("type de concept resultat non prevu")

MODE_ITER_INV=OPER(nom="MODE_ITER_INV",op=  44,sd_prod=mode_iter_inv_prod
                    ,fr="Modes propres par it�rations inverses ; valeurs propres et modes r�els ou complexes",
                     docu="U4.52.04-f",reentrant='n',
         MATR_A          =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_gene_r,matr_asse_pres_r ) ),
         MATR_B          =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_gene_r,matr_asse_pres_r ) ),
         MATR_C          =SIMP(statut='f',typ=matr_asse_depl_r ),
         TYPE_RESU       =SIMP(statut='f',position='global',typ='TXM',defaut="DYNAMIQUE",   
                               into=("MODE_FLAMB","DYNAMIQUE"),fr="Type d analyse" ),
         b_dynam         =BLOC(condition = "TYPE_RESU == 'DYNAMIQUE'",
           CALC_FREQ       =FACT(statut='o',min=1,max=1,fr="Choix des param�tres pour le calcul des valeurs propres",
           
             OPTION          =SIMP(statut='f',typ='TXM',defaut="AJUSTE",into=("SEPARE","AJUSTE","PROCHE"),
                                   fr="Choix de l option pour estimer les valeurs propres"  ),
             FREQ            =SIMP(statut='o',typ='R',max='**'),
             AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),     
             NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 0,val_min=0 ),           
             NMAX_ITER_SEPARE=SIMP(statut='f',typ='I' ,defaut= 30,val_min=0 ),
             PREC_SEPARE     =SIMP(statut='f',typ='R',defaut= 1.E-4,val_min=0.E+0 ),
             NMAX_ITER_AJUSTE=SIMP(statut='f',typ='I',defaut= 15,val_min=0 ),
             PREC_AJUSTE     =SIMP(statut='f',typ='R',defaut= 1.E-4,val_min=0.E+0 ),

             NPREC_SOLVEUR   =SIMP(statut='f',typ='I',defaut= 8,val_min=0 ),
             NMAX_ITER_SHIFT =SIMP(statut='f',typ='I',defaut= 5,val_min=0 ),
             PREC_SHIFT      =SIMP(statut='f',typ='R',defaut= 5.E-2,val_min=0.E+0, ),
             SEUIL_FREQ      =SIMP(statut='f',typ='R',defaut= 1.E-2,val_min=0.E+0, ),
           ),
         ),
         b_flamb        =BLOC(condition = "TYPE_RESU == 'MODE_FLAMB'",
           CALC_FREQ       =FACT(statut='o',min=1,max=1,fr="Choix des param�tres pour le calcul des valeurs propres",
           
             OPTION          =SIMP(statut='f',typ='TXM',defaut="AJUSTE",into=("SEPARE","AJUSTE","PROCHE"),
                                 fr="Choix de l option pour estimer les valeurs propres"  ),
             CHAR_CRIT       =SIMP(statut='o',typ='R',max='**' ),
             NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 0,val_min=0 ),           
             NMAX_ITER_SEPARE=SIMP(statut='f',typ='I' ,defaut= 30,val_min=0 ),
             PREC_SEPARE     =SIMP(statut='f',typ='R',defaut= 1.E-4,val_min=0.E+0, ),
             NMAX_ITER_AJUSTE=SIMP(statut='f',typ='I',defaut= 15 ),
             PREC_AJUSTE     =SIMP(statut='f',typ='R',defaut= 1.E-4,val_min=0.E+0, ),
           
             NPREC_SOLVEUR   =SIMP(statut='f',typ='I',defaut= 8,val_min=0 ),
             NMAX_ITER_SHIFT =SIMP(statut='f',typ='I',defaut= 5,val_min=0 ),
             PREC_SHIFT      =SIMP(statut='f',typ='R',defaut= 5.E-2,val_min=0.E+0, ),
             SEUIL_FREQ      =SIMP(statut='f',typ='R',defaut= 1.E-2,val_min=0.E+0, ),
           ),
         ),
         CALC_MODE       =FACT(statut='d',min=0,max=1,fr="Choix des param�tres pour le calcul des vecteurs propres",
           OPTION          =SIMP(statut='f',typ='TXM',defaut="DIRECT",into=("DIRECT","RAYLEIGH") ),
           PREC            =SIMP(statut='f',typ='R',defaut= 1.E-5,val_min=0.E+0,fr="Pr�cision de convergence" ),
           NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 30,val_min=0 ),
         ),
         VERI_MODE       =FACT(statut='d',min=0,max=1,
           STOP_ERREUR     =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           SEUIL           =SIMP(statut='f',typ='R',defaut= 1.E-2,val_min=0.E+0,
                                 fr="Valeur limite admise pour l ereur a posteriori des modes"  ),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 23/01/2002   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def mode_iter_simult_prod(MATR_A,MATR_C,TYPE_RESU,**args ):
  if TYPE_RESU == "MODE_FLAMB" : return mode_flamb
  if AsType(MATR_C) == matr_asse_depl_r : return mode_meca_c
  if AsType(MATR_A) == matr_asse_depl_r : return mode_meca
  if AsType(MATR_A) == matr_asse_pres_r : return mode_acou
  if AsType(MATR_A) == matr_asse_gene_r : return mode_gene
  raise AsException("type de concept resultat non prevu")

MODE_ITER_SIMULT=OPER(nom="MODE_ITER_SIMULT",op=  45,sd_prod=mode_iter_simult_prod,
                      fr="Modes propres par it�rations simultan�es ; valeurs propres et modes propres r�els ou complexes",
                      docu="U4.52.03-e",reentrant='n',
         MATR_A          =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_gene_r,matr_asse_pres_r ) ),
         MATR_B          =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_gene_r,matr_asse_pres_r ) ),
         MATR_C          =SIMP(statut='f',position='global',typ=matr_asse_depl_r ),
         METHODE         =SIMP(statut='f',position='global',typ='TXM',defaut="SORENSEN",
                               into=("TRI_DIAG","JACOBI","SORENSEN") ),
         TYPE_RESU       =SIMP(statut='f',position='global',typ='TXM',defaut="DYNAMIQUE",
                               into=("MODE_FLAMB","DYNAMIQUE"),
                               fr="Type d analyse" ),
         OPTION          =SIMP(statut='f',typ='TXM',defaut="SANS",into=("MODE_RIGIDE","SANS"),
                               fr="Calcul des modes de corps rigide, uniquement pour la m�thode TRI_DIAG" ),

         b_flamb         =BLOC(condition = "TYPE_RESU == 'MODE_FLAMB'",
           CALC_FREQ       =FACT(statut='d',min=0,max=1,
             OPTION          =SIMP(statut='f',typ='TXM',defaut="PLUS_PETITE",into=("PLUS_PETITE","BANDE","CENTRE"),
                                   fr="Choix de l option et par cons�quent du shift du probl�me modal" ),
             b_plus_petite =BLOC(condition = "OPTION == 'PLUS_PETITE'",fr="Recherche des plus petites valeurs propres",
               NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 10,val_min=0 ),
             ),
             b_centre      =BLOC(condition = "OPTION == 'CENTRE'",
                                 fr="Recherche des valeurs propres les plus proches d une valeur donn�e",
               CHAR_CRIT       =SIMP(statut='o',typ='R',min=1,max=1,
                                     fr="Charge critique autour de laquelle on cherche les charges critiques propres"),
             ),
             b_bande       =BLOC(condition = "(OPTION == 'BANDE')",
                                 fr="Recherche des valeurs propres dans une bande donn�e",
               CHAR_CRIT       =SIMP(statut='o',typ='R',min=2,max=2,
                                     fr="Valeur des deux charges critiques d�limitant la bande de recherche"),
             ),           
             APPROCHE        =SIMP(statut='f',typ='TXM',defaut="REEL",into=("REEL","IMAG"),
                                   fr="Choix du pseudo-produit scalaire pour la r�solution du probl�me quadratique" ),           
             regles=(EXCLUS('DIM_SOUS_ESPACE','COEF_DIM_ESPACE'),),
             DIM_SOUS_ESPACE =SIMP(statut='f',typ='I' ),
             COEF_DIM_ESPACE =SIMP(statut='f',typ='I' ),
             b_tri_diag =BLOC(condition = "METHODE == 'TRI_DIAG'",
               PREC_ORTHO      =SIMP(statut='f',typ='R',defaut= 1.E-12,val_min=0.E+0 ),
               NMAX_ITER_ORTHO =SIMP(statut='f',typ='I',defaut= 5,val_min=0 ),
               PREC_LANCZOS    =SIMP(statut='f',typ='R',defaut= 1.E-8,val_min=0.E+0 ),
               NMAX_ITER_QR    =SIMP(statut='f',typ='I',defaut= 30,val_min=0 ), 
             ),
             b_jacobi =BLOC(condition = "METHODE == 'JACOBI'",
               PREC_BATHE      =SIMP(statut='f',typ='R',defaut= 1.E-10,val_min=0.E+0 ),
               NMAX_ITER_BATHE =SIMP(statut='f',typ='I',defaut= 40,val_min=0 ),
               PREC_JACOBI     =SIMP(statut='f',typ='R',defaut= 1.E-2,val_min=0.E+0 ),
               NMAX_ITER_JACOBI=SIMP(statut='f',typ='I',defaut= 12,val_min=0 ),
             ),
             b_sorensen =BLOC(condition = "METHODE == 'SORENSEN'",
               PREC_SOREN      =SIMP(statut='f',typ='R',defaut= 0.E+0,val_min=0.E+0 ),  
               NMAX_ITER_SOREN =SIMP(statut='f',typ='I',defaut= 20,val_min=0 ),  
               PARA_ORTHO_SOREN=SIMP(statut='f',typ='R',defaut= 0.717,val_min=0.E+0 ),
             ),
             NPREC_SOLVEUR   =SIMP(statut='f',typ='I',defaut= 8,val_min=0 ),
             NMAX_ITER_SHIFT =SIMP(statut='f',typ='I',defaut= 5,val_min=0 ),
             PREC_SHIFT      =SIMP(statut='f',typ='R',defaut= 5.E-2,val_min=0.E+0 ),
             SEUIL_FREQ      =SIMP(statut='f',typ='R',defaut= 1.E-2,val_min=0.E+0 ),
           ),
         ),

         b_dynam        =BLOC(condition = "TYPE_RESU == 'DYNAMIQUE'",
           CALC_FREQ       =FACT(statut='d',min=0,max=1,
             OPTION          =SIMP(statut='f',typ='TXM',defaut="PLUS_PETITE",into=("PLUS_PETITE","BANDE","CENTRE"),
                                   fr="Choix de l option et par cons�quent du shift du probl�me modal" ),
             b_plus_petite =BLOC(condition = "OPTION == 'PLUS_PETITE'",fr="Recherche des plus petites valeurs propres",
               NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 10,val_min=0 ),
             ),
             b_centre       =BLOC(condition = "OPTION == 'CENTRE'",
                                  fr="Recherche des valeurs propres les plus proches d une valeur donn�e",
               FREQ            =SIMP(statut='o',typ='R',min=1,max=1,
                                     fr="Fr�quence autour de laquelle on cherche les fr�quences propres"),
               AMOR_REDUIT     =SIMP(statut='f',typ='R',max=1,),
               NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 10,val_min=0 ),
             ),
             b_bande         =BLOC(condition = "(OPTION == 'BANDE')",
                                   fr="Recherche des valeurs propres dans une bande donn�e",
               FREQ            =SIMP(statut='o',typ='R',min=2,max=2,
                                     fr="Valeur des deux fr�quences d�limitant la bande de recherche"),
             ),           
             APPROCHE        =SIMP(statut='f',typ='TXM',defaut="REEL",into=("REEL","IMAG"),
                                   fr="Choix du pseudo-produit scalaire pour la r�solution du probl�me quadratique" ),           
             regles=(EXCLUS('DIM_SOUS_ESPACE','COEF_DIM_ESPACE'),),
             DIM_SOUS_ESPACE =SIMP(statut='f',typ='I' ),
             COEF_DIM_ESPACE =SIMP(statut='f',typ='I' ),
             b_tri_diag =BLOC(condition = "METHODE == 'TRI_DIAG'",
               PREC_ORTHO      =SIMP(statut='f',typ='R',defaut= 1.E-12,val_min=0.E+0 ),
               NMAX_ITER_ORTHO =SIMP(statut='f',typ='I',defaut= 5,val_min=0 ),
               PREC_LANCZOS    =SIMP(statut='f',typ='R',defaut= 1.E-8,val_min=0.E+0 ),
               NMAX_ITER_QR    =SIMP(statut='f',typ='I',defaut= 30,val_min=0 ), 
             ),
             b_jacobi =BLOC(condition = "METHODE == 'JACOBI'",
               PREC_BATHE      =SIMP(statut='f',typ='R',defaut= 1.E-10,val_min=0.E+0 ),
               NMAX_ITER_BATHE =SIMP(statut='f',typ='I',defaut= 40,val_min=0 ),
               PREC_JACOBI     =SIMP(statut='f',typ='R',defaut= 1.E-2,val_min=0.E+0 ),
               NMAX_ITER_JACOBI=SIMP(statut='f',typ='I',defaut= 12,val_min=0 ),
             ),
             b_sorensen =BLOC(condition = "METHODE == 'SORENSEN'",
               PREC_SOREN      =SIMP(statut='f',typ='R',defaut= 0.E+0,val_min=0.E+0 ),  
               NMAX_ITER_SOREN =SIMP(statut='f',typ='I',defaut= 20,val_min=0 ),  
               PARA_ORTHO_SOREN=SIMP(statut='f',typ='R',defaut= 0.717,val_min=0.E+0 ),
             ),
             NPREC_SOLVEUR   =SIMP(statut='f',typ='I',defaut= 8,val_min=0 ),
             NMAX_ITER_SHIFT =SIMP(statut='f',typ='I',defaut= 5,val_min=0 ),
             PREC_SHIFT      =SIMP(statut='f',typ='R',defaut= 5.E-2,val_min=0.E+0 ),
             SEUIL_FREQ      =SIMP(statut='f',typ='R',defaut= 1.E-2,val_min=0.E+0 ),
           ),
         ),

         VERI_MODE       =FACT(statut='d',min=0,max=1,
           STOP_ERREUR     =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           PREC_SHIFT      =SIMP(statut='f',typ='R',defaut= 5.E-3,val_min=0.E+0 ),
           SEUIL           =SIMP(statut='f',typ='R',defaut= 1.E-6,val_min=0.E+0,
                                 fr="Valeur limite admise pour l ereur a posteriori des modes" ),
           STURM           =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         ),
         STOP_FREQ_VIDE  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),        
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def mode_stat_prod(MODE_STAT,FORCE_NODALE,PSEUDO_MODE,**args):
 if (MODE_STAT != None)          : return mode_stat_depl
 if (PSEUDO_MODE !=None)         : return mode_stat_acce
 if (FORCE_NODALE != None)       : return mode_stat_forc
 raise AsException("type de concept resultat non prevu")
MODE_STATIQUE=OPER(nom="MODE_STATIQUE",op= 93,sd_prod=mode_stat_prod,
                   fr="Calcul de modes statiques",
                   docu="U4.52.14-e",reentrant='n',
         MATR_RIGI       =SIMP(statut='o',typ=matr_asse_depl_r ),
         MATR_MASS       =SIMP(statut='f',typ=matr_asse_depl_r ),
               regles=(UN_PARMI('MODE_STAT','FORCE_NODALE','PSEUDO_MODE'),),
         MODE_STAT       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','NOEUD','GROUP_NO'),
                   UN_PARMI('TOUT_CMP','AVEC_CMP','SANS_CMP'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ,),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           TOUT_CMP        =SIMP(statut='f',typ='TXM',into=("OUI",) ,),
           AVEC_CMP        =SIMP(statut='f',typ='TXM',max='**'),
           SANS_CMP        =SIMP(statut='f',typ='TXM',max='**'),
         ),
         FORCE_NODALE    =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('TOUT','NOEUD','GROUP_NO'),
                   UN_PARMI('TOUT_CMP','AVEC_CMP','SANS_CMP'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",), ),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           TOUT_CMP        =SIMP(statut='f',typ='TXM',into=("OUI",), ),
           AVEC_CMP        =SIMP(statut='f',typ='TXM',max='**'),
           SANS_CMP        =SIMP(statut='f',typ='TXM',max='**'),
         ),
         PSEUDO_MODE       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('AXE','DIRECTION','TOUT','NOEUD','GROUP_NO' ),),
           AXE             =SIMP(statut='f',typ='TXM',into=("X","Y","Z"),max=3),
           DIRECTION       =SIMP(statut='f',typ='R',min=3,max=3),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",)),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           b_dir           =BLOC(condition = "DIRECTION != None",
             NOM_DIR         =SIMP(statut='f',typ='TXM' ),),
           b_cmp          =BLOC(condition="TOUT!= None or NOEUD!=None or GROUP_NO!=None",
             regles=(UN_PARMI('TOUT_CMP','AVEC_CMP','SANS_CMP'),),
             TOUT_CMP        =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             AVEC_CMP        =SIMP(statut='f',typ='TXM',max='**'),
             SANS_CMP        =SIMP(statut='f',typ='TXM',max='**'), 
        ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ,) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MODI_BASE_MODALE=OPER(nom="MODI_BASE_MODALE",op= 149,sd_prod=mode_meca,
                      docu="U4.66.21-c",reentrant='f',
#  la commande modi_base _modale : reentrant = f ou o                      
         regles=(EXCLUS('AMOR_UNIF','AMOR_REDUIT', ),),
         BASE            =SIMP(statut='o',typ=mode_meca ),
         BASE_ELAS_FLUI  =SIMP(statut='o',typ=melasflu ),
         NUME_VITE_FLUI  =SIMP(statut='o',typ='I' ),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
         AMOR_REDUIT     =SIMP(statut='f',typ='R',max='**'),
         AMOR_UNIF       =SIMP(statut='f',typ='R' ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 29/01/2002   AUTEUR CIBHHPD D.NUNEZ 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
MODI_MAILLAGE=OPER(nom="MODI_MAILLAGE",op= 154,sd_prod=maillage,
                   fr="Modification de la connectivit� de groupes de mailles 2D ou 3D affect�es � la mod�lisation de contact",
                   docu="U4.23.04-c",reentrant='o',
      regles=(UN_PARMI('ORIE_CONTACT','DEFORME','EQUE_PIQUA','ORIE_PEAU_2D',
                       'ORIE_PEAU_3D','ORIE_NORM_COQUE','PLAQ_TUBE','MODI_MAILLE'),
              EXCLUS('EQUE_PIQUA','PLAQ_TUBE'),
              EXCLUS('EQUE_PIQUA','TUBE_COUDE'),),
         MAILLAGE        =SIMP(statut='o',typ=maillage ),

         ORIE_CONTACT    =FACT(statut='f',min=01,max=01,
           GROUP_MA        =SIMP(statut='o',typ=grma,max='**'),
         ),

         DEFORME         =FACT(statut='f',min=01,max=01,
           OPTION          =SIMP(statut='o',typ='TXM',into=("TRAN","TRAN_APPUI") ),
           DEPL            =SIMP(statut='o',typ=cham_no_depl_r ),
        b_deform        =BLOC(condition = "OPTION=='TRAN_APPUI'", 
           GROUP_NO_APPUI = SIMP(statut='o',typ=grno,max='**' ),
           GROUP_NO_STRU = SIMP(statut='o',typ=grno,max='**' ),),
         ),

         EQUE_PIQUA      =FACT(statut='f',min=01,max=01,
           GROUP_NO        =SIMP(statut='o',typ=grno),
           E_BASE          =SIMP(statut='o',typ='R' ),
           DEXT_BASE       =SIMP(statut='o',typ='R' ),
           L_BASE          =SIMP(statut='o',typ='R' ),
           L_CHANF         =SIMP(statut='o',typ='R' ),
           H_SOUD          =SIMP(statut='o',typ='R' ),
           ANGL_SOUD       =SIMP(statut='o',typ='R' ),
           JEU_SOUD        =SIMP(statut='o',typ='R' ),
           E_CORP          =SIMP(statut='o',typ='R' ),
           DEXT_CORP       =SIMP(statut='o',typ='R' ),
           AZIMUT          =SIMP(statut='o',typ='R' ),
           RAFF_MAIL       =SIMP(statut='o',typ='TXM' ),
           X_MAX           =SIMP(statut='o',typ='R' ),
         ),
         ORIE_PEAU_2D    =FACT(statut='f',min=01,max='**',
           GROUP_MA        =SIMP(statut='o',typ=grma,max='**'),
         ),
         ORIE_PEAU_3D    =FACT(statut='f',min=01,max='**',
           GROUP_MA        =SIMP(statut='o',typ=grma,max='**'),
         ),
         ORIE_NORM_COQUE =FACT(statut='f',min=01,max='**',
           regles=(EXCLUS('NOEUD','GROUP_NO'),
                   PRESENT_PRESENT('NOEUD','VECT_NORM'),
                   PRESENT_PRESENT('GROUP_NO','VECT_NORM'),),
           GROUP_MA        =SIMP(statut='o',typ=grma,max='**'),
           VECT_NORM       =SIMP(statut='f',typ='R',max=03),
           NOEUD           =SIMP(statut='f',typ=no),
           GROUP_NO        =SIMP(statut='f',typ=grno),
         ),
         b_modele        =BLOC(condition = "(ORIE_PEAU_2D != None) or (ORIE_PEAU_3D != None) or(ORIE_NORM_COQUE != None)",
           MODELE          =SIMP(statut='o',typ=modele ),
         ),
         PLAQ_TUBE       =FACT(statut='f',min=01,max=01,
           DEXT            =SIMP(statut='o',typ='R' ),
           EPAIS           =SIMP(statut='o',typ='R' ),
           L_TUBE_P1       =SIMP(statut='o',typ='R' ),
           AZIMUT          =SIMP(statut='f',typ='R',defaut= 90. ),
           COUTURE         =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON",)  ),
         ),
         TUBE_COUDE      =FACT(statut='f',min=01,max=01,
           ANGLE           =SIMP(statut='o',typ='R' ),
           R_CINTR         =SIMP(statut='o',typ='R' ),
           L_TUBE_P1       =SIMP(statut='o',typ='R' ),
         ),
         MODI_MAILLE     =FACT(statut='f',min=01,max=01,
           regles=(AU_MOINS_UN('GROUP_MA_FOND','MAILLE_FOND','GROUP_NO_FOND','NOEUD_FOND'),),
           OPTION          =SIMP(statut='o',typ='TXM',into=("NOEUD_QUART",) ),
           GROUP_MA_FOND   =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_FOND     =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_FOND   =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_FOND      =SIMP(statut='f',typ=no,max='**'),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 15/01/2002   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
MODI_OBSTACLE=OPER(nom="MODI_OBSTACLE",op=182,sd_prod=obstacle,
                   fr=" ",docu="U4.44.22-a",reentrant='f',
      regles=(PRESENT_ABSENT('R_MOBILE','CRAYON'),
              PRESENT_PRESENT('TUBE_NEUF','TABL_USURE'),
              PRESENT_PRESENT('V_USUR_TUBE','V_USUR_OBST'),),
         TUBE_NEUF       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         V_USUR_TUBE     =SIMP(statut='f',typ='R',max='**'),
         V_USUR_OBST     =SIMP(statut='f',typ='R',max='**'),
         TABL_USURE      =SIMP(statut='f',typ=tabl_post_usur),
         INST            =SIMP(statut='f',typ='R'),  
         OBSTACLE        =SIMP(statut='f',typ=obstacle),
         GUIDE           =SIMP(statut='o',typ=obstacle),
         CRAYON          =SIMP(statut='f',typ=obstacle),
         R_MOBILE        =SIMP(statut='f',typ='R'),  
         PERCEMENT       =SIMP(statut='f',typ='R',defaut=1),  
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE JMBHH01 J.M.PROIX
def modi_repere_prod(RESULTAT,**args):
  if AsType(RESULTAT) == evol_elas :    return evol_elas
  if AsType(RESULTAT) == evol_noli :    return evol_noli
  if AsType(RESULTAT) == evol_ther :    return evol_ther
  if AsType(RESULTAT) == dyna_trans :   return dyna_trans
  if AsType(RESULTAT) == dyna_harmo :   return dyna_harmo
  if AsType(RESULTAT) == mode_meca :    return mode_meca
  if AsType(RESULTAT) == mode_flamb :   return mode_flamb
  if AsType(RESULTAT) == mult_elas :    return mult_elas
  if AsType(RESULTAT) == base_modale  : return base_modale
  raise AsException("type de concept resultat non prevu")

MODI_REPERE=OPER(nom="MODI_REPERE",op=191,sd_prod=modi_repere_prod,docu="U4.74.01-a1",reentrant='n',
                    fr="Impression des resultats dans un repere cylindrique",
         RESULTAT        =SIMP(statut='o',typ=(evol_elas,dyna_trans,dyna_harmo,mode_meca,
                                               evol_noli,mult_elas,
                                               evol_ther,base_modale,mode_flamb) ),
         regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','FREQ','NUME_MODE',
                        'NOEUD_CMP','LIST_INST','LIST_FREQ','NOM_CAS'),),
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
         NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
         NOEUD_CMP       =SIMP(statut='f',typ='TXM',max='**'),
         NOM_CAS         =SIMP(statut='f',typ='TXM' ),
 
         INST            =SIMP(statut='f',typ='R',max='**'),
         FREQ            =SIMP(statut='f',typ='R',max='**'),
         LIST_INST       =SIMP(statut='f',typ=listr8),
         LIST_FREQ       =SIMP(statut='f',typ=listr8),

         PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3 ),
         CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU",),),

         MODI_CHAM       =FACT(statut='o',min=01,max='**',
           TYPE_CHAM       =SIMP(statut='o',typ='TXM', max=1,    
                                 into=("VECT_2D","VECT_3D","TORS_3D","TENS_2D","TENS_3D"),),
           NOM_CHAM        =SIMP(statut='o',typ='TXM',max=1 ),  
           b_vect_2d       =BLOC(condition = "TYPE_CHAM=='VECT_2D'",
              NOM_CMP         =SIMP(statut='o',typ='TXM',min=2,max=2 ),),
           b_vect_3d       =BLOC(condition = "TYPE_CHAM=='VECT_3D'",
              NOM_CMP         =SIMP(statut='o',typ='TXM',min=3,max=3 ),),
           b_tors_3d       =BLOC(condition = "TYPE_CHAM=='TORS_3D'",
              NOM_CMP         =SIMP(statut='o',typ='TXM',min=6,max=6 ),),
           b_tens_2d       =BLOC(condition = "TYPE_CHAM=='TENS_2D'",
              NOM_CMP         =SIMP(statut='o',typ='TXM',min=4,max=4 ),),
           b_tens_3d       =BLOC(condition = "TYPE_CHAM=='TENS_3D'",
              NOM_CMP         =SIMP(statut='o',typ='TXM',min=6,max=6 ),),
         ),
         DEFI_REPERE     =FACT(statut='o',min=1,max=1,
         regles=(UN_PARMI('ANGL_NAUT','ORIGINE'),),
           REPERE          =SIMP(statut='f',typ='TXM',defaut="UTILISATEUR",
                                 into=("UTILISATEUR","CYLINDRIQUE"),),
           ANGL_NAUT       =SIMP(statut='f',typ='R',min=1,max=3),
           ORIGINE         =SIMP(statut='f',typ='R',min=2,max=3),  
           AXE_Z           =SIMP(statut='f',typ='R',min=3,max=3),  
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def norm_mode_prod(MODE,**args ):
  if AsType(MODE) == mode_meca   : return mode_meca
  if AsType(MODE) == mode_meca_c : return mode_meca_c
  if AsType(MODE) == mode_flamb  : return mode_flamb
  raise AsException("type de concept resultat non prevu")

NORM_MODE=OPER(nom="NORM_MODE",op=  37,sd_prod=norm_mode_prod,
               fr="Normalisation de modes propres",
               docu="U4.52.11-e",reentrant='f',
         regles=(UN_PARMI('NORME','NOEUD','AVEC_CMP','SANS_CMP'),),
         MODE       =SIMP(statut='o',typ=(mode_meca,mode_flamb) ),
         NORME      =SIMP(statut='f',typ='TXM',fr="Norme pr�d�finie : masse g�n�ralis�e, euclidienne,...",
                          into=("MASS_GENE","RIGI_GENE","EUCL","EUCL_TRAN","TRAN","TRAN_ROTA") ),
         NOEUD      =SIMP(statut='f',typ=no, fr="Composante donn�e d un noeud sp�cifi� �gale � 1"),
         b_noeud    =BLOC(condition = "NOEUD != None",
           NOM_CMP    =SIMP(statut='o',typ='TXM' ),
         ),
         AVEC_CMP   =SIMP(statut='f',typ='TXM',max='**'),
         SANS_CMP   =SIMP(statut='f',typ='TXM',max='**'),
         MASS_INER  =SIMP(statut='f',typ=tabl_mass_iner ),
         MODE_SIGNE =FACT(statut='f',min=00,max=01,fr="Imposer un signe sur une des composantes des modes",
           NOEUD      =SIMP(statut='o',typ=no,fr="Noeud ou sera impos� le signe"),
           NOM_CMP    =SIMP(statut='o',typ='TXM',fr="Composante du noeud ou sera impos� le signe" ),
           SIGNE      =SIMP(statut='f',typ='TXM',defaut="POSITIF",into=("NEGATIF","POSITIF"),
                            fr="Choix du signe" ),
         ),
         TITRE      =SIMP(statut='f',typ='TXM',max='**'),
         INFO       =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;
#& MODIF COMMANDE  DATE 22/01/2002   AUTEUR CIBHHPD D.NUNEZ 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
NUME_DDL=OPER(nom="NUME_DDL",op=11,sd_prod=nume_ddl,docu="U4.61.11-f",reentrant='n',
              fr="Etablissement de la num�rotation des ddl avec ou sans renum�rotation et du stockage de la matrice",
                  regles=(UN_PARMI('MATR_RIGI','MODELE'),), 
         MATR_RIGI       =SIMP(statut='f',typ=(matr_elem_depl_r ,matr_elem_depl_c,
                                               matr_elem_temp_r,matr_elem_pres_c),max=100 ),
         MODELE          =SIMP(statut='f',typ=modele ),
         b_modele        =BLOC(condition = "MODELE != None",
           CHARGE     =SIMP(statut='f',max='**',typ=(char_meca,char_ther,char_acou, ),),
         ),
         METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
         b_mult_front    =BLOC(condition="METHODE=='MULT_FRONT'",fr="param�tres associ�s � la m�thode multifrontale",
           RENUM           =SIMP(statut='f',typ='TXM',into=("MD","MDA","METIS"),defaut="METIS" ),
         ),
         b_ldlt          =BLOC(condition="METHODE=='LDLT'",fr="param�tres associ�s � la m�thode LDLT",
           RENUM           =SIMP(statut='f',typ='TXM',into=("RCMK","SANS"),defaut="RCMK"  ),
         ),
         b_gcpc          =BLOC(condition="METHODE=='GCPC'",fr="param�tres associ�s � la m�thode gradient conjugu�",
           RENUM           =SIMP(statut='f',typ='TXM',into=("RCMK","SANS"),defaut="RCMK"  ),
         ),
         INFO            =SIMP(statut='f',typ='I',into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
NUME_DDL_GENE=OPER(nom="NUME_DDL_GENE",op= 127,sd_prod=nume_ddl_gene,
                   fr="Etablissement de la num�rotation des ddl d un mod�le �tabli en coordonn�es g�n�ralis�es",
                    docu="U4.65.03-d",reentrant='n',
         MODELE_GENE     =SIMP(statut='f',typ=modele_gene ),
         BASE            =SIMP(statut='f',typ=(mode_meca,base_modale,mode_gene ) ),
         NB_VECT         =SIMP(statut='f',typ='I',defaut= 9999 ),
         STOCKAGE        =SIMP(statut='f',typ='TXM',defaut="LIGN_CIEL",into=("PLEIN","DIAG","LIGN_CIEL") ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
POST_DYNA_ALEA=OPER(nom="POST_DYNA_ALEA",op= 132,sd_prod=tabl_post_alea,
                    fr="Traitements statistiques de r�sultats de type interspectre et impression sur fichiers",
                    docu="U4.84.04-d",reentrant='n',
         regles=(UN_PARMI('NOEUD_I','NUME_ORDRE_I','OPTION'),),
         INTE_SPEC       =SIMP(statut='o',typ=tabl_intsp ),
         NUME_VITE_FLUI  =SIMP(statut='f',typ='I' ),  
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         NUME_ORDRE_I    =SIMP(statut='f',typ='I',max='**' ),
         NOEUD_I         =SIMP(statut='f',typ=no,max='**'),         
         OPTION          =SIMP(statut='f',typ='TXM',into=("DIAG",) ),
         b_nume_ordre_i =BLOC(condition = "NUME_ORDRE_I != None",
           NUME_ORDRE_J    =SIMP(statut='o',typ='I',max='**' ),   
         ),  
         b_noeud_i      =BLOC(condition = "NOEUD_I != None",
           NOEUD_J         =SIMP(statut='o',typ=no,max='**'),
           NOM_CMP_I       =SIMP(statut='o',typ='TXM',max='**' ),  
           NOM_CMP_J       =SIMP(statut='o',typ='TXM',max='**' ),     
         ),  
         DEPASSEMENT     =FACT(statut='f',min=01,max='**',
           fr="Loi de d�passement d un seuil pendant une dur�e donn�e",
           regles=(ENSEMBLE('VALE_MIN','VALE_MAX'),),
           VALE_MIN        =SIMP(statut='f',typ='R' ),  
           VALE_MAX        =SIMP(statut='f',typ='R' ),  
           PAS             =SIMP(statut='f',typ='R' ),  
           DUREE           =SIMP(statut='f',typ='R',defaut= 1. ),  
         ),
         RAYLEIGH        =FACT(statut='f',min=01,max='**',
           fr="Densit� de probabilit� de pic positif, loi adapt�e � des signaux � bande �troite",
           regles=(ENSEMBLE('VALE_MIN','VALE_MAX'),),
           VALE_MIN        =SIMP(statut='f',typ='R' ),  
           VALE_MAX        =SIMP(statut='f',typ='R' ),  
           PAS             =SIMP(statut='f',typ='R' ),  
         ),
         GAUSS           =FACT(statut='f',min=01,max='**',
           fr="Densit� de probabilit� de pic positif, loi normale adapt�e � des signaux large bande",
           regles=(ENSEMBLE('VALE_MIN','VALE_MAX'),),
           VALE_MIN        =SIMP(statut='f',typ='R' ),  
           VALE_MAX        =SIMP(statut='f',typ='R' ),  
           PAS             =SIMP(statut='f',typ='R' ),  
         ),
         VANMARCKE       =FACT(statut='f',min=01,max='**',
           fr="Probabilit� de non d�passement de seuil pendant une dur�e donn�e (analyse sismique)",
           regles=(ENSEMBLE('VALE_MIN','VALE_MAX'),),
           VALE_MIN        =SIMP(statut='f',typ='R' ),  
           VALE_MAX        =SIMP(statut='f',typ='R' ),  
           PAS             =SIMP(statut='f',typ='R' ),  
           DUREE           =SIMP(statut='f',typ='R',defaut= 10. ),  
         ),
         MOMENT          =SIMP(statut='f',typ='I',max='**',fr="Moments spectraux en compl�ment des cinq premiers" ),  
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
POST_DYNA_MODA_T=OPER(nom="POST_DYNA_MODA_T",op= 130,sd_prod=tabl_post_dyna,
                      fr="Post-traitements en coordonn�es g�n�ralis�es issus de DYNA_TRAN_MODAL",
                      docu="U4.84.02-d",reentrant='n',
        regles=(UN_PARMI('CHOC','RELA_EFFO_DEPL', ),),
         RESU_GENE       =SIMP(statut='o',typ=tran_gene ),
         CHOC            =FACT(statut='f',min=01,max='**',
                               fr="Analyse des non lin�arit�s de choc",
           INST_INIT       =SIMP(statut='f',typ='R',defaut= -1. ),  
           INST_FIN        =SIMP(statut='f',typ='R',defaut= 999. ),  
           NB_BLOC         =SIMP(statut='f',typ='I',defaut= 1 ),  
           SEUIL_FORCE     =SIMP(statut='f',typ='R',defaut= 0.E+0 ),  
           DUREE_REPOS     =SIMP(statut='f',typ='R',defaut= 0.E+0 ),  
           OPTION          =SIMP(statut='f',typ='TXM',defaut="USURE",into=("IMPACT","USURE") ),
           NB_CLASSE       =SIMP(statut='f',typ='I',defaut= 10 ),  
         ),
         RELA_EFFO_DEPL  =FACT(statut='f',min=01,max=01,
                               fr="Analyse des relationsnon lin�aires effort-d�placement",
           NOEUD           =SIMP(statut='o',typ=no),
           NOM_CMP         =SIMP(statut='o',typ='TXM' ),  
         ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=(1,2) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 30/01/2002   AUTEUR VABHHTS J.TESELET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
def post_elem_prod( MASS_INER,ENER_POT,ENER_CIN,ENER_EXT,WEIBULL,
                    CARA_GEOM,CARA_POUTRE,RICE_TRACEY,CHAR_LIMITE,
                    INDIC_ENER,INDIC_SEUIL,ENER_ELAS,ENER_TOTALE,
                    AIRE_INTERNE,**args ):
  if MASS_INER    != None  : return tabl_mass_iner
  if ENER_POT     != None  : return tabl_ener_pot
  if ENER_CIN     != None  : return tabl_ener_cin
  if ENER_EXT     != None  : return tabl_ener_ext
  if WEIBULL      != None  : return tabl_weibull
  if CARA_GEOM    != None  : return tabl_cara_geom
  if CARA_POUTRE  != None  : return tabl_cara_geom
  if RICE_TRACEY  != None  : return tabl_rice_tracey
  if CHAR_LIMITE  != None  : return tabl_char_limite
  if INDIC_ENER   != None  : return tabl_indic_ener
  if INDIC_SEUIL  != None  : return tabl_indic_seuil
  if ENER_ELAS    != None  : return tabl_ener_elas
  if ENER_TOTALE  != None  : return tabl_ener_totale
  if AIRE_INTERNE != None  : return tabl_aire_int
  raise AsException("type de concept resultat non prevu")

POST_ELEM=OPER(nom="POST_ELEM",op=107,sd_prod=post_elem_prod,docu="U4.81.22-d1",reentrant='f',
               fr="Calcul de quantit�s globales (masse, inerties, �nergie, ...) sur tout ou partie du mod�le",
         regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','FREQ','NUME_MODE',
                        'NOEUD_CMP','LIST_ORDRE','LIST_INST','LIST_FREQ','NOM_CAS'),
                 EXCLUS('CHAM_GD','RESULTAT'),
                 UN_PARMI('MASS_INER', 'ENER_POT', 'ENER_CIN','ENER_EXT',
                          'WEIBULL', 'RICE_TRACEY', 'CARA_GEOM','CHAR_LIMITE',
                          'CARA_POUTRE', 'INDIC_ENER', 'INDIC_SEUIL',
                          'AIRE_INTERNE','ENER_ELAS','ENER_TOTALE'),
                 PRESENT_PRESENT( 'MASS_INER', 'MODELE' ),
                 PRESENT_PRESENT( 'CARA_GEOM', 'MODELE' ),
                 PRESENT_PRESENT( 'AIRE_INTERNE', 'MODELE' ),
                 PRESENT_PRESENT( 'CARA_POUTRE', 'MODELE' ),
                 PRESENT_PRESENT( 'ENER_POT', 'MODELE', 'CHAM_MATER' ),
                 PRESENT_PRESENT( 'ENER_CIN', 'MODELE', 'CHAM_MATER' ),
                 PRESENT_PRESENT( 'WEIBULL', 'MODELE', 'CHAM_MATER' ),
                 PRESENT_PRESENT( 'RICE_TRACEY', 'MODELE', 'CHAM_MATER' ),
                 PRESENT_PRESENT( 'INDIC_ENER', 'MODELE', 'CHAM_MATER' ),
                 PRESENT_PRESENT( 'INDIC_SEUIL', 'MODELE', 'CHAM_MATER' ),
                 PRESENT_PRESENT( 'ENER_ELAS', 'MODELE', 'CHAM_MATER' ),
                 PRESENT_PRESENT( 'ENER_TOTALE', 'MODELE', 'CHAM_MATER' ),
                 PRESENT_PRESENT( 'CHAR_LIMITE', 'MODELE', 'CHAM_MATER' ),
             ),
         MODELE          =SIMP(statut='f',typ=modele),
         CHAM_MATER      =SIMP(statut='f',typ=cham_mater),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),
         CHARGE          =SIMP(statut='f',typ=(char_meca,char_ther,char_acou),max='**' ),
         MODE_FOURIER    =SIMP(statut='f',typ='I',defaut=0),
         NUME_COUCHE     =SIMP(statut='f',typ='I',defaut=1),
         NIVE_COUCHE     =SIMP(statut='f',typ='TXM',defaut="MOY",into=("INF","SUP","MOY"),),
         ANGLE           =SIMP(statut='f',typ='I',defaut=0),
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
         GEOMETRIE       =SIMP(statut='f',typ='TXM',defaut="INITIALE",into=("INITIALE","DEFORMEE")),
         CHAM_GD         =SIMP(statut='f',typ=(cham_no_depl_r,cham_no_temp_r,cham_elem_ener_r) ),
         RESULTAT        =SIMP(statut='f',typ=(mode_meca,evol_elas,evol_ther,evol_noli,mult_elas,
                                               fourier_elas,dyna_trans) ),
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
         LIST_ORDRE      =SIMP(statut='f',typ=listis),
         INST            =SIMP(statut='f',typ='R',max='**'),
         LIST_INST       =SIMP(statut='f',typ=listr8),
         FREQ            =SIMP(statut='f',typ='R',max='**'),
         LIST_FREQ       =SIMP(statut='f',typ=listr8),
         NUME_MODE       =SIMP(statut='f',typ='I',max='**'),
         NOEUD_CMP       =SIMP(statut='f',typ='TXM',max='**'),
         NOM_CAS         =SIMP(statut='f',typ='TXM',max='**'),
         PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3),
         CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU")),

         MASS_INER       =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           ORIG_INER       =SIMP(statut='f',typ='R',min=3,max=3 ),
         ),

         ENER_POT        =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         ),

         ENER_CIN        =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           OPTION          =SIMP(statut='f',typ='TXM',into=("MASS_MECA","MASS_MECA_DIAG"),
                                                      defaut="MASS_MECA" ),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         ),

         WEIBULL         =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           OPTION          =SIMP(statut='f',typ='TXM',defaut="SIGM_ELGA",into=("SIGM_ELGA","SIGM_ELMOY")),
           CORR_PLAST      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
           COEF_MULT       =SIMP(statut='f',typ='R',defaut=1.),
         ),

         RICE_TRACEY     =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           OPTION          =SIMP(statut='f',typ='TXM',defaut="SIGM_ELGA",into=("SIGM_ELGA","SIGM_ELMOY")),
           LOCAL           =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON")),
         ),

         INDIC_ENER      =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         ),

         ENER_ELAS       =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         ),

         ENER_TOTALE    =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         ),

         ENER_EXT     =FACT(statut='f',min=00,max=01,
           TOUT            =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI",) ),
         ),

         CHAR_LIMITE     =FACT(statut='f',min=00,max=01,
         CHAR_CSTE = SIMP(statut='f',typ='TXM',into=("OUI","NON"),defaut="NON")
         ),

         INDIC_SEUIL     =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
         ),

         CARA_GEOM       =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           SYME_X          =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           SYME_Y          =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
           ORIG_INER       =SIMP(statut='f',typ='R',min=2,max=2),
         ),

         CARA_POUTRE     =FACT(statut='f',min=1,max='**',
           regles=(AU_MOINS_UN('TOUT','GROUP_MA'),
                   ENSEMBLE('LONGUEUR','LIAISON','MATERIAU'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           GROUP_MA_INTE   =SIMP(statut='f',typ=grma,max='**'),
           CARA_GEOM       =SIMP(statut='f',typ=tabl_cara_geom),
           LAPL_PHI        =SIMP(statut='f',typ=evol_ther),
           LAPL_PHI_Y      =SIMP(statut='f',typ=evol_ther),
           LAPL_PHI_Z      =SIMP(statut='f',typ=evol_ther),
           LIAISON         =SIMP(statut='f',typ='TXM',into=("ROTULE","ENCASTREMENT")),
           LONGUEUR        =SIMP(statut='f',typ='R'),
           MATERIAU        =SIMP(statut='f',typ=mater),
           OPTION          =SIMP(statut='f',typ='TXM',into=("CARA_TORSION","CARA_CISAILLEMENT","CARA_GAUCHI") ),
         ),

         AIRE_INTERNE    =FACT(statut='f',min=1,max='**',
           GROUP_MA_BORD   =SIMP(statut='o',typ=grma,max='**'),
         ),
 )  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
POST_FATI_ALEA=OPER(nom="POST_FATI_ALEA",op=170,sd_prod=tabl_post_f_alea,docu="U4.84.03-c",reentrant='n',
                    fr="Calcul du dommage subi par une structure soumise � unesollicitation de type al�atoire",
         regles=(ENSEMBLE('MOMENT_SPEC_0','MOMENT_SPEC_2'),
                 PRESENT_PRESENT( 'MOMENT_SPEC_4','MOMENT_SPEC_0'),
                 UN_PARMI('TABL_POST_ALEA','MOMENT_SPEC_0'), ),
         MOMENT_SPEC_0   =SIMP(statut='f',typ='R'),  
         MOMENT_SPEC_2   =SIMP(statut='f',typ='R'),  
         MOMENT_SPEC_4   =SIMP(statut='f',typ='R'),  
         TABL_POST_ALEA  =SIMP(statut='f',typ=tabl_post_alea),
         COMPTAGE        =SIMP(statut='o',typ='TXM',into=("PIC","NIVEAU")),
         DUREE           =SIMP(statut='f',typ='R',defaut= 1.),  
         CORR_KE         =SIMP(statut='f',typ='TXM',into=("RCCM",)),
         DOMMAGE         =SIMP(statut='o',typ='TXM',into=("WOHLER",)),
         MATER           =SIMP(statut='o',typ=mater),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),  
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
POST_FATIGUE=OPER(nom="POST_FATIGUE",op=136,sd_prod=tabl_post_fatig,docu="U4.83.01-c",reentrant='n',
                  fr="Calcul du dommage subi par une structure soumise � une histoire de chargement",

         CHARGEMENT = SIMP(statut='o',typ='TXM',into=("UNIAXIAL","PERIODIQUE","QUELCONQUE")),

         b_uniaxial = BLOC( condition = "CHARGEMENT=='UNIAXIAL'",
                      regles=(PRESENT_PRESENT('CORR_KE','MATER'),
                              PRESENT_PRESENT('CORR_SIGM_MOYE','MATER'),
                              PRESENT_PRESENT('DOMMAGE','MATER'),),
             HISTOIRE       = FACT(statut='o',min=1,max=1,
                                 regles=(UN_PARMI('SIGM','EPSI'),),
                                 SIGM  = SIMP(statut='f',typ=fonction),
                                 EPSI  = SIMP(statut='f',typ=fonction),),
             COMPTAGE       = SIMP(statut='o',typ='TXM',into=("RAINFLOW","RCCM","NATUREL")),
             DELTA_OSCI     = SIMP(statut='f',typ='R',defaut= 0.0E+0),  
             COEF_MULT      = FACT(statut='f',min=1,max=1,
                                 KT    = SIMP(statut='o',typ='R'),),
             CORR_KE        = SIMP(statut='f',typ='TXM',into=("RCCM",)),
             DOMMAGE        = SIMP(statut='f',typ='TXM',into=("WOHLER","MANSON_COFFIN",
                                                              "TAHERI_MANSON","TAHERI_MIXTE")),
             MATER          = SIMP(statut='f',typ=mater),
             CORR_SIGM_MOYE = SIMP(statut='f',typ='TXM',into=("GOODMAN","GERBER")),
             TAHERI_NAPPE   = SIMP(statut='f',typ=fonction),
             TAHERI_FONC    = SIMP(statut='f',typ=fonction),
             CUMUL          = SIMP(statut='f',typ='TXM',into=("LINEAIRE",)),
         ),

         b_periodique = BLOC( condition = "CHARGEMENT=='PERIODIQUE'",
             HISTOIRE       = FACT(statut='o',min=1,max=1,
                                 SIGM_XX  = SIMP(statut='o',typ=fonction),
                                 SIGM_YY  = SIMP(statut='o',typ=fonction),
                                 SIGM_ZZ  = SIMP(statut='o',typ=fonction),
                                 SIGM_XY  = SIMP(statut='o',typ=fonction),
                                 SIGM_XZ  = SIMP(statut='f',typ=fonction),
                                 SIGM_YZ  = SIMP(statut='f',typ=fonction),),
             CRITERE        = SIMP(statut='o',typ='TXM',into=("CROSSLAND","PAPADOPOULOS")),
             DOMMAGE        = SIMP(statut='f',typ='TXM',into=("WOHLER",)),
             MATER          = SIMP(statut='o',typ=mater),
             COEF_CORR      = SIMP(statut='f',typ='R'),
         ),

         b_quelconque = BLOC( condition = "CHARGEMENT=='QUELCONQUE'",
             HISTOIRE       = FACT(statut='o',min=1,max=1,
                                 SIGM_XX  = SIMP(statut='o',typ=fonction),
                                 SIGM_YY  = SIMP(statut='o',typ=fonction),
                                 SIGM_ZZ  = SIMP(statut='o',typ=fonction),
                                 SIGM_XY  = SIMP(statut='o',typ=fonction),
                                 SIGM_XZ  = SIMP(statut='f',typ=fonction),
                                 SIGM_YZ  = SIMP(statut='f',typ=fonction),
                                 EPSP     = SIMP(statut='o',typ=fonction),
                                 TEMP     = SIMP(statut='o',typ=fonction),),
             DOMMAGE        = SIMP(statut='f',typ='TXM',into=("LEMAITRE",),defaut="LEMAITRE"),
             MATER          = SIMP(statut='o',typ=mater),
             CUMUL          = SIMP(statut='f',typ='TXM',into=("LINEAIRE",)),
         ),

         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
POST_GOUJ2E=OPER(nom="POST_GOUJ2E",op=187,sd_prod=tabl_post_gouj2e,reentrant='n', 
                 fr=" ",docu="U4.GJ.30-a",
         TABLE           =SIMP(statut='o',typ=tabl_post_rele),
)  ;
#& MODIF COMMANDE  DATE 09/07/2001   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE JMBHH01 J.M.PROIX
POST_K1_K2_K3=OPER(nom="POST_K1_K2_K3",op=188,sd_prod=tabl_post_k,
                   fr="Calcul des FIC par extrapolation du champ de d�placements sur les l�vres de la fissure",
                   docu="U4.82.05-a",reentrant='n',
         MODELISATION  =SIMP(statut='o',typ='TXM',
                             into=("3D","AXIS","D_PLAN","C_PLAN"),
                             fr="Mod�lisation coh�rente avec celle utilis�e pour le calcul des d�placements"),
         FOND_3D       =SIMP(statut='f',typ=fond_fiss,fr="Fond de fissure issu de DEFI_FOND_FISS"),
         b_fond_3d     =BLOC (condition="(FOND_3D != None)",
                         MAILLAGE      = SIMP(statut='o',typ=maillage),
                         PRECISION     = SIMP(statut='f',typ='R',defaut=0.001),
                         NOEUD         = SIMP(statut='f',typ=no,max='**'),
                         GROUP_NO      = SIMP(statut='f',typ=grno,max='**'),
                         SANS_NOEUD    = SIMP(statut='f',typ=no,max='**'),
                         SANS_GROUP_NO = SIMP(statut='f',typ=grno,max='**')
                         ),
         MATER         =SIMP(statut='o',typ=mater,
                             fr="Mat�riau homog�ne et isotrope coh�rent avec celui utilis� pour le calcul des d�placements"),
         TABL_DEPL_SUP =SIMP(statut='o',typ=tabl_post_rele,
                             fr="Table issue de post_releve_t sur les noeuds de la l�vre sup�rieure"),
         TABL_DEPL_INF =SIMP(statut='o',typ=tabl_post_rele,
                             fr="Table issue de post_releve_t sur les noeuds de la l�vre inf�rieure"),
         ABSC_CURV_MAXI=SIMP(statut='f',typ='R',
                             fr="distance maximum � partir du fond de fissure � utiliser pour le calcul"),  
         PREC_VIS_A_VIS= SIMP(statut='f',typ='R',defaut=0.001),
         INST          =SIMP(statut='f',typ='R',max='**'),
         LIST_INST     =SIMP(statut='f',typ=listr8),
             b_acce_reel     =BLOC(condition="(INST != None)or(LIST_INST != None)",
               PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-6),
               CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
             ),
         INFO          =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
         VECT_K1       =SIMP(statut='o',typ='R',max='**',
                             fr="Vecteur normal au plan de fissure, orient� de la l�vre inf�rieure vers la l�vre sup�rieure"),  
         TITRE         =SIMP(statut='f',typ='TXM',max='**'),  
)  ;
#& MODIF COMMANDE  DATE 23/01/2002   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE JMBHH01 J.M.PROIX
POST_RCCM=OPER(nom="POST_RCCM",op= 165,sd_prod=tabl_post_rccm,
               fr="V�rification des crit�res de niveau 0 et certains crit�res de niveau A du RCC-M-B3200 (Edition 1991)",
               docu="U4.83.11-c",reentrant='n',
         MATER           =SIMP(statut='o',typ=mater ),
         TYPE_RESU       =SIMP(statut='f',typ='TXM',defaut="VALE_MAX",into=("VALE_MAX","VALE_INST") ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         MAILLAGE        =SIMP(statut='f',typ=maillage),
         OPTION          =SIMP(statut='o',typ='TXM',max='**',
                               into=("PM_PB",
                                     "SN",
                                     "FATIGUE_SPMAX",
                                     "FATIGUE_ZH210"
                                     ) ),
         SEGMENT         =FACT(statut='o',min=01,max='**',fr="Segment sur lequel s effectue le depouillement",
           regles=(AU_MOINS_UN('CHEMIN','GROUP_NO','NOEUD'),
                   EXCLUS('CHEMIN','GROUP_NO'),
                   EXCLUS('CHEMIN','NOEUD'),),
           INTITULE        =SIMP(statut='f',typ='TXM' ),
           CHEMIN          =SIMP(statut='f',typ=(courbe,surface),),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno),
             b_acce_noeud     =BLOC(condition="(NOEUD != None)or(GROUP_NO != None)",
               PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3),
               CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
             ),
         ),
         TRANSITOIRE     =FACT(statut='o',min=01,max='**',fr="transitoire � d�pouiller",
           regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','LIST_INST','LIST_ORDRE'),),
           RESULTAT        =SIMP(statut='o',typ=(evol_elas,evol_noli) ),
           RESU_SIGM_THER  =SIMP(statut='f',typ=(evol_elas,evol_noli),fr="r�sultat sous chargement thermique seul" ),
           NB_OCCUR        =SIMP(statut='f',typ='I',defaut= 1,fr="nombre d occurences r�elles de ce transitoire" ),
           NOM_CHAM        =SIMP(statut='o',typ='TXM',into=("SIEF_ELNO_ELGA","SIGM_ELNO_DEPL") ),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           LIST_ORDRE      =SIMP(statut='f',typ=listis ),
           INST            =SIMP(statut='f',typ='R',max='**'),
           LIST_INST       =SIMP(statut='f',typ=listr8 ),
           b_inst          =BLOC(condition = "(INST != None) or (LIST_INST != None)" ,
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("ABSOLU","RELATIF") ),
           ), 
         ),
)  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
# ======================================================================
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE G8BHHXD X.DESROCHES
POST_RELEVE_T=OPER(nom="POST_RELEVE_T",op=51,sd_prod=tabl_post_rele,docu="U4.81.21-d",reentrant='n',
         ACTION          =FACT(statut='o',min=01,max='**',
           regles=(AU_MOINS_UN('CHEMIN','GROUP_NO','NOEUD'),
                   EXCLUS('CHEMIN','GROUP_NO'),
                   EXCLUS('CHEMIN','NOEUD'),
                   PRESENT_ABSENT('CHEMIN','GROUP_MA','MAILLE'),
                   UN_PARMI('RESULTAT','CHAM_GD'),            
                   UN_PARMI('TOUT_CMP','NOM_CMP','INVARIANT','ELEM_PRINCIPAUX','RESULTANTE'),
                   PRESENT_PRESENT('TRAC_DIR','DIRECTION'),          
                   PRESENT_PRESENT('TRAC_DIRECTION','DIRECTION'),
                   ENSEMBLE('MOMENT','POINT'),
                   PRESENT_PRESENT('MOMENT','RESULTANTE'),
                   PRESENT_ABSENT('TOUT_CMP','TRAC_DIRECTION','TRAC_NORMALE'),
                   PRESENT_ABSENT('TOUT_CMP','TRAC_DIR','TRAC_NOR'),
                   PRESENT_PRESENT('ORIGINE','AXE_Z'),),
           INTITULE        =SIMP(statut='o',typ='TXM'),  
           CHEMIN          =SIMP(statut='f',typ=(courbe,surface) ),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           FORMAT_C        =SIMP(statut='f',typ='TXM',defaut="MODULE",into=("MODULE","REEL","IMAG")),
           CHAM_GD         =SIMP(statut='f',typ=(cham_no_depl_r,cham_no_temp_r,cham_no_pres_r,cham_no_var2_r,
                                                 cham_elem_sief_r,cham_elem_epsi_r,cham_elem_flux_r,cham_elem_crit_r,
                                                 cham_elem_ener_r,cham_elem_dbel_r,cham_elem_pres_r,cham_elem_erreur,
                                                 cham_elem_vari_r,cham_no_depl_c,cham_no_temp_c,cham_no_pres_c,
                                                 cham_elem_sief_c,cham_elem_epsi_c)),
           RESULTAT        =SIMP(statut='f',typ=(evol_elas,evol_ther,evol_noli,dyna_trans,
                                                 mode_meca,mode_flamb,mode_acou,base_modale,mode_stat,
                                                 mult_elas,fourier_elas,dyna_harmo,acou_harmo)),
           b_sensibilite   =BLOC(condition="RESULTAT != None",
                                 fr="D�finition des param�tres de sensibilit�",
                                 ang="Definition of sensitivity parameters",
             SENSIBILITE     =SIMP(statut='f',typ=(para_sensi,theta_geom),max='**',
                                   fr="Liste des param�tres de sensibilit�.",
                                   ang="List of sensitivity parameters"),),

           b_extrac        =BLOC(condition = "RESULTAT != None",fr="extraction des r�sultats",
             regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','LIST_ORDRE','NUME_MODE','LIST_MODE',         
                            'INST','LIST_INST','FREQ','LIST_FREQ','NOEUD_CMP','NOM_CAS'), ),           
             NOM_CHAM        =SIMP(statut='o',typ='TXM' ),  
             TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),  
             LIST_ORDRE      =SIMP(statut='f',typ=listis),
             NUME_MODE       =SIMP(statut='f',typ='I',max='**'),  
             LIST_MODE       =SIMP(statut='f',typ=listis),
             NOEUD_CMP       =SIMP(statut='f',typ='TXM',max='**'),
             NOM_CAS         =SIMP(statut='f',typ='TXM',max='**'),  
             FREQ            =SIMP(statut='f',typ='R',max='**'),  
             LIST_FREQ       =SIMP(statut='f',typ=listr8),
             INST            =SIMP(statut='f',typ='R',max='**'),  
             LIST_INST       =SIMP(statut='f',typ=listr8),
             PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-6),  
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU")),
           ),
           TOUT_CMP        =SIMP(statut='f',typ='TXM',into=("OUI",)),
           NOM_CMP         =SIMP(statut='f',typ='TXM',max='**'),  
           INVARIANT       =SIMP(statut='f',typ='TXM',into=("OUI",)),
           ELEM_PRINCIPAUX =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           RESULTANTE      =SIMP(statut='f',typ='TXM',max='**'),  
           MOMENT          =SIMP(statut='f',typ='TXM',max='**'),  
           POINT           =SIMP(statut='f',typ='R',max='**'),  

           REPERE          =SIMP(statut='f',typ='TXM',defaut="GLOBAL",
                                 into=("GLOBAL","LOCAL","POLAIRE","UTILISATEUR","CYLINDRIQUE"),),
           ANGL_NAUT       =SIMP(statut='f',typ='R',min=3,max=3),  
           ORIGINE         =SIMP(statut='f',typ='R',min=3,max=3),  
           AXE_Z           =SIMP(statut='f',typ='R',min=3,max=3),  

           TRAC_NOR        =SIMP(statut='f',typ='TXM',into=("OUI",)),
           TRAC_DIR        =SIMP(statut='f',typ='TXM',into=("OUI",)),
           DIRECTION       =SIMP(statut='f',typ='R',max='**'),  
           TRAC_DIRECTION  =SIMP(statut='f',typ='TXM',into=("OUI",)),
           TRAC_NORMALE    =SIMP(statut='f',typ='TXM',into=("OUI",)),
 
           VECT_Y          =SIMP(statut='f',typ='R',max='**'),  
           MOYE_NOEUD      =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON")),
           OPERATION       =SIMP(statut='o',typ='TXM',into=("EXTRACTION","MOYENNE","MOYENNE_RCCM"),max=2),
         ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
POST_SIMPLIFIE=OPER(nom="POST_SIMPLIFIE",op=185,sd_prod=tabl_post_simpli,
                    fr=" ",docu="U4.PS.10-a",reentrant='n',
         MATER           =SIMP(statut='o',typ=(mater) ),
         DEF_EQUI        =FACT(statut='f',min=01,max=01,
           METHODE         =SIMP(statut='f',typ='TXM',max='**',defaut="UTO_2_3",
                                 into=("UTO_2_3",) ),
           EPAIS           =SIMP(statut='o',typ='R'),  
           LONG_FISS       =SIMP(statut='o',typ='R'),  
           LONG_LIGA_INT   =SIMP(statut='o',typ='R'),  
           DEXT            =SIMP(statut='o',typ='R'),  
           TEMP_ANALYSE    =SIMP(statut='f',typ='R'),  
         ),
)  ;
#& MODIF COMMANDE  DATE 07/02/2001   AUTEUR D6BHHJP J.P.LEFEBVRE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
POST_USURE=OPER(nom="POST_USURE",op=153,sd_prod=tabl_post_usur,docu="U4.84.05-c",reentrant='f',
                fr="Calcul des volumes d'usure et des profondeurs d'usure",
         regles=(UN_PARMI('RESU_GENE','PUIS_USURE'),
                 PRESENT_PRESENT('RESU_GENE','NOEUD'),
                 UN_PARMI('INST','LIST_INST'),),
         ETAT_INIT       =FACT(statut='f',min=01,max=01,
           TABL_USURE      =SIMP(statut='f',typ=tabl_post_usur),
           INST_INIT       =SIMP(statut='f',typ='R'),  
                         ),
         RESU_GENE       =SIMP(statut='f',typ=tran_gene),
         NOEUD           =SIMP(statut='f',typ=no,max=1),
         INST_INIT       =SIMP(statut='f',typ='R',defaut=-1.0E+0),  
         INST_FIN        =SIMP(statut='f',typ='R'),  
         NB_BLOC         =SIMP(statut='f',typ='I',defaut= 1 ),  
         PUIS_USURE      =SIMP(statut='f',typ='R'),  
         LOI_USURE       =SIMP(statut='o',typ='TXM',into=("ARCHARD","KWU_EPRI","EDF_MZ")),
         b_archard       =BLOC(condition = "LOI_USURE == 'ARCHARD'",
           regles=(EXCLUS('MATER_USURE','OBSTACLE'),
                   EXCLUS('MOBILE','USURE_OBST'),),
           MOBILE          =FACT(statut='f',min=01,max=01,
             COEF_USURE      =SIMP(statut='o',typ='R'), 
           ),   
           OBSTACLE        =FACT(statut='f',min=01,max=01,
             COEF_USURE      =SIMP(statut='o',typ='R'), 
           ),   
           MATER_USURE     =SIMP(statut='f',typ='TXM'),  
           USURE_OBST      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
         ),
         b_kwu_epri        =BLOC(condition = "LOI_USURE == 'KWU_EPRI'",
           regles=(UN_PARMI('MOBILE','MATER_USURE'), 
                   EXCLUS('MATER_USURE','OBSTACLE'),
                   EXCLUS('MOBILE','USURE_OBST'),),
           MOBILE          =FACT(statut='f',min=01,max=01,
             COEF_FNOR       =SIMP(statut='f',typ='R'),  
             COEF_VTAN       =SIMP(statut='f',typ='R'),  
             COEF_USURE      =SIMP(statut='f',typ='R'),  
             COEF_K          =SIMP(statut='f',typ='R',defaut=5.0E+0),  
             COEF_C          =SIMP(statut='f',typ='R',defaut=10.0E+0),  
           ),   
           OBSTACLE        =FACT(statut='f',min=01,max=01,
             COEF_FNOR       =SIMP(statut='f',typ='R' ),  
             COEF_VTAN       =SIMP(statut='f',typ='R' ),  
             COEF_USURE      =SIMP(statut='o',typ='R'), 
             COEF_K          =SIMP(statut='f',typ='R',defaut=5.0E+0),  
             COEF_C          =SIMP(statut='f',typ='R',defaut=10.0E+0),  
           ),   
           MATER_USURE     =SIMP(statut='f',typ='TXM'),  
           USURE_OBST      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
           FNOR_MAXI       =SIMP(statut='f',typ='R' ),  
           VTAN_MAXI       =SIMP(statut='f',typ='R' ),  
         ),
         b_edf_mz          =BLOC(condition = "LOI_USURE == 'EDF_MZ'",
           regles=(UN_PARMI('MOBILE','MATER_USURE'), 
                   EXCLUS('MATER_USURE','OBSTACLE'),
                   EXCLUS('MOBILE','USURE_OBST'),),
           MOBILE          =FACT(statut='f',min=01,max=01,
             COEF_USURE      =SIMP(statut='f',typ='R',defaut=1.0E-13),  
             COEF_B          =SIMP(statut='f',typ='R',defaut=1.2E+0),  
             COEF_N          =SIMP(statut='f',typ='R',defaut=2.44E-8),  
             COEF_S          =SIMP(statut='f',typ='R',defaut=1.14E-16),  
           ),   
           OBSTACLE        =FACT(statut='f',min=01,max=01,
             COEF_USURE      =SIMP(statut='o',typ='R',defaut=1.0E-13), 
             COEF_B          =SIMP(statut='f',typ='R',defaut=1.2E+0),  
             COEF_N          =SIMP(statut='f',typ='R',defaut=2.44E-8),  
             COEF_S          =SIMP(statut='f',typ='R',defaut=1.14E-16),  
           ),   
           MATER_USURE     =SIMP(statut='f',typ='TXM'),  
           USURE_OBST      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON")),
         ),
         SECTEUR         =FACT(statut='f',min=01,max='**',
           CONTACT         =SIMP(statut='f',typ='TXM',into=("TUBE_BAV","TUBE_ALESAGE","TUBE_4_ENCO",  
                                                            "GRAPPE_ALESAGE","TUBE_3_ENCO","TUBE_TUBE", 
                                                            "GRAPPE_1_ENCO","GRAPPE_2_ENCO")),
           COEF_USUR_MOBILE=SIMP(statut='f',typ='R'),  
           COEF_USUR_OBST  =SIMP(statut='f',typ='R'),  
           ANGL_INIT       =SIMP(statut='f',typ='R'),  
           ANGL_FIN        =SIMP(statut='f',typ='R'),  
         ),
         CONTACT         =SIMP(statut='f',typ='TXM',into=("TUBE_BAV","TUBE_ALESAGE","TUBE_4_ENCO",    
                                                          "GRAPPE_ALESAGE","TUBE_3_ENCO","TUBE_TUBE",        
                                                          "GRAPPE_1_ENCO","GRAPPE_2_ENCO")),
         RAYON_MOBILE    =SIMP(statut='f',typ='R'),  
         RAYON_OBST      =SIMP(statut='f',typ='R'),  
         LARGEUR_OBST    =SIMP(statut='f',typ='R'),  
         ANGL_INCLI      =SIMP(statut='f',typ='R'),  
         ANGL_ISTHME     =SIMP(statut='f',typ='R'),  
         ANGL_IMPACT     =SIMP(statut='f',typ='R'),  
         INST            =SIMP(statut='f',typ='R',max='**'),  
         LIST_INST       =SIMP(statut='f',typ=listr8),
         COEF_INST       =SIMP(statut='f',typ='R',defaut=1.0E+0),  
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
POST_ZAC=OPER(nom="POST_ZAC",op= 175,sd_prod=mult_elas,docu="U4.83.21-b",reentrant='n',
              fr="Donne l'�tat adapt� ou accommod� d'une structure sous chargement cyclique �lastique affine ou non",
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater),
         EXCIT           =FACT(statut='o',min=01,max='**',
           CHARGE          =SIMP(statut='o',typ=char_meca),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
           TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FIXE_CSTE",into=("FIXE_CSTE",)),
         ),
         EVOL_ELAS       =SIMP(statut='o',typ=evol_elas),
         b_evol_elas     =BLOC(condition="EVOL_ELAS != None",
           regles=(UN_PARMI('NUME_ORDRE','LIST_INST','INST'),),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),  
           LIST_INST       =SIMP(statut='f',typ=listr8),
           INST            =SIMP(statut='f',typ='R',max='**'),  
         ),
         TEMP_ZAC        =SIMP(statut='f',typ='R',defaut=0.0E+0),  
         EVOL_NOLI       =SIMP(statut='f',typ=evol_noli),
         b_evol_noli     =BLOC(condition="EVOL_NOLI != None",
           INST_MAX        =SIMP(statut='o',typ='R'),  
         ),
         PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3),  
         CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU")),

)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
POURSUITE=MACRO(nom="POURSUITE",op=0,repetable='n',fr="Poursuite d une �tude",
                docu="U4.11.03-f1",sd_prod = ops.POURSUITE,
                op_init = ops.POURSUITE_context,fichier_ini = 1,
         PAR_LOT         =SIMP(fr="mode de traitement des commandes",statut='f',typ='TXM',
                           into=("OUI","NON"),defaut="OUI"),
         BASE            =FACT(fr="d�finition des parm�tres associ�s aux bases JEVEUX",
                               statut='f',min=1,max=3,
           FICHIER         =SIMP(fr="nom de la base",statut='o',typ='TXM'),
           TITRE           =SIMP(statut='f',typ='TXM'),
           CAS             =SIMP(statut='f',typ='TXM'),
           NMAX_ENRE       =SIMP(fr="nombre maximum d enregistrements",statut='f',typ='I'),
           LONG_ENRE       =SIMP(fr="longueur des enregistrements",statut='f',typ='I'),
           LONG_REPE       =SIMP(fr="longueur du r�pertoire",statut='f',typ='I'),
         ),
         IMPRESSION      =FACT(statut='f',min=1,max=3,
           FICHIER         =SIMP(statut='o',typ='TXM'),
           UNITE           =SIMP(statut='o',typ='I'),
         ),
         CATALOGUE       =FACT(statut='f',min=1,max=10,
           FICHIER         =SIMP(statut='o',typ='TXM'),
           TITRE           =SIMP(statut='f',typ='TXM'),
           UNITE           =SIMP(statut='f',typ='I'),
         ),
         DEBUG           =FACT(fr="option de d�boggage reserv�e aux d�veloppeurs",
                               statut='f',min=1,max=1,
           JXVERI          =SIMP(fr="v�rifie l int�grit� de la segmentation m�moire",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           JEVEUX          =SIMP(fr="force les d�chargement sur disque",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           ENVIMA          =SIMP(fr="imprime les valeurs d�finies dans ENVIMA",
                                 statut='f',typ='TXM',into=('TES',)),
         ),
         MEMOIRE         =FACT(fr="mode de gestion m�moire utilis�",statut='f',min=1,max=1,
           GESTION         =SIMP(statut='f',typ='TXM',into=('COMPACTE','RAPIDE'),defaut='RAPIDE'),
           TYPE_ALLOCATION =SIMP(statut='f',typ='I',into=(1,2,3,4),defaut=1),
           TAILLE          =SIMP(statut='f',typ='I'),
           TAILLE_BLOC     =SIMP(statut='f',typ='R',defaut=800.),
           PARTITION       =SIMP(statut='f',typ='R' ),
         ),
         CODE            =FACT("d�finition d un nom pour l'esemble d'une �tude",
                               statut='f',min=1,max=1,
           NOM             =SIMP(statut='o',typ='TXM'),
           UNITE           =SIMP(statut='f',typ='I',defaut=15),
         ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
PRE_CHAR_IDEAS=PROC(nom="PRE_CHAR_IDEAS",op=100,docu="U7.01.02-e",
                    fr="Conversion de conditions aux limites et chargements IDEAS en commandes Aster",
         UNITE_IDEAS     =SIMP(statut='f',typ='I',defaut=19),  
         UNITE_ASTER     =SIMP(statut='f',typ='I',defaut=21),  
         MODELE          =SIMP(statut='o',typ=modele),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
PRE_GIBI=PROC(nom="PRE_GIBI",op=49,docu="U7.01.11-f",
              fr="Conversion d un fichier de maillage GIBI",
         UNITE_GIBI      =SIMP(statut='f',typ='I',defaut=19),  
         UNITE_MAILLAGE  =SIMP(statut='f',typ='I',defaut=20),  
)  ;
#& MODIF COMMANDE  DATE 17/09/2001   AUTEUR CIBHHGB G.BERTRAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
PRE_GMSH=PROC(nom="PRE_GMSH",op=47,docu="U7.01.01-f",
               fr="Conversion d un fichier universel GMSH au format Aster",
         UNITE_GMSH      =SIMP(statut='f',typ='I',defaut=19),  
         UNITE_MAILLAGE  =SIMP(statut='f',typ='I',defaut=20),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
PRE_IDEAS=PROC(nom="PRE_IDEAS",op=47,docu="U7.01.01-f",
               fr="Conversion d un fichier universel IDEAS-SUPERTAB au format Aster",
         UNITE_IDEAS     =SIMP(statut='f',typ='I',defaut=19),  
         UNITE_MAILLAGE  =SIMP(statut='f',typ='I',defaut=20),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
PROCEDURE=PROC(nom="PROCEDURE",op=-3, docu="U4.13.03-e",
          fr="Nommer le fichier de commandes secondaires",
          NOM  =SIMP(statut='f',typ='TXM',defaut=" "),
) ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def prod_matr_cham_prod(MATR_ASSE,**args):
  if AsType(MATR_ASSE) == matr_asse_depl_r : return cham_no_depl_r
  if AsType(MATR_ASSE) == matr_asse_depl_c : return cham_no_depl_c
  if AsType(MATR_ASSE) == matr_asse_temp_r : return cham_no_temp_r
  if AsType(MATR_ASSE) == matr_asse_pres_c : return cham_no_pres_c
  raise AsException("type de concept resultat non prevu")

PROD_MATR_CHAM=OPER(nom="PROD_MATR_CHAM",op= 156,sd_prod=prod_matr_cham_prod,
                    fr="Effectuer le produit d une matrice par un vecteur",
                    docu="U4.72.06-b",reentrant='n',
         MATR_ASSE       =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_depl_c,matr_asse_temp_r,matr_asse_pres_c ) ),
         CHAM_NO         =SIMP(statut='o',typ=(cham_no_depl_r,cham_no_depl_c,cham_no_temp_r,cham_no_pres_c ) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;
#& MODIF COMMANDE  DATE 12/09/2001   AUTEUR MCOURTOI M.COURTOIS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def proj_champ_prod(RESULTAT=None,CHAM_NO_REFE=None,**args ):
    if AsType(RESULTAT)     == evol_ther      : return evol_ther
    if AsType(RESULTAT)     == evol_elas      : return evol_elas
    if AsType(RESULTAT)     == evol_noli      : return evol_noli
    if AsType(RESULTAT)     == evol_char      : return evol_char
    if AsType(CHAM_NO_REFE) == cham_no_depl_r : return cham_no_depl_r
    if AsType(CHAM_NO_REFE) == cham_no_depl_c : return cham_no_depl_c
    if AsType(CHAM_NO_REFE) == cham_no_pres_c : return cham_no_pres_c
    if AsType(CHAM_NO_REFE) == cham_no_temp_r : return cham_no_temp_r
    if AsType(CHAM_NO_REFE) == cham_no_epsi_r : return cham_no_epsi_r
    if AsType(CHAM_NO_REFE) == cham_no_sief_r : return cham_no_sief_r
    if AsType(CHAM_NO_REFE) == cham_no_flux_r : return cham_no_flux_r
    raise AsException("type de concept resultat non prevu")

PROJ_CHAMP=OPER(nom="PROJ_CHAMP",op= 166,sd_prod=proj_champ_prod,docu="U4.72.05-c1",reentrant='n',
                fr="Projection d un champ aux noeuds sur les noeuds d un autre maillage",
#
         METHODE         =SIMP(statut='f',typ='TXM',defaut="NUAGE_DEG_1",
                               into=("NUAGE_DEG_0","NUAGE_DEG_1","ELEM",) ),
         b_nuage         =BLOC(condition="(METHODE=='NUAGE_DEG_1') or (METHODE=='NUAGE_DEG_0')",
                               fr="Lissage d un nuage de points",
           CHAM_NO         =SIMP(statut='f',typ=(cham_no_depl_r,cham_no_depl_c,cham_no_pres_c,cham_no_temp_r,
                                                 cham_no_epsi_r,cham_no_sief_r,cham_no_flux_r)),
           CHAM_NO_REFE    =SIMP(statut='f',typ=(cham_no_depl_r,cham_no_depl_c,cham_no_pres_c,cham_no_temp_r,
                                                 cham_no_epsi_r,cham_no_sief_r,cham_no_flux_r)),
         ),
         b_elem          =BLOC(condition="METHODE=='ELEM'",
                              fr="Utilisation des fonctions de forme",
           regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','FREQ','LIST_INST','LIST_FREQ','LIST_ORDRE'), ),
           RESULTAT        =SIMP(statut='f',typ=(evol_ther,evol_elas,evol_noli,evol_char) ),
           MODELE_1        =SIMP(statut='f',typ=modele),
           MODELE_2        =SIMP(statut='f',typ=modele),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI",) ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**' ),
           LIST_ORDRE      =SIMP(statut='f',typ=listis),
           INST            =SIMP(statut='f',typ='R',max='**' ),
           LIST_INST       =SIMP(statut='f',typ=listr8),
           FREQ            =SIMP(statut='f',typ='R',max='**' ),
           LIST_FREQ       =SIMP(statut='f',typ=listr8),
         ),

         VIS_A_VIS       =FACT(statut='f',min=01,max='**',
           regles=(AU_MOINS_UN('TOUT_1','GROUP_MA_1','MAILLE_1','GROUP_NO_1','NOEUD_1'),
                   AU_MOINS_UN('TOUT_2','GROUP_MA_2','MAILLE_2','GROUP_NO_2','NOEUD_2'),),
           TOUT_1          =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA_1      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_1        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_1      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_1         =SIMP(statut='f',typ=no,max='**'),
           TOUT_2          =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA_2      =SIMP(statut='f',typ=grma,max='**'),
           MAILLE_2        =SIMP(statut='f',typ=ma,max='**'),
           GROUP_NO_2      =SIMP(statut='f',typ=grno,max='**'),
           NOEUD_2         =SIMP(statut='f',typ=no,max='**'),
         ),

         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),
)  ;
#& MODIF COMMANDE  DATE 26/09/2001   AUTEUR CIBHHPD D.NUNEZ 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def matr_asse_gene_prod(MATR_ASSE,MATR_ASSE_GENE,**args):
  if AsType(MATR_ASSE) == matr_asse_depl_r  : return matr_asse_gene_r
  if AsType(MATR_ASSE_GENE) == matr_asse_gene_r  : return matr_asse_gene_r
  if AsType(MATR_ASSE) == matr_asse_depl_c  : return matr_asse_gene_c
  if AsType(MATR_ASSE_GENE) == matr_asse_gene_c  : return matr_asse_gene_c
  raise AsException("type de concept resultat non prevu")

PROJ_MATR_BASE=OPER(nom="PROJ_MATR_BASE",op=  71,sd_prod=matr_asse_gene_prod,
                    fr="Projection d une matrice assembl�e sur une base (modale ou de RITZ)",
                    docu="U4.63.12-e",reentrant='n',
         regles=(UN_PARMI('MATR_ASSE','MATR_ASSE_GENE'),),            
         BASE            =SIMP(statut='o',typ=(mode_meca,base_modale,mode_gene ) ),
         NUME_DDL_GENE   =SIMP(statut='o',typ=nume_ddl_gene ),
         NB_VECT         =SIMP(statut='f',typ='I',defaut= 9999 ),
         MATR_ASSE       =SIMP(statut='f',typ=(matr_asse_depl_r,matr_asse_depl_c) ),
         MATR_ASSE_GENE  =SIMP(statut='f',typ=(matr_asse_gene_r,matr_asse_gene_c) ),
)  ;

#& MODIF COMMANDE  DATE 19/12/2001   AUTEUR CIBHHAB N.RAHNI 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def proj_mesu_modal_prod(MESURE,**args):
     vale=MESURE['NOM_PARA']
     if  vale == 'INST'   : return tran_gene
     raise AsException("type de concept resultat non prevu")

PROJ_MESU_MODAL=OPER(nom="PROJ_MESU_MODAL",op= 193,
                     sd_prod=proj_mesu_modal_prod,
                     docu="U4.73.01-a",reentrant='n',
                     fr="Extrapolation de resultats experimentaux sur un modele numerique en dynamique",

# commentaire C. Durand-13/10/2000 :
#le mot cle NOM_PARA, par construction, vaut tjs INST : donc on retourne TRAN_GENE a chaque fois
#def proj_mesu_modal_prod(**args):
#     vale=args['MESURE'].get_child('NOM_PARA').get_valeur()
#     if  vale == 'INST'   : return tran_gene
#     raise AsException("type de concept resultat non prevu")
#PROJ_MESU_MODAL=OPER(nom="PROJ_MESU_MODAL",op= 193,sd_prod=proj_mesu_modal_prod,)

         MODELE          =SIMP(statut='f',typ=(modele) ),
         MASS_GENE       =SIMP(statut='o',typ=(matr_asse_gene_r) ),
         RIGI_GENE       =SIMP(statut='o',typ=(matr_asse_gene_r) ),
         MESURE          =FACT(statut='o',min=01,max=01,
           MODELE          =SIMP(statut='o',typ=(modele) ),
           MAILLAGE        =SIMP(statut='o',typ=(maillage) ),
           CARA_ELEM       =SIMP(statut='o',typ=(cara_elem) ),
           UNITE           =SIMP(statut='f',typ='I',defaut= 33 ),  
           NOM_PARA        =SIMP(statut='f',typ='TXM',defaut="INST",into=("INST",) ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),  
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU",) ),
           NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL","SIGM_NOEU_DEPL","EPSI_NOEU_DEPL",) ),
                         ),
         REGULARISATION  =FACT(statut='f',min=01,max=01,
      regles=(UN_PARMI('COEF_PONDER','COEF_PONDER_F', ),),
           METHODE         =SIMP(statut='f',typ='TXM',defaut="TIKHONOV",into=("TIKHONOV",) ),
           NORM_MIN        =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
           COEF_PONDER     =SIMP(statut='f',typ='R',max='**' ),  
           COEF_PONDER_F   =SIMP(statut='f',typ=(fonction),max='**' ),
                         ),
                       )  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
PROJ_SPEC_BASE=OPER(nom="PROJ_SPEC_BASE",op= 146,sd_prod=tabl_intsp,docu="U4.63.14-c",reentrant='n',
                    fr="Projection d un ou plusieurs spectres de turbulenc sur un ensemble de bases modales ",
      regles=(UN_PARMI('BASE_ELAS_FLUI','MODE_MECA','CHAM_NO'),
              ENSEMBLE('FREQ_INIT','FREQ_FIN','NB_POIN'),),
         SPEC_TURB       =SIMP(statut='o',typ=spectre,max='**' ),
         BASE_ELAS_FLUI  =SIMP(statut='f',typ=melasflu ),
         MODE_MECA       =SIMP(statut='f',typ=mode_meca ),
         CHAM_NO         =SIMP(statut='f',typ=cham_no_depl_r ),
         FREQ_INIT       =SIMP(statut='f',typ='R',val_min=0.E+0 ),  
         FREQ_FIN        =SIMP(statut='f',typ='R',val_min=0.E+0 ),  
         NB_POIN         =SIMP(statut='f',typ='I' ),  
         OPTION          =SIMP(statut='f',typ='TXM',defaut="TOUT",into=("TOUT","DIAG")),
         GROUP_MA        =SIMP(statut='f',typ=grma),
#  Quel est le type attendu derriere  MODELE_INTERFACE         
         MODELE_INTERFACE=SIMP(statut='f',typ=modele),
         VECT_X          =SIMP(statut='f',typ='R',min=3,max=3 ),  
         VECT_Y          =SIMP(statut='f',typ='R',min=3,max=3 ),  
         ORIG_AXE        =SIMP(statut='f',typ='R',min=3,max=3 ),  
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
PROJ_VECT_BASE=OPER(nom="PROJ_VECT_BASE",op=  72,sd_prod=vect_asse_gene,
                    fr="Projection d un vecteur assembl� sur une base (modale ou de RITZ)",
                    docu="U4.63.13-e",reentrant='n',
         regles=(UN_PARMI('VECT_ASSE','VECT_ASSE_GENE'),),              
         BASE            =SIMP(statut='o',typ=(mode_meca,base_modale,mode_gene ) ),
         NUME_DDL_GENE   =SIMP(statut='o',typ=nume_ddl_gene ),
         NB_VECT         =SIMP(statut='f',typ='I',defaut= 9999 ),
         TYPE_VECT       =SIMP(statut='f',typ='TXM',defaut="FORC"),
         VECT_ASSE       =SIMP(statut='f',typ=cham_no_depl_r ),
         VECT_ASSE_GENE  =SIMP(statut='f',typ=vect_asse_gene ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
RECA_WEIBULL=OPER(nom="RECA_WEIBULL",op= 197,sd_prod=tabl_reca_weib,
                     fr=" ",docu="U4.82.06-a",reentrant='n',
         LIST_PARA       =SIMP(statut='o',typ='TXM',max='**',into=("SIGM_REFE","M",) ),
         RESU            =FACT(statut='o',min=01,max='**',
           regles=(EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','LIST_INST',),
                   AU_MOINS_UN('TOUT','GROUP_MA','MAILLE', ),),
           EVOL_NOLI       =SIMP(statut='o',typ=(evol_noli) ),
           MODELE          =SIMP(statut='o',typ=(modele) ),
           CHAM_MATER      =SIMP(statut='o',typ=(cham_mater) ),
           TEMPE           =SIMP(statut='f',typ='R' ),
           LIST_INST_RUPT  =SIMP(statut='o',typ='R',max='**' ),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**' ),
           INST            =SIMP(statut='f',typ='R',max='**' ),
           LIST_INST       =SIMP(statut='f',typ=(listr8) ),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           COEF_MULT       =SIMP(statut='f',typ='R',defaut= 1.E0 ),
                         ),
         OPTION          =SIMP(statut='f',typ='TXM',defaut="SIGM_ELGA",into=("SIGM_ELGA","SIGM_ELMOY",) ),
         CORR_PLAST      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
         METHODE         =SIMP(statut='f',typ='TXM',defaut="MAXI_VRAI",into=("MAXI_VRAI","REGR_LINE",) ),
         INCO_GLOB_RELA  =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
         ITER_GLOB_MAXI  =SIMP(statut='f',typ='I',defaut= 10 ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ,) ),
                       )  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE MCOURTOI M.COURTOIS
def recu_fonction_prod(RESULTAT=None,TABLE=None,OBSTACLE=None,
                       RESU_GENE=None,BASE_ELAS_FLUI=None,CHAM_GD=None,
                       TYPE_RESU=None,**args):
  if AsType(RESULTAT) == dyna_harmo : return fonction_c
#  On ne sait pas interpreter les deux conditions suivantes
  if TABLE != None :
     if TYPE_RESU != None :
        if TYPE_RESU == "FONCTION_C" : return fonction_c
        if TYPE_RESU == "FONCTION"   : return fonction
     else:
        return fonction
  if RESU_GENE      != None         : return fonction
  if BASE_ELAS_FLUI != None         : return fonction
  if RESULTAT       != None         : return fonction
  if CHAM_GD        != None         : return fonction
  if OBSTACLE       != None         : return fonction
  raise AsException("type de concept resultat non prevu")

RECU_FONCTION=OPER(nom="RECU_FONCTION",op=  90,sd_prod=recu_fonction_prod,
                   fr="Extraire sous forme d une fonction, l �volution temporelle d une composante d un champ ou d une table",
                   docu="U4.32.03-e1",reentrant='n',
         regles=(UN_PARMI('CHAM_GD','RESULTAT','RESU_GENE','TABLE','BASE_ELAS_FLUI','OBSTACLE'),),

         CHAM_GD         =SIMP(statut='f',typ=(cham_no_depl_r,cham_no_temp_r,cham_no_pres_r,cham_elem_sief_r,
                                               cham_elem_vari_r,cham_elem_epsi_r,cham_elem_flux_r,
                                               cham_elem_pres_r,cham_elem_meta_r ) ),
         RESULTAT        =SIMP(statut='f',typ=(evol_elas,dyna_trans,evol_noli,evol_ther,dyna_harmo ) ),
         RESU_GENE       =SIMP(statut='f',typ=tran_gene),
#  concept table � cr�er
         TABLE           =SIMP(statut='f',typ=table),
         BASE_ELAS_FLUI  =SIMP(statut='f',typ=melasflu),
         REPERE          =SIMP(statut='f',typ='TXM',into=("POLAIRE","GLOBAL") ),
         OBSTACLE        =SIMP(statut='f',typ=obstacle),

         b_tran_gene = BLOC ( condition = "RESU_GENE != None",
                              fr="R�cup�ration de la fonction concernant les chocs � partir d un concept TRAN_GENE",
            regles=(PRESENT_PRESENT('SOUS_STRUC','INTITULE'),
                    PRESENT_ABSENT('MULT_APPUI','CORR_STAT'),),
             MULT_APPUI      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
             CORR_STAT       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
             ACCE_MONO_APPUI =SIMP(statut='f',typ=fonction),
             PARA_X          =SIMP(statut='f',typ='TXM' ),
             PARA_Y          =SIMP(statut='f',typ='TXM' ),
             SOUS_STRUC      =SIMP(statut='f',typ='TXM' ),
             LIST_PARA       =SIMP(statut='f',typ=listr8 ),
             INTITULE        =SIMP(statut='f',typ='TXM' ),
         ),
         b_base_elas_flui = BLOC ( condition = "BASE_ELAS_FLUI != None",
                                   fr="R�cup�ration de la fonction � partir d un concept melasflu",
           regles=(UN_PARMI('TOUT_ORDRE','NUME_ORDRE'),),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           NUME_MODE       =SIMP(statut='o',typ='I' ),
           PARA_X          =SIMP(statut='o',typ='TXM',into=("VITE_FLU",) ),
           PARA_Y          =SIMP(statut='o',typ='TXM',into=("FREQ","AMOR") ),
         ),
         b_table = BLOC ( condition = "TABLE != None",fr="R�cup�ration de la fonction � partir d un concept table",
           regles=(UN_PARMI('PARA_X','NOM_PARA_TABL'),
                   PRESENT_PRESENT('PARA_X','PARA_Y'),),
           PARA_X          =SIMP(statut='f',typ='TXM',
                                 fr="1�re colonne de la table qui d�finit la fonction � r�cup�rer", ),
           PARA_Y          =SIMP(statut='f',typ='TXM',
                                 fr="2�me colonne de la table qui d�finit la fonction � r�cup�rer", ),
           NOM_PARA_TABL   =SIMP(statut='f',typ='TXM',into=("FONCTION",),
                                 fr="Nom du param�tre de la table � qui est associ� la fonction" ),
           b_nom_para_tabl = BLOC (condition = "NOM_PARA_TABL != None",
             TYPE_RESU       =SIMP(statut='f',typ='TXM',defaut="FONCTION",into=("FONCTION","FONCTION_C") ),
           ),

           FILTRE          =FACT(statut='f',min=1,max='**',
              NOM_PARA        =SIMP(statut='o',typ='TXM' ),
              CRIT_COMP       =SIMP(statut='f',typ='TXM',defaut="EQ",
                                    into=("EQ","LT","GT","NE","LE","GE","VIDE",
                                          "NON_VIDE","MAXI","ABS_MAXI","MINI","ABS_MINI") ),
              b_vale          =BLOC(condition = "(CRIT_COMP in ('EQ','NE','GT','LT','GE','LE'))",
                 regles=(UN_PARMI('VALE','VALE_I','VALE_K','VALE_C',),),
                 VALE            =SIMP(statut='f',typ='R' ),
                 VALE_I          =SIMP(statut='f',typ='I' ),
                 VALE_C          =SIMP(statut='f',typ='C' ),
                 VALE_K          =SIMP(statut='f',typ='TXM' ),),

              CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
              PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           ),
         ),
# RESULTAT
         b_resu = BLOC ( condition = "RESULTAT != None", fr="Op�randes en cas de RESULTAT",
           regles=(
#    A voir par Mathieu Courtois : il existe de tests (SDNX300B) qui ne satisfont pas ce UN_PARMI
#           UN_PARMI('TOUT_ORDRE','NUME_ORDRE','LIST_ORDRE','TOUT_INST','LIST_INST','FREQ','LIST_FREQ'),
                   AU_MOINS_UN('MAILLE','GROUP_MA','GROUP_NO','NOEUD','NOEUD_CHOC','GROUP_NO_CHOC','NOM_PARA_RESU'),
                   PRESENT_PRESENT('MAILLE','NOM_CMP'),
                   PRESENT_PRESENT('GROUP_MA','NOM_CMP'),
                   PRESENT_PRESENT('NOEUD','NOM_CMP'),
                   PRESENT_PRESENT('GROUP_NO','NOM_CMP'),
                   PRESENT_PRESENT('POINT','NOM_CMP'),
                   EXCLUS('POINT','NOEUD'),
                   EXCLUS('GROUP_MA','MAILLE'),
                   EXCLUS('GROUP_NO','NOEUD'),
                   EXCLUS('NOEUD_CHOC','GROUP_NO_CHOC'),
                   UN_PARMI('NOM_CHAM','NOM_PARA_RESU'),),
           NOM_CHAM        =SIMP(statut='f',typ='TXM' ),
           NOM_PARA_RESU   =SIMP(statut='f',typ='TXM' ),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           LIST_ORDRE      =SIMP(statut='f',typ=listis ),
           TOUT_INST       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           INST            =SIMP(statut='f',typ='R',max='**'),
           LIST_INST       =SIMP(statut='f',typ=listr8 ),
           FREQ            =SIMP(statut='f',typ='R',max='**'),
           LIST_FREQ       =SIMP(statut='f',typ=listr8 ),
           b_prec = BLOC ( condition = "(INST != None) or (LIST_INST != None) or (FREQ != None) or (LIST_FREQ != None)",
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
             INTERP_NUME     =SIMP(statut='f',typ='TXM',max=2,into=("NON","LIN") ),
           ),
           NOM_CMP         =SIMP(statut='f',typ='TXM' ),

           MAILLE          =SIMP(statut='f',typ=ma),
           GROUP_MA        =SIMP(statut='f',typ=grma),
           NOEUD           =SIMP(statut='f',typ=no),
           GROUP_NO        =SIMP(statut='f',typ=grno),
           POINT           =SIMP(statut='f',typ='I' ),
           SOUS_POINT      =SIMP(statut='f',typ='I' ),
           NOEUD_CHOC      =SIMP(statut='f',typ=no),
           GROUP_NO_CHOC   =SIMP(statut='f',typ=grno),
         ),
# RESU_GENE
         b_resu_gene = BLOC ( condition = "RESU_GENE != None", fr="Op�randes en cas de RESU_GENE",
#    A voir par Mathieu Courtois : il existe de tests (SDNX300B) qui ne satisfont pas ce UN_PARMI
#           regles=(UN_PARMI('TOUT_ORDRE','NUME_ORDRE','LIST_ORDRE','TOUT_INST','LIST_INST','FREQ','LIST_FREQ'),),
           NOM_CHAM        =SIMP(statut='f',typ='TXM',into=("DEPL","VITE","ACCE","PTEM") ),
           TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           NUME_ORDRE      =SIMP(statut='f',typ='I',max='**'),
           LIST_ORDRE      =SIMP(statut='f',typ=listis ),
           TOUT_INST       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           INST            =SIMP(statut='f',typ='R',max='**'),
           LIST_INST       =SIMP(statut='f',typ=listr8 ),
           FREQ            =SIMP(statut='f',typ='R',max='**'),
           LIST_FREQ       =SIMP(statut='f',typ=listr8 ),
           b_prec = BLOC ( condition = "(INST != None) or (LIST_INST != None) or (FREQ != None) or (LIST_FREQ != None)",
             PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
             CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
             INTERP_NUME     =SIMP(statut='f',typ='TXM',max=2,into=("NON","LIN") ),
           ),
           b_local_cham = BLOC ( condition = "NOM_CHAM!='PTEM'", fr="Op�randes de localisation du champ",
             regles=(AU_MOINS_UN('MAILLE','GROUP_MA','GROUP_NO','NOEUD','NOEUD_CHOC','GROUP_NO_CHOC'),
                     PRESENT_PRESENT('MAILLE','NOM_CMP'),
                     PRESENT_PRESENT('GROUP_MA','NOM_CMP'),
                     PRESENT_PRESENT('NOEUD','NOM_CMP'),
                     PRESENT_PRESENT('GROUP_NO','NOM_CMP'),
                     PRESENT_PRESENT('POINT','NOM_CMP'),
                     EXCLUS('POINT','NOEUD'),
                     EXCLUS('GROUP_MA','MAILLE'),
                     EXCLUS('GROUP_NO','NOEUD'),
                     EXCLUS('NOEUD_CHOC','GROUP_NO_CHOC'),),
             NOM_CMP         =SIMP(statut='f',typ='TXM' ),

             MAILLE          =SIMP(statut='f',typ=ma),
             GROUP_MA        =SIMP(statut='f',typ=grma),
             NOEUD           =SIMP(statut='f',typ=no),
             GROUP_NO        =SIMP(statut='f',typ=grno),
             POINT           =SIMP(statut='f',typ='I' ),
             SOUS_POINT      =SIMP(statut='f',typ='I' ),
             NOEUD_CHOC      =SIMP(statut='f',typ=no),
             GROUP_NO_CHOC   =SIMP(statut='f',typ=grno),
           ),
         ),
# CHAM_GD
         b_cham_gd = BLOC ( condition = "(CHAM_GD != None)", fr="Op�randes en cas de CHAM_GD",

           regles=(AU_MOINS_UN('MAILLE','GROUP_MA','GROUP_NO','NOEUD','NOEUD_CHOC','GROUP_NO_CHOC'),
                   PRESENT_PRESENT('MAILLE','NOM_CMP'),
                   PRESENT_PRESENT('GROUP_MA','NOM_CMP'),
                   PRESENT_PRESENT('NOEUD','NOM_CMP'),
                   PRESENT_PRESENT('GROUP_NO','NOM_CMP'),
                   PRESENT_PRESENT('POINT','NOM_CMP'),
                   EXCLUS('POINT','NOEUD'),
                   EXCLUS('GROUP_MA','MAILLE'),
                   EXCLUS('GROUP_NO','NOEUD'),
                   EXCLUS('NOEUD_CHOC','GROUP_NO_CHOC'),),
           NOM_CMP         =SIMP(statut='f',typ='TXM' ),

           MAILLE          =SIMP(statut='f',typ=ma),
           GROUP_MA        =SIMP(statut='f',typ=grma),
           NOEUD           =SIMP(statut='f',typ=no),
           GROUP_NO        =SIMP(statut='f',typ=grno),
           POINT           =SIMP(statut='f',typ='I' ),
           SOUS_POINT      =SIMP(statut='f',typ='I' ),
           NOEUD_CHOC      =SIMP(statut='f',typ=no),
           GROUP_NO_CHOC   =SIMP(statut='f',typ=grno),
         ),
###
         NOM_PARA        =SIMP(statut='f',typ='TXM',
                               into=("DX","DY","DZ","DRX","DRY","DRZ","TEMP",
                                     "INST","X","Y","Z","EPSI","FREQ","PULS","AMOR","ABSC") ),
         NOM_RESU        =SIMP(statut='f',typ='TXM' ),
         INTERPOL        =SIMP(statut='f',typ='TXM',max=2,into=("NON","LIN","LOG") ),
         PROL_DROITE     =SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),
         PROL_GAUCHE     =SIMP(statut='f',typ='TXM',into=("CONSTANT","LINEAIRE","EXCLU") ),

         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2 ) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
RECU_GENE=OPER(nom="RECU_GENE",op=  76,sd_prod=vect_asse_gene,docu="U4.71.03-e",reentrant='n',
               fr="R�cup�ration d un champ de grandeur � partir d un r�sultat en coordonn�es g�n�ralis�es",
         RESU_GENE       =SIMP(statut='o',typ=tran_gene ),
         INST            =SIMP(statut='o',typ='R' ),
         NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL","VITE","ACCE") ),
         INTERPOL        =SIMP(statut='f',typ='TXM',defaut="NON",into=("NON","LIN") ),
         CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF" ,into=("ABSOLU","RELATIF") ),
         PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
)  ;
#& MODIF COMMANDE  DATE 19/12/2001   AUTEUR PBBHHPB P.BADEL 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
RECU_TABLE=OPER(nom="RECU_TABLE",op= 174,sd_prod=table,
                fr=" ",docu="U4.71.02-a1",reentrant='n',
         CO              =SIMP(statut='o',typ=assd),
         regles=(PRESENT_ABSENT('NOM_TABLE','NOM_PARA')),
         NOM_TABLE       =SIMP(statut='f',typ='TXM' ),
         NOM_PARA        =SIMP(statut='f',typ='TXM' ),  
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def reso_grad_prod(MATR_ASSE,**args ):
  if AsType(MATR_ASSE) == matr_asse_depl_r : return cham_no_depl_r
  if AsType(MATR_ASSE) == matr_asse_temp_r : return cham_no_temp_r
  if AsType(MATR_ASSE) == matr_asse_pres_r : return cham_no_pres_r
  raise AsException("type de concept resultat non prevu")

RESO_GRAD=OPER(nom="RESO_GRAD",op=  84,sd_prod=reso_grad_prod,
               fr="R�solution par la m�thode du gradient conjugu� pr�conditionn�",
               docu="U4.55.04-e",reentrant='f',
         MATR_ASSE       =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_temp_r,matr_asse_pres_r ) ),
         CHAM_NO         =SIMP(statut='o',typ=(cham_no_depl_r,cham_no_temp_r,cham_no_pres_r ) ),
         CHAM_CINE       =SIMP(statut='f',typ=(cham_no_temp_r,cham_no_depl_r,cham_no_pres_r ) ),
         MATR_FACT       =SIMP(statut='f',typ=(matr_asse_depl_r,matr_asse_temp_r,matr_asse_pres_r ) ),
         NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),  
         REPRISE         =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1E-6 ),  
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
def reso_ldlt_prod(CHAM_NO,**args ):
  if AsType(CHAM_NO) == cham_no_temp_r : return cham_no_temp_r
  if AsType(CHAM_NO) == cham_no_depl_r : return cham_no_depl_r
  if AsType(CHAM_NO) == cham_no_pres_r : return cham_no_pres_r
  if AsType(CHAM_NO) == cham_no_temp_c : return cham_no_temp_c
  if AsType(CHAM_NO) == cham_no_depl_c : return cham_no_depl_c
  if AsType(CHAM_NO) == cham_no_pres_c : return cham_no_pres_c
  raise AsException("type de concept resultat non prevu")

RESO_LDLT=OPER(nom="RESO_LDLT",op=15,sd_prod=reso_ldlt_prod,reentrant='f',
               fr="R�solution en place ou hors place d un syst�me factoris�",docu="U4.55.02-f",
         MATR_FACT       =SIMP(statut='o',typ=(matr_asse_depl_r,matr_asse_depl_c,matr_asse_temp_r,
                                               matr_asse_temp_c,matr_asse_pres_r,matr_asse_pres_c) ),
         CHAM_NO         =SIMP(statut='o',typ=(cham_no_temp_r,cham_no_depl_r,cham_no_pres_r,
                                               cham_no_temp_c,cham_no_depl_c,cham_no_pres_c) ),
         CHAM_CINE       =SIMP(statut='f',typ=(cham_no_temp_r,cham_no_depl_r,cham_no_pres_c) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
def rest_base_phys_prod(RESU_GENE,RESULTAT,**args ):
  if AsType(RESU_GENE) == tran_gene : return dyna_trans
  if AsType(RESU_GENE) == mode_gene : return mode_meca
  if AsType(RESU_GENE) == mode_cycl : return mode_meca
  if AsType(RESU_GENE) == harm_gene : return dyna_harmo
  if AsType(RESULTAT)  == mode_meca : return mode_meca
  raise AsException("type de concept resultat non prevu")

REST_BASE_PHYS=OPER(nom="REST_BASE_PHYS",op=  75,sd_prod=rest_base_phys_prod,
                    fr="Restituer dans la base physique des r�sultats en coordonn�es g�n�ralis�es",
                    docu="U4.63.21-e",reentrant='n',
        regles=(UN_PARMI('RESU_GENE','RESULTAT'),
                EXCLUS('TOUT_ORDRE','NUME_ORDRE','INST','LIST_INST','TOUT_INST'),
                EXCLUS('TOUT_INST','NUME_ORDRE','INST','LIST_INST','TOUT_ORDRE'),
#  Doc U � revoir
                PRESENT_ABSENT('MULT_APPUI','CORR_STAT'),
                EXCLUS('MULT_APPUI','NOEUD','GROUP_NO'),
                EXCLUS('CORR_STAT','NOEUD','GROUP_NO'),             
                EXCLUS('NOEUD','GROUP_NO'), 
                PRESENT_PRESENT('RESULTAT','SQUELETTE'),
                PRESENT_PRESENT('ACCE_MONO_APPUI','DIRECTION'),),
         RESU_GENE       =SIMP(statut='f',typ=(tran_gene,mode_gene,mode_cycl,harm_gene ) ),
         RESULTAT        =SIMP(statut='f',typ=mode_meca ),
         
         MODE_MECA       =SIMP(statut='f',typ=mode_meca ),
         TOUT_ORDRE      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**' ),  
         TOUT_INST       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         INST            =SIMP(statut='f',typ='R',max='**' ),  
         LIST_INST       =SIMP(statut='f',typ=listr8 ),
         FREQ            =SIMP(statut='f',typ='R',max='**' ),  
         LIST_FREQ       =SIMP(statut='f',typ=listr8 ),
         b_prec_crit     =BLOC(condition = "INST != None or LIST_INST != None or FREQ != None or LIST_FREQ != None",
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("ABSOLU","RELATIF") ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),  
         ),
         INTERPOL        =SIMP(statut='f',typ='TXM',defaut="NON",into=("NON","LIN") ),
         
         MULT_APPUI      =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         CORR_STAT       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         NOM_CHAM        =SIMP(statut='f',typ='TXM',max=8,defaut="ACCE",   
                               into=("DEPL","VITE","ACCE","ACCE_ABSOLU","EFGE_ELNO_DEPL","SIPO_ELNO_DEPL",                 
                                     "SIGM_ELNO_DEPL","FORC_NODA",) ),
         TOUT_CHAM       =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
         NOEUD           =SIMP(statut='f',typ=no,max='**'),
 
         ACCE_MONO_APPUI =SIMP(statut='f',typ=fonction),
         DIRECTION       =SIMP(statut='f',typ='R',max='**' ),

         SQUELETTE       =SIMP(statut='f',typ=squelette ),
         SOUS_STRUC      =SIMP(statut='f',typ='TXM' ),  
         SECTEUR         =SIMP(statut='f',typ='I',defaut= 1 ),  
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 28/03/2001   AUTEUR CIBHHLV L.VIVAN 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
REST_SPEC_PHYS=OPER(nom="REST_SPEC_PHYS",op= 148,sd_prod=tabl_intsp,
                    docu="U4.63.22-c",reentrant='n',
         regles=(AU_MOINS_UN('BASE_ELAS_FLUI','MODE_MECA'),),
         BASE_ELAS_FLUI  =SIMP(statut='f',typ=melasflu ),
         MODE_MECA       =SIMP(statut='f',typ=mode_meca ),
         BANDE           =SIMP(statut='f',typ='R',min=02,max=02 ),  
         NUME_ORDRE      =SIMP(statut='f',typ='I',max='**' ),  
         INTE_SPEC_GENE  =SIMP(statut='o',typ=tabl_intsp ),
         NOEUD           =SIMP(statut='o',typ=no,max='**'),
         NOM_CMP         =SIMP(statut='o',typ='TXM',max='**' ),  
         MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         NOM_CHAM        =SIMP(statut='o',typ='TXM',max=07,    
                               into=("DEPL","VITE","ACCE","EFGE_ELNO_DEPL",      
                                     "SIPO_ELNO_DEPL","SIGM_ELNO_DEPL","FORC_NODA") ),
         MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc), ),
         EXCIT           =FACT(statut='f',max=01,
           NOEUD           =SIMP(statut='o',typ=no,max='**'),
           NOM_CMP         =SIMP(statut='o',typ='TXM',max='**' ),  
         ),
         MOUVEMENT       =SIMP(statut='f',typ='TXM',defaut="ABSOLU",into=("RELATIF","ABSOLU","DIFFERENTIEL") ),
         OPTION          =SIMP(statut='f',typ='TXM',defaut="DIAG_DIAG",    
                               into=("DIAG_TOUT","DIAG_DIAG","TOUT_TOUT","TOUT_DIAG") ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),  
)  ;
#& MODIF COMMANDE  DATE 21/12/2000   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
RETOUR=PROC(nom="RETOUR",op= -2,docu="U4.13.02-e",
            fr="Retour au fichier de commandes appelant", 
) ;
#& MODIF COMMANDE  DATE 30/01/2002   AUTEUR VABHHTS J.TESELET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
#  RESPONSABLE ADBHHVV V.CANO
STAT_NON_LINE=OPER(nom="STAT_NON_LINE",op=70,sd_prod=evol_noli,
                   fr="Analyse m�canique statique non lin�aire",
                   docu="U4.51.03-e1",reentrant='f',
         regles=(AU_MOINS_UN('COMP_INCR','COMP_ELAS'),),
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),
         EXCIT           =FACT(statut='o',min=1,max='**',
           CHARGE          =SIMP(statut='o',typ=char_meca),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
           TYPE_CHARGE     =SIMP(statut='f',typ='TXM',defaut="FIXE_CSTE",
                                 into=("FIXE_CSTE","FIXE_PILO","SUIV","DIDI")),
         ),
         VARI_COMM           =FACT(statut='f',
           regles=(AU_MOINS_UN('SECH','IRRA','HYDR'),),
           IRRA     =SIMP(statut='f',typ=evol_varc),
           SECH     =SIMP(statut='f',typ=evol_ther),
           HYDR     =SIMP(statut='f',typ=evol_ther),
         ),
         COMP_INCR       =FACT(statut='f',min=1,max='**',
           RELATION        =SIMP(statut='o',typ='TXM',defaut="VMIS_ISOT_TRAC",
                                 into=( "ELAS",
                                        "VMIS_ISOT_TRAC",
                                        "VMIS_ISOT_LINE",
                                        "VMIS_ECMI_TRAC",
                                        "VMIS_ECMI_LINE",
                                        "LABORD_1D",
                                        "ENDO_LOCAL",
                                        "ENDO_FRAGILE",
                                        "BETON_ENDO_LOCAL",
                                        "RUPT_FRAG",
                                        "PLAS_GRAD_LINE",
                                        "PLAS_GRAD_TRAC",
                                        "DURC_GRAD",
                                        "META_P_IL",
                                        "META_P_IL_PT",
                                        "META_P_IL_RE",
                                        "META_P_IL_PT_RE",
                                        "META_V_IL",
                                        "META_V_IL_PT",
                                        "META_V_IL_RE",
                                        "META_V_IL_PT_RE",
                                        "META_P_INL",
                                        "META_P_INL_PT",
                                        "META_P_INL_RE",
                                        "META_P_INL_PT_RE",
                                        "META_V_INL",
                                        "META_V_INL_PT",
                                        "META_V_INL_RE",
                                        "META_V_INL_PT_RE",
                                        "META_P_CL",
                                        "META_P_CL_PT",
                                        "META_P_CL_RE",
                                        "META_P_CL_PT_RE",
                                        "META_V_CL",
                                        "META_V_CL_PT",
                                        "META_V_CL_RE",
                                        "META_V_CL_PT_RE",
                                        "VMIS_CINE_LINE",
                                        "VISC_TAHERI",
                                        "CHABOCHE",
                                        "VISCOCHAB",
                                        "VMIS_CIN1_CHAB",
                                        "VMIS_CIN2_CHAB",
                                        "POLY_CFC",
                                        "LMARC",
                                        "ROUSSELIER",
                                        "ROUSS_PR",
                                        "ROUSS_VISC",
                                        "VMIS_POU_LINE",
                                        "VMIS_POU_FLEJOU",
                                        "COULOMB",
                                        "ARME",
                                        "ASSE_CORN",
                                        "NORTON_HOFF",
                                        "LEMAITRE",
                                        "ZIRC_CYRA2",
                                        "ZIRC_EPRI",
                                        "ASSE_COMBU",
                                        "VENDOCHAB",
                                        "NADAI_B",
                                        "DIS_CONTACT",
                                        "DIS_CHOC",
                                        "DIS_GOUJ2E_PLAS",
                                        "DIS_GOUJ2E_ELAS",
                                        "GRILLE_ISOT_LINE",
                                        "GRILLE_CINE_LINE",
                                        "GRILLE_PINTO_MEN",
                                        "PINTO_MENEGOTTO",
                                        "CJS",
                                        "OHNO",
                                        "GRANGER_FP",
                                        "GRANGER_FP_V",
                                        "BETON_DOUBLE_DP",
                                        "KIT_HM",
                                        "KIT_HHM",
                                        "KIT_THH",
                                        "KIT_THM",
                                        "KIT_THHM",
                                        "VMIS_ASYM_LINE",
                                        "ELAS_THM",
                                        "SURF_ETAT_NSAT",
                                        "SURF_ETAT_SATU",
                                        "CAM_CLAY_THM",
                                        "KIT_DDI",
                                     ) ),
           ELAS            =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           VMIS_ISOT_TRAC  =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           VMIS_ISOT_LINE  =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           VMIS_ECMI_TRAC  =SIMP(statut='c',typ='I',defaut=8,into=(8,)),
           VMIS_ECMI_LINE  =SIMP(statut='c',typ='I',defaut=8,into=(8,)),
           LABORD_1D   =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           ENDO_LOCAL      =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           ENDO_FRAGILE    =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           BETON_ENDO_LOCAL=SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           RUPT_FRAG       =SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           PLAS_GRAD_LINE  =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           PLAS_GRAD_TRAC  =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           DURC_GRAD       =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           META_P_IL         =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_IL_PT       =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_IL_RE       =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_IL_PT_RE    =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_IL          =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_IL_PT       =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_IL_RE       =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_IL_PT_RE    =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_INL         =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_INL_PT      =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_INL_RE      =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_INL_PT_RE   =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_INL         =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_INL_PT      =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_INL_RE      =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_V_INL_PT_RE   =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
          META_P_CL          =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_P_CL_PT       =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_P_CL_RE       =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_P_CL_PT_RE    =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_V_CL          =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_V_CL_PT       =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_V_CL_RE       =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
          META_V_CL_PT_RE    =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
           VMIS_CINE_LINE  =SIMP(statut='c',typ='I',defaut=7,into=(7,)),
           CHABOCHE        =SIMP(statut='c',typ='I',defaut=14,into=(14,)),
           VISCOCHAB       =SIMP(statut='c',typ='I',defaut=28,into=(28,)),
           VMIS_CIN1_CHAB  =SIMP(statut='c',typ='I',defaut=8,into=(8,)),
           VMIS_CIN2_CHAB  =SIMP(statut='c',typ='I',defaut=14,into=(14,)),
           POLY_CFC        =SIMP(statut='c',typ='I',defaut=1688,into=(1688,)),
           LMARC           =SIMP(statut='c',typ='I',defaut=20,into=(20,)),
           VISC_TAHERI     =SIMP(statut='c',typ='I',defaut=9,into=(9,)),
           ROUSSELIER      =SIMP(statut='c',typ='I',defaut=9,into=(9,)),
           ROUSS_PR        =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           ROUSS_VISC      =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           VMIS_POU_LINE   =SIMP(statut='c',typ='I',defaut=9,into=(9,)),
           VMIS_POU_FLEJOU =SIMP(statut='c',typ='I',defaut=9 ,into=(9,)),
           COULOMB         =SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           ASSE_CORN       =SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           ARME            =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           NORTON_HOFF     =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           LEMAITRE        =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           ZIRC_CYRA2      =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           ZIRC_EPRI       =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           ASSE_COMBU      =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           NADAI_B         =SIMP(statut='c',typ='I',defaut=34,into=(34,)),
           VENDOCHAB       =SIMP(statut='c',typ='I',defaut=10,into=(10,)),
           GRILLE_ISOT_LINE=SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           GRILLE_CINE_LINE=SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           GRILLE_PINTO_MEN=SIMP(statut='c',typ='I',defaut=16,into=(16,)),
           DIS_CONTACT     =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
           DIS_CHOC        =SIMP(statut='c',typ='I',defaut=7,into=(7,)),
           DIS_GOUJ2E_PLAS =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           DIS_GOUJ2E_ELAS =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           PINTO_MENEGOTTO =SIMP(statut='c',typ='I',defaut=8,into=(8,)),
           CJS             =SIMP(statut='c',typ='I',defaut=16,into=(16,)),
           OHNO            =SIMP(statut='c',typ='I',defaut=32,into=(32,)),
           GRANGER_FP      =SIMP(statut='c',typ='I',defaut=55,into=(55,)),
           GRANGER_FP_V    =SIMP(statut='c',typ='I',defaut=55,into=(55,)),
           BETON_DOUBLE_DP =SIMP(statut='c',typ='I',defaut=4,into=(4,)),
           KIT_HM          =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           KIT_HHM         =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           KIT_THH         =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           KIT_THM         =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           KIT_THHM        =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           VMIS_ASYM_LINE  =SIMP(statut='c',typ='I',defaut=4,into=(4,)),

           RELATION_KIT    =SIMP(statut='f',typ='TXM',max='**',
                                 into=(
# MECA
                                       "ELAS",
                                       "CJS",
                                       "ELAS_THM",
                                       "SURF_ETAT_NSAT",
                                       "SURF_ETAT_SATU",
                                       "CAM_CLAY_THM",
# THMC
                                       "GAZ",
                                       "LIQU_SATU",
                                       "LIQU_SATU_GAT",
                                       "LIQU_GAZ_ATM",
                                       "LIQU_VAPE_GAZ",
                                       "LIQU_NSAT_GAT",
                                       "LIQU_GAZ",
# THER
                                       "THER_HOMO",
                                       "THER_POLY",
# HYDR
                                       "HYDR_UTIL",
                                       "HYDR",
# MECA_META
                                       "ACIER",
                                       "ZIRC",
# MECA KIT_DDI
                                       "VMIS_ISOT_TRAC",
                                       "VMIS_ISOT_LINE",
                                       "VMIS_ISOT_CINE",
                                       "GRANGER_FP",
                                       "GRANGER_FP_V",
                                       "ROUSSELIER",
                                       "CHABOCHE",
                                       "OHNO",
                                       "NADAI_B",
                                       "BETON_DOUBLE_DP",
                                       ) ),
           ELAS_THM        =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           SURF_ETAT_NSAT  =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           SURF_ETAT_SATU  =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           CAM_CLAY_THM    =SIMP(statut='c',typ='I',defaut=6,into=(6,)),
           GAZ             =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           LIQU_SATU       =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           LIQU_SATU_GAT   =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           LIQU_GAZ_ATM    =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           LIQU_VAPE_GAZ   =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           LIQU_NSAT_GAT   =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           LIQU_GAZ        =SIMP(statut='c',typ='I',defaut=2,into=(2,)),
           THER_HOMO       =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           THER_POLY       =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           HYDR_UTIL       =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           HYDR            =SIMP(statut='c',typ='I',defaut=0,into=(0,)),
           ACIER           =SIMP(statut='c',typ='I',defaut=5,into=(5,)),
           ZIRC            =SIMP(statut='c',typ='I',defaut=3,into=(3,)),

           DEFORMATION     =SIMP(statut='f',typ='TXM',defaut="PETIT",into=("PETIT","PETIT_REAC","SIMO_MIEHE","GREEN_GR","GREEN",)),
           ALGO_C_PLAN     =SIMP(statut='f',typ='TXM',defaut="ANALYTIQUE",into=("DEBORST","ANALYTIQUE",)),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         ),
         COMP_ELAS       =FACT(statut='f',min=1,max='**',
           RELATION        =SIMP(statut='o',typ='TXM',defaut="ELAS",
                                 into=("ELAS","ELAS_VMIS_LINE","ELAS_VMIS_TRAC",
                                       "ELAS_POUTRE_GR","CABLE")),
           ELAS            =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           ELAS_VMIS_TRAC  =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           ELAS_VMIS_LINE  =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           ELAS_POUTRE_GR  =SIMP(statut='c',typ='I',defaut=3,into=(3,)),
           CABLE           =SIMP(statut='c',typ='I',defaut=1,into=(1,)),
           DEFORMATION     =SIMP(statut='f',typ='TXM',defaut="PETIT" ,into=("PETIT","GREEN","GREEN_GR",) ),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         ),
         ETAT_INIT       =FACT(statut='f',min=1,max=1,
           regles=(AU_MOINS_UN('EVOL_NOLI','DEPL','SIGM','VARI','VARI_NON_LOCAL',),
                   EXCLUS('EVOL_NOLI','DEPL',),
                   EXCLUS('EVOL_NOLI','SIGM',),
                   EXCLUS('EVOL_NOLI','VARI',),
                   EXCLUS('EVOL_NOLI','VARI_NON_LOCAL',),
                   EXCLUS('NUME_ORDRE','INST'), ),
           DEPL            =SIMP(statut='f',typ=cham_no_depl_r),
           SIGM            =SIMP(statut='f',typ=(cham_elem_sief_r,carte_sief_r)),
           VARI            =SIMP(statut='f',typ=cham_elem_vari_r),
           VARI_NON_LOCAL  =SIMP(statut='f',typ=cham_no_vanl_r),
           EVOL_NOLI       =SIMP(statut='f',typ=evol_noli),
           NUME_ORDRE      =SIMP(statut='f',typ='I'),
           INST            =SIMP(statut='f',typ='R'),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           NUME_DIDI       =SIMP(statut='f',typ='I'),
           INST_ETAT_INIT  =SIMP(statut='f',typ='R'),
         ),
         INCREMENT       =FACT(statut='o',min=1,max=1,
           regles=(EXCLUS('NUME_INST_INIT','INST_INIT'),
                   EXCLUS('NUME_INST_FIN','INST_FIN'),),
           LIST_INST       =SIMP(statut='o',typ=listr8),
           EVOLUTION       =SIMP(statut='f',typ='TXM',defaut="CHRONOLOGIQUE",
                                 into=("CHRONOLOGIQUE","RETROGRADE","SANS",) ),
           NUME_INST_INIT  =SIMP(statut='f',typ='I'),
           INST_INIT       =SIMP(statut='f',typ='R'),
           NUME_INST_FIN   =SIMP(statut='f',typ='I'),
           INST_FIN        =SIMP(statut='f',typ='R'),
           PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3 ),
           SUBD_PAS        =SIMP(statut='f',typ='I',defaut=1),
           SUBD_PAS_MINI   =SIMP(statut='f',typ='R'),
           COEF_SUBD_PAS_1 =SIMP(statut='f',typ='R',defaut= 1.0E+0),
         ),
         NEWTON          =FACT(statut='d',min=1,max=1,
           REAC_INCR       =SIMP(statut='f',typ='I',defaut= 1 ),
           PREDICTION      =SIMP(statut='f',typ='TXM',into=("DEPL_CALCULE","TANGENTE","ELASTIQUE","EXTRAPOL") ),
           MATRICE         =SIMP(statut='f',typ='TXM',defaut="TANGENTE",into=("TANGENTE","ELASTIQUE") ),
           PAS_MINI_ELAS   =SIMP(statut='f',typ='R',defaut=0.0E+0),
           REAC_ITER       =SIMP(statut='f',typ='I',defaut=0),
           EVOL_NOLI       =SIMP(statut='f',typ=evol_noli),
         ),
         RECH_LINEAIRE   =FACT(statut='f',min=1,max=1,
           RESI_LINE_RELA  =SIMP(statut='f',typ='R',defaut= 1.0E-1 ),
           ITER_LINE_MAXI  =SIMP(statut='f',typ='I',defaut= 3),
         ),
         PILOTAGE        =FACT(statut='f',min=1,max=1,
           regles=(EXCLUS('NOEUD','GROUP_NO'),PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TYPE    =SIMP(statut='o',typ='TXM',into=("DDL_IMPO","LONG_ARC","PRED_ELAS","PRED_ELAS_INCR","DEFORMATION","ANA_LIM") ),
           COEF_MULT       =SIMP(statut='f',typ='R',defaut= 1.0E+0),
           ETA_PILO_MAX    =SIMP(statut='f',typ='R'),
           ETA_PILO_MIN    =SIMP(statut='f',typ='R'),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOM_CMP         =SIMP(statut='f',typ='TXM',max='**' ),
                         ),
         CONVERGENCE     =FACT(statut='d',min=1,max=1,
           RESI_GLOB_MAXI  =SIMP(statut='f',typ='R'),
           RESI_GLOB_RELA  =SIMP(statut='f',typ='R'),
           ITER_GLOB_MAXI  =SIMP(statut='f',typ='I',defaut=10),
           ITER_GLOB_ELAS  =SIMP(statut='f',typ='I',defaut=25),
           ARRET           =SIMP(statut='f',typ='TXM',defaut="OUI"),
           RESI_INTE_RELA  =SIMP(statut='f',typ='R'
                                ,defaut= 1.0E-6),
           ITER_INTE_MAXI  =SIMP(statut='f',typ='I',defaut= 10 ),
           ITER_INTE_PAS   =SIMP(statut='f',typ='I',defaut= 0 ),
           TYPE_MATR_COMP  =SIMP(statut='f',typ='TXM',defaut="TANG_VIT",into=("TANG_VIT",)),
           RESO_INTE       =SIMP(statut='f',typ='TXM',defaut="IMPLICITE",
                                 into=("RUNGE_KUTTA_2","RUNGE_KUTTA_4","IMPLICITE")),
         ),
         PARM_THETA      =SIMP(statut='f',typ='R'
                              ,defaut= 1. ),
         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt         =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
           ),
           b_ldlt_mult    =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non inversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON","DECOUPE") ),
           ),
           b_gcpc         =BLOC(condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
#  A quoi sert eps
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           SYME            =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         ),
         ARCHIVAGE       =FACT(statut='f',min=1,max=1,
           regles=(EXCLUS('PAS_ARCH','LIST_INST','INST'),
                   EXCLUS('ARCH_ETAT_INIT','NUME_INIT'), ),
           LIST_INST       =SIMP(statut='f',typ=(listr8) ),
           INST            =SIMP(statut='f',typ='R',max='**' ),
           PAS_ARCH        =SIMP(statut='f',typ='I' ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3),
           ARCH_ETAT_INIT  =SIMP(statut='f',typ='TXM',into=("OUI",)),
           NUME_INIT       =SIMP(statut='f',typ='I'),
           DETR_NUME_SUIV  =SIMP(statut='f',typ='TXM',into=("OUI",)),
           CHAM_EXCLU      =SIMP(statut='f',typ='TXM',max='**',into=("DEPL","SIEF_ELGA","VARI_ELGA",
                                                                     "VARI_NON_LOCAL","LANL_ELGA")),
         ),
         OBSERVATION     =FACT(statut='f',min=1,max='**',
           regles=(UN_PARMI('NOEUD','GROUP_NO','MAILLE'),
                   PRESENT_PRESENT('MAILLE','POINT'),),
           NOM_CHAM        =SIMP(statut='o',typ='TXM',max='**',into=("DEPL","VITE","ACCE","SIEF_ELGA",
                                              "VARI_ELGA","DEPL_ABSOLU","VITE_ABSOLU","ACCE_ABSOLU")),
           NOM_CMP         =SIMP(statut='o',typ='TXM',max='**' ),
           LIST_ARCH       =SIMP(statut='f',typ=listis),
           LIST_INST       =SIMP(statut='f',typ=listr8),
           INST            =SIMP(statut='f',typ='R',max='**' ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           PAS_OBSE        =SIMP(statut='f',typ='I'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           POINT           =SIMP(statut='f',typ='I',max='**'),
         ),
         MODELE_NON_LOCAL=SIMP(statut='f',typ=modele ),
         b_non_local = BLOC ( condition = "MODELE_NON_LOCAL != None",
                              fr="Donn�es sp�cifiques au mod�le non local",
           SOLV_NON_LOCAL  =FACT(statut='f',min=1,max=1,
             METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
             b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
               RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
             ),
             b_ldlt         =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
               RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
             ),
             b_ldlt_mult    =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                    fr="Param�tres relatifs � la non inversibilit� de la matrice � factorise",
               NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
               STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
             ),
             b_gcpc         =BLOC(condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
               PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
               NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
               RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
               NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
             ),
             EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           ),
           LAGR_NON_LOCAL  =FACT(statut='f',max=1,
             ITER_DUAL_MAXI  =SIMP(statut='f',typ='I',defaut= 50),
             RESI_DUAL_ABSO  =SIMP(statut='o',typ='R'),
             RESI_PRIM_ABSO  =SIMP(statut='o',typ='R'),
             RHO             =SIMP(statut='f',typ='R',defaut= 1000.),
             ITER_PRIM_MAXI  =SIMP(statut='f',typ='I',defaut= 10),
           ),
         ),
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),
 )  ;
#& MODIF COMMANDE  DATE 16/01/2002   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE MCOURTOI M.COURTOIS
TEST_FONCTION=PROC(nom="TEST_FONCTION",op= 135,fr="Extraction d une valeur num�rique ou d un attribut de fonction",
                   docu="U4.92.02-e1",
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT"),
         TEST_NOOK       =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         VALEUR          =FACT(statut='f',min=01,max='**',
                               fr="Tester la valeur d une fonction ou d une nappe",
           regles=(UN_PARMI('VALE_REFE','VALE_REFE_C', ),),
           FONCTION        =SIMP(statut='o',typ=fonction ),
           NOM_PARA        =SIMP(statut='f',typ='TXM',max=2),
           VALE_PARA       =SIMP(statut='o',typ='R',max=2),
           VALE_REFE       =SIMP(statut='f',typ='R' ),
           VALE_REFE_C     =SIMP(statut='f',typ='C' ),
           CRITERE         =SIMP(statut='f',typ='TXM',fr="Crit�re de comparaison avec la solution de r�f�rence",
                                 defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           PRECISION       =SIMP(statut='f',typ='R',fr="Ecart maximal autoris� avec la solution de r�f�rence",
                                 defaut= 1.E-3 ),
           REFERENCE       =SIMP(statut='f',typ='TXM',
                                 into=("ANALYTIQUE","SOURCE_EXTERNE","NON_REGRESSION","AUTRE_ASTER") ),
           b_version = BLOC (condition = "REFERENCE == 'NON_REGRESSION'", 
             VERSION         =SIMP(statut='f',typ='TXM' ),
           ),
         ),
         ATTRIBUT        =FACT(statut='f',min=01,max='**',
                               fr="Tester la valeur d un attribut d une fonction ou d''une nappe",
           FONCTION        =SIMP(statut='o',typ=fonction ),
           PARA            =SIMP(statut='f',typ='R' ),
           CRIT_PARA       =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           PREC_PARA       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           ATTR            =SIMP(statut='o',typ='TXM',
                                 into=("NOM_PARA","NOM_RESU","PROL_DROITE","PROL_GAUCHE","INTERPOL",
                                       "PROL_GAUCHE_FONC","PROL_DROITE_FONC","INTERPOL_FONC","NOM_PARA_FONC") ),
           ATTR_REFE       =SIMP(statut='o',typ='TXM' ),
           REFERENCE       =SIMP(statut='f',typ='TXM',
                                 into=("ANALYTIQUE","SOURCE_EXTERNE","NON_REGRESSION","AUTRE_ASTER") ),
           b_version       =BLOC(condition = "REFERENCE == 'NON_REGRESSION'", 
             VERSION         =SIMP(statut='f',typ='TXM' ),
           ),
         ),
         TABL_INTSP      =FACT(statut='f',min=01,max='**',
                               fr="Tester la valeur d une fonction contenue dans une table interspectrale",
           regles=(UN_PARMI('NUME_ORDRE_I','NOEUD_I'),),
           INTE_SPEC       =SIMP(statut='o',typ=tabl_intsp ),
           NOEUD_I         =SIMP(statut='f',typ=no),
           NUME_ORDRE_I    =SIMP(statut='f',typ='I' ),
           b_nume_ordre_i = BLOC (condition = "NUME_ORDRE_I != None", 
             NUME_ORDRE_J    =SIMP(statut='o',typ='I' ),
           ),
           b_noeud_i = BLOC (condition = "NOEUD_I != None",             
             NOEUD_J         =SIMP(statut='o',typ=no),
             NOM_CMP_I       =SIMP(statut='o',typ='TXM' ),
             NOM_CMP_J       =SIMP(statut='o',typ='TXM' ),
           ),
           NUME_VITE_FLUI  =SIMP(statut='f',typ='I' ),
           VALE_PARA       =SIMP(statut='o',typ='R' ),
           VALE_REFE_C     =SIMP(statut='o',typ='C' ),
           CRITERE         =SIMP(statut='f',typ='TXM',fr="Crit�re de comparaison avec la solution de r�f�rence",
                                 defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           PRECISION       =SIMP(statut='f',typ='R',fr="Ecart maximal autoris� avec la solution de r�f�rence",
                                 defaut= 1.E-3 ),
           REFERENCE       =SIMP(statut='f',typ='TXM',
                                 into=("ANALYTIQUE","SOURCE_EXTERNE","NON_REGRESSION","AUTRE_ASTER") ),
           b_version       =BLOC(condition = "REFERENCE == 'NON_REGRESSION'", 
             VERSION         =SIMP(statut='f',typ='TXM' ),
           ),
         ),
)  ;
#& MODIF COMMANDE  DATE 22/11/2001   AUTEUR VABHHTS J.PELLET 
# RESPONSABLE VABHHTS J.PELLET
TEST_RESU=PROC(nom="TEST_RESU",op=23,docu="U4.92.01-f1",
         fr="Extraction d une valeur et comparaison � une valeur de r�f�rence",
         regles=(AU_MOINS_UN('CHAM_NO','CHAM_ELEM','RESU','OBJET')),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT"),

         CHAM_NO         =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NOEUD','GROUP_NO','TYPE_TEST'),
                   EXCLUS('NOEUD','GROUP_NO'),
                   PRESENT_PRESENT('NOEUD','NOM_CMP'),
                   PRESENT_PRESENT( 'GROUP_NO','NOM_CMP'),
                   UN_PARMI('VALE','VALE_I','VALE_C'),),
           CHAM_GD         =SIMP(statut='o',typ=cham_no),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           NOM_CMP         =SIMP(statut='f',typ='TXM',max='**'),
           TYPE_TEST       =SIMP(statut='f',typ='TXM',into=("SOMM_ABS","SOMM","MAX","MIN")),
           VALE            =SIMP(statut='f',typ='R'),
           VALE_I          =SIMP(statut='f',typ='I'),
           VALE_C          =SIMP(statut='f',typ='C'),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU")),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3),
           REFERENCE       =SIMP(statut='f',typ='TXM',into=("ANALYTIQUE","SOURCE_EXTERNE",
                                                            "NON_REGRESSION","AUTRE_ASTER")),
           VERSION         =SIMP(statut='f',typ='TXM'),
         ),

         CHAM_ELEM       =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('MAILLE','TYPE_TEST',),
                   EXCLUS('NOEUD','GROUP_NO','POINT'),
                   PRESENT_PRESENT('NOEUD','NOM_CMP'),
                   PRESENT_PRESENT('GROUP_NO','NOM_CMP'),
                   PRESENT_PRESENT('POINT','NOM_CMP'),
                   UN_PARMI('VALE','VALE_I','VALE_C'), ),
           CHAM_GD         =SIMP(statut='o',typ=cham_elem),# CO()
           MAILLE          =SIMP(statut='f',typ=ma),# CO()
           POINT           =SIMP(statut='f',typ='I' ),
           SOUS_POINT      =SIMP(statut='f',typ='I'),
           NOEUD           =SIMP(statut='f',typ=no),# CO()
           GROUP_NO        =SIMP(statut='f',typ=grno),# CO()
           NOM_CMP         =SIMP(statut='f',typ='TXM',max='**'),
           TYPE_TEST       =SIMP(statut='f',typ='TXM',into=("SOMM_ABS","SOMM","MAX","MIN") ),
           VALE            =SIMP(statut='f',typ='R' ),
           VALE_I          =SIMP(statut='f',typ='I' ),
           VALE_C          =SIMP(statut='f',typ='C' ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU")),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
           REFERENCE       =SIMP(statut='f',typ='TXM',into=("ANALYTIQUE","SOURCE_EXTERNE",
                                                            "NON_REGRESSION","AUTRE_ASTER") ),
           VERSION         =SIMP(statut='f',typ='TXM' ),
         ),

         RESU            =FACT(statut='f',min=01,max='**',
           regles=(UN_PARMI('NUME_ORDRE','INST','FREQ','NUME_MODE','NOEUD_CMP','NOM_CAS','ANGL'),
                   UN_PARMI('NOM_CHAM','PARA'),
                   PRESENT_ABSENT('PARA','NOEUD','GROUP_NO','POINT','NOM_CMP','TYPE_TEST'),
                   PRESENT_PRESENT('NOM_CMP','NOM_CHAM'),
                   EXCLUS('NOEUD','GROUP_NO','POINT','TYPE_TEST'),
                   PRESENT_PRESENT('NOEUD','NOM_CMP'),
                   PRESENT_PRESENT('GROUP_NO','NOM_CMP'),
                   PRESENT_PRESENT('POINT','NOM_CMP'),
                   UN_PARMI('VALE','VALE_I','VALE_C') ,),
           RESULTAT        =SIMP(statut='o',typ=resultat),
           SENSIBILITE     =SIMP(statut='f',typ=(para_sensi,theta_geom),max='**',
                                 fr="Liste des param�tres de sensibilit�.",
                                 ang="List of sensitivity parameters"),
           NUME_ORDRE      =SIMP(statut='f',typ='I'),
           INST            =SIMP(statut='f',typ='R'),
           FREQ            =SIMP(statut='f',typ='R'),
           NUME_MODE       =SIMP(statut='f',typ='I'),
           NOEUD_CMP       =SIMP(statut='f',typ='TXM',max='**' ),
           NOM_CAS         =SIMP(statut='f',typ='TXM'),
           ANGL            =SIMP(statut='f',typ='R'),
           PARA            =SIMP(statut='f',typ='TXM'),
           NOM_CHAM        =SIMP(statut='f',typ='TXM'),
           NOM_CMP         =SIMP(statut='f',typ='TXM',max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
           POINT           =SIMP(statut='f',typ='I'),
           SOUS_POINT      =SIMP(statut='f',typ='I'),
           TYPE_TEST       =SIMP(statut='f',typ='TXM',into=("SOMM_ABS","SOMM","MAX","MIN")),
           VALE            =SIMP(statut='f',typ='R'),
           VALE_I          =SIMP(statut='f',typ='I'),
           VALE_C          =SIMP(statut='f',typ='C'),
           CRITERE         =SIMP(statut='f',typ='TXM',into=("RELATIF","ABSOLU"),max=02),
           PRECISION       =SIMP(statut='f',typ='R',max=02),
           REFERENCE       =SIMP(statut='f',typ='TXM',into=("ANALYTIQUE","SOURCE_EXTERNE",
                                                            "NON_REGRESSION","AUTRE_ASTER",) ),
           VERSION         =SIMP(statut='f',typ='TXM' ),
         ),

         OBJET           =FACT(statut='f',max='**',
           regles=(UN_PARMI('INDICE','S_I','S_R','RESUME',),
                 UN_PARMI('VALE','VALE_I','VALE_C','RESUME','S_R','S_I'),),
           NOM             =SIMP(statut='o',typ='TXM'),
           INDICE          =SIMP(statut='f',typ='I'),
           NUM_OBJ         =SIMP(statut='f',typ='I'),
           S_R             =SIMP(statut='f',typ='R'),
           S_I             =SIMP(statut='f',typ='I'),
           RESUME          =SIMP(statut='f',typ='I'),
           VALE            =SIMP(statut='f',typ='R'),
           VALE_I          =SIMP(statut='f',typ='I'),
           VALE_C          =SIMP(statut='f',typ='C'),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU")),
           PRECISION       =SIMP(statut='f',typ='R',defaut=1.0E-3 ),
           REFERENCE       =SIMP(statut='f',typ='TXM',into=("ANALYTIQUE","SOURCE_EXTERNE",
                                                            "NON_REGRESSION","AUTRE_ASTER",) ),
           VERSION         =SIMP(statut='f',typ='TXM' ),
         ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
# RESPONSABLE VABHHTS J.PELLET
TEST_TABLE=PROC(nom="TEST_TABLE",op= 177,
                docu="U4.92.03-b1",
         regles=(UN_PARMI('VALE','VALE_I','VALE_C', ),),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="RESULTAT"),
#  concept table � cr�er
         TABLE           =SIMP(statut='o',typ=table),

         FILTRE          =FACT(statut='f',min=1,max='**',
           NOM_PARA        =SIMP(statut='o',typ='TXM' ),
           CRIT_COMP       =SIMP(statut='f',typ='TXM',defaut="EQ",
                                 into=("EQ","LT","GT","NE","LE","GE","VIDE",
                                       "NON_VIDE","MAXI","ABS_MAXI","MINI","ABS_MINI") ),
           b_vale          =BLOC(condition = "(CRIT_COMP in ('EQ','NE','GT','LT','GE','LE'))",
              regles=(UN_PARMI('VALE','VALE_I','VALE_K','VALE_C',),),
              VALE            =SIMP(statut='f',typ='R' ),
              VALE_I          =SIMP(statut='f',typ='I' ),
              VALE_C          =SIMP(statut='f',typ='C' ),
              VALE_K          =SIMP(statut='f',typ='TXM' ),),

           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
         ),
         TYPE_TEST       =SIMP(statut='f',typ='TXM',into=("SOMM_ABS","SOMM","MAX","MIN") ),
         NOM_PARA        =SIMP(statut='o',typ='TXM' ),
         VALE            =SIMP(statut='f',typ='R' ),
         VALE_I          =SIMP(statut='f',typ='I' ),
         VALE_C          =SIMP(statut='f',typ='C' ),
         CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU") ),
         PRECISION       =SIMP(statut='f',typ='R',defaut= 1.2E-3 ),
         REFERENCE       =SIMP(statut='f',typ='TXM',
                               into=("ANALYTIQUE","SOURCE_EXTERNE","NON_REGRESSION","AUTRE_ASTER") ),
         b_version       =BLOC(condition = "REFERENCE == 'NON_REGRESSION'",
             VERSION         =SIMP(statut='f',typ='TXM' ),
         ),
)  ;
#& MODIF COMMANDE  DATE 04/12/2001   AUTEUR GNICOLAS G.NICOLAS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
THER_LINEAIRE=OPER(nom="THER_LINEAIRE",op=25,sd_prod=evol_ther,docu="U4.54.01-f1",reentrant='f',
                   fr="Analyse thermique lin�aire stationnaire ou transitoire",
         MODELE          =SIMP(statut='o',typ=modele),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater),
         CARA_ELEM       =SIMP(statut='f',typ=cara_elem),
         EXCIT           =FACT(statut='o',min=1,max='**',
           CHARGE          =SIMP(statut='o',typ=(char_ther,char_cine_ther)),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
         ),
         INCREMENT       =FACT(statut='f',min=1,max=1,
           LIST_INST       =SIMP(statut='o',typ=listr8 ),
           NUME_INIT       =SIMP(statut='f',typ='I'),
           NUME_FIN        =SIMP(statut='f',typ='I'),
         ),
         TEMP_INIT       =FACT(statut='f',min=1,max=1,
           regles=(EXCLUS('STATIONNAIRE','EVOL_THER','CHAM_NO','VALE'),),
           STATIONNAIRE    =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           EVOL_THER       =SIMP(statut='f',typ=evol_ther),
           CHAM_NO         =SIMP(statut='f',typ=cham_no_temp_r),
           VALE            =SIMP(statut='f',typ='R'),
           NUME_INIT       =SIMP(statut='f',typ='I'),
         ),
         SENSIBILITE     =SIMP(statut='f',typ=(para_sensi,theta_geom),max='**',
                               fr="Liste des param�tres de sensibilit�.",
                               ang="List of sensitivity parameters",
         ),
           SENS_INIT       =FACT(statut='f',min=1,max=1,
             regles=(EXCLUS('STATIONNAIRE','EVOL_THER', ),),
             STATIONNAIRE    =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             EVOL_THER       =SIMP(statut='f',typ=evol_ther),
             NUME_INIT       =SIMP(statut='f',typ='I'),
           ),
         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt          =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
             TAILLE_BLOC     =SIMP(statut='f',typ='R',defaut= 400. ),
           ),
           b_ldlt_mult      =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non inversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
           b_gcpc          =BLOC(condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
#  A quoi sert eps
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
         ),
         PARM_THETA      =SIMP(statut='f',typ='R',defaut= 0.57),
         ARCHIVAGE       =FACT(statut='f',min=1,max=1,
           regles=(UN_PARMI('LIST_ARCH','PAS_ARCH','LIST_INST','INST'),),
           LIST_ARCH       =SIMP(statut='f',typ=listis),
           LIST_INST       =SIMP(statut='f',typ=listr8),
           INST            =SIMP(statut='f',typ='R',max='**'),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",
                                 into=("RELATIF","ABSOLU")),
           PAS_ARCH        =SIMP(statut='f',typ='I'),
           CHAM_EXCLU      =SIMP(statut='f',typ='TXM',into=("VARI",)),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         INFO            =SIMP(statut='f',typ='I',into=(1,2)),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
THER_NON_LINE=OPER(nom="THER_NON_LINE",op= 186,sd_prod=evol_ther,docu="U4.54.02-d",reentrant='f',
                   fr="Analyse thermique non lin�aire stationnaire ou transitoire" ,
         MODELE          =SIMP(statut='o',typ=(modele) ),
         CHAM_MATER      =SIMP(statut='o',typ=(cham_mater) ),
         CARA_ELEM       =SIMP(statut='c',typ=(cara_elem) ),
         COMP_THER_NL    =FACT(statut='d',min=1,max='**',
           RELATION        =SIMP(statut='f',typ='TXM',defaut="THER_NL",
                                 into=("THER_NL",
                                       "THER_HYDR",
                                       "SECH_GRANGER",
                                       "SECH_MENSI",
                                       "SECH_BAZANT",
                                       "SECH_NAPPE"
                                       ) ),
      regles=(PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
           TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
           GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
           MAILLE          =SIMP(statut='f',typ=ma,max='**'),
         ),
         EVOL_THER_SECH  =SIMP(statut='f',typ=evol_ther),
         EXCIT           =FACT(statut='o',min=1,max='**',
           CHARGE          =SIMP(statut='o',typ=char_ther),
           FONC_MULT       =SIMP(statut='f',typ=fonction),
         ),
         INCREMENT       =FACT(statut='f',min=1,max=1,
           LIST_INST       =SIMP(statut='o',typ=listr8),
           NUME_INIT       =SIMP(statut='f',typ='I'),
           NUME_FIN        =SIMP(statut='f',typ='I'),
         ),
         TEMP_INIT       =FACT(statut='f',min=1,max=1,
           regles=(EXCLUS('STATIONNAIRE','EVOL_THER','CHAM_NO','VALE'),),
           STATIONNAIRE    =SIMP(statut='f',typ='TXM',into=("OUI",)),
           EVOL_THER       =SIMP(statut='f',typ=evol_ther),
           CHAM_NO         =SIMP(statut='f',typ=cham_no_temp_r),
           VALE            =SIMP(statut='f',typ='R'),
           NUME_INIT       =SIMP(statut='f',typ='I'),
         ),
         NEWTON          =FACT(statut='d',min=1,max=1,
           REAC_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           RESI_LINE_RELA  =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
           ITER_LINE_MAXI  =SIMP(statut='f',typ='I',defaut= 0 ),
         ),
         CONVERGENCE     =FACT(statut='d',min=1,max=1,
           RESI_GLOB_MAXI  =SIMP(statut='f',typ='R'),
           RESI_GLOB_RELA  =SIMP(statut='f',typ='R'),
           ITER_GLOB_MAXI  =SIMP(statut='f',typ='I',defaut= 10 ),
         ),
         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Parametres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt          =BLOC(condition = "METHODE == 'LDLT' ",fr="Parametres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
           ),
           b_ldlt_mult     =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Parametres relatifs a la non inversibilit� de la matrice a factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
           b_gcpc          =BLOC(condition = "METHODE == 'GCPC' ", fr="Parametres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
#  A quoi sert eps
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           SYME            =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
         ),
         PARM_THETA      =SIMP(statut='f',typ='R',defaut= 0.57 ),
         ARCHIVAGE       =FACT(statut='f',min=1,max=1,
           regles=(UN_PARMI('LIST_ARCH','PAS_ARCH','LIST_INST','INST', ),),
           LIST_ARCH       =SIMP(statut='f',typ=(listis) ),
           LIST_INST       =SIMP(statut='f',typ=(listr8) ),
           INST            =SIMP(statut='f',typ='R',max='**'),
           PRECISION       =SIMP(statut='f',typ='R',defaut= 1.0E-3 ),
           CRITERE         =SIMP(statut='f',typ='TXM',defaut="RELATIF",into=("RELATIF","ABSOLU",) ),
           PAS_ARCH        =SIMP(statut='f',typ='I'),
           CHAM_EXCLU      =SIMP(statut='f',typ='TXM',into=("VARI",)),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
         OPTION          =SIMP(statut='f',typ='TXM',max='**',
                               into=("FLUX_ELGA_TEMP","FLUX_ELNO_TEMP") ),
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
)  ;
#& MODIF COMMANDE  DATE 05/12/2001   AUTEUR VABHHTS J.PELLET 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
THER_NON_LINE_MO=OPER(nom="THER_NON_LINE_MO",op= 171,sd_prod=evol_ther,
                     fr="Thermique non lineaire en repere mobile",
                     docu="U4.54.03-b",reentrant='f',
         MODELE          =SIMP(statut='o',typ=modele ),
         CHAM_MATER      =SIMP(statut='o',typ=cham_mater ),
         CARA_ELEM       =SIMP(statut='c',typ=cara_elem ),
         EXCIT           =FACT(statut='o',min=1,max='**',
           CHARGE          =SIMP(statut='o',typ=char_ther ),
           FONC_MULT       =SIMP(statut='c',typ=fonction ),
         ),
         TEMP_INIT       =FACT(statut='f',min=1,max=1,
           EVOL_THER       =SIMP(statut='f',typ=evol_ther ),
           NUME_INIT       =SIMP(statut='f',typ='I',defaut= 0 ),
         ),
         CONVERGENCE     =FACT(statut='d',min=1,max=1,
           CRIT_TEMP_RELA  =SIMP(statut='f',typ='R',defaut= 1.E-3 ),
           CRIT_ENTH_RELA  =SIMP(statut='f',typ='R',defaut= 1.E-2 ),
           ITER_GLOB_MAXI  =SIMP(statut='f',typ='I',defaut= 10 ),
           ARRET           =SIMP(statut='c',typ='TXM',defaut="OUI",into=("OUI","NON") ),
         ),
         SOLVEUR         =FACT(statut='d',min=1,max=1,
           METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
           b_mult_front    =BLOC(condition = "METHODE == 'MULT_FRONT' ",fr="Param�tres de la m�thode multi frontale",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="METIS",into=("MD","MDA","METIS") ),
           ),
           b_ldlt          =BLOC(condition = "METHODE == 'LDLT' ",fr="Param�tres de la m�thode LDLT",
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("RCMK","SANS") ),
           ),
           b_ldlt_mult     =BLOC(condition = "METHODE == 'LDLT' or METHODE == 'MULT_FRONT' ",
                                   fr="Param�tres relatifs � la non inversibilit� de la matrice � factorise",
             NPREC           =SIMP(statut='f',typ='I',defaut= 8 ),
             STOP_SINGULIER  =SIMP(statut='f',typ='TXM',defaut="OUI",into=("OUI","NON") ),
           ),
           b_gcpc          =BLOC(condition = "METHODE == 'GCPC' ", fr="Param�tres de la m�thode du gradient conjugu�",
             PRE_COND        =SIMP(statut='f',typ='TXM',into=("LDLT_INC","SANS","DIAG") ),
             NIVE_REMPLISSAGE=SIMP(statut='f',typ='I',defaut= 0 ),
             RENUM           =SIMP(statut='f',typ='TXM',defaut="RCMK",into=("SANS","RCMK") ),
             RESI_RELA       =SIMP(statut='f',typ='R',defaut= 1.E-6 ),
             NMAX_ITER       =SIMP(statut='f',typ='I',defaut= 0 ),
           ),
           EPS             =SIMP(statut='f',typ='R',defaut= 0.E+0 ),
           SYME            =SIMP(statut='f',typ='TXM',defaut="NON",into=("OUI","NON") ),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**' ),
         INFO            =SIMP(statut='f',typ='I',into=(1,2) ),
)  ;



