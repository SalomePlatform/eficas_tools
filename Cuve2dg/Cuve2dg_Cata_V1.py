# -*- coding: utf-8 -*-

# --------------------------------------------------
# debut entete
# --------------------------------------------------

import Accas
from Accas import *

class loi ( ASSD ) : pass
class variable ( ASSD ) : pass


#CONTEXT.debug = 1
JdC = JDC_CATA ( code = 'CUVE1D-DEFAILLGLOB',
                 execmodul = None,
                 regles = ( AU_MOINS_UN ('OPTIONS','DEFAUT', 'CUVE', 'MODELES', 'INITIALISATION', 'REVETEMENT', 'METAL_BASE', 'TRANSITOIRE'), 
                            AU_MOINS_UN ( 'FIN' ), 
                            A_CLASSER ( ('OPTIONS', 'DEFAUT', 'CUVE', 'MODELES', 'INITIALISATION', 'REVETEMENT', 'METAL_BASE', 'TRANSITOIRE'),'FIN')
                          )
                 ) # Fin JDC_CATA

# --------------------------------------------------
# fin entete
# --------------------------------------------------






#================================
# 1. Definition des OPTIONS
#================================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)

OPTIONS = OPER ( nom = "OPTIONS",
                 sd_prod = loi,
                 op = 68,
                 fr = "Definitions des options", 

#===
# Liste des paramètres
#===

  INCRTPS = SIMP ( statut = "o",
                   typ = "I",
                   defaut = "1",
		   max = 1,
                   val_max = 100,
                   fr = "Increment temporel (=1 pour calcul deterministe)",
                  ),

  DTPREC = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "0.1",
                  max = 1,
                  val_max = 1.,
                  fr = "Increment maximum d'evolution de la temperature par noeud et par instant (°C)",
                ),

  DTARCH = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "1000.",
		  max = 1,
                  val_max = 1000.,
                  fr = "Increment maximum de temps pour l'affichage (s)",
                ),

  NBO = SIMP ( statut = "o",
               typ = "R",
	       max=1,
               val_max = 1000.,
               fr = "Nombre de noeuds a considerer dans le maillage interne",
              ),

  Liste_instants = SIMP ( statut = "o",
                          typ = "R",
                          max = "**",
                          fr = "Liste des instants ",
                        ),

) # Fin OPER OPTIONS

#================================
# 2. Caracteristiques du DEFAUT
#================================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)
DEFAUT = OPER ( nom = "DEFAUT",
                sd_prod = loi,
                op = 68,
                fr = "Caracteristiques du defaut", 

#===
# Liste des paramètres
#===

  TYPEDEF = SIMP ( statut = "o", typ = "TXM",
                   into = ( "DSR",
                            "DD",
                          ),
                   #defaut = "DSR",
                   fr = "Type de defaut : sous revetement ou debouchant",
                  ),

#====
# Definition des parametres selon le type du defaut
#====

  Parametres_DSR = BLOC ( condition = " TYPEDEF in ( 'DSR', ) ",

                  ORIEDEF = SIMP ( statut = "o",
                                   typ = "TXM",
                                   into = ( "LONGITUD", "CIRCONF" ),
                                   #defaut = "LONGITUD",
                                   fr = "Orientation du defaut : longitudinale ou circonferentielle",
                                 ),

                  PROFDEF = SIMP ( statut = "o",
                                   typ = "R",
                                   #defaut = "0.006",
                                   max = 1,
                                   val_max = 1.,
                                   fr = "Profondeur radiale du defaut (m)",
                                 ),

                  OPTLONG = SIMP ( statut = "o",
                                   typ = "TXM",
                                   into = ( "VALEUR", "RAPPORT" ),
                                   #defaut = "VALEUR",
                                   fr = "Option pour caracteriser la longueur du defaut : soit par valeur, soit par un rapport LONG/PROF",
                                 ),

                    Option_Valeur = BLOC ( condition = "OPTLONG in ( 'VALEUR', ) ",

                            LONGDEF = SIMP ( statut = "o",
                                             typ = "R",
                                             #defaut = "0.060",
                                             max = 1,
                                             val_max = 1.,
                                             fr = "Longueur du defaut sous revetement (m)",
                                            ),

	                                  ), # Fin BLOC Option_Valeur

                    Option_Rapport = BLOC ( condition = "OPTLONG in ( 'RAPPORT', ) ",

                            LONGSURPROF = SIMP ( statut = "o",
                                                 typ = "R",
                                                 #defaut = "6.",
                                                 max = 1,
                                                 val_max = 100.,
                                                 fr = "Rapport longueur/profondeur du defaut sous revetement",
                                                ),

		                           ), # Fin BLOC Option_Rapport

                  DECADEF = SIMP ( statut = "o",
                                   typ = "R",
                                   #defaut = "-0.00001",
                                   fr = "Decalage radial du defaut sous revetement (m)",
                                  ),

                  ANGLDEF = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "0.",
                                   fr = "Coordonnee angulaire du defaut (degres)",
                                  ),

                  ALTIDEF = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "2.",
                                   fr = "Altitude du defaut (m)",
                                  ),

                  POINDEF = SIMP ( statut = "o",
                                   typ = "TXM",
                                   into = ( "A", "B" ),
                                   defaut = "A",
                                   fr = "Choix du point considere du defaut sous revetement",
                                  ),

                  ARRETFISSURE = SIMP ( statut = "o",
                                        typ = "TXM",
                                        into = ( "OUI", "NON" ),
                                        defaut = "NON",
                                        fr = "Prise en compte de l arret de fissure",
                                       ),

                  INCRDEF = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "0.005",
                                   fr = "Increment de la taille de fissure (m)",
                                  ),

                  CORRECPLASTIC = SIMP ( statut = "o",
                                         typ = "TXM",
                                         into = ( "OUI", "NON" ),
                                         defaut = "NON",
                                         fr = "Prise en compte de la correction plastique BETA ",
                                        ),

                         ), # Fin BLOC Parametres_DSR

  Parametres_DD = BLOC ( condition = " TYPEDEF in ( 'DD', ) ",

                  ORIEDEF = SIMP ( statut = "o",
                                   typ = "TXM",
                                   into = ( "LONGITUD", "CIRCONF" ),
                                   #defaut = "LONGITUD",
                                   fr = "Orientation du defaut : longitudinale ou circonferentielle",
                                  ),

                  PROFDEF = SIMP ( statut = "o",
                                   typ = "R",
                                   #defaut = "0.006",
                                   max = 1,
                                   val_max = 1.,
                                   fr = "Profondeur radiale du defaut (m)",
                                  ),

                  ANGLDEF = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "0.",
                                   fr = "Coordonnee angulaire du defaut (degres)",
                                  ),

                  ALTIDEF = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "2.",
                                   fr = "Altitude du defaut (m)",
                                  ),

                  ARRETFISSURE = SIMP ( statut = "o",
                                        typ = "TXM",
                                        into = ( "OUI", "NON" ),
                                        defaut = "NON",
                                        fr = "Prise en compte de l arret de fissure",
                                       ),

                  INCRDEF = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "0.005",
                                   fr = "Increment de la taille de fissure (m)",
                                  ),

                  IRWIN = SIMP ( statut = "o",
                                 typ = "TXM",
                                 into = ( "OUI", "NON" ),
                                 defaut = "NON",
                                 fr = "Prise en compte de la correction plastique d'Irwin ",
                                ),

                  CORRECPLASTIC = SIMP ( statut = "o",
                                         typ = "TXM",
                                         into = ( "OUI", "NON" ),
                                         defaut = "NON",
                                         fr = "Prise en compte de la correction plastique BETA ",
                                        ),

                        ), # Fin BLOC Parametres_DD 

) # Fin OPER DEFAUT


