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
                 regles = ( AU_MOINS_UN ('OPTIONS'),
		            AU_MOINS_UN ('INITIALISATION'),
		            AU_MOINS_UN ('REVETEMENT'),
		            AU_MOINS_UN ('METAL_BASE'),
		            AU_MOINS_UN ('TRANSITOIRE'),
                          )
                 ) # Fin JDC_CATA

# --------------------------------------------------
# fin entete
# --------------------------------------------------

# --------------------------------------------------
# RESPONSABLE D. THAI VAN
# Ce fichier contient la liste des coefficients pour un
# modele de Weibull generalise
def Coef_WeibGen() : return FACT(statut='o',min=1,max='**',

  # A1
  A1 = SIMP ( statut="o", typ="R", defaut=21.263, 
              fr="coef du coef a(T) d'une Weibull générale", ),
  # A2
  A2 = SIMP ( statut="o", typ="R", defaut=9.159, 
              fr="coef du coef a(T) d'une Weibull générale", ),
  # A3
  A3 = SIMP ( statut="o", typ="R", defaut=0.04057, 
              fr="coef du coef a(T) d'une Weibull générale", ),
  # B1
  B1 = SIMP ( statut="o", typ="R", defaut=17.153, 
              fr="coef du coef b(T) d'une Weibull générale", ),
  # B2
  B2 = SIMP ( statut="o", typ="R", defaut=55.089, 
              fr="coef du coef b(T) d'une Weibull générale", ),
  # B3
  B3 = SIMP ( statut="o", typ="R", defaut=0.0144, 
              fr="coef du coef b(T) d'une Weibull générale", ),
  # C1
  C1 = SIMP ( statut="o", typ="R", defaut=4., 
              fr="coef du coef c(T) d'une Weibull générale", ),
  # C2
  C2 = SIMP ( statut="o", typ="R", defaut=0., 
              fr="coef du coef c(T) d'une Weibull générale", ),
  # C3
  C3 = SIMP ( statut="o", typ="R", defaut=0., 
              fr="coef du coef c(T) d'une Weibull générale", ),

); # FIN def Coef_WeibGen


# --------------------------------------------------
# RESPONSABLE D. THAI VAN
# Ce fichier contient la liste des coefficients 
def Coef_Fluence() : return FACT(statut='o',min=1,max='**',

  # COEFFLUENCE1
  Azimut_0deg  = SIMP ( statut="o", typ="R", defaut=5.8, 
                        fr="Fluence à l'azimut 0 (10^19 n/cm2)", ),
  # COEFFLUENCE2
  Azimut_5deg  = SIMP ( statut="o", typ="R", defaut=5.48, 
                        fr="Fluence à l'azimut 5 (10^19 n/cm2)", ),
  # COEFFLUENCE3
  Azimut_10deg = SIMP ( statut="o", typ="R", defaut=4.46, 
                        fr="Fluence à l'azimut 10 (10^19 n/cm2)", ),
  # COEFFLUENCE4
  Azimut_15deg = SIMP ( statut="o", typ="R", defaut=3.41, 
                        fr="Fluence à l'azimut 15 (10^19 n/cm2)", ),
  # COEFFLUENCE5
  Azimut_20deg = SIMP ( statut="o", typ="R", defaut=3.37, 
                        fr="Fluence à l'azimut 20 (10^19 n/cm2)", ),
  # COEFFLUENCE6
  Azimut_25deg = SIMP ( statut="o", typ="R", defaut=3.16, 
                        fr="Fluence à l'azimut 25 (10^19 n/cm2)", ),
  # COEFFLUENCE7
  Azimut_30deg = SIMP ( statut="o", typ="R", defaut=2.74, 
                        fr="Fluence à l'azimut 30 (10^19 n/cm2)", ),
  # COEFFLUENCE8
  Azimut_35deg = SIMP ( statut="o", typ="R", defaut=2.25, 
                        fr="Fluence à l'azimut 35 (10^19 n/cm2)", ),
  # COEFFLUENCE9
  Azimut_40deg = SIMP ( statut="o", typ="R", defaut=1.89, 
                        fr="Fluence à l'azimut 40 (10^19 n/cm2)", ),
  # COEFFLUENCE10
  Azimut_45deg = SIMP ( statut="o", typ="R", defaut=1.78, 
                        fr="Fluence à l'azimut 45 (10^19 n/cm2)", ),

); # FIN def Coef_Fluence

#================================
# 1. Definition des OPTIONS
#================================

OPTIONS = PROC ( nom = "OPTIONS",
                 op = 68,
		 repetable = 'n',
                 fr = "Définitions des options", 

#===
# Liste des paramètres
#===

  SortieEcran = FACT (statut="o",

    # MESSAGE_LEVEL
    NiveauImpression	= SIMP (statut="o", typ="TXM", defaut="Temps total",
                                fr="Niveau d impression a l ecran",
                                into=( "Aucune impression", # 0
                                       "Temps total", # 1
				       "Temps intermediaires",), # 2
				),

  ), # FIN FACT SortieEcran

  SortieFichier = FACT (statut="o",

    # DATARESUME_FILE
    FichierDataIn	= SIMP (statut="o", typ="TXM", defaut="NON",
                                fr="Fichier recapitulatif des donnees d entree : template.IN",
                                into=( "OUI", "NON",),
                                ),
    # TEMPSIG_FILE
    FichierTempSigma	= SIMP (statut="o", typ="TXM", defaut="NON",
                                fr="Fichiers de temperature et de contraintes : template.TEMP et template.SIG",
                                into=( "OUI", "NON",),
                                ),
    # RESU_FILE
    FichierResultats	= SIMP (statut="o", typ="TXM", defaut="NON",
                                fr="Fichier resultat : template_DEFAILLCUVE",
                                into=( "OUI", "NON",),
                                ),
    # CSV_FILE
    FichierCSV		= SIMP (statut="o", typ="TXM", defaut="NON",
                                fr="Fichier resultat au format CSV : template_DEFAILLCUVE.CSV",
                                into=( "OUI", "NON",),
                                ),
    # CREARE_FILE
    FichierCREARE	= SIMP (statut="o", typ="TXM", defaut="NON",
                                fr="Fichier Tfluide et coefficients d echange : template.CREA",
                                into=( "OUI", "NON",),
                                ),

  ), # FIN FACT SortieFichier

  # GRANDEUR
  GrandeurEvaluee	= SIMP (statut="o", typ="TXM", defaut="Facteur de marge KIc/KCP",
                                fr="Grandeur sous critere",
                                into=( "Facteur de marge KIc/KCP", # FM_KICSURKCP
                                       "Marge KIc-KI", # MARGE_KI
                                       "Marge KIc-KCP", ), # MARGE_KCP
                                ),

  AutresParametres = FACT (statut="o",

    # INCRTPS
    IncrementTemporel          = SIMP ( statut="o", typ="I", defaut=1, 
                                      fr="Incrément temporel (=1 pour calcul déterministe)", ),
    # DTPREC
    IncrementMaxTemperature    = SIMP ( statut="o", typ="R", val_min=0.1, val_max=1., defaut=0.1, 
				      fr="Incrément maximum d'évolution de la température par noeud et par instant (°C)", ),
    # DTARCH
    IncrementMaxTempsAffichage = SIMP ( statut="o", typ="R", val_min=0., val_max=1000., defaut=1000., 
				      fr="Incrément maximum de temps pour l'affichage (s)", ),
    # 
    ListeInstants              = SIMP ( statut="o", typ="R", max="**",
                                      fr = "Liste des instants pour lesquels la température et les contraintes seront archivés", ),

  ), # FIN FACT AutresParametres

) # Fin PROC OPTIONS

#================================
# 2. Caracteristiques de la CUVE
#================================

