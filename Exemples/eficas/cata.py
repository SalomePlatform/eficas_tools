# -*- coding: utf-8 -*-

from Accas import SIMP,FACT,BLOC
from Accas import AsException,AsType
from Accas import ASSD,CO,GEOM,fonction
from Accas import OPER,MACRO,JDC_CATA,FORM,PROC
from Accas import AU_MOINS_UN,UN_PARMI,PRESENT_PRESENT,EXCLUS,ENSEMBLE,PRESENT_ABSENT
from Accas import EVAL

#compatibilite avec V9
import Noyau
class ASSD(ASSD,Noyau.AsBase):pass
class GEOM(GEOM,Noyau.AsBase):pass
#fin compatibilite

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


class resultat(ASSD):pass

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

class table(ASSD):pass

class tabl_aire_int   (table):pass
class tabl_calc_g_loca(table):pass
class tabl_calc_g_th  (table):pass
class tabl_cara_geom  (table):pass
class tabl_char_limite(table):pass
class tabl_ener_elas  (table):pass
class tabl_ener_pot   (table):pass
class tabl_ener_cin   (table):pass
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


JdC=JDC_CATA(code="ASTER")

def DEBUT_prod(self,PAR_LOT,**args):
  """
     Fonction sdprod de la macro DEBUT
  """
  self.jdc.set_par_lot(PAR_LOT)

