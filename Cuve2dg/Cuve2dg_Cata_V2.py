# -*- coding: utf-8 -*-

# --------------------------------------------------
# Definition de variables sous forme de tuple
# --------------------------------------------------

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

  __repr__=info
  __str__=info

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
                            A_CLASSER ( ('OPTIONS'), ('DEFAUT') ),
                            A_CLASSER ( ('DEFAUT'), ('CUVE') ),
                            A_CLASSER ( ('CUVE'), ('MODELES') ),
                            A_CLASSER ( ('MODELES'), ('INITIALISATION') ),
                            A_CLASSER ( ('INITIALISATION'), ('REVETEMENT') ),
                            A_CLASSER ( ('REVETEMENT'), ('METAL_BASE') ),
                            A_CLASSER ( ('METAL_BASE'), ('TRANSITOIRE') )
                          )
                 ) # Fin JDC_CATA

# --------------------------------------------------
# fin entete
# --------------------------------------------------






#================================
# 1. Definition des OPTIONS
#================================

OPTIONS = PROC ( nom = "OPTIONS",
                 op = 68,
		 repetable = 'n',
                 fr = "D�finitions des options", 

#===
# Liste des param�tres
#===

# INCRTPS
  IncrementTemporel = SIMP ( statut = "o",
                             typ = "I",
                             defaut = "1",
          	             max = 1,
                             #val_max = 100,
                             fr = "Incr�ment temporel (=1 pour calcul d�terministe)",
                             ),

# DTPREC
  IncrementMaxTemperature = SIMP ( statut = "o", 
                                   typ = "R", 
				   defaut = "0.1", 
				   max = 1, 
				   val_min = 0., 
				   val_max = 1., 
				   fr = "Incr�ment maximum d'�volution de la temp�rature par noeud et par instant (�C)",
				   ),

# DTARCH
  IncrementMaxTempsAffichage = SIMP ( statut = "o", 
                                      typ = "R", 
				      defaut = "1000.", 
				      max = 1, 
				      val_min = 0., 
				      val_max = 1000., 
				      fr = "Incr�ment maximum de temps pour l'affichage (s)",
				      ),

# NBO
# Question : NBO depend-il de TYPGEOM ??
  NombreNoeudsMaillage = SIMP ( statut = "o", 
                                typ = "R", 
				max=1, 
				val_min = 1., 
				val_max = 100., 
				fr = "Nombre de noeuds � consid�rer dans le maillage interne",
				),

# 
  ListeInstants = SIMP ( statut = "o",
                         typ = "R",
                         max = "**",
                         fr = "Liste des instants pour lesquels la temp�rature et les contraintes seront archiv�s",
                         ),

) # Fin PROC OPTIONS

#================================
# 2. Caracteristiques du DEFAUT
#================================

DEFAUT = PROC ( nom = "DEFAUT",
                op = 68,
		repetable = 'n',
                fr = "Caract�ristiques du d�faut", 

#===
# Liste des param�tres
#===

# TYPEDEF
  TypeInitial = SIMP ( statut = "o", typ = "TXM",
                       into = ( "Sous Revetement", # DSR
                                "Debouchant", # DD
                                 ),
                       fr = "Type initial du d�faut : sous rev�tement ou d�bouchant",
                       ),

#====
# Definition des parametres selon le type du defaut
#====

  SousRevetement = BLOC ( condition = " TypeInitial in ( 'Sous Revetement', ) ",

    # ORIEDEF
    Orientation = SIMP ( statut = "o",
                         typ = "TXM",
                         into = ( "Longitudinale", # LONGITUD
		                  "Circonferentielle" ), # CIRCONF
                         fr = "Orientation du d�faut",
                         ),

    # PROFDEF
    ProfondeurRadiale = SIMP ( statut = "o",
                               typ = "R",
                               #defaut = "0.006",
                               max = 1,
                               val_max = 1.,
                               fr = "Profondeur radiale du d�faut (m)",
                               ),

    # OPTLONG
    OptionCalculLongueur = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( "Valeur", # VALEUR
			                   "Relation lineaire avec la longueur" ), # RAPPORT
                                  #defaut = "VALEUR",
                                  fr = "Option pour caract�riser la longueur du d�faut : soit par valeur, soit par un rapport LONG/PROF",
                                  ),

    Option_Valeur = BLOC ( condition = "OptionCalculLongueur in ( 'Valeur', ) ",

      # LONGDEF
      Longueur = SIMP ( statut = "o",
                        typ = "R",
                        #defaut = "0.060",
                        max = 1,
                        val_max = 1.,
                        fr = "Longueur du d�faut sous rev�tement (m)",
                        ),

    ), # Fin BLOC Option_Valeur

    Option_Rapport = BLOC ( condition = "OptionCalculLongueur in ( 'Relation lineaire avec la longueur', ) ",

        # LONGSURPROF
        LongueurSurProfondeur = SIMP ( statut = "o",
                                       typ = "R",
                                       #defaut = "6.",
                                       max = 1,
                                       val_max = 100.,
                                       fr = "Rapport longueur/profondeur du d�faut sous rev�tement",
                                       ),

    ), # Fin BLOC Option_Rapport

    # DECADEF
    DecalageRadial = SIMP ( statut = "o",
                            typ = "R",
                            #defaut = "-0.00001",
                            fr = "D�calage radial du defaut sous rev�tement (m)",
                            ),

    # ANGLDEF
    Azimut = SIMP ( statut = "o",
                    typ = "R",
                    defaut = "0.",
                    fr = "Position angulaire du d�faut dans le cylindre de cuve (degr�s)",
                    ),

    # ALTIDEF
    Altitude = SIMP ( statut = "o",
                      typ = "R",
                      defaut = "2.",
		      val_min = 0.,
		      val_max = 4.,
                      fr = "Altitude du d�faut sur le cylindre de cuve (m)",
                      ),

    # POINDEF
    Pointe = SIMP ( statut = "o",
                    typ = "TXM",
                    into = ( "A", "B" ),
                    defaut = "A",
                    fr = "Choix du point consid�r� du d�faut sous rev�tement",
                    ),

    # ARRETFISSURE
    ArretDeFissure = SIMP ( statut = "o",
                            typ = "TXM",
                            into = ( "OUI", "NON" ),
                            defaut = "NON",
                            fr = "Prise en compte de l'arr�t de fissure",
                            ),

    # INCRDEF
    IncrementTailleFissure = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "0.005",
                                    fr = "Incr�ment de la taille de fissure pour la propagation (m)",
                                    ),

    # CORRECPLASTIC
    CorrectionPlastiqueBeta = SIMP ( statut = "o",
                                     typ = "TXM",
                                     into = ( "OUI", "NON" ),
                                     defaut = "NON",
                                     fr = "Prise en compte de la correction plastique BETA dans le calcul du facteur d'intensit� de contraintes",
                                     ),

  ), # Fin BLOC SousRevetement

  Debouchant = BLOC ( condition = " TypeInitial in ( 'Debouchant', ) ",

    # ORIEDEF
    Orientation = SIMP ( statut = "o",
                         typ = "TXM",
                         into = ( "Longitudinale", # LONGITUD
		                  "Circonferentielle" ), # CIRCONF
                         #defaut = "LONGITUD",
                         fr = "Orientation du d�faut : longitudinale ou circonf�rentielle",
                         ),

    # PROFDEF
    ProfondeurRadiale = SIMP ( statut = "o",
                               typ = "R",
                               #defaut = "0.006",
                               max = 1,
                               val_max = 1.,
                               fr = "Profondeur radiale du d�faut (m)",
                               ),

    # ANGLDEF
    Azimut = SIMP ( statut = "o",
                    typ = "R",
                    defaut = "0.",
                    fr = "Position angulaire du d�faut dans le cylindre de la cuve (en degr�s)",
                    ),

    # ALTIDEF
    Altitude = SIMP ( statut = "o",
                      typ = "R",
                      defaut = "2.",
                      fr = "Altitude du d�faut sur le cylindre de la cuve (m)",
                      ),

    # ARRETFISSURE
    ArretDeFissure = SIMP ( statut = "o",
                            typ = "TXM",
                            into = ( "OUI", "NON" ),
                            defaut = "NON",
                            fr = "Prise en compte de l'arr�t de fissure",
                            ),

    # INCRDEF
    IncrementTailleFissure = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "0.005",
                                    fr = "Incr�ment de la taille de fissure pour la propagation (m)",
                                    ),

    # IRWIN
    CorrectionPlastiqueIrwin = SIMP ( statut = "o",
                                      typ = "TXM",
                                      into = ( "OUI", "NON" ),
                                      defaut = "NON",
                                      fr = "Prise en compte de la correction plastique d'Irwin dans le calcul du facteur d'intensit� de contraintes",
                                      ),

    # CORRECPLASTIC
    CorrectionPlastiqueBeta = SIMP ( statut = "o",
                                     typ = "TXM",
                                     into = ( "OUI", "NON" ),
                                     defaut = "NON",
                                     fr = "Prise en compte de la correction plastique BETA dans le calcul du facteur d'intensit� de contraintes",
                                     ),

  ), # Fin BLOC debouchant

) # Fin PROC DEFAUT


