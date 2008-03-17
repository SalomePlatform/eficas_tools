# -*- coding: iso-8859-1 -*-
"""
outil métier Cabri pour Salome

"""


def tetra( name, **param ):
    """
    construction géométrie Cabri en Tetra    
    """
    #*************************************************************
    # Paramètres physiques 
    #*************************************************************    
    # Nombre déléments circonférentiels (NBR_CIR)
    ncir = param['ncir']
    # Temps danalyse
    temps = param['temps']
    # Nombre déléments de lalésage (NBR_ALE)
    nsect = param['nsect']
    # Nombre déléments radiaux (NBR_RAD)
    nrad = param['nrad']
    # Nombre déléments verticaux (NBR_VER)
    nver = param['nver']
    
    
    # Epaisseur de la rondelle (GOUJ_E_RONDEL)
    he = param['he']
    # Hauteur de la bride (BRID_H)
    hc1 = param['hc1']
    # Epaisseur de lécrou (GOUJ_E_ECROU)
    e = param['e']
    # Nombre de goujons de la jonction boulonnée (GOUJ_N_GOUJON)
    nbgouj = param['nbgouj']
    # Diamètre des goujons de la jonction boulonnée (GOUJ_D_GOUJON)
    dg = param['dg']
    # Hauteur des alésages de la bride permettant lintroduction des goujons (BRID_H_ALESAG)
    htrou = param['htrou']
    # Epaisseur du joint au niveau de linterface détanchéité (ETAN_E_JOINT)
    j = param['j']
    # Hauteur de lépaulement de la bride au niveau de linterface détanchéité (BRID_H_EPAUL)
    hb = param['hb']
    # Rayon du congé de la bride (BRID_R_CONGE)
    rcong = param['rcong']
    # Position des alésages de la bride permettant lintroduction des goujons (BRID_P_ALESAG)
    dtrou = param['dtrou']
    # Profondeur (épaisseur) des filets des goujons (GOUJ_E_FILET)
    pf = param['pf']
    # Hauteur de conduite (TUBU_H)
    hcg1 = param['hcg1']
    # Diamètre intérieur de la bride (BRID_D_INT)
    dint = param['dint']
    # Diamètre extérieur de la bride (BRID_D_EXT)
    dext = param['dext']
    # Diamètre des alésages de la bride permettant lintroduction des goujons (BRID_D_ALESAG)
    dt = param['dt']
    # Diamètre de lécrou (GOUJ_D_ECROU)
    dec = param['dec']
    # Diamétre extérieur de la conduite (TUBU_D_EXT)
    dex1 = param['dex1']
    # Diamètre de la rondelle (GOUJ_D_RONDEL)
    drd = param['drd']
    # Diamètre de lépaulement de la bride au niveau de linterface détanchéité (BRID_D_EPAUL)
    dex3 = param['dex3']
    # Position (diamètre) du congé de la bride (BRID_D_CONGE)
    dex2 = param['dex2']
    
    
    
    import math
    import time
    
    # imports spécifiques à salome:
    
    import geompy
    import smesh
    import salome
    #Import de l'interface graphique de GEOM (nécessaire pour affecter de la couleur)
    gg = salome.ImportComponentGUI("GEOM")
    
    time_init = time.time()
    
    #**************************                                                   
    # test sur les parametres *                                                   
    #**************************
    
    #opti trac psc
    
    nrad = abs(nrad)
    ncir = abs(ncir)
    nver = abs(nver)
    temps = abs(temps)
    nsect = abs(nsect)
    nbgouj = abs(nbgouj)
    dint = abs(dint)
    dex1 = abs(dex1)
    dex2 = abs(dex2)
    dex3 = abs(dex3)
    dtrou = abs(dtrou)
    dext = abs(dext)
    dt = abs(dt)
    drd = abs(drd)
    dg = abs(dg)
    dec = abs(dec)
    rcong = abs(rcong)
    he =  abs(he)
    e = abs(e)
    j = abs(j)
    hc1 = abs(hc1)
    hcg1 = abs(hcg1)
    hb = abs(hb)
    htrou = abs(htrou)
    pf = abs(pf)
    j = abs(j)
    
    if (nbgouj <= 2):
        nbgouj = 2
    
    if ((nbgouj == 2) and (ncir <= 4)):
        ncir = 4
    
    if (dex1 <= dint):
        dex1 = dint+10.
    
    if (dex2 <= dex1):
        dex2 = dex1+20
    
    if (dg >= dt):
        dg = dt-2.
    
    if (dec <= dt):
        if (drd > dt):
            dec = (dt+drd)/2
        else:
            dec = dt+2
            drd = dec+2
    
    if ((dtrou-dt) <= dex2):
        if (dtrou <= dex2):
            dtrou = dex2+(2*dt)
        else:
            dt = (dtrou-dex2)/2
    
    if (dex3 < dint):
        dex3 = dtrou-drd
    if (dex3 > (dtrou-dt)):
        dex3 = dtrou-drd
    
    if ((dtrou+drd) <= (2*dtrou-dex3)):
        a = 2*dtrou-dex3
    else:
        a = dtrou+drd
    if (dext < a):
        dext = a 
    
    if (hb >= hc1):
        hb = 1
    if (htrou >= hc1):
        htrou = hc1/2
    if ((hb+htrou) >= hc1):
        hb = (hc1-htrou)/10
    
    if (rcong >= 15.):
        rcong = 15.
    
    rg = dg / 2.
    if (pf >= rg):
        pf = rg/2.
    
    if (nrad <= 0):
        nrad = 1
    
    if (ncir <= 1):
        ncir = 2
    
    if (nver <= 0):
        nver = 1
    
    if (nsect <= 3):
        nsect = 4
    
    if (temps <= 0):
        nsect = 3
    
    #**************************                                                   
    # parametres intrinsèques *                                                   
    #**************************
    #opti dime 3 elem cub8                           
    #dens 1
    
    # critere pour elim                                                     
    crit = 0.0001                                                              
    
    # rayons
    rint = dint / 2.
    rex1 = dex1 / 2.
    rex2 = dex2 / 2.
    rex3 = dex3 / 2.
    rtrou = dtrou / 2.
    rext = dext / 2.
    rt = dt / 2.
    rrd = drd / 2.
    rg = dg / 2.
    rec = dec / 2.
    
    # angle de coupe
    stet = rrd/rtrou 
    ctet = stet**2 
    ctet = 1-ctet 
    ctet = ctet**0.5 
    tet = stet/ctet 
    tet = math.atan(tet)
    beta = math.pi / nbgouj
    # if (tet >= beta):
    #     tet = 1.1*tet
    #     beta = tet 
    # else:
    #     if ((beta-tet) < (0.1*tet)):
    #         tet = beta
    #     else:
    #         tet = (tet+beta)/2 
    
    # hauteurs                                                        
    ht = hc1 + hcg1;                                                           
    h = (hb + htrou);
    mj = 0-j;     
    
    p0 = geompy.MakeVertex(0., 0., 0.)
    
    Vx = geompy.MakeVectorDXDYDZ(1., 0., 0.)
    Vy = geompy.MakeVectorDXDYDZ(0., 1., 0.)
    Vz = geompy.MakeVectorDXDYDZ(0., 0., 1.)
    
    
    p1 = geompy.MakeVertex(rint, 0., 0.)
    p2 = geompy.MakeVertex(rint, 0., -j/2.)
    p3 = geompy.MakeVertex(rex3, 0., -j/2.)
    p4 = geompy.MakeVertex(rex3, 0., 0.)
    
    edge1 = geompy.MakeEdge(p1,p2)
    edge2 = geompy.MakeEdge(p2,p3)
    edge3 = geompy.MakeEdge(p3,p4)
    edge4 = geompy.MakeEdge(p4,p1)
    
    wire_joint = geompy.MakeWire([edge1, edge2, edge3, edge4])
    face_joint = geompy.MakeFace(wire_joint,1)
    
    p5 = geompy.MakeVertex(rex3, 0., hb)
    
    edge5 = geompy.MakeEdge(p4, p5)
    
    p7 = geompy.MakeVertex(rext, 0., hb)
    p8 = geompy.MakeVertex(rext, 0., hb + htrou)
    p9 = geompy.MakeVertex(rex2, 0., hb + htrou)
    
    edge6 = geompy.MakeEdge(p5, p7)
    edge9 = geompy.MakeEdge(p7, p8)
    # construction du congé
    # Rq: voir ce que l'on fait si la rondelle s'appuye sur le congé                    
    
    an = math.atan ((hc1-h)/(rex2-rex1)) 
    alpha = (math.pi - an)/2.
    
    conge_p1 = geompy.MakeVertex(rex2 + rcong/math.tan(alpha), 0., h)
    conge_centre = geompy.MakeVertex(rex2 + rcong/math.tan(alpha), 0., h + rcong)
    
    gamma = math.pi - 2*alpha
    
    conge_axe = geompy.MakePrismVecH(conge_centre, Vy, 1)
    conge = geompy.MakeRevolution(conge_p1, conge_axe, gamma)
    # geompy.addToStudy(conge, "conge")
    
    conge_p2 = geompy.MakeRotation(conge_p1, conge_axe, gamma)
    
    ## fin construction du congé
    
    #avant le congé
    edge10 = geompy.MakeEdge(p8, conge_p1)
    # après le congé
    p12 = geompy.MakeVertex(rex1, 0., hc1)
    edge11 = geompy.MakeEdge(conge_p2, p12)
    
    p11 = geompy.MakeVertex(rint, 0., hc1)
    p13 = geompy.MakeVertex(rex1, 0., hc1 + hcg1)
    p14 = geompy.MakeVertex(rint, 0., hc1 + hcg1)
    
    edge16 = geompy.MakeEdge(p11, p14)
    edge17 = geompy.MakeEdge(p14, p13)
    edge18 = geompy.MakeEdge(p13, p12)
    
    edge19 = geompy.MakeEdge(p11, p1)
    
    wire_front = geompy.MakeWire([edge4, edge5, edge6, edge9, edge10, conge,
                                edge11, edge18, edge17, edge16, edge19])
    
    face_front = geompy.MakeFace(wire_front,1)
    # geompy.addToStudy(face_front, "face_front")
    # on ajoutera le joint après la révolution
    
    
    # Création du bloc solide
    
    bride_revol = geompy.MakeRevolution(face_front, Vz, beta)
    # geompy.addToStudy(bride_revol, "bride_revol")
    
    # outil de coupe
    p_goujon = geompy.MakeVertex(rtrou, 0., -j/2.)
    cut_tool = geompy.MakeCylinder(p_goujon, Vz, rt, hc1 + j)
    # geompy.addToStudy(cut_tool, "cut_tool")
    
    # coupe
    bride_cut = geompy.MakeCut(bride_revol, cut_tool)
    # geompy.addToStudy(bride_cut, "bride_cut")
    
    
    
    # goujon
    axe_goujon = geompy.MakePrismVecH(p_goujon, Vz, 1.)
    p_rayon_goujon = geompy.MakeTranslation(p_goujon, rg, 0., 0.)
    rayon_goujon = geompy.MakeEdge(p_goujon, p_rayon_goujon)
    # base_goujon = geompy.MakeRevolution(rayon_goujon, axe_goujon, math.pi)
    h_goujon = j/2. + h + e + 1.5 * he
    p1_filet_goujon = geompy.MakeVertex(rtrou + rg, 0., h_goujon - pf)
    p2_filet_goujon = geompy.MakeVertex(rtrou + rg - pf, 0., h_goujon)
    p_goujon_h = geompy.MakeVertex(rtrou, 0., h_goujon)
    edge1_goujon = geompy.MakeEdge(p_rayon_goujon, p1_filet_goujon)
    edge2_goujon = geompy.MakeEdge(p1_filet_goujon, p2_filet_goujon)
    edge3_goujon = geompy.MakeEdge(p2_filet_goujon, p_goujon_h)
    wire_goujon = geompy.MakeWire([rayon_goujon, edge1_goujon, edge2_goujon, edge3_goujon])
    face_ext_goujon = geompy.MakeRevolution(wire_goujon, axe_goujon, math.pi)
    # geompy.addToStudy(face_ext_goujon, "face_ext_goujon")
    wire_gauche_goujon = geompy.MakeRotation(wire_goujon, axe_goujon, math.pi)
    
    p2_filet_goujon_g = geompy.MakeRotation(p2_filet_goujon, axe_goujon, math.pi)
    p_rayon_goujon_g = geompy.MakeTranslation(p_goujon, - rg, 0., 0.)
    diametre_haut = geompy.MakeEdge(p2_filet_goujon_g, p2_filet_goujon)
    diametre_bas = geompy.MakeEdge(p_rayon_goujon_g, p_rayon_goujon)
    edge1_goujon_g = geompy.MakeRotation(edge1_goujon, axe_goujon, math.pi)
    edge2_goujon_g = geompy.MakeRotation(edge2_goujon, axe_goujon, math.pi)
    wire_face_int_goujon2 = geompy.MakeWire([diametre_bas, edge1_goujon, edge2_goujon, 
                diametre_haut, edge1_goujon_g, edge2_goujon_g])
    # geompy.addToStudy(wire_face_int_goujon2, "wire_face_int_goujon2")
    face_int_goujon = geompy.MakeFace(wire_face_int_goujon2, 1)
    
    shell_goujon = geompy.MakeShell([face_ext_goujon, face_int_goujon])
    goujon = geompy.MakeSolid([shell_goujon])
    # geompy.addToStudy(goujon, "goujon")
    
    # ecrou
    p1_ecrou = geompy.MakeVertex(rtrou + rg, 0., hb + htrou + e)
    p2_ecrou = geompy.MakeVertex(rtrou + rec, 0., hb + htrou + e)
    rayon_ecrou = geompy.MakeEdge(p1_ecrou, p2_ecrou)
    base_ecrou = geompy.MakeRevolution(rayon_ecrou, axe_goujon, math.pi)
    ecrou = geompy.MakePrismVecH(base_ecrou, Vz, he)
    # geompy.addToStudy(ecrou, "ecrou")
    
    # assemblage goujon, ecrou:
    goujon_ecrou = geompy.MakeCompound([goujon, ecrou])
    # geompy.addToStudy(goujon_ecrou, "goujon_ecrou")
    
    
    # rondelle
    p1_rondelle = geompy.MakeVertex(rtrou + rt, 0., hb + htrou)
    p2_rondelle = geompy.MakeVertex(rtrou + rrd, 0., hb + htrou)
    rayon_rondelle = geompy.MakeEdge(p1_rondelle, p2_rondelle)
    # base_rondelle = geompy.MakeRevolution(rayon_rondelle, axe_goujon, math.pi)
    face_rondelle = geompy.MakePrismVecH(rayon_rondelle, Vz, e)
    rondelle = geompy.MakeRevolution(face_rondelle, axe_goujon, math.pi)
    # geompy.addToStudy(rondelle, "rondelle")
    
    
    # assemblage goujon-ecrou avec rondelle
    goujon_ecrou_rondelle = geompy.MakeFuse(goujon_ecrou, rondelle)
    # geompy.addToStudy(goujon_ecrou_rondelle, "goujon_ecrou_rondelle")
    
    
    # assemblage sur la piece principale
    bride_but_joint_tmp = geompy.MakeFuse(bride_cut, goujon_ecrou_rondelle)
    # geompy.addToStudy(bride_but_joint_tmp, "bride_but_joint_tmp")
    
    # On partitionne avec la rondelle pour récupérer les solides physiques
    bride_but_joint = geompy.MakePartition([bride_but_joint_tmp], [rondelle])
    # geompy.addToStudy(bride_but_joint, "bride_but_joint")
    
    # on ajoute le joint (compound pour que les faces communes soient en double)
    joint = geompy.MakeRevolution(face_joint, Vz, beta)
    # geompy.addToStudy(joint, "joint")
    
    bride_tmp = geompy.MakeCompound([bride_but_joint, joint])
    # geompy.addToStudy(bride_tmp, "bride_tmp")
    
    time_0 = time.time()
    print "Temps Geometrie = ", (time_0-time_init)
    
    
    # on partitionne pour obtenir certains points (P_BRI, P_GOU)
    p6 = geompy.MakeVertex(rint, 0., hb)
    edge_part = geompy.MakeEdge(p6, p7)
    plan_part = geompy.MakeRevolution(edge_part, Vz, beta)
    bride_part = geompy.MakePartition([bride_tmp], [plan_part])
    # geompy.addToStudy(bride_part, "bride_part")
    
    edge_p5_p6 = geompy.GetEdge(bride_part, p5, p6)
    edge_p5_p6_ind = geompy.GetSubShapeID(bride_part, edge_p5_p6)
    bride_vertex1 = geompy.DivideEdge(bride_part, edge_p5_p6_ind, 1./3., 1)
    # geompy.addToStudy(bride_vertex1, "bride_vertex1")
    
    p_gouj_part1 = geompy.MakeVertex(rtrou - rg, 0., hb)
    p_gouj_part2 = geompy.MakeVertex(rtrou + rg, 0., hb)
    p_gouj_mid = geompy.MakeVertex(rtrou, 0., hb)
    edge_gouj_part = geompy.GetEdgeNearPoint(bride_vertex1, p_gouj_mid)
    edge_gouj_part_ind = geompy.GetSubShapeID(bride_vertex1, edge_gouj_part)
    bride = geompy.DivideEdge(bride_vertex1, edge_gouj_part_ind, 0.5, 1)
