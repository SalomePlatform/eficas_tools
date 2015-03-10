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

          Boundary_Condition_File = SIMP( statut='o', typ = ('Fichier', 'Boundary Condition (*.cli);;All Files (*)',),fr='Nom du fichier contenant les types de conditions aux limites. Ce fichier est rempli de facon automatique par le mailleur au moyen de couleurs affectees aux noeuds des frontieres du domaine de calcul.',ang='Name of the file containing the types of boundary conditions. This file is filled automatically by the mesh generator through through colours that are assigned to the boundary nodes.',),


     Validation=FACT( statut='f',

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

          Formatted_File1    = SIMP( statut='f', typ = ('Fichier', 'formated File (*.txt);;All Files (*)',),
              fr = "Fichier de donnees formate mis a la disposition de l''utilisateur.  \n\
Les donnees de ce fichier seront a lire sur le canal 26.",
              ang = 'Formatted data file made available to the user.\n\
The data in this file shall be read on channel 26.',
          ),
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
        Machine=FACT( statut='o',
# A voir plus tar Obsolete ? 
           Number_of_Processors=SIMP(statut='o',typ='I',val_min=0,defaut=1),
           #Parallel_Computation=SIMP(statut='o',typ=bool,defaut=False),
         ),
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

        Zone_number_in_Geographic_System=SIMP(statut='f',typ='I',
            #into=[-1,0,1,2,3,4,22,30],
            into=[ 'LAMBERT 1 NORD', 'LAMBERT 2 CENTRE', 'LAMBERT 3 SUD', 'LAMBERT 4 CORSE', 'LAMBERT 2 ETENDU', 'ZONE UTM, PAR EXEMPLE'],
            fr="Numero de zone (fuseau ou type de projection) lors de l'utilisation d'une projection plane.\n Indiquer le systeme geographique dans lequel est construit le modele numerique avec le mot-cle SYSTEME GEOGRAPHIQUE",
            ang='Number of zone when using a plane projection. \nIndicate the geographic system in which the numerical model is built with the keyword GEOGRAPHIC SYSTEM'),
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
                
            Options=SIMP(statut='f',typ='I',
            into=['classical boundary conditions','Thompson method based on characteristics'],
            fr='On donne 1 entier par frontiere liquide',
            ang='One integer per liquid boundary is given',
            ),

        Type_Condition=SIMP(statut='o',typ='TXM',into=['Flowrates','Elevations','Velocity'],),
#?????

         b_Flowrates     = BLOC (condition = "Type_Condition == 'Flowrates'",
             Prescribed_Flowrates=SIMP(statut='o',typ='R',
             fr=' Valeurs des debits imposes aux frontieres liquides entrantes.\n Lire la partie du mode d''emploi consacree aux conditions aux limites',
            ang='Values of prescribed flowrates at the inflow boundaries.\n The section about boundary conditions is to be read in the manual'),
             ),

         b_Elevations   = BLOC (condition = "Type_Condition == 'Elevations'",
                Prescribed_Elevations=SIMP(statut='o',typ='R',
                fr='Valeurs des cotes imposees aux frontieres liquides entrantes.\n Lire la partie du mode d''emploi consacree aux conditions aux limites',
                ang='Values of prescribed elevations at the inflow boundaries.\n The section about boundary conditions is to be read in the manual'),
             ),

         b_Velocity   = BLOC (condition = "Type_Condition == 'Velocity'",
               Prescribed_Velocity=SIMP(statut='o',typ='R',
               fr='Valeurs des vitesses imposees aux frontieres liquides entrantes.\n Lire la partie du mode d''emploi consacree aux conditions aux limites',
               ang='Values of prescribed velocities at the liquid inflow boundaries.\n Refer to the section dealing with the boundary conditions'),
         ),

       ), # fin des Liquid_Boundaries

       Stage_Discharge_Curves = SIMP(statut='f',typ='I',
        #into=[0,1,2],
        into=["no","Z(Q)","not programmed"],
        fr='Indique si une courbe de tarage doit etre utilisee pour une frontiere',
        ang='Says if a discharge-elevation curve must be used for a given boundary',
        ),
        b_discharge_curve   = BLOC (condition = "Stage_Discharge_Curves == 'Z(Q)'",
        Stage_Discharge_Curves_File   = SIMP( statut='f', typ = ('Fichier', 'All Files (*)',),
          fr='Nom du fichier contenant les courbes de tarage',
          ang='Name of the file containing stage-discharge curves',
          ),
        ),

       Treatment_Of_Fluxes_At_The_Boundaries   = SIMP( statut='f',typ='TXM',
         into=["Priority to prescribed values","Priority to fluxes"],
         fr='Utilise pour les schemas SUPG, PSI et N, \n\
si Priorité aux flux, on ne retrouve pas exactement les valeurs imposees des traceurs,mais le flux est correct',
         ang='Used so far only with the SUPG, PSI and N schemes.\n\
if Priority to fluxes, Dirichlet prescribed values are not obeyed,but the fluxes are correct'
        ),

