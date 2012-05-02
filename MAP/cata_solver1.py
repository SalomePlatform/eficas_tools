
from Accas import *

JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
SOLVER1_DATA=PROC(nom='SOLVER1_DATA',op=None,
e1=SIMP(typ='R',fr='',ang='The first data',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
e3=SIMP(typ='R',fr='',ang='The second data',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
e2=SIMP(typ='R',fr='',ang='The second data',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)

# This text should be dump into a file named 'map_cata.py' to be
# copied in the eficas directory $EFICAS_ROOT/MAP/.
# Then run 'qtEficas_map.py -s maquettemap'. The key name
# maquettemap is the name defined in prefs_MAP.py
