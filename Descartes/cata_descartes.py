# -*- coding: utf-8 -*-
# debut entete

import Accas
from Accas import *

JdC = JDC_CATA(code="DESCARTES",
               execmodul=None
              )

import string

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
class Isotope (TObjet):pass
class BornesEnergie (TObjet):pass
class BibliothequeIsotopes (TObjet):pass
class ChaineFiliation(TObjet) :pass
class Materiau (TObjet):pass
class Point (TObjet):pass
class Vecteur (TObjet):pass
class Droite (TObjet):pass
class Segment (TObjet):pass
class ArcCercle (TObjet):pass
class Secteur (TObjet):pass
class Conique (TObjet):pass
class Triangle (TObjet):pass
class Rectangle (TObjet):pass
class Carre (TObjet):pass
class Hexagone (TObjet):pass
class Polygone (TObjet):pass
class Sphere (TObjet):pass
class BoiteRectangulaire (TObjet):pass
class BoiteGenerale (TObjet):pass
class CylindreX (TObjet):pass
class CylindreY (TObjet):pass
class CylindreZ (TObjet):pass
class Cylindre (TObjet):pass
class Cone (TObjet):pass
class PrismeHexagonal (TObjet):pass
class Tore (TObjet):pass
class Plan (TObjet):pass
class PlanX (TObjet):pass
class PlanY (TObjet):pass
class PlanZ (TObjet):pass
class Polyedre (TObjet):pass
class Quadrique (TObjet):pass
class Cellule(TObjet) :pass
class Cluster(TObjet):pass
class Orientation(TObjet):pass
class FormePositionnee (TObjet):pass
class GeometrieSurfacique(TObjet):pass
class GeometrieCombinatoire(TObjet):pass
class Reseau(TObjet):pass
class GrilleAssemblage (TObjet):pass
class PartieInferieureAssemblageCombustible (TObjet):pass
class PartieSuperieureAssemblageCombustible (TObjet):pass
class OptionsAutoprotection(TObjet):pass
class AssemblageType(TObjet):pass
class AssemblageCombustibleCharge (TObjet):pass
class ElementBarre (TObjet):pass
class ElementsGrappeCommande (TObjet):pass
class ElementsAbsorbantsFixes (TObjet):pass
class GrappeBouchonAssemblage (TObjet):pass
#class ElementsAssemblage (TObjet):pass
class SystemeUnitesMesure (TObjet):pass
class Vide (TObjet):pass
class ReflexionIsotrope (TObjet):pass
class ReflexionSpeculaire (TObjet):pass
class Albedo (TObjet):pass
class Translation (TObjet):pass
class Rotation (TObjet):pass
class ConditionLimiteSpeciale (TObjet):pass
class ConditionLimiteGenerale (TObjet):pass
class CorrespondanceReperePositionReseau (TObjet):pass
class PositionAssemblageCombustible (TObjet):pass
class PositionInstrumentationInterne (TObjet):pass
class PositionGrappesCommande (TObjet):pass
class StructuresInternesReacteur (TObjet):pass
class CaracteristiquesPalier (TObjet):pass
class SiteNucleaire (TObjet):pass
class EspaceVariations (TObjet):pass
class DonneesEvolutionIrradiation (TObjet):pass
class ConditionsFonctionnementMoyennes (TObjet):pass
#class PlanChargementCoeur (TObjet):pass
class DateClesCampagne (TObjet):pass
class OptionsCodes (TObjet):pass
class DonneesGeneralesEtude (TObjet):pass
# fin entete

# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe ISOTOPE : Classe de definition d'un isotope
#                   Caracteristiques elementaires des isotopes ou molecules et liens avec les bibliotheques de donnees nucleaires
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ISOTOPE=OPER(nom="ISOTOPE",sd_prod=Isotope,op=0,

  fr                           = "Definition d'un isotope ou d'une molecule et de ses bibliotheques",
  ang = "Isotope or Molecule definition and data libraries",
  Symbole                      = SIMP (typ='TXM',statut='o'),
  MasseAtomique                = SIMP (typ='R',statut='o',fr="Masse atomique en uma"),
  NombreDeCharge               = SIMP (typ='I',statut='o',fr="Nombre de charge atomique Z"),
  NombreDeMasse                = SIMP (typ='I',statut='o',fr="Nombre de masse atomique A"),
  Type			       = SIMP (typ='TXM',statut='f',into=('Standard','Detecteur','Structure','Poison'),fr="Type de l'isotope"),
  ConstituantsChimiques        = SIMP (typ='TXM',max='**',statut='f',fr="Symboles des constituants elementaires de la molecule"),
  NomsBibliotheque             = NUPL ( max      = '**',
      					  statut   = 'o',
      					  elements = (	SIMP (typ='TXM',fr="Identificateur Procedure Bibliotheque"),
         						SIMP (typ='TXM',fr="Identifiant de l'isotope dans la bibliotheque"))),
  NomsBibliothequeAutoprotegee = NUPL ( max      = '**',
      					  statut   = 'f',
					  elements = (	SIMP (typ='TXM',fr="Identificateur Procedure Bibliotheque"),
							SIMP (typ='TXM',fr="Identifiant Bibliotheque autoprotegee de l'isotope")))
 ); 
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe BORNES_ENERGIE : Classe de definition des limites en energie d'un maillage multigroupe
#                   
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BORNES_ENERGIE=OPER(nom="BORNES_ENERGIE",sd_prod=BornesEnergie,op=0,
    fr             	= "Definition d une discretisation de l espace energetique",
    ang             	= "Definition of an energy discretisation",
    NbMacrogroupes 	= SIMP (typ='I',statut='o',fr="Nombre de macrogroupes du maillage energetique"),
    BornesEnergetiques  = SIMP (typ='R',max='**',statut='o',fr="Bornes en energie du maillage energetique"),
 ); 
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe BIBLIOTHEQUE_ISOTOPES : Classe de definition d'une bibliotheque des donnees nucleaires d'isotopes ou de molecules 
#                                 Caracteristiques elementaires des isotopes ou molecules
#                                 et liens avec les bibliotheques de donnees nucleaires
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BIBLIOTHEQUE_ISOTOPES=OPER(nom="BIBLIOTHEQUE_ISOTOPES",sd_prod=BibliothequeIsotopes,op=0, 

  fr                        = "Definition d une bibliotheque de donnees nucleaires des isotopes",
  ang = "Definition of an isotopic nuclear data library",
  Description               = SIMP (typ='TXM',statut='f'),
  Fichiers                  = FACT (
      max      = '**',
      statut   = 'o',
      SystemeExploitation       = SIMP (typ='TXM',fr="Systeme d'exploitation"),
      NomFichier                = SIMP (typ='TXM',fr="Nom du fichier"),
      FormatFichier             = SIMP (typ='TXM',fr="Format du fichier",statut='f'),
      BornesEnergetiques        = SIMP (typ=BornesEnergie,statut='f',fr="Bornes en eV du maillage en energie"))
  );
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CHAINE_FILIATION : Classe de definition des filiations isotopiques dues aux transmutations
#                            sous irradiation neutronique. 
#                            Description textuelle sous format (APOLLO2, SUNSET ou DARWIN) ou description particuliere Descartes.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CHAINE_FILIATION = OPER (nom="CHAINE_FILIATION",op=0,sd_prod=ChaineFiliation,

  fr                	= "Definition d'une chaine de filiation isotopique sous irradiation",
  ang                	= "Definition of a depletion chain",
  NombreIsotopes    	= SIMP (typ='I',statut='o',fr="Nombre d'isotopes decrits dans la chaine"),
  ChaineAPOLLO2 	= SIMP (typ='TXM',statut='f',fr="Description de la chaine sous format APOLLO2"),
  ChaineSUNSET  	= SIMP (typ='TXM',statut='f',fr="Description de la chaine sous format SUNSET"),
  ChaineDARWIN  	= SIMP (typ='TXM',statut='f',fr="Nom du fichier contenant la description DARWIN de la chaine"),
  Isotopes          = FACT ( max      = '**', statut   = 'f',
                              Isotope = FACT ( max      = '**', statut   = 'f',
                                               IsotopePere = SIMP (typ=Isotope,fr="Nom isotope pere",statut='o'),
                                               TypeReaction = SIMP (typ='TXM',fr="Type de reaction",statut='o'),
                                               RapportBranchement =  SIMP (typ='R',fr="Rapport de branchement",defaut=1.,statut='f')
                                             )
                           )
 );
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe MATERIAU : Classe de définition d'un matériau à partir de mélange d'isotopes ou de matériaux.
#		     Définition alternative par donnée des enrichissements
#                    Caractéristiques fournies a 20 C.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
MATERIAU=OPER(nom="MATERIAU",op=0,sd_prod=Materiau,

  fr                   = "Definition d'un materiau",
  ang = "Definition of a mixture",
  TypeDefinition       = SIMP (typ='TXM',statut='f',defaut="Isotopique",into=("Isotopique","Enrichissement")),
  BlocIsotopique       = BLOC (condition = "TypeDefinition=='Isotopique'",
        Type           = SIMP (	statut = 'o',
     				typ    = 'TXM',
     			 	into   = ('Absorbant','Combustible','Melange','ModerateurInterne','ModerateurExterne','Detecteur',
               				  'Grille','Gaine','Tube','Poison','PoisonConsommable','AbsorbantIntegre',
               				  'Solide','Liquide','Gaz','MateriauVide'),
      				defaut = 'Combustible'),
        MethodeMelange = SIMP (statut='o',typ='TXM',into=('Isotopique','Massique','Concentration'),defaut='Massique'),
        Constituants   = NUPL (	statut   = 'o',
				max      = '**',
				elements = (SIMP (typ=(Isotope,Materiau)),SIMP (typ='R')),
				fr       = "Couples (Isotope ou Materiau) et (Pourcentage ou Cencentration)")
  ),
  BlocEnrichissement   = BLOC (condition = "TypeDefinition=='Enrichissement'",
        Type                 = SIMP (typ='TXM',into=('UO2','MOX','UO2Gadolinium','MOXGadolinium'),statut='o'),
        EnrichissementU235   = SIMP (typ=('R','TXM'),defaut=3.7,statut='f',fr="Enrichissement % en U235 du combustible"),
        EnrichissementPu     = SIMP (typ=('R','TXM'),defaut=0.,statut='f',fr="Enrichissement % en plutonium du combustible"),
        EnrichissementGado   = SIMP (typ=('R','TXM'),defaut=0.,statut='f',fr="Enrichissement % en Gd2O3 du combustible"),
        VecteurPu            = NUPL (	max='**',statut='f',
				elements=(	SIMP (typ=Isotope,fr="Nom isotope du plutonium"), 
						SIMP (typ='R',fr="Pourcentage isotopique"))),
        DateReference        = SIMP (typ='I',min=3,max=3,statut='f',fr="Date J M A de reference du combustible"),
        DateDivergence       = SIMP (typ='I',min=3,max=3,statut='f',fr="Date J M A de divergence du reacteur ou ce combustible est charge"),
        VieillissementJours  = SIMP (	typ    = 'R',
      				defaut = 0.,
      				statut = 'f',
      				fr     = "Nbre de jours de vieillissement du combustible, calculable si on donne DateDivergence")),
  MasseVolumique       = SIMP (statut='f',typ=('R','I','TXM'),fr="Masse volumique theorique du materiau g/cm3"),
  TauxEvidement        = SIMP (statut='f',typ=('R','I'),fr="Taux % d'evidement du materiau"),
  TauxPorosite         = SIMP (statut='f',typ=('R','I'),fr="Taux % de porosite du materiau"),
  Temperature          = SIMP (statut='f',typ=('R','I','TXM'),fr="Temperature en Celsius du materiau"),
  GazRemplissage       = SIMP (statut='f',typ=(Isotope,Materiau),defaut='HE4',fr="Gaz de remplissage des evidements du materiau solide"),
  PressionInitialeGaz  = SIMP (statut='f',typ=('R','I'),defaut=32.,fr="Pression en bars du gaz de remplissage des evidements"),
  DilatationLineaire   = SIMP (statut='f',typ=('R','I'),fr="Coefficient de dilatation thermique lineaire cm/C du materiau"),
  Chaine	       = SIMP (statut='f',typ=ChaineFiliation,defaut='ChaineSaturee',fr="Chaine de filiation isotopique associee au materiau"),
  TauxImpuretes = SIMP (statut='f',typ=('R','I'),fr="Taux % d'impuretes")
 );
