# coding: utf-8

from Accas import *
class DateJJMMAAAA:
  def __init__(self):
    self.ntuple=3

  def __convert__(self,valeur):
    if type(valeur) == types.StringType: return None
    if len(valeur) != self.ntuple: return None
    return valeur

  def info(self):
    return "Date : jj/mm/aaaa "

  __repr__=info
  __str__=info

class HeureHHMMSS:
  def __init__(self):
    self.ntuple=3

  def __convert__(self,valeur):
    if type(valeur) == types.StringType: return None
    if len(valeur) != self.ntuple: return None
    return valeur

  def info(self):
    return "heure : hh/mm/ss "

  __repr__=info
  __str__=info


JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
# ======================================================================
# Catalog entry for the MAP function : c_pre_interfaceBody_mesh
# ======================================================================
INITIALIZATION=PROC(nom="INITIALIZATION",op=None,
     fr="Initialisation des fichiers d'entrée et de sortie",
     ang="Input and Output files initialization",

     Title = SIMP( statut='o',typ='TXM'),
     Working_Directory = SIMP( statut='o',typ='Repertoire',defaut='/tmp'),

     Files= FACT(statut='o',
          Dictionary     = SIMP( statut='o', typ = ('Fichier', 'Dico (*.dico);;All Files (*)',), defaut='telemac2d.dico',),
          Geometry_File_Format = SIMP( statut='o',typ='TXM',into=['SERAFIN','MED','SERAFIND'], defaut='SERAFIN',
          fr='Format du fichier de geometrie. Les valeurs possibles sont : - SERAFIN : format standard simple precision pour Telemac;  - SERAFIND: format standard double precision pour Telemac; - MED     : format MED base sur HDF5',
          ang='Results file format. Possible values are: - SERAFIN : classical single precision format in Telemac;  - SERAFIND: classical double precision format in Telemac; - MED     : MED format based on HDF5',) ,
          Geometry_File  = SIMP( statut='o', typ = ('Fichier', 'Geo Files (*.geo);;All Files (*)',),
                fr='Nom du fichier contenant le maillage du calcul a realiser.',
                ang='Name of the file containing the mesh. This file may also contain the topography and the friction coefficients.'),
          #Steering_File     = SIMP( statut='o', typ = ('Fichier', 'Steering Files (*.cas);;All Files (*)',),),
          Results_File_Format = SIMP( statut='o',typ='TXM',into=['SERAFIN','MED','SERAFIND'], defaut='SERAFIN',
                    fr = 'Format du fichier de resultats. Les valeurs possibles sont : \n- SERAFIN : format standard simple precision pour Telemac;  - SERAFIND: format standard double precision pour Telemac; - MED     : format MED base sur HDF5' ,
                    ang = 'Results file format. Possible values are:\n - SERAFIN : classical single precision format in Telemac;\n  - SERAFIND: classical double precision format in Telemac; - MED     : MED format based on HDF5' ,),
 
          Results_File     = SIMP( statut='o', typ = ('Fichier', 'Steering Files (*.cas);;All Files (*)',),),
# Inexistant eventuellement
          Fortran_File = SIMP(statut='f',typ = ('Fichier', 'Fortran files (*.f);;All Files (*)'),
                              fr='Nom du fichier a soumettre',
                              ang='Name of FORTRAN file to be submitted',),
          Boundary_Condition_File = SIMP( statut='o', typ = ('Fichier', 'Boundary Condition (*.cli);;All Files (*)',),),
          Reference_File     = SIMP( statut='f', typ = ('Fichier', 'Reference File (*.ref);;All Files (*)',),),
     ),

     Formated_And_Binary_Files=FACT( statut='f',
          Formated_File1     = SIMP( statut='f', typ = ('Fichier', 'formated File (*.txt);;All Files (*)',),),
          Formated_File2     = SIMP( statut='f', typ = ('Fichier', 'formated File (*.txt);;All Files (*)',),),
          Binary_Data_File1  = SIMP( statut='f', typ = ('Fichier', 'Reference File (*.txt);;All Files (*)',),),
          Binary_Data_File2  = SIMP( statut='f', typ = ('Fichier', 'Reference File (*.txt);;All Files (*)',),),
     ),
     Computation_Continued=FACT( statut='f',
          Previous_Computation_File_Format=SIMP( statut='o',typ='TXM',into=['SERAFIN','MED','SERAFIND'],defaut='SERAFIN',),
          Previous_Computation_File  = SIMP( statut='o', 
              typ = ('Fichier', 'Computation File (*.res);;All Files (*)',),
              fr = "Nom d'un fichier contenant les resultats d'un calcul precedent realise sur le meme maillage et dont le dernier pas de temps enregistre va fournir les conditions initiales pour une suite de de calcul.",
               ang = 'Name of a file containing the results of an earlier computation which was made on the same mesh. The last recorded time step will provid the initial conditions for the new computation.',
                                         ),
          Previous_Computation_Comm  = SIMP( statut='f', typ = ('Fichier', 'COMM(*.comm);;All Files (*)',),
              fr  = "Nom du fichier .comm décrivant le cas précédent",
              ang = "Name of a file containing the earlier study" ,),
          Initial_Time_Set     = SIMP(typ=bool, statut='f',
             fr = 'Remet le temps a zero en cas de suite de calcul',
             ang = 'Initial time set to zero in case of restart',
             defaut="False"),
          Record_Number_For_Restart = SIMP(typ='I', statut='o', defaut=0,
              fr = "numero de l'enregistrementde depart dans le fichier du calcul precedent. 0 signifie qu'on prend le dernier enregistrement", 
              ang ="record number to start from in the previous computation file, 0 for last record" ),
     ),
     Computation=FACT(statut='o',
        Machine=FACT( statut='o',
           Number_of_Processors=SIMP(statut='o',typ='I',val_min=0,defaut=1),
           Parallel_Computation=SIMP(statut='o',typ=bool,defaut=False),
         ),
        Coupling=FACT( statut='o',
           Sisyphe=SIMP(statut='o',typ=bool,defaut=False),
           Tomawac=SIMP(statut='o',typ=bool,defaut=False),
          Delwacq=SIMP(statut='o',typ=bool,defaut=False),
        ),
     ),
)

