
from Accas import *

JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
S_SCC_3D_ANALYSIS_DATA=PROC(nom='S_SCC_3D_ANALYSIS_DATA',op=None,
direction=SIMP(typ='I',fr='',ang='The direction type',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
alt_min=SIMP(typ='I',fr='',ang='The minimum altitude',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
calculation=SIMP(typ='TXM',fr='',ang='The calculation type',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
alt_max=SIMP(typ='I',fr='',ang='The maximum altitude',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_grid_field_raw_metadata=SIMP(typ='TXM',fr='',ang='field metadata file',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_grid_field_raw=SIMP(typ='TXM',fr='',ang='field data file',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)

# This text should be dump into a file named 'map_cata.py' to be
# copied in the eficas directory $EFICAS_ROOT/MAP/.
# Then run 'qtEficas_map.py -s maquettemap'. The key name
# maquettemap is the name defined in prefs_MAP.py
