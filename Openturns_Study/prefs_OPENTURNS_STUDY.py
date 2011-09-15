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

# repIni sert à localiser le fichier 
# initialdir sert comme directory initial des QFileDialog
# positionnee a repin au debut mise a jour dans configuration
repIni=os.path.dirname(os.path.abspath(__file__))
initialdir=repIni 

# INSTALLDIR sert à localiser l'installation d'Eficas
INSTALLDIR=os.path.join(repIni,'..')


# Codage des strings qui accepte les accents (en remplacement de 'ascii')
# lang indique la langue utilisée pour les chaines d'aide : fr ou ang
lang='fr'
encoding='iso-8859-1'

# Acces a la documentation
rep_cata        = INSTALLDIR
path_doc        = os.path.join(rep_cata,'Doc')
exec_acrobat    = "/usr/bin/xpdf"
savedir         = os.environ['HOME']


# OpenTURNS Python module
#OpenTURNS_path="/opt/Openturns/Install_0_13_2/lib/python2.5/site-packages"
OpenTURNS_path=""
# Choix des catalogues
if len(OpenTURNS_path) > 0:
    sys.path[:0]=[OpenTURNS_path]
sys.path[:0]=[INSTALLDIR]