#================================
# 3. Caracteristiques de la CUVE
#================================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)
CUVE = OPER (nom = "CUVE",
             sd_prod = loi,
             op = 68,
             fr = "Caracteristiques de la cuve", 

#===
# Liste des paramètres
#===

  TYPEGEOM = SIMP ( statut = "o",
                    typ = "TXM",
	   	    into = ( "GEOMETRIE", "MAILLAGE"), 
                    #defaut = "GEOMETRIE",
                    fr = "Traitement de la geometrie d'une cuve",
                   ),


#====
# Definition des parametres selon le type de traitement de la geometrie
#====

  Geometrie = BLOC ( condition = " TYPEGEOM in ( 'GEOMETRIE', ) ",

                  RINT = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "1.994",
                                fr = "Rayon interne de la cuve (m)",
                               ),

                  REXT = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "2,2015",
                                fr = "Rayon externe de la cuve (m)",
                               ),

                  LREV = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "0.0075",
                                fr = "Epaisseur du revetement (m)",
                               ),

                  LIGMIN = SIMP ( statut = "o",
                                  typ = "R",
                                  defaut = "0.75",
                                  fr = "Ligament externe minimal avant rupture (% de l'epaisseur de cuve)",
                                 ),

                     ), # Fin BLOC  Geometrie

  Maillage = BLOC ( condition = " TYPEGEOM in ( 'MAILLAGE', ) ",

                  Liste_abscisses = SIMP ( statut = "o",
                                           typ = "R",
                                           max = "**",
                                           fr = "Liste des abscisses (m) A FAIRE",
                                          ),
                   ), # Fin BLOC Maillage

) # Fin OPER CUVE

#====================================================
# 4. Modeles de fluence, d'irradiation et de tenacite
#====================================================

#=======================
# 4.1 Modeles de fluence
#=======================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)
MODELES = OPER ( nom = "MODELES",
                 sd_prod = loi,
                 op = 68,
                 fr = "Modeles de fluence, d'irradiation et de tenacite", 


#===
# Liste des paramètres
#===

  MODELFLUENCE = SIMP ( statut = "o",
                        typ = "TXM",
		        into = ( "Reglementaire", "France", "ValeurImposee", "SDM", "USNRC", "REV_2", "SDM_Lissage", "GrandeDev", "GD_Cuve"), 
                        #defaut = "Reglementaire",
                        fr = "Modele d'attenuation de la fluence dans l'epaisseur de la cuve",
                       ),


#====
# Definition des parametres selon le modele de fluence
#====

  Reglementaire = BLOC ( condition = " MODELFLUENCE in ( 'Reglementaire', ) ",

                  fmax = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "6.5",
                                fr = "Fluence maximale assimilee par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                               ),

                        ), # Fin BLOC Reglementaire

  France = BLOC ( condition = " MODELFLUENCE in ( 'France', ) ",

                  fmax = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "6.5",
                                fr = "Fluence maximale assimilee par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                               ),

	          KPFRANCE = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "12.7",
                                    fr = "Parametre exponentiel du modele France",
                                   ),

                   ), # Fin BLOC France

  ValeurImposee = BLOC ( condition = " MODELFLUENCE in ( 'ValeurImposee', ) ",

                  fmax = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "6.5",
                                fr = "Fluence maximale assimilee par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                               ),

                         ), # Fin BLOC ValeurImposee

  SDM = BLOC ( condition = " MODELFLUENCE in ( 'SDM', ) ",

                  fmax = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "6.5",
                                fr = "Fluence maximale assimilee par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                               ),

              ), # Fin BLOC SDM

  USNRC = BLOC ( condition = " MODELFLUENCE in ( 'USNRC', ) ",

                  fmax = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "6.5",
                                fr = "Fluence maximale assimilee par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                               ),

	          KPUS = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "9.4488",
                                fr = "Parametre exponentiel du modele US",
                               ),

                ), # Fin BLOC USNRC

  REV_2 = BLOC ( condition = " MODELFLUENCE in ( 'REV_2', ) ",

                  fmax = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "6.5",
                                fr = "Fluence maximale assimilee par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                               ),

                ), # Fin BLOC REV_2

  SDM_Lissage = BLOC ( condition = " MODELFLUENCE in ( 'SDM_Lissage', ) ",

                  fmax = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "6.5",
                                fr = "Fluence maximale assimilee par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                               ),

                      ), # Fin BLOC SDM_Lissage

  GrandeDev = BLOC ( condition = " MODELFLUENCE in ( 'GrandeDev', ) ",

                  fmax = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "6.5",
                                fr = "Fluence maximale assimilee par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                               ),

                     ), # Fin BLOC GrandeDev

  GD_Cuve = BLOC ( condition = " MODELFLUENCE in ( 'GD_Cuve', ) ",

                  fmax = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "6.5",
                                fr = "Fluence maximale assimilee par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                               ),

                  COEFFLUENCE1 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "5.8",
                                        fr = "Fluence a l'azimut 0 (10^19 n/cm)",
                                       ),

                  COEFFLUENCE2 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "5.48",
                                        fr = "Fluence a l'azimut 5 (10^19 n/cm)",
                                       ),

                  COEFFLUENCE3 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "4.46",
                                        fr = "Fluence a l'azimut 10 (10^19 n/cm)",
                                       ),

                  COEFFLUENCE4 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "3.41",
                                        fr = "Fluence a l'azimut 15 (10^19 n/cm)",
                                       ),

                  COEFFLUENCE5 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "3.37",
                                        fr = "Fluence a l'azimut 20 (10^19 n/cm)",
                                       ),

                  COEFFLUENCE6 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "3.16",
                                        fr = "Fluence a l'azimut 25 (10^19 n/cm)",
                                       ),

                  COEFFLUENCE7 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "2.74",
                                        fr = "Fluence a l'azimut 30 (10^19 n/cm)",
                                       ),

                  COEFFLUENCE8 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "2.25",
                                        fr = "Fluence a l'azimut 35 (10^19 n/cm)",
                                       ),

                  COEFFLUENCE9 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "1.89",
                                        fr = "Fluence a l'azimut 40 (10^19 n/cm)",
                                       ),

                  COEFFLUENCE10 = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "1.78",
                                        fr = "Fluence a l'azimut 45 (10^19 n/cm)",
                                       ),

                  ), # Fin BLOC GD_Cuve

#==========================
# 4.2 Modeles d'irradiation
#==========================

  TYPIRR = SIMP ( statut = "o",
                  typ = "TXM",
		  into = ( "RTNDT", "FLUENCE" ),
                  #defaut = "RTNDT",
                  fr = "Type d'irradiation ",
                 ),

