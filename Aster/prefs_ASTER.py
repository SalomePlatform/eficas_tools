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
# Obligatoire
repIni=os.path.dirname(os.path.abspath(__file__))
rep_cata = os.path.join(repIni,'Cata')
mode_nouv_commande='alpha'


# lang indique la langue utilisee pour les chaines d'aide : fr ou ang
lang='fr'

# Codage des strings qui accepte les accents (en remplacement de 'ascii')
encoding='iso-8859-1'

# Utilisateur/Developpeur
isdeveloppeur   =       "NON"

# Choix des catalogues
rep_mat_STA88=os.path.join(rep_cata,'cataSTA8','materiau')
rep_mat_STA98=os.path.join(rep_cata,'cataSTA9','materiau')
rep_mat_STA103=os.path.join(rep_cata,'cataSTA10','materiau')
#
catalogues=(
('ASTER','STA8.8',os.path.join(rep_cata,'cataSTA8'),'python'),
('ASTER','STA9.8',os.path.join(rep_cata,'cataSTA9'),'python'),
('ASTER','STA10.3',os.path.join(rep_cata,'cataSTA10'),'python'),
('ASTER','STA11',os.path.join(rep_cata,'cataSTA11'),'python','defaut'),
)

def addCatalog(catalogName, catalogPath):
    """
    This function helps you to add a new catalog dynamically
    """
    global catalogues
    item=('ASTER',catalogName,catalogPath,'python')
    catalogues+=(item,)
    
