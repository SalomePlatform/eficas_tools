from Accas import *

JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
# ======================================================================
# Catalog entry for the MAP function : c_pre_interfaceBody_mesh
# ======================================================================
C_PRE_INTERFACEBODY_MESH_DATA=PROC(nom='C_PRE_INTERFACEBODY_MESH_DATA',op=None,
layer_1_height=SIMP(typ='R',fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
layer_2_height=SIMP(typ='R',fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_surface_mesh_file_name=SIMP(typ=('Fichier', 'All Files (*)'),fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
layer_3_height=SIMP(typ='R',fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_image_2d_align
# ======================================================================
C_IMAGE_2D_ALIGN_DATA=PROC(nom='C_IMAGE_2D_ALIGN_DATA',op=None,
shift=SIMP(typ='R',fr= "number of pixel each image is to be shifted from the previous one",ang= "number of pixel each image is to be shifted from the previous one",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
gui=SIMP(typ='TXM',fr= "Run the Graphical User Interface if set to True",ang= "Run the Graphical User Interface if set to True",statut= "f",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=False),
input_directory=SIMP(typ='Repertoire',fr= "directory where the input images are read",ang= "directory where the input images are read",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_directory=SIMP(typ='Repertoire',fr= "directory where the aligned images are to be written",ang= "directory where the aligned images are to be written",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_post_grid_field
# ======================================================================
C_POST_GRID_FIELD_DATA=PROC(nom='C_POST_GRID_FIELD_DATA',op=None,
second_strain_dat_file_name=SIMP(typ=('Fichier', 'All Files (*)'),fr= "second Stereo output file",ang= "second Stereo output file",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
prior_strain_dat_file_name=SIMP(typ=('Fichier', 'All Files (*)'),fr= "first Stereo output file",ang= "first Stereo output file",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
strain_path_beta=SIMP(typ='TXM',fr= "save the strain path beta",ang= "save the strain path beta",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
second_strain=SIMP(typ='TXM',fr= "save the second strain",ang= "save the second strain",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
histograms=SIMP(typ='TXM',fr= "save histograms",ang= "save histograms",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
peek=SIMP(typ='TXM',fr= "save the peek",ang= "save the peek",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
study_name=SIMP(typ='TXM',fr= "the name of your study",ang= "the name of your study",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
prior_strain=SIMP(typ='TXM',fr= "save the prior strain",ang= "save the prior strain",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
mesh_size_in_micron=SIMP(typ='R',fr= "grid mesh size in microns",ang= "grid mesh size in microns",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
oxydation_map=SIMP(typ='TXM',fr= "save the oxydation map",ang= "save the oxydation map",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
matlab=SIMP(typ='TXM',fr= "formatting output for matlab",ang= "formatting output for matlab",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
mesh_size_in_pixel=SIMP(typ='I',fr= "grid mesh size in pixels",ang= "grid mesh size in pixels",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
bin_number=SIMP(typ='I',fr= "number of bins in histogram",ang= "number of bins in histogram",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
accuracy=SIMP(typ='I',fr= "number of subdivision",ang= "number of subdivision",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_image_2d_threshold
# ======================================================================
C_IMAGE_2D_THRESHOLD_DATA=PROC(nom='C_IMAGE_2D_THRESHOLD_DATA',op=None,
gui=SIMP(typ='TXM',fr= "Run the Graphical User Interface if set to True",ang= "Run the Graphical User Interface if set to True",statut= "f",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=False),
image_name=SIMP(typ='TXM',fr= "pathname of the files of input images ; globing (wild card) is allowed",ang= "pathname of the files of input images ; globing (wild card) is allowed",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_directory=SIMP(typ='Repertoire',fr= "(optional, default : <current directory>/refs) path where each output file is written",ang= "(optional, default : <current directory>/refs) path where each output file is written",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
threshold_level=SIMP(typ='R',fr= "(optional if GUI is used, mandatory otherwise) Threshold level applied to each input image file",ang= "(optional if GUI is used, mandatory otherwise) Threshold level applied to each input image file",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_prefix=SIMP(typ='TXM',fr= "(optional, default : empty string) Prefix appended before the output file name",ang= "(optional, default : empty string) Prefix appended before the output file name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_suffix=SIMP(typ='TXM',fr= "(optional, default : empty string) Suffix appended after the output file name",ang= "(optional, default : empty string) Suffix appended after the output file name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_pre_random_experimental_design
# ======================================================================
C_PRE_RANDOM_EXPERIMENTAL_DESIGN_DATA=PROC(nom='C_PRE_RANDOM_EXPERIMENTAL_DESIGN_DATA',op=None,
xml_output_filename=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "xml_output_filename  readable by OpenTURNS with input distribution information",ang= "xml_output_filename  readable by OpenTURNS with input distribution information",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_number=SIMP(typ='I',fr= "Number of random parameters in the design",ang= "Number of random parameters in the design",statut= "o",docu= "",into=None,min=1,max=1,val_min=1,val_max=10,defaut=None),
random_seed=SIMP(typ='I',fr= "Random seed",ang= "Random seed",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_4=SIMP(typ='TXM',fr= "Distribution of parameter 4",ang= "Distribution of parameter 4",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
design_type=SIMP(typ='TXM',fr= "Design type",ang= "Design type",statut= "o",docu= "",into=['MC', 'LHS', 'QMC_Sobol', 'QMC_Halton'],min=1,max=1,val_min='**',val_max='**',defaut=None),
dependancy_relationship=SIMP(typ='TXM',fr= "Dependancy relationship for input random parameters",ang= "Dependancy relationship for input random parameters",statut= "o",docu= "",into=['Independent', 'Normal'],min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_3=SIMP(typ='TXM',fr= "Distribution of parameter 3",ang= "Distribution of parameter 3",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_9=SIMP(typ='TXM',fr= "Distribution of parameter 9",ang= "Distribution of parameter 9",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_8=SIMP(typ='TXM',fr= "Distribution of parameter 8",ang= "Distribution of parameter 8",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_5=SIMP(typ='TXM',fr= "Distribution of parameter 5",ang= "Distribution of parameter 5",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
csv_output_filename=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "csv_output_filename readable with a text editor",ang= "csv_output_filename readable with a text editor",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_2=SIMP(typ='TXM',fr= "Distribution of parameter 2",ang= "Distribution of parameter 2",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_1=SIMP(typ='TXM',fr= "Distribution of parameter 1",ang= "Distribution of parameter 1",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_0=SIMP(typ='TXM',fr= "Distribution of first parameter",ang= "Distribution of first parameter",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_7=SIMP(typ='TXM',fr= "Distribution of parameter 7",ang= "Distribution of parameter 7",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
parameter_6=SIMP(typ='TXM',fr= "Distribution of parameter 6",ang= "Distribution of parameter 6",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
corr_matrix_filename=SIMP(typ=('Fichier', 'All Files (*)'),fr= "Correlation matrix filename",ang= "Correlation matrix filename",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
size=SIMP(typ='I',fr= "Size of the experimental design",ang= "Size of the experimental design",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_pre_interface_mesh
# ======================================================================
C_PRE_INTERFACE_MESH_DATA=PROC(nom='C_PRE_INTERFACE_MESH_DATA',op=None,
surface_type=SIMP(typ='TXM',fr= "nature of the input surface, select how it is interpreted by the component",ang= "nature of the input surface, select how it is interpreted by the component",statut= "o",docu= "",into=['rectangle_grid', 'crack_fit'],min=1,max=1,val_min='**',val_max='**',defaut='rectangle_grid'),
output_surf=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "pathname of the file where the output BREP surface is generated",ang= "pathname of the file where the output BREP surface is generated",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
nb_segments=SIMP(typ='I',fr= "number of 1D segments for each elementary face of the surface in the resulting mesh",ang= "number of 1D segments for each elementary face of the surface in the resulting mesh",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_surface_field_csv_file_name=SIMP(typ=('Fichier', 'All Files (*)'),fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_mesh=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "pathname of the file where the output MED mesh is generated",ang= "pathname of the file where the output MED mesh is generated",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_surface_field_csv_metadata_file_name=SIMP(typ=('Fichier', 'All Files (*)'),fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_solver_aster
# ======================================================================
C_SOLVER_ASTER_DATA=PROC(nom='C_SOLVER_ASTER_DATA',op=None,
meshfile=SIMP(typ=('Fichier', 'All Files (*)'),fr= "Geometry modelisation",ang= "Geometry modelisation",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
commfile=SIMP(typ=('Fichier', 'All Files (*)'),fr= "Code_Aster modelisation",ang= "Code_Aster modelisation",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_image_3d_altitude_thickness
# ======================================================================
C_IMAGE_3D_ALTITUDE_THICKNESS_DATA=PROC(nom='C_IMAGE_3D_ALTITUDE_THICKNESS_DATA',op=None,
direction=SIMP(typ='I',fr= "The direction type",ang= "The direction type",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
alt_min=SIMP(typ='I',fr= "The minimum altitude",ang= "The minimum altitude",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
calculation=SIMP(typ='TXM',fr= "The calculation type",ang= "The calculation type",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
alt_max=SIMP(typ='I',fr= "The maximum altitude",ang= "The maximum altitude",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_grid_field_csv_metadata=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "CVS formated grid metadata",ang= "CVS formated grid metadata",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_grid_field_raw_metadata=SIMP(typ=('Fichier', 'All Files (*)'),fr= "field metadata file",ang= "field metadata file",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_grid_field_csv=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "CVS formated grid",ang= "CVS formated grid",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_grid_field_raw=SIMP(typ=('Fichier', 'All Files (*)'),fr= "field data file",ang= "field data file",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_image_2d_inclusion_statistics
# ======================================================================
C_IMAGE_2D_INCLUSION_STATISTICS_DATA=PROC(nom='C_IMAGE_2D_INCLUSION_STATISTICS_DATA',op=None,
border_inclusion_option=SIMP(typ='I',fr= "0 : border inclusion area is doubled and their center of mass is set at the boundary, 1 : no special treatment for border inclusion, 2 : border inclusions are discarded",ang= "0 : border inclusion area is doubled and their center of mass is set at the boundary, 1 : no special treatment for border inclusion, 2 : border inclusions are discarded",statut= "f",docu= "",into=[0, 1, 2],min=1,max=1,val_min='**',val_max='**',defaut=0),
output_prefix=SIMP(typ='TXM',fr= "(optional, default : empty string) Prefix appended before the output file name",ang= "(optional, default : empty string) Prefix appended before the output file name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_suffix=SIMP(typ='TXM',fr= "(optional, default : empty string) Suffix appended after the output file name",ang= "(optional, default : empty string) Suffix appended after the output file name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
image_name=SIMP(typ='TXM',fr= "pathname of the files of input images ; globing (wild card) is allowed",ang= "pathname of the files of input images ; globing (wild card) is allowed",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_directory=SIMP(typ='Repertoire',fr= "(optional, default : <current directory>/refs) path where each output file is written",ang= "(optional, default : <current directory>/refs) path where each output file is written",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_image_2d_uncurtain
# ======================================================================
C_IMAGE_2D_UNCURTAIN_DATA=PROC(nom='C_IMAGE_2D_UNCURTAIN_DATA',op=None,
gui=SIMP(typ='TXM',fr= "Run the Graphical User Interface if set to True",ang= "Run the Graphical User Interface if set to True",statut= "f",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=False),
image_name=SIMP(typ='TXM',fr= "pathname of the files of input images ; globing (wild card) is allowed",ang= "pathname of the files of input images ; globing (wild card) is allowed",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
core_width=SIMP(typ='R',fr= "(optional if GUI is used, mandatory otherwise)center size not to be darken in the fourier transform image",ang= "(optional if GUI is used, mandatory otherwise)center size not to be darken in the fourier transform image",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=None),
mask_width=SIMP(typ='R',fr= "(optional if GUI is used, mandatory otherwise) dark bands width  of the mask",ang= "(optional if GUI is used, mandatory otherwise) dark bands width  of the mask",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=None),
mask_blur=SIMP(typ='R',fr= "(optional if GUI is used, mandatory otherwise)gaussian blur sigma applied on the mask",ang= "(optional if GUI is used, mandatory otherwise)gaussian blur sigma applied on the mask",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=None),
output_prefix=SIMP(typ='TXM',fr= "(optional, default : empty string) Prefix appended before the output file name",ang= "(optional, default : empty string) Prefix appended before the output file name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_directory=SIMP(typ='Repertoire',fr= "(optional, default : <current directory>/refs) path where each output file is written",ang= "(optional, default : <current directory>/refs) path where each output file is written",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_suffix=SIMP(typ='TXM',fr= "(optional, default : empty string) Suffix appended after the output file name",ang= "(optional, default : empty string) Suffix appended after the output file name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_post_distribution_properties
# ======================================================================
C_POST_DISTRIBUTION_PROPERTIES_DATA=PROC(nom='C_POST_DISTRIBUTION_PROPERTIES_DATA',op=None,
input_grid_field_csv_metadata_file_name=SIMP(typ=('Fichier', 'All Files (*)'),fr= "name of the metadata format input file (grid_field data read by the component)",ang= "name of the metadata format input file (grid_field data read by the component)",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_grid_field_csv_file_name=SIMP(typ=('Fichier', 'All Files (*)'),fr= "name of the csv format input file (grid_field data read by the component)",ang= "name of the csv format input file (grid_field data read by the component)",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_distribution_properties_text_file_name=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "gives the name of the output file of the component",ang= "gives the name of the output file of the component",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='c_post_distribution_properties.output.csv'),
output_distribution_properties_png_file_name=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "gives the name of the output file of the component",ang= "gives the name of the output file of the component",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='c_post_distribution_properties.output.png'),
variable_name=SIMP(typ='TXM',fr= "must be the name of one of the columns of the csv file whose name is given by input_grid_field_csv_name",ang= "must be the name of one of the columns of the csv file whose name is given by input_grid_field_csv_name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
post=SIMP(typ='TXM',fr= "the value must be included into the following list : CDF (Cumulative Density Function) , PDF (Probability Density Function), dbg (distance to grain boundary graph : needs a distance_grain_boundary column in the data file), quantification (computes the optimised distribution in a family of distributions and estimates its parameter)",ang= "the value must be included into the following list : CDF (Cumulative Density Function) , PDF (Probability Density Function), dbg (distance to grain boundary graph : needs a distance_grain_boundary column in the data file), quantification (computes the optimised distribution in a family of distributions and estimates its parameter)",statut= "o",docu= "",into=['CDF', 'PDF', 'dbg', 'quantification'],min=1,max=1,val_min='**',val_max='**',defaut=None),
interactive=SIMP(typ='TXM',fr= "True -> an interactive window appears when graphs are created. False -> no window.name of the output file of the component",ang= "True -> an interactive window appears when graphs are created. False -> no window.name of the output file of the component",statut= "o",docu= "",into=['False', 'True'],min=1,max=1,val_min='**',val_max='**',defaut=False),
)
# ======================================================================
# Catalog entry for the MAP function : c_image_2d_brightness_equalizer
# ======================================================================
C_IMAGE_2D_BRIGHTNESS_EQUALIZER_DATA=PROC(nom='C_IMAGE_2D_BRIGHTNESS_EQUALIZER_DATA',op=None,
orientation=SIMP(typ='R',fr= "(useful only if <mask_shape> is planar, optional if GUI is used, mandatory otherwise) direction toward which the plan is tilting in degrees",ang= "(useful only if <mask_shape> is planar, optional if GUI is used, mandatory otherwise) direction toward which the plan is tilting in degrees",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
gui=SIMP(typ='TXM',fr= "Run the Graphical User Interface if set to True",ang= "Run the Graphical User Interface if set to True",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=False),
image_name=SIMP(typ='TXM',fr= "pathname of the files of input images ; globing (wild card) is allowed",ang= "pathname of the files of input images ; globing (wild card) is allowed",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_directory=SIMP(typ='Repertoire',fr= "(optional, default : <current directory>/refs) path where each output file is written",ang= "(optional, default : <current directory>/refs) path where each output file is written",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
gaussian_blur_sigma=SIMP(typ='R',fr= "(useful only if <mask_shape> is gaussian, optional if GUI is used, mandatory otherwise) standard variation of the gaussian blur applied to the input image to create the mask",ang= "(useful only if <mask_shape> is gaussian, optional if GUI is used, mandatory otherwise) standard variation of the gaussian blur applied to the input image to create the mask",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=None),
output_prefix=SIMP(typ='TXM',fr= "(optional, default : empty string) Prefix appended before the output file name",ang= "(optional, default : empty string) Prefix appended before the output file name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
mask_shape=SIMP(typ='TXM',fr= "(optional if GUI is used, mandatory otherwise) technic used to create the mask shape",ang= "(optional if GUI is used, mandatory otherwise) technic used to create the mask shape",statut= "o",docu= "",into=['gaussian', 'parabolic', 'planar'],min=1,max=1,val_min='**',val_max='**',defaut=None),
relative_steepness=SIMP(typ='R',fr= "(useful only if <mask_shape> is parabolic, optional if GUI is used, mandatory otherwise) Set the steepness of the 2D parabola. The mask maximum value is computed as <relative_steepness> multiplied by the difference between input image minimum and maximum value divided by 100",ang= "(useful only if <mask_shape> is parabolic, optional if GUI is used, mandatory otherwise) Set the steepness of the 2D parabola. The mask maximum value is computed as <relative_steepness> multiplied by the difference between input image minimum and maximum value divided by 100",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_suffix=SIMP(typ='TXM',fr= "(optional, default : empty string) Suffix appended after the output file name",ang= "(optional, default : empty string) Suffix appended after the output file name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
relative_tilt=SIMP(typ='R',fr= "(useful only if <mask_shape> is planar, optional if GUI is used, mandatory otherwise) set the plan tilt. In the <orientation> direction, the mask value is decreased by <relative_tilt> multiplied by the difference between the input image maximum and minimum values divided by 100 times the image length",ang= "(useful only if <mask_shape> is planar, optional if GUI is used, mandatory otherwise) set the plan tilt. In the <orientation> direction, the mask value is decreased by <relative_tilt> multiplied by the difference between the input image maximum and minimum values divided by 100 times the image length",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_post_table_fft
# ======================================================================
C_POST_TABLE_FFT_DATA=PROC(nom='C_POST_TABLE_FFT_DATA',op=None,
output_spectr_y_png_file_name=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_surface_grid_field_csv_metadata_file_name=SIMP(typ=('Fichier', 'All Files (*)'),fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_spectr_x_png_file_name=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
show_image=SIMP(typ='TXM',fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=True),
output_surface_grid_field_png_file_name=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_surface_properties_file_name=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
show_spectr=SIMP(typ='TXM',fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=True),
input_surface_grid_field_csv_file_name=SIMP(typ=('Fichier', 'All Files (*)'),fr= "No comment",ang= "No comment",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
interactive=SIMP(typ='TXM',fr= "No comment",ang= "No comment",statut= "o",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=False),
)
# ======================================================================
# Catalog entry for the MAP function : c_solver_corrosion_evolution
# ======================================================================
C_SOLVER_CORROSION_EVOLUTION_DATA=PROC(nom='C_SOLVER_CORROSION_EVOLUTION_DATA',op=None,
x_Cr=SIMP(typ='R',fr= "the fraction of Cr in the alloy (non dimensional unit : must be between 0 and 1 (x_Cr = 0.3 <=> 30% Cr in the alloy))",ang= "the fraction of Cr in the alloy (non dimensional unit : must be between 0 and 1 (x_Cr = 0.3 <=> 30% Cr in the alloy))",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max=1.0,defaut=0.3),
save_history=SIMP(typ='TXM',fr= "must be set to yes if you want to save the integration times into the output file",ang= "must be set to yes if you want to save the integration times into the output file",statut= "o",docu= "",into=('True', 'False'),min=1,max=1,val_min='**',val_max='**',defaut='True'),
D_vO=SIMP(typ='R',fr= "diffusion coefficient of oxygen vacancies",ang= "diffusion coefficient of oxygen vacancies",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
F_0f=SIMP(typ='R',fr= "potential drop in the film",ang= "potential drop in the film",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
x_Fe=SIMP(typ='R',fr= "the fraction of Fe in the alloy (non dimensional unit : must be between 0 and 1 (x_Fe = 0.1 <=> 10% Fe in the alloy))",ang= "the fraction of Fe in the alloy (non dimensional unit : must be between 0 and 1 (x_Fe = 0.1 <=> 10% Fe in the alloy))",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max=1.0,defaut=0.1),
pH_temperature=SIMP(typ='R',fr= "it determines the value of the pH for the herebove determined temperature (must be >0)",ang= "it determines the value of the pH for the herebove determined temperature (must be >0)",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=7.2),
temperature_in_K=SIMP(typ='R',fr= "it determines the value of the temperature in Kelvin degrees (must be >0)",ang= "it determines the value of the temperature in Kelvin degrees (must be >0)",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=603.0),
x_Ni=SIMP(typ='R',fr= "the fraction of Ni in the alloy (non dimensional unit : must be between 0 and 1 (x_Ni = 0.58 <=> 58% Ni in the alloy))",ang= "the fraction of Ni in the alloy (non dimensional unit : must be between 0 and 1 (x_Ni = 0.58 <=> 58% Ni in the alloy))",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max=1.0,defaut=0.58),
time_in_seconds=SIMP(typ='R',fr= "the duration of the physical time experiment",ang= "the duration of the physical time experiment",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=36000.0),
DG1=SIMP(typ='R',fr= "Gibbs energy of formation of reaction 1 (Cr_M -> Cr3+_ox + 3e- + 3/2 V_o with V_o = oxygen vacancy)",ang= "Gibbs energy of formation of reaction 1 (Cr_M -> Cr3+_ox + 3e- + 3/2 V_o with V_o = oxygen vacancy)",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=10000.0),
DV=SIMP(typ='R',fr= "potential change with respect to a stationnary state",ang= "potential change with respect to a stationnary state",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
alpha=SIMP(typ='R',fr= "interface polarisability (between 0 and 1)",ang= "interface polarisability (between 0 and 1)",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
model=SIMP(typ='TXM',fr= "determines the physical model used in the code (must belong to the following list [Seyeux_2010, Leistner_2012])",ang= "determines the physical model used in the code (must belong to the following list [Seyeux_2010, Leistner_2012])",statut= "o",docu= "",into=['Seyeux_2010', 'Leistner_2012'],min=1,max=1,val_min='**',val_max='**',defaut='Seyeux_2010'),
F_0mf=SIMP(typ='R',fr= "potential drop at film-solution interface",ang= "potential drop at film-solution interface",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
output_file_name=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "the name of the text file where the results are written",ang= "the name of the text file where the results are written",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='c_solver_corrosion_evolution.output'),
F_0fs=SIMP(typ='R',fr= "potential drop at film-solution interface",ang= "potential drop at film-solution interface",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_pre_image2mesh_2d
# ======================================================================
C_PRE_IMAGE2MESH_2D_DATA=PROC(nom='C_PRE_IMAGE2MESH_2D_DATA',op=None,
input_image=SIMP(typ=('Fichier', 'All Files (*)'),fr= " name of the image input file name (pgm format only)",ang= " name of the image input file name (pgm format only)",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
mesh_size=SIMP(typ='R',fr= "size of the mesh elements",ang= "size of the mesh elements",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=0.2),
study_path=SIMP(typ='Repertoire',fr= "determines the name of the directory where intermediate files produced by PINK library are written.",ang= "determines the name of the directory where intermediate files produced by PINK library are written.",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='/tmp'),
output_mesh=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "name of the mesh output file name",ang= "name of the mesh output file name",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='output_c_pre_image2mesh_2d.med'),
study_name=SIMP(typ='TXM',fr= "determines the name of the study to determine the name of the intermediate files produced by PINK library are written",ang= "determines the name of the study to determine the name of the intermediate files produced by PINK library are written",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='study_c_pre_image2mesh_2d'),
)
# ======================================================================
# Catalog entry for the MAP function : c_transverse_empty_python
# ======================================================================
C_TRANSVERSE_EMPTY_PYTHON_DATA=PROC(nom='C_TRANSVERSE_EMPTY_PYTHON_DATA',op=None,
file_output=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "name of the output file of the component",ang= "name of the output file of the component",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='c_transverse_empty_python.output'),
an_integer=SIMP(typ='I',fr= "number of lines in the output file",ang= "number of lines in the output file",statut= "o",docu= "",into=None,min=1,max=1,val_min=1,val_max='**',defaut=4),
a_float=SIMP(typ='R',fr= "simply print in verbose mode",ang= "simply print in verbose mode",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=5.3),
a_string=SIMP(typ='TXM',fr= "simply print in verbose mode",ang= "simply print in verbose mode",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='Hello world of MAP'),
)
# ======================================================================
# Catalog entry for the MAP function : c_pre_morphology_synthesis_voronoi
# ======================================================================
C_PRE_MORPHOLOGY_SYNTHESIS_VORONOI_DATA=PROC(nom='C_PRE_MORPHOLOGY_SYNTHESIS_VORONOI_DATA',op=None,
param_volumes=SIMP(typ='TXM',fr= "list of 3 values used to generate the histogram to specify the minimum value, maximum value and step numbers for the histogram. In cas the value is not specified for min and max, a void field [] can be used and the default value of 0. will be used for the min while the max is automatically calculated, a few examples follow: param_volumes = [0.,[],20] will correspond to a 20-bar histogram of min value 0. and automatic max value, param_volumes = [[],[],20] will give the same result, param_volumes = [2.,10.,20] will correspond to a 20-bar histogram of min value 2. and max value 10.",ang= "list of 3 values used to generate the histogram to specify the minimum value, maximum value and step numbers for the histogram. In cas the value is not specified for min and max, a void field [] can be used and the default value of 0. will be used for the min while the max is automatically calculated, a few examples follow: param_volumes = [0.,[],20] will correspond to a 20-bar histogram of min value 0. and automatic max value, param_volumes = [[],[],20] will give the same result, param_volumes = [2.,10.,20] will correspond to a 20-bar histogram of min value 2. and max value 10.",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='[0.,[],20]'),
folder_out=SIMP(typ='Repertoire',fr= "name of the folder where output files will be written",ang= "name of the folder where output files will be written",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='/tmp'),
random_seed=SIMP(typ='I',fr= "Integer parameter, when set to -1 the random seed will be set by the alea parameter. For any different value, the random seed is arbitrary.",ang= "Integer parameter, when set to -1 the random seed will be set by the alea parameter. For any different value, the random seed is arbitrary.",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=-1),
puis=SIMP(typ='R',fr= "float ranging between 0. an 1. used to control the repulsion between germs. Indeed, a random germ distribution can sometimes give unexpected results when two germs are too close to each other. Setting a strictly positive repulsion distance will produce an aggregate of more homogeneous grain sizes.",ang= "float ranging between 0. an 1. used to control the repulsion between germs. Indeed, a random germ distribution can sometimes give unexpected results when two germs are too close to each other. Setting a strictly positive repulsion distance will produce an aggregate of more homogeneous grain sizes.",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max=1.0,defaut=1.0),
predef=SIMP(typ='R',fr= "float used to control the pre-strain in the aggregate ?",ang= "float used to control the pre-strain in the aggregate ?",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=0.0),
sdec=SIMP(typ='TXM',fr= "boolean used to determine ?",ang= "boolean used to determine ?",statut= "o",docu= "",into=['True', 'False'],min=1,max=1,val_min='**',val_max='**',defaut='False'),
maillage=SIMP(typ='TXM',fr= "boolean used to ask the print of the mesh in MED format",ang= "boolean used to ask the print of the mesh in MED format",statut= "o",docu= "",into=['True', 'False'],min=1,max=1,val_min='**',val_max='**',defaut='True'),
study_name=SIMP(typ='TXM',fr= "name given to the study, which will be used as the root to define output file names, e.g. 'my_aggregate_with_40_grains",ang= "name given to the study, which will be used as the root to define output file names, e.g. 'my_aggregate_with_40_grains",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='my_aggregate_with_xx_grains'),
printhist=SIMP(typ='TXM',fr= "boolean that will trigger the print of an .hist histogram datafile for garn sizes, volumes and surfaces",ang= "boolean that will trigger the print of an .hist histogram datafile for garn sizes, volumes and surfaces",statut= "o",docu= "",into=['True', 'False'],min=1,max=1,val_min='**',val_max='**',defaut='True'),
ngrains=SIMP(typ='I',fr= "number of grains in the generated aggregate",ang= "number of grains in the generated aggregate",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=20),
param_surfaces=SIMP(typ='TXM',fr= "list of 3 values used to generate the histogram to specify the minimum value, maximum value and step numbers for the histogram. In cas the value is not specified for min and max, a void field [] can be used and the default value of 0. will be used for the min while the max is automatically calculated, a few examples follow: param_volumes = [0.,[],20] will correspond to a 20-bar histogram of min value 0. and automatic max value, param_volumes = [[],[],20] will give the same result, param_volumes = [2.,10.,20] will correspond to a 20-bar histogram of min value 2. and max value 10.",ang= "list of 3 values used to generate the histogram to specify the minimum value, maximum value and step numbers for the histogram. In cas the value is not specified for min and max, a void field [] can be used and the default value of 0. will be used for the min while the max is automatically calculated, a few examples follow: param_volumes = [0.,[],20] will correspond to a 20-bar histogram of min value 0. and automatic max value, param_volumes = [[],[],20] will give the same result, param_volumes = [2.,10.,20] will correspond to a 20-bar histogram of min value 2. and max value 10.",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='[0.,[],20]'),
param_dg=SIMP(typ='TXM',fr= "list of 3 values used to generate the histogram to specify the minimum value, maximum value and step numbers for the histogram. In cas the value is not specified for min and max, a void field [] can be used and the default value of 0. will be used for the min while the max is automatically calculated, a few examples follow: param_volumes = [0.,[],20] will correspond to a 20-bar histogram of min value 0. and automatic max value, param_volumes = [[],[],20] will give the same result, param_volumes = [2.,10.,20] will correspond to a 20-bar histogram of min value 2. and max value 10.",ang= "list of 3 values used to generate the histogram to specify the minimum value, maximum value and step numbers for the histogram. In cas the value is not specified for min and max, a void field [] can be used and the default value of 0. will be used for the min while the max is automatically calculated, a few examples follow: param_volumes = [0.,[],20] will correspond to a 20-bar histogram of min value 0. and automatic max value, param_volumes = [[],[],20] will give the same result, param_volumes = [2.,10.,20] will correspond to a 20-bar histogram of min value 2. and max value 10.",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='[0.,[],20]'),
symet=SIMP(typ='TXM',fr= "boolean used to determine the symetry",ang= "boolean used to determine the symetry",statut= "o",docu= "",into=['True', 'False'],min=1,max=1,val_min='**',val_max='**',defaut='False'),
homot=SIMP(typ='R',fr= "float used to control the size of the aggregate ?",ang= "float used to control the size of the aggregate ?",statut= "f",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=1.0),
alea=SIMP(typ='I',fr= "integer parameter specifying the initial seed for the random algorithm used to distribute the germs of the voronoi cells. It will only be active when random_seed=-1. This situation is useful to reproduce the generation of similar aggregates.",ang= "integer parameter specifying the initial seed for the random algorithm used to distribute the germs of the voronoi cells. It will only be active when random_seed=-1. This situation is useful to reproduce the generation of similar aggregates.",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
printbrep=SIMP(typ='TXM',fr= "boolean used to ask the print of the .brep file",ang= "boolean used to ask the print of the .brep file",statut= "o",docu= "",into=['True', 'False'],min=1,max=1,val_min='**',val_max='**',defaut='True'),
)
# ======================================================================
# Catalog entry for the MAP function : c_solver_homogenisation_mechanics
# ======================================================================
C_SOLVER_HOMOGENISATION_MECHANICS_DATA=PROC(nom='C_SOLVER_HOMOGENISATION_MECHANICS_DATA',op=None,
microstructure_composition_file=SIMP(typ=('Fichier', 'All Files (*)'),fr= "microstructure's description",ang= "microstructure's description",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
effective_properties_visualisation_output_file=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "visualisation of effective properties",ang= "visualisation of effective properties",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
homogenisation_scheme=SIMP(typ='TXM',fr= "homogenisation scheme",ang= "homogenisation scheme",statut= "o",docu= "",into=['Voigt', 'Reuss', 'Self-Consistent', 'Hashin-Shtrikman'],min=1,max=1,val_min='**',val_max='**',defaut=None),
reference_phase_file=SIMP(typ=('Fichier', 'All Files (*)'),fr= "reference phase description",ang= "reference phase description",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
phase_input_file=SIMP(typ=('Fichier', 'All Files (*)'),fr= "phases description",ang= "phases description",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
effective_properties_text_output_file=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "computed effective properties",ang= "computed effective properties",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_transverse_display_map
# ======================================================================
C_TRANSVERSE_DISPLAY_MAP_DATA=PROC(nom='C_TRANSVERSE_DISPLAY_MAP_DATA',op=None,
palette=SIMP(typ='TXM',fr= "defines the color scale",ang= "defines the color scale",statut= "o",docu= "",into=['color', 'gray'],min=1,max=1,val_min='**',val_max='**',defaut=None),
x_title=SIMP(typ='TXM',fr= "X-axis title",ang= "X-axis title",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
z_title=SIMP(typ='TXM',fr= "Z-axis title",ang= "Z-axis title",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
contour_lines=SIMP(typ='TXM',fr= "display color lines",ang= "display color lines",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=True),
y_title=SIMP(typ='TXM',fr= "Y-axis title",ang= "Y-axis title",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
x_axis=SIMP(typ='TXM',fr= "the identifier of the x axis column",ang= "the identifier of the x axis column",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
show_img=SIMP(typ='TXM',fr= "Show the plot result",ang= "Show the plot result",statut= "o",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=False),
save_img=SIMP(typ='TXM',fr= "Save the plot result",ang= "Save the plot result",statut= "o",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=False),
output_img_name=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "name of the output image",ang= "name of the output image",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_datafile=SIMP(typ=('Fichier', 'All Files (*)'),fr= "contains the data the display_map should be made on",ang= "contains the data the display_map should be made on",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
color_scale=SIMP(typ='TXM',fr= "defines implicitely the number of colors to be used to represent the data",ang= "defines implicitely the number of colors to be used to represent the data",statut= "o",docu= "",into=['continuum', 'discrete'],min=1,max=1,val_min='**',val_max='**',defaut=None),
show_grid=SIMP(typ='TXM',fr= "display grid",ang= "display grid",statut= "o",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=True),
y_axis=SIMP(typ='TXM',fr= "the identifier of the y axis column",ang= "the identifier of the y axis column",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
z_axis=SIMP(typ='TXM',fr= "the identifier of the z axis column",ang= "the identifier of the z axis column",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
main_title=SIMP(typ='TXM',fr= "Graphic Main Title",ang= "Graphic Main Title",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
interpolation=SIMP(typ='TXM',fr= "defines how to interpolate the color levels between the given data",ang= "defines how to interpolate the color levels between the given data",statut= "o",docu= "",into=['nearest', 'bilinear', 'bicubic'],min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_transverse_interpolation
# ======================================================================
C_TRANSVERSE_INTERPOLATION_DATA=PROC(nom='C_TRANSVERSE_INTERPOLATION_DATA',op=None,
function=SIMP(typ='TXM',fr= "user defined function",ang= "user defined function",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
show=SIMP(typ='TXM',fr= "show plot of the result",ang= "show plot of the result",statut= "o",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=False),
initial_guess=SIMP(typ='TXM',fr= "initial guess for the adjustable parameters",ang= "initial guess for the adjustable parameters",statut= "f",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
save_img=SIMP(typ='L',fr= "save plot of the result",ang= "save plot of the result",statut= "o",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=False),
input_datafile=SIMP(typ=('Fichier', 'All Files (*)'),fr= "contains the data the interpolation should be made on",ang= "contains the data the interpolation should be made on",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
save_out=SIMP(typ='TXM',fr= "save interpolation result",ang= "save interpolation result",statut= "o",docu= "",into=('False','True'),min=1,max=1,val_min='**',val_max='**',defaut=True),
interpolation=SIMP(typ='TXM',fr= "the type of interpolation the user wants",ang= "the type of interpolation the user wants",statut= "o",docu= "",into=['poly1', 'poly2', 'poly3', 'poly4', 'poly5', 'poly6', 'poly7', 'poly8', 'poly9', 'inverse1', 'inverse2', 'inverse3', 'inverse4', 'inverse5', 'inverse6', 'inverse7', 'inverse8', 'inverse9', 'power', 'expo', 'logn', 'gauss', 'poisson', 'double_gauss', 'double_poisson', 'weibull2', 'weibull3', 'gumbel', 'logn_affin', 'user_defined'],min=1,max=1,val_min='**',val_max='**',defaut=None),
)
# ======================================================================
# Catalog entry for the MAP function : c_transverse_empty_c
# ======================================================================
C_TRANSVERSE_EMPTY_C_DATA=PROC(nom='C_TRANSVERSE_EMPTY_C_DATA',op=None,
file_output=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "name of the output file of the component",ang= "name of the output file of the component",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='c_transverse_empty_c.output'),
an_integer=SIMP(typ='I',fr= "number of lines in the output file",ang= "number of lines in the output file",statut= "o",docu= "",into=None,min=1,max=1,val_min=1,val_max='**',defaut=4),
a_float=SIMP(typ='R',fr= "simply print in verbose mode",ang= "simply print in verbose mode",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=5.3),
a_string=SIMP(typ='TXM',fr= "simply print in verbose mode",ang= "simply print in verbose mode",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='Hello world of MAP'),
)
# ======================================================================
# Catalog entry for the MAP function : c_pre_morphology_gravel
# ======================================================================
C_PRE_MORPHOLOGY_GRAVEL_DATA=PROC(nom='C_PRE_MORPHOLOGY_GRAVEL_DATA',op=None,
multiscale=SIMP(typ='TXM',fr= "determine, in the case of the microstructure computation if it is multiscale or no",ang= "determine, in the case of the microstructure computation if it is multiscale or no",statut= "o",docu= "",into=['yes', 'no'],min=1,max=1,val_min='**',val_max='**',defaut='no'),
random_seed=SIMP(typ='I',fr= "gives the value of the seed used to initialize the random process. This parameter is optional, if it is not given, random is initialised with time. The parameter is mainly used for non-regression tests purpose.",ang= "gives the value of the seed used to initialize the random process. This parameter is optional, if it is not given, random is initialised with time. The parameter is mainly used for non-regression tests purpose.",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=1332150941),
computation=SIMP(typ='TXM',fr= "determines the type of computation",ang= "determines the type of computation",statut= "o",docu= "",into=['microstructure'],min=1,max=1,val_min='**',val_max='**',defaut='microstructure'),
raw_type=SIMP(typ='TXM',fr= "unused",ang= "unused",statut= "o",docu= "",into=['image'],min=1,max=1,val_min='**',val_max='**',defaut='image'),
lambda_Poisson=SIMP(typ='R',fr= "density planes for buiding microstructures for class 1 polyhedra",ang= "density planes for buiding microstructures for class 1 polyhedra",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=0.035),
voxel_side=SIMP(typ='R',fr= "resolution of the output image",ang= "resolution of the output image",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=1.0),
fraction=SIMP(typ='R',fr= "volume fraction for class 1 polyhedra",ang= "volume fraction for class 1 polyhedra",statut= "o",docu= "",into=None,min=1,max=1,val_min=0.0,val_max='**',defaut=0.15),
polyhedra_library_path=SIMP(typ='TXM',fr= "relative path to polyhedra library",ang= "relative path to polyhedra library",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='/home/A28637/SVN_MAP/trunk/share/map/poissonPolyhedra/library_escoda_2012'),
file_out_raw=SIMP(typ=('Fichier', 'All Files (*)', 'Sauvegarde'),fr= "binary file output for binarized image",ang= "binary file output for binarized image",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut='c_pre_morphology_gravel.raw'),
size=SIMP(typ='I',fr= "size of the image (discretization in the case of the covariance measurment)",ang= "size of the image (discretization in the case of the covariance measurment)",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=250),
)
# ======================================================================
# Catalog entry for the MAP function : s_scc_3d_analysis
# ======================================================================
S_SCC_3D_ANALYSIS_DATA=PROC(nom='S_SCC_3D_ANALYSIS_DATA',op=None,
direction=SIMP(typ='I',fr= "The direction type",ang= "The direction type",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
alt_min=SIMP(typ='I',fr= "The minimum altitude",ang= "The minimum altitude",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
calculation=SIMP(typ='TXM',fr= "The calculation type",ang= "The calculation type",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
alt_max=SIMP(typ='I',fr= "The maximum altitude",ang= "The maximum altitude",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_grid_field_raw_metadata=SIMP(typ=('Fichier', 'All Files (*)'),fr= "field metadata file",ang= "field metadata file",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
input_grid_field_raw=SIMP(typ=('Fichier', 'All Files (*)'),fr= "field data file",ang= "field data file",statut= "o",docu= "",into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
)

# This text should be dump into a file named 'map_cata.py' to be
# copied in the eficas directory $EFICAS_ROOT/MAP/.
# Then run 'qtEficas_map.py -s maquettemap'. The key name
# maquettemap is the name defined in prefs_MAP.py
