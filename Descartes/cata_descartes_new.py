# -*- coding: utf-8 -*-
# debut entete

import Accas
from Accas import *
#

JdC = JDC_CATA(code='DESCARTES',
               execmodul=None,
               niveaux=(NIVEAU(nom='Isotopes',label='Donnees des Isotopes ou molecules et Bibliotheques associees'),
                        NIVEAU(nom='ChaineFiliationIsotopique',label='Chaines de filiation isotopique'),
                        NIVEAU(nom='MaillagesEnergie',label='Maillages en energie'),
                        NIVEAU(nom='DonneesNucleaires',label='Bibliotheques de donnees nucleaires et Fichiers'),
                        NIVEAU(nom='Materiaux',label='Materiaux'),
                        NIVEAU(nom='ElementsGeometriques',label='Elements geometriques elementaires'),
                        NIVEAU(nom='Geometries',label='Geometries globales'),
                        NIVEAU(nom='MaillagesSpatiaux',label='Maillages en espace'),
                        NIVEAU(nom='ElementsTechnologiquesAssemblages',label='Elements technologiques des assemblages combustibles'),
                        NIVEAU(nom='ElementsTechnologiquesReacteur',label='Elements technologiques des reacteurs'),
                        NIVEAU(nom='AssemblagesReels',label='Assemblages combustibles reels'),
                        NIVEAU(nom='ConditionsLimites',label='Conditions aux limites'),
                        NIVEAU(nom='ParametresCalcul',label='Parametres des calculs'),
                        NIVEAU(nom='SectionsEfficaces',label ='Bibliotheques de sections efficaces'),
                        NIVEAU(nom='OptionsCodesCalcul',label='Options des codes de calcul'),
                        NIVEAU(nom='ConfigurationInformatique',label='Choix des ressources informatiques'),
                        NIVEAU(nom='DonneesDesAccidents',label ='Donnees des etudes d_accidents'),
                        NIVEAU(nom='DonneesPilotage',label ='Donnees de pilotage du reacteur'),
                        NIVEAU(nom='DonneesEtude',label ='Donnees des cas de l etude'),
                        NIVEAU(nom='Operateurs',label ='Definition des operateurs de calcul'),
                        NIVEAU(nom='Resultats',label ='Resultats des calculs'),
                        NIVEAU(nom='ResultatsExperimentaux',label ='Resultats issus de mesures experimentales'),
                        NIVEAU(nom='ResultatsAccidents',label ='Resultats issus de la simulation des accidents'),
                        NIVEAU(nom='EtudeGenerale',label ="Cas d'etude et resultats")
                       )
              )

import string
#import lcm

class TObjet(ASSD):
  def __init__(self,**args):
    apply(ASSD.__init__,(self,),args)
    name=string.ljust(self.__class__.__name__[:12],12)

  def __getitem__(self,attrname):
    return self.etape[attrname]

  def db(self):
    if hasattr(self,'_dbsun'):return self._dbsun
    else:
      self._dbsun={'t':1}
      return self._dbsun

  def putdb(self,o):
    self._dbsun=o

#
# Definition des types d'objet qui seront produits par les commandes
# Il suffit de declarer une classe qui derive de la classe mere TObjet
# qui derive elle meme de la classe ASSD utilisee dans EFICAS
#
#     Isotopes
class Isotope				(TObjet):pass
#     ChaineFiliationIsotopique
class ChaineFiliation			(TObjet):pass
#     MaillagesEnergie
class BornesEnergie			(TObjet):pass
#     DonneesNucleaires
class FichierBibliothequeIsotopes	(TObjet):pass
#     Materiaux
class Materiau				(TObjet):pass
#     MaillagesSpatiaux
class Maillage1D			(TObjet):pass
#     ElementsGeometriques
class Point				(TObjet):pass
class Vecteur				(TObjet):pass
class Droite				(TObjet):pass
class Segment				(TObjet):pass
class ArcCercle				(TObjet):pass
class SecteurDisque			(TObjet):pass
class Conique				(TObjet):pass
class Triangle				(TObjet):pass
class Rectangle				(TObjet):pass
class Carre				(TObjet):pass
class Hexagone				(TObjet):pass
class Polygone				(TObjet):pass
class Sphere				(TObjet):pass
class BoiteRectangulaire		(TObjet):pass
class BoiteGenerale			(TObjet):pass
class CylindreX				(TObjet):pass
class CylindreY				(TObjet):pass
class CylindreZ				(TObjet):pass
class Cylindre				(TObjet):pass
class Cone				(TObjet):pass
class PrismeHexagonal			(TObjet):pass
class Tore				(TObjet):pass
class Plan				(TObjet):pass
class PlanX				(TObjet):pass
class PlanY				(TObjet):pass
class PlanZ				(TObjet):pass
class Polyedre				(TObjet):pass
class Quadrique				(TObjet):pass
class Orientation			(TObjet):pass
class FormePositionnee			(TObjet):pass
#     Geometries
class Cellule				(TObjet):pass
class Cluster				(TObjet):pass
class GeometrieSurfacique		(TObjet):pass
class GeometrieCombinatoire		(TObjet):pass
class Reseau				(TObjet):pass
class DecompositionDomaines		(TObjet):pass
#     ElementsTechnologiquesAssemblages
class GrilleAssemblage				(TObjet):pass
class PartieInferieureAssemblageCombustible	(TObjet):pass
class PartieSuperieureAssemblageCombustible	(TObjet):pass
class AssemblageType				(TObjet):pass
class ElementBarre				(TObjet):pass
class ElementsGrappeCommande			(TObjet):pass
class ElementsAbsorbantsFixes			(TObjet):pass
class GrappeBouchonAssemblage			(TObjet):pass
#     AssemblagesReels
class AssemblageCombustibleReel		(TObjet):pass
class ReparationAssemblage		(TObjet):pass
class PenaliteAssemblage		(TObjet):pass
#class SystemeUnitesMesure		(TObjet):pass
#     ConditionsLimites
class Vide				(TObjet):pass
class ReflexionIsotrope			(TObjet):pass
class ReflexionSpeculaire		(TObjet):pass
class Albedo				(TObjet):pass
class Translation			(TObjet):pass
class Rotation				(TObjet):pass
class SpecialeConditionLimite		(TObjet):pass
class GeneraleConditionLimite		(TObjet):pass
#     ElementsTechnologiquesReacteur
class CorrespondanceReperePositionReseau(TObjet):pass
class PositionAssemblageCombustible	(TObjet):pass
class PositionInstrumentationInterne	(TObjet):pass
class ImplantationGrappesCommande	(TObjet):pass
class StructuresInternesReacteur	(TObjet):pass
class PompePrimaire			(TObjet):pass
class Pressuriseur			(TObjet):pass
class GenerateurVapeur			(TObjet):pass
class CaracteristiquesPalier		(TObjet):pass
class SiteNucleaire			(TObjet):pass
#     ParametresCalcul
class EspaceVariations			(TObjet):pass
class DonneesIrradiation		(TObjet):pass
class ConditionsFonctionnementMoyennes	(TObjet):pass
class ConditionsTransitoire		(TObjet):pass
class PositionAxialeGrappesCommande	(TObjet):pass
class ParametresCalculGestion		(TObjet):pass
#     SectionsEfficaces
class Macrolib				(TObjet):pass
class SectionsReflecteur		(TObjet):pass
#     OptionsCodesCalcul
class OptionsAutoprotection		(TObjet):pass
class OptionsCodes			(TObjet):pass
class OptionsCodeReseau			(TObjet):pass
class OptionsCodeCoeurStatique		(TObjet):pass
class OptionsCodeCoeurCinetique		(TObjet):pass
class OptionsThermiqueThermohydraulique	(TObjet):pass
class OptionsContreReactionsCoeur	(TObjet):pass
#     ConfigurationInformatique
class RessourcesInformatiques		(TObjet):pass
#     DonneesDesAccidents
class AccidentDilution			(TObjet):pass
class AccidentRTV			(TObjet):pass
class AccidentChuteGrappe		(TObjet):pass
class AccidentEjection			(TObjet):pass
class CriteresSurete			(TObjet):pass
class DonneesAccidents			(TObjet):pass
#     DonneesPilotage
class ProlongationCampagne 		(TObjet):pass
class DonneesPilotageGeneral		(TObjet):pass
class CalibrageGroupes			(TObjet):pass
#     DonneesEtude
class DatesClesCampagne			(TObjet):pass
class DonneesCasEtude			(TObjet):pass
class DonneesAjustement			(TObjet):pass
#     Resultats
class ResultatsGlobauxCoeur		(TObjet):pass
class ResultatFlux			(TObjet):pass
class ResultatPuissances		(TObjet):pass
class ResultatIrradiations		(TObjet):pass
class ResultatActivites			(TObjet):pass
class ResultatRadial			(TObjet):pass
class ResultatAxial			(TObjet):pass
class ResultatsCalculGestion		(TObjet):pass
class ResultatsEtude			(TObjet):pass
#     ResultatsAccidents
class AccidentDilutionResultat		(TObjet):pass
class AccidentChuteGrappeResultat	(TObjet):pass
class AccidentEjectionResultat		(TObjet):pass
class AccidentsResultats		(TObjet):pass
#     ResultatsExperimentaux
class ActivitesExperimentales		(TObjet):pass
#     EtudeGenerale
class DictionnaireCasEtude		(TObjet):pass
# fin entete
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe ISOTOPE : Classe de definition d'un isotope ou d'une molecule
#                   Caracteristiques elementaires des isotopes ou molecules et liens avec les bibliotheques de donnees nucleaires
#                   Ces caracteristiques elementaires ne devraient pas apparaître dans ce type d'objet, mais etre recuperees directement
#                   dans la bibliotheque de donnees de base. La structure des APOLLIB n'etant pas simple d'acces, la solution
#                   adoptee permet de mettre a disposition ces informations de maniere simple. A revoir ulterieurement
#                   apres redefinition du contenu d'une bibliotheque de base.
#                   La decomposition en éléments chimiques simples est utile pour les calculs de type TRIPOLI, les données nucléaires
#                   étant définies parfois pour chaque élément et non pour la molécule (cas de l'eau par exemple)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ISOTOPE = OPER (nom="ISOTOPE", sd_prod=Isotope, op=0, niveau = 'Isotopes',
  fr  = "Definition d'un isotope ou d'une molecule et de ses bibliotheques",
  ang = "Isotope or Molecule definition and data libraries",
  Symbole                = SIMP (typ='TXM',statut='o',fr="Symbole de l'isotope ou de la molecule"),
  MasseAtomique          = SIMP (typ='R',  statut='o',fr="Masse atomique en uma"),
  NombreDeCharge         = SIMP (typ='I',  statut='o',fr="Nombre de charge atomique Z"),
  NombreDeMasse          = SIMP (typ='I',  statut='o',fr="Nombre de masse atomique A"),
  Type                   = SIMP (typ='TXM',statut='f',into=('Standard','Detecteur','Structure','Poison'),fr="Type de l'isotope"),
  NomsBibliotheque       = NUPL (max = '**', statut = 'o',fr="Association Procedure Bibliotheque et Nom isotope dans le Fichier",
                                 elements = ( SIMP (typ='TXM',fr="Identificateur Procedure Bibliotheque"),
                                              SIMP (typ='TXM',fr="Identifiant de l'isotope dans la bibliotheque"))),
  NomsBiblioAutoprotegee = NUPL (max = '**', statut = 'f',
                                 elements = ( SIMP (typ='TXM',fr="Identificateur Procedure Bibliotheque"),
                                              SIMP (typ='TXM',fr="Identifiant Bibliotheque autoprotegee de l'isotope"))),
  ComposantsElementaires = SIMP (typ=Isotope, max = '**', statut = 'f',
                                 fr="Liste des elements chimiques composant la molecule")
 ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe BORNES_ENERGIE : Classe de definition des limites en energie d'un maillage multigroupe
#                          Objets utilises pour la définition du maillage des bibliothèques de base
#                          ou des macro-groupes d'énergie de condensation des sections efficaces sur le flux détaillé
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BORNES_ENERGIE = OPER (nom="BORNES_ENERGIE", sd_prod=BornesEnergie, op=0, niveau = 'MaillagesEnergie',
    fr  = "Definition d'une discretisation de l'espace energetique",
    ang = "Definition of an energy discretisation",
    NbMacrogroupes     = SIMP (statut='o',typ='I',	    fr="Nombre de macrogroupes du maillage energetique"),
    BornesEnergetiques = SIMP (statut='o',typ='R',max='**',fr="Bornes en energie (MeV) du maillage energetique"),
 ) ; # Fin BORNES_ENERGIE
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe MAILLAGE_1D : Classe de definition d'un maillage spatial 1D : 4 possiblilites de definition :
#  1 et 2) Equidistant et Equivolumique : Largeur totale a fournir
#       3) Liste des dimensions des mailles
#       4) Abscisse initiale et couples (Nb sous-pas, Abscisse suivante)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
MAILLAGE_1D = OPER (nom="MAILLAGE_1D", sd_prod=Maillage1D, op=0, niveau = 'MaillagesSpatiaux',
    fr  = "Definition d'une discretisation d'un espace 1D",
    ang = "Definition of a 1D spatial discretisation",
    ModeDefinition  = SIMP (typ='TXM',statut='o',defaut='LargeurMaille',into=('Equidistant','Equivolumique','LargeurMaille','SousMaille'),
                            fr="Mode de definition du maillage"),
    NbMailles       = SIMP (typ='I',statut='o',fr="Nombre de mailles de discretisation"),
    BlocEqui        = BLOC (condition = "ModeDefinition=='Equidistant' or ModeDefinition=='Equivolumique'",
                            DimensionTotale = SIMP (typ='R',statut='o',fr="Largeur totale du maillage en cm")
                            ),
    BlocMailles     = BLOC (condition = "ModeDefinition=='LargeurMaille'",
                            LargeursMailles = SIMP (typ='R',max='**',statut='o',fr="Largeurs des mailles en cm")
                             ),
    BlocSousMailles = BLOC (condition = "ModeDefinition=='SousMaille'",
                            SousMailles = SIMP (typ=('I','R'),max='**',statut='o',fr="Abscisse initiale et couples (Nb sous-pas, Abscisse suivante)")
                            )
    ) ; # Fin MAILLAGE_1D
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe FICHIER_BIBLIOTHEQUE_ISOTOPES : Classe de definition des fichiers des bibliotheques des donnees nucleaires d'isotopes ou de molecules
#                                         Noms et formats des fichiers d'isotopes suivant le systeme d'exploitation
#                                         Dans le cas de TRIPOLI 4, on fournit le nom du dictionnaire ou se trouve la description des
#                                         isotopes disponibles pour le code et le chemin d'accès aux fichiers de sections de ces isotopes
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
FICHIER_BIBLIOTHEQUE_ISOTOPES = OPER (nom="FICHIER_BIBLIOTHEQUE_ISOTOPES", sd_prod=FichierBibliothequeIsotopes, op=0, niveau = 'DonneesNucleaires',
  fr  = "Definition d'une bibliotheque de donnees nucleaires des isotopes",
  ang = "Definition of a nuclear data isotope library",
  Description = SIMP (typ='TXM',statut='o',fr="Identificateur Bibliotheque ou Dictionnaire"),
  Fichiers    = FACT (max='**', statut='o',fr="Donnee des fichiers associes a la bibliotheque et du maillage energetique",
                      SystemeExploitation  = SIMP (typ='TXM',statut='o',fr="Systeme d'exploitation du reseau informatique"),
                      NomFichier           = SIMP (typ='TXM',statut='o',fr="Nom du fichier de la bibliotheque de donnees de base"),
                      FormatFichier        = SIMP (typ='TXM',statut='o',fr="Format du fichier"),
                      BornesEnergetiques   = SIMP (typ=BornesEnergie,statut='o',fr="Bornes en MeV du maillage en energie")
                     )
  ) ; # Fin FICHIER_BIBLIOTHEQUE_ISOTOPES
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CHAINE_FILIATION : Classe de definition des filiations isotopiques dues aux transmutations
#                            sous irradiation neutronique.
#                            Description textuelle sous format (APOLLO2, SUNSET ou DARWIN)
#                            ou description particuliere des filiations.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CHAINE_FILIATION = OPER (nom="CHAINE_FILIATION", op=0, sd_prod=ChaineFiliation, niveau = 'ChaineFiliationIsotopique',
  fr              = "Definition d'une chaine de filiation isotopique sous irradiation",
  ang             = "Definition of a depletion chain",
  NombreIsotopes  = SIMP (typ='I'  ,statut='o',fr="Nombre d'isotopes decrits dans la chaine"),
  ChaineAPOLLO2   = SIMP (typ='TXM',statut='f',fr="Description de la chaine sous format APOLLO2"),
  ChaineSUNSET    = SIMP (typ='TXM',statut='f',fr="Description de la chaine sous format SUNSET"),
  ChaineDARWIN    = SIMP (typ='TXM',statut='f',fr="Nom du fichier contenant la description DARWIN de la chaine"),
  ListeIsotopes   = FACT (max = '**',statut = 'f',
                          Isotope = SIMP (typ=Isotope,fr="Nom de l'isotope",statut='o'),
                          Peres   = FACT (max = '**',statut = 'o',
                                          IsotopePere        = SIMP (statut='o',typ=Isotope,fr="Nom de l'isotope pere"),
                                          TypeReaction       = SIMP (statut='o',typ='TXM'  ,fr="Type de reaction nucleaire",
                                                                     into=('nGamma','n2n','n3n','n4n','np','nalpha')),
                                          RapportBranchement = SIMP (statut='o',typ='R'    ,fr="Rapport de branchement",defaut=1.)
                                         )
                         )
 ) ; # Fin CHAINE_FILIATION
# regles = (UN_PARMI ('ChaineAPOLLO2','ChaineSUNSET','ChaineDARWIN','ListeIsotopes'),),
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe MATERIAU : Classe de définition d'un matériau à partir de mélange d'isotopes ou de matériaux.
#                    Définition alternative par donnée des enrichissements (Possibilités limitées aux combustibles UO2, MOX, Gd)
#                    Caractéristiques fournies a 20 C.
#                    Proprietes thermiques et thermomécaniques éventuelles
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
MATERIAU = OPER(nom="MATERIAU", op=0, sd_prod=Materiau, niveau = 'Materiaux',
  fr  = "Definition d'un materiau",
  ang = "Definition of a mixture",
  TypeDefinition       = SIMP (typ='TXM',statut='o',defaut="Isotopique",into=("Isotopique","Enrichissement")),
  TypeMateriau         = SIMP (statut = 'o', typ = 'TXM',     
                               into   = ('Combustible','Absorbant','Melange','ModerateurInterne','ModerateurExterne','Detecteur',
                                         'Grille','Gaine','Tube','Poison','PoisonConsommable','AbsorbantIntegre',
                                         'CoucheCorrosion','Solide','Liquide','Gaz','MateriauVide'),
                               defaut = 'Combustible'),
  BlocIsotopique       = BLOC (condition = "TypeDefinition=='Isotopique'",
                               MethodeMelange = SIMP (statut   = 'o',typ='TXM',into=('Isotopique','Massique','Concentration'),defaut='Massique'),
                               Constituants   = NUPL (statut   = 'o', max = '**',
                                                      fr       = "Couples (Isotope ou Materiau) et (Pourcentage ou Concentration)",
                                                      elements = (SIMP (typ=(Isotope,Materiau),fr="Isotope ou Materiau constituant"),
                                                                  SIMP (typ='R',fr="Pourcentage % ou Concentration 10E24 de l'isotope ou du materiau"))
                                                      )
                               ),
  BlocEnrichissement   = BLOC (condition = "TypeDefinition=='Enrichissement'",
        Type                 = SIMP (typ='TXM',into=('UO2','MOX','UO2Gadolinium','MOXGadolinium'),statut='o',defaut='UO2',fr="Type de combustible"),
        U235Enrichissement   = SIMP (typ='R',defaut=3.7,statut='o',val_min=0.,val_max=100.,
                                     fr="Enrichissement % en U235 du combustible"),
        TeneurU234Naturel    = SIMP (typ='R',defaut=110.,statut='f',fr="Teneur (ppm) en U234 de l'uranium naturel"),
        DonneesGado          = BLOC (condition = "Type=='UO2Gadolinium' or Type=='MOXGadolinium'",
                                     EnrichissementGado   = SIMP (typ=('R','TXM'),defaut=8.,statut='o',fr="Enrichissement % en Gd2O3 du combustible")),
        DonneesMOX           = BLOC (condition = "Type=='MOX' or Type=='MOXGadolinium'",
                                     PuEnrichissement     = SIMP (typ=('R','TXM'),defaut=5.3,statut='o',val_min=0.,val_max=100.,
                                                                  fr="Enrichissement % en plutonium du combustible"),
                                     VecteurPu            = FACT (statut='o',fr="Definition du vecteur isotopique du plutonium",
				                                  Pu238PourcentageMassique = SIMP (typ='R',statut='o',fr="Pourcentage Massique en Pu238"),
				                                  Pu239PourcentageMassique = SIMP (typ='R',statut='o',fr="Pourcentage Massique en Pu239"),
				                                  Pu240PourcentageMassique = SIMP (typ='R',statut='o',fr="Pourcentage Massique en Pu240"),
				                                  Pu241PourcentageMassique = SIMP (typ='R',statut='o',fr="Pourcentage Massique en Pu241"),
				                                  Pu242PourcentageMassique = SIMP (typ='R',statut='o',fr="Pourcentage Massique en Pu242"),
				                                  Am241PourcentageMassique = SIMP (typ='R',statut='o',fr="Pourcentage Massique en Am241"),
								 ),
                                     DateReference        = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A de reference du combustible"),
                                     DateDivergence       = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A de divergence du reacteur ou ce combustible est charge"),
                                     VieillissementJours  = SIMP (typ='R',defaut = 0.,statut = 'f',
      							   	  fr = "Nbre de jours de vieillissement du combustible, calculable si on donne DateDivergence")
                                     )
                              ),
  TauxEvidement        = SIMP (statut='f',typ='R',fr="Taux % d'evidement du materiau"),
  TauxPorosite         = SIMP (statut='f',typ='R',fr="Taux % de porosite du materiau"),
  Temperature          = SIMP (statut='f',typ='R',fr="Temperature en Celsius du materiau"),
  PlenumGaz            = SIMP (statut='f',typ=(Isotope,Materiau),defaut='HE4',fr="Gaz de remplissage des evidements du materiau solide et dans le plenum"),
# PlenumGaz            = SIMP (statut='f',typ=(Isotope,Materiau),fr="Gaz de remplissage des evidements du materiau solide et dans le plenum"),
  PressionPlenumGaz    = SIMP (statut='f',typ='R',defaut=32.,fr="Pression en bars du gaz de remplissage des evidements et dans le plenum"),
  Chaine	       = SIMP (statut='f',typ=ChaineFiliation,defaut='ChaineSaturee',fr="Chaine de filiation isotopique associee au materiau"),
  TauxImpuretes        = SIMP (statut='f',typ='R',fr="Taux % d'impuretes"),
  ChaleurSpecifiquePressionCte  = SIMP (statut='f',typ='R',fr="Chaleur Specifique a Pression Constante J/(kg.C)"),
  ConductiviteThermique = SIMP (statut='f',typ='R',fr="Conductivite Thermique W/(cm.C)"),
  MateriauGazBloc       = BLOC (condition = "TypeMateriau=='Gaz'",
                                GazLongueurExtrapolation = SIMP (statut='f',typ='R',fr="Longueur Extrapolation en cm"),
                                GazPression              = SIMP (statut='f',typ='R',fr="Pression du gaz en bars")
                               ),
  MateriauLiquideBloc   = BLOC (condition = "TypeMateriau in ('Liquide','ModerateurInterne','ModerateurExterne')",
                                RoLiquide             = SIMP (statut='f',typ='R',fr="Masse volumique theorique du liquide g/cm3"),
                                PressionLiquide       = SIMP (statut='f',typ='R',fr="Pression du liquide en bars"),
                                EbullitionTemperature = SIMP (statut='f',typ='R',fr="Temperature Ebullition en Celsius"),
                                EbullitionPression    = SIMP (statut='f',typ='R',fr="Pression Ebullition en bars")
                               ),
  MateriauSolideBloc    = BLOC (condition = "TypeMateriau not in ('Liquide','ModerateurInterne','ModerateurExterne','Gaz','MateriauVide')",
                                RoSolide           = SIMP (statut='f',typ='R',fr="Masse volumique theorique du materiau g/cm3"),
                                DilatationLineaire = SIMP (statut='f',typ='R',fr="Coefficient de dilatation thermique lineaire cm/C du materiau"),
                                LimiteElastique    = SIMP (statut='f',typ='R',fr="Limite Elastique en Pa"),
                                Fluence            = SIMP (statut='f',typ='R',fr="Fluence subie par le materiau en n/cm2"),
                                Emissivite         = SIMP (statut='f',typ='R',fr="Valeur d'emissivite"),
                                ModuleYoung        = SIMP (statut='f',typ='R',fr="Module d'Young en Pa"),
                                CoefficientPoisson = SIMP (statut='f',typ='R',fr="Coefficient de Poisson"),
                                RugositeSurface    = SIMP (statut='f',typ='R',fr="Rugosite de Surface en cm")
                               )
 ) ; # Fin MATERIAU
# ==================================================================================================================================
#                                    Definition des Classes elementaires pour la geometrie
# ==================================================================================================================================
#  Classe POINT : Classe de definition d'un point de l'espace
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POINT = OPER (nom="POINT", op=0, sd_prod=Point, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un point de l'espace",
  ang = "Definition of a point in space",
  Coordonnees = SIMP (typ='R',min=2,max=3,statut='o',fr="Coordonnees du point dans l'espace")
 ) ;# Fin POINT
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe VECTEUR : Classe de definition d'un vecteur dans l'espace
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
VECTEUR = OPER (nom="VECTEUR", op=0, sd_prod=Vecteur, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un vecteur dans l'espace",
  ang = "Definition of a vector in space",
  regles = (UN_PARMI ('Composantes','Points'),),
  Composantes = SIMP (typ='R'  ,min=2,max=3,statut='f',fr="Composantes du vecteur en 2D ou 3D"),
  Points      = SIMP (typ=Point,min=2,max=2,statut='f',fr="Vecteur defini par deux points")
 ) ; # Fin VECTEUR
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DROITE : Classe de definition d'une droite
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DROITE = OPER (nom="DROITE", op=0, sd_prod=Droite, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une droite par 2 POINTs, 1 POINT et 1 VECTEUR, ou Equation ax + by + cz + d = 0",
  ang = "Definition of a straight line by 2 POINTs or through an Equation ax + by + cz + d = 0",
  regles   = (UN_PARMI ('Points','Equation','VecteurOrigine'),),
  Points   = SIMP (typ=Point,min=2,max=2,statut='f',fr="Deux points de definition de la droite"),
  Equation = SIMP (typ='R'  ,min=2,max=4,statut='f',fr="Coefficients successifs abcd de l'equation d'une droite"),
  VecteurOrigine = FACT (statut='f',
                         Vecteur  = SIMP (typ=Vecteur,statut='o',fr="Donnee du vecteur directeur de la droite"),
                         Origine  = SIMP (typ=Point  ,statut='o',fr="Donnee d'un point de passage de la droite"))
 ) ; # Fin DROITE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe SEGMENT : Classe de definition d'un segment (Idem DROITE + Longueur et Origine)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SEGMENT = OPER (nom="SEGMENT", op=0, sd_prod=Segment, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un segment 2 Points ou Origine + ((Longueur + Equation ax + by + d = 0) ou vecteur)",
  ang = "Definition of a segment ax + by + cz + d = 0",
  regles   = (UN_PARMI ('Points','Equation','Vecteur'),),
  Points   = SIMP (typ=Point,min=2,max=2,statut='f',fr="Deux points de definition du segment"),
  Equation = FACT (statut='f',fr="Donnee du segment par son equation, sa longueur et son origine",
                   Coefficients = SIMP (typ='R'  ,min=2,max=4,statut='o',fr="Coefficients successifs abcd de l'equation de la droite"),
                   Longueur     = SIMP (typ='R',	      statut='o',fr="Longueur du segment en cm"),
                   Origine      = SIMP (typ=Point,	      statut='o',fr="Donnee de l'origine du segment")
                   ),
  Vecteur  = FACT (statut='f',fr="Donnee du segment par un vecteur, sa longueur et son origine",
                   Vecteur      = SIMP (typ=Vecteur,min=2,max=4,statut='o',fr="Coefficients successifs abcd de l'equation de la droite"),
                   Longueur     = SIMP (typ='R',	        statut='o',fr="Longueur du segment en cm"),
                   Origine      = SIMP (typ=Point,	        statut='o',fr="Donnee de l'origine du segment")
                   )
 ) ; # Fin SEGMENT
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ARC_CERCLE : Classe de definition d'un arc de cercle
#                      Angles donnes en degres
#                      Dans le cas 2D on peut positionner l'arc de cercle en donnant l'angle du debut de l'arc par rapport a l'axe Ox
#                      Dans le cas 3D on donne en plus la hauteur et l'axe directeur de l'arc
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ARC_CERCLE = OPER (nom="ARC_CERCLE", op=0, sd_prod=ArcCercle, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un arc de cercle",
  ang = "Definition of a circular arc",
  Type       = SIMP (typ='TXM'  ,statut='o',defaut='2D',into=('2D','3D'), fr="Type d'arc 2D ou 3D"),
  Rayon      = SIMP (typ='R'    ,statut='o',                              fr="Rayon de l'arc de cercle en cm"),
  Angles     = SIMP (typ='R'    ,statut='f',max=2,defaut=(360.,0.),       fr="Angles en degres de l'arc : Total et Debut"),
  VecteurAxe = SIMP (typ=Vecteur,statut='f',                              fr="Vecteur directeur de l'axe de l'arc")
 ) ; # Fin ARC_CERCLE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe SECTEUR_DISQUE : Classe de definition d'un disque ou d'un secteur d'une couronne circulaire
#                          Angle du secteur donne en degres (360° par defaut)
#                          Dans le cas 2D on peut positionner le secteur en donnant l'angle du debut de secteur par rapport a l'axe Ox
#                          Dans le cas 3D on donne en plus la hauteur et l'axe directeur du secteur
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SECTEUR_DISQUE = OPER (nom="SECTEUR_DISQUE", op=0, sd_prod=SecteurDisque, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un disque ou d'un secteur d'une couronne",
  ang = "Definition of a circular sector",
  Type       = SIMP (typ='TXM'  ,statut='o',into=('2D','3D'),defaut='2D',fr="Type de secteur 2D ou 3D"),
  Rayons     = SIMP (typ='R'    ,statut='o',min=2,max=2,	         fr="Rayons interne et externe de la couronne en cm"),
  Angles     = SIMP (typ='R'    ,statut='f',max=2,defaut=(360.,0.),	 fr="Angles en degres du secteur"),
  Hauteur    = SIMP (typ='R'    ,statut='f',defaut=0.,		         fr="Hauteur du secteur en cm"),
  VecteurAxe = SIMP (typ=Vecteur,statut='f',defaut=0.,		         fr="Vecteur directeur de l'axe du secteur")
 ) ;  # Fin SECTEUR_DISQUE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONIQUE : Classe de definition d'une conique 2D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONIQUE = OPER (nom="CONIQUE", op=0, sd_prod=Conique, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une conique 2D ax2+by2+cxy+dx+ey+f=0",
  ang = "Definition of a 2D quadratic curve ax2+by2+cxy+dx+ey+f=0",
  Equation = SIMP (typ='R',min=2,max=6,statut='o',fr="Coefficients successifs abcdef de l'equation d'une conique")
  ) ; # Fin CONIQUE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe TRIANGLE : Classe de definition d'un triangle
#                    Angles donnes en degres par rapport a l'axe Ox horizontal
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TRIANGLE = OPER (nom="TRIANGLE", op=0, sd_prod=Triangle, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un triangle",
  ang = "Definition of a triangle",
  regles = (UN_PARMI ('Points','AngleCotes'),),
  Points     = SIMP (typ=Point,min=3,max=3,statut='f',fr="Donnee des 3 sommets du triangle"),
  AngleCotes = SIMP (typ='R'  ,min=3,max=3,statut='f',fr="Donnee d'un Angle en degres et Longueurs de deux cotes en cm")
 ) ;  # Fin TRIANGLE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RECTANGLE : Classe de definition d'un rectangle
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RECTANGLE = OPER (nom="RECTANGLE", op=0, sd_prod=Rectangle, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un rectangle",
  ang = "Definition of a rectangle",
  regles = (UN_PARMI ('Points','Cotes'),),
  Points = SIMP (typ=Point,min=3,max=3,statut='f',fr="Definition du rectangle par trois points"),
  LongueursCotes  = SIMP (typ='R'  ,min=2,max=2,statut='f',fr="Donnee de la longueur de deux cotes en cm")
   ) ; # Fin RECTANGLE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CARRE : Classe de definition d'un carre
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CARRE = OPER (nom="CARRE", op=0, sd_prod=Carre, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un carre",
  ang = "Definition of a square",
  regles = (UN_PARMI ('Points','Cote'),),
  Points = SIMP (typ=Point,min=2,max=2, statut='f',fr="Definition du carre par deux points"),
  LongueurCote   = SIMP (typ='R',	statut='f',fr="Donnee de la longueur du cote du carre en cm")
 ) ;  # Fin CARRE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe HEXAGONE : Classe de definition d'un hexagone
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
HEXAGONE = OPER (nom="HEXAGONE", op=0, sd_prod=Hexagone, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un hexagone",
  ang = "Definition of an hexagon",
  Rayon = SIMP (typ='R',statut='f',fr="Rayon du cercle inscrit dans l'hexagone en cm")
 ) ;  # Fin HEXAGONE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POLYGONE : Classe de definition d'un polygone
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POLYGONE = OPER (nom="POLYGONE", op=0, sd_prod=Polygone, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un polygone",
  ang = "Definition of a polygon",
  Points = SIMP (typ=Point,max='**',statut='f',fr="Definition d'un polygone par tous ses points")
 ) ;   # Fin POLYGONE
