
from Accas import *

JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
C_POST_TABLE_FFT_DATA=PROC(nom='C_POST_TABLE_FFT_DATA',op=None,
output_spectr_y_png_file_name=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_surface_grid_field_csv_metadata_file_name=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_spectr_x_png_file_name=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
show_image=SIMP(typ='BOOL',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=True),
output_surface_grid_field_png_file_name=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_surface_properties_file_name=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
show_spectr=SIMP(typ='BOOL',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=True),
input_surface_grid_field_csv_file_name=SIMP(typ='TXM',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
interactive=SIMP(typ='BOOL',fr='',ang='NO COMMENT',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=False),
)

# This text should be dump into a file named 'map_cata.py' to be
# copied in the eficas directory $EFICAS_ROOT/MAP/.
# Then run 'qtEficas_map.py -s maquettemap'. The key name
# maquettemap is the name defined in prefs_MAP.py
