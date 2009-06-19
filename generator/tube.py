
# ==========
# PARAMETRES
# ==========

# methode de filling: par les generatrices ou par des ecailles de tortue

# Longueur
longueur_tube = 6363.655

# Facteur d'amplification pour voir si le filling passe bien par les generatrices
amplification_factor = 1

# teste si le maillage gibi passe par tous les points
test_gibi = False
maillage_gibi = '/home/PROJETS/OUVERT/edf_anode/from_edf/2008_11_28/Tube/tube.mail.med'

# MAILLAGE
# ========

type_maillage = "regle" # "regle" ou "libre"

if type_maillage == "libre":
     type_algo = "NETGEN_2D" # "BLSURF" ou "NETGEN_2D"

if methode == "generatrices":
    # nombre de segments dans la longueur des generatrices dans la zone de sous-epaisseur
    nb_seg_generatrices = 150 # methode generatrices
else:
    # nombre de segments dans la longueur des generatrices dans la zone de sous-epaisseur
    nb_seg_generatrices = 5 # methode tortue
    # distance entre 2 abscisses de points de mesure au dessous de laquelle on discretise avec nb_seg_petites_distances
    # au lieu de nb_seg_generatrices
    petite_distance = 100
    nb_seg_petites_distances = 3

# nombre de segments dans l'epaisseur du tube
nb_seg_ep= 3

# nombre de segments dans l'arc du tube entre 2 generatrices
if methode == "generatrices":
    nb_seg_arc = 20 # methode generatrices: partition en 2
else:
    nb_seg_arc = 5 # methode tortue: partition en 8

# nombre de segments dans la longueur de transition
nb_seg_transition = 4

# nombre de segments dans la longueur d'amortissement
nb_seg_amortissement = 11

# ===========

import salome
from geompy import *
import smesh

import os, csv, math, pdb, time

# DEBUT DES FONCTIONS
# ===================================================

# supprime recursivement un element dans une liste
# @exemple : 
#    l=["a", " ", "b", " ", "c"]
#    l = recursive_remove(l, " ")
#    print l
# => ["a", "b", "c"]
def recursive_remove(l, txt):
    finished = 0
    while not finished:
        try:
            l.remove(txt)
        except ValueError:
            finished = 1
    return l


## lit les valeurs des epaisseurs sur les generatrices a partir d'un fichier csv
# @return d_generatrices : dictionnaire dont la cle est le nom de la generatrice et la valeur est la liste des epaisseur sur cette generatrice
# @return l_abscisses: liste des abscisses des points de mesures
def read_generatrice(filename):
    file = open(filename, "rb")

    reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONE)
    
    # Dictionnaire pour stocker les mesures sur une generatrice donnee
    d_generatrices = {}
    
    # Liste des noms des generatrices
    l_noms_generatrices = []
    
    # Liste des abscisses des points de mesures
    l_abscisses = []
    
    for i, row in enumerate(reader):
        # On supprime les cases vides
        row = recursive_remove(row, "")
        # Sur la premiere ligne, on releve les noms des generatrices
        if i==0:
            for nom in row:
                if nom not in ["Abscisse", "Longueur"]:
                    # on initialise chaque generatrice avec une liste vide
                    d_generatrices[nom] = []
                    l_noms_generatrices.append(nom)
            # nombre de generatrices trouvees:
            nb_generatrices = len(d_generatrices)
        else:
            # sur les lignes suivantes, on releve les mesures des epaisseurs
            for j, nom_generatrice in enumerate(l_noms_generatrices):
                # la liste des epaisseurs commence a 1
                epaisseur_str_fr = row[j+1]
                # on convertit le format decimal francais par le format anglais
                epaisseur_str = epaisseur_str_fr.replace(",", ".")
                epaisseur = float(epaisseur_str)
                d_generatrices[nom_generatrice].append(epaisseur)
            # on ajoute la valeur de l'abscisse
            abscisse_str = row[nb_generatrices+1]
            abscisse = float(abscisse_str)
            l_abscisses.append(abscisse)
    
    file.close()
    
    return d_generatrices, l_noms_generatrices, l_abscisses

## lit les valeurs des angles definissant les generatrices a partir d'un fichier csv
# @return l_angles : liste des angles definissant les generatrices
def read_angles(filename):
    file = open(filename, "rb")

    reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONE)
    
    # Liste des angles des generatrices
    l_angles = []
    
    for row in reader:
        # On supprime les cases vides
        row = recursive_remove(row, "")
        
        # si la ligne comporte 3 valeurs, on peut lire les angles
        if len(row) == 3:
            angle_str = row[2]
            angle = float(angle_str)
            l_angles.append(angle)
    return l_angles