CUVE = PROC (nom = "CUVE",
             op = 68,
	     repetable = 'n',
             fr = "Caractéristiques de la cuve", 

#===
# Liste des paramètres
#===

  # TYPEGEOM
  TraitementGeometrie = SIMP ( statut="o", typ="TXM", defaut="Topologie",
                               fr="Choix de la définition de la geométrie d'une cuve",
	                       into=( "Topologie", # GEOMETRIE 
		                        "Maillage"), # MAILLAGE
                               ),

#====
# Definition des parametres selon le type de traitement de la geometrie
#====

  Geometrie = BLOC ( condition = "TraitementGeometrie=='Topologie'",

    # RINT
    RayonInterne        = SIMP ( statut="o", typ="R", val_min=0.,  defaut=1.994, 
                                 fr="Rayon interne de la cuve (en m)", ),
    # RINT_MESSAGE
    RayonInterne_mess   = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                 fr="Affichage ecran du rayon interne de la cuve (en m)",
				 into=( "NON", "OUI" ), ),

    # DTV : comment preciser que REXT > RINT ?
    # REXT
    RayonExterne        = SIMP ( statut="o", typ="R", defaut=2.2015, 
                                 fr="Rayon externe de la cuve (en m)", ),
    # REXT_MESSAGE
    RayonExterne_mess   = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                 fr="Affichage ecran du rayon externe de la cuve (en m)",
				 into=( "NON", "OUI" ), ),

    # DTV : comment preciser que LREV < RINT ?
    # LREV
    EpaisseurRevetement = SIMP ( statut="o", typ="R", defaut=0.0075, 
                                 fr="Epaisseur du revêtement (m)", ),
    # LREV_MESSAGE
    EpaisseurRevetement_mess = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de l'epaisseur du revêtement (m)",
				      into=( "NON", "OUI" ), ),

    # LIGMIN
    LigamentExterneMin  = SIMP ( statut="o", typ="R", defaut=0.75, 
                                 fr="Ligament externe minimal avant rupture (% de l'épaisseur de cuve)", ),
    # LIGMIN_MESSAGE
    LigamentExterneMin_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran du ligament externe minimal avant rupture (% de l'épaisseur de cuve)",
				      into=( "NON", "OUI" ), ),

    # NBNO
    NombreNoeudsMaillage = SIMP ( statut="o", typ="I", defaut=300, max=1, val_min=1, val_max=1000, 
			          fr = "Nombre de noeuds à considérer dans le maillage interne", ),
  
  ), # Fin BLOC  Geometrie

  Maillage  = BLOC ( condition = "TraitementGeometrie=='Maillage'",

    # DTV : comment preciser que c'est une suite de liste de nombres croissants ?
    # Question : NBO depend-il de TYPGEOM ??
    NombreNoeudsMaillage = SIMP ( statut="o", typ="I", defaut=300, max=1, val_min=1, val_max=1000, 
			          fr = "Nombre de noeuds à considérer dans le maillage interne", ),
  
    ListeAbscisses       = SIMP ( statut="o", typ="R", max="**",
                                  fr = "Liste des abscisses", ),
  ), # Fin BLOC Maillage

) # Fin PROC CUVE

#================================
# 3. Caracteristiques du DEFAUT
#================================

