import os

# REPINI sert � localiser le fichier editeur.ini
# Obligatoire
REPINI=os.path.dirname(os.path.abspath(__file__))

# INSTALLDIR sert � localiser l'installation d'Eficas
# Obligatoire
INSTALLDIR=os.path.join(REPINI,'..')

# CODE_PATH sert � localiser Noyau et Validation �ventuellement
# non contenus dans la distribution EFICAS
# Par d�faut on utilise les modules de INSTALLDIR
# Peut valoir None (defaut)
CODE_PATH = None
#CODE_PATH = os.path.join(REPINI,'../../Superv')

# ICONDIR sert � localiser le r�pertoire contenant les icones
# Par d�faut on utilise le r�pertoire icons dans Editeur
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
           #                        ('Fichier � plat','visu_a_plat'),
                                   ('Fichier .py','visuJDC_py'),
                                   ('Fichier source','visu_txt_brut_JDC'),
                                   ('Param�tres Eficas','affichage_fichier_ini'),
                                   ('Mots-cl�s inconnus','mc_inconnus'),
                                  ]
              ),
             ]
           }