#================================
# 3. Caracteristiques de la CUVE
#================================

CUVE = PROC (nom = "CUVE",
             op = 68,
	     repetable = 'n',
             fr = "Caract�ristiques de la cuve", 

#===
# Liste des param�tres
#===

  # TYPEGEOM
  TraitementGeometrie = SIMP ( statut = "o",
                               typ = "TXM",
	                       into = ( "Topologie", # GEOMETRIE 
		                        "Maillage"), # MAILLAGE
                               #defaut = "geometrie",
                               fr = "Choix de la d�finition de la geom�trie d'une cuve",
                               ),


#====
# Definition des parametres selon le type de traitement de la geometrie
#====

  Geometrie = BLOC ( condition = " TraitementGeometrie in ( 'Topologie', ) ",

    # RINT
    RayonInterne = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "1.994",
                          fr = "Rayon interne de la cuve (m)",
                          ),

    # REXT
    RayonExterne = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "2.2015",
                          fr = "Rayon externe de la cuve (m)",
                          ),

    # LREV
    EpaisseurRevetement = SIMP ( statut = "o",
                                 typ = "R",
                                 defaut = "0.0075",
                                 fr = "Epaisseur du rev�tement (m)",
                                 ),

    # LIGMIN
    LigamentExterneMin = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "0.75",
                                fr = "Ligament externe minimal avant rupture (% de l'�paisseur de cuve)",
                                ),

  ), # Fin BLOC  Geometrie

  Maillage = BLOC ( condition = " TraitementGeometrie in ( 'Maillage', ) ",

    # Question : quel rapport avec NBO ??
    Liste_abscisses = SIMP ( statut = "o",
                             typ = "R",
                             max = "**",
                             fr = "Liste des abscisses (m)",
                             ),
  ), # Fin BLOC Maillage

) # Fin PROC CUVE

#====================================================
# 4. Modeles de fluence, d'irradiation et de tenacite
#====================================================

#=======================
# 4.1 Modeles de fluence
#=======================

