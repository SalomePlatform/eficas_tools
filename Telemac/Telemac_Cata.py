# coding: utf-8
# PNPNPNPN

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

import types
class Tuple:
  def __init__(self,ntuple):
    self.ntuple=ntuple

  def __convert__(self,valeur):
    if type(valeur) == types.StringType:
      return None
    if len(valeur) != self.ntuple:
      return None
    return valeur

  def info(self):
    return "Tuple de %s elements" % self.ntuple



JdC = JDC_CATA (code = 'MAP',
                execmodul = None,
                )
# ======================================================================
# Catalog entry for the MAP function : c_pre_interfaceBody_mesh
# ======================================================================
INITIALIZATION=PROC(nom="INITIALIZATION",op=None,
     fr="Initialisation des fichiers d'entrée et de sortie",
     ang="Input and Output files initialization",

     Title = SIMP( statut='o',typ='TXM',
            fr='Titre du cas etudie. Ce titre figurera sur les dessins.',
            ang='Title of the case being considered. This title shall be marked on the drawings.'
                 ),
     #Working_Directory = SIMP( statut='o',typ='Repertoire',defaut='/tmp'),

     Input_Files= FACT(statut='o',
          Dictionary = SIMP( statut='o', typ = ('Fichier', 'Dico (*.dico);;All Files (*)',), 
                            defaut='telemac2d.dico', 
                            fr='Dictionnaire des mots cles.', ang='Key word dictionary.',),

          Geometry_File_Format = SIMP( statut='o',typ='TXM',into=['SERAFIN','MED','SERAFIND'], defaut='SERAFIN',
                                 fr='Format du fichier de geometrie. Les valeurs possibles sont : \n \
     - SERAFIN : format standard simple precision pour Telemac;   \n \
     - SERAFIND: format standard double precision pour Telemac;   \n \
     - MED     : format MED base sur HDF5',
                                ang='Results file format. Possible values are: \n\
     - SERAFIN : classical single precision format in Telemac;\n\
     - SERAFIND: classical double precision format in Telemac;\n\
     - MED     : MED format based on HDF5',) ,

          Geometry_File  = SIMP( statut='o', typ = ('Fichier', 'Geo Files (*.geo);;All Files (*)',),
                           fr='Nom du fichier contenant le maillage du calcul a realiser.',
                           ang='Name of the file containing the mesh. \n\
       This file may also contain the topography and the friction coefficients.'),

          #Steering_File     = SIMP( statut='o', typ = ('Fichier', 'Steering Files (*.cas);;All Files (*)',),),

          Bottom_Topography_File  = SIMP( statut='f', typ = ('Fichier', 'Geo Files (*.geo);;All Files (*)',),
                            fr = "Nom du fichier eventuel contenant la bathymetrie associee au maillage. \
Si ce mot-cle est utilise; c'est cette bathymetrie qui sera utilisee pour le calcul.",
                            ang = 'Name of the possible file containing the bathymetric data.\
Where this keyword is used, these bathymetric data shall be used in the computation.',
         ),

          Fortran_File = SIMP(statut='f',typ = ('Fichier', 'Fortran files (*.f);;All Files (*)'),
                              fr='Nom du fichier a soumettre',
                              ang='Name of FORTRAN file to be submitted',),

          Boundary_Conditions_File = SIMP( statut='o', typ = ('Fichier', 'Boundary Condition (*.cli);;All Files (*)',),
          fr='Nom du fichier contenant les types de conditions aux limites. Ce fichier est rempli de facon automatique\n\
              par le mailleur au moyen de couleurs affectees aux noeuds des frontieres du domaine de calcul.',
          ang='Name of the file containing the types of boundary conditions. This file is filled automatically\n\
              by the mesh generator through through colours that are assigned to the boundary nodes.',),


     Validation=FACT( statut='f',

#PNPN--> creer le Mot_clef simple Validation si ce fact existe
          Reference_File_Format = SIMP( statut='o',typ='TXM',into=['SERAFIN','MED','SERAFIND'], defaut='SERAFIN',
                                fr = 'Format du fichier de resultats. Les valeurs possibles sont : \n\
     - SERAFIN : format standard simple precision pour Telemac;  \n\
     - SERAFIND: format standard double precision pour Telemac; \n\
     - MED     : format MED base sur HDF5' ,
                               ang = 'Results file format. Possible values are:\n \
     - SERAFIN : classical single precision format in Telemac;\n\
     - SERAFIND: classical double precision format in Telemac; \n\
     - MED     : MED format based on HDF5' ,),

             Reference_File     = SIMP( statut='o', typ = ('Fichier', 'Reference File (*.ref);;All Files (*)',), 
          fr= 'Fichier de resultats de reference pour la validation. Les resultats a placer dans ce fichier seront a ecrire sur le canal 22.',
          ang= 'Binary-coded result file for validation. The results to be entered into this file shall be written on channel 22.',),
     ), # Fin de Validation


     Formatted_And_Binary_Files=FACT( statut='f',

          Formatted_File2    = SIMP( statut='f', typ = ('Fichier', 'formated File (*.txt);;All Files (*)',),
            fr = "Fichier de donnees formate mis a la disposition de l'utilisateur. \n\
Les donnees de ce fichier seront a lire sur le canal 27.",
           ang = "Formatted data file made available to the user.\n\
The data in this file shall be read on channel 27.",
          ),
          Binary_Data_File1  = SIMP( statut='f', typ = ('Fichier', 'Reference File (*.txt);;All Files (*)',),
                  fr = 'Fichier de donnees code en binaire mis a la disposition de l utilisateur. \n\
Les donnees de ce fichier seront a lire sur le canal 24.',
                  ang = 'Binary-coded data file made available to the user.\n\
The data in this file shall be read on channel 24.',
          ),
          Binary_Data_File2  = SIMP( statut='f', typ = ('Fichier', 'Reference File (*.txt);;All Files (*)',),
                  fr = 'Fichier de donnees code en binaire mis a la disposition de l utilisateur.\n\
Les donnees de ce fichier seront a lire sur le canal 25.',
                   ang = 'Binary-coded data file made available to the user. \n\
The data in this file shall be read on channel 25.',
          ),
     ), # fin Formatted_And_Binary_Files

     ), # Fin de InputFile 


     Computation_Continued=FACT( statut='f',

#PNPNPN Computation_Continued == Validation
          Previous_Computation_File_Format=SIMP( statut='o',typ='TXM',
                into=['SERAFIN','MED','SERAFIND'],
                defaut='SERAFIN',
                fr='Format du fichier de resultats du calcul precedent. Les valeurs possibles sont : \n\
         - SERAFIN : format standard simple precision pour Telemac;  \n\
         - SERAFIND: format standard double precision pour Telemac; \n\
         - MED     : format MED base sur HDF5',
                ang='Previous computation results file format. Possible values are: \n\
         - SERAFIN : classical single precision format in Telemac;  \n\
         - SERAFIND: classical double precision format in Telemac; \n\
         - MED     : MED format based on HDF5',
                  ),

          Previous_Computation_File  = SIMP( statut='o', 
              typ = ('Fichier', 'Computation File (*.res);;All Files (*)',),
              fr = "Nom d'un fichier contenant les resultats d'un calcul precedent realise sur le meme maillage \n\
 et dont le dernier pas de temps enregistre va fournir les conditions initiales pour une suite de de calcul.",
               ang = 'Name of a file containing the results of an earlier computation which was made on the same mesh.\n\
 The last recorded time step will provid the initial conditions for the new computation.',
                    ),
          Previous_Computation_Comm  = SIMP( statut='f', typ = ('Fichier', 'COMM(*.comm);;All Files (*)',),
              fr  = "Nom du fichier .comm décrivant le cas précédent",
              ang = "Name of a file containing the earlier study" ,),
          Initial_Time_Set     = SIMP(typ=bool, statut='f',
             fr = 'Remet le temps a zero en cas de suite de calcul',
             ang = 'Initial time set to zero in case of restart',
             defaut="False"),
          Record_Number_For_Restart = SIMP(typ='I', statut='o', defaut=0,
              fr = "numero de l'enregistrement de depart dans le fichier du calcul precedent. 0 signifie qu'on prend le dernier enregistrement", 
              ang ="record number to start from in the previous computation file, 0 for last record" ),
     ),

     Computation=FACT(statut='o',
        #Machine=FACT( statut='o',
# A voir plus tar Obsolete ? 
        #   Parallel_Processors=SIMP(statut='o',typ='I',val_min=0,defaut=1),
           #Parallel_Computation=SIMP(statut='o',typ=bool,defaut=False),
        # ),
        Coupling=FACT( statut='o',
           Sisyphe=SIMP(statut='o',typ=bool,defaut=False),
           Tomawac=SIMP(statut='o',typ=bool,defaut=False),
          Delwacq=SIMP(statut='o',typ=bool,defaut=False),
        fr='Liste des codes avec lesquels on couple Telemac-2D\n\
     SISYPHE : couplage interne avec Sisyphe\n\
     TOMAWAC : couplage interne avec Tomawac\n\
     DELWAQ : sortie de fichiers de resultats pour Delwaq',
        ang='List of codes to be coupled with Telemac-2D\n\
     SISYPHE : internal coupling with Sisyphe\n\
     TOMAWAC : internal coupling with Tomawac\n\
     DELWAQ: will yield results file for Delwaq',
        ),
     ),
)

