# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
    Ce module contient le plugin generateur de fichier au format 
    DefaillCUVE pour EFICAS.

"""
import traceback
import types,string,re

from Noyau import N_CR
from Accas import MCSIMP
from generator_python import PythonGenerator

def entryPoint():
   """
       Retourne les informations nécessaires pour le chargeur de plugins

       Ces informations sont retournées dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'cuve2dg',
        # La factory pour créer une instance du plugin
          'factory' : Cuve2dgGenerator,
          }


class Cuve2dgGenerator(PythonGenerator):
   """
       Ce generateur parcourt un objet de type JDC et produit
       un texte au format eficas et 
       un texte au format DefaillCUVE

   """
   # Les extensions de fichier préconisées
   extensions=('.comm',)

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR generateur format DefaillCUVE pour DefaillCUVE',
                         fin='fin CR format DefaillCUVE pour DefaillCUVE')
      # Le texte au format DefaillCUVE est stocké dans l'attribut textCuve
      self.textCuve=''

      # Ce dictionnaire liste le nom des variables utilisees dans le script
      self.variable = {
         "NiveauImpression" : "MESSAGE_LEVEL",
	 "FichierDataIn"    : "DATARESUME_FILE",
	 "FichierTempSigma" : "TEMPSIG_FILE",
	 "FichierCSV"       : "CSV_FILE",
	 "FichierCREARE" : "CREARE_FILE",
	 "GrandeurEvaluee" : "GRANDEUR",
	 "IncrementTemporel" : "INCRTPS",
	 "IncrementMaxTemperature" : "DTPREC",
	 "IncrementMaxTempsAffichage" : "DTARCH",
	 "TraitementGeometrie" : "TYPEGEOM",
	 "RayonInterne" : "RINT",
	 "RayonInterne_mess" : "RINT_MESSAGE",
	 "RayonExterne" : "REXT",
	 "RayonExterne_mess" : "REXT_MESSAGE",
	 "EpaisseurRevetement" : "LREV",
	 "EpaisseurRevetement_mess" : "LREV_MESSAGE",
	 "LigamentExterneMin" : "LIGMIN",
	 "LigamentExterneMin_mess" : "LIGMIN_MESSAGE",
	 "NombreNoeudsMaillage" : "NBNO",
	 "TypeInitial" : "TYPEDEF",
	 "Orientation" : "ORIEDEF",
	 "ProfondeurRadiale" : "PROFDEF",
	 "ProfondeurRadiale_mess" : "PROFDEF_MESSAGE",
	 "ModeCalculLongueur" : "OPTLONG",
	 "Longueur" : "LONGDEF",
	 "Longueur_mess" : "LONGDEF_MESSAGE",
	 "CoefDirecteur" : "PROFSURLONG",
	 "CoefDirecteur_mess" : "PROFSURLONG_MESSAGE",
	 "Constante" : "LONGCONST",
	 "ModeCalculDecalage" : "DECATYP",
	 "DecalageNormalise" : "DECANOR",
	 "DecalageNormalise_mess" : "DECANOR_MESSAGE",
	 "DecalageRadial" : "DECADEF",
	 "DecalageRadial_mess" : "DECADEF_MESSAGE",
	 "Azimut" : "ANGLDEF",
	 "Azimut_mess" : "ANGLDEF_MESSAGE",
	 "Altitude_mess" : "ANGLDEF_MESSAGE",
	 "Altitude" : "ALTIDEF",
	 "Altitude_mess" : "ALTIDEF_MESSAGE",
	 "Pointe" : "POINDEF",
	 "ModeleFluence" : "MODELFLUENCE",
	 "ZoneActiveCoeur_AltitudeSup" : "H1COEUR",
	 "ZoneActiveCoeur_AltitudeInf" : "H2COEUR",
	 "FluenceMax" : "fmax",
	 "KPFrance" : "KPFRANCE",
	 "KPUS" : "KPUS",
	 "Azimut_0deg" : "COEFFLUENCE1",
	 "Azimut_5deg" : "COEFFLUENCE2",
	 "Azimut_10deg" : "COEFFLUENCE3",
	 "Azimut_15deg" : "COEFFLUENCE4",
	 "Azimut_20deg" : "COEFFLUENCE5",
	 "Azimut_25deg" : "COEFFLUENCE6",
	 "Azimut_30deg" : "COEFFLUENCE7",
	 "Azimut_35deg" : "COEFFLUENCE8",
	 "Azimut_40deg" : "COEFFLUENCE9",
	 "Azimut_45deg" : "COEFFLUENCE10",
	 "TypeIrradiation" : "TYPEIRR",
	 "RTNDT" : "RTNDT",
	 "ModeleIrradiation" : "MODELIRR",
	 "TeneurCuivre" : "CU",
	 "TeneurCuivre_mess" : "CU_MESSAGE",
	 "TeneurNickel" : "NI",
	 "TeneurNickel_mess" : "NI_MESSAGE",
	 "TeneurPhosphore" : "P",
	 "TeneurPhosphore_mess" : "P_MESSAGE",
	 "MoyenneRTndt" : "RTimoy",
	 "MoyenneRTndt_mess" : "RTimoy_MESSAGE",
	 "CoefVariationRTndt" : "RTicov",
	 "CoefVariationRTndt_mess" : "RTicov_MESSAGE",
	 "EcartTypeRTndt" : "USectDRT",
	 "EcartTypeRTndt_mess" : "USectDRT_MESSAGE",
	 "NombreEcartTypeRTndt" : "nbectDRTNDT",
	 "NombreEcartTypeRTndt_mess" : "nbectDRTNDT_MESSAGE",
	 "ModeleTenacite" : "MODELKIC",
	 "NBRE_CARACTERISTIQUE" : "NBCARAC",
	 "NbEcartType_MoyKIc" : "nbectKIc",
	 "NbEcartType_MoyKIc_mess" : "nbectKIc_MESSAGE",
	 "PalierDuctile_KIc" : "KICPAL",
	 "CoefficientVariation_KIc" : "KICCDV",
	 "Fractile_KIc" : "fractKIc",
	 "Fractile_KIc_mess" : "fractKIc_MESSAGE",
	 "Temperature_KIc100" : "T0WALLIN",
	 "A1" : "A1",
	 "A2" : "A2",
	 "A3" : "A3",
	 "B1" : "B1",
	 "B2" : "B2",
	 "B3" : "B3",
	 "C1" : "C1",
	 "C2" : "C2",
	 "C3" : "C3",
	 "AttnCorrBeta" : "ATTNCORRBETA",
	 "CorrIrwin" : "CORRIRWIN",
	 "ArretDeFissure" : "ARRETFISSURE",
	 "IncrementTailleFissure" : "INCRDEF",
	 "IncrementTailleFissure_mess" : "INCRDEF_MESSAGE",
	 "NbEcartType_MoyKIa" : "nbectKIa",
	 "PalierDuctile_KIa" : "KIAPAL",
	 "CoefficientVariation_KIa" : "KIACDV",
	 "InstantInitialisation" : "INSTINIT",
	 "ConditionLimiteThermiqueREV" : "KTHREV",
	 "TemperatureDeformationNulleREV" : "TREFREV",
	 "TemperaturePourCoefDilatThermREV" : "TDETREV",
	 "CoefficientPoissonREV" : "NUREV",
	 "ConditionLimiteThermiqueMDB" : "KTHMDB",
	 "TemperatureDeformationNulleMDB" : "TREFMDB",
	 "TemperaturePourCoefDilatThermMDB" : "TDETMDB",
	 "CoefficientPoissonMDB" : "NUMDB",
	 "TypeConditionLimiteThermique" : "TYPCLTH",
	 "Instant_1" : "INSTANT1",
	 "Instant_2" : "INSTANT2",
	 "DebitAccumule" : "QACCU",
	 "DebitInjectionSecurite" : "QIS",
	 "TempInjectionSecurite_mess" : "TIS_MESSAGE",
	 "DiametreHydraulique" : "DH",
	 "DiametreHydraulique_mess" : "DH_MESSAGE",
	 "SectionEspaceAnnulaire" : "SECTION",
	 "SectionEspaceAnnulaire_mess" : "SECTION_MESSAGE",
	 "HauteurCaracConvectionNaturelle" : "DELTA",
	 "HauteurCaracConvectionNaturelle_mess" : "DELTA_MESSAGE",
	 "CritereConvergenceRelative" : "EPS",
	 "CoefficientsVestale" : "COEFVESTALE",
	 "VolumeMelange_CREARE" : "VM",
	 "VolumeMelange_CREARE_mess" : "VM_MESSAGE",
	 "TemperatureInitiale_CREARE" : "T0",
	 "TemperatureInitiale_CREARE_mess" : "T0_MESSAGE",
	 "SurfaceEchange_FluideStructure" : "SE",
	 "SurfaceEchange_FluideStructure_mess" : "SE_MESSAGE",
         }

      # Ce dictionnaire liste le commentaire des variables utilisees dans le script
      self.comment = {
         "NiveauImpression" : "Niveau d impression des messages a l ecran (=0 : rien, =1 : temps calcul total, =2 : temps intermediaires)",
	 "FichierDataIn"    : "sortie du fichier recapitulatif des donnees d entree {OUI ; NON}",
	 "FichierTempSigma" : "sortie des fichiers temperature et contraintes {OUI ; NON}",
	 "FichierCSV" : "sortie du fichier resultat template_DEFAILLCUVE.CSV {OUI ; NON}",
	 "FichierCREARE" : "sortie du fichier Tfluide et Coef Echange {OUI ; NON}",
	 "GrandeurEvaluee" : "choix de la grandeur sous critere evaluee {FM_KICSURKCP ; MARGE_KI ; MARGE_KCP}",
	 "IncrementTemporel" : "increment temporel pour l analyse PROBABILISTE (si DETERMINISTE, fixer a 1)",
	 "IncrementMaxTemperature" : "increment max de temp/noeud/instant (degC)",
	 "IncrementMaxTempsAffichage" : "increment max de temps pour affichage (s)",
	 "TraitementGeometrie" : "traitement de la geometrie de la cuve : {GEOMETRIE, MAILLAGE}",
	 "RayonInterne" : "rayon interne (m)",
	 "RayonInterne_mess" : "affichage ecran du rayon interne (m)",
	 "RayonExterne" : "rayon externe (m)",
	 "RayonExterne_mess" : "affichage ecran du rayon externe (m)",
	 "EpaisseurRevetement" : "epaisseur revetement (m)",
	 "EpaisseurRevetement_mess" : "affichage ecran de l epaisseur revetement (m)",
	 "LigamentExterneMin" : "ligament externe minimal avant rupture (% de l'epaisseur de cuve)",
	 "LigamentExterneMin_mess" : "affichage ecran du ligament externe minimal avant rupture (% de l'epaisseur de cuve)",
	 "NombreNoeudsMaillage" : "nbre de noeuds dans l'epaisseur de la cuve",
	 "TypeInitial" : "type initial du defaut : DEBOUCHANT=Defaut Debouchant, DSR=Defaut Sous Revetement, DECALE=Defaut Decale",
	 "Orientation" : "orientation (LONGITUD / CIRCONF)",
	 "ProfondeurRadiale" : "profondeur radiale ou encore hauteur (m)",
	 "ProfondeurRadiale_mess" : "affichage ecran de la profondeur radiale ou encore hauteur (m)",
	 "ModeCalculLongueur" : "option pour definir la longueur du defaut (VALEUR pour une valeur fixe, FCTAFFINE pour une fct affine de la profondeur)",
	 "Longueur" : "longueur (m) pour defaut Sous Revetement",
	 "Longueur_mess" : "affichage ecran de la longueur (m) pour defaut Sous Revetement",
	 "CoefDirecteur" : "pente de la fonction affine l = h/profsurlong + a0",
	 "CoefDirecteur_mess" : "affichage ecran de la pente de la fonction affine l = h/profsurlong + a0",
	 "Constante" : "constante de la fonction affine a0",
	 "ModeCalculDecalage" : "type de decalage : normalise (NORMALISE) ou reel (VALEUR)",
	 "DecalageNormalise" : "decalage radial normalise (valeur comprise entre 0. et 1.) pour defaut Sous Revetement",
	 "DecalageNormalise_mess" : "affichage ecran du decalage radial normalise (valeur comprise entre 0. et 1.) pour defaut Sous Revetement",
	 "DecalageRadial" : "decalage radial reel (m) pour defaut decale",
	 "DecalageRadial_mess" : "affichage ecran du decalage radial reel (m) pour defaut decale",
	 "Azimut" : "coordonnee angulaire (degre)",
	 "Azimut_mess" : "affichage ecran de la coordonnee angulaire (degre)",
	 "Altitude" : "altitude (m) : valeur negative",
	 "Altitude_mess" : "affichage ecran de l altitude (m) : valeur negative",
	 "Pointe" : "choix du(des) point(s) du defaut considere {'A','B','BOTH'} pour DSR et DECALE (pour DEBOUCHANT : automatiquement 'B')",
	 "ModeleFluence" : "modele de fluence : {Reglementaire, France, ValeurImposee, SDM, USNRC, REV_2, SDM_Lissage, GrandeDev, GD_Cuve, Cuve1D}",
	 "ZoneActiveCoeur_AltitudeSup" : "cote superieure de la zone active de coeur (ici pour cuve palier 900Mw)",
	 "ZoneActiveCoeur_AltitudeInf" : "cote inferieure de la zone active de coeur (ici pour cuve palier 900Mw)",
	 "FluenceMax" : "fluence maximale assimilee par la cuve (n/cm2)",
	 "KPFrance" : "parametre exponentiel du modele France",
	 "KPUS" : "parametre exponentiel du modele US",
	 "Azimut_0deg" : "fluence a l'azimut 0 (10^19 n/cm)",
	 "Azimut_5deg" : "fluence a l'azimut 5 (10^19 n/cm)",
	 "Azimut_10deg" : "fluence a l'azimut 10 (10^19 n/cm)",
	 "Azimut_15deg" : "fluence a l'azimut 15 (10^19 n/cm)",
	 "Azimut_20deg" : "fluence a l'azimut 20 (10^19 n/cm)",
	 "Azimut_25deg" : "fluence a l'azimut 25 (10^19 n/cm)",
	 "Azimut_30deg" : "fluence a l'azimut 30 (10^19 n/cm)",
	 "Azimut_35deg" : "fluence a l'azimut 35 (10^19 n/cm)",
	 "Azimut_40deg" : "fluence a l'azimut 40 (10^19 n/cm)",
	 "Azimut_45deg" : "fluence a l'azimut 45 (10^19 n/cm)",
	 "TypeIrradiation" : "type irradiation : {RTNDT, FLUENCE}",
	 "RTNDT" : "RTNDT finale (degC)",
	 "ModeleIrradiation" : "modele d irradiation : {HOUSSIN, PERSOZ, LEFEBVRE, USNRCmdb} pour virole et {BRILLAUD,USNRCsoud} pour jointsoude",
	 "TeneurCuivre" : "teneur en cuivre (%)",
	 "TeneurCuivre_mess" : "affichage ecran de la teneur en cuivre (%)",
	 "TeneurNickel" : "teneur en nickel (%)",
	 "TeneurNickel_mess" : "affichage ecran de la teneur en nickel (%)",
	 "TeneurPhosphore" : "teneur en phosphore (%)",
	 "TeneurPhosphore_mess" : "affichage ecran de la teneur en phosphore (%)",
	 "MoyenneRTndt" : "moyenne de la RTNDT initiale : virole C1 de cuve Chinon : mdb=>-17.degC et js=>42.degC (HT-56/05/038 : p.52)",
	 "MoyenneRTndt_mess" : "affichage ecran de la moyenne de la RTNDT initiale",
	 "CoefVariationRTndt" : "coef de variation de la RTNDT initiale",
	 "CoefVariationRTndt_mess" : "affichage ecran du coef de variation de la RTNDT initiale",
	 "EcartTypeRTndt" : "pour modeles USNRCsoud ou USNRCmdb, ecart-type du decalage de RTNDT (°F) (28. pour js et 17. pour mdb)",
	 "EcartTypeRTndt_mess" : "affichage ecran, pour modeles USNRCsoud ou USNRCmdb, ecart-type du decalage de RTNDT (°F) (28. pour js et 17. pour mdb)",
	 "NombreEcartTypeRTndt" : "Nbre d ecart-type par rapport a la moyenne de DRTNDT si analyse PROBABILISTE (en DETERMINISTE, fixer a 2.)",
	 "NombreEcartTypeRTndt_mess" : "affichage ecran du nbre d ecart-type par rapport a la moyenne de DRTNDT si analyse PROBABILISTE",
	 "ModeleTenacite" : "modele de tenacite : {RCC-M, RCC-M_pal, RCC-M_exp, RCC-M_simpl, Houssin_RC, Wallin, REME, ORNL, Frama, WEIB3, WEIB2, LOGWOLF, WEIB-GEN}",
	 "NBRE_CARACTERISTIQUE" : "Nb caracteristique : ORDRE ou QUANTILE",
	 "NbEcartType_MoyKIc" : "Nbre d ecart-type par rapport a la moyenne de KIc si analyse PROBABILISTE (en DETERMINISTE, fixer a -2.)",
	 "NbEcartType_MoyKIc_mess" : "affichage ecran du nbre d ecart-type par rapport a la moyenne de KIc si analyse PROBABILISTE",
	 "PalierDuctile_KIc" : "palier deterministe de K1c (MPa(m^0.5))",
	 "CoefficientVariation_KIc" : "coef de variation de la loi normale de K1c",
	 "Fractile_KIc" : "valeur caracteristique de KIc exprimee en ordre de fractile (%)",
	 "Fractile_KIc_mess" : "affichage ecran de la valeur caracteristique de KIc exprimee en ordre de fractile (%)",
	 "Temperature_KIc100" : "parametre T0 du modele Wallin (degC)",
	 "A1" : "coef des coefs d une WEIBULL generale",
	 "A2" : "",
	 "A3" : "",
	 "B1" : "",
	 "B2" : "",
	 "B3" : "",
	 "C1" : "",
	 "C2" : "",
	 "C3" : "",
	 "AttnCorrBeta" : "Attenuation de la correction plastique : {OUI, NON} ==> uniquement pour DSR ou DECALE",
	 "CorrIrwin" : "Correction plastique IRWIN : {OUI, NON} ==> uniquement pour DEBOUCHANT",
	 "ArretDeFissure" : "prise en compte de l arret de fissure {OUI, NON} (en PROBABILISTE, fixer a NON)",
	 "IncrementTailleFissure" : "increment de la taille de fissure (m)",
	 "IncrementTailleFissure_mess" : "affichage ecran de l increment de la taille de fissure (m)",
	 "NbEcartType_MoyKIa" : "Nbre d ecart-type par rapport a la moyenne de KIa (nb sigma)",
	 "PalierDuctile_KIa" : "palier deterministe de K1a quand modele RCC-M  (MPa(m^0.5))",
	 "CoefficientVariation_KIa" : "coef de variation de la loi normale de K1a",
	 "InstantInitialisation" : "instant initial (s)",
	 "ConditionLimiteThermiqueREV" : "Option 'ENTHALPIE' ou 'CHALEUR'",
	 "TemperatureDeformationNulleREV" : "temperature de deformation nulle (degC)",
	 "TemperaturePourCoefDilatThermREV" : "temperature de definition du coefficient de dilatation thermique (degC)",
	 "CoefficientPoissonREV" : "coefficient de Poisson",
	 "ConditionLimiteThermiqueMDB" : "Option 'ENTHALPIE' ou 'CHALEUR'",
	 "TemperatureDeformationNulleMDB" : "temperature de deformation nulle (degC)",
	 "TemperaturePourCoefDilatThermMDB" : "temperature de definition du coefficient de dilatation thermique (degC)",
	 "CoefficientPoissonMDB" : "coefficient de Poisson",
	 "TypeConditionLimiteThermique" : "Type de condition thermique en paroi interne {TEMP_IMPO,FLUX_REP,ECHANGE,DEBIT,TEMP_FLU,APRP}",
	 "Instant_1" : "Borne inferieure de l intervalle de temps du 2nd palier T1",
	 "Instant_2" : "Borne superieure de l intervalle de temps du 2nd palier T1",
	 "DebitAccumule" : "Debit accumule (en m3/h)",
	 "DebitInjectionSecurite" : "Debit injection de securite (en m3/h)",
	 "TempInjectionSecurite_mess" : "affichage ecran de la temperature injection de securite",
	 "DiametreHydraulique" : "Diametre hydraulique (m)",
	 "DiametreHydraulique_mess" : "affichage ecran du diametre hydraulique (m)",
	 "SectionEspaceAnnulaire" : "Section espace annulaire (m2)",
	 "SectionEspaceAnnulaire_mess" : "affichage ecran de la section espace annulaire (m2)",
	 "HauteurCaracConvectionNaturelle" : "Hauteur caracteristique convection naturelle (m)",
	 "HauteurCaracConvectionNaturelle_mess" : "affichage ecran de la hauteur caracteristique convection naturelle (m)",
	 "CritereConvergenceRelative" : "Critere convergence relative (-)",
	 "CoefficientsVestale" : "Application des coefs de Vestale {OUI;NON}",
	 "VolumeMelange_CREARE" : "Volume de melange CREARE (m3)",
	 "VolumeMelange_CREARE_mess" : "affichage ecran du volume de melange CREARE (m3)",
	 "TemperatureInitiale_CREARE" : "Temperature initiale CREARE (degC)",
	 "TemperatureInitiale_CREARE_mess" : "affichage ecran de la temperature initiale CREARE (degC)",
	 "SurfaceEchange_FluideStructure" : "Surface d'echange fluide/structure (m2)",
	 "SurfaceEchange_FluideStructure_mess" : "affichage ecran de la surface d'echange fluide/structure (m2)",
         }

      # Ce dictionnaire liste la valeur par defaut des variables utilisees dans le script
      self.default = {
         "NiveauImpression" : "1",
	 "FichierDataIn" : "NON",
	 "FichierTempSigma" : "NON",
	 "FichierCSV" : "NON",
	 "FichierCREARE" : "NON",
	 "GrandeurEvaluee" : "FM_KICSURKCP",
	 "IncrementTemporel" : "1",
	 "IncrementMaxTemperature" : "0.1",
	 "IncrementMaxTempsAffichage" : "1000.",
	 "TraitementGeometrie" : "GEOMETRIE",
	 "RayonInterne" : "1.994",
	 "RayonInterne_mess" : "NON",
	 "RayonExterne" : "2.2015",
	 "RayonExterne_mess" : "NON",
	 "EpaisseurRevetement" : "0.0075",
	 "EpaisseurRevetement_mess" : "NON",
	 "LigamentExterneMin" : "0.75",
	 "LigamentExterneMin_mess" : "NON",
	 "NombreNoeudsMaillage" : "300",
	 "TypeInitial" : "DSR",
	 "Orientation" : "LONGITUD",
	 "ProfondeurRadiale" : "0.006",
	 "ProfondeurRadiale_mess" : "NON",
	 "ModeCalculLongueur" : "VALEUR",
	 "Longueur" : "0.060",
	 "Longueur_mess" : "NON",
	 "CoefDirecteur" : "10.",
	 "CoefDirecteur_mess" : "NON",
	 "Constante" : "0.",
	 "ModeCalculDecalage" : "VALEUR",
	 "DecalageNormalise" : "0.1",
	 "DecalageNormalise_mess" : "NON",
	 "DecalageRadial" : "0.",
	 "DecalageRadial_mess" : "NON",
	 "Azimut" : "0.",
	 "Azimut_mess" : "NON",
	 "Altitude" : "-4.",
	 "Altitude_mess" : "NON",
	 "Pointe" : "B",
	 "ModeleFluence" : "Reglementaire",
	 "ZoneActiveCoeur_AltitudeSup" : "-3.536",
	 "ZoneActiveCoeur_AltitudeInf" : "-7.194",
	 "FluenceMax" : "6.5",
	 "KPFrance" : "12.7",
	 "KPUS" : "9.4488",
	 "Azimut_0deg" : "5.8",
	 "Azimut_5deg" : "5.48",
	 "Azimut_10deg" : "4.46",
	 "Azimut_15deg" : "3.41",
	 "Azimut_20deg" : "3.37",
	 "Azimut_25deg" : "3.16",
	 "Azimut_30deg" : "2.74",
	 "Azimut_35deg" : "2.25",
	 "Azimut_40deg" : "1.89",
	 "Azimut_45deg" : "1.78",
	 "TypeIrradiation" : "RTNDT",
	 "RTNDT" : "64.",
	 "ModeleIrradiation" : "HOUSSIN",
	 "TeneurCuivre" : "0.0972",
	 "TeneurCuivre_mess" : "NON",
	 "TeneurNickel" : "0.72",
	 "TeneurNickel_mess" : "NON",
	 "TeneurPhosphore" : "0.00912",
	 "TeneurPhosphore_mess" : "NON",
	 "MoyenneRTndt" : "-12.0",
	 "MoyenneRTndt_mess" : "NON",
	 "CoefVariationRTndt" : "0.1",
	 "CoefVariationRTndt_mess" : "NON",
	 "EcartTypeRTndt" : "-2.",
	 "EcartTypeRTndt_mess" : "NON",
	 "NombreEcartTypeRTndt" : "2.",
	 "NombreEcartTypeRTndt_mess" : "NON",
	 "ModeleTenacite" : "RCC-M",
	 "NBRE_CARACTERISTIQUE" : "QUANTILE",
	 "NbEcartType_MoyKIc" : "-2.",
	 "NbEcartType_MoyKIc_mess" : "NON",
	 "PalierDuctile_KIc" : "195.",
	 "CoefficientVariation_KIc" : "0.15",
	 "Fractile_KIc" : "5.",
	 "Fractile_KIc_mess" : "NON",
	 "Temperature_KIc100" : "-27.",
	 "A1" : "21.263",
	 "A2" : "9.159",
	 "A3" : "0.04057",
	 "B1" : "17.153",
	 "B2" : "55.089",
	 "B3" : "0.0144",
	 "C1" : "4.",
	 "C2" : "0.",
	 "C3" : "0.",
	 "AttnCorrBeta" : "NON",
	 "CorrIrwin" : "NON",
	 "ArretDeFissure" : "NON",
	 "IncrementTailleFissure" : "0.",
	 "IncrementTailleFissure_mess" : "NON",
	 "NbEcartType_MoyKIa" : "0.",
	 "PalierDuctile_KIa" : "0.",
	 "CoefficientVariation_KIa" : "0.",
	 "InstantInitialisation" : "-1.",
	 "ConditionLimiteThermiqueREV" : "CHALEUR",
	 "TemperatureDeformationNulleREV" : "20.",
	 "TemperaturePourCoefDilatThermREV" : "287.",
	 "CoefficientPoissonREV" : "0.3",
	 "ConditionLimiteThermiqueMDB" : "CHALEUR",
	 "TemperatureDeformationNulleMDB" : "20.",
	 "TemperaturePourCoefDilatThermMDB" : "287.",
	 "CoefficientPoissonMDB" : "0.3",
	 "TypeConditionLimiteThermique" : "TEMP_IMPO",
	 "Instant_1" : "21.",
	 "Instant_2" : "45.",
	 "DebitAccumule" : "2.3",
	 "DebitInjectionSecurite" : "0.375",
	 "TempInjectionSecurite_mess" : "NON",
	 "DiametreHydraulique" : "0.3816",
	 "DiametreHydraulique_mess" : "NON",
	 "SectionEspaceAnnulaire" : "0.21712",
	 "SectionEspaceAnnulaire_mess" : "NON",
	 "HauteurCaracConvectionNaturelle" : "6.",
	 "HauteurCaracConvectionNaturelle_mess" : "NON",
	 "CritereConvergenceRelative" : "0.00001",
	 "CoefficientsVestale" : "NON",
	 "VolumeMelange_CREARE" : "14.9",
	 "VolumeMelange_CREARE_mess" : "NON",
	 "TemperatureInitiale_CREARE" : "250.",
	 "TemperatureInitiale_CREARE_mess" : "NON",
	 "SurfaceEchange_FluideStructure" : "0.",
	 "SurfaceEchange_FluideStructure_mess" : "NON",
         }

      # Ce dictionnaire liste la rubrique d'appartenance des variables utilisees dans le script
      self.bloc = {
         "NiveauImpression" : "OPTIONS",
	 "FichierDataIn" : "OPTIONS",
	 "FichierTempSigma" : "OPTIONS",
	 "FichierCSV" : "OPTIONS",
	 "FichierCREARE" : "OPTIONS",
	 "GrandeurEvaluee" : "OPTIONS",
	 "IncrementTemporel" : "OPTIONS",
	 "IncrementMaxTemperature" : "OPTIONS",
	 "IncrementMaxTempsAffichage" : "OPTIONS",
	 "TraitementGeometrie" : "DONNEES DE LA CUVE",
	 "RayonInterne" : "DONNEES DE LA CUVE",
	 "RayonInterne_mess" : "DONNEES DE LA CUVE",
	 "RayonExterne" : "DONNEES DE LA CUVE",
	 "RayonExterne_mess" : "DONNEES DE LA CUVE",
	 "EpaisseurRevetement" : "DONNEES DE LA CUVE",
	 "EpaisseurRevetement_mess" : "DONNEES DE LA CUVE",
	 "LigamentExterneMin" : "DONNEES DE LA CUVE",
	 "LigamentExterneMin_mess" : "DONNEES DE LA CUVE",
	 "NombreNoeudsMaillage" : "DONNEES DE LA CUVE",
	 "TypeInitial" : "CARACTERISTIQUES DU DEFAUT",
	 "Orientation" : "CARACTERISTIQUES DU DEFAUT",
	 "ProfondeurRadiale" : "CARACTERISTIQUES DU DEFAUT",
	 "ProfondeurRadiale_mess" : "CARACTERISTIQUES DU DEFAUT",
	 "ModeCalculLongueur" : "CARACTERISTIQUES DU DEFAUT",
	 "Longueur" : "CARACTERISTIQUES DU DEFAUT",
	 "Longueur_mess" : "CARACTERISTIQUES DU DEFAUT",
	 "CoefDirecteur" : "CARACTERISTIQUES DU DEFAUT",
	 "CoefDirecteur_mess" : "CARACTERISTIQUES DU DEFAUT",
	 "Constante" : "CARACTERISTIQUES DU DEFAUT",
	 "ModeCalculDecalage" : "CARACTERISTIQUES DU DEFAUT",
	 "DecalageNormalise" : "CARACTERISTIQUES DU DEFAUT",
	 "DecalageNormalise_mess" : "CARACTERISTIQUES DU DEFAUT",
	 "DecalageRadial" : "CARACTERISTIQUES DU DEFAUT",
	 "DecalageRadial_mess" : "CARACTERISTIQUES DU DEFAUT",
	 "Azimut" : "CARACTERISTIQUES DU DEFAUT",
	 "Azimut_mess" : "CARACTERISTIQUES DU DEFAUT",
	 "Altitude" : "CARACTERISTIQUES DU DEFAUT",
	 "Altitude_mess" : "CARACTERISTIQUES DU DEFAUT",
	 "Pointe" : "CARACTERISTIQUES DU DEFAUT",
	 "ModeleFluence" : "MODELES",
	 "ZoneActiveCoeur_AltitudeSup" : "MODELES",
	 "ZoneActiveCoeur_AltitudeInf" : "MODELES",
	 "FluenceMax" : "MODELES",
	 "KPFrance" : "MODELES",
	 "KPUS" : "MODELES",
	 "Azimut_0deg" : "MODELES",
	 "Azimut_5deg" : "MODELES",
	 "Azimut_10deg" : "MODELES",
	 "Azimut_15deg" : "MODELES",
	 "Azimut_20deg" : "MODELES",
	 "Azimut_25deg" : "MODELES",
	 "Azimut_30deg" : "MODELES",
	 "Azimut_35deg" : "MODELES",
	 "Azimut_40deg" : "MODELES",
	 "Azimut_45deg" : "MODELES",
	 "TypeIrradiation" : "MODELES",
	 "RTNDT" : "MODELES",
	 "ModeleIrradiation" : "MODELES",
	 "TeneurCuivre" : "MODELES",
	 "TeneurCuivre_mess" : "MODELES",
	 "TeneurNickel" : "MODELES",
	 "TeneurNickel_mess" : "MODELES",
	 "TeneurPhosphore" : "MODELES",
	 "TeneurPhosphore_mess" : "MODELES",
	 "MoyenneRTndt" : "MODELES",
	 "MoyenneRTndt_mess" : "MODELES",
	 "CoefVariationRTndt" : "MODELES",
	 "CoefVariationRTndt_mess" : "MODELES",
	 "EcartTypeRTndt" : "MODELES",
	 "EcartTypeRTndt_mess" : "MODELES",
	 "NombreEcartTypeRTndt" : "MODELES",
	 "NombreEcartTypeRTndt_mess" : "MODELES",
	 "ModeleTenacite" : "MODELES",
	 "NBRE_CARACTERISTIQUE" : "MODELES",
	 "NbEcartType_MoyKIc" : "MODELES",
	 "NbEcartType_MoyKIc_mess" : "MODELES",
	 "PalierDuctile_KIc" : "MODELES",
	 "CoefficientVariation_KIc" : "MODELES",
	 "Fractile_KIc" : "MODELES",
	 "Fractile_KIc_mess" : "MODELES",
	 "Temperature_KIc100" : "MODELES",
	 "A1" : "MODELES",
	 "A2" : "MODELES",
	 "A3" : "MODELES",
	 "B1" : "MODELES",
	 "B2" : "MODELES",
	 "B3" : "MODELES",
	 "C1" : "MODELES",
	 "C2" : "MODELES",
	 "C3" : "MODELES",
	 "AttnCorrBeta" : "MODELES",
	 "CorrIrwin" : "MODELES",
	 "ArretDeFissure" : "MODELES",
	 "IncrementTailleFissure" : "MODELES",
	 "IncrementTailleFissure_mess" : "MODELES",
	 "NbEcartType_MoyKIa" : "MODELES",
	 "PalierDuctile_KIa" : "MODELES",
	 "CoefficientVariation_KIa" : "MODELES",
	 "InstantInitialisation" : "ETAT INITIAL",
	 "ConditionLimiteThermiqueREV" : "CARACTERISTIQUES DU REVETEMENT",
	 "TemperatureDeformationNulleREV" : "CARACTERISTIQUES DU REVETEMENT",
	 "TemperaturePourCoefDilatThermREV" : "CARACTERISTIQUES DU REVETEMENT",
	 "CoefficientPoissonREV" : "CARACTERISTIQUES DU REVETEMENT",
	 "ConditionLimiteThermiqueMDB" : "CARACTERISTIQUES DU MDB",
	 "TemperatureDeformationNulleMDB" : "CARACTERISTIQUES DU MDB",
	 "TemperaturePourCoefDilatThermMDB" : "CARACTERISTIQUES DU MDB",
	 "CoefficientPoissonMDB" : "CARACTERISTIQUES DU MDB",
	 "TypeConditionLimiteThermique" : "TRANSITOIRE",
	 "Instant_1" : "TRANSITOIRE",
	 "Instant_2" : "TRANSITOIRE",
	 "DebitAccumule" : "TRANSITOIRE",
	 "DebitInjectionSecurite" : "TRANSITOIRE",
	 "TempInjectionSecurite_mess" : "TRANSITOIRE",
	 "DiametreHydraulique" : "TRANSITOIRE",
	 "DiametreHydraulique_mess" : "TRANSITOIRE",
	 "SectionEspaceAnnulaire" : "TRANSITOIRE",
	 "SectionEspaceAnnulaire_mess" : "TRANSITOIRE",
	 "HauteurCaracConvectionNaturelle" : "TRANSITOIRE",
	 "HauteurCaracConvectionNaturelle_mess" : "TRANSITOIRE",
	 "CritereConvergenceRelative" : "TRANSITOIRE",
	 "CoefficientsVestale" : "TRANSITOIRE",
	 "VolumeMelange_CREARE" : "TRANSITOIRE",
	 "VolumeMelange_CREARE_mess" : "TRANSITOIRE",
	 "TemperatureInitiale_CREARE" : "TRANSITOIRE",
	 "TemperatureInitiale_CREARE_mess" : "TRANSITOIRE",
	 "SurfaceEchange_FluideStructure" : "TRANSITOIRE",
	 "SurfaceEchange_FluideStructure_mess" : "TRANSITOIRE",
         }

   def gener(self,obj,format='brut'):
      self.text=''
      self.textCuve=''
      self.dico_mot={}
      self.dico_genea={}
      self.text=PythonGenerator.gener(self,obj,format)
      return self.text

   def generMCSIMP(self,obj) :
       self.dico_mot[obj.nom]=obj.valeur
       clef=""
       for i in obj.get_genealogie() :
           clef=clef+"_"+i
       self.dico_genea[clef]=obj.valeur
       s=PythonGenerator.generMCSIMP(self,obj)
       return s

   def writeCuve2DG(self, filename):
      print "je passe dans writeCuve2DG"
      self.genereTexteCuve()
      f = open( filename, 'wb')
      print self.texteCuve
      f.write( self.texteCuve )
      f.close()
      ftmp = open( "/tmp/data_template", 'wb')
      ftmp.write( self.texteCuve )
      ftmp.close()

   def entete(self):
      '''
      Ecrit l'entete du fichier data_template
      '''
      texte  = "############################################################################################"+"\n"
      texte += "#"+"\n"
      texte += "#                OUTIL D'ANALYSE PROBABILISTE DE LA DUREE DE VIE DES CUVES REP"+"\n"
      texte += "#                                     ---------------"+"\n"
      texte += "#                               FICHIER DE MISE EN DONNEES"+"\n"
      texte += "#"+"\n"
      texte += "# SI CALCUL DETERMINISTE :"+"\n"
      texte += "#       - fixer INCRTPS=1, nbectDRTNDT=2., nbectKIc=-2."+"\n"
      texte += "#       - les calculs ne sont possibles qu'en une seule pointe du defaut (POINDEF<>BOTH)"+"\n"
      texte += "# SI CALCUL PROBABILISTE :"+"\n"
      texte += "#       - fixer ARRETFISSURE=NON"+"\n"
      texte += "#"+"\n"
      texte += "############################################################################################"+"\n"
      texte += "#"+"\n"
      return texte

   def rubrique(self, titre):
      '''
      Rubrique 
      '''
      texte  = "#"+"\n"
      texte += "############################################################################################"+"\n"
      texte += "# " + titre + "\n"
      texte += "############################################################################################"+"\n"
      texte += "#"+"\n"
      return texte

   def sousRubrique(self, soustitre, numtitre):
      '''
      Sous-rubrique 
      '''
      texte  = "#"+"\n"
      texte += "# " + numtitre + soustitre + "\n"
      texte += "#==========================================================================================="+"\n"
      texte += "#"+"\n"
      return texte

   def ecritLigne(self, variablelue):
      '''
      Ecrit l'affectation d'une valeur a sa variable, suivie d'un commentaire
      '''
      texte = "%s = %s   # %s\n" % (self.variable[variablelue], str(self.dico_mot[variablelue]), self.comment[variablelue])
      return texte

   def affecteValeurDefaut(self, variablelue):
      '''
      Affecte une valeur par defaut a une variable, suivie d'un commentaire
      '''
      print "Warning ==> Dans la rubrique",self.bloc[variablelue],", valeur par defaut pour ",variablelue," = ",self.default[variablelue]
      texte = "%s = %s   # %s\n" % (self.variable[variablelue], self.default[variablelue], self.comment[variablelue])
      return texte

   def affecteValeur(self, variablelue, valeuraffectee):
      '''
      Affecte une valeur a une variable, suivie d'un commentaire
      '''
      texte = "%s = %s   # %s\n" % (self.variable[variablelue], valeuraffectee, self.comment[variablelue])
      return texte

   def ecritVariable(self, variablelue):
      if self.dico_mot.has_key(variablelue):
         texte = self.ecritLigne(variablelue)
      else :
         texte = self.affecteValeurDefaut(variablelue)
      return texte

   def amontAval(self, amont, aval):
      if str(self.dico_mot[amont])=='Continu':
         if str(self.dico_mot[aval])=='Continu':
            texte = 'CC'+"\n"
	 if str(self.dico_mot[aval])=='Lineaire':
            texte = 'CL'+"\n"
	 if str(self.dico_mot[aval])=='Exclu':
            texte = 'CE'+"\n"
      if str(self.dico_mot[amont])=='Lineaire':
         if str(self.dico_mot[aval])=='Continu':
            texte = 'LC'+"\n"
	 if str(self.dico_mot[aval])=='Lineaire':
            texte = 'LL'+"\n"
	 if str(self.dico_mot[aval])=='Exclu':
            texte = 'LE'+"\n"
      if str(self.dico_mot[amont])=='Exclu':
         if str(self.dico_mot[aval])=='Continu':
            texte = 'EC'+"\n"
	 if str(self.dico_mot[aval])=='Lineaire':
            texte = 'EL'+"\n"
	 if str(self.dico_mot[aval])=='Exclu':
            texte = 'EE'+"\n"
      return texte

   def genereTexteCuve(self):
      self.texteCuve  = ""
      self.texteCuve += self.entete()

      # Rubrique OPTIONS
      self.texteCuve += self.rubrique('OPTIONS')

      self.texteCuve += self.sousRubrique('Impression a l ecran', '')
      if self.dico_mot.has_key('NiveauImpression'):
         if str(self.dico_mot["NiveauImpression"])=='Aucune impression':
            self.texteCuve += self.affecteValeur('NiveauImpression', '0')
         if str(self.dico_mot["NiveauImpression"])=='Temps total':
            self.texteCuve += self.affecteValeur('NiveauImpression', '1')
         if str(self.dico_mot["NiveauImpression"])=='Temps intermediaires':
            self.texteCuve += self.affecteValeur('NiveauImpression', '2')

      self.texteCuve += self.sousRubrique('Generation de fichiers', '')
      self.texteCuve += self.ecritVariable('FichierDataIn')
      self.texteCuve += self.ecritVariable('FichierTempSigma')
      self.texteCuve += self.ecritVariable('FichierCSV')
      self.texteCuve += self.ecritVariable('FichierCREARE')

      self.texteCuve += self.sousRubrique('Grandeur evaluee', '')
      if self.dico_mot.has_key('GrandeurEvaluee'):
         if str(self.dico_mot["GrandeurEvaluee"])=='Facteur de marge KIc/KCP':
            self.texteCuve += self.affecteValeur('GrandeurEvaluee', 'FM_KICSURKCP')
         if str(self.dico_mot["GrandeurEvaluee"])=='Marge KIc-KI':
            self.texteCuve += self.affecteValeur('GrandeurEvaluee', 'MARGE_KI')
         if str(self.dico_mot["GrandeurEvaluee"])=='Marge KIc-KCP':
            self.texteCuve += self.affecteValeur('GrandeurEvaluee', 'MARGE_KCP')

      self.texteCuve += self.sousRubrique('Divers', '')
      self.texteCuve += self.ecritVariable('IncrementTemporel')
      self.texteCuve += self.ecritVariable('IncrementMaxTemperature')
      self.texteCuve += self.ecritVariable('IncrementMaxTempsAffichage')
      if self.dico_mot.has_key('ListeInstants'):
         self.texteCuve += "# liste des instants pour ecriture des resultats (s)"+"\n"
         self.imprime(1,(self.dico_mot["ListeInstants"]))
      else :
         print "Warning ==> Dans la rubrique OPTIONS, fournir ListeInstants."
         self.texteCuve += "# liste des instants pour ecriture des resultats (s)"+"\n"
         self.texteCuve += "  0.\n"
         self.texteCuve += "  1.\n"


      # Rubrique DONNEES DE LA CUVE
      self.texteCuve += self.rubrique('DONNEES DE LA CUVE')
      if self.dico_mot.has_key('TraitementGeometrie'):
         if str(self.dico_mot["TraitementGeometrie"])=='Topologie':
            self.texteCuve += self.affecteValeur('TraitementGeometrie', 'GEOMETRIE')
            self.texteCuve+="# - si MAILLAGE, fournir NBNO et liste des abscisses (m)"+"\n"
            self.texteCuve+="# - si GEOMETRIE, fournir (RINT, RINT_MESSAGE),"+"\n"
            self.texteCuve+="#                         (REXT, REXT_MESSAGE),"+"\n"
            self.texteCuve+="#                         (LREV, LREV_MESSAGE),"+"\n"
            self.texteCuve+="#                         (LIGMIN, LIGMIN_MESSAGE),"+"\n"
            self.texteCuve+="#                         NBNO"+"\n"
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('RayonInterne')
            self.texteCuve += self.ecritVariable('RayonInterne_mess')
            self.texteCuve += self.ecritVariable('RayonExterne')
            self.texteCuve += self.ecritVariable('RayonExterne_mess')
            self.texteCuve += self.ecritVariable('EpaisseurRevetement')
            self.texteCuve += self.ecritVariable('EpaisseurRevetement_mess')
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('LigamentExterneMin')
            self.texteCuve += self.ecritVariable('LigamentExterneMin_mess')
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('NombreNoeudsMaillage')
         if str(self.dico_mot["TraitementGeometrie"])=='Maillage':
            self.texteCuve += self.affecteValeur('TraitementGeometrie', 'MAILLAGE')
            self.texteCuve+="# - si MAILLAGE, fournir NBNO et liste des abscisses (m)"+"\n"
            self.texteCuve+="# - si GEOMETRIE, fournir (RINT, RINT_MESSAGE),"+"\n"
            self.texteCuve+="#                         (REXT, REXT_MESSAGE),"+"\n"
            self.texteCuve+="#                         (LREV, LREV_MESSAGE),"+"\n"
            self.texteCuve+="#                         (LIGMIN, LIGMIN_MESSAGE),"+"\n"
            self.texteCuve+="#                         NBNO"+"\n"
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('NombreNoeudsMaillage')
            self.imprime(1,(self.dico_mot["ListeAbscisses"]))
      else :
         self.texteCuve += self.affecteValeurDefaut('TraitementGeometrie')
         self.texteCuve+="# - si MAILLAGE, fournir NBNO et liste des abscisses (m)"+"\n"
         self.texteCuve+="# - si GEOMETRIE, fournir (RINT, RINT_MESSAGE),"+"\n"
         self.texteCuve+="#                         (REXT, REXT_MESSAGE),"+"\n"
         self.texteCuve+="#                         (LREV, LREV_MESSAGE),"+"\n"
         self.texteCuve+="#                         (LIGMIN, LIGMIN_MESSAGE),"+"\n"
         self.texteCuve+="#                         NBNO"+"\n"
         self.texteCuve+="#"+"\n"
         self.texteCuve += self.affecteValeurDefaut('RayonInterne')
         self.texteCuve += self.affecteValeurDefaut('RayonInterne_mess')
         self.texteCuve += self.affecteValeurDefaut('RayonExterne')
         self.texteCuve += self.affecteValeurDefaut('RayonExterne_mess')
         self.texteCuve += self.affecteValeurDefaut('EpaisseurRevetement')
         self.texteCuve += self.affecteValeurDefaut('EpaisseurRevetement_mess')
         self.texteCuve+="#"+"\n"
         self.texteCuve += self.affecteValeurDefaut('LigamentExterneMin')
         self.texteCuve += self.affecteValeurDefaut('LigamentExterneMin_mess')
         self.texteCuve+="#"+"\n"
         self.texteCuve += self.affecteValeurDefaut('NombreNoeudsMaillage')


      # Rubrique CARACTERISTIQUES DU DEFAUT
      self.texteCuve += self.rubrique('CARACTERISTIQUES DU DEFAUT')

      if self.dico_mot.has_key('TypeInitial'):
         if str(self.dico_mot["TypeInitial"])=='Defaut Sous Revetement':
            self.texteCuve += self.affecteValeur('TypeInitial', 'DSR')
         if str(self.dico_mot["TypeInitial"])=='Defaut Decale':
            self.texteCuve += self.affecteValeur('TypeInitial', 'DECALE')
         if str(self.dico_mot["TypeInitial"])=='Defaut Debouchant':
            self.texteCuve += self.affecteValeur('TypeInitial', 'DEBOUCHANT')
      else :
         self.texteCuve += self.affecteValeurDefaut('TypeInitial')

      self.texteCuve+="# Fournir ORIEDEF, (PROFDEF, PROFDEF_MESSAGE)"+"\n"
      self.texteCuve+="# - Si DSR, fournir OPTLONG, (LONGDEF,LONGDEF_MESSAGE) ou (PROFSURLONG,PROFSURLONG_MESSAGE,LONGCONST)"+"\n"
      self.texteCuve+="# - Si DECALE, fournir OPTLONG, (LONGDEF,LONGDEF_MESSAGE) ou (PROFSURLONG,PROFSURLONG_MESSAGE,LONGCONST), DECATYP, (DECANOR,DECANOR_MESSAGE) ou (DECADEF,DECADEF_MESSAGE)"+"\n"
      self.texteCuve+="# - Si DEBOUCHANT, fournir IRWIN"+"\n"
      self.texteCuve+="# Fournir (ANGLDEF, ANGLDEF_MESSAGE), (ALTIDEF, ALTIDEF_MESSAGE)"+"\n"
      self.texteCuve+="# - Si DSR ou DECALE, fournir POINDEF"+"\n"
      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Remarque :"+"\n"
      self.texteCuve+="# - si DSR ou DECALE, dans la rubrique 'Modele de tenacite', fournir ATTNCORRBETA (ne pas fournir CORRIRWIN)"+"\n"
      self.texteCuve+="# - si DEBOUCHANT,    dans la rubrique 'Modele de tenacite', fournir CORRIRWIN    (ne pas fournir ATTNCORRBETA)"+"\n"

      self.texteCuve+="#"+"\n"

      if self.dico_mot.has_key('Orientation'):
         if str(self.dico_mot["Orientation"])=='Longitudinale':
            self.texteCuve += self.affecteValeur('Orientation', 'LONGITUD')
         if str(self.dico_mot["Orientation"])=='Circonferentielle':
            self.texteCuve += self.affecteValeur('Orientation', 'CIRCONF')
      else :
         self.texteCuve += self.affecteValeurDefaut('Orientation')
	 
      self.texteCuve+="#"+"\n"
      self.texteCuve += self.ecritVariable('ProfondeurRadiale')
      self.texteCuve += self.ecritVariable('ProfondeurRadiale_mess')

      self.texteCuve+="#"+"\n"
      if self.dico_mot.has_key('ModeCalculLongueur'):
         if str(self.dico_mot["ModeCalculLongueur"])=='Valeur':
            self.texteCuve += self.affecteValeur('ModeCalculLongueur', 'VALEUR')
            self.texteCuve+="# - Si VALEUR,    fournir (LONGDEF, LONGDEF_MESSAGE)"+"\n"
            self.texteCuve+="# - Si FCTAFFINE, fournir (PROFSURLONG, PROFSURLONG_MESSAGE) et LONGCONST : LONGDEF=PROFDEF/PROFSURLONG + LONGCONST"+"\n"
            self.texteCuve += self.ecritVariable('Longueur')
            self.texteCuve += self.ecritVariable('Longueur_mess')
         if str(self.dico_mot["ModeCalculLongueur"])=='Fonction affine de la profondeur':
            self.texteCuve += self.affecteValeur('ModeCalculLongueur', 'FCTAFFINE')
            self.texteCuve+="# - Si VALEUR,    fournir (LONGDEF, LONGDEF_MESSAGE)"+"\n"
            self.texteCuve+="# - Si FCTAFFINE, fournir (PROFSURLONG, PROFSURLONG_MESSAGE) et LONGCONST : LONGDEF=PROFDEF/PROFSURLONG + LONGCONST"+"\n"
            self.texteCuve += self.ecritVariable('CoefDirecteur')
            self.texteCuve += self.ecritVariable('CoefDirecteur_mess')
            self.texteCuve += self.ecritVariable('Constante')
      else :
         self.texteCuve += self.affecteValeurDefaut('ModeCalculLongueur')
         self.texteCuve+="# - Si VALEUR,    fournir (LONGDEF, LONGDEF_MESSAGE)"+"\n"
         self.texteCuve+="# - Si FCTAFFINE, fournir (PROFSURLONG, PROFSURLONG_MESSAGE) et LONGCONST : LONGDEF=PROFDEF/PROFSURLONG + LONGCONST"+"\n"
         self.texteCuve += self.affecteValeurDefaut('Longueur')
         self.texteCuve += self.affecteValeurDefaut('Longueur_mess')

      if self.dico_mot.has_key('TypeInitial'):
         if str(self.dico_mot["TypeInitial"])!='Defaut Sous Revetement':
            self.texteCuve+="#"+"\n"
            if self.dico_mot.has_key('ModeCalculDecalage'):
               if str(self.dico_mot["ModeCalculDecalage"])=='Valeur normalisee':
                  self.texteCuve += self.affecteValeur('ModeCalculDecalage', 'NORMALISE')
                  self.texteCuve+="# - Si NORMALISE, fournir (DECANOR, DECANOR_MESSAGE)"+"\n"
                  self.texteCuve+="# - Si VALEUR,    fournir (DECADEF, DECADEF_MESSAGE)"+"\n"
                  self.texteCuve += self.ecritVariable('DecalageNormalise')
                  self.texteCuve += self.ecritVariable('DecalageNormalise_mess')
               if str(self.dico_mot["ModeCalculDecalage"])=='Valeur':
                  self.texteCuve += self.affecteValeur('ModeCalculDecalage', 'VALEUR')
                  self.texteCuve+="# - Si NORMALISE, fournir (DECANOR, DECANOR_MESSAGE)"+"\n"
                  self.texteCuve+="# - Si VALEUR,    fournir (DECADEF, DECADEF_MESSAGE)"+"\n"
                  self.texteCuve += self.ecritVariable('DecalageRadial')
                  self.texteCuve += self.ecritVariable('DecalageRadial_mess')
            else :
               self.texteCuve += self.affecteValeurDefaut('ModeCalculDecalage')
               self.texteCuve+="# - Si NORMALISE, fournir (DECANOR, DECANOR_MESSAGE)"+"\n"
               self.texteCuve+="# - Si VALEUR, fournir (DECADEF, DECADEF_MESSAGE)"+"\n"
               self.texteCuve += self.affecteValeurDefaut('DecalageRadial')
               self.texteCuve += self.affecteValeurDefaut('DecalageRadial_mess')

      self.texteCuve+="#"+"\n"
      self.texteCuve += self.ecritVariable('Azimut')
      self.texteCuve += self.ecritVariable('Azimut_mess')
      self.texteCuve+="#"+"\n"
      self.texteCuve += self.ecritVariable('Altitude')
      self.texteCuve += self.ecritVariable('Altitude_mess')
      self.texteCuve+="#"+"\n"
      if self.dico_mot.has_key('Pointe'):
         if str(self.dico_mot["Pointe"])=='A':
            self.texteCuve += self.affecteValeur('Pointe', 'A')
         if str(self.dico_mot["Pointe"])=='B':
            self.texteCuve += self.affecteValeur('Pointe', 'B')
         if str(self.dico_mot["Pointe"])=='A et B':
            self.texteCuve += self.affecteValeur('Pointe', 'BOTH')
      else :
         self.texteCuve += self.affecteValeurDefaut('Pointe')

      # Rubrique MODELES FLUENCE, IRRADIATION, TENACITE
      self.texteCuve += self.rubrique('MODELES FLUENCE, IRRADIATION, TENACITE')
      self.texteCuve += self.sousRubrique('Modele d attenuation de la fluence dans l epaisseur','A.')

      if self.dico_mot.has_key('ModeleFluence'):
         if str(self.dico_mot["ModeleFluence"])=='Exponentiel sans revetement k=9.7 (Reglementaire)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'Reglementaire')
         if str(self.dico_mot["ModeleFluence"])=='Exponentiel sans revetement k=12.7 (France)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'France')
         if str(self.dico_mot["ModeleFluence"])=='Exponentiel sans revetement k=0. (ValeurImposee)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'ValeurImposee')
         if str(self.dico_mot["ModeleFluence"])=='Donnees francaises du palier CPY (SDM)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'SDM')
         if str(self.dico_mot["ModeleFluence"])=='Regulatory Guide 1.99 rev 2 (USNRC)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'USNRC')
         if str(self.dico_mot["ModeleFluence"])=='Dossier 900 MWe AP9701 rev 2 (REV_2)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'REV_2')
         if str(self.dico_mot["ModeleFluence"])=='Lissage du modele ajuste (SDM_Lissage)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'SDM_Lissage')
         if str(self.dico_mot["ModeleFluence"])=='Donnees francaises du palier CPY ajustees par secteur angulaire (GrandeDev)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'GrandeDev')
         if str(self.dico_mot["ModeleFluence"])=='Grand developpement (GD_Cuve)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'GD_Cuve')
         if str(self.dico_mot["ModeleFluence"])=='Exponentiel sans revetement k=9.7 (Reglementaire CUVE1D)':
            self.texteCuve += self.affecteValeur('ModeleFluence', 'Cuve1D')
      else :
         self.texteCuve += self.affecteValeurDefaut('ModeleFluence')

      self.texteCuve+="# - si France,          fournir KPFRANCE"+"\n"
      self.texteCuve+="# - si USNRC,           fournir KPUS"+"\n"
      self.texteCuve+="# - si modele GD_Cuve,  fournir COEFFLUENCE1, COEFFLUENCE2, ..., COEFFLUENCE9, COEFFLUENCE10"+"\n"
      self.texteCuve+="#"+"\n"

      self.texteCuve += self.ecritVariable('ZoneActiveCoeur_AltitudeSup')
      self.texteCuve += self.ecritVariable('ZoneActiveCoeur_AltitudeInf')
      self.texteCuve += self.ecritVariable('FluenceMax')
      if self.dico_mot.has_key('ModeleFluence'):
         if str(self.dico_mot["ModeleFluence"])=='Exponentiel sans revetement k=12.7 (France)':
            self.texteCuve += self.ecritVariable('KPFrance')
         if str(self.dico_mot["ModeleFluence"])=='Regulatory Guide 1.99 rev 2 (USNRC)':
            self.texteCuve += self.ecritVariable('KPUS')
         if str(self.dico_mot["ModeleFluence"])=='Grand developpement (GD_Cuve)':
            self.texteCuve += self.ecritVariable('Azimut_0deg')
            self.texteCuve += self.ecritVariable('Azimut_5deg')
            self.texteCuve += self.ecritVariable('Azimut_10deg')
            self.texteCuve += self.ecritVariable('Azimut_15deg')
            self.texteCuve += self.ecritVariable('Azimut_20deg')
            self.texteCuve += self.ecritVariable('Azimut_25deg')
            self.texteCuve += self.ecritVariable('Azimut_30deg')
            self.texteCuve += self.ecritVariable('Azimut_35deg')
            self.texteCuve += self.ecritVariable('Azimut_40deg')
            self.texteCuve += self.ecritVariable('Azimut_45deg')

      self.texteCuve += self.sousRubrique('Irradiation','B.')

      if self.dico_mot.has_key('TypeIrradiation'):

         if str(self.dico_mot["TypeIrradiation"])=='RTndt de la cuve a l instant de l analyse':
            self.texteCuve += self.affecteValeur('TypeIrradiation', 'RTNDT')
            self.texteCuve+="# - si RTNDT, fournir RTNDT"+"\n"
            self.texteCuve+="# - si FLUENCE, fournir MODELIRR, et autres parametres selon MODELIRR (voir ci-dessous)"+"\n"
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('RTNDT')

         if str(self.dico_mot["TypeIrradiation"])=='Modele d irradiation':
            self.texteCuve += self.affecteValeur('TypeIrradiation', 'FLUENCE')
            self.texteCuve+="# - si RTNDT, fournir RTNDT"+"\n"
            self.texteCuve+="# - si FLUENCE, fournir MODELIRR, et autres parametres selon MODELIRR (voir ci-dessous)"+"\n"
            self.texteCuve+="#"+"\n"
            if self.dico_mot.has_key('ModeleIrradiation'):
               if str(self.dico_mot["ModeleIrradiation"])=='Metal de Base : formule de FIM/FIS Houssin':
                  self.texteCuve += self.affecteValeur('ModeleIrradiation', 'HOUSSIN')
               if str(self.dico_mot["ModeleIrradiation"])=='Metal de Base : formule de FIM/FIS Persoz':
                  self.texteCuve += self.affecteValeur('ModeleIrradiation', 'PERSOZ')
               if str(self.dico_mot["ModeleIrradiation"])=='Metal de Base : formule de FIM/FIS Lefebvre':
                  self.texteCuve += self.affecteValeur('ModeleIrradiation', 'LEFEBVRE')
               if str(self.dico_mot["ModeleIrradiation"])=='Metal de Base : Regulatory Guide 1.00 rev 2':
                  self.texteCuve += self.affecteValeur('ModeleIrradiation', 'USNRCmdb')
               if str(self.dico_mot["ModeleIrradiation"])=='Joint Soude : formulation de FIM/FIS Brillaud':
                  self.texteCuve += self.affecteValeur('ModeleIrradiation', 'BRILLAUD')
               if str(self.dico_mot["ModeleIrradiation"])=='Joint Soude : Regulatory Guide 1.00 rev 2':
                  self.texteCuve += self.affecteValeur('ModeleIrradiation', 'USNRCsoud')
            else :
              self.texteCuve += self.affecteValeurDefaut('ModeleIrradiation')
            self.texteCuve+="# - pour tout modele,                       fournir (CU, CU_MESSAGE),"+"\n"
            self.texteCuve+="#                                                   (NI, NI_MESSAGE),"+"\n"
            self.texteCuve+="# - si HOUSSIN, PERSOZ, LEFEBVRE, BRILLAUD, fournir (P, P_MESSAGE)"+"\n"
            self.texteCuve+="# - pour tout modele,                       fournir (RTimoy, RTimoy_MESSAGE),"+"\n"
            self.texteCuve+="# - si USNRCsoud ou USNRCmdb,               fournir (RTicov, RTicov_MESSAGE)"+"\n"
            self.texteCuve+="#                                                   (USectDRT, USectDRT_MESSAGE)"+"\n"
            self.texteCuve+="# - pour tout modele,                       fournir (nbectDRTNDT, nbectDRTNDT_MESSAGE)"+"\n"
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('TeneurCuivre')
            self.texteCuve += self.ecritVariable('TeneurCuivre_mess')
            self.texteCuve += self.ecritVariable('TeneurNickel')
            self.texteCuve += self.ecritVariable('TeneurNickel_mess')
            if str(self.dico_mot["ModeleIrradiation"])=='Metal de Base : formule de FIM/FIS Houssin' or str(self.dico_mot["ModeleIrradiation"])=='Metal de Base : formule de FIM/FIS Persoz' or str(self.dico_mot["ModeleIrradiation"])=='Metal de Base : formule de FIM/FIS Lefebvre' or str(self.dico_mot["ModeleIrradiation"])=='Joint Soude : formulation de FIM/FIS Brillaud':
               self.texteCuve += self.ecritVariable('TeneurPhosphore')
               self.texteCuve += self.ecritVariable('TeneurPhosphore_mess')
            self.texteCuve += self.ecritVariable('MoyenneRTndt')
            self.texteCuve += self.ecritVariable('MoyenneRTndt_mess')
            if str(self.dico_mot["ModeleIrradiation"])=='Metal de Base : Regulatory Guide 1.00 rev 2' or str(self.dico_mot["ModeleIrradiation"])=='Joint Soude : Regulatory Guide 1.00 rev 2':
               self.texteCuve += self.ecritVariable('CoefVariationRTndt')
               self.texteCuve += self.ecritVariable('CoefVariationRTndt_mess')
               self.texteCuve += self.ecritVariable('EcartTypeRTndt')
               self.texteCuve += self.ecritVariable('EcartTypeRTndt_mess')
            self.texteCuve += self.ecritVariable('NombreEcartTypeRTndt')
            self.texteCuve += self.ecritVariable('NombreEcartTypeRTndt_mess')
      else :
         self.texteCuve += self.affecteValeurDefaut('TypeIrradiation')
         self.texteCuve+="# - si RTNDT, fournir RTNDT"+"\n"
         self.texteCuve+="# - si FLUENCE, fournir MODELIRR, et autres parametres selon MODELIRR (voir ci-dessous)"+"\n"
         self.texteCuve+="#"+"\n"
         self.texteCuve += self.affecteValeurDefaut('RTNDT')

      self.texteCuve += self.sousRubrique('Modele de tenacite','C.')
      self.texteCuve+="# tenacite d amorcage"+"\n"

      if self.dico_mot.has_key('ModeleTenacite'):
         if str(self.dico_mot["ModeleTenacite"])=='RCC-M/ASME coefficient=2':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'RCC-M')
         if str(self.dico_mot["ModeleTenacite"])=='RCC-M/ASME coefficient=2 CUVE1D':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'RCC-M_simpl')
         if str(self.dico_mot["ModeleTenacite"])=='RCC-M/ASME coefficient=2.33 (Houssin)':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'Houssin_RC')
         if str(self.dico_mot["ModeleTenacite"])=='RCC-M/ASME avec KI=KIpalier':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'RCC-M_pal')
         if str(self.dico_mot["ModeleTenacite"])=='RCC-M/ASME avec KI~exponentiel':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'RCC-M_exp')
         if str(self.dico_mot["ModeleTenacite"])=='Weibull basee sur la master cuve':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'Wallin')
         if str(self.dico_mot["ModeleTenacite"])=='Weibull basee sur la master cuve (REME)':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'REME')
         if str(self.dico_mot["ModeleTenacite"])=='Weibull n\xb01 (etude ORNL)':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'ORNL')
         if str(self.dico_mot["ModeleTenacite"])=='Weibull n\xb02':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'WEIB2')
         if str(self.dico_mot["ModeleTenacite"])=='Weibull n\xb03':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'WEIB3')
         if str(self.dico_mot["ModeleTenacite"])=='Weibull generalisee':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'WEIB-GEN')
         if str(self.dico_mot["ModeleTenacite"])=='Exponentielle n\xb01 (Frama)':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'Frama')
         if str(self.dico_mot["ModeleTenacite"])=='Exponentielle n\xb02 (LOGWOLF)':
            self.texteCuve += self.affecteValeur('ModeleTenacite', 'LOGWOLF')
      else :
         self.texteCuve += self.affecteValeurDefaut('ModeleTenacite')
      self.texteCuve+="# - si RCC-M, RCC-M_pal, Houssin_RC, fournir (nbectKIc, nbectKIc_MESSAGE), KICPAL, KICCDV"+"\n"
      self.texteCuve+="# - si RCC-M_exp,                    fournir (nbectKIc, nbectKIc_MESSAGE), KICCDV"+"\n"
      self.texteCuve+="# - si RCC-M_simpl,                  ne rien fournir"+"\n"
      self.texteCuve+="# - si Frama, LOGWOLF,               fournir (nbectKIc, nbectKIc_MESSAGE)"+"\n"
      self.texteCuve+="# - si REME, ORNL, WEIB3, WEIB2,     fournir NBCARAC, puis (nbectKIc, nbectKIc_MESSAGE) ou (fractKIc, fractKIc_MESSAGE) selon valeur de NBCARAC"+"\n"
      self.texteCuve+="# - si Wallin,                       fournir NBCARAC, puis (nbectKIc, nbectKIc_MESSAGE) ou (fractKIc, fractKIc_MESSAGE) selon valeur de NBCARAC,"+"\n"
      self.texteCuve+="#                                                     puis T0WALLIN"+"\n"
      self.texteCuve+="# - si WEIB-GEN,                     fournir NBCARAC, puis (nbectKIc, nbectKIc_MESSAGE) ou (fractKIc, fractKIc_MESSAGE) selon valeur de NBCARAC,"+"\n"
      self.texteCuve+="#                                                     puis A1, A2, A3, B1, B2, B3, C1, C2, C3"+"\n"
      self.texteCuve+="#   loi de Weibull P(K<x) = 1 - exp{-[ (x-a(T)) / b(T) ]^c(T) }"+"\n"
      self.texteCuve+="#   avec        a(T) = A1 + A2*exp[A3*(T-RTNDT)]"+"\n"
      self.texteCuve+="#               b(T) = B1 + B2*exp[B3*(T-RTNDT)]"+"\n"
      self.texteCuve+="#               c(T) = C1 + C2*exp[C3*(T-RTNDT)]"+"\n"
      self.texteCuve+="#"+"\n"
      if self.dico_mot.has_key('ModeleTenacite'):
         if str(self.dico_mot["ModeleTenacite"])=='Weibull basee sur la master cuve' or str(self.dico_mot["ModeleTenacite"])=='Weibull n\xb01 (etude ORNL)' or str(self.dico_mot["ModeleTenacite"])=='Weibull n\xb03' or str(self.dico_mot["ModeleTenacite"])=='Weibull n\xb02' :
            self.texteCuve += self.ecritVariable('NBRE_CARACTERISTIQUE')
            self.texteCuve+="# - Si CARAC = QUANTILE, fournir (nbectKIc, nbectKIc_MESSAGE)"+"\n"
            self.texteCuve+="# - Si CARAC = ORDRE,    fournir (fractKIc, fractKIc_MESSAGE)"+"\n"

         if str(self.dico_mot["ModeleTenacite"])=='RCC-M/ASME coefficient=2' or str(self.dico_mot["ModeleTenacite"])=='RCC-M/ASME avec KI=KIpalier' or str(self.dico_mot["ModeleTenacite"])=='RCC-M/ASME coefficient=2.33 (Houssin)' :
            self.texteCuve += self.ecritVariable('NbEcartType_MoyKIc')
            self.texteCuve += self.ecritVariable('NbEcartType_MoyKIc_mess')
            self.texteCuve += self.ecritVariable('PalierDuctile_KIc')
            self.texteCuve += self.ecritVariable('CoefficientVariation_KIc')

         if str(self.dico_mot["ModeleTenacite"])=='Exponentielle n\xb01 (Frama)' or str(self.dico_mot["ModeleTenacite"])=='Exponentielle n\xb02 (LOGWOLF)' :
            self.texteCuve += self.ecritVariable('NbEcartType_MoyKIc')
            self.texteCuve += self.ecritVariable('NbEcartType_MoyKIc_mess')

         if str(self.dico_mot["ModeleTenacite"])=='Weibull basee sur la master cuve (REME)' or str(self.dico_mot["ModeleTenacite"])=='Weibull n\xb01 (etude ORNL)' or str(self.dico_mot["ModeleTenacite"])=='Weibull n\xb03' or str(self.dico_mot["ModeleTenacite"])=='Weibull n\xb02' or str(self.dico_mot["ModeleTenacite"])=='Weibull basee sur la master cuve' or str(self.dico_mot["ModeleTenacite"])=='Weibull generalisee':
            if str(self.dico_mot["NBRE_CARACTERISTIQUE"])=='QUANTILE' :
               self.texteCuve += self.ecritVariable('NbEcartType_MoyKIc')
               self.texteCuve += self.ecritVariable('NbEcartType_MoyKIc_mess')
            if str(self.dico_mot["NBRE_CARACTERISTIQUE"])=='ORDRE' :
               self.texteCuve += self.ecritVariable('Fractile_KIc')
               self.texteCuve += self.ecritVariable('Fractile_KIc_mess')

            if str(self.dico_mot["ModeleTenacite"])=='Weibull basee sur la master cuve' :
               self.texteCuve += self.ecritVariable('Temperature_KIc100')

            if str(self.dico_mot["ModeleTenacite"])=='Weibull generalisee' :
               self.texteCuve += self.ecritVariable('A1')
               self.texteCuve += self.ecritVariable('A2')
               self.texteCuve += self.ecritVariable('A3')
               self.texteCuve += self.ecritVariable('B1')
               self.texteCuve += self.ecritVariable('B2')
               self.texteCuve += self.ecritVariable('B3')
               self.texteCuve += self.ecritVariable('C1')
               self.texteCuve += self.ecritVariable('C2')
               self.texteCuve += self.ecritVariable('C3')
      else :
         self.texteCuve += self.affecteValeurDefaut('NbEcartType_MoyKIc')
         self.texteCuve += self.affecteValeurDefaut('NbEcartType_MoyKIc_mess')
         self.texteCuve += self.affecteValeurDefaut('PalierDuctile_KIc')
         self.texteCuve += self.affecteValeurDefaut('CoefficientVariation_KIc')

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Correction plastique"+"\n"

      if self.dico_mot.has_key('CorrectionPlastique'):
         if str(self.dico_mot["CorrectionPlastique"])=='Correction plastique BETA (pour DSR et defaut decale)':
            self.texteCuve += self.affecteValeur('AttnCorrBeta','NON')
         if str(self.dico_mot["CorrectionPlastique"])=='Correction plastique BETA attenuee (pour DSR et defaut decale)':
            self.texteCuve += self.affecteValeur('AttnCorrBeta','OUI')
         if str(self.dico_mot["CorrectionPlastique"])=='Correction plastique IRWIN (pour defaut debouchant)':
            self.texteCuve += self.affecteValeur('CorrIrwin','OUI')
      else :
         self.texteCuve += self.affecteValeurDefaut('AttnCorrBeta')

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Prise en compte de l'arret de fissure si DETERMINISTE"+"\n"

      self.texteCuve += self.ecritVariable('ArretDeFissure')
      self.texteCuve+="# - si ARRETFISSURE=OUI, fournir (INCRDEF, INCRDEF_MESSAGE), nbectKIa, KIAPAL, KIACDV"+"\n"
      if self.dico_mot.has_key('ArretDeFissure'):
         if str(self.dico_mot["ArretDeFissure"])=='OUI':
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('IncrementTailleFissure')
            self.texteCuve += self.ecritVariable('IncrementTailleFissure_mess')
            self.texteCuve+="#"+"\n"
            self.texteCuve+="# Parametres pour le calcul de la tenacite a l arret"+"\n"
            self.texteCuve += self.ecritVariable('NbEcartType_MoyKIa')
            self.texteCuve += self.ecritVariable('PalierDuctile_KIa')
            self.texteCuve += self.ecritVariable('CoefficientVariation_KIa')

      # Rubrique Etat initial
      self.texteCuve += self.rubrique('ETAT INITIAL')

      self.texteCuve+="# Profil radial de la temperature initiale dans la cuve"+"\n"
      self.texteCuve+="# abscisse (m) / temp initiale dans la cuve"+"\n"
      self.texteCuve+="# Prolongation aux frontieres amont et aval: C = constant / E = exclu / L = lineaire"+"\n"
      if self.dico_mot.has_key('ProfilRadial_TemperatureInitiale'):
         self.imprime(2,(self.dico_mot["ProfilRadial_TemperatureInitiale"]))
         self.texteCuve += self.amontAval('Amont_TemperatureInitiale','Aval_TemperatureInitiale')
      else :
         self.texteCuve+="    1.9940    287."+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Profils radiaux des contraintes residuelles dans la cuve"+"\n"
      self.texteCuve+="# abscisse (m) / sigma rr / sigma tt / sigma zz"+"\n"
      self.texteCuve+="# Prolongation aux frontieres amont et aval: C = constant / E = exclu / L = lineaire"+"\n"
      if self.dico_mot.has_key('ProfilRadial_ContraintesInitiales'):
         self.imprime(4,(self.dico_mot["ProfilRadial_ContraintesInitiales"]))
         self.texteCuve += self.amontAval('Amont_ContraintesInitiales','Aval_ContraintesInitiales')
      else :
         self.texteCuve+="1.994     0. 0.  0."+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Instant initial"+"\n"
      self.texteCuve += self.ecritVariable('InstantInitialisation')

      # Rubrique CARACTERISTIQUES DU REVETEMENT
      self.texteCuve += self.rubrique('CARACTERISTIQUES DU REVETEMENT')

      self.texteCuve += self.ecritVariable('ConditionLimiteThermiqueREV')
      self.texteCuve+="# - si CHALEUR,   fournir Temperature (degC) / chaleur volumique (J/kg/K)"+"\n"
      self.texteCuve+="# - si ENTHALPIE, fournir Temperature (degC) / enthalpie (J/kg)"+"\n"
      self.texteCuve+="# Finir chacune des listes par la prolongation aux frontieres amont et aval: C = constant / E = exclu / L = lineaire"+"\n"
      self.texteCuve+="#"+"\n"
      if self.dico_mot.has_key('ChaleurREV_Fct_Temperature'):
         self.texteCuve+="# Temperature (degC) / chaleur volumique (J/kg/K)"+"\n"
         self.imprime(2,(self.dico_mot["ChaleurREV_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_ChaleurREV','Aval_ChaleurREV')
      elif self.dico_mot.has_key('EnthalpieREV_Fct_Temperature'):
         self.texteCuve+="# Temperature (degC) / enthalpie (J/kg)"+"\n"
         self.imprime(2,(self.dico_mot["EnthalpieREV_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_EnthalpieREV','Aval_EnthalpieREV')
      else :
         self.texteCuve+="# Temperature (degC) / chaleur volumique (J/kg/K)"+"\n"
         self.texteCuve+="0.    36.03E5 "+"\n"
         self.texteCuve+="20.   36.03E5 "+"\n"
         self.texteCuve+="200.  41.65E5 "+"\n"
         self.texteCuve+="350.  43.47E5 "+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Temperature (degC) / conductivite thermique (W/m/degC)"+"\n"
      if self.dico_mot.has_key('ConductiviteREV_Fct_Temperature'):
         self.imprime(2,(self.dico_mot["ConductiviteREV_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_ConductiviteREV','Aval_ConductiviteREV')
      else :
         self.texteCuve+="0.    14.7 "+"\n"
         self.texteCuve+="20.   14.7 "+"\n"
         self.texteCuve+="200.  17.2 "+"\n"
         self.texteCuve+="350.  19.3 "+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Temperature (degC) / module d'Young (MPa)"+"\n"
      if self.dico_mot.has_key('ModuleYoungREV_Fct_Temperature'):
         self.imprime(2,(self.dico_mot["ModuleYoungREV_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_ModuleYoungREV','Aval_ModuleYoungREV')
      else :
         self.texteCuve+="0.    198500. "+"\n"
         self.texteCuve+="20.   197000. "+"\n"
         self.texteCuve+="200.  184000. "+"\n"
         self.texteCuve+="350.  172000. "+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Temperature (degC) / coefficient de dilatation thermique (degC-1)"+"\n"
      if self.dico_mot.has_key('CoeffDilatThermREV_Fct_Temperature'):
         self.imprime(2,(self.dico_mot["CoeffDilatThermREV_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_CoeffDilatThermREV','Aval_CoeffDilatThermREV')
      else :
         self.texteCuve+="0.    16.40E-6 "+"\n"
         self.texteCuve+="20.   16.40E-6 "+"\n"
         self.texteCuve+="200.  17.20E-6 "+"\n"
         self.texteCuve+="350.  17.77E-6 "+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Temperature (degC) / limite d'elasticite (MPa)"+"\n"
      if self.dico_mot.has_key('LimiteElasticiteREV_Fct_Temperature'):
         self.imprime(2,(self.dico_mot["LimiteElasticiteREV_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_LimiteElasticiteREV','Aval_LimiteElasticiteREV')
      else :
         self.texteCuve+="0.    380. "+"\n"
         self.texteCuve+="20.   370. "+"\n"
         self.texteCuve+="100.  330. "+"\n"
         self.texteCuve+="300.  270. "+"\n"
         self.texteCuve+="LL"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve += self.ecritVariable('TemperatureDeformationNulleREV')
      self.texteCuve += self.ecritVariable('TemperaturePourCoefDilatThermREV')
      self.texteCuve += self.ecritVariable('CoefficientPoissonREV')

      # Rubrique CARACTERISTIQUES DU METAL DE BASE
      self.texteCuve += self.rubrique('CARACTERISTIQUES DU METAL DE BASE')

      self.texteCuve += self.ecritVariable('ConditionLimiteThermiqueMDB')

      self.texteCuve+="# - si CHALEUR,   fournir Temperature (degC) / chaleur volumique (J/kg/K)"+"\n"
      self.texteCuve+="# - si ENTHALPIE, fournir Temperature (degC) / enthalpie (J/kg)"+"\n"
      self.texteCuve+="# Finir chacune des listes par la prolongation aux frontieres amont et aval: C = constant / E = exclu / L = lineaire"+"\n"
      self.texteCuve+="#"+"\n"

      if self.dico_mot.has_key('ChaleurMDB_Fct_Temperature'):
         self.texteCuve+="# Temperature (degC) / chaleur volumique (J/kg/K)"+"\n"
         self.imprime(2,(self.dico_mot["ChaleurMDB_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_ChaleurMDB','Aval_ChaleurMDB')
      elif self.dico_mot.has_key('EnthalpieMDB_Fct_Temperature'):
         self.texteCuve+="# Temperature (degC) / enthalpie (J/kg)"+"\n"
         self.imprime(2,(self.dico_mot["EnthalpieMDB_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_EnthalpieMDB','Aval_EnthalpieMDB')
      else :
         self.texteCuve+="# Temperature (degC) / chaleur volumique (J/kg/K)"+"\n"
         self.texteCuve+="0.    34.88E+05 "+"\n"
         self.texteCuve+="20.   34.88E+05 "+"\n"
         self.texteCuve+="200.  40.87E+05 "+"\n"
         self.texteCuve+="350.  46.02E+05 "+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Temperature (degC) / conductivite thermique (W/m/degC)"+"\n"
      if self.dico_mot.has_key('ConductiviteMDB_Fct_Temperature'):
         self.imprime(2,(self.dico_mot["ConductiviteMDB_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_ConductiviteMDB','Aval_ConductiviteMDB')
      else :
         self.texteCuve+="0.    37.7 "+"\n"
         self.texteCuve+="20.   37.7 "+"\n"
         self.texteCuve+="200.  40.5 "+"\n"
         self.texteCuve+="350.  38.7 "+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Temperature (degC) / module d'Young (MPa)"+"\n"
      if self.dico_mot.has_key('ModuleYoungMDB_Fct_Temperature'):
         self.imprime(2,(self.dico_mot["ModuleYoungMDB_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Aval_ModuleYoungMDB','Aval_ModuleYoungMDB')
      else :
         self.texteCuve+="0.    205000. "+"\n"
         self.texteCuve+="20.   204000. "+"\n"
         self.texteCuve+="200.  193000. "+"\n"
         self.texteCuve+="350.  180000. "+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve+="# Temperature (degC) / coefficient de dilatation thermique (degC-1)"+"\n"
      if self.dico_mot.has_key('CoeffDilatThermMDB_Fct_Temperature'):
         self.imprime(2,(self.dico_mot["CoeffDilatThermMDB_Fct_Temperature"]))
         self.texteCuve += self.amontAval('Amont_CoeffDilatThermMDB','Aval_CoeffDilatThermMDB')
      else :
         self.texteCuve+="0.    11.22E-6 "+"\n"
         self.texteCuve+="20.   11.22E-6 "+"\n"
         self.texteCuve+="200.  12.47E-6 "+"\n"
         self.texteCuve+="350.  13.08E-6 "+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve+="#"+"\n"
      self.texteCuve += self.ecritVariable('TemperatureDeformationNulleMDB')
      self.texteCuve += self.ecritVariable('TemperaturePourCoefDilatThermMDB')
      self.texteCuve += self.ecritVariable('CoefficientPoissonMDB')

      # Rubrique CARACTERISTIQUES DU TRANSITOIRE MECANIQUE-THERMOHYDRAULIQUE
      self.texteCuve += self.rubrique('CARACTERISTIQUES DU TRANSITOIRE MECANIQUE-THERMOHYDRAULIQUE')
      self.texteCuve += self.sousRubrique('Chargement mecanique : transitoire de pression','')

      self.texteCuve+="# instant (s) / pression (MPa)"+"\n"
      self.texteCuve+="# Prolongation aux frontieres amont et aval: C = constant / E = exclu / L = lineaire"+"\n"
      if self.dico_mot.has_key('ProfilTemporel_Pression'):
         self.imprime(2,(self.dico_mot["ProfilTemporel_Pression"]))
         self.texteCuve += self.amontAval('Amont_Pression','Aval_Pression')
      else :
         self.texteCuve+="0.    15.5 "+"\n"
         self.texteCuve+="20.   0.1 "+"\n"
         self.texteCuve+="200.  0.1 "+"\n"
         self.texteCuve+="1000. 0.1 "+"\n"
         self.texteCuve+="CC"+"\n"

      self.texteCuve += self.sousRubrique('Chargement thermo-hydraulique','')
      if self.dico_mot.has_key('TypeConditionLimiteThermique'):
         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Temperature imposee en paroi':
            self.texteCuve += self.affecteValeur('TypeConditionLimiteThermique', 'TEMP_IMPO')
         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Flux de chaleur impose en paroi':
            self.texteCuve += self.affecteValeur('TypeConditionLimiteThermique', 'FLUX_REP')
         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Temperature imposee du fluide et coefficient echange':
            self.texteCuve += self.affecteValeur('TypeConditionLimiteThermique', 'ECHANGE')
         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Debit massique et temperature d injection de securite':
            self.texteCuve += self.affecteValeur('TypeConditionLimiteThermique', 'DEBIT')
         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Temperature imposee du fluide et debit d injection de securite':
            self.texteCuve += self.affecteValeur('TypeConditionLimiteThermique', 'TEMP_FLU')
         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Courbe APRP':
            self.texteCuve += self.affecteValeur('TypeConditionLimiteThermique', 'APRP')
      else :
         self.texteCuve += self.affecteValeurDefaut('TypeConditionLimiteThermique')

      self.texteCuve+="# - si TEMP_IMPO, fournir Instant (s) / Temperature imposee (degC)"+"\n"
      self.texteCuve+="# - si FLUX_REP,  fournir Instant (s) / Flux de chaleur impose (W/m2)"+"\n"
      self.texteCuve+="# - si ECHANGE,   fournir Instant (s) / Temperature impose (degC)"+"\n"
      self.texteCuve+="#                    puis Instant (s) / Coefficient d echange (W/m2/K)"+"\n"
      self.texteCuve+="# - si DEBIT,     fournir Instant (s) / Debit massique (kg/s)"+"\n"
      self.texteCuve+="#                    puis Instant (s) / Temperature d injection de securite  (degC)"+"\n"
      self.texteCuve+="#                    puis Modele VESTALE : (DH, DH_MESSAGE), (SECTION, SECTION_MESSAGE), (DELTA, DELTA_MESSAGE), EPS, COEFVESTALE"+"\n"
      self.texteCuve+="#                    puis Modele CREARE  : (VM, VM_MESSAGE), (T0, T0_MESSAGE), (SE, SE_MESSAGE)"+"\n"
      self.texteCuve+="# - si TEMP_FLU,  fournir Instant (s) / Temperature du fluide (degC)"+"\n"
      self.texteCuve+="#                    puis Instant (s) / Debit d injection de securite  (kg/s)"+"\n"
      self.texteCuve+="#                    puis Modele VESTALE : (DH, DH_MESSAGE), (SECTION, SECTION_MESSAGE), (DELTA, DELTA_MESSAGE), EPS, COEFVESTALE"+"\n"
      self.texteCuve+="# - si APRP,      fournir INSTANT1, INSTANT2, QACCU, QIS"+"\n"
      self.texteCuve+="#                    puis TIS_MESSAGE"+"\n"
      self.texteCuve+="#                    puis Instant (s) / Temperature du fluide (degC) tel que dans l'exemple ci-dessous"+"\n"
      self.texteCuve+="#                         0.    286."+"\n"
      self.texteCuve+="#                         12.   20.             # 1er palier à T=TACCU"+"\n"
      self.texteCuve+="#                         20.   20.             # idem que ci-dessus"+"\n"
      self.texteCuve+="#                         21.   18.             # 2nd palier à T=T1 : sera remplace par nouvelle valeur calculee par fonction idoine"+"\n"
      self.texteCuve+="#                         45.   18.             # idem que ci-dessus"+"\n"
      if self.dico_mot.has_key('TypeConditionLimiteThermique'):
         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Courbe APRP':
            self.texteCuve+="#                         46.   9999999999.     # 3eme palier à T=Tis, temperature d injection de securite"+"\n"
         else :
            self.texteCuve+="#                         46.   %INLET-TIS%     # 3eme palier à T=Tis, temperature d injection de securite"+"\n"
      else :
         self.texteCuve+="#                         46.   %INLET-TIS%     # 3eme palier à T=Tis, temperature d injection de securite"+"\n"
      self.texteCuve+="#                         1870. 9999999999.     # idem que ci-dessus"+"\n"
      self.texteCuve+="#                         1871. 80."+"\n"
      self.texteCuve+="#                         3871. 80."+"\n"
      self.texteCuve+="#                    puis Instant (s) / Debit d injection de securite  (kg/s)"+"\n"
      self.texteCuve+="#                    puis Modele VESTALE : (DH, DH_MESSAGE), (SECTION, SECTION_MESSAGE), (DELTA, DELTA_MESSAGE), EPS, COEFVESTALE"+"\n"
      self.texteCuve+="# Finir chacune des listes par la prolongation aux frontieres amont et aval: C = constant / E = exclu / L = lineaire"+"\n"
      self.texteCuve+="#"+"\n"

      if self.dico_mot.has_key('TypeConditionLimiteThermique'):

         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Courbe APRP':
            self.texteCuve+="#"+"\n"
            self.texteCuve+="# Definition de parametres pour le cas d un transitoire APRP"+"\n"
            self.texteCuve += self.ecritVariable('Instant_1')
            self.texteCuve += self.ecritVariable('Instant_2')
            self.texteCuve += self.ecritVariable('DebitAccumule')
            self.texteCuve += self.ecritVariable('DebitInjectionSecurite')
            self.texteCuve += self.ecritVariable('TempInjectionSecurite_mess')

         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Temperature imposee en paroi' or str(self.dico_mot["TypeConditionLimiteThermique"])=='Temperature imposee du fluide et coefficient echange' or str(self.dico_mot["TypeConditionLimiteThermique"])=='Temperature imposee du fluide et debit d injection de securite' or str(self.dico_mot["TypeConditionLimiteThermique"])=='Courbe APRP' :
            self.texteCuve+="#"+"\n"
            self.texteCuve+="# instant (s) / temperature imposee du fluide (degC)"+"\n"
            if self.dico_mot.has_key('ProfilTemporel_TemperatureImposeeFluide'):
               self.imprime(2,(self.dico_mot["ProfilTemporel_TemperatureImposeeFluide"]))
               self.texteCuve += self.amontAval('Amont_TemperatureImposeeFluide','Aval_TemperatureImposeeFluide')
	    else :
               self.texteCuve+="0.    286. "+"\n"
               self.texteCuve+="20.   20. "+"\n"
               self.texteCuve+="200.  7. "+"\n"
               self.texteCuve+="1000. 80. "+"\n"
               self.texteCuve+="CC"+"\n"

         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Flux de chaleur impose en paroi':
            self.texteCuve+="#"+"\n"
            self.texteCuve+="# instant (s) / flux de chaleur impose (W/m2)"+"\n"
            if self.dico_mot.has_key('ProfilTemporel_FluxChaleur'):
               self.imprime(2,(self.dico_mot["ProfilTemporel_FluxChaleur"]))
               self.texteCuve += self.amontAval('Amont_FluxChaleur','Aval_FluxChaleur')
               self.texteCuve+="#"+"\n"
	    else :
               self.texteCuve+="0.    -0. "+"\n"
               self.texteCuve+="20.   -366290. "+"\n"
               self.texteCuve+="200.  -121076. "+"\n"
               self.texteCuve+="1000.  -56372."+"\n"
               self.texteCuve+="CC"+"\n"

         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Temperature imposee du fluide et debit d injection de securite' or str(self.dico_mot["TypeConditionLimiteThermique"])=='Courbe APRP':
            self.texteCuve+="#"+"\n"
            self.texteCuve+="# instant (s) / Debit d injection de securite  (kg/s)"+"\n"
            if self.dico_mot.has_key('ProfilTemporel_DebitInjection'):
               self.imprime(2,(self.dico_mot["ProfilTemporel_DebitInjection"]))
               self.texteCuve += self.amontAval('Amont_DebitInjection','Aval_DebitInjection')
	    else :
               self.texteCuve+="0.    4590. "+"\n"
               self.texteCuve+="20.   4590. "+"\n"
               self.texteCuve+="200.  340. "+"\n"
               self.texteCuve+="1000. 31.1 "+"\n"
               self.texteCuve+="CC"+"\n"

         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Temperature imposee du fluide et coefficient echange' :
            self.texteCuve+="#"+"\n"
            self.texteCuve+="# instant (s) / Coefficient d echange (W/m2/K)"+"\n"
            if self.dico_mot.has_key('ProfilTemporel_CoefficientEchange'):
               self.imprime(2,(self.dico_mot["ProfilTemporel_CoefficientEchange"]))
               self.texteCuve += self.amontAval('Amont_CoefficientEchange','Aval_CoefficientEchange')
	    else :
               self.texteCuve+="0.    138454. "+"\n"
               self.texteCuve+="20.   19972. "+"\n"
               self.texteCuve+="200.  2668. "+"\n"
               self.texteCuve+="1000. 2668. "+"\n"
               self.texteCuve+="CC"+"\n"

         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Debit massique et temperature d injection de securite' :
            self.texteCuve+="#"+"\n"
            self.texteCuve+="# instant (s) / Debit massique (kg/s)"+"\n"
            if self.dico_mot.has_key('ProfilTemporel_DebitMassique'):
               self.imprime(2,(self.dico_mot["ProfilTemporel_DebitMassique"]))
               self.texteCuve += self.amontAval('Amont_DebitMassique','Aval_DebitMassique')
	    else :
               self.texteCuve+="0.    18.4 "+"\n"
               self.texteCuve+="20.   18.4 "+"\n"
               self.texteCuve+="200.  31.1 "+"\n"
               self.texteCuve+="1000. 31.1 "+"\n"
               self.texteCuve+="CC"+"\n"

            self.texteCuve+="#"+"\n"
            self.texteCuve+="# instant (s) / Temperature d injection de securite  (degC)"+"\n"
            if self.dico_mot.has_key('ProfilTemporel_TemperatureInjection'):
               self.imprime(2,(self.dico_mot["ProfilTemporel_TemperatureInjection"]))
               self.texteCuve += self.amontAval('Amont_TemperatureInjection','Aval_TemperatureInjection')
	    else :
               self.texteCuve+="0.    7.0 "+"\n"
               self.texteCuve+="20.   7.0 "+"\n"
               self.texteCuve+="200.  7.0 "+"\n"
               self.texteCuve+="1000. 7.0 "+"\n"
               self.texteCuve+="CC"+"\n"

         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Debit massique et temperature d injection de securite' or str(self.dico_mot["TypeConditionLimiteThermique"])=='Temperature imposee du fluide et debit d injection de securite' or str(self.dico_mot["TypeConditionLimiteThermique"])=='Courbe APRP' :
            self.texteCuve+="#"+"\n"
            self.texteCuve+="# Transitoire des coefficients d echange : modele VESTALE"+"\n"
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('DiametreHydraulique')
            self.texteCuve += self.ecritVariable('DiametreHydraulique_mess')
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('SectionEspaceAnnulaire')
            self.texteCuve += self.ecritVariable('SectionEspaceAnnulaire_mess')
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('HauteurCaracConvectionNaturelle')
            self.texteCuve += self.ecritVariable('HauteurCaracConvectionNaturelle_mess')
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('CritereConvergenceRelative')
            self.texteCuve += self.ecritVariable('CoefficientsVestale')
         if str(self.dico_mot["TypeConditionLimiteThermique"])=='Debit massique et temperature d injection de securite':
            self.texteCuve+="#"+"\n"
            self.texteCuve+="# Transitoire de temperature fluide locale : modele CREARE"+"\n"
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('VolumeMelange_CREARE')
            self.texteCuve += self.ecritVariable('VolumeMelange_CREARE_mess')
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('TemperatureInitiale_CREARE')
            self.texteCuve += self.ecritVariable('TemperatureInitiale_CREARE_mess')
            self.texteCuve+="#"+"\n"
            self.texteCuve += self.ecritVariable('SurfaceEchange_FluideStructure')
            self.texteCuve += self.ecritVariable('SurfaceEchange_FluideStructure_mess')
      else :
         self.texteCuve+="#"+"\n"
         self.texteCuve+="# instant (s) / temperature imposee du fluide (degC)"+"\n"
         self.texteCuve+="0.    286. "+"\n"
         self.texteCuve+="20.   20. "+"\n"
         self.texteCuve+="200.  7. "+"\n"
         self.texteCuve+="1000. 80. "+"\n"
         self.texteCuve+="CC"+"\n"
      self.texteCuve+="#"+"\n"
      self.texteCuve+="############################################################################################"+"\n"


   def imprime(self,nbdeColonnes,valeur):
      self.liste=[]
      self.transforme(valeur)
      i=0
      while i < len(self.liste):
          for k in range(nbdeColonnes) :
              self.texteCuve+=str(self.liste[i+k]) +"  "
          self.texteCuve+="\n"
          i=i+k+1
               

   def transforme(self,valeur):
      for i in valeur :
          if type(i) == tuple :
             self.transforme(i)
          else :
             self.liste.append(i)
          