MODELES = PROC ( nom = "MODELES",
                 op = 68,
	         repetable = 'n',
                 fr = "Mod�les de fluence, d'irradiation et de t�nacit�", 


#===
# Liste des param�tres
#===

  # MODELFLUENCE
  Fluence = SIMP ( statut = "o",
                   typ = "TXM",
		   into = ( "Exponentiel sans revetement k=9.7 (Reglementaire)", # Reglementaire
		            "Exponentiel sans revetement k=12.7 (France)", # France 
                            "Exponentiel sans revetement k=0. (ValeurImposee)", # ValeurImposee 
                            "Donnees francaises du palier CPY (SDM)", # SDM 
                            "Donnees francaises du palier CPY ajustees par secteur angulaire (GrandeDev)", # GrandeDev 
                            "Regulatory Guide 1.99 rev 2 (USNRC)", # USNRC 
                            "Dossier 900 MWe AP9701 rev 2 (REV_2)", # REV_2 
                            "Lissage du modele ajuste (SDM_Lissage)", # SDM_Lissage 
                            "Grand developpement (GD_Cuve)"), # GD_Cuve 
                   #defaut = "Reglementaire", 
                   fr = "Mod�le d'att�nuation de la fluence dans l'�paisseur de la cuve",
                   ),


#====
# Definition des parametres selon le modele de fluence
#====

  Reglementaire = BLOC ( condition = " Fluence in ( 'Exponentiel sans revetement k=9.7 (Reglementaire)', ) ",

    # fmax
    FluenceMax = SIMP ( statut = "o",
                        typ = "R",
                        defaut = "6.5",
                        fr = "Fluence maximale en surface interne assimil�e par la cuve (10^19 n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                        ),

  ), # Fin BLOC Reglementaire

  France = BLOC ( condition = " Fluence in ( 'Exponentiel sans revetement k=12.7 (France)', ) ",

    # fmax
    FluenceMax = SIMP ( statut = "o",
                        typ = "R",
                        defaut = "6.5",
                        fr = "Fluence maximale assimil�e par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                        ),

    # KPFRANCE = SIMP ( statut = "o",
    KPFrance = SIMP ( statut = "o",
                      typ = "R",
                      defaut = "12.7",
                      fr = "Param�tre exponentiel du mod�le France",
                      ),

  ), # Fin BLOC France

  ValeurImposee = BLOC ( condition = " Fluence in ( 'Exponentiel sans revetement k=0. (ValeurImposee)', ) ",

    # fmax
    FluenceMax = SIMP ( statut = "o",
                        typ = "R",
                        defaut = "6.5",
                        fr = "Fluence maximale assimil�e par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                        ),

  ), # Fin BLOC ValeurImposee

  SDM = BLOC ( condition = " Fluence in ( 'Donnees francaises du palier CPY' (SDM), ) ",

    # fmax
    FluenceMax = SIMP ( statut = "o",
                        typ = "R",
                        defaut = "6.5",
                        fr = "Fluence maximale assimil�e par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                        ),

  ), # Fin BLOC SDM

  USNRC = BLOC ( condition = " Fluence in ( 'Regulatory Guide 1.99 rev 2 (USNRC)', ) ",

    # fmax
    FluenceMax = SIMP ( statut = "o",
                        typ = "R",
                        defaut = "6.5",
                        fr = "Fluence maximale assimil�e par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                        ),

    KPUS = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "9.4488",
                  fr = "Param�tre exponentiel du mod�le US",
                  ),

  ), # Fin BLOC USNRC

  REV_2 = BLOC ( condition = " Fluence in ( 'Dossier 900 MWe AP9701 rev 2 (REV_2)', ) ",

    # fmax
    FluenceMax = SIMP ( statut = "o",
                        typ = "R",
                        defaut = "6.5",
                        fr = "Fluence maximale assimil�e par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                        ),

  ), # Fin BLOC REV_2

  SDM_Lissage = BLOC ( condition = " Fluence in ( 'Lissage du modele ajuste (SDM_Lissage)', ) ",

    # fmax
    FluenceMax = SIMP ( statut = "o",
                        typ = "R",
                        defaut = "6.5",
                        fr = "Fluence maximale assimil�e par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                        ),

  ), # Fin BLOC SDM_Lissage

  GrandeDev = BLOC ( condition = " Fluence in ( 'Donnees francaises du palier CPY ajustees par secteur angulaire (GrandeDev)', ) ",

    # fmax
    FluenceMax = SIMP ( statut = "o",
                        typ = "R",
                        defaut = "6.5",
                        fr = "Fluence maximale assimil�e par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                        ),

  ), # Fin BLOC GrandeDev

  GD_Cuve = BLOC ( condition = " Fluence in ( 'Grand developpement (GD_Cuve)', ) ",

    # fmax
    FluenceMax = SIMP ( statut = "o",
                        typ = "R",
                        defaut = "6.5",
                        fr = "Fluence maximale assimil�e par la cuve (n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95",
                        ),

    # COEFFLUENCE1
    FluenceAzimut0 = SIMP ( statut = "o",
                            typ = "R",
                            defaut = "5.8",
                            fr = "Fluence � l'azimut 0 (10^19 n/cm2)",
                            ),

    # COEFFLUENCE2
    FluenceAzimut5 = SIMP ( statut = "o",
                            typ = "R",
                            defaut = "5.48",
                            fr = "Fluence � l'azimut 5 (10^19 n/cm2)",
                            ),

    # COEFFLUENCE3
    FluenceAzimut10 = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "4.46",
                             fr = "Fluence � l'azimut 10 (10^19 n/cm2)",
                             ),

    # COEFFLUENCE4
    FluenceAzimut15 = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "3.41",
                             fr = "Fluence � l'azimut 15 (10^19 n/cm2)",
                             ),

    # COEFFLUENCE5
    FluenceAzimut20 = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "3.37",
                             fr = "Fluence � l'azimut 20 (10^19 n/cm2)",
                             ),

    # COEFFLUENCE6
    FluenceAzimut25 = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "3.16",
                             fr = "Fluence � l'azimut 25 (10^19 n/cm2)",
                             ),

    # COEFFLUENCE7
    FluenceAzimut30 = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "2.74",
                             fr = "Fluence � l'azimut 30 (10^19 n/cm2)",
                             ),

    # COEFFLUENCE8
    FluenceAzimut35 = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "2.25",
                             fr = "Fluence � l'azimut 35 (10^19 n/cm2)",
                             ),

    # COEFFLUENCE9
    FluenceAzimut40 = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "1.89",
                             fr = "Fluence � l'azimut 40 (10^19 n/cm2)",
                             ),

    # COEFFLUENCE10
    FluenceAzimut45 = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "1.78",
                             fr = "Fluence � l'azimut 45 (10^19 n/cm2)",
                             ),

  ), # Fin BLOC GD_Cuve

#==========================
# 4.2 Modeles d'irradiation
#==========================

  # TYPIRR
  Irradiation = SIMP ( statut = "o",
                       typ = "TXM",
	               into = ( "RTndt de la cuve a l instant de l analyse", # RTNDT 
		                "Modele d irradiation" ), # FLUENCE
                       fr = "Type d'irradiation",
                       ),

