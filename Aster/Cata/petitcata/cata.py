# -*- coding: utf-8 -*-
#& MODIF ENTETE  DATE 18/03/2003   AUTEUR MCOURTOI M.COURTOIS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
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
import Accas
from Accas import *
from Accas import _F
import string

import ops

try:
  import aster
except:
  pass

#
__version__="$Name:  $"
__Id__="$Id: cata.py,v 1.2.6.1 2006/05/24 16:44:25 cchris Exp $"
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
class liste           (ASSD):pass
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


# liste :
#--------------------------------
class listr8   (ASSD):
  def LIST_VALEURS(self) :
    """ retourne la liste des valeurs [ val1, ...] """
    vale=string.ljust(self.get_name(),19)+'.VALE'
    return list(aster.getvectjev(vale))
   


# maillage :
#--------------------------------
class maillage(ASSD):
  def LIST_GROUP_NO(self) :
    """ retourne la liste des groupes de noeuds sous la forme :
        [ (gno1, nb noeuds  gno1), ...] """
    return aster.GetMaillage(self.get_name(), "GROUP_NO")
  def LIST_GROUP_MA(self) :
    """ retourne la liste des groupes de mailles sous la forme :
        [ (gma1, nb mailles gma1, dime max des mailles gma1), ...] """
    return aster.GetMaillage(self.get_name(), "GROUP_MA")
    
    
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
class cham_elem_facy_r(cham_elem):pass
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
class cham_elem_spma_r(cham_elem):pass
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
class cham_no_spma_r   (cham_no):pass
class cham_no_temp_c   (cham_no):pass
class cham_no_temp_f   (cham_no):pass
class cham_no_temp_r   (cham_no):pass
class cham_no_vanl_r   (cham_no):pass
class cham_no_var2_r   (cham_no):pass
class cham_no_vnor_c   (cham_no):pass


# resultat : (evol,mode_stat,mode_meca)
#--------------------------------

class resultat(ASSD):
  def LIST_CHAMPS (self) :
    return aster.GetResu(self.get_name(), "CHAMPS")
  def LIST_NOM_CMP (self) :
    return aster.GetResu(self.get_name(), "COMPOSANTES")
  def LIST_VARI_ACCES (self) :
    return aster.GetResu(self.get_name(), "VARI_ACCES")

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
class fonction(ASSD):
  def LIST_VALEURS(self) :
    """ retourne la liste des valeurs [ val1, ...] """
    vale=string.ljust(self.get_name(),19)+'.VALE'
    lbl=list(aster.getvectjev(vale))
    lbr=[]
    for i in range(len(lbl)/2):
        lbr.append(lbl[i])
        lbr.append(lbl[len(lbl)/2+i])
    return lbr
class para_sensi(fonction):pass
class fonction_c(fonction):
  def LIST_VALEURS(self) :
    """ retourne la liste des valeurs [ val1, ...] """
    vale=string.ljust(self.get_name(),19)+'.VALE'
    lbl=list(aster.getvectjev(vale))
    lbr=[]
    for i in range(len(lbl)/3):
        lbr.append(lbl[i])
        lbr.append(lbl[len(lbl)/3+i*2])
        lbr.append(lbl[len(lbl)/3+i*2+1])
    return lbr
class nappe(fonction):pass


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




# table :
#--------------------------------

class table(ASSD):
  def __getitem__(self,key):
      requete=string.ljust(key[0],24)
      tblp=string.ljust(self.get_name(),19)+'.TBLP'
      tabnom=list(aster.getvectjev(tblp))
      for i in range(len(tabnom)) : 
         if tabnom[i]==requete: break
      resu=aster.getvectjev(tabnom[i+2])
      if key[1]>len(resu) : raise KeyError
      else                : return resu[key[1]-1]

