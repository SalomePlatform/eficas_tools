# debut entete

import Accas
from Accas import *

import ops

JdC = JDC_CATA(code='SATURNE',
               execmodul=None,
               regles = (AU_MOINS_UN('DEBUT','POURSUITE'),
                         AU_MOINS_UN('FIN'),
                         A_CLASSER(('DEBUT','POURSUITE'),'FIN')
                        )
              )

# P. RASCLE MMN
# remarques diverses sur le catalogue Saturne
# - dans les blocs, il faut au moins un mot clé de statut obligatoire
# probleme de rafraichissement des blocs dépendants quand la valeur d'un mot cle global (ITURB) passe de 1 à 0

# Type le plus general
class entier  (ASSD):pass
class reel    (ASSD):pass
class complexe(ASSD):pass
class liste   (ASSD):pass
class chaine  (ASSD):pass


class sonde(ASSD):pass
class varsca(ASSD):pass
class flusca(ASSD):pass
class varpre(ASSD):pass
class varvitx(ASSD):pass
class varvity(ASSD):pass
class varvitz(ASSD):pass
class eturb(ASSD):pass
class dturb(ASSD):pass
class tsr11(ASSD):pass
class tsr22(ASSD):pass
class tsr33(ASSD):pass
class tsr12(ASSD):pass
class tsr13(ASSD):pass
class tsr23(ASSD):pass
class resti(ASSD):pass

class maillage(ASSD):pass
class modele(ASSD):pass
class matr_asse(ASSD):pass
class cham_elem_sief_r(ASSD):pass
class theta_geom(ASSD):pass
class cham_mater(ASSD):pass
class cara_elem(ASSD):pass
class char_ther(ASSD):pass
class char_meca(ASSD):pass
class nume_ddl(ASSD):pass
class char_acou(ASSD):pass
class listr8 (ASSD):pass
class matr_elem(ASSD):pass
class matr_elem_depl_c(matr_elem):pass
class matr_elem_depl_r(matr_elem):pass
class matr_elem_pres_c(matr_elem):pass
class matr_elem_temp_r(matr_elem):pass

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


# fin entete

INCLUDE=MACRO(nom="INCLUDE",op=-1,docu="U4.13.01-e",
             fr="Débranchement vers un fichier de commandes secondaires",
             sd_prod=ops.INCLUDE,op_init=ops.INCLUDE_context,fichier_ini=1,
         UNITE = SIMP(statut='o',typ='I'),
         INFO  = SIMP(statut='f',typ='I',defaut=1,into=(1,2)),
);