## Cree une face a partir d'un nuage de points
# @param l_arcs_points : liste de points sur un contour
# @param closed_wire: flag pour savoir si le contour est deja ferme ou s'il faut le fermer
# @return face : une face passant par tous les points
# @warning: TODO: completer l'algo pour qu'il fonctionne si le nombre de generatrices est impair!!!
def MakeShellFromPoints(l_arcs_points, closed_wire = False):
    # on cree les arcs pour chaque quart de cercle
    nb_generatrices = len(l_arcs_points[0])
    nb_arcs_filling = nb_generatrices/2
    l_arcs_filling = [[] for i in range(nb_arcs_filling)]
    if closed_wire:
        if nb_generatrices%2 != 1:
            raise "L'algo ne fonctionne pour l'instant qu'avec un nombre de generatrices impair"
    else:
        if nb_generatrices%2 != 0:
            raise "L'algo ne fonctionne pour l'instant qu'avec un nombre de generatrices pair"
    # Creation des arcs a partir des points
    for arc_points in l_arcs_points:
        if not closed_wire:
            # Pour cloturer le contour
            arc_points.append(arc_points[0])
        for i in range(nb_arcs_filling):
            # 3 points a la meme abscisse sur 3 generatrices consecutives
            arc = MakeArc(arc_points[2*i], arc_points[1+2*i], arc_points[2+2*i])
            l_arcs_filling[i].append(arc)
    
    
    # on fait un filling pour tous les 1ers arcs, tous les 2emes arcs, ... jusqu'au 4e arc
    l_faces_filling = []
    for i, arc_filling in enumerate(l_arcs_filling):
        # On fait un filling entre 2 quarts de cercles
        for j in range(0, len(arc_filling) - 1):
            l_quart_arc = [arc_filling[j], arc_filling[j+1]]
            compound_quart_arcs = MakeCompound(l_quart_arc)
            quart_face_filling = MakeFilling(compound_quart_arcs, 0, 10, 1e-05, 1e-05, 0)
            #addToStudy(quart_face_filling, "quart_face_filling_%i"%(j+1))
            l_faces_filling.append(quart_face_filling)
    face = MakeShell(l_faces_filling)
    return face

## Cree une face a partir d'un nuage de points par un filling sur les generatrices
# @param l_arcs_points : liste de points sur un contour
# @param closed_wire: flag pour savoir si le contour est deja ferme ou s'il faut le fermer
# @return face : une face passant par tous les points
def MakeFillingFromPoints(l_arcs_points, closed_wire = False):
    nb_generatrices = len(l_arcs_points[0])
    l_points_generatrices = [[] for i in range(nb_generatrices)]
    l_generatrices = []
    # Creation des generatrices a partir des points
    for arc_points in l_arcs_points:
        for i, point in enumerate(arc_points):
            # on ajoute le point dans la generatrice correspondante
            l_points_generatrices[i].append(point)
    for points_generatrice in l_points_generatrices:
        generatrice_i = MakeInterpol(points_generatrice)
        l_generatrices.append(generatrice_i)
    if not closed_wire:
        # Pour cloturer le contour
        l_generatrices.append(l_generatrices[0])
    compound_generatrices = MakeCompound(l_generatrices)
    face = MakeFilling(compound_generatrices, 0, 10, 1e-05, 1e-05, 0)
    return face


# FIN DES FONCTIONS
# ===============================================

time0 = time.time()

# lecture des mesures dans le fichier csv
mesures_filename = os.path.join(dir_name, "mesure-transposee.csv")
d_generatrices, l_noms_generatrices, l_abscisses = read_generatrice(mesures_filename)

# lecture des angles dans le fichier csv
angles_filename = os.path.join(dir_name, "mesure-angles.csv")
l_angles = read_angles(angles_filename)

# dictionnaire indiquant les angles en fonction du nom de la generatrice
d_angles = {}
for nom, angle in zip(l_noms_generatrices, l_angles):
    d_angles[nom] = angle

time1 = time.time()

print "Temps de lecture des fichiers: %.1f s."%(time1-time0)

# Rq: pour conserver le point de plus faible epaisseur, il faut que la couture de la face de filling
# se situe sur la generatrice ou se situe ce point

# Points et vecteurs de base

P0 = MakeVertex(0, 0, 0)

Vx = MakeVectorDXDYDZ(1000, 0, 0)
Vy = MakeVectorDXDYDZ(0, 1000, 0)
Vz = MakeVectorDXDYDZ(0, 0, 1)
plane_size = longueur_tube * 10

P_ext = MakeVertex(0, r_ext, 0)
cercle_ext = MakeRevolution(P_ext, Vx, 2*math.pi)
face_ext_milieu = MakePrismVecH(cercle_ext, Vx, l_abscisses[-1])
addToStudy(face_ext_milieu, "face_ext_milieu")

# initialisation de l'epaisseur minimale pour l'algo de recherche de l'epaisseur minimale
ep_min = r_ext
# initialisation de la liste de generatrices
l_generatrices = []
# initialisation de la double liste d'arcs
l_arcs_points = [[] for abscisse in l_abscisses]
angle = 0
# angle de la generatrice ou se situe l'epaisseur minimale
angle_ep_mini = 0
# Point ou se situe l'epaisseur minimale
P_ep_mini = None
# indice de la generatrice ou se situe le point d'epaisseur minimale
i_generatrice_ep_mini = None
# Creation des generatrices
for i, nom_generatrice in enumerate(l_noms_generatrices):
    angle += d_angles[nom_generatrice]
    l_ep = d_generatrices[nom_generatrice]
    l_points_ep = []
    j = 0
    for ep, abscisse in zip(l_ep, l_abscisses):
        P_generatrice_tmp = MakeVertex(abscisse, r_ext - ep*amplification_factor, 0)
        P_generatrice = MakeRotation(P_generatrice_tmp, Vx, math.radians(angle))
        #addToStudy(P_generatrice, "P_generatrice_%i"%(i+1))
        # pour la methode par les generatrices
        l_points_ep.append(P_generatrice)
        # pour la methode par les arcs
        l_arcs_points[j].append(P_generatrice)
        # Test sur l'epaisseur minimale
        if ep < ep_min:
            ep_min = ep
            P_ep_mini = P_generatrice
            i_generatrice_ep_mini = i
            angle_ep_mini = angle
        j+=1
    # creation des generatrices
    generatrice = MakeInterpol(l_points_ep)
    addToStudy(generatrice, "Generatrice_%s"%nom_generatrice)
    l_generatrices.append(generatrice)