#     geompy.addToStudy(bride, "bride")
    geompy.addToStudy(bride, name )
    
    
    time_1 = time.time()
    print "Temps Partition = ", (time_1-time_0)
    
    # Détermination des différents solides et affichage en couleur
    
    idToDisplay=[]
    
    GOUJON1 = geompy.GetBlockNearPoint(bride, p_goujon)
    GOUJON2 = geompy.GetBlockNearPoint(bride, p_goujon_h)
    list_GOUJON = [GOUJON1, GOUJON2]
    
    GOUJON = geompy.CreateGroup(bride, geompy.ShapeType["SOLID"])
    id_GOUJON = geompy.addToStudyInFather(bride, GOUJON, "GOUJON")
    idToDisplay.append(id_GOUJON)
    
    for solid in list_GOUJON:
        f_ind_tmp = geompy.GetSubShapeID(bride, solid)
        geompy.AddObject(GOUJON, f_ind_tmp)
    
    
    JOINT = geompy.GetBlockNearPoint(bride, p2)
    id_JOINT = geompy.addToStudyInFather(bride, JOINT, "JOINT")
    idToDisplay.append(id_JOINT)
    
    p_rondelle = geompy.MakeTranslation(p2_rondelle, 0., 0., e)
    ROND = geompy.GetBlockNearPoint(bride, p_rondelle)
    id_ROND = geompy.addToStudyInFather(bride, ROND, "ROND")
    idToDisplay.append(id_ROND)
    
    p_ecrou = geompy.MakeTranslation(p2_ecrou, 0., 0., he)
    ECROU = geompy.GetBlockNearPoint(bride, p_ecrou)
    id_ECROU = geompy.addToStudyInFather(bride, ECROU, "ECROU")
    idToDisplay.append(id_ECROU)
    
    list_BRIDE = []
    
    BRIDE1 = geompy.GetBlockNearPoint(bride, p14)
    list_BRIDE.append(BRIDE1)
    
    p_BRIDE2 = geompy.MakeVertex((rint+rex3)/2., 0., hb/2.)
    p_BRIDE2_rota = geompy.MakeRotation(p_BRIDE2, Vz, beta/2.)
    BRIDE2 = geompy.GetBlockNearPoint(bride, p_BRIDE2_rota)
    list_BRIDE.append(BRIDE2)
    
    BRIDE = geompy.CreateGroup(bride, geompy.ShapeType["SOLID"])
    id_BRIDE = geompy.addToStudyInFather(bride, BRIDE, "BRIDE")
    idToDisplay.append(id_BRIDE)
    
    for solid in list_BRIDE:
        f_ind_tmp = geompy.GetSubShapeID(bride, solid)
        geompy.AddObject(BRIDE, f_ind_tmp)
    
    RedGreenBlue = [[189,97,0],[255,215,0],[255,0,0],[0,176,0],[0,0,255]]
    
    for i in range(len(idToDisplay)):
        gg.createAndDisplayGO(idToDisplay[i])
        gg.setDisplayMode(idToDisplay[i],1)
        gg.setColor(idToDisplay[i],RedGreenBlue[i][0],RedGreenBlue[i][1],RedGreenBlue[i][2])
    
    list_VTOT = geompy.SubShapeAllSorted(bride, geompy.ShapeType["SOLID"])
    VTOT = geompy.CreateGroup(bride, geompy.ShapeType["SOLID"])
    for solid in list_VTOT:
        f_ind_tmp = geompy.GetSubShapeID(bride, solid)
        geompy.AddObject(VTOT, f_ind_tmp)
    geompy.addToStudyInFather(bride, VTOT, "VTOT")
        
    time_2 = time.time()
    print "Temps affichage solides = ", (time_2-time_1)
    
    # Détermination des différentes faces
    
    p_SCEG = geompy.MakeVertex(rtrou, rg, h + e + he/2.)
    SCEG = geompy.GetFaceNearPoint(ECROU, p_SCEG)
    geompy.addToStudyInFather(bride, SCEG, "SCEG")
    
    SCGE = geompy.GetFaceNearPoint(GOUJON, p_SCEG)
    geompy.addToStudyInFather(bride, SCGE, "SCGE")
    
    p_2_3 = geompy.MakeVertexOnCurve(edge2, 0.5)
    p_2_3_rota = geompy.MakeRotation(p_2_3, Vz, beta/2.)
    M_JOI = geompy.GetFaceNearPoint(JOINT, p_2_3_rota)
    geompy.addToStudyInFather(bride, M_JOI, "M_JOI")
    
    p_1_4 = geompy.MakeVertexOnCurve(edge4, 0.5)
    p_1_4_rota = geompy.MakeRotation(p_1_4, Vz, beta/2.)
    SCJB = geompy.GetFaceNearPoint(JOINT, p_1_4_rota)
    geompy.addToStudyInFather(bride, SCJB, "SCJB")
    
    SCBJ = geompy.GetFaceNearPoint(BRIDE, p_1_4_rota)
    geompy.addToStudyInFather(bride, SCBJ, "SCBJ")
    
    p1_rota = geompy.MakeRotation(p1, Vz, beta/2.)
    Vint = geompy.MakeVector(p1_rota, p0)
    list_M_INT = geompy.GetShapesOnPlane(bride, geompy.ShapeType["FACE"],
                                Vint, geompy.GEOM.ST_ONOUT)
    
    M_INT = geompy.CreateGroup(bride, geompy.ShapeType["FACE"])
    geompy.addToStudyInFather(bride, M_INT, "M_INT")
    
    for face in list_M_INT:
        f_ind_tmp = geompy.GetSubShapeID(bride, face)
        geompy.AddObject(M_INT, f_ind_tmp)
    
    
    p_13_14 = geompy.MakeVertexOnCurve(edge17, 0.5)
    p_13_14_rota = geompy.MakeRotation(p_13_14, Vz, beta/2.)
    M_TUB = geompy.GetFaceNearPoint(BRIDE, p_13_14_rota)
    geompy.addToStudyInFather(bride, M_TUB, "M_TUB")
    
    p_M_GOU = geompy.MakeVertex(rtrou, rg/2., -j/2.)
    M_GOU = geompy.GetFaceNearPoint(GOUJON, p_M_GOU)
    geompy.addToStudyInFather(bride, M_GOU, "M_GOU")
    
    Vy_rota = geompy.MakeRotation(Vy, Vz, beta)
    list_M_L_SA = geompy.GetShapesOnPlane(bride, geompy.ShapeType["FACE"],
                                Vy_rota, geompy.GEOM.ST_ONOUT)
    
    M_L_SA = geompy.CreateGroup(bride, geompy.ShapeType["FACE"])
    geompy.addToStudyInFather(bride, M_L_SA, "M_L_SA")
    
    for face in list_M_L_SA:
        f_ind_tmp = geompy.GetSubShapeID(bride, face)
        geompy.AddObject(M_L_SA, f_ind_tmp)
    
    
    moins_Vy = geompy.ChangeOrientation(Vy)
    list_M_L_AA = geompy.GetShapesOnPlane(bride, geompy.ShapeType["FACE"],
                                moins_Vy, geompy.GEOM.ST_ONOUT)
    
    M_L_AA = geompy.CreateGroup(bride, geompy.ShapeType["FACE"])
    geompy.addToStudyInFather(bride, M_L_AA, "M_L_AA")
    
    for face in list_M_L_AA:
        f_ind_tmp = geompy.GetSubShapeID(bride, face)
        geompy.AddObject(M_L_AA, f_ind_tmp)
    
                                
    list_M_EXT = []
    
    p_4_5 = geompy.MakeVertexOnCurve(edge5, 0.5)
    p_4_5_rota = geompy.MakeRotation(p_4_5, Vz, beta/2.)
    M_EXT1 = geompy.GetFaceNearPoint(bride, p_4_5_rota)
    list_M_EXT.append(M_EXT1)
    
    p_M_EXT2 = geompy.MakeVertex((rex3 + rtrou-rt)/2., 0., hb)
    p_M_EXT2_rota = geompy.MakeRotation(p_M_EXT2, Vz, beta/2.)
    M_EXT2 = geompy.GetFaceNearPoint(bride, p_M_EXT2_rota)
    list_M_EXT.append(M_EXT2)
    
    p_7_8 = geompy.MakeVertexOnCurve(edge9, 0.5)
    p_7_8_rota = geompy.MakeRotation(p_7_8, Vz, beta/2.)
    M_EXT3 = geompy.GetFaceNearPoint(bride, p_7_8_rota)
    list_M_EXT.append(M_EXT3)
    
    p_M_EXT4 = geompy.MakeVertex((rext + rtrou+rrd)/2., 0., h)
    p_M_EXT4_rota = geompy.MakeRotation(p_M_EXT4, Vz, beta/2.)
    M_EXT4 = geompy.GetFaceNearPoint(bride, p_M_EXT4_rota)
    list_M_EXT.append(M_EXT4)
    
    p_mid_conge = geompy.MakeVertexOnCurve(conge, 0.5)
    p_mid_conge_rota = geompy.MakeRotation(p_mid_conge, Vz, beta/2.)
    M_EXT5 = geompy.GetFaceNearPoint(bride, p_mid_conge_rota)
    list_M_EXT.append(M_EXT5)
    
    p_9_12 = geompy.MakeVertexOnCurve(edge11, 0.5)
    p_9_12_rota = geompy.MakeRotation(p_9_12, Vz, beta/2.)
    M_EXT6 = geompy.GetFaceNearPoint(bride, p_9_12_rota)
    list_M_EXT.append(M_EXT6)
    
    p_12_13 = geompy.MakeVertexOnCurve(edge18, 0.5)
    p_12_13_rota = geompy.MakeRotation(p_12_13, Vz, beta/2.)
    M_EXT7 = geompy.GetFaceNearPoint(bride, p_12_13_rota)
    list_M_EXT.append(M_EXT7)
    
    p_haut_gouj = geompy.MakeTranslation(p_goujon_h, 0., (rg-pf)/2., 0.)
    M_EXT8 = geompy.GetFaceNearPoint(bride, p_haut_gouj)
    list_M_EXT.append(M_EXT8)
    
    p_filet_gouj = geompy.MakeVertexOnCurve(edge2_goujon, 0.5)
    p_filet_gouj_rota = geompy.MakeRotation(p_filet_gouj, axe_goujon, math.pi/2.)
    M_EXT9 = geompy.GetFaceNearPoint(bride, p_filet_gouj_rota)
    list_M_EXT.append(M_EXT9)
    
    p_cote_gouj = geompy.MakeVertex(rtrou, rg, (h+e+he + h_goujon) / 2.)
    M_EXT10 = geompy.GetFaceNearPoint(bride, p_cote_gouj)
    list_M_EXT.append(M_EXT10)
    
    p_haut_ecrou = geompy.MakeVertex(rtrou, (rg+rec)/2., h + e + he)
    M_EXT11 = geompy.GetFaceNearPoint(bride, p_haut_ecrou)
    list_M_EXT.append(M_EXT11)
    
    p_cote_ecrou = geompy.MakeVertex(rtrou, rec, h + e + he/2.)
    M_EXT12 = geompy.GetFaceNearPoint(bride, p_cote_ecrou)
    list_M_EXT.append(M_EXT12)
    
    p_haut_rondelle = geompy.MakeVertex(rtrou, (rec+rrd)/2., h + e)
    M_EXT13 = geompy.GetFaceNearPoint(bride, p_haut_rondelle)
    list_M_EXT.append(M_EXT13)
    
    p_cote_rondelle = geompy.MakeVertex(rtrou, rrd, h + e/2.)
    M_EXT14 = geompy.GetFaceNearPoint(bride, p_cote_rondelle)
    list_M_EXT.append(M_EXT14)
    
    M_EXT = geompy.CreateGroup(bride, geompy.ShapeType["FACE"])
    geompy.addToStudyInFather(bride, M_EXT, "M_EXT")
    
    for face in list_M_EXT:
        f_ind_tmp = geompy.GetSubShapeID(bride, face)
        geompy.AddObject(M_EXT, f_ind_tmp)
    
    time_3 = time.time()
    print "Temps explosion des faces = ", (time_3-time_2)
    
    
    # Détermination des différents points
    
    epsilon = 1e-7
    
    #P4
    PJE_OUV = geompy.GetPoint(JOINT, rex3, 0., 0., epsilon)
    geompy.addToStudyInFather(bride, PJE_OUV, "PJE_OUV")
    
    #P1
    PJI_OUV = geompy.GetPoint(JOINT, rint, 0., 0., epsilon)
    geompy.addToStudyInFather(bride, PJI_OUV, "PJI_OUV")
    
    #P4
    PBE_OUV = geompy.GetPoint(BRIDE, rex3, 0., 0., epsilon)
    geompy.addToStudyInFather(bride, PBE_OUV, "PBE_OUV")
    
    #P1
    PBI_OUV = geompy.GetPoint(BRIDE, rint, 0., 0., epsilon)
    geompy.addToStudyInFather(bride, PBI_OUV, "PBI_OUV")
    
    P_ECR = geompy.GetPoint(bride, rtrou + rt, 0., h + e, epsilon)
    geompy.addToStudyInFather(bride, P_ECR, "P_ECR")
    
    P_GOU = geompy.GetPoint(bride, rtrou, 0., hb, epsilon)
    geompy.addToStudyInFather(bride, P_GOU, "P_GOU")
    
    P_BRI = geompy.GetPoint(bride, rint + (rex3-rint)/3., 0., hb, epsilon)
    geompy.addToStudyInFather(bride, P_BRI, "P_BRI")
    
    time_4 = time.time()
    print "Temps explosion des vertices = ", (time_4-time_3)
    
    