# ==================================================================================================================================
#            Definition des Classes pour une geometrie 3D : Elements geometriques combinatoires ou surfaciques
# L'utilisation de certaines classes de combinatoire en surfacique consiste a simplement specifier la position de l'objet
# ou a eliminer certaines surfaces limites de la classe
# Pour une sphere : donnee du centre de la sphere
# Pour un cylindre : Pas de donnee de la hauteur, mais donnee d'un point de l'axe du cylindre
# ==================================================================================================================================
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe SPHERE : Classe de definition d'une sphere (ou d'une sphere sectorisee ou decoupee en rondelles)
#                  Des portions de la sphere peuvent etre selectionnees en donnant leurs cotes limites sur un axe de la sphere
#                  (origine de l'axe au centre de la sphere, donc cotes comprises entre -R, +R si R est le rayon de la sphere)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SPHERE = OPER (nom="SPHERE", op=0, sd_prod=Sphere, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme spherique",
  ang = "Definition of a spherical form",
  Rayon           = SIMP (typ='R',statut='o',fr="Rayon de la sphere en cm"),
  Secteur         = SIMP (typ='R',statut='f',fr="Angle du secteur de la sphere en degre"),
  TranchesAxiales = NUPL (max = '**', statut = 'f', fr = "Limites des tranches axiales de la sphere sectorisee",
                          elements = (	SIMP (typ='R',statut = 'o', fr="Cote depart de la tranche"),
                                        SIMP (typ='R',statut = 'o', fr="Cote finale de la tranche")))
 ) ;  # Fin SPHERE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe BOITE_RECTANGULAIRE : Classe de definition d'une forme parallelepipedique de cotes paralleles aux axes de reference
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BOITE_RECTANGULAIRE = OPER (nom="BOITE_RECTANGULAIRE", op=0, sd_prod=BoiteRectangulaire, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une d'une forme parallelepipedique rectangulaire",
  ang = "Definition of a rectangular box form",
  Cotes = SIMP (typ='R',min=3,max=3,statut='o',fr="Longueurs des Cotes de la boite rectangulaire en cm")
 ) ;  # Fin BOITE_RECTANGULAIRE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe BOITE_GENERALE : Classe de definition d'une forme parallelepipedique quelconque
#        Le plan de base de la boite doit etre le plan xOy. On donne donc uniquement les 2 vecteurs **normaux**
#        aux 2 autres plans, et les 3 longueurs des aretes principales.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BOITE_GENERALE = OPER (nom="BOITE_GENERALE", op=0, sd_prod=BoiteGenerale, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme parallelepipedique quelconque",
  ang = "Definition of a general box form",
  VecteursDirecteurs = SIMP (typ=Vecteur,min=2,max=2,statut='o',fr="Vecteurs normaux aux faces non horizontales de la boite"),
  Cotes              = SIMP (typ='R'    ,min=3,max=3,statut='o',fr="Longueurs des Cotes de la boite en cm")
 ) ;  # Fin BOITE_GENERALE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CYLINDRE_X : Classe de definition d'une forme cylindrique d'axe parallele a Ox
#         Pour tous les cylindres, la donnee de deux rayons transforme le cylindre circulaire en cylindre elliptique
#         La donnee d'un angle limite le cylindre a ce secteur
#         Pour un secteur d'un cylindre elliptique, il est necessaire de donner en plus l'angle de depart du secteur
#         par rapport a l'axe majeur de l'ellipse
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CYLINDRE_X = OPER (nom="CYLINDRE_X", op=0, sd_prod=CylindreX, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme cylindrique d'axe parallele a Ox",
  ang = "Definition of a right cylinder form // Ox",
  Rayons  = SIMP (typ='R', max=2, statut='o', fr="Rayons mineur et majeur du cylindre X en cm"),
  Hauteur = SIMP (typ='R',        statut='f', fr="Hauteur du cylindre X en cm"),
  Angles  = SIMP (typ='R', max=2, statut='f', fr="Angles du secteur du cylindre X en degres")
 ) ;  # Fin CYLINDRE_X
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CYLINDRE_Y : Classe de definition d'une forme cylindrique d'axe parallele a Oy
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CYLINDRE_Y = OPER (nom="CYLINDRE_Y", op=0, sd_prod=CylindreY, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme cylindrique d'axe parallele a Oy",
  ang = "Definition of a right cylinder form // Oy",
  Rayons  = SIMP (statut='o',typ='R',max=2,fr="Rayons mineur et majeur du cylindre Y en cm"),
  Hauteur = SIMP (statut='f',typ='R',      fr="Hauteur du cylindre Y en cm"),
  Angles  = SIMP (statut='f',typ='R',max=2,fr="Angles du secteur du cylindre Y en degres")
 ) ;  # Fin CYLINDRE_Y
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CYLINDRE_Z : Classe de definition d'une forme cylindrique d'axe parallele a Oz
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CYLINDRE_Z = OPER (nom="CYLINDRE_Z", op=0, sd_prod=CylindreZ, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme cylindrique d'axe parallele a Oz",
  ang = "Definition of a right cylinder form // Oz",
  Rayons  = SIMP (statut='o',typ='R',max=2,fr="Rayons mineur et majeur du cylindre Z en cm"),
  Hauteur = SIMP (statut='f',typ='R',      fr="Hauteur du cylindre Z en cm"),
  Angles  = SIMP (statut='f',typ='R',max=2,fr="Angles du secteur du cylindre Z en degres")
 ) ;  # Fin CYLINDRE_Z
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CYLINDRE : Classe de definition d'une forme cylindrique quelconque
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CYLINDRE = OPER (nom="CYLINDRE", op=0, sd_prod=Cylindre, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme cylindrique quelconque",
  ang = "Definition of a general cylinder form",
  Rayons     = SIMP (statut='o',typ='R',max=2,fr="Rayons mineur et majeur du cylindre en cm"),
  VecteurAxe = SIMP (statut='o',typ=Vecteur,  fr="Vecteur directeur de l'axe du cylindre"),
  Hauteur    = SIMP (statut='f',typ='R',      fr="Hauteur du cylindre en cm"),
  Angles     = SIMP (statut='f',typ='R',max=2,fr="Angles du secteur du cylindre en degres")
 ) ;  # Fin CYLINDRE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONE : Classe de definition d'un forme conique
#           Une portion de cone peut etre definie en donnant les cotes axiales (origine de l'axe du cone au sommet du cone) de
#           la zone retenue
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONE = OPER (nom="CONE", op=0, sd_prod=Cone, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme conique",
  ang = "Definition of a conic form",
  DemiAngleSommet = SIMP (statut='o',typ='R',            fr="Demi-angle au sommet en degres"),
  LimitesAxiales  = SIMP (statut='f',typ='R',min=2,max=2,fr="Limites axiales du cone"),
  VecteurAxe      = SIMP (statut='o',typ=Vecteur,        fr="Vecteur directeur de l'axe du cone")
 ) ;  # Fin CONE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PRISME_HEXAGONAL : Classe de definition d'une forme de prisme hexagonal 3D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PRISME_HEXAGONAL = OPER (nom="PRISME_HEXAGONAL",op=0,sd_prod=PrismeHexagonal,
                           niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme de prisme hexagonal 3D",
  ang = "Definition of a 3D hexagonal form",
  Rayon      = SIMP (statut='o',typ='R',    fr="Rayon du cercle circonscrit (=cote de l'hexagone) en cm"),
  Hauteur    = SIMP (statut='f',typ='R',    fr="Hauteur de l'hexagone en cm"),
  VecteurAxe = SIMP (statut='o',typ=Vecteur,fr="Vecteur directeur de l'axe de l'hexagone")
 ) ;  # Fin PRISME_HEXAGONAL
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe TORE : Classe de definition d'une forme toroidale
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TORE = OPER (nom="TORE",op=0,sd_prod=Tore,
               niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme toroidale",
  ang = "Definition of a toroidal form",
  Rayons = SIMP (typ='R',min=2,max=2,statut='o',
                 fr="Rayons du tore : 1/2 distance a l'axe et rayon de la section du tore en cm")
 ) ;  # Fin TORE
# ==================================================================================================================================
#               Definition des Classes pour une geometrie 3D : Elements geometriques surfaciques
# ==================================================================================================================================
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe PLAN : Classe de definition d'un plan
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PLAN = OPER (nom="PLAN", op=0, sd_prod=Plan, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un plan ax + by + cz + d = 0",
  ang = "Definition of a plane surface ax + by + cz + d = 0",
  regles = (UN_PARMI ('Points','Equation'),),
  Points   = SIMP (typ=Point,min=3,max=3,statut='f',fr="Donnee de 3 points non alignes"),
  Equation = SIMP (typ='R'  ,min=2,max=4,statut='f',fr="Coefficients successifs abcd de l'equation du plan")
 ) ;  # Fin PLAN
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe PLAN_X : Classe de definition d'un plan perpendiculaire a l'axe Ox
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PLAN_X = OPER (nom="PLAN_X", op=0, sd_prod=PlanX, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un plan perpendiculaire a Ox",
  ang = "Definition of a plane surface perpendicular to Ox",
  Cote = SIMP (typ='R',statut='o',fr="Cote du plan // OyOz")
 ) ;  # Fin PLAN_X
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe PLAN_Y : Classe de definition d'un plan perpendiculaire a l'axe Oy
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PLAN_Y = OPER (nom="PLAN_Y", op=0, sd_prod=PlanY, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un plan perpendiculaire a Oy",
  ang = "Definition of a plane surface perpendicular to Oy",
  Cote = SIMP (typ='R',statut='o',fr="Cote du plan // OxOz")
 ) ;  # Fin PLAN_Y
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe PLAN_Z : Classe de definition d'un plan perpendiculaire a l'axe Oz
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PLAN_Z = OPER (nom="PLAN_Z", op=0, sd_prod=PlanZ, niveau = 'ElementsGeometriques',
  fr  = "Definition d'un plan perpendiculaire a Oz",
  ang = "Definition of a plane surface perpendicular to Oz",
  Cote = SIMP (typ='R',statut='o',fr="Cote du plan // OxOy")
 ) ;  # Fin PLAN_Z
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POLYEDRE : Classe de definition d'une forme polyhedrique 3D quelconque (N faces, N > 4)
#                    Definition surfacique : Donnee des N plans et du choix du cote positif ou negatif
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POLYEDRE = OPER (nom="POLYEDRE", op=0, sd_prod=Polyedre, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme polyhedrique 3D quelconque ",
  ang = "Definition of a 3D polyhedron form with N > 4 plane faces",
  Plans = NUPL (min = 5, max = '**', statut = 'o', fr = "Surfaces planes limites du polyedre",
      elements = (SIMP (typ=(Plan,PlanX,PlanY,PlanZ)   ,fr="Plans limites du polyedre"),
                  SIMP (typ='TXM',into=('Plus','Moins'),fr="Choix du cote positif ou negatif de l'espace")))
  ) ;  # Fin POLYEDRE
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe QUADRIQUE : Classe de definition d'une quadrique 3D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
QUADRIQUE = OPER (nom="QUADRIQUE", op=0, sd_prod=Quadrique, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une quadrique 3D ax2+by2+cz2+dxy+eyz+fxz+gx+hy+iz+j=0",
  ang = "Definition of a quadratic curve 3D ax2+by2+cz2+dxy+eyz+fxz+gx+hy+iz+j=0",
  Equation = SIMP (typ='R',min=2,max=10,statut='o',fr="Coefficients successifs abcdefghij de l'equation d'une quadrique")
 ) ;  # Fin QUADRIQUE
# -----------------------------------------------------------------------------------------------------------------------------------
#   Classe CELLULE : Classe de definition d'une cellule (ensemble elementaire  de regions annulaires et sectorisees)
#   Apres la hauteur de la cellule, entree des donnees par listes successives pour l'ensemble des couronnes de la
#   cellule, la zone externe etant decrite a part dans l'attribut FormeTechnologique :
#   - Liste des materiaux
#   - Liste des rayons des couronnes correspondantes
#   - Liste des sous-couronnes : - Numero de couronne a discretiser (Numero 1 a partir du centre),
#                                - Nombre de sous-couronnes,
#                                - Mot-cle Equivolumique si decoupage en sections transverses egales,
#                                - Rayons des couronnes intermediaires ou proportions volumiques si mot-cle Proportions indique anterieurement.
#   - Liste des sectorisations : - Nom de couronne a sectoriser ,
#                                - Nombre de secteurs,
#                                - Mot-cle Equivolumique si decoupage en secteurs egaux et positionnement du premier
#                                  secteur par rapport a l'axe x, et pas de changement de composition du secteur,
#                                - Mot-cle alternatif Angle si on veut modifier ou positionner les secteurs dans la
#                                  couronne : on donne alors des triplets de donnees pour chaque secteur :
#                                - nom du materiau composant le le secteur,
#                                - position trigonometrique en degres du debut du secteur
#                                - et angle en degres du secteur.
#     Le trace des secteurs sont definis en partant du centre de la couronne.
#     Pour la sectorisation de la forme externe, deux cas se presentent :
#     - soit pas de couronnes internes : les secteurs se tracent alors en partant du centre de la forme externe,
#     - dans le cas contraire, les secteurs partent du centre des couronnes.
#     Les secteurs peuvent ne pas couvrir l'ensemble de la couronne.
#   - Pour la zone peripherique, on doit definir les cotes de la cellule (cas cartesien), son materiau, sa
#     discretisation, et le decentrage du centre des couronnes par rapport au centre de ce contour peripherique
#     (Coordonnees x,y du centre des couronnes / au centre du contour)
#   - Pour le moment, limitation a 2D, sauf la donnee optionnelle des positions axiales des couronnes
#   - Une cellule peut etre definie a partir d'une cellule d'un autre assemblage antérieurement calcule
#   - Cette classe sert aussi a definir des microstructures (double heterogeneite) a inclure dans des regions
#     d'autres cellules d'ou les attributs relatifs aux microstructures (une microstructure étant une petite cellule
#     cylindrique ou spherique a disseminer dans des regions particulieres d'une cellule de taille plus importante
#     dans des proportions fixees par l'attribut ProportionsMicroStructures
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CELLULE = OPER (nom="CELLULE", op=0, sd_prod=Cellule, niveau = 'Geometries',
  fr  = "Definition d'une cellule elementaire",
  ang = "Definition of a basic cell",
  regles = (UN_PARMI ('Couronnes', 'CelluleIrradiee'),),
  Type = SIMP (typ='TXM',defaut='Combustible',
               into=( 'Combustible','BarreGrise','BarreNoire','BarreAcier','BarreAic','BarreB4c',
                      'Detecteur','Trou','TubeGuide','Postiche','Pyrex','ExPyrex','Gadolinium',
                      'CellType1','CellType2','CellType3'),statut='o'),
  HauteurTotale  = SIMP (typ='R',defaut=1.,statut='o',fr="Hauteur totale de la cellule"),
  Cluster        = SIMP (typ=Cluster,statut='f',fr="Cluster a integrer dans la cellule de base en cm"),
  TypeGeometrie  = SIMP (typ='TXM',defaut='Cylindrique',statut='o',into=('Cylindrique','Spherique'),fr="Type de geometrie de la cellule"),
  Couronnes      = FACT (statut='f',fr="Definition des couronnes cylindriques physiques de materiaux",
        NomsSymboliques = SIMP (typ='TXM',    max='**',statut='o',fr="Liste des noms arbitraires des couronnes"),
        Materiaux       = SIMP (typ=Materiau, max='**',statut='o',fr="Liste des materiaux des couronnes"),
        Temperatures    = SIMP (typ='R',      max='**',statut='f',fr="Liste des temperatures des couronnes en Celsius"),
        PressionGaz     = SIMP (typ='R',               statut='f',fr="Valeur de pression de gaz (en bars)"),
        Rayons          = SIMP (typ='R',      max='**',statut='o',fr="Liste des rayons des couronnes en cm"),
        RayonsMineurs   = SIMP (typ='R',      max='**',statut='f',fr="Liste des rayons mineurs des couronnes elliptiques en cm"),
        Hauteurs        = SIMP (typ='R',      max='**',statut='f',fr="Liste des hauteurs des couronnes en cm"),
        AxialPositions  = SIMP (typ='R',     max='**',statut='f',
                                fr="Positions axiales de la base des couronnes en cm / au zero de la hauteur maximum")
                         ),
  MicroStructures  = FACT (max = '**', statut = 'f',fr="Chargement de la double heterogeneite dans chaque couronne",
        NomCouronne     = SIMP (typ='TXM',statut='o',fr="Nom symbolique de la couronne ou inserer des microstructures"),
        MicroStructures = SIMP (typ=Cellule,max='**',statut='o',fr="Liste des microstructures dans la couronne"),
        ProportionsMicroStructures = SIMP (typ='R',max='**',statut='o',fr="Proportions des microstructures dans la couronne")
                         ),
  SousCouronnes  = FACT (max = '**', statut = 'f',fr="Discretisation des couronnes de la cellule",
        NomCouronne        = SIMP (typ='TXM',statut='o',fr="Nom symbolique de la couronne"),
        NbSousCouronnes    = SIMP (typ='I'  ,statut='o',fr="Nombre de sous-couronnes de discretisation"),
        TypeDiscretisation = SIMP (typ='TXM',defaut='Equivolumique',statut='o',into=('Equivolumique','Proportions','Equidistant')),
        BlocProportions    = BLOC (condition = "TypeDiscretisation=='Proportions'",
                             ProportionsVolumiques = SIMP (typ='R',statut='o',max='**',fr="Proportions volumiques des sous-couronnes")),
        ProfilTemperature  = SIMP (typ='R',max='**',statut='f',fr="Profil de temperature")
                         ),
  Homogeneisation = FACT (max = '**', statut = 'f', fr="Homogeneisation de couronnes de la cellule",
        NomCouronne    = SIMP (typ='TXM'          , fr="Nom arbitraire de la couronne homogeneisee"),
        ListeCouronnes = SIMP (typ='TXM',max='**' , fr="Liste des noms des couronnes jointives a homogeneiser")
                          ),
  Secteurs     = FACT (max = '**', statut = 'f', fr="Sectorisation des couronnes de la cellule",
        NomCouronne       = SIMP (typ='TXM',statut='o',fr="Nom de la couronne ou de la forme externe a sectoriser"),
        NbSecteurs        = SIMP (typ='I'  ,statut='o',fr="Nombre de secteurs de la couronne"),
        TypeSectorisation = SIMP (typ='TXM',statut='o',defaut='Coins',into=('Equivolumique','Angle','Coins','MilieuxCotes')),
        AngleDepart       = SIMP (typ='R'  ,statut='o',defaut=0.,fr="Angle en degres de depart des secteurs (Origine 0 sur l'axe Ox)"),
        Sectorisation     = FACT (statut       = 'f',
                                  Materiaux    = SIMP (typ=Materiau,       max='**',statut='f',fr="Materiau des secteurs"),
                                  Temperatures = SIMP (typ=('R','I','TXM'),max='**',statut='f',fr="Temperature des secteurs en Celsius"),
                                  Angles       = SIMP (typ='R',            max='**',statut='f',fr="Angles en degres des secteurs")
                                                )
                       ),
  FormeExterne = FACT (statut='f',fr="Definition de la region externe au systeme cylindrique interne",
        NomSymbolique = SIMP (typ='TXM',statut='f',fr="Nom arbitraire de la zone externe"),
        Type          = SIMP (typ    = (ArcCercle,Carre,Rectangle,Hexagone,Triangle,Polygone),
                              statut = 'f',  # la donnee est facultative si la cellule est inserree dans un reseau
                              fr     = "Forme geometrique exterieure"),
        Materiau      = SIMP (typ=(Materiau,Cellule),fr="Materiau de la forme externe"),
        MicroStructures = SIMP (typ=Cellule,max='**',statut='f',fr="Microstructures de la region externe"),
        ProportionsMicroStructures = SIMP (typ='R',max='**',statut='f',
                                           fr="Proportions des microstructures dans la region externe"),
        Temperature   = SIMP (typ='R',fr="Temperature en Celsius du materiau de la forme externe"),
        PressionGaz   = SIMP (typ='R',statut='f',fr="Valeur de pression de gaz (en bars)"),
        Decentrement  = SIMP (typ    = 'R',
                              min    = 2,
                              max    = 3,
#                             defaut = (0.,0.,0.),
                              statut = 'f',
                              fr     = "Coordonnees xyz du centre des couronnes / barycentre du contour") ),
  CelluleIrradiee = FACT (statut='f',fr="Utilisation d'une cellule irradiee d'un assemblage existant",
        AssemblageOrigine  = SIMP (typ=(AssemblageType,AssemblageCombustibleReel),statut='o',
                                   fr="Assemblage d'origine de la cellule a extraire"),
        IrradiationMoyenne = SIMP (typ='R',statut='o',fr="Irradiation moyenne MWj/t de l'assemblage d'origine"),
        Position           = SIMP (typ='I', min=2, max=2, statut='o',
                                   fr="Coordonnees entieres ix,jy du crayon a extraire de l'assemblage") )
 ) ;  # Fin CELLULE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CLUSTER : Classe de definition d'un cluster de cellules
#                   Un cluster est defini comme une superposition centree de cadrans telephoniques (a l'ancienne mode), chaque
#                   cadran ayant des trous de tailles differentes, l'ensemble devant etre dispose ensuite dans une cellule de forme
#                   quelconque.
#                   Donnees de Positionnement des couronnes de canaux, chaque canal etant une CELLULE predefinie,
#                   Pour chaque type de cellule, on donne :
#                   - le nombre de cellules a positionner (de maniere uniformement repartie sur le cercle)
#                   - le rayon du cercle sur lequel on les positionne
#                   - l'angle / Ox du centre de la premiere cellule (en degres)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CLUSTER = OPER (nom="CLUSTER", op=0, sd_prod=Cluster, niveau = 'Geometries',
  fr  = "Definition d'un cluster de cellules cylindriques",
  ang = "Definition of a cylindrical cell cluster",
  Hauteur          = SIMP (typ='R',defaut=1.,statut='f',fr="Hauteur du cluster"),
  Couronnes        = FACT (statut='o',fr="Definition des couronnes de cellules",min=1,
      Cellules   = SIMP (typ=Cellule,max='**',statut='o',fr="Liste des types de cellules sur chaque cercle"),
      NbCellules = SIMP (typ='I'    ,max='**',statut='o',fr="Liste des nombres de cellules de chaque type sur chaque cercle"),
      Rayons     = SIMP (typ='R'    ,max='**',statut='o',fr="Liste des rayons des cercles correspondants en cm"),
      Angles     = SIMP (typ='R'    ,max='**',statut='o',fr="Liste des angles de positionnement / Ox de la premiere cellule de chaque type"))
 ) ;  # Fin CLUSTER
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ORIENTATION :         Classe de definition d'une orientation angulaire dans un plan 2D apres symetrie eventuelle / Ox
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ORIENTATION = OPER (nom="ORIENTATION", op=0, sd_prod=Orientation, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une orientation d'un reseau ou d'une cellule",
  ang = "Definition of a cell or lattice orientation",
  Symetrie       = SIMP (typ=(Plan,PlanX,PlanY,PlanZ),statut='f',
                         fr="Indication d'une operation de symetrie / Plan, avant rotation"),
  AngleRotation  = SIMP (typ='R'    ,statut='f',fr="Angle de rotation en degres",defaut=0.),
  CentreRotation = SIMP (typ=Point  ,statut='f',fr="Centre de rotation"),
  AxeRotation    = SIMP (typ=Vecteur,statut='f',fr="Vecteur de l'axe de rotation")
 ) ;  # Fin ORIENTATION
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe FORME_POSITIONNEE :   Classe de definition d'une forme geometrique positionnee
#                               La position est definie a l'aide du centre de la forme geometrique,
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
FORME_POSITIONNEE = OPER (nom="FORME_POSITIONNEE", op=0, sd_prod=FormePositionnee, niveau = 'ElementsGeometriques',
  fr  = "Definition d'une forme positionnee",
  ang = "Definition of a shape and its position",
  Forme = SIMP (
      typ    = (Sphere,BoiteRectangulaire,BoiteGenerale,CylindreX,CylindreY,CylindreZ,Cylindre,SecteurDisque,Cone,
                Carre,Rectangle,Triangle,Hexagone,Polygone,PrismeHexagonal,Tore,Polyedre,Cellule,Cluster),
      statut = 'o',
      fr     = "Forme geometrique de base a positionner"),
  PositionCentre   = SIMP (typ=Point      ,statut='o',fr="Coordonnees du centre de la forme geometrique"),
  OrientationForme = SIMP (typ=Orientation,statut='f',fr="Orientation de la forme")
 ) ;  # Fin FORME_POSITIONNEE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe GEOMETRIE_SURFACIQUE : Classe de definition d'une geometrie surfacique
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GEOMETRIE_SURFACIQUE = OPER (nom="GEOMETRIE_SURFACIQUE", op=0, sd_prod=GeometrieSurfacique, niveau = 'Geometries',
  fr  = "Definition d'une geometrie surfacique",
  ang = "Definition of a surfacic geometry",
  MateriauRemplissage = SIMP (typ=Materiau,statut='o',fr="Materiau de remplissage de la geometrie surfacique"),
  Surfaces      = NUPL (
      max      = '**',
      statut   = 'o',
      fr       = "Serie de couples (Surface,Plus ou Moins) definissant les surfaces limites de la geometrie",
      elements = (
          SIMP (typ=(PlanX,PlanY,PlanZ,Plan,CylindreX,CylindreY,CylindreZ,Cylindre,Sphere,Cone,Conique,Quadrique)),
          SIMP (typ='TXM',into=('Plus','Moins'))))
 ) ;  # Fin GEOMETRIE_SURFACIQUE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe GEOMETRIE_COMBINATOIRE : Classe de definition d'une geometrie combinatoire
#                                  Ecrasement : Constitution par ecrasements successifs (dans l'ordre des donnees) de la
#                                               Geometrie Initiale, la frontiere externe etant celle de la geometrie initiale
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GEOMETRIE_COMBINATOIRE = OPER (nom="GEOMETRIE_COMBINATOIRE", op=0, sd_prod=GeometrieCombinatoire, niveau = 'Geometries',
  fr  = "Definition d'une geometrie combinatoire",
  ang = "Definition of a combinatorial geometry",
  GeometriePremierPlan  = SIMP (typ=FormePositionnee,statut='o',fr="Geometrie se trouvant au premier plan"),
  GeometrieEcrasee      = SIMP (typ=FormePositionnee,max='**',statut='f',
                                fr="Geometries ecrasées et surchargées par la GeometriePremierPlan"),
  GeometrieUnion        = SIMP (typ=FormePositionnee,max='**',statut='f',
                                fr="Geometries a reunir a la GeometriePremierPlan en gardant les interfaces, les intersections etant des volumes particuliers"),
  GeometrieReunion      = SIMP (typ=FormePositionnee,max='**',statut='f',
                                fr="Geometries a reunir a la GeometriePremierPlan pour former un volume unique"),
  GeometrieIntersection = SIMP (typ=FormePositionnee,max='**',statut='f',
                                fr="Geometries a intersecter avec la GeometriePremierPlan")
 ) ;   # Fin GEOMETRIE_COMBINATOIRE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CORRESPONDANCE_REPERE_POSITION_RESEAU :
#  Classe de definition des reperes alphanumeriques des cases d'un reseau
#  Reperes (bataille navale ou autre) et Coordonnees cartesiennes entieres des cases dans un systeme i,j du reseau
#  Origine des coordonnees en bas a gauche d'un systeme en xy
#  Ceci n'a d'interet que pour l'utilisateur ou pour se conformer aux reperes industriels habituels dans le cas des REP
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CORRESPONDANCE_REPERE_POSITION_RESEAU = OPER (nom="CORRESPONDANCE_REPERE_POSITION_RESEAU",op=0,sd_prod=CorrespondanceReperePositionReseau,
                                              niveau = 'Geometries',
  fr  = "Correspondance entre reperes alphanumeriques et cases d'un reseau",
  ang = "Alphanumeric identificators and lattice coordinates",
  Positions = NUPL (max='**',statut='o',
                    elements=(SIMP (typ='TXM',fr="Repere alphanumerique arbitraire d'une case du reseau"),
                              SIMP (typ='I'  ,fr="Premiere Coordonnee entiere dans le systeme i,j du reseau"),
                              SIMP (typ='I'  ,fr="Seconde Coordonnee entiere dans le systeme i,j du reseau")))
 ) ;  # Fin CORRESPONDANCE_REPERE_POSITION_RESEAU