TIDE_PARAMETERS=PROC(nom="TIDE_PARAMETERS",op=None,
     fr="",
     ang="",
     Inputs_Outputs_For_Tide=FACT( statut='o',
        Harmonic_Constants_File = SIMP( statut='o',
          typ = ('Fichier', 'All Files (*)',),
          fr = 'Constantes harmoniques extraites du fichier du modele de maree',
          ang= 'Harmonic constants extracted from the tidalmodel file',
         ),

        Tidal_Model_File = SIMP( statut='o',
          typ = ('Fichier', 'All Files (*)',),
          fr = 'Fichier de geometrie du modele dont sont extraites les constantes harmoniques',
          ang= 'Geometry file of the model from which harmonic constituents are extracted',
         ),

      ),

     Time=FACT( statut='o',
       #Original_Date_Of_Time=SIMP(statut='f',typ=DateJJMMAAAA,validators=VerifTypeTuple(('R','R','R'))),
       #Original_Hour_Of_Time=SIMP(statut='f',typ=HeureHHMMSS,validators=VerifTypeTuple(('R','R','R'))),
       Original_Date_Of_Time=FACT( statut='o',
         fr = "Permet de fixer la date d'origine des temps du modele lors de la prise en compte de la force generatrice de la maree.",
         ang ='Give the date of the time origin of the model when taking into account the tide generating force.', 
         Year=SIMP(statut='o',typ='I',val_min=1900,defaut=1900),
         Month=SIMP(statut='o',typ='I',val_min=1,val_max=12,defaut=1),
         Day=SIMP(statut='o',typ='I',val_min=1,val_max=31,defaut=1),
          ),
       Original_Hour_Of_Time=FACT( statut='f',
         fr = "Permet de fixer l'heure d'origine des temps du modele lors de la prise en compte de la force generatrice de la maree.",
         ang ='Give the time of the time origin of the model when taking into account the tide generating force.', 
         Hour=SIMP(statut='o',typ='I',val_min=0,val_max=24,defaut=0),
         Minute=SIMP(statut='o',typ='I',val_min=0,val_max=60,defaut=0),
         Second=SIMP(statut='o',typ='I',val_min=0,val_max=60,defaut=0),
         ),
      ),
     Location=FACT( statut='f',
        #regles=( PRESENT_PRESENT('Longitude_Of_origin','Latitute_Of_origin', ),),
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
                 Latitude_Of_Origin=SIMP(statut='o',typ='R',val_min=-90,val_max=90,fr="en radians", ang="in radians"),
                 Longitude_Of_Origin=SIMP(statut='o',typ='R',fr="en radians", ang="in radians"),
                         ), # fin bloc b_lat
             ), # fin bloc b_geo
# declenchement du calcul du mot_clef SPHERICAL COORDINATES

        Zone_number_in_Geographic_System=SIMP(statut='f',typ='TXM',
            #into=[-1,0,1,2,3,4,22,30],
            into=[ 'LAMBERT 1 NORD', 'LAMBERT 2 CENTRE', 'LAMBERT 3 SUD', 'LAMBERT 4 CORSE', 'LAMBERT 2 ETENDU', 'ZONE UTM, PAR EXEMPLE'],
            fr="Numero de zone (fuseau ou type de projection) lors de l'utilisation d'une projection plane.\n Indiquer le systeme geographique dans lequel est construit le modele numerique avec le mot-cle SYSTEME GEOGRAPHIQUE",
            ang='Number of zone when using a plane projection. \nIndicate the geographic system in which the numerical model is built with the keyword GEOGRAPHIC SYSTEM'),
             ),
          Physical_Parameters=FACT(statut='o',
          Tide_Generating_Force=SIMP(statut='o',typ=bool,defaut=False),
          b_Tide  = BLOC(condition = "Tide_Generating_Force==True",
              Tidal_Data_Base=SIMP(statut='o',typ='TXM',
                into=[ "JMJ", "TPXO", "LEGOS-NEA", "FES20XX", "PREVIMER",],
fr = 'Pour JMJ, renseigner la localisation du fichier bdd_jmj et geofin dans les mots-cles BASE DE DONNEES DE MAREE \n\
et FICHIER DU MODELE DE MAREE.  Pour TPXO, LEGOS-NEA, FES20XX et PREVIMER, l utilisateur doit telecharger les fichiers \n\
de constantes harmoniques sur internet',
ang = 'For JMJ, indicate the location of the files bdd_jmj and geofin with keywords TIDE DATA BASE and TIDAL MODEL FILE.\n\
For TPXO, LEGOS-NEA, FES20XX and PREVIMER, the user has to download files of harmonic constituents on the internet',
             ),

#-1,1,2,3,4]),
              Coefficient_To_Calibrate_Tidal_Range=SIMP(statut='o',typ='R',sug=1.),
              Coefficient_To_Calibrate_Tidal_Velocity=SIMP(statut='o',typ='R',sug=999999),
              Coefficient_To_Calibrate_Sea_Level=SIMP(statut='o',typ='R',sug=0.),
              Binary_Database_1_for_Tide  = SIMP( statut='o', typ = ('Fichier', '(All Files (*),)',),),
              Binary_Database_2_for_Tide  = SIMP( statut='o', typ = ('Fichier', '(All Files (*),)',),),
                      ),

          Wave_Driven_Currents=SIMP(statut='f',typ=bool,sug=False),
          b_Wave     =BLOC(condition = "Wave_Driver_Currents=='True'",
              Record_Number_in_Wave_File=SIMP(statut='f',typ='I',sug=1),
         ),
         ),

       Option_For_Tidal_Boundary_Conditions   = SIMP( statut='o',typ='TXM',defaut='No tide',
       into=['No tide', 'Real tide (recommended methodology)', 'Astronomical tide', 'Mean spring tide', 'Mean tide',\
           'Mean neap tide', 'Astronomical neap tide', 'Real tide (methodology before 2010)'],
       ),
       b_Option_B = BLOC(condition ='Option_For_Tidal_Boundary_Conditions!="No tide"',
         Coefficient_To_Calibrate_Tidal_Velocities = SIMP( statut='o',typ='R',
               defaut=999999.0 ,
    fr = 'Coefficient pour ajuster les composantes de vitesse de londe de maree aux frontieres maritimes.  La valeur par defaut 999999. signifie que cest la racine carree du COEFFICIENT DE CALAGE DU MARNAGE qui est prise',
    ang= 'Coefficient to calibrate the tidal velocities of tidal wave at tidal open boundary conditions.  Default value 999999. means that the square root of COEFFICIENT TO CALIBRATE TIDAL RANGE is taken',
                 ),
         Coefficient_To_Calibrate_Sea_Level = SIMP( statut='o',typ='R',defaut=0,
           fr = 'Coefficient pour ajuster le niveau de mer',
           ang = 'Coefficient to calibrate the sea level',
                ),
         Coefficient_To_Calibrate_Tidal_Range = SIMP( statut='o',typ='R',
            defaut=1.,
            fr = 'Coefficient pour ajuster le marnage de l''onde de maree aux frontieres maritimes',
            ang = 'Coefficient to calibrate the tidal range of tidal wave at tidal open boundary conditions',
              ),
       ),

) # Fin TIDE_PARAMETERS