DEFAUT = PROC ( nom = "DEFAUT",
                op = 68,
		repetable = 'n',
                fr = "Caractéristiques du défaut", 

#===
# Liste des paramètres
#===

# TYPEDEF
  TypeInitial = SIMP ( statut="o", typ="TXM", defaut="Defaut Sous Revetement",
                       fr="Type initial du défaut : sous revêtement, decale ou débouchant",
                       into=( "Defaut Sous Revetement", # DSR
		              "Defaut Decale", # DECALE
                              "Defaut Debouchant", ), # DEBOUCHANT
                       ),

#====
# Definition des parametres selon le type du defaut
#====

  SousRevetement = BLOC ( condition = "TypeInitial=='Defaut Sous Revetement'",

    # ORIEDEF into LONGITUD, CIRCONF
    Orientation              = SIMP ( statut="o", typ="TXM", defaut="Longitudinale",
			              fr="Orientation du défaut",
                                      into=( "Longitudinale", 
			                     "Circonferentielle" ), ),

    Profondeur_parametres = FACT (statut="o",
      # PROFDEF
      # dtv : taille max d'un defaut ? Ici, 0.2 = epaisseur approximative de cuve
      ProfondeurRadiale        = SIMP ( statut="o", typ="R", max=1, val_min=0., val_max=0.2, defaut=0.006, 
                                      fr="Profondeur radiale du défaut (m)", ),
      # PROFDEF_MESSAGE
      ProfondeurRadiale_mess   = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la profondeur radiale du défaut (m)",
				      into=( "NON", "OUI" ), ),
    ), # Fin FACT Profondeur_parametres

    Longueur_parametres = FACT (statut="o",
      # OPTLONG into VALEUR, FCTAFFINE
      ModeCalculLongueur     = SIMP ( statut="o", typ="TXM", defaut="Valeur",
                                        fr="Option pour caractériser la longueur du défaut : soit par valeur, soit par une fonction affine de la profondeur",
                                        into = ( "Valeur", "Fonction affine de la profondeur" ), ),
      Mode_Valeur            = BLOC ( condition = "ModeCalculLongueur=='Valeur'",
        # LONGDEF
        Longueur                 = SIMP ( statut="o", typ="R", max=1, val_min=0., val_max=1., defaut = 0.060, 
                                          fr = "Longueur du défaut sous revêtement (m)", ),
        # LONGDEF_MESSAGE
        Longueur_mess            = SIMP ( statut="o", typ="TXM", defaut = "NON", 
                                          fr = "Affichage ecran de la longueur du défaut sous revêtement (m)",
    				        into=( "NON", "OUI" ), ),
      ), # Fin BLOC Mode_Valeur
      Mode_Fctaffine           = BLOC ( condition = "ModeCalculLongueur=='Fonction affine de la profondeur'",
        # PROFSURLONG
        CoefDirecteur     = SIMP ( statut="o", typ="R", max=1, val_max=100., defaut=10.,
                         fr="Inverse a1 du coefficient directeur de la fonction affine l=h/a1 + a0", ),
        # LONGCONST
        Constante = SIMP ( statut="o", typ="R", max=1, val_max=100., defaut=0.,
                         fr="constante a0 de la fonction affine l=pente*h + a0", ),
      ), # Fin BLOC Mode_Fctaffine
    ), # FIN FACT Longueur_parametres

    Azimut_parametres = FACT (statut="o",
      # ANGLDEF
      Azimut                   = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Position angulaire du défaut dans le cylindre de cuve (en degrés)", ),
      # ANGLDEF_MESSAGE
      Azimut_mess              = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la position angulaire du défaut dans le cylindre de cuve (en degrés)",
                                      into = ( "NON", "OUI" ), ),
    ), # Fin FACT Azimut_parametres

    Altitude_parametres = FACT (statut="o",
      # ALTIDEF
      # dtv : altitude entre -7m et 0m ? zone Vestale : -6.601<z<-3.510
      Altitude                 = SIMP ( statut="o", typ="R", val_min=-8., val_max=0., defaut=-4., 
                                      fr="Altitude du défaut sur le cylindre de cuve (en m)", ),
      # ALTIDEF_MESSAGE
      Altitude_mess            = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de l altitude du défaut sur le cylindre de cuve (en m)",
                                      into = ( "NON", "OUI" ), ),
    ), # Fin FACT Altitude_parametres

    # POINDEF
    Pointe                   = SIMP ( statut="o", typ="TXM", defaut="A", 
                                      fr="Choix du point considéré du défaut sous revêtement",
                                      into=( "A", "B", "A et B" ), ),

  ), # Fin BLOC SousRevetement

  Decale = BLOC ( condition = "TypeInitial=='Defaut Decale'",

    # ORIEDEF into LONGITUD, CIRCONF
    Orientation              = SIMP ( statut="o", typ="TXM", defaut="Longitudinale",
			              fr="Orientation du défaut",
                                      into=( "Longitudinale", 
			                     "Circonferentielle" ), ),

    Profondeur_parametres = FACT (statut="o",
      # PROFDEF
      # dtv : taille max d'un defaut ? Ici, 0.2 = epaisseur approximative de cuve
      ProfondeurRadiale        = SIMP ( statut="o", typ="R", max=1, val_min=0., val_max=0.2, defaut=0.006, 
                                      fr="Profondeur radiale du défaut (m)", ),
      # PROFDEF_MESSAGE
      ProfondeurRadiale_mess   = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la profondeur radiale du défaut (m)",
				      into=( "NON", "OUI" ), ),
    ), # Fin FACT Profondeur_parametres

    Longueur_parametres = FACT (statut="o",

      # OPTLONG into VALEUR, FCTAFFINE
      ModeCalculLongueur     = SIMP ( statut="o", typ="TXM", defaut="Valeur",
                                      fr="Option pour caractériser la longueur du défaut : soit par valeur, soit par une fonction affine de la profondeur",
                                      into = ( "Valeur", "Fonction affine de la profondeur" ), ),

      Mode_Valeur            = BLOC ( condition = "ModeCalculLongueur=='Valeur'",
        # LONGDEF
        Longueur                 = SIMP ( statut="o", typ="R", max=1, val_min=0., val_max=1., defaut = 0.060, 
                                        fr = "Longueur du défaut sous revêtement (m)", ),
        # LONGDEF_MESSAGE
        Longueur_mess            = SIMP ( statut="o", typ="TXM", defaut = "NON", 
                                        fr = "Affichage ecran de la longueur du défaut décalé (m)",
				        into=( "NON", "OUI" ), ),
      ), # Fin BLOC Mode_Valeur

      Mode_Fctaffine           = BLOC ( condition = "ModeCalculLongueur=='Fonction affine de la profondeur'",
        # PROFSURLONG
        CoefDirecteur     = SIMP ( statut="o", typ="R", max=1, val_max=100., defaut=10.,
                         fr="Inverse a1 du coefficient directeur de la fonction affine l=h/a1 + a0", ),
        # LONGCONST
        Constante = SIMP ( statut="o", typ="R", max=1, val_max=100., defaut=0.,
                         fr="constante a0 de la fonction affine l=pente*h + a0", ),
      ), # Fin BLOC Mode_Fctaffine

    ), # FIN FACT Longueur_parametres

   
    Decalage_parametres = FACT (statut="o",

      # DECATYP into NORMALISE, VALEUR
      ModeCalculDecalage     = SIMP ( statut="o", typ="TXM", defaut="Valeur",
                                      fr="Option de definition du decalage radial du defaut : soit par valeur reelle, soit par valeur normalisee",
                                      into = ( "Valeur", 
			                       "Valeur normalisee" ), ),

      Mode_Decalage_Valeur   = BLOC ( condition = "ModeCalculDecalage=='Valeur'",
        # DECADEF
        DecalageRadial           = SIMP ( statut="o", typ="R", defaut=-0.00001, 
                                      fr="Décalage radial du defaut sous revêtement (en m)", ),
        # DECADEF_MESSAGE
        DecalageRadial_mess      = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran du décalage radial du defaut sous revêtement (en m)",
                                      into = ( "NON", "OUI" ), ),
      ), # Fin BLOC Mode_Decalage_Valeur

      Mode_Decalage_Normalisee = BLOC ( condition = "ModeCalculDecalage=='Valeur normalisee'",
        # DECANOR
        DecalageNormalise          = SIMP ( statut="o", typ="R", defaut=0.01, 
                                       fr="Décalage radial normalise du defaut sous revêtement (entre 0. et 1.)", ),
      ), # Fin BLOC Mode_Decalage_Normalisee
  
    ), # Fin FACT Decalage_parametres

    Azimut_parametres = FACT (statut="o",
      # ANGLDEF
      Azimut                   = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Position angulaire du défaut dans le cylindre de cuve (en degrés)", ),
      # ANGLDEF_MESSAGE
      Azimut_mess              = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la position angulaire du défaut dans le cylindre de cuve (en degrés)",
                                      into = ( "NON", "OUI" ), ),
    ), # Fin FACT Azimut_parametres

    Altitude_parametres = FACT (statut="o",
      # ALTIDEF
      # dtv : altitude entre -7m et 0m ? zone Vestale : -6.601<z<-3.510
      Altitude                 = SIMP ( statut="o", typ="R", val_min=-8., val_max=0., defaut=-4., 
                                      fr="Altitude du défaut sur le cylindre de cuve (en m)", ),
      # ALTIDEF_MESSAGE
      Altitude_mess            = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de l altitude du défaut sur le cylindre de cuve (en m)",
                                      into = ( "NON", "OUI" ), ),
    ), # Fin FACT Altitude_parametres

    # POINDEF
    Pointe                   = SIMP ( statut="o", typ="TXM", defaut="A", 
                                      fr="Choix du point considéré du défaut décalé",
                                      into=( "A", "B", "A et B" ), ),

  ), # Fin BLOC Decale

  Debouchant = BLOC ( condition = "TypeInitial=='Defaut Debouchant'",

    # ORIEDEF into LONGITUD, CIRCONF
    Orientation              = SIMP ( statut="o", typ="TXM", defaut="Longitudinale",
                                      fr="Orientation du défaut : longitudinale ou circonférentielle",
                                      into=( "Longitudinale",
		                             "Circonferentielle" ), ),

    Profondeur_parametres = FACT (statut="o",
      # PROFDEF
      # dtv : taille max d'un defaut ? Ici, 0.2 = epaisseur approximative de cuve
      ProfondeurRadiale        = SIMP ( statut="o", typ="R", max=1, val_min=0., val_max=0.2, defaut=0.006, 
                                      fr="Profondeur radiale du défaut (m)", ),
      # PROFDEF_MESSAGE
      ProfondeurRadiale_mess   = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la profondeur radiale du défaut (m)",
				      into=( "NON", "OUI" ), ),
    ), # Fin FACT Profondeur_parametres

    Azimut_parametres = FACT (statut="o",
      # ANGLDEF
      Azimut                   = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Position angulaire du défaut dans le cylindre de cuve (en degrés)", ),
      # ANGLDEF_MESSAGE
      Azimut_mess              = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la position angulaire du défaut dans le cylindre de cuve (en degrés)",
                                      into = ( "NON", "OUI" ), ),
    ), # Fin FACT Azimut_parametres

    Altitude_parametres = FACT (statut="o",
      # ALTIDEF
      # dtv : altitude entre -7m et 0m ? zone Vestale : -6.601<z<-3.510
      Altitude                 = SIMP ( statut="o", typ="R", val_min=-8., val_max=0., defaut=-4., 
                                      fr="Altitude du défaut sur le cylindre de cuve (en m)", ),
      # ALTIDEF_MESSAGE
      Altitude_mess            = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de l altitude du défaut sur le cylindre de cuve (en m)",
                                      into = ( "NON", "OUI" ), ),
    ), # Fin FACT Altitude_parametres

  ), # Fin BLOC debouchant

) # Fin PROC DEFAUT


#====================================================
# 4. Modeles de fluence, d'irradiation et de tenacite
#====================================================

#=======================
# 4.1 Modeles de fluence
#=======================