# -----------------------------------------------------------------------------------------------------------------------------------
# Classe RESEAU :
#   Classe de definition d'un reseau de juxtapositions de cellules ou de reseaux
#   Assemblage de cellules ou de reseaux dans une grille rectangulaire ou hexagonale
#   Les positions des cellules et des reseaux dans le nouveau reseau sont a fournir sur les mailles
#   du reseau sans tenir compte des symetries,
#   Le reseau peut etre charge :
#     - de maniere uniforme : un seul type de CELLULE ou de RESEAU
#     - de maniere complete : a chaque maille doit etre affecte un reseau ou une cellule et optionnellement son
#       orientation, l'ordre des donnees dans le plan radial etant celui obtenu en partant de l'element le plus
#       bas a gauche, et dans le sens axial ensuite (eventuellement si 3D)
#     - de maniere partielle : liste des cellules et reseaux charges et leur position xyz dans le nouveau reseau
#       et orientations correspondantes de ces cellules et reseaux
#   Des reperes alphanumeriques arbitraires peuvent etre associes a chaque maille du reseau, ce qui permet
#   si necessaire de manipuler ces elements du reseau par l'intermediaire de ces symboles (exemple des
#   reperes bataille navale des assemblages dans le reseau d'un coeur REP).
#   Le reseau peut etre entoure de zones peripheriques homogenes ou heterogenes.
#     - Le cas Homogene peut s'appliquer aux reseaux hexagonaux ou cartesiens ;
#     - Dans le cas Heterogene, la reflexion s'est uniquement portee sur la situation cartesienne et particulierement en donnant la
#       la possibilite de decrire un assemblage bouillant (avec croix de contrôle et instrumentation)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESEAU = OPER (nom="RESEAU", op=0, sd_prod=Reseau, niveau = 'Geometries',
  fr  = "Definition d'un reseau compose de juxtapositions de cellules, de reseaux ou d'assemblages",
  ang = "Definition of a lattice",
  Identificateur          = SIMP (typ='TXM',statut='o',fr="Identificateur arbitraire du reseau"),
  ReseauReference         = SIMP (typ='TXM',statut='f',fr="Identificateur du reseau de reference dans le cas d'une composition de reseaux de reseau"),
  DifferenciationCellules = SIMP (typ='I',defaut=0,statut='f',fr="Nombre de couches de cellules a differencier autour du reseau de reference"),
  TypeGeometrie           = SIMP (typ='TXM',into=('cartesienne','hexagonale'),defaut='cartesienne',statut='f'),
  NbMaillesX              = SIMP (typ='I',defaut=17,statut='o',fr="Nbre de mailles sur le premier axe du reseau"),
  NbMaillesY              = SIMP (typ='I',defaut=17,statut='f',fr="Nbre de mailles sur le second axe du reseau"),
  NbMaillesZ              = SIMP (typ='I',defaut=1 ,statut='f',fr="Nbre de mailles sur l'axe vertical du reseau"),
  PasReseau               = SIMP (typ='R',defaut=1.26 ,statut='f',max=2,fr="Pas du reseau en X et Y (en cm)"),
  MateriauRemplissage     = SIMP (typ=Materiau,defaut='ModExt',statut='f',fr="Materiau de remplissage du reseau"),
  TypeDefinition          = SIMP (typ='TXM',statut='f',defaut="Complet",into=("Uniforme","Complet","Partiel"),fr="Mode de chargement du reseau"),
  ReseauUniforme          = BLOC (condition = "TypeDefinition=='Uniforme'",fr="Chargement uniforme du reseau",
       ElementGeomU       = SIMP (typ=(Cellule,Reseau,Cluster,GeometrieCombinatoire,AssemblageCombustibleReel,AssemblageType),statut='o',
                                  fr = "Remplissage uniforme du nouveau reseau par un element particulier"),
       OrientationU       = SIMP (typ=Orientation,fr="Orientation de l'element geometrique de base",statut='f')),
  ReseauComplet           = BLOC (condition = "TypeDefinition=='Complet'",fr="Chargement complet du reseau",
        ElementsGeomC     = NUPL (max='**', statut='o',
                                  fr="Liste des couples (ElementGeometrique,SigleTextuel) les sigles textuels servant ensuite au chargement complet du reseau",
                elements  =(SIMP (typ=(Cellule, Reseau, GeometrieCombinatoire, GeometrieSurfacique, AssemblageCombustibleReel,AssemblageType),
                                  fr="Element geometrique a associer au sigle"),
                            SIMP (typ='TXM',fr="Sigle alphanumerique associe a l'element geometrique"))),
        ChargementC       = SIMP (typ='TXM',statut='o',max='**',
                                  fr="Affectation des sigles aux cases geometriques du reseau"),
        RegroupementC     = SIMP (typ='I',statut='f',max='**',
                                  fr="Numeros des cellules de calcul en approximation multicellule dans chaque case du reseau"),
        OrientationC      = SIMP (typ=Orientation,max='**',statut='f',fr="Orientation des elements geometriques dans les cases du reseau"),
        ReperesC          = SIMP (typ='TXM',max='**',statut='f',fr="Reperes arbitraires des cases geometriques"),
                                ),
  ReseauPartiel           = BLOC (condition = "TypeDefinition=='Partiel'",fr="Chargement partiel du reseau",
        ChargementP       = FACT (max='**',fr="Chargement partiel du reseau",
                regles = (UN_PARMI ('ElementsPositionnesP', 'ElementsReperesP'),),
                ElementsPositionnesP = NUPL (max='**', statut='f',fr="Donnee des Positions des elements geometriques dans le systeme des coordonnees du reseau",
                        elements=(SIMP (typ=(Cellule, Reseau, GeometrieCombinatoire, GeometrieSurfacique, AssemblageCombustibleReel,AssemblageType),
                                        fr="Element geometrique a positionner"),
                                  SIMP (typ='I',min=2,max=2,fr="Coordonnees i j de l'element geometrique dans le reseau"))),
                ElementsReperesP    = NUPL (max='**', statut='f',fr="Donnee des reperes positionnels des elements geometriques",
                        elements=(SIMP (typ=(Cellule, Reseau, GeometrieCombinatoire, GeometrieSurfacique, AssemblageCombustibleReel,AssemblageType),
                                        fr="Element geometrique a positionner"),
                                  SIMP (typ='TXM',fr="Repere alphanumerique de l'element geometrique"))),
                CorrespondanceReperePositions = SIMP (typ=CorrespondanceReperePositionReseau,
                                                      statut='f',
                                                      fr="Correspondance entre Repere alphanumerique et coordonnees dans le reseau"),
                OrientationP = SIMP (typ=Orientation,max='**',statut='f',fr="Orientation des elements geometriques du chargement partiel"),
                             )),
  ZonesPeripheriquesHomogenes      = FACT (statut='f',fr="Zones homogenes peripheriques au reseau",
        Epaisseurs      = SIMP (typ='R'     ,max='**',statut='o',fr="Liste des epaisseurs (cm) des couches peripheriques"),
        Materiaux       = SIMP (typ=Materiau,max='**',statut='f',fr="Liste des materiaux des couches peripheriques"),
        MateriauExterne = SIMP (typ=Materiau         ,statut='f',fr="Materiau de remplissage de la zone externe du reseau hexagonal")),
  ZonesPeripheriquesHeterogenes  = FACT (max='**',statut='f',fr="Zones heterogenes peripheriques au reseau",
        DimensionsExternes = SIMP (typ='R',min=2,max=2,	statut='o',
                                   fr=" Dimensions (cm) externes X et Y zone peripherique comprise"),
        Decentrement = SIMP (typ='R',min=2,max=2,	statut='f',
                             fr=" Coordonnees (cm) X et Y du centre de la zone peripherique / au centre du réseau"),
        MateriauRemplissage = SIMP (typ=Materiau,	statut='f',
                                    fr="Materiau de remplissage de la zone"),
        Boitier = FACT (statut='f',fr="Definition d'un boitier",
                Epaisseur = SIMP (typ='R',statut='o',fr= "Epaisseur (cm) du boitier dans sa partie lineaire"),
                LongueurPartieLineaire  = SIMP (typ='R',statut='o',fr= "Longueur (cm) de la partie lineaire du boitier"),
                RayonExterneCoinBoitier = SIMP (typ='R',statut='o',fr= "Rayon externe (cm) du coin arrondi du boitier"),
                MateriauExterne = SIMP (typ=Materiau,statut='f',fr="Materiau de remplissage de la zone externe au boitier"),
                PositionBoitier = SIMP (typ='TXM',statut='o',defaut='Exterieure',into=('Exterieure','Interieure'),
                                        fr="Position du boitier dans la zone")),
        CroixControle = FACT (statut='f',fr="Definition d'une croix de controle",
                Epaisseur = SIMP (typ='R',statut='o',fr= "Epaisseur (cm) des branches de la croix de controle"),
                EpaisseurEnveloppe = SIMP (typ='R',statut='o',fr= "Epaisseur (cm) de l'enveloppe de la croix de controle"),
                DemiLongueurCroixCentrale = SIMP (typ='R',statut='o',
                                                  fr= "Demi-longueur (cm) de la partie homogene au centre de la croix de controle"),
                NombreBarres   = SIMP (typ='I',statut='o',fr= "Nombre de barres dans une aile de la croix de controle"),
                CellulesBarres = SIMP (typ=Cellule,max='**',statut='o',
                                       fr= "Liste des cellules correspondant aux barres de la croix de contrôle, en partant du centre de la croix"),
                MateriauCroix = SIMP (typ=Materiau,statut='o',fr="Materiau de la croix de controle"),
                BranchesCroix = SIMP (typ='TXM',statut='o',defaut='NordOuest',into=('NordOuest','NordEst','SudOuest','SudEst'),
                                      fr="Choix des deux branches de la croix de contrôle decrites"),
                PositionCroix = SIMP (typ='TXM',statut='o',defaut='AxeExterieure',into=('AxeExterieure','Exterieure','Interieure'),
                                      fr="Position de la croix dans la zone")),
        Instrumentation = FACT (statut='f',fr="Definition de l'instrumentation",
                Cellule  = SIMP (typ=Cellule,statut='o',fr= "Cellule decrivant la geometrie de l'instrumentation"),
                Position = SIMP (typ='TXM',statut='o',defaut='SudEst',into=('NordOuest','NordEst','SudOuest','SudEst'),
                                 fr="Choix du coin ou sera centree la cellule"))
                                )
 ) ;  # Fin RESEAU
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DECOMPOSITION_DOMAINES : Classe de definition de domaines de calcul
#                                  Pour le moment, on ne considere qu'une partition en 2D d'un reseau
#                                  (a completer ulterieurement pour une geometrie generale)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DECOMPOSITION_DOMAINES = OPER (nom="DECOMPOSITION_DOMAINES", op=0, sd_prod=DecompositionDomaines, niveau = 'Geometries',
  fr  = "Decomposition en domaines d'un reseau",
  ang = "Domain decomposition of a lattice",
  NbDomainesOx          = SIMP (statut='o', typ='I',		fr="Nombre de domaines sur l'axe Ox"),
  NbDomainesOy          = SIMP (statut='o', typ='I',		fr="Nombre de domaines sur l'axe Oy"),
  OxRepartitionDomaines = SIMP (statut='o', typ='I', max='**',	fr="Nombre de mailles du reseau pour chaque domaine de l'axe Ox"),
  OyRepartitionDomaines = SIMP (statut='o', typ='I', max='**',	fr="Nombre de mailles du reseau pour chaque domaine de l'axe Oy")
 ) ;  # Fin DECOMPOSITION_DOMAINES
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe GRILLE_ASSEMBLAGE : Classe de definition des grilles composant le squelette des assemblages combustibles
#                             Caracteristiques  technologiques (dimension, materiaux de composition) et positionnement simplifie
#                             des materiaux dans les canaux de l'assemblage pour dilution homogene a 2D dans le milieu peripherique.
#                               - Materiaux fournis sous forme de couples (nom de materiau et masse en g)
#                               - Repartition decrite en donnant pour une liste de materiaux (faisant partie des materiaux
#                                 precedemment indiques) la liste des types de cellules (precedee du mot-cle TypeCellule) et des
#                                 types de materiaux (precedes du mot-cle TypeMateriau) devant etre modifies par la presence des
#                                 grilles
#                                                    < liste de MATERIAU >,
#                                       TypeCellule  < liste de types de cellule >,
#                                       TypeMateriau < liste de types de materiau >
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GRILLE_ASSEMBLAGE = OPER (nom="GRILLE_ASSEMBLAGE", op=0, sd_prod=GrilleAssemblage, niveau = 'ElementsTechnologiquesAssemblages',
  fr  = "Definition d'une grille d'assemblage",
  ang = "Definition of an elementary assembly grid",
  TypeGrille     = SIMP (typ='TXM',defaut='GrilleMelange',statut='f',fr="Type de grille de structure assemblage"),
  Hauteur        = SIMP (typ='R',defaut=3.3,statut='f',fr="Hauteur de la grille de structure assemblage en cm"),
  Largeur        = SIMP (typ='R',defaut=21.338,statut='f',fr="Largeur de la grille de structure assemblage en cm"),
  MateriauxMasse = NUPL (max = '**', statut = 'o',
                         elements = (SIMP (typ=Materiau),SIMP (typ='R')),
                         fr       = "Serie de couples (Materiau,masse en g) de composition de la grille"),
  Repartition    = FACT (max = '**', statut = 'o',fr="Repartition des materiaux par type de cellule ou par type de materiau",
                         regles = (AU_MOINS_UN ('TypeCellule', 'TypeMateriau'),),
                         MateriauGrille = SIMP (typ=Materiau,fr="Nom du materiau a repartir",statut='o'),
                         TypeCellule    = SIMP (typ='TXM',max='**',statut='f',fr="Liste des types de cellule ou est reparti le materiau"),
                         TypeMateriau   = SIMP (typ='TXM',max='**',statut='f',fr="Liste des types de materiaux  ou est reparti le materiau") ),
  CoefficientsThermohydrauliques = FACT (statut = 'f',fr="Donnees de thermohydraulique",
      CoeffPerteCharge  = SIMP (typ='R',statut='f',
                                fr="Coefficient Cn de perte de charge au sens monodimensionnel de la singularite"),
      CoeffRedressement = SIMP (typ='R',statut='f',val_min=0,
                                fr="Coefficient R de redressement de l'ecoulement au passage de la singularite"),
      CoeffCkg          = SIMP (typ='R',statut='f',
                                fr="Coefficient lie au type de grille et de geometrie")),
  Ailettes = FACT (statut = 'f',fr="Donnees des ailettes de melange",
      PerteChargeSansAilettes       = SIMP (typ='R',statut='f',fr="Coefficient Cn de perte de charge monodimensionnel sans ailettes"),
      PerteChargeAvecAilettes       = SIMP (typ='R',statut='f',fr="Coefficient Cn de perte de charge avec ailettes"),
      CoeffRedressementSansAilettes = SIMP (typ='R',statut='f',val_min=0,
                                            fr="Coefficient R de redressement de l'ecoulement sans ailettes"),
      CoeffCkg                      = SIMP (typ='R',statut='f',fr="Coefficient lie au type de grille et de geometrie"),
      AngleOrientation              = SIMP (typ='R',statut='f',fr="Angle d'orientation des ailettes"),
      Repartition                   = SIMP (typ='TXM',max='**',into=('Rien','Droite','Gauche','Haut','Bas'),statut='f',
        fr="Positionnement des ailettes dans chaque quart de sous-canal (soit 4 donnees par sous-canal)"))
 ) ;  # Fin GRILLE_ASSEMBLAGE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PARTIE_INFERIEURE_ASSEMBLAGE_COMBUSTIBLE  :   Classe de definition de l'embout inferieur d'un assemblage combustible REP
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PARTIE_INFERIEURE_ASSEMBLAGE_COMBUSTIBLE = OPER (nom="PARTIE_INFERIEURE_ASSEMBLAGE_COMBUSTIBLE",op=0,sd_prod=PartieInferieureAssemblageCombustible,
                                                 niveau = 'ElementsTechnologiquesAssemblages',
  fr  = "Definition de la partie inferieure d'un assemblage combustible REP",
  ang = "Definition of the bottom part of a PWR fuel assembly",
  MateriauEmbout                            = SIMP (typ=Materiau,statut='f',fr="Materiau de l'embout inferieur",defaut='ACIER'),
  MasseBouchonInferieurCrayonCombustible    = SIMP (typ='R'     ,statut='o',fr="Masse (g) du bouchon inferieur du crayon combustible"),
  HauteurBouchonInferieurCrayonCombustible  = SIMP (typ='R'     ,statut='o',fr="Hauteur (cm) du bouchon inferieur du crayon combustible"),
  MateriauBouchonInferieurCrayonCombustible = SIMP (typ=Materiau,statut='f',fr="Materiau du bouchon inferieur du crayon combustible",defaut='ZIRCALOY'),
  MasseEmbout                               = SIMP (typ='R'     ,statut='o',fr="Masse (g) de l'embout inferieur"),
  EpaisseurPlaqueAdaptatrice                = SIMP (typ='R'     ,statut='o',fr="Epaisseur (cm) de la plaque adaptatrice de l'embout inferieur en cm"),
  LargeurPlaqueAdaptatrice                  = SIMP (typ='R'     ,statut='o',fr="Largeur (cm) de la plaque adaptatrice de l'embout inferieur"),
  TrousPlaqueAdaptatrice                    = NUPL (fr="Dimensions des trous de la plaque adaptatrice",
      max      = '**',
      statut   = 'o',
      elements = ( SIMP (typ='I'  ,statut='o',fr="Nombre de trous de taille definie ci-apres"),
                   SIMP (typ='TXM',statut='o',into=('Rayon','Cotes'),fr="Choix de la forme des trous, elliptique ou rectangulaire"),
                   SIMP (typ='R'  ,statut='o',min=2,max=2,fr="Rayons ou cotes (cm) des trous"),
                   SIMP (typ='TXM',statut='o',defaut='Hauteur',into=('Hauteur','Epaisseur'),fr="Mot-cle au choix"),
                   SIMP (typ='R'  ,statut='o',fr="Hauteur  (cm) des trous dans la plaque adaptatrice"))),
  JeuBouchonCombustiblePlaque = SIMP (typ='R',      statut='o',fr="Hauteur (cm) du jeu entre bouchon combustible et plaque adaptatrice"),
  HauteurPied                 = SIMP (typ='R',      statut='o',fr="Hauteur (cm) du pied de l'embout inferieur"),
  CapuchonRint                = SIMP (typ='R',      statut='f',fr="Rayon interne (cm) du capuchon"),
  CapuchonRext                = SIMP (typ='R',      statut='f',fr="Rayon externe (cm) du capuchon"),
  HauteurVisEpaulee           = SIMP (typ='R',      statut='f',fr="Hauteur des vis epaulees des tubes guides en cm"),
  MasseVisEpaulee             = SIMP (typ='R',      statut='f',fr="Masse totale des vis epaulees des tubes guides en g"),
  RintVisEpaulee              = SIMP (typ='R',      statut='f',fr="Rayon interne (cm) d'une vis epaulee"),
  RextVisEpaulee              = SIMP (typ='R',      statut='f',fr="Rayon externe (cm) d'une vis epaulee"),
  MasseFiltre                 = SIMP (typ='R',      statut='f',fr="Masse (g) du filtre anti-debris"),
  MateriauFiltre              = SIMP (typ=Materiau, statut='f',fr="Materiau du filtre anti-debris", defaut='INCONEL'),
  HauteurCale                 = SIMP (typ='R',      statut='f',fr="Hauteur (cm) de la cale dans le crayon combustible"),
  MateriauCale                = SIMP (typ=Materiau, statut='f',fr="Materiau de la cale dans le crayon combustible",defaut='ACIER'),
  RayonPionCentrage           = SIMP (typ='R',      statut='f',fr="Rayon externe des pions de centrage de la plaque inferieure coeur en cm"),
  HauteurPionCentrage         = SIMP (typ='R',      statut='f',fr="Hauteur des pions de centrage de la plaque inferieure coeur en cm"),
  HauteurOgivePionCentrage    = SIMP (typ='R',      statut='f',fr="Hauteur de l'ogive des pions de centrage de la plaque inferieure coeur en cm"),
  MateriauPionCentrage        = SIMP (typ=Materiau, statut='f',fr="Materiau des pions de centrage de la plaque inferieure coeur",defaut='ACIER'),
  BouchonTubGHauteur          = SIMP (typ='R',      statut='f',fr="Hauteur des bouchons des tubes guides en cm"),
  BouchonTubGMateriau         = SIMP (typ=Materiau, statut='f',fr="Materiau des bouchons des tubes guides",defaut='ACIER')
  ) ;  # Fin PARTIE_INFERIEURE_ASSEMBLAGE_COMBUSTIBLE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PARTIE_SUPERIEURE_ASSEMBLAGE_COMBUSTIBLE :    Classe de definition de l'embout superieur d'un assemblage combustible REP
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PARTIE_SUPERIEURE_ASSEMBLAGE_COMBUSTIBLE = OPER (nom="PARTIE_SUPERIEURE_ASSEMBLAGE_COMBUSTIBLE",op=0,sd_prod=PartieSuperieureAssemblageCombustible,
                                                   niveau = 'ElementsTechnologiquesAssemblages',
  fr  = "Definition de la partie superieure d'un assemblage combustible REP",
  ang = "Definition of the top part of a PWR fuel assembly",
  MateriauEmbout                             = SIMP (typ=Materiau, statut='f',fr="Materiau  de l'embout superieur",defaut='ACIER'),
  MasseBouchonSuperieurCrayonCombustible     = SIMP (typ='R',      statut='o',fr="Masse du bouchon superieur du crayon combustible en g"),
  HauteurBouchonSuperieurCrayonCombustible   = SIMP (typ='R',      statut='o',fr="Hauteur du bouchon superieur du crayon combustible en cm"),
  MateriauBouchonSuperieurCrayonCombustible  = SIMP (typ=Materiau, statut='f',fr="Materiau du bouchon superieur du crayon combustible",defaut='ZIRCALOY'),
  RessortCrayonCombustible                   = SIMP (typ='R',      statut='o',fr="Masse du ressort du crayon combustible en g"),
  ForceRessortCrayonCombustible              = SIMP (typ='R',      statut='f',fr="Force du ressort du crayon combustible en N"),
  HauteurChambreExpansion                    = SIMP (typ='R',      statut='o',fr="Hauteur de la chambre d'expansion en cm"),
  MasseEmbout                                = SIMP (typ='R',      statut='o',fr="Masse de l'embout superieur en g"),
  HauteurEmbout                              = SIMP (typ='R',      statut='o',fr="Hauteur de l'embout superieur en cm"),
  MasseRessortsEmbout                        = SIMP (typ='R',      statut='o',fr="Masse des ressorts de l'embout superieur en g"),
  MateriauRessortsEmbout                     = SIMP (typ=Materiau, statut='f',fr="Materiau des ressorts de l'embout superieur", defaut='INCONEL'),
  EpaisseurPlaqueAdaptatrice                 = SIMP (typ='R',      statut='o',fr="Epaisseur de la plaque adaptatrice en cm"),
  LargeurPlaqueAdaptatrice                   = SIMP (typ='R',      statut='o',fr="Largeur de la plaque adaptatrice en cm"),
  TrousPlaqueAdaptatrice                     = NUPL (fr="Dimensions des trous de la plaque adaptatrice",
      max      = '**',
      statut   = 'o',
      elements = (      SIMP (typ='I',					fr="Nombre de trous d'un type donne"),
                        SIMP (typ='TXM',into=('Rayon','Cotes'),		fr="Mot indiquant la donnee des rayons ou cotes des trous"),
                        SIMP (typ='R'  ,min=2,max=2,			fr="Rayons mineur et majeur ou Cotes du trou en cm"),
                        SIMP (typ='TXM',into=('Hauteur','Epaisseur'),	fr="Mot cle introduisant la hauteur des trous"),
                        SIMP (typ='R',					fr="Hauteur du trou en cm"))),
  JeuBouchonCombustiblePlaque = SIMP (typ='R',      statut='o',fr="Hauteur du jeu entre Bouchon combustible et Plaque adaptatrice en cm"),
  EpaisseurJupe               = SIMP (typ='R',      statut='o',fr="Epaisseur de la jupe de l'embout superieur en cm"),
  HauteurJupe                 = SIMP (typ='R',      statut='f',fr="Hauteur de la jupe de l'embout superieur en cm"),
  RayonPionCentrage           = SIMP (typ='R',      statut='f',fr="Rayon des pions de centrage superieurs en cm"),
  HauteurPionCentrage         = SIMP (typ='R',      statut='f',fr="Hauteur des pions de centrage superieurs en cm"),
  HauteurOgivePionCentrage    = SIMP (typ='R',      statut='f',fr="Hauteur de l'ogive des pions de centrage superieurs en cm"),
  MateriauPionCentrage        = SIMP (typ=Materiau, statut='f',fr="Materiau des pions de centrage superieurs",defaut='ACIER'),
  RayonInterneManchon         = SIMP (typ='R',      statut='f',fr="Rayon interne des manchons des tubes guides en cm"),
  RayonExterneManchon         = SIMP (typ='R',      statut='f',fr="Rayon externe des manchons des tubes guides en cm"),
  HauteurManchon              = SIMP (typ='R',      statut='f',fr="Hauteur des manchons des tubes guides en cm"),
  MasseManchon                = SIMP (typ='R',      statut='f',fr="Masse d'un manchon des tubes guides en g")
 ) ;  # Fin PARTIE_SUPERIEURE_ASSEMBLAGE_COMBUSTIBLE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ASSEMBLAGE_TYPE : Classe de definition d'un type d'assemblage (ensemble de crayons ou de reseaux quelconques)
#                           Rajout des structures grilles et embouts (dans le cas des REP)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ASSEMBLAGE_TYPE = OPER (nom="ASSEMBLAGE_TYPE",op=0,sd_prod=AssemblageType,
                          niveau = 'ElementsTechnologiquesAssemblages',
  fr  = "Definition d'un assemblage type et des elements associes eventuels",
  ang = "Definition of an assembly type and its associated elements",
  Geometrie         = SIMP (typ=(Cellule,Reseau,GeometrieCombinatoire),statut='o',max='**',
                            fr="Liste des geometries composant l'assemblage"),
  GrillesStructure  = NUPL (max = '**', statut = 'f',fr="Positions axiales des grilles",
                            elements = ( SIMP (typ=GrilleAssemblage,fr="Type de grille"),
                                         SIMP (typ='R',max='**',
                                               fr="Positions axiales des milieux des grilles (en cm) / a la limite inferieure du pied de l'assemblage"))),
  PartieInferieure  = SIMP (typ=PartieInferieureAssemblageCombustible,statut='f',fr="Type d'embout inferieur"),
  PartieSuperieure  = SIMP (typ=PartieSuperieureAssemblageCombustible,statut='f',fr="Type d'embout superieur"),
  ElementsAssocies  = SIMP (typ=(ElementsGrappeCommande,ElementsAbsorbantsFixes,GrappeBouchonAssemblage),max='**',statut='f',fr="Liste des elements technologiques associes")
 ) ;  # Fin ASSEMBLAGE_TYPE
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe ELEMENT_BARRE :	 Classe de définition d'une barre element d'un assemblage
#                         Definition des barres des grappes de commande (barre et gaine, et composants axiaux)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ELEMENT_BARRE = OPER (nom="ELEMENT_BARRE", op=0, sd_prod=ElementBarre, niveau = 'ElementsTechnologiquesAssemblages',
  fr  = "Definition d'une barre element d'un assemblage",
  ang = "Definition of an assembly rod element",
  MateriauInferieur    = SIMP (typ=Materiau,defaut='ACIER' ,statut='o',fr="Materiau composant la partie inferieure de la barre"),
  MateriauSuperieur    = SIMP (typ=Materiau,defaut='ACIER' ,statut='o',fr="Materiau composant la partie superieure de la barre"),
  HauteurBarre         = SIMP (typ='R'                     ,statut='o',fr="Hauteur (cm) de la barre"),
  HauteurInferieure    = SIMP (typ='R'                     ,statut='f',fr="Hauteur (cm) de la partie inferieure de la barre"),
  HauteurSuperieure    = SIMP (typ='R'                     ,statut='f',fr="Hauteur (cm) de la partie superieure de la barre"),
  RintPartieInferieure = SIMP (typ='R'     ,defaut=0.      ,statut='f',fr="Rayon Interne (cm) de la partie inferieure de la barre"),
  RintPartieSuperieure = SIMP (typ='R'     ,defaut=0.      ,statut='f',fr="Rayon Interne (cm) de la partie superieure de la barre"),
  RextPartieInferieure = SIMP (typ='R'                     ,statut='o',fr="Rayon Externe (cm) de la partie inferieure de la barre"),
  RextPartieSuperieure = SIMP (typ='R'                     ,statut='f',fr="Rayon Externe (cm) de la partie superieure de la barre"),
  MasseRessort         = SIMP (typ='R'                     ,statut='o',fr="Masse (g) du ressort de la barre"),
  MateriauRessort      = SIMP (typ=Materiau                ,statut='o',fr="Materiau du ressort de la barre"),
  HauteurRessort       = SIMP (typ='R'                     ,statut='o',fr="Hauteur (cm) du ressort de la barre"),
  BouchonInfHauteur    = SIMP (typ='R'     ,defaut=0.      ,statut='f',fr="Hauteur (cm) du bouchon inferieur de la barre"),
  BouchonSupHauteur    = SIMP (typ='R'     ,defaut=0.      ,statut='f',fr="Hauteur (cm) du bouchon superieur de la barre"),
  BouchonInfRayon      = SIMP (typ='R'     ,defaut=0.      ,statut='f',fr="Rayon externe (cm) du bouchon inferieur de la barre"),
  BouchonSupRayon      = SIMP (typ='R'     ,defaut=0.      ,statut='f',fr="Rayon externe (cm) du bouchon superieur de la barre"),
  MateriauGaine        = SIMP (typ=Materiau,defaut='ACIER' ,statut='o',fr="Materiau de la gaine externe de la barre"),
  RayonInterneGaine    = SIMP (typ='R'     ,defaut=0.      ,statut='f',fr="Rayon Interne (cm) de la gaine externe de la barre"),
  RayonExterneGaine    = SIMP (typ='R'     ,defaut=0.      ,statut='f',fr="Rayon Externe (cm) de la gaine externe de la barre")
 ) ;  # Fin ELEMENT_BARRE
#----------------------------------------------------------------------------------------------------------------------------------
#  Classe ELEMENTS_GRAPPE_COMMANDE : Classe de définition des éléments des grappes de commande
#                                    Association avec les différents types de barres absorbantes
#                                    Description simplifiée de l'araignée et du bouchon des barres
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ELEMENTS_GRAPPE_COMMANDE = OPER (nom="ELEMENTS_GRAPPE_COMMANDE",op=0,sd_prod=ElementsGrappeCommande,niveau = 'ElementsTechnologiquesAssemblages',
  fr  = "Définition des éléments des grappes de commande",
  ang = "Definition of control rod cluster components",
  ElementsBarre        = SIMP (typ= ElementBarre, max='**',statut='o',fr="Liste des barres absorbantes associees"),
  HauteurPasInsertion  = SIMP (typ='R',defaut=1.5875      ,statut='o',fr="Hauteur (cm) d'un pas d'insertion des grappes"),
  CourseTotalePossible = SIMP (typ='R',defaut=361.8       ,statut='o',fr="Course totale possible (cm) d'insertion d'une grappe"),
  CoteInferieureGrappe = SIMP (typ='R',defaut=8.5705      ,statut='o',fr="Cote inferieure (cm) d'une grappe / zone active ?"),
  VitesseDeplacement   = SIMP (typ='R',defaut=72.         ,statut='o',fr="Vitesse de deplacement d'une grappe en pas/mn"),
  NbPasInsertion       = SIMP (typ='I',defaut=225         ,statut='o',fr="Nombre maximum de pas d'insertion "),
  Araignee16Phauteur   = SIMP (typ='R',defaut=0.          ,statut='o',fr="Hauteur (cm) d'une des 16 petites tiges d'accrochage des barres"),
  Araignee4Mhauteur    = SIMP (typ='R',defaut=0.          ,statut='o',fr="Hauteur (cm) d'une des 4 tiges moyennes d'accrochage des barres"),
  Araignee4Ghauteur    = SIMP (typ='R',defaut=0.          ,statut='o',fr="Hauteur (cm) d'une des 4  grandes tiges d'accrochage des barres"),
  HauteurPommeau       = SIMP (typ='R',defaut=0.          ,statut='o',fr="Hauteur (cm) du pommeau d'accrochage de la grappe"),
  RayonPommeau         = SIMP (typ='R',defaut=0.          ,statut='o',fr="Rayon (cm) du pommeau d'accrochage de la grappe")
 ) ;  # Fin ELEMENTS_GRAPPE_COMMANDE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ELEMENTS_ABSORBANTS_FIXES :   Classe de definition des elements des grappes d'absorbants fixes
#                                       Description des pyrex uniquement pour le moment
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ELEMENTS_ABSORBANTS_FIXES = OPER (nom="ELEMENTS_ABSORBANTS_FIXES",op=0,sd_prod=ElementsAbsorbantsFixes,
                          niveau = 'ElementsTechnologiquesAssemblages',
  fr  = "Definition des elements des grappes d'absorbants fixes",
  ang = "Definition of non movable absorber control rod cluster elements",
# Limitation a 12 caracteres
# HBouchInfPyrex        = SIMP (typ='R',statut='f'),
# RBouchInfPyrex        = SIMP (typ='R',statut='f'),
# HZoneVidePyrex        = SIMP (typ='R',statut='f'),
# HBouchSupPyrex        = SIMP (typ='R',statut='f'),
# RBouchSupPyrex        = SIMP (typ='R',statut='f'),
# MatBouchonPyrex       = SIMP (typ=Materiau, statut='f')
  BIPyrexHauteur        = SIMP (typ='R',      statut='o',fr="Hauteur en cm du bouchon inferieur du crayon pyrex"),
  BIPyrexRayon          = SIMP (typ='R',      statut='o',fr="Rayon en cm du bouchon inferieur du crayon pyrex"),
  PyrexZoneVideHauteur  = SIMP (typ='R',      statut='o',fr="Hauteur en cm de la zone vide dans le crayon pyrex"),
  BSPyrexHauteur        = SIMP (typ='R',      statut='o',fr="Hauteur en cm du bouchon superieur du crayon pyrex"),
  BSPyrexRayon          = SIMP (typ='R',      statut='o',fr="Rayon en cm du bouchon superieur du crayon pyrex"),
  PyrexMateriauBouchon  = SIMP (typ=Materiau, statut='o',fr="Materiau du bouchon du crayon pyrex")
 ) ;  # Fin ELEMENTS_ABSORBANTS_FIXES
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe GRAPPE_BOUCHON_ASSEMBLAGE : Classe de definition d'une grappe bouchon REP
#  Rappel : Les grappes bouchons se trouvent dans le cas des REP inseres dans la partie embout superieur de tous les assemblages
#           ne comportant pas de grappe d'absorbant.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GRAPPE_BOUCHON_ASSEMBLAGE = OPER (nom="GRAPPE_BOUCHON_ASSEMBLAGE",op=0,sd_prod=GrappeBouchonAssemblage,
                          niveau = 'ElementsTechnologiquesAssemblages',
  fr  = "Definition d'une grappe bouchon d'assemblage combustible",
  ang = "Definition d'une grappe bouchon d'assemblage combustible",
  HauteurPartieBasseBouchon           = SIMP (typ='R'     ,statut='o',fr="Hauteur en cm de la partie basse du bouchon"),
  RayonPartieBasseBouchon             = SIMP (typ='R'     ,statut='o',fr="Rayon en cm de la partie basse du bouchon"),
  Hauteur1PartieIntermediaire1Bouchon = SIMP (typ='R'     ,statut='o',fr="Hauteur en cm de la 1ere partie intermédiaire du bouchon"),
  Rayon1PartieIntermediaire1Bouchon   = SIMP (typ='R'     ,statut='o',fr="Rayon en cm de la 1ere partie intermédiaire du bouchon"),
  Hauteur2PartieIntermediaire2Bouchon = SIMP (typ='R'     ,statut='o',fr="Hauteur en cm de la 2eme partie intermédiaire du bouchon"),
  Rayon2PartieIntermediaire2Bouchon   = SIMP (typ='R'     ,statut='o',fr="Rayon en cm de la 2eme partie intermédiaire du bouchon"),
  RegionSousPlaqueHauteurBouchon      = SIMP (typ='R'     ,statut='o',fr="Hauteur en cm de la region sous plaque"),
  RegionSurPlaqueHauteurBouchon       = SIMP (typ='R'     ,statut='o',fr="Hauteur en cm de la region au-dessus de la plaque"),
  Rayon3BouchonRegionPlaque           = SIMP (typ='R'     ,statut='o',fr="Rayon en cm du bouchon au niveau de la plaque"),
  HauteurSupport                      = SIMP (typ='R'     ,statut='o',fr="Hauteur en cm du support des bouchons"),
  MasseGrappe                         = SIMP (typ='R'     ,statut='o',fr="Masse en g de la grappe bouchon"),
  Materiau                            = SIMP (typ=Materiau,statut='o',fr="Materiau de la grappe bouchon",defaut='ACIER')
 ) ;  # Fin GRAPPE_BOUCHON_ASSEMBLAGE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ELEMENTS_ASSEMBLAGE : Classe de définition des éléments associes a l'assemblage combustible REP
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#ELEMENTS_ASSEMBLAGE = OPER (nom="ELEMENTS_ASSEMBLAGE",op=0,sd_prod=ElementsAssemblage,
#
#  fr  = "Definition des elements associes a l'assemblage",
#  ang = "Definition of the fuel assembly associated elements",
#  GrappeBouchon         = SIMP (typ=GrappeBouchonAssemblage,statut='o'),
#  CrayonsAbsorbants     = SIMP (typ=ElementsAbsorbants,statut='o'),
#  GrappesCommande       = SIMP (typ=ElementsGrappeCommande,statut='o')
# ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classes CONDITION_LIMITE elementaires : 	Classes de definition de Conditions limites elementaires
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
VIDE = OPER (nom="VIDE",op=0,sd_prod=Vide,   niveau = 'ConditionsLimites',
             fr  = "Condition aux limites de vide",
             ang = "Void boundary condition" ) ;
REFLEXION_ISOTROPE = OPER (nom="REFLEXION_ISOTROPE",op=0,sd_prod=ReflexionIsotrope, niveau = 'ConditionsLimites',
                           fr  = "Condition aux limites de reflexion isotrope",
                           ang = "Isotropic Reflexion boundary condition" ) ;
REFLEXION_SPECULAIRE = OPER (nom="REFLEXION_SPECULAIRE",op=0,sd_prod=ReflexionSpeculaire, niveau = 'ConditionsLimites',
                             fr  = "Condition aux limites de reflexion speculaire",
                             ang = "Specular Reflexion boundary condition" ) ;
ALBEDO  = OPER (nom="ALBEDO",op=0,sd_prod=Albedo,   niveau = 'ConditionsLimites',
                fr  = "Condition aux limites d'albedo",
                ang = "Albedo boundary condition",
                albedo = SIMP (typ='R',statut='o',max='**',fr="Valeurs des albedos") ) ;
TRANSLATION = OPER (nom="TRANSLATION",op=0,sd_prod=Translation, niveau = 'ConditionsLimites',
                    fr  = "Condition aux limites de translation",
                    ang = "Translation boundary condition",
                    Vecteur = SIMP (typ=Vecteur,statut='o',fr="Axe de translation") ) ;
