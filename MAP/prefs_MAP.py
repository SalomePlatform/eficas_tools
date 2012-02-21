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

# INSTALLDIR sert a localiser l'installation d'Eficas
PATH_MAP="/local/noyret/MAP/"
#PATH_MAP="/local00/bin/MAP/"
PATH_PYGMEE=PATH_MAP+"/components/pygmee_v2"
PATH_BENHUR=PATH_MAP+"/components/benhur"
PATH_FDVGRID=PATH_MAP+"components/fdvgrid/ther2d/bin"
PATH_STUDY=PATH_MAP+"/studies/demonstrateur_s_polymers_st_1"
PATH_MODULE=PATH_MAP+"/module"
#PATH_ASTER="/local/noyret/bin/Aster10/bin"
PATH_ASTER="/local00/aster"
PATH_GMSH="/usr/bin"


# Codage des strings qui accepte les accents (en remplacement de 'ascii')
# lang indique la langue utilisee pour les chaines d'aide : fr ou ang
lang='fr'
encoding='iso-8859-1'

# Acces a la documentation
path_doc        = os.path.join(repIni,'Doc')
exec_acrobat    = "/usr/bin/xpdf"
savedir         = os.environ['HOME']

MAP_DIRECTORY=os.getenv("MAP_DIRECTORY")

catalogues = (
# (code, identifiant, catalogue, formatOut, formatIN)
  ('MAP','V1',os.path.join(repIni,'s_Perfect_V1.py'),'Perfect'),
  ('MAP','V0',os.path.join(repIni,'s_DIC_V1.py'),'s_DIC'),
  ('MAP','V1',os.path.join(repIni,'s_DIC_V1.py'),'s_DIC','defaut'),
  ('MAP','V1',os.path.join(repIni,'s_scc_3d_analysis_V1.py'),'s_scc_3d','defaut'),
  ('MAP','V1',os.path.join(repIni,'Essai/maquette.py'),'maquette','defaut'),
  ('MAP','V1',os.path.join(repIni,'Essai/comp_c_image_3d.py'),'c_image_3d','defaut'),
  ('MAP','V1',os.path.join(repIni,'Essai/c_pre_interface_mesh.py.py'),'c_pre_interface_mesh','defaut'),
  ('MAP','V1',os.path.join(repIni,'Essai/c_post_distribution_properties.py'),'c_post_distribution_properties','defaut'),
)

OpenTURNS_path='/local/noyret/Salome/V6_main/tools/install/Openturns_tool-0150-py266-r272-ro144-rp208-sw204-xm278-la331-gr2263-dox173_patch-tbb30/lib/python2.6/site-packages'
sys.path[:0]=[repIni,INSTALLDIR, OpenTURNS_path]