print "epaisseur minimale mesuree: ", ep_min
addToStudy(P_ep_mini, "P_ep_mini")

# On cree un objet contenant tous les points pour voir si la face generee passe par tous les points
l_points = []
for arcs_points in l_arcs_points:
    l_points += arcs_points
Tous_Points = MakeCompound(l_points)
addToStudy(Tous_Points, "Tous_Points")

# methode par les generatrices
# ============================

# Pour s'assurer de passer par le point d'epaisseur minimale,
# on decalle la generatrice de recollement de la face et on l'ajoute a la fin pour fermer la face
l_generatrices = l_generatrices[i_generatrice_ep_mini:] + l_generatrices[:i_generatrice_ep_mini] + [l_generatrices[i_generatrice_ep_mini]]
# Creation de la face
compound_generatrices = MakeCompound(l_generatrices)
addToStudy(compound_generatrices, "compound_generatrices")
min_compound_generatrices = MinDistance(face_ext_milieu, compound_generatrices)
print "epaisseur minimale entre les generatrices et la face exterieure: ", min_compound_generatrices
if methode == "generatrices":
    face_int_milieu_tmp = MakeFilling(compound_generatrices, 0, 10, 1e-05, 1e-05, 0)
    face_int_milieu = ChangeOrientation(face_int_milieu_tmp)
    addToStudy(face_int_milieu, "face_int_milieu")
    min_distance = MinDistance(face_ext_milieu, face_int_milieu)
    print "epaisseur minimale avec la methode generatrices: ", min_distance


# methode par les arcs avec filling arc par arc, 3 points par points (methode ecaille de tortue)
# ==================================================================

if methode != "generatrices":
    face_int_milieu = MakeShellFromPoints(l_arcs_points)
    addToStudy(face_int_milieu, "face_int_milieu")
    
    min_distance = MinDistance(face_ext_milieu, face_int_milieu)
    print "epaisseur minimale avec la methode ecaille de tortue: ", min_distance

# => La face suit a la fois les generatrices et les arcs. L'epaisseur minimale est respectee

# Partie complementaire de la face interieure du tube
# ===================================================

# calcul de la longueur d'amortissement a partir de la formule de U4.PC.10-D
r_moyen = r_ext - ep_nominale/2.
l_amor_1 = 3/2.*math.sqrt(r_moyen**3/ep_nominale)
l_amor_2 = 3*math.sqrt(r_moyen*ep_nominale)
longueur_amortissement = max(l_amor_1, l_amor_2)

print "longueur d'amortissement: ", longueur_amortissement

# Longueur de transition entre tube deformé et longueur d'amortissement
longueur_transition = longueur_amortissement/5.
print "longueur de transition: ", longueur_transition


# On cree un nuage de points definissant les contours de la face de transition
r_int = r_ext - ep_nominale*amplification_factor
l_faces = []
l_abscisses_transition = []
# boucle pour traiter en meme temps le prolongement en bas et en haut
for i_abscisse, coef_translation in zip([0, -1], [-1, 1]):
    l_arcs_points_transition = []
    
    # On cree les points sur le cercle de la face de transition, en vis-a-vis des points du premier cercle de la face int
    abscisse_transition = l_abscisses[i_abscisse] + coef_translation*longueur_transition
    l_abscisses_transition.append(abscisse_transition)
    l_arcs_points_transition_base = []
    angle = 0
    for nom_generatrice in l_noms_generatrices:
        angle += d_angles[nom_generatrice]
        P_transition_base_tmp = MakeVertex(abscisse_transition, r_int, 0)
        P_transition_base = MakeRotation(P_transition_base_tmp, Vx, math.radians(angle))
        l_arcs_points_transition_base.append(P_transition_base)
    
    # contour bas
    l_arcs_points_transition.append(l_arcs_points_transition_base)
    # contour haut
    l_arcs_points_transition.append(l_arcs_points[i_abscisse])
    if methode == "generatrices":
        face_transition = MakeFillingFromPoints(l_arcs_points_transition)
        if coef_translation == -1:
            face_transition = ChangeOrientation(face_transition)
    else:
        face_transition = MakeShellFromPoints(l_arcs_points_transition)
    addToStudy(face_transition, "face_transition")
    l_faces.append(face_transition)
    
    
    # On recupere le contour bas pour creer la face d'amortissement
    
    P_transition = MakeVertex(abscisse_transition, 0, 0)
    l_edge_transition = GetShapesOnPlaneWithLocation(face_transition, ShapeType["EDGE"], Vx, P_transition, GEOM.ST_ON)
    wire_bas_transition = MakeWire(l_edge_transition)
    face_amortissement = MakePrismVecH(wire_bas_transition, Vx, coef_translation*longueur_amortissement)
    addToStudy(face_amortissement, "face_amortissement")
    l_faces.append(face_amortissement)