POURSUITE=MACRO(nom="POURSUITE",op=0,repetable='n',fr="Poursuite d une étude",
                docu="U4.11.03-f1",sd_prod = ops.POURSUITE,
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

FORMULE = FORM( nom='FORMULE',op=-5,sd_prod=fonction,
                fr="Définition d une fonction",reentrant = 'n',
                regles=(UN_PARMI('REEL','ENTIER','COMPLEXE'),),
                REEL = SIMP(typ = 'shell',max=1),
                ENTIER = SIMP(typ = 'shell',max=1),
                COMPLEXE = SIMP(typ = 'shell',max=1),
) ;

AFFE_MODELE=OPER(nom="AFFE_MODELE",op=18,sd_prod=modele,docu="U4.41.01-f1",
                 fr="Affectation des éléments finis sur le maillage",reentrant='n',
         MAILLAGE        =SIMP(statut='o',typ=(maillage) ),
         INFO            =SIMP(statut='f',typ='I',defaut=1,into=(1,2) ),
         VERIF           =SIMP(statut='f',typ='TXM',max=2,into=("MAILLE","NOEUD") ),
                );
NUME_DDL=OPER(nom="NUME_DDL",op=11,sd_prod=nume_ddl,docu="U4.61.11-f",reentrant='n',
              fr="Etablissement de la numérotation des ddl avec ou sans renumérotation et du stockage de la matrice",
         MATR_RIGI       =SIMP(statut='f',typ=(matr_elem_depl_r ,matr_elem_depl_c,
                                               matr_elem_temp_r,matr_elem_pres_c),max=100 ),
         MODELE          =SIMP(statut='f',typ=modele ),
         b_modele        =BLOC(condition = "MODELE != None",
           CHARGE     =SIMP(statut='f',max='**',typ=(char_meca,char_ther,char_acou, ),),
         ),
         METHODE         =SIMP(statut='f',typ='TXM',defaut="MULT_FRONT",into=("MULT_FRONT","LDLT","GCPC") ),
         b_mult_front    =BLOC(condition="METHODE=='MULT_FRONT'",fr="paramètres associés à la méthode multifrontale",
           RENUM           =SIMP(statut='f',typ='TXM',into=("MD","MDA","METIS"),defaut="METIS" ),
         ),
         b_ldlt          =BLOC(condition="METHODE=='LDLT'",fr="paramètres associés à la méthode LDLT",
           RENUM           =SIMP(statut='f',typ='TXM',into=("RCMK","SANS"),defaut="RCMK"  ),
         ),
         b_gcpc          =BLOC(condition="METHODE=='GCPC'",fr="paramètres associés à la méthode gradient conjugué",
           RENUM           =SIMP(statut='f',typ='TXM',into=("RCMK","SANS"),defaut="RCMK"  ),
         ),
         INFO            =SIMP(statut='f',typ='I',into=(1,2)),
)  ;

DEFI_SONDE = OPER(nom="DEFI_SONDE",op= 1,sd_prod=sonde,
     docu="U2D1",
     fr="définition d'une sonde historique avec ses coordonnées",
                  X = SIMP(statut ='o',typ='R',
                           fr="coordonnée X de la sonde"),
                  Y = SIMP(statut ='o',typ='R',
                           fr="coordonnée Y de la sonde"),
                  Z = SIMP(statut ='o',typ='R',
                           fr="coordonnée Z de la sonde")
                 );

def defi_scala_prod(**args):
   return varsca

DEFI_SCALA = OPER(nom="DEFI_SCALA",op=2,sd_prod=defi_scala_prod,
fr="définition d'une inconnue scalaire avec ses paramètres physico numériques",
                  NUMERIC = FACT(statut='o',max=01,
                                fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                 );

DEFI_FLUSCA = OPER(nom="DEFI_FLUSCA",op=2,sd_prod=flusca,fr="définition des fluctuations d'une inconnue scalaire avec ses paramètres physico numériques",
                  VARFL  = SIMP(statut='o',typ=varsca,fr="scalaire associé au calcul de la variance des fluctuations"),
                  NUMERIC = FACT(statut='o',max=01,
                                fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable"),
                                RVARFL = SIMP(statut='o',typ='R',val_min=0,defaut=0.8,
                                                       fr="nombre de Prandtl pour la variance des fluctuations du scalaire")
                                )
                  );

DEFI_PRESSION = OPER(nom="DEFI_PRESSION",op=2,sd_prod=varpre,fr="définition del'inconnue pression avec ses paramètres physico numériques",
                   NUMERIC = FACT(statut='o',max=01,
                                  fr="propriétés de l'équation de pression",
                                  ICONV  = SIMP(statut='o',typ='I',defaut=0,into=(0,1),
                                                fr="indicateur de convection"),
                                  ISTAT  = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                fr="présence terme instationnaire dans les matrices"),
                                  IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="diffusion"),
                                  IDIRCL = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                  SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                          BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                        fr="pourcentage schéma convectif au second ordre"),
                                                          ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                        fr ="type schéma convectif au second ordre 1 : centré")
                                                          ),
                                  NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                  EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                fr="précision relative pour la résolution des systèmes linéaires"),
                                  IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                fr="type de limitation des gradients"),
                                  NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                fr="reconstruction des gradients"),
                                  NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                  CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                fr="facteur de limitation des gradients"),
                                  EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                fr="précision relative pour la reconstruction itérative des gradients")
                                  ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée",
                                                defaut="Pression"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour la grandeur"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour la grandeur"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour la grandeur"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée à la grandeur"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                    );

