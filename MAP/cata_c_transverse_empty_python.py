
from Accas import *

JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
C_TRANSVERSE_EMPTY_PYTHON_DATA=PROC(nom='C_TRANSVERSE_EMPTY_PYTHON_DATA',op=None,
file_output=SIMP(typ='TXM',fr='',ang='name of the output file of the component',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
an_integer=SIMP(typ='I',fr='',ang='number of lines in the output file',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
a_float=SIMP(typ='R',fr='',ang='simply print in verbose mode',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
a_string=SIMP(typ='TXM',fr='',ang='simply print in verbose mode',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)

# This text should be dump into a file named 'map_cata.py' to be
# copied in the eficas directory $EFICAS_ROOT/MAP/.
# Then run 'qtEficas_map.py -s maquettemap'. The key name
# maquettemap is the name defined in prefs_MAP.py
