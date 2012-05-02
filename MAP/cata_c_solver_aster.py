
from Accas import *

JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
C_SOLVER_ASTER_DATA=PROC(nom='C_SOLVER_ASTER_DATA',op=None,
meshfile=SIMP(typ='TXM',fr='',ang='Geometry modelisation',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
commfile=SIMP(typ='TXM',fr='',ang='Code_Aster modelisation',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)

# This text should be dump into a file named 'map_cata.py' to be
# copied in the eficas directory $EFICAS_ROOT/MAP/.
# Then run 'qtEficas_map.py -s maquettemap'. The key name
# maquettemap is the name defined in prefs_MAP.py