TIDE_PARAMETERS=PROC(nom="TIDE_PARAMETERS",op=None,
     fr="",
     ang="",
     Time=FACT( statut='o',
       #Original_Date_of_Time=SIMP(statut='f',typ=DateJJMMAAAA,validators=VerifTypeTuple(('R','R','R'))),
       #Original_Hour_of_Time=SIMP(statut='f',typ=HeureHHMMSS,validators=VerifTypeTuple(('R','R','R'))),
       Original_Date_of_Time=FACT( statut='o',
         fr = "Permet de fixer la date d'origine des temps du modele lors de la prise en compte de la force generatrice de la maree.",
         ang ='Give the date of the time origin of the model when taking into account the tide generating force.', 
         Year=SIMP(statut='o',typ='I',val_min=1900,defaut=1900),
         Month=SIMP(statut='o',typ='I',val_min=1,val_max=12,defaut=1),
         Day=SIMP(statut='o',typ='I',val_min=1,val_max=31,defaut=1),
          ),
       Original_Hour_of_Time=FACT( statut='f',
         fr = "Permet de fixer l'heure d'origine des temps du modele lors de la prise en compte de la force generatrice de la maree.",
         ang ='Give the time of the time origin of the model when taking into account the tide generating force.', 
         Hour=SIMP(statut='o',typ='I',val_min=0,val_max=24,defaut=0),
         Minute=SIMP(statut='o',typ='I',val_min=0,val_max=60,defaut=0),
         Second=SIMP(statut='o',typ='I',val_min=0,val_max=60,defaut=0),
         ),
      ),
     Location=FACT( statut='f',
        #regles=( PRESENT_PRESENT('Longitude_of_origin','Latitute_of_origin', ),),
        #Spatial_Projection=SIMP(statut='f',typ='I',into=[1,2,3]),
        #Geographic_System=SIMP(statut='f',typ='I',into=[-1,0,1,2,3,4,5]),

        Geographic_System=SIMP(statut='f',typ='TXM',
              into=["DEFINI PAR L'UTILISATEUR", "WGS84 LONGITUDE/LATITUDE EN DEGRES REELS","WGS84 NORD UTM",'WGS84 SUD UTM','LAMBERT', 'MERCATOR'],
              defaut="DEFINI PAR L'UTILISATEUR",
              fr = 'Systeme de coordonnees geographiques dans lequel est construit le modele numerique.',
              ang = 'Geographic coordinates system in which the numerical model is built.Indicate the corresponding zone with the keyword ',
        ),
             b_geo_system  = BLOC(condition = "Geographic_System in ('WGS84 LONGITUDE/LATITUDE EN DEGRES REELS','WGS84 NORD UTM','WGS84 SUD UTM','MERCATOR')",
             Spatial_Projection=SIMP(statut='o',typ='TXM',into=["CARTESIAN, NOT GEOREFERENCED","MERCATOR","LATITUDE LONGITUDE"]),
             ang = 'Option 2 or 3 mandatory for spherical coordinates Option 3: latitude and longitude in radians!',
             b_lat     = BLOC(condition = "Spatial_Projection == 'LATITUDE LONGITUDE' ",
                 Latitude_of_origin=SIMP(statut='o',typ='R',val_min=-90,val_max=90,fr="en radians", ang="in radians"),
                 Longitude_of_origin=SIMP(statut='o',typ='R',fr="en radians", ang="in radians"),
                         ), # fin bloc b_lat
             ), # fin bloc b_geo
        Zone_number_in_Geographic_System=SIMP(statut='f',typ='I',into=[-1,0,1,2,3,4,22,30]),
     ),
)

