import os

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

# ICONDIR sert à localiser le répertoire contenant les icones
# Par défaut on utilise le répertoire icons dans Editeur
ICONDIR=os.path.join(INSTALLDIR,'Editeur','icons')

labels= ('Fichier','Edition','Jeu de commandes',
              # 'Catalogue','Browsers','Options'
           )

extensions=['readercata','bureau',
                 # 'browser','options'
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
           #                        ('Fichier à plat','visu_a_plat'),
                                   ('Fichier .py','visuJDC_py'),
                                   ('Fichier source','visu_txt_brut_JDC'),
                                   ('Paramètres Eficas','affichage_fichier_ini'),
                                   ('Mots-clés inconnus','mc_inconnus'),
                                  ]
              ),
             ]
           }

