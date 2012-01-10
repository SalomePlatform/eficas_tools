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

# repIni sert � localiser le fichier editeur.ini
# Obligatoire
repIni=os.path.dirname(os.path.abspath(__file__))

# INSTALLDIR sert � localiser l'installation d'Eficas
# Obligatoire
INSTALLDIR=os.path.join(repIni,'..')

# CODE_PATH sert � localiser Noyau et Validation �ventuellement
# non contenus dans la distribution EFICAS
# Par d�faut on utilise les modules de INSTALLDIR
# Peut valoir None (defaut)
CODE_PATH = None
#CODE_PATH = os.path.join(repIni,'../../Superv')

# ICONDIR sert � localiser le r�pertoire contenant les icones
# Par d�faut on utilise le r�pertoire icons dans Editeur
ICONDIR=os.path.join(INSTALLDIR,'Editeur','icons')

# lang indique la langue utilis�e pour les chaines d'aide : fr ou ang
lang='fr'

labels= ('Fichier','Edition','Jeu de commandes',
#               'Catalogue','Browsers',
                'Options',
                'Aide',
           )

appli_composants=['readercata','bureau',
#                  'browser',
                   'options',
           ]

menu_defs={ 'bureau': [
              ('Fichier',[
                           ('Nouveau','newJDC'),
                           ('Ouvrir','openJDC'),
                           ('Enregistrer','saveJDC'),
                           ('Enregistrer sous','saveasJDC'),
                           None,
                           ('Fermer','closeJDC'),
                           ('Quitter','exitEFICAS'),
                         ]
              ),
              ('Edition',[
                           ('Copier','copy'),
                           ('Couper','cut'),
                           ('Coller','paste'),
                         ]
              ),
              ('Jeu de commandes',[
                                   ('Rapport de validation','visuCRJDC'),
           #                        ('Fichier � plat','visu_a_plat'),
                                   ('Fichier format v6','visuJDC_py'),
                                   ('Fichier source','visu_txt_brut_JDC'),
                                   ('Param�tres Eficas','affichage_fichier_ini'),
                                   ('Mots-cl�s inconnus','mc_inconnus'),
                                  ]
              ),
              ('Aide',[
                        ('Aide EFICAS','aideEFICAS'),
                      ]
              ),
             ]
           }

