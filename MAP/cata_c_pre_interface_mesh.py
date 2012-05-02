
from Accas import *

JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
C_PRE_INTERFACE_MESH_DATA=PROC(nom='C_PRE_INTERFACE_MESH_DATA',op=None,
surface_type=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_surf=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
nb_segments=SIMP(typ='I',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_surface_field_csv_file_name=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_mesh=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_surface_field_csv_metadata_file_name=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)

# This text should be dump into a file named 'map_cata.py' to be
# copied in the eficas directory $EFICAS_ROOT/MAP/.
# Then run 'qtEficas_map.py -s maquettemap'. The key name
# maquettemap is the name defined in prefs_MAP.py