l_faces.append(face_int_milieu)

if methode == "generatrices":
    face_int = MakeSewing(l_faces, 0.1)
else:
    face_int = MakeShell(l_faces)
addToStudy(face_int, "face_int")


# Creation du tube solide
# =======================

# Face exterieure

h_tube = l_abscisses[-1] - l_abscisses[0] + 2*(longueur_amortissement+longueur_transition)
abscisse_base_tube = l_abscisses[0]-(longueur_amortissement+longueur_transition)
cercle_ext_bas = MakeTranslation(cercle_ext, abscisse_base_tube, 0, 0)
face_ext_tmp = MakePrismVecH(cercle_ext_bas, Vx, h_tube)
# on tourne la face, pour ne pas avoir l'edge de couture
face_ext = MakeRotation(face_ext_tmp, Vx, math.radians(l_angles[0]))
#face_ext = face_ext_tmp
addToStudy(face_ext, "face_ext")

# Face bas
P_bas_ext = MakeTranslation(P_ext, abscisse_base_tube, 0, 0)
cercle_int_bas = CreateGroup(face_int, ShapeType["EDGE"])
l_cercle_int_bas = GetShapesOnPlaneWithLocation(face_int, ShapeType["EDGE"], Vx, P_bas_ext, GEOM.ST_ON)
UnionList(cercle_int_bas, l_cercle_int_bas)

face_bas = MakeFaceWires([cercle_ext_bas, cercle_int_bas], 1)
addToStudy(face_bas, "face_bas")

# Face haut
P_haut_ext = MakeTranslation(P_bas_ext, h_tube, 0, 0)
cercle_ext_haut = MakeTranslation(cercle_ext_bas, h_tube, 0, 0)
cercle_int_haut = CreateGroup(face_int, ShapeType["EDGE"])
l_cercle_int_haut = GetShapesOnPlaneWithLocation(face_int, ShapeType["EDGE"], Vx, P_haut_ext, GEOM.ST_ON)
UnionList(cercle_int_haut, l_cercle_int_haut)

face_haut = MakeFaceWires([cercle_ext_haut, cercle_int_haut], 1)
addToStudy(face_haut, "face_haut")

l_faces_tube = [face_int, face_ext, face_bas, face_haut]
shell_tube = MakeShell(l_faces_tube)
addToStudy(shell_tube, "shell_tube")

tube = MakeSolid([shell_tube])
addToStudy(tube, "tube")

time2 = time.time()

print "Temps de creation de la geometrie: %.1f s."%(time2-time1)

    
# Partition pour que le maillage passe par les points de mesure
# =============================================================

l_plans_abscisses = []


if methode == "generatrices":
    l_abscisses_plan = [l_abscisses_transition[0]] + [l_abscisses[0], l_abscisses[-1]] + [l_abscisses_transition[1]]
else:
    l_abscisses_plan = [l_abscisses_transition[0]] + l_abscisses[:] + [l_abscisses_transition[1]]

# un plan par abscisse
for abscisse in l_abscisses_plan:
    P_plan_part = MakeVertex(abscisse, 0, 0)
    plan_part = MakePlane(P_plan_part, Vx, plane_size)
    l_plans_abscisses.append(plan_part)

P_axe_tube = MakeVertex(abscisse_base_tube, 0, 0)
axe_tube = MakePrismVecH(P_axe_tube, Vx, h_tube)

# pour rabotter les plans de partition
P_bas = MakeVertex(abscisse_base_tube, 0, 0)
cylindre_int = MakeCylinder(P_bas, Vx, r_int/2., h_tube)

angle = 0
l_plans_diag = []
# un plan sur toutes les generatrices
# Rq: si on cree un plan toutes les 2 generatrices uniquement, 
# le maillage ne passera pas par les points  de mesure de l'autre generatrice sur 2
for i, nom_generatrice in enumerate(l_noms_generatrices):
    angle += d_angles[nom_generatrice]
    if (methode != "generatrices") or (methode == "generatrices" and (i==i_generatrice_ep_mini)):
        # TODO: lorsque MakePartition fonctionnera mieux (!),
        # supprimer le if ci-dessus pour toujours partitionner par les plans des generatrices
        P_vec_plan_tmp = MakeVertex(0, r_int, 0)
        P_vec_plan = MakeRotation(P_vec_plan_tmp, Vx, math.radians(angle))
        V_plan = MakeVector(P0, P_vec_plan)
        plan_diag_tmp = MakePrismVecH(axe_tube, V_plan, 2*r_ext)
        plan_diag = MakeCut(plan_diag_tmp, cylindre_int)
        l_plans_diag.append(plan_diag)

# TODO: lorsque MakePartition fonctionnera mieux (!), supprimer ce bloc
# car on aura partitionne par toutes les generatrices dans le bloc precedent.
if methode == "generatrices":
    plan_oppose = MakeRotation(l_plans_diag[-1], Vx, math.pi)
    l_plans_diag.append(plan_oppose)

tous_plans = MakeCompound(l_plans_abscisses + l_plans_diag)
addToStudy(tous_plans, "tous_plans")

plans_diag = MakeCompound(l_plans_diag)
addToStudy(plans_diag, "plans_diag")

