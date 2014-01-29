from Accas import *

JdC = JDC_CATA (code = 'ZCrack',
                execmodul = None,
                )

class grma(GEOM):
  pass

class grno(GEOM):
  pass

FILES = PROC(nom='FILES',op=None,
  crack_name=SIMP(typ=('Fichier', 'Med Files(med);;All Files (*)',),fr= "",ang= "Name of the crack surface mesh",statut= "o"),
  sane_name=SIMP(typ=('Fichier', 'Med Files(med);;All Files (*)'),fr= "",ang= "Name of the initial uncracked mesh",statut= "o"),
  cracked_name=SIMP(typ=('Fichier', 'Med Files(med);;All Files (*)'),fr= "",ang= "Name of the final mesh",statut= "o"),
)
PRESERVATION = PROC(nom='PRESERVATION',op=None,
 elset_names=SIMP(typ=grma,fr="",ang="names of volume element groups to be kept",min=1,max="**",statut="f"),
 faset_names=SIMP(typ=grma,fr="",ang="names of surface element groups to be kept",min=1,max="**",statut="f"),
 liset_names=SIMP(typ=grma,fr="",ang="names of line element groups to be kept",min=1,max="**",statut="f"),
 nset_names=SIMP(typ=grno,fr="" ,ang="names of node element groups to be kept",min=1,max="**",statut="f"),
)
REMESHING=PROC(nom='REMESHING',op=None,
 gradation=SIMP(typ="R",fr="",ang="gradation remeshing parameter",val_max=2.3,defaut=1.3,statut='o'),
 min_size=SIMP(typ="R",fr="",ang="minimal element edges length",statut='o'),
 max_size=SIMP(typ="R",fr="",ang="maximal element edges length",statut='o'),
 nb_iter=SIMP(typ="I",fr="",ang="number of iterations for remeshing process",defaut=2,statut='o'),
 if_quad=SIMP(typ="I",fr="",ang="1 for quadratic mesh",defaut=0,statut='o',into=[0,1]),
  
 REMESHING_ADVANCED=FACT(statut="f",
 yams_options=SIMP(typ='TXM',fr="",ang="parameters for yams command line",statut="f"),
 filter_tol=SIMP(typ="R",fr="",ang="filtering tolerance for meshing operations",defaut=1.e-6,statut="f"),
 grid_max=SIMP(typ="R",fr="",ang="truncation number for meshing operations",defaut=1.e11,statut="f"),
 nb_velem=SIMP(typ="I",fr="",ang="number of element layers which size should be fixed to min_size",defaut=3,statut='f'),
 if_barsoum=SIMP(typ="I",fr="",ang="element barsoum",defaut=1,statut='f',into=[0,1]),

)
)
  