# ==================================================================================================================================
#                                    Definition des Classes elementaires pour la geometrie
# ==================================================================================================================================
#  Classe POINT : Classe de definition d'un point de l'espace
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POINT = OPER (nom="POINT",op=0,sd_prod=Point,

  fr          = "Definition d'un point de l'espace",
  ang = "Definition of a point in space",
  Coordonnees = SIMP (typ='R',min=2,max=3,statut='o',fr="Coordonnees du point dans l'espace")
 );
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe VECTEUR : Classe de definition d'un vecteur dans l'espace
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
VECTEUR = OPER (nom="VECTEUR",op=0,sd_prod=Vecteur,

  fr          = "Definition d'un vecteur dans l'espace",
  ang = "Definition of a vector in space",
  regles = (UN_PARMI ('Composantes','Points')),
  Composantes = SIMP (typ='R',min=2,max=3,statut='f',fr="Composantes du vecteur en 2D ou 3D"),
  Points      = SIMP (typ=Point,min=2,max=2,statut='f',fr="Vecteur defini par deux points") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DROITE : Classe de definition d'une droite
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DROITE = OPER (nom="DROITE",op=0,sd_prod=Droite,

  fr       = "Definition d'une droite par 2 POINTs, 1 POINT et 1 VECTEUR, ou Equation ax + by + cz + d = 0",
  ang = "Definition of a straight line with 2 POINTs or with Equation ax + by + cz + d = 0",
  regles = (UN_PARMI ('Points','Equation','VecteurOrigine')),
  Points   = SIMP (typ=Point,min=2,max=2,statut='f',fr="Deux points de definition de la droite"),
  Equation = SIMP (typ='R',min=2,max=4,statut='f',fr="Coefficients successifs abcd de l'equation d'une droite"),
  VecteurOrigine = FACT (statut='f',
  Vecteur  = SIMP (typ=Vecteur,statut='f',fr="Donnee du vecteur directeur de la droite"),
  Origine  = SIMP (typ=Point,statut='f',fr="Donnee d'un point de passage de la droite"))) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe SEGMENT : Classe de definition d'un segment (Idem DROITE + Longueur et Origine)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SEGMENT = OPER (nom="SEGMENT",op=0,sd_prod=Segment,

  fr       = "Definition d'un segment 2 Points ou Origine + ((Longueur + Equation ax + by + d = 0) ou vecteur)",
  ang = "Definition of a segment ax + by + cz + d = 0",
  regles = (UN_PARMI ('Points','Equation','Vecteur')),
  Points   = SIMP (typ=Point,min=2,max=2,statut='f',fr="Deux points de definition du segment"),
  Equation = SIMP (typ='R',min=2,max=4,statut='f',fr="Coefficients successifs abcd de l'equation de la droite "),
  Vecteur  = SIMP (typ=Vecteur,statut='f',fr="Donnee du vecteur directeur du segment"),
  Longueur = SIMP (typ='R',statut='f',fr="Longueur du segment"),
  Origine  = SIMP (typ=Point,statut='f',fr="Donnee de l'origine du segment") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ARC_CERCLE : Classe de definition d'un arc de cercle
#                      Angles donnes en degres 
#                       Dans le cas 2D on peut positionner l'arc de cercle en donnant l'angle du debut de l'arc par rapport a l'axe Ox
#                       Dans le cas 3D on donne en plus la hauteur et l'axe directeur de l'arc
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ARC_CERCLE = OPER (nom="ARC_CERCLE",op=0,sd_prod=ArcCercle,

  fr         = "Definition d'un arc de cercle",
  ang = "Definition of a circular arc",
  Type       = SIMP (typ='TXM',statut='f',defaut='2D',into=('2D','3D'),fr="Type d'arc 2D ou 3D"),
  Rayon      = SIMP (typ='R',statut='o',fr="Rayon de l'arc de cercle"),
  Angles     = SIMP (typ='R',max=2,defaut=(360.,0.),statut='f',fr="Angles en degres de l'arc : Total et Debut"),
  VecteurAxe = SIMP (typ=Vecteur,statut='f',fr="Vecteur directeur de l'axe de l'arc") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe SECTEUR :     Classe de definition d'un disque ou d'un secteur d'une couronne circulaire
#                       Angle du secteur donne en degres (360° par defaut)
#                       Dans le cas 2D on peut positionner le secteur en donnant l'angle du debut de secteur par rapport a l'axe Ox
#                       Dans le cas 3D on donne en plus la hauteur et l'axe directeur du secteur
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SECTEUR = OPER (nom="SECTEUR",op=0,sd_prod=Secteur,

  fr         = "Definition d'un disque ou d'un secteur d'une couronne",
  ang = "Definition of a circular sector",
  Type       = SIMP (typ='TXM',statut='o',into=('2D','3D'),fr="Type de secteur 2D ou 3D"),
  Rayons     = SIMP (typ='R',min=2,max=2,statut='o',fr="Rayons interne et externe de la couronne"),
  Angles     = SIMP (typ='R',max=2,defaut=(360.,0.),statut='f',fr="Angles en degres du secteur"),
  Hauteur    = SIMP (typ='R',defaut=0.,statut='f',fr="Hauteur du secteur"),
  VecteurAxe = SIMP (typ=Vecteur,defaut=0.,statut='f',fr="Vecteur directeur de l'axe du secteur") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONIQUE : Classe de definition d'une conique 2D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONIQUE = OPER (nom="CONIQUE",op=0,sd_prod=Conique,

  fr             = "Definition d'une conique 2D ax2+by2+cxy+dx+ey+f=0",
  ang = "Definition of a quadratic curve 2D",
  Equation       = SIMP (typ='R',min=2,max=6,statut='o',fr="Coefficients successifs abcdef de l'equation d'une conique"),
  OrigineVecteur = NUPL (
      elements = (SIMP (typ=Point),SIMP (typ=Vecteur)),
      statut   = 'f',
      fr       = "Donnee de l'origine et du vecteur directeur") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe TRIANGLE : Classe de definition d'un triangle
#                      Angles donnes en degres par rapport a l'axe Ox horizontal
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TRIANGLE = OPER (nom="TRIANGLE",op=0,sd_prod=Triangle,

  fr     = "Definition d'un triangle",
  ang = "Definition of a triangle",
  regles = (UN_PARMI ('Points','AngleCotes')),
  Points = SIMP (typ=Point,min=3,max=3,statut='f'),
  AngleCotes = SIMP (typ='R',min=3,max=3,statut='f',fr="Donnee d'un Angle en degres et Longueurs de deux cotes")
 );
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe RECTANGLE : Classe de definition d'un rectangle
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RECTANGLE = OPER (nom="RECTANGLE",op=0,sd_prod=Rectangle,

  fr     = "Definition d'un rectangle",
  ang = "Definition of a rectangle",
  regles = (UN_PARMI ('Points','Cotes')),
  Points = SIMP (typ=Point,min=3,max=3,statut='f',fr="Definition du rectangle par trois points"),
  Cotes  = SIMP (typ='R',min=2,max=2,statut='f',fr="Donnee de la longueur de deux cotes") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CARRE : Classe de definition d'un carre
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CARRE = OPER (nom="CARRE",op=0,sd_prod=Carre,

  fr     = "Definition d'un carre",
  ang = "Definition of a square",
  regles = (UN_PARMI ('Points','Cote')),
  Points = SIMP (typ=Point,min=2,max=2,statut='f',fr="Definition du carre par deux points"),
  Cote   = SIMP (typ='R',statut='f',fr="Donnee de la longueur du cote du carre")
 );
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe HEXAGONE : Classe de definition d'un hexagone
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
HEXAGONE = OPER (nom="HEXAGONE",op=0,sd_prod=Hexagone,

  fr    = "Definition d'un hexagone",
  ang = "Definition of an hexagon",
  Rayon = SIMP (typ='R',statut='f',fr="Rayon du cercle inscrit dans l'hexagone")
 );
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POLYGONE : Classe de definition d'un polygone
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POLYGONE = OPER (nom="POLYGONE",op=0,sd_prod=Polygone,

  fr     = "Definition d'un polygone",
  ang = "Definition of a polygon",
  Points = SIMP (typ=Point,max='**',statut='f',fr="Definition d'un polygone par tous ses points")
 );
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
SPHERE = OPER (nom="SPHERE",op=0,sd_prod=Sphere,

  fr              = "Definition d'une forme spherique",
  ang = "Definition of a spherical form",
  Rayon           = SIMP (typ='R',statut='o',fr="Rayon de la sphere"),
  Secteur         = SIMP (typ='R',statut='f',fr="Angle du secteur de la sphere"),
  TranchesAxiales = NUPL (
      max      = '**',
      statut   = 'f',
      fr       = "Limites des tranches axiales de la sphere sectorisee",
      elements = (SIMP (typ='R',fr="Cote depart de la tranche"),SIMP (typ='R',fr="Cote finale de la tranche"))) ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe BOITE_RECTANGULAIRE : Classe de definition d'une forme parallelepipedique de cotes paralleles aux axes de reference
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BOITE_RECTANGULAIRE = OPER (nom="BOITE_RECTANGULAIRE",op=0,sd_prod=BoiteRectangulaire,

  fr    = "Definition d'une d'une forme parallelepipedique rectangulaire",
  ang = "Definition of a rectangular box form",
  Cotes = SIMP (typ='R',min=3,max=3,statut='o',fr="Longueurs des Cotes de la boite rectangulaire") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe BOITE_GENERALE : Classe de definition d'une forme parallelepipedique quelconque
#        Le plan de base de la boite doit etre le plan xOy. On donne donc uniquement les 2 vecteurs **normaux**
#        aux 2 autres plans, et les 3 longueurs des arretes principales.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BOITE_GENERALE = OPER (nom="BOITE_GENERALE",op=0,sd_prod=BoiteGenerale,

  fr                 = "Definition d'une forme parallelepipedique quelconque",
  ang = "Definition of a general box form",
  VecteursDirecteurs = SIMP (typ=Vecteur,min=2,max=2,statut='o',fr="Vecteurs normaux aux faces non horizontales de la boite"),
  Cotes              = SIMP (typ='R',min=3,max=3,statut='o',fr="Longueurs des Cotes de la boite") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CYLINDRE_X : Classe de definition d'une forme cylindrique d'axe parallele a Ox
#         Pour tous les cylindres, la donnee de deux rayons transforme le cylindre circulaire en cylindre elliptique
#         La donnee d'un angle limite le cylindre a ce secteur
#         Pour un secteur d'un cylindre elliptique, il est necessaire de donner en plus l'angle de depart du secteur
#         par rapport a l'axe majeur de l'ellipse
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CYLINDRE_X = OPER (nom="CYLINDRE_X",op=0,sd_prod=CylindreX,

  fr      = "Definition d'une forme cylindrique d'axe parallele a Ox",
  ang = "Definition of a right cylinder form // Ox",
  Rayons  = SIMP (typ='R',max=2,statut='o',fr="Rayons mineur et majeur du cylindre X"),
  Hauteur = SIMP (typ='R',statut='f',fr="Hauteur du cylindre X"),
  Angles  = SIMP (typ='R',max=2,statut='f',fr="Angles du secteur du cylindre X") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CYLINDRE_Y : Classe de definition d'une forme cylindrique d'axe parallele a Oy
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CYLINDRE_Y = OPER (nom="CYLINDRE_Y",op=0,sd_prod=CylindreY,

  fr      = "Definition d'une forme cylindrique d'axe parallele a Oy",
  ang = "Definition of a right cylinder form // Oy",
  Rayons  = SIMP (typ='R',max=2,statut='o',fr="Rayons mineur et majeur du cylindre Y"),
  Hauteur = SIMP (typ='R',statut='f',fr="Hauteur du cylindre Y"),
  Angles  = SIMP (typ='R',max=2,statut='f',fr="Angles du secteur du cylindre Y") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CYLINDRE_Z : Classe de definition d'une forme cylindrique d'axe parallele a Oz
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CYLINDRE_Z = OPER (nom="CYLINDRE_Z",op=0,sd_prod=CylindreZ,

  fr      = "Definition d'une forme cylindrique d'axe parallele a Oz",
  ang = "Definition of a right cylinder form // Oz",
  Rayons  = SIMP (typ='R',max=2,statut='o',fr="Rayons mineur et majeur du cylindre Z"),
  Hauteur = SIMP (typ='R',statut='f',fr="Hauteur du cylindre Z"),
  Angles  = SIMP (typ='R',max=2,statut='f',fr="Angles du secteur du cylindre Z") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CYLINDRE : Classe de definition d'une forme cylindrique quelconque
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CYLINDRE = OPER (nom="CYLINDRE",op=0,sd_prod=Cylindre,

  fr         = "Definition d'une forme cylindrique quelconque",
  ang = "Definition of a general cylinder form",
  Rayons     = SIMP (typ='R',max=2,statut='o',fr="Rayons mineur et majeur du cylindre"),
  VecteurAxe = SIMP (typ=Vecteur,statut='o',fr="Vecteur directeur de l'axe du cylindre"),
  Hauteur    = SIMP (typ='R',statut='f',fr="Hauteur du cylindre"),
  Angles     = SIMP (typ='R',max=2,statut='f',fr="Angles du secteur du cylindre") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONE : Classe de definition d'un forme conique
#           Une portion de cone peut etre definie en donnant les cotes axiales (origine de l'axe du cone au sommet du cone) de
#           la zone retenue
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONE = OPER (nom="CONE",op=0,sd_prod=Cone,

  fr              = "Definition d'une forme conique",
  ang = "Definition of a conic form",
  DemiAngleSommet = SIMP (typ='R',statut='o',fr="Demi-angle au sommet"),
  LimitesAxiales  = SIMP (typ='R',min=2,max=2,statut='f',fr="Limites axiales du cone"),
  VecteurAxe      = SIMP (typ=Vecteur,statut='o',fr="Vecteur directeur de l'axe du cone") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PRISME_HEXAGONAL : Classe de definition d'une forme de prisme hexagonal 3D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PRISME_HEXAGONAL = OPER (nom="PRISME_HEXAGONAL",op=0,sd_prod=PrismeHexagonal,

  fr         = "Definition d'une forme de prisme hexagonal 3D",
  ang = "Definition of a 3D hexagonal form",
  Rayon      = SIMP (typ='R',statut='o',fr="Rayon du cercle circonscrit (=cote de l'hexagone)"),
  Hauteur    = SIMP (typ='R',statut='f',fr="Hauteur de l'hexagone"),
  VecteurAxe = SIMP (typ=Vecteur,statut='o',fr="Vecteur directeur de l'axe de l'hexagone") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe TORE : Classe de definition d'une forme toroidale
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TORE = OPER (nom="TORE",op=0,sd_prod=Tore,

  fr     = "Definition d'une forme toroidale",
  ang = "Definition of a toroidal form",
  Rayons = SIMP (typ='R',min=2,max=2,statut='o',fr="Rayons du tore : 1/2 distance a l'axe et rayon de la section du tore") ) ;
# ==================================================================================================================================
#               Definition des Classes pour une geometrie 3D : Elements geometriques surfaciques
# ==================================================================================================================================
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe PLAN : Classe de definition d'un plan
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PLAN = OPER (nom="PLAN",op=0,sd_prod=Plan,

  fr       = "Definition d'un plan ax + by + cz + d = 0",
  ang = "Definition of a plane surface ax + by + cz + d = 0",
  Points   = SIMP (typ=Point,min=3,max=3,statut='f',fr="Donnee de 3 points non alignes"),
  Equation = SIMP (typ='R',min=2,max=4,statut='f',fr="Coefficients successifs abcd de l'equation du plan")
 );
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe PLAN_X : Classe de definition d'un plan perpendiculaire a l'axe Ox
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PLAN_X = OPER (nom="PLAN_X",op=0,sd_prod=PlanX,

  fr   = "Definition d'un plan perpendiculaire a Ox",
  ang = "Definition of a plane surface perpendicular to Ox",
  Cote = SIMP (typ='R',statut='o',fr="Cote du plan // OyOz") ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe PLAN_Y : Classe de definition d'un plan perpendiculaire a l'axe Oy
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PLAN_Y = OPER (nom="PLAN_Y",op=0,sd_prod=PlanY,

  fr   = "Definition d'un plan perpendiculaire a Oy",
  ang = "Definition of a plane surface perpendicular to Oy",
  Cote = SIMP (typ='R',statut='o',fr="Cote du plan // OxOz") ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe PLAN_Z : Classe de definition d'un plan perpendiculaire a l'axe Oz
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PLAN_Z = OPER (nom="PLAN_Z",op=0,sd_prod=PlanZ,

  fr   = "Definition d'un plan perpendiculaire a Oz",
  ang = "Definition of a plane surface perpendicular to Oz",
  Cote = SIMP (typ='R',statut='o',fr="Cote du plan // OxOy") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POLYEDRE : Classe de definition d'une forme polyhedrique 3D quelconque (N faces, N > 4)
#                    Definition surfacique : Donnee des N plans et du choix du cote positif ou negatif
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POLYEDRE = OPER (nom="POLYEDRE",op=0,sd_prod=Polyedre,

  fr    = "Definition d'une forme polyhedrique 3D quelconque ",
  ang = "Definition of a 3D polyhedron form with N > 4 plane faces",
  Plans = NUPL (
      min      = 5,
      max      = '**',
      statut   = 'o',
      fr       = "Surfaces planes limites du polyedre",
      elements = (SIMP (typ=(Plan,PlanX,PlanY,PlanZ),fr="Plans limites du polyedre"),
                  SIMP (typ='TXM',into=('Plus','Moins'),fr="Choix du cote positif ou negatif de l'espace"))) 
                ) ;

#     elements = (SIMP (typ=(Plan,PlanX,PlanY,PlanZ),fr="Plans limites du polyedre"),
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe QUADRIQUE : Classe de definition d'une quadrique 3D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
QUADRIQUE = OPER (nom="QUADRIQUE",op=0,sd_prod=Quadrique,

  fr       = "Definition d'une quadrique 3D ax2+by2+cz2+dxy+eyz+fxz+gx+hy+iz+j=0",
  ang = "Definition of a quadratic curve 3D ax2+by2+cz2+dxy+eyz+fxz+gx+hy+iz+j=0",
  Equation = SIMP (typ='R',min=2,max=10,statut='o',fr="Coefficients successifs abcdefghij de l'equation d'une quadrique") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CELLULE : Classe de definition d'une cellule (ensemble elementaire  de regions annulaires et sectorisees)
#                   Apres la hauteur de la cellule, entree des donnees par listes successives pour l'ensemble des couronnes de la
#                   cellule, la zone externe etant decrite a part dans l'attribut FormeTechnologique :
#                   - Liste des materiaux
#                   - Liste des rayons des couronnes correspondantes
#                   - Liste des sous-couronnes : - Numero de couronne a discretiser (Numero 1 a partir du centre),
#                                                 - Nombre de sous-couronnes,
#                                                 - Mot-cle Equivolumique si decoupage en sections transverses egales,
#                                                 - Rayons des couronnes intermediaires ou proportions volumiques si mot-cle
#                                                   Proportions indique anterieurement.
#                   - Liste des sectorisations :  - Nom de couronne a sectoriser ,
#                                                 - Nombre de secteurs,
#                                                 - Mot-cle Equivolumique si decoupage en secteurs egaux et positionnement du premier
#                                                   secteur par rapport a l'axe x, et pas de changement de composition du secteur,
#                                                 - Mot-cle alternatif Angle si on veut modifier ou positionner les secteurs dans la
#                                                   couronne : on donne alors des triplets de donnees pour chaque secteur :
#                                                               - nom du materiau composant le le secteur,
#                                                               - position trigonometrique en \260 du debut du secteur
#                                                               - et angle en \260 du secteur.
#                                                 Le trace des secteurs sont definis en partant du centre de la couronne.
#                                                 Pour la sectorisation de la forme externe, deux cas se presentent :
#                                                       - soit pas de couronnes internes : les secteurs se tracent alors en partant
#                                                         du centre de la forme externe,
#                                                       - dans le cas contraire, les secteurs partent du centre des couronnes.
#                                                 Les secteurs peuvent ne pas couvrir l'ensemble de la couronne.
#                   Pour la zone peripherique, on doit definir les cotes de la cellule (cas cartesien), son materiau, sa
#                   discretisation, et le decentrage du centre des couronnes par rapport au centre de ce contour peripherique
#                   (Coordonnees x,y du centre des couronnes / au centre du contour)
#                   Pour le moment, limitation a 2D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CELLULE = OPER (nom="CELLULE",op=0,sd_prod=Cellule,

  fr             = "Definition d'une cellule elementaire d'un assemblage",
  ang = "Definition of a basic pin cell",
  Type           = SIMP (typ='TXM',defaut='Combustible',
                         into=( 'Combustible','BarreGrise','BarreNoire','BarreAcier','BarreAic','BarreB4c',
                                'Detecteur','Trou','TubeGuide','Postiche','Pyrex','ExPyrex','Gadolinium',
                                'CellType1','CellType2','CellType3'),statut='o'),
  HauteurMoyenne = SIMP (typ='R',defaut=1.,statut='o',fr="Hauteur moyenne de la cellule de base"),
  Couronnes      = FACT (
      NomsSymboliques = SIMP (typ='TXM',max='**',statut='o',fr="Liste des noms arbitraires des couronnes"),
      Materiaux       = SIMP (typ=Materiau,max='**',statut='o',fr="Liste des materiaux des couronnes"),
      Temperatures    = SIMP (typ=('R','I','TXM'),max='**',statut='o',fr="Liste des temperatures des couronnes"),
      Rayons          = SIMP (typ='R',max='**',statut='o',fr="Liste des rayons des couronnes"),
      RayonsMineurs   = SIMP (typ='R',max='**',statut='f',fr="Liste des rayons mineurs des couronnes elliptiques"),
      Hauteurs        = SIMP (typ='R',max='**',statut='f',fr="Liste des hauteurs des couronnes")),
  SousCouronnes   = FACT (
      max      = '**',
      statut   = 'f',
      NomCouronne 		= SIMP (typ='TXM',fr="Nom symbolique de la couronne"),
      NbSousCouronnes 		= SIMP (typ='I',fr="Nombre de sous-couronnes de discretisation"),
      TypeDiscretisation 	= SIMP (typ='TXM',defaut='Equivolumique',into=('Equivolumique','Proportions','Equidistant'),statut='f'),
      ProportionsVolumiques 	= SIMP (typ='R',statut='f',max='**',fr="Proportions volumiques optionnelles des sous-couronnes"),
      ProfilTemperature 	= SIMP (typ='R',max='**',statut='f',fr="Profil de temperature")), 
  Homogeneisation = FACT (
      max      = '**',
      statut   = 'f',
      NomCouronne 	= SIMP (typ='TXM',fr="Nom arbitraire de la couronne homogeneisee"),
      ListeCouronnes 	= SIMP (typ='TXM',max='**',fr="Liste des noms des couronnes jointives a homogeneiser")),
  Secteurs     = FACT (
      max      = '**',
      statut   = 'f',
      NomCouronne = SIMP (typ='TXM',statut='o',fr="Nom de la couronne ou de la forme externe a sectoriser"),
      NbSecteurs  = SIMP (typ='I',fr="Nombre de secteurs de la couronne",statut='o'),
      TypeSectorisation = SIMP (typ='TXM',defaut='Coins',into=('Equivolumique','Angle','Coins','MilieuxCotes'),statut='f'),
      Sectorisation = FACT (
              max       = '**',
              statut    = 'f',
              Materiaux = SIMP (typ=Materiau,max='**',fr="Materiau des secteurs"),
              Temperatures = SIMP (typ=('R','I','TXM'),max='**',fr="Temperature des secteurs"),
              AnglesDepart = SIMP (typ='R',max='**',fr="Angle de depart du secteur"),
              Angles       = SIMP (typ='R',max='**',fr="Angle du secteur"))),
  FormeExterne = FACT (
      NomSymbolique = SIMP (typ='TXM',statut='f'),
      Type          = SIMP (
          typ=(ArcCercle,Carre,Rectangle,Hexagone,Triangle,Polygone),
          statut = 'f',  # la donnee est facultative si la cellule est inserree dans un reseau
          fr     = "Forme geometrique exterieure"),
      Materiau      = SIMP (typ=Materiau,fr="Materiau de la forme externe"),
      Temperature   = SIMP (typ=('R','I','TXM'),fr="Temperature du materiau de la forme externe"),
      Decentrement  = SIMP (
          typ    = 'R',
          min    = 2,
          max    = 3,
          defaut = (0.,0.,0.),
          statut = 'f',
          fr     = "Coordonnees xyz du centre des couronnes / centre du contour")) ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CLUSTER : Classe de definition d'un cluster de cellules cylindriques de forme exterieure quelconque
#                   Un cluster est defini comme une superposition centree de cadrans telephoniques (a l'ancienne mode), chaque
#                   cadran ayant des trous de tailles differentes, l'ensemble etant dispose dans un contour de forme quelconque.
#                   Possibilites donnees ci-dessous : 
#                       - Positionnement des couronnes de canaux, chaque canal etant une CELLULE predefinie,
#                       - Definition du fond du cluster : 
#                               - Serie de couronnes de materiaux distincts
#                               - Forme exterieure quelconque
#                       - Sectorisation eventuelle de la zone peripherique
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CLUSTER = OPER (nom="CLUSTER",op=0,sd_prod=Cluster,
  fr               = "Definition d'un cluster de cellules cylindriques",
  ang = "Definition of a cylindrical cell cluster",
  Hauteur          = SIMP (typ='R',defaut=1.,statut='f',fr="Hauteur du cluster"),
  Couronnes        = FACT (
      Cellules = SIMP (typ=Cellule,max='**',fr="Liste des cellules sur chaque cercle"),
      Rayons   = SIMP (typ='R',max='**',fr="Liste des rayons des couronnes de cellules"),
      Angles   = SIMP (typ='R',max='**',fr="Liste des pas angulaires de positionnement des cellules cylindriques")),
  FormeGlobale     = FACT (
      NomSymbolique        = SIMP (typ='TXM'),
      RayonsInternes       = SIMP (typ='R',max='**',fr="Liste des rayons des couronnes internes",statut='f'),
      MateriauxInternes    = SIMP (typ=Materiau,max='**',fr="Materiaux Couronnes internes",statut='f'),
      TemperaturesInternes = SIMP (typ=('R','I','TXM'),max='**',fr="Temperatures des materiaux internes",statut='f'),
      FormeExterne         = SIMP (
          typ    = (ArcCercle,Carre,Rectangle,Hexagone,Triangle,Polygone),
          statut = 'o',
          fr     = "Forme geometrique exterieure"),
      MateriauExterne      = SIMP (typ=Materiau,fr="Materiau de la forme externe",statut='o'),
      TemperatureExterne   = SIMP (typ=('R','I','TXM'),max='**',fr="Temperature du materiau externe",statut='f'),
      Decentrement         = SIMP (
          typ    = 'R',
          min    = 2,
          max    = 3,
          defaut = (0.,0.,0.),
          statut = 'f',
          fr     = "Coordonnees xyz du centre des couronnes / centre du contour")),
  SecteursExternes = FACT (
      NbSecteurs   = SIMP (typ='I',fr="Nombre de secteurs de la couronne externe",statut='o'),
      TypeSecteur  = SIMP (
          typ    = 'TXM',
          defaut = 'Coins',
          into   = ('Equivolumique','Angle','Coins','MilieuxCotes'),
          statut = 'f'),
      Materiaux    = SIMP (max='**',typ=Materiau,fr="Materiau des secteurs",statut='f'),
      AngleDepart  = SIMP (max='**',typ='R',fr="Angle de depart des secteurs",statut='f'),
      AngleSecteur = SIMP (max='**',typ='R',fr="Angle des secteurs",statut='f')) ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ORIENTATION :         Classe de definition d'une orientation angulaire dans un plan 2D apres symetrie eventuelle / Ox
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ORIENTATION = OPER (nom="ORIENTATION",op=0,sd_prod=Orientation,

  fr              = "Definition d'une orientation d'un reseau ou d'une cellule",
  ang = "Definition of a cell or lattice orientation",
  Symetrie      = SIMP (typ=(Plan,PlanX,PlanY,PlanZ),statut='f',fr="Indication d'une operation de symetrie / Plan"),
  AngleRotation = SIMP (typ='R',defaut=0.,statut='f',fr="Angle de rotation en degres"),
  CentreRotation = SIMP (typ=Point,statut='f',fr='Centre de rotation'),
  AxeRotation    = SIMP (typ=Vecteur,statut='f',fr="Vecteur de l'axe de rotation") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe FORME_POSITIONNEE :   Classe de definition d'une forme geometrique positionnee
#                               La position est definie a l'aide du centre de la forme geometrique, 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
FORME_POSITIONNEE = OPER (nom="FORME_POSITIONNEE",op=0,sd_prod=FormePositionnee,

  fr             = "Definition d'une forme positionnee",
  ang = "Definition of a shape and its position",
  Forme          = SIMP (
      typ    = (Sphere,BoiteRectangulaire,BoiteGenerale,CylindreX,CylindreY,CylindreZ,Cylindre,Cone,
                PrismeHexagonal,Tore,Polyedre,Cellule,Cluster),
      statut = 'o',
      fr     = "Forme geometrique de base a positionner"),
  PositionCentre   = SIMP (typ=Point,statut='o',fr="Coordonnees du centre de la forme geometrique"),
  OrientationForme = SIMP (typ=Orientation,statut='f',fr="Orientation de la forme")
 ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe GEOMETRIE_SURFACIQUE : Classe de definition d'une geometrie surfacique
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GEOMETRIE_SURFACIQUE = OPER (nom="GEOMETRIE_SURFACIQUE",op=0,sd_prod=GeometrieSurfacique,

  fr            = "Definition d'une geometrie surfacique",
  ang = "Definition of a surfacic geometry",
  MateriauRemplissage = SIMP (typ=Materiau,statut='o',fr="Materiau de remplissage de la geometrie surfacique"),
  Surfaces      = NUPL (
      max      = '**',
      statut   = 'o',
      fr       = "Serie de couples (Surface,Plus ou Moins) definissant les surfaces limites de la geometrie",
      elements = (
          SIMP (typ='TXM'),
          SIMP (typ='TXM',into=('Plus','Moins'))))
 );

#         simp (typ=(PlanX,PlanY,PlanZ,Plan,CylindreX,CylindreY,CylindreZ,Cylindre,Sphere,Cone,Quadrique)),

# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe GEOMETRIE_COMBINATOIRE : Classe de definition d'une geometrie combinatoire
#                                  Ecrasement : Constitution par ecrasements successifs (dans l'ordre des donnees) de la
#                                               Geometrie Initiale, la frontiere externe etant celle de la geometrie initiale
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GEOMETRIE_COMBINATOIRE = OPER (nom="GEOMETRIE_COMBINATOIRE",op=0,sd_prod=GeometrieCombinatoire,

  fr                    = "Definition d'une geometrie combinatoire",
  ang = "Definition of a combinatorial geometry",
  GeometriePremierPlan	= SIMP (typ=FormePositionnee,statut='o',fr="Geometrie se trouvant au premier plan"),
  GeometrieEcrasee	= SIMP (typ=FormePositionnee,max='**',statut='f',
                                fr="Geometries ecrasées et surchargées par la GeometriePremierPlan"),
  GeometrieUnion        = SIMP (typ=FormePositionnee,max='**',statut='f',
                                fr="Geometries a reunir a la GeometriePremierPlan en gardant les interfaces, les intersections etant des volumes particuliers"),
  GeometrieReunion      = SIMP (typ=FormePositionnee,max='**',statut='f',
                                fr="Geometries a reunir a la GeometriePremierPlan pour former un volume unique"),
  GeometrieIntersection	= SIMP (typ=FormePositionnee,max='**',statut='f',
                                fr="Geometries a intersecter avec la GeometriePremierPlan")
 ) ; 

# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CORRESPONDANCE_REPERE_POSITION_RESEAU : Classe de definition de la position des assemblages combustibles dans un REP
#                                           Reperes (bataille navale ou autre) et
#                                           Coordonnees cartesiennes entieres des assemblages combustibles pour un type de palier
#                                           Origine des coordonnees en bas a gauche d'un systeme en xy
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CORRESPONDANCE_REPERE_POSITION_RESEAU = OPER (nom="CORRESPONDANCE_REPERE_POSITION_RESEAU",op=0,sd_prod=CorrespondanceReperePositionReseau,

  fr                        = "Correspondance entre reperes alphanumeriques et cases d'un reseau",
  ang = "Alphanumeric identificators and lattice coordinates",
  Positions                 = NUPL (	max='**',statut='o',
                                        elements=(SIMP (typ='TXM',fr="Repere alphanumerique arbitraire de l'assemblage"),
                                                  SIMP (typ='I',fr="Premiere Coordonnee entiere de l'assemblage"),
                                                  SIMP (typ='I',fr="Seconde Coordonnee entiere de l'assemblage")))
 );

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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RESEAU = OPER (nom="RESEAU",op=0,sd_prod=Reseau,

  fr			= "Definition d'un reseau compose de juxtapositions de cellules, de reseaux ou d'assemblages",
  en			= "Definition of a lattice",
  Identificateur	= SIMP (typ='TXM',statut='f',fr="Identificateur arbitraire du reseau"),
  TypeGeometrie		= SIMP (typ='TXM',into=('cartesienne','hexagonale'),defaut='cartesienne',statut='f'),
  NbMaillesX		= SIMP (typ='I',defaut=17,statut='o',fr="Nbre de mailles sur le premier axe du reseau"),
  NbMaillesY            = SIMP (typ='I',defaut=17,statut='f',fr="Nbre de mailles sur le second axe du reseau"),
  NbMaillesZ            = SIMP (typ='I',defaut=1 ,statut='f',fr="Nbre de mailles sur l'axe vertical du reseau"),
  PasReseau             = SIMP (typ='R',defaut=1.26 ,statut='f',max=2,fr="Pas du reseau en X et Y"),
  MateriauRemplissage   = SIMP (typ=Materiau,defaut='ModExt',statut='f',fr="Materiau de remplissage du reseau"),
  TypeDefinition        = SIMP (typ='TXM',statut='f',defaut="Complet",into=("Uniforme","Complet","Partiel")),
  BlocUniforme          = BLOC (condition = "TypeDefinition=='Uniforme'",
                                ElementsBase  = SIMP (typ=(Cellule,Reseau,Cluster,GeometrieCombinatoire,AssemblageCombustibleCharge),statut='o',
                                                           fr = "Remplissage uniforme du nouveau reseau par un element particulier"),
                                OrientationElement = SIMP (typ=Orientation,fr="Orientation de l'element geometrique de base",statut='f')),
  BlocComplet           = BLOC (condition = "TypeDefinition=='Complet'",      
                                ElementsBase    = NUPL (max='**', statut='f',
                                                        elements=(SIMP (typ=(Cellule, Reseau, GeometrieCombinatoire,AssemblageCombustibleCharge)),
                                                                  SIMP (typ='TXM',fr="Sigle ou repere associe a l'element geometrique de base"))),
                                Chargement	= SIMP (typ='TXM',statut='f',max='**',
                                                        fr="Liste ordonnee des sigles associes aux elements geometriques charges"),                                                                                                
                                Regroupement	= SIMP (typ='I',statut='f',max='**',
                                                        fr="Indices de regroupement des elements en approximation multicellule"),                                                                                                
                                Reperes		= SIMP (typ='TXM',max='**',statut='f',fr="Reperes arbitraires des elements charges"),
                                ),
  BlocPartiel           = BLOC (condition = "TypeDefinition=='Partiel'",
                                Chargement  = FACT (max='**',
                                        ElementsPositionnes = NUPL (max='**', statut='f',
                                                        elements=(SIMP (typ=(Cellule, Reseau, GeometrieCombinatoire,AssemblageCombustibleCharge)),
                                                                  SIMP (typ='I',min=2,max=2,fr="Coordonnees i j de l'element geometrique de base"))),                                 
                                        ElementsReperes    = NUPL (max='**', statut='f',
                                                        elements=(SIMP (typ=(Cellule, Reseau, GeometrieCombinatoire,AssemblageCombustibleCharge)),
                                                                  SIMP (typ='TXM',fr="Repere associe a l'element geometrique de base"))),                                
                                        CorrespondanceReperePositions = SIMP (typ=CorrespondanceReperePositionReseau,
                                                                              statut='f',
                                                                              fr="Correspondance entre Repere alphanumerique et coordonnees dans le reseau"),
                                        OrientationElement = SIMP (typ=Orientation,max='**',statut='f',fr="Orientation des elements a positionner"),
                                        )),
 ZonePeripherique      = FACT (
                          Epaisseurs      = SIMP (typ='R',max='**',statut='f',fr="Liste des epaisseurs des couches peripheriques"),
                          Materiaux       = SIMP (typ=Materiau,max='**',statut='f',fr="Liste des materiaux des couches peripheriques"),
                          MateriauExterne = SIMP (typ=Materiau,statut='f',fr="Materiau de remplissage de la zone externe du reseau hexagonal"))
 );

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
GRILLE_ASSEMBLAGE = OPER (nom="GRILLE_ASSEMBLAGE",op=0,sd_prod=GrilleAssemblage,

  fr             = "Definition d'une grille d'assemblage",
  ang = "Definition of an elementary assembly grid",
  TypeGrille     = SIMP (typ='TXM',defaut='GrilleMelange',statut='f',fr="Type de grille de structure assemblage"),
  Hauteur        = SIMP (typ='R',defaut=3.3,statut='f',fr="Hauteur de la grille de structure assemblage"),
  Largeur        = SIMP (typ='R',defaut=21.338,statut='f',fr="Largeur de la grille de structure assemblage"),
  MateriauxMasse = NUPL (
      elements = (SIMP (typ=Materiau),SIMP (typ='R')),
      max      = '**',
      statut   = 'f',
      fr       = "Serie de couples (Materiau,masse en g) de composition de la grille"),
  Repartition    = FACT (
      max      = '**',
      statut   = 'o',
      MateriauGrille = SIMP (typ=Materiau,fr="Nom du materiau a repartir",statut='o'),          
      TypeCellule    = SIMP (typ='TXM',max='**',statut='o',fr="Liste des types de cellule ou est reparti le materiau"),
      TypeMateriau   = SIMP (typ='TXM',max='**',statut='o') )
                        ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PARTIE_INFERIEURE_ASSEMBLAGE_COMBUSTIBLE  :   Classe de definition de l'embout inferieur d'un assemblage combustible
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PARTIE_INFERIEURE_ASSEMBLAGE_COMBUSTIBLE = OPER (nom="PARTIE_INFERIEURE_ASSEMBLAGE_COMBUSTIBLE",op=0,sd_prod=PartieInferieureAssemblageCombustible,

  fr                                       = "Definition de la partie inferieure d'un assemblage combustible",
  ang = "Definition of the bottom part of a fuel assembly",
  MateriauEmbout			   = SIMP (typ=Materiau, statut='f',defaut='ACIER',fr="Materiau de l'embout inferieur"),
  MasseBouchonInferieurCrayonCombustible   = SIMP (typ='R',statut='o',fr="Masse du bouchon inferieur du crayon combustible"),
  HauteurBouchonInferieurCrayonCombustible = SIMP (typ='R',statut='o',fr="Hauteur du bouchon inferieur du crayon combustible"),
  MateriauBouchonInferieurCrayonCombustible	= SIMP (typ=Materiau, statut='f',defaut='ZIRCALOY',fr="Materiau du bouchon inferieur du crayon combustible"),
  MasseEmbout                              = SIMP (typ='R',statut='o',fr="Masse de l'embout inferieur"),
  EpaisseurPlaqueAdaptatrice               = SIMP (typ='R',statut='o',fr="Epaisseur de la plaque adaptatrice de l'embout inferieur"),
  LargeurPlaqueAdaptatrice                 = SIMP (typ='R',statut='o',fr="Largeur de la plaque adaptatrice de l'embout inferieur"),
  TrousPlaqueAdaptatrice                   = NUPL (
      max      = '**',
      statut   = 'o',
      elements = ( SIMP (typ='I',statut='o',fr="Nombre de trous de taille definie ci-apres"),
                   SIMP (typ='TXM',into=('Rayon','Cotes'),statut='o',fr="Choix de la forme des trous, elliptique ou rectangulaire"),
                   SIMP (typ='R',min=2,max=2,statut='o',fr="Rayons ou cotes des trous"),
                   SIMP (typ='TXM',defaut='Hauteur',into=('Hauteur','Epaisseur'),statut='o',fr="Mot-cle au choix"),
                   SIMP (typ='R',statut='o',fr="Hauteur des trous dans la plaque adaptatrice"))),
  JeuBouchonCombustiblePlaque	= SIMP (typ='R',statut='o',fr="Hauteur du jeu entre bouchon combustible et plaque adaptatrice"),
  HauteurPied                   = SIMP (typ='R',statut='o',fr="Hauteur du pied de l'embout inferieur"),
  CapuchonRint		        = SIMP (typ='R',statut='f',fr="Rayon interne du capuchon"),
  CapuchonRext			= SIMP (typ='R',statut='f',fr="Rayon externe du capuchon"),
  HauteurVisEpaulee             = SIMP (typ='R',statut='f',fr="Hauteur des vis epaulees des tubes guides"),
  MasseVisEpaulee               = SIMP (typ='R',statut='f',fr="Masse totale des vis epaulees des tubes guides"),
  VisEpauleeRint	        = SIMP (typ='R',statut='f',fr="Rayon interne d'une vis epaulee"),
  VisEpauleeRext	        = SIMP (typ='R',statut='f',fr="Rayon externe d'une vis epaulee"),
  MasseFiltre                   = SIMP (typ='R',statut='f',fr="Masse du filtre anti-debris"),
  MateriauFiltre		= SIMP (typ=Materiau, statut='f', defaut='INCONEL',fr="Materiau du filtre anti-debris"),
  HauteurCale                   = SIMP (typ='R',statut='f',fr="Hauteur de la cale dans le crayon combustible"),
  MateriauCale			= SIMP (typ=Materiau, statut='f', defaut='ACIER',fr="Materiau de la cale dans le crayon combustible"),
  RayonPionCentrage             = SIMP (typ='R',statut='f',fr="Rayon externe des pions de centrage de la plaque inferieure coeur"),
  HauteurPionCentrage           = SIMP (typ='R',statut='f',fr="Hauteur des pions de centrage de la plaque inferieure coeur"),
  HauteurOgivePionCentrage      = SIMP (typ='R',statut='f',fr="Hauteur de l'ogive des pions de centrage de la plaque inferieure coeur"),
  MateriauPionCentrage		= SIMP (typ=Materiau, statut='f',defaut='ACIER',fr="Materiau des pions de centrage de la plaque inferieure coeur"),
  HauteurBouchonTubeGuide       = SIMP (typ='R',statut='f',fr="Hauteur des bouchons des tubes guides"),
  MateriauBouchonTubeGuide	= SIMP (typ=Materiau, statut='f',defaut='ACIER',fr="Materiau des bouchons des tubes guides") 
                                          ) ;

# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PARTIE_SUPERIEURE_ASSEMBLAGE_COMBUSTIBLE :    Classe de definition de l'embout superieur d'un assemblage combustible
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PARTIE_SUPERIEURE_ASSEMBLAGE_COMBUSTIBLE = OPER (nom="PARTIE_SUPERIEURE_ASSEMBLAGE_COMBUSTIBLE",op=0,sd_prod=PartieSuperieureAssemblageCombustible,

  fr                                       = "Definition de la partie superieure d'un assemblage combustible",
  ang = "Definition of the top part of a fuel assembly",
  MateriauEmbout		     	   = SIMP (typ=Materiau, statut='f',defaut='ACIER',fr="materiau  de l'embout superieur"),
  MasseBouchonSuperieurCrayonCombustible   = SIMP (typ='R',statut='o',fr="Masse du bouchon superieur du crayon combustible"),
  HauteurBouchonSuperieurCrayonCombustible = SIMP (typ='R',statut='o',fr="Hauteur du bouchon superieur du crayon combustible"),
  MateriauBouchonSuperieurCrayonCombustible	= SIMP (typ=Materiau, statut='f',defaut='ZIRCALOY',fr="Materiau du bouchon superieur du crayon combustible"),
  RessortCrayonCombustible                 = SIMP (typ='R',statut='o',fr="Masse du ressort du crayon combustible"),
  HauteurChambreExpansion                  = SIMP (typ='R',statut='o',fr="Hauteur de la chambre d'expansion"),
  MasseEmbout                              = SIMP (typ='R',statut='o',fr="Masse de l'embout superieur"),
  HauteurEmbout                            = SIMP (typ='R',statut='o',fr="Hauteur de l'embout superieur"),
  MasseRessortsEmbout                      = SIMP (typ='R',statut='o',fr="Masse des ressorts de l'embout superieur"),
  MateriauRessortsEmbout		   = SIMP (typ=Materiau,  statut='f', defaut='INCONEL',fr="Materiau des ressorts de l'embout superieur"),
  EpaisseurPlaqueAdaptatrice               = SIMP (typ='R',statut='o',fr="Epaisseur de la plaque adaptatrice"),
  LargeurPlaqueAdaptatrice                 = SIMP (typ='R',statut='o',fr="Largeur de la plaque adaptatrice"),
  TrousPlaqueAdaptatrice                   = NUPL (
      max      = '**',
      statut   = 'o',
      elements = (      SIMP (typ='I',),
                        SIMP (typ='TXM',into=('Rayon','Cotes')),
                        SIMP (typ='R',min=2,max=2,fr="Rayons mineur et majeur ou Cotes du trou"),
                        SIMP (typ='TXM',into=('Hauteur','Epaisseur')),
                        SIMP (typ='R',fr="Hauteur du trou"))), 
  JeuBouchonCombustiblePlaque              = SIMP (typ='R',statut='o',fr="Hauteur du jeu entre Bouchon combustible et Plaque adaptatrice"),
  EpaisseurJupe                            = SIMP (typ='R',statut='o',fr="Epaisseur de la jupe de l'embout superieur"),
  HauteurJupe                              = SIMP (typ='R',statut='f',fr="Hauteur de la jupe de l'embout superieur"),
  RayonPionCentrage                        = SIMP (typ='R',statut='f',fr="Rayon des pions de centrage superieurs"),
  HauteurPionCentrage                      = SIMP (typ='R',statut='f',fr="Hauteur des pions de centrage superieurs"),
  HauteurOgivePionCentrage                 = SIMP (typ='R',statut='f',fr="Hauteur de l'ogive des pions de centrage superieurs"),
  MateriauPionCentrage			   = SIMP (typ=Materiau, statut='f',defaut='ACIER',fr="Materiau des pions de centrage superieurs"),
  RayonInterneManchon		           = SIMP (typ='R',statut='f',fr="Rayon interne des manchons des tubes guides"),
  RayonExterneManchon       		   = SIMP (typ='R',statut='f',fr="Rayon externe des manchons des tubes guides"),
  HauteurManchon                           = SIMP (typ='R',statut='f',fr="Hauteur des manchons des tubes guides"),
  MasseManchon                             = SIMP (typ='R',statut='f',fr="Masse d'un manchon des tubes guides") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe OPTIONS_AUTOPROTECTION : Classe de definition des donnees d'autoprotection du code de reseau
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONS_AUTOPROTECTION = OPER (nom="OPTIONS_AUTOPROTECTION",op=0,sd_prod=OptionsAutoprotection,

  fr                    = "Definition des donnees d'autoprotection des resonances",
  ang = "Definition of resonance self shielding data",
  TypeCombustible	= SIMP (typ='TXM',max='**',statut='o',fr="Type de combustible auquel s'appliquent ces options d'autoprotection"),
  MethodeAutoprotection = SIMP (typ='TXM',into=('SanchezCoste','SousGroupes'),defaut='SanchezCoste',statut='f'),
  IsotopesAutoproteges  = NUPL (
      max	= '**',
      elements	= (SIMP (typ=Isotope,statut='o',fr="Nom de l'isotope a autoproteger"),
                   SIMP (typ='TXM',into=('Moyenne','Detaillee','Couronne'),statut='o'),
                   SIMP (typ='TXM',into=('Materiaux','Cellules'),statut='f',fr="Choix d'autoprotection sur les materiaux ou les cellules"),
                   SIMP (typ='TXM',max='**',statut='f',fr="Liste des types de materiaux ou de cellules concernes"))),
  Irradiations  = SIMP (typ='R',max='**',statut='f',fr="Irradiations ou se font les calculs d'autoprotection"),
  IrradiationsPoison  = SIMP (typ='R',max='**',statut='f',fr="Irradiations ou se font les calculs d'autoprotection des poisons integres au combustible")
  ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ASSEMBLAGE_TYPE : Classe de definition d'un type d'assemblage (ensemble de crayons ou de reseaux quelconques)
#                           Rajout des structures grilles et embouts (dans le cas des REP)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ASSEMBLAGE_TYPE = OPER (nom="ASSEMBLAGE_TYPE",op=0,sd_prod=AssemblageType,

  fr                    = "Definition d'un assemblage type et des elements associes eventuels",
  ang = "Definition of an assembly type and its associated elements",
# TypeGeometrie         = SIMP (typ='TXM',into=('Cartesienne','Hexagonale','Generale'),defaut='Cartesienne',statut='f'),
# TypeAbsorbant         = SIMP (typ='TXM',defaut='0P',statut='f'),
# Identificateur        = SIMP (typ='TXM',defaut='AFA  17 0P 0P',statut='f'),
  Geometrie             = SIMP (typ=(Cellule,Reseau,GeometrieCombinatoire),statut='o',max='**',
                                fr="Liste des geometries associees a l'assemblage"),
#    Symetrie           = SIMP (typ='TXM',into=('1/4','1/8','1/2','PI','PI/2','PI/6','PI/3','2PI/3','SansSymetrie'),
#                               defaut='SansSymetrie',statut='f'),
#    ZoneCalculee       = SIMP (typ='TXM',defaut='Entiere',
#                               into=('Entiere','1/2 N','1/2 S','1/2 E','1/2 O','1/4 N-E','1/4 N-O','1/4 S-E',
#                                               '1/4 S-O','1/8 E-NE','1/8 N-NE','1/8 N-NO',
#                                               '1/8 O-SO','1/8 S-SO','1/8 S-SE','1/8 E-SE',
#                                               '1/6 E','1/6 NE','1/6 NO','1/6 O''1/6 SO','1/6 SE'),statut='f'),
  GrillesStructure      = NUPL (
     			  max      = '**',
      			  statut   = 'f',
      			  elements = (	SIMP (typ=GrilleAssemblage,fr="Type de grille"),
					SIMP (typ='R',max='**',fr="Positions axiales du type de grille"))),
  PartieInferieure      = SIMP (typ=PartieInferieureAssemblageCombustible,statut='f',fr="Type d'embout inferieur"),
  PartieSuperieure      = SIMP (typ=PartieSuperieureAssemblageCombustible,statut='f',fr="Type d'embout superieur"),
  ElementsAssocies	= SIMP (typ=(ElementsGrappeCommande,ElementsAbsorbantsFixes,GrappeBouchonAssemblage),max='**',statut='f')
#  ZoneCalculee          = SIMP (typ='DROITE',min=2,max=2,statut='f',fr="Droites delimitant la zone de calcul"),
#  DonneesAutoprotection = SIMP (typ=Autoprotection,statut='f')
 ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ASSEMBLAGE_COMBUSTIBLE_CHARGE : Classe de definition d'un assemblage combustible charge dans un coeur REP
#                               
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ASSEMBLAGE_COMBUSTIBLE_CHARGE = OPER (nom="ASSEMBLAGE_COMBUSTIBLE_CHARGE",op=0,sd_prod=AssemblageCombustibleCharge,

  fr                          = "Definition d'un assemblage combustible charge en reacteur",
  ang = "Definition of a core loaded fuel assembly ",
  Identificateur              = SIMP (typ='TXM',statut='o',fr="Code d'identification de l'assemblage combustible"),
  Constructeur                = SIMP (typ='TXM',statut='o',into=('FRAMATOME','SIEMENS','ABB','ENUSA','WESTINGHOUSE')),
  TypeAssemblage              = SIMP (typ=AssemblageType,statut='o'),
  CleControle                 = SIMP (typ='TXM',statut='o'),
  Engagement                  = SIMP (typ='TXM',statut='o'),
  NumeroLot                   = SIMP (typ='I',statut='o'),
  EnrichissementTheoriqueU235 = SIMP (typ='R',statut='o'),
  EnrichissementTheoriquePu   = SIMP (typ='R',statut='f'),
  MasseTheoriqueNL            = SIMP (typ='R',statut='o'),
  MasseInitialeUPu            = SIMP (typ='R',statut='o'),
  MasseInitialeU232	      = SIMP (typ='R',statut='f'),
  MasseInitialeU234           = SIMP (typ='R',statut='f'),
  MasseInitialeU235           = SIMP (typ='R',statut='f'),
  MasseInitialeU236           = SIMP (typ='R',statut='f'),
  MasseInitialePu239          = SIMP (typ='R',statut='f'),
  MasseInitialePu240          = SIMP (typ='R',statut='f'),
  MasseInitialePu241          = SIMP (typ='R',statut='f'),
  MasseInitialePu242          = SIMP (typ='R',statut='f'),
  MasseInitialeAm241          = SIMP (typ='R',statut='f'),
  AbsorbantFixe		      = SIMP (typ='TXM',statut='f'),
  Campagnes                   = NUPL (
      max      = '**',
      statut   = 'f',
      elements = ( SIMP (typ='TXM',fr="Identificateur de la campagne"),SIMP (typ='TXM',fr="Etat de l'assemblage"))),
  BibliothequeNeutronique = SIMP (typ='TXM',statut='f',fr="Repertoire des Bibliothèques neutroniques associees") ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe ELEMENT_BARRE :	 Classe de définition d'une barre element d'un assemblage
# 				 Definition des barres des grappes de commande (barre et gaine, et composants axiaux)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ELEMENT_BARRE = OPER (nom="ELEMENT_BARRE",op=0,sd_prod=ElementBarre,

  fr				= "Définition d'une barre element d'un assemblage",
  en				= "Definition of an assembly rod element",
  MateriauPartieInferieure	= SIMP (typ=Materiau,statut='o',defaut='ACIER',fr="Materiau composant la partie inferieure de la barre"),
  MateriauPartieSuperieure	= SIMP (typ=Materiau,statut='o',defaut='ACIER',fr="Materiau composant la partie superieure de la barre"),
  HauteurBarre			= SIMP (typ='R',statut='o',fr="Hauteur de la barre"),
  HauteurPartieInferieure	= SIMP (typ='R',statut='f',fr="Hauteur de la partie inferieure de la barre"),
  HauteurPartieSuperieure	= SIMP (typ='R',statut='f',fr="Hauteur de la partie superieure de la barre"),
  RayonInternePartieInferieure	= SIMP (typ='R',statut='f',defaut=0.,fr="Rayon Interne de la partie inferieure de la barre"),
  RayonInternePartieSuperieure	= SIMP (typ='R',statut='f',defaut=0.,fr="Rayon Interne de la partie superieure de la barre"),
  RayonExternePartieInferieure	= SIMP (typ='R',statut='o',fr="Rayon Externe de la partie inferieure de la barre"),
  RayonExternePartieSuperieure	= SIMP (typ='R',statut='f',fr="Rayon Externe de la partie superieure de la barre"),
  MasseRessort			= SIMP (typ='R',statut='o',fr="Masse du ressort de la barre"),
  MateriauRessort		= SIMP (typ=Materiau,statut='o',fr="Materiau du ressort de la barre"),
  HauteurRessort		= SIMP (typ='R',statut='o',fr="Hauteur du ressort de la barre"),
  HauteurBouchonInferieur	= SIMP (typ='R',defaut=0.,statut='f',fr="Hauteur du bouchon inferieur de la barre"),
  HauteurBouchonSuperieur	= SIMP (typ='R',defaut=0.,statut='f',fr="Hauteur du bouchon superieur de la barre"),
  RayonBouchonInferieur		= SIMP (typ='R',defaut=0.,statut='f',fr="Rayon externe du bouchon inferieur de la barre"),
  RayonBouchonSuperieur		= SIMP (typ='R',defaut=0.,statut='f',fr="Rayon externe du bouchon superieur de la barre"),
  MateriauGaine			= SIMP (typ=Materiau,defaut='ACIER',statut='o',fr="Materiau de la gaine externe de la barre"),
  RayonInterneGaine		= SIMP (typ='R',defaut=0.,statut='f', fr="Rayon Interne de la gaine externe de la barre"),
  RayonExterneGaine		= SIMP (typ='R',defaut=0.,statut='f', fr="Rayon Externe de la gaine externe de la barre")
 ) ;
#----------------------------------------------------------------------------------------------------------------------------------
#  Classe ELEMENTS_GRAPPE_COMMANDE :	Classe de définition des éléments des grappes de commande
#				Association avec les différents types de barres absorbantes
#				Description simplifiée de l'araignée et du bouchon des barres
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ELEMENTS_GRAPPE_COMMANDE = OPER (nom="ELEMENTS_GRAPPE_COMMANDE",op=0,sd_prod=ElementsGrappeCommande,

  fr			= "Définition des éléments des grappes de commande",
  en			= "Definition of control rod cluster components",
  ElementsBarre		= SIMP (typ= ElementBarre,	max='**',statut='f',fr="Liste des barres absorbantes associees"),
  HauteurPasInsertion	= SIMP (typ='R',defaut=1.5875,	statut='f'),
  HauteurInsertionMax	= SIMP (typ='R',defaut=300.,	statut='f'),
  NbPasInsertion	= SIMP (typ='I',defaut=0,	statut='f'),
  HauteurAraignee16P	= SIMP (typ='R',defaut=0.,	statut='f'),
  HauteurAraignee4M	= SIMP (typ='R',defaut=0.,	statut='f'),
  HauteurAraignee4G	= SIMP (typ='R',defaut=0.,	statut='f'),
  HauteurPommeau	= SIMP (typ='R',defaut=0.,	statut='f'),
  RayonPommeau		= SIMP (typ='R',defaut=0.,	statut='f') ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ELEMENTS_ABSORBANTS_REP : Classe de definition des elements des grappes d'absorbants fixes
#                                 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ELEMENTS_ABSORBANTS_FIXES = OPER (nom="ELEMENTS_ABSORBANTS_FIXES",op=0,sd_prod=ElementsAbsorbantsFixes,

  fr                                 = "Definition des elements des grappes d'absorbants fixes",
  ang = "Definition of non movable absorber control rod cluster elements",
# Limitation a 12 caracteres
# HBouchInfPyrex 	= SIMP (typ='R',statut='f'),
# RBouchInfPyrex   	= SIMP (typ='R',statut='f'),
# HZoneVidePyrex        = SIMP (typ='R',statut='f'),
# HBouchSupPyrex 	= SIMP (typ='R',statut='f'),
# RBouchSupPyrex   	= SIMP (typ='R',statut='f'),
# MatBouchonPyrex       = SIMP (typ=Materiau,statut='f')
  CrayonPyrexHauteurBouchonInferieur = SIMP (typ='R',statut='f'),
  CrayonPyrexRayonBouchonInferieur   = SIMP (typ='R',statut='f'),
  CrayonPyrexHauteurZoneVide         = SIMP (typ='R',statut='f'),
  CrayonPyrexHauteurBouchonSuperieur = SIMP (typ='R',statut='f'),
  CrayonPyrexRayonBouchonSuperieur   = SIMP (typ='R',statut='f'),
  CrayonPyrexMateriauBouchon         = SIMP (typ=Materiau,statut='f') ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe GRAPPE_BOUCHON_ASSEMBLAGE_REP : Classe de definition d'une grappe bouchon
#                                 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GRAPPE_BOUCHON_ASSEMBLAGE = OPER (nom="GRAPPE_BOUCHON_ASSEMBLAGE",op=0,sd_prod=GrappeBouchonAssemblage,

  fr                                 = "Definition d'une grappe bouchon d'assemblage combustible",
  ang = "Definition of ",
  HauteurBouchonPartieBasse          = SIMP (typ='R',statut='f'),
  RayonBouchonPartieBasse            = SIMP (typ='R',statut='f'),
  HauteurBouchonPartieIntermediaire1 = SIMP (typ='R',statut='f'),
  RayonBouchonPartieIntermediaire1   = SIMP (typ='R',statut='f'),
  HauteurBouchonPartieIntermediaire2 = SIMP (typ='R',statut='f'),
  RayonBouchonPartieIntermediaire2   = SIMP (typ='R',statut='f'),
  HauteurBouchonRegionSousPlaque     = SIMP (typ='R',statut='f'),
  HauteurBouchonRegionSurPlaque      = SIMP (typ='R',statut='f'),
  RayonBouchonRegionPlaque           = SIMP (typ='R',statut='f'),
  HauteurSupport                     = SIMP (typ='R',statut='f'),
  MasseGrappe                        = SIMP (typ='R',statut='f'),
  Materiau                           = SIMP (typ=Materiau,statut='f') ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ELEMENTS_ASSEMBLAGE : Classe de définition des éléments associes a l'assemblage combustibe REP
#                                 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - class ReflexionIsotrope (TObjet):pass
#ELEMENTS_ASSEMBLAGE = OPER (nom="ELEMENTS_ASSEMBLAGE",op=0,sd_prod=ElementsAssemblage,
#
#  fr  = "Definition des elements associes a l'assemblage",
#  ang = "Definition of the fuel assembly associated elements",
#  GrappeBouchon         = SIMP (typ=GrappeBouchonAssemblage,statut='o'),
#  CrayonsAbsorbants     = SIMP (typ=ElementsAbsorbants,statut='o'),
#  GrappesCommande       = SIMP (typ=ElementsGrappeCommande,statut='o')
# ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe SYSTEME_UNITES_MESURE :       Classe de definition du systeme d'unites pour l'expression des donnees 
#                               Sauf indication contraire dans les attributs des classes, les unites utilisees sont definies
#                               dans la classe ci-dessous
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SYSTEME_UNITES_MESURE = OPER (nom="SYSTEME_UNITES_MESURE",op=0,sd_prod=SystemeUnitesMesure,

  fr                           = "Definition du systeme d'unites pour l'expression des donnees",
  ang = "Definition of data unit system",
  Longueur                     = SIMP (typ='TXM',statut='o',defaut='cm'),
  Masse                        = SIMP (typ='TXM',statut='o',defaut='g'),
  Temps                        = SIMP (typ='TXM',statut='o',defaut='s'),
  Irradiation                  = SIMP (typ='TXM',statut='o',defaut='MWj/t'),
  Fluence                      = SIMP (typ='TXM',statut='o',defaut='n/kb'),
  SectionEfficaceMicroscopique = SIMP (typ='TXM',statut='o',defaut='barn'),
  SectionEfficaceMacroscopique = SIMP (typ='TXM',statut='o',defaut='cm-1'),
  MasseVolumique               = SIMP (typ='TXM',statut='o',defaut='g/cm3'),
  Concentration                = SIMP (typ='TXM',statut='o',defaut='E24*atome/cm3'),
  Temperature                  = SIMP (typ='TXM',statut='o',defaut='C'),
  ProportionMateriau           = SIMP (typ='R',statut='o',defaut=0.01),
  Taux                         = SIMP (typ='R',statut='o',defaut=0.01),
  Enrichissement               = SIMP (typ='R',statut='o',defaut=0.01),
  Pression                     = SIMP (typ='TXM',statut='o',defaut='bar') ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classes CONDITION_LIMITE elementaires : 	Classes de definition de Conditions limites elementaires
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
VIDE = OPER (nom="VIDE",op=0,sd_prod=Vide,
				fr  = "Condition aux limites de vide",
  				ang= "Void boundary condition" ) ;

REFLEXION_ISOTROPE = OPER (nom="REFLEXION_ISOTROPE",op=0,sd_prod=ReflexionIsotrope,
 				fr  = "Condition aux limites de reflexion isotrope",
				ang= "Isotropic Reflexion boundary condition" ) ;

REFLEXION_SPECULAIRE = OPER (nom="REFLEXION_SPECULAIRE",op=0,sd_prod=ReflexionSpeculaire,
 				fr  = "Condition aux limites de reflexion speculaire",
				ang= "Specular Reflexion boundary condition" ) ;
ALBEDO = OPER (nom="ALBEDO",op=0,sd_prod=Albedo,
 				fr   = "Condition aux limites d'albedo",
 				ang= "Albedo boundary condition",
  				albedo = SIMP (typ='R',statut='o',max='**') ) ;
TRANSLATION = OPER (nom="TRANSLATION",op=0,sd_prod=Translation,
 				fr      = "Condition aux limites de translation",
				ang = "Translation boundary condition",
				Vecteur = SIMP (typ=Vecteur,statut='o') ) ;
ROTATION = OPER (nom="ROTATION",op=0,sd_prod=Rotation,
				fr     = "Condition aux limites de rotation",
				ang = "Rotational boundary condition",
				Centre = SIMP (typ=Point,statut='o'),
				Angle  = SIMP (typ='R',statut='o',defaut=90.) ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONDITION_LIMITE_SPECIALE : 	Classe de definition de Conditions limites sur les surfaces elementaires de la geometrie
#    					modifiant la CL generale
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONDITION_LIMITE_SPECIALE = OPER (nom="CONDITION_LIMITE_SPECIALE",op=0,sd_prod=ConditionLimiteSpeciale,

  fr     = "Condition limite particuliere qui sera plaquee sur la geometrie",
  ang = "Special boundary condition added to the geometry",
  Type = SIMP (typ=(Vide,ReflexionIsotrope,ReflexionSpeculaire, Albedo, Translation, Rotation),statut='o'),
  ZonesApplication = SIMP (	typ=(Segment,ArcCercle,Conique),max='**',statut='o',
				fr="Liste des segments ou surfaces sur lesquels porte la condition limite")
 ) ;
# ----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONDITION_LIMITE_GENERALE : Classe de definition des conditions limites de l'objet geometrique complet
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONDITION_LIMITE_GENERALE = OPER (nom="CONDITION_LIMITE_GENERALE",op=0,sd_prod=ConditionLimiteGenerale,

  fr  = "Condition limite a la surface externe de la geometrie complete",
  ang = "Boundary condition for the complete geometry",
  ZoneCalculee          = NUPL (statut='f',min=2,max=2,fr="Droites ou plans delimitant la zone de calcul",
                                elements = (SIMP (typ=(Droite,Plan)), SIMP (typ='TXM',into=('Plus','Moins')))),
  ConditionParDefaut	= SIMP (typ=(Vide, ReflexionIsotrope, ReflexionSpeculaire, Albedo),
				defaut=ReflexionIsotrope,
				statut='f',
				fr="Condition limite par defaut"),
  ConditionsParticulieres  = NUPL (
     				fr       = "Conditions particulieres modifiant localement la condition limite par defaut",
      				max      = '**',
      				statut   = 'f',
      				elements = (SIMP (typ='TXM',into=('X-','X+','Y-','Y+','Z-','Z+','R+','X','Y','Z')),
          				    SIMP (typ=(Vide,ReflexionIsotrope,ReflexionSpeculaire, Albedo, Translation, Rotation)))),
  ConditionsSupplementaires = SIMP (
      				typ    = ConditionLimiteSpeciale,
     				statut = 'f',
      				max    = '**',
      				fr     = "Conditions limites non exprimables avec les donnees precedentes") 
 ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POSITION_ASSEMBLAGE_COMBUSTIBLE : Classe de definition de la position des assemblages combustibles dans un REP
#                                           Reperes (bataille navale ou autre) et
#                                           Coordonnees cartesiennes entieres des assemblages combustibles pour un type de palier
#                                           Origine des coordonnees en bas a gauche d'un systeme en xy
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POSITION_ASSEMBLAGE_COMBUSTIBLE = OPER (nom="POSITION_ASSEMBLAGE_COMBUSTIBLE",op=0,sd_prod=PositionAssemblageCombustible,

  fr                        = "Position des assemblages combustibles",
  ang = "Position of fuel assemblies",
  NbAssemblagesCombustibles = SIMP (typ='I',statut='o',defaut=157),
  regles=(UN_PARMI('PositionReseau', 'Positions'),),
  PositionReseau            = SIMP (typ=CorrespondanceReperePositionReseau,statut="f"),
  Positions                 = NUPL (	max='**',statut='f',
                                        elements=(SIMP (typ='TXM',fr="Repere alphanumerique arbitraire de l'assemblage"),
                                                  SIMP (typ='I'  ,fr="Premiere Coordonnee entiere de l'assemblage"),
                                                  SIMP (typ='I'  ,fr="Seconde Coordonnee entiere de l'assemblage")))
 ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POSITION_INSTRUMENTATION : Classe de definition de la position des assemblages instrumentes dans un REP 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POSITION_INSTRUMENTATION_INTERNE = OPER (nom="POSITION_INSTRUMENTATION_INTERNE",op=0,sd_prod=PositionInstrumentationInterne,

  fr                        = "Definition de la position des assemblages instrumentes",
  ang = "Definition of neutron flux detector position",
# TypePalier                = SIMP (typ='TXM',max='**',statut='o'),
  NbAssemblagesInstrumentes = SIMP (typ='I',statut='o'),
  Positions                 = NUPL (
      max      = '**',
      statut   = 'o',
      elements = (SIMP (typ='TXM',fr= "Type d'instrumentation"),
                  SIMP (typ='I',min=2,max=2,fr= "Coordonnees entieres de l'assemblage instrumente dans le reseau"))) ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe POSITION_GRAPPES_COMMANDE : Classe de definition des grappes de commande pour un type de schema de grappe
#                                     Donnees de la position (coordonnees entieres en xy), du type de grappe et du groupe d'appartenance 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
POSITION_GRAPPES_COMMANDE = OPER (nom="POSITION_GRAPPES_COMMANDE",op=0,sd_prod=PositionGrappesCommande,

  fr              = "Definition des grappes de commande pour un schema d'implantation particulier",
  ang = "Definition of control rod cluster position ant type",
  TypeSchema      = SIMP (typ='TXM',statut='o'),
  NbTotalGrappes  = SIMP (typ='I',statut='o'),
  PositionsEtType = NUPL (max='**',statut='o',
                          elements=(SIMP (typ='TXM',fr="Nom du groupe de grappes"),
                                    SIMP (typ='I',fr="Nombre de grappes du groupe"),
                                    SIMP (typ='TXM',fr="Type de grappes"),
                                    SIMP (typ='I',max='**',fr="Coordonnees des grappes"))) ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe STRUCTURES_INTERNES_REACTEUR :        Classe de definition des structures internes du coeur du reacteur
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
STRUCTURES_INTERNES_REACTEUR = OPER (nom="STRUCTURES_INTERNES_REACTEUR",op=0,sd_prod=StructuresInternesReacteur,

  fr                      = "Definition des structures internes du coeur",
  ang = "Definition of core internal structures",
  PlaqueInferieureCoeur   = FACT (
      Epaisseur = SIMP (typ='R',statut='o',			fr="Epaisseur de la plaque inferieure du coeur"),
      Materiau  = SIMP (typ=Materiau,statut='f',defaut='ACIER',fr="Materiau  de la plaque inferieure du coeur"),
      Trous     = NUPL (
          max      = '**',
          elements = (
              SIMP (typ='I',				fr="Nombre de trous dont on donne les dimensions"),
              SIMP (typ='TXM',into=('Rayon','Cotes'),	fr="Mot-cle indiquant si on donne le rayon ou les cotes"),
              SIMP (typ='R',min=2,max=2,		fr="Rayon ou cotes des trous"),
              SIMP (typ='TXM',into=('Hauteur','Epaisseur'),fr="Mot-cle indiquant l'entree de la hauteur du trou"),
              SIMP (typ='R',				fr="Hauteur du trou")))),
  PlaqueSuperieureCoeur   = FACT (
      Epaisseur = SIMP (typ='R', 				 fr="Epaisseur de la plaque superieure du coeur"),
      Materiau  = SIMP (typ=Materiau,statut='f',defaut='ACIER',fr="Materiau  de la plaque superieure du coeur"),
      Trous     = NUPL (
          max      = '**',
          elements = (
              SIMP (typ='I',				fr="Nombre de trous dont on donne les dimensions"),
              SIMP (typ='TXM',into=('Rayon','Cotes'),	fr="Mot-cle indiquant si on donne le rayon ou les cotes"),
              SIMP (typ='R',min=2,max=2,		fr="Rayon ou cotes des trous"),
              SIMP (typ='TXM',into=('Hauteur','Epaisseur'),fr="Mot-cle indiquant l'entree de la hauteur du trou"),
              SIMP (typ='R',				fr="Hauteur du trou")))),
  CloisonnementCoeur      = FACT (
      Epaisseur             = SIMP (typ='R',					fr="Epaisseur du cloisonnement du coeur"),
      Materiau              = SIMP (typ=Materiau,statut='f',defaut='ACIER',	fr="Materiau  du cloisonnement du coeur"),
      DimensionsInterieures = NUPL (
          max      = '**',
          elements = (
              SIMP (typ='I',				 	fr="Nombre d'assemblages dans la rangee"),
              SIMP (typ='TXM',into=('Assemblages','Assemblies'),fr="Mot-cle suivant le nombre d'assemblages"),
              SIMP (typ='TXM',into=('Largeur','Cote'),		fr="Mot-cle precedant la largeur interieure du cloisonnement"),
              SIMP (typ='R',					fr="Largeur interieure du cloisonnement"),
              SIMP (typ='TXM',into=('NbJeuCloisonGrille','NbJeu'),fr="Mot-cle precedant le nombre de jeux CloisonGrille"),
              SIMP (typ='I',					fr="Nombre de jeux CloisonGrille"))),
      TrousDepressurisation = NUPL (elements=(SIMP (typ='I',fr="Nombre de trous de depressurisation"),
						SIMP (typ='TXM',into=('Rayon','Radius'),fr="Mot-cle precedant la valeur du rayon des trous"),
						SIMP (typ='R',fr="Rayon des trous de depressurisation"))),
      TemperatureMoyenne    = SIMP (typ='R',fr="Temperature Moyenne du cloisonnement")),
  RenfortsInternes        = FACT (
      Nombre                      = SIMP (typ='I',max='**'),
      Epaisseur                   = SIMP (typ='R',max='**'),
      Materiau                    = SIMP (typ=Materiau,max='**',statut='f',defaut='ACIER'),
      NbTrousDepressurisation     = SIMP (typ='I',max='**'),
      RayonsTrousDepressurisation = SIMP (typ='R',max='**'),
      TemperatureMoyenne          = SIMP (typ='R'),statut='f'),
  EnveloppeVirole        = FACT (
      RayonInterne       = SIMP (typ='R'),
      RayonExterne       = SIMP (typ='R'),
      Materiau           = SIMP (typ=Materiau,statut='f',defaut='ACIER'),
      TemperatureMoyenne = SIMP (typ='R')),
  Boucliers              = FACT (
      RayonInterne       = SIMP (typ='R'),
      RayonExterne       = SIMP (typ='R'),
      Materiau           = SIMP (typ=Materiau,statut='f',defaut='ACIER'),
      Secteurs           = NUPL (max='**',elements=(SIMP (typ='R'),SIMP (typ='R'))),
      TemperatureMoyenne = SIMP (typ='R')),
  Cuve                    = FACT (
      RayonInterne       = SIMP (typ='R'),
      RayonExterne       = SIMP (typ='R'),
      Materiau           = SIMP (typ=Materiau,statut='f',defaut='ACIER'),
      TemperatureMoyenne = SIMP (typ='R')) ) ; # Fin STRUCTURES_INTERNES_REACTEUR
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CARACTERISTIQUES_PALIER : Classe de definition des donnees generales d'un type de palier de reacteur 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CARACTERISTIQUES_PALIER = OPER (nom="CARACTERISTIQUES_PALIER",op=0,sd_prod=CaracteristiquesPalier,

  fr                  = "Definition des donnees generales d'un type de palier de reacteur",
  ang = "Definition of general data for a type of nuclear reactor",
  TypePalier	      = SIMP (typ='TXM',statut='o',fr="Identificateur du type de palier"),
  PositionCombustible = SIMP (typ=PositionAssemblageCombustible,statut='o'),
  PositionDetecteur   = SIMP (typ=PositionInstrumentationInterne,statut='o'),
  StructuresInternes  = SIMP (typ=StructuresInternesReacteur,statut='o'),
  NbBouclesPrimaires  = SIMP (typ='I',statut='o',defaut=3,fr="Nombre de boucles primaires"),
  NbTubesParGV        = SIMP (typ='I',statut='f',fr="Nombre de tubes par GV") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe SITE_NUCLEAIRE_EDF : Classe de definition d'un site nucleaire EDF (Tranches, paliers et numero comptable) 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SITE_NUCLEAIRE = OPER (nom="SITE_NUCLEAIRE",op=0,sd_prod=SiteNucleaire,

  fr       = "Definition d'un site nucleaire EDF",
  ang = "Definition of a nuclear power plant site",
  NomSite  = SIMP (typ='TXM',statut='o',fr="Nom du site nucleaire",defaut='TRICASTIN'),
  Tranches = NUPL (max='**',elements=(	SIMP (typ='I'  ,statut='o',fr="Numero de la tranche nucleaire"),
					SIMP (typ='TXM',statut='o',fr="Trigramme de la tranche nucleaire"),
					SIMP (typ=CaracteristiquesPalier,statut='o',fr="Type de palier"),
					SIMP (typ='I'  ,statut='o',fr="Numero comptable de la tranche"))) ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe ESPACE_VARIATIONS :     Classe de definition des parametres de contre-reactions neutroniques et de leurs variations
#                                       Donnees definissant l'espace des parametres dont dependent les bibliotheques
#                                       neutroniques et la discretisation de leur espace de variation.
#                                       Definition de la methode de balayage de cet espace (Suite d'options complementaires) :
#                                       1) ParametresIndependants :     Calculs independants en donnant successivement a chacun
#                                                                       des parametres leurs valeurs individuelles
#                                       2) CoinsDomaine :               Rajout des calculs aux limites extremes du domaine
#                                       3) BordsDomaine :               Rajout des calculs aux bords du domaine
#                                       4) Grilles2D :                  Rajout des calculs sur les grilles 2D 
#                                                                       passant par un point de reference
#                                       5) CasParticuliers :            Rajout de points specifiques de calcul
#                                       6) EspaceComplet :              Balayage complet du domaine des parametres
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ESPACE_VARIATIONS = OPER (nom="ESPACE_VARIATIONS",op=0,sd_prod=EspaceVariations,

  fr              = "Definition de l'espace de variation des parametres neutroniques",
  ang = "Definition of feedback or variable parameters",
  Variations      = NUPL (max='**',statut='f',
                          elements=(	SIMP (typ='TXM',fr="Nom du parametre a faire varier"),
                                        SIMP (typ='R',max='**',fr="Valeurs discretes de variation du parametre"))),
  MethodeBalayage = SIMP (
      typ    = 'TXM',
      max    = '**',
      defaut = 'ParametresIndependants',
      into   = ('ParametresIndependants','CoinsDomaine','BordsDomaine','Grilles2D','CasParticuliers','EspaceComplet'),
      statut = 'f'),
  TypeVariation   = SIMP (typ='TXM',defaut='absolu',into=('relatif','absolu'),statut='f'),
  CasParticuliers = NUPL (max='**',statut='f',fr="Liste des couples (Parametre, Valeur du parametre) pour les cas particuliers",
                          elements=(SIMP (typ='TXM'),SIMP (typ='R'))),
  CasReference    = NUPL (max='**',statut='f',fr="Liste des couples (Parametre, Valeur du parametre) pour le cas de reference",
                          elements=(SIMP (typ='TXM'),SIMP (typ='R'))) ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DONNEES_EVOLUTION_IRRADIATION : Classe de definition des valeurs d'irradiation intervenant dans les phases de calcul et d'edition
#                       Pour le moment, on ne considere que l'Evolution, les Editions, l'Autoprotection et les ContreReactions
#                       ou les irradiations de reprise (Normale, Gs et Beta pour EDF).
#                       Donnees consistant pour chaque phase d'une liste d'irradiations en MWj/t
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DONNEES_EVOLUTION_IRRADIATION = OPER (nom="DONNEES_EVOLUTION_IRRADIATION",op=0,sd_prod=DonneesEvolutionIrradiation,

  fr                   = "Definition des donnees du calcul d'evolution et des irradiations de reprise",
  ang = "Definition of depletion calculation data and burnup restart calculations",
  Unite		       = SIMP (typ='TXM',defaut='MWj/t',into=('MWj/t','Jours'),statut='f',fr="Unite pour les irradiations"),
  Minimum              = SIMP (typ='R',defaut=0.,statut='f',fr="Irradiation du debut de calcul"),
  Maximum              = SIMP (typ='R',defaut=100000.,statut='f',fr="Irradiation maximum des calculs"),
  Evolution            = SIMP (typ='R',max='**',defaut=0.,statut='f',fr="Irradiations du calcul d'evolution"),
  Editions             = SIMP (typ='R',max='**',defaut=0.,statut='f',fr="Irradiations ou se font les editions"),
  ContreReactions      = SIMP (typ='R',max='**',statut='f',fr="Irradiations ou se font les calculs de reprise de contre-reactions"),
  ReprisesGs           = SIMP (typ='R',max='**',statut='f',fr="Irradiations ou se font les calculs de reprise GS EDF"),
  ReprisesBeta         = SIMP (typ='R',max='**',statut='f',fr="Irradiations ou se font les calculs de reprise BETA EDF"),
  Reprises             = SIMP (typ='R',max='**',statut='f',fr="Irradiations ou se font les calculs de reprise"),
  Refroidissement      = FACT (
                         Instants = SIMP (typ='R',max='**',fr="Irradiations de debut de refroidissement du combustible"),
                         Jours    = SIMP (typ=('R','I'),max='**',fr="Nombre de jours de refroidissement correspondant aux instants de refroidissement")),
  InsertionGrappe      = NUPL (max='**',statut='f',elements=(
                                SIMP (typ='TXM',fr="Type de grappe inseree"),
                                SIMP (typ=('R','I'), min=2,max=2,fr="Irradiations de Debut et Fin d'insertion de la grappe"),
                                SIMP (typ='R',fr="Cote axiale de la limite inferieure de la grappe inseree"))) ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe CONDITIONS_FONCTIONNEMENT : Classe de definition des conditions de fonctionnement Reacteur pour une campagne donnee
#                               
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONDITIONS_FONCTIONNEMENT_MOYENNES = OPER (nom="CONDITIONS_FONCTIONNEMENT_MOYENNES",op=0,sd_prod=ConditionsFonctionnementMoyennes,

  fr                          = "Definition des conditions de fonctionnement pour une campagne donnee",
  ang = "Definition of a campaign operating conditions ",
  IdentificateurCampagne      = SIMP (typ='TXM',statut='f',fr="Identificateur de la campagne"),
  PuissanceElectriqueMW       = SIMP (typ='R',statut='o',defaut=900.,fr="Puissance electrique du reacteur en MW"),
  PuissanceThermiqueMWth      = SIMP (typ='R',statut='o',defaut=2775.,fr="Puissance thermique du reacteur en MWth"),
  PressionPrimaireEntreeBar   = SIMP (typ='R',statut='o',defaut=155.1,fr="Pression du moderateur en bars a l'entree du coeur actif"),
  PressionPrimaireSortieBar   = SIMP (typ='R',statut='o',defaut=155.1,fr="Pression du moderateur en bars en sortie du coeur actif"),
  TitreMoyenBorePpm           = SIMP (typ='R',statut='o',defaut=500.,fr="Titre moyen en ppm en bore dans le moderateur"),
  TmodEntreePnulleC           = SIMP (typ='R',statut='o',defaut=286.0,fr="Temperature en C du moderateur a puissance nulle a l'entree du coeur"),
  TmodEntreePnomC             = SIMP (typ='R',statut='o',defaut=286.4,fr="Temperature en C du moderateur a puissance nominale a l'entree du coeur"),
  DeltaTmodEntreeSortiePnomC  = SIMP (typ='R',statut='o',defaut=39.0,fr="Ecart en C de temperature entre entree et sortie du coeur a puissance nominale"),
  TmodMoyenneCoeurPnomC       = SIMP (typ='R',statut='o',defaut=305.3,fr="Temperature moyenne en C du moderateur dans le coeur actif"),
  TmodMoyenneCuvePnomC        = SIMP (typ='R',statut='f',defaut=305.0,fr="Temperature moyenne en C du moderateur dans la cuve"),
  TcomMoyennePnomC            = SIMP (typ='R',statut='f',defaut=600.0,fr="Temperature moyenne en C du combustible dans le coeur"),
  TmodMoyenneReflecteurPnomC  = SIMP (typ='R',statut='f',defaut=296.0,fr="Temperature moyenne en C du reflecteur radial"),
  PositionGrappeHaute         = SIMP (typ='I',statut='f',defaut=225,fr="Position haute des grappes, en nombre de pas extraits"),
  DebitPrimaireConceptionM3_h = SIMP (typ='R',statut='f',defaut=70500.,fr="Debit primaire de conception dans le coeur en m3/h"),
  ProportionDebitCoeurCuve    = SIMP (typ='R',statut='f',defaut=0.97,fr="Rapport du debit coeur / debit cuve"),
  NbTubesGVBouches            = SIMP (typ='I',statut='f',defaut=0,fr="Nombre de tubes GV bouches"),
  SectionEcoulementCoeur      = SIMP (typ='R',statut='f',defaut=3.87,fr="Section d'ecoulement du moderateur dans le coeur en m2")
 ) ; # Fin CONDITIONS_FONCTIONNEMENT
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe PLAN_CHARGEMENT_COEUR : Classe de definition du plan de chargement combustible d'un coeur pour une campagne donnee                               
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#PLAN_CHARGEMENT_COEUR = OPER (nom="PLAN_CHARGEMENT_COEUR",op=0,sd_prod=PlanChargementCoeur,
#
#  fr                     = "Definition du plan de chargement combustible d'un coeur",
#  ang = "Definition of a fuel loading core map ",
#  IdentificateurCampagne = SIMP (typ='TXM',statut='o'),
#  TypePlan               = SIMP (typ='TXM',into=('STD','FR','FF','FFG'), statut='f'),
#  AssemblagePosition     = NUPL (
#      max      = '**',
#      elements = (      SIMP (typ=AssemblageCombustibleCharge,fr="Identificateur de l'assemblage"),
#                        SIMP (typ='TXM',statut='f',fr="Repere alphanumerique de la Position dans le coeur"),
#                        SIMP (typ='I',min=2,max=2,statut='f',fr="Coordonnees ij dans le plan radial du reseau du coeur")))
# );
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DATES_CLES_CAMPAGNE : Classe de definition des dates cles d'une campagne et de sa longueur
#                               
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DATES_CLES_CAMPAGNE = OPER (nom="DATES_CLES_CAMPAGNE",op=0,sd_prod=DateClesCampagne,

  fr                                  = "Definition des dates cles d'une campagne et de sa longueur",
  ang = "Definition of the campaign dates and length",
  IdentificateurCampagne              = SIMP (typ='TXM',statut='o',defaut='CZ101'),
  DateDDC                             = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A de debut de campagne"),
  DatePnom                            = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A d'atteinte de la puissance nominale"),
  DateFDC                             = SIMP (typ='I',min=3,max=3,statut='o',fr="Date J M A de fin de campagne"),
  LongueurNaturelleTheoriqueMWj_t     = SIMP (typ='R',statut='f',fr="Longueur naturelle theorique calculee de la campagne en MWj/t"),
  LongueurNaturelleRecaleeMWj_t       = SIMP (typ='R',statut='f',fr="Longueur naturelle recalee calculee de la campagne en MWj/t"),
  LongueurNaturelleExperimentaleMWj_t = SIMP (typ='R',statut='f',fr="Longueur naturelle mesuree de la campagne en MWj/t"),
  LongueurAnticipationJepp            = SIMP (typ='R',statut='f',fr="Nombre de JEPP d'anticipation"),
  LongueurProlongationJepp            = SIMP (typ='R',statut='f',fr="Nombre de JEPP de prolongation"),
  LongueurTotaleExperimentaleMWj_t    = SIMP (typ='R',statut='f',fr="Longueur totale de la campagne en MWj/t") ) ;
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe OPTIONS_CODES :      Classe de definition des options generales et du type de calcul demande
#                               
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONS_CODES = OPER (nom="OPTIONS_CODES",op=0,sd_prod=OptionsCodes,
  fr                 = "Definition des options des codes de calcul",
  ang = "Definition of calculation code options",
# TypeCalcul         = SIMP (typ='TXM',defaut='Evolution',statut='f'),
# CodeCalcul         = SIMP (typ='TXM',defaut='SUNSET',statut='f'),
# ConditionLimite    = SIMP (typ=ConditionLimiteGenerale,statut='o'),
  OptionsCodeReseau  = FACT (
      OptionMulticellule        = SIMP (typ='TXM',defaut='ROTH',statut='f',into=('ROTH','MULTICELLULE'),fr="Option du calcul multicellule"),
      OptionPij                 = SIMP (typ='TXM',defaut='&UP0 &ROTH',statut='f',into=('&UP0 &ROTH','&UP0 &HETE','&UP1 &HETE'),fr="Option du calcul des Pij"),
      ParametresIntegration     = SIMP (typ='TXM',defaut='MAIL_INT 7 7 7 7',statut='f',fr="Donnees du maillage d'integration en heterogene"),
      ProportionNoyauxParDefaut = SIMP (typ='R',defaut=1.E-12,statut='f',fr="Valeur initiale des concentrations des noyaux lourds non definis"),
      OptionLaplacienB2         = SIMP (typ='TXM',defaut='CRITIQUE',statut='f',into=('CRITIQUE','NUL','IMPOSE'),fr="Option du calcul des fuites homogenes"),
      LaplacienB2               = SIMP (typ='R',defaut=0.,statut='f',fr="Valeur initiale du laplacien du calcul des fuites"),
      OrdreAnisotropie          = SIMP (typ='I',defaut=1,statut='f',fr="Ordre d'anisotropie des sections de transfert"),
      Autoprotection            = SIMP (typ='TXM',defaut='Oui',statut='f',into=('Oui','Non'),fr="Calcul d'autoprotection ou non"),
      DonneesAutoprotection     = SIMP (typ=OptionsAutoprotection,statut='f',max='**',fr="Nom des objets decrivant les isotopes a autoproteger et les options associees"),
      RecalculAutoprotection    = SIMP (typ='TXM',defaut='Oui',statut='f',into=('Oui','Non'),fr="Demande ou non de recalcul de l'autoprotection"),
      Equivalence               = SIMP (typ='TXM',defaut='Non',statut='f',into=('Oui','Non'),fr="Demande ou non de calcul d'equivalence"),
      NbGroupesEquivalence      = SIMP (typ='I',max='**',defaut=(2,6,16),statut='f',fr="Liste des nombres de groupes des calculs d'quivalence"),
      EditionAssemblage         = SIMP (typ='TXM',defaut='Oui',statut='f',into=('Oui','Non'),fr="Demande d'edition des sections efficaces homogeneisees sur l'ensemble du domaine"),
      EditionCellule            = SIMP (typ='TXM',defaut='Oui',statut='f',into=('Oui','Non'),fr="Demande d'edition des sections efficaces homogeneisees par cellule"),
      EditionFluxDetaille       = SIMP (typ='TXM',defaut='Oui',statut='f',into=('Oui','Non'),fr="Demande d'edition des flux moyens sur l'ensemble du domaine sur la maillage multigroupe detaille"),
      EditionMilieu             = SIMP (typ='TXM',defaut='Oui',statut='f',into=('Oui','Non'),fr="Demande d'edition des compositions isotopiques detaillees sur tous les milieux de calcul"),
      EditionTrimaran           = SIMP (typ='TXM',defaut='Non',statut='f',into=('Oui','Non'),fr="Demande d'edition des sections efficaces pour TRIPOLI multigroupe"),
      SpectreNeutrons           = SIMP (typ='TXM',defaut='Prompt',statut='f',into=('Prompt','Retarde'),fr="Type de spectre de neutrons pour le calcul de transport"),
      ListeIsotopesEdites       = SIMP (typ='TXM',statut='f',max='**',fr="Liste des initiales des symboles des isotopes a editer"),
      FichierBickley            = SIMP (typ='TXM',statut='f',fr="Nom du fichier des fonctions Bickley"),
      EditionIsotopeHomogene    = SIMP (typ='TXM',defaut='Non',statut='f',into=('Oui','Non'),fr="Demande d'edition de constitution d'isotopes homogeneises sous forme APOLLIB"),
      RepertoireHomoge          = SIMP (typ='TXM',statut='f',fr="Nom du repertoire du fichier des isotopes homogenes sous forme APOLLIB"),
      FichierHomoge             = SIMP (typ='TXM',statut='f',fr="Nom du fichier des isotopes homogenes sous forme APOLLIB"),
      ExecutableAPOLLO          = NUPL (
          elements = ( SIMP (typ='TXM',fr="Systeme d'exploitation"),SIMP (typ='TXM',fr="Nom du fichier executable")),
          statut   = 'f'),
      ProceduresApollo2         = FACT (
                OptionsListing  = SIMP (typ='TXM',statut='f'),
                Evolution       = SIMP (typ='TXM',statut='f'),
                Reprise         = SIMP (typ='TXM',statut='f'),
                Equivalence     = SIMP (typ='TXM',statut='f'),
                EditionCellule  = SIMP (typ='TXM',statut='f'),
                EditionHomoge   = SIMP (typ='TXM',statut='f')),
      ProceduresSunset          = FACT (
                Evolution       = SIMP (typ='TXM',statut='f'),
                Reprise         = SIMP (typ='TXM',statut='f'),
                Equivalence     = SIMP (typ='TXM',statut='f'),
                EditionCellule  = SIMP (typ='TXM',statut='f'),
                EditionHomoge   = SIMP (typ='TXM',statut='f'))),
# --------------------------------------------------------------
  OptionsCodeCoeur  = FACT (
      ReactiviteVisee = SIMP (typ='R',defaut=0.,statut='f',fr="Valeur en pcm de la reactivite visee en calcul critique"),
      EfficaciteBoreEstimee = SIMP (typ='R',defaut=-6.,statut='f',fr="Valeur estimee en pcm/ppm de l'efficacite du bore"),
      TitreBoreInitiale = SIMP (typ='R',defaut=600.,statut='f',fr="Valeur estimee en ppm du titre en bore du moderateur"),
      ApproximationTransport = SIMP (typ='TXM',defaut='SPn',statut='f',into=('SPn','Sn')),
      BlocSPn	= BLOC (condition = "ApproximationTransport=='SPn'",
                        OrdreApproximation = SIMP (typ='I',defaut=1,statut='f',fr="Ordre n impair de la methode SPn"),
                        ElementFini	   = SIMP (typ='TXM',defaut='RTN0',statut='f',into=('RTN0','RTN1'),fr="Type d'element fini"),
                        MaxIterationsDiffusion = SIMP (typ='I',defaut=1,into=(1,2,3,4,5),statut='f',fr="Nombre maximal d'iterations de diffusion")),
      BlocSn	= BLOC (condition = "ApproximationTransport=='Sn'",
                        OrdreApproximation = SIMP (typ='I',defaut=4,statut='f',fr="Ordre n pair de la methode Sn"),
                        ElementFini	   = SIMP (typ='TXM',defaut='RTN',statut='f',into=('RTN','BDM'),fr="Type d'element fini"),
                        Acceleration	   = SIMP (typ='TXM',defaut='Oui',statut='f',into=('Oui','Non'),fr="Acceleration par la diffusion"),
                        MaxIterationsDiffusion = SIMP (typ='I',defaut=20,statut='f',fr="Nombre maximal d'iterations de calcul de diffusion") ),
      PrecisionValeurPropre = SIMP (typ='R',defaut=1.E-5,statut='f',fr="Precision sur la valeur propre"),
      PrecisionFlux = SIMP (typ='R',defaut=1.E-3,statut='f',fr="Precision sur le flux"),
      PrecisionResolutionMultigroupe = SIMP (typ='R',defaut=1.E-6,statut='f',fr="Precision de la resolution multigroupe"),
      PrecisionIterationTermeDiffusion = SIMP (typ='R',defaut=1.E-6,statut='f',fr="Precision des iterations sur le terme de diffusion"),
      MaxIterationsEnEnergie = SIMP (typ='I',defaut=1,statut='f',fr="Nombre maximal d'iterations pour la resolution Gauss Seidel en energie"),
      MaxIterationsTermeDiffusion = SIMP (typ='I',defaut=1,statut='f',fr="Nombre maximal d'iterations sur le terme de diffusion"),
      MaxIterationsDecompositionDomaine = SIMP (typ='I',defaut=1,statut='f',fr="Nombre d'iterations de decomposition de domaine"),
      MaxIterationsKeffAvantCR = SIMP (typ='I',defaut=1,statut='f',fr="Nombre de calculs de keff avant appel aux contre-reactions"),
      GestionAutomatiquePasCinetique = SIMP (typ='TXM',defaut='Oui',into=('Oui','Non'),statut='f',fr="Gestion automatique du pas de temps du calcul cinetique"),
      PrecisionIterationsFluxPrecurseurs = SIMP (typ='R',defaut=1.E-6,statut='f',fr="Precision sur les iterations Flux Precurseurs"),
      PrecisionParametreGestionAutomatique = SIMP (typ='R',defaut=0.0008,statut='f',fr="Precision sur les iterations Flux Precurseurs"),
      MaxIterationsFluxPrecurseurs = SIMP (typ='I',defaut=50,statut='f',fr="Nombre maximal d'iterations Flux Precurseurs"),
      ThetaSchemaCinetique = SIMP (typ='R',defaut=0.5,statut='f',fr="Valeur du parametre theta du schema cinetique") ),
#  ------------------------------------------------------------------------------------------------------------------------------------
   OptionsThermiqueThermohydraulique = FACT (
       CoefficientEchangeGaineFluide = SIMP (typ='TXM',defaut='DITTUS_BOELTER',into=('FLICA','DITTUS_BOELTER'),statut='f',
                                             fr="Option du Coefficient d'échange gaine-fluide (flux < au flux critique)"),
       CoefficientEchangeGaineFluideEbullition = SIMP (typ='TXM',defaut='BST',into=('BST','TONG'),statut='f',
                                                       fr="Option du Coefficient d'échange gaine-fluide (Ebullition en film)"),
       CoefficientEchangeJeuPastilleGaineConstantTransitoire = SIMP (typ='TXM',defaut='Non',into=('Non','Oui'),statut='f',
                                                                     fr="Option de constance des coefficients d'échange gap"),
       CoefficientEchangeJeuPastilleGaine = SIMP (typ='TXM',defaut='HGAP_88',into=('EJECTION','TUO2','PLIN_BU','FIXE','HGAP_88'),statut='f',
                                                       fr="Option du Coefficient d'échange du jeu pastille-gaine"),
       BlocHgapTuo2	= BLOC (condition = "CoefficientEchangeJeuPastilleGaine=='TUO2'",
                                 Tuo2Initiale = SIMP (typ='R',statut='o',
                                                      fr="Température initiale combustible pour le calcul du coefficient d'échange") ),
       BlocHgapFixe	= BLOC (condition = "CoefficientEchangeJeuPastilleGaine=='FIXE'",
                                 Hgap = SIMP (typ='R',statut='o',defaut=5850.,fr="Valeur imposée du coefficient d'échange") ),
       ConductiviteCombustible = SIMP (typ='TXM',defaut='HGAP_88',into=('STORA','WESTINGHOUSE','HGAP_88','COMETHE'),statut='f',
                                                       fr="Option du Coefficient de conductivité du combustible"),
       CapaciteCalorifiqueCombustible = SIMP (typ='TXM',defaut='UO2_FRAMATOME',into=('UO2_BATES','UO2_FRAMATOME','UO2_THYC'),statut='f',
                                                       fr="Option du Coefficient de conductivité du combustible"),
       MateriauGaine = SIMP (typ='TXM',defaut='ZIRCALOY_CYRANO',into=('ZIRCALOY_CYRANO', 'ZIRCALOY_THYC', 'INCOLOY_800',
 								     'CHROMESCO_3', 'INOX_16', 'INOX_321', 'INOX_347', 'INOX_347_OXYDE',
 								     'INCONEL_600', 'NICKEL_75', 'PLATINE'),statut='f',
 			    fr="Materiau de la gaine pour le calcul du roCp de la gaine et de sa conductivite"),
       FluxCritique = SIMP (typ='R',defaut=180.E4,fr="Valeur du flux critique en W/m2"),
       FractionPuissanceCombustible = SIMP (typ='R',defaut=0.974,fr="Fraction de la puissance degagee dans le combustible"),
       Creusement = SIMP (typ='TXM',defaut='Uniforme',statut='f',into=('Uniforme','Runnals','Framatome','Twinkle','Mox','EDF','Specifique')),
       BlocCreusement	= BLOC (condition = "Creusement=='Specifique'", 
                           RayonsCreusement = SIMP (typ='R',statut='o',fr="Rayons de definition du creusement de puissance (nz)"),
                           IrradiationsCreusement = SIMP (typ='R',statut='o',fr="Irradiations de definition du creusement de puissance (nbu)"),
                           EnrichissementsCreusement = SIMP (typ='R',statut='o',fr="Enrichissements de definition du creusement de puissance (nen)"),
                           PuissancesUO2 = SIMP (typ='R',max='**',statut='f',fr="Valeurs des creusements de puissance P(nz,nbu,nen) dans une pastille UO2"),
                           PuissancesMOX = SIMP (typ='R',statut='f',fr="Valeurs des creusements de puissance P(nz,nbu,nen) dans une pastille MOX") ),
       DiscretisationPastilleCombustible = SIMP (typ='I',defaut=4,statut='f',fr="Nombre de points de discretisation radiale de la pastille combustible"),
       DiscretisationGaine = SIMP (typ='I',defaut=2,statut='f',fr="Nombre de points de discretisation radiale de la gaine de la pastille combustible"),
       PrecisionCalculThermique = SIMP (typ='R',defaut=0.1,fr="Precision en Celsius du calcul thermique radiale du crayon"),
       PrecisionCalculThermohydraulique = SIMP (typ='R',defaut=0.01,fr="Precision en Celsius du calcul thermohydraulique de la temperature du moderateur"),
       MaxIterationsThermique = SIMP (typ='I',defaut=100,statut='f',fr="Nombre maximum d'iterations du calcul de thermique"),
       MaxIterationsThermohydraulique = SIMP (typ='I',defaut=100,statut='f',fr="Nombre maximum d'iterations du calcul de thermohydraulique"),
       MethodeIntegrationThermohydraulique = SIMP (typ='TXM',defaut='Gauss',statut='f',into=('Gauss','NonGauss'),fr="Methode d'integration thermohydraulique"),
       PerteDeCharge = SIMP (typ='TXM',defaut='Non',statut='f',into=('Non','Oui'),fr="Prise en compte ou non de la perte de charge axiale"),
       TableEau = SIMP (typ='TXM',defaut='Thetis',statut='f',into=('Thetis','Interne'),
                        fr="Calcul des caracteristiques du moderateur par THETIS ou par des tables internes") ),
#  ----------------------------------------------------------------------------------------------------------------------------------
   OptionsContreReactions = FACT (
       ContreReactions = SIMP (typ='TXM',defaut='Oui',into=('Oui','Non'),fr="Prise en compte des contre-reactions ou non"),
       PrecisionPuissance = SIMP (typ='R',defaut=1.E-4,fr="Precision sur la puissance a la fin des iterations de contre-reactions"),
       PrecisionKeff = SIMP (typ='R',defaut=1.E-5,fr="Precision sur keff a la fin des iterations de contre-reactions"),
       MethodeCalculSection = SIMP (typ='TXM',defaut='Spline1D',into=('Spline1D','SplinenD','Tabulation'),
                                    fr="Methode de calcul des sections efficaces avec Contre-reactions") )
 ) ; # Fin OPTIONS_CODES
# -----------------------------------------------------------------------------------------------------------------------------------
#  Classe DONNEES_GENERALES_ETUDE :     Classe de definition des caracteristiques globales de l'etude
#                                       Definition de la centrale (site, numero de tranche) et numero de campagne d'irradiation
#                                       Ces caracteristiques  d'environnement de l'etude doivent permettre de recuperer l'ensemble 
#                                       des parametres de fonctionnement nominales du reacteur sujet de l'etude (creation de
#                                       bibliotheques ou calcul de coeur)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DONNEES_GENERALES_ETUDE = OPER (nom="DONNEES_GENERALES_ETUDE",op=0,sd_prod=DonneesGeneralesEtude,

  fr                     = "Definition de la centrale sujet de l'etude et des options globales de l'etude",
  ang = "Definition of the power plant and of the global options",
  TypeCode		 = SIMP (typ='TXM',defaut='Reseau',into=('Reseau','Coeur'),statut='o'),
  SiteNucleaire          = SIMP (typ=SiteNucleaire,defaut='TRICASTIN',statut='o'),
  BlocCoeur              = BLOC (condition = "TypeCode=='Coeur'",
                           NumeroTranche          = SIMP (typ='I',defaut=1,statut='f'),
                           NumeroCampagne         = SIMP (typ='I',defaut=1,statut='f'),
                           IdentificateurCampagne = SIMP (typ='TXM',defaut='TN101',statut='f'),
                           DatesCampagne          = SIMP (typ=DateClesCampagne,statut='f'),
                           TypeGestion            = SIMP (typ    = 'TXM',
                                                          defaut = '370Q',
                                                          statut = 'f',
                                                          into   = ('310Q','310T','325T','325Q','340Q','345AL',
                                                                    '370Q','370T','400T','HMOX','MOXNT','TMOX')),
                           TypeSchemaGrappe       = SIMP (typ    = 'TXM',
                                                          defaut = '900CPYUO2',
                                                          statut = 'f',
                                                          into   = ('900CP0','900CPYUO2INITIAL','900CPYUO2',
                                                                    '900CPYUO2AL','900CPYMOX','1300','N4')),
                           PositionGrappe        = SIMP (typ=PositionGrappesCommande,statut='f'),
                           TypeEvaluationSurete  = SIMP (typ='TXM',defaut='900STD',statut='f',
                                                         into=('900STD','900GARANCE','1300STD','1300GEMMES','N4STD')),
                           ModePilotage          = SIMP (typ='TXM',defaut='G',statut='f',into=('A','G','X')),
                           PlanChargement        = SIMP (typ=Reseau,statut='f'),
                           CodeCalcul            = SIMP (typ='TXM',defaut='SNCODE',statut='f')),
  BlocReseau            = BLOC (condition = "TypeCode=='Reseau'",
                           Assemblage            = SIMP (typ=AssemblageType,statut='f'),
                           ContreReactions       = SIMP (typ=EspaceVariations,statut='f'),
                           CodeCalcul            = SIMP (typ='TXM',defaut='SUNSET',statut='f')),
  ConditionsMoyennes    = SIMP (typ=ConditionsFonctionnementMoyennes,statut='f'),
  Options               = SIMP (typ=OptionsCodes,statut='f'),
  PasIrradiation        = SIMP (typ=DonneesEvolutionIrradiation,statut='f'),
# ConditionLimite       = SIMP (typ=ConditionLimiteGenerale,statut='o'),
  TypeCalcul            = SIMP (typ='TXM',max='**',defaut='Evolution',
                                into=('Evolution','EvolutionMicroscopique','Reprise','Statique','Cinetique',
                                      'BoreImpose','BoreCritique'),statut='f')
 ) ;
 
class resultat(TObjet): pass
class resultat2(resultat): pass

CALCUL=OPER(nom="CALCUL",op=10,sd_prod=resultat,
             materiau=SIMP(typ=Materiau),
            PRESSION=SIMP(defaut=10000.,typ="R")
	    );

CALCUL2=OPER(nom="CALCUL2",op=11,sd_prod=resultat2,
             donnee=SIMP(typ=resultat),
             materiau=SIMP(typ=Materiau),
            );

 
 
 
