# -*- coding: utf-8 -*-
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
#CODE_PATH = "/home01/chris/projet_Eficas/Devel/SUPER6_3/Aster6_3/bibpyt"

# la variable code donne le nom du code a selectionner
code="MINICODE"

# lang indique la langue utilisée pour les chaines d'aide : fr ou ang
lang='fr'

# Codage des strings qui accepte les accents (en remplacement de 'ascii')
encoding='iso-8859-1'

sys.path[:0]=[INSTALLDIR]

# ICONDIR sert à localiser le répertoire contenant les icones
# Par défaut on utilise le répertoire icons dans Editeur
ICONDIR=os.path.join(INSTALLDIR,'Editeur','icons')