#====
# Definition des parametres selon le type d'irradiation
#====

  RTndt = BLOC ( condition = " Irradiation in ( 'RTndt de la cuve a l instant de l analyse', ) ",
 
    RTNDT = SIMP ( statut = "o",
                   typ = "R",
                   defaut = "73.",
                   fr = "RTNDT de la cuve � l'instant de l'analyse (�C)",
                   ),

  ), # Fin BLOC RTndt

  Modele = BLOC ( condition = " Irradiation in ( 'Modele d irradiation', ) ",
 
    # MODELIRR
    ModeleIrradiation = SIMP ( statut = "o",
                               typ = "TXM",
		               into = ( "Metal de Base : formule de FIM/FIS Houssin", # HOUSSIN 
		                        "Metal de Base : formule de FIM/FIS Persoz", # PERSOZ
			                "Metal de Base : formule de FIM/FIS Lefebvre", # LEFEBVRE
				        "Metal de Base : Regulatory Guide 1.00 rev 2", # USNRCmdb
				        "Joint Soude : formulation de FIM/FIS Brillaud", # BRILLAUD
				        "Joint Soude : Regulatory Guide 1.00 rev 2" ), # USNRCsoud
                               fr = "Mod�le d'irradiation pour virole ou joint soud�",
                               ),

    # CU
    TeneurCuivre = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "0.",
                          fr = "Teneur en cuivre (%)",
                          ),

    # NI
    TeneurNickel = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "0.",
                          fr = "Teneur en nickel (%)",
                          ),

    # P
    TeneurPhosphore = SIMP ( statut = "o",
                             typ = "R",
                             defaut = "0.",
                             fr = "Teneur en phosphore (%)",
                             ),

    Parametres_USNRC = BLOC ( condition = " ModeleIrradiation in ( 'Joint Soude : Regulatory Guide 1.00 rev 2', 'Metal de Base : Regulatory Guide 1.00 rev 2' , ) ",
 
      # RTimoy
      MoyenneRTndt = SIMP ( statut = "o",
                            typ = "R",
                            defaut = "0.",
                            fr = "Moyenne de RTNDT : virole C1 de cuve Chinon : mdb=>-17.�C et js=>42.�C (HT-56/05/038 : p.52)",
                            ),

      # RTicov
      CoefVariationRTndt = SIMP ( statut = "o",
                                  typ = "R",
                                  defaut = "0.",
                                  fr = "Coefficient de variation de la RTNDT initiale",
                                  ),

      # USectDRT
      EcartTypeRTndt = SIMP ( statut = "o",
                              typ = "R",
                              defaut = "28.",
                              fr = "Ecart-type du d�calage de RTNDT (�F) (28. pour js et 17. pour mdb)",
                              ),

      # nbectDRTNDT
      NombreEcartTypeRTndt = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "2.",
                                    fr = "Nombre d'�cart-type par rapport � la moyenne de DRTNDT",
                                    ),

    ), # Fin BLOC Parametres_USNRC 

  ), # Fin BLOC Modele

#========================
# 4.3 Modeles de tenacite
#========================

  # MODELKIC
  Tenacite = SIMP ( statut = "o",
                    typ = "TXM",
		    into = ( "RCC-M/ASME coefficient=2", # RCC-M
			     "RCC-M/ASME coefficient=2.33 (Houssin)", # Houssin_RC
		             "RCC-M/ASME avec KI=KIpalier", # RCC-M_pal
			     "RCC-M/ASME avec KI~exponentiel", # RCC-M_exp
			     "Weibull basee sur la master cuve", # Wallin
			     "Weibull basee sur la master cuve (REME)", # REME
			     "Weibull n�1 (etude ORNL)", # ORNL
			     "Weibull n�2", # WEIB2
			     "Weibull n�3", # WEIB3
			     "Weibull generalisee", # WEIB_GEN
			     "Exponentielle n�1 (Frama)", # Frama
			     "Exponentielle n�2 (LOGWOLF)" ), # LOGWOLF
                    fr = "Mod�le de t�nacit�",
                    ),

#====
# Definition des parametres selon le modele de tenacit�
#====

  RCCM_delta2 = BLOC ( condition = " Tenacite in ( 'RCC-M/ASME coefficient=2', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caract�ristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # KICPAL
    PalierDuctile_KIc = SIMP ( statut = "o",
                               typ = "R",
                               defaut = "195.",
                               fr = "Palier d�terministe de K1c quand mod�le RCC-M  (MPa(m^0.5)) ",
                               ),

    # KICCDVD = SIMP ( statut = "o",
    CoefficientVariation_KIc = SIMP ( statut = "o",
                                      typ = "R",
                                      defaut = "0.15",
                                      fr = "Coefficient de variation de la loi normale de K1c quand mod�le RCC-M ",
                                      ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),


    # KIAPAL
    PalierDuctile_KIa = SIMP ( statut = "o",
                               typ = "R",
                               defaut = "195.",
                               fr = "Palier d�terministe de K1a -t�nacite � l'arr�t- quand mod�le RCC-M  (MPa(m^0.5)) ",
                               ),

    # KIACDV
    CoefficientVariation_KIa = SIMP ( statut = "o",
                                      typ = "R",
                                      defaut = "0.10",
                                      fr = "Coefficient de variation de la loi normale de K1a -t�nacite � l'arr�t- quand mod�le RCC-M ",
                                      ),

  ), # Fin BLOC Parametres_RCC-M

  RCCM_KIpal = BLOC ( condition = " Tenacite in ( 'RCC-M/ASME avec KI=KIpalier', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caract�ristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_RCCMpal

  RCCM_KIexp = BLOC ( condition = " Tenacite in ( 'RCC-M/ASME avec KI~exponentiel', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caract�ristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_RCCMexp

  RCCM_delta233 = BLOC ( condition = " Tenacite in ( 'RCC-M/ASME coefficient=2.33 (Houssin)', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caract�ristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_Houssin_RC
      
  Weibull_MasterCuve = BLOC ( condition = " Tenacite in ( 'Weibull basee sur la master cuve', ) ",
 
    # T0WALLIN
    Temperature_KIc100 = SIMP ( statut = "o",
                                typ = "I",
                                defaut = "-27",
                                fr = "Param�tre T0 du mod�le Wallin (�C) : temp�rature pour laquelle la t�ncit� du mat�riau vaut en moyenne 100MPa.m^5",
                                ),

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caract�ristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_Wallin

  Weibull_MasterCuveREME = BLOC ( condition = " Tenacite in ( 'Weibull basee sur la master cuve (REME)', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caract�ristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_REME

  Weibull1_ORNL = BLOC ( condition = " Tenacite in ( 'Weibull n�1 (etude ORNL)', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caract�ristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_ORNL

  Exponentielle1_Frama = BLOC ( condition = " Tenacite in ( 'Exponentielle n�1 (Frama)', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caracteristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_Frama

  Weibull3 = BLOC ( condition = " Tenacite in ( 'Weibull n�3', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caracteristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_WEIB3

  Weibull2 = BLOC ( condition = " Tenacite in ( 'Weibull n�2', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caracteristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_WEIB2

  Exponentielle2_LOGWOLF = BLOC ( condition = " Tenacite in ( 'Exponentielle n�2 (LOGWOLF)', ) ",

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caracteristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_LOGWOLF

  Weibull_Generalisee = BLOC ( condition = " Tenacite in ( 'Weibull generalisee',) ",
 
    Coefficients = FACT ( statut = "o",

      # A1
      A1 = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "21.263",
                  fr = "coef du coef a(T) d'une Weibull g�n�rale",
                  ),
 
      # A2
      A2 = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "9.159",
                  fr = "coef du coef a(T) d'une Weibull g�n�rale",
                  ),
 
      # A3
      A3 = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "0.04057",
                  fr = "coef du coef a(T) d'une Weibull g�n�rale",
                  ),
 
      # B1
      B1 = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "17.153",
                  fr = "coef du coef b(T) d'une Weibull g�n�rale",
                  ),
 
      # B2
      B2 = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "55.089",
                  fr = "coef du coef b(T) d'une Weibull g�n�rale",
                  ),
 
      # B3
      B3 = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "0.0144",
                  fr = "coef du coef b(T) d'une Weibull g�n�rale",
                  ),
 
      # C1
      C1 = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "4.",
                  fr = "coef du coef c(T) d'une Weibull g�n�rale",
                  ),
 
      # C2
      C2 = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "0.",
                  fr = "coef du coef c(T) d'une Weibull g�n�rale",
                  ),
 
      # C3
      C3 = SIMP ( statut = "o",
                  typ = "R",
                  defaut = "0.",
                  fr = "coef du coef c(T) d'une Weibull g�n�rale",
                  ),

    ), # FIN FACT Coefficients

    # nbectKIc
    NbEcartType_MoyKIc = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIc (nb sigma) : det = -2 ",
                                ),

    # fractKIc
    Fractile_KIc = SIMP ( statut = "o",
                          typ = "R",
                          defaut = "5.",
                          fr = "Valeur caracteristique de KIc exprim�e en ordre de fractile (%) ",
                          ),

    # nbectKIa
    NbEcartType_MoyKIa = SIMP ( statut = "o",
                                typ = "R",
                                defaut = "-2.",
                                fr = "Nombre d'�cart-type par rapport � la moyenne de KIa (nb sigma) ",
                                ),

  ), # Fin BLOC Parametres_WEIB_GEN

) # Fin PROC MODELES