#     #=============== MAILLAGE ======================
#     
#     AverageLength = (rex1-rint)/nrad
#     
#     # Creation du maillage
#     # --------------------
#     
#     maillageBride = smesh.Mesh(bride, "MeshBride")
#     
#     # Algorithmes et hypotheses globales
#     # ----------------------------------
#     
#     # 1D
#     
#     algo = maillageBride.Segment()
#     algo.LocalLength(AverageLength)
#     # On veut un maillage quadratique
#     algo.QuadraticMesh()
#     
#     # 2D
#     
#     algo = maillageBride.Triangle()
#     algo.LengthFromEdges()
#     
#     # 3D
#     
#     maillageBride.Tetrahedron(smesh.NETGEN)
#     
#     
#     # Calcul
#     # ------
#     
#     maillageBride.Compute()    
#     time_5 = time.time()    
#     print "Temps Maillage = ", (time_5-time_4)
#     
#     # Création des groupes
#     # --------------------
#     
#     maillageBride.Group(P_GOU, "P_GOU")
#     maillageBride.Group(PBI_OUV, "PBI_OUV")
#     maillageBride.Group(P_BRI, "P_BRI")
#     maillageBride.Group(PBE_OUV, "PBE_OUV")
#     maillageBride.Group(P_ECR, "P_ECR")
#     maillageBride.Group(PJI_OUV, "PJI_OUV")
#     maillageBride.Group(SCEG, "SCEG")
#     maillageBride.Group(SCGE, "SCGE")
#     maillageBride.Group(M_JOI, "M_JOI")
#     maillageBride.Group(SCJB, "SCJB")
#     maillageBride.Group(SCBJ, "SCBJ")
#     maillageBride.Group(M_EXT, "M_EXT")
#     maillageBride.Group(M_INT, "M_INT")
#     maillageBride.Group(M_TUB, "M_TUB")
#     maillageBride.Group(M_GOU, "M_GOU")
#     maillageBride.Group(M_L_SA, "M_L_SA")
#     maillageBride.Group(M_L_AA, "M_L_AA")
#     maillageBride.Group(GOUJON, "GOUJON")
#     maillageBride.Group(ROND, "ROND")
#     maillageBride.Group(ECROU, "ECROU")
#     maillageBride.Group(BRIDE, "BRIDE")
#     maillageBride.Group(JOINT, "JOINT")
#     maillageBride.Group(VTOT, "VTOT")
#             
#     time_6 = time.time()
#     
#     print "Temps Groupes Maillage = ", (time_6-time_5)      
#     # Mise à jour de l'arbre d'étude
    
    salome.sg.updateObjBrowser(1)
    
    
    
    