INITIAL_STATE=PROC(nom="INITIAL_STATE",op=None,

       Initial_Conditions=SIMP(statut='o',typ='TXM',
          into=['ZERO ELEVATION','CONSTANT ELEVATION','ZERO DEPTH','CONSTANT DEPTH','SPECIAL','TPXO SATELLITE ALTIMETRY'],
          defaut='ZERO ELEVATION',
          fr = "Permet de definir les conditions initiales sur les hauteurs d'eau. Les valeurs possibles sont :\n\
       - COTE NULLE. Initialise la cote de surface libre a 0. \nLes hauteurs d'eau initiales sont alors retrouvees en faisant la difference entre les cotes de surface libre et du fond. \n\
      - COTE CONSTANTE . Initialise la cote de surface libre a la valeur donnee par le mot-cle COTE INITIALE. Les hauteurs d'eau initiales sont calculees comme precedemment.\n\
      - HAUTEUR NULLE .Initialise les hauteurs d'eau a 0. \n\
      - HAUTEUR CONSTANTE. Initialise les hauteurs d'eau a la valeur donnee par le mot-cle HAUTEUR INITIALE. \n\
      - PARTICULIERES. Les conditions initiales sur la hauteur d'eau doivent etre precisees dans le sous-programme CONDIN. \n\
      - ALTIMETRIE SATELLITE TPXO. Les conditions initiales sur la hauteur  d'eau et les vitesses sont etablies sur \n\
        la base des donnees satellite TPXO dont les 8 premiers constistuents ont ete extraits et sauves dans le fichier\n\
         BASE DE DONNEES DE MAREE." ,
        ang = 'Makes it possible to define the initial conditions with the water depth. The possible values are : \n\
       - ZERO ELEVATION. Initializes the free surface elevation to 0. \n The initial water depths are then found by computing the difference between the free surface and the bottom.  \n\
       - CONSTANT ELEVATION. Initializes the water elevation to the value given by the keyword \n\
       - INITIAL ELEVATION. The initial water depths are computed as in the previous case. \n\
       - ZERO DEPTH. Initializes the water depths to 0. \n\
       - CONSTANT DEPTH. Initializes the water depths to the value givenby the key-word  INITIAL DEPTH. \n\
       - SPECIAL. The initial conditions with the water depth should be stated in the CONDIN subroutine. \n\
       - TPXO SATELITE ALTIMETRY. The initial conditions on the free surface and velocities are established from the TPXO satellite program data,\n the harmonic constituents of which are stored in the TIDE DATA BASE file.', ),
 
         b_initial_elevation = BLOC (condition = "Initial_Conditions == 'CONSTANT ELEVATION'",
           Initial_Elevation  = SIMP(statut='o',typ='R',
              fr='Valeur utilisee avec l''option :  CONDITIONS INITIALES - COTE CONSTANTE',
              ang='Value to be used with the option : INITIAL CONDITIONS  -CONSTANT ELEVATION' 
              ),
         ) , # fin b_initial_elevation

         b_initial_depth = BLOC (condition = "Initial_Conditions == 'CONSTANT DEPTH'",
           Initial_Depth = SIMP(statut='o',typ='R',
                fr='Valeur utilisee avec l''option : CONDITIONS INITIALES :-HAUTEUR CONSTANTE-',
                ang='Value to be used along with the option: INITIAL CONDITIONS -CONSTANT DEPTH-' ),
         ),# fin b_initial_depth
 
         b_special= BLOC (condition = "Initial_Conditions == 'SPECIAL'",
           # Ce mot clef est juste informatif
           special    = SIMP(statut='o',typ='TXM',
           defaut="The initial conditions with the water depth should be stated in the CONDIN subroutine"),
         ), # fin b_special


         b_initial_TPXO = BLOC (condition = "Initial_Conditions == 'TPXO SATELLITE ALTIMETRY'",
           Base_Ascii_De_Donnees_De_Maree = SIMP( statut='o', typ = ('Fichier', 'All Files (*)',), ),
           fr  = 'Base de donnees de constantes harmoniques tirees du fichier du modele de maree',
           ang = 'Tide data base of harmonic constituents extracted from the tidal model file',
         ), # fin b_initial_TPXO
) # fin INITIAL_STATE

BOUNDARY_CONDITIONS=PROC(nom="BOUNDARY_CONDITIONS",op=None,
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
                
            Options=SIMP(statut='f',typ='I',
            into=['classical boundary conditions','Thompson method based on characteristics'],
            fr='On donne 1 entier par frontiere liquide',
            ang='One integer per liquid boundary is given',
            ),

        Type_Condition=SIMP(statut='o',typ='TXM',into=['Prescribed Flowrates','Prescribed Elevations','Prescribed Velocity'],),
#?????
# PN On ajouter le type pour rendre l 'ihm plus lisible
# mais ce mot-cle n existe pas dans le dico

         b_Flowrates     = BLOC (condition = "Type_Condition == 'Prescribed Flowrates'",
             Prescribed_Flowrates=SIMP(statut='o',typ='R',
             fr=' Valeurs des debits imposes aux frontieres liquides entrantes.\n Lire la partie du mode d''emploi consacree aux conditions aux limites',
            ang='Values of prescribed flowrates at the inflow boundaries.\n The section about boundary conditions is to be read in the manual'),
             ),

         b_Elevations   = BLOC (condition = "Type_Condition == 'Prescribed Elevations'",
                Prescribed_Elevations=SIMP(statut='o',typ='R',
                fr='Valeurs des cotes imposees aux frontieres liquides entrantes.\n Lire la partie du mode d''emploi consacree aux conditions aux limites',
                ang='Values of prescribed elevations at the inflow boundaries.\n The section about boundary conditions is to be read in the manual'),
             ),

         b_Velocity   = BLOC (condition = "Type_Condition == 'Prescribed Velocity'",
               Prescribed_Velocity=SIMP(statut='o',typ='R',
               fr='Valeurs des vitesses imposees aux frontieres liquides entrantes.\n Lire la partie du mode d''emploi consacree aux conditions aux limites',
               ang='Values of prescribed velocities at the liquid inflow boundaries.\n Refer to the section dealing with the boundary conditions'),
         ),

       ), # fin des Liquid_Boundaries
       Liquid_Boundaries_File = SIMP( statut='f', typ = ('Fichier', 'All Files (*)',),
         fr = 'Fichier de variations en temps des conditions aux limites.\n\
Les donnees de ce fichier seront a lire sur le canal 12.',
         ang = 'Variations in time of boundary conditions. Data of this file are read on channel 12.',
      ),
   

#PNPN Attention dans le Dico STAGE-DISCHARGE CURVES
       Stage_Discharge_Curves = SIMP(statut='f',typ='TXM',
        #into=[0,1,2],
        into=["no","Z(Q)","not programmed"],
        fr='Indique si une courbe de tarage doit etre utilisee pour une frontiere',
        ang='Says if a discharge-elevation curve must be used for a given boundary',
        ),
        b_discharge_curve   = BLOC (condition = "Stage_Discharge_Curves == 'Z(Q)'",

#PNPN Attention dans le Dico STAGE-DISCHARGE CURVES FILES
        Stage_Discharge_Curves_File   = SIMP( statut='f', typ = ('Fichier', 'All Files (*)',),
          fr='Nom du fichier contenant les courbes de tarage',
          ang='Name of the file containing stage-discharge curves',
          ),
        ),

      Elements_Masked_By_User =SIMP(statut='o',typ=bool,
       defaut=False,
       fr = 'Si oui remplir le sous-programme maskob',
       ang = 'if yes rewrite subroutine maskob',
      ),
      maskob = BLOC (condition = 'Elements_Masked_By_User==True',
      Consigne = SIMP(statut="o",homo='information',typ="TXM", defaut="Remplir le sous-programme maskob"),
      )

) # fin Boundary_Conditions


