# -*- coding: utf-8 -*-
import os

# REPINI sert � localiser le fichier editeur.ini
REPINI=os.path.dirname(os.path.abspath(__file__))

# ICONDIR sert � localiser le r�pertoire contenant les icones
ICONDIR=os.path.join(REPINI,'../..','Editeur','icons')

# CODE_PATH sert � localiser Accas et Cata (si pas infos dans editeur.ini)
#CODE_PATH = os.path.join(REPINI,'..')

# INSTALLDIR sert � localiser faqs.txt et les modules Eficas
#INSTALLDIR=os.path.join(REPINI,'..','Editeur')

# lang indique la langue utilis�e pour les chaines d'aide : fr ou ang
lang='fr'