#==================
# 5. Initialisation
#==================

INITIALISATION = PROC ( nom = "INITIALISATION",
                        op = 68,
	                repetable = 'n',
                        fr = "Initialisation : instant initial, profils radiaux de temp�rature et contraintes", 

  TemperatureInitiale = FACT ( statut = "o",

    ProfilRadial_TemperatureInitiale = SIMP ( statut = "o",
                                              typ = Tuple(2),
                                              max = "**",
                                              fr = "Profil radial de la temp�rature initiale dans la cuve (m) (�C) ",
                                              ),

    Amont_TemperatureInitiale = SIMP ( statut = "o",
                                       typ = "TXM",
                                       into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                       fr = "Prolongation � la fronti�re amont",
                                       ),
            
    Aval_TemperatureInitiale = SIMP ( statut = "o",
                                      typ = "TXM",
                                      into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                      fr = "Prolongation � la fronti�re aval",
                                      ),

  ), # Fin FACT TemperatureInitiale

  ContraintesInitiales = FACT ( statut = "o",

    ProfilRadial_ContraintesInitiales = SIMP ( statut = "o",
                                               typ = Tuple(4),
                                               max = "**",
                                               fr = "Profil radial des contraintes radiale, circonf�rentielle et longitudinale dans la cuve (m) (xx) (xx) (xx) ",
                                               ),

    Amont_ContraintesInitiales = SIMP ( statut = "o",
                                        typ = "TXM",
                                        into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                        fr = "Prolongation � la fronti�re amont",
                                        ),
            
    Aval_ContraintesInitiales = SIMP ( statut = "o",
                                       typ = "TXM",
                                       into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                       fr = "Prolongation � la fronti�re aval",
                                       ),

  ), # Fin FACT ContraintesInitiales

  # INSTINIT
  InstantInitialisation = SIMP ( statut = "o",
                                 typ = "R",
                                 defaut = "-1.",
                                 fr = "Instant initial auquel sont d�finies la temp�rature, ainsi que les contraintes initiales (en s) ",
                                 ),

) # Fin PROC INITIALISATION


#==================================
# 6. CARACTERISTIQUES DU REVETEMENT
#==================================

