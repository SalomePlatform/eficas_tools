# -*- coding: utf-8 -*-
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

# ICONDIR sert � localiser le r�pertoire contenant les icones
# Par d�faut on utilise le r�pertoire icons dans Editeur
ICONDIR=os.path.join(INSTALLDIR,'Editeur','icons')

# lang indique la langue utilis�e pour les chaines d'aide : fr ou ang
lang='fr'