MODELES = PROC ( nom = "MODELES",
                 op = 68,
	         repetable = 'n',
                 fr = "Modèles de fluence, d'irradiation et de ténacité", 


#===
# Liste des paramètres
#===

  Fluence = FACT ( statut="o",
  
    # MODELFLUENCE
    ModeleFluence = SIMP ( statut="o", typ="TXM", defaut="Exponentiel sans revetement k=9.7 (Reglementaire)",
                           fr="Modèle d'atténuation de la fluence dans l'épaisseur de la cuve",
		           into=( "Exponentiel sans revetement k=9.7 (Reglementaire)", # Reglementaire
		                  "Exponentiel sans revetement k=9.7 (Reglementaire CUVE1D)", # Cuve1D
		                  "Exponentiel sans revetement k=12.7 (France)", # France 
                                  "Exponentiel sans revetement k=0. (ValeurImposee)", # ValeurImposee 
                                  "Donnees francaises du palier CPY (SDM)", # SDM 
                                  "Donnees francaises du palier CPY ajustees par secteur angulaire (GrandeDev)", # GrandeDev 
                                  "Regulatory Guide 1.99 rev 2 (USNRC)", # USNRC 
                                  "Dossier 900 MWe AP9701 rev 2 (REV_2)", # REV_2 
                                  "Lissage du modele ajuste (SDM_Lissage)", # SDM_Lissage 
                                  "Grand developpement (GD_Cuve)"), # GD_Cuve 
                         ),

#====
# Definition des parametres selon le modele de fluence
#====
    
    # H1COEUR
    ZoneActiveCoeur_AltitudeSup    = SIMP ( statut="o", typ="R", defaut=-3.536, 
                             fr="Cote supérieure de la zone active de coeur", ),
    # H2COEUR
    ZoneActiveCoeur_AltitudeInf    = SIMP ( statut="o", typ="R", defaut=-7.194, 
                             fr="Cote inférieure de la zone active de coeur", ),

    Reglementaire = BLOC ( condition = " ModeleFluence in ( 'Exponentiel sans revetement k=9.7 (Reglementaire)', ) ",
      # DTV : comment proposer une liste de valeurs, tout en proposant de fournir d'autres valeurs ?
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2)", ),
    ), # Fin BLOC Reglementaire

    Cuve1D = BLOC ( condition = " ModeleFluence in ( 'Exponentiel sans revetement k=9.7 (Reglementaire CUVE1D)', ) ",
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95", ),
    ), # Fin BLOC Cuve1D

    France        = BLOC ( condition = " ModeleFluence in ( 'Exponentiel sans revetement k=12.7 (France)', ) ",
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95", ),
      # KPFRANCE
      KPFrance      = SIMP ( statut="o", typ="R", defaut = 12.7,
                             fr="Paramètre exponentiel du modèle France", ),
    ), # Fin BLOC France

    ValeurImposee = BLOC ( condition = " ModeleFluence in ( 'Exponentiel sans revetement k=0. (ValeurImposee)', ) ",
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95", ),
    ), # Fin BLOC ValeurImposee

    SDM           = BLOC ( condition = " ModeleFluence in ( 'Donnees francaises du palier CPY (SDM)', ) ",
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95", ),
    ), # Fin BLOC SDM

    USNRC         = BLOC ( condition = " ModeleFluence in ( 'Regulatory Guide 1.99 rev 2 (USNRC)', ) ",
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95", ),
      KPUS          = SIMP ( statut="o", typ="R", defaut=9.4488,
                             fr="Paramètre exponentiel du modèle US", ),
    ), # Fin BLOC USNRC

    REV_2         = BLOC ( condition = " ModeleFluence in ( 'Dossier 900 MWe AP9701 rev 2 (REV_2)', ) ",
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2) ; HP-26/99/045 : p.31 : fluence max = 7.3/9.125/10/95", ),
    ), # Fin BLOC REV_2

    SDM_Lissage   = BLOC ( condition = " ModeleFluence in ( 'Lissage du modele ajuste (SDM_Lissage)', ) ",
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2)", ),
    ), # Fin BLOC SDM_Lissage

    GrandeDev     = BLOC ( condition = " ModeleFluence in ( 'Donnees francaises du palier CPY ajustees par secteur angulaire (GrandeDev)', ) ",
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2)", ),
    ), # Fin BLOC GrandeDev

    GD_Cuve       = BLOC ( condition = " ModeleFluence in ( 'Grand developpement (GD_Cuve)', ) ",
      # fmax
      FluenceMax    = SIMP ( statut="o", typ="R", defaut=6.5, 
                             fr="Fluence maximale en surface interne assimilée par la cuve (10^19 n/cm2)", ),
      Coefficients  = Coef_Fluence(),
    ), # Fin BLOC GD_Cuve

  ), # Fin FACT Fluence

#==========================
# 4.2 Modeles d'irradiation
#==========================

  Irradiation = FACT ( statut="o",

    # TYPEIRR INTO RTNDT, FLUENCE
    TypeIrradiation = SIMP ( statut = "o", typ = "TXM", defaut="RTndt de la cuve a l instant de l analyse",
                       fr = "Type d'irradiation",
	               into = ( "RTndt de la cuve a l instant de l analyse", # RTNDT 
		                "Modele d irradiation" ), # FLUENCE
                       ),

#====
# Definition des parametres selon le type d'irradiation
#====

    IrradiationParValeur = BLOC ( condition = "TypeIrradiation=='RTndt de la cuve a l instant de l analyse'",
 
      RTNDT = SIMP ( statut="o", typ="R", defaut=73., 
                     fr="RTNDT de la cuve à l'instant de l'analyse (°C)", ),

    ), # Fin BLOC IrradiationParValeur

    IrradiationParModele = BLOC ( condition = "TypeIrradiation=='Modele d irradiation'",
 
      # MODELIRR
      ModeleIrradiation = SIMP ( statut="o", typ="TXM", defaut="Metal de Base : formule de FIM/FIS Houssin",
                                fr="Modèle d'irradiation pour virole ou joint soudé",
		                into=( "Metal de Base : formule de FIM/FIS Houssin", # HOUSSIN 
		                       "Metal de Base : formule de FIM/FIS Persoz", # PERSOZ
		                       "Metal de Base : formule de FIM/FIS Lefebvre", # LEFEBVRE
		                       "Metal de Base : Regulatory Guide 1.00 rev 2", # USNRCmdb
		                       "Joint Soude : formulation de FIM/FIS Brillaud", # BRILLAUD
		                       "Joint Soude : Regulatory Guide 1.00 rev 2" ), # USNRCsoud
                                ),
      Parametres_FIMFIS = BLOC ( condition = " ModeleIrradiation in ( 'Metal de Base : formule de FIM/FIS Houssin' , 'Metal de Base : formule de FIM/FIS Persoz', 'Metal de Base : formule de FIM/FIS Lefebvre', 'Joint Soude : formulation de FIM/FIS Brillaud', ) ",
        # CU
        TeneurCuivre         = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Teneur en cuivre (%)", ),
        # CU_MESSAGE
        TeneurCuivre_mess    = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la teneur en cuivre (%)",
				      into=( "NON","OUI" ), ),
        # NI
        TeneurNickel         = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Teneur en nickel (%)", ),
        # NI_MESSAGE
        TeneurNickel_mess    = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la teneur en nickel (%)",
				      into=( "NON","OUI" ), ),
        # P
        TeneurPhosphore      = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Teneur en phosphore (%)", ),
        # P_MESSAGE
        TeneurPhosphore_mess = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la teneur en phosphore (%)",
				      into=( "NON","OUI" ), ),
        # RTimoy
        MoyenneRTndt         = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Moyenne de RTNDT : virole C1 de cuve Chinon : mdb=>-17.°C et js=>42.°C (HT-56/05/038 : p.52)", ),
        # RTimoy_MESSAGE
        MoyenneRTndt_mess    = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la moyenne de RTNDT",
				      into=( "NON","OUI" ), ),
        # nbectDRTNDT
        NombreEcartTypeRTndt = SIMP ( statut="o", typ="R", defaut=2., 
                                      fr="Nombre d'écart-type par rapport à la moyenne de DRTNDT", ),
        # nbectDRTNDT_MESSAGE
        NombreEcartTypeRTndt_mess = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran du nombre d'écart-type par rapport à la moyenne de DRTNDT",
				      into=( "NON","OUI" ), ),
      ), # Fin BLOC Parametres_FIMFIS

      Parametres_USNRC = BLOC ( condition = " ModeleIrradiation in ( 'Metal de Base : Regulatory Guide 1.00 rev 2' , 'Joint Soude : Regulatory Guide 1.00 rev 2', ) ",
        # CU
        TeneurCuivre         = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Teneur en cuivre (%)", ),
        # CU_MESSAGE
        TeneurCuivre_mess    = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la teneur en cuivre (%)",
				      into=( "NON","OUI" ), ),
        # NI
        TeneurNickel         = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Teneur en nickel (%)", ),
        # NI_MESSAGE
        TeneurNickel_mess    = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la teneur en nickel (%)",
				      into=( "NON","OUI" ), ),
        # RTimoy
        MoyenneRTndt         = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Moyenne de RTNDT : virole C1 de cuve Chinon : mdb=>-17.°C et js=>42.°C (HT-56/05/038 : p.52)", ),
        # RTimoy_MESSAGE
        MoyenneRTndt_mess    = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran de la moyenne de RTNDT",
				      into=( "NON","OUI" ), ),
        # RTicov
        CoefVariationRTndt   = SIMP ( statut="o", typ="R", defaut=0., 
                                      fr="Coefficient de variation de la RTNDT initiale", ),
        # RTicov_MESSAGE
        CoefVariationRTndt_mess = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                         fr="Affichage ecran du coefficient de variation de la RTNDT initiale",
				         into=( "NON","OUI" ), ),
        # USectDRT
        EcartTypeRTndt       = SIMP ( statut="o", typ="R", defaut=28., 
                                      fr="Ecart-type du décalage de RTNDT (°F) (28. pour js et 17. pour mdb)", ),
        # nbectDRTNDT
        NombreEcartTypeRTndt = SIMP ( statut="o", typ="R", defaut=2., 
                                      fr="Nombre d'écart-type par rapport à la moyenne de DRTNDT", ),
        # nbectDRTNDT_MESSAGE
        NombreEcartTypeRTndt_mess = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                      fr="Affichage ecran du nombre d'écart-type par rapport à la moyenne de DRTNDT",
				      into=( "NON","OUI" ), ),
      ), # Fin BLOC Parametres_USNRC 

    ), # Fin BLOC IrradiationParModele

  ), # Fin FACT Irradiation

