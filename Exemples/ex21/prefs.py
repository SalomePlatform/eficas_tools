# -*- coding: utf-8 -*-
import os

# repIni sert à localiser le fichier editeur.ini
repIni=os.path.dirname(os.path.abspath(__file__))

# ICONDIR sert à localiser le répertoire contenant les icones
ICONDIR=os.path.join(repIni,'../..','Editeur','icons')

# CODE_PATH sert à localiser Accas et Cata (si pas infos dans editeur.ini)
#CODE_PATH = os.path.join(repIni,'..')

# INSTALLDIR sert à localiser faqs.txt et les modules Eficas
#INSTALLDIR=os.path.join(repIni,'..','Editeur')

# lang indique la langue utilisée pour les chaines d'aide : fr ou ang
lang='fr'

