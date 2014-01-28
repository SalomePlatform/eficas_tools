from Accas import *

class source(ASSD):
   pass

class conducteur(ASSD):
   pass

class nocond(ASSD):
   pass

class vcut(ASSD):
   pass

JdC = JDC_CATA (code = 'monCode',
                execmodul = None,
                regles=(AU_MOINS_UN('DONNEES_GENE','SOURCE','NOCOND','PARAMETRES'),
                         A_CLASSER('DONNEES_GENE',('SOURCE','NOCOND','PARAMETRES')),)
               )
                
# ======================================================================
# ======================================================================
#INCLUDE = MACRO ( nom = "INCLUDE", op = None,
#DONNEES_GENE=MACRO(nom='DONNEES_GENE',op=None,
#                UIinfo = { "groupes" : ( "iii", ) },
#                sd_prod = opsCarmelCND.INCLUDE,
#                fichier_ini = 1,

#          mesh_file_name=SIMP(typ=('Fichier', 'All Files (*.med)'),fr= "No comment",ang= "No comment",statut= "o",),
#)


SOURCE=OPER(nom='SOURCE',op=None,sd_prod=source,
            NomDomaine=SIMP(statut='o',typ='TXM',defaut="default"),
            VecteurDirecteur=SIMP(statut='o',typ='R',min=3,max=3),
            Centre=SIMP(statut='o',typ='R',min=3,max=3),
            SectionDomaine=SIMP(statut='o',typ='R',),
            Amplitude=SIMP(statut='o',typ='R',),
            NbdeTours=SIMP(statut='o',typ='I',val_min=1),
)

CONDUCTEUR=OPER(nom='CONDUCTEUR',op=None,sd_prod=conducteur,
                Conductivite=SIMP(statut='o',typ='R',),
                Permeabilite=SIMP(statut='o',typ='R',),
)
NOCOND=OPER(nom='NOCOND',op=None,sd_prod=nocond,
            Permeabilite=SIMP(statut='o',typ='R',),
)
#
VCUT=OPER(nom='VCUT',op=None,sd_prod=vcut,
            Orientation=SIMP(statut='o',typ='TXM',into=("Oppose","Meme sens")),
)
PARAMETRES=PROC(nom='PARAMETRES',op=None,
             RepCarmel=SIMP(typ='Repertoire',fr= "Repertoire Carmel",ang= "Carmel Directory",statut= "o",),
             TypedeFormule=SIMP(statut='o',typ='TXM',into=("TOMEGA","APHI")),
             Frequence_en_Hz=SIMP(statut='o',typ='I',fr="frequence en hz",ang="frequence en hz"),
             Nb_Max_Iterations=SIMP(statut='o',typ='I',val_min=1,val_max=10000,defaut=10000),
             Erreur_Max=SIMP(statut='o',typ='R',defaut=1E-9),
)