REVETEMENT = PROC ( nom = "REVETEMENT",
                    op = 68,
	            repetable = 'n',
                    fr = "Caracteristiques du rev�tement", 

  # KTHREV
  ConditionLimiteThermiqueREV = SIMP ( statut = "o",
                                       typ = "TXM",
                                       into = ( "ENTHALPIE", "CHALEUR",),
                                       #defaut = "CHALEUR",
                                       fr = "Option pour d�finir les caract�ristiques du rev�tement ",
                                       ),

  EnthalpieREV = BLOC ( condition = " ConditionLimiteThermiqueREV in ( 'ENTHALPIE', ) ",

    EnthalpieREV_Fct_Temperature = SIMP ( statut = "o",
                                          typ = Tuple(2),
                                          max = "**",
                                          fr = "Temp�rature (�C) / enthalpie massique  (J/kg) ",
                                          ),

    Amont_EnthalpieREV = SIMP ( statut = "o",
                                typ = "TXM",
                                into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                fr = "Prolongation � la fronti�re amont",
                                ),
            
    Aval_EnthalpieREV = SIMP ( statut = "o",
                               typ = "TXM",
                               into = ( 'Continu', 'Exclu', 'Lineaire' ),
                               fr = "Prolongation � la fronti�re aval",
                               ),

  ), # Fin BLOC EnthalpieREV


  ChaleurREV = BLOC ( condition = " ConditionLimiteThermiqueREV in ( 'CHALEUR', ) ",

    ChaleurREV_Fct_Temperature = SIMP ( statut = "o",
                                        typ = Tuple(2),
                                        max = "**",
                                        fr = "Temp�rature (�C) / chaleur volumique (J/kg/K) ",
                                        ),

    Amont_ChaleurREV = SIMP ( statut = "o",
                              typ = "TXM",
                              into = ( 'Continu', 'Exclu', 'Lineaire' ),
                              fr = "Prolongation � la fronti�re amont",
                              ),
            
    Aval_ChaleurREV = SIMP ( statut = "o",
                             typ = "TXM",
                             into = ( 'Continu', 'Exclu', 'Lineaire' ),
                             fr = "Prolongation � la fronti�re aval",
                             ),

  ), # Fin BLOC ChaleurREV

  ConductiviteREV = FACT (statut = "o",

    ConductiviteREV_Fct_Temperature = SIMP ( statut = "o",
                                             typ = Tuple(2),
                                             max = "**",
                                             fr = "Temp�rature (�C) / conductivit� thermique (W/m/�C) ",
                                             ),

    Amont_ConductiviteREV = SIMP ( statut = "o",
                                   typ = "TXM",
                                   into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                   fr = "Prolongation � la fronti�re amont",
                                   ),
            
    Aval_ConductiviteREV = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                  fr = "Prolongation � la fronti�re aval",
                                  ),

  ), # Fin FACT ConductiviteREV

  ModuleYoungREV = FACT (statut = "o",

    ModuleYoungREV_Fct_Temperature = SIMP ( statut = "o",
                                            typ = Tuple(2),
                                            max = "**",
                                            fr = "Temp�rature (�C) / module d'Young (MPa) ",
                                            ),

    Amont_ModuleYoungREV = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                  fr = "Prolongation � la fronti�re amont",
                                  ),
            
    Aval_ModuleYoungREV = SIMP ( statut = "o",
                                 typ = "TXM",
                                 into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                 fr = "Prolongation � la fronti�re aval",
                                 ),

  ), # Fin FACT ModuleYoungREV

  CoeffDilatThermREV = FACT (statut = "o",

    CoeffDilatThermREV_Fct_Temperature = SIMP ( statut = "o",
                                                typ = Tuple(2),
                                                max = "**",
                                                fr = "Temp�rature (�C) / coefficient de dilatation thermique (�C-1) ",
                                               ),

    Amont_CoeffDilatThermREV = SIMP ( statut = "o",
                                      typ = "TXM",
                                      into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                      fr = "Prolongation � la fronti�re amont",
                                      ),
            
    Aval_CoeffDilatThermREV = SIMP ( statut = "o",
                                     typ = "TXM",
                                     into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                     fr = "Prolongation � la fronti�re aval",
                                     ),

  ), # Fin FACT CoeffDilatThermREV

  LimiteElasticiteREV = FACT (statut = "o",

    LimiteElasticiteREV_Fct_Temperature = SIMP ( statut = "o",
                                                 typ = Tuple(2),
                                                 max = "**",
                                                 fr = "Temp�rature (�C) / limite d'�lasticite (MPa) ",
                                                 ),

    Amont_LimiteElasticiteREV = SIMP ( statut = "o",
                                       typ = "TXM",
                                       into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                       fr = "Prolongation � la fronti�re amont",
                                       ),
            
    Aval_LimiteElasticiteREV = SIMP ( statut = "o",
                                      typ = "TXM",
                                      into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                      fr = "Prolongation � la fronti�re aval",
                                      ),

  ), # Fin FACT LimiteElasticiteREV

  AutresParametresREV = FACT (statut = "o",

    # TREFREV
    TemperatureDeformationNulleREV = SIMP ( statut = "o",
                                            typ = "R",
                                            defaut = "20.",
                                            fr = "Temp�rature de r�f�rence pour laquelle les d�formations thermiques sont nulles (�C) ",
                                            ),

    # TDETREV
    TemperaturePourCoefDilatThermREV = SIMP ( statut = "o",
                                              typ = "R",
                                              defaut = "287.",
                                              fr = "Temp�rature de d�finition du coefficient de dilatation thermique (�C) ",
                                              ),

    # NUREV
    CoefficientPoissonREV = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "0.3",
                                   fr = "Coefficient de Poisson ",
                                   ),

  ), # Fin FACT AutresParametresREV

) # Fin PROC REVETEMENT


#=====================================
# 7. CARACTERISTIQUES DU METAL DE BASE
#=====================================

METAL_BASE = PROC ( nom = "METAL_BASE",
                    op = 68,
	            repetable = 'n',
                    fr = "Caracteristiques du metal de base", 

  # KTHMDB
  ConditionLimiteThermiqueMDB = SIMP ( statut = "o",
                                       typ = "TXM",
                                       into = ( "ENTHALPIE", "CHALEUR",),
                                       #defaut = "CHALEUR",
                                       fr = "Option pour definir les caract�ristiques du rev�tement ",
                                       ),

  EnthalpieMDB = BLOC ( condition = " ConditionLimiteThermiqueMDB in ( 'ENTHALPIE', ) ",

    EnthalpieMDB_Fct_Temperature = SIMP ( statut = "o",
                                          typ = Tuple(2),
                                          max = "**",
                                          fr = "Temp�rature (�C) / enthalpie massique (J/kg) ",
                                          ),

    Amont_EnthalpieMDB = SIMP ( statut = "o",
                                typ = "TXM",
                                into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                fr = "Prolongation � la fronti�re amont",
                                ),
            
    Aval_EnthalpieMDB = SIMP ( statut = "o",
                               typ = "TXM",
                               into = ( 'Continu', 'Exclu', 'Lineaire' ),
                               fr = "Prolongation � la fronti�re aval",
                               ),

  ), # Fin BLOC EnthalpieMDB

  ChaleurMDB = BLOC ( condition = " ConditionLimiteThermiqueMDB in ( 'CHALEUR', ) ",

    ChaleurMDB_Fct_Temperature = SIMP ( statut = "o",
                                        typ = Tuple(2),
                                        max = "**",
                                        fr = "Temp�rature (�C) / chaleur volumique (J/kg/K) ",
                                        ),

    Amont_ChaleurMDB = SIMP ( statut = "o",
                              typ = "TXM",
                              into = ( 'Continu', 'Exclu', 'Lineaire' ),
                              fr = "Prolongation � la fronti�re amont",
                              ),
            
    Aval_ChaleurMDB = SIMP ( statut = "o",
                             typ = "TXM",
                             into = ( 'Continu', 'Exclu', 'Lineaire' ),
                             fr = "Prolongation � la fronti�re aval",
                             ),

  ), # Fin BLOC ChaleurMDB

  ConductiviteMDB = FACT ( statut = "o",

    ConductiviteMDB_Fct_Temperature = SIMP ( statut = "o",
                                             typ = Tuple(2),
                                             max = "**",
                                             fr = "Temp�rature (�C) / conductivit� thermique (W/m/�C) ",
                                             ),

    Amont_ConductiviteMDB = SIMP ( statut = "o",
                                   typ = "TXM",
                                   into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                   fr = "Prolongation � la fronti�re amont",
                                   ),
            
    Aval_ConductiviteMDB = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                  fr = "Prolongation � la fronti�re aval",
                                  ),

  ), # Fin FACT ConductiviteMDB

  ModuleYoungMDB = FACT ( statut = "o",

    ModuleYoungMDB_Fct_Temperature = SIMP ( statut = "o",
                                            typ = Tuple(2),
                                            max = "**",
                                            fr = "Temp�rature (�C) / module d'Young (MPa) ",
                                            ),

    Amont_ModuleYoungMDB = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                  fr = "Prolongation � la fronti�re amont",
                                  ),
            
    Aval_ModuleYoungMDB = SIMP ( statut = "o",
                                 typ = "TXM",
                                 into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                 fr = "Prolongation � la fronti�re aval",
                                 ),

  ), # Fin FACT ModuleYoungMDB

  CoeffDilatThermMDB = FACT ( statut = "o",

    CoeffDilatThermMDB_Fct_Temperature = SIMP ( statut = "o",
                                                typ = Tuple(2),
                                                max = "**",
                                                fr = "Temp�rature (�C) / coefficient de dilatation thermique (�C-1) ",
                                                ),

    Amont_CoeffDilatThermMDB = SIMP ( statut = "o",
                                      typ = "TXM",
                                      into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                      fr = "Prolongation � la fronti�re amont",
                                      ),
            
    Aval_CoeffDilatThermMDB = SIMP ( statut = "o",
                                     typ = "TXM",
                                     into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                     fr = "Prolongation � la fronti�re aval",
                                     ),

  ), # Fin FACT CoeffDilatThermMDB

  AutresParametresMDB = FACT ( statut = "o",

    # TREFMDB
    TemperatureDeformationNulleMDB = SIMP ( statut = "o",
                                            typ = "R",
                                            defaut = "20.",
                                            fr = "Temp�rature de r�f�rence pour laquelle les d�formations thermiques sont nulles (�C) ",
                                            ),

    # TDETMDB
    TemperaturePourCoefDilatThermMDB = SIMP ( statut = "o",
                                              typ = "R",
                                              defaut = "287.",
                                              fr = "Temp�rature de d�finition du coefficient de dilatation thermique (�C) ",
                                              ),

    # NUMDB
    CoefficientPoissonMDB = SIMP ( statut = "o",
                                   typ = "R",
                                   defaut = "0.3",
                                   fr = "Coefficient de Poisson ",
                                   ),

  ), # Fin FACT TemperatureDeformationNulleMDB

) # Fin PROC METAL_BASE