#========================
# 4.3 Modeles de tenacite
#========================

  Tenacite = FACT ( statut = "o",

    # MODELKIC
    ModeleTenacite = SIMP ( statut="o", typ="TXM", defaut="RCC-M/ASME coefficient=2",
                    fr="Modèle de calcul de la ténacité à l'amorçage KIc", 
		    into=( "RCC-M/ASME coefficient=2", # RCC-M
		           "RCC-M/ASME coefficient=2 CUVE1D", # RCC-M_simpl
		           "RCC-M/ASME coefficient=2.33 (Houssin)", # Houssin_RC
		           "RCC-M/ASME avec KI=KIpalier", # RCC-M_pal
		           "RCC-M/ASME avec KI~exponentiel", # RCC-M_exp
		           "Weibull basee sur la master cuve", # Wallin
		           "Weibull basee sur la master cuve (REME)", # REME
		           "Weibull n°1 (etude ORNL)", # ORNL
		           "Weibull n°2", # WEIB2
		           "Weibull n°3", # WEIB3
		           "Weibull generalisee", # WEIB_GEN
      		           "Exponentielle n°1 (Frama)", # Frama
		           "Exponentielle n°2 (LOGWOLF)" ), # LOGWOLF
	            ),


#====
# Definition des parametres selon le modele de tenacité
#====

# Modeles type RCC-M

    KIc_RCCM = BLOC ( condition = " ModeleTenacite in ( 'RCC-M/ASME coefficient=2', 'RCC-M/ASME coefficient=2.33 (Houssin)', 'RCC-M/ASME avec KI=KIpalier', ) ",

      # nbectKIc
      NbEcartType_MoyKIc       = SIMP ( statut="o", typ="R", defaut=-2., 
                                        fr = "Nombre d'écart-type par rapport à la moyenne de KIc (nb sigma) : det = -2 ", ),
      # nbectKIc_MESSAGE
      NbEcartType_MoyKIc_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                        fr = "Affichage ecran du nombre d'écart-type par rapport à la moyenne de KIc",
					into = ( "NON","OUI" ), ),

      # KICPAL
      PalierDuctile_KIc        = SIMP ( statut="o", typ="R", defaut=195., 
                                        fr="Palier déterministe de K1c ou valeur du palier ductile plafonnant la courbe (en MPa(m^0.5)) ", ),

      # KICCDV
      CoefficientVariation_KIc = SIMP ( statut="o", typ="R", defaut = 0.15, 
                                        fr = "Coefficient de variation de la loi normale de K1c ", ),

    ), # Fin BLOC KIc_RCCM

    KIc_RCCM_exp = BLOC ( condition = " ModeleTenacite in ( 'RCC-M/ASME avec KI~exponentiel', ) ",

      # nbectKIc
      NbEcartType_MoyKIc       = SIMP ( statut="o", typ="R", defaut=-2., 
                                        fr = "Nombre d'écart-type par rapport à la moyenne de KIc (nb sigma) : det = -2 ", ),
      # nbectKIc_MESSAGE
      NbEcartType_MoyKIc_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                        fr = "Affichage ecran du nombre d'écart-type par rapport à la moyenne de KIc",
					into = ( "NON","OUI" ), ),

      # KICCDV
      CoefficientVariation_KIc = SIMP ( statut="o", typ="R", defaut = 0.15, 
                                        fr = "Coefficient de variation de la loi normale de K1c ", ),

    ), # Fin BLOC KIc_RCCM_exp

# Modeles type exponentiel (Frama, LOGWOLF)

    KIc_Exponentielle = BLOC ( condition = " ModeleTenacite in ( 'Exponentielle n°1 (Frama)', 'Exponentielle n°2 (LOGWOLF)', ) ",

      # nbectKIc
      NbEcartType_MoyKIc = SIMP ( statut="o", typ="R", defaut=-2., 
                                  fr="Nombre d'écart-type par rapport à la moyenne de KIc (nb sigma) : det = -2 ", ),
      # nbectKIc_MESSAGE
      NbEcartType_MoyKIc_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                        fr = "Affichage ecran du nombre d'écart-type par rapport à la moyenne de KIc",
					into = ( "NON","OUI" ), ),

    ), # Fin BLOC KIc_Exponentielle

