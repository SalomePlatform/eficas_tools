from Accas import *

class source(ASSD):
   pass

class conducteur(ASSD):
   pass

class nocond(ASSD):
   pass

class vcut(ASSD):
   pass

class zs(ASSD):
   pass

JdC = JDC_CATA (code = 'monCode',
                execmodul = None,
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


SOURCE=OPER(nom='SOURCE',op=None,sd_prod=source,UIinfo = { "groupes" : ( "CACHE", ) },
            EnveloppeConnexeInducteur=SIMP(statut='o',typ='TXM',defaut="default"),
            VecteurDirecteur=SIMP(statut='o',typ='R',min=3,max=3,defaut=(0,0,1)),
            Centre=SIMP(statut='o',typ='R',min=3,max=3),
            SectionBobine=SIMP(statut='o',typ='R',fr='en m2',ang='en m2'),
            Amplitude=SIMP(statut='o',typ='R',fr='en A',ang='en A'),
            NbdeTours=SIMP(statut='o',typ='I',val_min=1),
)

CONDUCTEUR=OPER(nom='CONDUCTEUR',op=None,sd_prod=conducteur,UIinfo = { "groupes" : ( "CACHE", ) },
                Conductivite=SIMP(statut='o',typ='R',fr='en S/m',ang='en S/m'),
                PermeabiliteRelative=SIMP(statut='o',typ='R',),
)
NOCOND=OPER(nom='NOCOND',op=None,sd_prod=nocond,UIinfo = { "groupes" : ( "CACHE", ) },
            PermeabiliteRelative=SIMP(statut='o',typ='R',),
)
#
VCUT=OPER(nom='VCUT',op=None,sd_prod=vcut,UIinfo = { "groupes" : ( "CACHE", ) },
            Orientation=SIMP(statut='o',typ='TXM',into=("Oppose","Meme sens"),defaut="Oppose"),
)
ZS=OPER(nom='ZS',op=None,sd_prod=zs,UIinfo = { "groupes" : ( "CACHE", ) },
                Conductivite=SIMP(statut='o',typ='R',),
                PermeabiliteRelative=SIMP(statut='o',typ='R',),
)
PARAMETRES=PROC(nom='PARAMETRES',op=None, UIinfo = { "groupes" : ( "CACHE", ) },
             RepCarmel=SIMP(typ='Repertoire',fr= "Repertoire Carmel",ang= "Carmel Directory",statut= "o",defaut="/projets/projets.002/carmel3d.001/frequentiel/V_240/Compil"),
             TypedeFormule=SIMP(statut='o',typ='TXM',into=("TOMEGA","APHI")),
             Frequence=SIMP(statut='o',typ='I',fr="en Hz",ang="en Hz"),
             Nb_Max_Iterations=SIMP(statut='o',typ='I',val_min=1,val_max=10000,defaut=10000),
             Erreur_Max=SIMP(statut='o',typ='R',defaut=1E-9),
)