#===============================
# 8. TRANSITOIRE THERMOMECANIQUE
#===============================

TRANSITOIRE = PROC ( nom = "TRANSITOIRE",
                     op = 68,
	             repetable = 'n',
                     fr = "Description du transitoire thermohydraulique", 

  Pression = FACT ( statut = "o",

    ProfilTemporel_Pression = SIMP ( statut = "o",
                                   typ = Tuple(2),
                                   max = "**",
                                   fr = "Instant (s) / pression (MPa) ",
                                   ),

    Amont_Pression = SIMP ( statut = "o",
                          typ = "TXM",
                          into = ( 'Continu', 'Exclu', 'Lineaire' ),
                          fr = "Prolongation � la fronti�re amont",
                          ),
            
    Aval_Pression = SIMP ( statut = "o",
                         typ = "TXM",
                         into = ( 'Continu', 'Exclu', 'Lineaire' ),
                         fr = "Prolongation � la fronti�re aval",
                         ),

  ), # FIN FACT Pression

  # TYPCLTH
  TypeConditionLimiteThermique = SIMP ( statut = "o",
                                        typ = "TXM",
                                        into = ( "Temperature imposee en paroi", # TEMP_IMPO 
					         "Flux de chaleur impose en paroi", # FLUX_REP 
						 "Temperature imposee du fluide et coefficient echange", # ECHANGE 
						 "Debit massique et temperature d injection de securite", # DEBIT 
						 "Temperature imposee du fluide et debit d injection de securite"), # TEMP_FLU
                                        #defaut = "ECHANGE",
                                        fr = "Type de condition thermique en paroi interne ",
                                        ),

  TemperatureImposeeParoi = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Temperature imposee en paroi', ) ",

    ProfilTemporel_TemperatureImposeeParoi = SIMP ( statut = "o",
                                               typ = Tuple(2),
                                               max = "**",
                                               fr = "Instant (s) / Temp�rature impos�e (�C) ",
                                               ),

    Amont_TemperatureImposeeParoi = SIMP ( statut = "o",
                                      typ = "TXM",
                                      into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                      fr = "Prolongation � la fronti�re amont",
                                      ),
            
    Aval_TemperatureImposeeParoi = SIMP ( statut = "o",
                                     typ = "TXM",
                                     into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                     fr = "Prolongation � la fronti�re aval",
                                     ),

  ), # Fin BLOC TemperatureImposeeParoi

  FluxChaleur = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Flux de chaleur impose en paroi', ) ",

    ProfilTemporel_FluxChaleur = SIMP ( statut = "o",
                                        typ = Tuple(2),
                                        max = "**",
                                        fr = "Instant (s) / Flux de chaleur impose (W/m2) ",
                                        ),

    Amont_FluxChaleur = SIMP ( statut = "o",
                               typ = "TXM",
                               into = ( 'Continu', 'Exclu', 'Lineaire' ),
                               fr = "Prolongation � la fronti�re amont",
                               ),
            
    Aval_FluxChaleur = SIMP ( statut = "o",
                              typ = "TXM",
                              into = ( 'Continu', 'Exclu', 'Lineaire' ),
                              fr = "Prolongation � la fronti�re aval",
                              ),

  ), # Fin BLOC FluxChaleur

  TemperatureImposeeFluide = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Temperature imposee du fluide et coefficient echange', 'Temperature imposee du fluide et debit d injection de securite', ) ",

    ProfilTemporel_TemperatureImposeeFluide = SIMP ( statut = "o",
                                               typ = Tuple(2),
                                               max = "**",
                                               fr = "Instant (s) / Temp�rature impos�e (�C) ",
                                               ),

    Amont_TemperatureImposeeFluide = SIMP ( statut = "o",
                                      typ = "TXM",
                                      into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                      fr = "Prolongation � la fronti�re amont",
                                      ),
            
    Aval_TemperatureImposeeFluide = SIMP ( statut = "o",
                                     typ = "TXM",
                                     into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                     fr = "Prolongation � la fronti�re aval",
                                     ),

  ), # Fin BLOC TemperatureImposeeFluide

  CoefficientEchange = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Temperature imposee du fluide et coefficient echange', ) ",

    ProfilTemporel_CoefficientEchange = SIMP ( statut = "o",
                                               typ = Tuple(2),
                                               max = "**",
                                               fr = "Instant (s) / Coefficient d'�change (W/m2/K) ",
                                               ),

    Amont_CoefficientEchange = SIMP ( statut = "o",
                                      typ = "TXM",
                                      into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                      fr = "Prolongation � la fronti�re amont",
                                      ),
            
    Aval_CoefficientEchange = SIMP ( statut = "o",
                                     typ = "TXM",
                                     into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                     fr = "Prolongation � la fronti�re aval",
                                     ),

  ), # Fin BLOC CoefficientEchange

  DebitMassique = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Debit massique et temperature d injection de securite', ) ",

    ProfilTemporel_DebitMassique = SIMP ( statut = "o",
                                          typ = Tuple(2),
                                          max = "**",
                                          fr = "Instant (s) / D�bit massique (kg/s) ",
                                          ),

    Amont_DebitMassique = SIMP ( statut = "o",
                                 typ = "TXM",
                                 into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                 fr = "Prolongation � la fronti�re amont",
                                 ),
            
    Aval_DebitMassique = SIMP ( statut = "o",
                                typ = "TXM",
                                into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                fr = "Prolongation � la fronti�re aval",
                                ),

  ), # Fin BLOC DebitMassique

  TemperatureInjection = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Debit massique et temperature d injection de securite', ) ",

    ProfilTemporel_TemperatureInjection = SIMP ( statut = "o",
                                                 typ = Tuple(2),
                                                 max = "**",
                                                 fr = "Instant (s) / Temp�rature d'injection de s�curit�  (�C) ",
                                                 ),

    Amont_TemperatureInjection = SIMP ( statut = "o",
                                        typ = "TXM",
                                        into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                        fr = "Prolongation � la fronti�re amont",
                                        ),
            
    Aval_TemperatureInjection = SIMP ( statut = "o",
                                       typ = "TXM",
                                       into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                       fr = "Prolongation � la fronti�re aval",
                                       ),
  ), # Fin BLOC TemperatureInjection

  Creare = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Debit massique et temperature d injection de securite', ) ",

    # DH
    DiametreHydraulique = SIMP ( statut = "o",
                                 typ = "R",
                                 defaut = "-2.",
                                 fr = "Diam�tre hydraulique (m) ",
                                 ),

    # SECTION
    SectionEspaceAnnulaire = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Section espace annulaire (m2) ",
                                    ),

    # DELTA
    HauteurCaracConvectionNaturelle = SIMP ( statut = "o",
                                             typ = "R",
                                             defaut = "-2.",
                                             fr = "Hauteur caract�ristique convection naturelle (m) ",
                                             ),

    # ALPHA_CF
    CoeffVestale_ConvectionForcee = SIMP ( statut = "o",
                                           typ = "R",
                                           defaut = "1.",
                                           fr = "Coefficient Vestale convection forc�e (-) ",
                                           ),

    # ALPHA_CN
    CoeffVestale_ConvectionNaturelle = SIMP ( statut = "o",
                                              typ = "R",
                                              defaut = "1.",
                                              fr = "Coefficient Vestale convection naturelle (-) ",
                                              ),

    # EPS
    CritereConvergenceRelative = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "0.00001",
                                        fr = "Crit�re convergence relative (-) ",
                                        ),

    # VM
    VolumeMelange_CREARE = SIMP ( statut = "o",
                                  typ = "R",
                                  defaut = "-2.",
                                  fr = "Volume de m�lange CREARE (m3) ",
                                  ),

    # T0
    TemperatureInitiale_CREARE = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "-2.",
                                        fr = "Temp�rature initiale CREARE (�C) ",
                                        ),

    # SE
    SurfaceEchange_FluideStructure = SIMP ( statut = "o",
                                            typ = "R",
                                            defaut = "-2.",
                                            fr = "Surface d'�change fluide/structure (m2) ",
                                            ),

  ), # Fin BLOC Creare


  DebitInjection = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Temperature imposee du fluide et debit d injection de securite', ) ",

    ProfilTemporel_DebitInjection = SIMP ( statut = "o",
                                           typ = Tuple(2),
                                           max = "**",
                                           fr = "Instant (s) / D�bit d'injection de s�curit� (kg/s) ",
                                           ),

    Amont_DebitInjection = SIMP ( statut = "o",
                                  typ = "TXM",
                                  into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                  fr = "Prolongation � la fronti�re amont",
                                  ),
            
    Aval_DebitInjection = SIMP ( statut = "o",
                                 typ = "TXM",
                                 into = ( 'Continu', 'Exclu', 'Lineaire' ),
                                 fr = "Prolongation � la fronti�re aval",
                                 ),

  ), # Fin BLOC DebitInjection


  Vestale = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Temperature imposee du fluide et debit d injection de securite', ) ",

    # DH
    DiametreHydraulique = SIMP ( statut = "o",
                                 typ = "R",
                                 defaut = "-2.",
                                 fr = "Diam�tre hydraulique (m) ",
                                 ),

    # SECTION
    SectionEspaceAnnulaire = SIMP ( statut = "o",
                                    typ = "R",
                                    defaut = "-2.",
                                    fr = "Section espace annulaire (m2) ",
                                    ),

    # DELTA
    HauteurCaracConvectionNaturelle = SIMP ( statut = "o",
                                             typ = "R",
                                             defaut = "-2.",
                                             fr = "Hauteur caract�ristique convection naturelle (m) ",
                                             ),

    # ALPHA_CF
    CoeffVestale_ConvectionForcee = SIMP ( statut = "o",
                                           typ = "R",
                                           defaut = "1.",
                                           fr = "Coefficient d'�change Vestale convection forc�e (-) ",
                                           ),

    # ALPHA_CN
    CoeffVestale_ConvectionNaturelle = SIMP ( statut = "o",
                                              typ = "R",
                                              defaut = "1.",
                                              fr = "Coefficient d'�change Vestale convection naturelle (-) ",
                                              ),

    # EPS
    CritereConvergenceRelative = SIMP ( statut = "o",
                                        typ = "R",
                                        defaut = "0.00001",
                                        fr = "Crit�re convergence relative (-) ",
                                        ),

  ), # Fin BLOC Vestale

) # Fin PROC TRANSITOIRE