# Modeles type Weibull

    KIc_Weibull = BLOC ( condition = " ModeleTenacite in ( 'Weibull basee sur la master cuve (REME)', 'Weibull n°1 (etude ORNL)', 'Weibull n°2', 'Weibull n°3', ) ",
 
      # NBCARAC
      NBRE_CARACTERISTIQUE = SIMP ( statut="o", typ="TXM", defaut="QUANTILE", 
                                        fr="Nombre caracteristique : ORDRE ou QUANTILE",
                                        into=( "ORDRE", "QUANTILE" ), ),

      ORDRE = BLOC ( condition = "NBRE_CARACTERISTIQUE=='ORDRE'",
        # nbectKIc
        NbEcartType_MoyKIc = SIMP ( statut="o", typ="R", defaut=-2., 
                                    fr="Valeur caractéristique de KIc exprimée en nombre d'écart-type par rapport à la moyenne de KIc (nb sigma) : det = -2 ", ),
        # nbectKIc_MESSAGE
        NbEcartType_MoyKIc_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                          fr = "Affichage ecran du nombre d'écart-type par rapport à la moyenne de KIc",
                                          into = ( "NON","OUI" ), ),
      ), # Fin BLOC ORDRE 

      QUANTILE = BLOC ( condition = "NBRE_CARACTERISTIQUE=='QUANTILE'",
        # fractKIc
        Fractile_KIc       = SIMP ( statut="o", typ="R", defaut=5., 
                                  fr="Valeur caractéristique de KIc exprimée en ordre de fractile (%) ", ),
        # fractKIc_MESSAGE
        Fractile_KIc_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                    fr="Affichage ecran de la valeur caractéristique de KIc exprimée en ordre de fractile (%) ",
                                    into = ( "NON","OUI" ), ),
      ), # Fin BLOC ORDRE 

    ), # Fin BLOC KIc_Weibull

    KIc_MasterCuve = BLOC ( condition = " ModeleTenacite in ( 'Weibull basee sur la master cuve', ) ",
 
      # NBCARAC
      NBRE_CARACTERISTIQUE = SIMP ( statut="o", typ="TXM", defaut="QUANTILE", 
                                        fr="Nombre caracteristique : ORDRE ou QUANTILE",
                                        into=( "ORDRE", "QUANTILE" ), ),

      ORDRE = BLOC ( condition = "NBRE_CARACTERISTIQUE=='ORDRE'",
        # nbectKIc
        NbEcartType_MoyKIc = SIMP ( statut="o", typ="R", defaut=-2., 
                                    fr="Valeur caractéristique de KIc exprimée en nombre d'écart-type par rapport à la moyenne de KIc (nb sigma) : det = -2 ", ),
        # nbectKIc_MESSAGE
        NbEcartType_MoyKIc_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                          fr = "Affichage ecran du nombre d'écart-type par rapport à la moyenne de KIc",
                                          into = ( "NON","OUI" ), ),
      ), # Fin BLOC ORDRE 

      QUANTILE = BLOC ( condition = "NBRE_CARACTERISTIQUE=='QUANTILE'",
        # fractKIc
        Fractile_KIc       = SIMP ( statut="o", typ="R", defaut=5., 
                                  fr="Valeur caractéristique de KIc exprimée en ordre de fractile (%) ", ),
        # fractKIc_MESSAGE
        Fractile_KIc_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                    fr="Affichage ecran de la valeur caractéristique de KIc exprimée en ordre de fractile (%) ",
                                    into = ( "NON","OUI" ), ),
      ), # Fin BLOC ORDRE 

      # T0WALLIN
      Temperature_KIc100 = SIMP ( statut="o", typ="I", defaut=-27, 
                                  fr="Paramètre T0 du modèle Wallin (°C) : température pour laquelle la téncité du matériau vaut en moyenne 100MPa.m^5", ),

    ), # Fin BLOC KIc_MasterCuve

    Weibull_Generalisee = BLOC ( condition = " ModeleTenacite in ( 'Weibull generalisee',) ",
 
      # NBCARAC
      NBRE_CARACTERISTIQUE = SIMP ( statut="o", typ="TXM", defaut="QUANTILE", 
                                        fr="Nombre caracteristique : ORDRE ou QUANTILE",
                                        into=( "ORDRE", "QUANTILE" ), ),

      ORDRE = BLOC ( condition = "NBRE_CARACTERISTIQUE=='ORDRE'",
        # nbectKIc
        NbEcartType_MoyKIc = SIMP ( statut="o", typ="R", defaut=-2., 
                                    fr="Valeur caractéristique de KIc exprimée en nombre d'écart-type par rapport à la moyenne de KIc (nb sigma) : det = -2 ", ),
        # nbectKIc_MESSAGE
        NbEcartType_MoyKIc_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                          fr = "Affichage ecran du nombre d'écart-type par rapport à la moyenne de KIc",
                                          into = ( "NON","OUI" ), ),
      ), # Fin BLOC ORDRE 

      QUANTILE = BLOC ( condition = "NBRE_CARACTERISTIQUE=='QUANTILE'",
        # fractKIc
        Fractile_KIc       = SIMP ( statut="o", typ="R", defaut=5., 
                                  fr="Valeur caractéristique de KIc exprimée en ordre de fractile (%) ", ),
        # fractKIc_MESSAGE
        Fractile_KIc_mess  = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                    fr="Affichage ecran de la valeur caractéristique de KIc exprimée en ordre de fractile (%) ",
                                    into = ( "NON","OUI" ), ),
      ), # Fin BLOC ORDRE 

      Coefficients       = Coef_WeibGen(),

    ), # Fin BLOC Weibull_Generalisee

    # ATTNCORRBETA - CORRIRWIN
    CorrectionPlastique  = SIMP ( statut="o", typ="TXM", defaut="Correction plastique BETA (pour DSR et defaut decale)", 
                                  fr="Correction plastique dans le calcul du facteur d'intensité de contraintes",
                                  into=( "Correction plastique BETA (pour DSR et defaut decale)", # ATTNCORRBETA = NON
                                         "Correction plastique BETA attenuee (pour DSR et défaut decale)", # ATTNCORRBETA = OUI
				         "Correction plastique IRWIN (pour defaut debouchant)" ), ), # CORRIRWIN = OUI

    Fissure = BLOC ( condition = " ModeleTenacite in ( 'RCC-M/ASME coefficient=2', 'RCC-M/ASME coefficient=2.33 (Houssin)', 'RCC-M/ASME avec KI=KIpalier', 'RCC-M/ASME avec KI~exponentiel', )",

      # ARRETFISSURE
      ArretDeFissure = SIMP ( statut="o", typ="TXM", defaut="NON", 
                              fr="Prise en compte de l'arrêt de fissure",
                              into=( "OUI", "NON" ), ),

      KIa_RCCM = BLOC ( condition = "ArretDeFissure=='OUI'",
        # INCRDEF
        IncrementTailleFissure   = SIMP ( statut="o", typ="R", defaut=0.005, 
                                          fr="Incrément de la taille de fissure pour la propagation (en m)", ),
        # INCRDEF_MESSAGE
        IncrementTailleFissure_mess = SIMP ( statut="o", typ="TXM", defaut="NON", 
                                             fr="Affichage ecran de l incrément de la taille de fissure pour la propagation (en m)",
					     into = ("NON", "OUI"), ),

        # nbectKIa
        NbEcartType_MoyKIa       = SIMP ( statut="o", typ="R", defaut=-2., 
                                          fr="Nombre d'écart-type par rapport à la moyenne de KIa (nb sigma) ", ),

        # KIAPAL
        PalierDuctile_KIa        = SIMP ( statut="o", typ="R", defaut=195., 
                                          fr="Palier déterministe de K1a -ténacite à l'arrêt- (en MPa(m^0.5)) ", ),
        # KIACDV
        CoefficientVariation_KIa = SIMP ( statut="o", typ="R", defaut=0.10, 
                                          fr="Coefficient de variation de la loi normale de K1a -ténacite à l'arrêt- ", ),

      ), # Fin BLOC KIa_RCCM

    ), # Fin BLOC Fissure

  ), # Fin FACT Tenacite

) # Fin PROC MODELES


#==================
# 5. Initialisation
#==================