ROTATION = OPER (nom="ROTATION",op=0,sd_prod=Rotation,   niveau = 'ConditionsLimites',
		 fr  = "Condition aux limites de rotation",
		 ang = "Rotational boundary condition",
		 Centre  = SIMP (typ=Point  ,statut='o',fr="Centre de la rotation"),
		 Vecteur = SIMP (typ=Vecteur,statut='o',fr="Axe de rotation"),
		 Angle   = SIMP (typ='R'    ,statut='o',fr="Angle de rotation",defaut=90.) ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONDITION_LIMITE_SPECIALE : 	Classe de definition de Conditions limites sur les surfaces elementaires de la geometrie
#    					modifiant la CL generale
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONDITION_LIMITE_SPECIALE = OPER (nom="CONDITION_LIMITE_SPECIALE",op=0,sd_prod=SpecialeConditionLimite,
                                    niveau = 'ConditionsLimites',
  fr  = "Condition limite particuliere qui sera plaquee sur la geometrie",
  ang = "Special boundary condition added to the geometry",
  Type = SIMP (typ=(Vide,ReflexionIsotrope,ReflexionSpeculaire, Albedo, Translation, Rotation),statut='o',
               fr="Type de condition limite a appliquer aux surfaces listees"),
  ZonesApplication = SIMP (typ=(Segment,ArcCercle,Conique),max='**',statut='o',
                           fr="Liste des segments ou surfaces sur lesquels porte la condition limite")
 ) ;  # Fin CONDITION_LIMITE_SPECIALE
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONDITION_LIMITE_GENERALE : Classe de definition des conditions limites de l'objet geometrique complet
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONDITION_LIMITE_GENERALE = OPER (nom="CONDITION_LIMITE_GENERALE",op=0,sd_prod=GeneraleConditionLimite,
                                    niveau = 'ConditionsLimites',
  fr  = "Condition limite a la surface externe de la geometrie complete",
  ang = "Boundary condition for the complete geometry",
  ZoneCalculee              = NUPL (statut='f',min=2,max=2,fr="Droites ou plans delimitant la zone de calcul",
                                    elements = (SIMP (typ=(Droite,Plan)), SIMP (typ='TXM',into=('Plus','Moins')))),
  ParDefautCondition        = SIMP (typ=(Vide, ReflexionIsotrope, ReflexionSpeculaire, Albedo),
                                    defaut=ReflexionIsotrope,
                                    statut='f',
                                    fr="Condition limite par defaut"),
  ParticulieresConditions   = NUPL (fr       = "Conditions particulieres modifiant localement la condition limite par defaut",
                                    statut   = 'f', max = '**',
                                    elements = (SIMP (typ='TXM',into=('X-','X+','Y-','Y+','Z-','Z+','R+','X','Y','Z')),
                                                SIMP (typ=(Vide,ReflexionIsotrope,ReflexionSpeculaire, Albedo, Translation, Rotation)))),
  SupplementairesConditions = SIMP (typ    = SpecialeConditionLimite,
                                    statut = 'f', max = '**',
                                    fr     = "Conditions limites non exprimables avec les donnees precedentes")
 ) ;  # Fin CONDITION_LIMITE_GENERALE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POSITION_ASSEMBLAGE_COMBUSTIBLE : Classe de definition de la position des assemblages combustibles dans un REP
#                                           Reperes (bataille navale ou autre) et
#                                           Coordonnees cartesiennes entieres des assemblages combustibles pour un type de palier
#                                           Origine des coordonnees en bas a gauche d'un systeme en xy
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POSITION_ASSEMBLAGE_COMBUSTIBLE = OPER (nom="POSITION_ASSEMBLAGE_COMBUSTIBLE",op=0,sd_prod=PositionAssemblageCombustible,
        niveau = 'ElementsTechnologiquesReacteur',
  fr  = "Position des assemblages combustibles",
  ang = "Position of fuel assemblies",
  NbAssemblagesCombustibles = SIMP (typ='I',statut='o',defaut=157,fr="Nombre d'assemblages combustibles positionnes"),
  regles = (UN_PARMI('PositionReseau', 'Positions'),),
  PositionReseau = SIMP (typ=CorrespondanceReperePositionReseau,statut="f",fr="Objet donnant la correspondance entre Repere et Coordonnees entieres des assemblages"),
  Positions      = NUPL (max='**',statut='f',
                         elements=(SIMP (typ='TXM',fr="Repere alphanumerique arbitraire de l'assemblage"),
                                   SIMP (typ='I'  ,fr="Premiere Coordonnee entiere de l'assemblage"),
                                   SIMP (typ='I'  ,fr="Seconde  Coordonnee entiere de l'assemblage")))
 ) ;  # Fin POSITION_ASSEMBLAGE_COMBUSTIBLE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POSITION_INSTRUMENTATION_INTERNE : Classe de definition de la position des assemblages instrumentes dans le cœur d'un REP
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POSITION_INSTRUMENTATION_INTERNE = OPER (nom="POSITION_INSTRUMENTATION_INTERNE",op=0,sd_prod=PositionInstrumentationInterne,
        niveau = 'ElementsTechnologiquesReacteur',
  fr  = "Definition de la position des assemblages instrumentes",
  ang = "Definition of neutron flux detector position",
# TypePalier                = SIMP (typ='TXM',max='**',statut='o'),
  NbAssemblagesInstrumentes = SIMP (typ='I',statut='o',fr="Nombre d'assemblages instrumentes"),
  Positions                 = NUPL (
      max      = '**',
      statut   = 'o',
      elements = (SIMP (typ='TXM',fr= "Type d'instrumentation (CFM, Collectron, ou Autre)"),
                  SIMP (typ='I',min=2,max=2,fr= "Coordonnees entieres de l'assemblage instrumente dans le reseau")))
 ) ;  # Fin POSITION_INSTRUMENTATION_INTERNE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe IMPLANTATION_GRAPPES_COMMANDE : Classe de definition de l'implantation des grappes de commande pour un type de schema de grappe (REP)
#                                         Donnees de la position (coordonnees entieres en xy), du type de grappe et du groupe d'appartenance
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
IMPLANTATION_GRAPPES_COMMANDE = OPER (nom="IMPLANTATION_GRAPPES_COMMANDE", op=0, sd_prod=ImplantationGrappesCommande,
        niveau = 'ElementsTechnologiquesReacteur',
  fr  = "Position radiale des grappes de commande pour un schema d'implantation particulier",
  ang = "Control rod cluster radial positions and types",
  TypeSchema      = SIMP (typ='TXM',statut='o',fr="Identificateur arbitraire du type de schema"),
  NbTotalGrappes  = SIMP (typ='I'  ,statut='o',fr="Nombre total de grappes du schema"),
  PositionsEtType = NUPL (max='**' ,statut='o',
                          elements=(SIMP (typ='TXM',statut='o',fr="Nom du groupe de grappes"),
                                    SIMP (typ='I'  ,statut='o',fr="Nombre de grappes du groupe"),
                                    SIMP (typ='TXM',statut='o',fr="Type de grappes (exemple : '8B', '12B', '24B')"),
                                    SIMP (typ='I'  ,statut='o',max='**',fr="Coordonnees entieres des grappes dans le reseau coeur")))
 ) ;  # Fin IMPLANTATION_GRAPPES_COMMANDE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe STRUCTURES_INTERNES_REACTEUR : Classe de definition des structures internes d'un coeur de REP
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
STRUCTURES_INTERNES_REACTEUR = OPER (nom="STRUCTURES_INTERNES_REACTEUR", op=0, sd_prod=StructuresInternesReacteur,
        niveau = 'ElementsTechnologiquesReacteur',
  fr  = "Definition des structures internes d'un cœur REP",
  ang = "Definition of a PWR core internal structures",
  PlaqueInferieureCoeur   = FACT (
      Epaisseur = SIMP (typ='R',statut='o',fr="Epaisseur de la plaque inferieure du coeur en cm"),
      Materiau  = SIMP (typ=Materiau,statut='f',defaut='ACIER',fr="Materiau de la plaque inferieure du coeur"),
      Trous     = NUPL (
          max      = '**',
          elements = (
              SIMP (typ='I',                               fr="Nombre de trous dont on donne les dimensions"),
              SIMP (typ='TXM',into=('Rayon','Cotes'),      fr="Mot-cle indiquant si on donne le rayon ou les cotes"),
              SIMP (typ='R',min=2,max=2,                   fr="Rayons ou cotes des trous en cm"),
              SIMP (typ='TXM',into=('Hauteur','Epaisseur'),fr="Mot-cle indiquant l'entree de la hauteur du trou"),
              SIMP (typ='R',                               fr="Hauteur du trou en cm")))),
  PlaqueSuperieureCoeur   = FACT (
      Epaisseur = SIMP (typ='R',                               fr="Epaisseur de la plaque superieure du coeur en cm"),
      Materiau  = SIMP (typ=Materiau,statut='f',defaut='ACIER',fr="Materiau  de la plaque superieure du coeur"),
      Trous     = NUPL (
          max      = '**',
          elements = (
              SIMP (typ='I',                               fr="Nombre de trous dont on donne les dimensions"),
              SIMP (typ='TXM',into=('Rayon','Cotes'),      fr="Mot-cle indiquant si on donne le rayon ou les cotes"),
              SIMP (typ='R',min=2,max=2,                   fr="Rayons ou cotes des trous en cm"),
              SIMP (typ='TXM',into=('Hauteur','Epaisseur'),fr="Mot-cle indiquant l'entree de la hauteur du trou"),
              SIMP (typ='R',                               fr="Hauteur du trou en cm")))),
  CloisonnementCoeur      = FACT (
      Epaisseur             = SIMP (typ='R',                                fr="Epaisseur du cloisonnement du coeur"),
      Materiau              = SIMP (typ=Materiau,statut='f',defaut='ACIER', fr="Materiau  du cloisonnement du coeur"),
      DimensionsInterieures = NUPL (
          max      = '**',
          elements = (
              SIMP (typ='I',                                      fr="Nombre d'assemblages dans la rangee"),
              SIMP (typ='TXM',into=('Assemblages','Assemblies'),  fr="Mot-cle suivant le nombre d'assemblages"),
              SIMP (typ='TXM',into=('Largeur','Cote'),            fr="Mot-cle precedant la largeur interieure du cloisonnement"),
              SIMP (typ='R',                                      fr="Largeur interieure du cloisonnement en cm"),
              SIMP (typ='TXM',into=('NbJeuCloisonGrille','NbJeu'),fr="Mot-cle precedant le nombre de jeux CloisonGrille"),
              SIMP (typ='I',                                      fr="Nombre de jeux CloisonGrille"))),
      TrousDepressurisation = NUPL (elements=(SIMP (typ='I',      fr="Nombre de trous de depressurisation"),
                                              SIMP (typ='TXM',into=('Rayon','Radius'),fr="Mot-cle precedant la valeur du rayon des trous"),
                                              SIMP (typ='R',fr="Rayon des trous de depressurisation en cm"))),
      TemperatureMoyenne    = SIMP (typ='R',fr="Temperature Moyenne du cloisonnement en Celsius")),
  RenfortsInternes        = FACT (statut='f',
      Nombre                      = SIMP (typ='I',max='**',statut='o',fr="Liste des nombres de chaque type de renfort interne"),
      Epaisseur                   = SIMP (typ='R',max='**',statut='o',fr="Nombre de renforts internes pour chaque type de renfort"),
      Materiau                    = SIMP (typ=Materiau,max='**',statut='f',defaut='ACIER',fr="Materiau de chaque type de renfort"),
      NbTrousDepressurisation     = SIMP (typ='I',max='**',statut='o',fr="Nombre de trous dans chaque type de renfort"),
      RayonsTrousDepressurisation = SIMP (typ='R',max='**',statut='o',fr="Rayons des trous dans chaque type de renfort en cm"),
      TemperatureMoyenne          = SIMP (typ='R',statut='f',fr="Temperature moyenne des renforts internes en Celsius")),
  EnveloppeVirole        = FACT (statut='f',
      RayonInterne       = SIMP (typ='R',statut='o',fr="Rayon interne de l'enveloppe du coeur en cm"),
      RayonExterne       = SIMP (typ='R',statut='o',fr="Rayon externe de l'enveloppe du coeur en cm"),
      Materiau           = SIMP (typ=Materiau,statut='f',defaut='ACIER',fr="Materiau de l'enveloppe du coeur"),
      TemperatureMoyenne = SIMP (typ='R',statut='f',fr="Temperature moyenne de l'enveloppe du coeur en Celsius")),
  Boucliers              = FACT (statut='f',
      RayonInterne       = SIMP (typ='R',statut='o',fr="Rayon interne des boucliers thermiques du coeur en cm"),
      RayonExterne       = SIMP (typ='R',statut='o',fr="Rayon externe des boucliers thermiques du coeur en cm"),
      Materiau           = SIMP (typ=Materiau,statut='f',defaut='ACIER',fr="Materiau des boucliers thermiques du coeur"),
      Secteurs           = NUPL (max='**',statut='f',elements=(
                                 SIMP (typ='R',statut='o',fr="Angle en degres du debut du secteur du bouclier / axe Ox"),
                                 SIMP (typ='R',statut='o',fr="Angle en degres du secteur du bouclier"))),
      TemperatureMoyenne = SIMP (typ='R',statut='f',fr="Temperature moyenne en Celsius des boucliers du coeur")),
  Cuve                   = FACT (statut='f',
      RayonInterne       = SIMP (typ='R',statut='o',fr="Rayon interne de la cuve en cm"),
      RayonExterne       = SIMP (typ='R',statut='o',fr="Rayon externe de la cuve en cm"),
      Materiau           = SIMP (typ=Materiau,statut='f',defaut='ACIER',fr="Materiau de la cuve"),
      TemperatureMoyenne = SIMP (typ='R',statut='f',fr="Temperature moyenne en Celsius de la cuve"))
 ) ; # Fin STRUCTURES_INTERNES_REACTEUR
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PRESSURISEUR : Classe de definition d'un pressuriseur REP (Valeurs par defaut pour un CP2 900)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PRESSURISEUR = OPER (nom="PRESSURISEUR", op=0, sd_prod=Pressuriseur, niveau = 'ElementsTechnologiquesReacteur',
  fr  = "Donnees d'un pressuriseur REP",
  ang = "Definition of a PWR pressurizor",
  TmNominale            = SIMP (typ='R',statut='o',defaut=345.0  ,fr="Temperature nominale en Celsius dans le pressuriseur"),
  Volume                = SIMP (typ='R',statut='o',defaut=39.865 ,fr="Volume total du pressuriseur en m3"),
  VolumeHaut            = SIMP (typ='R',statut='o',defaut=37.196 ,fr="Volume d'eau au niveau haut du pressuriseur en m3"),
  VolumeBas             = SIMP (typ='R',statut='o',defaut=2.597  ,fr="Volume d'eau au niveau bas du pressuriseur en m3"),
  DiametreExterne       = SIMP (typ='R',statut='o',defaut=235.   ,fr="Diametre externe du pressuriseur en cm"),
  Hauteur               = SIMP (typ='R',statut='o',defaut=1280.  ,fr="Hauteur du pressuriseur en cm"),
  Pression              = SIMP (typ='R',statut='o',defaut=172.37 ,fr="Pression de calcul du pressuriseur en bars"),
  CapaciteChaufferette  = SIMP (typ='R',statut='o',defaut=1440.  ,fr="Capacite des chaufferettes du pressuriseur en kW"),
  NbChaufferettes       = SIMP (typ='I',statut='o',defaut=60     ,fr="Nombre de chaufferettes du pressuriseur"),
  MasseAVide            = SIMP (typ='R',statut='o',defaut=78.    ,fr="Masse a vide du pressuriseur en tonnes"),
  MasseEnService        = SIMP (typ='R',statut='o',defaut=95.    ,fr="Masse du pressuriseur en service normal en tonnes"),
  PressionDecharge      = SIMP (typ='R',statut='o',defaut=162.   ,fr="Pression d'ouverture de la decharge du pressuriseur en bars"),
  PressionSoupape       = SIMP (typ='R',statut='o',defaut=171.5  ,fr="Pression de tarage des soupapes de surete du pressuriseur en bars"),
  VolumeDecharge        = SIMP (typ='R',statut='o',defaut=37.    ,fr="Volume total du reservoir de decharge du pressuriseur en m3"),
  VolumeliquideDecharge = SIMP (typ='R',statut='o',defaut=25.5   ,fr="Volume de liquide du reservoir de decharge du pressuriseur en fct normal en m3")
 ) ;  # Fin PRESSURISEUR
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe GENERATEUR_VAPEUR : Classe de definition d'un generateur de vapeur REP (Valeurs par defaut pour un CP2 900) 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GENERATEUR_VAPEUR = OPER (nom="GENERATEUR_VAPEUR", op=0, sd_prod=GenerateurVapeur, niveau = 'ElementsTechnologiquesReacteur',
  fr  = "Donnees d'un generateur de vapeur REP",
  ang = "Definition of a PWR Steam Generator",
  HauteurTotale         = SIMP (typ='R',statut='o',defaut=2064.8 ,fr="Hauteur totale d'un GV en cm"),
  DiametreMaximum       = SIMP (typ='R',statut='o',defaut=446.8  ,fr="Diametre maximum d'un GV en cm"),
  DiametreMinimum       = SIMP (typ='R',statut='o',defaut=343.4  ,fr="Diametre minimum d'un GV en cm"),
  NbTubes               = SIMP (typ='I',statut='o',defaut=3330   ,fr="Nombre de tubes d'un GV"),
  TubeDiametre          = SIMP (typ='R',statut='o',defaut=2.222  ,fr="Diametre des tubes d'un GV en cm"),
  TubeEpaisseur         = SIMP (typ='R',statut='o',defaut=0.127  ,fr="Epaisseur des tubes d'un GV en cm"),
  PasReseau             = SIMP (typ='R',statut='o',defaut=3.254  ,fr="Pas du reseau des tubes d'un GV en cm"),
  LongueurTube          = SIMP (typ='R',statut='o',defaut=963.7  ,fr="Longueur droite des tubes d'un GV en cm"),
  SurfaceEchange        = SIMP (typ='R',statut='o',defaut=4700.  ,fr="Surface d'échange d'un GV en m2"),
  PlaqueEpaisseur       = SIMP (typ='R',statut='o',defaut=53.4   ,fr="Epaisseur de la plaque tubulaire d'un GV en cm"),
  PlaqueDiametre        = SIMP (typ='R',statut='o',defaut=345.4  ,fr="Diametre de la plaque tubulaire d'un GV en cm"),
  NbEntretoises         = SIMP (typ='I',statut='o',defaut=8	      ,fr="Nombre de plaques entretoises d'un GV"),
  MasseAVide            = SIMP (typ='R',statut='o',defaut=300.   ,fr="Masse a vide d'un GV en tonnes"),
  MasseFctNormal        = SIMP (typ='R',statut='o',defaut=364.   ,fr="Masse en fonctionnement normal d'un GV en tonnes"),
  MasseFaisceau         = SIMP (typ='R',statut='o',defaut=51.5   ,fr="Masse du faisceau tubulaire d'un GV en tonnes"),
  ViroleSupEpaisseur    = SIMP (typ='R',statut='o',defaut=9.4    ,fr="Epaisseur de la virole superieure d'un GV en cm"),
  ViroleInfEpaisseur    = SIMP (typ='R',statut='o',max=3,defaut=(8.4,7.4),fr="Epaisseur(s) de la virole inferieure d'un GV en cm"),
  MateriauEntretroises  = SIMP (typ=Materiau,statut='o',defaut='ACIER'  ,fr="Materiau des plaques entretoises d'un GV"),
  MateriauTube          = SIMP (typ=Materiau,statut='o',defaut='INCONEL',fr="Materiau des tubes du faisceau d'un GV"),
  GeomReseau            = SIMP (typ='TXM',statut='o',defaut='Carre',into=('Carre','Triangulaire'),
                                fr="Type de geometrie du reseau des tubes d'un GV")
 ) ;  # Fin GENERATEUR_VAPEUR
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POMPE_PRIMAIRE : Classe de definition d'une pompe primaire REP (Valeurs par defaut pour un CP2 900)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POMPE_PRIMAIRE = OPER (nom="POMPE_PRIMAIRE", op=0, sd_prod=PompePrimaire, niveau = 'ElementsTechnologiquesReacteur',
  fr  = "Donnees d'une pompe primaire REP",
  ang = "Definition of a PWR primary pomp",
  Type                = SIMP (typ='TXM',statut='o', defaut='93-D7'	,fr="Type de pompe"),
  TensionNominale     = SIMP (typ='R'  ,statut='o', defaut=6600.	,fr="Tension nominale en Volts d'une pompe primaire"),
  VitesseRotation     = SIMP (typ='I'  ,statut='o', defaut=1485		,fr="Vitesse de rotation tours/mn ? d'une pompe primaire"),
  DebitConception     = SIMP (typ='R'  ,statut='o', defaut=21250.	,fr="Debit de conception m3/h d'une pompe primaire"),
  HauteurManometrique = SIMP (typ='R'  ,statut='o', defaut=90.7		,fr="Hauteur manometrique ds pompes en mCE"),
  PuissanceFroid      = SIMP (typ='R'  ,statut='o', defaut=6600.	,fr="Puissance absorbee a froid sur l'arbre de la pompe en kW"),
  PuissanceChaud      = SIMP (typ='R'  ,statut='o', defaut=5000.	,fr="Puissance absorbee a chaud sur l'arbre de la pompe en kW"),
  PuissanceNominale   = SIMP (typ='R'  ,statut='o', defaut=5300.	,fr="Puissance absorbee nominale par moteur en kW"),
  TensionMinimale     = SIMP (typ='R'  ,statut='o', defaut=0.75		,fr="Tension minimale de démarrage en fraction de la tension nominale"),
  Masse               = SIMP (typ='R'  ,statut='o', defaut=93.9		,fr="Masse d'une pompe primaire en tonnes avec huile et eau"),
  HauteurTotale       = SIMP (typ='R'  ,statut='o', defaut=8.1		,fr="Hauteur totale d'une pompe primaire en cm"),
  Inertie             = SIMP (typ='R'  ,statut='o', defaut=3730.	,fr="Inertie des pieces tournantes en kg.m2"),
  DebitInjection      = SIMP (typ='R'  ,statut='o', defaut=1800.	,fr="Debit d'injection aux joints en l/h")
 ) ;  # Fin POMPE_PRIMAIRE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CARACTERISTIQUES_PALIER : Classe de definition des donnees generales d'un type de palier de reacteur
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CARACTERISTIQUES_PALIER = OPER (nom="CARACTERISTIQUES_PALIER",op=0,sd_prod=CaracteristiquesPalier,
        niveau = 'ElementsTechnologiquesReacteur',
  fr  = "Donnees generales pour un type de palier de reacteur",
  ang = "General data for a particular type of nuclear reactor",
  TypePalier                     = SIMP (typ='TXM',statut='o',fr="Identificateur du type de palier"),
  PositionCombustible            = SIMP (typ=PositionAssemblageCombustible ,statut='o',
                                         fr="Objet definissant la position des assemblages dans le coeur"),
  PositionDetecteur              = SIMP (typ=PositionInstrumentationInterne,statut='o',
                                         fr="Objet definissant la position des assemblages instrumentes"),
  StructuresInternes             = SIMP (typ=StructuresInternesReacteur    ,statut='o',
                                         fr="Objet definissant les structures internes du reacteur"),
  Pressuriseur                   = SIMP (typ=Pressuriseur                  ,statut='f',
                                         fr="Objet contenant les caracteristiques du pressuriseur du reacteur"),
  Generateur                     = SIMP (typ=GenerateurVapeur              ,statut='f',
                                         fr="Objet contenant les caracteristiques des GV du reacteur"),
  Pompes                         = SIMP (typ=PompePrimaire                 ,statut='f',
                                         fr="Objet contenant les caracteristiques des pompes primaires du reacteur"),
  CoeurPElectriqueNominle        = SIMP (typ='R',statut='o',defaut= 900.,
                                         fr="Puissance electrique nominale de coeur en MW"),
  CoeurPThermiqueNominale        = SIMP (typ='R',statut='o',defaut=2775.,
                                         fr="Puissance thermique nominale de coeur en MWth"),
  ChaudierePThermiqueNominale    = SIMP (typ='R',statut='o',defaut=2785.,
                                         fr="Puissance thermique nominale de la chaudiere MWth"),
  ChaudierePmaxThermique         = SIMP (typ='R',statut='o',defaut=2905.,
                                         fr="Puissance thermique maximum de la chaudiere MWth"),
  NbBouclesPrimaires             = SIMP (typ='I',statut='o',defaut=3,
                                         fr="Nombre de boucles primaires"),
  ProportionDebitCoeurCuve       = SIMP (typ='R',statut='o',defaut=0.97,
                                         fr="Rapport du debit coeur / debit cuve"),
  PressionNominalePrimaire       = SIMP (typ='R',statut='o',defaut=155.,
                                         fr="Pression nominale du circuit primaire en bars"),
  PerteChargeCoeurNominale       = SIMP (typ='R',statut='o',defaut=1.24,
                                         fr="Perte de charge nominale dans le coeur en bars"),
  PerteChargeCuveNominale        = SIMP (typ='R',statut='o',defaut=2.34,
                                         fr="Perte de charge nominale dans la cuve en bars"),
  TmNomSortieCuveEntreeGV        = SIMP (typ='R',statut='o',defaut=323.2,
                                         fr="Temperature nominale sortie Cuve / Entree GV en Celsius"),
  TmNomSortieGVEntreePPrimaire   = SIMP (typ='R',statut='o',defaut=285.8,
                                         fr="Temperature nominale sortie GV / Entree Pompe primaire en Celsius"),
  TmNomSortiePPrimaireEntreeCuve = SIMP (typ='R',statut='o',defaut=286.,
                                         fr="Temperature nominale sortie Pompe primaire / Entree Cuve en Celsius"),
  TmEntreeCoeurPnulle            = SIMP (typ='R',statut='o',defaut=286.0,
                                         fr="Temperature en Celsius du moderateur a puissance nulle a l'entree du coeur"),
  TmEntreeCoeurPnom              = SIMP (typ='R',statut='o',defaut=286.4,
                                         fr="Temperature en Celsius du moderateur a puissance nominale a l'entree du coeur"),
  TmSortieCoeurPnom              = SIMP (typ='R',statut='o',defaut=324.7,
                                         fr="Temperature en Celsius du moderateur a puissance nominale a l'entree du coeur"),
  TmMoyenneCoeurPnom             = SIMP (typ='R',statut='o',defaut=305.3,
                                         fr="Temperature moyenne en Celsius du moderateur dans le coeur actif"),
  TmMoyenneCuvePnom              = SIMP (typ='R',statut='o',defaut=305.0,
                                         fr="Temperature moyenne en Celsius du moderateur dans la cuve"),
  TmMoyenneReflecteurPnom        = SIMP (typ='R',statut='o',defaut=296.0,
                                         fr="Temperature moyenne en Celsius du reflecteur radial"),
  TcMoyennePnom                  = SIMP (typ='R',statut='o',defaut=600.0,
                                         fr="Temperature moyenne en Celsius du combustible dans le coeur"),
  TcCentrePnom                   = SIMP (typ='R',statut='o',defaut=1830.,
                                         fr="Temperature au centre Pastille en Celsius en fct nominal"),
  SectionEcoulementCoeur         = SIMP (typ='R',statut='o',defaut=3.86,
                                         fr="Section d'ecoulement du moderateur dans le coeur en m2"),
  SurfaceEchangeCoeur            = SIMP (typ='R',statut='o',defaut=4520.,
                                         fr="Surface d'échange dans le coeur en m2"),
  VolumeEauCuve                  = SIMP (typ='R',statut='o',defaut=105.8,
                                         fr="Volume d'eau primaire m3 dans la cuve (coeur et internes en place)"),
  VolumeEauPrimaire              = SIMP (typ='R',statut='o',defaut=215.,
                                         fr="Volume total d'eau primaire m3)"),
  VolumeBallonRCV                = SIMP (typ='R',statut='o',defaut=7.,
                                         fr="Volume du ballon RCV m3)"),
  DebitThermohConception         = SIMP (typ='R',statut='o',defaut=63325.,
                                         fr="Debit thermohydraulique de conception dans la cuve en m3/h"),
  DebitMecaniqueConception       = SIMP (typ='R',statut='o',defaut=70920.,
                                         fr="Debit mecanique de conception dans la cuve en m3/h"),
  BypassConception               = SIMP (typ='R',statut='o',defaut=7.,
                                         fr="Pourcentage de debit Conception dans le contournement du coeur en %"),
  BypassSpin                     = SIMP (typ='R',statut='o',defaut=4.5,
                                         fr="Pourcentage de debit dans le contournement du coeur en % utilise dans le SPIN"),
  DebitBestEstimateBoucle        = SIMP (typ='R',statut='o',defaut=21075.,
                                         fr="Debit best-estimate par boucle en m3/h"),
  DebitMassiqueNominal           = SIMP (typ='R',statut='o',defaut=47675.,
                                         fr="Debit massique nominal best-estimate dans la cuve en t/h"),
  DebitEffMassiqueNominal        = SIMP (typ='R',statut='o',defaut=45530.,
                                         fr="Debit massique effectif du coeur en t/h"),
  FluxMoyenChaleurCoeur          = SIMP (typ='R',statut='o',defaut=60.,
                                         fr="Flux de chaleur moyen dans le coeur W/cm2"),
  FluxMaxChaleurCoeur            = SIMP (typ='R',statut='o',defaut=128.,
                                         fr="Flux de chaleur maximal dans le coeur W/cm2"),
  PlinMoyen                      = SIMP (typ='R',statut='o',defaut=178.,
                                         fr="Puissance lineique Moyenne en W/cm"),
  PlinMax                        = SIMP (typ='R',statut='o',defaut=382.,
                                         fr="Puissance lineique Maximum en W/cm"),
  FacteurFQN                     = SIMP (typ='R',statut='o',defaut=2.69,
                                         fr="Facteur de point chaud de conception FQN"),
  FacteurFDH                     = SIMP (typ='R',statut='o',defaut=1.55,
                                         fr="Facteur total d'élévation d'enthalpie FDH de conception"),
  RECMinimalNominal              = SIMP (typ='R',statut='o',defaut=1.78,
                                         fr="REC minimal en fonctionnement nominal"),
  VitesseMoyenneModerCoeur       = SIMP (typ='R',statut='o',defaut=4.72,
                                         fr="Vitesse moyenne dans le coeur en m/s"),
  VitesseMassiqueModerCoeur      = SIMP (typ='R',statut='o',defaut=328.,
                                         fr="Vitesse massique moyenne dans le coeur en g/s.cm2"),
  VitesseRechaufRefroid          = SIMP (typ='R',statut='o',defaut=28.,
                                         fr="Vitesse normale maximale de rechauffage ou de refroidissementnormal en Celsius/h"),
  VitesseMaxRechaufRefroid       = SIMP (typ='R',statut='o',defaut=56.,
                                         fr="Vitesse maximale de rechauffage ou de refroidissementnormal en Celsius/h")
 ) ;  # Fin CARACTERISTIQUES_PALIER
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe SITE_NUCLEAIRE_EDF : Classe de definition d'un site nucleaire EDF (Tranches, paliers et numero EPN)
#  Le numero EPN correspond au code de la tranche, cette donnee figure dans le fichier ASN transmis par la Division Combustible
#  decrivant chaque recharge combustible (et identifie donc la tranche a laquelle elle est destinee)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SITE_NUCLEAIRE = OPER (nom="SITE_NUCLEAIRE", op=0, sd_prod=SiteNucleaire, niveau = 'ElementsTechnologiquesReacteur',
  fr  = "Definition d'un site nucleaire EDF et de ses tranches",
  ang = "Definition of a nuclear power plant site",
  NomSite  = SIMP (typ='TXM',statut='o',fr="Nom du site nucleaire",defaut='TRICASTIN'),
  Tranches = NUPL (max='**',elements=(	SIMP (typ='I'  ,statut='o',fr="Numero de la tranche nucleaire"),
					SIMP (typ='TXM',statut='o',fr="Trigramme de la tranche nucleaire"),
					SIMP (typ=CaracteristiquesPalier,statut='o',fr="Type de palier"),
					SIMP (typ='I'  ,statut='o',fr="Numero EPN de la tranche")))
 ) ;   # Fin SITE_NUCLEAIRE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ESPACE_VARIATIONS :	Classe de definition de l'espace des parametres variables et sa discretisation.