INITIAL_STATE=PROC(nom="INITIAL_STATE",op=None,
        Initial_Conditions=SIMP(statut='o',typ='TXM',into=['ZERO ELEVATION', 'CONSTANT ELEVATION','ZERO DEPTH','CONSTANT DEPTH','SPECIAL','TPXO SATELLITE ALTIMETRY'],defaut='ZERO ELEVATION',
         fr = "Permet de definir les conditions initiales sur les hauteurs d'eau. Les valeurs possibles sont : - COTE NULLE. Initialise la cote de surface libre a 0. Les hauteurs d'eau initiales sont alors retrouvees en faisant la difference entre les cotes de surface libre et du fond. - COTE CONSTANTE . Initialise la cote de surface libre a la valeur donnee par le mot-cle COTE INITIALE. Les hauteurs d'eau initiales sont calculees comme precedemment.- HAUTEUR NULLE .Initialise les hauteurs d'eau a 0. - HAUTEUR CONSTANTE. Initialise les hauteurs d'eau a la valeur donnee par le mot-cle HAUTEUR INITIALE. - PARTICULIERES. Les conditions initiales sur la hauteur d'eau doivent etre precisees dans le sous-programme CONDIN. - ALTIMETRIE SATELLITE TPXO. Les conditions initiales sur la hauteur  d'eau et les vitesses sont etablies sur la base des donnees.  satellite TPXO dont les 8 premiers constistuents ont ete extrait et sauves dans le fichier BASE DE DONNEES DE MAREE." ,
          ang = 'Makes it possible to define the initial conditions with the water depth. The possible values are as follows: - ZERO ELEVATION-. Initializes the free surface elevation to 0.The initial water depths are then found by computing the difference between the free surface and the bottom.  - CONSTANT ELEVATION-. Initializes the water elevation to the value given by the keyword -INITIAL ELEVATION-. The initial water depths are computed as in the previous case. - ZERO DEPTH-. Initializes the water depths to 0. - CONSTANT DEPTH-. Initializes the water depths to the value givenby the key-word -INITIAL DEPTH-.   - SPECIAL-. The initial conditions with the water depth should be stated in the CONDIN subroutine.   - TPXO SATELITE ALTIMETRY. The initial conditions on the free surface andvelocities are established from the TPXO satellite program data, the harmonicconstituents of which are stored in the TIDE DATA BASE file.', ),
 
         b_initial_elevation = BLOC (condition = "Initial_Conditions == 'CONSTANT ELEVATION'",
           Initial_Elevation       = SIMP(statut='o',typ='R' ),
         ),
         b_initial_depth     = BLOC (condition = "Initial_Conditions == 'CONSTANT DEPTH'",
           Initial_Depth       = SIMP(statut='o',typ='R' ),
         ),
         b_special     = BLOC (condition = "Initial_Conditions == 'SPECIAL'",
           special    = SIMP(statut='o',typ='TXM',defaut="The initial conditions with the water depth should be stated in the CONDIN subroutine"),
         ),
         b_initial_TPXO      = BLOC (condition = "Initial_Conditions == 'TPXO SATELLITE ALTIMETRY'",
          Base_Ascii_De_Donnees_De_Maree     = SIMP( statut='o', typ = ('Fichier', 'All Files (*)',), ),
           fr  = 'Base de donnees de constantes harmoniques tirees du fichier du modele de maree',
           ang = 'Tide data base of harmonic constituents extracted from the tidal model file',
         ),

    Boundary_Conditions=FACT(statut='f', 
            fr  = 'On donne un ensemble de conditions par frontiere liquide',
            ang = 'One condition set per liquid boundary is given',
 # Dans l ideal il faut aller regarder selon les groupes dans le fichier med
 # en sortie il faut aller chercher le .cli qui va bien 
            #Liquid_Boundaries=FACT(statut='f',max='**',
            #    Options=SIMP(statut='f',typ='I',into=['classical boundary conditions','Thompson method based on characteristics'])
            #    Prescribed_Flowrates=SIMP(statut='f',typ='R'),
            #    Prescribed_Elevations=SIMP(statut='f',typ='R'),
            #    Prescribed_Velocity=SIMP(statut='f',typ='R'),
      # ),
# Il va falloir une "traduction dans le langage du dico"
# Il faut seulement l un des 3
        Liquid_Boundaries=FACT(statut='f',max='**',
                
            Options=SIMP(statut='f',typ='I',into=['classical boundary conditions','Thompson method based on characteristics']),

            Type_Condition=SIMP(statut='o',typ='TXM',into=['Flowrates','Elevations','Velocity'],),
             b_Flowrates     = BLOC (condition = "Type_Condition == 'Flowrates'",
                Prescribed_Flowrates=SIMP(statut='o',typ='R'),
             ),
             b_Elevations   = BLOC (condition = "Type_Condition == 'Elevations'",
                Prescribed_Elevations=SIMP(statut='o',typ='R'),
             ),
             b_Velocity   = BLOC (condition = "Type_Condition == 'Velocity'",
                Prescribed_Velocity=SIMP(statut='o',typ='R'),
         ),
       ),
       Stage_Discharge_Curves=SIMP(statut='f',typ='I',into=[0,1,2]),
       Stage_Discharge_Curves_File   = SIMP( statut='f', typ = ('Fichier', 'All Files (*)',),),
       Treatment_of_Fluxes_at_the_Boundaries   = SIMP( statut='f',typ='I',into=[1,2],sug=1),
       Option_for_tidal_Boundary_Conditions   = SIMP( statut='f',typ='I',into=[1,2],sug=1),
   ),
)

