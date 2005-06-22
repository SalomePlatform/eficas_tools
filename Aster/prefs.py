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

import os,sys

# REPINI sert à localiser le fichier editeur.ini
# Obligatoire
REPINI=os.path.dirname(os.path.abspath(__file__))

# INSTALLDIR sert à localiser l'installation d'Eficas
# Obligatoire
INSTALLDIR=os.path.join(REPINI,'..')

# CODE_PATH sert à localiser Noyau et Validation éventuellement
# non contenus dans la distribution EFICAS
# Par défaut on utilise les modules de INSTALLDIR
# Peut valoir None (defaut)
CODE_PATH = None
#CODE_PATH = os.path.join(REPINI,'../../Superv')

# la variable code donne le nom du code a selectionner
code="ASTER" 

# ICONDIR sert à localiser le répertoire contenant les icones
# Par défaut on utilise le répertoire icons dans Editeur
ICONDIR=os.path.join(INSTALLDIR,'Editeur','icons')

# lang indique la langue utilisée pour les chaines d'aide : fr ou ang
lang='fr'

# Codage des strings qui accepte les accents (en remplacement de 'ascii')
encoding='iso-8859-1'

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
                           ('Nouveau','newJDC','<Control-n>','Ctrl+N'),
                           ('Nouvel INCLUDE','newJDC_include'),
                           ('Ouvrir','openJDC','<Control-o>','Ctrl+O'),
                           ('Enregistrer','saveJDC','<Control-e>','Ctrl+E'),
                           ('Enregistrer sous','saveasJDC','<Control-s>','Ctrl+S'),
                           None,
                           ('Fermer','closeJDC','<Control-f>','Ctrl+F'),
                           ('Quitter','exitEFICAS','<Control-q>','Ctrl+Q'),
                         ]
              ),
              ('Edition',[
                           ('Copier','copy','<Control-c>','Ctrl+C'),
                           ('Couper','cut','<Control-x>','Ctrl+X'),
                           ('Coller','paste','<Control-v>','Ctrl+V'),
                         ]
              ),
              ('Jeu de commandes',[
               ('Rapport de validation','visuCRJDC','<Control-r>','Ctrl+R'),
               ('Fichier à plat','visu_a_plat','<Control-p>','Ctrl+P'),
               ('Fichier format v6','visuJDC_py','<Control-t>','Ctrl+T'),
               ('Fichier source','visu_txt_brut_JDC','<Control-b>','Ctrl+B'),
               ('Paramètres Eficas','affichage_fichier_ini'),
               ('Mots-clés inconnus','mc_inconnus'),
                                  ]
              ),
              ('Aide',[
                        ('Aide EFICAS','aideEFICAS','<Control-a>','Ctrl+A'),
                      ]
              ),
             ]
           }

userprefs=os.path.expanduser("~/Eficas_install/prefs.py")
if os.path.isfile(userprefs):
   try:
      execfile(userprefs)
   except:
      pass

sys.path[:0]=[INSTALLDIR]