#				De manière generale, un parametre peut valoriser un attribut quelconque de plusieurs objets. L'association
#				Parametre-Attributs se fait par l'attribut ObjetsVariations de la classe definie ci-dessous
#				de maniere purement textuelle sous la forme 'NomObjet.NomAttribut(.NomSousAttribut)[Index]'.
#				L'attribut variable peut etre un objet, auquel cas les valeurs de variation sont les noms textuels
#				des objets a remplacer successivement dans chaque calcul elementaire.
#				Il n'y a pas de verification de coherence au niveau de la saisie des donnees mais immediatement apres
#				lors de l'interpretation de l'ensemble de l'objet DonneesCasEtude .
# 				Definition de la methode de balayage de cet espace (Suite d'options complementaires) :
#				1) ParametresIndependants :     Calculs independants en donnant successivement a chacun
#                                                               des parametres leurs valeurs individuelles
#				2) CoinsDomaine :               Rajout des calculs aux limites extremes du domaine
#				3) BordsDomaine :               Rajout des calculs aux bords du domaine
#				4) Grilles2D :                  Rajout des calculs sur les grilles 2D
#                                                               passant par un point de reference
#				5) CasParticuliers :            Rajout de points specifiques de calcul
#				6) EspaceComplet :              Balayage complet du domaine des parametres
#				Par defaut, le cas de reference est le premier cas defini soit dans CasParticuliers si les cas sont fournis
#				de cette façon, soit par les premieres valeurs rentrees pour chacun des paramètres,
#				sauf entree explicite de l'attribut CasReference
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ESPACE_VARIATIONS = OPER (nom="ESPACE_VARIATIONS", op=0, sd_prod=EspaceVariations, niveau = 'ParametresCalcul',
  fr  = "Definition de l'espace des parametres et de leurs variations",
  ang = "Definition of feedback or variable parameters",
  regles = (AU_MOINS_UN ('Variations', 'CasParticuliers'),),
  Variations       = NUPL (max='**',statut='f',
                           elements=( SIMP (typ='TXM',statut='o',fr="Nom arbitraire du parametre a faire varier"),
                                      SIMP (typ=('R','I','TXM'),max='**',statut='o',fr="Valeurs discretes de variation du parametre"))),
  ObjetsVariations = NUPL (max='**',statut='o',fr="Association Parametre et attributs des objets du modele de donnees",
                           elements=( SIMP (typ='TXM',statut='o',fr="Nom arbitraire du parametre a faire varier"),
                                      SIMP (typ='TXM',max='**',statut='o',fr="Objets, attributs et index associes au parametre"))),
  MethodeBalayage = SIMP (
      typ    = 'TXM',
      max    = '**',
      defaut = 'ParametresIndependants',
      into   = ('ParametresIndependants','CoinsDomaine','BordsDomaine','Grilles2D','CasParticuliers','EspaceComplet'),
      statut = 'o'),
  TypeVariation   = SIMP (typ='TXM',defaut='Absolu',into=('Relatif','Absolu'),statut='o'),
  CasParticuliers = NUPL (max='**',statut='f',fr="Liste des couples (Parametre, Valeur du parametre) pour les cas particuliers",
                          elements=(SIMP (typ='TXM',fr="Nom arbitraire du parametre a faire varier"),
                                    SIMP (typ=('I','R','TXM'),fr="Valeur du parametre"))),
  CasReference    = NUPL (max='**',statut='f',fr="Liste des couples (Parametre, Valeur du parametre) pour le cas de reference",
                          elements=(SIMP (typ='TXM',fr="Nom arbitraire du parametre a faire varier"),
                                    SIMP (typ=('I','R','TXM'),fr="Valeur du parametre")))
 ) ;   # Fin ESPACE_VARIATIONS
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DONNEES_IRRADIATION : Classe de definition des valeurs d'irradiation intervenant dans les phases de calcul ou d'edition
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DONNEES_IRRADIATION = OPER (nom="DONNEES_IRRADIATION",op=0,sd_prod=DonneesIrradiation,
        niveau = 'ParametresCalcul',
  fr  = "Definition des donnees d'irradiation",
  ang = "Definition of burnup values",
  regles = (AU_MOINS_UN ('Irradiations', 'Refroidissement','InsertionGrappeX'),),
  Unite           = SIMP (typ='TXM',defaut='MWj/t',into=('MWj/t','Jours'),statut='o',fr="Unite pour les irradiations"),
  Minimum         = SIMP (typ='R',defaut=0.,statut='f',fr="Irradiation du debut de calcul"),
  Maximum         = SIMP (typ='R',defaut=100000.,statut='f',fr="Irradiation maximum des calculs"),
  Irradiations    = SIMP (typ='R',max='**',defaut=0.,statut='f',fr="Liste previsionnelle des irradiations"),
  Refroidissement = FACT (statut='f',fr="Definition de la periode de refroidissement",
                          Instants = SIMP (typ='R',max='**',fr="Irradiations MWj/t de debut de refroidissement du combustible"),
                          Duree    = SIMP (typ=('R','I'),max='**',fr="Nombre de jours de refroidissement correspondant aux instants de refroidissement")
                         ),
  InsertionGrappeX     = FACT (statut='f',fr="Simulation d'une insertion de grappe dans un assemblage seul (Mode X)",
	TypeGrappe            = SIMP (typ='TXM',     statut='o',fr="Type de grappe inseree"),
	IrradiationInsertion  = SIMP (typ=('R','I'), statut='o',max='**',fr="Irradiations MWj/t de debut d'insertion de la grappe"),
	IrradiationExtraction = SIMP (typ=('R','I'), statut='o',max='**',fr="Irradiations MWj/t d'extraction de la grappe"),
	CoteAxiale            = SIMP (typ='R',       statut='f',fr="Cote axiale (cm) de la limite inferieure de la grappe aux instants d'insertion")
				)
 ) ;  # Fin DONNEES_IRRADIATION
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONDITIONS_FONCTIONNEMENT_MOYENNES : Classe de definition des conditions de fonctionnement Reacteur pour une campagne donnee
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONDITIONS_FONCTIONNEMENT_MOYENNES = OPER (nom="CONDITIONS_FONCTIONNEMENT_MOYENNES",op=0,sd_prod=ConditionsFonctionnementMoyennes,
        niveau = 'ParametresCalcul',
  fr  = "Definition des conditions de fonctionnement moyennes pour une campagne donnee",
  ang = "Definition of a campaign operating conditions ",
  IdentificateurCampagne       = SIMP (typ='TXM',statut='f',fr="Identificateur de la campagne"),
  DescriptifFonctionnement     = SIMP (typ='TXM',statut='f',fr="Descriptif textuel arbitraire du mode de fonctionnement"),
  regles = (UN_PARMI ('PuissanceThermiqueCoeur', 'PuissanceRelativeCoeur'),),
  PuissanceThermiqueCoeur      = SIMP (typ='R',statut='o',defaut=2775.,fr="Puissance thermique du reacteur en MWth"),
  PuissanceRelativeCoeur       = SIMP (typ='R',statut='o',defaut=100. ,fr="Puissance relative du reacteur en %"),
  FluxSurfaciquePn             = SIMP (typ='R',statut='o',defaut=59.74 ,fr="Flux a la surface du crayon en W/cm2"),
  PressionEntreePrimaire       = SIMP (typ='R',statut='o',defaut=155.1,fr="Pression du moderateur en bars a l'entree du coeur actif"),
  PressionSortiePrimaire       = SIMP (typ='R',statut='o',defaut=155.1,fr="Pression moyenne du moderateur en bars en sortie du coeur actif"),
  TitreMoyenBore               = SIMP (typ='R',statut='o',defaut= 500.,fr="Titre moyen en ppm en bore dans le moderateur"),
#
  TmEntreePnulle               = SIMP (typ='R',statut='o',defaut=286.0,fr="Temperature en Celsius du moderateur a puissance nulle a l'entree du coeur"),
  TmEntreePnom                 = SIMP (typ='R',statut='o',defaut=286.4,fr="Temperature en Celsius du moderateur a puissance nominale a l'entree du coeur"),
  DeltaTmEntreeSortiePnom      = SIMP (typ='R',statut='o',defaut= 39.0,fr="Ecart en Celsius de temperature entre entree et sortie du coeur a puissance nominale"),
  TmMoyenneCoeurPnom           = SIMP (typ='R',statut='o',defaut=305.3,fr="Temperature moyenne en Celsius du moderateur dans le coeur actif"),
  TmMoyenneCuvePnom            = SIMP (typ='R',statut='f',defaut=305.0,fr="Temperature moyenne en Celsius du moderateur dans la cuve"),
  TmMoyenneReflecteurPnom      = SIMP (typ='R',statut='f',defaut=296.0,fr="Temperature moyenne en Celsius du reflecteur radial"),
  TcMoyennePnom                = SIMP (typ='R',statut='f',defaut=600.0,fr="Temperature moyenne en Celsius du combustible dans le coeur"),
#
  PositionGrappeHaute          = SIMP (typ='I',statut='f',defaut=225  ,fr="Position haute des grappes, en nombre de pas extraits"),
  DebitMesureParBoucle         = FACT (statut='f',max='**',fr="Debit primaire mesure sur chaque boucle en m3/h",
                                       DateEssai = SIMP (typ='I',min=3,max=3,fr="Date J M A de l'essai"),
                                       Debits    = SIMP (typ='R',min=3,max=4,fr="Valeurs des debits primaire par boucle en m3/h")
                                       ),
  NbTubesGVBouches             = SIMP (typ='I',statut='f',min=3,max=4,fr="Nombre de tubes bouches pour chaque GV")
 ) ; # Fin CONDITIONS_FONCTIONNEMENT_MOYENNES
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONDITIONS_TRANSITOIRE : Classe de definition des conditions de fonctionnement Reacteur pour une campagne donnee en transitoire
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONDITIONS_TRANSITOIRE = OPER (nom="CONDITIONS_TRANSITOIRE", op=0, sd_prod=ConditionsTransitoire, niveau = 'ParametresCalcul',
  fr  = "Definition des conditions de fonctionnement en transitoire pour une campagne donnee",
  ang = "Definition of a campaign dynamic operating conditions ",
  IdentificateurCampagne          = SIMP (typ='TXM',max='**',statut='f',fr="Identificateur de la campagne"),
  NeutroniqueDiscretisation       = SIMP (typ='R',max='**',statut='f',fr="Liste des pas de temps successifs pour le calcul neutronique (en s)"),
  ThermohydrauliqueDiscretisation = SIMP (typ='R',statut='f',fr="Liste des pas de temps successifs pour le calcul thermohydraulique (en s)"),
  DureeTransitoire                = SIMP (typ='R',statut='o',fr="Duree totale en s du transitoire a simuler"),
  PuissanceThermiqueRelative      = SIMP (typ='R',max='**',statut='f',fr="Couples (Instant en s, Puissance thermique relative du reacteur en %)"),
  PressionPrimaireEntree          = SIMP (typ='R',max='**',statut='f',fr="Couples (Instant en s, Pression du moderateur en bars a l'entree du coeur actif)"),
  TitreBore                       = SIMP (typ='R',max='**',statut='f',fr="Couples (Instant en s, Titre en bore dans le moderateur (en ppm))"),
  DebitPrimaire                   = SIMP (typ='R',max='**',statut='f',fr="Couples (Instant en s, Debit primaire dans le coeur en m3/h)")
# PositionsGrappes                = SIMP (typ=PositionAxialeGrappesCommande,statut='f')
# PositionsGrappes                = FACT (max='**',statut='f',
#                                         RepereGrappeouGroupe = SIMP (typ='TXM',fr="Repere du groupe de grappes ou de la grappe"),
#                                         Positions            = SIMP (typ='R',max='**',
#                                                                      fr="Couples (Instant en s, Position dans le coeur en nombre de pas extraits)"))
 ) ;  # Fin CONDITIONS_TRANSITOIRE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POSITION_AXIALE_GRAPPES_COMMANDE : Classe de definition des positions axiales des grappes de commande
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POSITION_AXIALE_GRAPPES_COMMANDE = OPER (nom="POSITION_AXIALE_GRAPPES_COMMANDE",op=0,sd_prod=PositionAxialeGrappesCommande,
        niveau = 'ParametresCalcul',
  fr  = "Positions axiales des grappes de commande pour une campagne donnee ou pour un transitoire",
  ang = "Control rod cluster axial positions for a campaign or for a static or dynamic calculation",
  TypeDonnee    = SIMP (typ='TXM',statut='o',defaut='Statique',into=('Statique','Cinetique','Campagne'),
                        fr="Indication de dependance ou non d'un parametre Temps ou Irradiation"),
  UnitePosition = SIMP (typ='TXM',statut='o',defaut='PasExtrait',into=('PasExtrait', 'cm', 'Recouvrement')),
  BlocStatique  = BLOC (condition = "TypeDonnee=='Statique'",
                        PositionStatique = NUPL (max='**',statut='o',elements =(
                                          SIMP (typ='TXM',fr="Nom du groupe de grappes ou de la grappe"),
                                          SIMP (typ=('R','I'),fr="Position axiale"))
                                          )
                       ),
  BlocCinetique  = BLOC (condition = "TypeDonnee=='Cinetique'",
                         PositionCinetique = FACT (max='**',statut='o',
                                           NomGrappeouGroupe = SIMP (typ='TXM',fr="Nom du groupe de grappes ou de la grappe"),
                                           CotesAxiales      = SIMP (typ=('R','I'),max='**',
                                                                     fr="Liste des Couples (Instant en s, Position axiale)")
                                           )
                        ),
  BlocCampagne  = BLOC (condition = "TypeDonnee=='Campagne'",
                        PositionCampagne = FACT (max='**',statut='o',
                                          NomGrappeouGroupe = SIMP (typ='TXM',fr="Nom du groupe de grappes ou de la grappe"),
                                          CotesAxiales      = SIMP (typ=('R','I'),max='**',
                                                                    fr="Liste des Couples (Irradiation MWj/t, Position axiale)")
                                          )
                        )
  ) ;  # Fin POSITION_AXIALE_GRAPPES_COMMANDE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DATES_CLES_CAMPAGNE : Classe de definition des dates cles d'une campagne et de sa longueur
#  Definition des attributs :
#  LongueurNaturelleExperimentaleMWj_t : Irradiation moyenne coeur depuis le debut de la campagne jusqu'au moment du passage en
#                                        prolongation de campagne (valeur experimentale transmise par le site). En cas d'anticipation,
#                                        c'est la valeur recalee qui y est stockee.
#  LongueurNaturelleRecaleeMWj_t : Longueur naturelle previsionnelle estimee en cours de campagne (par le suivi du bore,
#                                  a chaque carte de flux)
#  LongueurNaturelleTheoriqueMWj_t : Longueur naturelle estimee par le code de coeur
#  LongueurAnticipationJepp : Longueur d'anticipation de campagne en Jours Equivalents Pleine Puissance
#  LongueurProlongationJepp : Longueur de prolongation de campagne en Jours Equivalents Pleine Puissance
#  LongueurTotaleExperimentaleMWj_t : Longueur totale de la campagne en MWj/t (Donnee transmise par le site)
#  TypePlanChargement : Type de plan pour la fluence cuve : Determine par les irradiations des assemblages places sur les axes medians
#			et sur les diagonales
#			- 3 Assemblages neufs aux bouts des deux axes : Plan Standard
#			- 3 Assemblages (Irradie, Neuf, Irradie) ou (Neuf, Irradie, Neuf) sur les axes : Fluence reduite (REP 900 ou N4)
#			- 2 assemblages irradies aux bouts des diagonales : Fluence reduite (REP 1300)
#			- 3 Assemblages irradies aux bouts des deux axes : Fluence Faible (REP 900 ou N4)
#			- 3 Assemblages irradies aux bouts des deux axes et
#			  2 assemblages irradies aux bouts des diagonales : Faible Fluence Generalisee
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DATES_CLES_CAMPAGNE = OPER (nom="DATES_CLES_CAMPAGNE", op=0, sd_prod=DatesClesCampagne, niveau = 'DonneesEtude',
  fr  = "Definition des dates cles d'une campagne et de ses longueurs caracteristiques",
  ang = "Definition of the campaign dates and lengths",
  IdentificateurCampagne         = SIMP (typ='TXM',statut='o',defaut='CZ101',fr="Identificateur de la campagne"),
  TypePlanChargement             = SIMP (typ='TXM',statut='f',defaut='FluenceFaible',
                                         into=('Standard','FluenceReduite','FluenceFaible','FaibleFluenceGeneralisee')),
  DateDDC                        = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A de debut de campagne"),
  regles	                        = (ENSEMBLE ('DatePnom','IrradiationDatePnom'),
                                   ENSEMBLE ('DateCouplage','IrradiationDateCouplage'),
                                   ENSEMBLE ('DatePassageEnProlongation','LongueurNaturelleExperimentale'),),
  DatePnom                       = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A d'atteinte de la puissance nominale"),
  IrradDatePnom                  = SIMP (typ='R',	     statut='f',fr="Irradiation de la campagne a la date d'atteinte de la puissance nominale"),
  DateCouplage                   = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A de couplage au reseau"),
  IrradDateCouplage              = SIMP (typ='R',	     statut='f',fr="Irradiation de la campagne atteinte a la date de couplage au reseau"),
  DateFDC                        = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A de fin de campagne reelle"),
  LNatTheorique                  = SIMP (typ='R',	     statut='f',fr="Longueur naturelle theorique calculee de la campagne en MWj/t"),
  LNatRecalee                    = SIMP (typ='R',	     statut='f',fr="Longueur naturelle recalee calculee de la campagne en MWj/t"),
  DatePassageEnProlongation      = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A de passage en prolongation de campagne"),
  LnatExperimentale              = SIMP (typ='R',	     statut='f',fr="Longueur naturelle mesuree de la campagne en MWj/t"),
  LongueurAnticipationJepp       = SIMP (typ='R',	     statut='f',fr="Nombre de JEPP d'anticipation"),
  LongueurProlongationJepp       = SIMP (typ='R',	     statut='f',fr="Nombre de JEPP de prolongation"),
  LongueurTotaleExperimentale    = SIMP (typ='R',	     statut='f',fr="Longueur totale de la campagne en MWj/t")
 ) ;  # Fin DATES_CLES_CAMPAGNE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe OPTIONS_AUTOPROTECTION : Classe de definition des donnees d'autoprotection du code de reseau
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONS_AUTOPROTECTION = OPER (nom="OPTIONS_AUTOPROTECTION",op=0,sd_prod=OptionsAutoprotection,
        niveau = 'OptionsCodesCalcul',
  fr  = "Definition des donnees d'autoprotection des resonances",
  ang = "Definition of resonance self shielding data",
  TypeCombustible          = SIMP (typ='TXM',max='**',statut='o',
                             fr="Type de combustible auquel s'appliquent ces options d'autoprotection"),
  MethodeAutoprotection    = SIMP (typ='TXM',into=('SanchezCoste','SousGroupes'),defaut='SanchezCoste',statut='f'),
  EnergieSupAutoprotection = SIMP (typ='R',defaut=55.5952,statut='f',
                                   fr="Energie superieure eV du premier groupe d'autoprotection, gpe 38 dans le cas a 99 groupes"),
  IsotopesAutoproteges  = NUPL (
      max	= '**',
      elements	= (SIMP (typ=Isotope,statut='o',fr="Nom de l'isotope a autoproteger"),
                   SIMP (typ='TXM',into=('Moyenne','Detaillee','Couronne'),statut='o'),
                   SIMP (typ='TXM',into=('Materiaux','Cellules'),statut='f',
                         fr="Choix d'autoprotection sur les materiaux ou les cellules"),
                   SIMP (typ='TXM',max='**',statut='f',fr="Liste des types de materiaux ou de cellules concernes"))),
  Irradiations  = SIMP (typ='R',max='**',statut='f',fr="Irradiations ou se font les calculs d'autoprotection"),
  PoisonIrradiations  = SIMP (typ='R',max='**',statut='f',
                        fr="Irradiations ou se font les calculs d'autoprotection des poisons integres au combustible")
  ) ;   # Fin OPTIONS_AUTOPROTECTION
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe OPTIONS_CODE_RESEAU : Classe de definition des options du code de reseau
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONS_CODE_RESEAU = OPER (nom="OPTIONS_CODE_RESEAU", op=0, sd_prod=OptionsCodeReseau, niveau = 'OptionsCodesCalcul',
  fr  = "Definition des options des codes de calcul de reseau",
  ang = "Definition of lattice code options",
  MethodeCalcul             = SIMP (typ='TXM',defaut='Multicellule',statut='o',
                                    into=('Multicellule','Pij','Caracteristiques','Monte-Carlo/TRIPOLI','Monte-Carlo/MCNP'),
                                    fr="Methode de calcul"),
  ProcedureBibliothequeBase = SIMP (typ='TXM',defaut='CEA93_G99_V5',statut='o',
                                    into=('CEA93_G99_V0','CEA93_G99_V2','CEA93_G99_V3','CEA93_G99_V4',
                                          'CEA93_G99_V5','CEA93_G99_V6','CEA93_G172_V4'),
                                    fr="Nom de la procedure Bibliotheque"),
  CorrectionTransport       = SIMP (typ='TXM',defaut='APOLLO',statut='o',into=('APOLLO','WIMS','Non'),
                                    fr="Demande ou non de correction de transport (de type APOLLO ou WIMS)"),
  TypeBibliothequeBase      = SIMP (typ='TXM',defaut='APOLLIB_2',statut='o',
                                    into=('APOLLIB_1','APOLLIB_2','DRAGON','NJOY_89','NJOY_91','WIMS_D4','WIMS_AECL'),
                                    fr="Format de la bibliotheque de donnees nucleaires multigroupes"),
  TableProbabilites         = SIMP (typ='TXM',defaut='CALENDF',statut='o',into=('CALENDF','SUBG','Non'),
                                    fr="Calcul des tables de probabilites mathematiques CALENDF ou physiques SUBG"),
  RegionPeripheriqueCellule = SIMP(typ='R',defaut=0.,statut='o',
                                    fr="Proportion de Volume de la zone peripherique des cellules cylindrisees"),
  OptionMulticellule        = SIMP (typ='TXM',defaut='ROTH',statut='o',into=('ROTH','MULTICELLULE'),
                                    fr="Option du calcul multicellule"),
  OptionPij                 = SIMP (typ='TXM',defaut='&UP0 &ROTH',statut='o',into=('&UP0 &ROTH','&UP0 &HETE','&UP1 &HETE'),
                                    fr="Option du calcul des Pij"),
  ParametresIntegration     = SIMP (typ='TXM',defaut='MAIL_INT 7 7 7 7',statut='f',
                                    fr="Donnees du maillage d'integration en heterogene"),
  ProportionNoyauxParDefaut = SIMP (typ='R',defaut=1.E-12,statut='o',
                                    fr="Valeur initiale des concentrations des noyaux lourds non definis"),
  OptionLaplacienB2         = SIMP (typ='TXM',defaut='CRITIQUE',statut='o',into=('CRITIQUE','NUL','IMPOSE'),
                                    fr="Option du calcul des fuites homogenes"),
  LaplacienB2               = SIMP (typ='R',defaut=0.,statut='o',fr="Valeur initiale du laplacien du calcul des fuites"),
  OrdreAnisotropie          = SIMP (typ='I',defaut=1 ,statut='o',fr="Ordre d'anisotropie des sections de transfert"),
  Autoprotection            = SIMP (typ='TXM',defaut='Oui',statut='o',into=('Oui','Non'),
                                    fr="Calcul d'autoprotection ou non"),
  BlocAutoprotection  = BLOC (condition = "Autoprotection=='Oui'",
        DonneesAutoprotection     = SIMP (typ=OptionsAutoprotection,statut='f',max='**',
                                    fr="Nom des objets decrivant les isotopes a autoproteger et les options associees"),
        RecalculAutoprotection    = SIMP (typ='TXM',defaut='Oui',statut='o',into=('Oui','Non'),
                                    fr="Demande ou non de recalcul de l'autoprotection")),
  Equivalence               = SIMP (typ='TXM',defaut='Non',statut='o',into=('Oui','Non'),
                                    fr="Demande ou non de calcul d'equivalence"),
  NbGroupesEquivalence      = SIMP (typ='I',max='**',defaut=(2,6,16),statut='o',
                                    fr="Liste des nombres de groupes des calculs d'equivalence"),
  EditionSaphyb             = SIMP (typ='TXM',defaut='Non',statut='o',into=('Oui','Non'),
                                    fr="Demande d'edition des bibliotheques de type Saphyb"),
  EditionAssemblage         = SIMP (typ='TXM',defaut='Oui',statut='o',into=('Oui','Non'),
                                    fr="Demande d'edition des sections efficaces homogeneisees sur l'ensemble du domaine"),
  EditionCellule            = SIMP (typ='TXM',defaut='Oui',statut='o',into=('Oui','Non'),
                                    fr="Demande d'edition des sections efficaces homogeneisees par cellule"),
  EditionFluxDetaille       = SIMP (typ='TXM',defaut='Oui',statut='o',into=('Oui','Non'),
                                    fr="Demande d'edition des flux moyens sur l'ensemble du domaine sur la maillage multigroupe detaille"),
  EditionMilieu             = SIMP (typ='TXM',defaut='Oui',statut='o',into=('Oui','Non'),
                                    fr="Demande d'edition des compositions isotopiques detaillees sur tous les milieux de calcul"),
  EditionTrimaran           = SIMP (typ='TXM',defaut='Non',statut='o',into=('Oui','Non'),
                                    fr="Demande d'edition des sections efficaces pour TRIPOLI multigroupe"),
  SpectreNeutrons           = SIMP (typ='TXM',defaut='Prompt',statut='o',into=('Prompt','Retarde'),
                                    fr="Type de spectre de neutrons pour le calcul de transport"),
  ListeIsotopesEdites       = SIMP (typ='TXM',statut='f',max='**',fr="Liste des initiales des symboles des isotopes a editer"),
  FichierBickley            = SIMP (typ='TXM',statut='f',fr="Nom du fichier des fonctions Bickley"),
  EditionIsotopeHomogene    = SIMP (typ='TXM',defaut='Non',statut='o',into=('Oui','Non'),
                                    fr="Demande d'edition de constitution d'isotopes homogeneises sous forme APOLLIB"),
  BlocHomoge  = BLOC (condition = "EditionIsotopeHomogene=='Oui'",
        RepertoireHomoge          = SIMP (typ='TXM',statut='f',
                                    fr="Nom du repertoire du fichier des isotopes homogenes sous forme APOLLIB"),
        FichierHomoge             = SIMP (typ='TXM',statut='f',fr="Nom du fichier des isotopes homogenes sous forme APOLLIB")),
  Executable                = NUPL (statut   = 'f', elements = (
                                    SIMP (typ='TXM',fr="Systeme d'exploitation"),
                                    SIMP (typ='TXM',fr="Nom du fichier executable"))),
  ProceduresApollo2         = FACT (statut='f',
                                    OptionsListing  = SIMP (typ='TXM',statut='f',fr="Commandes Gibiane des options d'edition listing"),
                                    Evolution       = SIMP (typ='TXM',statut='f',fr="Procedure d'evolution"),
                                    Reprise         = SIMP (typ='TXM',statut='f',fr="Procedure de reprise"),
                                    Equivalence     = SIMP (typ='TXM',statut='f',fr="Procedure d'equivalence"),
                                    EditionCellule  = SIMP (typ='TXM',statut='f',fr="Procedure d'edition par cellule"),
                                    EditionHomoge   = SIMP (typ='TXM',statut='f',fr="Procedure d'edition des isotopes Homoge")
                                    ),
  ProceduresSunset          = FACT (statut='f',
                                    Evolution       = SIMP (typ='TXM',statut='f',fr="Procedure d'evolution"),
                                    Reprise         = SIMP (typ='TXM',statut='f',fr="Procedure de reprise")
                                    )
  ) ;  # Fin OPTIONS_CODE_RESEAU
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe OPTIONS_CODE_COEUR_STATIQUE : Classe de definition des options du code de coeur en statique
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONS_CODE_COEUR_STATIQUE = OPER (nom="OPTIONS_CODE_COEUR_STATIQUE", op=0, sd_prod=OptionsCodeCoeurStatique, niveau = 'OptionsCodesCalcul',
  fr  = "Definition des options des codes de calcul de coeur en statique",
  ang = "Definition of core code static options",
  DeltaReactivite = SIMP (typ='TXM',statut='o',defaut='DeltaRo',into=('DeltaRo','LogKeff'),
                          fr="Methode de calcul de variation de reactivite entre deux etats"),
  OxMaillageFlux = SIMP (typ=Maillage1D,statut='o',fr="Maillage du calcul de flux suivant l'axe x d'un assemblage"),
  OyMaillageFlux = SIMP (typ=Maillage1D,statut='o',fr="Maillage du calcul de flux suivant l'axe y d'un assemblage"),
  OzMaillageFlux = SIMP (typ=Maillage1D,statut='o',fr="Maillage du calcul de flux suivant l'axe z d'un assemblage"),
  ReactiviteVisee           = SIMP (typ='R',defaut=  0.,statut='o',fr="Valeur en pcm de la reactivite visee en calcul critique"),
  EfficaciteBoreEstimee     = SIMP (typ='R',defaut= -6.,statut='o',fr="Valeur estimee en pcm/ppm de l'efficacite du bore"),
  TitreBoreInitiale         = SIMP (typ='R',defaut=600.,statut='o',fr="Valeur estimee en ppm du titre en bore du moderateur"),
  Factorisation             = SIMP (typ='TXM',defaut='Non',statut='o',into=('Coeur2D','Assemblage','Non'),
                                    fr="Option ou non de factorisation par le flux fin Coeur ou Assemblage"),
  AxialTypeReflecteurs      = SIMP (typ='TXM',defaut='Equivalent',statut='o',into=('Equivalent','Homogeneise')),
  RadialTypeReflecteurs     = SIMP (typ='TXM',defaut='Equivalent',statut='o',into=('Equivalent','Homogeneise')),
  ReflAxiauxEquivalents     = BLOC (condition = "TypeReflecteursAxiaux=='Equivalent'",
                                    ReflecteurInferieur = SIMP (typ=SectionsReflecteur,statut='o'),
                                    MaillageInferieur   = SIMP (typ=Maillage1D,statut='o'),
                                    ReflecteurSuperieur = SIMP (typ=SectionsReflecteur,statut='o'),
                                    MaillageSuperieur   = SIMP (typ=Maillage1D,statut='o')
                                    ),
  ReflAxiauxHomogeneises = BLOC (condition = "TypeReflecteursAxiaux=='Homogeneise'",
                                 AxialAbscisses = SIMP (typ='R'     ,statut='o',max='**'),
                                 AxialMateriaux = SIMP (typ=Materiau,statut='o',max='**')
                                 ),
  ReflRadialEquivalent    = BLOC (condition = "TypeReflecteurRadial=='Equivalent'",
                                  ReflecteurRadial = SIMP (typ=SectionsReflecteur,statut='o'),
                                  Epaisseur        = SIMP (typ='R'     ,statut='o')
                                  ),
  ReflRadialHomogeneise   = BLOC (condition = "TypeReflecteurRadial=='Homogeneise'",
                                  RadialAbscisses = SIMP (typ='R'     ,statut='o',max='**'),
                                  RadialMateriaux = SIMP (typ=Materiau,statut='o',max='**')
                                  ),
  ApproximationMigration    = SIMP (typ='TXM',defaut='SPn',statut='o',into=('SPn','Sn','Diffusion')),
  BlocSPn = BLOC (condition = "ApproximationTransport=='SPn'",
                        SPnOrdreApproximation = SIMP (typ='I'  ,defaut=1,statut='o',fr="Ordre n impair de la methode SPn"),
                        SPnElementFini        = SIMP (typ='TXM',defaut='RTN0',statut='o',into=('RTN0','RTN1'),fr="Type d'element fini"),
                        SPnMaxIterDiffusion   = SIMP (typ='I'  ,defaut=1,into=(1,2,3,4,5),statut='o',
                                                      fr="Nombre maximal d'iterations de diffusion")
                       ),
  BlocSn = BLOC (condition = "ApproximationTransport=='Sn'",
                        SnOrdreApproximation = SIMP (typ='I'  ,defaut=4,statut='o',fr="Ordre n pair de la methode Sn"),
                        SnElementFini        = SIMP (typ='TXM',defaut='RTN',statut='o',into=('RTN','BDM'),fr="Type d'element fini"),
                        SnAcceleration       = SIMP (typ='TXM',defaut='Oui',statut='o',into=('Oui','Non'),fr="Acceleration par la diffusion"),
                        SnMaxIterDiffusion   = SIMP (typ='I'  ,defaut=20,statut='o',fr="Nombre maximal d'iterations de calcul de diffusion")
                       ),
  BlocDiff = BLOC (condition = "ApproximationTransport=='Diffusion'",
                        MaxIterFlux     = SIMP (typ='I',defaut= 5       ,statut='o',fr="Maximum d'iterations du calcul de flux"),
                        MaxIterKeff     = SIMP (typ='I',defaut=50       ,statut='o',fr="Maximum d'iterations du calcul de keff"),
                        PrecPuissance   = SIMP (typ='R',defaut=0.005    ,statut='o',fr="Precision sur la puissance"),
                        PrecKeff        = SIMP (typ='R',defaut=0.0001   ,statut='o',fr="Precision sur keff")
                       ),
  PrecisionValeurPropre       = SIMP (typ='R',defaut=1.E-5,statut='o',fr="Precision sur la valeur propre"),
  PrecisionFlux               = SIMP (typ='R',defaut=1.E-3,statut='o',fr="Precision sur le flux"),
  PrecisionMultigroupe        = SIMP (typ='R',defaut=1.E-6,statut='o',fr="Precision de la resolution multigroupe"),
  PrecisionIterTermeDiffusion = SIMP (typ='R',defaut=1.E-6,statut='o',fr="Precision des iterations sur le terme de diffusion"),
  MaxIterEnergie              = SIMP (typ='I',defaut=1,statut='o',
                                      fr="Nombre maximal d'iterations pour la resolution Gauss Seidel en energie"),
  MaxIterTermeDiffusion       = SIMP (typ='I',defaut=1,statut='o',fr="Nombre maximal d'iterations sur le terme de diffusion"),
  MaxIterDecompositionDomaine = SIMP (typ='I',defaut=1,statut='o',fr="Nombre d'iterations de decomposition de domaine"),
  MaxIterKeffAvantCR          = SIMP (typ='I',defaut=1,statut='o',fr="Nombre de calculs de keff avant appel aux contre-reactions")
  ) ;  # Fin OPTIONS_CODE_COEUR_STATIQUE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe OPTIONS_CODE_COEUR_CINETIQUE : Classe de definition des options du code de coeur en cinetique
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONS_CODE_COEUR_CINETIQUE = OPER (nom="OPTIONS_CODE_COEUR_CINETIQUE", op=0, sd_prod=OptionsCodeCoeurCinetique, niveau = 'OptionsCodesCalcul',
  fr  = "Definition des options des codes de calcul de coeur en cinetique",
  ang = "Definition of core code kinetic options",
  NombrePrecurseurs              = SIMP (typ='I',defaut=6,statut='o',fr="Nombre de groupes de precurseurs"),
  GestionAutomatiquePasCinetique = SIMP (typ='TXM',defaut='Oui',into=('Oui','Non'),statut='o',
                                         fr="Gestion automatique du pas de temps du calcul cinetique"),
  BlocSansGestionPas             = BLOC (condition = "GestionAutomatiquePasCinetique=='Non'",
                                         DefinitionPasDeTemps = SIMP (typ='R',max='**',statut='o',
                                         fr="Liste de couples (pas de temps, limite superieure de validite du pas de temps)"),
                                               ),
  PrecisionIterationFluxPrecurseurs    = SIMP (typ='R',defaut=1.E-6,statut='o',fr="Precision sur les iterations Flux Precurseurs"),
  PrecisionParametreGestionAutomatique = SIMP (typ='R',defaut=0.0008,statut='o',fr="Precision sur les iterations Flux Precurseurs"),
  MaxIterationsFluxPrecurseurs         = SIMP (typ='I',defaut=50,statut='o',fr="Nombre maximal d'iterations Flux Precurseurs"),
  ThetaSchemaCinetique                 = SIMP (typ='R',defaut=0.5,statut='o',fr="Valeur du parametre theta du schema cinetique")
  ) ;  # Fin OPTIONS_CODE_COEUR_CINETIQUE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe OPTIONS_THERMIQUE_THERMOHYDRAULIQUE : Classe de definition des options du code de coeur en cinetique
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONS_THERMIQUE_THERMOHYDRAULIQUE = OPER (nom="OPTIONS_THERMIQUE_THERMOHYDRAULIQUE", op=0, sd_prod=OptionsThermiqueThermohydraulique, niveau = 'OptionsCodesCalcul',
  fr  = "Definition des options des modules de calcul de coeur thermique et thermohydraulique simplifiees",
  ang = "Definition of thermohydraulic and thermic module options",
  HGaineFluide                        = SIMP (typ='TXM',defaut='DITTUS_BOELTER',into=('FLICA','DITTUS_BOELTER'),statut='o',
                                              fr="Option du Coefficient d'echange gaine-fluide (flux < au flux critique)"),
  HGaineFluideEbullition              = SIMP (typ='TXM',defaut='BST',into=('BST','TONG'),statut='o',
                                              fr="Option du Coefficient d'echange gaine-fluide (Ebullition en film)"),
  OptionHGapConstantTransitoire       = SIMP (typ='TXM',defaut='Non',into=('Non','Oui'),statut='o',
                                                                     fr="Option de constance du coefficient d'echange JeuPastilleGaine"),
  OptionHGap                          = SIMP (typ='TXM',defaut='HGAP_88',into=('EJECTION','TUO2','PLIN_BU','FIXE','HGAP_88'),statut='o',
                                              fr="Option de calcul du Coefficient d'echange du jeu pastille-gaine"),
  BlocHgapTuo2                        = BLOC (condition = "CoefficientEchangeJeuPastilleGaine=='TUO2'",
                                              Tuo2Initiale = SIMP (typ='R',statut='o',
                                                                   fr="Temperature initiale combustible pour le calcul du coefficient d'echange") ),
  BlocHgapFixe                        = BLOC (condition = "CoefficientEchangeJeuPastilleGaine=='FIXE'",
                                              Hgap = SIMP (typ='R',statut='o',defaut=5850.,fr="Valeur imposée du coefficient d'echange") ),
  ConductiviteCombustible             = SIMP (typ='TXM',defaut='HGAP_88',into=('STORA','WESTINGHOUSE','HGAP_88','COMETHE'),statut='o',
                                                       fr="Option du Coefficient de conductivite du combustible"),
  CapaciteCalorifiqueCombustible      = SIMP (typ='TXM',defaut='UO2_FRAMATOME',into=('UO2_BATES','UO2_FRAMATOME','UO2_THYC'),statut='o',
                                                       fr="Option du Coefficient de conductivite du combustible"),
  MateriauGaine                       = SIMP (typ='TXM',defaut='ZIRCALOY_CYRANO',into=('ZIRCALOY_CYRANO', 'ZIRCALOY_THYC', 'INCOLOY_800',
                                                               'CHROMESCO_3', 'INOX_16', 'INOX_321', 'INOX_347', 'INOX_347_OXYDE',
                                                               'INCONEL_600', 'NICKEL_75', 'PLATINE'),statut='o',
                                              fr="Materiau de la gaine pour le calcul du roCp de la gaine et de sa conductivite"),
  FluxCritique                        = SIMP (typ='R',defaut=180.E4,statut='o',fr="Valeur du flux critique en W/m2"),
  FractionPuissanceCombustible        = SIMP (typ='R',defaut=0.974,statut='o',fr="Fraction de la puissance degagee dans le combustible"),
  Creusement                          = SIMP (typ='TXM',defaut='Uniforme',statut='o',
                                              into=('Uniforme','Runnals','Framatome','Twinkle','Mox','EDF','Specifique')),
  BlocCreusement                      = BLOC (condition = "Creusement=='Specifique'",
                                              RayonsCreusement = SIMP (typ='R',statut='o',fr="Rayons de definition du creusement de puissance (nz)"),
                                              IrradiationsCreusement = SIMP (typ='R',statut='o',fr="Irradiations de definition du creusement de puissance (nbu)"),
                                              EnrichissementsCreusement = SIMP (typ='R',statut='o',fr="Enrichissements de definition du creusement de puissance (nen)"),
                                              PuissancesUO2 = SIMP (typ='R',max='**',statut='f',fr="Valeurs des creusements de puissance P(nz,nbu,nen) dans une pastille UO2"),
                                              PuissancesMOX = SIMP (typ='R',statut='f',fr="Valeurs des creusements de puissance P(nz,nbu,nen) dans une pastille MOX") ),
  PastilleDiscretisation              = SIMP (typ='I',defaut=4,statut='o',fr="Nombre de points de discretisation radiale de la pastille combustible"),
  GaineDiscretisation                 = SIMP (typ='I',defaut=2,statut='o',
                                              fr="Nombre de points de discretisation radiale de la gaine de la pastille combustible"),
  ThermiquePrecision                  = SIMP (typ='R',defaut=0.1,statut='o',fr="Precision en Celsius du calcul thermique radiale du crayon"),
  ThermohydrauliquePrecision          = SIMP (typ='R',defaut=0.01,statut='o',
                                              fr="Precision en Celsius du calcul thermohydraulique de la temperature du moderateur"),
  MaxIterThermique                    = SIMP (typ='I',defaut=100,statut='o',
                                              fr="Nombre maximum d'iterations du calcul de thermique"),
  MaxIterThermohydraulique            = SIMP (typ='I',defaut=100,statut='o',
                                              fr="Nombre maximum d'iterations du calcul de thermohydraulique"),
  MethodeIntegrationThermohydraulique = SIMP (typ='TXM',defaut='Gauss',statut='o',into=('Gauss','NonGauss'),
                                              fr="Methode d'integration thermohydraulique"),
  PerteDeCharge                       = SIMP (typ='TXM',defaut='Non',statut='o',into=('Non','Oui'),
                                              fr="Prise en compte ou non de la perte de charge axiale"),
  TableEau                            = SIMP (typ='TXM',defaut='Thetis',statut='o',into=('Thetis','Interne'),
                                              fr="Calcul des caracteristiques du moderateur par THETIS ou par des tables internes")
 ) ;  # Fin OPTIONS_THERMIQUE_THERMOHYDRAULIQUE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe OPTIONS_CONTRE_REACTIONS_COEUR : Classe de definition des options du code de coeur en cinetique
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONS_CONTRE_REACTIONS_COEUR = OPER (nom="OPTIONS_CONTRE_REACTIONS_COEUR", op=0, sd_prod=OptionsContreReactionsCoeur, niveau = 'OptionsCodesCalcul',
  fr  = "Definition des options des modules de calcul de contre-reactions coeur",
  ang = "Definition of feedback module options",
  Iter2dCRN            = SIMP (typ='I',defaut=30,statut='o',fr="Nombre maximal d'iterations de contre-reactions en 2D, si 0 pas de CRN"),
  Iter3dCRN            = SIMP (typ='I',defaut=15,statut='o',fr="Nombre maximal d'iterations de contre-reactions en 3D, si 0 pas de CRN"),
  CoeffAttenuation     = SIMP (typ='R',defaut=0.8,statut='o',fr="Coefficient d'attenuation des contre-reactions"),
  PrecisionPuissance   = SIMP (typ='R',defaut=1.E-4,statut='o',fr="Precision sur la puissance a la fin des iterations de contre-reactions"),
  PrecisionKeff        = SIMP (typ='R',defaut=1.E-5,statut='o',fr="Precision sur keff a la fin des iterations de contre-reactions"),
  MethodeCalculSection = SIMP (typ='TXM',defaut='TabulationLineaire',into=('Spline1D','SplinenD','TabulationLineaire'),statut='o',
                               fr="Methode d'interpolation des sections efficaces avec Contre-reactions"),
  FigerCRN             = SIMP (typ='TXM',statut='f',max='**',fr="Liste des parametres de contre-reactions a figer")
 ) ;  # Fin OPTIONS_CONTRE_REACTIONS_COEUR
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe OPTIONS_CODES : Classe de definition des options generales et du type de calcul demande
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONS_CODES = OPER (nom="OPTIONS_CODES", op=0, sd_prod=OptionsCodes, niveau = 'OptionsCodesCalcul',
  fr  = "Definition des options des codes de calcul",
  ang = "Definition of calculation code options",
  regles = (AU_MOINS_UN('OptionsReseau', 'OptionsStatiqueCoeur', 'OptionsCinetiqueCoeur','OptionsThermo', 'OptionsCRNCoeur'),),
  OptionsReseau         = SIMP (typ=OptionsCodeReseau                ,statut='f', fr="Options du code de reseau"),
  OptionsStatiqueCoeur  = SIMP (typ=OptionsCodeCoeurStatique         ,statut='f', fr="Options du code de coeur en statique"),
  OptionsCinetiqueCoeur = SIMP (typ=OptionsCodeCoeurCinetique        ,statut='f', fr="Options du code de coeur en cinetique"),
  OptionsThermo         = SIMP (typ=OptionsThermiqueThermohydraulique,statut='f', fr="Options des modules de thermique et thermohydraulique simplifiées)"),
  OptionsCRNCoeur       = SIMP (typ=OptionsContreReactionsCoeur      ,statut='f', fr="Prise en compte des contre-reactions ou non")
 ) ;  # Fin OPTIONS_CODES
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe RESSOURCES_INFORMATIQUES : Classe de definition des ressources de calcul informatiques
#                                    Cette classe est liee aux possibilites du gestionnaire du traitement par lots et pour le moment
#                                    les attributs affiches sont dependants de LSF :
#                                       si on donne un type   de serveur       : bsub -R "type=USPARC" monjob
#                                       si on donne un modele de serveur       : bsub -R "model=HPK640" monjob
#                                       si on donne un type   de ressource     : bsub -R "Solaris" monjob
#                                       si on donne des machines particulieres : bsub -m " Nommachine1 NomMachine2 " monjob
#				     Dans le cas des machines particulieres, il est necessaire de fournir aussi le systeme d'exploitation
#				     associe (ceci pour distinguer les fichiers necessaires en entree, leurs noms devant contenir
#				     le nom du systeme d'exploitation (les fichiers etant differents a priori suivant l'OS utilise
#				     et de format non portable)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESSOURCES_INFORMATIQUES = OPER (nom="RESSOURCES_INFORMATIQUES",sd_prod=RessourcesInformatiques,op=0,niveau = 'ConfigurationInformatique',
  fr	 = "Definition des systemes d'exploitation et des calculateurs de l'etude",
  ang	 = "Software operating system and computers used",
  regles = (UN_PARMI('TypesServeursCibles', 'ModelesServeursCibles','OSCible','CalculateursCibles'),),
  TypesServeursCibles   = SIMP (typ='TXM',statut='f',max='**',defaut='USPARC' ,into=('SPARC', 'USPARC', 'PWR2', 'HPPA20', 'ALPHA'),
                                fr="Liste des types de serveurs cibles pour la soumission des calculs"),
  ModelesServeursCibles = SIMP (typ='TXM',statut='f',max='**',defaut='U2200'  ,into=('SS1000E','U2200','IBM3BT','HPK460','DEC5400','U1140'),
                                fr="Liste des modeles de serveurs cibles pour la soumission des calculs"),
  OSCible               = SIMP (typ='TXM',statut='f',         defaut='solaris',into=('solaris','aix','usparc','alpha','hpux'),
                                fr="Type de ressource cible pour la soumission des calculs"),
  CalculateursCibles    = NUPL (statut='f',max='**',fr="Liste des noms des calculateurs cibles pour la soumission des calculs",
                                elements = (SIMP (typ='TXM',statut='o',fr="Nom du calculateur cible"),
                                            SIMP (typ='TXM',statut='o',fr="Systeme d'exploitation de la machine cible",
                                                  defaut='solaris',into=('solaris','aix','usparc','alpha','hpux')))
                                )
 ) ;  # Fin RESSOURCES_INFORMATIQUES
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DONNEES_CAS_ETUDE :     Classe de definition des caracteristiques globales d'un cas de l'etude
#                                       Definition de la centrale (site, numero de tranche) et numero de campagne d'irradiation
#                                       Ces caracteristiques  d'environnement de l'etude doivent permettre de recuperer l'ensemble
#                                       des parametres de fonctionnement nominales du reacteur sujet de l'etude (creation de
#                                       bibliotheques ou calcul de coeur)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DONNEES_CAS_ETUDE = OPER (nom="DONNEES_CAS_ETUDE", op=0, sd_prod=DonneesCasEtude, niveau = 'DonneesEtude',
  fr  = "Definition de la centrale sujet du cas de l'etude et des options globales du cas",
  ang = "Definition of the power plant and of the global options of the calculation case",
  TypeCode               = SIMP (typ='TXM',defaut='Reseau',into=('Reseau','Coeur'),statut='o'),
  SiteNucleaire          = SIMP (typ=SiteNucleaire,defaut='TRICASTIN',statut='o'),
  BlocCoeur              = BLOC (condition = "TypeCode=='Coeur'",
                           NumeroTranche          = SIMP (typ='I',defaut=1,statut='o',fr="Numero de la tranche nucleaire"),
                           NumeroCampagne         = SIMP (typ='I',defaut=1,statut='o',fr="Numero de la campagne d'irradiation"),
                           IdentificateurCampagne = SIMP (typ='TXM',defaut='TN101',statut='o',fr="Identificateur de la campagne"),
                           DatesCampagne          = SIMP (typ=DatesClesCampagne,statut='f',fr="Dates cles de la campagne"),
                           TypeGestion            = SIMP (typ    = 'TXM',
                                                          defaut = '370Q',
                                                          statut = 'f', fr="Type de gestion du combustible",
                                                          into   = ('310Q','310T','325T','325Q','340Q','345AL',
                                                                    '370Q','370T','400T','HMOX','MOXNT','TMOX')),
                           TypeSchemaGrappe       = SIMP (typ    = 'TXM',
                                                          defaut = '900CPYUO2',
                                                          statut = 'f',fr="Type de schema d'implantation des grappes",
                                                          into   = ('900CP0','900CPYUO2INITIAL','900CPYUO2',
                                                                    '900CPYUO2AL','900CPYMOX','1300','N4')),
                           TypeEvaluationSurete  = SIMP (typ='TXM',defaut='900STD',statut='f',fr="Type d'evaluation de surete",
                                                         into=('900STD','900GARANCE','1300STD','1300GEMMES','N4STD')),
                           ModePilotage          = SIMP (typ='TXM',defaut='G',statut='f',into=('A','G','X'),fr="Mode de pilotage de la tranche"),
                           ImplantationGrappe    = SIMP (typ=ImplantationGrappesCommande,statut='f',fr="Schema d'implantation des grappes de commande dans le coeur"),
                           PositionAxialeGrappes = SIMP (typ=PositionAxialeGrappesCommande,statut='f',fr="Positions axiales des grappes de commande"),
                           PlanChargement        = SIMP (typ=Reseau,statut='o',fr="Plan de chargement du reseau coeur"),
                           Penalites             = SIMP (typ=PenaliteAssemblage,statut='f',max='**',fr="Liste des objets PenalitesAssemblage"),
                           ActivitesMesurees     = SIMP (typ=ActivitesExperimentales,statut='f',fr="Carte d'activite experimentale"),
#                          OptionsStatique       = SIMP (typ=OptionsCodeCoeurStatique,statut='f'),
#                          OptionsCinetique      = SIMP (typ=OptionsCodeCoeurCinetique,statut='f'),
                           CodeCalculC           = SIMP (typ='TXM',defaut='CodeSn',statut='o',fr="Type de code de coeur a utiliser")),
  BlocReseau            = BLOC (condition = "TypeCode=='Reseau'",
                           Assemblage            = SIMP (typ=(AssemblageType,ReparationAssemblage),statut='o',fr="Objet Assemblage a reparer et a calculer"),
#                          Options               = SIMP (typ=OptionsCodeReseau,statut='f'),
                           CodeCalculR           = SIMP (typ='TXM',defaut='SUNSET',statut='o',fr="Code de reseau a utiliser")),
  Domaines              = SIMP (typ=DecompositionDomaines            ,statut='f',fr="Objet definissant la decomposition de domaines"),
  ConditionsMoyennes    = SIMP (typ=ConditionsFonctionnementMoyennes ,statut='f',fr="Objet definissant les conditions de fonctionnement moyennes"),
  Transitoire           = SIMP (typ=ConditionsTransitoire            ,statut='f',fr="Objet contenant les conditions du transtoire"),
  Variations            = SIMP (typ=EspaceVariations                 ,statut='f',fr="Objet definissant l'espace de variations des parametres d'une etude parametrique"),
  Irradiations          = SIMP (typ=DonneesIrradiation               ,statut='f',fr="Objet definissant les irradiations du calcul"),
  Gestion               = SIMP (typ=ParametresCalculGestion	          ,statut='f',fr="Parametres du calcul de gestion"),
  Ajustement            = SIMP (typ=DonneesAjustement                ,statut='f',fr="Parametres d'ajustement du calcul"),
  Accidents             = SIMP (typ=DonneesAccidents                 ,statut='f',fr="Donnees des calculs d'accidents"),
  Pilotage              = SIMP (typ=DonneesPilotageGeneral           ,statut='f',fr="Donnees generales de pilotage du reacteur"),
  Calibrage             = SIMP (typ=CalibrageGroupes                 ,statut='f',fr="Donnees de calibrage des groupes de commande du reacteur"),
  Stretch               = SIMP (typ=ProlongationCampagne             ,statut='f',fr="Objet definissant la prolongation de campagne"),
  Bibliotheques         = SIMP (typ=FichierBibliothequeIsotopes      ,statut='f',fr="Fichiers des bibliotheques de donnees de base"),
  Ressources            = SIMP (typ=RessourcesInformatiques	          ,statut='f',fr="Objet definissant les ressources informatiques a utiliser"),
  ConditionLimite       = SIMP (typ=GeneraleConditionLimite	          ,statut='o',fr="Objet definissant les conditions limites"),
  Options               = SIMP (typ=OptionsCodes                     ,statut='o',fr="Options des codes impliques dans le calcul"),
  TypeCalcul            = SIMP (typ='TXM',max='**',defaut='Evolution',statut='o',
                                into=('Evolution','EvolutionMicroscopique','EvolutionRefroidissement','Reprise','Statique','Cinetique',
                                      'BoreImpose','BoreCritique')	,fr="Type de calcul demande")
 ) ;  # Fin DONNEES_CAS_ETUDE
