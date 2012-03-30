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
print "import des prefs de OPENTURNS"

# repIni sert a localiser le fichier 
# initialdir sert comme directory initial des QFileDialog
# positionnee a repin au debut mise a jour dans configuration
repIni=os.path.dirname(os.path.abspath(__file__))
INSTALLDIR=os.path.join(repIni,'..')
sys.path[:0]=[INSTALLDIR]


# Codage des strings qui accepte les accents (en remplacement de 'ascii')
# lang indique la langue utilisée pour les chaines d'aide : fr ou ang
lang='fr'
encoding='iso-8859-1'

# Acces a la documentation
path_doc        = os.path.join(INSTALLDIR,'Doc')
exec_acrobat    = "/usr/bin/xpdf"
savedir         = os.environ['HOME']


# OpenTURNS Python module
OpenTURNS_path=""
if len(OpenTURNS_path) > 0: sys.path[:0]=[OpenTURNS_path]

# Choix des catalogues
from Editeur.catadesc import CatalogDescription

catalogues = (
    CatalogDescription(identifier = "OPENTURNS_WRAPPER_V4",
                       cata_file_path = os.path.join(os.path.abspath(repIni), 'OpenTURNS_Cata_Wrapper_V4.py'),
                       file_format = "openturns_wrapper"),
)

