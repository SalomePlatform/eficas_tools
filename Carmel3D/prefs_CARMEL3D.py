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

import os

# repIni sert a localiser le fichier editeur.ini  
repIni=os.path.dirname(os.path.abspath(__file__))

# lang indique la langue utilisee pour les chaines d'aide : fr ou ang
lang='fr'

# Codage des strings qui accepte les accents (en remplacement de 'ascii')
encoding='iso-8859-1'

# Choix des catalogues
# format du Tuple (code,version,catalogue,formatOut, finit par defaut Ãventuellement)
catalogues = (

# catalogue de la maquette finale avec generation Phys
 ('CARMEL3D','G2',os.path.join(repIni,'Carmel3D_cata_g2.py'),'CARMEL3D','defaut'),
# catalogue de la maquette finale avec generation Phys
# ('CARMEL3D','G1',os.path.join(repIni,'Carmel3D_cata_g1.py'),'CARMEL3D','defaut'),
# catalogue de la maquette finale avec materiau en premier pour reunion du 24 janvier
 ('CARMEL3D','V0',os.path.join(repIni,'Carmel3D_cata_v0.py'),'python'),
# catalogue entier et etendu : tout est decrit avec les repetitions qui en decoulent 
 ('CARMEL3D','V1',os.path.join(repIni,'Carmel3D_cata_etendu.py'),'python'),
# catalogue avec essai de mise en commun de certains blocs (loi) 
 ('CARMEL3D','V2',os.path.join(repIni,'Carmel3D_cata_fact.py'),'python'),
# catalogue avec materiau en tete 
 ('CARMEL3D','V3',os.path.join(repIni,'Carmel3D_cata_mat.py'),'python'),
 ('CARMEL3D','V4',os.path.join(repIni,'Carmel3D_cata_matloi.py'),'python'),
 ('CARMEL3D','V5',os.path.join(repIni,'Carmel3D_cata_pa.py'),'python'),
 ('CARMEL3D','V6',os.path.join(repIni,'Carmel3D_cata_pn.py'),'python'),
)

