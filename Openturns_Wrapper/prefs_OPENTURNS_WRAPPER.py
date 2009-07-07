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
# "CODE_PATH_SURCHARGE","OpenTURNS_path","rep_user","INSTALLDIR","path_doc","exec_acrobat","rep_cata"
print "import des prefs de OPENTURNS_WRAPPER"

# REPINI sert � localiser le fichier 
# initialdir sert comme directory initial des QFileDialog
# positionnee a repin au debut mise a jour dans configuration
REPINI=os.path.dirname(os.path.abspath(__file__))
initialdir=REPINI 

# INSTALLDIR sert � localiser l'installation d'Eficas
INSTALLDIR=os.path.join(REPINI,'..')


# Codage des strings qui accepte les accents (en remplacement de 'ascii')
# lang indique la langue utilis�e pour les chaines d'aide : fr ou ang
lang='fr'
encoding='iso-8859-1'

# Acces a la documentation
rep_cata        = INSTALLDIR
path_doc        = os.path.join(rep_cata,'Doc')
exec_acrobat    = "/usr/bin/xpdf"

# OpenTURNS Python module
OpenTURNS_path="/opt/OpenTURNS/install/lib/python2.4/site-packages"

# Choix des catalogues
sys.path[:0]=[INSTALLDIR]
sys.path.append( OpenTURNS_path )