DEFI_VITX = OPER(nom="DEFI_VITX",op=2,sd_prod=varvitx,fr="définition de l'inconnue vitesse X avec ses paramètres physico numériques",
                   NUMERIC = FACT(statut='o',max=01,
                                  fr="propriétés de l'équation de vitesse X",
                                  ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                fr="indicateur de convection"),
                                  ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="présence terme instationnaire dans les matrices"),
                                  IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="diffusion"),
                                  IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                  SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                          BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                        fr="pourcentage schéma convectif au second ordre"),
                                                          ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                        fr ="type schéma convectif au second ordre 1 : centré")
                                                          ),
                                  NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                  EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                fr="précision relative pour la résolution des systèmes linéaires"),
                                  IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                fr="type de limitation des gradients"),
                                  NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                fr="reconstruction des gradients"),
                                  NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                  CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                fr="facteur de limitation des gradients"),
                                  EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                fr="précision relative pour la reconstruction itérative des gradients")
                                  ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée",
                                                defaut="vitesse_u1"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour la grandeur"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour la grandeur"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour la grandeur"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée à la grandeur"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                );

DEFI_VITY = OPER(nom="DEFI_VITY",op=2,sd_prod=varvity,fr="définition de l'inconnue vitesse Y avec ses paramètres physico numériques",
                   NUMERIC = FACT(statut='o',max=01,
                                  fr="propriétés de l'équation de vitesse Y",
                                  ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                fr="indicateur de convection"),
                                  ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="présence terme instationnaire dans les matrices"),
                                  IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="diffusion"),
                                  IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                  SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                          BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                        fr="pourcentage schéma convectif au second ordre"),
                                                          ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                        fr ="type schéma convectif au second ordre 1 : centré")
                                                          ),
                                  NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                  EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                fr="précision relative pour la résolution des systèmes linéaires"),
                                  IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                fr="type de limitation des gradients"),
                                  NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                fr="reconstruction des gradients"),
                                  NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                  CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                fr="facteur de limitation des gradients"),
                                  EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                fr="précision relative pour la reconstruction itérative des gradients")
                                  ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée",
                                                defaut="vitesse_v1"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour la grandeur"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour la grandeur"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour la grandeur"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée à la grandeur"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                );

DEFI_VITZ = OPER(nom="DEFI_VITZ",op=2,sd_prod=varvitz,fr="définition de l'inconnue vitesse Z avec ses paramètres physico numériques",
                   NUMERIC = FACT(statut='o',max=01,
                                  fr="propriétés de l'équation de vitesse Z",
                                  ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                fr="indicateur de convection"),
                                  ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="présence terme instationnaire dans les matrices"),
                                  IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="diffusion"),
                                  IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                  SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                          BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                        fr="pourcentage schéma convectif au second ordre"),
                                                          ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                        fr ="type schéma convectif au second ordre 1 : centré")
                                                          ),
                                  NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                  EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                fr="précision relative pour la résolution des systèmes linéaires"),
                                  IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                fr="type de limitation des gradients"),
                                  NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                fr="reconstruction des gradients"),
                                  NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                  CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                fr="facteur de limitation des gradients"),
                                  EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                fr="précision relative pour la reconstruction itérative des gradients")
                                  ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée",
                                                defaut="vitesse_w1"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour la grandeur"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour la grandeur"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour la grandeur"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée à la grandeur"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable"),
                                )
                );


