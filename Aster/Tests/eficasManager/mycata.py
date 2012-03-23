
from Accas import *

JdC = JDC_CATA (code = 'DEMO_AUS20120329',
                execmodul = None,
                )
S_TEST02_PARAM=PROC(nom='S_TEST02_PARAM',op=None,
v=SIMP(typ='TXM',fr='',ang='',statut='o',docu='',into=['1', '2'],min=1,max=1,val_min='**',val_max='**',defaut=None),
)
S_TEST02_DATA=PROC(nom='S_TEST02_DATA',op=None,
y=SIMP(typ='R',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
x=SIMP(typ='R',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
z=SIMP(typ='I',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)

# This text should be dump into a file named 'map_cata.py' to be
# copied in the eficas directory $EFICAS_ROOT/MAP/.
# Then run 'qtEficas_map.py -s maquettemap'. The key name
# maquettemap is the name defined in prefs_MAP.py