class resultat(TObjet): pass
class resultat2(resultat): pass
CALCUL=OPER(nom="CALCUL",op=10,sd_prod=resultat,
            niveau = 'Operateurs',
            materiau=SIMP(typ=Materiau),
            PRESSION=SIMP(defaut=10000.,typ="R")
	    );
CALCUL2=OPER(nom="CALCUL2",op=11,sd_prod=resultat2,
             niveau = 'Operateurs',
             donnee=SIMP(typ=resultat),
             materiau=SIMP(typ=Materiau),
            );
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe SECTIONS_REFLECTEUR : Classe de definition des sections efficaces multigroupes des reflecteurs
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SECTIONS_REFLECTEUR = OPER (nom="SECTIONS_REFLECTEUR",sd_prod=SectionsReflecteur,op=0,niveau = 'SectionsEfficaces',
  fr  = "Definition des sections efficaces equivalentes d'un reflecteur",
  ang = "Equivalent reflector cross sections",
  NbGroupesEnergie	= SIMP (typ='I'  ,statut='o',defaut=2,fr="Nombre de groupes d'energie"),
  LimitesEnergie	= SIMP (typ='R'  ,statut='o',defaut=(0.,0.0625,1.E7),max='**',fr="Limites des groupes d'energie"),
  DeltaLethargie	= SIMP (typ='R'  ,statut='o',max='**',fr="Largeur en lethargie des groupes d'energie"),
  Sections = FACT (min=1, max='**', statut='o',      
                   TypeSection  = SIMP (typ='TXM',fr="Type de section efficace",statut='o',
                                        into=( 'Totale','CorrectionTransport',
                                               'Absorption','Capture','N2N',
                                               'CoefficientDiffusionHomogene','CoefficientsDiffusionOrientes',
                                               'SectionDiffusionTotale','Transfert')),
                   Valeurs = SIMP (typ='R',min=1,max='**',statut='o',
                                   fr="Valeurs des sections efficaces pour le reflecteur")
                   )
  ) ;  # Fin SECTIONS_REFLECTEUR
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe MACROLIB : Classe de definition des sections efficaces multigroupes
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
MACROLIB = OPER (nom="MACROLIB",sd_prod=Macrolib,op=0,niveau = 'SectionsEfficaces',
  fr  = "Definition d'une macrolib",
  ang = "Macrolib Definition",
  Signature            = SIMP (typ='TXM',statut='o',defaut="MACROLIB",fr="Signature de l'objet MACROLIB"),
  NbMateriaux          = SIMP (typ='I'  ,statut='o',defaut=1,fr="Nombre de materiaux"),
  NomsMateriaux        = SIMP (typ='TXM',statut='o',max='**',fr="Noms des materiaux"),
  OrdreAnisotropieMax  = SIMP (typ='I'  ,statut='o',defaut=1,fr="Ordre d'anisotropie"),
  MaxIsotopesFissiles  = SIMP (typ='I'  ,statut='o',fr="Nombre maximum d'isotopes fissiles"),
  NbTypesSections      = SIMP (typ='I'  ,statut='o',fr="Nombre de sections efficaces definies"),
  CorrectionTransport  = SIMP (typ='TXM',statut='o',defaut='Non',into=('Oui','Non'),fr="Indication de Correction de transport"),
  NbGroupesPrecurseurs = SIMP (typ='I'  ,statut='o',defaut=6,fr="Nombre de groupes de precurseurs de neutrons retardes"),
  NbGroupesEnergie     = SIMP (typ='I'  ,statut='o',defaut=2,fr="Nombre de groupes d'energie"),
  LimitesEnergie       = SIMP (typ='R'  ,statut='o',defaut=(0.,0.0625,1.E7),max='**',fr="Limites des groupes d'energie"),
  DeltaLethargie       = SIMP (typ='R'  ,statut='o',max='**',fr="Largeur en lethargie des groupes d'energie"),
  ListeSections        = SIMP (typ='TXM',statut='o',max='**',fr="Liste des sections efficaces decrites dans la Macrolib",
                               into=('Totale','CorrectionTransport','Spectre','Vitesse',
                                     'Production','Fission','Energie','Absorption','Capture','N2N',
                                     'CoefficientDiffusionHomogene','CoefficientsDiffusionOrientes',
                                     'CoefficientEquivalence','ProductionRetardee','SpectreRetarde',
                                     'SectionDiffusionTotale','Transfert')),
  ModeEntreeSections   = SIMP (typ='TXM',statut='o',defaut='ParGroupe',into=('ParGroupe','ParMilieu'),
                               fr="Choix du mode d'entree des sections par groupe ou par milieu"),
  SectionsParGroupe    = BLOC (condition = "ModeEntreeSections=='ParGroupe'",
             SectionsG = FACT (min=1, max='**', statut='o',
                TypeSectionG = SIMP (typ='TXM',fr="Type de section efficace",statut='o',
                             into=('Totale','CorrectionTransport','Spectre','Vitesse',
                                   'Production','Fission','Energie','Absorption','Capture','N2N',
                                   'CoefficientDiffusionHomogene','CoefficientsDiffusionOrientes',
                                   'CoefficientEquivalence','ProductionRetardee','SpectreRetarde',
                                   'SectionDiffusionTotale','Transfert')),
                Groupes = BLOC (condition = "TypeSection=='Transfert'",
                        NumerosGroupes = SIMP (typ='I',min=2,max=2,statut='o',
                                               fr="Numeros des groupes de depart et d'arrivee")),
                Groupe = BLOC (condition = "TypeSection!='Transfert'",
                        NumeroGroupe = SIMP (typ='I',statut='o',fr="Numero de groupe d'energie")),
                BlocAnisotropie = BLOC (condition = "TypeSection=='Transfert' or TypeSection== 'SectionDiffusionTotale'",
                        OrdreAnisotropie = SIMP (typ='I',statut='o',defaut=1,
                                                 fr="Ordre d'anisotropie de la section de transfert")),
                Valeurs = SIMP (typ='R',min=1,max='**',statut='o',
                                fr="Valeurs des sections efficaces pour tous les materiaux")
        )
   ),
  SectionsParMateriau     = BLOC (condition = "ModeEntreeSections=='ParMateriau'",
        Materiau  = SIMP (typ='TXM',statut='o',fr="Nom du materiau dont on valorise les sections efficaces"),
        SectionsM = FACT (min=1, max='**', statut='o',fr="Entree des valeurs de chaque type de section efficace",     
                TypeSectionM  = SIMP (typ='TXM',fr="Type de section efficace definie",statut='o',
                                     into=('Totale','CorrectionTransport','Spectre','Vitesse',
                                           'Production','Fission','Energie','Absorption','Capture','N2N',
                                           'CoefficientDiffusionHomogene','CoefficientsDiffusionOrientes',
                                           'CoefficientEquivalence','ProductionRetardee','SpectreRetarde',
                                           'SectionDiffusionTotale','Transfert')),
                BlocPasTransfert = BLOC (condition = "TypeSection not in ('Transfert','SectionDiffusionTotale')",
                                         ValeursS = SIMP (typ='R',min=1,max='**',statut='o',
                                                          fr="Valeurs des sections efficaces pour tous les groupes")),
                BlocDiffusion = BLOC (condition = "TypeSection=='SectionDiffusionTotale'",
                        OrdreAnisotropieD = SIMP (typ='I',statut='o',defaut=1,
                                                 fr="Ordre d'anisotropie de la section de diffusion totale"),
                        ValeursD = SIMP (typ='R',min=1,max='**',statut='o',
                                         fr="Valeurs des sections de diffusion totale pour tous les groupes")),
                BlocTransfert = BLOC (condition = "TypeSection=='Transfert'",
                        OrdreAnisotropieT = SIMP (typ='I',statut='o',defaut=1,
                                                 fr="Ordre d'anisotropie de la section de transfert"),
                        ValeursT = NUPL (min=1,max='**',statut='o',
                                        elements=(SIMP (typ='I',min=2,max=2,fr="Groupes de depart et d'arrivee"),
                                                  SIMP (typ='R',fr="Valeur de la section de transfert")))
                 )
         )
   )
 ) ;  # Fin MACROLIB
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ASSEMBLAGE_COMBUSTIBLE_REEL : Classe de definition d'un assemblage combustible reel charge ou decharge d'un coeur REP
#  DefautFabrication     : Champ texte indicateur precisant si l'assemblage appartient a un lot de fabrication
#                          ayant un defaut impactant les resultats neutroniques
#  CleControle           : Donnee fournie par la Division Combustible (Fichier ASN) et calculee a partir du nom de l'assemblage
#  IdentificateurInitial : En cas de remplacement de la structure de l'assemblage, ce dernier  change de nom
#                         (donnee transmise par le site)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ASSEMBLAGE_COMBUSTIBLE_REEL = OPER (nom="ASSEMBLAGE_COMBUSTIBLE_REEL",op=0,sd_prod=AssemblageCombustibleReel,
                                        niveau = 'AssemblagesReels',
  fr  = "Definition d'un assemblage combustible a charger, charge en reacteur, ou decharge en coeur, en piscine ou pour retraitement",
  ang = "Definition of a core loaded fuel assembly",
  regles        = (ENSEMBLE('Identificateur','CampagneResquelettage'),
                   ENSEMBLE('ProgrammeExperimental','NatureElementExperimental'),),
  IdentInitial                = SIMP (typ='TXM',statut='o',fr="Code d'identification initial de l'assemblage combustible en cas de resquelettage"),
  Identificateur              = SIMP (typ='TXM',statut='f',fr="Code d'identification de l'assemblage combustible apres resquelettage"),
  CampagneResquelettage       = SIMP (typ='I',statut='f',fr="Numero de la campagne de rechargement de l'assemblage resquelette"),
  Constructeur                = SIMP (typ='TXM',statut='o',into=('FRAMATOME','SIEMENS','ABB','ENUSA','WESTINGHOUSE','CEA','KWU','EXXON','ANF'),
                                      fr="Constructeur de l'assemblage combustible"),
  TypeTechnologique           = SIMP (typ='TXM',defaut='AFA2GE',statut='o',
                                      into=('ABB-97','AB-DEMOS','AB-LFA','AEF-XL',
                                            'AFA','AFA-XL','AFA-XL-N4','AFA2G','AFA2GE','AFA2GL','AFA2GLE','AFA3G','AA3GL','AGI','AGI-XL',
                                            'AKA','ALIX','BM','CEA','DEMONSTRATIONS','ENUSA-LFA','HTP','KWU','X1'),
                                      fr="Type technologique de l'assemblage"),
  TypeAssemblage              = SIMP (typ=AssemblageType,statut='o',fr="Type de l'assemblage"),
  CleControle                 = SIMP (typ='TXM',statut='o',fr="Cle de controle de l'assemblage"),
  Engagement                  = SIMP (typ='TXM',statut='o',fr="Engagement de l'assemblage"),
  NumeroLot                   = SIMP (typ='I',	statut='o',fr="Numero du lot de combustible"),
  TypeCombustibleDuLot        = SIMP (typ='TXM',statut='f',fr="Type combustible et nom du lot (exemple 'MOX FMO1')"),
  U235EnrichissementTheorique = SIMP (typ='R',	statut='o',fr="Enrichissement theorique en U235 du combustible en %"),
  PuEnrichissementTheorique   = SIMP (typ='R',	statut='o',fr="Enrichissement theorique en Pu du combustible en %",defaut=0.),
  MasseTheoriqueNL            = SIMP (typ='R',	statut='o',fr="Masse theorique en g des noyaux lourds  Z > 89 de l'assemblage"),
  MasseInitialeNL             = SIMP (typ='R',	statut='o',fr="Masse initiale reelle en g des noyaux lourds de l'assemblage a la date de reference"),
  U232MasseInitiale           = SIMP (typ='R',	statut='o',fr="Masse initiale reelle en g d'uranium 232",defaut=0.),
  U234MasseInitiale           = SIMP (typ='R',	statut='o',fr="Masse initiale reelle en g d'uranium 234",defaut=0.),
  U235MasseInitiale           = SIMP (typ='R',	statut='o',fr="Masse initiale reelle en g d'uranium 235",defaut=0.),
  U236MasseInitiale           = SIMP (typ='R',	statut='o',fr="Masse initiale reelle en g d'uranium 236",defaut=0.),
  U238MasseInitiale           = SIMP (typ='R',	statut='o',fr="Masse initiale reelle en g d'uranium 238",defaut=0.),
  BlocPu                      = BLOC (condition = "EnrichissementTheoriquePu > 0.",
                                DateReference      = SIMP (typ='I',min=3,max=3,statut='o',fr="Date de reference Jour, Mois, An du lot MOX"),
                                DatePrevDivergence = SIMP (typ='I',min=3,max=3,statut='o',
                                                                     fr="Date de divergence previsionnelle de la tranche chargee de cet assemblage MOX"),
                                DateDivergence     = SIMP (typ='I',min=3,max=3,statut='o',
                                                            fr="Date de divergence reelle de la tranche chargee de cet assemblage MOX"),
                                U235EquivEnrichissement = SIMP (typ='R',statut='f',defaut=3.25,fr="Enrichissement en U235 equivalent"),
                                Pu239MasseInitiale = SIMP (typ='R',statut='o',fr="Masse reelle initiale en g de plutonium 239 a la date de reference"),
                                Pu240MasseInitiale = SIMP (typ='R',statut='o',fr="Masse reelle initiale en g de plutonium 240 a la date de reference"),
                                Pu241MasseInitiale = SIMP (typ='R',statut='o',fr="Masse reelle initiale en g de plutonium 241 a la date de reference"),
                                Pu24MasseInitiale2 = SIMP (typ='R',statut='o',fr="Masse reelle initiale en g de plutonium 242 a la date de reference"),
                                Am241MasseInitiale = SIMP (typ='R',statut='o',fr="Masse reelle initiale en g  d'americium 241 a la date de reference")
                                      ),
  AbsorbantFixe               = SIMP (typ='TXM',statut='f',fr="Texte caracteristique des absorbants fixes inseres dans l'assemblage"),
  DefautFabrication           = SIMP (typ='TXM',statut='f',fr="Libelle du defaut de fabrication"),
  ProgrammeExperimental       = SIMP (typ='TXM',statut='f',fr="Nom du programme experimental s'il s'agit d'un assemblage experimental"),
  NatureElementExperimental   = SIMP (typ='TXM',statut='f',into=('Combustible','Grille','Structure'),fr="Nature de l'element experimental"),
  LocalisationAssemblage      = SIMP (typ='TXM',statut='f',into=('BR Coeur','BK Piscine','HAGUE'),fr="Localisation de l'assemblage"),
  SituationAdministrative     = SIMP (typ='TXM',statut='f',into=('SansParticularite','EnReservePourGestionFuture','EnAttenteReparationExamen',
                                                                 'aDispositionDAC','AccordCogema','IndisponibleSurSite'),
                                      fr="Situation administrative de l'assemblage"),
  EtatGCN                     = SIMP (typ='TXM',statut='f',into=('Evacuable 0','En attente 1','Rechargeable 2','PourAccordCogema 3'),
                                      fr="Etat de l'assemblage au sens GCN"),
  ContraintesPhysiques        = NUPL ( max      = '**',
                                       statut   = 'f',
                                       elements = ( SIMP (typ='TXM',statut='o',fr="Texte precisant la contrainte",
                                                             into=('NonRechargeable','NonSain','aExaminer','aReparer',
                                                                   'Repare','aSubiExtraction','aPenaliser','NonInstrumentable','NonGrappable','Resquelette')),
                                                    SIMP (typ='TXM',statut='o',fr="Premiere Campagne concernee")
                                                   )
                                     ),
  ContraintesNbCycles        = NUPL (max = '**', statut = 'f',
                                     fr       = "Liste des contraintes en nombre de cycles",
                                     elements = ( SIMP (typ='TXM',statut='o',fr="Texte precisant la contrainte",
                                                        into=('NombreDeCyclesSuccessifsImperatif','NombreMaximumDeCycles')),
                                                  SIMP (typ='I',statut='o',fr="Nombre de cycles")
                                                 )
                                    ),
  Campagnes                  = NUPL (max = '**', statut = 'o',
                                     fr       = "Liste des campagnes d'irradiation subies par l'assemblage et etats correspondants",
                                     elements = ( SIMP (typ='TXM',fr="Identificateur de la campagne"),
                                                  SIMP (typ='TXM',fr="Etat de l'assemblage")
                                                 )
                                     ),
  BibliothequesNeutroniques = NUPL (statut='f',elements=(SIMP (typ='TXM',
                                                               fr="Identificateur de non presence d'absorbants (TBH) ou d'insertion (24B, 12B, 8B, 12P, 12P0P, etc)"),
                                                         SIMP (typ='TXM',fr="Nom du fichier de la bibliotheque neutronique associee"))
                                    ),
  TypeDescriptionCalcul = SIMP (typ='TXM',statut='f',defaut='HomogeneAssemblage',into=('HomogeneAssemblage','ParCrayon')),
  OxMaillageIrradiation = SIMP (typ=Maillage1D,statut='f',fr="Maillage suivant l'axe x de l'assemblage"),
  OyMaillageIrradiation = SIMP (typ=Maillage1D,statut='f',fr="Maillage suivant l'axe y de l'assemblage"),
  OzMaillageIrradiation = SIMP (typ=Maillage1D,statut='f',fr="Maillage suivant l'axe z de l'assemblage, Origine en bas de la zone active"),
  IrradiationHomogene	= FACT (max='**',statut='f',fr="Taux d'irradiation pseudo-experimentale de l'assemblage",
                                TempsIrradiation   = SIMP (typ='R', statut='o', fr="Temps d'irradiation en s"),
                                IrradiationMoyenne = SIMP (typ='R', statut='o', fr="Irradiation moyenne MWj/t de l'assemblage"),
                                IrradiationCycle   = SIMP (typ='R', statut='o', fr="Irradiation moyenne MWj/t de l'assemblage lors du cycle en cours"),
                                Irradiations       = SIMP (typ='R', max='**', statut='o', fr="Irradiations des mailles (MWj/t) (en partant du bas et a gauche et par plan)")
                                ),
  IrradiationCrayon	= FACT (max='**',statut='f',fr="Taux d'irradiation pseudo-experimentale des crayons de l'assemblage",
                                TempsIrradiation   = SIMP (typ='R', statut='o', fr="Temps d'irradiation en s  de l'assemblage"),
                                IrradiationMoyenne = SIMP (typ='R', statut='o', fr="Irradiation moyenne MWj/t de l'assemblage"),
                                Irradiations       = SIMP (typ='R', max='**', statut='o', fr="Irradiations des crayons (MWj/t) (en partant du bas et a gauche et par plan)")
                                ),
  FluenceHomogene	= FACT (max='**',statut='f',
                                TempsIrradiation = SIMP (typ='R', statut='o', fr="Temps d'irradiation en s de l'assemblage"),
                                FluenceMoyenne   = SIMP (typ='R', statut='o', fr="Fluence moyenne n/kb de l'assemblage"),
                                Fluences         = SIMP (typ='R', max='**', statut='o', fr="Fluences des mailles (n/kb) (en partant du bas et a gauche et par plan)")
                                ),
  FluenceCrayon	= FACT (max='**',statut='f',
                                TempsIrradiation = SIMP (typ='R', statut='o', fr="Temps d'irradiation en s de l'assemblage"),
                                FluenceMoyenne   = SIMP (typ='R', statut='o', fr="Fluence moyenne n/kb de l'assemblage"),
                                Fluences         = SIMP (typ='R', max='**', statut='o', fr="Fluences des crayons (n/kb) (en partant du bas et a gauche et par plan)")
                                ),
  CompositionHomogene	= FACT (max='**',statut='f',
                                TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
                                IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t de l'assemblage"),
                                FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb de l'assemblage"),
                                Isotopes           = SIMP (typ='TXM', statut='o', max='**',fr="Liste des noms des isotopes"),
                                Concentrations     = SIMP (typ='R'  , statut='o', max='**',
                                                           fr="Concentrations des isotopes pour chaque maille radiale et pour chaque plan axial")
                                ),
  CompositionCrayon	= FACT (max='**',statut='f',
                                TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s de l'assemblage"),
                                IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t de l'assemblage"),
                                FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
                                Isotopes           = SIMP (typ='TXM', statut='o', max='**',fr="Liste des noms des isotopes"),
                                Concentrations     = SIMP (typ='R'  , statut='o', max='**',
                                                           fr="Concentrations des isotopes pour chaque crayon et pour chaque plan axial (du bas vers le haut)")
                                )
  ) ;  # Fin ASSEMBLAGE_COMBUSTIBLE_REEL
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe REPARATION_ASSEMBLAGE : Classe de definition des donnees de reparation d'un assemblage
#                                 Donnee de l'assemblage a reparer et des crayons de remplacement
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
REPARATION_ASSEMBLAGE = OPER (nom="REPARATION_ASSEMBLAGE", op=0, sd_prod=ReparationAssemblage, niveau = 'AssemblagesReels',
  fr  = "Donnee de reparation ou de restauration d'un assemblage",
  ang = "Data for an assembly repair",
  AssemblageInitial  = SIMP (typ=(AssemblageType,AssemblageCombustibleReel),statut='o',fr="Type de l'assemblage a reparer"),
  IrradiationMoyenne = SIMP (typ='R',statut='o',fr="Taux d'irradiation moyenne MWj/t de l'assemblage a reparer"),
  CrayonRemplacement = FACT (max='**',statut='o',
  			     Position            = SIMP (typ='I', min=2, max=2, statut='o', fr="Coordonnees x,y du crayon a remplacer dans l'assemblage"),
			     CelluleRemplacement = SIMP (typ=Cellule, statut='o', fr="Cellule de remplacement")
                             )
   ) ; # Fin REPARATION_ASSEMBLAGE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PENALITE_ASSEMBLAGE : Classe de definition des penalites a appliquer aux puissances des crayons d'un assemblage
