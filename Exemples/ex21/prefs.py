# -*- coding: utf-8 -*-
import os

# REPINI sert à localiser le fichier editeur.ini
REPINI=os.path.dirname(os.path.abspath(__file__))

# ICONDIR sert à localiser le répertoire contenant les icones
ICONDIR=os.path.join(REPINI,'../..','Editeur','icons')

# CODE_PATH sert à localiser Accas et Cata (si pas infos dans editeur.ini)
#CODE_PATH = os.path.join(REPINI,'..')

# INSTALLDIR sert à localiser faqs.txt et les modules Eficas
#INSTALLDIR=os.path.join(REPINI,'..','Editeur')

# lang indique la langue utilisée pour les chaines d'aide : fr ou ang
lang='fr'