#====
# Definition des parametres selon le type d'irradiation
#====

  Parametres_RTNDT = BLOC ( condition = " TYPIRR in ( 'RTNDT', ) ",
 
                  RTNDT = SIMP ( statut = "o",
                                 typ = "R",
                                 defaut = "73.",
                                 fr = "RTNDT finale (°C)",
                                ),

                            ), # Fin BLOC Parametres_RTNDT

  Parametres_FLUENCE = BLOC ( condition = " TYPIRR in ( 'FLUENCE', ) ",
 
                  MODELIRR = SIMP ( statut = "o",
                                    typ = "TXM",
		                    into = ( "HOUSSIN", "PERSOZ", "LEFEBVRE", "USNRCmdb", "BRILLAUD", "USNRCsoud" ),
                                    #defaut = "HOUSSIN",
                                    fr = "Modele d'irradiation pour virole ou joint soude",
                                   ),

                  CU = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "0.",
                              fr = "Teneur en cuivre (%)",
                             ),

                  Ni = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "0.",
                              fr = "Teneur en nickel (%)",
                             ),

                  P = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "0.",
                             fr = "Teneur en phosphore (%)",
                            ),

                  RTimoy = SIMP ( statut = "o",
                                  typ = "R",
                                  defaut = "0.",
                                  fr = "Moyenne de RTNDT : virole C1 de cuve Chinon : mdb=>-17.°C et js=>42.°C (HT-56/05/038 : p.52)",
                                 ),

                  RTicov = SIMP ( statut = "o",
                                  typ = "R",
                                  defaut = "0.",
                                  fr = "Coefficient de variation de la RTNDT initiale",
                                 ),

  Parametres_USNRC = BLOC ( condition = " MODELIRR in ( 'USNRCsoud', 'USNRCmdb' , ) ",
 
                  USectDRT = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "28.",
                                    fr = "pour modeles USNRCsoud ou USNRCmdb, ecart-type du decalage de RTNDT (°F) (28. pour js et 17. pour mdb)",
                                   ),

                           ), # Fin BLOC Parametres_USNRC 

                  nbectDRTNDT = SIMP ( statut = "o",
                                       typ = "R",
                                       defaut = "2.",
                                       fr = "Nombre d ecart-type par rapport a la moyenne de DRTNDT",
                                      ),

                           ), # Fin BLOC Parametres_FLUENCE

#========================
# 4.3 Modeles de tenacite
#========================

  MODELKIC = SIMP ( statut = "o",
                    typ = "TXM",
		    into = ( "RCC-M", "RCC-M_pal", "RCC-M_exp", "Houssin_RC", "Wallin", "REME", "ORNL", "Frama", "WEIB3", "WEIB2", "LOGWOLF", "WEIB_GEN" ),
                    #defaut = "RCC-M",
                    fr = "Modele de tenacite ",
                   ),

#====
# Definition des parametres selon le modele de tenacité
#====

  Parametres_RCCM = BLOC ( condition = " MODELKIC in ( 'RCC-M', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  KICPAL = SIMP ( statut = "o",
                                  typ = "R",
                                  defaut = "195.",
                                  fr = "palier deterministe de K1c quand modele RCC-M  (MPa(m^0.5)) ",
                                 ),

                  KICCDV = SIMP ( statut = "o",
                                  typ = "R",
                                  defaut = "0.15",
                                  fr = "coef de variation de la loi normale de K1c quand modele RCC-M ",
                                 ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),


                  KIAPAL = SIMP ( statut = "o",
                                  typ = "R",
                                  defaut = "195.",
                                  fr = "palier deterministe de K1a -tenacite a l'arret- quand modele RCC-M  (MPa(m^0.5)) ",
                                 ),

                  KIACDV = SIMP ( statut = "o",
                                  typ = "R",
                                  defaut = "0.10",
                                  fr = "coef de variation de la loi normale de K1a -tenacite a l'arret- quand modele RCC-M ",
                                 ),

                          ), # Fin BLOC Parametres_RCC-M

  Parametres_RCCMpal = BLOC ( condition = " MODELKIC in ( 'RCC-M_pal', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                             ), # Fin BLOC Parametres_RCCMpal

  Parametres_RCCMexp = BLOC ( condition = " MODELKIC in ( 'RCC-M_exp', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                             ), # Fin BLOC Parametres_RCCMexp

  Parametres_Houssin_RC = BLOC ( condition = " MODELKIC in ( 'Houssin_RC', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                                ), # Fin BLOC Parametres_Houssin_RC
      
  Parametres_Wallin = BLOC ( condition = " MODELKIC in ( 'Wallin', ) ",
 
                  T0WALLIN = SIMP ( statut = "o",
                                    typ = "I",
                                    defaut = "-27",
                                    fr = "parametre T0 du modele Wallin (°C)",
                                   ),

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                            ), # Fin BLOC Parametres_Wallin

  Parametres_REME = BLOC ( condition = " MODELKIC in ( 'REME', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                          ), # Fin BLOC Parametres_REME

  Parametres_ORNL = BLOC ( condition = " MODELKIC in ( 'ORNL', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                          ), # Fin BLOC Parametres_ORNL

  Parametres_Frama = BLOC ( condition = " MODELKIC in ( 'Frama', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                           ), # Fin BLOC Parametres_Frama

  Parametres_WEIB3 = BLOC ( condition = " MODELKIC in ( 'WEIB3', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                           ), # Fin BLOC Parametres_WEIB3

  Parametres_WEIB2 = BLOC ( condition = " MODELKIC in ( 'WEIB2', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                           ), # Fin BLOC Parametres_WEIB2

  Parametres_LOGWOLF = BLOC ( condition = " MODELKIC in ( 'LOGWOLF', ) ",

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                             ), # Fin BLOC Parametres_LOGWOLF

  Parametres_WEIB_GEN = BLOC ( condition = " MODELKIC in ( 'WEIB_GEN',) ",
 
                  A1 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "21.263",
                              fr = "coef du coef a(T) d'une Weibull generale",
                             ),
 
                  A2 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "9.159",
                              fr = "coef du coef a(T) d'une Weibull generale",
                             ),
 
                  A3 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "0.04057",
                              fr = "coef du coef a(T) d'une Weibull generale",
                             ),
 
                  B1 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "17.153",
                              fr = "coef du coef b(T) d'une Weibull generale",
                             ),
 
                  B2 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "55.089",
                              fr = "coef du coef b(T) d'une Weibull generale",
                             ),
 
                  B3 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "0.0144",
                              fr = "coef du coef b(T) d'une Weibull generale",
                             ),
 
                  C1 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "4.",
                              fr = "coef du coef c(T) d'une Weibull generale",
                             ),
 
                  C2 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "0.",
                              fr = "coef du coef c(T) d'une Weibull generale",
                             ),
 
                  C3 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "0.",
                              fr = "coef du coef c(T) d'une Weibull generale",
                             ),

                  nbectKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIc (nb sigma) : det = -2 ",
                                   ),

                  fractKIc = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "5.",
                                    fr = "Valeur caracteristique de KIc exprimee en ordre de fractile (%) ",
                                   ),

                  nbectKIa = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma) ",
                                   ),

                              ), # Fin BLOC Parametres_WEIB_GEN

) # Fin OPER MODELES


#==================
# 5. Initialisation
#==================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)
INITIALISATION = OPER ( nom = "INITIALISATION",
                        sd_prod = loi,
                        op = 68,
                        fr = "Initialisation", 

  Liste_tempinit = SIMP ( statut = "o",
                          typ = "R",
                          max = "**",
                          fr = "Profil radial de la temperature initiale dans la cuve (m) (°C) ",
                         ),

  Prolongation_tempsinit = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                  fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                 ),

  Liste_sigmainit = SIMP ( statut = "o",
                           typ = "R",
                           max = "**",
                           fr = "Profil radial des contraintes residuelles dans la cuve (m) (xx) (xx) (xx) ",
                          ),

  Prolongation_sigmainit = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                  fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                 ),

  INSTINIT = SIMP ( statut = "o",
                    typ = "R",
                    defaut = "-1.",
                    fr = "Instant initial (s) ",
                   ),

) # Fin OPER INITIALISATION