NUMERICAL_PARAMETERS=PROC(nom="NUMERICAL_PARAMETERS",op=None,

        Solver_Definition=FACT(statut='o',

          Equations=SIMP(statut='o',typ='TXM',
             into=['SAINT-VENANT EF','SAINT-VENANT VF','BOUSSINESQ'],
             defaut='SAINT-VENANT EF',
             fr='Choix des equations a resoudre',
             ang= 'Choice of equations to solve',
             ),

          Solver=SIMP(statut='o',typ='TXM',
           into = ["conjugate gradient", "conjugate residual","conjugate gradient on a normal equation",\
                   "minimum error", "cgstab", "gmres", "direct",],
           fr = 'Permet de choisir le solveur utilise pour la resolution de l''etape de propagation. \n\
Toutes les methodes proposees actuellement s''apparentent au Gradient Conjugue. Ce sont :\n\
  1 : gradient conjugue 2 : residu conjugue       3 : gradient conjugue sur equation normale \n\
  4 : erreur minimale   5 : gradient conjugue carre (non programme) 6 : gradient conjugue carre stabilise (cgstab)\n\
  7 : gmres (voir aussi option du solveur) 8 : direct',
ang = 'Makes it possible to select the solver used for solving the propagation step.\n\
All the currently available methods are variations of the Conjugate Gradient method. They are as follows: \n\
1: conjugate gradient 2: conjugate residual 3: conjugate gradient on a normal equation\n\
4: minimum error 5: conjugate gradient squared (not implemented) 6: conjugate gradient squared stabilised (cgstab) \n\
7: gmres (see option for solver) 8: direct',
            ),

          b_gmres = BLOC (condition = "Solver == 'gmres'",
          Solver_Option = SIMP(statut='o',typ='I', defaut=2, val_min=2,val_max=15,
              fr = 'la dimension de l''espace de KRILOV',
              ang = 'dimension of the KRYLOV space',
               ),
          ),

          Solver_Accuracy = SIMP(statut='o',typ='R', defaut=1e-4,
            fr = 'Precision demandee pour la resolution de l''etape de propagation (cf.  Note de principe).',
            ang = 'Required accuracy for solving the propagation step (refer to Principle note).',
           ),

          Maximum_Number_Of_Iterations_For_Solver=SIMP(statut='o',typ='I', defaut=40,
          fr = 'Les algorithmes utilises pour la resolution de l''etape de propagation etant iteratifs, \n\
il est necessaire de limiter le nombre d''iterations autorisees.\n\
Remarque : un maximum de 40 iterations par pas de temps semble raisonnable.',
          ang = 'Since the algorithms used for solving the propagation step are iterative, \
the allowed number of iterations should be limited.\n\
Note: a maximum number of 40 iterations per time step seems to be reasonable.',
           ),
        ), # fin Solver

        Time=FACT(statut='f',
        regles=(AU_MOINS_UN('Number_Of_Time_Steps','Duration'),
                EXCLUS('Number_Of_Time_Steps','Duration'),
               ),

           Time_Step=SIMP(statut='o',typ='R'),
           Number_Of_Time_Steps=SIMP(statut='f',typ='I',
              fr='Definit le nombre de pas de temps effectues lors de l''execution du code.',
              ang='Specifies the number of time steps performed when running the code.'),
           Duration=SIMP(statut='f',typ='R'),
           Variable_Time_Step=SIMP(statut='f',typ=bool),
           b_var_time  = BLOC(condition = "Variable_Time_Step==True" ,
             Desired_Courant_Number=SIMP(statut='o',typ='R'),
           ),

           Stop_If_A_Steady_State_Is_Reached=SIMP(statut='f',typ=bool,defaut='False'),
           b_stop  = BLOC(condition = "Stop_If_A_Steady_State_Is_Reached==True" ,

           Stop_Criteria=SIMP(statut='o',typ=Tuple(3),validators=VerifTypeTuple(('R','R','R')),
            fr = "Criteres d'arret pour un ecoulement permanent. ces coefficients sont respectivement appliques a\n\
        1- U et V 2- H 3- T ",
            ang = 'Stop criteria for a steady state These coefficients are applied respectively to\n\
        1- U and V 2- H 3-  T ',),
                    ),

           Control_Of_Limit=SIMP(statut='f',typ=bool,defaut='False',
fr = 'Le programme s''arrete si les limites sur u,v,h ou t sont depassees',
ang = 'The program is stopped if the limits on u,v,h, or t are trespassed',
           ),

           b_limit  = BLOC(condition = "Control_Of_Limit==True" ,

              Limit_Values=FACT(statut='o',
                  fr = 'valeurs mini et maxi acceptables  min puis  max',
                  ang= 'min and max acceptable values ',
                  Limit_Values_H=SIMP(statut='o',typ=Tuple(2),validators=VerifTypeTuple(('R','R')),defaut=(-1000,9000)),
                  Limit_Values_U=SIMP(statut='o',typ=Tuple(2),validators=VerifTypeTuple(('R','R')),defaut=(-1000,1000)),
                  Limit_Values_V=SIMP(statut='o',typ=Tuple(2),validators=VerifTypeTuple(('R','R')),defaut=(-1000,1000)),
                  Limit_Values_T=SIMP(statut='o',typ=Tuple(2),validators=VerifTypeTuple(('R','R')),defaut=(-1000,1000)),
                               ),
                  ),
    ), # Fin de Time

     Linearity=FACT(statut='f',
           Continuity_Correction  =SIMP(typ=bool, statut='o',defaut=False,
             fr = 'Corrige les vitesses sur les points avec hauteur imposee ou l''equation de continuite n''a pas ete resolue',
            ang = 'Correction of the velocities on points with a prescribed elevation, where the continuity equation has not been solved',
            ),
           Number_Of_Sub_Iterations_For_Non_Linearity=SIMP(statut='o',typ='I',defaut=1,
fr = 'Permet de reactualiser, pour un meme pas de temps, les champs convecteur et propagateur au cours de plusieurs sous-iterations.\n\
A la premiere sous-iteration, ces champs sont donnes par C et le champ de vitesses au pas de temps precedent.\n\
Aux iterations suivantes, ils sont pris egaux au champ de vitesse obtenu a la fin de la sous-iteration precedente. \n\
Cette technique permet d''ameliorer la prise en compte des non linearites.',
ang = 'Used for updating, within one time step, the advection and propagation field.  upon the first sub-iteration, \n\
these fields are given by C and the velocity field in the previous time step. At subsequent iterations, \n\
the results of the previous sub-iteration is used to update the advection and propagation field.\n\
The non-linearities can be taken into account through this technique.',),
     ),
     Precondionning_setting=FACT(statut='f',

          Preconditionning=SIMP(statut='f',typ='I',
              into=[ "diagonal", "no preconditioning", "diagonal condensee", "crout", \
                     "gauss-seidel", "diagonal and crout", "diagonal condensed and crout"],
          ),
          C_U_Preconditionning  =SIMP(typ=bool, statut='f',
             fr = 'Changement de variable de H en C dans le systeme lineaire final',
            ang = 'Change of variable from H to C in the final linear system'
           ),
        ),# fin Preconditionnement
     
     
     Matrix_Informations=FACT(statut='f',
          Matrix_Vector_Product =SIMP(statut='f',typ='TXM',
             into=["classic", "frontal"],
             fr='attention, si frontal, il faut une numerotation speciale des points',
             ang='beware, with option 2, a special numbering of points is required',
          ),
          Matrix_Storage =SIMP(statut='f',typ='TXM',
             into=["EBE classique","Stockage par segments",]
          ),
     ),# fin Matrix_Informations

     Advection=FACT(statut='o',
 
        Advection_Propagation=FACT(statut='o',
          Advection_Of_U_And_V=SIMP(statut='o',typ=bool,defaut=False,
            fr = 'Prise en compte ou non de la convection de U et V.',
            ang= 'The advection of U and V is taken into account or ignored.'
            ),

          b_u_v = BLOC( condition = "Advection_Of_U_And_V==True",
          Type_Of_Advection_U_And_V=SIMP(statut='o',typ='TXM',position="global",
          into=["characteristics", "SUPG", "Conservative N-scheme",  'Conservative N-scheme',\
                 'Conservative PSI-scheme', 'Non conservative PSI scheme', 'Implicit non conservative N scheme',\
                 'Edge-based N-scheme'],
          defaut="characteristics",

                 ),
           b_upwind     =BLOC(condition = "Type_Of_Advection_U_And_V== 'SUPG'",
            Upwind_Coefficients_Of_U_And_V=SIMP(statut='o',typ='R',defaut=1.)
               ),
           ),

          Advection_Of_H=SIMP(statut='o',typ=bool,defaut=False,
            fr = 'Prise en compte ou non de la convection de H.',
            ang= 'The advection of H is taken into account or ignored.'
            ),

          b_h = BLOC( condition = "Advection_Of_H==True",

          Type_Of_Advection_H=SIMP(statut='o',typ='TXM',position="global",
          into=["characteristics", "SUPG", "Conservative N-scheme",  'Conservative N-scheme',\
                 'Conservative PSI-scheme', 'Non conservative PSI scheme', 'Implicit non conservative N scheme',\
                 'Edge-based N-scheme'],
          defaut="Conservative PSI-scheme",
                 ),
           b_upwind_H     = BLOC(condition = "Type_Of_Advection_H== 'SUPG'",
            Upwind_Coefficients_Of_H=SIMP(statut='o',typ='R',defaut=1.)
               ),
           ),


         Advection_Of_K_And_Epsilon=SIMP(statut='o',typ=bool,defaut=False,
           fr = 'Prise en compte ou non de la convection de Tracer.',
            ang= 'The advection of Tracer is taken into account or ignored.'
            ),

          b_k = BLOC( condition = "Advection_Of_K_And_Epsilon==True",

          Type_Of_Advection_K_And_Epsilon=SIMP(statut='o',typ='TXM',position="global",
          into=["characteristics", "SUPG", "Conservative N-scheme",  'Conservative N-scheme',\
                 'Conservative PSI-scheme', 'Non conservative PSI scheme', 'Implicit non conservative N scheme',\
                 'Edge-based N-scheme'],
          defaut="characteristics",
                 ),
           b_upwind_k     =BLOC(condition = "Type_Of_Advection_K_And_Epsilon== 'SUPG'",
            Upwind_Coefficients_Of_K_And_Epsilon=SIMP(statut='o',typ='R',defaut=1.)
               ),
           ),

          Advection_Of_Tracers=SIMP(statut='o',typ=bool,defaut=False,
            fr = 'Prise en compte ou non de la convection de Tracer.',
            ang= 'The advection of Tracer is taken into account or ignored.'
            ),

          b_tracers = BLOC( condition = "Advection_Of_Tracers==True",

          Type_Of_Advection_Tracers=SIMP(statut='o',typ='TXM',position="global",
          into=["characteristics", "SUPG", "Conservative N-scheme",  'Conservative N-scheme',\
                 'Conservative PSI-scheme', 'Non conservative PSI scheme', 'Implicit non conservative N scheme',\
                 'Edge-based N-scheme'],
                 ),
           b_upwind_Tracers     =BLOC(condition = "Type_Of_Advection_Tracers== 'SUPG'",
            Upwind_Coefficients_Of_Tracers=SIMP(statut='o',typ='R',defaut=1.)
               ),
           ),

          b_max=BLOC( condition = "(Advection_Of_Tracers==True and Type_Of_Advection_Tracers=='Edge-based N-scheme') or (Advection_Of_K_And_Epsilon==True and Type_Of_Advection_K_And_Epsilon=='Edge-based N-scheme') or (Advection_Of_U_And_V==True and Type_Of_Advection_U_And_V=='Edge-based N-scheme') or ( Advection_Of_H == True and Type_Of_Advection_H=='Edge-based N-scheme')",
            Maximum_Number_Of_Iterations_For_Advection_Schemes = SIMP( statut='o',typ='I', defaut=10 ,
               fr = 'Seulement pour schemes Edge-based N-scheme',
               ang= 'Only for Edge-based N-scheme',
                ),
          ),
        ),

#PNPNPN
# recalculer la liste de 4
# Attention bloc selon le type de convection
     SUPG=FACT(statut='o',
        Supg_Option_U_And_V=SIMP(statut='o',defaut='modified SUPG',typ='TXM',into=['no upwinding', 'classical SUPG','modified SUPG']),
        Supg_Option_H=SIMP(statut='o',defaut='modified SUPG',typ='TXM',into=['no upwinding', 'classical SUPG','modified SUPG']),
        Supg_Option_Tracers=SIMP(statut='o',defaut='modified SUPG',typ='TXM',into=['no upwinding', 'classical SUPG','modified SUPG']),
        Supg_Option_K_and_Epsilon=SIMP(statut='o',defaut='modified SUPG',typ='TXM',into=['no upwinding', 'classical SUPG','modified SUPG']),
         ),

          Mass_Lumping_On_H =SIMP(statut='f',typ='R',defaut=0,
            fr = 'TELEMAC offre la possibilite d''effectuer du mass-lumping sur H ou U.\n\
Ceci revient a ramener tout ou partie (suivant la valeur de ce coefficient) des matrices AM1 (h) ou AM2 (U) \n\
et AM3 (V) sur leur diagonale.  Cette technique permet d''accelerer le code dans des proportions tres\n\
importantes et de le rendre egalement beaucoup plus stable. Cependant les solutions obtenues se trouvent lissees.\n\
Ce parametre fixe le taux de mass-lumping effectue sur h.',
            ang = 'TELEMAC provides an opportunity to carry out mass-lumping either on C,H or on the velocity. \n\
This is equivalent to bringing the matrices AM1(h) or AM2(U) and AM3(V) wholly or partly, back onto their diagonal.\n\
Thanks to that technique, the code can be speeded up to a quite significant extent and it can also be made much \n\
more stable. The resulting solutions, however, become artificially smoothed. \n\
This parameter sets the extent of mass-lumping that is performed on h.'),

          Mass_Lumping_On_Velocity =SIMP(statut='f',typ='R',defaut=0,
            fr = 'Fixe le taux de mass-lumping effectue sur la vitesse.',
            ang = 'Sets the amount of mass-lumping that is performed on the velocity.'
),


#PNPNPNPN
#
# Attention a recalculer
# Il faut recalculer des listes de 4 en sortie
#
       Treatment_Of_The_Linear_System=SIMP(statut='f', typ='TXM',
#CHOIX1 = '1="coupled"';'2="Wave equation"'
           into=["coupled","Wave equation"],
           defaut="coupled",
       ),
       Free_Surface_Gradient_Compatibility=SIMP(statut='f',typ='R',defaut=1.,
            fr = 'Des valeurs inferieures a 1 suppriment les oscillations parasites',
            ang = 'Values less than 1 suppress spurious oscillations'
       ),

 ), # fin Advection

        Propagation=FACT(statut='f',
#PNPNPN Il faut recalculer le MCSIM Propagation
          Linearized_Propagation=SIMP(statut='o',typ=bool,defaut=False),
          b_linear     =BLOC(condition = "Linearized_Propagation==True ",
            Mean_Depth_For_Linearity=SIMP(statut='o',typ='R',defaut=0.0,val_min=0),
          ),
          Initial_Guess_for_H=SIMP(statut='f',typ='TXM',into=['zero','previous','extrapolation'],defaut='previous',
         fr = 'Tir initial du solveur de l etape de propagation.  Offre la possibilite de modifier la valeur initiale de DH,\n\
accroissement de H, a chaque iteration, dans l etape de propagation en utilisant les valeurs finales de cette variable \n\
aux pas de temps precedents. Ceci peut permettre daccelerer la vitesse de convergence lors de la resolution du systeme.',
    ang= 'Initial guess for the solver in the propagation step.  Makes it possible to modify the initial value of H, \n\
upon each iteration in the propagation step, by using the ultimate values this variable had in the earlier time steps.\n\
Thus, the convergence can be speeded up when the system is being solved.',
),
          Initial_Guess_for_U=SIMP(statut='f',typ='TXM',into=['zero','previous','extrapolation'], defaut='previous',
         fr = 'Tir initial du solveur de l etape de propagation.  Offre la possibilite de modifier la valeur initiale de DH,\n\
accroissement de U, a chaque iteration, dans l etape de propagation en utilisant les valeurs finales de cette variable \n\
aux pas de temps precedents. Ceci peut permettre daccelerer la vitesse de convergence lors de la resolution du systeme.',
    ang= 'Initial guess for the solver in the propagation step.  Makes it possible to modify the initial value of U, \n\
upon each iteration in the propagation step, by using the ultimate values this variable had in the earlier time steps.\n\
Thus, the convergence can be speeded up when the system is being solved.',
),
),
        Discretisation_Implicitation=FACT(statut='f',
          Discretisations_In_Space=SIMP(statut='f',typ='TXM', 
            into =["linear for velocity and depth", "quasi-bubble-velocity and linear depth", "quadratic velocity and linear depth"],
            defaut="linear for velocity and depth",),
          Implicitation_For_Depth=SIMP(statut='f',typ='R',defaut=0.55,
fr = 'Fixe la valeur du coefficient d''implicitation sur C dans l''etape de propagation (cf.  Note de principe).\n\
Les valeurs inferieures a 0.5 donnent un schema instable.',
ang = 'Sets the value of the implicitation coefficient for C (the celerity of waves) in the propagation step (refer to principle note).\n\
Values below 0.5 result in an unstable scheme.'),

          Implicitation_for_Velocity=SIMP(statut='f',typ='R',defaut=0.55,
fr = 'Fixe la valeur du coefficient d''implicitation sur la vitesse dans l''etape de propagation (cf.  Note de principe).\n\
Les valeurs inferieures a 0.5 donnent un schema instable.',
ang= 'Sets the value of the implicitation coefficient for velocity in the propagation step (refer to principle note).\n\
Values below 0.5 result in an unstable condition.'),

          Implicitation_For_Diffusion_Of_Velocity=SIMP(statut='f',typ='R',defaut=0,
          fr = 'Fixe la valeur du coefficient d''implicitation sur les termes de diffusion des vitesses',
          ang = 'Sets the value of the implicitation coefficient for the diffusion of velocity',
              ),
        ),
      

        Tidal_Flats=SIMP(statut='o',typ=bool,defaut=False,
fr='permet de supprimer les tests sur les bancs decouvrants, dans les cas ou l''on est certain qu''il n''y en aura pas, En cas de doute : oui',
ang='When no,the specific treatments for tidal flats are by-passed. This spares time, but of course you must be sure that you have no tidal flats'
        ),
        b_tidal_flats=BLOC(condition='Tidal_Flats==True',

           Option_For_The_Treatment_Of_Tidal_Flats=SIMP(statut='o',typ='TXM',
        into=["Equations resolues partout avec correction sur les bancs decouvrants",\
        "gel des elements decouvrants","comme 1 mais avec porosite (methode defina)"],
        defaut="equations resolues partout avec correction sur les bancs decouvrants",
                                   ),
                    b_option_tidal_flats=BLOC(condition='Option_For_The_Treatment_Of_Tidal_Flats=="Equations resolues partout avec correction sur les bancs decouvrants"',
                      Treatment_Of_Negative_Depths = SIMP( statut='o',typ='TXM',
                       into=[ 'no treatment', 'smoothing', 'flux control'],
                       defaut='smoothing' ,),
                     ),
          Threshold_For_Negative_Depths = SIMP( statut='o',typ='R', defaut=0.0 ,
             fr = 'En dessous du seuil, les hauteurs negatives sont lissees',
             ang= 'Below the threshold the negative depths are smoothed',
             ),
          
          H_Clipping=SIMP(statut='o',typ=bool,defaut=False,
                fr = 'Determine si l''on desire ou non limiter par valeur inferieure la hauteur d''eau H (dans le cas des bancs decouvrants par exemple).',
              ang = 'Determines whether limiting the water depth H by a lower value desirable or not. (for instance in the case of tidal flats)\n\
This key-word may have an influence on mass conservation since the truncation of depth is equivalent to adding mass.',),

        b_clipping=BLOC(condition='H_Clipping==True',
          Minimum_Value_Of_Depth = SIMP( statut='o',typ='R', defaut=0.0 ,
    fr = 'Fixe la valeur minimale de a lorsque loption CLIPPING DE H est activee.',
    ang= 'Sets the minimum H value when option H CLIPPING is implemented. Not fully implemented.',),
              ),
     ),

   Turbulence=FACT(statut='f',
      Solver_For_K_epsilon_Model = SIMP( statut='o',typ='TXM',
            defaut="conjugate gradient" ,
   into =("conjugate gradient", "conjugate residuals", "conjugate gradient on normal equation", "minimum error", "conjugate gradient squared",\
        "conjugate gradient squared stabilised (cgstab)", "gmres", "direct"),
   #into =('1="conjugate gradient"', '2="conjugate residuals"', '3="conjugate gradient on normal equation"', '4="minimum error"', '5="conjugate gradient squared"', '6="conjugate gradient squared stabilised (cgstab)"', '7="gmres (see option for the solver for k-epsilon model)"', '8="direct"'),
    fr = 'Permet de choisir le solveur utilise pour la resolution du systeme du modele k-epsilon',
    ang= 'Makes it possible to select the solver used for solving the system of the k-epsilon model.',
     ),

       b_gmres=BLOC(condition='Solver_For_K_epsilon_Model=="gmres"',
         Option_For_The_Solver_For_K_epsilon_Model = SIMP( statut='o',typ='I',
              defaut=2 ,val_min=2,val_max=15,
              fr = 'le mot cle est la dimension de lespace de KRILOV (valeurs conseillees entre 2 et 7)',
              ang= 'dimension of the krylov space try values between 2 and 7',),
            ),

      Preconditioning_For_K_epsilon_Model = SIMP( statut='o',typ='TXM',
         defaut='diagonal' ,
         into =("diagonal", "no preconditioning", "diagonal condensed", "crout", "diagonal and crout", "diagonal condensed and crout"),
   #into =('2="diagonal"', '0="no preconditioning"', '3="diagonal condensed"', '7="crout"', '14="diagonal and crout"', '21="diagonal condensed and crout"'),
         fr = 'Permet de preconditionner le systeme relatif au modele k-epsilon',
         ang= 'Preconditioning of the linear system in the diffusion step of the k-epsilon model.',
     ),

    Turbulence_Model = SIMP( statut='o',typ='TXM', defaut="CONSTANT VISCOSITY", 
   #into =('1="CONSTANT VISCOSITY"', '2="ELDER"', '3="K-EPSILON MODEL"', '4="SMAGORINSKI"'),
   into =("Constant Viscosity", "Elder", "K-Epsilon Model", "Smagorinski"),
    
    fr = 'si on choisit loption 2 il ne faut pas oublier dajuster les deux valeurs du mot-cle : COEFFICIENTS ADIMENSIONNELS DE DISPERSION Si on choisit loption 3, ce meme parametre doit retrouver sa vraie valeur physique car elle est utilisee comme telle dans le modele de turbulence',
    ang= 'When option 2 is chosen, the two values of key-word : NON-DIMENSIONAL DISPERSION COEFFICIENTS are used When option 3 is chosen, this parameter should recover its true physical value, since it is used as such in the turbulence model.',
     ),

    b_turbu_const=BLOC(condition='Turbulence_Model=="Constant Viscosity"',
      Velocity_Diffusivity=SIMP( statut='o',typ='R',defaut=1.E-6,
      fr='Fixe de facon uniforme pour l ensemble du domaine la valeur du coefficient de diffusion de viscosite globale (dynamique + turbulente).\n\
Cette valeur peut avoir une influence non negligeable sur la forme et la taille des recirculations.',
      ang = 'Sets, in an even way for the whole domain, the value of the coefficient of global (dynamic+turbulent) viscosity. \n\
this value may have a significant effect both on the shapes and sizes of recirculation zones.',),

    ),
    b_turbu_elder=BLOC(condition='Turbulence_Model=="Elder"',
 Non_Dimensional_Dispersion_Coefficients = SIMP (statut='o',
          typ=Tuple(2),validators=VerifTypeTuple(('R','R')),defaut=(6.,0.6),
          fr = 'coefficients longitudinal et transversal dans la formule de Elder.',
           ang = 'Longitudinal and transversal coefficients in elder s formula.  Used only with turbulence model number 2',),
    ),

     Accuracy_Of_K = SIMP( statut='o',typ='R', defaut=1e-09 ,
            fr = 'Fixe la precision demandee sur k pour le test darret dans letape de diffusion et termes sources du modele k-epsilon.',
            ang= 'Sets the required accuracy for computing k in the diffusion and source terms step of the k-epsilon model.',
     ),

     Accuracy_Of_Epsilon = SIMP( statut='o',typ='R', defaut=1e-09 ,
           fr = 'Fixe la precision demandee sur epsilon pour le test darret dans letape de diffusion et termes sources de k et epsilon.',
           ang= 'Sets the required accuracy for computing epsilon in the diffusion and source-terms step of the k-epsilon model.',
     ),
     Time_Step_Reduction_For_K_epsilon_Model = SIMP( statut='f',typ='R', defaut=1.0 ,
    fr = 'Coefficient reducteur du pas de temps pour le modele k-epsilon (qui est normalement identique a celui du systeme hydrodynamique).\n\
Utilisation deconseillee',
    ang= 'Time step reduction coefficient for k-epsilon model (which is normally same the same as that of the hydrodynamic system).\n\
Not recommended for use.',
     ),
     Maximum_Number_Of_Iterations_For_K_And_Epsilon = SIMP( statut='o',typ='I',
               defaut=50 ,
           fr = 'Fixe le nombre maximum diterations accepte lors de la resolution du systeme diffusion-termes sources du modele k-epsilon.',
           ang= 'Sets the maximum number of iterations that are acceptable when solving the diffusion source-terms step of the k-epsilon model.',
     ),
     Turbulence_Model_For_Solid_Boundaries = SIMP( statut='o',typ='TXM',
         defaut='rough' ,
         #into =('1=smooth', '2=rough'),
         into =('smooth', 'rough'),
         fr = 'Permet de choisir le regime de turbulence aux parois ',
         ang= 'Provided for selecting the type of friction on the walls',
     ),


     ),# fin Turbulence

     Various=FACT(
         Finite_Volume_Scheme = SIMP( statut='o',typ='TXM',
              #CHoix de 0 a 6
              into=[ "Roe scheme", "kinetic order 1", "kinetic order 2", "Zokagoa scheme order 1",\
                     "Tchamen scheme order 1", "HLLC scheme order 1", "WAF scheme order 2"],
              defaut="kinetic order 1",
         ),
         Newmark_Time_Integration_Coefficient = SIMP( statut='o',typ='R',
             defaut=1.0 ,
             fr = '1. : Euler explicite 0.5 : ordre 2 en temps',
              ang= '1. : Euler explicit 0.5 : order 2 in time',
          ),
        Option_For_Characteristics = SIMP( statut='o',typ='TXM',
            defaut="strong form" ,
            into=['strong form','weak form',],
            ),
     ),
    Mass_Lumping_For_Weak_Characteristics=SIMP(statut='f',typ='R',defaut=0,
        fr = 'Applique a la matrice de masse',
        ang = 'To be applied to the mass matrix',
     ),
   
)# fin NUMERICAL_PARAMETERS

