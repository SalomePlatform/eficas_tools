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

import os, sys
# Les variables pouvant positionnees sont :
print "import des prefs de MAP"

# repIni sert a localiser le fichier 
# initialdir sert comme directory initial des QFileDialog
# positionnee a repin au debut mise a jour dans configuration
repIni=os.path.dirname(os.path.abspath(__file__))
INSTALLDIR=os.path.join(repIni,'..')


# Codage des strings qui accepte les accents (en remplacement de 'ascii')
# lang indique la langue utilisee pour les chaines d'aide : fr ou ang
lang='fr'
encoding='iso-8859-1'

# Acces a la documentation
path_doc        = os.path.join(repIni,'Doc')
exec_acrobat    = "/usr/bin/xpdf"
savedir         = os.environ['HOME']

rep_cata=os.path.dirname(os.path.abspath(__file__))
 
catalogues=(
 ('MAP','Solver',os.path.join(rep_cata,'cata_solver1.py'),'solver1'),
 ('MAP','Test',os.path.join(rep_cata,'cata_s_test03.py'),'s_test03'),
 ('MAP','Exemple python',os.path.join(rep_cata,'cata_c_transverse_empty_python.py'),'c_transverse_empty_python'),
 ('MAP','Image 3D',os.path.join(rep_cata,'cata_c_image_3d_altitude_thickness.py'),'c_image_3d_altitude_thickness'),
 ('MAP','Table FFT',os.path.join(rep_cata,'cata_c_post_table_fft.py'), 'c_post_table_fft'),
 ('MAP','PRE Mesh',os.path.join(rep_cata,'cata_c_pre_interface_mesh.py'), 'c_pre_interface_mesh'),
 ('MAP','Analyse 3D',os.path.join(rep_cata,'cata_s_scc_3d_analysis.py'), 's_scc_3d_analysis'),
)