#  Trois possibilites :	1) de maniere uniforme
#			2) a quelques crayons
#			3) a l'ensemble des crayons et en fonction du taux d'irradiation de l'assemblage
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PENALITE_ASSEMBLAGE = OPER (nom="PENALITE_ASSEMBLAGE", op=0, sd_prod=PenaliteAssemblage, niveau = 'AssemblagesReels',
  fr  = "Penalites dues a la reparation ou a la restauration d'un assemblage",
  ang = "Penalties applied to a repaired assembly",
  Assemblage = SIMP (typ=(AssemblageType,AssemblageCombustibleReel),statut='o',fr="Type de l'assemblage concerne par les penalites"),
  regles = (UN_PARMI('UniformeDeltaP', 'CrayonDeltaP','CarteDeltaP'),),
  UniformeDeltaP = SIMP (typ='R', statut='f', fr="Penalite en % a appliquer de maniere uniforme sur l'assemblage"),
  CrayonDeltaP = FACT (statut='f',fr="Liste des penalites pour une liste particuliere de crayons d'un assemblage",
                 Crayons = SIMP (typ='I', statut='o', max='**', fr="Numeros des crayons de l'assemblage"),
                 DeltaP  = SIMP (typ='R', statut='o', max='**', fr="Penalites en % a appliquer aux crayons listes")),
  CarteDeltaP  = FACT (max='**',statut='f',fr="Penalites pour l'ensemble des crayons de l'assemblage",
                 BuMoyen = SIMP (typ='R', statut='o',fr="Taux d'irradiation MWj/t de l'assemblage a reparer"),
                 DeltaP  = SIMP (typ='R', statut='o', max='**', fr="Pourcentage de variation de puissance par crayon en %"))
) ; # Fin PENALITE_ASSEMBLAGE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RESULTATS_GLOBAUX_COEUR : Classe de stockage des resultats globaux du coeur
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESULTATS_GLOBAUX_COEUR = OPER (nom="RESULTATS_GLOBAUX_COEUR", op=0, sd_prod=ResultatsGlobauxCoeur, niveau = 'Resultats',
  fr  = "Resultats globaux du calcul de coeur",
  ang = "Global Core Calculation Results",
  ResultatsCoeur = FACT (max='**',statut='o',fr="Resultats globaux du calcul de coeur calcules a un instant et pour une configuration donnee",
        Configuration       = SIMP (typ='TXM', statut='o', max='**', fr="Configuration du coeur : Liste des groupes ou grappes inseres"),
        PasInsertion        = SIMP (typ='I'  , statut='o', max='**', fr="Niveau d'insertion des groupes ou grappes inseres en nombre de pas extraits"),
        IndiceConvergence   = SIMP (typ='I'  , statut='o', fr="Indice de convergence du calcul"),
        TempsIrradiation    = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
        IrradiationMoyenne  = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t"),
        FluenceMoyenne      = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
        NiveauPuissance     = SIMP (typ='R'  , statut='o', fr="Niveau de puissance du calcul en %"),
        TypeDeCalcul        = SIMP (typ='TXM', statut='o', fr="Type de calcul de coeur Critique ou non"),
        ParametreCritique   = SIMP (typ='TXM', statut='o', fr="Parametre critique du calcul de coeur"),
        TitreBore           = SIMP (typ='R'  , statut='o', fr="Titre en bore soluble du calcul de coeur en ppm"),
        EfficaciteBore      = SIMP (typ='R'  , statut='o', fr="Efficacite differentielle du bore soluble pcm/ppm"),
        Reactivite          = SIMP (typ='R'  , statut='o', fr="Reactivite du calcul en pcm"),
        B2AxialRapide       = SIMP (typ='R'  , statut='o', fr="Laplacien axial rapide en cm-2"),
        B2AxialThermique    = SIMP (typ='R'  , statut='o', fr="Laplacien axial thermique en cm-2"),
        XeAntireactivite    = SIMP (typ='R'  , statut='o', fr="Antireactivite du xenon en pcm"),
        FxyAssemblage       = SIMP (typ='R'  , statut='o', fr="Fxy Assemblage"),
        DopplerCoefficient  = SIMP (typ='R'  , statut='o', fr="Coefficient Doppler en pcm/C"),
        CTModerateur        = SIMP (typ='R'  , statut='o', fr="Coefficient Temperature moderateur en pcm/C"),
        DopplerPuissance    = SIMP (typ='R'  , statut='o', fr="Coefficient Puissance Doppler seul en pcm/%P"),
        CoeffPuissance      = SIMP (typ='R'  , statut='o', fr="Coefficient Puissance en pcm/%P"),
        EfficDiffGrappes    = SIMP (typ='R'  , statut='f', max='**',
                                    fr="Efficacites differentielles des grappes inserees, Couples de valeurs (Insertion,Efficacite differentielle)"),
        Bite                = SIMP (typ='R'  , statut='f', fr="Position du bite en cours d'evolution, en nombre de pas extraits"),
        RMBM                = SIMP (typ='R'  , statut='f', fr="Position Milieu de la bande de manoeuvre du groupe R, en nombre de pas extraits"),
        FxyCrayon           = SIMP (typ='R'  , statut='f', fr="Fxy Crayon (apres factorisation eventuelle)"),
        AssemblageChaud     = SIMP (typ='R'  , statut='f', fr="Assemblage portant le crayon chaud"),
        LotAssemblageChaud  = SIMP (typ='I'  , statut='f', fr="Lot de l'assemblage portant le crayon chaud"),
        NumeroCrayonChaud   = SIMP (typ='I'  , statut='f', fr="Numero du crayon chaud dans l'assemblage chaud"),
        TmEntreeCoeur       = SIMP (typ='R'  , statut='o', fr="Temperature entree coeur en Celsius"),
        TmMoyenneCuve       = SIMP (typ='R'  , statut='o', fr="Temperature moyenne cuve en Celsius"),
        PressionEntreeCoeur = SIMP (typ='R'  , statut='o', fr="Pression entree coeur en bars"),
        PressionSortieCoeur = SIMP (typ='R'  , statut='o', fr="Pression sortie coeur en bars"),
        AOCoeur             = SIMP (typ='R'  , statut='o', fr="Axial Offset Coeur en %"),
        DeltaICoeur         = SIMP (typ='R'  , statut='o', fr="Desequilibre Axial Coeur"),
        AOXenon             = SIMP (typ='R'  , statut='o', fr="Axial Offset Xenon Coeur en %"),
        AOIode              = SIMP (typ='R'  , statut='o', fr="Axial Offset Iode Coeur en %"),
        FzCoeur             = SIMP (typ='R'  , statut='o', fr="Fz Coeur"),
        FDH                 = SIMP (typ='R'  , statut='o', fr="Facteur d'elevation d'enthalpie Coeur"),
        FQ                  = SIMP (typ='R'  , statut='o', fr="Facteur de point chaud Coeur Fq"),
        FQCote              = SIMP (typ='R'  , statut='o', fr="Cote du Facteur de point chaud Coeur Fq"),
        FQAssemblage        = SIMP (typ='R'  , statut='o', fr="Repere de l'assemblage portant le facteur de point chaud Fq"),
        FQCrayon            = SIMP (typ='R'  , statut='o', fr="Numero de crayon de l'assemblage portant le facteur de point chaud Fq"),
        FQLot               = SIMP (typ='R'  , statut='o', fr="Numero de lot de l'assemblage portant le facteur de point chaud Fq"),
        TiltRadial4         = SIMP (typ='R'  , statut='o', fr="Desequilibre radial par quart de coeur NE, NO, SO, SE", min=4,max=4),
        TiltRadial8         = SIMP (typ='R'  , statut='o',
                                    fr="Desequilibre radial par huitieme de coeur, Origine en Ox et sens trigonometrique", min=8,max=8),
        BetaTotal           = SIMP (typ='R'  , statut='f', fr="Contribution des neutrons retardes Beta total Coeur"),
        BetaEffTotal        = SIMP (typ='R'  , statut='f', fr="Contribution des neutrons retardes Beta effectif total Coeur"),
        ImportanceTotale    = SIMP (typ='R'  , statut='f', fr="Importance totale Coeur"),
        TempsViePrompt      = SIMP (typ='R'  , statut='f', fr="Temps de vie effectif des neutrons prompts"),
        ProductionU5        = SIMP (typ='R'  , statut='f', fr="Contribution U235 a la production totale nuSf"),
        ProductionU8        = SIMP (typ='R'  , statut='f', fr="Contribution U238 a la production totale nuSf"),
        ProductionPu        = SIMP (typ='R'  , statut='f', fr="Contribution Pu9+Pu0+Pu1+Pu2 a la production totale nuSf"),
        Lambdai             = SIMP (typ='R'  , statut='f', fr="Constantes de decroissance moyennes des 6 groupes de precurseurs", min=6,max=6),
        Betai               = SIMP (typ='R'  , statut='f', fr="Contribution des neutrons retardes Beta i des 6 groupes de precurseurs", min=6,max=6),
        BetaiEff            = SIMP (typ='R'  , statut='f', fr="Contribution des neutrons retardes Beta i effectif des 6 groupes de precurseurs", min=6,max=6),
        RoNordheim          = FACT (statut='f', fr="Reactivite en fct du temps de doublement par la relation de Nordheim",
                                  Temps = SIMP (typ='R', statut='o', max='**', fr="Liste des temps de doublement en s"),
                                  Ro    = SIMP (typ='R', statut='o', max='**', fr="Liste des reactivites correspondantes en pcm"))
  )
) ;  # Fin RESULTATS_GLOBAUX_COEUR
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RESULTAT_FLUX : Classe de stockage des resultats de flux et des courants (a revoir pour ces derniers)
#  L'edition se fait sur les mailles du reseau associe a l'etude (PlanChargement)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESULTAT_FLUX = OPER (nom="RESULTAT_FLUX", op=0, sd_prod=ResultatFlux, niveau = 'Resultats',
  fr  = "Distributions de flux moyens et de courants",
  ang = "Average Flux and current distributions",
  NbAssemblages = SIMP (typ='I'  , statut='o', fr="Nombre d'assemblages edites"),
  OzNbValeurs   = SIMP (typ='I'  , statut='o', fr="Nombre de mailles axiales par assemblage"),
  OzMaillage    = SIMP (typ=Maillage1D  , statut='o', fr="Maillage axial d'edition"),
  NbGroupes     = SIMP (typ='I'  , statut='o', fr="Nombre de groupes d'energie"),
  NbFluxBord    = SIMP (typ='I'  , statut='o', fr="Nombre de flux au bord par assemblage et par groupe d'energie"),
  NbCourant     = SIMP (typ='I'  , statut='o', fr="Nombre de courants par assemblage et par groupe d'energie"),
  Flux = FACT (max='**',statut='o',fr="Flux calcules a un instant et pour une configuration donnee",
        Configuration      = SIMP (typ='TXM', statut='o', fr="Configuration du coeur ou de l'assemblage"),
        TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
        IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t"),
        FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
        Valeurs            = SIMP (typ='R'  , statut='o', max='**',
                                   fr="Flux moyens par assemblage (en partant du bas a gauche) et par groupe")
               ),
  FluxBord = FACT (max='**',statut='f',fr="Flux moyens au bord des assemblages calcules a un instant et pour une configuration donnee",
        Configuration      = SIMP (typ='TXM', statut='o', fr="Configuration du coeur ou de l'assemblage"),
        TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
        IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t"),
        FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
        Valeurs            = SIMP (typ='R'  , statut='o', max='**',
                                   fr="Flux moyens au bord par assemblage (en partant du bas a gauche) et par groupe")
                  ),
  Courant = FACT (max='**',statut='f',fr="Courants calcules a un instant et pour une configuration donnee",
        Configuration      = SIMP (typ='TXM', statut='o', fr="Configuration du coeur ou de l'assemblage"),
        TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
        IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t"),
        FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
        Valeurs            = SIMP (typ='R'  , statut='o', max='**',
                                   fr="Courants detailles par assemblage (en partant du bas a gauche) et par groupe")
                  )
  ) ;  # Fin RESULTAT_FLUX
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RESULTAT_PUISSANCES : Classe de stockage des resultats de puissance
#  L'edition se fait sur les mailles actives du reseau associe a l'etude (PlanChargement)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESULTAT_PUISSANCES = OPER (nom="RESULTAT_PUISSANCES", op=0, sd_prod=ResultatPuissances, niveau = 'Resultats',
  fr  = "Distribution de puissance",
  ang = "Power distributions",
  NbAssemblages  = SIMP (typ='I'  , statut='o', fr="Nombre d'assemblages edites"),
  OzNbValeurs    = SIMP (typ='I'  , statut='o', fr="Nombre de mailles axiales par assemblage"),
  OzMaillage     = SIMP (typ=Maillage1D  , statut='o', fr="Maillage axial d'edition"),
  Puissances               = FACT (max='**',statut='o',fr="Puissances calculees a un instant et pour une configuration donnee",
        Configuration      = SIMP (typ='TXM', statut='o', fr="Configuration du coeur ou de l'assemblage"),
        TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
        IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t"),
        FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
        Valeurs            = SIMP (typ='R'  , statut='o', max='**',
                                   fr="Puissances (en partant du bas a gauche) par assemblage")
  )
) ;  # Fin RESULTAT_PUISSANCES
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RESULTAT_RADIAL : Classe de stockage des resultats integres sur une zone axiale particuliere (par defaut, toute la zone active)
#  L'edition se fait sur les mailles du reseau associe a l'etude (PlanChargement)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESULTAT_RADIAL = OPER (nom="RESULTAT_RADIAL", op=0, sd_prod=ResultatRadial, niveau = 'Resultats',
  fr  = "Distribution radiale 2D apres integration axiale d'un type de resultat",
  ang = "Radial Result Distribution",
  TypeResultat	= SIMP (typ='TXM', statut='o', into=('Puissance','Flux','Activite','Irradiation','IrradiationGradient4','Importance',
                                                     'FDHmax','FDHcrayon','TauxReaction','TauxReactionParGroupe','SectionEfficace',
                                                     'SectionEfficaceParGroupe','Kinf','AntireactiviteXenon','AntireactiviteIode',
                                                     'AOPuissance','Tc','TcMax','Tm','TmMax','RoModerateur','Tgaine'),
                                                      fr="Type de resultat"),
# BlocGroupe	= BLOC (condition = "TypeResultat in ['Flux','TauxReactionParGroupe','SectionEfficaceParGroupe']",
        NumeroGroupe	   = SIMP (typ='I'  , statut='o', max=2, fr="Numeros de groupe d'energie associes"),
# ),
# BlocSection	= BLOC (condition = "TypeResultat in ['SectionEfficaceParGroupe','TauxReactionParGroupe','SectionEfficace','TauxReaction']",
        TypeSection	   = SIMP (typ='TXM'  , statut='o', fr="Type de section concerne"),
# ),
  CotesAxiales  = SIMP (typ='R', statut='f', min=2,max=2, fr="Cotes axiales de la zone moyennee"),
  Radial = FACT (max='**',statut='o',fr="Distribution radiale 2D calculee a un instant et pour une configuration donnee",
        Configuration      = SIMP (typ='TXM', statut='o', fr="Configuration du coeur ou de l'assemblage"),
        TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
        IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t"),
        FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
        Valeurs            = SIMP (typ=('R','I'), statut='o', max='**',
                                   fr="Valeurs (en partant du bas a gauche) par assemblage")
  )
) ;  # Fin RESULTAT_RADIAL
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RESULTAT_AXIAL : Classe de stockage des resultats moyennes axialement sur l'ensemble du reseau combustible
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESULTAT_AXIAL = OPER (nom="RESULTAT_AXIAL", op=0, sd_prod=ResultatAxial, niveau = 'Resultats',
  fr  = "Distribution axiale moyenne coeur",
  ang = "Average Core Axial Distribution",
  OzNbValeurs	= SIMP (typ='I', statut='o', fr="Nombre de mailles axiales"),
  OzMaillage	= SIMP (typ=Maillage1D, statut='o', fr="Maillage axial d'edition"),
  TypeResultat	= SIMP (typ='TXM', statut='o', into=('Puissance','Flux','Xenon','Iode','Courant','Fxy(z)','Q(z)'), fr="Type de resultat"),
  BlocGroupe	= BLOC (condition = "TypeResultat in ('Flux','Courant')",
        NumeroGroupe	   = SIMP (typ='I'  , statut='o', fr="Numero de groupe d'energie")),
  Axial = FACT (max='**',statut='o',fr="Distribution axiale a un instant et pour une configuration donnee",
        Configuration      = SIMP (typ='TXM', statut='o', fr="Configuration du coeur ou de l'assemblage"),
        TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
        IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t"),
        FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
        Valeurs            = SIMP (typ='R'  , statut='o', max='**',
                                   fr="Distribution axiale moyenne (en partant du bas)")
                                )
  ) ;  # Fin RESULTAT_AXIAL
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RESULTAT_IRRADIATIONS : Classe de stockage des resultats de taux d'irradiation
#  L'edition se fait sur les mailles du reseau associe a l'etude (PlanChargement)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESULTAT_IRRADIATIONS = OPER (nom="RESULTAT_IRRADIATIONS", op=0, sd_prod=ResultatIrradiations, niveau = 'Resultats',
  fr  = "Distribution de taux d'irradiation",
  ang = "Burnup distributions",
  NbAssemblages  = SIMP (typ='I', statut='o', fr="Nombre d'assemblages"),
  OzNbValeurs    = SIMP (typ='I', statut='o', fr="Nombre de valeurs d'irradiation par assemblage"),
  OzMaillage     = SIMP (typ=Maillage1D, statut='o', fr="Maillage axial d'edition des irradiations"),
  Gradient       = SIMP (typ='I', statut='o', defaut=4, fr="Nombre de valeurs d'irradiation par assemblage"),
  Irradiation              = FACT (max='**',statut='o',fr="Irradiations calculees a un instant et pour une configuration donnee",
        Configuration      = SIMP (typ='TXM', statut='o', fr="Configuration du coeur ou de l'assemblage"),
        TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
        IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t"),
        FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
        Valeurs            = SIMP (typ='R'  , statut='o', max='**',
                                   fr="Irradiations (en partant du bas a gauche) par assemblage")
  )
) ;  # Fin RESULTAT_IRRADIATIONS
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RESULTAT_ACTIVITES : Classe de stockage des resultats d'activite au centre des assemblages instrumentes
#  L'edition se fait sur une liste particuliere d'assemblages du reseau associe a l'etude (PlanChargement)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESULTAT_ACTIVITES = OPER (nom="RESULTAT_ACTIVITES", op=0, sd_prod=ResultatActivites, niveau = 'Resultats',
  fr  = "Distributions d'activite des detecteurs",
  ang = "Detector Activity distributions",
  NbAssemblages      = SIMP (typ='I'        , statut='o', fr="Nombre d'assemblages dont on fournit l'activite calculee"),
  ReperesAssemblages = SIMP (typ='TXM'      , statut='o', fr="Reperes des assemblages dont on fournit l'activite", max='**'),
  OzNbValeurs        = SIMP (typ='I'        , statut='o', fr="Nombre de valeurs d'activite par assemblage"),
  OzMaillage         = SIMP (typ=Maillage1D , statut='o', fr="Maillage axial d'edition des activites"),
  CarteActivite            = FACT (max='**' , statut='o',fr="Activites calculees a un instant et pour une configuration donnee",
        Configuration      = SIMP (typ='TXM', statut='o', fr="Configuration du coeur ou de l'assemblage"),
        TempsIrradiation   = SIMP (typ='R'  , statut='o', fr="Temps d'irradiation en s"),
        IrradiationMoyenne = SIMP (typ='R'  , statut='o', fr="Irradiation moyenne MWj/t"),
        FluenceMoyenne     = SIMP (typ='R'  , statut='o', fr="Fluence moyenne n/kb"),
        Valeurs            = SIMP (typ='R'  , statut='o', max='**',
                                   fr="Activites par assemblage (en partant du bas) dans l'ordre de la liste fournie des assemblages")
  )
) ;  # Fin RESULTAT_ACTIVITES
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ACTIVITES_EXPERIMENTALES : Classe de stockage des cartes d'activite mesuree au centre des assemblages instrumentes
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ACTIVITES_EXPERIMENTALES = OPER (nom="ACTIVITES_EXPERIMENTALES", op=0, sd_prod=ActivitesExperimentales, niveau = 'ResultatsExperimentaux',
  fr  = "Distributions experimentales d'activite mesuree dans les detecteurs mobiles",
  ang = "Measured Detector Activity distributions",
  CaracteristiquesCarte       = FACT (statut='o',fr="Caracteristiques de la carte d'Activite mesurees",
        Site                  = SIMP (typ=SiteNucleaire, statut='o', fr="Site nucleaire de realisation de la carte de flux"),
        Tranche               = SIMP (typ='I', statut='o', fr="Numero de la tranche nucleaire"),
        Campagne              = SIMP (typ='I', statut='o', fr="Numero de la campagne d'irradiation"),
        IrradiationMoyenne    = SIMP (typ='R', statut='o', fr="Irradiation moyenne MWj/t au debut de la carte"),
        TitreBoreSoluble      = SIMP (typ='I', statut='o', fr="Titre en ppm en bore soluble du moderateur"),
        EnergieProduite       = SIMP (typ='R', statut='o', fr="Energie produite en MWh"),
        NumeroCarte           = SIMP (typ='I', statut='o', fr="Numero de la carte de flux"),
        ValiditeCarte         = SIMP (typ='TXM', statut='o', into=('Oui','Non'),fr="Validite ou non de la carte de flux"),
        DateHeureCarte        = SIMP (typ='I', min=5, max=5, statut='o', fr="Date (Jour Mois An) et heure (Heure Minute)de realisation de la carte de flux"),
        PuissanceElectrique   = SIMP (typ='R', statut='o', fr="Puissance electrique MW au debut de la carte de flux"),
        PuissanceRelative     = SIMP (typ='R', statut='o', fr="Puissance relative % au debut de la carte de flux"),
        ModePilotage          = SIMP (typ='TXM', statut='o', fr="Mode de pilotage du reacteur"),
        GroupesInseres        = SIMP (typ='TXM', statut='f', fr="Groupes inseres dans le coeur"),
        PositionsGroupes      = SIMP (typ='I'  , statut='f', fr="Positions des groupes inseres dans le coeur en nb de pas extraits"),
        NbPointsAxiaux        = SIMP (typ='I'  , statut='o', fr="Nombre de points mesures par trace axiale"),
        NbPasses              = SIMP (typ='I'  , statut='o', fr="Nombre de passes de mesures"),
        NbTracesAxiales       = SIMP (typ='I'  , statut='o', fr="Nombre de traces axiales d'activite mesuree"),
        NbThermocouples       = SIMP (typ='I'  , statut='o', fr="Nombre de thermocouples"),
        ReperesThermocouples  = SIMP (typ='TXM', statut='f', max='**', fr="Reperes des thermocouples dans le coeur"),
        NumerosThermocouples  = SIMP (typ='I'  , statut='f', max='**', fr="Numeros des thermocouples dans le coeur")
                                ),
  ActivitesAxiales = FACT (statut='o',max='**',fr="Trace axiale d'activite mesuree",
        RepereAssemblage   = SIMP (typ='TXM', statut='o', fr="Repere de l'assemblage instrumente"),
        HeureDeMesure      = SIMP (typ='I', min=5, max=5, statut='o', fr="Date (Jour Mois An) et heure (Heure Minute)de realisation de la carte de flux"),
        NumeroDetecteur    = SIMP (typ='I', statut='o', fr="Numero du detecteur de mesure"),
        NumeroFourreau     = SIMP (typ='I', statut='o', fr="Numero de fourreau de mesure"),
        NumeroPasse        = SIMP (typ='I', statut='o', fr="Numero de la passe de mesure"),
        PuissanceThermique = SIMP (typ='R', statut='o', fr="Puissance thermique MWth au moment de la passe"),
        ValeursActivites   = SIMP (typ='R', statut='o', max='**',
                                                        fr="Trace d'activite dans l'assemblage (en partant du bas)"),
                          ),
  ChambresExternes = FACT (statut='f',max='**',fr="Courants mesures dans les chambres externes",
        NumeroPasse = SIMP (typ='I', statut='o',            fr="Numero de la passe de mesure"),
        Courants    = SIMP (typ='R', statut='o', max= '**', fr="Valeurs des courants mesures")
                          ),
  Thermohydraulique = FACT (statut='f',max='**',fr="Temperatures et pressions mesurees dans les boucles primaires",
        NumeroPasse       = SIMP (typ='I', statut='o',               fr="Numero de la passe de mesure"),
        TemperatureEntree = SIMP (typ='R', statut='o', min=3,max= 4, fr="Valeurs des temperatures mesurees en entree des boucles"),
        TemperatureSortie = SIMP (typ='R', statut='o', min=3,max= 4, fr="Valeurs des temperatures mesurees en sortie des boucles"),
        DeltaTemperature  = SIMP (typ='R', statut='o', min=3,max= 4, fr="Ecarts de temperature mesurees sur les boucles"),
        IndiceFctBoucles  = SIMP (typ='I', statut='o', min=3,max= 4, fr="Indices de fonctionnement des boucles")
                          ),
  Thermocouples = FACT (statut='f',max='**',fr="Temperatures mesurees par les thermocouples",
        NumeroPasse = SIMP (typ='I', statut='o', fr="Numero de la passe de mesure"),
        Temperature = SIMP (typ='R', statut='o', max= '**', fr="Temperatures mesurees par les thermocouples")
                       )
  ) ; # Fin ACTIVITES_EXPERIMENTALES
# -----------------------------------------------------------------------------------------------------------------------------------
#   Classe RESULTATS_ETUDE : Classe de definition des resultats d'une etude
#                               Regroupement des resultats d'une etude en fonction des donnees
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESULTATS_ETUDE = OPER (nom="RESULTATS_ETUDE", op=0, sd_prod=ResultatsEtude, niveau = 'Resultats',
  fr  = "Resultats de tous les cas d'une etude",
  ang = "Cases and associated Results",
  Resultats = FACT (statut='o',max='**',
        Donnees          = SIMP (typ=DonneesCasEtude       ,statut='o',fr="Objet DonneesGeneralesEtude auquel sont associes les objets resultats "),
        Sections         = SIMP (typ=Macrolib              ,statut='f',max='**',fr="Liste des Objets Sections issus du calcul"),
        Flux             = SIMP (typ=ResultatFlux          ,statut='f',max='**',fr="Liste des Objets Flux issus du calcul"),
        Puissances       = SIMP (typ=ResultatPuissances    ,statut='f',max='**',fr="Liste des Objets Puissances"),
        Activites        = SIMP (typ=ResultatActivites     ,statut='f',max='**',fr="Liste des Objets Activites"),
        Irradiations     = SIMP (typ=ResultatIrradiations  ,statut='f',max='**',fr="Liste des Objets Irradiations"),
        ResultatsGlobaux = SIMP (typ=ResultatsGlobauxCoeur ,statut='f',max='**',fr="Liste des Objets contenant les resultats globaux"),
        ResultatsAxiaux  = SIMP (typ=ResultatAxial	   ,statut='f',max='**',fr="Liste des Objets contenant les resultats axiaux"),
        ResultatsRadiaux = SIMP (typ=ResultatRadial	   ,statut='f',max='**',fr="Liste des Objets contenant les resultats radiaux"),
        Accidents        = SIMP (typ=AccidentsResultats,statut='f',         fr="Resultats des calculs d'accidents"),
        Gestion          = SIMP (typ=ResultatsCalculGestion,statut='f',max='**',fr="Liste des Objets contenant les resultats de calcul de gestion")
   )
 ) ;  # Fin RESULTATS_ETUDE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DICTIONNAIRE_CAS_ETUDE : Classe de definition de l'ensemble des resultats d'une etude