PHYSICAL_PARAMETERS=PROC(nom="PHYSICAL_PARAMETERS",op=None,
        Atmosphere=FACT(statut='f',
          Wind=SIMP(statut='f',typ=bool,sug=False),
          b_Wind     =BLOC(condition = "Wind=='True'",
            regles=( PRESENT_PRESENT('Wind_Velocity_along_X','Wind_Velocity_along_Y', ),),
            Coefficient_Of_Wind_Influence=SIMP(statut='f',typ='R',sug=0,),
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


          Friction_Data=SIMP(statut='o',typ=bool,defaut=False),
          b_Friction  = BLOC(condition = "Friction_Data==True",
             Friction_Data_File = SIMP( statut='o',
               typ = ('Fichier', ';;All Files (*)'),
               fr = 'fichier de donnees pour le frottement',
               ang= 'friction data file',
              ),
              Depth_In_Friction_Terms = SIMP( statut='o',typ='TXM',
               defaut= '1="nodal"' ,
               into =('1="nodal"', '2="average"'),
               fr = '1 : nodale 2 : moyenne',
               ang= '1: nodal   2: average',
             ),
             Law_Of_Bottom_Friction = SIMP( statut='o',typ='TXM',
             defaut='0="NO FRICTION"' ,
             into =('0="NO FRICTION"', '1="HAALAND"', '2="CHEZY"', '3="STRICKLER"', '4="MANNING"', '5="NIKURADSE"','Log Law of Boundaries 6','Colebrooke_White Log 7'),
             fr = 'selectionne le type de formulation utilisee pour le calcul du frottement sur le fond.',
             ang= 'Selects the type of formulation used for the bottom friction.',
             ),
             b_Law_Friction  = BLOC(condition = "Law_Of_Bottom_Friction!=0",
                     Friction_Coefficient = SIMP( statut='o',typ='R',
                     defaut=50.0 ,
                     fr = 'Fixe la valeur du coefficient de frottement pour la formulation choisie.  \
Attention, la signification de ce chiffre varie suivant la formule choisie : \
1 : coefficient lineaire 2 : coefficient de Chezy 3 : coefficient de Strickler \
4 : coefficient de Manning 5 : hauteur de rugosite de Nikuradse',
    ang= 'Sets the value of the friction coefficient for the selected formulation. \
It is noteworthy that the meaning of this figure changes according to the selected formula (Chezy, Strickler, etc.) : \
1 : linear coefficient 2 : Chezy coefficient 3 : Strickler coefficient 4 : Manning coefficient 5 : Nikuradse grain size',
                   ),
              ),
             b_Colebrooke_White  = BLOC(condition =' "Law_Of_Bottom_Friction" in ("Colebrooke_White Log 7",)',
                 Manning_Default_Value_For_Colebrook_white_Law = SIMP( statut='o',typ='R',
                 defaut=0.02 ,
                 fr = 'valeur par defaut du manning pour la loi de frottement de  Colebrook-White ',
                 ang= 'Manning default value for the friction law of Colebrook-White ',
                  ),
            ),

         Non_submerged_Vegetation_Friction = SIMP( statut='o',typ=bool,
           defaut=False ,
           fr = 'calcul du frottement du a la vegetation non submergee',
           ang= 'friction calculation of the non-submerged vegetation',
             ),
          b_Non_Sub  = BLOC(condition =' Non_submerged_Vegetation_Friction == True',
            Diameter_Of_Roughness_Elements = SIMP( statut='o',typ='R',
              defaut=0.006 ,
              fr = 'diametre des elements de frottements',
              ang= 'diameter of roughness element',
               ),

          Spacing_Of_Roughness_Elements = SIMP( statut='o',typ='R',
              defaut=0.14 ,
              fr = 'espacement des elements de frottement',
              ang= 'spacing of rouhness element',
              ),
            ),
          Law_Of_Friction_On_Lateral_Boundaries = SIMP( statut='o',typ='TXM',
             defaut=0 ,
             into =('0="NO FRICTION"', '1="HAALAND"', '2="CHEZY"', '3="STRICKLER"', '4="MANNING"', '5="NIKURADSE"', '6="LOG LAW"', '7="COLEBROOK-WHITE"'),
             fr = 'selectionne le type de formulation utilisee pour le calcul du frottement sur les parois laterales.',
             ang= 'Selects the type of formulation used for the friction on lateral boundaries.',
            ),
          Roughness_Coefficient_Of_Boundaries = SIMP( statut='o',typ='R',
            defaut=100.0 ,
            fr = 'Fixe la valeur du coefficient de frottement sur les frontieres solides avec un regime turbulent rugueux\n\
 sur les bords du domaine.  meme convention que pour le coefficient de frottement',
    ang= 'Sets the value of the friction coefficient of the solid boundary with the bed roughness option. Same meaning than friction coefficient',
              ),
          Maximum_Number_Of_Friction_Domains = SIMP( statut='o',typ='I',
             defaut=10 ,
             fr = 'nombre maximal de zones pouvant etre definies pour le frottement. Peut etre augmente si necessaire',
             ang= 'maximal number of zones defined for the friction.  Could be increased if needed',
              ),

          Bottom_Smoothings = SIMP( statut='o',typ='I', defaut=0 ,
    fr = 'Nombre de lissages effectues sur la topographie.  chaque lissage, effectue a l aide dune matrice de masse, est conservatif.\n\
Utilise lorsque les donnees de bathymetrie donnent des resultats trop irreguliers apres interpolation.',
     ang= 'Number of smoothings on bottom topography.  each smoothing is mass conservative.  \n\
to be used when interpolation of bathymetry on the mesh gives very rough results.',
     ),

Threshold_Depth_For_Receding_Procedure=SIMP(statut='o',typ='R',defaut=0 ,
fr ='Si > 0., declenche la procedure de ressuyage qui evite le franchissement parasite des digues mal discretisees',
ang='If > 0., will trigger the receding procedure that avoids overwhelming of dykes which are too loosely discretised ',
     ),

     ), # Fin de Friction
     Parameter_Estimation=FACT(statut='f',
           Parameter_Estimation = SIMP( statut='o',typ='TXM', into =["FRICTION","FROTTEMENT, STEADY"],
           fr ='Liste des parametres a estimer', 
          ang = 'List of parameter to be estimated',),
         
      Definition_Of_Zones   = SIMP(typ=bool, statut='o', defaut=False,
        fr = 'Declenche l''appel a def_zones, pour donner un numero de zone a chaque point',
        ang = 'Triggers the call to def_zones to give a zone number to every point',
       ),
      b_def_zone = BLOC (condition = 'Definition_Of_Zones==True',
      Consigne = SIMP(statut="o",homo='information',typ="TXM", defaut="complete DEF_ZONES subroutine"),
       ),

      Identification_Method = SIMP( statut='o',typ='TXM',
        into=["list of tests", "gradient simple", "conj gradient", "Lagrange interp."],
        defaut='gradient simple',
      ),
      Maximum_Number_Of_Iterations_For_Identification=SIMP(statut='o',typ='I',defaut=20,
      fr = 'chaque iteration comprend au moins un calcul direct et un calcul adjoint',
      ang = 'every iteration implies at least a direct and an adjoint computation',

      ),
      Cost_Function=SIMP(statut="o",typ='TXM', defaut = 'computed with h, u , v',
      into=['computed with h, u , v', 'computed with c, u , v'],
#     fr = '1 : calculee sur h, u , v  2 : calculee avec c, u , v'
      ),
      Tolerances_For_Identification=SIMP( statut='o',typ='R',
       defaut = (1.E-3,1.E-3,1.E-3,1.E-4),
       fr = '4 nombres : precision absolue sur H, U, V, et precision relative sur la fonction cout',
       ang = '4 numbers: absolute precision on H, U V, and relative precision on the cost function',
       min=4,max=4,)
      ),

)

POST_PROCESSING=PROC(nom="POST_PROCESSING",op=None,
   Graphic_Printouts=FACT(statut='f',
        Graphic_Printout_Period=SIMP(statut='o', typ='I',defaut=1),
        Number_Of_First_TimeStep_For_Graphic_Printouts=SIMP(statut='o', typ='I',defaut=1),
        Variables_For_Graphic_Printouts=SIMP(statut='o',max="**", typ='TXM',into=['a','b','c'],),
        # ajouter le into
   ),
  Listing_Printouts=FACT(statut='f',

          Results_File_Format = SIMP( statut='o',typ='TXM',into=['SERAFIN','MED','SERAFIND'], defaut='SERAFIN',
                                fr = 'Format du fichier de resultats. Les valeurs possibles sont : \n\
     - SERAFIN : format standard simple precision pour Telemac;  \n\
     - SERAFIND: format standard double precision pour Telemac; \n\
     - MED     : format MED base sur HDF5' ,
                               ang = 'Results file format. Possible values are:\n \
     - SERAFIN : classical single precision format in Telemac;\n\
     - SERAFIND: classical double precision format in Telemac; \n\
     - MED     : MED format based on HDF5' ,
                                   ),
 
          Results_File     = SIMP( statut='o', typ = ('Fichier', 'Steering Files (*.cas);;All Files (*)',),
                           fr='Nom du fichier dans lequel seront ecrits les resultats du calcul avec la periodicite donnee par le mot cle : PERIODE POUR LES SORTIES GRAPHIQUES.', 
                          ang='Name of the file into which the computation results shall be written, the periodicity being given by the key-word: GRAPHIC PRINTOUT PERIOD.',
                                ),
        Listing_Printout_Period = SIMP(statut='o', typ='I',defaut=1,
          fr  = 'Determine la periode en nombre de pas de temps d''impression des variables',
          ang = 'Determines, in number of time steps, the printout period for the variables',
        ),

        Number_Of_First_TimeStep_For_Graphic_Printouts=SIMP(statut='o', typ='I',defaut=1),
        Variables_To_Be_Printed=SIMP(statut='o',max="**", typ='TXM',into=['a','b','c']),
   ),#Listing_Printouts

   Formatted_Results_File = SIMP( statut='o',typ= ('Fichier','All Files (*)',),
        fr = 'Fichier de resultats formate mis a la disposition de l utilisateur. \
Les resultats a placer dans ce fichier seront a ecrire sur le canal 29.',
       ang= 'Formatted file of results made available to the user.  \
The results to be entered into this file shall be written on channel 29.',
     ),


   Debugger     = SIMP(typ=bool, statut='o', defaut=False),
   Output_Of_Initial_Conditions = SIMP(typ=bool, statut='o', defaut=True,
        fr = 'Si Vrai, impression des conditions initiales dans les resultats',
        ang = 'If True, output of initial conditions in the results'
   ),

   Binary_Results_File = SIMP( statut='f', typ = ('Fichier', ';;All Files (*)',), 
       fr = "Fichier de resultats code en binaire mis a la disposition de l'utilisateur.\n\
Les resultats a placer dans ce fichier seront a ecrire sur le canal 28.",
       ang = "Additional binary-coded result file made available to the user. \n\
The results to be entered into this file shall be written on channel 28.",
    ),

Information_About_Solver = SIMP(typ=bool, statut='f',defaut=False,
       fr = "Si vrai, Donne a chaque pas de temps le nombre d'iterations necessaires a la convergence du solveur de l'etape de propagation.",
     ang = "if True, prints the number of iterations that have been necessary to get the solution of the linear system.",
),



PRECONDITIONING = SIMP( statut='o',typ='I',
    defaut=2 ,
    fr = 'Permet de preconditionner le systeme de letape de propagation afin daccelerer la convergence lors de sa resolution.  - 0 : pas de preconditionnement;  - 2 : preconditionnement diagonal.  - 3 : preconditionnement diagonal-bloc  - 7 : preconditionnement de Crout par element ou segment  -11 : preconditionnement de Gauss-Seidel par element ou segment Certains preconditionnements sont cumulables (les diagonaux 2 ou 3 avec les autres) Pour cette raison on ne retient que les nombres premiers pour designer les preconditionnements. Si lon souhaite en cumuler plusieurs on formera le produit des options correspondantes.',
    ang= 'Choice of the preconditioning in the propagation step linear system that the convergence is speeded up when it is being solved.  0: no preconditioning  2: diagonal preconditioning  3: diagonal preconditioning with the condensed matrix  7: Crouts preconditioning per element or segment 11: Gauss-Seidels preconditioning per element or segment Some operations (either 2 or 3 diagonal preconditioning) can be performed concurrently with the others. Only prime numbers are therefore kept to denote the preconditioning operations. When several of them are to be performed concurrently, the product of relevant options shall be made.',
     ),

) # FIN POST-PRO


# Attention calculer le logique BREACH 
STRUCTURES=PROC(nom="STRUCTURES",op=None,

# Attention calculer le logique BREACH 

        Number_Of_Culverts = SIMP( statut='o',typ='I',
               defaut=0 ,
          fr = 'Nombre de siphons traites comme des termes sources ou puits. Ces siphons doivent etre decrits comme des sources \
dans le fichier cas. Leurs caracteristiques sont donnees dans le fichier de donnees des siphons (voir la documentation ecrite)',
          ang= 'Number of culverts treated as source terms.  They must be described as sources in the domain\
 and their features are given in the culvert data file (see written documentation)',
           ),

        culvert_exist=BLOC(condition="Number_Of_Culverts!=0",
        Culverts= FACT(statut='o',
         min=1,max="**",
         Abscissae_Of_Sources = SIMP( statut='o',
          typ=Tuple(2),validators=VerifTypeTuple(('R','R')),
          fr = 'Valeurs des abscisses des sources de debit et de traceur.',
          ang= 'abscissae of sources of flowrate and/or tracer',
         ),

          Ordinates_Of_Sources = SIMP( statut='o',
          typ=Tuple(2),validators=VerifTypeTuple(('R','R')),
          fr = 'Valeurs des ordonnees des sources de debit et de traceur.',
          ang= 'ordinates of sources of flowrate and/or tracer',
          ),
          Water_Discharge_Of_Sources = SIMP( statut='o',
          typ=Tuple(2),validators=VerifTypeTuple(('R','R')),
          fr = 'Valeurs des debits des sources.',
          ang= 'values of water discharge of sources',
          ),
          Velocities_Of_The_Sources_Along_X = SIMP( statut='o',
          typ=Tuple(2),validators=VerifTypeTuple(('R','R')),
          fr = 'Vitesses du courant a chacune des sources. Si elles ne sont pas donnees, on considere que la vitesse est celle du courant',
          ang= 'Velocities at the sources. If they are not given, the velocity of the flow at this location is taken',
          ),
          Velocities_Of_The_Sources_Along_Y = SIMP( statut='o',
          typ=Tuple(2),validators=VerifTypeTuple(('R','R')),
          fr = 'Vitesses du courant a chacune des sources',
          ang= 'Velocities at the sources',
         ),
        ),

        Culvert_Data_File = SIMP( statut='o',typ = ('Fichier', 'All Files (*)',),
            fr = 'Fichier de description des siphons presents dans le modele',
            ang= 'Description of culvert existing in the model',
        ),

        ),

          Number_Of_Tubes = SIMP( statut='o',typ='I',
          defaut=0 ,
          fr = 'Nombre de buses ou ponts traites comme des termes sources ou puits. Ces buses doivent etre decrits comme des sources\n\
dans le fichier cas. Leurs caracteristiques sont donnees dans le fichier de donnees des buses (voir la documentation ecrite)',
          ang= 'Number of tubes or bridges treated as source terms.  They must be described as sources in the domain \n\
and their features are given in the tubes data file (see written documentation)',
        ),

        b_Tubes= BLOC(condition="Number_Of_Tubes!=0",
        Tubes_Data_File = SIMP( statut='o',
           typ = ('Fichier', 'All Files (*)',),
           fr = 'Fichier de description des buses/ponts presents dans le modele',
           ang= 'Description of tubes/bridges existing in the model',
          ),
          ),

      Number_Of_Weirs=SIMP(statut='o',typ='I',defaut=0,
           fr = 'Nombre de seuils qui seront traites par des conditions aux limites. \n\
Ces seuils doivent etre decrits comme des frontieres du domaine de calcul',
           ang = 'Number of weirs that will be treated by boundary conditions.',
     ),

     b_Weirs= BLOC(condition="Number_Of_Weirs!=0",
        Weirs_Data_File = SIMP( statut='o',
        typ = ('Fichier', 'All Files (*)',),
        fr = 'Fichier de description des seuils presents dans le modele',
        ang= 'Description of weirs existing in the model',),
     ),

     Breach=SIMP(statut='o',typ=bool,defaut=False,
         fr = 'Prise en compte de breches dans le calcul par modification altimetrique dans le maillage.',
         ang = 'Take in account some breaches during the computation by modifying the bottom level of the mesh.',
     ),
     b_Breaches= BLOC (condition = 'Breach==True',
         Breaches_Data_File = SIMP( statut='o',typ = ('Fichier', 'All Files (*)',),
                fr = 'Fichier de description des breches',
                ang= 'Description of breaches',
         ),
      ),
      Vertical_Structures=SIMP(statut='o',typ=bool,defaut=False,
      fr = 'Prise en compte de la force de trainee de structures verticales',
      ang = 'drag forces from vertical structures are taken into account',
      ),
      maskob = BLOC (condition = 'Vertical_Structures==True',
      Consigne = SIMP(statut="o",homo='information',typ="TXM", defaut="subroutine DRAGFO must then be implemented"),
      ),
      Formatted_File1    = SIMP( statut='f', typ = ('Fichier', 'formated File (*.txt);;All Files (*)',),
              fr = "Fichier de donnees formate mis a la disposition de l''utilisateur.  \n\
Les donnees de ce fichier seront a lire sur le canal 26.",
              ang = 'Formatted data file made available to the user.\n\
The data in this file shall be read on channel 26.',
          ),
) # FIn STRUCTURE
TRACERS=PROC(nom="TRACERS",op=None,
        Boundary_conditions=FACT(statut='o',
       Treatment_Of_Fluxes_At_The_Boundaries   = SIMP( statut='f',typ='TXM',
         into=["Priority to prescribed values","Priority to fluxes"],
         fr='Utilise pour les schemas SUPG, PSI et N, \n\
si Priorité aux flux, on ne retrouve pas exactement les valeurs imposees des traceurs,mais le flux est correct',
         ang='Used so far only with the SUPG, PSI and N schemes.\n\
if Priority to fluxes, Dirichlet prescribed values are not obeyed,but the fluxes are correct',
        ),
        ), # fin Boundary_conditions
)          # FIN TRACERS