plans_abscisses = MakeCompound(l_plans_abscisses)
addToStudy(plans_abscisses, "plans_abscisses")

if type_maillage == "regle":
    # Partion d'un tube plein par la face_int
    cylindre_tmp = MakeCylinder(P_bas, Vx, r_ext, h_tube)
    # le cylindre ainsi cree a sa ligne de couture sur Z
    # => on la decalle sur l'edge de couture de la face interieure: -pi/2 + angle_ep_mini
    if methode == "generatrices":
        cylindre = MakeRotation(cylindre_tmp, Vx, -math.pi/2. + math.radians(angle_ep_mini))
    else:
        # en methode ecailles de tortue, la reparation plante si on tourne le cylindre
        # mais reussi si le cylindre reste avec des edges de couture non paralleles!
        cylindre = cylindre_tmp
    addToStudy(cylindre, "cylindre")
    
    cylindre_part = MakePartition([cylindre, face_int])
    addToStudy(cylindre_part, "cylindre_part")
    
    # on recupere le solide correspondant au tube
    P_tube = MakeVertex(abscisse_base_tube, (r_ext+r_int)/2., 0)
    tube = GetBlockNearPoint(cylindre_part, P_tube)
    addToStudy(tube, "tube")
    
    if methode == "generatrices":
        # partition par plans diag puis plans abscisses
        tube_part_tmp = MakePartition([tube], [plans_diag])
        addToStudy(tube_part_tmp, "tube_part_tmp")
        tube_part = MakePartition([tube_part_tmp], [plans_abscisses])
    else:
        # partition par plans abscisses puis plans diag
        tube_part_tmp = MakePartition([tube], [plans_abscisses])
        addToStudy(tube_part_tmp, "tube_part_tmp")
        tube_part = MakePartition([tube_part_tmp], [plans_diag])
    addToStudy(tube_part, "tube_part")
        
    tube_part_improved = CheckAndImprove(tube_part)
    if not tube_part_improved:
        print "pas de reparation effectuee"
        tube_part_improved = tube_part
    addToStudy(tube_part_improved, "tube_part_improved")

else:
    # on partitionne les faces du bas et du haut pour pouvoir imposer le nombre de segments dans l'epaisseur
    face_bas_part = MakePartition([face_bas], [tous_plans], Limit=ShapeType["FACE"])
    face_haut_part = MakePartition([face_haut], [tous_plans], Limit=ShapeType["FACE"])
    # pour le maillage libre, on partitionne uniquement avec les points de mesure
    # pour qu'ils soient contenus dans le maillage
    if methode == "generatrices":
        # pour la methode generatrices, il faut partitionner la face interieure
        face_int_part = MakePartition([face_int], [tous_plans], Limit=ShapeType["FACE"])
    else:
        # pour la methode tortue, il suffit de partitionner par les points
        # (en fait, seuls manquent les points au milieu des arcs)
        face_int_part = MakePartition([face_int], [Tous_Points], Limit=ShapeType["FACE"])
    
    l_faces_tube = [face_int_part, face_ext, face_bas_part, face_haut_part]
    shell_tube = MakeShell(l_faces_tube)
    addToStudy(shell_tube, "shell_tube")
    
    tube_part_improved = MakeSolid([shell_tube])
    addToStudy(tube_part_improved, "tube_part_improved")
    
time3 = time.time()

print "Temps de partitionnement: %.1f s."%(time3-time2)

# Sous-geometries pour les sous-maillages
# =======================================

# edges dans l'epaisseur
l_edges_bas = GetShapesOnPlaneWithLocation(tube_part_improved, ShapeType["EDGE"], Vx, P_bas, GEOM.ST_ON)
edges_bas = CreateGroup(tube_part_improved, ShapeType["EDGE"])
UnionList(edges_bas, l_edges_bas)
edges_ep_bas = GetEdgesByLength (edges_bas, 0, r_ext-r_int + 1e-1)
addToStudyInFather(tube_part_improved, edges_ep_bas, "edges_ep_bas")

if type_maillage == "libre":
    # on recupere les faces bas et haut
    l_faces_bas = GetShapesOnPlaneWithLocation(tube_part_improved, ShapeType["FACE"], Vx, P_bas, GEOM.ST_ON)
    l_faces_haut = GetShapesOnPlaneWithLocation(tube_part_improved, ShapeType["FACE"], Vx, P_haut_ext, GEOM.ST_ON)
    faces_extremites = CreateGroup(tube_part_improved, ShapeType["FACE"])
    UnionList(faces_extremites, l_faces_bas + l_faces_haut)
    addToStudyInFather(tube_part_improved, faces_extremites, "faces_extremites")

# edges sur les arcs
edges_arc_bas = CreateGroup(edges_bas, ShapeType["EDGE"])
l_edges_ep_bas = SubShapeAllSorted(edges_ep_bas, ShapeType["EDGE"])
UnionList(edges_arc_bas, l_edges_bas)
DifferenceList(edges_arc_bas, l_edges_ep_bas)
addToStudyInFather(tube_part_improved, edges_arc_bas, "edges_arc_bas")

# on recupere la face interieure
l_face_int = GetShapesOnCylinder(tube_part_improved, ShapeType["FACE"], Vx, r_ext - ep_min, GEOM.ST_IN)
sub_face_int = CreateGroup(tube_part_improved, ShapeType["FACE"])
UnionList(sub_face_int, l_face_int)
addToStudyInFather(tube_part_improved, sub_face_int, "SURF_INT")