DEFI_ETURB = OPER(nom="DEFI_ETURB",op=2,sd_prod=eturb,fr="définition de l'inconnue energie turbulente k-eps avec ses paramètres physico numériques",
                  NUMERIC = FACT(statut='o',max=01,
                                    fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                 );

DEFI_DTURB = OPER(nom="DEFI_DTURB",op=2,sd_prod=dturb,fr="définition de l'inconnue dissipation turbulente k-eps avec ses paramètres physico numériques",
                  NUMERIC = FACT(statut='o',max=01,
                                fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                 );

DEFI_TSR11 = OPER(nom="DEFI_TSR11",op=2,sd_prod=tsr11,fr="définition de l'inconnue tension Reynolds R11 Rij-eps avec ses paramètres physico numériques",
                  NUMERIC = FACT(statut='o',max=01,
                                fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                 );

DEFI_TSR22 = OPER(nom="DEFI_TSR22",op=2,sd_prod=tsr11,fr="définition de l'inconnue tension Reynolds R22 Rij-eps avec ses paramètres physico numériques",
                  NUMERIC = FACT(statut='o',max=01,
                                fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                 );

DEFI_TSR33 = OPER(nom="DEFI_TSR33",op=2,sd_prod=tsr11,fr="définition de l'inconnue tension Reynolds R33 Rij-eps avec ses paramètres physico numériques",
                  NUMERIC = FACT(statut='o',max=01,
                                fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                 );

DEFI_TSR12 = OPER(nom="DEFI_TSR12",op=2,sd_prod=tsr11,fr="définition de l'inconnue tension Reynolds R12 Rij-eps avec ses paramètres physico numériques",
                  NUMERIC = FACT(statut='o',max=01,
                                fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                 );

DEFI_TSR13 = OPER(nom="DEFI_TSR13",op=2,sd_prod=tsr11,fr="définition de l'inconnue tension Reynolds R13 Rij-eps avec ses paramètres physico numériques",
                  NUMERIC = FACT(statut='o',max=01,
                                fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                 );

DEFI_TSR23 = OPER(nom="DEFI_TSR23",op=2,sd_prod=tsr11,fr="définition de l'inconnue tension Reynolds R23 Rij-eps avec ses paramètres physico numériques",
                  NUMERIC = FACT(statut='o',max=01,
                                fr="propriétés numériques liées à l'inconnue",
                                    ICONV  = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                  fr="indicateur de convection"),
                                    ISTAT  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="présence terme instationnaire dans les matrices"),
                                    IDIFF  = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="diffusion"),
                                    IDIRCL = SIMP(statut='f',typ='I',defaut=1,into=(0,1),
                                                  fr="décalage du spectre des valeurs propres en l'absence de Dirichlet"),
                                    SCHEMA_CONVECTIF = BLOC(condition="ICONV == 1", fr ="ordre du schéma convectif",
                                                            BLENCV = SIMP(statut='o',typ='R',defaut=0,val_min=0,val_max=1,
                                                                          fr="pourcentage schéma convectif au second ordre"),
                                                            ISCHCV = SIMP(statut='f',typ='I',defaut=0,into=(0,1),
                                                                          fr ="type schéma convectif au second ordre 1 : centré")
                                                            ),
                                    NITMAX = SIMP(statut='f',typ='I',defaut=10000,val_min=0,
                                                  fr="nombre max d'itération pour la résolution des systèmes linéaires"),
                                    EPSILO = SIMP(statut='f',typ='R',defaut=1.e-4,val_min=0,
                                                  fr="précision relative pour la résolution des systèmes linéaires"),
                                    IMLIGR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,-1,0,1),
                                                  fr="type de limitation des gradients"),
                                    NSWRGR = SIMP(statut='f',typ='I',defaut=100,val_min=0,
                                                  fr="reconstruction des gradients"),
                                    NSWRSM = SIMP(statut='f',typ='I',defaut=2,val_min=0,
                                                  fr="nombre d'itérations pour la reconstruction des seconds membres"),
                                    CLIMGR = SIMP(statut='f',typ='R',defaut=1.5,val_min=0,
                                                  fr="facteur de limitation des gradients"),
                                    EPSRGR = SIMP(statut='f',typ='R',defaut=1.e-5,val_min=0,
                                                  fr="précision relative pour la reconstruction itérative des gradients")
                                 ),
                  RESTITUE = FACT(statut='o',max=01,
                                  fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                                  ),
                  MODELE = FACT(statut='o',max=01,
                                fr="modélisation",
                                VALREF = SIMP(statut='o',typ='R',fr="valeur de référence (température, masse volumique...)"),
                                SCAMIN = SIMP(statut='f',typ='R',defaut=1.e12,fr="valeur minimale pour le scalaire"),
                                SCAMAX = SIMP(statut='f',typ='R',defaut=-1.e12,fr="valeur maximale pour le scalaire"),
                                SIGMAS = SIMP(statut='f',typ='R',val_min=0,defaut=1,fr="nombre de Prandtl pour le scalaire"),
                                VISLS0 = SIMP(statut='o',typ='R',fr="valeur de référence de la viscosité associée au scalaire"),
                                IVISLS = SIMP(statut='f',typ='I',defaut=0,into=(0,1),fr="viscosité variable")
                                )
                 );


DEFI_RESTI = OPER(nom="DEFI_RESTI",op=2,sd_prod=resti,fr = "Description de la grandeur restituée",
                                  NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur restituée"),
                                  ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                  IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                fr = "inventaire des sondes utilisées pour la grandeur scalaire")
                  );

CALCUL_SATURNE = PROC(nom = "CALCUL_SATURNE",op = 1,
                      fr = "définition des paramètres généraux pour un calcul Saturne",
                      docu = "néant",reentrant = 'n',
        NomsBibliotheque   = NUPL ( max      = '**',
                                    statut   = 'o',
                                    elements = (  SIMP (typ='TXM',fr="Identificateur Procedure Bibliotheque"),
                                                  SIMP (typ='TXM',fr="Identifiant de l'isotope dans la bibliotheque")
                                               )
                                  ),
        ENVELOPPE = FACT(statut='o',max=01,fr = "gestion de l'enveloppe",
                         IFOENV = SIMP(statut='o',typ='I',defaut=2,into=(0,1,2),position='global',
                                       fr = "mode de communication enveloppe solveur"),
                         ENVTOSOLV = BLOC(condition="IFOENV > 0",
                                          fr = "liaison enveloppe vers solveur",
                                          IMPEVI = SIMP(statut='o',typ='I',defaut=13,val_min=0,val_max=99,
                                                        fr = "numéro de fichier enveloppe vers solveur"),
                                          FICEVI = SIMP(statut='o',typ='TXM',defaut="enveloppe_vers_solveur          ",
                                                        fr = "nom de fichier enveloppe vers solveur")
                                         ),
                         SOLVTOENV = BLOC(condition="IFOENV > 0",
                                          fr = "liaison solveur vers enveloppe",
                                          IMPEVO = SIMP(statut='o',typ='I',defaut=14,val_min=0,val_max=99,
                                                        fr = "numéro de fichier solveur vers enveloppe"),
                                          FICEVO = SIMP(statut='o',typ='TXM',defaut="solveur_vers_enveloppe          ",
                                                        fr = "nom de fichier solveur vers enveloppe")
                                         )
                        ),
        FICHIERS_CALCUL = FACT(statut='f',max=01,
                               fr ="définition des fichiers géométrie, suite, stop",
                               GEOMETRIE = BLOC(condition="IFOENV == 0",
                                                fr = "fichier géométrique (pas d'enveloppe)",
                                                IMPGEO = SIMP(statut='o',typ='I',defaut=10,val_min=0,val_max=99,
                                                              fr = "numéro de fichier géométrique"),
                                                FICGEO = SIMP(statut='o',typ='TXM',defaut="geomet",
                                                              fr = "nom de fichier géométrique")
                                               ),
                               SUITE_AMONT = BLOC(condition="ISUITE == 1",
                                                  fr = "fichier suite amont",
                                                  IMPAMO = SIMP(statut='o',typ='I',defaut=11,val_min=0,val_max=99,
                                                              fr = "numéro de fichier suite amont"),
                                                  FICGEO = SIMP(statut='o',typ='TXM',defaut="suiamo",
                                                              fr = "nom de fichier suite amont"),
                                                  IFOAMO = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                              fr = "format du fichier suite amont, 0 = binaire")
                                                 ),
                               FICHIER_STOP = FACT(fr = "fichier stop",
                                                   IMPSTP = SIMP(statut='o',typ='I',defaut=12,val_min=0,val_max=99,
                                                                 fr = "numéro de fichier stop"),
                                                   FICSTP = SIMP(statut='o',typ='TXM',defaut="ficstp",
                                                                 fr = "nom de fichier stop")
                                                  ),
                               SUITE_AVAL = FACT(fr = "fichier suite aval",
                                                 IMPAVA = SIMP(statut='o',typ='I',defaut=20,val_min=0,val_max=99,
                                                             fr = "numéro de fichier suite aval"),
                                                 FICAVA = SIMP(statut='o',typ='TXM',defaut="suiamo",
                                                             fr = "nom de fichier suite aval"),
                                                 IFOAVA = SIMP(statut='o',typ='I',defaut=1,into=(0,1),
                                                             fr = "format du fichier suite aval, 0 = binaire")
                                                )
                              ),
        POST_PROC_ENSIGHT = FACT(statut='f',max=01,
                                 fr = "options de post processing par Ensight",
                                 IFOENS = SIMP(statut='f',typ='I',defaut=-2,into=(-2,-1,0,1),
                                               fr = "option type de fichier et processus générateur"),
                                 NTCHR  = SIMP(statut='f',typ='I',defaut=-1,
                                               fr = "périodicité de sortie des fichiers Ensight"),
                                 ITCHR  = SIMP(statut='f',typ='I',defaut=0,val_min=0,
                                               fr = "compteur des sorties des fichiers Ensight"),
                                 N3S_ASCII_NOY = BLOC(condition="(IFOENS == -1) and (IFOENV == 0)",
                                                      fr = "format Ensight N3S ASCII généré par le noyau",
                                                      IMPPST = SIMP(statut='o',typ='I',defaut=21,val_min=0,val_max=99,
                                                                    fr = "numéro de fichier Ensight"),
                                                      FICPST = SIMP(statut='o',typ='TXM',defaut="dessin",
                                                                    fr = "nom de fichier Ensight")
                                                      ),
                                 P0_NOY =        BLOC(condition="((IFOENS == 0) or (IFOENS == 1)) and (IFOENV == 0)",
                                                      fr = "format Ensight P0 généré par le noyau",
                                                      IMPEP0 = SIMP(statut='o',typ='I',defaut=22,val_min=0,val_max=99,
                                                                    fr = "numéro de fichier Ensight"),
                                                      EMPCHR = SIMP(statut='o',typ='TXM',defaut="./",
                                                                    fr = "répertoire de fichier Ensight"),
                                                      ENTCHR = SIMP(statut='o',typ='TXM',defaut="chr",
                                                                    fr = "préfixe nom de fichier Ensight")
                                                      )
                                ),
        HISTORIQUE_PONCTUEL = FACT(statut='o',max=01,
                                   fr = "Sondes historiques",
                                   FICHIERS_HISTORIQUES = FACT(statut='f',max=01,
                                                               fr = "description des fichiers historiques",
                                                               EMPHIS = SIMP(statut='o',typ='TXM',defaut="./",
                                                                             fr="répertoire fichiers historiques"),
                                                               EXTHIS = SIMP(statut='o',typ='TXM',defaut="hst",
                                                                             fr="extension fichiers historiques")
                                                               ),
                                   NTHIST = SIMP(statut='f',typ='I',defaut=-999,
                                                 fr="fréquence de sortie des historiques en pas de temps"),
                                   NTHSAV = SIMP(statut='f',typ='I',defaut=-999,
                                                 fr="fréquence de sauvegarde des historiques en pas de temps")
                                  ),
        OPTIONS_TURBULENCE = FACT(statut='o',max=01,
                                  fr="modèle de turbulence",
                                  ITURB  = SIMP(statut='f',fr="laminaire : 0, k-epsilon :1,Rij-epsilon :2",
                                                typ='I',into=(0,1,2),defaut=1,position='global'),
                                  MODTURB = BLOC(condition="ITURB == 1",
                                                 fr = "option k-epsilon",
                                                 IGRAKE = SIMP(statut='o',typ='I',
                                                               fr="prise en compte gravité dans k-epsilon",
                                                               into=(0,1),defaut=0),
                                                 IDEUCH = SIMP(statut='f',typ='I',
                                                               fr="prise en compte k-epsilon deux échelles",
                                                               into=(0,1),defaut=1),
                                                 IKEKOU = SIMP(statut='f',typ='I',
                                                               fr="prise en compte couplage en incréments sur k-epsilon",
                                                               into=(0,1),defaut=1)
                                                 ),
                                  TEMPTURB = BLOC(condition="ITURB == 1",
                                                  fr = "option k-epsilon",
                                                  ISCALT = SIMP(statut='o',typ=varsca,
                                                                fr=" identificateur inconnue scalaire température ")
                                                  )
                                  ),
        MARCHE_TEMPS = FACT(statut='o',max=01,
                            fr = "définition de la marche en temps",
                            DTREF  = SIMP(statut='o',fr="pas de temps de référence",
                                                        typ='R',val_min=0),
                            IDTVAR = SIMP(statut='f',fr="pas de temps constant : 0, variable temps espace : 1, variable temps : 2",
                                          typ='I',into=(0,1,2),defaut=0,position='global'),
                                  # probleme trace eficas quand un mot cle position global change
                            PASVAR = BLOC(condition="IDTVAR != 0",fr="options pas de temps variable",
                                          XCFMAX = SIMP(statut='o',fr="nombre de Courant-Fourier cible",
                                                        typ='R',defaut=0.5,val_min=0),
                                          FMIN =   SIMP(statut='f',fr="rapport min pas calculé DTREF",
                                                        typ='R',defaut=0.1,val_min=0),
                                          FMAX =   SIMP(statut='f',fr="rapport max pas calculé DTREF",
                                                        typ='R',defaut=1000,val_min=0),
                                          VARRDT = SIMP(statut='f',fr="variation relative max pas calculé entre deux instants",
                                                        typ='R',defaut=0.1,val_min=0)
                                          )
                            ),
        OPTIONS_EQUATIONS = FACT(statut='o',max=01,
                                   fr = "propriétés des équations, inconnues principales",
                                   IMGR   = SIMP(statut='f',fr="utilisation du multigrille pour la résolution des systèmes linéaires",
                                                 typ='I',into=(0,1),defaut=0),
                                   IMRGRA = SIMP(statut='f',fr="type de reconstruction des gradients 1 : moindres carrés",
                                                 typ='I',into=(0,1),defaut=0),
                                   ),
        VARIABLES = FACT(statut='o',max=01,
                         fr = "Restitution des grandeurs principales",
                         NTLIST = SIMP(statut='f',typ='I',defaut=1,val_min=1,val_max='**',
                                       fr = "fréquence de sortie (en pas de temps) dans le compte rendu d'éxécution"),
                         IWARNI = SIMP(statut='f',typ='I',defaut=2,val_min=0,val_max='**',
                                       fr = "niveau de détail des impressions dans le compte rendu d'éxécution"),
                         MASVOL1 = FACT(statut='o',max=01,
                                         fr = "Description de la grandeur restituée : masse volumique",
                                         NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur : masse volumique",
                                                       defaut="Masse_vol1"),
                                         ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                       fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                         ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                       fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                         IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                       fr = "inventaire des sondes utilisées pour la grandeur masse volumique")
                                        ),
                        TURB_KE = BLOC(condition="ITURB == 1",
                                       E_TURB = FACT(statut='o',max=01,
                                                     fr = "Description de la grandeur restituée : énergie turbulente",
                                                     NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur : energie turbulente",
                                                                   defaut="Energie_1"),
                                                     ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                                   fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                                     ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                                   fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                                     IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                                   fr = "inventaire des sondes utilisées pour la grandeur énergie turbulente")
                                                    ),
                                       D_TURB = FACT(statut='o',max=01,
                                                     fr = "Description de la grandeur restituée : dissipation turbulente",
                                                     NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur : dissipation turbulente",
                                                                   defaut="Dissipation"),
                                                     ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                                   fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                                     ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                                   fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                                     IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                                   fr = "inventaire des sondes utilisées pour la grandeur dissipation turbulente")
                                                    ),
                                       V_TURB = FACT(statut='o',max=01,
                                                     fr = "Description de la grandeur restituée : viscosité turbulente",
                                                     NOMVAR = SIMP(statut='o',typ='TXM',fr = "nom de la grandeur : viscosité turbulente",
                                                                   defaut="Visc_turb1"),
                                                     ICHRVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                                   fr = "post-traitement (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                                     ILISVR = SIMP(statut='f',typ='I',defaut=-999,into=(-999,0,1),
                                                                   fr = "impression dans CR exécution (-999 : le code décide ; 0 : non ; 1 : oui)"),
                                                     IHISVR = SIMP(statut='f',typ=sonde,min=0,max='**',
                                                                   fr = "inventaire des sondes utilisées pour la grandeur viscosité turbulente")
                                                    ),
                                      )
                        ),
        GESTION_CALCUL = FACT(statut='o',max=01,
                              fr = "calcul suite et numéros de pas de temps début et fin",
                              ISUITE = SIMP(statut='o',typ='I',defaut=0,into=(0,1),position='global',
                                            fr = "indicateur calcul suite (1 = suite)"),
                              NTPABS = SIMP(statut='f',typ='I',defaut=0,
                                            fr = "numéro dernier pas de temps calcul précédent (initialisation automatique)"),
                              NTMABS = SIMP(statut='o',typ='I',
                                            fr = "numéro dernier pas de temps visé (absolu)"),
                              TTPABS = SIMP(statut='f',typ='R',defaut=0,
                                            fr = "temps simulation au dernier pas de temps précédent (initialisation automatique)")
                             ),
        CONSTANTES_PHYSIQUES=FACT(statut='o',max=01,
                                  fr = "Grandeurs physiques et modélisation",
                                  GRAVITE = FACT(statut='o',max=01,
                                                 fr = "composantes de la gravité",
                                                 GX = SIMP(statut ='o',typ='R',defaut=0, fr = "gravité selon X"),
                                                 GY = SIMP(statut ='o',typ='R',defaut=0, fr = "gravité selon Y"),
                                                 GZ = SIMP(statut ='o',typ='R',defaut=0, fr = "gravité selon Z")
                                                 ),
                                  FLUIDE = FACT(statut='o',max=01,
                                                fr = "propriétés du fluide",
                                                RO0 = SIMP(statut ='o',typ='R',val_min=0,fr="masse volumique de référence"),
                                                VISCL0 = SIMP(statut ='o',typ='R',val_min=0,fr="viscosité dynamique de référence"),
                                                P0 = SIMP(statut ='o',typ='R',val_min=0,fr="pression de référence")
                                                ),
                                  TURBULENCE = BLOC(condition="ITURB >= 0",
                                                    XKAPPA = SIMP(statut ='o',typ='R',defaut=0.42,val_min=0,fr="constante de Karman"),
                                                    CSTLOG = SIMP(statut ='f',typ='R',defaut=5.2,val_min=0,fr="constante de la loi log"),
                                                    YPLULI = SIMP(statut ='f',typ='R',defaut=2/0.42,val_min=0,fr="valeur limite de y+ pour la sous couche visqueuse"),
                                                    CMU = SIMP(statut ='f',typ='R',defaut=0.009,val_min=0,fr="constante C mu"),
                                                    CE1 = SIMP(statut ='f',typ='R',defaut=1.44,val_min=0,fr="constante C epsilon 1"),
                                                    CE2 = SIMP(statut ='f',typ='R',defaut=1.92,val_min=0,fr="constante C epsilon 2"),
                                                    CE3 = SIMP(statut ='f',typ='R',defaut=1.0,val_min=0,fr="constante C epsilon 3"),
                                                    SIGMAK = SIMP(statut ='f',typ='R',defaut=1.0,val_min=0,fr="nombre de Prandtl pour k en k-epsilon"),
                                                    SIGMAE = SIMP(statut ='f',typ='R',defaut=1.3,val_min=0,fr="nombre de Prandtl pour epsilon en k-epsilon"),
                                                    ALMAX = SIMP(statut ='f',typ='R',val_min=0,fr="longueur macroscopique caractéristique du domaine"),
                                                    UREF = SIMP(statut ='f',typ='R',val_min=0,fr="vitesse caractéristique de l'écoulement pour l'initialisation du k-epsilon")
                                                    )
                                  )
                                 );

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

DEBUT=MACRO(nom="DEBUT",op=0 ,docu="U4.11.01-f1",repetable='n',
           fr="Ouverture d une étude. Allocation des ressources mémoire et disque",
          sd_prod=ops.DEBUT,

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

def macro2_prod(self,MODELE,**args):
   return maillage

MACRO2 =MACRO(nom="MACRO2",op= -5 ,docu="U4.61.21-c",
                      sd_prod=macro2_prod,
                      fr="Calcul des matrices assemblées (matr_asse_gd) par exemple de rigidité, de masse ",
         MODELE          =SIMP(statut='o',typ=modele),
);
