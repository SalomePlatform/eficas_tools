"""
Contient la description des fichiers d'aide et leur structuration

chaque panneau est un tuple de 3 �l�ments :

- �l�ment 1 : titre de la page
- �l�ment 2 : URL du fichier � afficher quand on visualise cette page d'aide ou None si aucun
- �l�ment 3 : tuple contenant les sous-panneaux de ce panneau (tuple de 3-tuples) ou None si aucun

La variable repertoire est initialisee avec le chemin du repertoire local
"""

import os

items =("Aide en ligne EFICAS",None,
            ( 
               ("FAQs",os.path.join(repertoire,"..","Editeur","faqs.txt"),None),
               ("Install",os.path.join(repertoire,"..","INSTALL"), 
                                                      ( 
                                                         ("Procedure d'installation",os.path.join(repertoire,"..","README_install"),None), 
                                                      )
              ),
            ),
       )