# on recupere les edges d'amortissement
P_bas_int = MakeTranslation(P_bas, 0, r_int, 0)
P_edge_tmp = MakeRotation(P_bas_int, Vx, math.radians(angle_ep_mini))
P_edge_amortissement_1 = MakeTranslation(P_edge_tmp, longueur_amortissement/2., 0, 0)
P_edge_amortissement_2 = MakeTranslation(P_edge_tmp, h_tube-longueur_amortissement/2., 0, 0)
edge_amortissement_1 = GetEdgeNearPoint(tube_part_improved, P_edge_amortissement_1)
edge_amortissement_2 = GetEdgeNearPoint(tube_part_improved, P_edge_amortissement_2)
edges_amortissement = CreateGroup(tube_part_improved, ShapeType["EDGE"])
UnionList(edges_amortissement, [edge_amortissement_1, edge_amortissement_2])
addToStudyInFather(tube_part_improved, edges_amortissement, "edges_amortissement")

# on recupere les edges de transition
P_edge_transition_1 = MakeTranslation(P_edge_tmp, longueur_transition/2. + longueur_amortissement, 0, 0)
P_edge_transition_2 = MakeTranslation(P_edge_tmp, h_tube-(longueur_transition/2. + longueur_amortissement), 0, 0)
edge_transition_1 = GetEdgeNearPoint(tube_part_improved, P_edge_transition_1)
edge_transition_2 = GetEdgeNearPoint(tube_part_improved, P_edge_transition_2)
edges_transition = CreateGroup(tube_part_improved, ShapeType["EDGE"])
UnionList(edges_transition, [edge_transition_1, edge_transition_2])
addToStudyInFather(tube_part_improved, edges_transition, "edges_transition")

# on recupere les edges d'une generatrice

axe_generatrice_tmp = MakeTranslation(Vx, 0, r_int, 0)
axe_generatrice = MakeRotation(axe_generatrice_tmp, Vx, math.radians(angle_ep_mini))
l_edges_generatrice = GetShapesOnCylinder(tube_part_improved, ShapeType["EDGE"], axe_generatrice, ep_nominale, GEOM.ST_IN)
edges_generatrice = CreateGroup(tube_part_improved, ShapeType["EDGE"])
UnionList(edges_generatrice, l_edges_generatrice)
DifferenceList(edges_generatrice, [edge_amortissement_1, edge_amortissement_2]+[edge_transition_1, edge_transition_2])
addToStudyInFather(tube_part_improved, edges_generatrice, "edges_generatrice")

# on recupere les edges d'une generatrice dont la longueur est inferieure a petite_distance
# pour pouvoir imposer moins de segments
if methode != "generatrices":
    edges_petite_distance = CreateGroup(tube_part_improved, ShapeType["EDGE"])
    l_petite_distance = []
    for edge in l_edges_generatrice:
        length = BasicProperties(edge)[0]
        if length <= petite_distance:
            l_petite_distance.append(edge)
    UnionList(edges_petite_distance, l_petite_distance)
    addToStudyInFather(tube_part_improved, edges_petite_distance, "edges_petite_distance")



# Sous-geometries pour les groupes
# ================================

# on recupere la face interieure sans les zones de transition et d'amortissement
P_abs_first = MakeVertex(l_abscisses[0], 0, 0)
l_face_int_inf = GetShapesOnPlaneWithLocation(tube_part_improved, ShapeType["FACE"], Vx, P_abs_first, GEOM.ST_IN)
P_abs_last = MakeVertex(l_abscisses[-1], 0, 0)
l_face_int_sup = GetShapesOnPlaneWithLocation(tube_part_improved, ShapeType["FACE"], Vx, P_abs_last, GEOM.ST_OUT)
sub_face_int_milieu = CreateGroup(tube_part_improved, ShapeType["FACE"])
UnionList(sub_face_int_milieu, l_face_int)
DifferenceList(sub_face_int_milieu, l_face_int_inf + l_face_int_sup)
addToStudyInFather(tube_part_improved, sub_face_int_milieu, "FaceIntM")

# on recupere la face exterieure
l_face_ext = GetShapesOnCylinder(tube_part_improved, ShapeType["FACE"], Vx, r_ext, GEOM.ST_ON)
sub_face_ext = CreateGroup(tube_part_improved, ShapeType["FACE"])
UnionList(sub_face_ext, l_face_ext)
addToStudyInFather(tube_part_improved, sub_face_ext, "SURF_EXT")

# on recupere la face a l'extremite amont du tube
l_face_bas = GetShapesOnPlaneWithLocation(tube_part_improved, ShapeType["FACE"], Vx, P_bas, GEOM.ST_ON)
sub_face_bas = CreateGroup(tube_part_improved, ShapeType["FACE"])
UnionList(sub_face_bas, l_face_bas)
addToStudyInFather(tube_part_improved, sub_face_bas, "CLGV")

# on recupere la face a l'extremite aval du tube
l_face_haut = GetShapesOnPlaneWithLocation(tube_part_improved, ShapeType["FACE"], Vx, P_haut_ext, GEOM.ST_ON)
sub_face_haut = CreateGroup(tube_part_improved, ShapeType["FACE"])
UnionList(sub_face_haut, l_face_haut)
addToStudyInFather(tube_part_improved, sub_face_haut, "EXTUBE")