#==================================
# 6. CARACTERISTIQUES DU REVETEMENT
#==================================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)
REVETEMENT = OPER ( nom = "REVETEMENT",
                    sd_prod = loi,
                    op = 68,
                    fr = "Caracteristiques du revetement", 

  KTHREV = SIMP ( statut = "o",
                  typ = "TXM",
                  into = ( "ENTHALPIE", "CHALEUR",),
                  #defaut = "CHALEUR",
                  fr = "Options pour definir les caracteristiques du revetement ",
                 ),

  Parametres_ENTHALPIErev = BLOC ( condition = " KTHREV in ( 'ENTHALPIE', ) ",

                  Liste_enthalpie_rev = SIMP ( statut = "o",
                                               typ = "R",
                                               max = "**",
                                               fr = "Temperature (°C) / enthalpie (J/kg) ",
                                              ),

                  Prolongation_enthalpie_rev = SIMP ( statut = "o",
                                                      typ = "TXM",
                                                      into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                      fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                     ),

                                  ), # Fin BLOC Parametres_ENTHALPIErev


  Parametres_CHALEURrev = BLOC ( condition = " KTHREV in ( 'CHALEUR', ) ",

                  Liste_chaleur_rev = SIMP ( statut = "o",
                                             typ = "R",
                                             max = "**",
                                             fr = "Temperature (°C) / chaleur volumique (J/kg/K) ",
                                            ),

                  Prolongation_chaleur_rev = SIMP ( statut = "o",
                                                    typ = "TXM",
                                                    into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                    fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                   ),

                                ), # Fin BLOC Parametres_CHALEURrev

   Liste_conductivite_rev = SIMP ( statut = "o",
                                   typ = "R",
                                   max = "**",
                                   fr = "Temperature (°C) / conductivite thermique (W/m/°C) ",
                                  ),

   Prolongation_conductivite_rev = SIMP ( statut = "o",
                                          typ = "TXM",
                                          into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                          fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                         ),

   Liste_young_rev = SIMP ( statut = "o",
                            typ = "R",
                            max = "**",
                            fr = "Temperature (°C) / module d'Young (MPa) ",
                           ),

   Prolongation_young_rev = SIMP ( statut = "o",
                                   typ = "TXM",
                                   into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                   fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                  ),

   Liste_dilatation_rev = SIMP ( statut = "o",
                                 typ = "R",
                                 max = "**",
                                 fr = "Temperature (°C) / coefficient de dilatation thermique (°C-1) ",
                                ),

   Prolongation_dilatation_rev = SIMP ( statut = "o",
                                        typ = "TXM",
                                        into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                        fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                       ),

   Liste_elasticite_rev = SIMP ( statut = "o",
                                 typ = "R",
                                 max = "**",
                                 fr = "Temperature (°C) / limite d'elasticite (MPa) ",
                                ),

   Prolongation_elasticite_rev = SIMP ( statut = "o",
                                        typ = "TXM",
                                        into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                        fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                       ),

   TREFREV = SIMP ( statut = "o",
                    typ = "R",
                    defaut = "20.",
                    fr = "Temperature de deformation nulle (°C) ",
                   ),

   TDETREV = SIMP ( statut = "o",
                    typ = "R",
                    defaut = "287.",
                    fr = "Temperature de definition du coefficient de dilatation thermique (°C) ",
                   ),

   NUREV = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "0.3",
                  fr = "Coefficient de Poisson ",
                 ),

) # Fin OPER REVETEMENT


#=====================================
# 7. CARACTERISTIQUES DU METAL DE BASE
#=====================================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)
METAL_BASE = OPER ( nom = "METAL_BASE",
                    sd_prod = loi,
                    op = 68,
                    fr = "Caracteristiques du metal de base", 

  KTHMDB = SIMP ( statut = "o",
                  typ = "TXM",
                  into = ( "ENTHALPIE", "CHALEUR",),
                  #defaut = "CHALEUR",
                  fr = "Options pour definir les caracteristiques du revetement ",
                 ),

  Parametres_ENTHALPIEmdb = BLOC ( condition = " KTHMDB in ( 'ENTHALPIE', ) ",

                  Liste_enthalpie_mdb = SIMP ( statut = "o",
                                               typ = "R",
                                               max = "**",
                                               fr = "Temperature (°C) / enthalpie (J/kg) ",
                                              ),

                  Prolongation_enthalpie_mdb = SIMP ( statut = "o",
                                                      typ = "TXM",
                                                      into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                      fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                     ),

                                  ), # Fin BLOC Parametres_ENTHALPIEmdb


  Parametres_CHALEURmdb = BLOC ( condition = " KTHMDB in ( 'CHALEUR', ) ",

                  Liste_chaleur_mdb = SIMP ( statut = "o",
                                             typ = "R",
                                             max = "**",
                                             fr = "Temperature (°C) / chaleur volumique (J/kg/K) ",
                                            ),

                  Prolongation_chaleur_mdb = SIMP ( statut = "o",
                                                    typ = "TXM",
                                                    into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                    fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                   ),

                                ), # Fin BLOC Parametres_CHALEURmdb

   Liste_conductivite_mdb = SIMP ( statut = "o",
                                   typ = "R",
                                   max = "**",
                                   fr = "Temperature (°C) / conductivite thermique (W/m/°C) ",
                                  ),

   Prolongation_conductivite_mdb = SIMP ( statut = "o",
                                          typ = "TXM",
                                          into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                          fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                         ),

   Liste_young_mdb = SIMP ( statut = "o",
                            typ = "R",
                            max = "**",
                            fr = "Temperature (°C) / module d'Young (MPa) ",
                           ),

   Prolongation_young_mdb = SIMP ( statut = "o",
                                   typ = "TXM",
                                   into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                   fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                  ),

   Liste_dilatation_mdb = SIMP ( statut = "o",
                                 typ = "R",
                                 max = "**",
                                 fr = "Temperature (°C) / coefficient de dilatation thermique (°C-1) ",
                                ),

   Prolongation_dilatation_mdb = SIMP ( statut = "o",
                                        typ = "TXM",
                                        into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                        fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                       ),

   TREFMDB = SIMP ( statut = "o",
                    typ = "R",
                    defaut = "20.",
                    fr = "Temperature de deformation nulle (°C) ",
                   ),

   TDETMDB = SIMP ( statut = "o",
                    typ = "R",
                    defaut = "287.",
                    fr = "Temperature de definition du coefficient de dilatation thermique (°C) ",
                   ),

   NUMDB = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "0.3",
                  fr = "Coefficient de Poisson ",
                 ),

) # Fin OPER METAL_BASE


#================
# 8. TRANSITOIRES
#================