DEBUT=MACRO(nom="DEBUT",op=0 ,docu="U4.11.01-f1",repetable='n',
           fr="Ouverture d une étude. Allocation des ressources mémoire et disque",
          sd_prod=DEBUT_prod,

         PAR_LOT         =SIMP(fr="mode de traitement des commandes",statut='f',typ='TXM',
                           into=("OUI","NON"),defaut="OUI"),
         BASE            =FACT(fr="définition des paramètres associés aux bases JEVEUX",
                               statut='f',min=01,max=03,
           FICHIER         =SIMP(fr="nom de la base",statut='o',typ='TXM',
                                 into=('GLOBALE','VOLATILE','LOCALE'),),
           TITRE           =SIMP(statut='f',typ='TXM'),
           CAS             =SIMP(statut='f',typ='TXM'),
           NMAX_ENRE       =SIMP(fr="nombre maximum d enregistrements",statut='f',typ='I'),
           LONG_ENRE       =SIMP(fr="longueur des enregistrements",statut='f',typ='I'),
           LONG_REPE       =SIMP(fr="longueur du répertoire",statut='f',typ='I'),
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
         CODE            =FACT("définition d un nom pour l'esemble d'une étude",
                               statut='f',min=01,max=01,
           NOM             =SIMP(statut='o',typ='TXM'),
           UNITE           =SIMP(statut='f',typ='I',defaut=15),
         ),
         DEBUG           =FACT(fr="option de déboggage reservée aux développeurs",
                               statut='f',min=01,max=01,
           JXVERI          =SIMP(fr="vérifie l intégrité de la segmentation mémoire",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           JEVEUX          =SIMP(fr="force les déchargement sur disque",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           ENVIMA          =SIMP(fr="imprime les valeurs définies dans ENVIMA",
                                 statut='f',typ='TXM',into=('TEST',)),
         ),
         MEMOIRE         =FACT(fr="mode de gestion mémoire utilisé",statut='f',min=01,max=01,
           GESTION         =SIMP(statut='f',typ='TXM',into=('COMPACTE','RAPIDE'),defaut='RAPIDE'),
           TYPE_ALLOCATION =SIMP(statut='f',typ='I',into=(1,2,3,4),defaut=1),
           TAILLE          =SIMP(statut='f',typ='I'),
           TAILLE_BLOC     =SIMP(statut='f',typ='R',defaut=800.),
           PARTITION       =SIMP(statut='f',typ='R'),
         ),
 );

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
                           fr="Informations complémentaires pour la lecture MED.",
                           ang="Further information for MED readings.",
#
# Pour une lecture dans un fichier MED, on peut préciser le nom sous lequel
# le maillage y a été enregistré. Par défaut, on va le chercher sous le nom du concept à créer.
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

AFFE_MODELE=OPER(nom="AFFE_MODELE",op=18,sd_prod=modele,docu="U4.41.01-f1",
                 fr="Affectation des éléments finis sur le maillage",reentrant='n',
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
                                        fr="modelisations mécaniques",
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
                                                                      "PLAN_INCO",
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

AFFE_CARA_ELEM=OPER(nom="AFFE_CARA_ELEM",op=  19,sd_prod=cara_elem,
                    fr="Affectation de caractéristiques à des éléments de structure",
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

AFFE_CHAR_MECA=OPER(nom="AFFE_CHAR_MECA",op=   7,sd_prod=char_meca
                    ,fr="Affectation de charges et conditions aux limites mécaniques constantes",
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
         TEMP_CALCULEE   =SIMP(statut='f',fr="Champ de température issu d'un autre calcul",
                               typ=(evol_ther,cham_no_temp_r,carte_temp_r,carte_temp_f ) ),
         HYDR_CALCULEE   =SIMP(statut='f',fr="Champ d hydratation issu d'un autre calcul",
                               typ=evol_ther ),
         SECH_CALCULEE   =SIMP(statut='f',fr="Champ de séchage issu d'un autre calcul",
                               typ=(evol_ther,cham_no_temp_r,carte_temp_r,carte_temp_f ) ),
         EPSA_CALCULEE   =SIMP(statut='f',fr="Champ de déformation anélastique issu d'un autre calcul",
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
                                 fr="Paramètres de la méthode des contraintes actives (contact uniquement)",
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
                                 fr="Paramètres de la méthode Lagrangienne (contact avec ou sans frottement)",
                NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL",)),
                FROTTEMENT      =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SANS","COULOMB",) ),
                REAC_GEOM_INTE  =SIMP(statut='f',typ='I',defaut= 2),
                SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'),
                SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
                DIST_1          =SIMP(statut='f',typ='R'),
                DIST_2          =SIMP(statut='f',typ='R'),
                b_frottement    =BLOC(condition = "FROTTEMENT == 'COULOMB' ",fr="Paramètres du frottement de Coulomb",
                     COULOMB         =SIMP(statut='o',typ='R',max=1),
                     COEF_MATR_FROT  =SIMP(statut='f',typ='R',defaut=0.E+0),
                     VECT_Y          =SIMP(statut='f',typ='R',min=3,max=3),),),
           b_penalisation       =BLOC(condition = "METHODE == 'PENALISATION' ",
                                      fr="Paramètres de la méthode pénalisée (contact avec ou sans frottement)",
                NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL",)),
                E_N             =SIMP(statut='f',typ='R'),
                FROTTEMENT      =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SANS","COULOMB",) ),
                REAC_GEOM_INTE  =SIMP(statut='f',typ='I',defaut= 2),
                SANS_NOEUD      =SIMP(statut='f',typ=no,max='**'),
                SANS_GROUP_NO   =SIMP(statut='f',typ=grno,max='**'),
                DIST_1          =SIMP(statut='f',typ='R'),
                DIST_2          =SIMP(statut='f',typ='R'),
                b_frottement    =BLOC(condition = "FROTTEMENT == 'COULOMB' ",fr="Paramètres du frottement de Coulomb",
                     COULOMB         =SIMP(statut='o',typ='R',max=1),
                     E_T             =SIMP(statut='f',typ='R',
                                           fr="Active la pénalisation sur le frottement et définit le coefficient de pénalisation"),
                     COEF_MATR_FROT  =SIMP(statut='f',typ='R',defaut=0.E+0),
                     VECT_Y          =SIMP(statut='f',typ='R',min=3,max=3),),),
           b_continue      =BLOC(condition = "METHODE == 'CONTINUE' ",
                                 fr="Paramètres de la méthode continue (contact avec ou sans frottement)",
                NOM_CHAM        =SIMP(statut='f',typ='TXM',defaut="DEPL",into=("DEPL",)),
                FROTTEMENT      =SIMP(statut='f',typ='TXM',defaut="SANS",into=("SANS","COULOMB",) ),
                INTEGRATION     =SIMP(statut='f',typ='TXM',defaut="NOEUD",into=("GAUSS","NOEUD")),
                COEF_REGU_CONT  =SIMP(statut='f',typ='R',defaut=100.E+0),
                MODL_AXIS       =SIMP(statut='o',typ='TXM',into=("OUI","NON")),
                ITER_GEOM_MAXI  =SIMP(statut='f',typ='I',defaut=2),
                ITER_CONT_MAXI  =SIMP(statut='f',typ='I',defaut=30),
                b_frottement    =BLOC(condition = "FROTTEMENT == 'COULOMB' ",fr="Paramètres du frottement de Coulomb",
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

         EPSI_INIT       =FACT(statut='f',fr="Appliquer un chargement de déformation initiale à un volume 3D ou 2D",
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
#  rajout d'un mot clé REPERE :/ LOCAL /GLOBAL
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

         FORCE_ARETE     =FACT(statut='f',fr="Appliquer des forces linéiques à une arete d élément volumique ou de coque",
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
#  rajour d'un mot clé REPERE :/ LOCAL /GLOBAL
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

         FORCE_CONTOUR   =FACT(statut='f',fr="Appliquer des forces linéiques au bord d'un domaine 2D ou AXIS_FOURIER",
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
                                 fr="Force de Laplace due à la présence d'un conducteur rectiligne secondaire non maillé",
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

             POSITION        =SIMP(statut='f',typ='TXM',fr="Direction prédéfinie",into=("PARA","INFI","FINI",) ),
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

         FORCE_FACE      =FACT(statut='f',fr="Appliquer des forces surfaciques sur une face d'éléments volumiques",
                                 min=1,max='**',
             regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),
                     AU_MOINS_UN('FX','FY','FZ'),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             FX              =SIMP(statut='f',typ='R' ),
             FY              =SIMP(statut='f',typ='R' ),
             FZ              =SIMP(statut='f',typ='R' ),
           ),
         FORCE_INTERNE   =FACT(statut='f',fr="Appliquer des forces volumiques (2D ou 3D) à un domaine volumique",
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

         IMPE_FACE       =FACT(statut='f',fr="Appliquer une impédance acoustique à une face",min=1,max='**',
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
        FORCE_POUTRE    =FACT(statut='f',fr="Appliquer des forces linéiques sur des poutres",min=1,max='**',
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
#  rajour d'un mot clé REPERE :/ LOCAL /GLOBAL
               FX              =SIMP(statut='f',typ='R' ),
               FY              =SIMP(statut='f',typ='R' ),
               FZ              =SIMP(statut='f',typ='R' ),

               N               =SIMP(statut='f',typ='R' ),
               VY              =SIMP(statut='f',typ='R' ),
               VZ              =SIMP(statut='f',typ='R' ),

           ),

         FORCE_TUYAU     =FACT(statut='f',fr="imposer une pression dans un élément TUYAU",min=1,max='**',
             regles=(AU_MOINS_UN('TOUT','GROUP_MA','MAILLE'),
                     PRESENT_ABSENT('TOUT','GROUP_MA','MAILLE'),),
             TOUT            =SIMP(statut='f',typ='TXM',into=("OUI",) ),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             PRES            =SIMP(statut='f',typ='R' ),
           ),

        INTE_ELEC       =FACT(statut='f',fr="Force de Laplace due à la présence d'un conducteur non rectiligne secondaire",
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

         LIAISON_CHAMNO  =FACT(statut='f',fr="définir une relation linéaire entre tous les ddls d'un concept cham_nno",
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
           LIAISON_DDL     =FACT(statut='f',fr="Définir une relation linéaire entre des ddls de deux ou plusieurs noeuds",
                                 min=1,max='**',
             regles=(UN_PARMI('GROUP_NO','NOEUD'),),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             DDL             =SIMP(statut='o',typ='TXM',max='**'),
             COEF_MULT       =SIMP(statut='o',typ='R',max='**'),
             COEF_IMPO       =SIMP(statut='o',typ='R' ),
           ),
           LIAISON_ELEM    =FACT(statut='f',fr="Raccorder une poutre à une partie massive 3D ou une coque", min=1,max='**',
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

           LIAISON_GROUP   =FACT(statut='f',fr="Définir des relations linéaires entre certains ddls de couples de noeuds",
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

           LIAISON_OBLIQUE =FACT(statut='f',fr="Appliquer à des noeuds une valeur de déplacement dans un repere oblique",
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

           LIAISON_SOLIDE  =FACT(statut='f',fr="Modéliser une partie indéformable d'une structure",min=1,max='**',
             regles=(UN_PARMI('GROUP_NO','NOEUD','GROUP_MA','MAILLE'),),
             GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
             NOEUD           =SIMP(statut='f',typ=no,max='**'),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             NUME_LAGR       =SIMP(statut='f',typ='TXM',defaut="NORMAL",into=("NORMAL","APRES") ),
           ),

           LIAISON_UNIF    =FACT(statut='f',fr="Imposer une meme valeur (inconnue) à des ddls d'un emsemble de noeuds",
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

         PRES_REP        =FACT(statut='f',fr="Appliquer une pression à un domaine de milieu continu 2D ou 3D",
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

         VITE_FACE       =FACT(statut='f',fr="Imposer des vitesses acoustiquesnormales à une face",min=1,max='**',
             regles=(AU_MOINS_UN('GROUP_MA','MAILLE'),),
             GROUP_MA        =SIMP(statut='f',typ=grma,max='**'),
             MAILLE          =SIMP(statut='f',typ=ma,max='**'),
             VNOR            =SIMP(statut='o',typ='R' ),
           ),
         INFO            =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;

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
                      fr="Calcul des matrices assemblées (matr_asse_gd) par exemple de rigidité, de masse ",
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

def mode_iter_simult_prod(MATR_A,MATR_C,TYPE_RESU,**args ):
  if TYPE_RESU == "MODE_FLAMB" : return mode_flamb
  if AsType(MATR_C) == matr_asse_depl_r : return mode_meca_c
  if AsType(MATR_A) == matr_asse_depl_r : return mode_meca
  if AsType(MATR_A) == matr_asse_pres_r : return mode_acou
  if AsType(MATR_A) == matr_asse_gene_r : return mode_gene
  raise AsException("type de concept resultat non prevu")

MODE_ITER_SIMULT=OPER(nom="MODE_ITER_SIMULT",op=  45,sd_prod=mode_iter_simult_prod,
                      fr="Modes propres par itérations simultanées ; valeurs propres et modes propres réels ou complexes",
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
                               fr="Calcul des modes de corps rigide, uniquement pour la méthode TRI_DIAG" ),

         b_flamb         =BLOC(condition = "TYPE_RESU == 'MODE_FLAMB'",
           CALC_FREQ       =FACT(statut='d',min=0,max=1,
             OPTION          =SIMP(statut='f',typ='TXM',defaut="PLUS_PETITE",into=("PLUS_PETITE","BANDE","CENTRE"),
                                   fr="Choix de l option et par conséquent du shift du problème modal" ),
             b_plus_petite =BLOC(condition = "OPTION == 'PLUS_PETITE'",fr="Recherche des plus petites valeurs propres",
               NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 10,val_min=0 ),
             ),
             b_centre      =BLOC(condition = "OPTION == 'CENTRE'",
                                 fr="Recherche des valeurs propres les plus proches d une valeur donnée",
               CHAR_CRIT       =SIMP(statut='o',typ='R',min=1,max=1,
                                     fr="Charge critique autour de laquelle on cherche les charges critiques propres"),
             ),
             b_bande       =BLOC(condition = "(OPTION == 'BANDE')",
                                 fr="Recherche des valeurs propres dans une bande donnée",
               CHAR_CRIT       =SIMP(statut='o',typ='R',min=2,max=2,
                                     fr="Valeur des deux charges critiques délimitant la bande de recherche"),
             ),
             APPROCHE        =SIMP(statut='f',typ='TXM',defaut="REEL",into=("REEL","IMAG"),
                                   fr="Choix du pseudo-produit scalaire pour la résolution du problème quadratique" ),
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
                                   fr="Choix de l option et par conséquent du shift du problème modal" ),
             b_plus_petite =BLOC(condition = "OPTION == 'PLUS_PETITE'",fr="Recherche des plus petites valeurs propres",
               NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 10,val_min=0 ),
             ),
             b_centre       =BLOC(condition = "OPTION == 'CENTRE'",
                                  fr="Recherche des valeurs propres les plus proches d une valeur donnée",
               FREQ            =SIMP(statut='o',typ='R',min=1,max=1,
                                     fr="Fréquence autour de laquelle on cherche les fréquences propres"),
               AMOR_REDUIT     =SIMP(statut='f',typ='R',max=1,),
               NMAX_FREQ       =SIMP(statut='f',typ='I',defaut= 10,val_min=0 ),
             ),
             b_bande         =BLOC(condition = "(OPTION == 'BANDE')",
                                   fr="Recherche des valeurs propres dans une bande donnée",
               FREQ            =SIMP(statut='o',typ='R',min=2,max=2,
                                     fr="Valeur des deux fréquences délimitant la bande de recherche"),
             ),
             APPROCHE        =SIMP(statut='f',typ='TXM',defaut="REEL",into=("REEL","IMAG"),
                                   fr="Choix du pseudo-produit scalaire pour la résolution du problème quadratique" ),
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
         NORME      =SIMP(statut='f',typ='TXM',fr="Norme prédéfinie : masse généralisée, euclidienne,...",
                          into=("MASS_GENE","RIGI_GENE","EUCL","EUCL_TRAN","TRAN","TRAN_ROTA") ),
         NOEUD      =SIMP(statut='f',typ=no, fr="Composante donnée d un noeud spécifié égale à 1"),
         b_noeud    =BLOC(condition = "NOEUD != None",
           NOM_CMP    =SIMP(statut='o',typ='TXM' ),
         ),
         AVEC_CMP   =SIMP(statut='f',typ='TXM',max='**'),
         SANS_CMP   =SIMP(statut='f',typ='TXM',max='**'),
         MASS_INER  =SIMP(statut='f',typ=tabl_mass_iner ),
         MODE_SIGNE =FACT(statut='f',min=00,max=01,fr="Imposer un signe sur une des composantes des modes",
           NOEUD      =SIMP(statut='o',typ=no,fr="Noeud ou sera imposé le signe"),
           NOM_CMP    =SIMP(statut='o',typ='TXM',fr="Composante du noeud ou sera imposé le signe" ),
           SIGNE      =SIMP(statut='f',typ='TXM',defaut="POSITIF",into=("NEGATIF","POSITIF"),
                            fr="Choix du signe" ),
         ),
         TITRE      =SIMP(statut='f',typ='TXM',max='**'),
         INFO       =SIMP(statut='f',typ='I',defaut= 1,into=( 1 , 2) ),
)  ;

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

DEFI_LIST_REEL=OPER(nom="DEFI_LIST_REEL",op=24,sd_prod=listr8,
                    fr="Définition d une suite croissante de réels",
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

def defi_valeur_prod(self,IS=None,R8=None,TX=None,C8=None,LS=None):
  if IS != None  : return entier
  if R8 != None  : return reel
  if TX != None  : return chaine
  if C8 != None  : return complexe
  if LS != None  : return liste
  raise AsException("type de concept resultat non prevu")

DEFI_VALEUR=MACRO(nom="DEFI_VALEUR",op=-4,sd_prod=defi_valeur_prod,
                 fr="Affectation d une valeur à une variable Superviseur",
                 docu="U4.31.04-e1",reentrant='f',
         regles=(UN_PARMI('IS','R8','TX','C8','LS'),),
         IS              =SIMP(statut='f',typ='I',max='**'),
         R8              =SIMP(statut='f',typ='R',max='**'),
         TX              =SIMP(statut='f',typ='TXM',max='**'),
         C8              =SIMP(statut='f',typ='C',max='**'),
         LS              =SIMP(statut='f',typ='L',max='**'),
)  ;

FORMULE = FORM( nom='FORMULE',op=-5,sd_prod=fonction,
                fr="Définition d une fonction",reentrant = 'n',
                regles=(UN_PARMI('REEL','ENTIER','COMPLEXE'),),
                REEL = SIMP(typ = 'shell',max=1),
                ENTIER = SIMP(typ = 'shell',max=1),
                COMPLEXE = SIMP(typ = 'shell',max=1),
) ;

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

def INCLUDE_prod(self,UNITE,**args):
  """ Fonction sd_prod pour la macro include
  """
  # Si unite a change on reevalue le fichier associe
  if not hasattr(self,'unite') or self.unite != UNITE:
    f,text=self.get_file(unite=UNITE)
    self.unite=UNITE
    self.fichier_init = f
    # on execute le texte fourni dans le contexte forme par
    # le contexte de l etape pere (global au sens Python)
    # et le contexte de l etape (local au sens Python)
    code=compile(text,f,'exec')
    if self.jdc and self.jdc.par_lot == 'NON':
      # On est en mode commande par commande
      # On teste la validite de la commande avec interruption eventuelle
      cr=self.report()
      self.parent.cr.add(cr)
      if not cr.estvide():
        raise EOFError
    d={}
    self.g_context = d
    self.contexte_fichier_init = d
    exec code in self.parent.g_context,d

def INCLUDE_context(self,d):
  """ Fonction op_init pour macro INCLUDE
  """
  for k,v in self.g_context.items():
    d[k]=v

INCLUDE=MACRO(nom="INCLUDE",op=-1,docu="U4.13.01-e",
             fr="Débranchement vers un fichier de commandes secondaires",
             #fichier_ini=1,
             sd_prod=INCLUDE_prod,
             op_init=INCLUDE_context,
         UNITE = SIMP(statut='o',typ='I'),
         INFO  = SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
);

def calc_char_seisme_prod(MATR_MASS,**args ):
  if AsType(MATR_MASS) == matr_asse_depl_r : return cham_no_depl_r
  raise AsException("type de concept resultat non prevu")

CALC_CHAR_SEISME=OPER(nom="CALC_CHAR_SEISME",op=  92,sd_prod=calc_char_seisme_prod,
                      docu="U4.63.01-e",reentrant='n',
         regles=(UN_PARMI('MONO_APPUI','MODE_STAT' ),),
         MATR_MASS       =SIMP(statut='o',typ=matr_asse_depl_r,fr="Matrice de masse" ),
         DIRECTION       =SIMP(statut='o',typ='R',max=06,fr="Directions du séisme imposé"),
         MONO_APPUI      =SIMP(statut='f',typ='TXM',into=("OUI",) ),
         MODE_STAT       =SIMP(statut='f',typ=(mode_stat_depl,mode_stat_acce,mode_stat_forc,) ),
         b_mode_stat     =BLOC ( condition = "MODE_STAT != None",
           regles=(UN_PARMI('NOEUD','GROUP_NO' ),),
           NOEUD           =SIMP(statut='f',typ=no,max='**'),
           GROUP_NO        =SIMP(statut='f',typ=grno,max='**'),
         ),
         TITRE           =SIMP(statut='f',typ='TXM',max='**'),
)  ;

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
         __num=NUME_DDL_GENE(BASE=BASE,NB_VECT=NB_VECT,STOCKAGE=m['PROFIL'])
      nompro=m['PROFIL']
      motscles={}
      if   m['MATR_ASSE']     :  motscles['MATR_ASSE']     =m['MATR_ASSE']
      elif m['MATR_ASSE_GENE']:  motscles['MATR_ASSE_GENE']=m['MATR_ASSE_GENE']
      else:
          ier=ier+1
          self.cr.fatal("MATR_ASSE et MATR_ASSE_GENE absents")
          return ier
      self.DeclareOut('mm',m['MATRICE'])
      mm=PROJ_MATR_BASE(BASE=BASE,NUME_DDL_GENE=__num,NB_VECT=NB_VECT,**motscles)

  iocc=0
  if VECT_ASSE_GENE:
    for v in VECT_ASSE_GENE:
      iocc=iocc+1
      if (iocc==1 and not MATR_ASSE_GENE):
         __num=NUME_DDL_GENE(BASE=BASE,NB_VECT=NB_VECT,STOCKAGE='DIAG')
      motscles={}
      if   v['VECT_ASSE']     :  motscles['VECT_ASSE']     =v['VECT_ASSE']
      elif v['VECT_ASSE_GENE']:  motscles['VECT_ASSE_GENE']=v['VECT_ASSE_GENE']
      else:
          ier=ier+1
          self.cr.fatal("MATR_ASSE et MATR_ASSE_GENE absents")
          return ier
      motscles['TYPE_VECT']=v['TYPE_VECT']
      self.DeclareOut('vv',v['VECTEUR'])
      vv=PROJ_VECT_BASE(BASE=BASE,NUME_DDL_GENE=__num,NB_VECT=NB_VECT,**motscles)

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
                      fr="Projection des matrices et/ou vecteurs assemblés sur une base de vecteurs",
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

RETOUR=PROC(nom="RETOUR",op= -2,docu="U4.13.02-e",
            fr="Retour au fichier de commandes appelant",
) ;

DEFI_OBSTACLE=OPER(nom="DEFI_OBSTACLE",op=  73,sd_prod=obstacle
                    ,fr="Définition d un obstacle plan perpendiculaire à une structure filaire",
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

DYNA_TRAN_MODAL=OPER(nom="DYNA_TRAN_MODAL",op=  74,sd_prod=tran_gene,
                     fr="Réponse dynamique transitoire en coordonnées généralisées par recombinaison modale",
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
           CORR_STAT       =SIMP(statut='f',typ='TXM',into=("OUI","NON") ),
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

FIN=PROC(nom="FIN",op=9999,repetable='n',fr="Fin d'une étude",
         docu="U4.11.02-f",
         RETASSAGE       =SIMP(fr="provoque le retassage de la base GLOBALE",
                               statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
         PERFORMANCE     =SIMP(fr="provoque l'impression d'un résumé des mesures de temps ",
                               statut='f',typ='TXM',defaut="OUI",into=("OUI","NON",) ),
         INFO_RESU       =SIMP(fr="provoque l'impression des informations sur les structures de données",
                               statut='f',typ='TXM',defaut="OUI",into=("OUI","NON",) ),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="MESSAGE"),
)  ;