# On recupere les edges communs a face_int et face_haut
l_edge_int = GetShapesOnCylinderIDs(tube_part_improved, ShapeType["EDGE"], Vx, r_ext - ep_min, GEOM.ST_IN)
l_edge_haut = GetShapesOnPlaneWithLocationIDs(tube_part_improved, ShapeType["EDGE"], Vx, P_haut_ext, GEOM.ST_ON)
l_edge_bord_int_haut = []
for id_edge in l_edge_int:
    if id_edge in l_edge_haut:
        l_edge_bord_int_haut.append(id_edge)

edge_bord_int_haut = CreateGroup(tube_part_improved, ShapeType["EDGE"])
UnionIDs(edge_bord_int_haut, l_edge_bord_int_haut)
addToStudyInFather(tube_part_improved, edge_bord_int_haut, "BORDTU")

# on recupere le point d'epaisseur minimale
# avec la methode tortue le maillage passe forcement par le point d'epaisseur minimale
#if methode != "generatrices":
x, y, z = PointCoordinates(P_ep_mini)
P_ep_mini_sub = GetPoint(tube_part_improved, x, y, z, 1e-5)
addToStudyInFather(tube_part_improved, P_ep_mini_sub, "P_ep_mini")

time4 = time.time()

print "Temps de recuperation des sous-geometries: %.1f s."%(time4-time3)

# MAILLAGE
# ========

# on divise le nombre de segments par le nombre de plans suivant les abscisses

Maillage = smesh.Mesh(tube_part_improved, "Tube")

if type_maillage == "regle":
    algo1D = Maillage.Segment()
    algo1D.NumberOfSegments(nb_seg_generatrices)
    #algo1D.QuadraticMesh()
    
    Maillage.Quadrangle()
    
    Maillage.Hexahedron()
else:
    # 30
    average_length = h_tube/(nb_seg_generatrices + 2*(nb_seg_amortissement+nb_seg_transition))/5.
    # BLSURF est un algo 1D/2D
    if type_algo == "BLSURF":
         algo2D = Maillage.Triangle(algo=smesh.BLSURF)
         algo2D.SetPhySize(average_length)
    else:
         algo1D = Maillage.Segment()
         algo1D.LocalLength(average_length)
         
	 Maillage.Triangle(smesh.NETGEN_2D)
    
    
    #algo3D = Maillage.Tetrahedron(smesh.GHS3D)
    algo3D = Maillage.Tetrahedron()


# hypotheses locales
# ==================

# On impose finalement un maillage fin partout, seul moyen d'avoir plusieurs elements dans l'epaisseur
if type_maillage == "libre":
    # 8
    average_length_extremites = average_length/8.
    # BLSURF est un aglo 1D/2D
    if type_algo == "BLSURF":
         #algo2D = Maillage.Triangle(geom=faces_extremites, algo=smesh.BLSURF)
         #algo2D.SetPhySize(average_length_extremites)
	 pass
    else:
        # 8
        algo1D = Maillage.Segment(faces_extremites)
        algo1D.LocalLength(average_length_extremites)

if type_maillage == "regle":
    # dans l'epaisseur
    algo1D = Maillage.Segment(edges_ep_bas)
    algo1D.NumberOfSegments(nb_seg_ep)
    algo1D.Propagation()
    
    # sur les arcs
    algo1D = Maillage.Segment(edges_arc_bas)
    algo1D.NumberOfSegments(nb_seg_arc)
    algo1D.Propagation()

    # sur les longueurs d'amortissement
    algo1D = Maillage.Segment(edges_amortissement)
    algo1D.NumberOfSegments(nb_seg_amortissement)
    algo1D.Propagation()
    
    # sur les longueurs de transition
    algo1D = Maillage.Segment(edges_transition)
    algo1D.NumberOfSegments(nb_seg_transition)
    algo1D.Propagation()
    
    if methode == "tortue":
        algo1D = Maillage.Segment(edges_petite_distance)
        algo1D.NumberOfSegments(nb_seg_petites_distances)
        algo1D.Propagation()

Maillage.Compute()

# on fait passer le maillage par le point de plus faible epaisseur
#if methode == "generatrices":
    #x, y, z = PointCoordinates(P_ep_mini)
    #id_node = Maillage.MeshToPassThroughAPoint(x, y, z)
    ## on cree le groupe avec le point de plus faible epaisseur
    #Maillage.MakeGroupByIds("P_ep_mini", smesh.NODE, [id_node])

# on a deja cree le groupe geometrique
#if methode != "generatrices":
Maillage.Group(P_ep_mini_sub)

# conversion en quadratique (tres long Ã  afficher)
#Maillage.ConvertToQuadratic(1)

# on ajoute deux points aux extremites de l'axe du tube
x, y, z = PointCoordinates(P_bas)
id_p2 = Maillage.AddNode(x, y, z)
Maillage.MakeGroupByIds("P2", smesh.NODE, [id_p2])

id_p1 = Maillage.AddNode(x+h_tube, y, z)
Maillage.MakeGroupByIds("P1", smesh.NODE, [id_p1])

# Groupes
# =========