#???? into no coherent avec dico
# Ira dans la marée
       Option_For_Tidal_Boundary_Conditions   = SIMP( statut='f',typ='I',
       #into=[1,2],sug=1),
       into=['No tide', 'Real tide (recommended methodology)', 'Astronomical tide', 'Mean spring tide', 'Mean tide',\
           'Mean neap tide', 'Astronomical neap tide', 'Real tide (methodology before 2010)'],
       ),


  ), # fin Boundary_Conditions

) # fin INITIAL_STATE

NUMERICAL_PARAMETERS=PROC(nom="NUMERICAL_PARAMETERS",op=None,

        Solver=FACT(statut='o',

          Equations=SIMP(statut='o',typ='TXM',
             into=['SAINT-VENANT EF','SAINT-VENANT VF','BOUSSINESQ'],
             defaut='SAINT-VENANT EF',
             fr='Choix des equations a resoudre',
             ang= 'Choice of equations to solve',
             ),

          Solver=SIMP(statut='o',typ='TXM',
           into = ["conjugate gradient", "conjugate residual", "minimum error", "cgstab", "gmres", "direct",],
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

          Maximum_Number_of_Iterations_For_Solver=SIMP(statut='o',typ='I', defaut=40,
          fr = 'Les algorithmes utilises pour la resolution de l''etape de propagation etant iteratifs, \n\
il est necessaire de limiter le nombre d''iterations autorisees.\n\
Remarque : un maximum de 40 iterations par pas de temps semble raisonnable.',
          ang = 'Since the algorithms used for solving the propagation step are iterative, \
the allowed number of iterations should be limited.\n\
Note: a maximum number of 40 iterations per time step seems to be reasonable.',
           ),
        ), # fin Solver

        Time=FACT(statut='f',
        regles=(UN_PARMI('Number_of_Time_Steps','Duration'),),

           Time_Step=SIMP(statut='f',typ='R'),
           Number_of_Time_Steps=SIMP(statut='f',typ='I',
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
           Treatment_of_Fluxes_at_the_Boundaries =SIMP( statut='f',typ='I',into=[1,2],sug=1),
           Continuity_Correction  =SIMP(typ=bool, statut='f'),
           Number_of_Sub_Iterations=SIMP(statut='f',typ='I'),
     ),
     Precondionning=FACT(statut='f',

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

     Advection=FACT(statut='f',

          Mass_Lumping_on_H =SIMP(statut='f',typ='R',defaut=0,
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

          Mass_Lumping_on_Velocity =SIMP(statut='f',typ='R',defaut=0,
            fr = 'Fixe le taux de mass-lumping effectue sur la vitesse.',
            ang = 'Sets the amount of mass-lumping that is performed on the velocity.'
),


#PNPNPNPN
#
# Attention a recalculer
# Il faut recalculer des listes de 4 en sortie
#
        Advection_Propagation=FACT(statut='f',
          Advection_Of_U_and_V=SIMP(statut='o',typ=bool,defaut=False,
            fr = 'Prise en compte ou non de la convection de U et V.',
            ang= 'The advection of U and V is taken into account or ignored.'
            ),

          b_u_v = BLOC( condition = "Advection_Of_U_and_V==True",

          Type_of_Advection_U_and_V=SIMP(statut='o',typ='TXM',
          into=["CARACTERISTIQUES", "SUPG", "SCHEMA VOLUME FINI EXPLICIT", "SCHEMA DISTRIBUTIF N CONSERVATIF",\
                "SCHEMA PSI CONSERVATIF", "SCHEMA PSI NON CONSERVATIF", "SCHEMA N IMPLICITE NON CONSERVATIF",\
                 "SCHEMA N PAR SEGMENTS SCHEMA 3", "SCHEMA N PAR SEGMENTS SCHEMA 4"],
                 ),
           b_upwind     =BLOC(condition = "Type_of_Advection_U_and_V== 'SUPG'",
            Upwind_Coefficients_of_U_and_V=SIMP(statut='o',typ='R',)
               ),
           ),

          Advection_Of_H=SIMP(statut='o',typ=bool,defaut=False,
            fr = 'Prise en compte ou non de la convection de H.',
            ang= 'The advection of H is taken into account or ignored.'
            ),

          b_h = BLOC( condition = "Advection_Of_H==True",

          Type_of_Advection_H=SIMP(statut='o',typ='TXM',
          into=["CARACTERISTIQUES", "SUPG", "SCHEMA VOLUME FINI EXPLICIT", "SCHEMA DISTRIBUTIF N CONSERVATIF",\
                "SCHEMA PSI CONSERVATIF", "SCHEMA PSI NON CONSERVATIF", "SCHEMA N IMPLICITE NON CONSERVATIF",\
                 "SCHEMA N PAR SEGMENTS SCHEMA 3", "SCHEMA N PAR SEGMENTS SCHEMA 4"],
                 ),
           b_upwind_H     = BLOC(condition = "Type_of_Advection_H== 'SUPG'",
            Upwind_Coefficients_of_H=SIMP(statut='o',typ='R',)
               ),
           ),

          Advection_Of_Tracers=SIMP(statut='o',typ=bool,defaut=False,
            fr = 'Prise en compte ou non de la convection de Tracer.',
            ang= 'The advection of Tracer is taken into account or ignored.'
            ),

          b_tracers = BLOC( condition = "Advection_Of_Travers==True",

          Type_of_Advection_Tracers=SIMP(statut='o',typ='TXM',
          into=["CARACTERISTIQUES", "SUPG", "SCHEMA VOLUME FINI EXPLICIT", "SCHEMA DISTRIBUTIF N CONSERVATIF",\
                "SCHEMA PSI CONSERVATIF", "SCHEMA PSI NON CONSERVATIF", "SCHEMA N IMPLICITE NON CONSERVATIF",\
                 "SCHEMA N PAR SEGMENTS SCHEMA 3", "SCHEMA N PAR SEGMENTS SCHEMA 4"],
                 ),
           b_upwind_Tracers     =BLOC(condition = "Type_of_Advection_Tracers== 'SUPG'",
            Upwind_Coefficients_of_Tracers=SIMP(statut='o',typ='R',)
               ),
           ),


         Advection_of_K_and_Epsilon=SIMP(statut='f',typ=bool,defaut=False,
           fr = 'Prise en compte ou non de la convection de Tracer.',
            ang= 'The advection of Tracer is taken into account or ignored.'
            ),

          b_k = BLOC( condition = "Advection_Of_K_and_Epsilon==True",

          Type_of_Advection_K_and_Epsilon=SIMP(statut='o',typ='TXM',
          into=["CARACTERISTIQUES", "SUPG", "SCHEMA VOLUME FINI EXPLICIT", "SCHEMA DISTRIBUTIF N CONSERVATIF",\
                "SCHEMA PSI CONSERVATIF", "SCHEMA PSI NON CONSERVATIF", "SCHEMA N IMPLICITE NON CONSERVATIF",\
                 "SCHEMA N PAR SEGMENTS SCHEMA 3", "SCHEMA N PAR SEGMENTS SCHEMA 4"],
                 ),
           b_upwind_k     =BLOC(condition = "Type_of_Advection_K_and_Epsilon== 'SUPG'",
            Upwind_Coefficients_of_K_and_Epsilon=SIMP(statut='o',typ='R',)
               ),
           ),

        ),
      ), # fin Advection

        Propagation=FACT(statut='f',
          Linearized_Propagation=SIMP(statut='o',typ=bool,defaut=False),
          b_linear     =BLOC(condition = "Linearized_Propagation==True ",
            Mean_Depth_For_Linearity=SIMP(statut='o',typ='R',defaut=0.0,val_min=0),
          ),
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
)# fin NUMERICAL_PARAMETERS

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