NUMERICAL_PARAMETERS=PROC(nom="NUMERICAL_PARAMETERS",op=None,
        Solver=FACT(statut='o',
          Equations=SIMP(statut='o',typ='TXM',into=['SAINT-VENANT EF','SAINT-VENANT VF','BOUSSINESQ'],sug='SAINT-VENANT EF'),
          Solver=SIMP(statut='o',typ='I',into=[1,2,3,4,6,7,8]),
          Solver_Accuracy=SIMP(statut='o',typ='R'),
          Maximum_Number_of_Iterations=SIMP(statut='o',typ='I'),
        ),
        Time=FACT(statut='f',
        regles=(AU_MOINS_UN('Number_of_time_Steps','Variable_Time_Step'),
                PRESENT_PRESENT('Time_Step','Duration',),),
           Number_of_Time_Steps=SIMP(statut='f',typ='I'),
           Time_Step=SIMP(statut='f',typ='R'),
           Duration=SIMP(statut='f',typ='R'),
           Variable_Time_Step=SIMP(statut='f',typ=bool),
        ),
        Linearity=FACT(statut='f',
           Treatment_of_Fluxes_at_the_Boundaries =SIMP( statut='f',typ='I',into=[1,2],sug=1),
           Continuity_Correction  =SIMP(typ=bool, statut='f'),
           Number_of_Sub_Iterations=SIMP(statut='f',typ='I'),
        ),
        Precondionning=FACT(statut='f',
          Preconditionning=SIMP(statut='f',typ='I',into=[0,2,3,7,11,14,21],sug=2),
          C_U_Preconditionning  =SIMP(typ=bool, statut='f',),
          Matrix_Vector_Product =SIMP(statut='f',typ='I',into=[1,2]),
          Matrix_Storage =SIMP(statut='f',typ='I',into=[1,3]),
          Mass_Lumping_on_H =SIMP(statut='f',typ='R',sug=0),
          Mass_Lumping_on_Velocity =SIMP(statut='f',typ='R',sug=0),
        ),
        Advection_Propagation=FACT(statut='f',
          Type_of_Advection=SIMP(statut='f',typ='I',min=4,max=4,into=[1,2,3,4,5,6,7,13,14],defaut=(1,5,1,1),),
          Advection_of_U_and_V=SIMP(statut='f',typ=bool),
          Advection_of_H=SIMP(statut='f',typ=bool),
          Advection_of_Tracers=SIMP(statut='f',typ=bool),
          Advection_of_K_and_Epsilon=SIMP(statut='f',typ=bool),

         b_upwind     =BLOC(condition = "2 in Type_of_Advection",
            Upwind_Coefficients=SIMP(statut='o',typ='R',min=4,max=4,)
           ),
          Linearized_Propoagation=SIMP(statut='f',typ=bool,sug=False),
          Mean_Depth_For_Linearity=SIMP(statut='f',typ='R',sug=0.0),
        ),
        Discretisation_Implicitation=FACT(statut='f',
          Discretisation_in_Space=SIMP(statut='f',typ='I',min=4,max=4,into=[11,12,13],defaut=(11,11,11),),
          Implicitation_for_Diffusion_of_velocity=SIMP(statut='f',typ='R',sug=0),
          Implicitation_for_Depth=SIMP(statut='f',typ='R',sug=0.55),
          Implicitation_for_Velocity=SIMP(statut='f',typ='R',sug=0.55),
          Free_Surface_Gradient_Compatibility=SIMP(statut='f',typ='R',sug=1.),
        ),
        Initial_Guess_for_H=SIMP(statut='f',typ='TXM',into=['zero','previous','extrapolation'],defaut='previous',),
        Initial_Guess_for_U=SIMP(statut='f',typ='TXM',into=['zero','previous','extrapolation'],defaut='previous',),
)