Maillage.Group(edge_bord_int_haut)
Maillage.Group(sub_face_int)
Maillage.Group(sub_face_int, "PEAUINT")
Maillage.Group(sub_face_ext)
Maillage.Group(sub_face_ext, "PEAUEXT")
Maillage.Group(sub_face_bas)
Maillage.Group(sub_face_bas, "FACE1")
Maillage.Group(sub_face_haut)
Maillage.Group(sub_face_haut, "FACE2")
group_nodes_int_milieu = Maillage.GroupOnGeom(sub_face_int_milieu, "NodesInt", smesh.NODE)
Maillage.GroupOnGeom(tube_part_improved, "VOL_TUBE", smesh.VOLUME)
Maillage.GroupOnGeom(tube_part_improved, "COUDE", smesh.VOLUME)

if test_gibi:
    time4 = time.time()
    ([MaillageGibi], status) = smesh.smesh.CreateMeshesFromMED(maillage_gibi)
    
    # on met le maillage gibi dans le meme axe que le maillage SALOME
    MaillageGibi.RotateObject(MaillageGibi, Vz, -math.pi/2., False)
    
    V_trans = MakeVectorDXDYDZ(-longueur_amortissement-longueur_transition+l_abscisses[0], 0, 0)
    MaillageGibi.TranslateObject(MaillageGibi, V_trans, False)
    
    MaillageInt = MaillageGibi
    
    gibi_groupes = MaillageGibi.GetGroups()
    
    # on determine le groupe correspondant a la face interieure
    group_int = None
    for groupe in gibi_groupes:
        name = groupe.GetName()
        if name.strip() == "SURF_INT":
            group_int = groupe
            break
    l_faces_int = group_int.GetIDs()
    l_nodes_ids = []
    for face_id in l_faces_int:
        l_nodes = MaillageGibi.GetElemNodes(face_id)
        for node in l_nodes:
            if node not in l_nodes_ids:
                l_nodes_ids.append(node)

time5 = time.time()

print "Temps de generation du maillage: %.1f s."%(time5-time4)

# Verifions si le maillage passe par les points de mesure
# =======================================================

# on cree un maillage avec les points de mesure
MaillageTousPoints = smesh.Mesh(Tous_Points, "Tous_Points")
## BUG: smesh ne peut pas creer un maillage de points!
#MaillageTousPoints.Compute()
# => On ajoute les points un par un...
l_tous_points = SubShapeAllSorted(Tous_Points, ShapeType["VERTEX"])
for point in l_tous_points:
    x, y, z = PointCoordinates(point)
    MaillageTousPoints.AddNode(x, y, z)

l_points_mesures_ids = MaillageTousPoints.GetNodesId()

# on ajoute les noeuds mailles de la face interieure
if not test_gibi:
    l_nodes_ids = group_nodes_int_milieu.GetIDs()
    MaillageInt = Maillage
for node in l_nodes_ids:
    # on recupere les coordonnees depuis le maillage global
    x, y, z = MaillageInt.GetNodeXYZ(node)
    # on ajoute ce noeud dans le maillage de points
    MaillageTousPoints.AddNode(x, y, z)

# on trouve les noeuds en double
tolerance = 1e0
coincident_nodes = MaillageTousPoints.FindCoincidentNodes(tolerance)

# nombre de points de mesure
nb_points = len(l_points)

# nombre de noeuds en commun
nb_coincident_nodes = len(coincident_nodes)

# nombre de points perdus
nb_points_perdus = nb_points - nb_coincident_nodes

print "%i/%i points de mesure ont ete conserves dans le maillage"%(nb_coincident_nodes, nb_points)
if nb_points_perdus:
    print "%i/%i points de mesure ont ete perdus dans le maillage"%(nb_points_perdus, nb_points)

# affichage des points de mesure conserves
group_kept_nodes = MaillageTousPoints.CreateEmptyGroup(smesh.NODE, "Kept_measure_points")
l_id_coincident_nodes = []
for l_id in coincident_nodes:
    l_id_coincident_nodes += l_id
group_kept_nodes.Add(l_id_coincident_nodes)

# affichage des points de mesure perdus
group_lost_nodes = MaillageTousPoints.CreateEmptyGroup(smesh.NODE, "Lost_measure_points")
l_id_lost_points = []
for id_point in l_points_mesures_ids:
    if id_point not in l_id_coincident_nodes:
        l_id_lost_points.append(id_point)
group_lost_nodes.Add(l_id_lost_points)

# On merge les noeuds en double
if coincident_nodes:
    MaillageTousPoints.MergeNodes(coincident_nodes)

# on regarde si le point d'epaisseur minimale fait partie des points garde
x_mini, y_mini, z_mini = PointCoordinates(P_ep_mini)
id_p_ep_mini = MaillageTousPoints.AddNode(x_mini, y_mini, z_mini)
MaillageTousPoints.MakeGroupByIds("P_ep_mini", smesh.NODE, [id_p_ep_mini])

coincident_nodes_ep_mini = MaillageTousPoints.FindCoincidentNodes(tolerance)
if coincident_nodes_ep_mini:
    print "Le point d'epaisseur minimale a ete conserve"
else:
    print "Le point d'epaisseur minimale a ete perdu"

time6 = time.time()

print "Temps de verification du maillage: %.1f s."%(time6-time5)

print "Temps total: %.1f s."%(time6 - time0)

salome.sg.updateObjBrowser(0)