# Nota : les variables de type OPER doivent etre en majuscules !
# Nota : les variables de type OPER doivent etre de premier niveau (pas imbriquees dans un autre type)
TRANSITOIRE = OPER ( nom = "TRANSITOIRE",
                     sd_prod = loi,
                     op = 68,
                     fr = "Description du transitoire", 

  Liste_pression = SIMP ( statut = "o",
                          typ = "R",
                          max = "**",
                          fr = "instant (s) / pression (MPa) ",
                         ),

  Prolongation_pression = SIMP ( statut = "o",
                                 typ = "TXM",
                                 into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                 fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                ),

  TYPCLTH = SIMP ( statut = "o",
                   typ = "TXM",
                   into = ( "TEMP_IMPO", "FLUX_REP", "ECHANGE", "DEBIT", "TEMP_FLU"),
                   #defaut = "ECHANGE",
                   fr = "Type de condition thermique en paroi interne ",
                  ),

  Parametres_TEMP_IMPO = BLOC ( condition = " TYPCLTH in ( 'TEMP_IMPO', ) ",

                  Liste_temp_impo = SIMP ( statut = "o",
                                           typ = "R",
                                           max = "**",
                                           fr = "Instant (s) / Temperature imposee (°C) ",
                                          ),

                  Prolongation_temp_impo = SIMP ( statut = "o",
                                                  typ = "TXM",
                                                  into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                  fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                 ),

                               ), # Fin BLOC Parametres_TEMP_IMPO

  Parametres_FLUX_REP = BLOC ( condition = " TYPCLTH in ( 'FLUX_REP', ) ",

                  Liste_flux_rep = SIMP ( statut = "o",
                                          typ = "R",
                                          max = "**",
                                          fr = "Instant (s) / Flux de chaleur impose (W/m2) ",
                                         ),

                  Prolongation_flux_rep = SIMP ( statut = "o",
                                                 typ = "TXM",
                                                 into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                 fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                ),

                              ), # Fin BLOC Parametres_FLUX_REP

  Parametres_ECHANGE = BLOC ( condition = " TYPCLTH in ( 'ECHANGE', ) ",

                  Liste_echange_temp = SIMP ( statut = "o",
                                              typ = "R",
                                              max = "**",
                                              fr = "Instant (s) / Temperature impose (°C) ",
                                             ),

                  Prolongation_echange_temp = SIMP ( statut = "o",
                                                     typ = "TXM",
                                                     into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                     fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                    ),

                  Liste_echange_coef = SIMP ( statut = "o",
                                              typ = "R",
                                              max = "**",
                                              fr = "Instant (s) / Coefficient d echange (W/m2/K) ",
                                             ),

                  Prolongation_echange_coef = SIMP ( statut = "o",
                                                     typ = "TXM",
                                                     into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                     fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                    ),

                             ), # Fin BLOC Parametres_ECHANGE

  Parametres_DEBIT = BLOC ( condition = " TYPCLTH in ( 'DEBIT', ) ",

                  Liste_debit = SIMP ( statut = "o",
                                       typ = "R",
                                       max = "**",
                                       fr = "Instant (s) / Debit massique (kg/s) ",
                                      ),

                  Prolongation_debit = SIMP ( statut = "o",
                                              typ = "TXM",
                                              into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                              fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                             ),

                  Liste_temp_injection = SIMP ( statut = "o",
                                                typ = "R",
                                                max = "**",
                                                fr = "Instant (s) / Temperature d injection de securite  (°C) ",
                                               ),

                  Prolongation_temp_injection = SIMP ( statut = "o",
                                                       typ = "TXM",
                                                       into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                       fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                      ),

                  DH = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "-2.",
                              fr = "Diametre hydraulique (m) ",
                             ),

                  SECTION = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "-2.",
                                   fr = "Section espace annulaire (m2) ",
                                  ),

                  DELTA = SIMP ( statut = "o",
                                 typ = "R",
                                 defaut = "-2.",
                                 fr = "Hauteur caracteristique convection naturelle (m) ",
                                ),

                  ALPHA_CF = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "1.",
                                    fr = "Coefficient Vestale convection forcee (-) ",
                                   ),

                  ALPHA_CN = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "1.",
                                    fr = "Coefficient Vestale convection naturelle (-) ",
                                   ),

                  EPS = SIMP ( statut = "o",
                               typ = "R",
                               defaut = "0.00001",
                               fr = "Critere convergence relative (-) ",
                              ),

                  VM = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "-2.",
                              fr = "Volume de melange CREARE (m3) ",
                             ),

                  T0 = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "-2.",
                              fr = "Temperature initiale CREARE (degC) ",
                             ),

                  SE = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "-2.",
                              fr = "Surface d'echange fluide/structure (m2) ",
                             ),

                           ), # Fin BLOC Parametres_DEBIT

  Parametres_TEMP_FLU = BLOC ( condition = " TYPCLTH in ( 'TEMP_FLU', ) ",

                  Liste_temp_flu = SIMP ( statut = "o",
                                          typ = "R",
                                          max = "**",
                                          fr = "Instant (s) / Debit massique (kg/s) ",
                                         ),

                  Prolongation_temp_flu = SIMP ( statut = "o",
                                                 typ = "TXM",
                                                 into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                 fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                ),

                  Liste_debit_injection = SIMP ( statut = "o",
                                                 typ = "R",
                                                 max = "**",
                                                 fr = "Instant (s) / Debit d injection de securite (kg/s) ",
                                                ),

                  Prolongation_debit_injection = SIMP ( statut = "o",
                                                        typ = "TXM",
                                                        into = ( 'CC', 'CE', 'CL', 'EC', 'EE', 'EL', 'LC', 'LE', 'LL'),
                                                        fr = "Prolongation aux frontieres amont et aval : C=constant, E=exclus, L=lineaire ",
                                                       ),

                  DH = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "-2.",
                              fr = "Diametre hydraulique (m) ",
                             ),

                  SECTION = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "-2.",
                                   fr = "Section espace annulaire (m2) ",
                                  ),

                  DELTA = SIMP ( statut = "o",
                                 typ = "R",
                                 defaut = "-2.",
                                 fr = "Hauteur caracteristique convection naturelle (m) ",
                                ),

                  ALPHA_CF = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "1.",
                                    fr = "Coefficient Vestale convection forcee (-) ",
                                   ),

                  ALPHA_CN = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "1.",
                                    fr = "Coefficient Vestale convection naturelle (-) ",
                                   ),

                  EPS = SIMP ( statut = "o",
                               typ = "R",
                               defaut = "0.00001",
                               fr = "Critere convergence relative (-) ",
                              ),

                              ), # Fin BLOC Parametres_TEMP_FLU

) # Fin OPER TRANSITOIRE


#================================
# 3. Definition de l'etude
#================================