class tabl_aire_int   (table):pass
class tabl_calc_g_loca(table):pass
class tabl_calc_g_th  (table):pass
class tabl_cara_geom  (table):pass
class tabl_char_limite(table):pass
class tabl_ener_elas  (table):pass
class tabl_ener_pot   (table):pass
class tabl_ener_cin   (table):pass
class tabl_trav_ext   (table):pass
class tabl_ener_totale(table):pass
class tabl_indic_ener (table):pass
class tabl_indic_seuil(table):pass
class tabl_intsp      (table):pass
class tabl_mass_iner  (table):pass
class tabl_post_alea  (table):pass
class tabl_post_beta  (table):pass
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

#& MODIF COMMUN  DATE 31/03/2003   AUTEUR ASSIRE A.ASSIRE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2003  EDF R&D                  WWW.CODE-ASTER.ORG
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
DEBUT=MACRO(nom="DEBUT",op=ops.build_debut ,docu="U4.11.01-g",repetable='n',
            UIinfo={"groupes":("Gestion du travail",)},
           fr="Ouverture d une étude. Allocation des ressources mémoire et disque",

         PAR_LOT         =SIMP(fr="mode de traitement des commandes",statut='f',typ='TXM',
                           into=("OUI","NON"),defaut="OUI"),
         BASE            =FACT(fr="définition des paramètres associés aux bases JEVEUX",
                               statut='f',min=1,max=3,
           FICHIER         =SIMP(fr="nom de la base",statut='o',typ='TXM',
                                 into=('GLOBALE','VOLATILE','LOCALE'),),
           TITRE           =SIMP(statut='f',typ='TXM'),
           CAS             =SIMP(statut='f',typ='TXM'),
           NMAX_ENRE       =SIMP(fr="nombre maximum d enregistrements",statut='f',typ='I'),
           LONG_ENRE       =SIMP(fr="longueur des enregistrements",statut='f',typ='I'),
           LONG_REPE       =SIMP(fr="longueur du répertoire",statut='f',typ='I'),
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
         CODE            =FACT(fr="définition d un nom pour l'esemble d'une étude",
                               statut='f',min=1,max=1,
           NOM             =SIMP(statut='o',typ='TXM'),
           NIV_PUB_WEB     =SIMP(statut='o',typ='TXM',into=('INTERNET','INTRANET')),
           UNITE           =SIMP(statut='f',typ='I',defaut=15),
         ),
         DEBUG           =FACT(fr="option de déboggage reservée aux développeurs",
                               statut='f',min=1,max=1,
           JXVERI          =SIMP(fr="vérifie l intégrité de la segmentation mémoire",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           JEVEUX          =SIMP(fr="force les déchargement sur disque",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           ENVIMA          =SIMP(fr="imprime les valeurs définies dans ENVIMA",
                                 statut='f',typ='TXM',into=('TEST',)),
         ),
         MEMOIRE         =FACT(fr="mode de gestion mémoire utilisé",statut='f',min=1,max=1,
           GESTION         =SIMP(statut='f',typ='TXM',into=('COMPACTE','RAPIDE'),defaut='RAPIDE'),
           TYPE_ALLOCATION =SIMP(statut='f',typ='I',into=(1,2,3,4),defaut=1),
           TAILLE          =SIMP(statut='f',typ='I'),
           TAILLE_BLOC     =SIMP(statut='f',typ='R',defaut=800.),
           PARTITION       =SIMP(statut='f',typ='R'),
         ),
 );
#& MODIF COMMANDE  DATE 22/04/2003   AUTEUR MCOURTOI M.COURTOIS 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
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
AFFE_MODELE=OPER(nom="AFFE_MODELE",op=18,sd_prod=modele,docu="U4.41.01-g",
            fr="Affectation des éléments finis sur le maillage",
            reentrant='n',
            UIinfo={"groupes":("Modélisation",)},
VERIF=SIMP(statut='f',typ='TXM',max=2,into=("MAILLE","NOEUD")),
) ;

GLOB_OPER=OPER(nom="GLOB_OPER",op=18,sd_prod=modele,docu="U4.41.01-g",
        FORMAT          =SIMP(statut='f',typ='TXM',position='global',
                               into=("TABLEAU","AGRAF","XMGRACE",),),
                b_unit1  =BLOC(condition = "FORMAT == 'TABLEAU'",
                               TOTO1  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                              ),
                b_unit2  =BLOC(condition = "FORMAT == None",
                               TOTO2  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                              ),
             )

PLS_BASE_SIMPLE=OPER(nom="PLS_BASE_SIMPLE",op=19,sd_prod=cara_elem,
                    fr="Exemple de PLUSIEURS_BASE_Panel sans validator",
                    docu="U4.42.01-g",reentrant='n',
            	    UIinfo={"groupes":("Modélisation",)},
  VAR1=SIMP(statut='o',typ='TXM',min=1,max=6 ),
  VAR2=SIMP(statut='o',typ='TXM',min=1,max=6,into =( "TUTU","TATA","CCCC")),
  VAR3=SIMP(statut='o',typ='I',min=1,max=1,into =( 1,2,3)),
  VAR4=SIMP(statut='o',typ='I',min=1,max=1),
  VAR44=SIMP(statut='o',typ='I',min=1,max=6),
  VAR5=SIMP(statut='o',typ='TXM',min=1,max=1),
  VAR6=SIMP(statut='o',typ='C',min=1,max=1),
  MODELE=SIMP(statut='o',typ=modele ),
) ;

TESTS_VALID=OPER(nom="TESTS_VALID",op=19,sd_prod=cara_elem,
                    fr="Exemple de PLUSIEURS_BASE_Panel sans validator",
                    docu="U4.42.01-g",reentrant='n',
            	    UIinfo={"groupes":("Modélisation",)},
  LongStr=SIMP(statut='o',typ='TXM',validators=LongStr(3,5)),
  ListStr=SIMP(statut='o',typ='TXM',min=1,max=4,validators=LongStr(3,5)),
  PairVal=SIMP(statut='o',typ='I',min=1,max=4,validators=PairVal()),
  RangeVal=SIMP(statut='o',typ='I',validators=RangeVal(3,15)),
  CardVal=SIMP(statut='o',typ='I',max='**',validators=CardVal(3,15)),
  EnumVal=SIMP(statut='o',typ='I',validators=EnumVal((3,2,4,8,9,15))),
  OrdList=SIMP(statut='o',typ='I',max='**',validators=OrdList("croissant")),
  OrdList2=SIMP(statut='o',typ='I',into=(1,2,3,4,5,6),max='**',validators=OrdList("croissant")),
  TypeVal=SIMP(statut='o',typ='I',validators=TypeVal(1)),
  Compul=SIMP(statut='o',typ='I',max=5,validators=Compulsory((1,2))),
  CompulInto=SIMP(statut='o',typ='I',max=5,into=(1,2,3,4,5),validators=Compulsory((1,2))),
  Norep=SIMP(statut='o',typ='I',max=5,validators=NoRepeat()),
  NorepInto=SIMP(statut='o',typ='I',max=5,into=(1,2,3,4,5),validators=NoRepeat()),
) ;

PLS_BASE_NOREPEAT=OPER(nom="PLS_BASE_NOREPEAT",op=19,sd_prod=cara_pout,
                    fr="Exemple de PLUSIEURS_BASE_Panel avec validator",
                    docu="U4.42.01-g",reentrant='n',
            	    UIinfo={"groupes":("Modélisation",)},
  VAR1=SIMP(statut='o',typ='TXM',min=1,max=6,validators=NoRepeat()),
  VAR2=SIMP(statut='o',typ='TXM',min=1,max=6,into =( "TUTU","TATA","CCCC"),validators=NoRepeat()),
  VAR3=SIMP(statut='o',typ='I',min=1,max=1,into =( 1,2,3),validators=PairVal()),
  VAR4=SIMP(statut='o',typ='I',min=1,max=1,validators=PairVal()),
  VAR5=SIMP(statut='o',typ='I',min=1,max=6,validators=PairVal()),
  VAR6=SIMP(statut='o',typ='I',min=1,max=6,validators=(NoRepeat(),PairVal())),
  VAR7=SIMP(statut='o',typ='I',min=1,max=6,validators=[NoRepeat(),PairVal()]),
) ;

def toto(**args):
    return maillage

BLOCBLOC=OPER(nom="BLOCBLOC",op=1,sd_prod=toto,
                TITI  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                TUTU  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                TATA  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                TOTO  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                b_unit1  =BLOC(condition = "TITI =='AAA'",
                               TOTO1  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                               c_unit1       =BLOC(condition = "TOTO1 == 'AAA'", UNITE1   =SIMP(statut='f',typ='I',defaut=25),),
                              ),
                b_unit2  =BLOC(condition = "TUTU =='AAA'",
                               TOTO2  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                               c_unit2       =BLOC(condition = "TOTO2 == 'BBB'", UNITE2   =SIMP(statut='f',typ='I',defaut=25),),
                              ),
                b_unit3  =BLOC(condition = "TATA =='BBB'",
                               TOTO3  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                               c_unit3       =BLOC(condition = "TOTO3 == 'BBB'", UNITE3   =SIMP(statut='f',typ='I',defaut=25),),
                              ),
                b_unit4  =BLOC(condition = "TOTO =='BBB'",
                               TOTO4  =SIMP(statut='f',typ='TXM',defaut='AAA',into=('AAA','BBB'),),
                               c_unit4       =BLOC(condition = "TOTO4 == 'AAA'", UNITE4   =SIMP(statut='f',typ='I',defaut=25),),
                              ),
             )

CARDFACT=OPER(nom="CARDFACT",op=1,sd_prod=toto,reentrant='f',
              A=FACT(F=SIMP(typ='TXM')),
              B=FACT(statut='f',F=SIMP(typ='TXM')),
              C=FACT(statut='o',F=SIMP(typ='TXM')),
              D=FACT(statut='f',min=3,max=5,F=SIMP(typ='TXM')),
              E=FACT(statut='o',min=3,max=5,F=SIMP(typ='TXM')),
              F=FACT(statut='o',min=3,max=5,F=SIMP(statut='o',typ='TXM')),
              TOTO=SIMP(typ='TXM'),
              bl=BLOC(condition="TOTO=='a'",
                      DD=FACT(statut='f',min=3,max=5,F=SIMP(typ='TXM')),
                      DE=FACT(statut='o',min=3,max=5,F=SIMP(typ='TXM')),
                      DF=FACT(statut='o',min=3,max=5,F=SIMP(statut='o',typ='TXM')),
                     ),
              bl2=BLOC(condition="reuse",
                      ED=FACT(statut='f',min=3,max=5,F=SIMP(typ='TXM')),
                      EE=FACT(statut='o',min=3,max=5,F=SIMP(typ='TXM')),
                      EF=FACT(statut='o',min=3,max=5,F=SIMP(statut='o',typ='TXM')),
                     ),
              X=FACT(statut='f',min=3,max=5,F=FACT(max=3,X=SIMP(typ='TXM'),
                                                   Y=FACT(max=3,Z=SIMP(typ='TXM'),),
                                                  ),
                    ),
	     )

#& MODIF COMMANDE  DATE 21/03/2003   AUTEUR ASSIRE A.ASSIRE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
POURSUITE=MACRO(nom="POURSUITE",op=ops.build_poursuite,repetable='n',fr="Poursuite d une étude",
                docu="U4.11.03-g",sd_prod = ops.POURSUITE,
            UIinfo={"groupes":("Gestion du travail",)},
                op_init = ops.POURSUITE_context,fichier_ini = 1,
         PAR_LOT         =SIMP(fr="mode de traitement des commandes",statut='f',typ='TXM',
                           into=("OUI","NON"),defaut="OUI"),
         BASE            =FACT(fr="définition des parmètres associés aux bases JEVEUX",
                               statut='f',min=1,max=3,
           FICHIER         =SIMP(fr="nom de la base",statut='o',typ='TXM'),
           TITRE           =SIMP(statut='f',typ='TXM'),
           CAS             =SIMP(statut='f',typ='TXM'),
           NMAX_ENRE       =SIMP(fr="nombre maximum d enregistrements",statut='f',typ='I'),
           LONG_ENRE       =SIMP(fr="longueur des enregistrements",statut='f',typ='I'),
           LONG_REPE       =SIMP(fr="longueur du répertoire",statut='f',typ='I'),
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
         DEBUG           =FACT(fr="option de déboggage reservée aux développeurs",
                               statut='f',min=1,max=1,
           JXVERI          =SIMP(fr="vérifie l intégrité de la segmentation mémoire",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           JEVEUX          =SIMP(fr="force les déchargement sur disque",
                                 statut='f',typ='TXM',into=('OUI','NON'),defaut='NON'),
           ENVIMA          =SIMP(fr="imprime les valeurs définies dans ENVIMA",
                                 statut='f',typ='TXM',into=('TES',)),
         ),
         MEMOIRE         =FACT(fr="mode de gestion mémoire utilisé",statut='f',min=1,max=1,
           GESTION         =SIMP(statut='f',typ='TXM',into=('COMPACTE','RAPIDE'),defaut='RAPIDE'),
           TYPE_ALLOCATION =SIMP(statut='f',typ='I',into=(1,2,3,4),defaut=1),
           TAILLE          =SIMP(statut='f',typ='I'),
           TAILLE_BLOC     =SIMP(statut='f',typ='R',defaut=800.),
           PARTITION       =SIMP(statut='f',typ='R' ),
         ),
         CODE            =FACT("définition d un nom pour l'esemble d'une étude",
                               statut='f',min=1,max=1,
           NOM             =SIMP(statut='o',typ='TXM'),
           UNITE           =SIMP(statut='f',typ='I',defaut=15),
         ),
)  ;
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
# ======================================================================
FIN=PROC(nom="FIN",op=9999,repetable='n',fr="Fin d'une étude",
         docu="U4.11.02-g",
            UIinfo={"groupes":("Gestion du travail",)},
         RETASSAGE       =SIMP(fr="provoque le retassage de la base GLOBALE",
                               statut='f',typ='TXM',defaut="NON",into=("OUI","NON",) ),
         PERFORMANCE     =SIMP(fr="provoque l'impression d'un résumé des mesures de temps ",
                               statut='f',typ='TXM',defaut="OUI",into=("OUI","NON",) ),
         INFO_RESU       =SIMP(fr="provoque l'impression des informations sur les structures de données",
                               statut='f',typ='TXM',defaut="OUI",into=("OUI","NON",) ),
         FICHIER         =SIMP(statut='f',typ='TXM',defaut="MESSAGE"),
)  ;

#FORMULE = FORM( nom='FORMULE',op=ops.build_formule,sd_prod=formule,
#                docu="U4.31.05-e",
#                fr="Définition d une fonction",reentrant = 'n',
#                regles=(UN_PARMI('REEL','COMPLEXE'),),

##### fonctions entieres interdites suite au probleme AL2003-072
#####           regles=(UN_PARMI('REEL','ENTIER','COMPLEXE'),),
#####           ENTIER   = SIMP(typ = 'shell',),

#                REEL     = SIMP(typ = 'shell',),
#                COMPLEXE = SIMP(typ = 'shell',),
#) ;

DETRUIRE=PROC(nom="DETRUIRE",op=-7,docu="U4.14.01-e",
            UIinfo={"groupes":("Gestion du travail",)},
              fr="Destruction d un concept utilisateur dans la base GLOBALE",
             op_init=ops.detruire,
             regles=(UN_PARMI('CONCEPT','OBJET',),),
            CONCEPT     =FACT(statut='f',
                NOM         =SIMP(statut='o',typ=assd,validators=NoRepeat(),max='**'),
            ),
            OBJET  =FACT(statut='f',
               CHAINE      =SIMP(statut='o',typ='TXM',validators=NoRepeat(),max='**'),
               POSITION    =SIMP(statut='o',typ='I'  ,validators=NoRepeat(),max='**'),
            ),
            INFO          =SIMP(statut='f',typ='I',into=(1,2),defaut=2, ),
);