INITIALISATION = PROC ( nom = "INITIALISATION",
                        op = 68,
	                repetable = 'n',
                        fr = "Initialisation : instant initial, profils radiaux de température et contraintes", 

  TemperatureInitiale = FACT ( statut = "o",

    ProfilRadial_TemperatureInitiale = SIMP ( statut="o", typ=Tuple(2), max="**",
                                              fr="Profil radial de la température initiale dans la cuve (en m : °C) ", ),
    Amont_TemperatureInitiale        = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                              fr="Prolongation à la frontière amont",
                                              into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_TemperatureInitiale         = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                              fr="Prolongation à la frontière aval",
                                              into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin FACT TemperatureInitiale

  ContraintesInitiales = FACT ( statut = "o",

    ProfilRadial_ContraintesInitiales = SIMP ( statut="o", typ=Tuple(4), max="**",
                                               fr="Profil radial des contraintes radiale, circonférentielle et longitudinale dans la cuve (en m : xx : xx : xx) ", ),
    Amont_ContraintesInitiales        = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                               fr="Prolongation à la frontière amont",
                                               into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_ContraintesInitiales         = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                               fr="Prolongation à la frontière aval",
                                               into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin FACT ContraintesInitiales

  # INSTINIT
  InstantInitialisation = SIMP ( statut="o", typ="R", defaut = -1., 
                                 fr="Instant initial auquel sont définies la température, ainsi que les contraintes initiales (en s) ", ),

) # Fin PROC INITIALISATION


#==================================
# 6. CARACTERISTIQUES DU REVETEMENT
#==================================

REVETEMENT = PROC ( nom = "REVETEMENT",
                    op = 68,
	            repetable = 'n',
                    fr = "Caracteristiques du revêtement", 

  # KTHREV
  ConditionLimiteThermiqueREV = SIMP ( statut="o", typ="TXM", defaut="CHALEUR",
                                       fr="Option pour définir les caractéristiques du revêtement ",
                                       into=( "ENTHALPIE", "CHALEUR",),
                                       ),

  EnthalpieREV = BLOC ( condition = "ConditionLimiteThermiqueREV=='ENTHALPIE'",

    EnthalpieREV_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                          fr="Température (°C) / enthalpie massique  (J/kg) ", ),
    Amont_EnthalpieREV           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                          fr="Prolongation à la frontière amont",
                                          into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_EnthalpieREV            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                          fr="Prolongation à la frontière aval",
                                          into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin BLOC EnthalpieREV


  ChaleurREV = BLOC ( condition = "ConditionLimiteThermiqueREV=='CHALEUR'",

    ChaleurREV_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                        fr="Température (°C) / chaleur volumique (J/kg/K) ", ),
    Amont_ChaleurREV           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                        fr="Prolongation à la frontière amont",
                                        into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_ChaleurREV            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                        fr="Prolongation à la frontière aval",
                                        into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin BLOC ChaleurREV

  ConductiviteREV = FACT (statut = "o",

    ConductiviteREV_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                             fr="Température (°C) / conductivité thermique (W/m/°C) ", ),
    Amont_ConductiviteREV           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                             fr="Prolongation à la frontière amont",
                                             into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_ConductiviteREV            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                             fr="Prolongation à la frontière aval",
                                             into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin FACT ConductiviteREV

  ModuleYoungREV = FACT (statut = "o",

    ModuleYoungREV_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                            fr="Température (°C) / module d'Young (MPa) ", ),
    Amont_ModuleYoungREV           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                            fr="Prolongation à la frontière amont",
                                            into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_ModuleYoungREV            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                            fr="Prolongation à la frontière aval",
                                            into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin FACT ModuleYoungREV

  CoeffDilatThermREV = FACT (statut = "o",

    CoeffDilatThermREV_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                                fr="Température (°C) / coefficient de dilatation thermique (°C-1) ", ),
    Amont_CoeffDilatThermREV           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                                fr="Prolongation à la frontière amont",
                                                into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_CoeffDilatThermREV            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                                fr="Prolongation à la frontière aval",
                                                into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin FACT CoeffDilatThermREV

  LimiteElasticiteREV = FACT (statut = "o",

    LimiteElasticiteREV_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                                 fr="Température (°C) / limite d'élasticite (MPa) ", ),
    Amont_LimiteElasticiteREV           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                                 fr="Prolongation à la frontière amont",
                                                 into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_LimiteElasticiteREV            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                                 fr="Prolongation à la frontière aval",
                                                 into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin FACT LimiteElasticiteREV

  AutresParametresREV = FACT (statut = "o",

    # TREFREV
    TemperatureDeformationNulleREV   = SIMP ( statut="o", typ="R", defaut=20.,
                                              fr="Température de référence pour laquelle les déformations thermiques sont nulles (°C) ", ),
    # TDETREV
    TemperaturePourCoefDilatThermREV = SIMP ( statut="o", typ="R", defaut=287.,
                                              fr="Température de définition du coefficient de dilatation thermique (°C) ", ),
    # NUREV
    CoefficientPoissonREV            = SIMP ( statut="o", typ="R", defaut=0.3,
                                              fr="Coefficient de Poisson ", ),

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
  ConditionLimiteThermiqueMDB = SIMP ( statut="o", typ="TXM", defaut="CHALEUR",
                                       fr="Option pour definir les caractéristiques du revêtement ",
                                       into=( "ENTHALPIE", "CHALEUR",), ),

  EnthalpieMDB = BLOC ( condition = "ConditionLimiteThermiqueMDB=='ENTHALPIE'",

    EnthalpieMDB_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                          fr="Température (°C) / enthalpie massique (J/kg) ", ),
    Amont_EnthalpieMDB           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                          fr="Prolongation à la frontière amont",
                                          into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_EnthalpieMDB            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                          fr="Prolongation à la frontière aval",
                                          into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin BLOC EnthalpieMDB

  ChaleurMDB = BLOC ( condition = "ConditionLimiteThermiqueMDB=='CHALEUR'",

    ChaleurMDB_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                        fr="Température (°C) / chaleur volumique (J/kg/K) ", ),
    Amont_ChaleurMDB           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                        fr="Prolongation à la frontière amont",
                                        into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_ChaleurMDB            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                        fr="Prolongation à la frontière aval",
                                        into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin BLOC ChaleurMDB

  ConductiviteMDB = FACT ( statut = "o",

    ConductiviteMDB_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                             fr="Température (°C) / conductivité thermique (W/m/°C) ", ),
    Amont_ConductiviteMDB           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                             fr="Prolongation à la frontière amont",
                                             into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_ConductiviteMDB            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                             fr="Prolongation à la frontière aval",
                                             into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin FACT ConductiviteMDB

  ModuleYoungMDB = FACT ( statut="o",

    ModuleYoungMDB_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                            fr="Température (°C) / module d'Young (MPa) ", ),
    Amont_ModuleYoungMDB           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                            fr="Prolongation à la frontière amont",
                                            into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_ModuleYoungMDB            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                            fr="Prolongation à la frontière aval",
                                            into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin FACT ModuleYoungMDB

  CoeffDilatThermMDB = FACT ( statut="o",

    CoeffDilatThermMDB_Fct_Temperature = SIMP ( statut="o", typ=Tuple(2), max="**",
                                                fr="Température (°C) / coefficient de dilatation thermique (°C-1) ", ),
    Amont_CoeffDilatThermMDB           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                                fr="Prolongation à la frontière amont",
                                                into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_CoeffDilatThermMDB            = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                                fr="Prolongation à la frontière aval",
                                                into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # Fin FACT CoeffDilatThermMDB

  AutresParametresMDB = FACT ( statut = "o",

    # TREFMDB
    TemperatureDeformationNulleMDB   = SIMP ( statut="o", typ="R", defaut=20.,
                                              fr="Température de référence pour laquelle les déformations thermiques sont nulles (°C) ", ),
    # TDETMDB
    TemperaturePourCoefDilatThermMDB = SIMP ( statut="o", typ="R", defaut=287.,
                                              fr="Température de définition du coefficient de dilatation thermique (°C) ", ),
    # NUMDB
    CoefficientPoissonMDB            = SIMP ( statut="o", typ="R", defaut=0.3,
                                              fr="Coefficient de Poisson ", ),

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

    ProfilTemporel_Pression = SIMP ( statut="o", typ=Tuple(2), max="**",
                                     fr = "Instant (s) / pression (MPa) ", ),
    Amont_Pression          = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                     fr="Prolongation à la frontière amont",
                                     into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    Aval_Pression           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                     fr="Prolongation à la frontière aval",
                                     into=( 'Continu', 'Exclu', 'Lineaire' ), ),

  ), # FIN FACT Pression


  CL_thermique = FACT ( statut = "o",

    # TYPCLTH
    TypeConditionLimiteThermique = SIMP ( statut="o", typ="TXM",
                                         fr="Type de condition thermique en paroi interne ",
                                         into=( "Temperature imposee en paroi", # TEMP_IMPO
                                               "Flux de chaleur impose en paroi", # FLUX_REP
                                               "Temperature imposee du fluide et coefficient echange", # ECHANGE
                                               "Debit massique et temperature d injection de securite", # DEBIT
                                               "Temperature imposee du fluide et debit d injection de securite", # TEMP_FLU
                                               "Courbe APRP"), # APRP
                                        ),

    APRP = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Courbe APRP', ) ",

      # INSTANT1
      Instant_1              = SIMP ( statut="o", typ="R", defaut=21.,
                                    fr="Palier 2 à T1 : borne inférieure (en s) ", ),
      # INSTANT2
      Instant_2              = SIMP ( statut="o", typ="R", defaut=45.,
                                      fr="Palier 2 à T1 : borne supérieure (en s) ", ),
      # QACCU
      DebitAccumule          = SIMP ( statut="o", typ="R", defaut=2.3,
                                      fr="Debit accumule (en m3/h) ", ),
      # QIS
      DebitInjectionSecurite = SIMP ( statut="o", typ="R", defaut=0.375,
                                      fr="Debit injection securite (en m3/h) ", ),
      # TIS_MESSAGE
      TempInjectionSecurite_mess = SIMP ( statut="o", typ="TXM", defaut="NON",
                                      fr="Affichage ecran de la temperature injection securite",
                                      into = ( "NON", "OUI" ), ),
    ), # Fin BLOC APRP

    TemperatureImposeeFluide     = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Temperature imposee en paroi','Temperature imposee du fluide et coefficient echange', 'Temperature imposee du fluide et debit d injection de securite', 'Courbe APRP' ) ",

      ProfilTemporel_TemperatureImposeeFluide = SIMP ( statut="o", typ=Tuple(2), max="**",
                                                       fr = "Instant (s) / Température imposée (°C) ", ),
      Amont_TemperatureImposeeFluide          = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                                       fr="Prolongation à la frontière amont",
                                                       into=( 'Continu', 'Exclu', 'Lineaire' ), ),
      Aval_TemperatureImposeeFluide           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                                       fr="Prolongation à la frontière aval",
                                                       into=( 'Continu', 'Exclu', 'Lineaire' ), ),

    ), # Fin BLOC TemperatureImposeeFluide
 

    FluxChaleur                  = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Flux de chaleur impose en paroi', ) ",

      ProfilTemporel_FluxChaleur    = SIMP ( statut="o", typ=Tuple(2), max="**",
  	                                   fr="Instant (s) / Flux de chaleur impose (W/m2) ", ),
      Amont_FluxChaleur             = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                           fr="Prolongation à la frontière amont",
                                           into=( 'Continu', 'Exclu', 'Lineaire' ), ),
      Aval_FluxChaleur              = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                           fr="Prolongation à la frontière aval",
                                           into=( 'Continu', 'Exclu', 'Lineaire' ), ),

    ), # Fin BLOC FluxChaleur

    CoefficientEchange          = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Temperature imposee du fluide et coefficient echange', ) ",

      ProfilTemporel_CoefficientEchange = SIMP ( statut="o", typ=Tuple(2), max="**",
                                               fr="Instant (s) / Coefficient d'échange (W/m2/K) ", ),
      Amont_CoefficientEchange          = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                               fr="Prolongation à la frontière amont",
                                               into=( 'Continu', 'Exclu', 'Lineaire' ), ),
      Aval_CoefficientEchange           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                               fr="Prolongation à la frontière aval",
                                               into=( 'Continu', 'Exclu', 'Lineaire' ), ),

    ), # Fin BLOC CoefficientEchange

    DebitMassique               = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Debit massique et temperature d injection de securite', ) ",

      ProfilTemporel_DebitMassique = SIMP ( statut="o", typ=Tuple(2), max="**",
                                          fr="Instant (s) / Débit massique (kg/s) ", ),
      Amont_DebitMassique          = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                          fr="Prolongation à la frontière amont",
                                          into=( 'Continu', 'Exclu', 'Lineaire' ), ),
      Aval_DebitMassique = SIMP ( statut="o", typ="TXM",
                                fr="Prolongation à la frontière aval", defaut="Continu",
                                into=( 'Continu', 'Exclu', 'Lineaire' ), ),

    ), # Fin BLOC DebitMassique

    TemperatureInjection        = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Debit massique et temperature d injection de securite', ) ",

      ProfilTemporel_TemperatureInjection = SIMP ( statut="o", typ=Tuple(2), max="**",
                                                 fr="Instant (s) / Température d'injection de sécurité  (°C) ", ),
      Amont_TemperatureInjection          = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                                 fr="Prolongation à la frontière amont",
                                                 into=( 'Continu', 'Exclu', 'Lineaire' ), ),
      Aval_TemperatureInjection           = SIMP ( statut="o", typ = "TXM", defaut="Continu",
                                                 fr="Prolongation à la frontière aval",
                                                 into=( 'Continu', 'Exclu', 'Lineaire' ), ),
    ), # Fin BLOC TemperatureInjection

    DebitInjection              = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Temperature imposee du fluide et debit d injection de securite', 'Courbe APRP', ) ",

      ProfilTemporel_DebitInjection = SIMP ( statut="o", typ=Tuple(2), max="**",
                                           fr="Instant (s) / Débit d'injection de sécurité (kg/s) ", ),
      Amont_DebitInjection          = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                           fr="Prolongation à la frontière amont",
                                           into=( 'Continu', 'Exclu', 'Lineaire' ), ),
      Aval_DebitInjection           = SIMP ( statut="o", typ="TXM", defaut="Continu",
                                           fr="Prolongation à la frontière aval",
                                           into=( 'Continu', 'Exclu', 'Lineaire' ), ),

    ), # Fin BLOC DebitInjection

    Vestale = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Temperature imposee du fluide et debit d injection de securite', 'Debit massique et temperature d injection de securite', 'Courbe APRP', ) ",

      # DH
      DiametreHydraulique             = SIMP ( statut="o", typ="R", defaut=0.3816,
                                             fr="Diamètre hydraulique (m) ", ),
      # DH_MESSAGE
      DiametreHydraulique_mess        = SIMP ( statut="o", typ="TXM", defaut="NON",
                                             fr="Affichage ecran du diamètre hydraulique (m) ",
					     into = ( "NON", "OUI" ), ),
      # SECTION
      SectionEspaceAnnulaire          = SIMP ( statut="o", typ="R", defaut=0.21712,
                                             fr="Section espace annulaire (m2) ", ),
      # SECTION_MESSAGE
      SectionEspaceAnnulaire_mess     = SIMP ( statut="o", typ="TXM", defaut="NON",
                                             fr="Affichage ecran de la section espace annulaire (m2) ",
					     into = ( "NON", "OUI" ), ),
      # DELTA
      HauteurCaracConvectionNaturelle = SIMP ( statut="o", typ="R", defaut=6.,
                                             fr="Hauteur caractéristique convection naturelle (m) ", ),
      # DELTA_MESSAGE
      HauteurCaracConvectionNaturelle_mess = SIMP ( statut="o", typ="TXM", defaut="NON",
                                                  fr="Affichage ecran de la hauteur caractéristique convection naturelle (m) ",
					          into = ( "NON", "OUI" ), ),
      # EPS
      CritereConvergenceRelative      = SIMP ( statut="o", typ="R", defaut=0.00001,
                                             fr="Critère convergence relative (-) ", ),
      # COEFVESTALE
      CoefficientsVestale             = SIMP ( statut="o", typ="TXM", defaut="NON",
                                             fr="Application des coefficients de Vestale", 
                                             into=( 'OUI', 'NON' ), ),

    ), # Fin BLOC Vestale

    Creare = BLOC ( condition = " TypeConditionLimiteThermique in ( 'Debit massique et temperature d injection de securite', ) ",

      # VM
      VolumeMelange_CREARE           = SIMP ( statut="o", typ="R", defaut=14.9,
                                            fr = "Volume de mélange CREARE (m3) ", ),
      # VM_MESSAGE
      VolumeMelange_CREARE_mess      = SIMP ( statut="o", typ="TXM", defaut="NON",
                                            fr = "Affichage ecran du volume de mélange CREARE (m3) ",
                                             into=( 'OUI', 'NON' ), ),
      # T0
      TemperatureInitiale_CREARE     = SIMP ( statut="o", typ="R", defaut=250.,
                                            fr="Température initiale CREARE (°C) ", ),
      # T0_MESSAGE
      TemperatureInitiale_CREARE_mess = SIMP ( statut="o", typ="TXM", defaut="NON",
                                             fr="Affichage ecran de la température initiale CREARE (°C) ",
                                             into=( 'OUI', 'NON' ), ),
      # SE
      SurfaceEchange_FluideStructure = SIMP ( statut="o", typ="R", defaut=0.,
                                            fr="Surface d'échange fluide/structure (m2) ", ),
      # SE_MESSAGE
      SurfaceEchange_FluideStructure_mess = SIMP ( statut="o", typ="TXM", defaut="NON",
                                                 fr="Affichage ecran de la surface d'échange fluide/structure (m2) ",
                                                 into=( 'OUI', 'NON' ), ),

    ), # Fin BLOC Creare

  ), # FIN FACT CL_thermique

) # Fin PROC TRANSITOIRE
