# -*- coding: utf-8 -*-
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
#CODE_PATH = "/home01/chris/projet_Eficas/Devel/SUPER6_3/Aster6_3/bibpyt"

# ICONDIR sert à localiser le répertoire contenant les icones
# Par défaut on utilise le répertoire icons dans Editeur
ICONDIR=os.path.join(INSTALLDIR,'Editeur','icons')

# lang indique la langue utilisée pour les chaines d'aide : fr ou ang
lang='fr'


