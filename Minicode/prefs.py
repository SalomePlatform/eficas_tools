# -*- coding: utf-8 -*-
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
#CODE_PATH = "/home01/chris/projet_Eficas/Devel/SUPER6_3/Aster6_3/bibpyt"

# ICONDIR sert � localiser le r�pertoire contenant les icones
# Par d�faut on utilise le r�pertoire icons dans Editeur
ICONDIR=os.path.join(INSTALLDIR,'Editeur','icons')

# lang indique la langue utilis�e pour les chaines d'aide : fr ou ang
lang='fr'