# Nota : les variables de type PROC doivent etre en majuscules !
CRITERIA = PROC ( nom = "CRITERIA",
                  op = None,
                  docu = "",
                  fr = "Mise en donnee pour le fichier de configuration de OPENTURNS.",
                  ang = "Writes the configuration file for OPENTURNS.",



  Type = SIMP ( statut = "o",
                typ = "TXM",
                into = ( "Min/Max", "Central Uncertainty", "Threshold Exceedence" ),
                fr = "Type d'Analyse",
                ang = "Analysis",
                ),




  MinMax = BLOC ( condition = " Type in ( 'Min/Max', ) ",

                  Method = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( "Experiment Plane", "Random Sampling" ),
                                  fr = "Methode",
                                  ang = "Method",
                                  ),
                  # UC 3.1.1
                  ExperimentPlaneSettings = BLOC ( condition = " Method in ( 'Experiment Plane', ) ",

                          ExperimentPlane = SIMP ( statut = "o",
                                                   typ = "TXM",
                                                   into = ( "Axial", "Factorial", "Composite", ),
                                                   fr = "Methode",
                                                   ang = "Method",
                                                   ),

                          Levels = SIMP ( statut = "o",
                                          typ = "R",
                                          val_min = 0.0,
                                          max = '**',    
                                          fr = "Nombre de niveaux dans chaque direction",
                                          ang = "Levels in each direction",
                                          ),

                          # Scaled Vector
                          UnitsPerDimension = SIMP ( statut = "o",
                                          typ = "R",
                                          max = '**',    
                                          fr = "Unite par dimension (autant que de variables declarees)",
                                          ang = "Units per dimension (as much as declared variables)",
                                          ),

                          # Translation Vector
                          Center = SIMP ( statut = "o",
                                          typ = "R",
                                          max = '**',    
                                          fr = "Unite par dimension",
                                          ang = "Units per dimension",
                                          ),

                    ), # Fin BLOC ExperimentPlaneSettings



                  RandomSamplingSettings = BLOC ( condition = " Method in ( 'Random Sampling', ) ",

                          PointsNumber = SIMP ( statut = "o",
                                                typ = "I",
                                                val_min = 1,
                                                fr = "Nombre de points",
                                                ang = "Points number",
                                                ),

                    ), # Fin BLOC RandomSamplingSettings

                  Result = SIMP (  statut = "o",
                                   typ = "TXM",
                                   into = ( "Min/Max", ),
                                   defaut = "Min/Max",
                                   fr = "Le minimum et le maximum",
                                   ang = "The min and max values",
                                   ),


  ), # Fin BLOC MinMax




  CentralUncertainty = BLOC ( condition = " Type in ( 'Central Uncertainty', ) ",

                  Method = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( "Taylor Variance Decomposition", "Random Sampling" ),
                                  fr = "Methode",
                                  ang = "Method",
                                  ),
                              
                  # UC 3.2.
                  TaylorVarianceDecompositionSettings = BLOC ( condition = " Method in ( 'Taylor Variance Decomposition', ) ",

                      Result = FACT ( statut = "o",
                                      min = 1,
                                      max = "**",

                              MeanFirstOrder = SIMP ( statut = "o",
                                                typ = 'TXM',
                                                into = ( 'yes', 'no' ),
                                                defaut = 'yes',
                                                max = 1,
                                                fr = "Moyenne au premier ordre",
                                                ang = "MeanFirstOrder",
                                                ),

                              StandardDeviationFirstOrder = SIMP ( statut = "o",
                                                                   typ = 'TXM',
                                                                   into = ( 'yes', 'no' ),
                                                                   defaut = 'yes',
                                                                   max = 1,
                                                                   fr = "Ecart-type au premier ordre",
                                                                   ang = "StandardDeviationFirstOrder",
                                                                   ),

                              MeanSecondOrder = SIMP ( statut = "o",
                                                       typ = 'TXM',
                                                       into = ( 'yes', 'no' ),
                                                       defaut = 'yes',
                                                       max = 1,
                                                       fr = "Moyenne au second ordre",
                                                       ang = "MeanSecondOrder",
                                                       ),

                              ImportanceFactor = SIMP ( statut = "o",
                                                        typ = 'TXM',
                                                        into = ( 'yes', 'no' ),
                                                        defaut = 'no',
                                                        max = 1,
                                                        fr = "Facteur d'importance pour variable de sortie scalaire",
                                                        ang = "ImportanceFactor",
                                                        ),

                             ImportanceFactorSettings = BLOC ( condition = " ImportanceFactor in ( 'yes', ) ",

                                    NumericalResults  = SIMP ( statut = "o",
                                                               typ = 'TXM',
                                                               into = ( 'yes', 'no' ),
                                                               defaut = 'yes',
                                                               max = 1,
                                                               fr = "Resultats numeriques",
                                                               ang = "NumericalResults",
                                                               ),

                                     GraphicalResults  = SIMP ( statut = "o",
                                                                typ = 'TXM',
                                                                into = ( 'yes', 'no' ),
                                                                defaut = 'no',
                                                                max = 1,
                                                                fr = "Resultats graphiques",
                                                                ang = "GraphicalResults",
                                                                ),

                            ), # Fin BLOC ImportanceFactorSettings

                      ), # Fin FACT Result
                                                               
                  ), # Fin BLOC TaylorVarianceDecompositionSettings



                  RandomSamplingSettings = BLOC ( condition = " Method in ( 'Random Sampling', ) ",

                          PointsNumber = SIMP ( statut = "o",
                                                typ = "I",
                                                val_min = 1,
                                                fr = "Nombre de points",
                                                ang = "Points number",
                                                ),

                       Result = FACT ( statut = "o",
                                      min = 1,
                                      max = "**",

                              EmpiricalMean = SIMP ( statut = "o",
                                                     typ = 'TXM',
                                                     into = ( 'yes', 'no' ),
                                                     defaut = 'yes',
                                                     max = 1,
                                                     fr = "Moyenne empirique",
                                                     ang = "Empirical mean",
                                                     ),

                              EmpiricalStandardDeviation = SIMP ( statut = "o",
                                                                  typ = 'TXM',
                                                                  into = ( 'yes', 'no' ),
                                                                  defaut = 'yes',
                                                                  max = 1,
                                                                  fr = "Ecart-type empirique",
                                                                  ang = "Empirical standard deviation",
                                                                  ),

                              EmpiricalQuantile = SIMP ( statut = "o",
                                                         typ = 'R',
                                                         defaut = 0.0,
                                                         max = 1,
                                                         val_min = 0.0,
                                                         val_max = 1.0,
                                                         fr = "Quantile empirique",
                                                         ang = "Empirical quantile",
                                                         ),

                              AnalysedCorrelations = SIMP ( statut = "o",
                                                            typ = 'TXM',
                                                            into = ( 'yes', 'no' ),
                                                            defaut = 'no',
                                                            max = 1,
                                                            fr = "Correlations analysees",
                                                            ang = "Analysed correlations",
                                                            ),

                              KernelSmoothing = SIMP ( statut = "o",
                                                       typ = 'TXM',
                                                       into = ( 'yes', 'no' ),
                                                       defaut = 'no',
                                                       max = 1,
                                                       fr = "Kernel smoothing de l'echantillon",
                                                       ang = "Kernel smoothing of the sample",
                                                       ),

                      ), # Fin FACT Result
                                                               
                  ), # Fin BLOC RandomSamplingSettings

  ), # Fin BLOC CentralUncertainty




  ThresholdExceedence = BLOC ( condition = " Type in ( 'Threshold Exceedence', ) ",

         Event =  FACT ( statut = "o",
                         min = 1,
                         max = 1,

                         Threshold = SIMP ( statut = "o",
                                            typ = "R",
                                            max = 1,
                                            fr = "Le seuil de defaillance",
                                            ang = "Failure threshold",
                                            ),

                         ComparisonOperator = SIMP ( statut = "o",
                                                     typ = "TXM",
                                                     max = 1,
                                                     into = ( "Less", "LessOrEqual", "Equal", "GreaterOrEqual", "Greater" ),
                                                     fr = "Que faut-il ne pas depasser : un maximum ou un minimum",
                                                     ang = "What is the failure threshold : maximum or minimum",
                                                     ),
         ), # Fin FACT Event
                         

         Method = SIMP ( statut = "o",
                         typ = "TXM",
                         into = ( "Simulation", "Analytical" ),
                         fr = "Methode",
                         ang = "Method",
                         ),

         SimulationSettings = BLOC ( condition = " Method in ( 'Simulation', ) ",

               Algorithm = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( "MonteCarlo", "LHS", "ImportanceSampling" ),
                                  fr = "Algorithme de simulation",
                                  ang = "Simulation algorithm",
                                  ),

                                 
               RandomGenerator = FACT ( statut = "o",
                                        min = 1,
                                        max = 1,

                           SeedToBeSet = SIMP ( statut = "o",
                                                typ = 'TXM',
                                                into = ( 'yes', 'no' ),
                                                defaut = 'no',
                                                max = 1,
                                                fr = "La racine du generateur aleatoire doit-elle etre positionnee ?",
                                                ang = "Does the random generator seed need to be set ?",
                                                ),

                           SeedSettings = BLOC ( condition = " SeedToBeSet in ( 'yes', ) ",

                                                 RandomGeneratorSeed = SIMP ( statut = "o",
                                                                              typ = "I",
                                                                              max = 1,
                                                                              fr = "Racine du generateur aleatoire",
                                                                              ang = "Random generator seed",
                                                                              ),

                                               ), # Fin BLOC SeedSettings

               ), # Fin FACT RandomGenerator


               BlockSize = SIMP ( statut = "f",
                                  typ = "I",
                                  max = 1,
                                  val_min = 1,
                                  defaut = 1,
                                  fr = "Nombre de calculs realises en bloc",
                                  ang = "Number of computations as a block",
                                  ),

               MaximumOuterSampling = SIMP ( statut = "o",
                                             typ = "I",
                                             max = 1,
                                             val_min = 1,
                                             fr = "Maximum d'iterations externes",
                                             ang = "Maximum outer Sampling value",
                                             ),

               MaximumCoefficientOfVariation = SIMP ( statut = "f",
                                                      typ = "R",
                                                      max = 1,
                                                      defaut = 0.1,
                                                      val_min = 0.0,
                                                      fr = " maximum ...",
                                                      ang = "Absolute maximum ...."
                                                      ),

               ImportanceSamplingSettings = BLOC ( condition = " Algorithm in ( 'ImportanceSampling', ) ",

                            MeanVector = SIMP ( statut = "o",
                                                typ = "R",
                                                max = "**",
                                                fr = "Moyenne",
                                                ang = "Mean vector",
                                                ),

                            Correlation = SIMP ( statut = "o",
                                                 typ = 'TXM',
                                                 into = ( 'Independent', 'Linear' ),
                                                 defaut = 'Linear',
                                                 max = 1,
                                                 fr = "Le type de correlation entre les variables",
                                                 ang = "Correlation between variables",
                                                 ),

               ), # Fin BLOC ImportanceSamplingSettings

               Result = FACT ( statut = "o",
                                      min = 1,
                                      max = "**",

                    Probability = SIMP ( statut = "o",
                                         typ = 'TXM',
                                         into = ( 'yes', ),
                                         defaut = 'yes',
                                         max = 1,
                                         fr = "Probabiblite",
                                         ang = "Probability",
                                         ),

                    ConfidenceInterval = SIMP ( statut = "o",
                                                typ = 'TXM',
                                                into = ( 'yes', 'no' ),
                                                defaut = 'yes',
                                                max = 1,
                                                fr = "Ecart-type empirique",
                                                ang = "Empirical standard deviation",
                                                ),

                    ConfidenceIntervalSettings = BLOC ( condition = " ConfidenceInterval in ( 'yes', ) ",

                          Level = SIMP ( statut = "o",
                                         typ = 'R',
                                         defaut = 0.0,
                                         max = 1,
                                         val_min = 0.0,
                                         val_max = 1.0,
                                         fr = "Niveau de confiance",
                                         ang = "Confidence level",
                                         ),
                                                     
                    ), # Fin BLOC ConfidenceIntervalSettings
                               
                    VariationCoefficient = SIMP ( statut = "o",
                                                  typ = 'TXM',
                                                  into = ( 'yes', 'no' ),
                                                  defaut = 'yes',
                                                  max = 1,
                                                  fr = "Coefficient de variation",
                                                  ang = "VariationCoefficient",
                                                  ),

                    IterationNumber = SIMP ( statut = "o",
                                             typ = 'TXM',
                                             into = ( 'yes', 'no' ),
                                             defaut = 'yes',
                                             max = 1,
                                             fr = "Nombre d'iterations",
                                             ang = "Iteration number",
                                             ),

                    ConvergenceGraph = SIMP ( statut = "o",
                                             typ = 'TXM',
                                             into = ( 'yes', 'no' ),
                                             defaut = 'yes',
                                             max = 1,
                                             fr = "Graphe de convergence",
                                             ang = "Convergence graph",
                                             ),

               ), # Fin FACT Result
                                                               


         ), # Fin BLOC SimulationSettings


                               
         AnalyticalSettings = BLOC ( condition = " Method in ( 'Analytical', ) ",

                Approximation = SIMP ( statut = "o",
                                       typ = "TXM",
                                       into = ( "FORM", "SORM" ),
                                       fr = "Approximation",
                                       ang = "Approximation",
                                       ),

                OptimizationAlgorithm = SIMP ( statut = "o",
                                               typ = "TXM",
                                               into = ( "Cobyla", "AbdoRackwitz" ),
                                               fr = "Methode d'optimisation",
                                               ang = "Optimisation method",
                                               ),

                                     
                PhysicalStartingPoint = SIMP ( statut = "f",
                                               typ = "R",
                                               max = "**",
                                               fr = "Point de demarrage de l'algorithme iteratif",
                                               ang = "Initial point for iterative process",
                                               ),

                MaximumIterationsNumber = SIMP ( statut = "f",
                                                 typ = "I",
                                                 max = 1,
                                                 val_min = 1,
                                                 fr = "Nombre maximum d iterations",
                                                 ang = "Maximum number of iterations",
                                                 ),

                regles = ( EXCLUS ( "MaximumAbsoluteError", "RelativeAbsoluteError" ),  ),
                                     
                MaximumAbsoluteError = SIMP ( statut = "f",
                                              typ = "R",
                                              max = 1,
                                              defaut = 1E-6,
                                              val_min = 0.0,
                                              fr = "Distance maximum absolue entre 2 iterations successifs",
                                              ang = "Absolute maximum distance between 2 successive iterates",
                                              ),

                RelativeAbsoluteError = SIMP ( statut = "f",
                                               typ = "R",
                                               max = 1,
                                               defaut = 1E-6,
                                               val_min = 0.0,
                                               fr = "Distance maximum relative entre 2 iterations successives",
                                               ang = "Relative maximum distance between 2 successive iterates",
                                               ),
                                     
                MaximumConstraintError = SIMP ( statut = "f",
                                                typ = "R",
                                                max = 1,
                                                val_min = 0.0,
                                                fr = "Valeur maximum absolue de la fonction moins la valeur du niveau",
                                                ang = "Maximum absolute value of the constraint function minus the level value",
                                                ),

                ImportanceSampling = SIMP ( statut = "o",
                                            typ = 'TXM',
                                            into = ( 'yes', 'no' ),
                                            defaut = 'no',
                                            max = 1,
                                            fr = "Tirage d'importance au point de conception",
                                            ang = "Importance sampling at design point",
                                            ),

                FORM = BLOC ( condition = " Approximation in ( 'FORM', ) ",

                    Probability = SIMP ( statut = "o",
                                         typ = 'TXM',
                                         into = ( 'yes', ),
                                         defaut = 'yes',
                                         max = 1,
                                         fr = "Probabiblite",
                                         ang = "Probability",
                                         ),

                    DesignPoint = SIMP ( statut = "o",
                                         typ = 'TXM',
                                         into = ( 'yes', 'no' ),
                                         defaut = 'yes',
                                         max = 1,
                                         fr = "Point de conception",
                                         ang = "Design point",
                                         ),

                    HasReliabilityIndex = SIMP ( statut = "o",
                                                 typ = 'TXM',
                                                 into = ( 'yes', 'no' ),
                                                 defaut = 'yes',
                                                 max = 1,
                                                 fr = "Indice de fiabilite",
                                                 ang = "Reliability index",
                                                 ),

                    ImportanceFactor = SIMP ( statut = "o",
                                              typ = 'TXM',
                                              into = ( 'yes', 'no' ),
                                              defaut = 'no',
                                              max = 1,
                                              fr = "Facteur d'importance pour variable de sortie scalaire",
                                              ang = "ImportanceFactor",
                                              ),

                    ImportanceFactorSettings = BLOC ( condition = " ImportanceFactor in ( 'yes', ) ",

                            NumericalResults  = SIMP ( statut = "o",
                                                       typ = 'TXM',
                                                       into = ( 'yes', 'no' ),
                                                       defaut = 'yes',
                                                       max = 1,
                                                       fr = "Resultats numeriques",
                                                       ang = "NumericalResults",
                                                       ),

                             GraphicalResults  = SIMP ( statut = "o",
                                                        typ = 'TXM',
                                                        into = ( 'yes', 'no' ),
                                                        defaut = 'no',
                                                        max = 1,
                                                        fr = "Resultats graphiques",
                                                        ang = "GraphicalResults",
                                                        ),

                    ), # Fin BLOC ImportanceFactorSettings


                    SensitivityAnalysis = SIMP ( statut = "o",
                                                 typ = 'TXM',
                                                 into = ( 'yes', 'no' ),
                                                 defaut = 'no',
                                                 max = 1,
                                                 fr = "Analyse de sensibilite",
                                                 ang = "Sensitivity analysis",
                                                 ),

                    SensitivityAnalysisSettings = BLOC ( condition = " SensitivityAnalysis in ( 'yes', ) ",

                            HasoferReliabilityIndex = SIMP ( statut = "o",
                                                             typ = 'TXM',
                                                             into = ( 'yes', 'no' ),
                                                             defaut = 'no',
                                                             max = 1,
                                                             fr = "Indice de fiabilite de Hasofer",
                                                             ang = "Hasofer reliability index",
                                                             ),
        
                            HasoferReliabilityIndexSettings = BLOC ( condition = " HasoferReliabilityIndex in ( 'yes', ) ",
        
                                    NumericalResults  = SIMP ( statut = "o",
                                                               typ = 'TXM',
                                                               into = ( 'yes', 'no' ),
                                                               defaut = 'yes',
                                                               max = 1,
                                                               fr = "Resultats numeriques",
                                                               ang = "NumericalResults",
                                                               ),
        
                                     GraphicalResults  = SIMP ( statut = "o",
                                                                typ = 'TXM',
                                                                into = ( 'yes', 'no' ),
                                                                defaut = 'no',
                                                                max = 1,
                                                                fr = "Resultats graphiques",
                                                                ang = "GraphicalResults",
                                                                ),

                            ), # Fin BLOC HasoferReliabilityIndexSettings
                                                         
                    ), # Fin BLOC SensitivityAnalysisSettings

                    FunctionCallsNumber = SIMP ( statut = "o",
                                                 typ = 'TXM',
                                                 into = ( 'yes', 'no' ),
                                                 defaut = 'no',
                                                 max = 1,
                                                 fr = "Nombre d'appels a la fonction",
                                                 ang = "Function calls number",
                                                 ),


                ), # Fin BLOC FORM


                SORM = BLOC ( condition = " Approximation in ( 'SORM', ) ",


                    TvedtApproximation = SIMP ( statut = "o",
                                                typ = 'TXM',
                                                into = ( 'yes', 'no' ),
                                                defaut = 'no',
                                                max = 1,
                                                fr = "Approximation de Tvedt",
                                                ang = "Tvedt approximation",
                                                ),

                    HohenBichlerApproximation = SIMP ( statut = "o",
                                                       typ = 'TXM',
                                                       into = ( 'yes', 'no' ),
                                                       defaut = 'no',
                                                       max = 1,
                                                       fr = "Approximation de HohenBichler",
                                                       ang = "HohenBichler approximation",
                                                       ),

                    BreitungApproximation = SIMP ( statut = "o",
                                                   typ = 'TXM',
                                                   into = ( 'yes', 'no' ),
                                                   defaut = 'no',
                                                   max = 1,
                                                   fr = "Approximation de Breitung",
                                                   ang = "Breitung approximation",
                                                   ),

                    DesignPoint = SIMP ( statut = "o",
                                         typ = 'TXM',
                                         into = ( 'yes', 'no' ),
                                         defaut = 'yes',
                                         max = 1,
                                         fr = "Point de conception",
                                         ang = "Design point",
                                         ),

                    ImportanceFactor = SIMP ( statut = "o",
                                              typ = 'TXM',
                                              into = ( 'yes', 'no' ),
                                              defaut = 'no',
                                              max = 1,
                                              fr = "Facteur d'importance pour variable de sortie scalaire",
                                              ang = "ImportanceFactor",
                                              ),

                    ImportanceFactorSettings = BLOC ( condition = " ImportanceFactor in ( 'yes', ) ",

                            NumericalResults  = SIMP ( statut = "o",
                                                       typ = 'TXM',
                                                       into = ( 'yes', 'no' ),
                                                       defaut = 'yes',
                                                       max = 1,
                                                       fr = "Resultats numeriques",
                                                       ang = "NumericalResults",
                                                       ),

                             GraphicalResults  = SIMP ( statut = "o",
                                                        typ = 'TXM',
                                                        into = ( 'yes', 'no' ),
                                                        defaut = 'no',
                                                        max = 1,
                                                        fr = "Resultats graphiques",
                                                        ang = "GraphicalResults",
                                                        ),

                    ), # Fin BLOC ImportanceFactorSettings


                    SensitivityAnalysis = SIMP ( statut = "o",
                                                 typ = 'TXM',
                                                 into = ( 'yes', 'no' ),
                                                 defaut = 'no',
                                                 max = 1,
                                                 fr = "Analyse de sensibilite",
                                                 ang = "Sensitivity analysis",
                                                 ),

                    SensitivityAnalysisSettings = BLOC ( condition = " SensitivityAnalysis in ( 'yes', ) ",

                            HasoferReliabilityIndex = SIMP ( statut = "o",
                                                             typ = 'TXM',
                                                             into = ( 'yes', 'no' ),
                                                             defaut = 'no',
                                                             max = 1,
                                                             fr = "Indice de fiabilite de Hasofer",
                                                             ang = "Hasofer reliability index",
                                                             ),
        
                            HasoferReliabilityIndexSettings = BLOC ( condition = " HasoferReliabilityIndex in ( 'yes', ) ",
        
                                    NumericalResults  = SIMP ( statut = "o",
                                                               typ = 'TXM',
                                                               into = ( 'yes', 'no' ),
                                                               defaut = 'yes',
                                                               max = 1,
                                                               fr = "Resultats numeriques",
                                                               ang = "NumericalResults",
                                                               ),
        
                                     GraphicalResults  = SIMP ( statut = "o",
                                                                typ = 'TXM',
                                                                into = ( 'yes', 'no' ),
                                                                defaut = 'no',
                                                                max = 1,
                                                                fr = "Resultats graphiques",
                                                                ang = "GraphicalResults",
                                                                ),

                            ), # Fin BLOC HasoferReliabilityIndexSettings
                                                         
                    ), # Fin BLOC SensitivityAnalysisSettings

                    FunctionCallsNumber = SIMP ( statut = "o",
                                                 typ = 'TXM',
                                                 into = ( 'yes', 'no' ),
                                                 defaut = 'no',
                                                 max = 1,
                                                 fr = "Nombre d'appels a la fonction",
                                                 ang = "Function calls number",
                                                 ),


                ), # Fin BLOC SORM


                                     
        ), # Fin BLOC AnalyticalSettings


                               
  ), # Fin BLOC ThresholdExceedence



) # Fin PROC CRITERIA


#===============================
# 5. Definition des parametres
#===============================
VARI = OPER ( nom = "VARI",
                      sd_prod = variable,
                      op = None,
                      fr = "Definitions des lois marginales utilisees par les variables d'entree", 
                      type=SIMP(statut='f',defaut="IN",into=("IN","OUT"), typ = "TXM",)
              )

ESSAI=PROC(nom="ESSAI",
       op=None,
       fr="Essai",
       ang = "Test",
       
       MALOI       = SIMP(statut='o',typ=(loi,),),
       MAVARIABLE  = SIMP(statut='o',typ=(variable,),),
) ;

                     