#                                  Regroupement des resultats d'une etude en fonction des donnees
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DICTIONNAIRE_CAS_ETUDE = OPER (nom="DICTIONNAIRE_CAS_ETUDE", op=0, sd_prod=DictionnaireCasEtude, niveau = 'EtudeGenerale',
  fr  = "Dictionnaire des resultats de tous les cas d'une etude",
  ang = "Cases and associated Results dictionary",
  AssociationDonneesResultats = FACT (statut='o',max='**',
        Donnees   = SIMP (typ=DonneesCasEtude,statut='o',fr="Objet DonneesGeneralesEtude auquel sont associes les objets resultats"),
        Resultats = SIMP (typ=ResultatsEtude,statut='o',max='**',fr="Liste des Objets regroupement des resultats")
   )
 ) ;    # Fin DICTIONNAIRE_CAS_ETUDE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PROLONGATION_CAMPAGNE : Classe de definition des donnees de prolongation de campagne
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PROLONGATION_CAMPAGNE = OPER (nom="PROLONGATION_CAMPAGNE", op=0, sd_prod=ProlongationCampagne, niveau = 'DonneesPilotage',
  fr  = "Donnees de la prolongation de campagne ",
  ang = "Stretch out Data",
  NbPas              = SIMP (typ='I',statut='o',fr="Nombre d'instants (en JEPP) descriptifs de la prolongation de campagne"),
  Jepp               = SIMP (typ='R',statut='o',max='**',fr="Instants descriptifs de la prolongation de campagne, en JEPP"),
  Puissance          = SIMP (typ='R',statut='o',max='**',fr="Niveaux de puissance % correspondant aux Jepp de la prolongation de campagne"),
  Temperature        = SIMP (typ='R',statut='o',max='**',fr="Temperatures Moderateur (Celsius) correspondant aux Jepp de la prolongation de campagne"),
  PositionRegulation = SIMP (typ='R',statut='o',defaut=221.,fr="Position du groupe de regulation en nombre de pas extraits")
 ) ;  # Fin PROLONGATION_CAMPAGNE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DONNEES_PILOTAGE_GENERAL : Classe de definition des donnees de pilotage general du reacteur
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DONNEES_PILOTAGE_GENERAL = OPER (nom="DONNEES_PILOTAGE_GENERAL", op=0, sd_prod=DonneesPilotageGeneral, niveau = 'DonneesPilotage',
  fr  = "Donnees generales de pilotage du reacteur ",
  ang = "General Reactor Control Data",
  RegulationGroupe      = SIMP (typ='TXM',statut='o',defaut='R' ,fr="Nom symbolique du groupe de regulation"),
  PnomDdcLimitInsR      = SIMP (typ='R'  ,statut='o',defaut=180.,fr="Limite d'insertion R a Pnom DDC en nombre de pas extraits"),
  PnomFdcLimitInsR      = SIMP (typ='R'  ,statut='o',defaut=180.,fr="Limite d'insertion R a Pnom FDC en nombre de pas extraits"),
  PnulDdcLimitInsR      = SIMP (typ='R'  ,statut='o',defaut=195.,fr="Limite d'insertion R a Pnul DDC en nombre de pas extraits"),
  PnulFdcLimitInsR      = SIMP (typ='R'  ,statut='o',defaut=195.,fr="Limite d'insertion R a Pnul FDC en nombre de pas extraits"),
  PuissanceGroupes      = SIMP (typ='TXM',statut='o',max='**',defaut=('G1','G2','N1','N2'),fr="Liste ordonnee des noms symboliques des groupes de compensation de puissance"),
  Recouvrement          = SIMP (typ='I'  ,statut='o',max='**',defaut=(100,90,90),
                                fr="Liste ordonnee des valeurs de recouvrement des groupes de compensation de puissance, en nombre de pas d'insertion"),
  BiteDefinition        = SIMP (typ='R'  ,statut='o',defaut=-2.5, 
                                fr="Efficacite differentielle minimale de la regulation donnant la definition du bite, en pcm/pas"),
  BiteFDCPosition       = SIMP (typ='I'  ,statut='o',defaut=225.,	fr="Position imposee du bite en FDC, en nombre de pas extraits"),
  BiteLimiteBasse       = SIMP (typ='I'  ,statut='o',defaut=207.,	fr="Position limite basse du bite, en nombre de pas extraits"),
  GrappeExtraite        = SIMP (typ='R'  ,statut='o',defaut=225.,	fr="Position Grappe extraite en nombre de pas extraits"),
  GrappeInseree         = SIMP (typ='R'  ,statut='o',defaut=5.,		fr="Position Grappe inseree en nombre de pas extraits"),
  PositionR1ereDiverg   = SIMP (typ='R'  ,statut='o',defaut=170.,	fr="Position du groupe de Regulation R a la 1ere divergence"),
  BandeManoeuvre        = SIMP (typ='R'  ,statut='o',defaut=24.,	fr="Largeur de la bande de manoeuvre du groupe de Regulation R"),
  ConfigModeA           = SIMP (typ='TXM',statut='o',defaut=('D','CD','BCD','ABCD'),max='**', fr="Configuration des groupes en mode A"),
  ConfigModeG           = SIMP (typ='TXM',statut='o',defaut=('G1','G1G2','G1G2N1','G1G2N1N2','R','RG1','RG1G2','RG1G2N1','RG1G2N1N2'),
                                max='**', fr="Configuration des groupes en mode G"),
  LimiteDomaineFct      = SIMP (typ='I',statut='o',defaut=0.05,fr="Limite du domaine de fonctionnement"),
  NbPtsSpin             = SIMP (typ='I',statut='o',defaut=31,fr="Nombre de points SPIN"),
  SeuilDnbrs            = FACT (statut='o',fr="Seuil DNBRS",
                                PtsSpin = SIMP (typ='I',max='**',statut='o',fr="Liste des points Spin"),
                                Seuils  = SIMP (typ='R',max='**',statut='o',fr="Liste des seuils DNBRS")),
  CritereDNBRL          = SIMP (typ='R',statut='o',                 fr="Critere sur le REC"),
  AlarmeBasDnbr         = SIMP (typ='R',statut='o',defaut=2.03,	    fr="Alarme Bas DNBR"),
  CsteCalibrage         = SIMP (typ='R',statut='o',defaut=-0.492,   fr="Constante A de calibrage des grappes SPIN"),
  DebitCalibrage        = SIMP (typ='R',statut='o',defaut=99507.,   fr="Debit QCAL de calibrage de la puissance SPIN, m3/h"),
  ConfigEpsilon         = SIMP (typ='TXM',statut='o',defaut=('TBH','R','RG1','RG1G2','RG1G2N1','G1G2N1','G1G2','G1'),
                                max='**', fr="Configurations pour le calcul des epsilon(z)"),
  IrradEpsilon          = SIMP (typ='R',statut='o',defaut=(150.,20000.),max='**',fr="Irradiations MWj/t du calcul des epsilon(z)")
  ) ;  # Fin DONNEES_PILOTAGE_GENERAL
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DONNEES_AJUSTEMENT : Classe de definition des donnees d'ajustement des parametres de calcul
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DONNEES_AJUSTEMENT = OPER (nom="DONNEES_AJUSTEMENT", op=0, sd_prod=DonneesAjustement, niveau = 'DonneesEtude',
  fr  = "Donnees generales d'ajustement",
  ang = "Adjustment Data",
  PnomReactivite = SIMP (typ='R',statut='o',defaut=0.,fr="Facteur additif correctif de la reactivite du coeur a Pnom, en pcm"),
  PnulReactivite = SIMP (typ='R',statut='o',defaut=0.,fr="Facteur additif correctif de la reactivite du coeur a Pnul, en pcm"),
  SectionsBore   = SIMP (typ='R',statut='o',defaut=1.,fr="Facteur multiplicatif correctif des sections du bore soluble du moderateur"),
  AlphaIsotherme = SIMP (typ='R',statut='o',defaut=3.,fr="Facteur additif correctif du coefficient de temperature isotherme en pcm/C"),
  Grappes        = NUPL (max = '**', statut = 'f',
                         fr = "Liste des ajustements associes aux types de grappes de controle",
                         elements = (SIMP (typ='TXM',statut='o',fr="Type de grappe 0P 24B 8B 12B etc."),
                                     SIMP (typ='R'  ,statut='o',max='**',
                                           fr="Coefficients multiplicatifs des sections d'absorption pour tous les groupes d'energie"))),
  Configurations = NUPL (max = '**', statut = 'f',
                         fr = "Liste des ajustements associes aux configurations de groupes de grappes de controle",
                         elements = (SIMP (typ='TXM',statut='o',fr="Nom de la configuration"),
                                     SIMP (typ='R'  ,statut='o',max='**',
                                           fr="Coefficient multiplicatif de l'efficacites de la configuration"))),
  Samarium       = NUPL (max = '**', statut = 'f',
                         fr = "Liste des couples (Irradiation, Correction Reactivite due au samarium)",
                         elements = (SIMP (typ='R',statut='o',fr="Taux d'irradiation en MWj/t"),
                                     SIMP (typ='R',statut='o',fr="Correction de reactivite en pcm au taux d'irradiation precedent")))
 ) ;  # Fin DONNEES_AJUSTEMENT
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ACCIDENT_DILUTION : Classe de definition des donnees du calcul d'accident de dilution
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ACCIDENT_DILUTION = OPER (nom="ACCIDENT_DILUTION", op=0, sd_prod=AccidentDilution, niveau = 'DonneesDesAccidents',
  fr  = "Donnees de la simulation de l'accident de dilution",
  ang = "Data for dilution accident simulation",
  ConfigArretChaud            = SIMP (typ='TXM',statut='o',defaut=('R','G1','G2','N1','N2'),max='**',
                                      fr="Liste des groupes de grappes de la configuration a l'arret a chaud"),
  ConfigArretFroid            = SIMP (typ='TXM',statut='o',defaut=('G1','G2','N1','N2'),max='**',
                                      fr="Liste des groupes de grappes de la configuration a l'arret a froid"),
  ConfigFroidDepassement      = SIMP (typ='TXM',statut='o',defaut=('G1','N1','N2'),max='**',
                                      fr="Liste des groupes de la configuration a l'arret a froid en cas de depassement du delai"),
  ConfigChaudDepassement      = SIMP (typ='TXM',statut='o',defaut=('R','G1','N1','N2'),max='**',
                                      fr="Liste des groupes de la configuration a l'arret a chaud en cas de depassement du delai"),
  IrradDepassement            = SIMP (typ='TXM',statut='o',max='**',    fr="Liste des irradiations de calcul en cas de depassement du delai"),
  SousCriticiteArret          = SIMP (typ='R',statut='o', defaut=1000., fr="Sous-criticite a l'arret en pcm"),
  CbDilutionCorrection        = SIMP (typ='R',statut='o', defaut=100. , fr="Correction du titre en bore de dilution, en ppm"),
  EfficaciteGrappesCorrection = SIMP (typ='R',statut='o', defaut=10.  , fr="Correction de l'efficacite des grappes en %"),
  DefautPuissanceCorrection   = SIMP (typ='R',statut='o', defaut=10.  , fr="Correction du defaut de puissance en %"),
  DecalageGroupes             = SIMP (typ='R',statut='o', defaut=10.  , fr="Decalage des groupes, en nombre de pas extraits"),
  PerteEfficacite             = SIMP (typ='R',statut='o', defaut=1.   , fr="Perte d'efficacite par pas des groupes, en pcm/pas"),
  PmaxChaud                   = SIMP (typ='R',statut='o', defaut=35.  , fr="Puissance relative maximum en dilution a chaud, en %"),
  DebitChaud                  = SIMP (typ='R',statut='o', defaut=31.  , fr="Debit de dilution a chaud en m3/h"),
  DebitFroid                  = SIMP (typ='R',statut='o', defaut=31.  , fr="Debit de dilution a froid en m3/h"),
  DebitDilution               = SIMP (typ='R',statut='o', defaut=60.  , fr="Debit de dilution en puissance en m3/h"),
  RoEauRCV                    = SIMP (typ='R',statut='o', defaut=1.   , fr="Masse volumique de l'eau du ballon RCV en g/cm3"),
  CRNFroid                    = SIMP (typ='R',statut='o', defaut=250. , fr="Effet des CRN en dilution a froid en pcm"),
  TiltFroidMn                 = SIMP (typ='R',statut='o', defaut=-2.  , fr="Provision sur le delai operateur due au tilt radial en accident a froid, en mn"),
  TiltChaudMn                 = SIMP (typ='R',statut='o', defaut=-2.  , fr="Provision sur le delai operateur due au tilt radial en accident a chaud, en mn"),
  TiltFroidPpm                = SIMP (typ='R',statut='o', defaut=5.,
                                      fr="Majoration de la teneur en bore a la criticite due au tilt radial en accident a froid, en ppm"),
  TiltChaudPpm                = SIMP (typ='R',statut='o', defaut=22.,
                                      fr="Majoration de la teneur en bore a la criticite due au tilt radial en accident a chaud, en ppm"),
  TiltPnDdc                   = SIMP (typ='R',statut='o', defaut=53., fr="Provision due au tilt radial en accident a Pn DDDC, en pcm"),
  DelaiOperateur              = SIMP (typ='R',statut='o', defaut=15., fr="Delai d'intervention en accident a froid ou a chaud en mn"),
  DelaiRechargement           = SIMP (typ='R',statut='o', defaut=20., fr="Delai d'intervention en accident au rechargement en mn")
 ) ;  # Fin ACCIDENT_DILUTION
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ACCIDENT_DILUTION_RESULTAT : Classe de definition des resultats du calcul d'accident de dilution
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ACCIDENT_DILUTION_RESULTAT = OPER (nom="ACCIDENT_DILUTION_RESULTAT", op=0, sd_prod=AccidentDilutionResultat, niveau = 'ResultatsAccidents',
  fr  = "Resultats de la simulation de l'accident de dilution",
  ang = "Results from dilution accident simulation",
  EtatArret               = SIMP (typ='TXM',statut='o', fr="Etat d'arret",into=('Chaud','Froid','Rechargement')),
  BlocRechargement        = BLOC (condition = "EtatArret=='Rechargement'",
        Keff              = SIMP (typ='R'  ,statut='o', fr="Keff au rechargement"),
        Ebore             = SIMP (typ='R'  ,statut='o', fr="Efficacite du bore au rechargement pcm/ppm")),
  BlocArret               = BLOC (condition = "EtatArret!='Rechargement'",
        Configuration     = SIMP (typ='TXM',statut='o', fr="Configuration a l'arret"),
        Irradiation       = SIMP (typ='R'  ,statut='o', fr="Irradiation de calcul MWj/t"),
        CbArret           = SIMP (typ='R'  ,statut='o', fr="Titre en bore a l'arret en ppm"),
        Eb                = SIMP (typ='R'  ,statut='o', fr="Efficacite du bore a l'arret en pcm/ppm"),
        CbArretUrgence    = SIMP (typ='R'  ,statut='o', fr="Titre en bore a l'arret d'urgence en ppm"),
        CbCriticite       = SIMP (typ='R'  ,statut='o', fr="Titre en bore a l'instant de criticite en ppm"),
        EfficaciteAU      = SIMP (typ='R'  ,statut='o', fr="Efficacite de l'arret d'urgence en pcm"),
        DelaiIntervention = SIMP (typ='R'  ,statut='o', fr="Delai d'intervention en mn"),
        InstantCriticite  = SIMP (typ='R'  ,statut='f', fr="Instant de criticite en mn"),
        IrradiationMin    = SIMP (typ='R'  ,statut='f', fr="Irradiation minimum MWj/t ou le delai d'intervention est suffisant"))
 ) ;  # Fin ACCIDENT_DILUTION_RESULTAT
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ACCIDENT_RTV : Classe de definition des donnees du calcul d'accident de RTV
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ACCIDENT_RTV = OPER (nom="ACCIDENT_RTV", op=0, sd_prod=AccidentRTV, niveau = 'DonneesDesAccidents',
  fr  = "Donnees de la simulation de l'accident de RTV",
  ang = "Data for Steam Line Break accident simulation",
  CodeCalcul            = SIMP (typ='TXM' ,statut='o', defaut='COBRA',into=('COBRA','THYC','FLICA'),fr="Debit primaire en m3/h"),
  DebitPrimaire         = SIMP (typ='R'   ,statut='o', defaut=70500.     ,fr="Debit primaire en m3/h"),
  DebitContournement    = SIMP (typ='R'   ,statut='o', defaut=4.5        ,fr="Debit de contournement en % du debit primaire"),
  PressionPrimaire      = SIMP (typ='R'   ,statut='o', defaut=57.5       ,fr="Pression primaire en bars"),
  TmMoyenne             = SIMP (typ='R'   ,statut='o', defaut=239.8      ,fr="Temperature moyenne moderateur en Celsius"),
  TmPnul                = SIMP (typ='R'   ,statut='o', defaut=286.       ,fr="Temperature moderateur a Pnul en Celsius"),
  TmPnom                = SIMP (typ='R'   ,statut='o', defaut=287.8      ,fr="Temperature moderateur a Pnom en Celsius"),
  BorePpm               = SIMP (typ='R'   ,statut='o', defaut=21.9       ,fr="Titre en bore du moderateur en ppm"),
  NiveauPuissance       = SIMP (typ='R'   ,statut='o', defaut=14.1       ,fr="Puissance relative en %"),
  GrappeCoincee         = SIMP (typ='TXM' ,statut='o', defaut='F14'      ,fr="Repere de la grappe coincee lors de l'accident"),
  GrappesCorrespondance = SIMP (typ='TXM' ,statut='o', max='**'          ,fr="Correspondance entre grappes coincees lors de l'accident"),
  AnglesBouclesFroides  = SIMP (typ='R'   ,statut='o', defaut=(0., 120., 240.),max=4,fr="Positions angulaires des boucles froides"),
  TmBoucles             = SIMP (typ='R'   ,statut='o', defaut=(216.8,250.8,250.8),max=4,fr="Temperatures des boucles"),
  TmCanaux              = SIMP (typ='R'   ,statut='o', max='**',fr="Temperatures moyennes d'entree des canaux COBRA"),
  TmAssemblages         = SIMP (typ='R'   ,statut='o', max='**',fr="Temperatures moyennes a l'entree des assemblages du coeur"),
  OrientationBoucles    = NUPL (max='**'  ,statut='o',fr="Orientation des boucles suivant la grappe coincee",
               elements = (SIMP (typ='TXM',statut='o', fr="Repere de la grappe"),
                           SIMP (typ='R'  ,statut='o', fr="Orientation des boucles suivant la grappe coincee, en degres")))
 ) ;  # Fin ACCIDENT_RTV
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ACCIDENT_CHUTE_GRAPPE : Classe de definition des donnees du calcul d'accident de chute de grappe(s)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ACCIDENT_CHUTE_GRAPPE = OPER (nom="ACCIDENT_CHUTE_GRAPPE", op=0, sd_prod=AccidentChuteGrappe, niveau = 'DonneesDesAccidents',
  fr  = "Donnees de la simulation de l'accident de chute de grappes",
  ang = "Data for rod insertion accident simulation",
  RecMinimum         = SIMP (typ='R',statut='o',defaut=1.225,fr="REC minimum"),
  RoPenalite         = SIMP (typ='R',statut='f',defaut=10.,fr="Penalite en % a appliquer aux variations de reactivite"),
  RoPenaliteSupp     = NUPL (statut='f',fr="Penalite supplementaire suivant la grappe chutee",elements = (
                             SIMP (typ='TXM',statut='o',fr="Repere de la grappe"),
                             SIMP (typ='R'  ,statut='o',fr="Penalite supplementaire en %"))),
  DroiteDetection    = SIMP (typ='R',statut='o',min=4,max=4,defaut=(0.92, 50., 1.11, 250.),
                             fr="Droite de detection de la chute de grappe dans le plan (Tilt,DeltaRo)(2 points a definir tilt1,deltaro1 et tilt2,deltaro2)"),
  CoeffDesalignement = SIMP (typ='R',statut='o',min=8,max=8,defaut=(1.010,1.040,1.040,1.040,1.110,1.040,1.110,1.000),
                             fr="Coefficients de desalignements K1 KP1 K2 KP2 K3 K4 K5 E"),
  DeltaDnbrThermo    = SIMP (typ='R',statut='o',min=2,max=2,defaut=(5.7, 0.),
                             fr="Variation du REC due aux effets thermohydrauliques, pour les chutes d'1 grappe et de 2 grappes"),
  DeltaDnbrMax       = SIMP (typ='R',statut='o',min=2,max=2,defaut=(39., 74.),
                             fr="Variation maximum du REC, pour les chutes d'1 grappe et de 2 grappes"),
  RecEnveloppe       = SIMP (typ='R',statut='o',defaut=(1., 2., 1.5), min=3, max=3,
                             fr="Definition du domaine REC pour la determination de l'enveloppe de la flyspeck : RecMin RecMax Pente"),
  FxyIncertitude     = SIMP (typ='R',statut='o',defaut=(0.,1.03,150.,1.03,2000.,1.061), max='**',
                             fr="Incertitude sur Fxy en fonction de l'irradiation (Couples (MWj/t, Facteur))")
 ) ;  # Fin ACCIDENT_CHUTE_GRAPPE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ACCIDENT_CHUTE_GRAPPE_RESULTAT : Classe de definition des resultats du calcul d'accident de chute de grappe(s)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ACCIDENT_CHUTE_GRAPPE_RESULTAT = OPER (nom="ACCIDENT_CHUTE_GRAPPE_RESULTAT", op=0, sd_prod=AccidentChuteGrappeResultat, niveau='ResultatsAccidents',
  fr  = "Resultats de la simulation de l'accident de chute de grappes",
  ang = "Rod insertion accident simulation Results",
  Irradiation       = SIMP (typ='R'  ,statut='o', fr="Irradiation de calcul MWj/t"),
  Chute             = FACT (max='**' ,statut='f', fr="Resultats de la chute d'1 ou 2 grappes",
    Grappes         = SIMP (typ='TXM', statut='o', max=2, fr="Reperes des grappes chutees"),
    DeltaRo         = SIMP (typ='R',statut='o', fr="Antireactivite introduite par la chute des grappes, en pcm"),
    DeltaRoPen      = SIMP (typ='R',statut='o', fr="Antireactivite penalisee introduite par la chute des grappes, en pcm"),
    Keff            = SIMP (typ='R',statut='o', fr="Keff apres chute des grappes"),
    KeffPen         = SIMP (typ='R',statut='o', fr="Keff penalise apres la chute des grappes"),
    DeltaFxy        = SIMP (typ='R',statut='o', fr="Rapport Fxy/FxyTBH"),
    Tilt2emeMinimum = SIMP (typ='R',statut='o', fr="Valeur du 2eme tilt minimum")),
  ChuteMax          = FACT (statut='f',fr="Valeurs maximales atteintes pour les chutes d'1 ou 2 grappes",
    FDH             = SIMP (typ='R'  ,statut='o', fr="Facteur d'elevation d'enthalpie"),
    DeltaRo         = SIMP (typ='R'  ,statut='o', fr="Antireactivite introduite par la chute des grappes, en pcm"),
    DeltaRoPen      = SIMP (typ='R'  ,statut='o', fr="Antireactivite penalisee introduite par la chute des grappes, en pcm"),
    Keff            = SIMP (typ='R'  ,statut='o', fr="Keff apres chute des grappes"),
    KeffPen         = SIMP (typ='R'  ,statut='o', fr="Keff penalise apres la chute des grappes"),
    DeltaFxy        = SIMP (typ='R'  ,statut='o', fr="Rapport Fxy/FxyTBH"),
    PositionDeltaRo = SIMP (typ='TXM',statut='o', max=2,fr="Grappes associees a l'antireactivite max"),
    PositionFxy     = SIMP (typ='TXM',statut='o', max=2,fr="Grappes associees au Fxy/FxyTBH max"))
 ) ;  # Fin ACCIDENT_CHUTE_GRAPPE_RESULTAT
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ACCIDENT_EJECTION : Classe de definition des donnees du calcul d'accident d'ejection d'une grappe
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ACCIDENT_EJECTION = OPER (nom="ACCIDENT_EJECTION", op=0, sd_prod=AccidentEjection, niveau = 'DonneesDesAccidents',
  fr  = "Donnees de la simulation de l'accident d'ejection d'une grappe",
  ang = "Data for rod ejection accident simulation",
  Recouvrement     = SIMP (typ='R', statut='o', defaut=100., fr="Recouvrement en ejection Mode A, en nombre de pas"),
  DeltaRoPenalite  = SIMP (typ='R', statut='o', defaut=1.10, fr="Facteur multiplicatif general des efficacites des grappes ejectees"),
  FqPenalite       = SIMP (typ='R', statut='o', defaut=1.12, fr="Facteur multiplicatif general des Fq"),
  DeltaRoPenGrappe = FACT (statut='f', fr="Corrections specifiques aux grappes ejectees : Couples RepereGrappe,PenaliteDeltaro",
        Grappes    = SIMP (typ='TXM', statut='f', max='**', fr="Liste des grappes ejectees"),
        Penalites  = SIMP (typ='R'  , statut='f', max='**', fr="Corrections des DeltaRo specifiques aux grappes ejectees")),
  FqPenGrappe      = FACT (statut='f', fr="Corrections specifiques aux grappes ejectees : Couples RepereGrappe,PenaliteFq",
        Grappes    = SIMP (typ='TXM', statut='f', max='**', fr="Liste des grappes ejectees"),
        Penalites  = SIMP (typ='R'  , statut='f', max='**', fr="Corrections des Fq specifiques aux grappes ejectees"))
 ) ;  # Fin ACCIDENT_EJECTION
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ACCIDENT_EJECTION_RESULTAT : Classe de definition des donnees du calcul d'accident d'ejection d'une grappe
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ACCIDENT_EJECTION_RESULTAT = OPER (nom="ACCIDENT_EJECTION_RESULTAT", op=0, sd_prod=AccidentEjectionResultat, niveau = 'ResultatsAccidents',
  fr  = "Resultats de la simulation de l'accident d'ejection d'une grappe",
  ang = "Rod ejection accident simulation Results",
  Ejection	= FACT (statut='o', max='**', fr="Resultats du calcul d'ejection d'une grappe",
        Irradiation	= SIMP (typ='R'  , statut='o', fr="Irradiation MWj/t du calcul d'ejection"),
        Puissance	= SIMP (typ='R'  , statut='o', fr="Niveau de du calcul d'ejection"),
        Configuration	= SIMP (typ='TXM', statut='o', max='**',fr="Configuration d'ejection (liste des groupes inseres)"),
        Grappe		= SIMP (typ='TXM', statut='o', fr="Repere de la grappe ejectee"),
        Fxy		= SIMP (typ='R'  , statut='o', fr="Fxy dans la configuration d'ejection"),
        Efficacite	= SIMP (typ='R'  , statut='o', fr="Efficacite de la grappe ejectee"),
        Dollar		= SIMP (typ='R'  , statut='o', fr="Rapport DeltaRoEjectee/BetaTot"),
        Fq		= SIMP (typ='R'  , statut='o', fr="Facteur de point chaud Fq"))
 ) ;  # Fin ACCIDENT_EJECTION_RESULTAT
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CRITERES_SURETE : Classe de definition des criteres de surete et des valeurs limites des parametres cles des accidents
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CRITERES_SURETE = OPER (nom="CRITERES_SURETE", op=0, sd_prod=CriteresSurete, niveau = 'DonneesDesAccidents',
  fr  = "Criteres et valeurs limites des parametres cles de surete",
  ang = "Safety Criteria and Accident Key Parameter Values",
  FDHConception = SIMP (typ='R',statut='o',defaut=1.55 ,fr="Facteur d'elevation d'enthalpie de conception"),
  RECMinimal    = SIMP (typ='R',statut='o',defaut=1.225,fr="Valeur minimale du REC"),
  FxyLimite     = FACT (statut='o',fr="Liste des configurations de groupes et Fxy limites associes",
                  Configurations  = SIMP (typ='TXM',max='**',statut='o',fr="Liste des configurations de groupes"),
                  Fxy             = SIMP (typ='R'  ,max='**',statut='o',fr="Valeurs limites de Fxy pour toutes les configurations"))
 ) ;  # Fin CRITERES_SURETE
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DONNEES_ACCIDENTS : Agregation des donnees de tous les accidents et des criteres de surete
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DONNEES_ACCIDENTS = OPER (nom="DONNEES_ACCIDENTS", op=0, sd_prod=DonneesAccidents, niveau = 'DonneesDesAccidents',
  fr  = "Package des classes des donnees de simulation de tous les accidents",
  ang = "All Accident Simulation Data",
  regles = (AU_MOINS_UN('Dilution', 'RTV', 'ChuteGrappe','Ejection', 'CriteresSurete'),),
  Dilution       = SIMP (typ=AccidentDilution    ,statut='f', fr="Donnees de l'accident de dilution"),
  RTV            = SIMP (typ=AccidentRTV         ,statut='f', fr="Donnees de l'accident de RTV"),
  ChuteGrappe    = SIMP (typ=AccidentChuteGrappe ,statut='f', fr="Donnees de l'accident de chute de grappe"),
  Ejection       = SIMP (typ=AccidentEjection    ,statut='f', fr="Donnees de l'accident d'ejection"),
  CriteresSurete = SIMP (typ=CriteresSurete      ,statut='f', fr="Criteres de surete")
 ) ;  # Fin DONNEES_ACCIDENTS
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ACCIDENTS_RESULTATS : Classe de definition des options generales et du type de calcul demande
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ACCIDENTS_RESULTATS = OPER (nom="ACCIDENTS_RESULTATS", op=0, sd_prod=AccidentsResultats, niveau = 'ResultatsAccidents',
  fr  = "Package des classes des resultats de simulation de tous les accidents",
  ang = "All Accident Simulation Results",
# regles = (AU_MOINS_UN('Dilution', 'RTV', 'ChuteGrappe','Ejection'),),
  Dilution     = SIMP (typ=AccidentDilutionResultat    ,statut='f', fr="Resultats de la simulation de l'accident de dilution"),
# RTV          = SIMP (typ=AccidentRTVResultat         ,statut='f', fr="Resultats de la simulation de l'accident de RTV"),
  ChuteGrappe  = SIMP (typ=AccidentChuteGrappeResultat ,statut='f', fr="Resultats de la simulation de l'accident de chute de grappe"),
  Ejection     = SIMP (typ=AccidentEjectionResultat    ,statut='f', fr="Resultats de la simulation de l'accident d'ejection")
 ) ;  # Fin ACCIDENTS_RESULTATS
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PARAMETRES_CALCUL_GESTION : Classe de definition de parametres de calcul de gestion du coeur
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PARAMETRES_CALCUL_GESTION = OPER (nom="PARAMETRES_CALCUL_GESTION", op=0, sd_prod=ParametresCalculGestion, niveau = 'ParametresCalcul',
  fr  = "Parametres divers pour le calcul de gestion du coeur",
  ang = "Core Management Calculation Parameters",
  DecalageGroupes   = SIMP (typ='R',statut='o',defaut=0.,fr="Valeur du decalage (en nombre de pas) des groupes a chaque campagne"),
  ErreurMaxLnat     = SIMP (typ='R',statut='o',defaut=5.,fr="Erreur maximale (MWj/t) du calcul de la longueur naturelle de campagne"),
  ErreurBite        = SIMP (typ='R',statut='o',defaut=5.,fr="Erreur maximale (en nombre de pas) du calcul de la position du bite en evolution"),
  LnatCbDdc         = SIMP (typ='R',statut='o',defaut=(7500., 758., 12060., 1300.), min=4, max=4,
                            fr="Loi lineaire Lnat fonction de CbDDC : 2 points a fournir (MWj/t, Cb)"),
  TiltBuMax         = SIMP (typ='R',statut='o',defaut=5.,fr="Pourcentage max de desequilibre radial admissible pour les calculs 1/4 coeur"),
  CalculMarge       = FACT (statut='o',fr="Parametres du calcul de la marge d'antireactivite",
                    MajorationDefP  = SIMP (typ='R' ,statut='o',defaut= 10.,fr="Majoration % du defaut de puissance"),
                    Redistribution  = SIMP (typ='R' ,statut='o',defaut=950.,fr="Effet de redistribution en pcm"),
                    EffetVide       = SIMP (typ='R' ,statut='o',defaut= 50.,fr="Effet de vide en pcm"),
                    MinorationEFG   = SIMP (typ='R' ,statut='o',defaut= 10.,fr="Minoration de l'efficacite des grappes en %"),
                    Regulation      = SIMP (typ='R' ,statut='o',defaut=500.,fr="Antireactivite de la regulation en pcm"),
                    UsureGrappes    = SIMP (typ='R' ,statut='o',defaut=100.,fr="Effet de l'usure des grappes en pcm"),
                    Calibrage       = SIMP (typ='R' ,statut='o',defaut=280.,fr="Incertitude de calibrage en pcm")),
  SousCriticiteDdc = SIMP (typ='R',statut='o',defaut=1000.,fr="Sous-criticite initiale en etat d'arret, en pcm"),
  SousCriticiteFdc = SIMP (typ='R',statut='o',defaut=1770.,fr="Sous-criticite minimale en etat d'arret FDC bore nul, en  pcm"),
  CritereArChaud   = SIMP (typ='R',statut='o',defaut= 690.,fr="Cb (ppm) de changement de critere sur la sous-criticite minimale en etat d'arret (Ex: 1000 a 1770 pcm)"),
  MajorCbArret	   = SIMP (typ='R',statut='o',defaut= 100.,fr="Majoration (en ppm) des titres en bore en etat d'arret")
 ) ;  # Fin PARAMETRES_CALCUL_GESTION
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RESULTATS_CALCUL_GESTION : Classe de stockage des resultats de calcul de gestion
# -----------------------------------------------------------------------------------------------------------------------------------
RESULTATS_CALCUL_GESTION = OPER (nom="RESULTATS_CALCUL_GESTION", op=0, sd_prod=ResultatsCalculGestion, niveau = 'Resultats',
  fr  = "Resultats divers des calculs de gestion du coeur",
  ang = "Core Management Calculation Results",
  Cb1ereDivergence = SIMP (typ='R',statut='f',defaut=0.,fr="Titre en bore a la premiere divergence, en ppm"),
  CTMNegatif = FACT (statut='f',
    Cbore = SIMP (typ='R',statut='o',fr="Titre en bore (ppm) garantissant un CTM negatif en DDC Pnul"),
    Irrad = SIMP (typ='R',statut='o',fr="Irradiation MWj/t au-dela de laquelle le CTM est negatif a Pnul"),
    Pmax  = SIMP (typ='R',statut='o',defaut=100.,fr="Niveau % de puissance limite garantissant un CTM negatif en DDC"),
    CTMP  = SIMP (typ='R',statut='o',max='**',fr="CTM pcm/C en fonction du niveau de puissance en DDC (Serie de couples Pr, CTM)"),
    Position = SIMP (typ='R',statut='o',max='**',
              fr="Chevauchement des groupes conduisant a un CTM nul suivant la puissance (Couples Pr, Chevauchement)"))
 ) ;  # Fin RESULTATS_CALCUL_GESTION
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CALIBRAGE_GROUPES : Classe de stockage des positions de calibrage des groupes gris
# -----------------------------------------------------------------------------------------------------------------------------------
CALIBRAGE_GROUPES = OPER (nom="CALIBRAGE_GROUPES", op=0, sd_prod=CalibrageGroupes, niveau = 'DonneesPilotage',
  fr  = "Positions de calibrage des groupes gris et coefficients isothermes associes",
  ang = "Grey Control Rod Cluster Positions Versus Power Level and Isothermal Coefficients",
  PasPuissance    = SIMP (typ='R', statut='o', defaut=5.,
                          fr="Pas en puissance (%) pour la donnee des positions de calibrage"),
  Calibrage       = FACT (statut='o',max='**',
     Irradiation  = SIMP (typ='R',statut='o', fr="Irradiation MWj/t"),
     Positions    = SIMP (typ='I',statut='o',max='**',fr="Positions de calibrage pour tous les niveaux de puissance")),
  AlphaIso        = FACT (statut='o',max='**',
     Irradiation  = SIMP (typ='R',statut='o', fr="Irradiation MWj/t"),
     Coefficients = SIMP (typ='R',statut='o',max='**',fr="Coefficients isothermes pour tous les niveaux de puissance pcm/C")),
  Chevauchement   = FACT (statut='o',max='**',
     Irradiation  = SIMP (typ='R',statut='o', fr="Irradiation MWj/t"),
     Pas          = SIMP (typ='I',statut='o',max='**',fr="Pas de chevauchement des groupes pour tous les niveaux de puissance")),
  PnulDDCPosition = SIMP (typ='I',statut='o',max='**',fr="Positions de groupes gris dans les conditions d'essai de demarrage")
 ) ;  # Fin CALIBRAGE_GROUPES