PHYSICAL_PARAMETERS=PROC(nom="PHYSICAL_PARAMETERS",op=None,
        Atmosphere=FACT(statut='f',
          Wind=SIMP(statut='f',typ=bool,sug=False),
          b_Wind     =BLOC(condition = "Wind=='True'",
            regles=( PRESENT_PRESENT('Wind_Velocity_along_X','Wind_Velocity_along_Y', ),),
            Coefficient_of_Wind_Influence=SIMP(statut='f',typ='R',sug=0,),
            Wind_Velocity_along_X=SIMP(statut='f',typ='R',sug=0,),
            Wind_Velocity_along_Y=SIMP(statut='f',typ='R',sug=0,),
            Threashold_Depth_for_Wind=SIMP(statut='f',typ='R',sug=0,),
            Air_Pressure=SIMP(statut='f',typ=bool,sug=False),
         ),
          Rain_or_Evaporation=SIMP(statut='f',typ=bool,sug=False),
          b_Rain     =BLOC(condition = "Rain_or_Evaporation=='True'",
            Rain_or_Evaporation_in_mm_perday=SIMP(statut='f',typ='I',sug=0),
                         ),
         ),
          Tide_Generating_Force=SIMP(statut='f',typ=bool,sug=False),
          b_Tide     =BLOC(condition = "Tide_Generating_Force=='True'",
              Tidal_Data_Base=SIMP(statut='f',typ='I',into=[-1,1,2,3,4]),
              Coefficient_To_Calibrate_Tidal_Range=SIMP(statut='f',typ='R',sug=1.),
              Coefficient_To_Calibrate_Tidal_Velocity=SIMP(statut='f',typ='R',sug=999999),
              Coefficient_To_Calibrate_Sea_Level=SIMP(statut='f',typ='R',sug=0.),
              Binary_Database_1_for_Tide  = SIMP( statut='f', typ = ('Fichier', '(All Files (*)',),),
              Binary_Database_2_for_Tide  = SIMP( statut='f', typ = ('Fichier', '(All Files (*)',),),
         ),
          Wave_Driver_Currents=SIMP(statut='f',typ=bool,sug=False),
          b_Wave     =BLOC(condition = "Wave_Driver_Currents=='True'",
              Record_Number_in_Wave_File=SIMP(statut='f',typ='I',sug=1),
         ),
)

POST_PROCESSING=PROC(nom="POST_PROCESSING",op=None,
   Graphic_Printouts=FACT(statut='f',
        Graphic_Printout_Period=SIMP(statut='o', typ='I',defaut=1),
        Number_of_First_TimeStep_For_Graphic_Printouts=SIMP(statut='o', typ='I',defaut=1),
        Variables_For_Graphic_Printouts=SIMP(statut='f',max="**", typ='TXM'),
        # ajouter le into
   ),
  Listing__Printouts=FACT(statut='f',
        Graphic_Printout_Period=SIMP(statut='o', typ='I',defaut=1),
        Number_of_First_TimeStep_For_Graphic_Printouts=SIMP(statut='o', typ='I',defaut=1),
        Variables_to_be_printed=SIMP(statut='f',max="**", typ='TXM'),
        # ajouter le into
   ),
)
